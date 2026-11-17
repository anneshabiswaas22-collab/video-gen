"""Real local HTTP/SQLite checks for privacy, ownership, retries and lifecycle."""
import asyncio
from contextlib import asynccontextmanager

import httpx
import pytest
from english_friend import routes, storage
from english_friend.providers import ProviderUnavailable
from fastapi import FastAPI
from fastapi.testclient import TestClient


@asynccontextmanager
async def lifespan(_app):
    routes.initialize()
    yield


def practice_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(routes.router)
    return app


@pytest.fixture
def practice_client(tmp_path, monkeypatch):
    monkeypatch.setenv("VIDEOGEN_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("VIDEOGEN_COACH_PROVIDER", "offline_practice")
    with TestClient(practice_app()) as client:
        yield client


def session(client, *, save_history=False, scenario_id="everyday"):
    result = client.post("/v1/english/sessions", json={
        "scenario_id": scenario_id, "save_history": save_history,
    })
    assert result.status_code == 201, result.text
    return result.json()


def turn(client, session_id, text="Yesterday I go market.", key="request-0001"):
    return client.post(f"/v1/english/sessions/{session_id}/turns", json={
        "text": text, "idempotency_key": key,
    })


def db_bytes():
    return b"".join(p.read_bytes() for p in storage.database_path().parent.glob("english.sqlite3*") if p.is_file())


def test_scenarios_mint_private_owner_cookie_and_label_provider(practice_client):
    result = practice_client.get("/v1/english/scenarios")
    assert result.status_code == 200
    assert {row["id"] for row in result.json()["scenarios"]} == {"everyday", "work", "travel"}
    assert result.json()["provider"]["mode"] == "offline_practice"
    cookie = result.headers["set-cookie"]
    assert "HttpOnly" in cookie and "SameSite=strict" in cookie
    assert practice_client.cookies.get(routes.COOKIE_NAME) not in result.text


def test_real_correction_retry_and_no_default_transcript_on_disk(practice_client):
    created = session(practice_client)
    assert created["save_history"] is False and created["turn_count"] == 0 and created["turns"] == []
    first = turn(practice_client, created["id"])
    assert first.status_code == 200
    assert first.json()["kind"] == "correction"
    improved = first.json()["suggestions"][0]
    assert turn(practice_client, created["id"], improved, "request-0002").json()["kind"] == "accepted"
    private = "never-persist-this-private-learner-phrase-983461"
    unknown = turn(practice_client, created["id"], private, "request-0003")
    assert unknown.status_code == 200 and unknown.json()["kind"] == "unsupported"
    snapshot = practice_client.get(f"/v1/english/sessions/{created['id']}").json()
    assert snapshot["turn_count"] == 3 and snapshot["turns"] == []
    assert private.encode() not in db_bytes()
    assert b"Yesterday I go market" not in db_bytes()
    assert b"This is limited offline phrase practice" not in db_bytes()


def test_saved_history_survives_restart_with_same_owner(practice_client):
    created = session(practice_client, save_history=True)
    private = "explicitly-saved-private-practice-715820"
    reply = turn(practice_client, created["id"], private).json()
    assert private.encode() in db_bytes()
    cookie = practice_client.cookies.get(routes.COOKIE_NAME)
    with TestClient(practice_app()) as restarted:
        restarted.cookies.set(routes.COOKIE_NAME, cookie)
        result = restarted.get(f"/v1/english/sessions/{created['id']}")
        assert result.status_code == 200
        assert result.json()["turns"] == [reply]
        assert result.json()["turn_count"] == 1
        replay = turn(restarted, created["id"], private)
        assert replay.status_code == 200 and replay.json() == reply


def test_other_owner_cannot_read_submit_or_delete(practice_client):
    created = session(practice_client, save_history=True)
    turn(practice_client, created["id"])
    with TestClient(practice_app()) as stranger:
        stranger.get("/v1/english/scenarios")
        assert stranger.get(f"/v1/english/sessions/{created['id']}").status_code == 404
        assert turn(stranger, created["id"]).status_code == 404
        assert stranger.delete(f"/v1/english/sessions/{created['id']}").status_code == 404
    assert practice_client.get(f"/v1/english/sessions/{created['id']}").status_code == 200


def test_invalid_and_missing_owner_cookie_does_not_grant_access(practice_client):
    created = session(practice_client)
    practice_client.cookies.clear()
    assert practice_client.get(f"/v1/english/sessions/{created['id']}").status_code == 404
    practice_client.cookies.set(routes.COOKIE_NAME, "invalid")
    assert turn(practice_client, created["id"]).status_code == 404
    # An invalid client-supplied cookie is replaced with a fresh random owner.
    response = practice_client.post("/v1/english/sessions", json={"scenario_id": "everyday"})
    assert response.status_code == 201
    assert "invalid;" not in response.headers["set-cookie"]


def test_delete_removes_saved_children_and_ephemeral_replay(practice_client):
    created = session(practice_client, save_history=True)
    private = "erase-private-phrase-after-consented-retention-7129"
    turn(practice_client, created["id"], private)
    assert private.encode() in db_bytes()
    assert practice_client.delete(f"/v1/english/sessions/{created['id']}").status_code == 204
    assert practice_client.get(f"/v1/english/sessions/{created['id']}").status_code == 404
    with storage.connection() as db:
        assert db.execute("SELECT count(*) FROM english_turns").fetchone()[0] == 0
    assert private.encode() not in db_bytes()
    temporary = session(practice_client)
    turn(practice_client, temporary["id"])
    assert any(key[1] == temporary["id"] for key in storage._REPLY_CACHE)
    assert practice_client.delete(f"/v1/english/sessions/{temporary['id']}").status_code == 204
    assert not any(key[1] == temporary["id"] for key in storage._REPLY_CACHE)


def test_expired_session_is_purged_with_saved_text(practice_client):
    created = session(practice_client, save_history=True)
    private = "expired-private-sentence-854921"
    turn(practice_client, created["id"], private)
    with storage.connection() as db:
        db.execute("UPDATE english_sessions SET expires_at='2000-01-01' WHERE id=?", (created["id"],))
    assert practice_client.get(f"/v1/english/sessions/{created['id']}").status_code == 404
    with storage.connection() as db:
        assert db.execute("SELECT count(*) FROM english_sessions").fetchone()[0] == 0
        assert db.execute("SELECT count(*) FROM english_turns").fetchone()[0] == 0
    assert private.encode() not in db_bytes()


def test_idempotency_replay_conflict_and_restart_never_repeat_provider(practice_client, monkeypatch):
    calls = []
    async def reply(text, scenario_id):
        calls.append(text)
        return {"kind": "accepted", "suggestions": [], "explanation": "", "reply": "Clear.",
                "next_question": "What next?", "engine": "offline_practice", "supported": True}
    monkeypatch.setattr(routes.providers, "respond", reply)
    created = session(practice_client)
    first = turn(practice_client, created["id"])
    replay = turn(practice_client, created["id"])
    assert replay.status_code == 200 and replay.json() == first.json()
    conflict = turn(practice_client, created["id"], "A different phrase.")
    assert conflict.status_code == 409 and conflict.json()["detail"]["code"] == "IDEMPOTENCY_CONFLICT"
    assert len(calls) == 1
    assert practice_client.get(f"/v1/english/sessions/{created['id']}").json()["turn_count"] == 1
    # Simulate process loss: default responses are deliberately not kept on disk.
    storage.initialize()
    lost = turn(practice_client, created["id"])
    assert lost.status_code == 409 and lost.json()["detail"]["code"] == "RETRY_NOT_AVAILABLE"
    assert len(calls) == 1


def test_provider_failure_is_safe_and_same_request_can_retry(practice_client, monkeypatch):
    created = session(practice_client)
    private = "failed-provider-private-phrase-83421"
    async def unavailable(*_args):
        raise ProviderUnavailable("PROVIDER_CONNECTION_FAILED")
    monkeypatch.setattr(routes.providers, "respond", unavailable)
    failed = turn(practice_client, created["id"], private)
    assert failed.status_code == 503
    assert failed.json()["detail"]["code"] == "PROVIDER_CONNECTION_FAILED"
    assert private not in failed.text and private.encode() not in db_bytes()
    assert practice_client.get(f"/v1/english/sessions/{created['id']}").json()["turn_count"] == 0
    from english_friend.coach import coach
    async def available(text, scenario_id):
        return coach(text, scenario_id)
    monkeypatch.setattr(routes.providers, "respond", available)
    assert turn(practice_client, created["id"], private).status_code == 200


def test_invalid_inputs_and_explicit_boolean_consent(practice_client):
    assert practice_client.post("/v1/english/sessions", json={"scenario_id": "no-such-scenario"}).status_code == 422
    assert practice_client.post("/v1/english/sessions", json={"scenario_id": "everyday", "save_history": "true"}).status_code == 422
    assert practice_client.post("/v1/english/sessions", json={"scenario_id": "everyday", "model": "untrusted"}).status_code == 422
    created = session(practice_client)
    for text in ("", "   ", "a" * 1001):
        assert turn(practice_client, created["id"], text).status_code == 422
    assert turn(practice_client, created["id"], key="tiny").status_code == 422
    assert turn(practice_client, created["id"], key="untrusted/key").status_code == 422
    assert practice_client.get(f"/v1/english/sessions/{created['id']}").json()["turn_count"] == 0


def test_session_and_turn_limits_are_enforced_without_losing_replays(practice_client, monkeypatch):
    monkeypatch.setattr(storage, "MAX_SESSIONS", 2)
    first = session(practice_client)
    session(practice_client)
    assert practice_client.post("/v1/english/sessions", json={"scenario_id": "everyday"}).status_code == 429
    monkeypatch.setattr(storage, "MAX_TURNS", 1)
    response = turn(practice_client, first["id"])
    assert response.status_code == 200
    assert turn(practice_client, first["id"]).json() == response.json()
    assert turn(practice_client, first["id"], key="request-0002").status_code == 429


def test_concurrent_same_key_executes_provider_once(tmp_path, monkeypatch):
    monkeypatch.setenv("VIDEOGEN_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("VIDEOGEN_COACH_PROVIDER", "offline_practice")
    calls = []
    async def slow_reply(text, scenario_id):
        calls.append(text)
        await asyncio.sleep(0.02)
        return {"kind": "accepted", "suggestions": [], "explanation": "", "reply": "Clear.",
                "next_question": "", "engine": "offline_practice", "supported": True}
    monkeypatch.setattr(routes.providers, "respond", slow_reply)
    async def exercise():
        app = practice_app()
        routes.initialize()
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://testserver") as client:
            created = session_response = await client.post("/v1/english/sessions", json={"scenario_id": "everyday"})
            assert session_response.status_code == 201
            session_id = created.json()["id"]
            async def post():
                return await client.post(f"/v1/english/sessions/{session_id}/turns", json={
                    "text": "Hello", "idempotency_key": "concurrent-key-001"})
            first, second = await asyncio.gather(post(), post())
            assert first.status_code == second.status_code == 200
            assert first.json() == second.json()
            result = await client.get(f"/v1/english/sessions/{session_id}")
            assert result.json()["turn_count"] == 1
    asyncio.run(exercise())
    assert len(calls) == 1


def test_saved_session_list_excludes_ephemeral_and_other_owners(practice_client):
    hidden = session(practice_client)
    saved = session(practice_client, save_history=True)
    private = "saved-list-must-not-include-transcript-812734"
    turn(practice_client, saved["id"], private)
    result = practice_client.get("/v1/english/sessions")
    assert result.status_code == 200
    items = result.json()["sessions"]
    assert [item["id"] for item in items] == [saved["id"]]
    assert items[0]["turn_count"] == 1 and items[0]["turns"] == []
    assert private not in result.text and hidden["id"] not in result.text
    with TestClient(practice_app()) as stranger:
        stranger.get("/v1/english/scenarios")
        other = session(stranger, save_history=True)
        own = stranger.get("/v1/english/sessions", params={"owner": "forged-owner"})
        assert [item["id"] for item in own.json()["sessions"]] == [other["id"]]
        assert saved["id"] not in own.text
    assert [item["id"] for item in practice_client.get("/v1/english/sessions").json()["sessions"]] == [saved["id"]]


def test_saved_session_list_survives_restart_and_removes_deleted_expired(practice_client):
    older = session(practice_client, save_history=True)
    newer = session(practice_client, save_history=True, scenario_id="work")
    expired = session(practice_client, save_history=True)
    with storage.connection() as db:
        db.execute("UPDATE english_sessions SET expires_at='2000-01-01' WHERE id=?", (expired["id"],))
    cookie = practice_client.cookies.get(routes.COOKIE_NAME)
    with TestClient(practice_app()) as restarted:
        restarted.cookies.set(routes.COOKIE_NAME, cookie)
        response = restarted.get("/v1/english/sessions")
        assert response.status_code == 200
        assert [item["id"] for item in response.json()["sessions"]] == [newer["id"], older["id"]]
        assert all(item["turns"] == [] for item in response.json()["sessions"])
        assert restarted.delete(f"/v1/english/sessions/{newer['id']}").status_code == 204
        listed = restarted.get("/v1/english/sessions").json()["sessions"]
        assert [item["id"] for item in listed] == [older["id"]]


def test_owner_cookie_renews_without_changing_session_ownership(practice_client):
    client = practice_client
    initial = client.get('/v1/english/scenarios')
    token = initial.cookies[routes.COOKIE_NAME]
    renewed = client.post('/v1/english/sessions', json={
        'scenario_id': 'everyday', 'save_history': True,
    })
    assert renewed.status_code == 201
    assert renewed.cookies[routes.COOKIE_NAME] == token
    assert 'Max-Age=604800' in renewed.headers['set-cookie']
    assert client.get('/v1/english/sessions/' + renewed.json()['id']).status_code == 200
