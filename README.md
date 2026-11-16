# VideoGen — Creative Studio + English AI Friend

One proposed product for creating images, videos, voices and editable movies,
and practising English with a friendly speaking avatar. The original studio
vision remains; the English companion is now a first-class feature.

**Current state:** product plans, engineering handoffs and CPU-tested third-party
references. This checkout has no owned production web/API stack, implemented
English tutor or verified GPU generation. Feature folders describe responsibilities,
not completed applications. Historical evidence from another repository is
labeled separately in [PROJECT_MEMORY.md](PROJECT_MEMORY.md).

Read or download the plain-text plans:

- [Combined product idea — PROJECT_IDEA.txt](PROJECT_IDEA.txt)
- [Detailed English AI friend idea](features/english-speaking-friend/PROJECT_IDEA.txt)
- [Full future vision and multi-year roadmap](AnalyseFuture/PROJECT_VISION_AND_FUTURE_ROADMAP.txt)

## Find a feature

| Feature folder | Intended outcome |
|---|---|
| [Image studio](features/image-studio/README.md) | Generate and edit images; prepare reference sheets |
| [Video studio](features/video-studio/README.md) | Create and revise short clips with supported controls |
| [Audio studio](features/audio-studio/README.md) | Speech, captions, music and sound |
| [Movie studio](features/movie-studio/README.md) | Assemble versioned scenes, shots and takes |
| [Character continuity](features/character-continuity/README.md) | Keep consented characters and environments reusable |
| [English-speaking friend](features/english-speaking-friend/README.md) | Practise with an AI avatar; get gentle English corrections and multilingual help |

[The feature map](features/README.md) explains shared services and development
order. Creative rendering uses asynchronous jobs; conversation needs a separate
interactive speech path. Private learning recordings do not become creative
assets without explicit consent. Start with English/Bangla and a simple licensed
avatar; universal languages and photorealistic live video are research goals.

## Repository organization and preservation

- `features/`: one guide per product feature, with status and acceptance criteria.
- `docs/`: shared architecture, roadmap, feature registry, licensing and history.
- `scripts/`, `notebooks/colab/`, `.github/`: shared validation, hardware inspection and CI.
- [AnalyseFuture](AnalyseFuture/README.md): imported ComfyUI/FreeField sources, examples and recovery reports.

All 2,131 bulk-import files are preserved byte-for-byte. Nothing was deduplicated
or silently discarded. See [the inventory and findings](docs/REPOSITORY_REORGANIZATION.md)
and [relocation manifest](AnalyseFuture/RELOCATION_MANIFEST.json). The
[previous README](AnalyseFuture/project-history/README.before-reorganization.txt)
is also preserved. Repository cleanup does not establish account security.

## Develop and verify

Read [AGENTS.md](AGENTS.md), [documentation index](docs/README.md),
[build/run instructions](docs/BUILD_RUN.md), [roadmap](docs/ROADMAP.md),
[feature registry](docs/FEATURE_REGISTRY.md) and [current status](docs/STATUS.md).
Root checks use Python's standard library:

```sh
python scripts/check_docs.py
python scripts/check_structure.py
python -m py_compile scripts/gpu_preflight.py scripts/check_docs.py scripts/check_structure.py
```

Introduce owned application code through bounded, tested milestones. Prefer
maintained, pinned integrations over copying model repositories. Review source,
model, voice and asset rights separately. No paid APIs, model downloads, training
or GPU rental without owner budget approval. CPU mocks are separate from real
hardware and media validation.

Current repository: [sarfiaroui-oss/video-gen](https://github.com/sarfiaroui-oss/video-gen).
Older `anneshabiswaas22-collab/video-gen` links remain historical provenance,
not proof its unmerged application code exists here. The preserved
[54-source catalog](docs/ALL_RECOMMENDED_REPOSITORIES.txt) remains research,
not an installation list. Project plans do not imply frontier-model parity.
