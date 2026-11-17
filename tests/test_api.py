"""Real HTTP/API contract tests against isolated SQLite and the executing CPU worker."""
import hashlib
import time


def make_project(client):
    reply = client.post("/v1/projects", json={"name": "My film"})
    assert reply.status_code == 201
    return reply.json()["id"]


def make_request(project_id, key="request-00000001", **overrides):
    return {
        "project_id": project_id,
        "model_id": "mock-preview-v1",
        "prompt": "A forest sunrise in a wide frame",
        "idempotency_key": key,
        **overrides,
    }


def wait_for_terminal(client, job_id):
    for _ in range(40):
        result = client.get(f"/v1/jobs/{job_id}")
        assert result.status_code == 200
        if result.json()["state"] in ("SUCCEEDED", "FAILED"):
            return result.json()
        time.sleep(0.05)
    raise AssertionError("Mock job did not finish")


def test_health_models_and_openapi(client):
    health = client.get("/v1/health").json()
    assert health == {"status": "ok", "mode": "mock", "inference_enabled": False}
    models = client.get("/v1/models").json()
    assert len(models) == 1
    assert models[0]["is_mock"] is True
    assert models[0]["requires_gpu"] is False
    assert client.get("/v1/worker-capability").json()["gpu_available"] is False
    schema = client.get("/openapi.json").json()
    assert "/v1/jobs" in schema["paths"]
    assert "/v1/projects" in schema["paths"]


def test_create_project_and_mock_generation_lifecycle(client):
    project_id = make_project(client)
    assert client.get(f"/v1/projects/{project_id}").json()["name"] == "My film"
    assert len(client.get("/v1/projects").json()) == 1
    submitted = client.post("/v1/jobs", json=make_request(project_id))
    assert submitted.status_code == 202
    created = submitted.json()
    assert created["is_mock"] is True
    assert created["state"] in ("QUEUED", "RUNNING")
    assert "idempotency_key" not in created
    assert "fingerprint" not in created
    job = wait_for_terminal(client, created["id"])
    assert job["state"] == "SUCCEEDED"
    assert job["progress"] == 100
    assert len(client.get(f"/v1/projects/{project_id}/jobs").json()) == 1
    events = client.get(f"/v1/jobs/{job['id']}/events").json()
    assert events[0]["state"] == "QUEUED"
    assert events[-1]["state"] == "SUCCEEDED"
    assert any(e["state"] == "RUNNING" for e in events)
    artifact = client.get(f"/v1/artifacts/{job['artifact_id']}").json()
    assert artifact["is_mock"] is True
    assert artifact["mime_type"] == "text/plain"
    assert artifact["workflow_version"] == "mock-preview/1"
    downloaded = client.get(artifact["download_url"])
    assert downloaded.status_code == 200
    assert downloaded.headers["content-disposition"].startswith("attachment;")
    assert downloaded.content.startswith(b"MOCK ARTIFACT")
    assert b"NOT AI-GENERATED" in downloaded.content
    assert hashlib.sha256(downloaded.content).hexdigest() == artifact["sha256"]
    assert len(downloaded.content) == artifact["bytes"]


def test_idempotency_and_conflicting_payload(client):
    project_id = make_project(client)
    payload = make_request(project_id)
    first = client.post("/v1/jobs", json=payload)
    replay = client.post("/v1/jobs", json=payload)
    assert first.status_code == replay.status_code == 202
    assert first.json()["id"] == replay.json()["id"]
    assert len(client.get(f"/v1/projects/{project_id}/jobs").json()) == 1
    conflict = client.post("/v1/jobs", json={**payload, "prompt": "Different"})
    assert conflict.status_code == 409
    assert conflict.json()["detail"]["code"] == "IDEMPOTENCY_CONFLICT"


def test_worker_failure_is_recorded_without_artifact(client):
    project_id = make_project(client)
    response = client.post(
        "/v1/jobs",
        json=make_request(project_id, key="mock-failure-0001", simulate_failure=True),
    )
    assert response.status_code == 202
    job = wait_for_terminal(client, response.json()["id"])
    assert job["state"] == "FAILED"
    assert job["error_code"] == "MOCK_EXECUTION_FAILED"
    assert job["artifact_id"] is None
    assert client.get(f"/v1/jobs/{job['id']}/events").json()[-1]["state"] == "FAILED"


def test_validation_and_negative_access(client):
    missing_project = "proj_" + "a" * 32
    result = client.post("/v1/jobs", json=make_request(missing_project))
    assert result.status_code == 404
    assert result.json()["detail"]["code"] == "PROJECT_NOT_FOUND"
    project = make_project(client)
    invalid = client.post("/v1/jobs", json=make_request(project, model_id="unknown-model"))
    assert invalid.status_code == 422
    assert invalid.json()["error"]["code"] == "INPUT_INVALID"
    blank = client.post("/v1/jobs", json=make_request(project, prompt="   "))
    assert blank.status_code == 422
    assert client.get("/v1/jobs/job_unknown").status_code == 404
    assert client.get("/v1/artifacts/art_unknown/download").status_code == 404
    invalid_fields = client.post(
        "/v1/projects", json={"name": "Bad", "unexpected": "untrusted"}
    )
    assert invalid_fields.status_code == 422
    # CORS is only browser-origin protection, NOT authentication. Do not publicly bind API.
    forbidden_origin = client.options(
        "/v1/jobs",
        headers={
            "Origin": "https://unknown.example",
            "Access-Control-Request-Method": "POST",
        },
    )
    assert forbidden_origin.status_code == 400
