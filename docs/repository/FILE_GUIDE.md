# Every source file: responsibility guide

Read [PROJECT_HANDOFF.md](../../PROJECT_HANDOFF.md) for implemented features, limits
and the remaining task backlog. [FOLDER_GUIDE.md](FOLDER_GUIDE.md) explains **every
source directory**. This file and the two linked reference pages account for
every tracked or proposed source file in this delivery, including deeply nested
preserved packages. Ignored dependencies, build output, private local databases,
Git internals and caches are generated state, not source entries.

[FILE_PLACEMENT.json](FILE_PLACEMENT.json) retains original/current paths and
functional collections. Purpose descriptions come from code, module declarations,
content and package context; they do not claim that every preserved file was run,
visually inspected, licensed for all uses or formally security-audited.

## Preserved package file lists

- [Every ComfyUI inference-engine file](files/INFERENCE_REFERENCE.md): 1,306 files.
- [Every reference workflow-studio/gallery file](files/WORKFLOW_REFERENCE.md): 825 files,
  including the 61 reunited gallery fragments.

Those 2,131 imported files remain byte-identical. Their capabilities are reference
material, not completed owned product features. Package-relative modules,
resources, tests, licenses and example assets stay with their package.

## Root entrypoints and configuration

| File | Purpose / feature ownership |
|---|---|
| [.env.example](../../.env.example) | Documented local configuration names/defaults for API, worker, practice provider and storage; contains no real credentials. |
| [.gitignore](../../.gitignore) | Excludes local databases, transcripts, dependencies, caches, builds and other generated/private material from Git. |
| [.npmrc](../../.npmrc) | Ignored repository-local npm cache location for the cloud filesystem. |
| [AGENTS.md](../../AGENTS.md) | Standing engineering mission, reuse/rights rules, original-byte preservation, validation and continuation requirements. |
| [CONTRIBUTING.md](../../CONTRIBUTING.md) | Contributor workflow, original-source/model rights, scope, test evidence and review expectations. |
| [PROJECT_HANDOFF.md](../../PROJECT_HANDOFF.md) | Homepage continuation manual, implemented status, task backlog and PR review rules. |
| [PROJECT_STRUCTURE.md](../../PROJECT_STRUCTURE.md) | Functional directory/ownership guide and historical layout explanation. |
| [README.md](../../README.md) | Short current capability/setup entrypoint and prominent handoff link. |
| [eslint.config.mjs](../../eslint.config.mjs) | Root frontend lint discovery/configuration for workspace and feature source. |
| [package-lock.json](../../package-lock.json) | Locked npm dependency graph including workspace and patched test tools. |
| [package.json](../../package.json) | Root npm workspace, supported Node versions and development/verification commands. |
| [pyproject.toml](../../pyproject.toml) | Explicit owned Python package discovery, lesson-resource inclusion, pinned runtime requirements, pytest and lint settings. |
| [requirements-dev.lock](../../requirements-dev.lock) | Pinned tested Python development/audit dependencies layered on the owned runtime requirements. |

## .github

| File | Purpose / feature ownership |
|---|---|
| [.github/ISSUE_TEMPLATE/bug_report.md](../../.github/ISSUE_TEMPLATE/bug_report.md) | Optional manual bug-report fields; its presence does not authorize automated issue creation. |
| [.github/ISSUE_TEMPLATE/feature_request.md](../../.github/ISSUE_TEMPLATE/feature_request.md) | Optional manual feature-request proposal with scope/evidence; no issues are posted by this file. |
| [.github/pull_request_template.md](../../.github/pull_request_template.md) | Contribution review checklist for behavior, verification, provenance, costs and remaining limitations. |
| [.github/workflows/application-ci.yml](../../.github/workflows/application-ci.yml) | Owned CPU/application CI, excluding archived engines and GPU/model downloads |
| [.github/workflows/docs-check.yml](../../.github/workflows/docs-check.yml) | GitHub Actions workflow that checks required documentation, relative links and repository preservation. |

## Preserved evidence: README.md

| File | Purpose / feature ownership |
|---|---|
| [AnalyseFuture/README.md](../../AnalyseFuture/README.md) | Preservation collections, provenance and safe reference-use rules; these imports are not shipped product features. |

## Preserved evidence: analysis

| File | Purpose / feature ownership |
|---|---|
| [AnalyseFuture/analysis/CONSOLIDATION_REPORT.txt](../../AnalyseFuture/analysis/CONSOLIDATION_REPORT.txt) | Earlier analysis observation/snapshot retained with original provenance |
| [AnalyseFuture/analysis/DUPLICATE_ANALYSIS.txt](../../AnalyseFuture/analysis/DUPLICATE_ANALYSIS.txt) | Earlier analysis observation/snapshot retained with original provenance |
| [AnalyseFuture/analysis/FEATURE_INVENTORY.txt](../../AnalyseFuture/analysis/FEATURE_INVENTORY.txt) | Earlier analysis observation/snapshot retained with original provenance |
| [AnalyseFuture/analysis/REPOSITORY_AUDIT.txt](../../AnalyseFuture/analysis/REPOSITORY_AUDIT.txt) | Earlier analysis observation/snapshot retained with original provenance |

## Preserved evidence: migration-history

| File | Purpose / feature ownership |
|---|---|
| [AnalyseFuture/migration-history/MIGRATION_SUMMARY.txt](../../AnalyseFuture/migration-history/MIGRATION_SUMMARY.txt) | Earlier migration-history observation/snapshot retained with original provenance |
| [AnalyseFuture/migration-history/TEST_AND_VALIDATION_REPORT.txt](../../AnalyseFuture/migration-history/TEST_AND_VALIDATION_REPORT.txt) | Earlier migration-history observation/snapshot retained with original provenance |

## Preserved evidence: project-history

| File | Purpose / feature ownership |
|---|---|
| [AnalyseFuture/project-history/README.before-reorganization.txt](../../AnalyseFuture/project-history/README.before-reorganization.txt) | Earlier project-history observation/snapshot retained with original provenance |
| [AnalyseFuture/project-history/recovered-next-env.d.ts.txt](../../AnalyseFuture/project-history/recovered-next-env.d.ts.txt) | Exact recovered generated declaration; live framework-managed copy is ignored and regenerated. |

## Preserved evidence: repository-inventory

| File | Purpose / feature ownership |
|---|---|
| [AnalyseFuture/repository-inventory/ARCHIVED_FILES_MANIFEST.txt](../../AnalyseFuture/repository-inventory/ARCHIVED_FILES_MANIFEST.txt) | Earlier repository-inventory observation/snapshot retained with original provenance |
| [AnalyseFuture/repository-inventory/COMPLETE_FILE_INVENTORY.txt](../../AnalyseFuture/repository-inventory/COMPLETE_FILE_INVENTORY.txt) | Earlier repository-inventory observation/snapshot retained with original provenance |
| [AnalyseFuture/repository-inventory/ORIGINAL_TO_NEW_PATH_MAPPING.txt](../../AnalyseFuture/repository-inventory/ORIGINAL_TO_NEW_PATH_MAPPING.txt) | Earlier repository-inventory observation/snapshot retained with original provenance |
| [AnalyseFuture/repository-inventory/RELOCATION_MANIFEST.json](../../AnalyseFuture/repository-inventory/RELOCATION_MANIFEST.json) | Earlier repository-inventory observation/snapshot retained with original provenance |

## Preserved evidence: security-reports

| File | Purpose / feature ownership |
|---|---|
| [AnalyseFuture/security-reports/SECURITY_AUDIT.txt](../../AnalyseFuture/security-reports/SECURITY_AUDIT.txt) | Earlier security-reports observation/snapshot retained with original provenance |

## apps

| File | Purpose / feature ownership |
|---|---|
| [apps/web/AGENTS.md](../../apps/web/AGENTS.md) | Next.js-managed guidance for coding agents; consult the installed version docs. |
| [apps/web/app/globals.css](../../apps/web/app/globals.css) | Recovered creative studio/shared document presentation. |
| [apps/web/app/layout.tsx](../../apps/web/app/layout.tsx) | Shared web document layout, metadata and base CSS import. |
| [apps/web/app/page.tsx](../../apps/web/app/page.tsx) | Recovered creative studio UI: project selection, mock submission, live status, history and receipt preview/download. |
| [apps/web/app/practice/page.tsx](../../apps/web/app/practice/page.tsx) | Thin Next.js route that mounts the feature-owned practice room. |
| [apps/web/eslint.config.mjs](../../apps/web/eslint.config.mjs) | ESLint/Next frontend rules for the web workspace and feature-owned React components. |
| [apps/web/lib/api.test.ts](../../apps/web/lib/api.test.ts) | Frontend creative-client tests for API errors, request behavior and terminal-state handling. |
| [apps/web/lib/api.ts](../../apps/web/lib/api.ts) | Shared creative API URL, request handling and terminal-job predicate. |
| [apps/web/next.config.ts](../../apps/web/next.config.ts) | Next/Turbopack root configuration so feature-owned imports resolve in the workspace. |
| [apps/web/package.json](../../apps/web/package.json) | Web workspace scripts and pinned Next/React/Vitest direct dependencies with supported Node engines. |
| [apps/web/postcss.config.mjs](../../apps/web/postcss.config.mjs) | PostCSS plugin registration for Tailwind processing in the web build. |
| [apps/web/test/live-api.mjs](../../apps/web/test/live-api.mjs) | Node HTTP smoke against an actually running API: project, job lifecycle and mock receipt contracts. |
| [apps/web/tsconfig.json](../../apps/web/tsconfig.json) | TypeScript compiler/resolution settings and include paths for web, schemas and feature-owned components. |
| [apps/web/vitest.config.mts](../../apps/web/vitest.config.mts) | ES-module test runner discovery for shared and feature-owned frontend tests. |

## Documentation: entrypoint

| File | Purpose / feature ownership |
|---|---|
| [docs/README.md](../../docs/README.md) | Navigation for responsibility-based documentation collections and current-versus-historical evidence. |

## Documentation: architecture

| File | Purpose / feature ownership |
|---|---|
| [docs/architecture/API_CONTRACT.md](../../docs/architecture/API_CONTRACT.md) | Versioned creative and English-practice HTTP contracts, job states, request examples and implemented boundary notes. |
| [docs/architecture/ARCHITECTURE.md](../../docs/architecture/ARCHITECTURE.md) | Owned monorepo, application/inference separation, component boundaries and future system design. |
| [docs/architecture/DATA_MODEL.md](../../docs/architecture/DATA_MODEL.md) | Proposed product entities, relationships and durability/provenance requirements; check code for current schemas. |
| [docs/architecture/DECISIONS.md](../../docs/architecture/DECISIONS.md) | Architecture decision register, rationale, corrections and unresolved design choices. |
| [docs/architecture/INDEX.md](../../docs/architecture/INDEX.md) | Navigation and reading order for the architecture responsibility collection. |

## Documentation: design

| File | Purpose / feature ownership |
|---|---|
| [docs/design/INDEX.md](../../docs/design/INDEX.md) | Navigation and reading order for the design responsibility collection. |
| [docs/design/UI_UX.md](../../docs/design/UI_UX.md) | Target creator and learner workflows, interaction/accessibility guidance and future interface requirements. |

## Documentation: development

| File | Purpose / feature ownership |
|---|---|
| [docs/development/CODEX_START_HERE.md](../../docs/development/CODEX_START_HERE.md) | Earlier agent starting brief and constraints; current task/status evidence takes precedence. |
| [docs/development/IMPLEMENTATION_PROGRESS.md](../../docs/development/IMPLEMENTATION_PROGRESS.md) | Implementation provenance, current status, next gates or validation evidence |
| [docs/development/INDEX.md](../../docs/development/INDEX.md) | Navigation and reading order for the development responsibility collection. |
| [docs/development/NEXT_DEVELOPER_INSTRUCTIONS.txt](../../docs/development/NEXT_DEVELOPER_INSTRUCTIONS.txt) | Self-contained combined-product continuation instructions and preservation/implementation constraints. |
| [docs/development/STATUS.md](../../docs/development/STATUS.md) | Current local implementation status followed by explicitly preserved historical status snapshots. |
| [docs/development/TECHNICAL_DEBT.txt](../../docs/development/TECHNICAL_DEBT.txt) | Known integration, security, privacy, infrastructure and reference-source gaps; not a completion claim. |
| [docs/development/WORK_PROGRESS.txt](../../docs/development/WORK_PROGRESS.txt) | Dated recovery, sorting and implementation progress; older no-test entries remain historical. |

## Documentation: memory

| File | Purpose / feature ownership |
|---|---|
| [docs/memory/ARCHITECTURE_AND_WORKFLOW_DIAGRAMS.md](../../docs/memory/ARCHITECTURE_AND_WORKFLOW_DIAGRAMS.md) | Historical architecture, job-lifecycle, media and continuation diagrams for design context. |
| [docs/memory/CONVERSATION_AND_DECISION_HISTORY.md](../../docs/memory/CONVERSATION_AND_DECISION_HISTORY.md) | Dated owner requirements and engineering decisions without relying on inaccessible chat. |
| [docs/memory/DEVELOPER_CONTINUATION_GUIDE.md](../../docs/memory/DEVELOPER_CONTINUATION_GUIDE.md) | Maintainer continuation and milestone evidence protocol, including preserved earlier assumptions. |
| [docs/memory/INDEX.md](../../docs/memory/INDEX.md) | Navigation and reading order for the memory responsibility collection. |
| [docs/memory/MAINTENANCE_PROTOCOL.md](../../docs/memory/MAINTENANCE_PROTOCOL.md) | Instructions for keeping memory, verification ledgers and portable historical handoffs synchronized. |
| [docs/memory/PROJECT_CANONICAL_HANDOFF.md](../../docs/memory/PROJECT_CANONICAL_HANDOFF.md) | Detailed preserved product/engineering brief and historical branch evidence; not proof of current deployment. |
| [docs/memory/PROJECT_HISTORY.md](../../docs/memory/PROJECT_HISTORY.md) | Earlier owner goals and milestones, clearly separated from implementation claims. |
| [docs/memory/PROJECT_MEMORY.md](../../docs/memory/PROJECT_MEMORY.md) | Current memory entrypoint, latest handoff/testing links and retained earlier project snapshots. |
| [docs/memory/README.md](../../docs/memory/README.md) | Reading order for current memory and the historical decision/evidence bundle. |
| [docs/memory/SOURCE_AND_REPOSITORY_LINKS.md](../../docs/memory/SOURCE_AND_REPOSITORY_LINKS.md) | Historical upstream/repository research links and reuse candidates requiring current verification. |
| [docs/memory/STATE_EVIDENCE_AND_OPEN_ISSUES.md](../../docs/memory/STATE_EVIDENCE_AND_OPEN_ISSUES.md) | Dated branch/PR/CI observations and known gaps; historical issue references do not create new issues. |
| [docs/memory/VIDEOGEN_ONE_FILE_HANDOFF.txt](../../docs/memory/VIDEOGEN_ONE_FILE_HANDOFF.txt) | Portable preserved historical memory bundle with explicit warning about stale implementation/remote evidence. |

## Documentation: operations

| File | Purpose / feature ownership |
|---|---|
| [docs/operations/BUILD_RUN.md](../../docs/operations/BUILD_RUN.md) | Locked installation, local startup, optional model configuration, combined verification and older reference runbooks. |
| [docs/operations/COST_PLAN.md](../../docs/operations/COST_PLAN.md) | Budget constraints and measured-cost planning for models, compute, storage and release operations. |
| [docs/operations/GPU_COLAB.md](../../docs/operations/GPU_COLAB.md) | Permitted external GPU/Colab preflight and resource/hosting constraints, without hardware-success claims. |
| [docs/operations/INDEX.md](../../docs/operations/INDEX.md) | Navigation and reading order for the operations responsibility collection. |

## Documentation: product

| File | Purpose / feature ownership |
|---|---|
| [docs/product/COMPETITORS.md](../../docs/product/COMPETITORS.md) | Competitive feature/benchmark research plan; marketing comparisons require reproducible current evidence. |
| [docs/product/FEATURE_REGISTRY.md](../../docs/product/FEATURE_REGISTRY.md) | Capability IDs and roadmap status across creative and English features; planned entries are not delivered code. |
| [docs/product/FUTURE_ROADMAP.txt](../../docs/product/FUTURE_ROADMAP.txt) | Combined staged roadmap, feasibility limits and longer-term exploration gates. |
| [docs/product/INDEX.md](../../docs/product/INDEX.md) | Navigation and reading order for the product responsibility collection. |
| [docs/product/PROJECT_CHARTER.md](../../docs/product/PROJECT_CHARTER.md) | Original studio mission, audiences, positioning, goals and non-goals. |
| [docs/product/PROJECT_IDEA.txt](../../docs/product/PROJECT_IDEA.txt) | Detailed combined English companion and creative studio concept, feasibility boundaries and future vision. |
| [docs/product/ROADMAP.md](../../docs/product/ROADMAP.md) | Original M0–M7 dependency milestones, acceptance criteria and engineering release path. |

## Documentation: quality

| File | Purpose / feature ownership |
|---|---|
| [docs/quality/BENCHMARKS.md](../../docs/quality/BENCHMARKS.md) | Proposed quality, cost, latency and reliability evaluation methodology. |
| [docs/quality/COMPREHENSIVE_VALIDATION.md](../../docs/quality/COMPREHENSIVE_VALIDATION.md) | Actual combined test outcomes, repaired defects, evidence and blocked/unrun gates. |
| [docs/quality/IMPLEMENTATION_VALIDATION.md](../../docs/quality/IMPLEMENTATION_VALIDATION.md) | Implementation provenance, current status, next gates or validation evidence |
| [docs/quality/INDEX.md](../../docs/quality/INDEX.md) | Navigation and reading order for the quality responsibility collection. |
| [docs/quality/TEST_PLAN.md](../../docs/quality/TEST_PLAN.md) | Validation strategy and required evidence levels for application, inference, security and releases. |
| [docs/quality/evidence/2026-11-17-cpu-verification.json](../../docs/quality/evidence/2026-11-17-cpu-verification.json) | Portable combined-run evidence: exact check outcomes/counts, source baseline, repaired-scope note and explicit unrun gates. |

## Documentation: repository

| File | Purpose / feature ownership |
|---|---|
| [docs/repository/FILE_GUIDE.md](../../docs/repository/FILE_GUIDE.md) | This exhaustive per-file/folder responsibility index. |
| [docs/repository/FILE_PLACEMENT.json](../../docs/repository/FILE_PLACEMENT.json) | Complete original-to-current placement ledger with provenance, content-change indicators and functional collections. |
| [docs/repository/FOLDER_GUIDE.md](../../docs/repository/FOLDER_GUIDE.md) | Every source directory, direct/descendant file counts and functional responsibility, excluding ignored generated state. |
| [docs/repository/FUNCTIONAL_REORGANIZATION.md](../../docs/repository/FUNCTIONAL_REORGANIZATION.md) | Dated explanation of the functional sorting pass, original-byte guarantees and then-applicable no-test policy. |
| [docs/repository/GALLERY_CONSOLIDATION.json](../../docs/repository/GALLERY_CONSOLIDATION.json) | Machine-readable manifest linking reunited gallery fragments and documenting missing/duplicate media references. |
| [docs/repository/GALLERY_CONSOLIDATION.md](../../docs/repository/GALLERY_CONSOLIDATION.md) | Human-readable gallery reconstruction evidence, file relationships and inherited missing-MP4 findings. |
| [docs/repository/INDEX.md](../../docs/repository/INDEX.md) | Navigation and reading order for the repository responsibility collection. |
| [docs/repository/RECOVERED_APPLICATION_SOURCE.json](../../docs/repository/RECOVERED_APPLICATION_SOURCE.json) | Exact historical revision/blob provenance for selectively recovered owned M0 application modules. |
| [docs/repository/REPOSITORY_REORGANIZATION.md](../../docs/repository/REPOSITORY_REORGANIZATION.md) | Initial recovery analysis, migration decisions, preserved import boundaries and repaired paths. |
| [docs/repository/files/INFERENCE_REFERENCE.md](../../docs/repository/files/INFERENCE_REFERENCE.md) | Exhaustive per-file ComfyUI reference source responsibilities; preserved package, not active owned generation. |
| [docs/repository/files/WORKFLOW_REFERENCE.md](../../docs/repository/files/WORKFLOW_REFERENCE.md) | Exhaustive per-file FreeField and reunited gallery responsibilities; preserves existing examples and missing-media limits. |

## Documentation: research

| File | Purpose / feature ownership |
|---|---|
| [docs/research/ALL_RECOMMENDED_REPOSITORIES.txt](../../docs/research/ALL_RECOMMENDED_REPOSITORIES.txt) | Catalog of previously proposed reusable repositories with verification, license and applicability cautions. |
| [docs/research/DEPENDENCY_REGISTER.csv](../../docs/research/DEPENDENCY_REGISTER.csv) | Dependency evaluation fields for versions, source/weight rights, resource use and integration decisions. |
| [docs/research/INDEX.md](../../docs/research/INDEX.md) | Navigation and reading order for the research responsibility collection. |
| [docs/research/OPEN_SOURCE_STACK.md](../../docs/research/OPEN_SOURCE_STACK.md) | Reuse-versus-build shortlist and integration rationale for engines, models and supporting tools. |
| [docs/research/REUSE_FIRST.md](../../docs/research/REUSE_FIRST.md) | Policy for inspecting upstream alternatives before adding original code or new dependencies. |

## Documentation: security

| File | Purpose / feature ownership |
|---|---|
| [docs/security/INDEX.md](../../docs/security/INDEX.md) | Navigation and reading order for the security responsibility collection. |
| [docs/security/LICENSE_SECURITY.md](../../docs/security/LICENSE_SECURITY.md) | Separate source/weight/media/voice rights and trust-boundary/security diligence requirements. |

## Product feature: README.md

| File | Purpose / feature ownership |
|---|---|
| [features/README.md](../../features/README.md) | Combined product map and feature boundaries with current implementation/planned status. |

## Product feature: audio-studio

| File | Purpose / feature ownership |
|---|---|
| [features/audio-studio/README.md](../../features/audio-studio/README.md) | audio-studio feature scope, dependencies and future acceptance gates; primarily planned, not real generated output. |

## Product feature: character-continuity

| File | Purpose / feature ownership |
|---|---|
| [features/character-continuity/README.md](../../features/character-continuity/README.md) | character-continuity feature scope, dependencies and future acceptance gates; primarily planned, not real generated output. |

## Product feature: english-speaking-friend

| File | Purpose / feature ownership |
|---|---|
| [features/english-speaking-friend/PROJECT_IDEA.txt](../../features/english-speaking-friend/PROJECT_IDEA.txt) | Full English companion idea, multilingual correction/translation, consent, feasibility limits and future development. |
| [features/english-speaking-friend/README.md](../../features/english-speaking-friend/README.md) | Implemented bounded typed practice, local-model protocol/privacy/UI boundaries and next learning/speech gates. |
| [features/english-speaking-friend/backend/english_friend/__init__.py](../../features/english-speaking-friend/backend/english_friend/__init__.py) | Bounded, authored offline phrase practice; no model or general correction. |
| [features/english-speaking-friend/backend/english_friend/coach.py](../../features/english-speaking-friend/backend/english_friend/coach.py) | Conservative scenario-scoped authored phrase matching, accepted retries and honest unsupported fallback. |
| [features/english-speaking-friend/backend/english_friend/lessons.json](../../features/english-speaking-friend/backend/english_friend/lessons.json) | 18 original English/Bangla practice records and three public scenario descriptions; educator evaluation pending. |
| [features/english-speaking-friend/backend/english_friend/providers.py](../../features/english-speaking-friend/backend/english_friend/providers.py) | Offline/local-Ollama selection, loopback configuration, bounded strict JSON protocol and safe model errors. |
| [features/english-speaking-friend/backend/english_friend/routes.py](../../features/english-speaking-friend/backend/english_friend/routes.py) | Practice owner cookie, strict requests, session API, idempotent turns and interruption/storage error boundary. |
| [features/english-speaking-friend/backend/english_friend/storage.py](../../features/english-speaking-friend/backend/english_friend/storage.py) | Practice metadata/explicit saved transcripts, scoped deletion/expiry, retry cache and durable idempotency state. |
| [features/english-speaking-friend/tests/test_coach.py](../../features/english-speaking-friend/tests/test_coach.py) | Behavior checks for authored practice and its explicit coverage boundary. |
| [features/english-speaking-friend/tests/test_content_and_provider_matrix.py](../../features/english-speaking-friend/tests/test_content_and_provider_matrix.py) | Data coverage and hostile provider contracts; no real model or GPU calls. |
| [features/english-speaking-friend/tests/test_providers.py](../../features/english-speaking-friend/tests/test_providers.py) | Provider contracts use local mocked HTTP; no AI model or external service runs. |
| [features/english-speaking-friend/tests/test_session_adversarial.py](../../features/english-speaking-friend/tests/test_session_adversarial.py) | Fault and race regressions for the single-process practice session boundary. All model behavior is controlled in-process; these tests never contact a model. |
| [features/english-speaking-friend/tests/test_sessions.py](../../features/english-speaking-friend/tests/test_sessions.py) | Real local HTTP/SQLite checks for privacy, ownership, retries and lifecycle. |
| [features/english-speaking-friend/web/PracticeRoom.tsx](../../features/english-speaking-friend/web/PracticeRoom.tsx) | Learner screen, scenarios, illustrated character, editable examples, feedback/retry, device speech and consent/history controls. |
| [features/english-speaking-friend/web/api.test.ts](../../features/english-speaking-friend/web/api.test.ts) | Implemented phrase coaching/provider, session lifecycle, practice UI or feature-specific tests |
| [features/english-speaking-friend/web/api.ts](../../features/english-speaking-friend/web/api.ts) | Credentialed typed HTTP calls plus runtime validation of untrusted successful responses and safe errors. |
| [features/english-speaking-friend/web/practice.css](../../features/english-speaking-friend/web/practice.css) | Scoped responsive, focus and reduced-motion presentation for the practice feature. |
| [features/english-speaking-friend/web/types.ts](../../features/english-speaking-friend/web/types.ts) | Practice scenario/provider/session/turn client interfaces. |

## Product feature: image-studio

| File | Purpose / feature ownership |
|---|---|
| [features/image-studio/README.md](../../features/image-studio/README.md) | image-studio feature scope, dependencies and future acceptance gates; primarily planned, not real generated output. |

## Product feature: movie-studio

| File | Purpose / feature ownership |
|---|---|
| [features/movie-studio/DESIGN.md](../../features/movie-studio/DESIGN.md) | Movie-domain design for scripts/scenes/shots/takes, character continuity and non-destructive assembly. |
| [features/movie-studio/README.md](../../features/movie-studio/README.md) | movie-studio feature scope, dependencies and future acceptance gates; primarily planned, not real generated output. |

## Product feature: video-studio

| File | Purpose / feature ownership |
|---|---|
| [features/video-studio/README.md](../../features/video-studio/README.md) | video-studio feature scope, dependencies and future acceptance gates; primarily planned, not real generated output. |

## integrations

| File | Purpose / feature ownership |
|---|---|
| [integrations/__init__.py](../../integrations/__init__.py) | Isolated inference and media adapters. |
| [integrations/comfyui/__init__.py](../../integrations/comfyui/__init__.py) | ComfyUI integration boundary, not active in M0. |
| [integrations/comfyui/adapter.py](../../integrations/comfyui/adapter.py) | Operator-approved workflow HTTP boundary with validated engine responses and no redirect following; real engine integration remains gated. |

## notebooks

| File | Purpose / feature ownership |
|---|---|
| [notebooks/colab/00_gpu_preflight.ipynb](../../notebooks/colab/00_gpu_preflight.ipynb) | Opt-in notebook that inspects actual GPU/runtime resources; no model download or generation proof. |
| [notebooks/colab/README.md](../../notebooks/colab/README.md) | Notebook usage, external hardware evidence and constrained-runtime guidance. |

## packages

| File | Purpose / feature ownership |
|---|---|
| [packages/schemas/src/types.ts](../../packages/schemas/src/types.ts) | Recovered typed creative job/artifact contracts |

## scripts

| File | Purpose / feature ownership |
|---|---|
| [scripts/README.md](../../scripts/README.md) | Tool collection entrypoint and execution-policy guidance |
| [scripts/development/dev.sh](../../scripts/development/dev.sh) | Loopback development launcher, matching API/web origin and child-process cleanup. |
| [scripts/development/smoke_mock.py](../../scripts/development/smoke_mock.py) | Isolated executing API/worker/receipt smoke check with synthetic data. |
| [scripts/hardware/gpu_preflight.py](../../scripts/hardware/gpu_preflight.py) | Resource inspection only; does not download models or generate media. |
| [scripts/maintenance/check_docs.py](../../scripts/maintenance/check_docs.py) | Required documentation and relative-link integrity check; no model execution. |
| [scripts/maintenance/check_structure.py](../../scripts/maintenance/check_structure.py) | Feature entrypoint and original archived-blob preservation check through the current placement map. |
| [scripts/quality/verify.py](../../scripts/quality/verify.py) | One-command CPU/reference/build/audit/browser verifier with owned child processes, per-check logs and structured outcomes. |

## services

| File | Purpose / feature ownership |
|---|---|
| [services/__init__.py](../../services/__init__.py) | Owned VideoGen application services. |
| [services/api/__init__.py](../../services/api/__init__.py) | HTTP API and durable local storage. |
| [services/api/contracts.py](../../services/api/contracts.py) | Strict versioned Pydantic models for creative inputs/jobs/models/artifacts. |
| [services/api/main.py](../../services/api/main.py) | Shared FastAPI lifespan, creative routes, practice registration, origin/host/error boundary and verified mock receipt download. |
| [services/api/storage.py](../../services/api/storage.py) | SQLite projects, idempotent jobs, atomic queue/state transitions and immutable generated receipt metadata/files. |
| [services/worker/__init__.py](../../services/worker/__init__.py) | Execution backends, independent of the HTTP contract. |
| [services/worker/mock.py](../../services/worker/mock.py) | CPU-only queue executor, synthetic text receipts, cancellation/failure and transient-storage recovery. |

## tests

| File | Purpose / feature ownership |
|---|---|
| [tests/browser/regression.py](../../tests/browser/regression.py) | Fault-injected and responsive checks against an isolated running application. |
| [tests/browser/smoke.py](../../tests/browser/smoke.py) | Real browser -> Next.js -> FastAPI -> SQLite/worker integration. Run against an isolated local data directory, never a shared/user database. Browser speech availability is inspected, not an assertion that audio was heard. |
| [tests/conftest.py](../../tests/conftest.py) | Shared owned API test fixtures and isolated per-test application/storage setup. |
| [tests/test_adapter.py](../../tests/test_adapter.py) | HTTP transport simulation without a running ComfyUI or any model downloads. |
| [tests/test_api.py](../../tests/test_api.py) | Real HTTP/API contract tests against isolated SQLite and the executing CPU worker. |
| [tests/test_creative_regressions.py](../../tests/test_creative_regressions.py) | Creative persistence/worker regressions and simulated engine HTTP boundaries. No model, external engine, GPU, or paid service is contacted by this module. |
| [tests/test_http_boundaries.py](../../tests/test_http_boundaries.py) | Check the shared application boundary, not only the isolated feature router. |

Files accounted for across these three indexes: **2291**. Add new source paths and explanations here and in the placement ledger when contributing.
