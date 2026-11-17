"""Fault and race regressions for the single-process practice session boundary.

All model behavior is controlled in-process; these tests never contact a model.
"""
import asyncio
import sqlite3
from contextlib import asynccontextmanager

import httpx
import pytest
from english_friend import routes, storage
from fastapi import FastAPI
from fastapi.testclient import TestClient


@asynccontextmanager
async def lifespan(_app):
    routes.initialize()
    yield


def application():
    result = FastAPI(lifespan=lifespan)
    result.include_router(routes.router)
    return result


@pytest.fixture
def isolated_store(tmp_path, monkeypatch):
    monkeypatch.setenv("VIDEOGEN_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("VIDEOGEN_COACH_PROVIDER", "offline_practice")
    routes.initialize()
    return tmp_path


def feedback():
    return {"kind": "accepted", "suggestions": [], "explanation": "",
            "reply": "This test phrase is clear.", "next_question": "",
            "engine": "offline_practice", "supported": True}


def disk_bytes(root):
    return b"".join(path.read_bytes() for path in root.glob("english.sqlite3*"))


async def create(client, *, save_history=False):
    result = await client.post("/v1/english/sessions", json={
        "scenario_id": "everyday", "save_history": save_history,
    })
    assert result.status_code == 201, result.text
    return result.json()["id"]


async def send(client, session_id, key="fault-request-0001", text="Synthetic learner phrase"):
    return await client.post(f"/v1/english/sessions/{session_id}/turns", json={
        "text": text, "idempotency_key": key,
    })


def test_cancelled_provider_releases_quota_without_repeating_indeterminate_call(
    isolated_store, monkeypatch,
):
    monkeypatch.setattr(storage, "MAX_TURNS", 1)
    calls = []

    async def exercise():
        started = asyncio.Event()
        release = asyncio.Event()

        async def provider(text, _scenario):
            calls.append(text)
            started.set()
            await release.wait()
            return feedback()

        monkeypatch.setattr(routes.providers, "respond", provider)
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=application()), base_url="http://testserver",
        ) as client:
            session_id = await create(client)
            task = asyncio.create_task(send(client, session_id, text="cancel-private-852754"))
            await asyncio.wait_for(started.wait(), 2)
            task.cancel()
            with pytest.raises(asyncio.CancelledError):
                await task
            with storage.connection() as db:
                assert db.execute("SELECT state FROM english_turns").fetchone()[0] == "interrupted"
            replay = await send(client, session_id, text="cancel-private-852754")
            assert replay.status_code == 409
            assert replay.json()["detail"]["code"] == "RETRY_NOT_AVAILABLE"
            assert calls == ["cancel-private-852754"]
            release.set()
            completed = await send(client, session_id, key="fault-request-0002")
            assert completed.status_code == 200
            result = await client.get(f"/v1/english/sessions/{session_id}")
            assert result.json()["turn_count"] == 1
            assert b"cancel-private-852754" not in disk_bytes(isolated_store)

    asyncio.run(exercise())


def test_expiry_during_provider_removes_saved_text_before_returning(
    isolated_store, monkeypatch,
):
    private = "expired-while-model-runs-private-729362"

    async def exercise():
        calls = 0
        started = asyncio.Event()
        release = asyncio.Event()

        async def provider(_text, _scenario):
            nonlocal calls
            calls += 1
            if calls == 2:
                started.set()
                await release.wait()
            return feedback()

        monkeypatch.setattr(routes.providers, "respond", provider)
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=application()), base_url="http://testserver",
        ) as client:
            session_id = await create(client, save_history=True)
            assert (await send(client, session_id, text=private)).status_code == 200
            assert private.encode() in disk_bytes(isolated_store)
            pending = asyncio.create_task(send(client, session_id, key="slow-request-0002"))
            await asyncio.wait_for(started.wait(), 2)
            with storage.connection() as db:
                db.execute("UPDATE english_sessions SET expires_at='2000-01-01' WHERE id=?",
                           (session_id,))
            release.set()
            result = await pending
            assert result.status_code == 404
            with storage.connection() as db:
                assert db.execute("SELECT count(*) FROM english_sessions").fetchone()[0] == 0
                assert db.execute("SELECT count(*) FROM english_turns").fetchone()[0] == 0
            assert private.encode() not in disk_bytes(isolated_store)

    asyncio.run(exercise())


def test_delete_waits_for_inflight_turn_then_removes_its_result(isolated_store, monkeypatch):
    private = "delete-while-model-runs-private-632574"

    async def exercise():
        started = asyncio.Event()
        release = asyncio.Event()

        async def provider(_text, _scenario):
            started.set()
            await release.wait()
            return feedback()

        monkeypatch.setattr(routes.providers, "respond", provider)
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=application()), base_url="http://testserver",
        ) as client:
            session_id = await create(client, save_history=True)
            pending = asyncio.create_task(send(client, session_id, text=private))
            await asyncio.wait_for(started.wait(), 2)
            deletion = asyncio.create_task(client.delete(f"/v1/english/sessions/{session_id}"))
            await asyncio.sleep(0)
            assert not deletion.done()
            release.set()
            sent, deleted = await asyncio.gather(pending, deletion)
            assert sent.status_code == 200 and deleted.status_code == 204
            assert (await client.get(f"/v1/english/sessions/{session_id}")).status_code == 404
            assert (await send(client, session_id)).status_code == 404
            assert private.encode() not in disk_bytes(isolated_store)
            assert not any(key[1] == session_id for key in storage._REPLY_CACHE)

    asyncio.run(exercise())


@pytest.mark.parametrize("failure_phase", ["reserve", "finish_before_commit", "finish_after_commit"])
def test_database_failure_is_safe_and_does_not_repeat_completed_provider(
    isolated_store, monkeypatch, failure_phase,
):
    calls = []
    private = "database-error-private-496372"

    async def provider(text, _scenario):
        calls.append(text)
        return feedback()

    monkeypatch.setattr(routes.providers, "respond", provider)
    with TestClient(application(), raise_server_exceptions=False) as client:
        created = client.post("/v1/english/sessions", json={
            "scenario_id": "everyday", "save_history": True,
        }).json()["id"]
        original_reserve = storage.reserve_turn
        original_finish = storage.finish_turn

        def unavailable(*args, **kwargs):
            if failure_phase == "finish_after_commit":
                original_finish(*args, **kwargs)
            raise sqlite3.OperationalError("synthetic storage failure")

        if failure_phase == "reserve":
            monkeypatch.setattr(storage, "reserve_turn", unavailable)
        else:
            monkeypatch.setattr(storage, "finish_turn", unavailable)
        payload = {"text": private, "idempotency_key": "database-fault-0001"}
        failed = client.post(f"/v1/english/sessions/{created}/turns", json=payload)
        assert failed.status_code == 503
        assert failed.json()["detail"]["code"] == "STORAGE_UNAVAILABLE"
        assert private not in failed.text and "synthetic" not in failed.text
        monkeypatch.setattr(storage, "reserve_turn", original_reserve)
        monkeypatch.setattr(storage, "finish_turn", original_finish)
        repeated = client.post(f"/v1/english/sessions/{created}/turns", json=payload)
        if failure_phase == "reserve":
            assert repeated.status_code == 200
            assert calls == [private]
        elif failure_phase == "finish_before_commit":
            assert repeated.status_code == 409
            assert repeated.json()["detail"]["code"] == "RETRY_NOT_AVAILABLE"
            assert calls == [private]
            assert private.encode() not in disk_bytes(isolated_store)
        else:
            assert repeated.status_code == 200
            assert repeated.json()["original"] == private
            assert calls == [private]
        assert client.get(f"/v1/english/sessions/{created}").json()["turn_count"] == (
            0 if failure_phase == "finish_before_commit" else 1
        )


def test_cache_eviction_and_restart_preserve_keys_without_repeating_provider(
    isolated_store, monkeypatch,
):
    monkeypatch.setattr(storage, "MAX_CACHED_REPLIES", 1)
    calls = []

    async def provider(text, _scenario):
        calls.append(text)
        return feedback()

    monkeypatch.setattr(routes.providers, "respond", provider)
    with TestClient(application()) as client:
        session_id = client.post("/v1/english/sessions", json={"scenario_id": "everyday"}).json()["id"]
        url = f"/v1/english/sessions/{session_id}/turns"
        first = {"text": "Private initial phrase", "idempotency_key": "cache-request-0001"}
        second = {"text": "Private second phrase", "idempotency_key": "cache-request-0002"}
        assert client.post(url, json=first).status_code == 200
        retained = client.post(url, json=second)
        assert retained.status_code == 200
        assert client.post(url, json=first).status_code == 409
        assert client.post(url, json=second).json() == retained.json()
        assert len(calls) == 2
        storage.initialize()
        assert client.post(url, json=second).status_code == 409
        assert len(calls) == 2


def test_same_key_contention_with_different_payload_keeps_first_owner_input(
    isolated_store, monkeypatch,
):
    calls = []

    async def exercise():
        started = asyncio.Event()
        release = asyncio.Event()

        async def provider(text, _scenario):
            calls.append(text)
            started.set()
            await release.wait()
            return feedback()

        monkeypatch.setattr(routes.providers, "respond", provider)
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=application()), base_url="http://testserver",
        ) as client:
            session_id = await create(client)
            original = asyncio.create_task(send(client, session_id, text="First chosen phrase"))
            await asyncio.wait_for(started.wait(), 2)
            conflicting = asyncio.create_task(send(client, session_id, text="Different phrase"))
            await asyncio.sleep(0)
            release.set()
            first, second = await asyncio.gather(original, conflicting)
            assert first.status_code == 200 and first.json()["original"] == "First chosen phrase"
            assert second.status_code == 409
            assert second.json()["detail"]["code"] == "IDEMPOTENCY_CONFLICT"
            assert calls == ["First chosen phrase"]

    asyncio.run(exercise())


def test_clear_all_recovers_quota_and_preserves_other_owners(isolated_store):
    app = application()
    with TestClient(app) as first, TestClient(app) as other:
        other_id = other.post('/v1/english/sessions', json={
            'scenario_id': 'everyday', 'save_history': True,
        }).json()['id']
        for _ in range(storage.MAX_SESSIONS):
            assert first.post('/v1/english/sessions', json={'scenario_id': 'everyday'}).status_code == 201
        assert first.post('/v1/english/sessions', json={'scenario_id': 'everyday'}).status_code == 429
        assert first.get('/v1/english/sessions').json()['sessions'] == []
        assert first.delete('/v1/english/sessions').status_code == 204
        assert first.post('/v1/english/sessions', json={'scenario_id': 'everyday'}).status_code == 201
        assert other.get('/v1/english/sessions/' + other_id).status_code == 200
