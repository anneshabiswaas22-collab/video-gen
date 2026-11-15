# M0.2 local mock studio — setup and teardown

This branch introduces an executable CPU-only generation **mock**. It generates a
plain-text receipt, **not** an AI-produced image, video or audio file. Never expose
this unauthenticated development service on a public network.

## Requirements
- Python 3.11+ and Node.js 22+, npm, Git; internet for installation only.
- No GPU, model weights, paid account, cloud service, Redis or PostgreSQL.

## One-time install (repository root)
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
cd apps/web
npm install
cd ../..
```

On Windows PowerShell activate with `.venv\Scripts\Activate.ps1`.
The shell script below assumes `python` resolves to the installed environment.
For MSYS2/Git Bash, activate `.venv/Scripts/activate` where applicable.

## Start locally
```bash
bash scripts/dev.sh
```
Open http://127.0.0.1:3000 in the browser. Create a project, enter a prompt,
select the sole MOCK model, click Run mock generation, watch job progress and
download its text receipt. API docs: http://127.0.0.1:8000/docs.

If you prefer separate terminals, run:
```bash
python -m uvicorn services.api.main:app --host 127.0.0.1 --port 8000
# in another terminal
cd apps/web && npm run dev -- --hostname 127.0.0.1
```

The API automatically starts one local mock worker for dev. Do NOT simultaneously
launch the standalone worker against the same data directory from a second process.
For standalone/worker-unit experiments only: `python -m services.worker.mock`.
`VIDEOGEN_DATA_DIR` defaults to `.local/videogen` and holds a persistent
SQLite database and mock artifact files. This directory is local and ignored by Git.

## Verify CPU-only path
```bash
python scripts/check_docs.py
ruff check services integrations tests scripts/smoke_mock.py
pytest
python -m scripts.smoke_mock
cd apps/web
npm run typecheck && npm run lint && npm run test && npm run build
```

## Teardown
Press Ctrl+C to stop the launcher; the local SQLite records remain. Delete
`.local/videogen` **only if you intentionally want to erase all local projects,
jobs, provenance and mock receipts**. No external paid or GPU resources are started.

## HTTP boundaries and known limits
- API: `GET /v1/health`, `GET /v1/models`, `POST/GET /v1/projects`,
  `POST /v1/jobs`, `GET /v1/jobs/{id}`, `GET /v1/projects/{id}/jobs`,
  `GET /v1/jobs/{id}/events`, `GET /v1/artifacts/{id}`, and
  `GET /v1/artifacts/{id}/download`.
- POST jobs example fields: `project_id`, `model_id: mock-preview-v1`,
  `prompt`, `idempotency_key` (8–128 safe characters). Optional
  `simulate_failure: true` tests worker errors. Reusing a key with different
  input returns 409. No billing or model inference.
- One local development identity. **No authentication, role-based access,
  quota control, production retries, cancellation or multi-tenant isolation.**
  CORS is restricted to localhost browsers, but is NOT authentication.
  Never bind this application or ComfyUI to an external address.
- Failed/abandoned RUNNING jobs are marked `WORKER_LOST` when API restarts;
  queued jobs remain queued. SQLite is the M0 persistence choice.
- `NEXT_PUBLIC_API_URL` is a public, browser-visible config and must only
  contain the local API URL; never place secrets in it.
- Source-control policy: do not commit `.local/` data, model checkpoints,
  paid API credentials or user-uploaded private media.
- No real GPU test has been run. M1 will require engine/weight license gate
  and hardware preflight before a genuine PNG.
