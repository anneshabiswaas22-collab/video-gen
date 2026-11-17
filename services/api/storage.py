"""SQLite persistence for the single-user, localhost development mock."""
import hashlib
import json
import os
import sqlite3
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from services.api.contracts import GenerationRequest

WORKFLOW_VERSION = "mock-preview/1"


def _utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def data_dir() -> Path:
    root = Path(os.environ.get("VIDEOGEN_DATA_DIR", ".local/videogen")).resolve()
    root.mkdir(parents=True, exist_ok=True)
    return root


@contextmanager
def connection():
    conn = sqlite3.connect(data_dir() / "studio.sqlite3", timeout=15)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()


def initialize() -> None:
    with connection() as db:
        db.execute("PRAGMA journal_mode=WAL")
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS projects (
              id TEXT PRIMARY KEY, name TEXT NOT NULL, created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS jobs (
              id TEXT PRIMARY KEY,
              project_id TEXT NOT NULL REFERENCES projects(id),
              idempotency_key TEXT NOT NULL,
              fingerprint TEXT NOT NULL,
              model_id TEXT NOT NULL,
              prompt TEXT NOT NULL,
              simulate_failure INTEGER NOT NULL,
              state TEXT NOT NULL,
              progress INTEGER NOT NULL,
              workflow_version TEXT NOT NULL,
              artifact_id TEXT,
              error_code TEXT,
              created_at TEXT NOT NULL,
              updated_at TEXT NOT NULL,
              UNIQUE(project_id, idempotency_key)
            );
            CREATE TABLE IF NOT EXISTS artifacts (
              id TEXT PRIMARY KEY, job_id TEXT NOT NULL UNIQUE,
              project_id TEXT NOT NULL, model_id TEXT NOT NULL,
              sha256 TEXT NOT NULL, mime_type TEXT NOT NULL, bytes INTEGER NOT NULL,
              workflow_version TEXT NOT NULL, created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS job_events (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              job_id TEXT NOT NULL, state TEXT NOT NULL,
              progress INTEGER NOT NULL, created_at TEXT NOT NULL
            );
            """
        )


def _row(result):
    return dict(result) if result is not None else None


def create_project(name: str) -> dict:
    project = {"id": f"proj_{uuid.uuid4().hex}", "name": name.strip(), "created_at": _utc()}
    with connection() as db:
        db.execute(
            "INSERT INTO projects (id, name, created_at) VALUES (:id, :name, :created_at)",
            project,
        )
    return project


def project(project_id: str) -> dict | None:
    with connection() as db:
        return _row(db.execute("SELECT * FROM projects WHERE id=?", (project_id,)).fetchone())


def projects() -> list[dict]:
    with connection() as db:
        return [dict(row) for row in db.execute("SELECT * FROM projects ORDER BY created_at DESC")]


def job(job_id: str) -> dict | None:
    with connection() as db:
        row = db.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        return _row(row)


def jobs(project_id: str) -> list[dict]:
    with connection() as db:
        return [
            dict(row)
            for row in db.execute(
                "SELECT * FROM jobs WHERE project_id=? ORDER BY created_at DESC", (project_id,)
            )
        ]


def create_job(request: GenerationRequest) -> tuple[dict, bool]:
    payload = request.model_dump(exclude={"idempotency_key"})
    fingerprint = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    now = _utc()
    with connection() as db:
        db.execute("BEGIN IMMEDIATE")
        prior = db.execute(
            "SELECT * FROM jobs WHERE project_id=? AND idempotency_key=?",
            (request.project_id, request.idempotency_key),
        ).fetchone()
        if prior is not None:
            if prior["fingerprint"] != fingerprint:
                raise ValueError("IDEMPOTENCY_CONFLICT")
            return dict(prior), False
        record = {
            "id": f"job_{uuid.uuid4().hex}",
            **request.model_dump(),
            "simulate_failure": int(request.simulate_failure),
            "fingerprint": fingerprint,
            "state": "QUEUED",
            "progress": 0,
            "workflow_version": WORKFLOW_VERSION,
            "artifact_id": None,
            "error_code": None,
            "created_at": now,
            "updated_at": now,
        }
        db.execute(
            """INSERT INTO jobs
            (id,project_id,idempotency_key,fingerprint,model_id,prompt,
             simulate_failure,state,progress,workflow_version,artifact_id,
             error_code,created_at,updated_at)
            VALUES (:id,:project_id,:idempotency_key,:fingerprint,:model_id,:prompt,
                    :simulate_failure,:state,:progress,:workflow_version,:artifact_id,
                    :error_code,:created_at,:updated_at)""",
            record,
        )
        db.execute(
            "INSERT INTO job_events (job_id,state,progress,created_at) VALUES (?,?,?,?)",
            (record["id"], "QUEUED", 0, now),
        )
        return record, True


def _transition(db, job_id: str, state: str, progress: int, error: str | None = None,
                artifact_id: str | None = None) -> None:
    now = _utc()
    db.execute(
        """UPDATE jobs SET state=?, progress=?, error_code=?, artifact_id=?, updated_at=?
           WHERE id=?""",
        (state, progress, error, artifact_id, now, job_id),
    )
    db.execute(
        "INSERT INTO job_events (job_id,state,progress,created_at) VALUES (?,?,?,?)",
        (job_id, state, progress, now),
    )


def claim_job() -> dict | None:
    with connection() as db:
        db.execute("BEGIN IMMEDIATE")
        row = db.execute(
            "SELECT * FROM jobs WHERE state='QUEUED' ORDER BY created_at,rowid LIMIT 1"
        ).fetchone()
        if row is not None:
            _transition(db, row["id"], "RUNNING", 15)
            return _row(db.execute("SELECT * FROM jobs WHERE id=?", (row["id"],)).fetchone())
        return None


def progress_job(job_id: str, value: int) -> None:
    if type(value) is not int or not 0 <= value < 100:
        raise ValueError("INVALID_RUNNING_PROGRESS")
    with connection() as db:
        db.execute("BEGIN IMMEDIATE")
        if db.execute(
            "SELECT 1 FROM jobs WHERE id=? AND state='RUNNING' AND progress<?", (job_id, value)
        ).fetchone():
            _transition(db, job_id, "RUNNING", value)


def fail_job(job_id: str, code: str) -> None:
    with connection() as db:
        db.execute("BEGIN IMMEDIATE")
        if db.execute(
            "SELECT 1 FROM jobs WHERE id=? AND state='RUNNING'", (job_id,)
        ).fetchone():
            _transition(db, job_id, "FAILED", 100, error=code)


def recover_interrupted() -> None:
    """Fail abandoned work without letting a late worker revive terminal jobs."""
    with connection() as db:
        db.execute("BEGIN IMMEDIATE")
        rows = db.execute("SELECT id FROM jobs WHERE state='RUNNING'").fetchall()
        for row in rows:
            _transition(db, row["id"], "FAILED", 100, error="WORKER_LOST")


def complete_job(request: dict, body: bytes) -> dict:
    """Commit one running task, cleaning generated files after failed writes/transactions."""
    artifact_id = f"art_{uuid.uuid4().hex}"
    folder = data_dir() / "artifacts"
    target = folder / f"{artifact_id}.txt"
    temp = folder / f".{artifact_id}.tmp"
    try:
        with connection() as db:
            db.execute("BEGIN IMMEDIATE")
            task = db.execute(
                "SELECT * FROM jobs WHERE id=? AND state='RUNNING'", (request["id"],)
            ).fetchone()
            if task is None:
                raise ValueError("JOB_NOT_RUNNING")
            folder.mkdir(parents=True, exist_ok=True)
            temp.write_bytes(body)
            os.replace(temp, target)
            artifact = {
                "id": artifact_id, "job_id": task["id"], "project_id": task["project_id"],
                "model_id": task["model_id"], "sha256": hashlib.sha256(body).hexdigest(),
                "mime_type": "text/plain", "bytes": len(body),
                "workflow_version": task["workflow_version"], "created_at": _utc(),
            }
            db.execute(
                """INSERT INTO artifacts
                (id,job_id,project_id,model_id,sha256,mime_type,bytes,workflow_version,created_at)
                VALUES (:id,:job_id,:project_id,:model_id,:sha256,:mime_type,:bytes,
                        :workflow_version,:created_at)""", artifact,
            )
            _transition(db, task["id"], "SUCCEEDED", 100, artifact_id=artifact_id)
    except BaseException:
        # Only these server-generated files from this attempted completion are removed.
        temp.unlink(missing_ok=True)
        target.unlink(missing_ok=True)
        raise
    return artifact


def artifact(artifact_id: str) -> dict | None:
    with connection() as db:
        return _row(db.execute("SELECT * FROM artifacts WHERE id=?", (artifact_id,)).fetchone())


def history(job_id: str) -> list[dict]:
    with connection() as db:
        return [
            dict(row)
            for row in db.execute(
                "SELECT state,progress,created_at FROM job_events WHERE job_id=? ORDER BY id",
                (job_id,),
            )
        ]
