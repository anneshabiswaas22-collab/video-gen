"""HTTP boundary for the local, consent-aware English practice feature."""
import asyncio
import hashlib
import re
import secrets
from weakref import WeakValueDictionary

from fastapi import APIRouter, HTTPException, Request, Response
from pydantic import BaseModel, ConfigDict, Field, field_validator

from . import providers, storage
from .coach import scenarios

router = APIRouter(prefix="/v1/english", tags=["English practice"])
COOKIE_NAME = "videogen_english_owner"
_COOKIE = re.compile(r"[A-Za-z0-9_-]{43}\Z")
_LOCKS: WeakValueDictionary[str, asyncio.Lock] = WeakValueDictionary()


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class SessionCreate(StrictModel):
    scenario_id: str = Field(min_length=1, max_length=80)
    save_history: bool = Field(default=False, strict=True)


class TurnCreate(StrictModel):
    text: str = Field(min_length=1, max_length=1000)
    idempotency_key: str = Field(min_length=8, max_length=100, pattern=r"^[A-Za-z0-9_-]+$")

    @field_validator("text")
    @classmethod
    def nonblank(cls, value):
        if not value.strip():
            raise ValueError("Text must contain a phrase")
        return value.strip()


def initialize():
    storage.initialize()
    _LOCKS.clear()


def _owner(request: Request, response: Response | None = None) -> str:
    token = request.cookies.get(COOKIE_NAME, "")
    if not _COOKIE.fullmatch(token):
        if response is None:
            raise HTTPException(404, detail={"code": "SESSION_NOT_FOUND", "message": "Session not found"})
        token = secrets.token_urlsafe(32)
    if response is not None:
        response.set_cookie(COOKIE_NAME, token, httponly=True, samesite="strict",
                            secure=request.url.scheme == "https", max_age=7 * 24 * 3600, path="/")
    return hashlib.sha256(token.encode()).hexdigest()


def _lock(session_id: str):
    lock = _LOCKS.get(session_id)
    if lock is None:
        lock = asyncio.Lock()
        _LOCKS[session_id] = lock
    return lock


def _error(exc):
    code = exc.code
    status = 404 if code == "SESSION_NOT_FOUND" else 429 if code in {"TURN_LIMIT", "SESSION_LIMIT"} else 409
    messages = {"SESSION_NOT_FOUND": "Session not found", "TURN_LIMIT": "This session reached its turn limit.",
                "SESSION_LIMIT": "Delete an existing session before creating another.",
                "IDEMPOTENCY_CONFLICT": "This request key was already used for a different phrase.",
                "RETRY_NOT_AVAILABLE": "The earlier response is unavailable. It was not run again. Start a new turn explicitly."}
    return HTTPException(status, detail={"code": code, "message": messages.get(code, "Practice request failed")})


@router.get("/scenarios")
def list_scenarios(request: Request, response: Response):
    _owner(request, response)
    return {"scenarios": scenarios(), "provider": providers.provider_info()}


@router.post("/sessions", status_code=201)
def new_session(body: SessionCreate, request: Request, response: Response):
    if body.scenario_id not in {item["id"] for item in scenarios()}:
        raise HTTPException(422, detail={"code": "SCENARIO_INVALID", "message": "Choose a supported scenario."})
    try:
        return storage.create_session(_owner(request, response), body.scenario_id, body.save_history)
    except storage.StoreError as exc:
        raise _error(exc) from None


@router.get("/sessions")
def list_sessions(request: Request):
    return {"sessions": storage.list_saved_sessions(_owner(request))}


@router.get("/sessions/{session_id}")
def get_session(session_id: str, request: Request):
    try:
        return storage.read_session(session_id, _owner(request))
    except storage.StoreError as exc:
        raise _error(exc) from None


@router.delete("/sessions/{session_id}", status_code=204)
async def remove_session(session_id: str, request: Request):
    owner = _owner(request)
    async with _lock(session_id):
        try:
            storage.delete_session(session_id, owner)
        except storage.StoreError as exc:
            raise _error(exc) from None
    return Response(status_code=204)


@router.post("/sessions/{session_id}/turns")
async def submit_turn(session_id: str, body: TurnCreate, request: Request):
    owner = _owner(request)
    async with _lock(session_id):
        try:
            turn, replay = storage.reserve_turn(session_id, owner, body.idempotency_key, body.text)
            if replay is not None:
                return replay
            try:
                reply = await providers.respond(body.text, turn["scenario_id"])
            except providers.ProviderUnavailable as exc:
                storage.abort_turn(turn)
                raise HTTPException(503, detail={"code": exc.code, "message": str(exc)}) from None
            except Exception:
                storage.abort_turn(turn)
                raise HTTPException(503, detail={"code": "COACH_UNAVAILABLE", "message": "Coaching could not complete. Try again."}) from None
            result = {"id": turn["id"], "session_id": session_id, "original": body.text,
                      "created_at": turn["created_at"], **reply}
            storage.finish_turn(turn, owner, result)
            return result
        except storage.StoreError as exc:
            raise _error(exc) from None
