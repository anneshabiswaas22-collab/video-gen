#!/usr/bin/env bash
# Run from any directory after the documented one-time installation.
set -euo pipefail
cd "$(dirname "$0")/../.."
api_port="${VIDEOGEN_API_PORT:-8001}"
web_port="${VIDEOGEN_WEB_PORT:-3000}"
python_bin="${VIDEOGEN_PYTHON:-$(pwd)/.venv/bin/python}"
if [ ! -x "$python_bin" ]; then
  echo 'Install the project first; see docs/operations/BUILD_RUN.md.' >&2
  exit 1
fi
export WORKER_BACKEND=mock
export VIDEOGEN_DATA_DIR="${VIDEOGEN_DATA_DIR:-$(pwd)/.local/videogen}"
export NEXT_PUBLIC_API_URL="http://127.0.0.1:$api_port"
export VIDEOGEN_WEB_ORIGIN="http://127.0.0.1:$web_port"
api_pid=''
web_pid=''
cleanup() {
  if [ -n "$web_pid" ]; then kill "$web_pid" 2>/dev/null || true; fi
  if [ -n "$api_pid" ]; then kill "$api_pid" 2>/dev/null || true; fi
}
trap cleanup EXIT INT TERM
"$python_bin" -m uvicorn services.api.main:app --host 127.0.0.1 --port "$api_port" &
api_pid=$!
for attempt in $(seq 1 100); do
  if curl -fsS "$NEXT_PUBLIC_API_URL/v1/health" >/dev/null; then break; fi
  if ! kill -0 "$api_pid" 2>/dev/null; then wait "$api_pid"; exit 1; fi
  sleep 0.2
done
curl -fsS "$NEXT_PUBLIC_API_URL/v1/health" >/dev/null
(cd apps/web && exec npm run dev -- --hostname 127.0.0.1 --port "$web_port") &
web_pid=$!
wait -n "$api_pid" "$web_pid"
