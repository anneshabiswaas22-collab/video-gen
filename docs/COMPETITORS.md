# Competitive benchmarking: Higgsfield, Runway, Flow, Kling and adjacent studios

## Market positioning
Our target is a **competitive experience**, not copying competitors' exact UI, assets, terms or proprietary models. There is no reliable blanket "number one" ranking across image, video, film editing and audio. Evaluate per feature, by date and model version.

| Benchmark product | Capabilities to inspect | Our intended product response |
|---|---|---|
| Higgsfield | Camera presets, motion effects, ad/creator workflows, image/video studio | Camera-conditioned effects, creator UX, repeatable presets |
| Runway | Video quality, motion consistency, creative controls and editing | Quantitative quality and editing comparison |
| Google Flow | Shot creation, reference assets, scene planning and film workflow | Our shot graph + assets + film planning |
| Kling | Identity and motion, image references, audio-video when available | Character continuity and motion model adapters |
| CapCut/Premiere/DaVinci (adjacent) | Timeline ergonomics, subtitles, export, professional control | Efficient non-destructive timeline and FFmpeg pipeline |
| FreeField/ComfyUI | Open-source workflow reuse, model breadth, GPU capabilities | Reuse infrastructure, build own UX and differentiated direction |

## Competitive evaluation method
1. Choose a precise product version, date, allowed inputs and equivalent settings.
2. Select task categories: portrait/dialogue, people moving, camera moves, environment, multi-character continuity, editing, audio-sync and generation reliability.
3. Match inputs, clip lengths, resolution and review conditions as closely as models permit; publish any unavoidable difference.
4. Blind-score by independent reviewers; calculate latency, failed outputs, cost per usable clip, identity drift and GPU expense.
5. Separate **model fidelity** (may require frontier research/training) from **platform features** (can be built with software).
6. Save model/version/seed/prompt/settings and legally shareable outputs.
7. Update regularly; "best model" claims stale quickly.

## Proposed differentiation thesis
A creator should be able to make and maintain a coherent multi-scene film with reusable characters and controllable reshoots, rather than repeatedly generate disconnected clips. Focus development effort on continuity, shot control, reproducibility, editable timeline, accessible defaults, and cost transparency.

## Explicit caveats
- Competitor feature descriptions here are research prompts, not current capability guarantees.
- Some "free" studio clones simply call paid APIs; test for real local inference.
- Quality superiority cannot be determined from GitHub stars or number of features.
