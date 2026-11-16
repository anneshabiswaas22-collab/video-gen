# Issue #2 — dependency-ordered implementation checklist

Status is tied to branch `feat/m0-2-mock-studio` until PR merge. Code existence
is not proof of a tested release. **GPU is NOT REQUIRED for any M0 task.**

| Priority | Task / implementation paths | Depends on | Acceptance and test | GPU |
|---|---|---|---|---|
| P0 | Verify baseline and license boundaries; AGENTS, DECISIONS, TWO_REPO_DEEP_STUDY | None | Links/repo SHA recorded; source vs weights separated | No |
| P0 | Versioned typed contracts; services/api/contracts.py, packages/schemas/src/types.ts | Baseline | Request validation, OpenAPI and TS typecheck | No |
| P0 | Project/job SQLite persistence; services/api/storage.py | Contracts | Fresh DB, durable IDs, hash and idempotency 409 | No |
| P0 | Mock executor; services/worker/mock.py | Storage | QUEUED->RUNNING->SUCCEEDED/FAILED; isolated failure | No |
| P0 | FastAPI surface; services/api/main.py | Contracts/worker | Health/models/projects/jobs/artifacts/events tests | No |
| P0 | Original Next UI; apps/web/app, lib/api.ts | API | Project, prompt, submit, progress, history, receipt | No |
| P0 | Local install/launcher; docs/BUILD_RUN.md, scripts/dev.sh | API/web | New clone, one setup, mock workflow without secrets | No |
| P0 | CI: docs-check + application-ci | Tests/install | Python pytest/ruff, TS types/lint/test/build, audits | No |
| P0 | Contract tests; tests/, apps/web/lib/api.test.ts | API/web | Replay/conflict, failure, invalid model, artifact hash, CORS | No |
| P1 | ComfyUI HTTP MockTransport test; integrations/comfyui/adapter.py | Contracts | Only approved workflow; typed unavailable/cancel errors | No |
| P1 | Owner review, merge PR, update status | All passing and review | Green CI, reviewer approval; no auto merge | No |
| Next M0.1 | Commercial license review; docs/DEPENDENCY_REGISTER.csv | Source pin | Check every selected model weight/license and dependencies | No |
| Next M0.3 | Colab GPU preflight; existing notebook/script | Owner Colab session | Actual GPU/VRAM/disk logs; no guessed hardware | **Real GPU session** |
| Later M1 | First real PNG in approved ComfyUI workflow | M0 + licenses + preflight | Decode PNG, SHA, timing and VRAM measured | Yes |
| Later M2 | First real Wan MP4 | M1 + model fit | Decode frames/fps/codec, SHA, OOM evidence | Yes |

### Architecture mapping

`Browser (Next.js)` -> `FastAPI v1` -> `SQLite project/jobs/events` ->
`local mock worker` -> `plain text mock artifact`.

Later, the worker will call an allowlisted `integrations/comfyui` adapter
over a private authenticated network, and copy validated media bytes to an
object-store adapter. In M0 the in-process mock worker is a local development
convenience. The separate worker entrypoint exists, but multi-process reliable
scheduling and retries are **not** completed.

### Acceptance classification

- **PASSED**: [application CI run 43741158859](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741158859) at `70dba92d1f8fc32b4f4064e0f919976566fa66fc`: Python lint, 7 pytest tests, isolated mock smoke, JS client/live API roundtrip, pip audit, TS typecheck, ESLint, Vitest, Next production build and npm production audit.
- **PASSED**: documentation integrity [run 43741109382](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741109382).
- Fresh clone manual test on owner Windows machine remains **NOT RUN**; npm transitive lockfile not yet committed (direct dependencies pinned).
- Real image generation: NOT RUN.
- Real video generation: NOT RUN.
- Real audio generation: NOT RUN.
- Real Colab hardware preflight: NOT RUN.
- User/tenant authorization, paid quotas and secure public hosting: NOT IMPLEMENTED.
