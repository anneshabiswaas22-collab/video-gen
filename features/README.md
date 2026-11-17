# Combined product features

VideoGen combines a creative studio with an English-speaking AI friend. Each folder below owns one feature's scope, development entry point and acceptance criteria. Shared architecture, licensing, operational rules and historical handoffs remain in [docs](../docs/README.md); preserved third-party imports remain in [AnalyseFuture](../AnalyseFuture/README.md).

The owned local API, CPU mock studio and English phrase-practice prototype now run here. Other feature domains remain plans. No GPU generation or production service is verified. See [implementation progress](../docs/development/IMPLEMENTATION_PROGRESS.md) for exact capabilities and remaining integrations.

| Folder | User outcome | Existing roadmap / registry |
|---|---|---|
| [image-studio](image-studio/README.md) | Create and edit still images and reference sheets | M1; IMG-01–05 |
| [video-studio](video-studio/README.md) | Generate and revise short clips | M2; VID-01–06 |
| [audio-studio](audio-studio/README.md) | Speech, captions, music and sound finishing | M3; AUD-01–04 |
| [movie-studio](movie-studio/README.md) | Assemble versioned scenes and shots into films | M5; MOV-01–06, AI-01–03 |
| [character-continuity](character-continuity/README.md) | Reuse consented characters, looks and environments | M5; IMG-05, MOV-02 |
| [english-speaking-friend](english-speaking-friend/README.md) | Practise English with a friendly speaking avatar and multilingual help | ENG-01 / T0 bounded CPU prototype; real model/voice evaluation pending |

## How the features fit together

The proposed shared platform provides identity, projects, consent records, asset metadata, model capabilities, cost limits and observability. The creative features use asynchronous jobs for image, clip and film generation. The English friend needs a separate interactive session path for speech recognition, turn-taking, correction, speech output and avatar display. A slow video-generation job must not block a conversation turn.

The friend may use a licensed avatar prepared through the creative studio, and a learner may explicitly save a practice scene as a creative project. Sharing an account does not grant permission to reuse private recordings, learning history or uploaded likenesses. Keep learning records separate and require explicit consent for exports or creative reuse.

## Development order and evidence

Complete the shared M0 audit and owned CPU mock path first. Develop one measurable end-to-end feature at a time, following the [roadmap](../docs/product/ROADMAP.md) and [test plan](../docs/quality/TEST_PLAN.md). The learning feature can begin with text and push-to-talk interaction before photorealistic video. It does not depend on completing long-form movie generation.

Every capability needs its own issue, pinned dependency and license review, runnable checks, limitations and evidence before its status changes. Candidate tools in preserved imports are research references, not automatically approved dependencies. No paid APIs, model downloads or GPU spending are authorized by this folder structure.
