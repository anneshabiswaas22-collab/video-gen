# Functional documentation collections

Choose by responsibility: [product](product/INDEX.md), [architecture](architecture/INDEX.md), [operations](operations/INDEX.md), [research](research/INDEX.md), [quality](quality/INDEX.md), [security](security/INDEX.md), [design](design/INDEX.md), [development](development/INDEX.md), [repository](repository/INDEX.md), [memory](memory/INDEX.md).

See [the complete structure](../PROJECT_STRUCTURE.md). All files below have been moved into these collections; the earlier reading list remains with repaired links.

# Documentation index

**Start here:** [project charter](product/PROJECT_CHARTER.md) -> [architecture](architecture/ARCHITECTURE.md) -> [feature registry](product/FEATURE_REGISTRY.md) -> [roadmap](product/ROADMAP.md) -> [contributing](../CONTRIBUTING.md).

| File | Purpose |
|---|---|
| [PROJECT_CHARTER.md](product/PROJECT_CHARTER.md) | Mission, target users, competitive positioning, goals, non-goals |
| [COMPETITORS.md](product/COMPETITORS.md) | Feature-by-feature benchmarking approach; do not claim #1 |
| [ARCHITECTURE.md](architecture/ARCHITECTURE.md) | Owned monorepo and pluggable inference service boundaries |
| [API_CONTRACT.md](architecture/API_CONTRACT.md) | Proposed jobs, projects, models, artifacts and lifecycle |
| [FEATURE_REGISTRY.md](product/FEATURE_REGISTRY.md) | Image/video/audio/3D/film/AI agent capabilities and status |
| [OPEN_SOURCE_STACK.md](research/OPEN_SOURCE_STACK.md) | Shortlist of reusable public repositories and candidates |
| [REUSE_FIRST.md](research/REUSE_FIRST.md) | Credit-saving dependency and code reuse policy |
| [ROADMAP.md](product/ROADMAP.md) | Phased milestones, dependencies and acceptance criteria |
| [GPU_COLAB.md](operations/GPU_COLAB.md) | GPU discovery, storage, limits, experiments and deployment |
| [DESIGN.md](../features/movie-studio/DESIGN.md) | Character consistency, shot graph, editing and assembly |
| [LICENSE_SECURITY.md](security/LICENSE_SECURITY.md) | License diligence, trust boundaries and deployment safety |
| [BENCHMARKS.md](quality/BENCHMARKS.md) | Quality, cost, reliability and competitor evaluation |
| [DECISIONS.md](architecture/DECISIONS.md) | Architecture decisions, unresolved points, corrections |
| [BUILD_RUN.md](operations/BUILD_RUN.md) | Local/Colab execution expectations and preflight status |

**Status vocabulary:** IDEA = only envisioned; CANDIDATE = evaluated as possible dependency; SPECIFIED = interface/acceptance criteria documented; IMPLEMENTED = code merged and tests executed; GPU VERIFIED = genuine artifact generated on named hardware; RELEASED = end-user deployment verified. Do not upgrade a label based only on prose.

Review model versions, upstream commit SHAs, licenses, hosted API pricing and GPU requirements at integration time; previous conversations included preliminary claims that require independent verification.

## Additional handoff files
- [Current status and first issues](development/STATUS.md)
- [Project history](memory/PROJECT_HISTORY.md)
- [Codex start prompt](development/CODEX_START_HERE.md)
- [Cost control](operations/COST_PLAN.md)
- [Test plan](quality/TEST_PLAN.md)
- [User experience](design/UI_UX.md)
- [Data model](architecture/DATA_MODEL.md)
- [Dependency register](research/DEPENDENCY_REGISTER.csv)
- [Colab preflight notebook](../notebooks/colab/00_gpu_preflight.ipynb)

## Full historical source repository catalog

- [ALL_RECOMMENDED_REPOSITORIES.txt](research/ALL_RECOMMENDED_REPOSITORIES.txt) — 54 previously discussed GitHub repositories and practical use cases, with research/compatibility cautions.

## Current combined product and repository recovery

- [Feature-oriented product entry points](../features/README.md)
- [Combined product idea](product/PROJECT_IDEA.txt)
- [Detailed English-speaking AI friend idea](../features/english-speaking-friend/PROJECT_IDEA.txt)
- [Repository analysis and path changes](repository/REPOSITORY_REORGANIZATION.md)
- [Recovery reports and preserved imports](../AnalyseFuture/README.md)
- [Complete file inventory](../AnalyseFuture/repository-inventory/COMPLETE_FILE_INVENTORY.txt)
- [Feature inventory](../AnalyseFuture/analysis/FEATURE_INVENTORY.txt)
- [Security findings and review limits](../AnalyseFuture/security-reports/SECURITY_AUDIT.txt)
- [Validation outcomes](../AnalyseFuture/migration-history/TEST_AND_VALIDATION_REPORT.txt)
- [Future product vision and roadmap](product/FUTURE_ROADMAP.txt)
