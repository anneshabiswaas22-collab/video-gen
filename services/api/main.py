"""VideoGen M0: localhost-only development API and CPU mock-worker integration."""
import asyncio
from contextlib import asynccontextmanager
import os

from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from services.api import storage
from services.api.contracts import (
    GenerationArtifact,
    GenerationJob,
    GenerationRequest,
    JobEvent,
    ModelDefinition,
    Project,
    ProjectCreate,
    WorkerCapability,
    WorkflowDefinition,
)
from services.worker.mock import worker_loop

MODEL = ModelDefinition(
    id="mock-preview-v1",
    name="Mock preview receipt — no AI inference",
    engine="mock",
    capabilities=["mock_preview"],
    version="1",
)
WORKFLOW = WorkflowDefinition(
    id="mock-preview", version="1", model_id=MODEL.id, output_mime="text/plain"
)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    if os.environ.get("WORKER_BACKEND", "mock") != "mock":
        raise RuntimeError("M0 supports only WORKER_BACKEND=mock")
    storage.initialize()
    storage.recover_interrupted()
    worker = asyncio.create_task(worker_loop())
    try:
        yield
    finally:
        worker.cancel()
        try:
            await worker
        except asyncio.CancelledError:
            pass


app = FastAPI(
    title="VideoGen local mock API",
    version="0.2.0",
    description="Development-only API, no real AI or authentication. Bind to localhost only.",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.exception_handler(RequestValidationError)
async def invalid_request(_request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": {"code": "INPUT_INVALID", "message": "Request validation failed",
                           "details": exc.errors()}},
    )


def _not_found(resource: str) -> HTTPException:
    return HTTPException(
        404,
        detail={"code": f"{resource}_NOT_FOUND", "message": f"{resource.title()} not found"},
    )


def _public_job(record: dict) -> dict:
    """Never serialize private worker flags or idempotency fingerprints."""
    return {name: record.get(name) for name in GenerationJob.model_fields}


@app.get("/v1/health")
def health():
    return {"status": "ok", "mode": "mock", "inference_enabled": False}


@app.get("/v1/models", response_model=list[ModelDefinition])
def models():
    return [MODEL]


@app.get("/v1/workflows", response_model=list[WorkflowDefinition])
def workflows():
    return [WORKFLOW]


@app.get("/v1/worker-capability", response_model=WorkerCapability)
def capabilities():
    return WorkerCapability()


@app.post("/v1/projects", response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(request: ProjectCreate):
    if not request.name.strip():
        raise HTTPException(422, detail={"code": "INPUT_INVALID", "message": "Name is blank"})
    return storage.create_project(request.name)


@app.get("/v1/projects", response_model=list[Project])
def list_projects():
    return storage.projects()


@app.get("/v1/projects/{project_id}", response_model=Project)
def read_project(project_id: str):
    result = storage.project(project_id)
    if result is None:
        raise _not_found("PROJECT")
    return result


@app.post("/v1/jobs", response_model=GenerationJob, status_code=status.HTTP_202_ACCEPTED)
def create_job(request: GenerationRequest):
    if storage.project(request.project_id) is None:
        raise _not_found("PROJECT")
    if not request.prompt.strip():
        raise HTTPException(422, detail={"code": "INPUT_INVALID", "message": "Prompt is blank"})
    try:
        record, _created = storage.create_job(request)
        return _public_job(record)
    except ValueError as exc:
        if str(exc) == "IDEMPOTENCY_CONFLICT":
            raise HTTPException(
                409,
                detail={"code": "IDEMPOTENCY_CONFLICT", "message": "Key reused with new inputs"},
            ) from exc
        raise


@app.get("/v1/projects/{project_id}/jobs", response_model=list[GenerationJob])
def list_jobs(project_id: str):
    if storage.project(project_id) is None:
        raise _not_found("PROJECT")
    return [_public_job(item) for item in storage.jobs(project_id)]


@app.get("/v1/jobs/{job_id}", response_model=GenerationJob)
def read_job(job_id: str):
    result = storage.job(job_id)
    if result is None:
        raise _not_found("JOB")
    return _public_job(result)


@app.get("/v1/jobs/{job_id}/events", response_model=list[JobEvent])
def job_events(job_id: str):
    if storage.job(job_id) is None:
        raise _not_found("JOB")
    return storage.history(job_id)


@app.get("/v1/artifacts/{artifact_id}", response_model=GenerationArtifact)
def read_artifact(artifact_id: str):
    result = storage.artifact(artifact_id)
    if result is None:
        raise _not_found("ARTIFACT")
    return {
        **result,
        "is_mock": True,
        "download_url": f"/v1/artifacts/{artifact_id}/download",
    }


@app.get("/v1/artifacts/{artifact_id}/download")
def download_artifact(artifact_id: str):
    result = storage.artifact(artifact_id)
    if result is None:
        raise _not_found("ARTIFACT")
    # The path is derived from a server-generated ID, not untrusted request path segments.
    target = storage.data_dir() / "artifacts" / f"{result['id']}.txt"
    if not target.is_file():
        raise HTTPException(503, detail={"code": "ARTIFACT_MISSING",
                                         "message": "Stored result is unavailable"})
    return FileResponse(
        target,
        media_type="text/plain",
        filename=f"{artifact_id}-MOCK.txt",
        headers={"X-Content-Type-Options": "nosniff", "Content-Security-Policy": "sandbox"},
    )
