# Architecture decision log

Decision statuses: ACCEPTED (planning constraint), PROPOSED (to verify in M0), REJECTED, OPEN. These decisions summarize owner instructions and the latest architecture guidance, not an executed product.

| ID | Status | Decision and rationale |
|---|---|---|
| ADR-001 | ACCEPTED | **Own the app** in anneshabiswaas22-collab/video-gen rather than rebrand/copy one proprietary product. |
| ADR-002 | ACCEPTED | Use an application **monorepo** with external model engines as adapters/dependencies; avoid indiscriminate code merging. |
| ADR-003 | PROPOSED | ComfyUI as default workflow backend; verify GPL architecture and distribution obligations before release. |
| ADR-004 | PROPOSED | FreeField as an app/workflow source to **study and selectively reuse**, not guaranteed full product foundation. |
| ADR-005 | PROPOSED | Wan 2.2 small/compatible checkpoint as first video; choose after Colab GPU preflight. |
| ADR-006 | PROPOSED | FLUX or Qwen for images, Kokoro for speech, ACE-Step for music, FFmpeg for media export. |
| ADR-007 | ACCEPTED | Codex Cloud for engineering; GPU verification on Colab initially; Kaggle optional, dedicated GPUs eventually. |
| ADR-008 | ACCEPTED | Reuse first to reduce Codex credit costs; evaluate LightX2V and optimizations through benchmarks. |
| ADR-009 | ACCEPTED | Character continuity, camera controls and multi-scene movie production are primary differentiators. |
| ADR-010 | ACCEPTED | Never claim frontier-quality parity, current availability, hardware performance, or open-source licensing without verification. |
| ADR-011 | OPEN | App original-code license, final product name/brand, target launch pricing, hosting jurisdiction, auth provider. |
| ADR-012 | OPEN | Real GPU configuration, model license versions, first checkpoint hash, cost ceilings, storage architecture. |

## Corrections / ambiguities from earlier research
- The question "K 3.1 Pro" may have referred to a Kling video product, but a prior response identified it as Kimi without clear confirmation. **Do not build against that assumption**.
- Model names and version counts in earlier plans may have changed. Use official repository/model cards, not stale conversational claims.
- "FreeField supports 120 apps" and competitor claims come from third-party documentation; verify exact implementation and maturity.
- Being publicly downloadable does not mean an entire model's original training system is public.
- A tutorial that says "unlimited-length" does not imply a single reliable hours-long coherent generation.
- Separating GPL/AGPL components into services does not automatically resolve legal obligations.

## When architecture changes
Create a new ADR in this file with alternatives, license/security impact, benchmark evidence, migration/rollback plan and acceptance tests. Never silently replace a core engine due to a new trending repository.

## ADR-013 — Preserve imports; organize the combined product by feature

**ACCEPTED, 2026-11-17, explicit owner instruction.** Combine the existing studio
vision with the English-speaking AI friend; use six feature entry folders.
Retain stable shared documentation paths. Move full third-party imports and
loose examples intact into `AnalyseFuture` with original-blob verification; do
not split upstream frameworks or merge their UI into owned application code.
No owned competing implementations were found on the accessible current refs.
Historical source-repository PR evidence remains labeled and unmodified.

Alternative rejected: delete imports or hard-reset main, losing useful evidence
and uncertain assets. Alternative deferred: importing a different repository's
unmerged mock implementation without verifying source availability and scope.
No source-code behavior/API/database change is required for this reorganization.
Separate the tutor's interactive session from asynchronous studio jobs, and
private learning records from creative assets. Source/weight/media rights and
real GPU validation remain release gates. Rollback and checks are recorded in
[the recovery report](REPOSITORY_REORGANIZATION.md). Direct ordinary push to
`main` without a PR is authorized for this recovery task; no force push.
