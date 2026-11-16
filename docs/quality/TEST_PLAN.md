# Testing and release evidence

## Levels
**Static/docs CI:** check required files and relative docs links (scripts/maintenance/check_docs.py); validate Python syntax for preflight utilities. This does not test generation.

**CPU unit tests:** validate API schemas, permissions, input media types, idempotency, model compatibility routing, job state transitions, cancellation and mock worker. No CUDA requirement or downloaded checkpoint.

**Integration tests:** run API, database, queue and a stub worker in ephemeral services; verify durable asset read/write and authorized download. Generate a synthetic video via FFmpeg for encode/export testing.

**Real GPU tests (gated):** run a pinned model on recorded GPU/VRAM; generate a genuine image, video or audio file. Verify file signature, decoding, frames, dimensions, audio, timing, hashes, job metadata and GPU peak consumption.

**E2E UI tests:** authenticated nontechnical user can create a project, pick a real supported model, submit a job, preview and download result, then reshoot a film scene without overwriting approved takes.

**Security tests:** prompt/media input cannot invoke shell, arbitrary local files or network endpoints; unauthorized user cannot access another tenant's assets; test job quota bypass, replay, path traversal, SSRF and unsafe ComfyUI workflows.

**Quality benchmarks:** reproducible fixed task suite; multiple seeds; human/blinded evaluation for perceptual quality and continuity; failed jobs included in cost and success metrics.

## Evidence format
- Commit; source/workflow/weights SHA; GPU and CUDA/PyTorch.
- Exact command and requirements; input hashes; prompts/settings/seed.
- Result status (PASS / FAIL / NOT RUN / BLOCKED); generated artifact hashes and screenshots where lawful.
- Peak VRAM, runtime, reported error details and cost.
- Explicit separation of mock output from AI-generated output.

## CI gating strategy
For M0 only docs/static + CPU tests. Do not force large model downloads or paid inference in public CI. Later require developer-run GPU proof attached to PR for inference changes.

As of 2026-11-13 no real VideoGen GPU test evidence is available.
