# Product feature registry

**This is a requirements inventory, not a list of implemented features.** All below are IDEA/SPECIFIED only unless a tracked PR and real demonstration upgrades their status. Model-specific controls appear only for engines which truly support them.

| ID | Feature | Scope | Priority | Proposed engine |
|---|---|---|---|---|
| IMG-01 | Text to image, preset resolution/seed/steps | Image | P0 | FLUX Schnell / Qwen |
| IMG-02 | Image-to-image, editing, inpainting, masking | Image | P1 | Qwen image-edit / ComfyUI |
| IMG-03 | Outpainting, aspect extension, object/background removal | Image | P1 | rembg, SAM2, suitable inpaint |
| IMG-04 | Upscaling/restoration, batch and provenance | Image | P1 | Real-ESRGAN |
| IMG-05 | Character/environment reference sheets & reusable assets | Image | P0 | App + image workflows |
| VID-01 | Text-to-video with visible settings | Video | P0 | Wan |
| VID-02 | Image-to-video with reproducible references | Video | P0 | Wan |
| VID-03 | Video-to-video, motion transfer, character animation | Video | P1 | Wan Animate / compatible workflows |
| VID-04 | First/last frame, extension, loop, reshoot | Video | P1 | Supported model adapters |
| VID-05 | Camera presets, choreography, shot control | Video | P1 | Supported control models |
| VID-06 | Video upscaling, interpolation, stabilization | Video | P2 | Existing libraries |
| AUD-01 | Text-to-speech / voice selection / narration | Audio | P0 | Kokoro |
| AUD-02 | Multi-speaker, dubbed dialogue, lip-sync | Audio | P1 | VibeVoice / MuseTalk |
| AUD-03 | Music and SFX | Audio | P1 | ACE-Step / other licensed models |
| AUD-04 | Transcription, captions, alignment, language | Audio | P1 | faster-whisper |
| MOV-01 | Script -> storyboard -> shot plan | Movie | P1 | Own director + templates |
| MOV-02 | Character/wardrobe/scene continuity ledger | Movie | P1 | Own continuity engine |
| MOV-03 | Multi-track timeline, clips, transitions, export | Movie | P1 | Reuse editor concepts + FFmpeg |
| MOV-04 | Regenerate individual shot without losing history | Movie | P1 | Own scene/shot versioning |
| MOV-05 | 60s coherent movie demonstration | Movie | P1 | End-to-end workflow |
| MOV-06 | 20–120 minute movie pipeline | Movie | P3 | Scalable orchestration + editing |
| AI-01 | Prompt polishing, planning, shot suggestions | Agent | P1 | LLM/agent orchestration |
| AI-02 | Model recommendation by capability and GPU budget | Agent | P1 | Rules first, LLM optional |
| AI-03 | Human approvals, tool authorization and agent audit | Agent | P1 | Own guardrails |
| SYS-01 | Accounts, projects, asset library, downloads | Platform | P0 | Own app |
| SYS-02 | Async queue, progress, cancellation, retries | Platform | P0 | FastAPI + worker |
| SYS-03 | ComfyUI workflow and model registry | Platform | P0 | ComfyUI adapter |
| SYS-04 | GPU detection, offload, quantization, performance logs | Platform | P0 | Worker, LightX2V candidate |
| SYS-05 | Colab research notebook; eventual dedicated workers | Platform | P0 | Notebook + worker API |
| SYS-06 | Usage pricing, budget guardrails, billing | Platform | P2 | Own accounting; provider later |
| SYS-07 | Model/LoRA uploads, fine-tune experiments | Platform | P3 | Musubi Tuner, after GPU proof |
| SYS-08 | Multi-user permissions, privacy, safety, abuse prevention | Platform | P1 | Own platform controls |
| 3D-01 | Image to editable 3D, environments, 3D staging | Future | P3 | Hunyuan3D / others verify |

## Priority meanings
P0 = first end-to-end working product; P1 = key differentiation; P2 = growth; P3 = expensive research/later. Do not code P3 before core generation works.

## Traceability
For every implemented feature, add issue/PR link, upstream version, license check, tests and real output evidence. Use a feature flag for capabilities not currently available on the selected GPU. Maintain accessibility and honest error states for unsupported models.

## Combined-product learning feature — added 2026-11-17

The original 33 requirements above remain. These additional requirements are
**IDEA**, not implemented. They share reviewed platform/audio/asset interfaces
but keep learning records isolated from studio publishing.

| ID | Feature | Scope | Delivery gate |
|---|---|---|---|
| ENG-01 | Text conversation, meaning-preserving English alternatives, ambiguity questions | English friend | T0 teacher-reviewed text pilot |
| ENG-02 | English/Bangla push-to-talk, editable transcripts, replay and fallback | English friend | T1 measured speech evaluation |
| ENG-03 | Disclosed, licensed synthetic avatar and optional correction modes | English friend | T1 accessibility and rights checks |
| ENG-04 | Opt-in phrase review, consent, deletion and learning-data isolation | English friend | T1 privacy tests and adult pilot |
| ENG-05 | Streaming turns, interruption and additional evaluated languages | Research | T2 evidence and budget required |

See [the guide](../features/english-speaking-friend/README.md) and
[detailed idea](../features/english-speaking-friend/PROJECT_IDEA.txt).
All six product domains are indexed in [features](../features/README.md).
