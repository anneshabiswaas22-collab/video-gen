# Google Colab experiments

Start with a GPU preflight. In a GPU-enabled Colab notebook:

    !git clone https://github.com/anneshabiswaas22-collab/video-gen.git
    %cd video-gen
    !python scripts/gpu_preflight.py

Do not start a multi-gigabyte model download before recording GPU, VRAM, CPU RAM, storage, account quotas and the approved checkpoint. No permanent Colab web server: use a compliant interactive notebook and later move to dedicated compute. A full inference notebook and pinned checkpoint are M1/M2 deliverables, not yet verified.

See [GPU plan](../../docs/GPU_COLAB.md) and [roadmap](../../docs/ROADMAP.md).
