# Audio studio

Create narration, dialogue, captions, sound effects and music, then mix them with media. This feature also supplies reusable speech components to the English-speaking friend, subject to different latency and privacy requirements.

**Current status:** planned; no owned speech or music generation service is verified in this checkout. Model names in older plans are candidates, not installed capabilities.

## Scope and first delivery

Start with licensed text-to-speech, explicit voice choice and captioned media assembly. Add transcription, alignment, multi-speaker dialogue, dubbing and music/SFX through separately reviewed integrations. Preserve original speech and edited takes so users can compare revisions.

Traceability: [M3 roadmap](../../docs/ROADMAP.md), [AUD-01–04 registry](../../docs/FEATURE_REGISTRY.md), [source candidates](../../docs/OPEN_SOURCE_STACK.md). The [movie studio](../movie-studio/README.md) consumes mastered tracks; the [English friend](../english-speaking-friend/README.md) consumes interactive transcription and speech output. Reuse adapters where appropriate, while keeping private practice recordings separate from creative assets.

## Dependencies and acceptance

Evaluate existing ASR/TTS tools and FFmpeg before building replacements. Pin releases and review code, voice, weight and commercial-use rights separately. Voice cloning is outside the initial delivery; a real person's voice or likeness requires specific permission and must not be impersonated.

CPU tests should cover transcript/caption timestamps, format validation, permission checks and recoverable failures. Functional acceptance requires audible, decodable speech and correctly aligned subtitles in a playable export. Evaluate intelligibility and transcription errors with representative speakers rather than treating accent differences as mistakes. Measure conversational latency separately from offline rendering. **Model/hardware validation: NOT RUN.**
