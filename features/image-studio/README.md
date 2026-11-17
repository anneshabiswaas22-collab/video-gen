# Image studio

Create and edit still images, masks, backgrounds, product visuals and reusable reference sheets. This feature owns image-specific controls and results; projects, jobs, permissions and artifact provenance belong to the shared platform.

**Current status:** planned and specified in the existing registry; no owned image-generation path or real GPU output is verified in this checkout. Imported workflows are reference material.

## Scope and first delivery

Start with one permitted text-to-image workflow producing a genuine PNG with prompt, seed, model revision, settings and artifact checksum. Add image editing, inpainting, outpainting, removal and upscaling only after the first path works. Expose controls only when the selected model supports them.

Traceability: [M1 roadmap](../../docs/product/ROADMAP.md), [IMG-01–05 registry](../../docs/product/FEATURE_REGISTRY.md), [benchmark rules](../../docs/quality/BENCHMARKS.md). Reference sheets feed [character continuity](../character-continuity/README.md), [video](../video-studio/README.md) and optional licensed avatars for the [English friend](../english-speaking-friend/README.md).

## Dependencies and acceptance

Reuse the proposed ComfyUI adapter, capability registry, asynchronous worker and durable artifact metadata. Select the exact model only after hardware and separate code/weight/commercial-use checks. See the [source stack](../../docs/research/OPEN_SOURCE_STACK.md), [license/security rules](../../docs/security/LICENSE_SECURITY.md) and preserved [ComfyUI source](../../AnalyseFuture/references/inference-engine/comfyui/).

CPU checks should exercise schema validation, unsupported controls, idempotent jobs, failures and artifact access boundaries. GPU acceptance requires opening and validating a real PNG, recording runtime and peak VRAM, and repeating the documented workflow. A mock receipt is not an image result. **GPU checks: NOT RUN.**
