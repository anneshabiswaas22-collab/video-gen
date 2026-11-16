# Cost and credit-saving plan

The priority is to minimize early development expenditure without pretending that GPU generation is free at scale.

## Costs to track separately
- **Codex coding credits:** feature investigation, code writing, tests, rework. Reduce by reusing existing implementations and splitting work into bounded issues.
- **Model code and weights:** many are free to download, but checkpoint-specific licenses/availability vary.
- **GPU time:** Colab owner's existing quota initially; later dedicated rented/owned GPUs. Free tiers are limited and non-SLA.
- **Storage and bandwidth:** videos, checkpoint cache, upload traffic, backup and CDN.
- **Third-party APIs:** optional licensed external models, TTS, auth, observability and payment processing. Explicitly opt in.
- **Operations:** failed runs, retries, model cold starts, monitoring and support.

## Pre-approval limits
No paid API calls, rented GPU hours, large checkpoint downloads or fine-tuning without owner approval of projected budget and acceptance tests. Build mock mode for routine local/CI runs.

## Cost estimator (not a price quote)
Effective cost per accepted clip = (GPU minutes x billed GPU price + paid API fees + storage/egress + retry overhead) / accepted clips.

For movies count not only successful shots but unused generations, scene changes, subtitles, voice synthesis and re-exports. Use the same hardware and resolution for comparative benchmarks.

## Order of optimization
1. Measure failure and retry rate first; prevent unnecessary rerenders.
2. Select minimal suitable model and checkpoint for task.
3. Keep output storage and provenance to reuse prior shots.
4. Measure offload/quantization/caching versus quality degradation.
5. Only then test advanced workers and multiple GPUs.

## Before an expense
Record expected artifact, model version, input constraints, resource estimate, upper spend limit, rollback and decision owner. Report actual spend and quality after experiment.
