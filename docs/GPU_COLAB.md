# GPU/Colab/Kaggle execution plan

## Real constraints
Owner has access to a Google Colab GPU, but GPU model/VRAM, quotas, CPU RAM and storage are NOT recorded. Never assume A100, T4, 24 GB, unlimited free GPU, or uninterrupted sessions. Notebook environments can stop, change hardware, and restrict remote web-service hosting. Do not circumvent usage policies. Kaggle is an optional comparable research environment, not an open-source GPU service under our control.

## Preflight before choosing models
In a Colab Python cell run:

    import torch, shutil, subprocess
    print("CUDA:", torch.cuda.is_available())
    if torch.cuda.is_available():
        p = torch.cuda.get_device_properties(0)
        print("GPU:", p.name, "VRAM GiB:", round(p.total_memory/2**30, 2))
    print("disk GiB free:", round(shutil.disk_usage("/content").free/2**30, 2))
    print(subprocess.run(["nvidia-smi"], capture_output=True, text=True).stdout[:3000])

Also inspect available host RAM, installed CUDA/PyTorch versions, disk persistence and network restrictions.

## Experimental execution path
- Keep Colab workflow notebook as a **developer-controlled, interactive job**.
- Clone our own repo from a pinned commit, run preflight and select a model variant compatible with available resources.
- Pin engine/package versions and weight commit hashes. Download only chosen weights, respecting terms.
- Choose output workspace and durable storage before starting; avoid exposing private Google Drive files.
- Execute one job at a time on limited hardware. Clear caches only when safe; avoid holding multiple heavy models at once.
- Record job ID, input media hashes, prompt, seed, steps, resolution, duration, engine/weights, VRAM peak, runtime, output hash and failure reason.
- Download/backup outputs. Do not rely on /content existing after runtime ends.
- On OOM: reduce frame count/size, use a smaller checkpoint, offload/quantize if supported; report changes rather than silently degrading the output.

## Suggested hardware tiers (illustrative, not guarantees)
- ~16 GB (T4 class): prototype light image/TTS and small/quantized video workflows; baseline 5B Wan may not fit in reference implementation.
- ~24 GB (L4 class): evaluate Wan 2.2 5B offload, depending on RAM, checkpoint and dependencies.
- 40/80 GB (A100 class): broader experiments, certain larger models and LoRA workloads; still finite.
Always use the upstream's *currently validated* VRAM requirements, not cached memory estimates.

## Codex Cloud boundary
Codex produces API code, workflows, scripts and mock tests. It cannot assert a model generated a real MP4 without a compatible GPU test result. Build a local mock worker for API tests; mark actual CUDA tests required and pending.

## Production
Use authorized dedicated GPUs with secure isolated workers, job queue, observability, storage and autoscaling. Free Colab and Kaggle are not production backends. Avoid exposing notebooks as public multi-user inference servers or bypassing restrictions.

## Cost
Track cost per usable output = (GPU runtime x real unit rate + storage + data transfer + provider APIs + retries) / number of accepted outputs. Include rejection/regeneration rates, not just marginal model inference time.

## M0 deliverable
A reproducible notebook with GPU detection, small model download, one real artifact, metrics JSON and clean uninstall/restart instructions. Do not download a multi-terabyte checkpoint.
