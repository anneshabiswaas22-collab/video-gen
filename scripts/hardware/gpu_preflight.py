#!/usr/bin/env python3
"""Hardware preflight for local/Colab experimentation; no model downloads."""
import importlib.util
import json
import os
import platform
import shutil
import subprocess

info = {"python": platform.python_version(),
        "platform": platform.platform(),
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
        "gpu": None}

disk = shutil.disk_usage(os.getcwd())
info["disk_free_gib"] = round(disk.free / 2**30, 2)

if importlib.util.find_spec("torch") is not None:
    try:
        import torch
        info["torch"] = str(torch.__version__)
        info["cuda_available"] = bool(torch.cuda.is_available())
        if torch.cuda.is_available():
            dev = torch.cuda.get_device_properties(0)
            info["gpu"] = dev.name
            info["vram_gib"] = round(dev.total_memory / 2**30, 2)
            info["cuda_runtime"] = torch.version.cuda
    except Exception as exc:
        info["torch_probe_error"] = str(exc)
else:
    info["torch"] = "not installed"

try:
    proc = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total",
                           "--format=csv,noheader"], capture_output=True,
                          text=True, timeout=10, check=False)
    info["nvidia_smi"] = proc.stdout.strip() if proc.returncode == 0 else "unavailable"
except (FileNotFoundError, subprocess.TimeoutExpired):
    info["nvidia_smi"] = "unavailable"

print(json.dumps(info, indent=2))
print("This is hardware detection ONLY. No model inference has been performed.")
