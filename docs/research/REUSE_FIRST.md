# Reuse-first policy — save Codex credits

## Objective
Codex should implement only the parts that form our differentiated product. Existing maintained tools should handle common media and infrastructure functionality where integration is cheaper and lawful.

## Decision gate required before each feature
1. Describe desired behavior, inputs/outputs, and acceptance tests.
2. Search candidate libraries, models, ComfyUI custom nodes and existing workflows.
3. Evaluate license, checkpoint license, API/compute pricing, health/maintainers, GPU memory, dependency conflicts and security.
4. Compare three options: direct dependency; service/workflow adapter; original implementation.
5. Prefer a pinned dependency with tests. Do not vendor entire repos because they are public.
6. If rejecting a reusable component, document why; if upgrading it, run regression and baseline benchmarks.

## Reuse vs build
**Prefer reuse:** FFmpeg for encoding/transitions/muxing; ComfyUI for workflow execution; Wan/FLUX/Qwen for generation; rembg, SAM2, Real-ESRGAN for processing; faster-whisper for transcription; Kokoro for speech; ACE-Step for music; OpenCut as editor reference; Celery/Valkey for queues; shadcn/ui for widgets; React Flow for graph editing.

**Build ourselves:** cohesive product UX, intelligent model selection, cost budgets, continuity/reference ledger, prompt/shot templates, scene graph/timeline versioning, AI director orchestration, worker integration contracts, observability, quality evaluation and brand.

## Evidence
Never trust marketing feature counts or VRAM benchmarks from another repo as proof of our own performance. Validate against the pinned version with a real GPU. Even when code has a permissive license, weights or third-party API models may not.

## Do not spend credits on
- Duplicating existing public generation engines or building a new transformer/diffusion foundation model for MVP.
- Implementing billing/teams/LoRA training before the first actual output.
- More than one competing queue/database/frontend framework.
- Integrating every upstream model immediately.
- Rewriting working code merely to conform to aesthetic preferences.
- Building a Colab workaround that violates service restrictions.

## PR template sentence
"Existing alternatives assessed: __. Selected: __ because __. Code license: __. Weight license: __. VRAM/compute measured: __. CPU tests: __. GPU tests: __/not run."
