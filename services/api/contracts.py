"""Versioned, validated local-mode contracts. No real inference models are advertised."""
from datetime import datetime
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class JobState(StrEnum):
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"


class ProjectCreate(StrictModel):
    name: str = Field(min_length=1, max_length=100)


class Project(ProjectCreate):
    id: str
    created_at: datetime


class ModelDefinition(StrictModel):
    id: str
    name: str
    engine: Literal["mock"]
    capabilities: list[str]
    version: str
    is_mock: bool = True
    requires_gpu: bool = False


class WorkflowDefinition(StrictModel):
    id: str
    version: str
    model_id: str
    output_mime: str
    is_mock: bool = True


class Asset(StrictModel):
    id: str
    project_id: str
    sha256: str
    mime_type: str
    bytes: int


class GenerationArtifact(Asset):
    job_id: str
    workflow_version: str
    model_id: str
    created_at: datetime
    is_mock: bool = True
    download_url: str


class WorkerCapability(StrictModel):
    engine: str = "mock"
    capabilities: list[str] = Field(default_factory=lambda: ["mock_preview"])
    gpu_available: bool = False
    concurrency: int = 1


class GenerationRequest(StrictModel):
    project_id: str = Field(pattern=r"^proj_[a-f0-9]{32}$")
    model_id: Literal["mock-preview-v1"]
    prompt: str = Field(min_length=1, max_length=2000)
    idempotency_key: str = Field(min_length=8, max_length=128, pattern=r"^[a-zA-Z0-9._:-]+$")
    simulate_failure: bool = False


class GenerationJob(StrictModel):
    id: str
    project_id: str
    model_id: str
    prompt: str
    state: JobState
    progress: int = Field(ge=0, le=100)
    workflow_version: str
    is_mock: bool = True
    artifact_id: str | None = None
    error_code: str | None = None
    created_at: datetime
    updated_at: datetime


class JobEvent(StrictModel):
    state: JobState
    progress: int
    created_at: datetime


class ApiError(StrictModel):
    code: str
    message: str
