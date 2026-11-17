# Project handoff: VideoGen + English-speaking AI friend

**Read this first when continuing with another AI tool.** This is the current product
and engineering handoff. It does not create GitHub issues or start an unattended
monitor. The owner deferred issue creation; task IDs below are local references.

## Main goal

Build one original creative workspace for images, short video, voice, reusable
characters and editable movies, with a friendly English-speaking companion.
A learner sees a disclosed synthetic man/woman/character, speaks or types English,
Bangla or another explicitly supported language, gets a gentle natural-English
alternative, can retry or ask for clarification, and continues at their own pace.
The studio can prepare cleared avatars/scenarios, but private learning records
must never become public creative assets or training data without explicit consent.

This is a staged engineering project. Perfect translation, guaranteed fluency,
human feelings, free unlimited GPU video, exact identity in every shot and coherent
hours-long generation from one prompt are not supported promises.

## What exists now — use these status boundaries

| Feature / responsibility | Actual implementation | Status and limits |
|---|---|---|
| Creative foundation | Owned Next.js screen; FastAPI projects/jobs; SQLite state; queue/CPU worker; progress/history; verified downloadable text receipts | **CPU implemented/tested.** Text receipt is explicitly mock, not an AI image/video. No public account isolation yet. |
| English text practice | 18 original developer-authored cases across everyday/work/travel, Bangla/transliteration/code-switch samples, accepted variants, ambiguity and retries | **CPU implemented/tested.** Finite matching only; unknown text is unassessed. Educator and learning-outcome evaluation pending. |
| Local language-model boundary | Optional Ollama protocol, strict bounded JSON, loopback/no redirects, safe errors | **Protocol tested with mocked HTTP.** Real model availability/semantic quality NOT RUN; no model downloaded. |
| Practice privacy/lifecycle | Random HttpOnly cookie ownership, explicit save consent, default metadata-only disk storage, saved resume/delete, replay and quotas | **Local prototype tested.** Not a production identity service. Expiry is24h default/7days saved with purge during service operations; backups outside this app remain unverified. |
| Companion presentation | Feature-owned `/practice`, original illustrated characters, optional explicit device/browser speech controls | **Browser tested.** No camera/microphone capture, actual speech-quality proof, lip sync or live video. |
| Inference adapter | Operator allowlist and tested ComfyUI HTTP boundary | **Boundary only.** Not wired to real image/video generation. |
| Images, video, music, continuity, movies | Specifications and preserved source references | **Planned/not hardware verified.** See ordered gates below. |
| Archived reference studio | Preserved FreeField source, workflows and collected examples; 120 manifests | **Reference CPU checks only.** Not 120 completed owned features; 162 indexed MP4s remain absent. |

Current owned source was selectively recovered from historical revision
`ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37`; its exact file origins are recorded in
[RECOVERED_APPLICATION_SOURCE.json](docs/repository/RECOVERED_APPLICATION_SOURCE.json).
All 2,131 original imported files remain preserved; don't merge/delete them casually.

## Current testing and fixes

Use [COMPREHENSIVE_VALIDATION.md](docs/quality/COMPREHENSIVE_VALIDATION.md) for the latest
combined run, actual counts, discovered defects, remaining warnings and unrun gates.
The earlier [implementation validation](docs/quality/IMPLEMENTATION_VALIDATION.md)
is dated evidence, not a substitute for testing later changes.

The current testing pass adds regressions for interrupted practice, expiry,
storage faults, replay/concurrency, immutable creative job state and artifact
integrity, hostile engine/provider output, malformed browser responses, metadata
quota recovery and responsive/browser behavior. Passing CPU tests does not verify
teaching effectiveness, microphone audio, model quality or GPU generation.

## Where files and folders belong

| Location | What it owns | Current feature / next work |
|---|---|---|
| `apps/web/app/` | Next.js routes, layout, recovered creative UI | `/` is mock studio; `/practice` mounts the feature component. Keep framework entrypoints here. |
| `apps/web/lib/` | Shared creative HTTP helper and tests | Versioned client errors/contracts; never put provider secrets in client code. |
| `services/api/` | Shared app/contract/job storage/download boundary | Local foundation; production access controls and migrations remain. |
| `services/worker/` | CPU mock execution and queue polling | Real model workers must be separate reviewed integrations. |
| `features/english-speaking-friend/backend/english_friend/` | Authored coaching, provider adapter, practice API and storage | Current implemented learning feature; add teacher/model/speech work incrementally. |
| `features/english-speaking-friend/web/` | Practice UI, styles, HTTP contracts/guards and frontend tests | Learner interactions stay with the feature. |
| `features/english-speaking-friend/tests/` | Content/provider/session/adversarial tests | No real model calls are hidden inside unit tests. |
| Other `features/*/` | Image, video, audio, movie and character boundaries | Primarily plans; add actual code only for a scoped implementation. |
| `integrations/comfyui/` | Typed allowlisted external-engine adapter | No arbitrary public graph submissions or automatic model downloads. |
| `packages/schemas/` | Shared creative TypeScript contracts | Evolve with explicit API compatibility. |
| `tests/` and `tests/browser/` | Shared API/worker and real browser integration checks | Feature tests remain beside features where appropriate. |
| `scripts/development/` | Local launcher and isolated CPU smoke | Own child processes, bind loopback, never kill unrelated listeners. |
| `scripts/quality/` | Combined validation orchestration | Save logs/counts/exit codes; don't mark blocked checks as passed. |
| `scripts/maintenance/` | Docs and archived-byte preservation | Maintain current paths without mutating archived originals. |
| `scripts/hardware/`, `notebooks/colab/` | Resource inspection and permitted hardware research | No unapproved weights, paid GPU or permanent notebook hosting. |
| `docs/product/` | Charter, requirements, combined ideas/roadmaps | Requirements are not implementation claims. |
| `docs/architecture/` | API, data model and decisions | Update when behavior/contracts change. |
| `docs/development/` | Progress, next tasks, debt and continuation | Keep this handoff and current evidence consistent. |
| `docs/quality/` | Test/benchmark plans and actual evidence | Separate mock, protocol, GPU and human results. |
| `docs/research/`, `docs/security/` | Reuse, dependency/rights and security rules | Source, weight, media and voice rights are separate. |
| `docs/operations/`, `docs/design/` | Runbooks, cost constraints and shared UX | Keep commands accurate and accessible. |
| `docs/memory/` | Historical decisions/evidence and current memory entrypoint | Earlier no-code/no-test statements remain dated snapshots. |
| `docs/repository/` | File placement, gallery provenance and exhaustive file guide | [FILE_GUIDE.md](docs/repository/FILE_GUIDE.md) explains every tracked path. |
| `AnalyseFuture/references/` | Cohesive external engine/reference packages | Preserve internal imports, licenses, workflows and assets. Do not auto-execute. |
| Other `AnalyseFuture/` collections | Prior inventories, security analysis and migration history | Historical paths resolve through the placement ledger. |
| Root configuration | Workspaces, Python packaging/locks, lint, CI and entry guides | Conventional discovery files stay at the root. |
| Ignored `.local/`, `.venv/`, `node_modules/`, `.next/` | Local data, caches and generated dependencies | Not source; never commit transcripts, tokens, model weights or private media. |

Every tracked file, including deeply nested preserved packages, has an entry in
[FILE_GUIDE.md](docs/repository/FILE_GUIDE.md), and every source directory has an
entry in [FOLDER_GUIDE.md](docs/repository/FOLDER_GUIDE.md). The
[placement ledger](docs/repository/FILE_PLACEMENT.json) records original paths and
collections. Package-relative resources remain with the package, not scattered
by file extension. Original binaries are classified by manifest/index role,
not claimed to have received a forensic or visual security review.

## Start and verify

Read [AGENTS.md](AGENTS.md), the nested framework guide and
[BUILD_RUN.md](docs/operations/BUILD_RUN.md). Use the existing isolated checkout.
Supported Node versions follow `package.json`; use Node 22.x (22.12 or newer),
24.x or 26+, and Python 3.11+ (current execution uses Python3.12). No paid service/model is needed
for built-in practice and mock jobs.

After the documented locked installation:

```sh
npm run dev
# In a separate terminal; use an isolated test data directory:
npm run verify
```

The verifier builds with its own test API URL, owns its test processes, writes
per-check logs and `summary.json` under ignored `.local/verification/`, and
continues independent checks after a failure. Reduced-scope flags are explicit;
a blocked browser/model/GPU check is never counted as a passed test. Model/GPU
and human gates remain separate. Do not run browser tests against personal data.

## How another AI tool should continue

1. Read this file, the owning feature guide, current evidence and relevant ADR.
2. Choose **one ready local task ID** below. Check dependencies, existing source and
   available PRs; do not rebuild a feature already present.
3. Work on a short-lived branch, for example `feat/VG-025-local-model-proof`.
   Keep changes in the named functional collection; do not rewrite unrelated files.
4. Follow reuse-first/source/weight/voice/media review. Pin dependencies and keep
   integrity/TLS checks. Never invent credentials or put them in chat/Git.
5. Add meaningful regression/integration tests and real evidence for the task.
   Clearly label CPU mock/protocol/GPU/manual/unrun results; don't disable assertions.
6. Update this task's status, the feature guide, current progress, API/ADR changes
   and file placement when relevant. Preserve old work and uncertainty safely.
7. Open a PR with the local task ID, concrete before/after behavior, changed files,
   tests, artifacts and remaining limits. **Do not open GitHub issues automatically.**
8. Request review. The reviewer checks scope/security/provenance, inspects all code,
   reruns relevant checks, records blocking findings and verifies required CI.
9. Merge only after required evidence and review are satisfied, using normal GitHub
   permissions. No force push, history rewrite or branch-protection bypass.

**Review/monitoring boundary:** Other tools should create PRs. This chat does not
run a persistent background PR watcher. Ask for a review/check of current PRs or
provide PR links in a new session; the reviewer can then inspect/test and handle
an authorized merge. Never claim unseen PRs were reviewed or CI passed.

## Ordered remaining tasks

All tasks below are **TODO**, not completion claims or GitHub issues. They describe
the remaining release path rather than repeating already-tested mock/phrase work.
Use the phase gates and each row's acceptance evidence. A row may be split into
smaller PRs after review; don't combine a whole phase into one rewrite.

- Shared controls and review precede public exposure.
- Real-model/speech/GPU tasks need approved resources, rights and actual evidence.
- Work inside a later feature may start in parallel only when its listed prerequisites
  are satisfied; higher realism and long-form work do not block a useful text/audio MVP.
- Labels in future PRs should distinguish IMPLEMENTED, CPU TESTED, PROTOCOL TESTED,
  GPU VERIFIED, HUMAN EVALUATED and RELEASED.


### Phase 1: Foundation and delivery

Primary home: `services/api/, packages/schemas/, scripts/quality/`.

#### VG-001 — Choose the original application license

- **Status:** TODO. **Home:** `docs/security/, root LICENSE (only after owner decision)`
- **Prerequisites:** Owner must choose a license; engineering research can proceed without declaring that choice.
- **Scope:** Record the owner-approved license and third-party notice policy; do not infer rights from public visibility.
- **Done/evidence:** Owner decision and license/notice checks recorded before public distribution.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-002 — Maintain the dependency and rights register

- **Status:** TODO. **Home:** `docs/research/DEPENDENCY_REGISTER.csv, docs/security/`
- **Prerequisites:** Current locked dependencies and source provenance; VG-001 before distribution approval.
- **Scope:** Record each shipped library, model, voice and asset separately, including exact version and intended use.
- **Done/evidence:** Every approved dependency has provenance and commercial/distribution constraints.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-003 — Freeze the first release scope

- **Status:** TODO. **Home:** `docs/product/, docs/development/`
- **Prerequisites:** Owner/product decision; current implemented-status table.
- **Scope:** Choose the audience, supported tasks, privacy defaults and explicit non-goals for one small release.
- **Done/evidence:** A release checklist names measurable user outcomes and excludes unsupported claims.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-004 — Version API contracts

- **Status:** TODO. **Home:** `services/api/contracts.py, packages/schemas/, features/english-speaking-friend/web/types.ts`
- **Prerequisites:** Existing M0/T0 endpoints; no external model or budget required.
- **Scope:** Generate/review shared client contracts and document compatibility for studio and practice endpoints.
- **Done/evidence:** Contract tests catch an incompatible request or response change.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-005 — Add database migration versions

- **Status:** TODO. **Home:** `services/api/storage.py, features/english-speaking-friend/backend/english_friend/storage.py`
- **Prerequisites:** Current storage formats and a synthetic pre-migration fixture.
- **Scope:** Introduce explicit schema versioning and safe forward/rollback procedures for both local databases.
- **Done/evidence:** Upgrade an existing test database without losing projects or saved practice.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-006 — Schedule retention cleanup

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/storage.py, services/api/main.py`
- **Prerequisites:** VG-005 for migration changes; current retention/deletion semantics.
- **Scope:** Add controlled cleanup independent of page visits, retaining explicit deletion semantics.
- **Done/evidence:** Clock-driven tests remove expired text/cache and preserve active/other-owner data.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-007 — Prove backup and restore

- **Status:** TODO. **Home:** `scripts/maintenance/, docs/operations/`
- **Prerequisites:** VG-005; documented private-data/backup scope.
- **Scope:** Create a local documented backup/restore path with clear treatment of saved learning data.
- **Done/evidence:** Restore into a separate directory and verify integrity, access and retention.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-008 — Add worker supervision

- **Status:** TODO. **Home:** `services/worker/, services/api/main.py`
- **Prerequisites:** Current mock worker; no GPU/model required.
- **Scope:** Expose meaningful worker readiness and bounded recovery instead of claiming healthy when processing stops.
- **Done/evidence:** A deliberately stopped worker changes readiness and recovers without duplicate jobs.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-009 — Add privacy-safe operational logs

- **Status:** TODO. **Home:** `services/api/, services/worker/, docs/operations/`
- **Prerequisites:** Current API/worker error codes; exclude personal text and credentials.
- **Scope:** Record request/job/turn correlation and safe error codes without raw prompts, cookies or recordings.
- **Done/evidence:** Redaction tests and an injected failure show no sensitive text in logs.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-010 — Bound request size and rate

- **Status:** TODO. **Home:** `services/api/, features/english-speaking-friend/backend/english_friend/routes.py`
- **Prerequisites:** Current request schemas, owner quotas and local threat model.
- **Scope:** Enforce transport body/time/concurrency limits consistently across local API endpoints.
- **Done/evidence:** Oversized/chunked and repeated requests fail predictably without excess allocations.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-011 — Keep CI and verification reproducible

- **Status:** TODO. **Home:** `.github/workflows/, scripts/quality/, requirements-dev.lock, package-lock.json`
- **Prerequisites:** Current verifier and lockfiles; retain distinct CPU/browser/model outcomes.
- **Scope:** Run the combined verifier on supported clean environments and publish test artifacts per PR.
- **Done/evidence:** A clean checkout executes the documented gates; failed/blocked/unrun remain distinct.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-012 — Publish a capability registry

- **Status:** TODO. **Home:** `services/api/contracts.py, packages/schemas/, docs/product/FEATURE_REGISTRY.md`
- **Prerequisites:** VG-004; keep planned capabilities separate from verified ones.
- **Scope:** Distinguish installed/configured/healthy/tested capabilities and disable unsupported actions honestly.
- **Done/evidence:** The UI cannot offer a real model based solely on a config variable.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

### Phase 2: English learning and evaluation

Primary home: `features/english-speaking-friend/`.

#### VG-013 — Review the authored English/Bangla examples

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/lessons.json, features/english-speaking-friend/tests/`
- **Prerequisites:** English/Bangla educator availability and the current 18 original cases.
- **Scope:** Have a qualified educator review all18 cases, variants, explanations and natural translations.
- **Done/evidence:** Signed-off content notes and corrections; do not call developer text teacher-approved.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-014 — Create a consented language evaluation set

- **Status:** TODO. **Home:** `features/english-speaking-friend/tests/, docs/quality/`
- **Prerequisites:** VG-013; explicit consent and rights for evaluation samples.
- **Scope:** Cover accents, proficiency, valid varieties, ambiguity and Bangla-English code-switching.
- **Done/evidence:** Document consent, sample splits, rubric and meaningful error categories.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-015 — Separate grammar from optional style

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/coach.py, features/english-speaking-friend/web/`
- **Prerequisites:** VG-013, VG-014; educator definition of error versus optional style.
- **Scope:** Represent accepted variants, unclear meaning and optional style without shaming valid English.
- **Done/evidence:** False-correction tests and educator review distinguish these categories.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-016 — Add correction preferences

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/, features/english-speaking-friend/web/`
- **Prerequisites:** VG-015; migration plan if preferences persist.
- **Scope:** Support after-turn, light conversation and end-of-session review with explicit learner control.
- **Done/evidence:** Each mode changes feedback timing while retaining meaning and opt-out behavior.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-017 — Add feedback on wrong suggestions

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/, features/english-speaking-friend/web/`
- **Prerequisites:** VG-015; data-minimization and correction-review policy.
- **Scope:** Let a learner flag an unhelpful response without silently exporting their conversation.
- **Done/evidence:** An explicit preview/consent flow and access/deletion tests protect reports.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-018 — Add safe scenario authoring

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/lessons.json, features/english-speaking-friend/tests/`
- **Prerequisites:** VG-013, VG-014; schema/content review before publishing scenarios.
- **Scope:** Define a bounded scenario schema and reviewed content import path.
- **Done/evidence:** Invalid/executable content is rejected; approved scenarios have versioned provenance.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-019 — Add opt-in phrase review

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/storage.py, features/english-speaking-friend/web/`
- **Prerequisites:** VG-016, VG-024; explicit opt-in persistence.
- **Scope:** Build a learner-controlled phrase notebook and spaced practice without storing all dialogue by default.
- **Done/evidence:** Save/review/delete works; default sessions create no notebook entries.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-020 — Evaluate learning progress

- **Status:** TODO. **Home:** `docs/quality/, features/english-speaking-friend/`
- **Prerequisites:** VG-014, VG-019; consented study design and human review.
- **Scope:** Measure transfer to unseen speaking tasks rather than inferring fluency from streaks or activity.
- **Done/evidence:** A documented study protocol distinguishes engagement from actual improvement.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-021 — Audit learning accessibility

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, tests/browser/`
- **Prerequisites:** Existing text UI; manual keyboard/screen-reader evaluation access.
- **Scope:** Test keyboard, screen reader, low vision, reduced motion and text-only interaction.
- **Done/evidence:** Manual and automated findings are recorded and blocking issues repaired.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-022 — Localize the learning interface

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, docs/product/`
- **Prerequisites:** VG-013, VG-021; human translation review.
- **Scope:** Add reviewed English/Bangla UI wording without claiming every language is supported.
- **Done/evidence:** Language switching preserves form/session state and interpolation values.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-023 — Improve low-bandwidth recovery

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/api.ts, features/english-speaking-friend/web/PracticeRoom.tsx, tests/browser/`
- **Prerequisites:** Existing idempotency/replay behavior and current fault tests.
- **Scope:** Handle slow/offline connections, saved replies and explicit retries without duplicate model use.
- **Done/evidence:** Fault-injected browser checks verify reconnect and idempotency behavior.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-024 — Export and delete learning data

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/routes.py, features/english-speaking-friend/backend/english_friend/storage.py, features/english-speaking-friend/web/`
- **Prerequisites:** VG-005, VG-007; delete-all exists already, extend export and lifecycle coverage.
- **Scope:** Provide scoped machine-readable export and deletion, including explicit retention/backup limits.
- **Done/evidence:** Another owner cannot export data; deletion/export tests cover saved and metadata-only sessions.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

### Phase 3: Real model integration

Primary home: `features/english-speaking-friend/backend/english_friend/`.

#### VG-025 — Select one permitted local model

- **Status:** TODO. **Home:** `docs/research/, docs/operations/, features/english-speaking-friend/README.md`
- **Prerequisites:** VG-002, VG-014; approved hardware/resources and exact weight rights.
- **Scope:** Choose an exact model/version after rights, hardware, memory and cost review.
- **Done/evidence:** Owner-approved model decision with sources and explicit download permission when needed.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-026 — Prepare a reproducible model runtime

- **Status:** TODO. **Home:** `docs/operations/, scripts/development/ (approved runtime outside Git)`
- **Prerequisites:** VG-025; explicit approval for any weight download or spending.
- **Scope:** Document the selected runtime/model hash and operator-controlled startup; do not auto-download weights.
- **Done/evidence:** A named machine can reproduce startup and report resource usage.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-027 — Run the actual Ollama adapter

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/providers.py, docs/quality/`
- **Prerequisites:** VG-026; an actually running permitted model, not a mocked transport.
- **Scope:** Exercise an existing local model through the current strict protocol and safe failure boundary.
- **Done/evidence:** Real request/response evidence, model ID and unsupported/error behavior are recorded.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-028 — Evaluate meaning preservation

- **Status:** TODO. **Home:** `features/english-speaking-friend/tests/, docs/quality/`
- **Prerequisites:** VG-014, VG-027; educator rubric and representative consented samples.
- **Scope:** Use the reviewed corpus to compare corrections, translations and false corrections.
- **Done/evidence:** Publish counts, uncertainty, failures and conditions rather than a universal accuracy claim.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-029 — Add bounded conversation context

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/providers.py, features/english-speaking-friend/backend/english_friend/storage.py`
- **Prerequisites:** VG-028, VG-005; bounded opt-in context and retention specification.
- **Scope:** Maintain context only with explicit retention policy, token limits and reset controls.
- **Done/evidence:** Context cannot cross owners/sessions and can be deleted; long turns stay bounded.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-030 — Implement validated response streaming

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/routes.py, features/english-speaking-friend/backend/english_friend/providers.py, features/english-speaking-friend/web/`
- **Prerequisites:** VG-027, VG-031; schema-safe partial output design.
- **Scope:** Stream useful progress without exposing partial invalid JSON as a completed correction.
- **Done/evidence:** Fragmentation, malformed output, disconnect and final-schema tests pass.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-031 — Implement targeted model cancellation

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/routes.py, features/english-speaking-friend/backend/english_friend/providers.py`
- **Prerequisites:** VG-027; cancellation behavior of the actual chosen runtime.
- **Scope:** Cancel a specific turn when the runtime supports it, without globally interrupting another user.
- **Done/evidence:** Race/disconnect/retry tests prevent duplicate or cross-session cancellation.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-032 — Measure and limit model usage

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/, docs/quality/`
- **Prerequisites:** VG-027; named runtime with measurable resource usage.
- **Scope:** Record latency and compute/token usage with bounded session/model budgets.
- **Done/evidence:** Limits reject excess work before a model call and never log private prompt content.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-033 — Evaluate prompt injection and unsafe output

- **Status:** TODO. **Home:** `features/english-speaking-friend/tests/, tests/browser/, docs/security/`
- **Prerequisites:** VG-028, VG-029; adversarial evaluation rubric.
- **Scope:** Use a fixed hostile-input set; preserve schema and tool restrictions.
- **Done/evidence:** No model output executes code, changes server configuration or claims external actions.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-034 — Version teaching prompts and rollbacks

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/providers.py, docs/architecture/`
- **Prerequisites:** VG-028; versioned prompts and baseline evaluation results.
- **Scope:** Pin the system prompt and model configuration with reproducible comparisons.
- **Done/evidence:** A regression can roll back safely with old-session/provenance behavior documented.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-035 — Evaluate one additional support language

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/, features/english-speaking-friend/tests/, docs/quality/`
- **Prerequisites:** VG-028; fluent human reviewer and consented samples for the named language.
- **Scope:** Add a language only with qualified reviewers and representative consented examples.
- **Done/evidence:** Publish actual coverage and failure cases; unsupported languages remain explicit.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-036 — Design authenticated remote-model transport

- **Status:** TODO. **Home:** `features/english-speaking-friend/backend/english_friend/providers.py, docs/security/, docs/operations/`
- **Prerequisites:** VG-093, VG-095; rights/owner-approved remote endpoint, never relax loopback silently.
- **Scope:** If needed, add operator-managed secure remote destinations without allowing user-controlled URLs.
- **Done/evidence:** Separate review verifies TLS, secret handling, destination policy and spending approval.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

### Phase 4: Speech and audio interaction

Primary home: `features/audio-studio/, features/english-speaking-friend/`.

#### VG-037 — Choose an ASR engine and audio policy

- **Status:** TODO. **Home:** `features/audio-studio/, docs/security/, docs/research/`
- **Prerequisites:** VG-002; approved audio privacy policy and exact engine/weight rights.
- **Scope:** Review source/weight rights and representative Bangla-English recognition before selecting a model.
- **Done/evidence:** Approved pinned adapter and a consent/processing/retention policy.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-038 — Add explicit microphone consent

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, tests/browser/`
- **Prerequisites:** VG-037; permission/revocation UX and supported-browser plan.
- **Scope:** Provide visible start/stop, permission denial handling and a reliable text fallback.
- **Done/evidence:** No capture starts automatically; browser permission/revoke tests pass.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-039 — Validate audio uploads

- **Status:** TODO. **Home:** `features/audio-studio/, services/api/, tests/`
- **Prerequisites:** VG-037, VG-004; controlled input limits and audio-decoding threat model.
- **Scope:** Bound file size/duration/type, decoding resources and storage paths.
- **Done/evidence:** Malformed, oversized and misleading audio files fail safely.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-040 — Implement push-to-talk capture

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, tests/browser/`
- **Prerequisites:** VG-038, VG-039; synthetic/consented test audio.
- **Scope:** Deliver one bounded recording per learner action with cancellation and editable transcript.
- **Done/evidence:** Real device testing verifies capture/stop, empty audio and retry behavior.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-041 — Connect the ASR adapter

- **Status:** TODO. **Home:** `features/audio-studio/, integrations/ (a reviewed ASR adapter), features/english-speaking-friend/backend/`
- **Prerequisites:** VG-037, VG-039, VG-040; approved engine/model available.
- **Scope:** Translate supported captured audio into text without silently overwriting the intended meaning.
- **Done/evidence:** Real recognition results are measured separately from mocked API tests.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-042 — Review transcription edits

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, features/english-speaking-friend/tests/`
- **Prerequisites:** VG-041; typed fallback and uncertainty design.
- **Scope:** Let users correct recognition before grammar/translation feedback is requested.
- **Done/evidence:** The coach receives the edited text and marks recognition uncertainty appropriately.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-043 — Evaluate noisy/code-switched speech

- **Status:** TODO. **Home:** `features/audio-studio/, docs/quality/`
- **Prerequisites:** VG-041, VG-042; representative consented noise/accent/code-switch samples.
- **Scope:** Measure usable meaning across accents, microphones and noise, not only clean samples.
- **Done/evidence:** A fixed consented corpus reports error and clarification rates.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-044 — Select cleared speech voices

- **Status:** TODO. **Home:** `features/audio-studio/, docs/research/, docs/security/`
- **Prerequisites:** VG-002; cleared voice rights and intended commercial/distribution uses.
- **Scope:** Review TTS code, weights, voice identity and language rights independently.
- **Done/evidence:** Each offered voice has approval and tested language coverage.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-045 — Generate and validate real speech

- **Status:** TODO. **Home:** `features/audio-studio/, integrations/ (a reviewed TTS adapter), services/worker/`
- **Prerequisites:** VG-044; owner-approved speech runtime and actual audio playback checks.
- **Scope:** Produce decodable speech through a versioned adapter with text fallback.
- **Done/evidence:** Intelligibility, duration, failures and actual resource usage are recorded.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-046 — Add synchronized timing/captions

- **Status:** TODO. **Home:** `features/audio-studio/, features/english-speaking-friend/web/`
- **Prerequisites:** VG-045; validated duration/timing metadata.
- **Scope:** Connect validated word/phrase timings to captions and optional animation.
- **Done/evidence:** Audio/text alignment and seek/playback tests use actual files.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-047 — Implement interruption and echo controls

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, features/audio-studio/`
- **Prerequisites:** VG-040, VG-041, VG-045; explicit interruption and echo policy.
- **Scope:** Stop or replace a speaking turn deliberately without overlapping stale audio.
- **Done/evidence:** Barge-in, cancellation, device errors and stale-turn tests pass.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-048 — Measure end-to-end speech latency

- **Status:** TODO. **Home:** `docs/quality/, features/english-speaking-friend/, features/audio-studio/`
- **Prerequisites:** VG-028, VG-043, VG-046, VG-047; actual end-to-end audio and named device.
- **Scope:** Measure microphone stop through first understandable audio on named devices/networks.
- **Done/evidence:** Median/tail latency and failures are published; no unmeasured real-time promise.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

### Phase 5: Characters and avatars

Primary home: `features/character-continuity/, features/english-speaking-friend/web/`.

#### VG-049 — Review character and voice consent

- **Status:** TODO. **Home:** `features/character-continuity/, docs/security/`
- **Prerequisites:** Owner-approved original/consented characters and voice policy.
- **Scope:** Define approved synthetic/owned likenesses and allowed uses across learning and creation.
- **Done/evidence:** No uploaded real-person likeness is used without verified permission.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-050 — Add an inclusive avatar preference model

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, features/character-continuity/`
- **Prerequisites:** VG-049; current illustrated-character UI.
- **Scope:** Provide accessible disclosed synthetic choices independent of learner identity.
- **Done/evidence:** Preferences persist only as chosen and do not expose private learning history.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-051 — Support reduced motion and visual fallback

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, tests/browser/`
- **Prerequisites:** Existing illustration; accessibility/reduced-motion checks can proceed now.
- **Scope:** Keep learning usable with animation disabled or rendering unavailable.
- **Done/evidence:** Keyboard/text-only/reduced-motion browser checks pass.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-052 — Drive simple mouth animation from timings

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, features/audio-studio/`
- **Prerequisites:** VG-046, VG-050, VG-051; validated timings and stop behavior.
- **Scope:** Use validated speech events/visemes rather than pretending an illustration is live video.
- **Done/evidence:** Animation follows the current turn and stops on interruption.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-053 — Evaluate lip synchronization

- **Status:** TODO. **Home:** `features/character-continuity/, docs/quality/`
- **Prerequisites:** VG-052; cleared audio/visual samples and manual synchronization rubric.
- **Scope:** Measure speech/visual offset with approved assets and named rendering hardware.
- **Done/evidence:** A reproducible small evaluation reports latency and artifacts.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-054 — Optimize avatar rendering

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, docs/quality/`
- **Prerequisites:** VG-052; named low-power and normal test devices.
- **Scope:** Profile frame rate, memory and device limits before richer graphics.
- **Done/evidence:** Low-power device measurements and fallbacks are documented.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-055 — Design optional camera permissions

- **Status:** TODO. **Home:** `features/english-speaking-friend/web/, docs/security/`
- **Prerequisites:** VG-049; owner-approved useful camera purpose and privacy design before capture.
- **Scope:** Keep camera off by default; define a useful consented purpose before implementation.
- **Done/evidence:** Capture/revoke/delete tests pass; no emotion/truth inference is introduced.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-056 — Validate richer avatar research

- **Status:** TODO. **Home:** `features/character-continuity/, docs/quality/`
- **Prerequisites:** VG-048, VG-053, VG-054; bounded research budget and learner value study.
- **Scope:** Compare learning value with simple illustration against cost, privacy and latency.
- **Done/evidence:** A measured experiment justifies promotion; photorealistic video stays optional.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

### Phase 6: Image generation

Primary home: `features/image-studio/, integrations/comfyui/`.

#### VG-057 — Record real GPU preflight

- **Status:** TODO. **Home:** `scripts/hardware/, notebooks/colab/, docs/operations/`
- **Prerequisites:** Access to owner-approved hardware; no checkpoint required for inspection.
- **Scope:** Measure actual GPU/VRAM/RAM/disk/runtime constraints on owner-approved hardware.
- **Done/evidence:** Save hardware evidence without downloading a checkpoint first.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-058 — Select one licensed image checkpoint

- **Status:** TODO. **Home:** `features/image-studio/, docs/research/, docs/security/`
- **Prerequisites:** VG-002, VG-057; owner approval of exact weight/license/resource costs.
- **Scope:** Choose exact model rights, size and workflow based on the measured machine.
- **Done/evidence:** Decision records source/weight licenses, hashes, cost ceiling and owner approval.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-059 — Verify model download integrity

- **Status:** TODO. **Home:** `scripts/hardware/, docs/research/ (weights outside Git)`
- **Prerequisites:** VG-058; approved download sources and expected hashes.
- **Scope:** Create controlled manifests and checksum verification for approved files only.
- **Done/evidence:** Truncated/changed artifacts fail verification; no TLS/hash checks are disabled.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-060 — Install a pinned external engine

- **Status:** TODO. **Home:** `integrations/comfyui/, docs/operations/ (runtime outside Git)`
- **Prerequisites:** VG-058, VG-059; external engine/node/version and security review.
- **Scope:** Keep a separately versioned inference runtime outside the owned product source.
- **Done/evidence:** Record exact engine/custom-node versions and license/security review.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-061 — Approve one image workflow

- **Status:** TODO. **Home:** `integrations/comfyui/, features/image-studio/`
- **Prerequisites:** VG-060, VG-012; typed permitted graph and operator allowlist.
- **Scope:** Allowlist a typed versioned graph with supported inputs rather than arbitrary user JSON.
- **Done/evidence:** Unknown nodes/settings and path/network escape attempts are rejected.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-062 — Connect the real image worker

- **Status:** TODO. **Home:** `features/image-studio/, services/worker/, integrations/comfyui/`
- **Prerequisites:** VG-061, VG-063; approved actual GPU runtime and licensed weights.
- **Scope:** Use the existing job boundary for one permitted generation path with explicit failures.
- **Done/evidence:** A real job produces a validated PNG, not a mock receipt.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-063 — Persist real artifact provenance

- **Status:** TODO. **Home:** `services/api/storage.py, services/api/contracts.py, features/image-studio/`
- **Prerequisites:** VG-004, VG-005; real-artifact schema/hash/download design (may precede generation).
- **Scope:** Record immutable model/workflow/settings/input/output metadata and file hashes.
- **Done/evidence:** Downloaded bytes match metadata and survive a controlled restart.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-064 — Benchmark image quality and resources

- **Status:** TODO. **Home:** `docs/quality/, features/image-studio/`
- **Prerequisites:** VG-062; genuine decoded outputs and fixed evaluation prompts/seeds.
- **Scope:** Evaluate fixed prompts/seeds and actual latency/memory/cost without marketing parity claims.
- **Done/evidence:** Publish successes, failures and human review methodology.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-065 — Add mask-based editing

- **Status:** TODO. **Home:** `features/image-studio/, integrations/comfyui/`
- **Prerequisites:** VG-062, VG-064; supported editing workflow and consented masks/reference images.
- **Scope:** Integrate a supported editing workflow with bounded masks and owned references.
- **Done/evidence:** Real edit inputs/outputs and invalid-mask cases are verified.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-066 — Add restoration/upscaling

- **Status:** TODO. **Home:** `features/image-studio/, integrations/comfyui/`
- **Prerequisites:** VG-062, VG-064; separately reviewed upscaler/model rights.
- **Scope:** Reuse a reviewed upscaler with honest detail/identity limitations.
- **Done/evidence:** Real output dimensions, decoding, resource use and failure handling are measured.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

### Phase 7: Video generation

Primary home: `features/video-studio/, integrations/comfyui/`.

#### VG-067 — Select a feasible video model

- **Status:** TODO. **Home:** `features/video-studio/, docs/research/, docs/security/`
- **Prerequisites:** VG-057, VG-064; approved exact video weights and measured hardware limits.
- **Scope:** Choose an exact permitted variant after real image/GPU evidence and budget review.
- **Done/evidence:** No unverified model/version/VRAM assumption becomes a hardcoded promise.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-068 — Approve a reproducible video workflow

- **Status:** TODO. **Home:** `features/video-studio/, integrations/comfyui/`
- **Prerequisites:** VG-067; exact engine/nodes/weights and permitted frame/resolution settings.
- **Scope:** Pin engine/nodes/weights and model-specific frame/resolution constraints.
- **Done/evidence:** Typed validation rejects unsupported combinations before GPU work.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-069 — Deliver one genuine image-to-video path

- **Status:** TODO. **Home:** `features/video-studio/, services/worker/, integrations/comfyui/`
- **Prerequisites:** VG-068, VG-071; genuine approved source image and real GPU runtime.
- **Scope:** Use a permitted reference image and preserve job settings/provenance.
- **Done/evidence:** A decodable short MP4 is produced and inspected on named hardware.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-070 — Deliver supported text-to-video

- **Status:** TODO. **Home:** `features/video-studio/, integrations/comfyui/`
- **Prerequisites:** VG-068, VG-071; selected model must explicitly support text-to-video.
- **Scope:** Add only when the selected model supports the capability and hardware fits.
- **Done/evidence:** Actual output and an unsupported-capability error are demonstrated.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-071 — Validate media structure

- **Status:** TODO. **Home:** `features/video-studio/, services/api/, tests/`
- **Prerequisites:** VG-004, VG-063; reviewed media decoder and controlled fixtures (can precede generation).
- **Scope:** Inspect codec, dimensions, frame count, frame rate, duration and audio streams.
- **Done/evidence:** Corrupt/mislabeled outputs fail and verified metadata matches the file.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-072 — Handle OOM, interruption and retry

- **Status:** TODO. **Home:** `services/worker/, features/video-studio/, tests/`
- **Prerequisites:** VG-069; controlled failure/restart budget on actual hardware.
- **Scope:** Make memory failures explicit and prevent duplicate expensive work.
- **Done/evidence:** Controlled fault/restart tests and actual hardware limits are recorded.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-073 — Expose real motion/camera controls

- **Status:** TODO. **Home:** `features/video-studio/, apps/web/`
- **Prerequisites:** VG-069; selected workflow must support each exposed control.
- **Scope:** Offer controls only for workflows that support them.
- **Done/evidence:** Fixed examples demonstrate the effect and limitations of each control.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-074 — Version clips and reshoots

- **Status:** TODO. **Home:** `features/video-studio/, services/api/storage.py`
- **Prerequisites:** VG-005, VG-069; immutable artifact/take provenance.
- **Scope:** Keep previous takes when regenerating one clip or supported extension.
- **Done/evidence:** The user can compare/download prior takes without losing provenance.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

### Phase 8: Media finishing and sound

Primary home: `features/audio-studio/, features/movie-studio/`.

#### VG-075 — Create safe FFmpeg command planning

- **Status:** TODO. **Home:** `features/movie-studio/, integrations/ (reviewed FFmpeg boundary)`
- **Prerequisites:** VG-004; reviewed FFmpeg executable/version and synthetic fixtures.
- **Scope:** Build argument arrays from validated operations and controlled paths.
- **Done/evidence:** No prompt/path content becomes shell code; invalid operations are rejected.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-076 — Implement trim/concat exports

- **Status:** TODO. **Home:** `features/movie-studio/, services/worker/`
- **Prerequisites:** VG-075; decodable rights-cleared clips; synthetic fixtures can start early.
- **Scope:** Assemble compatible approved clips with explicit time/format handling.
- **Done/evidence:** A real playable export has expected frames and duration.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-077 — Mix speech and background audio

- **Status:** TODO. **Home:** `features/audio-studio/, features/movie-studio/`
- **Prerequisites:** VG-045, VG-075; cleared source audio and explicit timing/gain rules.
- **Scope:** Apply track timing, gains and clipping protection using reviewed media tools.
- **Done/evidence:** A decoded export has measured alignment/loudness and no unintended clipping.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-078 — Export captions and transcripts

- **Status:** TODO. **Home:** `features/audio-studio/, features/movie-studio/`
- **Prerequisites:** VG-046, VG-075; reviewed Unicode/timestamp subtitle formats.
- **Scope:** Generate supported subtitle formats with Unicode/timestamp validation.
- **Done/evidence:** Bangla/English captions align and render in a tested player.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-079 — Evaluate a licensed music/SFX model

- **Status:** TODO. **Home:** `features/audio-studio/, docs/research/`
- **Prerequisites:** VG-002, VG-057; explicit owner budget/weight approval.
- **Scope:** Separate source and weight rights and measure resource/cost before adopting it.
- **Done/evidence:** One real cleared output and reproducible settings are recorded.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-080 — Create proxy media previews

- **Status:** TODO. **Home:** `features/movie-studio/, services/api/`
- **Prerequisites:** VG-071, VG-075; immutable original assets and bounded preview plans.
- **Scope:** Produce bounded preview/poster assets without overwriting original media.
- **Done/evidence:** Preview files decode and preserve links to immutable original artifacts.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-081 — Validate seek and interrupted exports

- **Status:** TODO. **Home:** `features/movie-studio/, services/worker/`
- **Prerequisites:** VG-076, VG-077; fault/cancellation fixtures and partial-output policy.
- **Scope:** Handle long media, failed encoders and cancellation without marking partial files complete.
- **Done/evidence:** Fault tests leave explicit failed state and no broken successful download.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-082 — Add reviewed export presets

- **Status:** TODO. **Home:** `features/movie-studio/, docs/operations/`
- **Prerequisites:** VG-076, VG-077, VG-078, VG-081; player compatibility evidence.
- **Scope:** Offer only validated codec/container/resolution/audio combinations.
- **Done/evidence:** Each preset has a playable real artifact and documented limits.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

### Phase 9: Continuity and movie creation

Primary home: `features/character-continuity/, features/movie-studio/`.

#### VG-083 — Version reusable character references

- **Status:** TODO. **Home:** `features/character-continuity/, services/api/`
- **Prerequisites:** VG-049, VG-005; rights metadata and scoped reference access.
- **Scope:** Store consented reference sheets, approved voices and changes as immutable versions.
- **Done/evidence:** Shots link to exact versions and revoked access cannot be bypassed.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-084 — Track wardrobe and environments

- **Status:** TODO. **Home:** `features/character-continuity/, features/movie-studio/`
- **Prerequisites:** VG-083; approved continuity/reference schema.
- **Scope:** Distinguish intended scene changes from continuity errors.
- **Done/evidence:** A multi-shot record preserves declared changes and reference provenance.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-085 — Evaluate identity drift

- **Status:** TODO. **Home:** `features/character-continuity/, docs/quality/`
- **Prerequisites:** VG-064, VG-069, VG-083; human evaluation of cleared multi-shot examples.
- **Scope:** Use a fixed approved multi-shot set with human review and reported limitations.
- **Done/evidence:** Measurements do not claim perfect identity or use unconsented biometric data.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-086 — Add supported reference conditioning

- **Status:** TODO. **Home:** `features/character-continuity/, integrations/comfyui/`
- **Prerequisites:** VG-083, VG-085; chosen model/workflow actually supports reference conditioning.
- **Scope:** Route approved references only to models/workflows that actually support them.
- **Done/evidence:** Capability rejection and real conditioning examples are verified.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-087 — Represent scripts/scenes/shots/takes

- **Status:** TODO. **Home:** `features/movie-studio/, services/api/, packages/schemas/`
- **Prerequisites:** VG-004, VG-005; stable versioned movie-domain schema.
- **Scope:** Create versioned structures with stable IDs and scoped project access.
- **Done/evidence:** Editing one shot preserves previous takes and unrelated scenes.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-088 — Build an editable storyboard

- **Status:** TODO. **Home:** `features/movie-studio/, apps/web/`
- **Prerequisites:** VG-087, VG-083; accessible editing and no hidden compute spend.
- **Scope:** Connect script/shot descriptions to references and approved results.
- **Done/evidence:** Users can reorder/revise without losing history or silently spending compute.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-089 — Serialize a non-destructive timeline

- **Status:** TODO. **Home:** `features/movie-studio/, packages/schemas/`
- **Prerequisites:** VG-087; explicit timeline serialization/validation format.
- **Scope:** Define clips/tracks/transitions/audio and stable export plans.
- **Done/evidence:** Round-trip/edit/validation tests preserve IDs, timings and provenance.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-090 — Add a human-approved AI director

- **Status:** TODO. **Home:** `features/movie-studio/, services/api/, docs/security/`
- **Prerequisites:** VG-028, VG-088, VG-089, VG-096; bounded tools and human approval.
- **Scope:** Suggest shot plans and revisions through bounded tools and budgets.
- **Done/evidence:** Suggestions cannot execute workflows, spend, publish or replace shots without authorization.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-091 — Assemble a 60-second demonstration

- **Status:** TODO. **Home:** `features/movie-studio/, docs/quality/`
- **Prerequisites:** VG-069, VG-077, VG-078, VG-082, VG-085, VG-089; measured cleared assets.
- **Scope:** Combine individually regenerable clips with coherent reviewed characters, speech and captions.
- **Done/evidence:** A playable real sequence and measured continuity/cost report exist.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-092 — Explore longer production incrementally

- **Status:** TODO. **Home:** `features/movie-studio/, docs/research/`
- **Prerequisites:** VG-091; owner-approved longer experiment with budget/stop condition.
- **Scope:** Add resumable scene assembly only after shorter proofs; avoid one-prompt feature-film promises.
- **Done/evidence:** A bounded experiment defines failures, storage, budget and a stop condition.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

### Phase 10: Production identity, safety and release

Primary home: `services/, shared platform and infrastructure to be introduced deliberately`.

#### VG-093 — Implement real account identity

- **Status:** TODO. **Home:** `services/api/, apps/web/, docs/security/`
- **Prerequisites:** VG-003; reviewed identity choice and account/privacy threat model.
- **Scope:** Choose a reviewed identity provider/session model rather than treating a random local cookie as an account.
- **Done/evidence:** Login/logout/session rotation and account recovery have security tests.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-094 — Isolate creative projects by owner/tenant

- **Status:** TODO. **Home:** `services/api/, services/worker/, tests/`
- **Prerequisites:** VG-093, VG-005; explicit owner/tenant schema and migration.
- **Scope:** Apply authorization to projects, jobs, files and asset references.
- **Done/evidence:** Cross-owner/tenant read/write/download tests fail safely.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-095 — Secure private worker transport

- **Status:** TODO. **Home:** `services/worker/, integrations/, docs/security/, docs/operations/`
- **Prerequisites:** VG-093; private authenticated transport and credential-rotation design.
- **Scope:** Add authenticated encrypted worker communication and narrowly scoped credentials.
- **Done/evidence:** No public unauthenticated GPU/worker endpoint is introduced.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-096 — Add account quotas and cost accounting

- **Status:** TODO. **Home:** `services/api/, services/worker/, docs/operations/`
- **Prerequisites:** VG-094, VG-095; measured model costs and owner-approved spending limits.
- **Scope:** Bound concurrency/storage/model usage and require explicit spending authorization.
- **Done/evidence:** Bypass/replay/concurrent-request tests preserve actual cost ceilings.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-097 — Quarantine uploads and rights metadata

- **Status:** TODO. **Home:** `services/api/, features/character-continuity/, docs/security/`
- **Prerequisites:** VG-094; rights review, decoder/path/resource isolation and approved storage.
- **Scope:** Validate content/type/path/resource limits and provenance before model use.
- **Done/evidence:** Unsafe uploads cannot run code, escape storage or become approved public assets.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-098 — Extend deletion to backups and vendors

- **Status:** TODO. **Home:** `scripts/maintenance/, services/api/, docs/operations/`
- **Prerequisites:** VG-007, VG-024, VG-093; actual backup/vendor inventory and deletion policy.
- **Scope:** Define actual retention, export, recovery and third-party processing commitments.
- **Done/evidence:** Document verified deletion boundaries; do not promise erasure outside tested systems.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-099 — Deploy a protected staging environment

- **Status:** TODO. **Home:** `docs/operations/, deployment configuration introduced in its own reviewed collection`
- **Prerequisites:** VG-094, VG-095, VG-096, VG-097, VG-098; approved hosting/resources.
- **Scope:** Add reproducible configuration, TLS, secrets and rollback without shipping private data.
- **Done/evidence:** Fresh deployment and rollback checks pass under owned approved infrastructure.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-100 — Exercise incidents and disaster recovery

- **Status:** TODO. **Home:** `docs/operations/, docs/security/, tests/`
- **Prerequisites:** VG-007, VG-098, VG-099; authorized isolated incident drills.
- **Scope:** Test compromised access, failed workers, corrupt files and restored databases.
- **Done/evidence:** Runbooks identify detection, containment, restoration and communication ownership.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-101 — Measure production capacity

- **Status:** TODO. **Home:** `scripts/quality/, docs/quality/, docs/operations/`
- **Prerequisites:** VG-099; authorized load-test target and fixed budget ceilings.
- **Scope:** Load test only the intended protected environment with approved budgets.
- **Done/evidence:** Publish latency/tail failures/cost rather than extrapolating from the local demo.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-102 — Complete release/legal review

- **Status:** TODO. **Home:** `docs/security/, docs/product/, docs/quality/`
- **Prerequisites:** VG-001, VG-002, VG-020, VG-021, VG-100, VG-101; review only advertised capabilities.
- **Scope:** Audit source/weights/voices/media, terms, safety, accessibility and unsupported claims.
- **Done/evidence:** Named release gates and actual artifacts support every advertised capability.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-103 — Design sustainable usage and pricing

- **Status:** TODO. **Home:** `docs/operations/COST_PLAN.md, docs/product/`
- **Prerequisites:** VG-096, VG-101; actual compute/storage/support measurements and owner decisions.
- **Scope:** Base plans on measured model/storage/support costs, not unlimited free compute.
- **Done/evidence:** Cost assumptions, caps, failure accounting and owner approval are recorded.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

#### VG-104 — Publish the release evidence and maintenance plan

- **Status:** TODO. **Home:** `README.md, PROJECT_HANDOFF.md, docs/operations/, docs/memory/`
- **Prerequisites:** VG-102, VG-103; actual release artifacts, CI and maintenance ownership.
- **Scope:** Document versions, reproducible setup, outputs, limitations and security update ownership.
- **Done/evidence:** A new maintainer can reproduce the release and identify all remaining gaps.
- **PR validation:** Targeted regression tests plus `npm run verify` for changed active behavior. Provide actual hardware/manual evidence when unit tests cannot establish the result.

## Recommended first assignments

Keep PRs small and independent. These are suggested starting tasks, not remote issues:

| Priority / parallel lane | Task | Required result |
|---|---|---|
| Engineering first | VG-005 | Version both local schemas with a migration fixture and preserved saved data. |
| Delivery in parallel | VG-011 | Reproduce the current verifier on a clean task and add appropriate CI coverage; the local verifier already exists. |
| Learning in parallel | VG-013, then VG-014 | Human-review the current authored content and build a consented evaluation rubric. |
| Usability in parallel | VG-021, VG-023, VG-051 | Extend accessibility, network recovery and reduced-motion evidence beyond current smoke checks. |
| Real-model gate | VG-025 → VG-026 → VG-027 → VG-028 | Owner-approved existing runtime and genuine meaning-preservation evaluation. |
| Creative hardware gate | VG-057 → VG-058 → VG-059 → VG-060 → VG-061 → VG-062 | Named hardware, cleared weights, verified files, pinned engine and a genuine image. VG-063 can proceed alongside engine setup. |
| Before any public access | VG-093 → VG-094 / VG-095 → VG-096 / VG-097 / VG-098 → VG-099 | Account/tenant isolation, secure transport, limits, rights and deletion before protected staging. |

Phase numbers group related work, not a requirement to finish every creative feature
before security. In particular, production identity/authorization can start early.
Documentation-only tasks need link/provenance checks; model/hardware tasks need the
actual named runtime and outputs. Do not run expensive work simply to fill a checklist.

## Definition of done for every contribution

- The promised user action works with a real request/output at the required level.
- Existing behavior and archived work remain preserved; migrations/rollback are explicit.
- Error, unsupported, privacy and ownership cases have meaningful coverage.
- Dependencies, versions, rights, resource cost and processing boundaries are documented.
- Tests actually executed and the target/count/exit status are recorded; no zero-test victory.
- The status table and next task are accurate. A mock receipt is never an image,
  a protocol stub is never model quality, and a visible face is never live video.
- The PR is reviewed before an authorized merge; no autonomous background monitoring
  or issue creation is implied by this document.
