# Project structure

This repository combines the VideoGen creative studio and an English-speaking AI friend. Its files are grouped by feature or shared responsibility. The layout preserves previous project work and separates owned plans from imported reference material.

The recovered owned CPU studio now runs alongside a feature-owned English phrase-practice prototype. These are local development capabilities, not a production generation service or a verified general-AI tutor. See [implementation progress](docs/development/IMPLEMENTATION_PROGRESS.md) and [validation](docs/quality/IMPLEMENTATION_VALIDATION.md).

## Start here

- [README](README.md): current project overview and entry points.
- [Combined project idea](docs/product/PROJECT_IDEA.txt): the complete product direction.
- [Feature map](features/README.md): feature ownership and delivery boundaries.
- [Project memory](docs/memory/PROJECT_MEMORY.md): prior decisions and historical evidence.
- [Current development status](docs/development/STATUS.md): implementation status and next work.
- [Current reorganization record](docs/repository/FUNCTIONAL_REORGANIZATION.md): what moved and why.

Historical handoffs preserve older repository URLs, branches and verification records. Treat those as dated evidence, not proof that code from another branch or repository exists in this checkout.

## Main layout

```text
video-gen/
├── README.md                     Project entry point
├── PROJECT_STRUCTURE.md           This directory guide
├── AGENTS.md                      Instructions for future coding agents
├── CONTRIBUTING.md                Contributor workflow
├── .env.example                  Example configuration; no real credentials
├── .github/                      Repository automation and issue/PR templates
├── apps/web/                     Next.js entrypoints and creative studio
├── services/                     Shared API and CPU mock worker
├── integrations/                 Typed external-engine boundaries
├── packages/schemas/             Shared creative contracts
├── tests/                        Shared API/worker and browser checks
├── features/                     Feature-owned behavior, UI and specifications
├── docs/                         Shared product and engineering knowledge
├── scripts/                      Maintenance and hardware utilities
├── notebooks/                    Interactive research notebooks
└── AnalyseFuture/                Preserved imports and material to evaluate
```

The root contains project entry points and repository configuration. A feature belongs under `features/`; cross-feature policy or architecture belongs under the appropriate `docs/` category. Imported engines remain separate from owned product code.

## Feature folders

```text
features/
├── README.md
├── image-studio/
│   └── README.md
├── video-studio/
│   └── README.md
├── audio-studio/
│   └── README.md
├── movie-studio/
│   ├── README.md
│   └── DESIGN.md
├── character-continuity/
│   └── README.md
└── english-speaking-friend/
    ├── README.md
    ├── PROJECT_IDEA.txt
    ├── backend/english_friend/    Coaching, provider, routes, consent-aware storage
    ├── web/                      Practice UI, types and HTTP contract tests
    └── tests/                    Domain, provider and API/privacy checks
```

| Folder | Responsibility |
|---|---|
| `image-studio` | Image generation/editing and visual reference creation. |
| `video-studio` | Short clip generation, revisions and supported motion controls. |
| `audio-studio` | Speech, captions, narration, sound and media finishing. |
| `movie-studio` | Storyboards, scene/shot/take history, timeline and film assembly. |
| `character-continuity` | Consented character references, identity, wardrobe and environment records. |
| `english-speaking-friend` | Friendly English practice, meaning-preserving corrections, multilingual support and an avatar. |

Features share proposed identity, consent, asset metadata, model capabilities and cost controls. Generated media uses asynchronous jobs. The English friend needs a separate interactive conversation path so a slow video render cannot block a speaking turn. Private learning recordings do not automatically become creative assets.

The English feature now contains an implemented bounded prototype; the other feature folders remain plans. Shared API/worker entrypoints are in services, web routing in apps, and feature behavior stays in the feature folder. The original owned M0 code was recovered rather than rebuilding it or executing archived third-party engines.

## Shared documentation

```text
docs/
├── README.md
├── product/
│   ├── PROJECT_CHARTER.md
│   ├── PROJECT_IDEA.txt
│   ├── ROADMAP.md
│   ├── FUTURE_ROADMAP.txt
│   ├── FEATURE_REGISTRY.md
│   └── COMPETITORS.md
├── architecture/
│   ├── ARCHITECTURE.md
│   ├── API_CONTRACT.md
│   ├── DATA_MODEL.md
│   └── DECISIONS.md
├── operations/
│   ├── BUILD_RUN.md
│   ├── GPU_COLAB.md
│   └── COST_PLAN.md
├── research/
│   ├── OPEN_SOURCE_STACK.md
│   ├── REUSE_FIRST.md
│   ├── ALL_RECOMMENDED_REPOSITORIES.txt
│   └── DEPENDENCY_REGISTER.csv
├── quality/
│   ├── BENCHMARKS.md
│   └── TEST_PLAN.md
├── security/
│   └── LICENSE_SECURITY.md
├── design/
│   └── UI_UX.md
├── development/
│   ├── STATUS.md
│   ├── CODEX_START_HERE.md
│   ├── TECHNICAL_DEBT.txt
│   ├── NEXT_DEVELOPER_INSTRUCTIONS.txt
│   └── WORK_PROGRESS.txt
├── repository/
│   ├── FUNCTIONAL_REORGANIZATION.md
│   ├── REPOSITORY_REORGANIZATION.md
│   ├── GALLERY_CONSOLIDATION.md
│   ├── GALLERY_CONSOLIDATION.json
│   └── FILE_PLACEMENT.json
└── memory/
    ├── README.md
    ├── PROJECT_MEMORY.md
    ├── PROJECT_HISTORY.md
    └── Other preserved continuity documents and portable handoffs
```

Each documentation group has an `INDEX.md` entry point. Product requirements, architecture, operations, research, quality, security, design and development status each have a distinct home. The movie-specific design belongs beside its feature. The English friend's detailed idea remains beside that feature, while the combined idea belongs to product documentation.

Memory documents preserve prior context. New decisions should update the current status and memory entry points without presenting historical claims as newly verified behavior.

## Utilities and research notebooks

```text
scripts/
├── maintenance/
│   ├── check_docs.py
│   └── check_structure.py
├── hardware/
│   └── gpu_preflight.py
└── development/
    ├── dev.sh                    Start the local API and web app
    └── smoke_mock.py             Executing CPU job/receipt check

notebooks/
└── colab/                        Existing Colab research material
```

Maintenance utilities describe repository integrity checks. Hardware utilities inspect runtime resources. Notebook placement follows its interactive research role. Neither hardware inspection nor a successful documentation check proves that model inference works.

## Preserved material in AnalyseFuture

```text
AnalyseFuture/
├── README.md
├── references/
│   ├── inference-engine/
│   │   └── comfyui/               Preserved ComfyUI package; wrapper flattened
│   └── workflow-studio/
│       └── freefield/             Preserved FreeField package
├── analysis/                      Findings and evaluation material
├── repository-inventory/
│   └── RELOCATION_MANIFEST.json   Earlier relocation inventory, preserved
├── security-reports/              Scoped security observations and limitations
├── migration-history/             Earlier migration records
└── project-history/
    └── README.before-reorganization.txt
```

The [file placement map](docs/repository/FILE_PLACEMENT.json) records every starting file's current collection, dependencies and destination. Earlier manifests are unchanged historical snapshots; resolve their paths through this current map.

The preserved FreeField gallery now collects all 118 example folders and the original index in `references/workflow-studio/freefield/web/examples/`. Its per-app folders already represent actual functions, including talking avatars, image editing and video effects. The [gallery collection map](docs/repository/GALLERY_CONSOLIDATION.md) traces each app's image/video/audio responsibility, original assets and metadata references. Sixty loose assets and their original index were reunited with 420 gallery assets. This is data recovery inside a reference package, not a production release. The metadata still refers to 162 missing MP4s; no media was invented. Starting the archived reference would expose those inherited missing links and its existing thumbnail autoplay; it is not started automatically.

Preserved source packages keep package-relative modules, configuration, assets, tests, license files and notices together. Splitting an imported engine into generic `components`, `utils` or extension-based folders would break imports and obscure its upstream structure. The archive groups packages by their role while preserving the package itself.

Imported media remains reference material with its original provenance limitations. Keeping a file does not establish permission to redistribute its contents commercially, run its code or use a depicted person's likeness. Check source, model-weight, voice and media rights separately before adoption.

## Rules for future changes

- Put feature-specific behavior and its explanation beside the owning feature.
- Keep shared contracts and infrastructure shared; avoid copying the same service into every feature.
- Keep engines and dependency-managed packages cohesive rather than mixing upstream source into owned feature folders.
- Update links and saved setup paths whenever a file or package moves.
- Preserve uncertain material in `AnalyseFuture` with a relocation record instead of silently discarding it.
- Add runnable application boundaries only when the corresponding code actually exists.
- Keep secrets, personal recordings, model weights and generated private media out of Git.

## Historical verification status for the sorting pass

No tests were run for this reorganization, as requested. Directory, relocation and link review are static inspection; they do not establish runtime correctness. Earlier test results remain historical and must not be represented as tests of the new paths. Application startup, inference, live conversation, avatar rendering and new-environment restoration require separate validation when authorized.

## Current implementation and source recovery

The subsequent owner request authorized implementation and tests. Current results
are in [IMPLEMENTATION_VALIDATION.md](docs/quality/IMPLEMENTATION_VALIDATION.md);
the no-tests paragraph above remains the historical sorting record.
[RECOVERED_APPLICATION_SOURCE.json](docs/repository/RECOVERED_APPLICATION_SOURCE.json)
identifies the exact earlier owned source and its source blobs. `.npmrc`, root
`package.json`/lock and `pyproject.toml`/development lock manage the active runtime.
No archived engine is included in those workspace/package lists.

## Complete handoff and per-file guide

[PROJECT_HANDOFF.md](PROJECT_HANDOFF.md) is the current homepage task/status manual.
[FILE_GUIDE.md](docs/repository/FILE_GUIDE.md) explains every source path, including
deep archive modules. [FOLDER_GUIDE.md](docs/repository/FOLDER_GUIDE.md) covers each
source directory and its responsibility. Other tools should work in scoped branches and request PR
review; this documentation does not run continuous background monitoring.
