# Licensing, commercial readiness, security and privacy

This is an engineering checklist, not legal advice.

## Separate rights questions
1. **Our original app**: choose and publish the desired code license only after owner decision. A public repo without a license is not automatically open source.
2. **Third-party source**: record copyright holder, LICENSE file, pinned commit/version, notice obligations, distribution/modified-source obligations and compatibility.
3. **Model weights**: check checkpoint-specific license separately from library code. Some "open" weights have restricted commercial usage, geographic or user-count conditions.
4. **Datasets and generated outputs**: input media permissions, consent, training restrictions, recognizable likeness/voice, music and third-party intellectual property.
5. **Services**: API terms, usage fees, privacy policies, quota rules, and whether external data is sent to a provider.

## Copyleft
ComfyUI code uses GPL-3.0; some upstream film/editor code is AGPL-3.0. Building a proprietary app alongside GPL/AGPL components may trigger source-disclosure obligations depending on integration, distribution and network use. Process isolation alone is not a legal guarantee. Seek legal counsel before distributing paid software or launching AGPL-backed services. FFmpeg builds vary (LGPL/GPL); verify the actual build and linked codecs.

## License review register
Every integrated component gets: URL, version, code LICENSE, weight LICENSE/model card, license restrictions, copyright notices, acceptance owner, distribution architecture, and review date. No unresolved "unknown" component ships in commercial release.

## Security boundaries
- Require authentication/authorization for projects, jobs, uploads, artifacts, billing. Strong tenant isolation.
- Never allow prompt text to become shell commands or file paths.
- Untrusted ComfyUI workflows/custom nodes execute arbitrary code: only approved, reviewed workflows and pinned nodes on isolated workers.
- Validate input MIME, size, duration, decode limits; scan media when appropriate. Prevent zip bombs, path traversal, SSRF and unsafe URLs.
- Store uploaded media under generated IDs, not user-controlled file paths.
- Apply quota, limits, cancellation, concurrency per tenant, and GPU bill safeguards.
- Put API keys in managed secrets; never in browser bundles, logs, notebooks committed to repo, or generated assets.
- Sandbox plugins; restrict network egress and mounted filesystem as needed; review dependencies/SBOM, CVEs and supply chain.
- AI director/agent tools: least privilege, approval gates, prompt-injection defenses, audit actions and output validation.
- Media safety: consent for voice/face imitation, identity misuse detection where feasible, restrictions against illicit/abusive outputs; explain how to report abuse.
- Maintain privacy and deletion policies for projects/media, encryption in transit, retention period and back-up access.
- Avoid displaying user input media publicly by default; do not train on user uploads without informed authorization.

## Release gate
Security and dependency scans, operator runbook, incident handling, media access tests, license register and reproducible dependency lockfiles must be complete before public commercial launch.
