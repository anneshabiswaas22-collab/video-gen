# English-speaking AI friend

Practise English with a friendly speaking avatar. The learner can speak English, Bangla or another supported language, receive a natural English version of their intended meaning, hear gentle suggestions such as “You could say it this way,” and continue the conversation.

**Current status: IDEA.** This folder contains the feature brief and [detailed project idea](PROJECT_IDEA.txt). There is no implemented tutor, live avatar service, verified translation coverage or measured learning outcome in this checkout.

## Scope and first delivery

Start with text and push-to-talk, English and Bangla evaluation, editable transcripts, optional corrections, speech playback and a simple disclosed synthetic avatar. Let learners choose conversation-first, correction-after-turn or review-at-end modes. Ask about uncertain speech or meaning rather than confidently correcting a transcription error. Treat valid dialects and accents respectfully.

Later features can include interruption handling, pronunciation practice, role-play scenarios, spaced review and richer avatar animation. Support for every language, flawless correction, human-equivalent friendship and low-cost photorealistic live video are not initial promises.

## Relationship to the combined product

The friend shares approved voice adapters from the [audio studio](../audio-studio/README.md), avatar assets from [image creation](../image-studio/README.md) and consented identity preferences from [character continuity](../character-continuity/README.md). Optional practice-scene exports can feed the [movie studio](../movie-studio/README.md).

Conversation needs an interactive session path rather than waiting for asynchronous generated-video jobs. Share platform authentication, consent, cost limits and monitoring, while separating learning records from creative projects. Do not record the learner's camera or reuse conversations for training or asset creation by default.

## Acceptance and next work

Register a bounded learning-feature milestone alongside the existing [roadmap](../../docs/ROADMAP.md); review current ASR, translation, language-model, TTS and avatar candidates under the [reuse](../../docs/REUSE_FIRST.md) and [license/security](../../docs/LICENSE_SECURITY.md) rules before installation.

CPU checks should exercise transcript edits, meaning-preserving corrections, unsupported languages, consent/deletion and failure recovery. Human evaluation with Bangla-English speakers and an English educator should measure correction usefulness, meaning preservation and false corrections. Measure real turn latency and speech intelligibility on chosen hardware. Any numeric goals in the idea document are targets until measured. **Tutor behavior, language coverage, avatar rendering and hardware checks: NOT RUN.**
