# VideoGen — research sources, official links and upstream study register

**Snapshot date:** 2026-11-16. This is an index, not a statement of current maintenance, fit, license, checkpoint availability or commercial clearance. GitHub and model cards may change. Always independently verify current head and release before integrating.

## 1. VideoGen project sources (authoritative)

- [Main repository](https://github.com/anneshabiswaas22-collab/video-gen)
- [Current branches](https://github.com/anneshabiswaas22-collab/video-gen/branches)
- [Open pull requests](https://github.com/anneshabiswaas22-collab/video-gen/pulls)
- [Issues / milestones](https://github.com/anneshabiswaas22-collab/video-gen/issues)
- [GitHub Actions](https://github.com/anneshabiswaas22-collab/video-gen/actions)
- [M0.2 PR #8](https://github.com/anneshabiswaas22-collab/video-gen/pull/8) — real CPU mock, **not** image/video AI inference
- [M0.2 commit](https://github.com/anneshabiswaas22-collab/video-gen/commit/ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37)
- [Verified application CI](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390592)
- [Verified docs CI](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43741390571)
- [Existing initial project roadmap](../product/ROADMAP.md), [status](../development/STATUS.md), [architecture](../architecture/ARCHITECTURE.md), [feature registry](../product/FEATURE_REGISTRY.md), [reuse-first](../research/REUSE_FIRST.md), [security/license](../security/LICENSE_SECURITY.md), [Colab research plan](../operations/GPU_COLAB.md), [cost plan](../operations/COST_PLAN.md), [movie studio](../../features/movie-studio/DESIGN.md), [test plan](../quality/TEST_PLAN.md), [decisions](../architecture/DECISIONS.md), [data model](../architecture/DATA_MODEL.md), [API contract](../architecture/API_CONTRACT.md), [complete history](PROJECT_HISTORY.md).
- **Primary deep-study research and triage:** [PR #8 report](https://github.com/anneshabiswaas22-collab/video-gen/blob/ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37/docs/TWO_REPO_DEEP_STUDY.md). See source-level links and code/license analysis there.
- [Historical 54-repository study catalog](../research/ALL_RECOMMENDED_REPOSITORIES.txt) — full prior list retained as-is.

## 2. Exactly two deeply studied foundation repositories

### ComfyUI — external execution engine

**Official:** [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI). Snapshot SHA `258f880d0c026bfc22acab679858ab2e2c70573d` (2026-11-15 source inspection).

| Relevant official source | Why it matters |
|---|---|
| [LICENSE](https://github.com/Comfy-Org/ComfyUI/blob/258f880d0c026bfc22acab679858ab2e2c70573d/LICENSE) | GPL-3.0 source; assess actual distribution/derivative obligations |
| [server.py](https://github.com/Comfy-Org/ComfyUI/blob/258f880d0c026bfc22acab679858ab2e2c70573d/server.py) | HTTP/WS API, queue, history, model and node endpoints |
| [execution.py](https://github.com/Comfy-Org/ComfyUI/blob/258f880d0c026bfc22acab679858ab2e2c70573d/execution.py) | Node graph execution, validation, caches and scheduling |
| [comfy/model_management.py](https://github.com/Comfy-Org/ComfyUI/blob/258f880d0c026bfc22acab679858ab2e2c70573d/comfy/model_management.py) | GPU/VRAM/device policies |
| [Official Comfy documentation](https://docs.comfy.org/) | API/workflow guidance; verify versioned behaviors |
| [Repository tests and CI](https://github.com/Comfy-Org/ComfyUI/tree/258f880d0c026bfc22acab679858ab2e2c70573d/.github/workflows) | Versioning and validation patterns |

**Workflow integration strategy:** a reviewed API-format graph + typed input binding → `POST /prompt` → `prompt_id` → WebSocket/progress/history lookup → controlled, validated and SHA-256-hashed artifact in our storage. Never allow user graph uploads/custom nodes without review. Remote host must be private and authenticated; global cancel/interrupt semantics require investigation. Neither a typed adapter stub nor mock transport is real inference.

### FreeField — manifest and application pattern reference

**Official:** [neuregex/freefield](https://github.com/neuregex/freefield). Snapshot SHA `f0c2358a46c7008ff8503d4324b6cc8bc7657e75` (2026-11-15 source inspection). MIT application source; attached models, weights, workflows and media require separate licensing.

| Relevant official source | Why it matters |
|---|---|
| [LICENSE](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/LICENSE) | Verified MIT app-code license |
| [schema/app.schema.json](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/schema/app.schema.json) | Manifest input schema, node-field bindings, model/output/VRAM metadata |
| [apps/create-image/app.json](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/apps/create-image/app.json) | Manifest-specified UI, settings and workflow bindings |
| [apps/cinema-studio/app.json](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/apps/cinema-studio/app.json) | Camera/lens/light controls converted to supported prompting |
| [apps/cinema-video/workflow.api.json](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/apps/cinema-video/workflow.api.json) | Example ComfyUI API graph |
| [server/registry.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/server/registry.ts) | AJV schema and graph-binding validation |
| [server/runner.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/server/runner.ts) | Coercion, ranges, runtime workflow binding |
| [server/history.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/server/history.ts) | Generation history and media metadata |
| [server/guard.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/server/guard.ts) | Access gate/caps, not a universal production auth model |
| [infra/gateway.py](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/infra/gateway.py) | Private ComfyUI gateway/model switching |
| [tools/comfy_validate.py](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/tools/comfy_validate.py) | CPU graph acceptance checks without generation |
| [tools/catalog.py](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/tools/catalog.py) | Generated model pack / VRAM estimates |
| [lab/core.py](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/lab/core.py) | Benchmark/lab repeatability and memory metrics |
| [.github/workflows/validate.yml](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/.github/workflows/validate.yml) | Validated manifests/tests/builds |
| [test/runner.test.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/test/runner.test.ts) | Unit tests for workflow form and binding contracts |

**Do not:** copy FreeField proprietary-looking product branding, media galleries, full codebase, or any unauthorized weights. Reimplement *our own* typed, allowlisted version of its useful manifest patterns after M0, not 120 speculative apps.

## 3. Complete 54-repository historical catalog (clickable)

This table is **generated from** the existing `docs/research/ALL_RECOMMENDED_REPOSITORIES.txt` in this repo. It intentionally lists candidates outside the two primary foundation studies; don't confuse presence with approval. The historical existence check said 53/54 resolved and the Montagio URL was unavailable at that time. Avoid assuming repositories are maintained today.

| No. | Repository | Historical category | Adoption state |
|---:|---|---|---|
| 1 | [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 2 | [FreeField (neuregex)](https://github.com/neuregex/freefield) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 3 | [FreeField (droppedmyza)](https://github.com/droppedmyza/freefield) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 4 | [OpenField (wexloops)](https://github.com/wexloops/openfield) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 5 | [OpenField (VedSoni-dev)](https://github.com/VedSoni-dev/openfield) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 6 | [SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 7 | [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 8 | [EasyComfee](https://github.com/sintetizacom/easycomfee) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 9 | [Montagio](https://github.com/Jubzh-29/montagio) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 10 | [Hildegard](https://github.com/baney75/hildegard) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 11 | [Remiqora Video](https://github.com/inikolax/remiqora-video) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 12 | [NVAI-open](https://github.com/Mantux775/NVAI-open) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 13 | [Velorn](https://github.com/VelornLabs/velorn) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 14 | [Vanta](https://github.com/itsjwill/vanta) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 15 | [BeatDesign](https://github.com/BeatAPI/BeatDesign) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 16 | [OpenCut](https://github.com/opencutvideo/Opencut) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 17 | [OpenChatCut](https://github.com/0xsline/OpenChatCut) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 18 | [OpenMontage](https://github.com/bhakimi/openmontage) | CORE GENERATION PLATFORMS / HIGGSFIELD-STYLE STUDIO REFERENCES | STUDY ONLY — review exact license/model weights/version |
| 19 | [Wan 2.2](https://github.com/Wan-Video/Wan2.2) | VIDEO AND AUDIO-VIDEO FOUNDATION MODELS | STUDY ONLY — review exact license/model weights/version |
| 20 | [Wan 2.1](https://github.com/Wan-Video/Wan2.1) | VIDEO AND AUDIO-VIDEO FOUNDATION MODELS | STUDY ONLY — review exact license/model weights/version |
| 21 | [LTX-2 family](https://github.com/Lightricks/LTX-2) | VIDEO AND AUDIO-VIDEO FOUNDATION MODELS | STUDY ONLY — review exact license/model weights/version |
| 22 | [HunyuanVideo 1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | VIDEO AND AUDIO-VIDEO FOUNDATION MODELS | STUDY ONLY — review exact license/model weights/version |
| 23 | [CogVideo](https://github.com/THUDM/CogVideo) | VIDEO AND AUDIO-VIDEO FOUNDATION MODELS | STUDY ONLY — review exact license/model weights/version |
| 24 | [SkyReels V2](https://github.com/SkyworkAI/SkyReels-V2) | VIDEO AND AUDIO-VIDEO FOUNDATION MODELS | STUDY ONLY — review exact license/model weights/version |
| 25 | [FramePack](https://github.com/lllyasviel/FramePack) | VIDEO AND AUDIO-VIDEO FOUNDATION MODELS | STUDY ONLY — review exact license/model weights/version |
| 26 | [Wan2GP / WanGP](https://github.com/deepbeepmeep/Wan2GP) | VIDEO AND AUDIO-VIDEO FOUNDATION MODELS | STUDY ONLY — review exact license/model weights/version |
| 27 | [MiniMax H3](https://github.com/MiniMax-AI/MiniMax-H3) | VIDEO AND AUDIO-VIDEO FOUNDATION MODELS | STUDY ONLY — review exact license/model weights/version |
| 28 | [FLUX](https://github.com/black-forest-labs/flux) | IMAGE GENERATION AND EDITING | STUDY ONLY — review exact license/model weights/version |
| 29 | [Qwen Image](https://github.com/QwenLM/Qwen-Image) | IMAGE GENERATION AND EDITING | STUDY ONLY — review exact license/model weights/version |
| 30 | [Kokoro](https://github.com/hexgrad/kokoro) | SPEECH, MUSIC AND SOUND | STUDY ONLY — review exact license/model weights/version |
| 31 | [VibeVoice](https://github.com/microsoft/VibeVoice) | SPEECH, MUSIC AND SOUND | STUDY ONLY — review exact license/model weights/version |
| 32 | [ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5) | SPEECH, MUSIC AND SOUND | STUDY ONLY — review exact license/model weights/version |
| 33 | [MuseTalk](https://github.com/TMElyralab/MuseTalk) | SPEECH, MUSIC AND SOUND | STUDY ONLY — review exact license/model weights/version |
| 34 | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | SPEECH, MUSIC AND SOUND | STUDY ONLY — review exact license/model weights/version |
| 35 | [LightX2V](https://github.com/ModelTC/LightX2V) | OPTIMIZED INFERENCE / TRAINING | STUDY ONLY — review exact license/model weights/version |
| 36 | [Cache-DiT](https://github.com/vipshop/cache-dit) | OPTIMIZED INFERENCE / TRAINING | STUDY ONLY — review exact license/model weights/version |
| 37 | [Nunchaku](https://github.com/nunchaku-tech/nunchaku) | OPTIMIZED INFERENCE / TRAINING | STUDY ONLY — review exact license/model weights/version |
| 38 | [FastVideo](https://github.com/hao-ai-lab/FastVideo) | OPTIMIZED INFERENCE / TRAINING | STUDY ONLY — review exact license/model weights/version |
| 39 | [Musubi Tuner](https://github.com/kohya-ss/musubi-tuner) | OPTIMIZED INFERENCE / TRAINING | STUDY ONLY — review exact license/model weights/version |
| 40 | [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) | OPTIMIZED INFERENCE / TRAINING | STUDY ONLY — review exact license/model weights/version |
| 41 | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | VIDEO EDITING, RESTORATION, 3D AND MEDIA PIPELINE | STUDY ONLY — review exact license/model weights/version |
| 42 | [Editly](https://github.com/mifi/editly) | VIDEO EDITING, RESTORATION, 3D AND MEDIA PIPELINE | STUDY ONLY — review exact license/model weights/version |
| 43 | [SAM 2](https://github.com/facebookresearch/sam2) | VIDEO EDITING, RESTORATION, 3D AND MEDIA PIPELINE | STUDY ONLY — review exact license/model weights/version |
| 44 | [rembg](https://github.com/danielgatis/rembg) | VIDEO EDITING, RESTORATION, 3D AND MEDIA PIPELINE | STUDY ONLY — review exact license/model weights/version |
| 45 | [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | VIDEO EDITING, RESTORATION, 3D AND MEDIA PIPELINE | STUDY ONLY — review exact license/model weights/version |
| 46 | [Hunyuan3D 2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | VIDEO EDITING, RESTORATION, 3D AND MEDIA PIPELINE | STUDY ONLY — review exact license/model weights/version |
| 47 | [shadcn/ui](https://github.com/shadcn-ui/ui) | APP FRAMEWORK, WORKFLOW UI, JOBS, ACCOUNTS | STUDY ONLY — review exact license/model weights/version |
| 48 | [React Flow / xyflow](https://github.com/xyflow/xyflow) | APP FRAMEWORK, WORKFLOW UI, JOBS, ACCOUNTS | STUDY ONLY — review exact license/model weights/version |
| 49 | [LangGraph](https://github.com/langchain-ai/langgraph) | APP FRAMEWORK, WORKFLOW UI, JOBS, ACCOUNTS | STUDY ONLY — review exact license/model weights/version |
| 50 | [Keycloak](https://github.com/keycloak/keycloak) | APP FRAMEWORK, WORKFLOW UI, JOBS, ACCOUNTS | STUDY ONLY — review exact license/model weights/version |
| 51 | [Celery](https://github.com/celery/celery) | APP FRAMEWORK, WORKFLOW UI, JOBS, ACCOUNTS | STUDY ONLY — review exact license/model weights/version |
| 52 | [Valkey](https://github.com/valkey-io/valkey) | APP FRAMEWORK, WORKFLOW UI, JOBS, ACCOUNTS | STUDY ONLY — review exact license/model weights/version |
| 53 | [Yjs](https://github.com/yjs/yjs) | APP FRAMEWORK, WORKFLOW UI, JOBS, ACCOUNTS | STUDY ONLY — review exact license/model weights/version |
| 54 | [FastAPI](https://github.com/fastapi/fastapi) | APP FRAMEWORK, WORKFLOW UI, JOBS, ACCOUNTS | STUDY ONLY — review exact license/model weights/version |

## 4. Other relevant source and process links

- [Open source stack and shortlisting](../research/OPEN_SOURCE_STACK.md)
- [Dependency license register](../research/DEPENDENCY_REGISTER.csv) — main baseline may be behind PR #8 updates; see [PR dependency version](https://github.com/anneshabiswaas22-collab/video-gen/blob/ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37/docs/DEPENDENCY_REGISTER.csv).
- [Colab notebook](../../notebooks/colab/00_gpu_preflight.ipynb) and [GPU preflight script](../../scripts/hardware/gpu_preflight.py) — **hardware inspection only**, not inference proof.
- [ComfyUI GitHub issue/security pages](https://github.com/Comfy-Org/ComfyUI/security)
- [FreeField GitHub issue/security pages](https://github.com/neuregex/freefield/issues)
- [FastAPI](https://github.com/fastapi/fastapi), [Next.js](https://github.com/vercel/next.js), [FFmpeg](https://github.com/FFmpeg/FFmpeg), [Wan2.2](https://github.com/Wan-Video/Wan2.2), [Kokoro](https://github.com/hexgrad/kokoro), [LightX2V](https://github.com/ModelTC/LightX2V)

## 5. What must be rechecked when choosing a dependency

For every component, log **official URL**, repo HEAD and *chosen immutable version*, code license, downstream package dependencies, any GPL/AGPL rights obligations, **model-weight license separately**, commercially permitted uses, uploaded user-data restrictions, downloaded size/checkpoint hash, GPU/VRAM, security advisories, capability coverage and a reproducible test. Label **VERIFIED/PENDING/BLOCKED**. Never choose a benchmark model solely based on README speed/VRAM marketing. Source linking is not a distribution license, and ComfyUI separated into a process doesn't automatically eliminate copyleft obligations.
