# Run the recovered studio and English companion

This implementation supersedes the earlier documentation-only setup notes below.
It is a local CPU prototype; neither server is intended for public deployment.
Use the existing checkout rather than creating a worktree.

## Install (Linux / WSL, Python 3.11+, Node 22+)

From the repository root:

```sh
python -m venv .venv
.venv/bin/python -m pip install --upgrade pip==26.2
.venv/bin/python -m pip install -r requirements-dev.lock
.venv/bin/python -m pip install --no-deps -e .
npm ci --ignore-scripts --no-fund
npm run dev
```

The root Python package maps `english_friend` to its feature-owned backend and
includes `lessons.json`; root npm workspaces share React/Next between entrypoints
and feature components. Locks pin the tested Python development environment and
npm dependency graph. No archived engine, checkpoint or paid provider is installed.

The launcher uses `.venv/bin/python`, loopback API port8001 and web port3000.
Open the local web interface and choose English friend (`/practice`) or use the
creative studio. A mock job returns a text receipt, never generated media.
Shell variables `VIDEOGEN_API_PORT` and `VIDEOGEN_WEB_PORT` override ports; the
launcher sets the matching API URL and CORS web origin. It checks API readiness
and stops both processes when either exits. Stop with Ctrl-C.

For a port conflict, for example:

```sh
VIDEOGEN_WEB_PORT=3002 npm run dev
```

Data defaults to ignored `.local/videogen/`; export `VIDEOGEN_DATA_DIR` for an
isolated location. `.env.example` is documentation, not an automatically sourced
shell file. Export needed variables explicitly. Do not commit data or secrets.

## Optional existing local AI model

Built-in practice works without model credentials. To use a model you already
installed and started on loopback:

```sh
export VIDEOGEN_COACH_PROVIDER=ollama
export OLLAMA_BASE_URL=http://127.0.0.1:11434
export OLLAMA_MODEL=YOUR_EXISTING_LOCAL_MODEL
npm run dev
```

The app never installs or starts a model. It rejects remote URLs and redirects,
uses bounded structured output and displays explicit errors without switching
providers silently. Configuration is not proof of model readiness or quality.
No real model was queried in this delivery. Review model rights/hardware/costs
before selecting or downloading weights. No paid-service use is authorized here.

## Verification commands

```sh
.venv/bin/python -m pytest
.venv/bin/ruff check services integrations tests features/english-speaking-friend/backend features/english-speaking-friend/tests scripts/development/smoke_mock.py
.venv/bin/python -m scripts.development.smoke_mock
npm run typecheck
npm run lint
npm test
npm run build
npm audit --omit=dev --audit-level=high
.venv/bin/python -m pip_audit --local
python scripts/maintenance/check_docs.py
python scripts/maintenance/check_structure.py
```

Run the live JavaScript contract test while the API is running:
`node apps/web/test/live-api.mjs` (defaults to loopback8001).

For browser tests, install the optional tool with
`.venv/bin/python -m pip install -e '.[browser]'`, then use Playwright's supported
Chromium install or an existing system Chromium. Start both servers with a fresh
`VIDEOGEN_DATA_DIR` so tests do not alter personal projects/practice. Then:

```sh
VIDEOGEN_TEST_WEB_URL=http://127.0.0.1:3002 \
VIDEOGEN_BROWSER_EXECUTABLE=/usr/bin/chromium \
.venv/bin/python tests/browser/smoke.py
```

Omit the executable variable when using Playwright's bundled browser. Browser
artifacts default to ignored `.local/browser/`. Test-generated projects use unique
names; the practice sessions they create are deleted. Audio playback availability
is checked, but no claim is made that a voice was heard or recording works.

[Current evidence](../quality/IMPLEMENTATION_VALIDATION.md) distinguishes real CPU
execution, mocked provider protocol and unrun model/hardware checks.

## Historical setup records (preserved)

# Path migration and current execution policy

Read [PROJECT_STRUCTURE.md](../../PROJECT_STRUCTURE.md) for current homes.
**No tests, compilation, installs or application startup were run in the current
functional restructuring pass, per owner instruction.** Commands below are for
a later explicitly authorized validation session. Existing earlier results do
not verify these moved paths. Moved ignored Python venv launcher/activation
scripts may still reference their previous absolute path; recreate the venv
when runtime work resumes. The archived reference gallery now has its original
index and118 app folders, but162 indexed MP4s remain missing.

# Current setup and validation — 2026-11-17

Use the existing isolated checkout; do not create a worktree unless requested.
There is no owned VideoGen or tutor application to deploy in this checkout.
The [feature map](../../features/README.md) and [inventory](../../AnalyseFuture/analysis/FEATURE_INVENTORY.txt)
separate plans from preserved reference implementations.

From the repository root, run `python scripts/maintenance/check_docs.py`,
`python scripts/maintenance/check_structure.py`, and
`python -m py_compile scripts/hardware/gpu_preflight.py scripts/maintenance/check_docs.py scripts/maintenance/check_structure.py`.
These checks need only the Python standard library (Python 3.12 validated).

For an explicitly scoped reference-development task, use
`AnalyseFuture/references/workflow-studio/freefield/` (Node 24.22.1 validated; its declared
minimum is Node 22.6). Run `npm ci --ignore-scripts --no-audit --no-fund`,
`npm run validate`, `npm run typecheck`, and `npm test`. This package has no
build step; Node executes TypeScript directly. Its manifest/workflow tests do
not prove real generation. Do not run upstream installers automatically.

Optional reference server: from that same directory run
`FREEFIELD_HOST=127.0.0.1 PORT=3000 npm run serve`. Check the UI returns HTML,
`/api/apps` returns 120 entries, `/api/history` returns JSON and `/api/gpu`
reports no configured backend when `COMFY_BASE_URL` is absent. Use local requests;
do not expose the unconfigured reference as the owned product. Live processes
must restart after moves or in a new task. Keep the reference server loopback-only.

Optional Python reference checks use its ignored `.venv`:
`python -m venv .venv`, then `.venv/bin/python -m pip install aiohttp==3.14.4`,
`.venv/bin/python test/gateway_test.py`, and
`.venv/bin/python test/import_workflow_test.py`.
After relocation, recreate venv launcher scripts; do not rely on old absolute paths.
No real secrets or inference backend are required for these fake-backend tests.

Archived code is excluded from the active product by explicit paths and the
absence of any root package/workspace/import/deploy linkage. This is not an OS
sandbox: manual execution is still possible and requires review. GPU inference,
model downloads, custom-node installation and paid provider use are separate,
owner-approved tasks. [Validation evidence](../../AnalyseFuture/migration-history/TEST_AND_VALIDATION_REPORT.txt)
records what actually ran.

## Historical build brief (preserved)

# Build, run and verify — current state

**As of 2026-11-13, this is a documentation-first repository.** There is no application or working inference backend yet. Running "npm start" or "python generate.py" in the root would be misleading. See M0 in ROADMAP.md for scaffold requirements.

## Today
- Read the docs in order from docs/README.md.
- Check open issues and assign a bounded milestone task.
- Verify candidate upstream repos at their official URLs in OPEN_SOURCE_STACK.md before integrating.
- Do not download model weights, install many unrelated runtimes, or use GPU time until a small, reproducible job is defined.

## M0 expected development commands (not implemented)
Future scaffold should provide:
- one documented command to install web dependencies;
- one documented command to create a Python venv and install the API;
- one command to start a mock worker and API;
- one command to run unit/static tests;
- a separate hardware-gated Colab notebook with preflight/real generation.

These commands become copy/paste instructions **only after Codex creates and verifies them**, not before.

## Suggested environment variables (names only; do not commit values)
DATABASE_URL, OBJECT_STORAGE_ENDPOINT, OBJECT_STORAGE_BUCKET, WORKER_BACKEND, COMFYUI_BASE_URL, MODEL_CACHE_DIR, API_SECRET_KEY, MAX_CONCURRENT_GPU_JOBS, PROVIDER_API_KEY (optional only).

## Security
No secrets or access tokens in GitHub commits or notebook outputs. Access to deployed job endpoints must require auth; arbitrary workflow uploads forbidden by default. Avoid free Colab server tunneling against platform terms.

## Test labels
- CPU PASS: mock/local tests executed without real generation.
- GPU PASS: real generation with file verified and hardware recorded.
- NOT RUN: test unavailable in this environment.
- BLOCKED: explicit reproducible error, not silently ignored.
