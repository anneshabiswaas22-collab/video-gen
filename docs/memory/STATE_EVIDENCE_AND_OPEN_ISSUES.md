> **Current checkout note — 2026-11-17:** This is
> `sarfiaroui-oss/video-gen`, with the feature map in
> [features](../../features/README.md) and current
> [validation report](../../AnalyseFuture/TEST_AND_VALIDATION_REPORT.txt).
> The source-repository PR/CI snapshot below is historical. It does not establish
> that its application code is present here. The bulk imports were preserved,
> and the English companion was added to product planning; no GPU inference or
> tutor behavior is claimed. See [reorganization findings](../REPOSITORY_REORGANIZATION.md).

# VideoGen — verified evidence, branch/PR state and open backlog

**Observation date:** 2026-11-16 (Asia/Kolkata). GitHub may change after this snapshot. **Always re-fetch live branch refs, PRs, issues and Action runs before modifying code.** This document separates completed CPU work from planned GPU/product work.

## GitHub state at observation

| Object | Source / exact evidence | Status |
|---|---|---|
| Default branch | [main](https://github.com/anneshabiswaas22-collab/video-gen/tree/main) | Before new docs commits, `2a88181dc0408f6477dd52a6ed8ded762f149bcd`, documentation-only |
| Feature branch | [feat/m0-2-mock-studio](https://github.com/anneshabiswaas22-collab/video-gen/tree/feat/m0-2-mock-studio) | Contains working M0.2 code |
| Open PR | [#8](https://github.com/anneshabiswaas22-collab/video-gen/pull/8) | Open, **ready for review**, not merged at observation; mergeable state clean |
| PR head commit | [ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37](https://github.com/anneshabiswaas22-collab/video-gen/commit/ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37) | Implementation/test/documentation snapshot |
| Application CI | [run 43741390592](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390592) | **PASSED**, all jobs |
| Documentation CI | [run 43741390571](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390571) | **PASSED** |
| Prior main docs CI | [run 43719613690](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43719613690) | PASSED before M0.2 PR |
| This documentation handoff | [PROJECT_MEMORY.md](../../PROJECT_MEMORY.md), [memory index](README.md) | Committed directly to main; check latest SHA in GitHub |

**Do not say that PR #8 is merged or that real AI generation succeeded.** An updated `main` might now include handoff-only docs, not the application code. Update the ledger after a real merge, not before.

## Verified implemented components on PR #8

1. Original responsive Next.js/React/TS/Tailwind interface with create/select project, prompt box, mock model choice, real HTTP submit, progress, failure, history and downloadable receipt.
2. FastAPI/Pydantic with health, models, workflows, project CRUD subset, jobs, events, artifact metadata/download endpoints; OpenAPI available locally.
3. SQLite durability for projects, jobs, events, artifacts; generated stable IDs, scoped idempotency key and request fingerprint, 409 on conflicting payload.
4. Executable mock worker (in-process local dev loop with separate test entrypoint) handles `QUEUED -> RUNNING -> SUCCEEDED/FAILED`, simulates failure, persists history and materializes a plain-text receipt.
5. ComfyUI adapter typed interface and `httpx.MockTransport` tests for approve-only workflow submission; this adapter is **not invoked for real inference**.
6. Local launch script, runbook and CI to check application + security dependencies.

### Test matrix (latest confirmed PR head)

| Test / operation | Evidence | Outcome |
|---|---|---|
| Python Ruff lint | [Application CI](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390592) | PASSED |
| Python unit/API/adapter integration | Same run | **7 tests PASSED** |
| CPU worker mock smoke | Same run | PASSED |
| Node JavaScript client → live local FastAPI → SQLite → worker → downloaded artifact | Same run | PASSED |
| Python installation/dependency consistency | Same run | PASSED |
| Python vulnerability scan | Same run | PASSED for installed set |
| TypeScript typecheck | Same run | PASSED |
| ESLint | Same run | PASSED |
| Frontend tests | Same run | PASSED |
| Next.js production build | Same run | PASSED |
| npm production dependency audit | Same run | PASSED |
| Markdown/documentation integrity | [Docs CI](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390571) | PASSED |
| Fresh clone on owner's local Windows environment | None | **NOT RUN** |
| Actual Colab GPU/VRAM/torch/CUDA report | None | **NOT RUN** |
| Genuine PNG decoded + SHA + actual hardware | None | **NOT RUN** |
| Genuine MP4 encoded/decoded + frames/fps/codec/VRAM | None | **NOT RUN** |
| Real voice/audio waveform and sync | None | **NOT RUN** |
| Auth/multi-tenant security / production recovery | Not implemented | **PENDING** |

Earlier CI had failures in Python import lint, React effect lint and outdated vulnerable dependencies; these were fixed before final green checks. The existence of old failed runs does not invalidate the passing PR-head run, nor does green CI prove the owner's Windows setup works.

## Open issues (exact links)

| Issue | Description | Next acceptance gate |
|---|---|---|
| [#1](https://github.com/anneshabiswaas22-collab/video-gen/issues/1) | M0.1 dependency, source/weights/commercial license review | Exact pinned licenses, model card, compatibility |
| [#2](https://github.com/anneshabiswaas22-collab/video-gen/issues/2) | M0.2 original web/API/mock vertical slice | Review/merge PR #8 after latest CI/manual run |
| [#3](https://github.com/anneshabiswaas22-collab/video-gen/issues/3) | M0.3 actual Colab hardware preflight | GPU name/VRAM/host RAM/disk/CUDA evidence |
| [#4](https://github.com/anneshabiswaas22-collab/video-gen/issues/4) | M1 first real image | Approved checkpoint, PNG hash, latency and VRAM |
| [#5](https://github.com/anneshabiswaas22-collab/video-gen/issues/5) | M2 Wan-compatible real image-to-video | Verified short MP4, real hardware metrics |
| [#6](https://github.com/anneshabiswaas22-collab/video-gen/issues/6) | M3 Kokoro/FFmpeg speech and post-production | Valid voice+caption+video/audio output and sync |
| [#7](https://github.com/anneshabiswaas22-collab/video-gen/issues/7) | M5 recurring-character continuity and editable takes | Coherent editable 60-second measured proof |

### Highest priority outstanding tasks

1. Verify latest CI/PR still clean; **human review and authorized merge** PR #8 (avoid changing unrelated code).
2. Run a **fresh clone** on real Windows with documented commands; fix any reproducible install/runtime issues, pin and commit transitive npm lockfile; update tests and CI.
3. Complete legal/source/weight license audit (#1), with the selected model's **specific** version and rights.
4. Collect real hardware preflight (#3) in owner-controlled Colab. Do not invent VRAM.
5. One genuine PNG through ComfyUI adapter (#4), with model/weights pin, seed/inputs, artifact SHA, decode check, latency, peak VRAM and cost.
6. Only later real Wan video, Kokoro/FFmpeg and movie/continuity.

## Explicitly deferred or risky areas

- No real GPU adapter integration; allowlisted ComfyUI stub only.
- No auth/quota/multitenant isolation. **Never publish M0 directly.**
- No production cancellation/retries/distributed exactly-once scheduling.
- SQLite + local text files are only the M0 environment; later migration and object storage required.
- GPU checkpoints and legal commercialization clearance remain unverified.
- No real user-level usability study and no benchmark results versus commercial competitors.

## Post-change update instructions

When PR #8 merges or a new feature ships, append the *new* branch/commit/PR/CI URLs, test outcomes and actual evidence. Mark earlier content as historical rather than silently overwriting it. New tasks must update [root handoff](../../PROJECT_MEMORY.md), [canon](PROJECT_CANONICAL_HANDOFF.md), [history](CONVERSATION_AND_DECISION_HISTORY.md) and [maintenance protocol](MAINTENANCE_PROTOCOL.md).
