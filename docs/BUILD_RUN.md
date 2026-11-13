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
