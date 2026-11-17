# Project-memory maintenance standard — must be followed after every session

**Reason:** Long ChatGPT/Codex conversations can truncate or become inaccessible. Any contributor must leave the VideoGen repository fully understandable to the next developer without chat access.

## Before beginning any task

1. Read [root project memory](PROJECT_MEMORY.md), [canonical spec](PROJECT_CANONICAL_HANDOFF.md), [state/evidence](STATE_EVIDENCE_AND_OPEN_ISSUES.md), [history](CONVERSATION_AND_DECISION_HISTORY.md), [diagrams](ARCHITECTURE_AND_WORKFLOW_DIAGRAMS.md), [research sources](SOURCE_AND_REPOSITORY_LINKS.md), plus root [AGENTS](../../AGENTS.md).
2. **Check live GitHub**: main SHA, PR branches and merge status, CI for latest commits, issues and current code. Current status may supersede this dated snapshot.
3. Define one bounded issue with dependencies, acceptance criteria and test plan. Record source code vs model weight license and cost/GPU resource approval.
4. Before editing code, search existing implementation to avoid duplicate effort; no blind full forks.

## After each meaningful code/doc change (required)

- Update root `docs/memory/PROJECT_MEMORY.md`: succinct latest branch/PR/state and next step.
- Update `docs/memory/STATE_EVIDENCE_AND_OPEN_ISSUES.md` with **actual** date, commit SHA, PR URL, CI URL, tests passed/failed/not run and outstanding blockers.
- Append to `docs/memory/CONVERSATION_AND_DECISION_HISTORY.md` one concise milestone entry with source/evidence; don't rewrite old history as current.
- Update `docs/memory/PROJECT_CANONICAL_HANDOFF.md` if requirements, architecture, entity contracts, milestone gates or costs changed.
- Update `docs/memory/ARCHITECTURE_AND_WORKFLOW_DIAGRAMS.md` whenever modules/data flows change; adjust captions to distinguish plans vs real implementation.
- Update `docs/memory/SOURCE_AND_REPOSITORY_LINKS.md` and `docs/research/DEPENDENCY_REGISTER.csv` when choosing/upgrading dependencies, with exact pins/licenses/cost implications.
- Update `docs/architecture/DECISIONS.md` for any changed core architectural decision and `docs/development/STATUS.md` when an implementation moves state.
- Update setup commands if development tools/versions change. Ensure markdown relative links, tests, CI and no secrets.
- Prefer small focused commits/PRs; do not auto-merge another developer's unreviewed PR. Leave working source and docs in GitHub, not only assistant output.

## Standard dated handoff entry — copy into state ledger

```markdown
### YYYY-MM-DD — [issue #] / short change title
- Repo and branch:
- Base commit SHA / new commit SHA:
- PR and review status (open/draft/merged/conflict):
- Scope implemented (source paths):
- Changed API/model/worker interfaces:
- Tests PASSED (exact command + CI URL):
- Tests FAILED (cause + remediation):
- Tests NOT RUN (especially GPU/Windows/real media):
- Genuine artifacts (source/weights hash, output sha256, dimensions/fps/duration/VRAM/latency) or NONE:
- Dependency code license / model weight license / commercial gate:
- Budget or resource approval: yes/no/not applicable
- Known security limitations:
- Documentation/chart updated:
- Next task, dependencies and acceptance criteria:
```

## Verification vocabulary

- **SPECIFIED**: requirements/interface documented; code not yet shipped.
- **IMPLEMENTED ON BRANCH**: code exists; may be unreviewed/not merged.
- **CPU TESTED**: executable API/worker/unit/integration checks passed, no model output.
- **GPU VERIFIED**: genuine media produced on named GPU, parsed/decoded/hashes recorded, checkpoint and license clear.
- **MERGED**: GitHub merge commit exists on main and CI passed.
- **RELEASED**: deployed, users can use it under an operational/security gate.
- **PENDING**: evidence incomplete, not necessarily broken.
- **BLOCKED**: specific reproducible obstacle.
- **FAILED**: test actually run and failed, preserve logs.

Never classify MOCK as real generation. Never say "passed" for unrun checks. Never conflate upstream claims with our GPU measurements. Preserve temporal status: "at 2026-11-15 observation", not "currently" without verifying.

## Privacy/security/documentation hygiene

This repository may be publicly visible. **Never commit full private ChatGPT exports, private documents, personal identifiers, access tokens, account secrets, URLs with credentials, media without rights, user-uploaded content or checkpoints**. Summarize relevant project decisions and include only public safe URLs. External code/weight licenses must be separately checked. Mermaid source is text and can be edited in GitHub.

If a prior conversation is missing, say so; **do not fabricate exact historical quotes**. Ask the owner for the missing export only when essential; otherwise continue from this repository. Preserve existing authoritative docs rather than overwriting or duplicating with contradictory instructions.

## Continuous improvement for reliable memory

At each session end, produce a short `STATE_EVIDENCE...` changelog entry and update the first paragraph of `docs/memory/PROJECT_MEMORY.md`. Once a month or major release, review broken research links and obsolete model names, report current date/version, archive historical snapshots instead of deleting provenance. Keep the full 54-repo catalog as historical and track newly adopted dependencies separately. Avoid bloating the core README or writing unsupported marketing claims.

## Refresh offline handoff

After changing canonical docs, reconstruct the one-file handoff from the eight
source paths described in [memory index](README.md). The GitHub native Markdown
files remain the authoritative editable source; the .txt is a snapshot. Keep the
snapshot dated and never claim it is a verbatim private chat export.
