# Latest implementation milestone — 2026-11-17

The owner now authorized coding and tests. Original M0 source at
`ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37` was fetched and selectively recovered;
[provenance](../repository/RECOVERED_APPLICATION_SOURCE.json) records each source blob.
The working foundation is extended with the feature-owned English practice
backend, optional local-model protocol, cookie/consent/session lifecycle and UI.
See [current progress](../development/IMPLEMENTATION_PROGRESS.md),
[setup](../operations/BUILD_RUN.md) and
[validation evidence](../quality/IMPLEMENTATION_VALIDATION.md).

The built-in engine is a finite phrase set; real model/voice/GPU quality and
production readiness remain unverified. Earlier “no owned code” and “no tests”
statements below describe their dated recovery/sorting snapshots, not this milestone.

## Earlier project memory (preserved)

# Latest repository structure — 2026-11-17

The owner requested a complete functional sorting pass without tests. See
[PROJECT_STRUCTURE.md](../../PROJECT_STRUCTURE.md), the
[file-placement ledger](../repository/FILE_PLACEMENT.json) and
[current reorganization record](../repository/FUNCTIONAL_REORGANIZATION.md).
All2206 starting tracked files are accounted for. Shared docs and utilities have
actual functional homes; full source packages remain internally coherent. The
English companion's detailed idea remains unchanged in its feature.
Earlier test results below are historical and were not rerun for this structure.

> **Current repository update — 2026-11-17 (Asia/Kolkata):** The working origin is
> `sarfiaroui-oss/video-gen`. The owner explicitly combined the creative studio
> with an English-speaking AI friend. See [feature folders](../../features/README.md),
> [combined idea](../product/PROJECT_IDEA.txt), and [recovery report](../repository/REPOSITORY_REORGANIZATION.md).
> All 2,131 files introduced at `f34553a` are preserved under `AnalyseFuture/`.
> This checkout contains no owned web/API/tutor implementation. The PR #8 and CI
> evidence below belongs to the historical source repository; it is preserved,
> not claimed as current code. Current validation lives in
> [TEST_AND_VALIDATION_REPORT.txt](../../AnalyseFuture/migration-history/TEST_AND_VALIDATION_REPORT.txt).

# VideoGen — CANONICAL PROJECT MEMORY / START HERE

**Last comprehensive handoff snapshot:** 2026-11-16 (Asia/Kolkata).  
**Source of truth:** [VideoGen repository](https://github.com/anneshabiswaas22-collab/video-gen).  
**Audience:** any human developer, ChatGPT session, GPT-6 Astra/Codex agent, reviewer or new contributor.  
**Read this file first whenever the original chat is inaccessible.** This is a durable *engineering handoff*, not a verbatim or complete export of all past private chats.

> **IMPORTANT CURRENT STATE:** On 2026-11-16, `main` is the documentation-first branch at `2a88181dc0408f6477dd52a6ed8ded762f149bcd`. A real CPU-only mock vertical slice lives in **[PR #8](https://github.com/anneshabiswaas22-collab/video-gen/pull/8)**, branch `feat/m0-2-mock-studio`, commit `ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37`. GitHub Actions [application CI](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390592) and [documentation CI](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390571) both passed for this commit. **PR #8 was open, ready for review, cleanly mergeable, but not merged** at the time of the snapshot. Recheck GitHub live before acting; this snapshot can become stale.

## What we are building

Build **VideoGen, an original, ownable, commercially viable AI Creative Studio** with integrated image generation/editing, short-form video, voice/speech, sound/music, post-production, controllable cinematic shots, persistent characters/environments, reshoots, and eventually an editable multi-shot movie pipeline. Compare *user experience* with Higgsfield, Runway, Google Flow and Kling; they are **benchmarks, not freely available source code**. Never claim to outperform them without measured tests.

Owner priorities: save GPT/Codex credits; reuse maintained legally compatible libraries instead of rewriting inference engines; start locally with CPU mocks; use owner-controlled Colab GPU for **interactive testing** once verified; no unapproved paid APIs, GPU rental, giant model downloads, or unlicensed third-party code/weights. Own the product identity, UI, API, project/job data model and distinctive movie workflow.

Primary differentiation: **stable character identity across shots**, editable scene/shot/take history, explicit camera/motion controls when the active model supports them, human-approved AI director, cost/quality transparency, individually regenerable shots, long-form assembly with FFmpeg rather than single-prompt 120-minute generation.

This is a general-purpose software platform; the separately discussed 3D animated American-English-learning family channel can be a **future integration/stress test**, but its scripts, assets, characters and other repositories are NOT to be copied or modified here without explicit scope.

## Exact primary research foundations (TWO)

1. **[ComfyUI](https://github.com/Comfy-Org/ComfyUI)** — managed external inference/workflow engine. Source code inspected at `258f880d0c026bfc22acab679858ab2e2c70573d`; source LICENSE GPL-3.0. Integrate by a typed private HTTP/WS adapter; no wholesale vendoring. Commercial distribution/integration effects and every model weight license remain separate legal gates.
2. **[FreeField](https://github.com/neuregex/freefield)** — MIT-licensed *source-code* reference for app manifests, workflow bindings, model packs, generated UI, results history, GPU laboratory and validation. Inspected at `f0c2358a46c7008ff8503d4324b6cc8bc7657e75`. Don't fork or copy its whole UI/branding; build our own VideoGen manifest system. Every external media asset, checkpoint, custom node and workflow must be checked independently.

Historical research catalog: **[54 recommended repositories](../research/ALL_RECOMMENDED_REPOSITORIES.txt)**. They are *candidates*, not 54 approved runtime dependencies. The historical list reported 53/54 URLs resolving on 2026-11-15, with Montagio unavailable; URL existence is not safety/commercial permission. Detailed study: [two-repository audit on the PR branch](https://github.com/anneshabiswaas22-collab/video-gen/blob/ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37/docs/TWO_REPO_DEEP_STUDY.md).

## Architecture and verified code boundaries

```text
Next.js / React / TS / Tailwind (owned VideoGen Studio UI)
       |
FastAPI / Pydantic v1 API (owned; auth/quota future)
       |
Job orchestration + persistent projects/jobs/events/artifact provenance
       |
CPU mock worker (M0)  →  ComfyUI adapter / real private GPU worker (M1+)
       |                         |
SQLite + local text receipts      Pinned workflow -> selected licensed model
(M0 dev only)                     | -> verified media -> durable storage
       |
Later: FFmpeg, speech, storyboards, character bible, editable scene/shot/timeline
```

Proposed monorepo: `apps/web/`, `services/api/`, `services/worker/`, `packages/schemas/`, `integrations/comfyui/`, `integrations/media/`, `workflows/`, `notebooks/colab/`, `tests/`, `infra/`, `scripts/`, `docs/`, `.github/workflows/`. These are *intended boundaries*, not a claim every folder has working code on main.

PR #8 implements: Next.js project/prompt/model/job/history screen; FastAPI `/v1/health`, `/v1/models`, `/v1/projects`, `/v1/projects/{id}`, `/v1/jobs`, `/v1/jobs/{id}`, plus list/history/artifacts routes; Pydantic models; SQLite status persistence; idempotent job creation; worker transitions `QUEUED → RUNNING → SUCCEEDED | FAILED`, marked `text/plain` mock artifact (SHA-256); ComfyUI typed adapter *stub* with simulated HTTP transport. The mock job returns a **receipt**, NOT an AI image/video. It has **no authentication or production tenant isolation** and must only be bound to localhost.

**CI evidence:** seven Python API/adapter tests passed, Python lint, CPU smoke, real Node fetch → running FastAPI → worker → artifact round trip, Python audit, frontend typecheck/lint/tests/production build, npm audit, and docs integrity all passed. No real GPU, genuine PNG/MP4/WAV or owner-Windows fresh-clone proof was executed. Exact final commit `ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37`.

## Roadmap / gates, in dependency order

| Stage | Outcome | Status at snapshot |
|---|---|---|
| M0.1 / [#1](https://github.com/anneshabiswaas22-collab/video-gen/issues/1) | Code + weights + commercial/license gate | PENDING |
| M0.2 / [#2](https://github.com/anneshabiswaas22-collab/video-gen/issues/2) | Original web/API/SQLite/mock worker/CI | **IMPLEMENTED ON UNMERGED PR #8**, CI PASSED |
| M0.3 / [#3](https://github.com/anneshabiswaas22-collab/video-gen/issues/3) | Real Colab GPU/VRAM/RAM/disk preflight | PENDING hardware validation |
| M1 / [#4](https://github.com/anneshabiswaas22-collab/video-gen/issues/4) | One genuine licensed checkpoint → verified PNG | NOT RUN |
| M2 / [#5](https://github.com/anneshabiswaas22-collab/video-gen/issues/5) | Real Wan-compatible short MP4, measured frames/codec/VRAM | NOT RUN |
| M3 / [#6](https://github.com/anneshabiswaas22-collab/video-gen/issues/6) | Kokoro speech, subtitles, FFmpeg assembly | NOT RUN |
| M4 | Usable multi-modality studio, preview, asset library | PLANNED |
| M5 / [#7](https://github.com/anneshabiswaas22-collab/video-gen/issues/7) | Versioned character/scene/shot/take/movie timeline; 60-second proof | PLANNED |
| M6 | Benchmark quality/VRAM/latency/cost; LightX2V comparison | PLANNED |
| M7 | Auth/tenant boundaries, quotas, deployment, billing, legal release gates | PLANNED |

The first *genuine* model must be chosen **after** the actual GPU hardware preflight. Wan2.2 is the preferred *video candidate*, NOT an approved fixed 5B/14B checkpoint. For images, FLUX or Qwen variants require precise weight-license and GPU verification. Audio candidate Kokoro. Media assembly FFmpeg. No production Colab web hosting.

## Five immutable engineering rules

1. **Never confuse implemented, CPU MOCK TESTED, GPU VERIFIED, deployed and planned**. Status must have a test/commit/artifact link.
2. **Inspect latest GitHub state and existing AGENTS.md / ADR first**, then branch or use PR as appropriate; do not overwrite PR #8 or erase history.
3. **Choose REUSE vs BUILD** only after license, model-weight, VRAM, maintenance, security and version assessment. No automatic cloning/copying all 54 repositories.
4. **Budget/security:** no paid APIs or GPUs without approval; no model weights/secrets/PII in Git; no arbitrary executable ComfyUI graphs; no unauthenticated public GPU/worker endpoints.
5. **Finish working narrow vertical slices with tests**, docs, CI, evidence and a clear PR rather than a fancy inactive UI or overengineered roadmap.

## Quick resume instructions for next agent

- Open the latest default branch and [open PRs](https://github.com/anneshabiswaas22-collab/video-gen/pulls); check whether [PR #8](https://github.com/anneshabiswaas22-collab/video-gen/pull/8) merged since this document.
- Read [AGENTS.md](../../AGENTS.md), [architecture](../architecture/ARCHITECTURE.md), [decisions](../architecture/DECISIONS.md), [existing project history](PROJECT_HISTORY.md), and the [complete continuity bundle](README.md).
- If PR #8 unmerged, **review it rather than build a second M0**. Do not merge without owner/reviewer instructions. Run CI and a fresh clone test.
- Then handle [license issue #1](https://github.com/anneshabiswaas22-collab/video-gen/issues/1) and [Colab preflight #3](https://github.com/anneshabiswaas22-collab/video-gen/issues/3); only then plan genuine inference milestone M1.
- Every future PR must update this memory bundle and [verification snapshot](STATE_EVIDENCE_AND_OPEN_ISSUES.md) with live commit/PR/CI results, unresolved blockers, and exact next step.

## Documents in this continuity bundle

- [Memory index and reading order](README.md)
- [Canonical scope, requirements, detailed roadmap and architecture](PROJECT_CANONICAL_HANDOFF.md)
- [Past-conversation summary, chronology and decisions](CONVERSATION_AND_DECISION_HISTORY.md)
- [Architecture, job, GPU, continuity and roadmap charts](ARCHITECTURE_AND_WORKFLOW_DIAGRAMS.md)
- [All core research links and 54-repo catalog](SOURCE_AND_REPOSITORY_LINKS.md)
- [Verified state, PR, issues, tests and gaps](STATE_EVIDENCE_AND_OPEN_ISSUES.md)
- [Exact continuation prompt + developer workflow](DEVELOPER_CONTINUATION_GUIDE.md)
- [Updating project memory after each change](MAINTENANCE_PROTOCOL.md)

**Scope and honesty:** Some older conversations are unavailable verbatim. This archive preserves their accessible, relevant *decisions and project facts*, not a fabricated full conversation transcript. The current GitHub repo and PR are the authoritative technical record; the next agent should refresh statuses from live GitHub.

## One-file portable handoff

For new ChatGPT/Codex chats that cannot browse GitHub, upload the
[VIDEOGEN_ONE_FILE_HANDOFF.txt](VIDEOGEN_ONE_FILE_HANDOFF.txt)
file. It includes the complete canonical specification, history, architecture
diagrams, 54-repository links, CI evidence and reusable continuation prompt.
It is a repository knowledge snapshot, **not** a verbatim export of chats that
were not available to the assistant.
