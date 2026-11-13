# Evaluation and benchmark methodology

## Purpose
Evaluate whether VideoGen is useful and competitive **without inventing results**. Keep model/engine inference and application UX scores separate.

## Proposed weighted product dimensions (initial planning weights)
- Visual image/video quality: 25%
- Multi-shot character/reference consistency: 25%
- Motion and camera control: 15%
- Prompt adherence: 15%
- Generation time + cost per accepted result: 10%
- Editing/creator workflow usability: 10%

These weights are a hypothesis for movie-focused creators, not market research or measured scores. Revisit with user feedback.

## Task suite
- 10 common short prompt tasks: still images -> video with natural movement, cinematic landscapes, action, talking character.
- 10 identity-continuity tasks: same subject in changed locations/wardrobe, multiple camera angles, two-person interactions.
- 5 camera motion / reference motion tasks.
- 5 audio-video tasks (speech intelligibility, lip-sync, SFX/music alignment).
- 3 full workflows: create a 10s clip, edit the clip, stitch a coherent 60s sequence.

## Reproducibility
Version, checkpoint hash, license, prompt, negative prompt, conditioning images, seed, scheduler, denoise steps, resolution, fps, duration, hardware, quantization, offload, total time, VRAM peak and artifact SHA. For hosted competitors, report their version/date and limitations around hidden internal settings.

## Measurement
1. Run multiple seeds and repeat evaluations; don't cherry-pick only the best clips.
2. Track generation **success rate**, accepted-output rate, rerender count and median/p95 latency.
3. Ask blinded evaluators to score identity consistency, motion, artifact frequency, adherence and usefulness.
4. Use automated checks for MP4 decodability, fps, dimensions, audio track, duration and file integrity.
5. For TTS record intelligibility, speaker consistency, transcription agreement and latency; human reviews for prosody.
6. For film grade temporal identity drift, wardrobe/background continuity, cuts and narration synchronization.
7. For optimization compare same model/version/prompt/hardware/quality settings; accelerated outputs may diverge and must be quality-scored.

## Claim policy
No statement such as "2x faster", "same quality as Higgsfield", "8 GB works" or "industry #1" without a linked dataset, environment and run record. Upstream README claims may be cited as upstream claims but aren't our measurements.

## Benchmark result template
Date | Task | Input version | Engine | Checkpoint | GPU | VRAM peak GiB | Gen seconds | Clip length | Success | Human score | Cost | Output hash | Notes

**Baseline status as of 2026-11-13: no VideoGen hardware benchmarks have been performed by this repository.**
