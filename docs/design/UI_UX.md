# Proposed user experience and major screens

## Brand position
An original pro-but-approachable AI creative studio. Do not duplicate competitor logos, interface assets or trademarked feature naming.

## App navigation
- Dashboard: recent projects, credits/usage, queued jobs, template discovery.
- Image Studio: prompt, style/reference controls, generate/edit/mask, side-by-side compare, download.
- Video Studio: text/image/video inputs, compatible model selector, aspect/fps/duration, advanced camera/motion tools, preview.
- Audio Studio: speech voices, music/SFX, transcript and captions.
- AI Director: script breakdown, scenes, reusable characters, storyboard, generation budget and human approval.
- Movie Editor: asset bin, multi-track video/audio/subtitle timeline, shot reshoots, export.
- Models/Settings: installed weights, supported GPU, estimates, licenses, error explanations, billing and privacy.

## User journey for first real product
1. Create project.
2. Enter prompt/upload an authorized image.
3. Choose model or use budget-aware suggested default.
4. Inspect actual capability constraints and estimated compute.
5. Generate; see progress and failure reasons; revisit a prior version.
6. Preview and download artifact; add to project/storyboard.

## Core UI rules
- Display true runtime/quality settings, not fictional switches.
- Explain unavailable controls clearly (e.g. camera conditioning unsupported by chosen checkpoint).
- Preserve prompt history, model version, seed and reference provenance.
- Drag/drop and keyboard-accessible controls; semantic labels; manageable layout on desktop/mobile.
- Never silently charge for a retry or trigger an expensive job twice.
- No fabricated previews or sample models mistaken for real generated output.

## Acceptance
In M4, a newcomer should finish an image -> video -> narrated MP4 workflow without documentation, with clear costs, obvious preview and downloadable result. Conduct 5+ observed usability sessions and document findings before calling UX competitive.
