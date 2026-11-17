# Implemented local API surface — 0.3.0

The recovered M0 creative API and the English feature run in one FastAPI app.
This is localhost development, not a multi-tenant or publicly authenticated service.
The existing `/v1/health` describes the mock creative worker; tutor provider
configuration is reported separately by `/v1/english/scenarios`.

| Method | Route | Implemented behavior |
|---|---|---|
| GET | `/v1/health`, `/v1/models`, `/v1/workflows`, `/v1/worker-capability` | Explicit mock/no-GPU metadata |
| POST/GET | `/v1/projects` | Persist/list local creative projects |
| GET | `/v1/projects/{id}`, `/v1/projects/{id}/jobs` | Project and durable job history |
| POST/GET | `/v1/jobs`, `/v1/jobs/{id}` | Idempotent creation and state/progress |
| GET | `/v1/jobs/{id}/events` | JSON event list, not SSE |
| GET | `/v1/artifacts/{id}`, `/v1/artifacts/{id}/download` | Metadata and text/plain mock receipt |
| GET | `/v1/english/scenarios` | Supported examples, configuration-only provider facts and owner cookie |
| POST | `/v1/english/sessions` | `{scenario_id,save_history:false}`; strict explicit Boolean consent |
| GET | `/v1/english/sessions` | Owner's saved-session metadata only; no transcript in list |
| GET/DELETE | `/v1/english/sessions/{id}` | Owner-scoped resume or deletion |
| POST | `/v1/english/sessions/{id}/turns` | `{text,idempotency_key}`; typed feedback, replay-safe requests |

English inputs are capped at1000 characters, sessions at50 completed turns and
10 active sessions per cookie owner. A random HttpOnly SameSiteStrict cookie
scopes practice access; permitted browser origins and loopback hosts are checked.
Different owners receive404 rather than learning whether another session exists.
This cookie is not a production account, and the creative API remains single-user.

Replies include `kind`, `suggestions`, `explanation`, `reply`, `next_question`,
`engine` and `supported`, plus turn/session IDs, original input and timestamp.
Offline unknown inputs return `unsupported` without claiming a grammar verdict.

Default sessions store metadata/fingerprints but no text on disk. Saved sessions
explicitly store response JSON including original text. Same-key/same-input replay
returns the prior reply; a changed phrase conflicts409. After restart, unsaved
replies are unavailable and replay returns409 rather than rerunning a model.
Provider failures return503 with safe codes, not raw model/network details. Failed
turns do not count as completed; deletion removes rows/caches and checkpoints WAL.

No creative cancellation, asset upload, timeline, real inference or streaming
conversation endpoint is implemented. Earlier routes below remain design proposals.

## Historical proposed contracts

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
