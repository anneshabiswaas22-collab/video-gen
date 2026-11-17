"""Check the shared application boundary, not only the isolated feature router."""

import sqlite3

from services.api.storage import data_dir


def test_companion_integrated_with_shared_api(client):
    catalog = client.get("/v1/english/scenarios")
    assert catalog.status_code == 200
    assert catalog.json()["provider"]["mode"] == "offline_practice"
    session = client.post("/v1/english/sessions", json={"scenario_id": "everyday"})
    assert session.status_code == 201
    sid = session.json()["id"]
    response = client.post(f"/v1/english/sessions/{sid}/turns", json={
        "text": "Yesterday I go market.", "idempotency_key": "integrated-phrase-1"
    })
    assert response.status_code == 200
    assert response.json()["kind"] == "correction"
    assert response.json()["engine"] == "offline_practice"
    assert response.json()["suggestions"]
    # Default sessions retain request metadata, without storing learner text.
    with sqlite3.connect(data_dir() / "english.sqlite3") as db:
        assert db.execute("SELECT response_json FROM english_turns").fetchone()[0] is None
    assert client.delete(f"/v1/english/sessions/{sid}").status_code == 204
    assert client.get(f"/v1/english/sessions/{sid}").status_code == 404


def test_untrusted_browser_cannot_change_local_state(client):
    response = client.post("/v1/projects", json={"name": "Forbidden"},
                           headers={"Origin": "https://attacker.example"})
    assert response.status_code == 403
    assert client.get("/v1/projects").json() == []
    assert client.get("/v1/health", headers={"Host": "attacker.example"}).status_code == 400


def test_invalid_practice_input_does_not_echo_text_or_validation_objects(client):
    session = client.post("/v1/english/sessions", json={"scenario_id": "everyday"}).json()
    response = client.post(f"/v1/english/sessions/{session['id']}/turns", json={
        "text": " " * 4, "idempotency_key": "validation-123"
    })
    assert response.status_code == 422
    details = response.json()["error"]["details"]
    assert details and all("input" not in item and "ctx" not in item for item in details)


def test_same_api_origin_can_use_documented_api(client):
    # Swagger's Try it out uses the API origin rather than the separate web origin.
    response = client.post("/v1/projects", json={"name": ""},
                           headers={"Origin": "http://testserver"})
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "INPUT_INVALID"
