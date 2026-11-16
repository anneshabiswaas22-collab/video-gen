# VideoGen conversation history and decision provenance

**Version:** 2026-11-16. **Purpose:** make the long-running VideoGen project resumable without conversational memory. Records known user objectives and previously verified engineering actions. **This is a curated, factual reconstruction—not a word-for-word export of all chats.** Earlier conversation messages unavailable in the current working context must never be fabricated.

## Timeline — known project milestones

| Time / event | User need or research outcome | Persistent consequence | Confidence |
|---|---|---|---|
| Before 2026-11-12 | Wants to own a low-cost AI image/video creation platform; GPT/Codex writes application; owner has access to Colab GPU | Own application, prefer open-source dependencies, not an expensive API-only wrapper | Context available |
| 2026-11-12 | Asked which public video-generation repos surpass FreeField, FreeField vs Wan, MiniMax source availability, and Colab/Kaggle model/GPU feasibility | Distinguish application stack from model inference; verify source and checkpoints, do not assume proprietary code is public | Context available |
| 2026-11-12 to 2026-11-13 | Wants a competitor to best user-facing creative platforms, as many useful features as lawful and economically sustainable, minimal wasted Codex credits; single vs combined repo question | One owned monorepo + best specialized engines through adapters, not a giant merged source repository | Context available |
| 2026-11-13 | Requested all research, product vision, priorities, architecture, developer guide in `video-gen` so any new AI/developer can contribute without the chat | Initial charter, roadmap, AGENTS, docs, issue list, CI, Colab preflight committed to main | Previously reported + current GitHub verified |
| 2026-11-13 to 2026-11-15 | Asked for catalog of all repositories studied and a `.txt` file in GitHub | `docs/research/ALL_RECOMMENDED_REPOSITORIES.txt` lists 54 historical candidates, grouped by category | Live file verified |
| 2026-11-15 | Asked to check GitHub PRs and merge where appropriate; open VideoGen PR list was initially empty | PR policy: inspect branches/CI, don't overwrite; avoid merging unreviewed changes | Live check |
| 2026-11-15 | Supplied detailed Master Development Prompt (principal engineer; study **exactly two** primary repos ComfyUI + FreeField; implement Issue #2 end-to-end mock rather than documentation only) | M0.2 chosen before real inference; strict legal/security/budget and verification requirements; branch+review PR | User directive available |
| 2026-11-15 | Live repo main inspected, starting `2a88181dc0408f6477dd52a6ed8ded762f149bcd`: documentation-only; first checks pass for docs | No false claims of existing generation backend; preserve original docs | Live evidence |
| 2026-11-15 | ComfyUI master source `258f880d...` and FreeField main `f0c2358a...` inspected, licenses checked | ComfyUI GPL external engine; FreeField MIT source manifest reference; third-party assets/weights pending | Live GitHub source code/license review |
| 2026-11-15 | Implemented API/web/SQLite/mock worker and scoped ComfyUI HTTP adapter in `feat/m0-2-mock-studio`; tested/iteratively fixed CI | Working **CPU mock** implementation lives in PR #8; do not label as GPU inference | GitHub commits/CI |
| 2026-11-15 | Final M0 PR #8 commit `ae953a3...`, Python 7 tests, lint, live JS->FastAPI smoke, frontend tests/types/build, npm+pip audits, docs CI passed | PR ready for review, left unmerged; M1 remains not run | GitHub actions |
| 2026-11-16 | Wants **all project details, research, charts, links, history, decisions, tasks and future-agent instructions pushed to GitHub**, because long ChatGPT chats fail to load | This self-contained permanent `docs/memory/PROJECT_MEMORY.md` + `docs/memory/` archive is the handoff path | Current user directive |

## User's stable requirements — MUST preserve

- Our software is independently owned and branded, developed in `anneshabiswaas22-collab/video-gen`; competitors' products are product-quality references, not source to copy.
- The end goal is a capable creative studio for text/image/video/audio generation, editing and movie production, but **build it incrementally** with tested vertical slices and capability gates.
- Prioritize **practical reuse** (ComfyUI, licensed models, FFmpeg, manifest patterns), avoid spending GPT/Codex credits building a new base model or duplicating code.
- GPU inference is resource-intensive; start with mock API and local CPU CI, then use owner-run Colab preflight and approved compatible checkpoints; Colab is not a 24/7 production service.
- Maintain **character identity across multi-shot videos**, approved references, scene graph, shot/take history, non-destructive regeneration, cinematic/camera controls and AI director with human approvals.
- Real verification means a genuine PNG/MP4/WAV decoded and hashed on recorded hardware; merely compiling, listing a workflow or making a mock text file is NOT generation proof.
- Separate model-weight license from repository source-code license, third-party workflows/assets, deployment and training-data rights. Not all public repos or checkpoints allow commercial redistribution.
- No paid API, GPU rental, hidden costs, large M0 weights, unsafe custom nodes, public unauthenticated inference worker endpoints or secrets in Git without explicit owner authorization.
- Keep developer instructions, decisions, exact links and checklists in GitHub so lost chats do not block development.

## Decisions made and reasons

| Decision | Why | Revisit only when |
|---|---|---|
| One VideoGen monorepo | Own stable product/data contracts; prevent scattered forks and accidental license mixing | Documented ADR and measured integration reason |
| ComfyUI as external engine | Existing tested graph execution/GPU resource model; avoids writing new inference framework | Verified blocker/license incompatibility or benchmark advantage |
| FreeField as pattern/reference | Detailed manifest->form->workflow structure; fast learning without rebranding | Feature-specific legal and compatibility review |
| Exactly TWO deep study foundations for M0 | Prevent open-ended clone/research spending | New verified blocking evidence |
| Async job contract, idempotency, provenance | Needed for robust expensive GPU operations and reproducible movie shots | Never remove; can evolve schema |
| SQLite + in-process mock worker for M0 | Test full path without Redis/Postgres/GPU cost | Real multi-worker load/persistence/recovery requirements |
| Separate real GPU milestones | Honest output quality, hardware feasibility and model licensing | Not negotiable; only status advances after evidence |
| Single coherent movie = short scene/shot graph + editor | Long 20–120 minute productions cannot be one reliable giant inference | Better model evidence, while retaining editability |

## Related interests intentionally outside scope

There are separate AI animation/story-building, advanced video-editor, English tutor, and other application repositories. **Do not combine their code, issues or assets into VideoGen**. VideoGen can later become a model provider for content creation but no direct cross-repo work is authorized in this project scope.

A previously discussed American-English-learning 3D family video series needs 15-second shots and recurring characters, useful as a later **continuity benchmark only**. Original content assets and scripts belong to the separate creative production project.

## Caveats: what cannot be restored

This archive does **not** preserve all exact user/assistant messages, full model reasoning, expired external pages, or every unverified suggestion in earlier chats. It preserves decisions, substantive requirements, research sources, evidence, links and workflow. To add a full verbatim conversation export later, verify rights/privacy and explicitly mark provenance/date; never claim the missing text was recovered.
