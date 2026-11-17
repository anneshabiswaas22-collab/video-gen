# English-speaking friend

A working local typed-practice prototype now lives in this feature folder.
The [full project idea](PROJECT_IDEA.txt) remains the long-term specification.

| Folder | Responsibility |
|---|---|
| `backend/english_friend/coach.py`, `lessons.json` | 18 original examples across everyday/work/travel; Bangla, transliteration, code-switching, valid variants, ambiguity and accepted retries |
| `backend/english_friend/providers.py` | Explicit offline mode or optional already-running local Ollama model; strict structured output and safe errors |
| `backend/english_friend/routes.py`, `storage.py` | Owner-cookie scoped sessions, request idempotency, opt-in retention and deletion |
| `web/` | Accessible practice room, illustrated characters, editable examples, suggestions, retry and saved-session resume |
| `tests/` | Domain, provider-contract, privacy and HTTP/SQLite lifecycle tests |

The shared API registers this router; `apps/web/app/practice/page.tsx` registers
the feature UI. Root Python packaging includes the feature and its lesson data;
root npm workspaces share React/Next without copying code between feature folders.

## Use and limits

Run the commands in [BUILD_RUN.md](../../docs/operations/BUILD_RUN.md), then open
`/practice` through the local web application. Pick an example, edit it, send,
and retry the suggested English. Unknown input is explicitly unassessed rather
than being given an invented correction. These examples are developer-authored
and still need independent Bengali-English educator review.

Built-in practice is not general AI conversation, a grammar assessment or a
universal translator. For an existing local model, explicitly export
`VIDEOGEN_COACH_PROVIDER=ollama` and `OLLAMA_MODEL` before starting. No model is
installed, downloaded or started automatically. Only loopback HTTP model servers
are permitted; timeouts, invalid responses and service failures remain errors,
with no hidden change back to offline practice. Real model quality is NOT RUN.

Optional speech uses the browser/device service only after clicking Play. Voice
availability and processing depend on that service. Microphone recognition and
real-time video are not implemented; the camera/microphone are never requested.
The illustrated characters are original interface artwork, not live people.

## Privacy and development boundary

Default sessions persist metadata and idempotency fingerprints, not phrases or
responses. A bounded in-memory retry cache is cleared on restart/deletion/expiry.
Only explicit Save consent stores transcript JSON; saved sessions can resume
and be deleted. Default metadata expires after 24 hours, saved sessions after
7 days; expired records are purged at initialization and session operations.
The confirmed **Delete all practice data** control also clears default-session
metadata left after closing a page, releasing the owner's 10-session quota while
preserving other owners. Cancelled/interrupted requests do not leave permanently
pending slots or silently re-run an indeterminate request key.
Deletion removes child rows and clears the local write-ahead log; external
backups/filesystem snapshots remain outside this prototype's control.

A random HttpOnly SameSite cookie scopes practice records to a browser. This is
local ownership isolation, not a production identity system. The creative studio
is still a single-user local mock. Do not expose either service publicly.

Next integrations: teacher evaluation, a measured real local-model run, consented
speech recognition, interruption handling and measured voice/avatar latency.
See [progress](../../docs/development/IMPLEMENTATION_PROGRESS.md) and
[test evidence](../../docs/quality/COMPREHENSIVE_VALIDATION.md). The root
[handoff](../../PROJECT_HANDOFF.md) details the remaining task dependencies and PR workflow.
