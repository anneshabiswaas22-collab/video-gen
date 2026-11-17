> **Start here:** [Complete project handoff, implemented features and 104 ordered remaining tasks](PROJECT_HANDOFF.md).
> Other AI tools should take one ready task on a branch and submit a PR for review. No GitHub issues are being created.

# VideoGen — Creative Studio + English Friend

A local development application with two working paths:

- **Creative foundation:** projects, durable jobs, progress/history and downloadable
  CPU mock receipts. Receipts are text, not generated images or videos.
- **English practice:** three scenarios, 18 authored English/Bangla practice cases,
  gentle suggestions and retries, two illustrated characters, optional browser
  speech, and opt-in saved sessions with resume/delete.

Built-in phrase practice is a limited authored set, not general AI correction or
translation. An optional Ollama adapter can use an already running local model;
its protocol is tested, but no real model or learning quality has been verified.
Microphone input, live avatar video and GPU media generation remain future work.

## Run locally (Linux / WSL)

Use Node 22.12+, 24.x or 26+ (see `package.json`) and Python 3.11+ from the existing checkout:

```sh
python -m venv .venv
.venv/bin/python -m pip install --upgrade pip==26.2
.venv/bin/python -m pip install -r requirements-dev.lock
.venv/bin/python -m pip install --no-deps -e .
npm ci --ignore-scripts --no-fund
npm run dev
```

The launcher binds the API to loopback port 8001 and the web interface to port
3000. `/practice` opens the English companion. Set `VIDEOGEN_WEB_PORT` or
`VIDEOGEN_API_PORT` if needed. This is a single-machine prototype; the creative
API has no production account system. Keep it bound to localhost.

See [setup and execution](docs/operations/BUILD_RUN.md),
[implementation and remaining work](docs/development/IMPLEMENTATION_PROGRESS.md)
and [API contracts](docs/architecture/API_CONTRACT.md).

## Functional organization

| Collection | Contents |
|---|---|
| `apps/web/` | Next.js entrypoints and recovered creative studio |
| `services/api/`, `services/worker/` | Shared API, SQLite job state and CPU mock worker |
| `features/english-speaking-friend/` | Feature-owned coaching, local-model adapter, API/storage, UI and tests |
| `integrations/comfyui/` | Tested allowlisted adapter boundary; real inference not wired |
| `packages/schemas/` | Shared typed creative contracts |
| `docs/`, `scripts/`, `notebooks/` | Product knowledge, commands, maintenance and hardware research |
| `AnalyseFuture/` | Preserved external engines, examples and historical evidence; no automatic execution |

[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) explains each home. The
[original placement ledger](docs/repository/FILE_PLACEMENT.json) and
[recovered-source record](docs/repository/RECOVERED_APPLICATION_SOURCE.json)
preserve provenance. Historical M0 code was recovered from the exact earlier
revision rather than replaced with a second implementation. All 2,131 original
imported files remain unchanged.

## Tests

Run the combined checks, including production browser flows, from the repository root:

```sh
npm run verify
```

See [the setup guide](docs/operations/BUILD_RUN.md) for browser/reference prerequisites
and explicit reduced-scope options. Results and individual logs are saved under
ignored `.local/verification/`. The verifier uses isolated synthetic data and stops
the test servers it starts. Individual checks remain available:

```sh
.venv/bin/python -m pytest
.venv/bin/ruff check services integrations tests features/english-speaking-friend/backend features/english-speaking-friend/tests scripts/development/smoke_mock.py
.venv/bin/python -m scripts.development.smoke_mock
npm run typecheck
npm run lint
npm test
npm run build
python scripts/maintenance/check_docs.py
python scripts/maintenance/check_structure.py
```

Browser instructions and current outcomes are in
[COMPREHENSIVE_VALIDATION.md](docs/quality/COMPREHENSIVE_VALIDATION.md). Tests
are now authorized; earlier no-test sorting reports remain historical.

The [combined idea](docs/product/PROJECT_IDEA.txt),
[detailed English companion idea](features/english-speaking-friend/PROJECT_IDEA.txt)
and [future roadmap](docs/product/FUTURE_ROADMAP.txt) remain intact. Source,
weight, voice and media rights require separate review. No paid APIs, model
weights, training or GPU rental were used for this milestone.
