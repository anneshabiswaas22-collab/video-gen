# AnalyseFuture — preserved material for future analysis

Nothing here was discarded during the 2026-11-17 repository reorganization.
These are preserved imports and examples, not approved product dependencies,
owned VideoGen features, or a finding of malicious code.

| Folder | Contents | Use and limits |
|---|---|---|
| [upstream/ComfyUI-master](upstream/ComfyUI-master/ComfyUI-master/README.md) | Complete imported ComfyUI tree, including its original wrapper | Inference-engine reference; GPL-3.0 obligations and each model/custom-node license require separate review. |
| [upstream/freefield-main](upstream/freefield-main/README.md) | Complete imported FreeField studio | Workflow/UI/reference tests; MIT source does not establish media or weight rights. |
| [imported-examples](imported-examples/index.json) | Original root index and 19 loose media folders | Kept together so their relative layout survives; do not deduplicate or publish assets without provenance review. |

[RELOCATION_MANIFEST.json](RELOCATION_MANIFEST.json) records the original path,
new path, byte count, SHA-256, original Git blob and mode for every one of the
2,131 relocated tracked files. Original filenames, licenses and file bytes are
unchanged. Ignored local dependencies and outputs moved with FreeField and are
not committed. Historical copies remain recoverable from the source commit
recorded in the manifest.

Run `python scripts/check_structure.py` from the repository root to check the
preserved files and the feature map. This verifies preservation, not software
trustworthiness. The current structure and recovery limits are explained in
[the reorganization report](../docs/REPOSITORY_REORGANIZATION.md).

Do not automatically install, execute, promote, or delete this material. A future
integration task must first check provenance, licenses, security, exact upstream
versions, runtime compatibility and an owner-approved budget. Prefer a pinned
external dependency over another wholesale copy into the active product.

## Recovery reports

- [Repository audit](REPOSITORY_AUDIT.txt)
- [Complete file inventory](COMPLETE_FILE_INVENTORY.txt)
- [Feature inventory](FEATURE_INVENTORY.txt)
- [Duplicate analysis](DUPLICATE_ANALYSIS.txt)
- [Security audit and limits](SECURITY_AUDIT.txt)
- [Original-to-new mapping](ORIGINAL_TO_NEW_PATH_MAPPING.txt)
- [Consolidation report](CONSOLIDATION_REPORT.txt)
- [Archived-files manifest](ARCHIVED_FILES_MANIFEST.txt)
- [Future vision and roadmap](PROJECT_VISION_AND_FUTURE_ROADMAP.txt)
- [Technical debt](TECHNICAL_DEBT.txt)
- [Tests and validation](TEST_AND_VALIDATION_REPORT.txt)
- [Migration summary](MIGRATION_SUMMARY.txt)
- [Next developer instructions](NEXT_DEVELOPER_INSTRUCTIONS.txt)
- [Work progress](WORK_PROGRESS.txt)
