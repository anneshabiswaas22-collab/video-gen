# Implementation validation — 2026-11-17

Scope: selective recovery of owned M0 source plus the first feature-owned typed
English practice integration. Tests were explicitly authorized after sorting.
These results are local; no GitHub-hosted CI result or public deployment is claimed.

Environment: Linux CPU, Python3.12.14, Node24.22.1, npm11.9.0, Playwright1.62.0
and system Chromium. Runtime/test versions and transitive locks are in the root
Python/npm manifests. All test data was synthetic and stored in temporary or
ignored paths; no learner recording, credential or model weight was added.

| Check | Outcome | What it establishes |
|---|---|---|
| `python -m pytest` in project venv | **51 PASSED**, 66 subtests; 0 failed/skipped | Recovered API/worker/adapter, authored coaching, local-model protocol, ownership/retention/replay/concurrency and HTTP boundaries |
| `ruff check` on owned Python | **PASSED** | Imports/static checks for service, integration, feature, tests and smoke tooling |
| CPU mock smoke | **PASSED** | Running API + SQLite + worker produces a real text receipt with explicit mock label |
| Live Node fetch test | **PASSED** | JavaScript HTTP client creates a job and verifies stored/downloaded artifact identity |
| `npm run typecheck` | **PASSED** | Shared and feature-owned React/TypeScript imports/contracts resolve |
| `npm run lint` | **PASSED** | Owned web entrypoints and external feature component rules |
| `npm test` | **15 PASSED**, 2 files; 0 failed/skipped | Shared creative helper and practice request/cookie/error/retry/deletion contracts |
| `npm run build` | **PASSED** | Next.js production build includes `/` and `/practice` |
| Browser smoke against dev servers | **PASSED** | Actual browser/API flow before review fixes |
| Browser smoke against fresh production servers | **PASSED** | Final code: correction/retry/Bangla/unknown/XSS text, cross-tab deletion recovery, saved restart/resume/delete, mobile width, mock receipt download and feature navigation |
| Python wheel resource inspection | **PASSED** | Feature modules and lesson JSON packaged; archived engines absent |
| `pip check` | **PASSED** | Installed Python dependency constraints are consistent |
| `pip-audit --local` after tooling fix | **No known vulnerabilities found** | Published dependency advisories; original local project is correctly skipped because it is not on PyPI |
| `npm audit --omit=dev --audit-level=high` | **0 known production vulnerabilities** | Registry advisory result at execution time, not a security certification |

The final production browser run used isolated API8003/web3004 and a fresh temporary
database; its processes were stopped afterward. Its Next build explicitly baked
that test API URL. Rebuild with the intended `NEXT_PUBLIC_API_URL` before any
later `next start`; the development launcher always sets the matching URL/origin.
Browser checks were headless, not a shared signed-in desktop session. Device
speech capability was inspected; no assertion was made that audio was heard.

## Diagnosed failures and review fixes

- Feature-owned React/Next imports originally could not resolve from a nested
  app-only install. Root npm workspaces and a single hoisted dependency graph
  now resolve them; typecheck/build/browser checks passed afterward.
- React lint rejected synchronous capability state set in an effect. The component
  now uses an SSR-safe external capability snapshot; no lint rule was disabled.
- A renewal regression test initially named the wrong pytest fixture; it was fixed,
  and the complete final51-test run has no failures/errors.
- The new virtualenv initially contained vulnerable pip25.0.1. It was upgraded to
  pinned26.2; repeat audit found no known vulnerabilities. Dependency verification
  was never disabled. Original project code remains outside PyPI advisory coverage.
- Independent review found owner-cookie lifetime, stale deleted-session UI and
  Swagger same-API-origin issues. Cookie renewal, safe already-deleted cleanup and
  same-origin access were repaired and covered by additional tests/browser flow.
- One non-failing Starlette deprecation warning remains: TestClient's HTTPX backend
  is being superseded by HTTPX2. Runtime requests and assertions completed; no
  warning or test failure was hidden. Migration can be evaluated separately.

## Unrun and unfinished gates

Real Ollama inference/model availability and semantic quality: **NOT RUN**.
Provider tests use HTTPX MockTransport and exercise request/response constraints,
not a real model. No model download, startup, paid API or GPU request occurred.

Teaching effectiveness and bilingual educator approval: **NOT RUN**. The finite
examples are developer-authored; unknown input is explicitly unsupported.

Speech recognition, microphone/camera capture, real-time avatar video/lip sync,
actual device voice intelligibility and interruptions: **NOT IMPLEMENTED/NOT RUN**.
The visible illustrations and optional speech controls do not prove these.

Genuine image/video/audio inference, core ComfyUI/custom-node compatibility,
continuity/movie outputs, public account isolation, production deployment/load,
external backups and fresh-machine snapshot restoration: **NOT RUN**.

Documentation and archived-byte checks are run before delivery and recorded below.
Earlier migration test reports remain dated historical observations, not tests of
this implementation. See [the next integrations](../development/IMPLEMENTATION_PROGRESS.md).

## Delivery preparation checks

- Locked Python installation/editable package refresh and `npm ci --ignore-scripts`
  completed successfully using the saved root locks.
- Documentation checker passed18 required entrypoints and relative links.
- Preservation checker passed: all2131 original imported blobs remain unchanged.
- The root npm cache is directed to ignored `.local/npm-cache` so installation
  works in this cloud filesystem as well as normal developer checkouts.
- Reusable environment install/start instructions were saved for the current
  app and tests. Saving does not publish or prove restoration in a new task.

The final delivery uses a normal direct-main commit/push and remote read-back.
The final chat/Git history identify its exact SHA; hosted CI results remain separate.

Next.js generated its managed app-level AGENTS guide during development; it is
retained. Installed framework guidance was consulted. The original recovered
`next-env.d.ts` is preserved as historical text, while the live generated file
is ignored and `next typegen` precedes typechecking for cold checkouts.
