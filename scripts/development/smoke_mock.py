"""Repeatable end-to-end CPU-only API smoke test, in an isolated temporary directory."""
import os
import tempfile
import time
from pathlib import Path

from fastapi.testclient import TestClient

from services.api.main import app


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="videogen-m0-") as temp:
        os.environ["VIDEOGEN_DATA_DIR"] = str(Path(temp))
        os.environ["WORKER_BACKEND"] = "mock"
        with TestClient(app) as client:
            project = client.post("/v1/projects", json={"name": "Smoke test"})
            project.raise_for_status()
            response = client.post(
                "/v1/jobs",
                json={
                    "project_id": project.json()["id"],
                    "model_id": "mock-preview-v1",
                    "prompt": "Smoke workflow",
                    "idempotency_key": "smoke-00000001",
                },
            )
            response.raise_for_status()
            job_id = response.json()["id"]
            for _ in range(50):
                job = client.get(f"/v1/jobs/{job_id}").json()
                if job["state"] == "SUCCEEDED":
                    artifact = client.get(f"/v1/artifacts/{job['artifact_id']}").json()
                    body = client.get(artifact["download_url"]).content
                    assert b"NOT AI-GENERATED" in body
                    print(f"CPU MOCK SMOKE PASSED: {job_id}; bytes={len(body)}")
                    return
                if job["state"] == "FAILED":
                    raise RuntimeError(f"Mock execution failed: {job['error_code']}")
                time.sleep(0.05)
            raise TimeoutError("Mock did not reach terminal state")


if __name__ == "__main__":
    main()
