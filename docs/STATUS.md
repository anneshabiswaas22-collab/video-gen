# Verified repository status and first tasks

## M0.2 feature branch activity — 2026-11-15

Branch `feat/m0-2-mock-studio` introduces original Next.js UI, FastAPI local-only
API, durable SQLite project/job/artifact metadata, CPU worker, typed contracts,
ComfyUI HTTP boundary and initial CI/tests. **This is a feature branch, not a merged
release.** See [local setup](BUILD_RUN.md), [implementation checklist](M0_2_CHECKLIST.md),
[two-repository study](TWO_REPO_DEEP_STUDY.md), and GitHub PR checks for current
execution evidence. It runs a synthetic plain-text mock receipt, NOT AI inference.



**Date:** 2026-11-13. **Branch:** main. **Scope:** architecture and developer handoff, NOT a finished AI generation service.

## Completed in this handoff
- Root README, project charter, architecture, roadmap, feature registry, source stack, decisions, Codex agents guide, contributor guide, production/benchmark/licensing/security specifications.
- CI workflow intended to validate local Markdown links; reusable docs validator (Python standard library).
- GPU hardware preflight script and a Colab notebook (inspection only; no inference).
- Issue/PR templates and a first batch of GitHub task tickets.

## Not yet completed
- Own frontend/backend/worker stack and model adapter implementations.
- Any actual checkpoint downloads, real generated PNG/MP4/WAV, model fine-tuning or GPU benchmarks.
- Verified execution of the GitHub Actions CI workflow (check Actions tab), Colab notebook or scripted tests.
- Final app license, platform costs, commercial launch and legal signoff.

## First GitHub issues
1. https://github.com/anneshabiswaas22-collab/video-gen/issues/1 — model and source license audit.
2. https://github.com/anneshabiswaas22-collab/video-gen/issues/2 — original web/API monorepo and CPU-mock jobs.
3. https://github.com/anneshabiswaas22-collab/video-gen/issues/3 — Colab hardware notebook verification.
4. https://github.com/anneshabiswaas22-collab/video-gen/issues/4 — first real image.
5. https://github.com/anneshabiswaas22-collab/video-gen/issues/5 — first real Wan video.
6. https://github.com/anneshabiswaas22-collab/video-gen/issues/6 — speech and FFmpeg.
7. https://github.com/anneshabiswaas22-collab/video-gen/issues/7 — character continuity design.

## Recommended contributor start
Pick M0.1 or M0.2, read AGENTS.md and docs/REUSE_FIRST.md, create a branch and open a small, tested PR. Avoid starting a massive "build all features" task in Codex.

## Verification record
GitHub connector confirmed repository permissions and successfully updated main. In the execution environment used for this handoff, a separate CLI clone attempt failed DNS resolution for github.com; **this does not mean the GitHub push failed**. Remote read-back and Actions checks are separate from a local end-to-end test.
