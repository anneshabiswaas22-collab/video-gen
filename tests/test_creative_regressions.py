"""Creative persistence/worker regressions and simulated engine HTTP boundaries.

No model, external engine, GPU, or paid service is contacted by this module.
"""
import asyncio
import hashlib
import json
import sqlite3
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

import httpx
import pytest

from integrations.comfyui.adapter import AdapterError, AdapterErrorCode, ComfyUIAdapter
from services.api import storage
from services.api.contracts import GenerationRequest
from services.worker import mock


@pytest.fixture
def creative_store(tmp_path, monkeypatch):
    monkeypatch.setenv("VIDEOGEN_DATA_DIR", str(tmp_path))
    storage.initialize()
    return storage.create_project("Concurrent film")


def request(project, key="creative-00000001", **values):
    return GenerationRequest(project_id=project["id"], model_id="mock-preview-v1",
                             prompt="An original synthetic test scene", idempotency_key=key,
                             **values)


def queued(project, key="creative-00000001"):
    return storage.create_job(request(project, key))[0]


def artifact_paths():
    return sorted((storage.data_dir() / "artifacts").glob("*"))


def test_parallel_same_key_creates_one_job_and_one_initial_event(creative_store):
    payload = request(creative_store)
    with ThreadPoolExecutor(max_workers=12) as pool:
        outcomes = list(pool.map(lambda _: storage.create_job(payload), range(32)))
    ids = {row["id"] for row, _created in outcomes}
    assert len(ids) == 1
    assert sum(created for _row, created in outcomes) == 1
    assert len(storage.jobs(creative_store["id"])) == 1
    assert storage.history(ids.pop())[0]["state"] == "QUEUED"
    assert len(storage.history(outcomes[0][0]["id"])) == 1


def test_parallel_conflicting_key_never_overwrites_input(creative_store):
    barrier = Barrier(2)

    def submit(prompt):
        payload = request(creative_store).model_copy(update={"prompt": prompt})
        barrier.wait()
        try:
            row, created = storage.create_job(payload)
            return "created", row["prompt"], created
        except ValueError as error:
            return "error", str(error), False

    with ThreadPoolExecutor(max_workers=2) as pool:
        outcomes = list(pool.map(submit, ["First immutable prompt", "Second immutable prompt"]))
    assert sorted(item[0] for item in outcomes) == ["created", "error"]
    assert next(item[1] for item in outcomes if item[0] == "error") == "IDEMPOTENCY_CONFLICT"
    assert len(storage.jobs(creative_store["id"])) == 1
    assert storage.jobs(creative_store["id"])[0]["prompt"] in {
        "First immutable prompt", "Second immutable prompt"
    }


def test_parallel_claims_are_unique_and_return_running_state(creative_store, monkeypatch):
    monkeypatch.setattr(storage, "_utc", lambda: "2026-11-17T00:00:00+00:00")
    ids = [queued(creative_store, f"parallel-key-{n:04d}")["id"] for n in range(20)]
    with ThreadPoolExecutor(max_workers=10) as pool:
        tasks = list(pool.map(lambda _: storage.claim_job(), range(20)))
    assert {task["id"] for task in tasks} == set(ids)
    assert all(task["state"] == "RUNNING" and task["progress"] == 15 for task in tasks)
    assert storage.claim_job() is None
    assert all(len(storage.history(job_id)) == 2 for job_id in ids)


def test_created_jobs_require_an_existing_project(creative_store):
    missing = {"id": "proj_" + "f" * 32}
    with pytest.raises(sqlite3.IntegrityError):
        queued(missing)
    assert storage.jobs(missing["id"]) == []


def test_queued_order_remains_stable_when_timestamps_tie(creative_store, monkeypatch):
    monkeypatch.setattr(storage, "_utc", lambda: "2026-11-17T00:00:00+00:00")
    expected = [queued(creative_store, f"ordered-key-{n:04d}")["id"] for n in range(7)]
    assert [storage.claim_job()["id"] for _ in expected] == expected


def test_progress_never_decreases_or_adds_events_for_duplicate_progress(creative_store):
    queued(creative_store)
    task = storage.claim_job()
    storage.progress_job(task["id"], 70)
    storage.progress_job(task["id"], 20)
    storage.progress_job(task["id"], 70)
    assert storage.job(task["id"])["progress"] == 70
    assert [row["progress"] for row in storage.history(task["id"])] == [0, 15, 70]


@pytest.mark.parametrize("value", [-1, 100, 101, 10.5, True, "70"])
def test_invalid_running_progress_cannot_corrupt_job(creative_store, value):
    queued(creative_store)
    task = storage.claim_job()
    with pytest.raises(ValueError):
        storage.progress_job(task["id"], value)
    assert storage.job(task["id"])["progress"] == 15


def test_recovery_only_fails_inflight_once_and_preserves_queue(creative_store):
    first = queued(creative_store, "recover-key-0001")
    second = queued(creative_store, "recover-key-0002")
    assert storage.claim_job()["id"] == first["id"]
    storage.recover_interrupted()
    storage.recover_interrupted()
    storage.initialize()
    assert storage.job(first["id"])["state"] == "FAILED"
    assert storage.job(first["id"])["error_code"] == "WORKER_LOST"
    assert [event["state"] for event in storage.history(first["id"])] == [
        "QUEUED", "RUNNING", "FAILED"
    ]
    assert storage.job(second["id"])["state"] == "QUEUED"
    assert storage.claim_job()["id"] == second["id"]


@pytest.mark.parametrize("state", ["QUEUED", "FAILED", "SUCCEEDED"])
def test_completion_rejects_nonrunning_task_without_new_files(creative_store, state):
    original = queued(creative_store)
    task = original if state == "QUEUED" else storage.claim_job()
    if state == "FAILED":
        storage.fail_job(task["id"], "WORKER_LOST")
    elif state == "SUCCEEDED":
        storage.complete_job(task, b"MOCK ARTIFACT first and immutable")
    before = [(p.name, p.read_bytes()) for p in artifact_paths()]
    before_events = storage.history(task["id"])
    with pytest.raises(ValueError, match="JOB_NOT_RUNNING"):
        storage.complete_job(task, b"a stale worker completion")
    assert storage.job(task["id"])["state"] == state
    assert [(p.name, p.read_bytes()) for p in artifact_paths()] == before
    assert storage.history(task["id"]) == before_events


def test_artifact_database_failure_cleans_files_and_rolls_back(creative_store):
    queued(creative_store)
    task = storage.claim_job()
    with storage.connection() as db:
        db.executescript("""
            CREATE TRIGGER fail_artifact BEFORE INSERT ON artifacts BEGIN
              SELECT RAISE(ABORT, 'deliberate test rejection');
            END;
        """)
    with pytest.raises(sqlite3.IntegrityError):
        storage.complete_job(task, b"MOCK ARTIFACT cannot be committed")
    assert artifact_paths() == []
    assert storage.job(task["id"])["state"] == "RUNNING"
    with storage.connection() as db:
        assert db.execute("SELECT count(*) FROM artifacts").fetchone()[0] == 0
    assert len(storage.history(task["id"])) == 2


def test_artifact_rename_failure_cleans_temporary_file(creative_store, monkeypatch):
    queued(creative_store)
    task = storage.claim_job()

    def broken_replace(_source, _target):
        raise OSError("deliberate filesystem failure")

    monkeypatch.setattr(storage.os, "replace", broken_replace)
    with pytest.raises(OSError):
        storage.complete_job(task, b"MOCK ARTIFACT interrupted write")
    assert artifact_paths() == []
    assert storage.job(task["id"])["state"] == "RUNNING"


def test_successful_artifact_is_immutable_and_terminal(creative_store):
    queued(creative_store)
    task = storage.claim_job()
    body = b"MOCK ARTIFACT immutable test receipt"
    artifact = storage.complete_job(task, body)
    storage.progress_job(task["id"], 5)
    storage.fail_job(task["id"], "LATE_FAILURE")
    assert storage.job(task["id"])["state"] == "SUCCEEDED"
    assert storage.artifact(artifact["id"])["sha256"] == hashlib.sha256(body).hexdigest()
    assert artifact_paths()[0].read_bytes() == body
    assert [row["state"] for row in storage.history(task["id"])][-1] == "SUCCEEDED"


def test_late_running_worker_cannot_undo_restart_recovery(creative_store):
    job = queued(creative_store)

    async def run():
        task = asyncio.create_task(mock.execute_one(delay=.01))
        await asyncio.sleep(0)
        storage.recover_interrupted()
        await task

    asyncio.run(run())
    current = storage.job(job["id"])
    assert current["state"] == "FAILED" and current["error_code"] == "WORKER_LOST"
    assert current["artifact_id"] is None
    assert artifact_paths() == []


def test_worker_cancellation_records_failure_and_does_not_create_receipt(creative_store):
    job = queued(creative_store)

    async def run():
        task = asyncio.create_task(mock.execute_one(delay=30))
        await asyncio.sleep(0)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task

    asyncio.run(run())
    assert storage.job(job["id"])["error_code"] == "WORKER_LOST"
    assert artifact_paths() == []


def test_worker_continues_after_one_receipt_failure(creative_store, monkeypatch):
    first = queued(creative_store, "failing-receipt-01")
    second = queued(creative_store, "good-receipt-0002")
    complete = storage.complete_job
    calls = 0

    def one_failure(task, body):
        nonlocal calls
        calls += 1
        if calls == 1:
            raise OSError("deliberate test write failure")
        return complete(task, body)

    monkeypatch.setattr(storage, "complete_job", one_failure)
    asyncio.run(mock.execute_one(delay=0))
    asyncio.run(mock.execute_one(delay=0))
    assert storage.job(first["id"])["state"] == "FAILED"
    assert storage.job(second["id"])["state"] == "SUCCEEDED"
    assert len(artifact_paths()) == 1


def test_worker_loop_retries_transient_claim_storage_failure(creative_store, monkeypatch):
    async def run():
        recovered = asyncio.Event()
        attempts = 0

        def claim():
            nonlocal attempts
            attempts += 1
            if attempts == 1:
                raise sqlite3.OperationalError("deliberate transient database error")
            recovered.set()
            return None

        monkeypatch.setattr(storage, "claim_job", claim)
        task = asyncio.create_task(mock.worker_loop())
        try:
            await asyncio.wait_for(recovered.wait(), timeout=1)
        finally:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        assert attempts >= 2

    asyncio.run(run())


def finished_http_job(client):
    project = client.post("/v1/projects", json={"name": "Artifact integrity"}).json()
    submitted = client.post("/v1/jobs", json=request(project).model_dump()).json()
    for _ in range(100):
        job = client.get("/v1/jobs/" + submitted["id"]).json()
        if job["state"] == "SUCCEEDED":
            return client.get("/v1/artifacts/" + job["artifact_id"]).json()
        time.sleep(.01)
    raise AssertionError("Synthetic worker did not finish")


@pytest.mark.parametrize("damage", ["missing", "changed", "symlink"])
def test_download_refuses_missing_or_modified_receipt(client, tmp_path, damage):
    artifact = finished_http_job(client)
    target = storage.data_dir() / "artifacts" / (artifact["id"] + ".txt")
    if damage == "missing":
        target.unlink()
    elif damage == "changed":
        target.write_bytes(b"different bytes from stored provenance")
    else:
        private = tmp_path / "outside-artifact.txt"
        private.write_bytes(b"private local file must not be served")
        target.unlink()
        target.symlink_to(private)
    response = client.get(artifact["download_url"])
    assert response.status_code == 503
    assert b"private local file" not in response.content


def approved_adapter(client, graph=None):
    return ComfyUIAdapter(client, {"approved": graph or {"1": {"class_type": "TestNode", "inputs": {}}}})


@pytest.mark.parametrize("payload", [{}, [], {"prompt_id": None}, {"prompt_id": ""},
                                      {"prompt_id": "   "}, {"prompt_id": "id\nsecret"},
                                      {"prompt_id": "x" * 257},
                                      {"prompt_id": "id", "error": {"message": "rejected"}}])
def test_adapter_rejects_invalid_submission_results(payload):
    async def run():
        async with httpx.AsyncClient(base_url="http://engine.test", transport=httpx.MockTransport(
            lambda _request: httpx.Response(200, json=payload)
        )) as client:
            with pytest.raises(AdapterError) as error:
                await approved_adapter(client).generate("approved", "client")
            assert error.value.code == AdapterErrorCode.REMOTE_REJECTED
    asyncio.run(run())


@pytest.mark.parametrize("body", [b"<html>not an engine</html>", b"{}", b"[]",
                                   b'{"queue_running":{},"queue_pending":[]}'])
def test_adapter_health_requires_queue_contract(body):
    async def run():
        async with httpx.AsyncClient(base_url="http://engine.test", transport=httpx.MockTransport(
            lambda _request: httpx.Response(200, content=body)
        )) as client:
            assert await approved_adapter(client).health() is False
    asyncio.run(run())


def test_adapter_refuses_redirect_even_if_client_follows_redirects():
    seen = []

    def handler(req):
        seen.append(str(req.url))
        if req.url.host == "engine.test":
            return httpx.Response(307, headers={"Location": "http://elsewhere.test/exfiltrate"})
        return httpx.Response(200, json={"prompt_id": "should-not-arrive"})

    async def run():
        async with httpx.AsyncClient(base_url="http://engine.test", follow_redirects=True,
                                    transport=httpx.MockTransport(handler)) as client:
            adapter = approved_adapter(client)
            assert await adapter.health() is False
            with pytest.raises(AdapterError):
                await adapter.generate("approved", "client")
    asyncio.run(run())
    assert seen == ["http://engine.test/queue", "http://engine.test/prompt"]


def test_adapter_approval_is_detached_from_later_caller_mutation():
    graph = {"1": {"class_type": "ReviewedNode", "inputs": {"value": 1}}}

    def handler(req):
        assert json.loads(req.content)["prompt"]["1"]["class_type"] == "ReviewedNode"
        return httpx.Response(200, json={"prompt_id": "approved-result"})

    async def run():
        async with httpx.AsyncClient(base_url="http://engine.test", transport=httpx.MockTransport(handler)) as client:
            adapter = approved_adapter(client, graph)
            graph["1"]["class_type"] = "ChangedAfterReview"
            assert await adapter.generate("approved", "client") == "approved-result"
    asyncio.run(run())


def test_adapter_rejects_non_json_approved_graph():
    async def run():
        async with httpx.AsyncClient(base_url="http://engine.test", transport=httpx.MockTransport(
            lambda _: pytest.fail("Invalid graph must not reach HTTP")
        )) as client:
            with pytest.raises(AdapterError) as error:
                approved_adapter(client, {"1": {"class_type": "A", "inputs": {"x": object()}}})
            assert error.value.code == AdapterErrorCode.INVALID_WORKFLOW
    asyncio.run(run())


@pytest.mark.parametrize("endpoint", ["health", "generate"])
def test_adapter_bounds_decoded_engine_output(endpoint):
    async def run():
        async with httpx.AsyncClient(base_url="http://engine.test", transport=httpx.MockTransport(
            lambda _: httpx.Response(200, content=b" " * (256 * 1024 + 1))
        )) as client:
            adapter = approved_adapter(client)
            if endpoint == "health":
                assert await adapter.health() is False
            else:
                with pytest.raises(AdapterError) as error:
                    await adapter.generate("approved", "client")
                assert error.value.code == AdapterErrorCode.REMOTE_REJECTED
    asyncio.run(run())
