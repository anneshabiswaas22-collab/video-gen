# API and worker contracts (design proposal)

**Not implemented.** Schemas and routes will be finalized in M0 after tech selection.

## Versioned REST surface
| Method | Path | Description |
|---|---|---|
| GET | /v1/health | API readiness, not GPU readiness |
| GET | /v1/models | Declared models + capabilities, licenses, VRAM guidance, live worker compatibility |
| GET | /v1/workflows | Workflow schemas and allowed settings |
| POST | /v1/projects | Create a named project |
| GET | /v1/projects/{id} | Project with access controls |
| POST | /v1/assets | Pre-signed upload process or multipart upload with validation |
| GET | /v1/assets/{id} | Authorized artifact metadata/download |
| POST | /v1/jobs | Create idempotent generation job |
| GET | /v1/jobs/{id} | Status, progress, error and artifact IDs |
| POST | /v1/jobs/{id}/cancel | Best-effort cancellation |
| GET | /v1/jobs/{id}/events | Server-sent events or WebSocket updates |
| POST | /v1/scenes/{id}/shots | Create versioned shot |
| POST | /v1/shots/{id}/takes | Reshoot without overwriting approved take |
| POST | /v1/exports | Queue movie render job |

## Job request shape (illustrative)

    {
      "project_id": "proj_123",
      "idempotency_key": "client-unique-request",
      "type": "image_to_video",
      "model_id": "wan-ti2v-compatible",
      "workflow_version": "v1",
      "inputs": { "prompt": "...", "reference_asset_id": "asset_123" },
      "settings": { "seed": 42, "width": 512, "height": 512, "frames": 33 },
      "budget": { "max_gpu_seconds": 600, "allow_paid_api": false }
    }

Do not assume these settings are valid for every checkpoint: model-specific typed schema must validate width/height/frame counts.

## Job lifecycle
QUEUED -> RESERVING -> DOWNLOADING_MODELS (only authorized) -> RUNNING -> UPLOADING -> SUCCEEDED, or FAILED/CANCELLED/TIMED_OUT. Progress updates and partial logs are best effort; use immutable error codes such as UNSUPPORTED_CAPABILITY, GPU_OOM, MODEL_UNAVAILABLE, INPUT_INVALID, QUOTA_EXCEEDED and WORKER_LOST.

## Worker adapter
Interface: capabilities(), health(), estimate(request), generate(request, progress_callback, cancellation), shutdown(). Each adapter enforces workflow allowlists and output validation. Return artifact URI within controlled object storage, hash, duration/frame-rate/size, resource use and model provenance. Never return raw local filesystem paths to clients.

## Security / business rules
Token-scoped access; project membership; per-user/organization quotas; idempotent requests to avoid duplicate paid jobs; content safety hooks; request size/time limits; billing/usage reconciliation. Client must not submit executable arbitrary ComfyUI JSON in public multi-tenant deployments.
