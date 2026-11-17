"""Local practice metadata with explicit opt-in transcript retention.

Default sessions never persist learner text or coaching responses. Ephemeral
replies are bounded in process memory for safe request retries, not a transcript.
This single-process development store is separate from creative project data.
"""
import hashlib
import json
import sqlite3
import uuid
from collections import OrderedDict
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path

from services.api.storage import data_dir

MAX_TURNS = 50
MAX_SESSIONS = 10
MAX_CACHED_REPLIES = 256
_REPLY_CACHE: OrderedDict[tuple[str, str, str], dict] = OrderedDict()


class StoreError(RuntimeError):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def database_path() -> Path:
    return data_dir() / "english.sqlite3"


@contextmanager
def connection():
    db = sqlite3.connect(database_path(), timeout=15)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    db.execute("PRAGMA secure_delete=ON")
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def _cache_key(session_id: str, key: str) -> tuple[str, str, str]:
    return str(database_path()), session_id, key


def _forget(session_ids):
    ids = set(session_ids)
    current_db = str(database_path())
    for key in list(_REPLY_CACHE):
        if key[0] == current_db and key[1] in ids:
            del _REPLY_CACHE[key]


def _purge(db):
    expired = [row["id"] for row in db.execute(
        "SELECT id FROM english_sessions WHERE expires_at<=?", (now(),)
    )]
    db.execute("DELETE FROM english_sessions WHERE expires_at<=?", (now(),))
    _forget(expired)
    return expired


def purge_expired():
    with connection() as db:
        expired = _purge(db)
    if expired:
        with connection() as db:
            db.execute("PRAGMA wal_checkpoint(TRUNCATE)")


def initialize():
    """Initialize the feature-owned database; retain interrupted idempotency keys."""
    with connection() as db:
        db.execute("PRAGMA journal_mode=WAL")
        db.executescript("""
            CREATE TABLE IF NOT EXISTS english_sessions (
                id TEXT PRIMARY KEY, owner TEXT NOT NULL,
                scenario_id TEXT NOT NULL, save_history INTEGER NOT NULL,
                created_at TEXT NOT NULL, expires_at TEXT NOT NULL,
                turn_count INTEGER NOT NULL DEFAULT 0
            );
            CREATE INDEX IF NOT EXISTS english_owner ON english_sessions(owner);
            CREATE TABLE IF NOT EXISTS english_turns (
                id TEXT PRIMARY KEY,
                session_id TEXT NOT NULL REFERENCES english_sessions(id) ON DELETE CASCADE,
                request_key TEXT NOT NULL, fingerprint TEXT NOT NULL,
                state TEXT NOT NULL, created_at TEXT NOT NULL,
                response_json TEXT,
                UNIQUE(session_id, request_key)
            );
        """)
        # A prior process may have contacted a model before it stopped. Never
        # execute that key again just because its response was not retained.
        db.execute("UPDATE english_turns SET state='interrupted' WHERE state='pending'")
        _purge(db)
    _REPLY_CACHE.clear()


def _owned(db, session_id, owner):
    row = db.execute(
        "SELECT * FROM english_sessions WHERE id=? AND owner=? AND expires_at>?",
        (session_id, owner, now()),
    ).fetchone()
    if row is None:
        raise StoreError("SESSION_NOT_FOUND")
    return row


def _metadata(row):
    return {"id": row["id"], "scenario_id": row["scenario_id"],
            "save_history": bool(row["save_history"]), "created_at": row["created_at"],
            "turn_count": row["turn_count"], "turns": []}


def _public(db, row):
    result = _metadata(row)
    if row["save_history"]:
        result["turns"] = [json.loads(turn["response_json"]) for turn in db.execute(
            "SELECT response_json FROM english_turns "
            "WHERE session_id=? AND state='done' AND response_json IS NOT NULL "
            "ORDER BY created_at,id", (row["id"],)
        )]
    return result


def list_saved_sessions(owner):
    """List only this owner's opted-in session metadata, never transcript text."""
    purge_expired()
    with connection() as db:
        rows = db.execute(
            "SELECT * FROM english_sessions WHERE owner=? AND save_history=1 "
            "AND expires_at>? ORDER BY created_at DESC,id DESC LIMIT ?",
            (owner, now(), MAX_SESSIONS),
        )
        return [_metadata(row) for row in rows]


def create_session(owner: str, scenario_id: str, save_history: bool):
    created = now()
    expiry = datetime.now(timezone.utc) + timedelta(days=7 if save_history else 1)
    record = {"id": "eng_" + uuid.uuid4().hex, "owner": owner,
              "scenario_id": scenario_id, "save_history": int(save_history),
              "created_at": created, "expires_at": expiry.isoformat()}
    with connection() as db:
        db.execute("BEGIN IMMEDIATE")
        _purge(db)
        if db.execute("SELECT count(*) FROM english_sessions WHERE owner=?", (owner,)).fetchone()[0] >= MAX_SESSIONS:
            raise StoreError("SESSION_LIMIT")
        db.execute("""INSERT INTO english_sessions
            (id,owner,scenario_id,save_history,created_at,expires_at)
            VALUES (:id,:owner,:scenario_id,:save_history,:created_at,:expires_at)""", record)
        return _public(db, _owned(db, record["id"], owner))


def read_session(session_id, owner):
    purge_expired()
    with connection() as db:
        return _public(db, _owned(db, session_id, owner))


def delete_session(session_id, owner):
    with connection() as db:
        _owned(db, session_id, owner)
        db.execute("DELETE FROM english_sessions WHERE id=?", (session_id,))
    _forget([session_id])
    # Truncate this local feature DB's write-ahead log after explicit deletion.
    # External filesystem snapshots/backups remain outside this app's control.
    with connection() as db:
        db.execute("PRAGMA wal_checkpoint(TRUNCATE)")


def reserve_turn(session_id: str, owner: str, key: str, text: str):
    """Return a cached replay, or reserve exactly one provider call for this key."""
    fingerprint = hashlib.sha256((owner + session_id + text).encode()).hexdigest()
    purge_expired()
    with connection() as db:
        db.execute("BEGIN IMMEDIATE")
        _purge(db)
        session = _owned(db, session_id, owner)
        previous = db.execute(
            "SELECT * FROM english_turns WHERE session_id=? AND request_key=?",
            (session_id, key),
        ).fetchone()
        if previous is not None:
            if previous["fingerprint"] != fingerprint:
                raise StoreError("IDEMPOTENCY_CONFLICT")
            if previous["state"] != "done":
                raise StoreError("RETRY_NOT_AVAILABLE")
            if previous["response_json"] is not None:
                return None, json.loads(previous["response_json"])
            cache_key = _cache_key(session_id, key)
            if cache_key not in _REPLY_CACHE:
                raise StoreError("RETRY_NOT_AVAILABLE")
            _REPLY_CACHE.move_to_end(cache_key)
            return None, json.loads(json.dumps(_REPLY_CACHE[cache_key]))
        pending = db.execute(
            "SELECT count(*) FROM english_turns WHERE session_id=? AND state='pending'",
            (session_id,),
        ).fetchone()[0]
        if session["turn_count"] + pending >= MAX_TURNS:
            raise StoreError("TURN_LIMIT")
        turn = {"id": "turn_" + uuid.uuid4().hex, "session_id": session_id,
                "request_key": key, "fingerprint": fingerprint, "created_at": now()}
        db.execute("""INSERT INTO english_turns
            (id,session_id,request_key,fingerprint,state,created_at)
            VALUES (:id,:session_id,:request_key,:fingerprint,'pending',:created_at)""", turn)
        return {**turn, "scenario_id": session["scenario_id"]}, None


def finish_turn(turn: dict, owner: str, response: dict):
    with connection() as db:
        db.execute("BEGIN IMMEDIATE")
        session = _owned(db, turn["session_id"], owner)
        stored = json.dumps(response, ensure_ascii=False) if session["save_history"] else None
        updated = db.execute(
            "UPDATE english_turns SET state='done',response_json=? WHERE id=? AND state='pending'",
            (stored, turn["id"]),
        ).rowcount
        if updated != 1:
            raise StoreError("RETRY_NOT_AVAILABLE")
        db.execute("UPDATE english_sessions SET turn_count=turn_count+1 WHERE id=?",
                   (turn["session_id"],))
    if not session["save_history"]:
        key = _cache_key(turn["session_id"], turn["request_key"])
        _REPLY_CACHE[key] = json.loads(json.dumps(response))
        _REPLY_CACHE.move_to_end(key)
        while len(_REPLY_CACHE) > MAX_CACHED_REPLIES:
            _REPLY_CACHE.popitem(last=False)


def abort_turn(turn: dict):
    """A known failed provider call can be retried; it did not complete a turn."""
    with connection() as db:
        db.execute("DELETE FROM english_turns WHERE id=? AND state='pending'", (turn["id"],))
