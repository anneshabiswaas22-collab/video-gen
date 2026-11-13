# Product charter

## The ambition
Create an original, commercially viable AI Creative Studio that can compete in user value with Higgsfield, Runway, Google Flow and Kling. "Number one" is a long-term aspiration, **not a factual market ranking or launch promise**. We will benchmark leaders per task rather than assume one universally best competitor.

## User and origin
Owner wants to control their own software, built using GPT-6 Astra/Codex Cloud + maintained open-source components, and initially run video/image/audio inference using their Google Colab GPU; Kaggle is an optional experimentation runtime. Low cost, minimal duplicate development, and future commercial readiness are central requirements.

## Target users
- Creators turning a prompt or photograph into short videos for social media.
- Film/YouTube creators needing camera controls, reusable characters, shot continuity, music and post-production.
- Independent studios needing transparent costs, editable assets and reproducible projects.
- Developers integrating generation via APIs (future).

## Product pillars
1. **Image Studio**: text-to-image, image-to-image, edit/inpaint/outpaint, reference images, upscaling, backgrounds, character sheets.
2. **Video Studio**: text/image/video-to-video, motion references, first/last frame, extension, aspect ratio, cinematic effects, camera control through supported model conditioning.
3. **Audio Studio**: speech, narration, multi-voice, dialogue, transcription, subtitles, music, SFX, synchronized audio/video when supported.
4. **Movie Studio**: script -> storyboard -> shot plan -> scene generations -> voice/SFX/music -> editable timeline -> encode/export; regenerate a shot without rewriting whole production.
5. **Model/GPU Studio**: registry, model comparison, versioning, selective loading, VRAM budget, predictable jobs, cost metrics, fine-tune/LoRA later.
6. **AI Director**: assist prompts, composition, shots, continuity and model selection with human review.

## Key differentiators to build ourselves
- Character IDs and visual references that persist across projects and scenes; measurable identity drift.
- Editable scene graph and non-destructive regeneration.
- Intelligent model routing informed by capability, latency, GPU, quality and expense.
- Reproducible projects: prompt, seed, conditioning input, engine/version, settings, output provenance.
- Budget previews, accessible creator interface, reusable camera and story templates.

## Principles
- One product repo; many model engines behind adapters.
- Buy/rent compute when required, never assume Colab is production hosting.
- Reuse working, licensed tools before coding originals.
- Model quality != frontend workflow quality: do not claim compositing open models matches proprietary weights without a fair evaluation.
- No hidden paid-API dependency in the default local/offline feature path.
- Preserve creator rights, prevent impersonation/unsafe content where applicable, and honor third-party IP.
- Human editing/approval for expensive multi-shot jobs.

## What success looks like
First: one real image, one real video, one real voice output, saved with reproducible metadata. Next: a 60-second connected sequence with persistent characters, edited and exported. Long-term: a repeatable movie pipeline and a competitive creator product with measured quality, latency, reliability and cost, scalable beyond Colab.

## Scope boundary
This repository is the general-purpose video/image/audio platform. The separately discussed English-learning animated family series ("Maple House English") can be a **future test scenario**, not a dependency or assets to copy from another repository. Content production and this software platform remain independent projects.
