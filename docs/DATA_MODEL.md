# Initial data model (proposed)

These definitions make early backend implementation consistent; they are not yet deployed.

- **Organization/User/Membership:** subjects, roles, per-tenant isolation and quotas.
- **Project:** owner, name, lifecycle, storage namespace, creative settings, export versions.
- **Asset:** immutable content hash, MIME, duration, fps, dimensions, rights/consent metadata, storage key, project scope.
- **Character:** unique stable identity, reference asset versions, voice style references, wardrobe variants, allowed use.
- **Environment:** approved reference images, layout/camera notes, props, asset versions.
- **ModelDefinition:** source URL and pinned commit, weight hash and license, capabilities, recommended hardware, supported parameters.
- **WorkflowDefinition:** validated versioned engine specification, dependency inventory, input/output JSON schemas, estimated VRAM.
- **Worker:** private worker ID, GPU description, capabilities, connected/disconnected, resource metrics.
- **GenerationJob:** idempotency key, immutable input/settings, status, progress, estimate/actual usage, parent job, retry count, error, worker ID.
- **GenerationArtifact:** generated asset, job, quality review, provenance, lineage to source assets and parameters.
- **Film/Scene/Shot/Take:** story and chronological order, character/environment versions, timecode, approved take, alternative takes.
- **TimelineTrack/Clip/Transition:** editable non-destructive time intervals, audio/video/subtitle links, effect settings.
- **AuditEvent/UsageEntry:** actor, operation, limited metadata, GPU seconds, paid API costs, policy decisions.

## Key invariants
- Content assets use immutable IDs and hashes; changing reference artwork creates new versions.
- A job can be retried, but completed artifacts never silently change.
- Users can access only assets and jobs authorized for their organization/project.
- A scene can be re-rendered without regenerating unrelated shots.
- Model definitions have stable IDs with versioned capabilities; don't mutate features silently.
- Cost entries are reconciled to real worker usage; failed jobs retain failure diagnostics.
- Audit logs do not leak passwords, provider keys, private uploads or high-risk content.

## Schema first
Write Pydantic and TypeScript contracts; generate OpenAPI client types where possible. Migration scripts and rollback tests accompany database changes. Do not store enormous video binaries in PostgreSQL.
