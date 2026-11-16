# Public repositories, model candidates and integration decisions

**Not an installation list.** These are evaluated candidates for later milestone-specific integration. Exact version, maintainer status, license and checkpoint rights must be verified **at integration time**. A published repository is not necessarily a fully open training pipeline. A hosted API wrapper does not expose proprietary weights. Use the official source whenever possible.

## Core foundation
| Component | Repo | Use | Decision |
|---|---|---|---|
| ComfyUI | https://github.com/Comfy-Org/ComfyUI | Pluggable image/video/audio workflow runner and API | PRIMARY backend candidate; GPL-3.0 code implications |
| FreeField (neuregex) | https://github.com/neuregex/freefield | Workflow manifests, app catalog, presets and studio UX patterns | REFERENCE and selective permitted workflow reuse; do not automatically merge |
| SwarmUI | https://github.com/mcmonkeyprojects/SwarmUI | Alternate local frontend using ComfyUI | REFERENCE; don't run two frontends without need |
| OpenField | https://github.com/wexloops/openfield | Camera, characters, film references | STUDY architecture before adoption |
| Open Generative AI | https://github.com/Anil-matcha/Open-Generative-AI | Hosted-model gateway and catalog ideas | API-DEPENDENT; not free inference |
| WanGP | https://github.com/deepbeepmeep/Wan2GP | Low-memory model execution options | GPU benchmark candidate |
| FramePack | https://github.com/lllyasviel/FramePack | Longer sequence inference patterns | GPU benchmark candidate |

## Generation models
| Role | Official project | Notes |
|---|---|---|
| Video (first) | https://github.com/Wan-Video/Wan2.2 | Select TI2V/Animate variants per GPU; separate model/card license verification |
| Video/audio (alternative) | https://github.com/Lightricks/LTX-2 | Synchronized audio-video direction; check specific version/weights |
| Video alternative | https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5 | Compare quality/hardware after MVP |
| Video alternative | https://github.com/THUDM/CogVideo | Check model version/license |
| Long-video research | https://github.com/SkyworkAI/SkyReels-V2 | Research experimental long-form workflows |
| Images | https://github.com/black-forest-labs/flux | Select checkpoint by rights and hardware |
| Image editing | https://github.com/QwenLM/Qwen-Image | Image reference, edit workflow candidate |
| Speech | https://github.com/hexgrad/kokoro | Small TTS engine candidate for first audio output |
| Multi-speaker speech | https://github.com/microsoft/VibeVoice | Research speech variants and rights |
| Music | https://github.com/ace-step/ACE-Step-1.5 | Model support and licensing to validate |
| LoRA training | https://github.com/kohya-ss/musubi-tuner | Later, GPU-dependent experiments |
| Training/inference research | https://github.com/modelscope/DiffSynth-Studio | Alternative workflows/training, not MVP |

## Optimization / acceleration
| Project | Repo | Policy |
|---|---|---|
| LightX2V | https://github.com/ModelTC/LightX2V | Evaluate model support, memory, speed with matched prompts |
| Nunchaku | https://github.com/nunchaku-tech/nunchaku | Check GPU/hardware support and install complexity |
| Cache-DiT | https://github.com/vipshop/cache-dit | Quantization/caching candidate, benchmark degradation |
| FastVideo | https://github.com/hao-ai-lab/FastVideo | Research optimized video inference |
| ComfyUI built-ins | https://github.com/Comfy-Org/ComfyUI | Baseline before extra optimization layers |

## Editing, audio, scene and 3D
| Project | Repo | Why |
|---|---|---|
| FFmpeg | https://github.com/FFmpeg/FFmpeg | Essential encode, mux, trim, stitch, resample |
| OpenCut | https://github.com/opencutvideo/opencut | Web editor and timeline reference; verify repo identity before reuse |
| OpenChatCut | https://github.com/0xsline/OpenChatCut | AI editor/MCP research; assess AGPL |
| Editly | https://github.com/mifi/editly | Programmatic video composition |
| OpenMontage | https://github.com/bhakimi/openmontage | Film-production agent skill ideas; verify maturity/AGPL |
| Hildegard | https://github.com/baney75/hildegard | Character/camera and agent direction inspiration; assess AGPL |
| Remiqora | https://github.com/inikolax/remiqora-video | Movie assembly and continuity inspiration; early-stage |
| MuseTalk | https://github.com/TMElyralab/MuseTalk | Lip synchronization, check rights for media/dependencies |
| faster-whisper | https://github.com/SYSTRAN/faster-whisper | Transcription/subtitles |
| SAM 2 | https://github.com/facebookresearch/sam2 | Segment foreground objects in images/videos |
| rembg | https://github.com/danielgatis/rembg | Background removal |
| Real-ESRGAN | https://github.com/xinntao/Real-ESRGAN | Restoration/upscaling |
| Hunyuan3D | https://github.com/Tencent-Hunyuan/Hunyuan3D-2 | Future 3D assets (not included until validated) |

## Product infrastructure
| Repo | Use |
|---|---|
| https://github.com/shadcn-ui/ui | Interface components |
| https://github.com/xyflow/xyflow | Visual workflows and graph UI |
| https://github.com/langchain-ai/langgraph | Optional agent orchestration |
| https://github.com/tiangolo/fastapi | Python HTTP API |
| https://github.com/celery/celery | Background job queues |
| https://github.com/valkey-io/valkey | Broker/cache candidate |
| https://github.com/keycloak/keycloak | Authentication candidate |
| https://github.com/yjs/yjs | Optional real-time collaboration |

## Explicitly NOT our free/open weights
Kling Pro, Sora, Veo and Runway proprietary models: these are **competitive benchmarks or authorized paid provider API options**, not available source models merely because open-source wrappers exist. Prior chat references to "K 3.1 Pro" were ambiguous; do not treat an unverified third-party or fabricated release link as an official downloadable model.

## Reuse vs integrate vs study
- PRIMARY: one ComfyUI adapter, one concrete Wan variant, one image model, one TTS engine, FFmpeg, our API + UI.
- EVALUATE AFTER MVP: LightX2V speed, FreeField workflows, additional image/video/audio models, MuseTalk, SAM2, editor integrations.
- STUDY ONLY: early-stage film tools and proprietary API wrappers where compatibility/cost/license is unclear.
- DEFER: full model training, multiple competing backend engines at once, public Colab production hosting.
