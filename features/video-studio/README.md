# Video studio

Generate and revise short clips from text or a reference image. Later scope includes supported first/last-frame conditioning, camera controls, motion transfer, reshoots, interpolation and clip extension.

**Current status:** planned; no owned video adapter or genuine generated MP4 has been verified in this checkout. Existing imported examples do not prove local inference works.

## Scope and first delivery

Begin with one short image-to-video job on suitable hardware. Preserve the input reference, selected model and workflow revisions, seed, settings and output metadata. Make failures, cancellation and out-of-memory conditions explicit. Do not promise that arbitrary camera instructions or character identity will be obeyed exactly.

Traceability: [M2 roadmap](../../docs/product/ROADMAP.md), [VID-01–06 registry](../../docs/product/FEATURE_REGISTRY.md), [GPU preflight](../../docs/operations/GPU_COLAB.md). Use [image references](../image-studio/README.md) and [continuity records](../character-continuity/README.md); send accepted takes to the [movie studio](../movie-studio/README.md).

## Dependencies and acceptance

Reuse the shared asynchronous job system, ComfyUI integration, artifact store and media validation tools. Wan and other named models remain candidates pending exact checkpoint, licensing and hardware review. [Preserved FreeField](../../AnalyseFuture/references/workflow-studio/freefield/) is a workflow reference, not this feature's implementation.

CPU checks should cover job transitions, retries, cancellation, capability gating and references to inaccessible assets. GPU acceptance requires a decodable MP4 with verified frame count, duration, resolution and codec, plus provenance, runtime and peak VRAM. **GPU checks: NOT RUN.** Long films are assembled from approved clips rather than promised as a single reliable generation.
