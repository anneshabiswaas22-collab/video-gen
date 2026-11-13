#!/usr/bin/env python3
"""Verify required handoff docs and relative markdown links. No dependencies."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "CONTRIBUTING.md",
    "docs/README.md", "docs/PROJECT_CHARTER.md", "docs/ARCHITECTURE.md",
    "docs/FEATURE_REGISTRY.md", "docs/OPEN_SOURCE_STACK.md",
    "docs/ROADMAP.md", "docs/REUSE_FIRST.md", "docs/GPU_COLAB.md",
    "docs/LICENSE_SECURITY.md", "docs/BENCHMARKS.md", "docs/API_CONTRACT.md",
    "docs/MOVIE_STUDIO.md", "docs/DECISIONS.md", "docs/BUILD_RUN.md",
]
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
errors = []

for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f"Missing required file: {name}")

for doc in ROOT.rglob("*.md"):
    if ".git" in doc.parts or "node_modules" in doc.parts:
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
