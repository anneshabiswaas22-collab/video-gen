# Copy to Codex Cloud — first scoped engineering task

You are principal full-stack architect and AI inference engineer for the repository:
https://github.com/anneshabiswaas22-collab/video-gen

Read README.md, AGENTS.md, docs/README.md, docs/DECISIONS.md, docs/REUSE_FIRST.md, docs/ROADMAP.md and docs/STATUS.md first. Treat these as the authoritative project brief; the planning chat is not needed.

**Business mission:** Build our original, ownable AI Creative Studio that aims to compete with Higgsfield, Runway, Google Flow and Kling in the experience of image/video/audio creation and long-form, character-consistent filmmaking. Avoid claims of superiority without benchmarks.

**Do not rebuild known technologies:** ComfyUI (workflow inference), FreeField (research/reusable workflow candidates), Wan (video), Qwen/FLUX (image), Kokoro (voice), ACE-Step (music), FFmpeg (media), LightX2V (optimization candidate), and other specific libraries listed in docs/OPEN_SOURCE_STACK.md. Every dependency requires license and version validation.

**First implementation task = GitHub Issue #2 only** (after examining Issue #1 and #3 requirements).
1. Check the repo's documentation, open issues and latest branch.
2. Propose a minimal Next.js + FastAPI + mock-worker monorepo consistent with docs/ARCHITECTURE.md and docs/API_CONTRACT.md.
3. Implement and test the MOCK path only. No model downloads or paid GPU/API calls.
4. Document one-command setup, inputs, outputs, environment variables, job state contract and next GPU integration step.
5. Run all available tests, report results verbatim, and update feature statuses accurately.
6. Create one small PR with a clear checklist and no unrelated changes.

**Acceptance:** a new developer can clone, install, run a mock job via API and UI, and execute tests locally. No claim of working video generation until a genuine MP4 is produced on a suitable GPU.

After that, address Colab preflight Issue #3, then the first real image and video milestones in order. Stop after the assigned milestone rather than spending credits on speculative extras.
