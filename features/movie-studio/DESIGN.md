# Long-form AI movie studio design

## Goal
Make it possible to create stories from coherent scenes rather than disconnected clips. Prototype a 60-second movie; later support 20-minute episodes and eventually 1–2-hour film projects through many generated shots (not a single enormous video model invocation).

## Data model
**Project** -> Script versions -> Scenes -> Shots -> Takes/Generations -> Approved take -> Timeline -> Export.
Each shot references character IDs, environment IDs, wardrobe, time of day, camera/framing, motion intent, dialogue/audio cues, target duration, reference frames, and approved output. Store every reshoot independently; never overwrite approved takes.

## Continuity
Character bible: stable name/ID; approved front/side/full-body images; style notes; clothing variants; voice persona; optional LoRA. Environment bible: layout/images, consistent lighting/objects. Scene ledger: who is present, positions, outfits, props, time, last-shot transition. QA flags: face/appearance drift, object teleportation, incorrect clothing, missing props, voice mismatch and motion jump.

Character consistency is an *engineering and evaluation problem*, not guaranteed by reusing one prompt/seed. Explore reference-conditioned generation, identity control, LoRA and post-generation review only when lawful and supported by the active model.

## Flow from script to finished movie
1. User supplies concept/script; AI director proposes scenes, characters, locations and shot list.
2. Human reviews shot plan, cost/duration estimate and reference asset rights.
3. Create/reuse character sheet and environment references; lock approved character version.
4. Choose frame/keyframe and compatible video engine per shot.
5. Generate short shots with stable references and camera/motion instructions.
6. Review continuity, reject bad takes and regenerate **only** affected shots.
7. Generate dialogue/narration, aligned timestamps, SFX/music and subtitles.
8. Edit on multitrack timeline; trim, crossfade, normalize audio and inspect cuts.
9. Export via FFmpeg; validate full media file and preserve project metadata.
10. Publish final output, generation manifests and an editable project; allow future reshoots.

## Example use case (separate creative content project)
The owner's earlier family-friendly 3D American-English-learning series (six recurring characters, A1–B2 learning, 15-second shots, periodic recap inserts) is a useful future stress test for repeatability and continuity. It remains a **separate content project**; no character art, scripts or videos are copied here without explicit scope/rights.

## Long duration math and cost
A 20-minute episode assembled from 15-second video shots contains about 80 such slots if no recaps/credits; 2 hours would be ~480 slots. Real production needs extra takes, transition shots, recaps, audio and editing; don't promise one-click generation or a fixed low budget.

## Milestone proof
M5 exit: one 60-second film with at least two recurring character appearances, references and scene ledger, dialogue/subtitles, audible mix, editable shot-level project, one successful reshoot, and documented time/cost/VRAM. Don't claim movie capability from 60s demo alone.
