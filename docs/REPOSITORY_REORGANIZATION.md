# Repository analysis and preservation report

**Date:** 2026-11-17 (Asia/Kolkata). **Scope:** M0 repository hygiene and feature
planning, including the owner's combined English-speaking AI friend concept.
This is a structural recovery, not a security incident clearance or restoration
of a presumed known-good account state. No hard reset, history rewrite, force
push, or deletion of imported material is part of this change.

## Findings from the complete tracked inventory

The inspected starting commit was
`f34553a3d2c2d68c15f4644520e65816f0d516f3` on the requested repository
`sarfiaroui-oss/video-gen`. Its parent is
`fcad35485521c311cf727b53d5abe1a9f2a7b9f3`.

| Starting group | Tracked files | Disposition |
|---|---:|---|
| Original root configuration, project guides and contribution files | 6 | Retained; current entry points clarified |
| Root GitHub workflow/templates | 4 | Retained; documentation CI gains preservation validation |
| Shared docs and historical memory | 33 | Retained; current status supplements historical evidence |
| Colab notebook and its guide | 2 | Retained; hardware inference remains unverified |
| Project scripts | 2 | Retained; preservation validator added |
| Complete imported ComfyUI | 1,306 | Moved intact into AnalyseFuture |
| Complete imported FreeField | 764 | Moved intact into AnalyseFuture |
| Loose root index and 19 example directories | 61 | Moved together into AnalyseFuture |
| **Total before reorganization** | **2,178** | **All tracked material accounted for** |

The latest commit added the 2,131 imported files; it did not alter or delete the
47 earlier tracked project files. This distinction matters: the earlier work
was obscured by imports, not shown by this comparison to have been destroyed.
The report is based on all tracked paths, file groups, Git history, workflow and
manifest inspection and limited security checks; it is not a line-by-line
security review of two upstream codebases.

Thirty of the 61 loose index/media files match some FreeField example bytes;
31 do not. Both sets are preserved, including apparently duplicate files.

All imported tracked entries had regular-file Git mode `100644`; no gitlinks or
tracked symlinks were found. Git object connectivity passed. A limited scan for
known credential formats found no matches; this cannot establish absence of
secrets or malicious code. The only active root workflow was documentation CI;
upstream workflows nested inside imported folders are not active root workflows.
Neither a bulk import nor its author metadata proves who accessed the account.

## Feature-oriented active structure

```text
video-gen/
  README.md                     Current product entry point
  PROJECT_IDEA.txt               Combined product vision and feasibility
  PROJECT_MEMORY.md             Current note plus preserved historical handoff
  features/
    image-studio/                Image creation and editing feature guide
    video-studio/                Short video and motion feature guide
    audio-studio/                Voice, sound and music feature guide
    movie-studio/                Scene/shot/take assembly feature guide
    character-continuity/        Reusable, consented character identity guide
    english-speaking-friend/     Live avatar English coach guide and detailed idea
  docs/                         Shared architecture, roadmap, status and history
  scripts/                      Shared validation and hardware preflight
  notebooks/colab/              Existing hardware inspection notebook
  .github/                      Shared CI and contribution templates
  AnalyseFuture/
    README.md
    RELOCATION_MANIFEST.json
    upstream/ComfyUI-master/    Complete original wrapper and source tree
    upstream/freefield-main/    Complete reference studio
    imported-examples/          Original index and all 19 media directories
```

Each folder under `features/` represents one product feature. Shared docs,
scripts, CI, and future platform infrastructure remain shared rather than being
duplicated for every feature. Existing architecture documents remain in their
stable locations to preserve links. Feature folders contain truthful guides,
not placeholder application code or claims that a service has been built.

The live language companion and asynchronous media generation belong to the
same product but need separate latency, data-consent and runtime boundaries.
Language coaching can use a simple licensed animated avatar before expensive
photorealistic generation. User camera access is optional and is not required
to teach sentence construction.

## Provenance and previous work

Historical handoff files cite `anneshabiswaas22-collab/video-gen`, including an
unmerged mock-studio PR #8 and past CI results. These are historical source
references, not proof that this repository currently contains that code.
The current origin advertised `main` at the inspected starting commit; no PR #8
ref was advertised. Do not replace the current repository with another owner's
branch, or claim those older tests ran on this checkout. Recovering that code
would be a separately verified integration task.

FreeField source carries MIT notices; ComfyUI carries GPL-3.0 notices. Both are
retained. Media, checkpoints, custom nodes and commercial distribution rights
must be reviewed independently. Moving files does not remove license duties or
make them safe to redistribute. No new model downloads, paid APIs or GPU jobs
were used for the reorganization.

## Preservation, validation and rollback

[The relocation manifest](../AnalyseFuture/RELOCATION_MANIFEST.json) lists every
moved file's original and new path, original Git blob/mode, byte count and
SHA-256. [The validator](../scripts/check_structure.py) verifies that archived
bytes still match the recorded original blob and that all six feature guides
exist. A staged-tree comparison also checks the manifest against the starting
commit before publication. Git records these moves as content-preserving
renames; the preservation manifest is authoritative when rename display limits
make the Git summary incomplete.

Run from the repository root:

```sh
python scripts/check_docs.py
python scripts/check_structure.py
python -m py_compile scripts/check_docs.py scripts/check_structure.py scripts/gpu_preflight.py
```

Reference-only FreeField checks can run from
`AnalyseFuture/upstream/freefield-main`: `npm run validate`, `npm run typecheck`,
and `npm test`. Its tests validate that preserved reference, not an implemented
VideoGen product. Local ignored dependencies were moved without committing
them; recreate the Python venv at the new path before relying on activation
scripts. Runtime processes started at old paths must be restarted.

The final commit should be a normal descendant of the fetched `origin/main`.
An ordinary push to `main` is owner-authorized for this task, without a PR.
Never force a rejected push; fetch and reconcile concurrent work. Roll back
through a normal reviewed inverse move or revert, preserving subsequent work;
do not reset a shared branch. The original commit also remains in Git history.

## Account recovery boundary

This change cannot secure GitHub login or revoke someone else's access. If
unauthorized access is suspected, the owner must review GitHub's security log,
sessions, collaborators, SSH/deploy keys, installed apps and tokens, revoke
unknown access and rotate affected secrets through GitHub's secure settings.
Do not post credentials in this repository or in chat. A tidy tree is not proof
that an account compromise has ended.
