#!/usr/bin/env bash
# Single-command local launcher, after one-time Python and npm installation.
set -euo pipefail
cd "$(dirname "$0")/.."
export WORKER_BACKEND=mock
export VIDEOGEN_DATA_DIR="${VIDEOGEN_DATA_DIR:-$(pwd)/.local/videogen}"
export NEXT_PUBLIC_API_URL="http://127.0.0.1:8000"
cleanup() {
  kill "$(jobs -pr)" 2>/dev/null || true
}
trap cleanup EXIT INT TERM
python -m uvicorn services.api.main:app --host 127.0.0.1 --port 8000 &
(cd apps/web && npm run dev -- --hostname 127.0.0.1) &
wait
