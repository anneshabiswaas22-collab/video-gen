# AnalyseFuture — preserved reference and recovery collections

Everything here has a functional home and remains outside the owned product's
runtime. Preservation is not approval to execute, publish or redistribute it.
Original source, licenses and media bytes remain; no duplicate was discarded.

| Collection | Contents and responsibility |
|---|---|
| [Inference engine](references/inference-engine/comfyui/README.md) | Cohesive ComfyUI source, model loading, graph execution and engine-specific assets/tests/configuration; duplicate wrapper removed. |
| [Workflow studio](references/workflow-studio/freefield/README.md) | Cohesive FreeField server, manifests, workflows, browser UI, laboratory, tooling and tests. |
| [Collected gallery](references/workflow-studio/freefield/web/examples/index.json) | Original index plus all118 example folders; fragments reunited with provenance. |
| [Analysis](analysis/REPOSITORY_AUDIT.txt) | Earlier repository, feature, duplicate and consolidation findings. |
| [Repository inventory](repository-inventory/COMPLETE_FILE_INVENTORY.txt) | Earlier file inventories, original mappings and the unchanged first relocation manifest. |
| [Security reports](security-reports/SECURITY_AUDIT.txt) | Bounded earlier static security findings and unresolved risks. |
| [Migration history](migration-history/MIGRATION_SUMMARY.txt) | Prior delivery and validation observations, retained as historical evidence. |
| [Project history](project-history/README.before-reorganization.txt) | Exact original README snapshot. |

The accepted combined product idea and future roadmap now belong in
[product documentation](../docs/product/INDEX.md). Active continuation, technical
debt and work progress belong in [development](../docs/development/INDEX.md).
They are useful project knowledge, not uncertain executable material.

Read [PROJECT_STRUCTURE.md](../PROJECT_STRUCTURE.md) and the current
[file-placement ledger](../docs/repository/FILE_PLACEMENT.json) to resolve any old
path in a historical report. The earlier manifest remains unchanged and describes
its original move; the new ledger composes that mapping with the current layout.

The gallery collection contains480 actual assets and its original index.
Its metadata references162 absent MP4s. Their absence predates this change;
files were not generated, fetched or silently replaced. The
[gallery analysis](../docs/repository/GALLERY_CONSOLIDATION.md) identifies every
app, original asset and missing reference. Manually starting the archived UI would
expose those missing links and its existing thumbnail autoplay. No root product
entrypoint, automatic installer or service startup is added.

**No tests were run for this functional sorting pass.** Earlier tests in migration
history do not verify the new paths. Source packages keep their internal imports,
configuration and data conventions intact; inspect rights, security, versions and
runtime behavior separately before any promotion or execution.
