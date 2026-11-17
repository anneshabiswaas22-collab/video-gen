> **Current structure:** Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) and the
> [file-placement ledger](docs/repository/FILE_PLACEMENT.json). Shared documents now
> live in functional docs collections; repository scripts are in `scripts/maintenance/`
> and GPU inspection in `scripts/hardware/`. The owner has now authorized
> implementation, incremental integration and tests. The earlier no-tests rule
> applied only to the completed sorting task. Keep its historical evidence dated.

# AGENTS.md — Instructions for Codex and all coding agents

Read README.md and docs/README.md before editing. This file is the standing project brief; the original chat is NOT required.

## Mission / ownership
Build an original, ownable, competitive AI creative studio for image, video, audio, cinematic effects, character continuity, and long-form movies. Market benchmarks: Higgsfield, Runway, Google Flow, Kling. Do not claim to be the best without reproducible measurements.

## Guardrails (always)
1. REUSE FIRST: before building a feature, inspect upstream alternatives and record integration-vs-build rationale in docs/research/OPEN_SOURCE_STACK.md or a new ADR.
2. Our app is one monorepo; external inference engines are versioned dependencies/services, NOT random copied repositories. FreeField is a workflow/reference source; ComfyUI is the preferred inference adapter.
3. Check source code license, model-weight license, dependency licenses, training-data and commercial-use terms separately. Never treat public GitHub as blanket permission to redistribute. GPL/AGPL can affect distribution and network services; escalate uncertainty for legal review.
4. No paid APIs, massive checkpoint downloads, scraping, GPU renting, or training without explicit owner budget approval. Never commit model weights, secrets, tokens, private media or personal data.
5. Codex Cloud is for implementation and CPU-side testing; GPU inference must run on a suitable external GPU (initially Google Colab). Never fake success for GPU-only paths.
6. Colab/Kaggle are constrained notebook runtimes. Do not work around session, quota, or hosting restrictions.
7. Prefer one active inference job per small GPU. Measure latency, peak VRAM, CPU RAM, video duration, quality and actual compute cost.
8. Use an asynchronous job contract, idempotent job creation, model capability registry, persistent artifact metadata and explicit errors. Implement cancellation, retries, and observability incrementally.
9. Security: untrusted prompts/uploads/workflows must not execute arbitrary code; sandbox workers, restrict paths, URL access and file types; keep provider tokens server-side. Treat AI agent output as untrusted.
10. Build behind tests, maintain stable compatibility, document every assumption. Avoid rewriting working functionality for style alone.

## Every task begins with
- Restate the precise goal and link to its roadmap milestone / feature-registry item.
- Inspect the current repo to avoid duplicating code.
- Identify reusable upstream packages and pinned versions.
- Note license and GPU constraints.
- State acceptance criteria and automated test plan.
- Implement the smallest end-to-end vertical slice and run the available tests.
- Mark tests as PASSED / FAILED / NOT RUN (GPU unavailable) accurately.
- Update docs, changelog/decisions and examples in the same PR.

## Priority
M0 audit + scaffold -> M1 first real image -> M2 first real image-to-video -> M3 voice and media assembly -> M4 original creator UX -> M5 continuity/camera/film tools -> M6 optimization -> M7 commercial hardening.

## Done criteria
A feature is NOT done because code compiles, the UI renders, a README mentions it, or a mock returns a URL. Done requires usable output, suitable real GPU validation where applicable, tests, documented dependencies and known limitations.

## Do not
- Build a new model architecture from scratch for MVP.
- Promise that open models match proprietary frontier models.
- Merge complete FreeField, ComfyUI and model repos into this Git tree.
- Treat disputed/unverified product version names, VRAM numbers or model releases as confirmed.
- Touch unrelated repositories (including the separate English-learning channel) without explicit scope.

## Essential long-chat continuity — READ THIS BEFORE NEW WORK
The canonical self-contained project handoff is [docs/memory/PROJECT_MEMORY.md](docs/memory/PROJECT_MEMORY.md).
Its [memory bundle](docs/memory/README.md) preserves requirements, historical decisions,
upstream research links, GitHub branch/PR/CI evidence, architecture diagrams and a
self-contained next-session prompt. **Never rely on unavailable chat messages** to
understand the project. Refresh live GitHub issues, commits and CI because recorded
snapshots can be stale. After EVERY meaningful PR or milestone, update this
version-controlled handoff and the verification/status ledger with facts and exact links.

## Current repository and feature boundaries (2026-11-17)

The owner explicitly combined VideoGen with the English-speaking AI friend.
Read `features/README.md`, `docs/product/PROJECT_IDEA.txt` and
`docs/development/NEXT_DEVELOPER_INSTRUCTIONS.txt` before new implementation.
The separate channel/assets mentioned above remain out of scope; the new tutor
feature is in scope here. Historical PR/CI links do not establish current code.
`AnalyseFuture/references/inference-engine/comfyui/` and
`AnalyseFuture/references/workflow-studio/freefield/` are preserved
references, excluded from the active product. Do not automatically execute or
promote them, or change their bytes without an explicit reviewed migration.
Run `python scripts/maintenance/check_structure.py` along with the documentation check.
Use the existing isolated checkout; do not create worktrees unless requested.
