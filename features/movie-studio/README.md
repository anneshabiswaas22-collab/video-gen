# Movie studio

Turn scripts and storyboards into editable scenes, shots and takes, then assemble an approved timeline. Keep human approval over generated plans, shot replacements, dialogue and final exports.

**Current status:** specified product direction; no owned timeline editor, director agent or coherent generated movie is verified in this checkout.

## Scope and first delivery

Build scene/shot/take versioning and an editable short sequence before attempting a feature-length pipeline. Support regenerating one shot without losing previous takes, track source assets and choices, and assemble media with a reviewed export tool. A script suggestion must never silently authorize spending or arbitrary tool execution.

Traceability: [movie design](DESIGN.md), [M5 roadmap](../../docs/product/ROADMAP.md), [MOV-01–06 and AI-01–03 registry](../../docs/product/FEATURE_REGISTRY.md). This feature combines accepted outputs from [image](../image-studio/README.md), [video](../video-studio/README.md), [audio](../audio-studio/README.md) and [character continuity](../character-continuity/README.md). A learner may explicitly export an English practice scene into a creative project; practice history is not shared automatically.

## Dependencies and acceptance

Reuse the shared project/asset records, asynchronous job system and media tooling; evaluate existing timeline/editing components before implementing new ones. See [architecture](../../docs/architecture/ARCHITECTURE.md), [data model](../../docs/architecture/DATA_MODEL.md) and [reuse rules](../../docs/research/REUSE_FIRST.md).

CPU checks should verify shot history, repeatable timeline serialization, permissions and export planning. The M5 demonstration needs a playable 60-second sequence with repeat characters, individually replaceable shots, subtitles and measured continuity review. **End-to-end/GPU demonstration: NOT RUN.** A 20–120 minute pipeline remains a future orchestration and editing goal, not a guarantee of coherent single-prompt movie generation.
