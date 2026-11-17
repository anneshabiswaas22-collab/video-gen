import pytest
from fastapi.testclient import TestClient

from services.api.main import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("VIDEOGEN_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("WORKER_BACKEND", "mock")
    monkeypatch.setenv("VIDEOGEN_COACH_PROVIDER", "offline_practice")
    with TestClient(app) as test_client:
        yield test_client
