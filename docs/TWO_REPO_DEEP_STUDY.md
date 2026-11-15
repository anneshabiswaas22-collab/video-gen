# M0 engineering research — exactly two primary foundations

**Source inspection date:** 2026-11-15. **Scope:** code review and GitHub metadata only, no
GPU, no model downloads and no runtime benchmarks. These are study snapshots, **not**
approval to distribute code/weights or a claim of replicated model quality.

## Evidence baseline — our own repository

- VideoGen `main` was inspected at `2a88181dc0408f6477dd52a6ed8ded762f149bcd`.
- Pre-M0 tree contained README, AGENTS, CONTRIBUTING, 20+ documentation files,
  `.github/workflows/docs-check.yml`, `scripts/check_docs.py`,
  `scripts/gpu_preflight.py`, and `notebooks/colab/00_gpu_preflight.ipynb`.
- No production frontend, generation API, worker or model adapter appeared in that tree.
  Notebook/preflight is inspection-only. No image/video/audio inference proof.
- Issues [#1](https://github.com/anneshabiswaas22-collab/video-gen/issues/1)
  and [#3](https://github.com/anneshabiswaas22-collab/video-gen/issues/3)
  are licensing/GPU prerequisites. [#2](https://github.com/anneshabiswaas22-collab/video-gen/issues/2)
  is the active M0.2 implementation. No open PR was found at initial audit.
- Latest pre-change docs integrity run was
  [successful](https://github.com/anneshabiswaas22-collab/video-gen/actions/runs/43719613690),
  but did NOT cover API/web functionality.

## Primary repository 1 — ComfyUI

- Official: https://github.com/Comfy-Org/ComfyUI
- Inspected `master` head: `258f880d0c026bfc22acab679858ab2e2c70573d`;
  observed latest commit timestamp 2026-11-15 16:47 UTC.
- [LICENSE](https://github.com/Comfy-Org/ComfyUI/blob/258f880d0c026bfc22acab679858ab2e2c70573d/LICENSE)
  states **GPL-3.0**. Code license VERIFIED; SaaS/distribution/modified-source
  consequences PENDING counsel. Each checkpoint/model has separate terms.

| Verified path | Relevance |
|---|---|
| [server.py](https://github.com/Comfy-Org/ComfyUI/blob/258f880d0c026bfc22acab679858ab2e2c70573d/server.py) | HTTP routes, origin middleware, WebSocket, model discovery, queue and history |
| [execution.py](https://github.com/Comfy-Org/ComfyUI/blob/258f880d0c026bfc22acab679858ab2e2c70573d/execution.py) | Prompt execution, node validation and caching boundary |
| [comfy/model_management.py](https://github.com/Comfy-Org/ComfyUI/blob/258f880d0c026bfc22acab679858ab2e2c70573d/comfy/model_management.py) | Device/VRAM states, model resource management |
| [docs HTTP/WS routes](https://github.com/Comfy-Org/docs/blob/main/development/comfyui-server/comms_routes.mdx) | Endpoint descriptions; implementation version must be pinned |
| [.github/workflows](https://github.com/Comfy-Org/ComfyUI/tree/258f880d0c026bfc22acab679858ab2e2c70573d/.github/workflows) | Test/build/version/format automation |

**Concrete integration contract (future M1):**
1. Keep ComfyUI as a private external GPU engine, not a vendored app or public endpoint.
2. VideoGen owns user identity, project authorization, idempotency, quota, job metadata,
   output storage, provenance and error handling.
3. Operator pins engine revision, custom-node allowlist and an audited ComfyUI API-format
   workflow graph. No arbitrary graph, external URL or node injection from users.
4. Adapter discovers compatible nodes via `GET /object_info`, checks health via
   `GET /queue`, submits `POST /prompt` with `{"prompt": <validated graph>,
   "client_id": <id>}`, receives `prompt_id`. Monitor `/ws` and retrieve
   `GET /history/{prompt_id}` plus controlled `/view` output. Recent
   `/api/jobs` endpoints exist but must be evaluated against the pinned release.
5. Parse workflow rejection including `node_errors`, transport outages,
   timeouts and disconnected worker into typed internal errors. Persist mapping from
   VideoGen job ID to ComfyUI prompt ID and version; never leak private engine URLs.
6. Treat `POST /interrupt` and broad queue modification as potentially
   **global**; implement per-job safe cancellation only after testing isolation.
   Export media by downloading, MIME/codec-checking, SHA-256 hashing and copying to our
   durable storage; never trust a raw filesystem path from upstream.

**Strengths:** rich node ecosystem, image/video/audio graph workflows, mature GPU
memory handling, established queue/API, strong modular inference boundary.

**Weaknesses/risks:** GPL compliance review, large changing dependency/torch surface,
custom nodes can execute code, API/schema changes, GPUs/OOM, model-specific
input validation, global cancellation semantics, unsafe exposure.

**Engineering effort:** M0 typed stub + HTTP MockTransport tests (small);
M1 actual pinned engine + workflow conversion + output validator (medium/large);
multi-tenant isolation and production GPU scheduling (large).

**Do NOT implement yet:** copying engine code into monorepo; custom node marketplace,
unreviewed ComfyUI graph execution, remote GPU tunneling, production cancellation,
or guessed model compatibility.

## Primary repository 2 — FreeField

- Official: https://github.com/neuregex/freefield
- Inspected `main` head: `f0c2358a46c7008ff8503d4324b6cc8bc7657e75`;
  observed latest commit timestamp 2026-11-15 10:23 UTC.
- [LICENSE](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/LICENSE)
  is **MIT**, copyright Sammir Femat (2026). Application code license VERIFIED;
  packaged media/model weights/workflows/custom nodes individually **PENDING**.
- The upstream README reports 120 apps, a validation suite and GPU labs; **these
  are upstream-reported counts/performance, not reproduced VideoGen measurements**.

| Verified path | Relevance to our own design |
|---|---|
| [schema/app.schema.json](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/schema/app.schema.json) | JSON-schema manifests: typed inputs, node bindings, outputs, model metadata, examples, measured VRAM |
| [apps/create-image/app.json](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/apps/create-image/app.json) | Reference inputs, preset and workflow mapping |
| [apps/cinema-studio/app.json](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/apps/cinema-studio/app.json) | Camera/palette controls translated to model-understood prompts |
| [apps/cinema-video/workflow.api.json](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/apps/cinema-video/workflow.api.json) | ComfyUI API-format graph example |
| [server/registry.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/server/registry.ts) | AJV 2020 schema validation; checks every referenced node/field |
| [server/runner.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/server/runner.ts) | Coercion, input bounds, form->node binding, submits with Comfy SDK |
| [server/history.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/server/history.ts) | Durable history/media metadata, status and progress |
| [server/guard.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/server/guard.ts) | Hosted gate/limits with explicit localhost caveat |
| [infra/gateway.py](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/infra/gateway.py) | Token protected private ComfyUI proxy, model-unload preparation |
| [tools/catalog.py](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/tools/catalog.py) | Derived model packs, download/VRAM maps |
| [tools/comfy_validate.py](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/tools/comfy_validate.py) | CPU graph validation with placeholders; no real inference claim |
| [lab/core.py](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/lab/core.py) | Case provenance, metrics/VRAM sampler |
| [.github/workflows/validate.yml](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/.github/workflows/validate.yml) | Manifest, unit/type checks, placeholder ComfyUI graph validation |
| [test/runner.test.ts](https://github.com/neuregex/freefield/blob/f0c2358a46c7008ff8503d4324b6cc8bc7657e75/test/runner.test.ts) | Tests of enum choices, numerical limits, ordered camera moves, binding |

**Recommended reuse boundary:** study the pattern `manifest -> validated form ->
allowlisted workflow binding -> private engine -> persistent output/provenance`.
Implement an **original VideoGen manifest registry** as features enter M1;
only add UI controls supported by verified model schema. Continue with our own
Next.js/FastAPI contracts, not an MIT FreeField full fork. Treat upstream
`packs` metadata and GPU labels as hints pending independent tests.

**Strengths:** clear source organization, strong manifest schema and binding
validation, sample app tests, prior code-level GPU experiment organization.
The `apps/`, `schema/`, `server/`, `web/`, `tools/`, `test/`, `packs/`,
`lab/`, `infra/` and CI directories were present in the inspected tree.

**Weaknesses/risks:** changing model catalog and file formats, transient custom
nodes/workflows, Modal/cloud dependencies for some scenarios, no automatic
commercial permission for weights or benchmark media, upstream marketing
claims should not be adopted as our results.

**Engineering effort:** own small manifest schema + validator (medium);
approved workflow compilation and golden tests (medium);
GPU reproducibility/quality lab, multi-shot continuity (large).

**Do NOT implement yet:** copying branding, gallery images, large example
assets, unapproved third-party graph pack, 120-app parity, Modal dependency
or other external hosting.

## Why these two complement each other

ComfyUI is the **inference execution plane**; FreeField is a **manifest/workflow
product-design reference**. Neither replaces our ownership of the domain model,
project history, permissions, user experience or shot continuity. Their interface
is the only planned seam. We select **exactly these two** as primary foundations
for M0/M1 study.

## Triage of all 54 historical repositories

[Complete 54-item catalog](ALL_RECOMMENDED_REPOSITORIES.txt) was reviewed,
including its 2026-11-15 existence-check note (53/54 URLs resolved;
Montagio reported unavailable). That is URL existence, **not** license/quality
or upstream-maturity verification. These are not additional foundations.

| Catalog IDs | Scope / triage decision | Status |
|---|---|---|
| 01–02 | ComfyUI engine and FreeField manifest reference; deep study above | VERIFIED (code/license only) |
| 03–18 | Competing studios, creative patterns and editing references; no clones | PENDING |
| 09 | Montagio historical URL reported 404 by existing catalog; reject until corrected | BLOCKED |
| 19–27 | Video models/runners: Wan first candidate, others later based on GPU and weights | PENDING |
| 28–29 | Image model candidates; select one licensed compatible checkpoint in M1 | PENDING |
| 30–34 | TTS, music, lip-sync and captions; M3 license/compute gate | PENDING |
| 35–40 | Optimization/training; compare against measured baseline in M6 | PENDING |
| 41–46 | FFmpeg, restoration, editing/3D tools; integrate by feature later | PENDING |
| 47–54 | UI, queue, auth, agents, collaboration; avoid infrastructure overbuild | PENDING |

**Key decision:** issue #2 uses lightweight SQLite and an in-process
background mock loop, not Celery+Redis or live ComfyUI, as no genuine compute
has yet been proven. Upgrade to dedicated broker and object store only when
recovery/load requirements are measured. Never infer GPL safety solely from
process separation.

## Risks and next research gates

1. **Legal** — ComfyUI code GPL-3.0; FreeField source MIT; graph/media assets,
   custom nodes and all weight files require separate review. Product's own
   original-code license is OPEN.
2. **GPU** — Google Colab device/VRAM/storage unknown; Wan checkpoint UNKNOWN;
   no real benchmark or output claims permitted.
3. **Security** — custom node execution and local mock unauthenticated routes
   prohibit public deployment until isolation/auth/quota are implemented.
4. **Operations** — model downloads, cold starts, OOM, partial output, cancellation,
   remote retries, stdout secrets and artifacts require explicit design/test gates.
5. **Reproducibility** — pin selected engine commit, model hash, workflow JSON,
   native packages and output provenance before genuine generation.
