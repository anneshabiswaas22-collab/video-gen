# Project decisions recovered from planning discussions (non-verbatim)

This is a developer handoff, not a transcript. Entries capture goals and instructions previously discussed, **not claims that code has been built**.

- **2026-11-12:** Owner wants own generative video software; prefers strongest reusable public repo(s), customization by GPT-powered Codex, and low-cost execution on Google Colab/Kaggle GPUs.
- Explored public generation models including Wan, HunyuanVideo, CogVideoX, SkyReels and FramePack, and distinction between model weights vs generation studio platforms.
- Explored FreeField as a Higgsfield-like open creative studio; considered using its workflow catalog alongside ComfyUI. User also wants image, speech, music, sound effects, camera motions, editing and animation.
- Discussed MiniMax, LTX, Qwen/FLUX and GPU feasibility; checked that proprietary video-provider APIs do not equate to open model weights.
- **2026-11-13:** Owner clarified the project should be an original **competitive software product**, not only a personal tool or copy of FreeField; benchmark Higgsfield, Runway, Google Flow and Kling.
- Selected strategy: one owned application monorepo with specialized integrated engines, not one huge imported codebase or one model for every feature.
- Prioritized original value: multi-shot character identity, AI director, camera/motion control, story-to-movie workflow, editable project history, model/compute selection and cost transparency.
- Owner explicitly requested minimizing Codex credits: investigate public maintained components before building things from scratch. Candidate additions include video editor, inference optimizers, lip-sync, background removal, video segmentation, upscaling, transcription and queue infrastructure.
- Owner gave the destination repository: https://github.com/anneshabiswaas22-collab/video-gen and requested a complete developer-ready handoff usable without the original conversation.

## Important related but separate creative project
Owner also has a 3D animated American-English family learning channel/film workflow, with six recurring characters and repeatable short shots. It can serve as a future product test scenario. Do **not** automatically merge its scripts/assets into this software repository or suggest that its videos were generated here.

## What has not occurred in this repository
No verified product frontend, no API, no local or Colab video generation, no commercial launch, no fine-tuned new foundation model, and no validated performance claims. Every milestone is future work unless linked to a tested PR.
