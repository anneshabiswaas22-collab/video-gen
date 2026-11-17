#!/usr/bin/env python3
"""Run the CPU application/reference validation in one command, preserving all outcomes."""

import argparse
import json
import os
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = ROOT / ".venv/bin/python"
NPM = shutil.which("npm") or "npm"
STARTED = time.monotonic()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / ".local/verification")
    parser.add_argument("--api-port", type=int, default=8021)
    parser.add_argument("--web-port", type=int, default=3021)
    parser.add_argument(
        "--without-browser", action="store_true", help="Explicit reduced scope, recorded as NOT RUN"
    )
    parser.add_argument(
        "--without-reference",
        action="store_true",
        help="Explicit reduced scope, recorded as NOT RUN",
    )
    args = parser.parse_args()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    output = args.output.resolve() / run_id
    output.mkdir(parents=True, exist_ok=False)
    summary = {
        "run_id": run_id,
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "working_tree_dirty": bool(
            subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT)
        ),
        "scope": "CPU application, browser, packaging/dependency, documentation/preservation and optional retained reference checks",
        "checks": [],
        "unrun_gates": [
            "Real Ollama/model quality: no configured running model verified; no model download/startup.",
            "GPU inference, ComfyUI/custom-node runtime: required hardware/dependencies/approved weights unavailable.",
            "Actual speech audio, microphone, camera, lip sync and learning efficacy: not verified.",
            "Hosted CI, public production deployment, Windows/Python3.11 execution and continuous PR monitoring: not established.",
        ],
    }
    base_env = {
        **os.environ,
        "WORKER_BACKEND": "mock",
        "VIDEOGEN_COACH_PROVIDER": "offline_practice",
        "PYTHONUNBUFFERED": "1",
        "NEXT_TELEMETRY_DISABLED": "1",
    }

    def persist():
        summary["elapsed_seconds"] = round(time.monotonic() - STARTED, 3)
        (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")

    def run(name, argv, *, cwd=ROOT, env=None, timeout=300):
        print("VERIFY", name, flush=True)
        started = time.monotonic()
        log = output / (name + ".log")
        entry = {"name": name, "command": list(map(str, argv)), "cwd": str(cwd), "log": log.name}
        with log.open("w") as stream:
            try:
                process = subprocess.Popen(
                    list(map(str, argv)),
                    cwd=cwd,
                    env=env or base_env,
                    stdout=stream,
                    stderr=subprocess.STDOUT,
                    start_new_session=True,
                )
                try:
                    code = process.wait(timeout=timeout)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGTERM)
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        os.killpg(process.pid, signal.SIGKILL)
                        process.wait()
                    code = 124
                entry.update(status="PASSED" if code == 0 else "FAILED", exit_code=code)
            except OSError as error:
                stream.write(type(error).__name__ + ": " + str(error))
                entry.update(status="BLOCKED", exit_code=None)
        entry["seconds"] = round(time.monotonic() - started, 3)
        summary["checks"].append(entry)
        persist()
        print(entry["status"], name, entry["seconds"], "seconds", flush=True)
        return entry

    def not_run(name, reason):
        summary["checks"].append({"name": name, "status": "NOT RUN", "reason": reason})
        persist()

    with tempfile.TemporaryDirectory(prefix="videogen-verify-data-") as data:
        base_env["VIDEOGEN_DATA_DIR"] = data
        run("python-dependencies", [PYTHON, "-m", "pip", "check"])
        run("python-tests", [PYTHON, "-m", "pytest", "--junitxml=" + str(output / "pytest.xml")])
        if (output / "pytest.xml").exists():
            suite = ET.parse(output / "pytest.xml").getroot()
            summary["python_junit"] = {
                key: sum(int(s.get(key, 0)) for s in suite.iter("testsuite"))
                for key in ["tests", "failures", "errors", "skipped"]
            }
        run(
            "python-lint",
            [
                ROOT / ".venv/bin/ruff",
                "check",
                "services",
                "integrations",
                "tests",
                "features/english-speaking-friend/backend",
                "features/english-speaking-friend/tests",
                "scripts/development",
                "scripts/quality",
                "scripts/maintenance",
            ],
        )
        run("mock-smoke", [PYTHON, "-m", "scripts.development.smoke_mock"])
        run("docs", [PYTHON, "scripts/maintenance/check_docs.py"])
        run("preservation", [PYTHON, "scripts/maintenance/check_structure.py"])
        run("web-dependencies", [NPM, "ls", "--all"])
        run("web-types", [NPM, "run", "typecheck"])
        run("web-lint", [NPM, "run", "lint"])
        run(
            "web-tests",
            [
                NPM,
                "run",
                "test",
                "--workspace",
                "@videogen/web",
                "--",
                "--reporter=json",
                "--outputFile=" + str(output / "vitest.json"),
            ],
        )
        if (output / "vitest.json").exists():
            results = json.loads((output / "vitest.json").read_text())
            summary["web_tests"] = {
                key: results.get(key)
                for key in ["numTotalTests", "numPassedTests", "numFailedTests", "numPendingTests"]
            }
        run(
            "python-audit",
            [PYTHON, "-m", "pip_audit", "--local", "--cache-dir", str(ROOT / ".local/audit-cache")],
        )
        run("web-audit-production", [NPM, "audit", "--omit=dev", "--audit-level=high"])
        run("web-audit-all", [NPM, "audit", "--audit-level=moderate"])
        run(
            "wheel",
            [PYTHON, "-m", "pip", "wheel", "--no-deps", "--wheel-dir", str(output / "wheels"), "."],
        )
        wheel_code = """import sys,zipfile; from pathlib import Path
w=next(Path(sys.argv[1]).glob('*.whl'))
with zipfile.ZipFile(w) as z:
 n=z.namelist(); assert 'english_friend/lessons.json' in n; assert 'services/api/main.py' in n
 assert not any('AnalyseFuture' in x or '.sqlite' in x for x in n)
print('Packaged lesson, feature and service modules; no archive/database payloads')
"""
        run("wheel-contents", [PYTHON, "-c", wheel_code, str(output / "wheels")])
        if args.without_reference:
            not_run("reference", "Explicit --without-reference reduced scope")
        else:
            reference = ROOT / "AnalyseFuture/references/workflow-studio/freefield"
            for label, command in [
                ("validate", [NPM, "run", "validate"]),
                ("types", [NPM, "run", "typecheck"]),
                ("tests", [NPM, "test"]),
                ("importer", [reference / ".venv/bin/python", "test/import_workflow_test.py"]),
                ("gateway", [reference / ".venv/bin/python", "test/gateway_test.py"]),
            ]:
                run("reference-" + label, command, cwd=reference)
        build_env = {**base_env, "NEXT_PUBLIC_API_URL": f"http://127.0.0.1:{args.api_port}"}
        built = run("production-build", [NPM, "run", "build"], env=build_env)
        if args.without_browser:
            not_run("browser", "Explicit --without-browser reduced scope")
        elif built["status"] != "PASSED":
            summary["checks"].append(
                {"name": "browser", "status": "BLOCKED", "reason": "Production build failed"}
            )
        else:
            processes = []
            handles = []
            try:
                for port in [args.api_port, args.web_port]:
                    with socket.socket() as sock:
                        sock.bind(("127.0.0.1", port))
                server_env = {
                    **build_env,
                    "VIDEOGEN_WEB_ORIGIN": f"http://127.0.0.1:{args.web_port}",
                }
                for name, command, cwd in [
                    (
                        "api",
                        [
                            PYTHON,
                            "-m",
                            "uvicorn",
                            "services.api.main:app",
                            "--host",
                            "127.0.0.1",
                            "--port",
                            str(args.api_port),
                        ],
                        ROOT,
                    ),
                    (
                        "web",
                        [
                            ROOT / "node_modules/.bin/next",
                            "start",
                            "--hostname",
                            "127.0.0.1",
                            "--port",
                            str(args.web_port),
                        ],
                        ROOT / "apps/web",
                    ),
                ]:
                    handle = (output / (name + "-server.log")).open("w")
                    handles.append(handle)
                    processes.append(
                        subprocess.Popen(
                            list(map(str, command)),
                            cwd=cwd,
                            env=server_env,
                            stdout=handle,
                            stderr=subprocess.STDOUT,
                            start_new_session=True,
                        )
                    )
                for url in [
                    f"http://127.0.0.1:{args.api_port}/v1/health",
                    f"http://127.0.0.1:{args.web_port}/practice",
                ]:
                    for _ in range(150):
                        try:
                            with urllib.request.urlopen(url, timeout=2) as reply:
                                if reply.status == 200:
                                    break
                        except OSError:
                            if any(p.poll() is not None for p in processes):
                                raise RuntimeError("A test service exited; inspect server logs")
                            time.sleep(0.2)
                    else:
                        raise RuntimeError("A test service was not ready: " + url)
                browser_python = next(
                    (
                        exe
                        for exe in [sys.executable, shutil.which("python"), shutil.which("python3")]
                        if exe
                        and subprocess.run(
                            [exe, "-c", "import playwright"], capture_output=True
                        ).returncode
                        == 0
                    ),
                    None,
                )
                if not browser_python:
                    raise RuntimeError(
                        "Install the optional browser dependency or provide Python with Playwright"
                    )
                browser_env = {
                    **server_env,
                    "VIDEOGEN_TEST_API_URL": f"http://127.0.0.1:{args.api_port}",
                    "VIDEOGEN_TEST_WEB_URL": f"http://127.0.0.1:{args.web_port}",
                    "VIDEOGEN_BROWSER_OUTPUT": str(output / "screenshots"),
                }
                if shutil.which("chromium"):
                    browser_env["VIDEOGEN_BROWSER_EXECUTABLE"] = shutil.which("chromium")
                run("live-node", ["node", "apps/web/test/live-api.mjs"], env=browser_env)
                run("browser-smoke", [browser_python, "tests/browser/smoke.py"], env=browser_env)
                run(
                    "browser-regression",
                    [browser_python, "tests/browser/regression.py"],
                    env=browser_env,
                )
            except (OSError, RuntimeError) as error:
                summary["checks"].append(
                    {"name": "browser-startup", "status": "BLOCKED", "reason": str(error)}
                )
            finally:
                for process in processes:
                    if process.poll() is None:
                        os.killpg(process.pid, signal.SIGTERM)
                for process in processes:
                    try:
                        process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        os.killpg(process.pid, signal.SIGKILL)
                        process.wait()
                for handle in handles:
                    handle.close()
        persist()
    failures = [r["name"] for r in summary["checks"] if r["status"] in {"FAILED", "BLOCKED"}]
    summary["overall"] = (
        "FAILED"
        if failures
        else (
            "PASSED_REDUCED_SCOPE" if args.without_browser or args.without_reference else "PASSED"
        )
    )
    summary["failed_or_blocked"] = failures
    summary["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
    persist()
    print("SUMMARY", output / "summary.json", summary["overall"], flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
