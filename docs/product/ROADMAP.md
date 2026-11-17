> **Current delivery:** Original M0 CPU application recovered and extended with
> the typed English-practice slice. See [implementation progress](../development/IMPLEMENTATION_PROGRESS.md)
> and [test evidence](../quality/IMPLEMENTATION_VALIDATION.md). T0 is a bounded
> developer-authored phrase prototype; educator review and general AI quality
> remain pending. The original milestone definitions below are acceptance gates,
> not claims that every item is completed.

# Execution roadmap and measurable completion criteria

Stages are dependency-ordered, **not time or cost promises**. Codex Cloud can write/test code; GPU verification is separate. Track each milestone with GitHub Issues and PRs.

## M0 — Repository and licensing audit (next)
- Inventory current source, selected upstream repos, licenses, exact releases, checkpoint sizes and Colab compatibility.
- Create owned monorepo scaffold, local dev commands, CI, environment template and diagrams.
- Define typed model/job/artifact schemas and a mock worker; test without GPU.
- Documentation complete enough that a new contributor can run the mock path.
**Exit:** clean clone + documented setup + passing CI and a reproducible mock job; no model-quality claims.

## M1 — First genuine image
- Choose a permitted lightweight model that fits detected GPU; pin weights and hashes.
- Build one end-to-end image workflow with job status and durable artifact storage.
**Exit:** real PNG from a provided prompt, settings/seed and provenance saved; measured peak VRAM and runtime; can repeat instructions.

## M2 — First genuine image-to-video and text-to-video
- Select correct Wan checkpoint for real GPU, not a hardcoded assumption.
- Run one short generation, save MP4, check frame count/duration/resolution, handle OOM and resumed jobs.
**Exit:** real MP4 stored and downloadable with reproducible metadata and failure logs.

## M3 — Voice / audio / media finishing
- Add Kokoro speech, simple SFX/music candidate (licensed), FFmpeg mixing and subtitle generation.
**Exit:** one correctly playable video with speech and mastered background track, plus reusable media assets.

## M4 — Original creator interface
- Polished generation workspaces, previews, job list, asset browser, project organization, presets and error guidance.
**Exit:** nontechnical user completes image -> video -> audio -> export from product UI; accessible basic UX.

## M5 — Cinematic and movie differentiation
- Character reference library, versioned scene/shot graph, storyboard tool, camera presets through supported conditioning, human approvals, lip-sync.
**Exit:** 60-second sequence with repeat characters, individually regenerable shots, subtitles, editable timeline, measurable continuity checks.

## M6 — Optimization and evaluation
- Benchmark base runner vs ComfyUI optimization vs LightX2V and other accelerations on same hardware and tasks.
- Only adopt paths that show actual benefit or quality tradeoff worth keeping.
**Exit:** documented performance table: latency, peak VRAM, success rate, blind preference and cost at fixed settings.

## M7 — Product hardening / commercialization
- Secure identities, permissions, isolated workers, quotas and abuse controls; persistence, backups, payments, monitoring, deployment.
- Review licenses of every distributed engine and weight and obtain counsel for uncertain copyleft/commercial terms.
**Exit:** deployment under owned accounts with operational runbooks, reproducible setup, security and load testing.

## Explicitly deferred research
Large language-model control plane, multimodal model training from scratch, true >1-hour generation in one shot, public multi-tenant Colab hosting, proprietary Kling/Veo/Sora source replication, and unsupported performance superiority claims.

## Work queue format
Each GitHub issue: user story, priority, dependencies, reuse alternatives, license notes, definition of done, test modes (CPU/GPU), artifacts/links and risk. No broad "implement everything" mega tasks.

## Combined-product tutor track — added 2026-11-17

The M0–M7 studio milestones remain. The owner added the English-speaking friend
as a first-class feature; it need not wait for long-form film generation.
Shared M0 contract/security foundations precede any public service.

- **T0 — text learning loop (PLANNED):** English/Bangla teacher-reviewed examples,
  transcript editing, correction preferences, uncertainty/valid-variant handling.
  Acceptance: a usable text loop and documented human evaluation, not mock output
  presented as effective teaching.
- **T1 — narrow adult speech pilot (PLANNED):** push-to-talk, replay, a licensed
  simple avatar, optional phrase review, privacy/deletion, text fallback.
  Acceptance: actual recognition and speech tests, measured turn latency and cost,
  teacher review and consented adult usability results. No user camera required.
- **T2 — research after pilot evidence (NOT RUN):** interruptions, richer avatars,
  additional reviewed languages and optional approved creative-scene export.
  Each experiment needs a test, accountable owner, cost ceiling and stop condition.

Year 1, Year 2 and Years 3–5 in [the future vision](FUTURE_ROADMAP.txt)
are conditional ambitions, not delivery commitments or guaranteed AI breakthroughs.
See [the feature map](../../features/README.md) for dependencies and boundaries.
