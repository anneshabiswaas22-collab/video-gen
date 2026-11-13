# VideoGen — Open AI Creative Studio

> **Status: project charter and developer handoff (documentation-first).** This repository describes the product to build; it **does not** yet contain a proven working generation service, trained model, benchmark results, or deployed product.

## Our mission

Build an **original, commercially viable AI creative studio** competitive with the user experience of Higgsfield, Runway, Google Flow, and Kling: generate and edit **images, videos, voices, music, sound effects, and eventually long-form movies** in one cohesive workspace. Our differentiation: character continuity across shots, AI-assisted directing, scene-level revision, camera/motion workflows, model-choice transparency, editable projects, and low-cost GPU operations.

**Non-negotiables:** own our application's code and identity; reuse maintained open-source tooling; do not copy proprietary models/services; check licenses for *code and weights*; minimize wasteful Codex work; verify output on real GPU rather than claiming success from code review. Core engineering via Codex Cloud; real inference initially on the owner's Google Colab GPU (and optionally Kaggle, where permitted). Dedicated GPU workers are a future deployment option.

## New here? Read these in order

1. [PROJECT_CHARTER.md](docs/PROJECT_CHARTER.md) — business objective, audience, benchmark, product principles.
2. [ARCHITECTURE.md](docs/ARCHITECTURE.md) — owned monorepo, model adapters, GPU execution, persistence, API and boundaries.
3. [FEATURE_REGISTRY.md](docs/FEATURE_REGISTRY.md) — complete target feature inventory and maturity labels.
4. [OPEN_SOURCE_STACK.md](docs/OPEN_SOURCE_STACK.md) — candidate repos and **reuse/build decisions**.
5. [ROADMAP.md](docs/ROADMAP.md) — milestones, sequencing, measurable acceptance criteria.
6. [GPU_COLAB.md](docs/GPU_COLAB.md) — Colab constraints, proposed notebook workflow and resource discipline.
7. [LICENSE_SECURITY.md](docs/LICENSE_SECURITY.md) — code/weights rights, security/privacy and operating constraints.
8. [BENCHMARKS.md](docs/BENCHMARKS.md) — fair comparisons and quality/cost measurement.
9. [DECISIONS.md](docs/DECISIONS.md) — decisions vs. open questions; avoid assumed claims.
10. [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md) — Codex and human contributor instructions.

The [documentation index](docs/README.md) connects every design, operation, and reference. No access to the original planning conversation is needed.

## High-level design

```text
Own Web App (Next.js/React, original product UX)
        |
Own API (FastAPI, auth, jobs, projects, assets, quotas)
        |
Orchestrator / queues / model registry / cost & quality policies
        |
ComfyUI adapter + optional optimized inference adapters (LightX2V etc.)
        |
Images (FLUX/Qwen) | Video (Wan/LTX) | Audio (Kokoro/ACE-Step)
        |
GPU worker (Colab notebook during research; dedicated workers in production)
        |
Assets + immutable generation metadata + FFmpeg movie assembly
```

**Repository strategy:** one owned *application monorepo*, multiple external engines installed/versioned as dependencies or isolated services; do not indiscriminately vendor entire upstream repos or commit model weights. FreeField is a **workflow/reference source**, not a second mandatory competing backend.

## What exists today

- Product vision, architecture proposal, candidate repository map, security/licensing checklist, staged backlog, contributor instructions.
- Actual model integration, UI, APIs, Colab inference and tests are **planned, not implemented** until proven in code and hardware.
- Any upstream project feature counts, memory needs, model versions or marketing claims are **candidates requiring verification**, not accepted benchmarks.

## First work item

See [Milestone M0](docs/ROADMAP.md): audit pinned upstream sources, verify licenses and GPU constraints, scaffold an ownable repo with a minimal FastAPI/Next.js integration and tests, and then implement one reproducible generation path. Define CPU-mock tests for Codex Cloud and mark GPU-dependent tests explicitly.

## Guiding rule

**Reuse foundations. Build differentiation. Benchmark everything.** Read [REUSE_FIRST.md](docs/REUSE_FIRST.md) before adding a feature.

---

Public repo: https://github.com/anneshabiswaas22-collab/video-gen  
Project documentation date: 2026-11-13. External project links, model releases and license details must be rechecked at integration time.
