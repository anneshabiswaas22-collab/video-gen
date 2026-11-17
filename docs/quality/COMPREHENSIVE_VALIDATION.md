# Comprehensive validation and hardening

**Final result: PASSED — 24 required check groups, no failed/blocked group.**
Run completed **2026-11-17 at 12:26:57 IST**. This validates the owned working-tree
changes delivered with this report, based on commit `53aae94`, followed only by
documentation/evidence updates. It does not claim hosted CI or a deployed release.

The portable [machine-readable evidence](evidence/2026-11-17-cpu-verification.json)
records exact outcomes, counts, source baseline and SHA-256 digests of the tested
owned executable/configuration files. This report and
[PROJECT_HANDOFF.md](../../PROJECT_HANDOFF.md) are the continuation entrypoints.
No GitHub issues were created. The 104 remaining task IDs are local documentation.

## What ran and what the result establishes

| Check | Result | Evidence / boundary |
|---|---|---|
| Owned Python unit/integration/adversarial suite | **155 passed; 66 subtests passed** | 0 failed, 0 skipped. JUnit reports 221 entries including those subtests; do not add them a second time. |
| Python dependency consistency and lint | **PASSED** | `pip check`; Ruff over owned services, integrations, tests, English backend/tests, development/quality/maintenance scripts. |
| CPU mock end-to-end smoke | **PASSED** | Durable project/job lifecycle and genuine downloadable mock text receipt, not media generation. |
| Source preservation and guide coverage | **PASSED** | All 2,131 original imported blobs unchanged; 2,291 source files and 570 directories accounted for. |
| Documentation links/required entrypoints | **PASSED** | 22 required documents and relative Markdown links. External link availability is a separate check. |
| npm dependency graph | **PASSED** | Clean `npm ci --ignore-scripts --no-fund`, followed by `npm ls --all`. Platform-specific unneeded optional packages are not missing required dependencies. |
| TypeScript, frontend lint and HTTP clients | **PASSED; 27 frontend tests** | No failed/pending frontend case; successful response shapes and safe errors are checked. |
| Python package vulnerability audit | **PASSED** | No known dependency vulnerabilities found. Owned unpublished package is skipped by the advisory service, not security-certified. |
| npm production and full development audits | **PASSED; 0 vulnerabilities reported** | Production high threshold and full moderate threshold. Advisory results are a dated snapshot, not a permanent guarantee. |
| Wheel build and contents | **PASSED** | Feature backend, lessons and shared service modules packaged; archive/database payloads excluded. |
| Preserved FreeField validation/typecheck/tests | **PASSED; 50 Node tests** | 120 manifests checked. Importer checks and fake-backend gateway relinking also passed. These are reference checks, not 120 completed owned features. |
| Production Next.js build | **PASSED** | Built `/` and `/practice` using the isolated test API URL. |
| Live Node → API contract | **PASSED** | Real API/SQLite/mock-worker requests rather than a frontend transport stub. |
| Production Chromium smoke | **PASSED** | Practice correction/retry/Bangla/unknown-text handling, saved resume/delete, navigation, mobile layout and mock receipt. |
| Production Chromium regression | **PASSED** | 30 grouped assertions across 320/390/768/1440 widths; malformed 200 response recovery, dropped-response replay, quota/clear-all recovery, cross-browser ownership, keyboard navigation and project switching. |

## Defects reproduced and repaired

New adversarial and creative regressions first reproduced **37 failures** before
the fixes. Those regression modules and the expanded combined suite now pass.

| Area / functional home | Repair and practical result |
|---|---|
| Practice lifecycle — `features/english-speaking-friend/backend/english_friend/` | A cancelled request or database failure marks an indeterminate key interrupted without leaving a permanently pending quota slot. Expiry while a provider is running purges session data before finishing. Deleted/expired sessions cannot be revived by a late result. |
| Practice privacy and recovery — backend + feature web | Added owner-scoped `DELETE /v1/english/sessions` and a confirmed “Delete all practice data” control. This clears saved sessions and default metadata left after lost pages; another browser owner is unaffected. |
| Creative state — `services/api/storage.py` | Enable SQLite foreign keys, claim tasks deterministically, serialize transitions, require monotonic running progress, and prevent stale workers completing terminal jobs. Completion uses stored task provenance rather than a caller's mutable copy. |
| Receipt writes/downloads — `services/api/` | Failed writes/transactions clean their newly generated partial receipt files. Download opens a regular file without following symlinks on the tested Linux runtime and verifies size/SHA-256 before serving the same verified bytes. Missing/tampered results fail safely. |
| Worker resilience — `services/worker/` | Transient SQLite/filesystem faults do not permanently terminate the polling loop. Worker supervision, readiness, explicit migrations and full power-loss recovery remain backlog items. |
| Engine boundary — `integrations/comfyui/` | Snapshot the approved graph; reject invalid graph/response data, oversized replies, malformed prompt IDs and node errors; do not follow redirects. Tests simulate the HTTP engine, not real inference. |
| Teaching provider — English backend | Reject duplicate JSON keys and missing/false completion markers, in addition to the existing loopback, size, schema and safe-error constraints. This does not establish semantic teaching quality. |
| Browser contract/UI — feature web + `apps/web/` | Validate successful practice response shapes, show recovery errors for malformed payloads, preserve idempotent replay after a lost reply, avoid displaying delayed history from a previous project and stop polling terminal jobs. |
| Test tooling — workspace manifests/lock | Replaced vulnerable Vitest 3.x with explicitly pinned Vitest 5.1.0 and its resolved graph; converted its config to `.mts`. A clean locked reinstall fixed leftover conflicting optional packages. No forced audit rewrite or disabled assertion was used. |

## Reproduce and inspect

Follow [BUILD_RUN.md](../operations/BUILD_RUN.md) for locked dependencies and the
optional browser/reference prerequisites. From the repository root:

```sh
npm run verify
```

The runner preserves each exit status, continues independent checks after a failure,
uses temporary synthetic data, owns its test child processes, and writes a unique
directory under ignored `.local/verification/`. It uses ports 8021/3021 by default,
rejects occupied ports and accepts explicit port overrides. Browser tests never
belong on private/shared data. Reduced-scope flags are explicitly reported as
NOT RUN and `PASSED_REDUCED_SCOPE`.

Final raw run ID: `20261117T065618Z-a697c35d`. Local-only logs/screenshots are under
`/tmp/videogen-combined-verification/<run-id>/`; these paths will not survive every
future task. The portable JSON above retains the important results in Git.
The final combined execution took **38.765 seconds** with dependencies already
installed; this is not a claim of two hours of execution or two hours of load testing.
Earlier iterations and defect diagnosis are separate from that measured run.

After verification, the production build contains its test API address. Use
`npm run dev` for normal development or rebuild with the intended `NEXT_PUBLIC_API_URL`
before serving a production build.

## Warnings and checks not performed

- Starlette's TestClient emits an HTTPX-to-HTTPX2 deprecation warning. The tests pass;
  the warning remains visible. Migration should be evaluated with the framework's
  compatible versions, rather than suppressing it or forcing an unrelated upgrade.
- `pip-audit` disabled its unwritable default cache and completed successfully. It
  skips only the unpublished owned package, whose source is checked locally.
- **Real Ollama inference and teaching quality: NOT RUN.** No model was downloaded,
  started or queried. Exact model rights, named hardware and human evaluation remain gates.
- **GPU/ComfyUI inference and full archived engine/custom-node suites: NOT RUN.**
  Torch, required engine/model dependencies, approved weights and GPU hardware are
  unavailable here. A tested adapter or preserved architecture is not a generated image/video.
- **Actual heard speech, microphone/camera capture, lip sync and learning efficacy:
  NOT VERIFIED.** Browser speech controls are present; ASR/live video are future work.
- **Windows, execution on Python 3.11, hosted CI and production deployment: NOT RUN
  in this pass.** Current execution used Linux, Python 3.12 and Node 24.22.1. CI
  definitions include Python 3.11/Node 22, but definitions do not prove a hosted run.
- **Full security certification and production accounts: NOT COMPLETE.** Creative
  routes remain localhost/single-user. SQLite/file completion is not a distributed
  power-loss transaction. Cleanup is operation-triggered; backups/vendor deletion
  and public tenant isolation require the handoff tasks.
- The reference gallery retains **162 missing indexed MP4s** documented during
  recovery; no absent original media was fabricated or deleted.
- **Continuous PR monitoring: NOT RUN.** Future tools submit scoped PRs; review and
  authorized merges happen when requested or through a separately configured service.
