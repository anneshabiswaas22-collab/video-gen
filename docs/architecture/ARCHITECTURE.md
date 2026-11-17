# Proposed system architecture (M0 decision draft)

## Boundaries

    Browser / Next.js frontend (our original code)
                   |
           FastAPI application API
     auth | projects | assets | jobs | quota
                   |
       Job queue and orchestration layer
                   |
      GPU worker API / model capability registry
         |                 |                  |
       ComfyUI        LightX2V optional    Direct adapters
         |                 |                  |
    Wan, image models       Wan etc.       Kokoro/FFmpeg/etc.
                   |
       Object storage / project metadata
                   |
          Movie scene/timeline compiler

**One application monorepo** for original web/app/api/workers/interfaces/docs. Keep ComfyUI or other framework as managed package or isolated worker service. Avoid copying upstream repos wholesale. Do not package huge checkpoints in Git.

## Proposed code layout (not implemented yet)

    apps/web/                Creator UI, player, project editor
    services/api/            FastAPI HTTP+WebSocket/SSE endpoints
    services/worker/         GPU worker, allocation, execution adapter
    packages/schemas/        Versioned model, job, asset contracts
    packages/sdk/            Client SDK, optional
    integrations/comfyui/    Workflow transform and execution
    integrations/lightx2v/   Optional fast model runner
    integrations/media/      FFmpeg, background, transcription, lip-sync
    workflows/               Pinned, validated ComfyUI workflow JSON
    notebooks/colab/         Reproducible, terms-compliant experiments
    docs/                    Research and engineering requirements
    tests/                   Mock CPU and real GPU test suites
    infra/                   Local dev, CI and production deployment

## Core domain entities
- User/organization and permissions, project and media assets.
- CharacterReference and EnvironmentReference: ownership, accepted images, versions, embeddings optional, identity policy.
- ModelDefinition and ModelDeployment: name, source repo/commit, weight hash, license, capabilities, supported GPU.
- WorkflowDefinition: input/output schema, version, dependencies, models, resource estimates.
- GenerationJob: immutable request, status, idempotency key, progress, GPU selection, errors, cost/usage, retries.
- GenerationArtifact: bytes location, MIME type, duration, resolution, sha256, parent job, provenance.
- Scene/Shot/Timeline: timecode, character references, audio layers, clip versions, approvals.

## Generation lifecycle
1. Validate model capability, quota, media safety, content types, reference accessibility and cost estimate.
2. Store a durable request and enqueue idempotently with a job ID.
3. Scheduler checks worker health, VRAM estimates and model cache; limit concurrency by GPU.
4. Worker downloads/pins allowed weights and executes the workflow in a bounded sandbox.
5. Stream progress and record errors without leaking private media or credentials.
6. Validate output file, MIME, size, duration, hashes; write durable assets + metadata.
7. User views/downloads, retries with edited settings, or adds artifact to a movie shot.

## GPU boundary
Colab is a **developer-controlled notebook test runner**, not an always-on publicly accessible production service. The product backend must support local mock execution and external GPU workers through a defined protocol. Scale workers independently when paid infrastructure exists. No dependency on an indefinite session or on tunneling around notebook service restrictions.

## Technical defaults to decide in M0
Frontend Next.js + TypeScript; backend Python FastAPI/Pydantic; metadata PostgreSQL; artifacts S3-compatible object storage; queue Celery + Valkey/Redis candidate; media transformations FFmpeg; auth managed service or Keycloak candidate. Defaults are proposals, not installed facts.

## Compatibility and evolution
Version schemas and workflows; never let a UI button imply a model capability not present in the active deployment. Keep tests for adapter inputs/outputs. Keep the entire film project editable and append-only job history when possible. Maintain reliable migrations, backups and rollback.
