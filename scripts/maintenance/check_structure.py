#!/usr/bin/env python3
"""Check feature entry points and byte preservation of the reorganized import."""
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "AnalyseFuture/repository-inventory/RELOCATION_MANIFEST.json"
FEATURES = (
    "image-studio", "video-studio", "audio-studio", "movie-studio",
    "character-continuity", "english-speaking-friend",
)


def local_path(value):
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"Unsafe manifest path: {value}")
    resolved = (ROOT / path).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError(f"Path escapes repository: {value}")
    return ROOT / path


def check():
    errors = []
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    placement = json.loads((ROOT / "docs/repository/FILE_PLACEMENT.json").read_text(encoding="utf-8"))
    source_files = {
        name for name in subprocess.check_output(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT, text=True,
        ).split("\0") if name and (ROOT / name).is_file()
    }
    placed = [row["current_path"] for row in placement["files"]]
    if len(set(placed)) != len(placed) or placement["file_count"] != len(placed):
        errors.append("Placement ledger contains duplicate paths or an incorrect count")
    for label, missing in (
        ("Source files absent from placement ledger", source_files - set(placed)),
        ("Placement paths absent from source tree", set(placed) - source_files),
    ):
        if missing:
            errors.append(label + ": " + ", ".join(sorted(missing)))
    guide_paths = [
        "docs/repository/FILE_GUIDE.md",
        "docs/repository/files/INFERENCE_REFERENCE.md",
        "docs/repository/files/WORKFLOW_REFERENCE.md",
    ]
    indexed = []
    for name in guide_paths:
        guide = ROOT / name
        if guide.is_file():
            indexed.extend(re.findall(r"^\| \[([^\]]+)\]\(", guide.read_text(), re.MULTILINE))
    if len(indexed) != len(set(indexed)) or set(indexed) != source_files:
        errors.append("Per-file responsibility guides must explain each source file exactly once")
    folder_guide = ROOT / "docs/repository/FOLDER_GUIDE.md"
    folders = {str(parent) for name in source_files for parent in Path(name).parents}
    indexed_folders = set()
    if folder_guide.is_file():
        indexed_folders = {
            value.rstrip("/")
            for value in re.findall(r"^\| \[([^\]]+)\]\(", folder_guide.read_text(), re.MULTILINE)
        }
    if indexed_folders != folders:
        errors.append("Folder guide must explain every source directory")
    current_paths = {
        row["source_path"]: row["current_path"]
        for row in placement["files"] if row["source_path"] is not None
    }
    records = manifest["files"]
    if manifest["schema_version"] != 1 or manifest["file_count"] != len(records):
        errors.append("Manifest schema or count mismatch")
    expected = {
        "inference-engine-reference": 1306,
        "workflow-studio-reference": 764,
        "unclassified-example-media": 61,
    }
    if Counter(row["category"] for row in records) != expected:
        errors.append("Imported file groups differ from the audited baseline")
    for key in ("original_path", "preserved_path"):
        if len({row[key] for row in records}) != len(records):
            errors.append(f"Duplicate {key} in manifest")
    for row in records:
        old = local_path(row["original_path"])
        new = local_path(current_paths.get(row["preserved_path"], row["preserved_path"]))
        if not row["preserved_path"].startswith("AnalyseFuture/"):
            errors.append(f"Import outside AnalyseFuture: {row['preserved_path']}")
        if old.exists():
            errors.append(f"Old loose import path still present: {row['original_path']}")
        if new.is_symlink() or not new.is_file():
            errors.append(f"Missing or non-file preservation path: {row['preserved_path']}")
            continue
        data = new.read_bytes()
        if len(data) != row["bytes"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
            errors.append(f"Preserved bytes changed: {row['preserved_path']}")
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if blob != row["git_blob"] or row["git_mode"] != "100644":
            errors.append(f"Original Git identity mismatch: {row['preserved_path']}")
    required = [
        "PROJECT_STRUCTURE.md", "PROJECT_HANDOFF.md", "docs/repository/FILE_PLACEMENT.json",
        "docs/quality/COMPREHENSIVE_VALIDATION.md", "docs/repository/FOLDER_GUIDE.md",
        *guide_paths,
        "docs/repository/GALLERY_CONSOLIDATION.md",
        "features/README.md", "docs/product/PROJECT_IDEA.txt",
        "features/english-speaking-friend/PROJECT_IDEA.txt",
        "docs/repository/REPOSITORY_REORGANIZATION.md", "AnalyseFuture/README.md",
        *(f"features/{feature}/README.md" for feature in FEATURES),
        *(f"AnalyseFuture/{name}.txt" for name in (
            "REPOSITORY_AUDIT", "COMPLETE_FILE_INVENTORY", "FEATURE_INVENTORY",
            "DUPLICATE_ANALYSIS", "SECURITY_AUDIT", "ORIGINAL_TO_NEW_PATH_MAPPING",
            "CONSOLIDATION_REPORT", "ARCHIVED_FILES_MANIFEST",
            "PROJECT_VISION_AND_FUTURE_ROADMAP", "TECHNICAL_DEBT",
            "TEST_AND_VALIDATION_REPORT", "MIGRATION_SUMMARY",
            "NEXT_DEVELOPER_INSTRUCTIONS", "WORK_PROGRESS",
        )),
    ]
    required = [current_paths.get(p, p) for p in required]
    errors.extend(f"Missing feature/layout entry point: {p}" for p in required if not (ROOT / p).is_file())
    if errors:
        print("Structure check FAILED:\n" + "\n".join(f"- {e}" for e in errors))
        return 1
    print(f"Structure check PASSED: {len(FEATURES)} feature guides; {len(records)} original blobs preserved byte-for-byte; {len(source_files)} files and {len(folders)} directories explained.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(check())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Structure check FAILED: {exc}")
        sys.exit(1)
