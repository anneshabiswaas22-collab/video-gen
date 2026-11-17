#!/usr/bin/env python3
"""Verify required handoff docs and relative markdown links. No dependencies."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    "README.md", "PROJECT_STRUCTURE.md", "PROJECT_HANDOFF.md", "AGENTS.md", "CONTRIBUTING.md",
    "docs/repository/FILE_GUIDE.md", "docs/repository/FOLDER_GUIDE.md",
    "docs/quality/COMPREHENSIVE_VALIDATION.md",
    "docs/README.md", "docs/product/PROJECT_CHARTER.md", "docs/architecture/ARCHITECTURE.md",
    "docs/product/FEATURE_REGISTRY.md", "docs/research/OPEN_SOURCE_STACK.md",
    "docs/product/ROADMAP.md", "docs/research/REUSE_FIRST.md", "docs/operations/GPU_COLAB.md",
    "docs/security/LICENSE_SECURITY.md", "docs/quality/BENCHMARKS.md", "docs/architecture/API_CONTRACT.md",
    "features/movie-studio/DESIGN.md", "docs/architecture/DECISIONS.md", "docs/operations/BUILD_RUN.md",
]
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
errors = []

for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f"Missing required file: {name}")

for doc in ROOT.rglob("*.md"):
    if any(part in {".git", "node_modules", ".venv"} for part in doc.parts):
        continue
    text = doc.read_text(encoding="utf-8")
    for item in LINK.findall(text):
        if item.startswith(("#", "mailto:", "tel:", "data:")):
            continue
        parsed = urlsplit(item)
        if parsed.scheme or parsed.netloc:
            continue  # external link validity is a separate network-dependent audit
        path = unquote(parsed.path)
        if not path:
            continue
        target = (doc.parent / path).resolve()
        if not target.is_relative_to(ROOT.resolve()) or not target.exists():
            errors.append(f"{doc.relative_to(ROOT)}: broken relative link {item}")

if errors:
    print("Documentation check FAILED:")
    print("\n".join("- " + err for err in errors))
    sys.exit(1)

print(f"Documentation check PASSED; required files: {len(REQUIRED)}.")
