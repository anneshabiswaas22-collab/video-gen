# VideoGen — complete canonical product and engineering handoff

**Recorded:** 2026-11-16. Read [PROJECT_MEMORY.md](../../PROJECT_MEMORY.md) first. This document is intended to answer **what, why, how, current state, and next action** without an old chat.

## 1. Mission, owner requirements and position

**Mission:** Build one original commercial AI Creative Studio covering image generation/editing, video generation, audio/voice/music, media finishing, controllable cinematic shots, reusable characters/environments and eventually coherent editable movies. Target individual creators, YouTubers, filmmakers, independent studios and later API users. UX benchmarks: Higgsfield, Runway, Google Flow and Kling. Do NOT copy proprietary product visuals, logos, APIs or model weights, and do not claim #1 or quality parity without fair measurements.

Owner wants a software business whose users can self-serve, rather than labor-intensive client-service engagements. Product should be approachable and credible, with future free/premium or other sustainable monetization only after real compute costs, consent and commercial rights are understood. **M0 does not implement billing, subscriptions, ads, hosting or pricing.** The current engineering task is not a speculative business redesign.

The owner can collaborate with GPT-6 Astra/Codex Cloud and has access to an interactive Google Colab GPU, but the actual device class, VRAM, storage and quota are UNKNOWN. Keep runtime requirements explicit. Free Colab and Kaggle are *experimentation platforms*, not unlimited reliable public production capacity. No unapproved paid APIs, GPU rental or bulk checkpoint download.

## 2. Exact product feature pillars

**Image Studio:** prompt-to-image, image-to-image, image edit/inpaint/outpaint, masks, aspect extension, background/object handling, upscaling, presets, references and image versions. Don't show model-specific controls unless actually supported.

**Video Studio:** text-to-video, image-to-video, later video-to-video/motion-transfer, first/last frame, supported extension, supported camera and motion conditions, temporal comparison, reshoots and export. Start with a *short* real video and verify actual decoded codec/fps/frames.

**Audio Studio:** text-to-speech/narration, approved multi-voice, background music/SFX, transcript/subtitles, synchronization, mixing, lip-sync (later). Kokoro and faster-whisper are candidates; FFmpeg for media assembly. Check every model/voice/music license and consent.

**Cinematic/Movie Studio:** written premise/script -> storyboards -> scene/shot graph -> character/environment bible -> approved references -> generation per shot -> independent take review/reshoot -> dialogue/SFX/music/subtitles -> non-destructive timeline -> FFmpeg export -> validated movie artifact. First measurable film proof is an editable 60-second sequence with recurring characters; 20 minutes and 1–2 hours are **later assembly targets**, not one-inference requests.

**AI Director:** suggested prompts, scenes, camera/framing/continuity and cost-aware routing; human approval before expensive actions, untrusted agent output cannot execute shell, workflows, remote requests or secret access.

**Model/GPU Studio:** versioned model/capability registry, approved workflow schemas, checkpoint hash/license, GPU tier and cost estimates, benchmark actual latency/VRAM/success/accepted result, one heavy inference per constrained GPU when needed. LightX2V/quantization/offload only after baseline.

**Platform:** accessible original Next.js interface; durable jobs/assets/projects, progress/error/retry/cancellation semantics, API; later auth/tenants/quota/payment/deployment. Do not implement all product modules at M0.

## 3. Boundaries and code organization

```text
video-gen/
  apps/web/                  Next.js/React/TypeScript/Tailwind product UI
  services/api/              FastAPI, Pydantic, REST v1 and future auth
  services/worker/           CPU mock then isolated GPU execution
  packages/schemas/          Versioned shared API/domain contracts
  integrations/comfyui/      Typed private service adapter
  integrations/media/        FFmpeg and related media-specific adapters (future)
  workflows/                 Approved, pinned and validated templates (future)
  notebooks/colab/           Reproducible device preflight/experiments
  tests/                     CPU unit/integration and optional GPU
  infra/                     Local and later production infrastructure
  scripts/                   Docs validation, GPU preflight, smoke/setup
  docs/                      This handoff, research, decisions and roadmap
  .github/workflows/         Validation, tests, security and build checks
```

**One owned application** with multiple replaceable engines; avoid vendoring full ComfyUI, FreeField, model repos or unmaintained UI forks. ComfyUI speaks to our worker over a protected adapter; FreeField contributes architectural patterns/learning, not a second backend. Preserve existing functional code and ADRs. Main is still documentation-first until PR #8 merges.

**Preferred M0 technology:** Next.js 16, React 19, TS, Tailwind (version pins in PR #8), FastAPI/Pydantic, SQLite for local durable metadata, local filesystem for *mock* receipt bytes; HTTP poll for job progress. No Celery/Valkey/Postgres/S3 yet because M0 needs verified local usability, not expensive ops. Later add PostgreSQL-compatible metadata migrations, S3-like durable media, a real queue, isolated workers and secure authentication when requirements demand.

## 4. Domain data and invariants

| Entity | Primary data | Invariants |
|---|---|---|
| Project | ID, owner/tenant (future), name, timestamps, settings | User/tenant owns it; never reveal another tenant |
| Asset | ID, project, storage key, MIME, size, SHA-256, dimensions/fps if media, rights | Immutable bytes/hash/version; private by default |
| ModelDefinition | stable ID/version, repo/source pin, weight pin/hash/license, true capabilities, input constraints | Never advertise an unavailable installed model |
| WorkflowDefinition | ID, version, approved engine graph, input/output schema and resource estimates | Only operator-reviewed node graph; no arbitrary executable JSON |
| GenerationJob | stable ID, immutable request/model/workflow, idempotency scope/key, state/progress/errors, timestamps | No duplicate charge/work on idempotent retries; append-only provenance |
| GenerationArtifact | asset ID, job, model/workflow/seed/reference metadata, hash, media validation | Completed artifacts never silently mutate |
| WorkerCapability | engine, available models, VRAM, memory, concurrency and health | GPU placement informed by observed data |
| CharacterReference | stable character ID, approved appearance/voice/wardrobe versions | Regeneration reuses approved reference versions; drift is measured |
| EnvironmentReference | image/layout/set references and props | Versioned and reproducible |
| Scene/Shot/Take | narrative order, assigned characters, reference IDs, camera/time, many take versions | Reshoot one shot without overwriting accepted takes |
| TimelineTrack/Clip | non-destructive audio/video/subtitle tracks, timecodes, effects | Editable after exporting |
| Usage/AuditEvent | real GPU seconds, costs, errors, authorized actions | No secrets/private media leaked into logs |

M0 currently implements a small subset of these in the PR: Project, ModelDefinition, WorkflowDefinition, GenerationRequest/Job, Artifact, WorkerCapability, SQLite events. It does **not** implement user/organization auth, real video asset metadata, true cost metering, movie timeline or expensive dispatch.

## 5. M0 v1 HTTP contract and job state machine

Required endpoint surface: GET `/v1/health`, GET `/v1/models`, POST `/v1/projects`, GET `/v1/projects/{id}`, POST `/v1/jobs`, GET `/v1/jobs/{id}`. PR #8 additionally implements project listing/job listing, events, workflow list, artifact metadata and receipt download.

Example **mock-only** job request after creating a project:

```json
{
  "project_id": "proj_<generated_uuid_hex>",
  "model_id": "mock-preview-v1",
  "prompt": "A lantern-lit mountain village at dusk",
  "idempotency_key": "client-request-00001"
}
```

States: `QUEUED -> RUNNING -> SUCCEEDED | FAILED` for local mock. Error responses use stable codes; reusing a key with conflicting inputs returns `IDEMPOTENCY_CONFLICT`. Tests cover failure flags and invalid models. Later GPU lifecycle can include RESERVING/DOWNLOADING_MODELS/UPLOADING, timed-out/cancelled worker states with correct semantics. **Mock artifact = text/plain receipt labelled NOT AI-GENERATED.**

## 6. Reuse and exact two foundation projects

**ComfyUI:** [official GitHub](https://github.com/Comfy-Org/ComfyUI), inspected at `258f880d0c026bfc22acab679858ab2e2c70573d`. GPL-3.0 source; use external managed engine. In pinned versions, inspect `server.py` (HTTP/WebSocket/queue/history), `execution.py` (execution and graph validation), `comfy/model_management.py` (VRAM/memory policy) and workflow API formats. A VideoGen worker translates validated *allowlisted* workflow inputs into `POST /prompt`, monitors progress/history and imports verified output. Cancel safely; do not use global interrupt on unrelated jobs. Third-party nodes can execute code; isolate/approve them.

**FreeField:** [official GitHub](https://github.com/neuregex/freefield), inspected at `f0c2358a46c7008ff8503d4324b6cc8bc7657e75`. MIT source; inspect `schema/app.schema.json`, `apps/*/app.json`, `apps/*/workflow.api.json`, `server/registry.ts`, `server/runner.ts`, `server/history.ts`, `server/guard.ts`, `tools/comfy_validate.py`, `tools/catalog.py`, `infra/gateway.py`, `lab/core.py`, `.github/workflows/validate.yml`. Use patterns for generated forms, input-to-node binding checks, model license/VRAM manifests, provenance and lab cases; do NOT clone the entire product or its visual branding. Upstream GPU example counts are not our benchmarks.

Wan2.2 is the preferred first **video candidate after GPU preflight**, not a promise any particular checkpoint fits Colab. FLUX/Qwen for licensed compatible first image candidate. Kokoro speech in M3, FFmpeg assembly in M3, LightX2V optimization only in M6. The [complete catalog](../ALL_RECOMMENDED_REPOSITORIES.txt) lists 54 studies, not adopted dependencies.

## 7. Milestones and acceptance

**M0.1 license research (Issue #1):** verify correct upstream repos, source and weight licenses, exact version pins, dependency compatibility, deployment/commercial concerns; mark VERIFIED/PENDING/BLOCKED. No software-license assumption from GitHub visibility.

**M0.2 mock vertical slice (Issue #2):** Next.js UI, FastAPI with real backend requests, durable SQLite, mock worker/jobs/provenance, tests and CI, no GPU; implemented on **PR #8** with passing CI, pending human review/merge and fresh-clone owner test. No inference claim.

**M0.3 Colab preflight (Issue #3):** execute checked-in preflight in owner-controlled notebook; capture GPU device, VRAM, RAM, disk, torch/CUDA, runtime restrictions, storage persistence. Do not hardcode a GPU tier.

**M1 real image (Issue #4):** choose one permitted model/weight after licenses/hardware; start actual ComfyUI and generate a PNG; validate PNG decoding, width/height, SHA, prompt/seed/model/weight version, latency/VRAM. Evidence required.

**M2 real video (Issue #5):** select GPU-compatible Wan variant; generate a short genuine MP4; FFmpeg/ffprobe verify codec, frames, FPS, resolution, duration; record OOM/latency/VRAM and provenance.

**M3 audio/post (Issue #6):** Kokoro TTS, subtitles, FFmpeg mux/encode and verified sync. No fake previews or bought voices without rights.

**M4 studio:** integrated image/video/audio tabs and asset library with honest capability gating, comparison/history and previews; usable by new creators.

**M5 film (Issue #7):** character references, versioned environment/scene/shot/takes, human-approved direction, non-destructive timeline, per-shot reshoot and full 60-second repeated-character benchmark.

**M6 optimization:** baseline vs LightX2V/offload/quantization; same settings/hardware, reproducible quality and VRAM/latency metrics.

**M7 commercialization:** auth, multi-tenant isolation, quotas, secure GPU worker service, billing/cost, observability/recovery, legal and model-license review, secure deployment.

## 8. Security, cost, legal, quality: mandatory gates

- No API keys/secrets/PII/user media/model weights in Git; no arbitrary prompt->shell conversion.
- Check source, checkpoint weights, third-party assets/custom nodes, training sources and output rights independently.
- ComfyUI GPL-3.0 and potential AGPL dependencies require actual legal review; process isolation alone does not automatically eliminate obligations.
- No public unauthenticated ComfyUI, uploaded arbitrary workflow graphs, unreviewed custom node code, or open Colab production tunnel.
- Cost per **accepted output** includes all GPU time, failures/retries, storage/egress, API charges and post-processing; no unsupported quality/VRAM assertions.
- All output metadata should include model/checkpoint pins, hash, prompt/settings/seed, input hashes, GPU, runtime, VRAM and integrity checks when applicable.
- Separate PASSED, FAILED, NOT RUN, PENDING, BLOCKED. A green CPU mock CI is not a GPU result.
- No model foundation training from scratch in MVP, no massive download in M0, no unapproved charges.

## 9. Verified project state at handoff

`main` initial baseline: `2a88181dc0408f6477dd52a6ed8ded762f149bcd`; documentation-first with existing docs CI and Colab preflight script/notebook. PR #8 branch `feat/m0-2-mock-studio`, last implementation/evidence commit `ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37`. Both [application CI](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390592) and [documentation CI](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390571) passed for PR head. PR unmerged at observation. **Main may have newer docs-only commits from this handoff; check live state before using these old SHA values.**

CLI / dev commands from PR branch [runbook](https://github.com/anneshabiswaas22-collab/video-gen/blob/ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37/docs/BUILD_RUN.md):

```bash
git clone https://github.com/anneshabiswaas22-collab/video-gen.git
cd video-gen
git switch feat/m0-2-mock-studio
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
python -m pip install -e ".[dev]"
npm install --prefix apps/web
bash scripts/dev.sh
```

Open local web `http://127.0.0.1:3000`, FastAPI docs `http://127.0.0.1:8000/docs`. Re-evaluate commands after merge/changes.

## 10. Biggest blockers and next exact action

1. **Review/merge PR #8 if still open**, with explicit owner/reviewer instruction; check latest main, merge conflicts, CI, smoke on a clean clone. Do not overwrite, force-push or auto-merge unreviewed changes.
2. Finish **source+weight+commercial licensing register** (#1). Decide owned application source license.
3. Execute **real Colab hardware preflight** (#3) and archive non-sensitive measurements.
4. Then implement **one** licensed real image workflow (#4); stop and verify the artifact before pursuing video.
5. For every completed task update [canonical memory](../../PROJECT_MEMORY.md), [state ledger](STATE_EVIDENCE_AND_OPEN_ISSUES.md), [history](CONVERSATION_AND_DECISION_HISTORY.md), source/version register, ADR, and task checklist.

**This document is deliberately readable standalone.** The memory archive index links to detailed charts, source URLs, chronological rationale, the copy-ready continuation prompt, and maintenance protocol.
