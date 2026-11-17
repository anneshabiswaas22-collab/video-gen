# Shared utilities

- `maintenance/`: repository documentation and preservation utilities used by
  the existing root CI workflow, with paths updated to the functional layout.
- `hardware/`: GPU/CPU/RAM/storage inspection, without model downloads.

No utility, test, build, compilation or application startup was executed in the
current restructuring task. Future execution is separate from this static review.
See [project structure](../PROJECT_STRUCTURE.md) and
[operations](../docs/operations/BUILD_RUN.md).

## Active development commands

The owner subsequently authorized implementation and tests. `development/dev.sh`
starts the owned API/web app; `development/smoke_mock.py` executes an isolated
CPU job/receipt check. The earlier no-execution paragraph refers to sorting only.
See [current setup](../docs/operations/BUILD_RUN.md).
