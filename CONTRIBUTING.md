# Contributing to VideoGen

Thanks for helping build a creator-first AI generation studio. Start with [README](README.md), [architecture](docs/ARCHITECTURE.md), [roadmap](docs/ROADMAP.md) and [AGENTS.md](AGENTS.md). This repository currently contains a *plan*, not a working AI service.

## First contribution path
1. Read the active milestone and [feature registry](docs/FEATURE_REGISTRY.md); claim one small, clearly bounded issue.
2. Create a topic branch from main and open a pull request. Do not push huge external model repositories or binary checkpoints.
3. Before writing new code, search for maintained libraries/workflows that already do the task. Document links, licenses, maintenance, implementation cost and VRAM demands.
4. Add or update tests and example data. Distinguish mocked CPU tests from real GPU tests.
5. Update implementation status and documentation; include what was tested, on which GPU, and what remains unknown.

## PR checklist
- [ ] Solves a linked issue/milestone; no unrequested unrelated refactor.
- [ ] Describes reuse-vs-build decision and upstream license obligations.
- [ ] No credentials, PII, model weights or large generated media.
- [ ] Unit/static tests pass; hardware tests stated honestly.
- [ ] Generation commands pin model/version, seed, steps, resolution and provenance.
- [ ] Includes a screenshot/video link only when produced and lawful to share.
- [ ] Documents migration/rollback and known failure modes where applicable.

## Development conventions (proposed until scaffold lands)
- Web: TypeScript + Next.js/React; typed schemas; accessible components.
- API: Python 3.11+ + FastAPI; OpenAPI; explicit validation with Pydantic.
- Storage: PostgreSQL for metadata, blob storage for assets; never use local temp files as the only durable copy.
- Workers: isolated Python process/container for ComfyUI / model adapter; async job queue and GPU scheduler.
- Testing: pytest for Python, frontend test runner selected in M0, end-to-end tests with test fixtures.
- Logging: JSON logs with correlation and job ID; omit prompt secrets and private uploads from logs.
- Versioned external model configs rather than hardcoded paths.

## Good starter issues
Review upstream license matrix; produce portable Colab preflight notebook; scaffold API health endpoint + mock worker; add structured model capability schema; add docs/link validation CI; implement an FFmpeg export adapter with synthetic test assets.

## Community
Use GitHub Issues for design questions and bug reports. Keep discussions respectful, disclose AI-assisted changes in PR notes, and avoid committing unlicensed benchmark clips or brand assets.

## License
No blanket project license is selected yet. Public visibility alone does not grant redistribution rights; contributors must avoid assuming this repo's original content/code has an open-source license until the owner chooses one. Every third-party component remains under its own terms.
