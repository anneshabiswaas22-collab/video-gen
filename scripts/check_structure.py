#!/usr/bin/env python3
"""Check feature entry points and byte preservation of the reorganized import."""
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "AnalyseFuture/RELOCATION_MANIFEST.json"
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
        new = local_path(row["preserved_path"])
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
        "features/README.md", "PROJECT_IDEA.txt",
        "features/english-speaking-friend/PROJECT_IDEA.txt",
        "docs/REPOSITORY_REORGANIZATION.md", "AnalyseFuture/README.md",
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
    errors.extend(f"Missing feature/layout entry point: {p}" for p in required if not (ROOT / p).is_file())
    if errors:
        print("Structure check FAILED:\n" + "\n".join(f"- {e}" for e in errors))
        return 1
    print(f"Structure check PASSED: {len(FEATURES)} feature guides; {len(records)} original blobs preserved byte-for-byte.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(check())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Structure check FAILED: {exc}")
        sys.exit(1)
