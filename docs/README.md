# Documentation index

**Start here:** [project charter](PROJECT_CHARTER.md) -> [architecture](ARCHITECTURE.md) -> [feature registry](FEATURE_REGISTRY.md) -> [roadmap](ROADMAP.md) -> [contributing](../CONTRIBUTING.md).

| File | Purpose |
|---|---|
| PROJECT_CHARTER.md | Mission, target users, competitive positioning, goals, non-goals |
| COMPETITORS.md | Feature-by-feature benchmarking approach; do not claim #1 |
| ARCHITECTURE.md | Owned monorepo and pluggable inference service boundaries |
| API_CONTRACT.md | Proposed jobs, projects, models, artifacts and lifecycle |
| FEATURE_REGISTRY.md | Image/video/audio/3D/film/AI agent capabilities and status |
| OPEN_SOURCE_STACK.md | Shortlist of reusable public repositories and candidates |
| REUSE_FIRST.md | Credit-saving dependency and code reuse policy |
| ROADMAP.md | Phased milestones, dependencies and acceptance criteria |
| GPU_COLAB.md | GPU discovery, storage, limits, experiments and deployment |
| MOVIE_STUDIO.md | Character consistency, shot graph, editing and assembly |
| LICENSE_SECURITY.md | License diligence, trust boundaries and deployment safety |
| BENCHMARKS.md | Quality, cost, reliability and competitor evaluation |
| DECISIONS.md | Architecture decisions, unresolved points, corrections |
| BUILD_RUN.md | Local/Colab execution expectations and preflight status |

**Status vocabulary:** IDEA = only envisioned; CANDIDATE = evaluated as possible dependency; SPECIFIED = interface/acceptance criteria documented; IMPLEMENTED = code merged and tests executed; GPU VERIFIED = genuine artifact generated on named hardware; RELEASED = end-user deployment verified. Do not upgrade a label based only on prose.

Review model versions, upstream commit SHAs, licenses, hosted API pricing and GPU requirements at integration time; previous conversations included preliminary claims that require independent verification.

## Additional handoff files
- [Current status and first issues](STATUS.md)
- [Project history](PROJECT_HISTORY.md)
- [Codex start prompt](CODEX_START_HERE.md)
- [Cost control](COST_PLAN.md)
- [Test plan](TEST_PLAN.md)
- [User experience](UI_UX.md)
- [Data model](DATA_MODEL.md)
- [Dependency register](DEPENDENCY_REGISTER.csv)
- [Colab preflight notebook](../notebooks/colab/00_gpu_preflight.ipynb)
