# Implementation and remaining integrations

The current continuation plan is [PROJECT_HANDOFF.md](../../PROJECT_HANDOFF.md):
104 local tasks with exact homes, dependencies and acceptance evidence. Other tools
should use branches/PRs for reviewed contributions. Issue creation is deferred.
[Comprehensive validation](../quality/COMPREHENSIVE_VALIDATION.md) supersedes earlier
test counts. This pass hardens cancellation/expiry/database failures, replay,
job transitions, receipt integrity, provider responses, browser recovery and
owner-scoped delete-all. It does not add real model/GPU/voice generation.

The owner authorized implementation and tests after the completed sorting pass.
The first delivered slice restores M0 and implements bounded ENG-01 / T0 practice.

| Integration | Evidence in this checkout | Status / remaining gate |
|---|---|---|
| Owned CPU studio foundation | Recovered original Next.js/API/SQLite/mock worker from exact historical `ae953a3e5e2c82e5c2ee639d0f0b07403e8f3d37` source; idempotent jobs, progress/history, receipt download | CPU WORKING; single-user localhost only, not generated media |
| English phrase coaching | 18 developer-authored cases, three scenarios, conservative matching, valid variants, ambiguity, unknown fallback and accepted retries | CPU WORKING; teacher and learning-outcome review pending |
| Local AI adapter | Ollama JSON request/output, bounded response, loopback/no redirects, safe failures | CONTRACT TESTED; real model availability/quality NOT RUN |
| Practice API and privacy | Cookie owner isolation, explicit save consent, metadata-only default, saved resume/delete, quotas, expiry, retries | CPU TESTED; no production accounts or encrypted backup policy |
| Companion interface | Feature-owned `/practice`, two original illustrated characters, editable examples, feedback, optional speech and saved-session UI | BROWSER TESTED desktop/mobile; speech audio not verified |
| Real image/video generation | Typed allowlisted ComfyUI adapter remains a tested boundary | NOT RUN; choose permitted model after actual GPU/hardware/budget review |
| Speech recognition/live conversation | Interface deliberately does not capture the microphone | NOT IMPLEMENTED; consented ASR evaluation, interruption and latency work required |
| Realistic avatar/lip synchronization | Simple illustrated UI only | NOT IMPLEMENTED; rights, rendering and latency evaluation required |
| Film, continuity, advanced audio | Original specifications preserved in their feature folders | PLANNED; depend on verified media paths |
| Public deployment | Local origin/host guards and practice ownership are not tenant authentication | NOT READY; identity, account isolation, quotas and release review required |

The full source revision is recorded in
[RECOVERED_APPLICATION_SOURCE.json](../repository/RECOVERED_APPLICATION_SOURCE.json).
No old project documents were replaced by the historical branch. Recovered
application modules are extended in place; archived engines remain unchanged.

## What to integrate next, in order

1. **Evaluate the learning content:** an English/Bangla educator reviews the examples,
   acceptable variants and clarification policy; run an opt-in adult usability pilot.
   Current phrases are authored examples, not a validated teaching curriculum.
2. **Validate one existing local model:** the adapter is ready for an already-running
   Ollama model. The owner selects/installs a permitted model on suitable hardware;
   record model/version, meaning preservation, false corrections, latency and cost.
   No model was downloaded or queried during this milestone.
3. **Speech input:** select and pin an ASR adapter only after checking voice/audio data
   policy, accuracy on representative Bangla-English speech and a budget. Keep the
   typed fallback and editable transcript; add cancellation and interruption tests.
4. **First genuine image:** collect real GPU/VRAM/RAM/storage evidence, model rights,
   exact checkpoint/workflow hashes and an owner-approved download. Wire the existing
   ComfyUI boundary to one approved workflow; validate a real PNG and provenance.
5. **Short video and media finishing:** one real MP4, measured frames/codec/runtime,
   licensed speech/captions and FFmpeg export before adding multiple engines.
6. **Continuity/movie workflow:** versioned references and shot/take editing, then a
   measured 60-second sequence. Full-length generation is not a single-prompt promise.
7. **Production hardening:** accounts, tenant isolation for creative data, permission
   and deletion policies, usage limits, observability, backup/recovery and legal gates.

These are dependency gates, not promised dates. A working local UI or adapter test
cannot establish GPU generation, learning effectiveness or production security.

## Run and verify

[BUILD_RUN.md](../operations/BUILD_RUN.md) contains complete commands.
[COMPREHENSIVE_VALIDATION.md](../quality/COMPREHENSIVE_VALIDATION.md) records
actual checks and limitations. The earlier no-tests instruction applied to the
sorting task; it does not block the current owner-authorized test work.
