# Static review: data-only FreeField gallery consolidation

Repository: `sarfiaroui-oss/video-gen`
Baseline: `f34553a3d2c2d68c15f4644520e65816f0d516f3`
Review: source/data inspection only. No upstream code executed and no runtime tests run.

## Decision and evidence

The 19 loose original-root example directories and 99 preserved FreeField gallery
directories are disjoint. Their union exactly matches all 118 keys in the
original root index's `apps` map. Combining these actual same-function fragments
under the archived FreeField `web/examples` convention is a data-only consolidation;
it is not a merge of competing inference implementations or an owned product release.
No generated-video files should be invented, downloaded or replaced.

Proposed final gallery:
`AnalyseFuture/references/workflow-studio/freefield/web/examples/`

Move the original `index.json` into that gallery with its original bytes and
all 19 original-root directories intact. The source index is metadata and not
executable code. Existing source-relative asset links then keep the exact
`examples/<app>/...` paths expected by the preserved server and browser code.
Keep provenance/path mappings for the original 19 directories and the 99 existing
ones, preserve all notices and distinct repeated media, and refuse overwrites.

## Static server compatibility

`server/server.ts` sets `examplesFile = join(root, "web", "examples", "index.json")`.
`loadExamples()` parses that file and returns `.apps ?? {}`. The original index
is an object with an `apps` map and `updated_from` field, so its shape is compatible.
The `GET /api/apps` handler attaches `examples[a.id] ?? null`. No source-code
changes are needed to expose the preserved metadata. This is a static conclusion,
not a runtime validation result.

Importing the index WILL change the archived reference's catalog if manually
started: metadata and missing MP4 links become visible instead of every example
being null. `web/js/media.js` intentionally plays visible and hover video thumbnails.
Therefore do not claim the archived UI lacks autoplay. The relevant safety boundary
is that no active owned product entrypoint, root autostart or production deployment
is introduced. The archived reference is not declared runtime-ready or production-ready.
All reference runtime checks are deferred under the user's no-tests instruction.

## Asset completeness

- **indexed_apps:** `118`
- **existing_gallery_apps:** `99`
- **loose_gallery_apps:** `19`
- **existing_source_files:** `420`
- **loose_source_files:** `60`
- **asset_reference_occurrences:** `643`
- **unique_asset_paths:** `642`
- **present_asset_occurrences:** `481`
- **unique_present_assets:** `480`
- **missing_asset_occurrences:** `162`
- **unique_missing_assets:** `162`
- **missing_extensions:** `{'.mp4': 162}`
- **manifest_sections:** `{'image': 70, 'video': 45, 'audio': 2, 'utility': 1}`
- **feature_collections:** `{'image-studio': 70, 'video-studio': 46, 'audio-studio': 2}`

All 162 unique missing asset paths are `.mp4`; every indexed non-MP4 path has
source bytes somewhere in the combined gallery fragments. The directory count
does not mean all original output media were supplied. Future developers must
retain the explicit missing-video limitation rather than infer success from
JPEG posters or third-party lab metadata.

Paths occur in `card`, `poster`, `full`, `inputs[*].src/full`, and nested
`options.<input>.<option>.card/poster`. The JSON companion records every occurrence,
its JSON pointer, original source path, proposed path and presence status.

## Exact mapping of the 19 loose app folders

| Original folder | Manifest section | Feature collection | Actual function | Files |
|---|---|---|---|---:|
| `style-snap` | image | image-studio | outfit editing | 4 |
| `talking` | video | video-studio | talking-avatar animation from portrait and audio | 3 |
| `transitions` | video | video-studio | first/last-frame transition | 5 |
| `truck-ad` | video | video-studio | animated product advertisement | 3 |
| `try-on` | image | image-studio | virtual garment try-on | 6 |
| `ugc-shot` | image | image-studio | product marketing still | 4 |
| `upscale` | image | image-studio | image restoration | 4 |
| `upscale-video` | video | video-studio | video restoration | 2 |
| `vfx-clean-plate` | video | video-studio | video subject removal | 2 |
| `vfx-day-to-night` | video | video-studio | video relighting | 2 |
| `vfx-water` | video | video-studio | video water effects | 2 |
| `victory-card` | image | image-studio | portrait compositing | 4 |
| `video` | video | video-studio | image-to-video animation | 3 |
| `video-remove-bg` | video | video-studio | video foreground cutout and matte | 2 |
| `video-t2v` | video | video-studio | text-to-video generation | 1 |
| `volcano-ad` | video | video-studio | animated product advertisement | 3 |
| `whats-next` | image | image-studio | scene continuation stills (movie storyboard cross-reference) | 4 |
| `z-image` | image | image-studio | text-to-image generation | 2 |
| `zooms` | image | image-studio | image reframing | 4 |

Talking Avatar belongs to video animation; its audio input does not make it an
audio-output generator or an implemented English tutor. What's Next generates
scene-continuation stills, so its primary section stays image while movie
storyboarding can reference it. No loose folder implements independent learning
or a continuity ledger. The `smooth` example in the existing 99 is marked utility
by its manifest and belongs to video post-processing as a semantic collection.

## All 118 indexed-app provenance rows

| App | Manifest section | Feature collection | Original source | Proposed directory | Source files | Missing refs |
|---|---|---|---|---|---:|---:|
| `ai-influencer` | image | image-studio | `freefield-main/web/examples/ai-influencer` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer` | 11 | 0 |
| `ai-influencer-photo` | image | image-studio | `freefield-main/web/examples/ai-influencer-photo` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer-photo` | 4 | 0 |
| `angles` | image | image-studio | `freefield-main/web/examples/angles` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/angles` | 4 | 0 |
| `asmr-host` | video | video-studio | `freefield-main/web/examples/asmr-host` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-host` | 3 | 2 |
| `asmr-product` | video | video-studio | `freefield-main/web/examples/asmr-product` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-product` | 3 | 2 |
| `asmr-whisper` | video | video-studio | `freefield-main/web/examples/asmr-whisper` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-whisper` | 3 | 2 |
| `behind-the-scenes` | video | video-studio | `freefield-main/web/examples/behind-the-scenes` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/behind-the-scenes` | 3 | 2 |
| `billboard` | image | image-studio | `freefield-main/web/examples/billboard` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/billboard` | 4 | 0 |
| `breakdown` | image | image-studio | `freefield-main/web/examples/breakdown` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/breakdown` | 4 | 0 |
| `brick-toy` | image | image-studio | `freefield-main/web/examples/brick-toy` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/brick-toy` | 4 | 0 |
| `bullet-time-scene` | video | video-studio | `freefield-main/web/examples/bullet-time-scene` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-scene` | 3 | 2 |
| `bullet-time-splash` | video | video-studio | `freefield-main/web/examples/bullet-time-splash` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-splash` | 3 | 2 |
| `bullet-time-white` | video | video-studio | `freefield-main/web/examples/bullet-time-white` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-white` | 3 | 2 |
| `burning-sunset` | image | image-studio | `freefield-main/web/examples/burning-sunset` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/burning-sunset` | 4 | 0 |
| `cafe-60s` | image | image-studio | `freefield-main/web/examples/cafe-60s` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cafe-60s` | 4 | 0 |
| `camera-copy` | video | video-studio | `freefield-main/web/examples/camera-copy` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-copy` | 4 | 3 |
| `camera-moves` | video | video-studio | `freefield-main/web/examples/camera-moves` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-moves` | 3 | 2 |
| `chameleon` | video | video-studio | `freefield-main/web/examples/chameleon` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/chameleon` | 3 | 2 |
| `character` | image | image-studio | `freefield-main/web/examples/character` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character` | 4 | 0 |
| `character-3` | image | image-studio | `freefield-main/web/examples/character-3` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-3` | 8 | 0 |
| `character-swap` | image | image-studio | `freefield-main/web/examples/character-swap` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-swap` | 6 | 0 |
| `cinema-studio` | image | image-studio | `freefield-main/web/examples/cinema-studio` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cinema-studio` | 2 | 0 |
| `cinema-video` | video | video-studio | `freefield-main/web/examples/cinema-video` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cinema-video` | 1 | 2 |
| `cloud-surf` | video | video-studio | `freefield-main/web/examples/cloud-surf` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cloud-surf` | 3 | 2 |
| `color-grade` | image | image-studio | `freefield-main/web/examples/color-grade` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/color-grade` | 4 | 0 |
| `comic-book` | image | image-studio | `freefield-main/web/examples/comic-book` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/comic-book` | 4 | 0 |
| `commercial-faces` | image | image-studio | `freefield-main/web/examples/commercial-faces` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/commercial-faces` | 4 | 0 |
| `create-image` | image | image-studio | `freefield-main/web/examples/create-image` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/create-image` | 2 | 0 |
| `depth-map` | image | image-studio | `freefield-main/web/examples/depth-map` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/depth-map` | 4 | 0 |
| `dub` | video | video-studio | `freefield-main/web/examples/dub` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/dub` | 2 | 3 |
| `edit` | image | image-studio | `freefield-main/web/examples/edit` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit` | 4 | 0 |
| `edit-text` | image | image-studio | `freefield-main/web/examples/edit-text` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit-text` | 4 | 0 |
| `effects` | video | video-studio | `freefield-main/web/examples/effects` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects` | 27 | 26 |
| `expand-image` | image | image-studio | `freefield-main/web/examples/expand-image` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/expand-image` | 4 | 0 |
| `extend-video` | video | video-studio | `freefield-main/web/examples/extend-video` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/extend-video` | 2 | 3 |
| `face-swap` | image | image-studio | `freefield-main/web/examples/face-swap` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/face-swap` | 6 | 0 |
| `fashion-factory` | image | image-studio | `freefield-main/web/examples/fashion-factory` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fashion-factory` | 6 | 0 |
| `figure-3d` | image | image-studio | `freefield-main/web/examples/figure-3d` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/figure-3d` | 4 | 0 |
| `fridge-ad` | image | image-studio | `freefield-main/web/examples/fridge-ad` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fridge-ad` | 4 | 0 |
| `game-styles` | image | image-studio | `freefield-main/web/examples/game-styles` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/game-styles` | 4 | 0 |
| `genjutsu` | video | video-studio | `freefield-main/web/examples/genjutsu` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/genjutsu` | 3 | 2 |
| `giallo` | image | image-studio | `freefield-main/web/examples/giallo` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giallo` | 4 | 0 |
| `giant-product` | image | image-studio | `freefield-main/web/examples/giant-product` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giant-product` | 4 | 0 |
| `glitter-sticker` | image | image-studio | `freefield-main/web/examples/glitter-sticker` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/glitter-sticker` | 4 | 0 |
| `graffiti-ad` | image | image-studio | `freefield-main/web/examples/graffiti-ad` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/graffiti-ad` | 4 | 0 |
| `h3-photo` | video | video-studio | `freefield-main/web/examples/h3-photo` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-photo` | 3 | 2 |
| `h3-video` | video | video-studio | `freefield-main/web/examples/h3-video` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-video` | 1 | 2 |
| `headshot` | image | image-studio | `freefield-main/web/examples/headshot` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/headshot` | 4 | 0 |
| `idol` | video | video-studio | `freefield-main/web/examples/idol` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/idol` | 3 | 2 |
| `image-effects` | image | image-studio | `freefield-main/web/examples/image-effects` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/image-effects` | 4 | 0 |
| `inpaint` | image | image-studio | `freefield-main/web/examples/inpaint` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/inpaint` | 5 | 0 |
| `j-magazine` | image | image-studio | `freefield-main/web/examples/j-magazine` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-magazine` | 4 | 0 |
| `j-poster` | image | image-studio | `freefield-main/web/examples/j-poster` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-poster` | 4 | 0 |
| `japanese-show` | image | image-studio | `freefield-main/web/examples/japanese-show` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/japanese-show` | 4 | 0 |
| `kick-ad` | video | video-studio | `freefield-main/web/examples/kick-ad` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/kick-ad` | 3 | 2 |
| `macro-product` | image | image-studio | `freefield-main/web/examples/macro-product` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-product` | 4 | 0 |
| `macro-scene` | image | image-studio | `freefield-main/web/examples/macro-scene` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-scene` | 4 | 0 |
| `magic-button` | video | video-studio | `freefield-main/web/examples/magic-button` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/magic-button` | 3 | 2 |
| `mascot` | image | image-studio | `freefield-main/web/examples/mascot` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mascot` | 4 | 0 |
| `melting-doodle` | video | video-studio | `freefield-main/web/examples/melting-doodle` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/melting-doodle` | 3 | 2 |
| `meme` | image | image-studio | `freefield-main/web/examples/meme` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/meme` | 2 | 0 |
| `micro-beasts` | image | image-studio | `freefield-main/web/examples/micro-beasts` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/micro-beasts` | 4 | 0 |
| `mixed-media` | video | video-studio | `freefield-main/web/examples/mixed-media` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media` | 18 | 19 |
| `moodboard` | image | image-studio | `freefield-main/web/examples/moodboard` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moodboard` | 8 | 0 |
| `morph` | video | video-studio | `freefield-main/web/examples/morph` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph` | 18 | 17 |
| `moss-image` | image | image-studio | `freefield-main/web/examples/moss-image` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moss-image` | 2 | 0 |
| `motion-transfer` | video | video-studio | `freefield-main/web/examples/motion-transfer` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/motion-transfer` | 4 | 3 |
| `mukbang` | video | video-studio | `freefield-main/web/examples/mukbang` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mukbang` | 3 | 2 |
| `mural` | image | image-studio | `freefield-main/web/examples/mural` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mural` | 4 | 0 |
| `music` | audio | audio-studio | `freefield-main/web/examples/music` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/music` | 2 | 0 |
| `outfit-shot` | image | image-studio | `freefield-main/web/examples/outfit-shot` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-shot` | 6 | 0 |
| `outfit-swap` | image | image-studio | `freefield-main/web/examples/outfit-swap` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-swap` | 6 | 0 |
| `outfit-vending` | image | image-studio | `freefield-main/web/examples/outfit-vending` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-vending` | 4 | 0 |
| `packshot` | image | image-studio | `freefield-main/web/examples/packshot` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/packshot` | 4 | 0 |
| `paint-app` | image | image-studio | `freefield-main/web/examples/paint-app` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/paint-app` | 4 | 0 |
| `photodump` | image | image-studio | `freefield-main/web/examples/photodump` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/photodump` | 4 | 0 |
| `pixel-game` | image | image-studio | `freefield-main/web/examples/pixel-game` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/pixel-game` | 4 | 0 |
| `plushie` | image | image-studio | `freefield-main/web/examples/plushie` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/plushie` | 4 | 0 |
| `poster` | image | image-studio | `freefield-main/web/examples/poster` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/poster` | 4 | 0 |
| `product-shot` | image | image-studio | `freefield-main/web/examples/product-shot` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/product-shot` | 4 | 0 |
| `rap-video` | video | video-studio | `freefield-main/web/examples/rap-video` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/rap-video` | 3 | 2 |
| `recast` | video | video-studio | `freefield-main/web/examples/recast` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/recast` | 4 | 3 |
| `reframe` | video | video-studio | `freefield-main/web/examples/reframe` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reframe` | 2 | 3 |
| `relight` | image | image-studio | `freefield-main/web/examples/relight` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/relight` | 4 | 0 |
| `remove-bg` | image | image-studio | `freefield-main/web/examples/remove-bg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/remove-bg` | 4 | 0 |
| `renaissance` | image | image-studio | `freefield-main/web/examples/renaissance` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/renaissance` | 4 | 0 |
| `render-3d` | image | image-studio | `freefield-main/web/examples/render-3d` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/render-3d` | 4 | 0 |
| `reshoot` | video | video-studio | `freefield-main/web/examples/reshoot` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reshoot` | 2 | 3 |
| `roller-coaster` | video | video-studio | `freefield-main/web/examples/roller-coaster` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/roller-coaster` | 3 | 2 |
| `sdr-hdr` | video | video-studio | `freefield-main/web/examples/sdr-hdr` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sdr-hdr` | 2 | 3 |
| `sfx` | audio | audio-studio | `freefield-main/web/examples/sfx` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sfx` | 2 | 0 |
| `shots` | image | image-studio | `freefield-main/web/examples/shots` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/shots` | 4 | 0 |
| `sketch-to-real` | image | image-studio | `freefield-main/web/examples/sketch-to-real` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sketch-to-real` | 4 | 0 |
| `skin-enhancer` | image | image-studio | `freefield-main/web/examples/skin-enhancer` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/skin-enhancer` | 4 | 0 |
| `smooth` | utility | video-studio | `freefield-main/web/examples/smooth` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/smooth` | 2 | 3 |
| `speak` | video | video-studio | `freefield-main/web/examples/speak` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/speak` | 3 | 2 |
| `storm-creature` | video | video-studio | `freefield-main/web/examples/storm-creature` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/storm-creature` | 3 | 2 |
| `style-reference` | image | image-studio | `freefield-main/web/examples/style-reference` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-reference` | 4 | 0 |
| `style-snap` | image | image-studio | `style-snap` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-snap` | 4 | 0 |
| `styles` | image | image-studio | `freefield-main/web/examples/styles` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/styles` | 2 | 0 |
| `talking` | video | video-studio | `talking` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/talking` | 3 | 2 |
| `transitions` | video | video-studio | `transitions` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/transitions` | 5 | 2 |
| `truck-ad` | video | video-studio | `truck-ad` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/truck-ad` | 3 | 2 |
| `try-on` | image | image-studio | `try-on` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/try-on` | 6 | 0 |
| `ugc-shot` | image | image-studio | `ugc-shot` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ugc-shot` | 4 | 0 |
| `upscale` | image | image-studio | `upscale` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale` | 4 | 0 |
| `upscale-video` | video | video-studio | `upscale-video` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale-video` | 2 | 3 |
| `vfx-clean-plate` | video | video-studio | `vfx-clean-plate` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-clean-plate` | 2 | 3 |
| `vfx-day-to-night` | video | video-studio | `vfx-day-to-night` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-day-to-night` | 2 | 3 |
| `vfx-water` | video | video-studio | `vfx-water` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-water` | 2 | 3 |
| `victory-card` | image | image-studio | `victory-card` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/victory-card` | 4 | 0 |
| `video` | video | video-studio | `video` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video` | 3 | 2 |
| `video-remove-bg` | video | video-studio | `video-remove-bg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-remove-bg` | 2 | 3 |
| `video-t2v` | video | video-studio | `video-t2v` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-t2v` | 1 | 2 |
| `volcano-ad` | video | video-studio | `volcano-ad` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/volcano-ad` | 3 | 2 |
| `whats-next` | image | image-studio | `whats-next` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/whats-next` | 4 | 0 |
| `z-image` | image | image-studio | `z-image` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/z-image` | 2 | 0 |
| `zooms` | image | image-studio | `zooms` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/zooms` | 4 | 0 |

## Every indexed asset occurrence

| JSON pointer | Original asset path | Proposed repository path | Presence |
|---|---|---|---|
| `/apps/ai-influencer/card` | `examples/ai-influencer/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer/full` | `examples/ai-influencer/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/full.jpg` | `present_source_asset` |
| `/apps/ai-influencer/options/kind/an ordinary, believable person/card` | `examples/ai-influencer/options/kind/an-ordinary-believable-person/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/options/kind/an-ordinary-believable-person/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer/options/kind/a person with bold, striking, slightly exaggerated features/card` | `examples/ai-influencer/options/kind/a-person-with-bold-striking-slightly-exaggerated-features/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/options/kind/a-person-with-bold-striking-slightly-exaggerated-features/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer/options/kind/a person with extremely exaggerated, cartoonish features and proportions, still photographed for real/card` | `examples/ai-influencer/options/kind/a-person-with-extremely-exaggerated-cartoonish-features-and-proportions-still-photographed-for-real/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/options/kind/a-person-with-extremely-exaggerated-cartoonish-features-and-proportions-still-photographed-for-real/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer/options/kind/an anthropomorphic cat character: a furry cat head on a human body/card` | `examples/ai-influencer/options/kind/an-anthropomorphic-cat-character-a-furry-cat-head-on-a-human-body/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/options/kind/an-anthropomorphic-cat-character-a-furry-cat-head-on-a-human-body/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer/options/kind/an anthropomorphic dog character: a dog head with floppy ears on a human body/card` | `examples/ai-influencer/options/kind/an-anthropomorphic-dog-character-a-dog-head-with-floppy-ears-on-a-human-body/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/options/kind/an-anthropomorphic-dog-character-a-dog-head-with-floppy-ears-on-a-human-body/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer/options/kind/an anthropomorphic capybara character: a capybara head on a human body/card` | `examples/ai-influencer/options/kind/an-anthropomorphic-capybara-character-a-capybara-head-on-a-human-body/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/options/kind/an-anthropomorphic-capybara-character-a-capybara-head-on-a-human-body/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer/options/kind/a character whose whole head is a grasshopper's head, with large compound eyes and long antennae, on a human body: no human face/card` | `examples/ai-influencer/options/kind/a-character-whose-whole-head-is-a-grasshopper-s-head-with-large-compound-eyes-and-long-antennae-on-a-human-body-no-human-face/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/options/kind/a-character-whose-whole-head-is-a-grasshopper-s-head-with-large-compound-eyes-and-long-antennae-on-a-human-body-no-human-face/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer/options/kind/a character whose whole head is a puffin's head, black and white feathers and a bright orange beak, on a human body: no human face/card` | `examples/ai-influencer/options/kind/a-character-whose-whole-head-is-a-puffin-s-head-black-and-white-feathers-and-a-bright-orange-beak-on-a-human-body-no-human-face/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/options/kind/a-character-whose-whole-head-is-a-puffin-s-head-black-and-white-feathers-and-a-bright-orange-beak-on-a-human-body-no-human-face/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer/options/kind/a character whose whole head is a green frog's head, with a wide mouth and big round eyes, on a human body: no human face/card` | `examples/ai-influencer/options/kind/a-character-whose-whole-head-is-a-green-frog-s-head-with-a-wide-mouth-and-big-round-eyes-on-a-human-body-no-human-face/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer/options/kind/a-character-whose-whole-head-is-a-green-frog-s-head-with-a-wide-mouth-and-big-round-eyes-on-a-human-body-no-human-face/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer-photo/card` | `examples/ai-influencer-photo/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer-photo/card.jpg` | `present_source_asset` |
| `/apps/ai-influencer-photo/full` | `examples/ai-influencer-photo/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer-photo/full.jpg` | `present_source_asset` |
| `/apps/ai-influencer-photo/inputs/0/src` | `examples/ai-influencer-photo/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer-photo/input-image.jpg` | `present_source_asset` |
| `/apps/ai-influencer-photo/inputs/0/full` | `examples/ai-influencer-photo/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ai-influencer-photo/input-image-full.jpg` | `present_source_asset` |
| `/apps/angles/card` | `examples/angles/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/angles/card.jpg` | `present_source_asset` |
| `/apps/angles/full` | `examples/angles/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/angles/full.jpg` | `present_source_asset` |
| `/apps/angles/inputs/0/src` | `examples/angles/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/angles/input-image.jpg` | `present_source_asset` |
| `/apps/angles/inputs/0/full` | `examples/angles/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/angles/input-image-full.jpg` | `present_source_asset` |
| `/apps/asmr-host/card` | `examples/asmr-host/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-host/card.mp4` | `missing_inherited_mp4` |
| `/apps/asmr-host/poster` | `examples/asmr-host/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-host/poster.jpg` | `present_source_asset` |
| `/apps/asmr-host/full` | `examples/asmr-host/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-host/full.mp4` | `missing_inherited_mp4` |
| `/apps/asmr-host/inputs/0/src` | `examples/asmr-host/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-host/input-image.jpg` | `present_source_asset` |
| `/apps/asmr-host/inputs/0/full` | `examples/asmr-host/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-host/input-image-full.jpg` | `present_source_asset` |
| `/apps/asmr-product/card` | `examples/asmr-product/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-product/card.mp4` | `missing_inherited_mp4` |
| `/apps/asmr-product/poster` | `examples/asmr-product/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-product/poster.jpg` | `present_source_asset` |
| `/apps/asmr-product/full` | `examples/asmr-product/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-product/full.mp4` | `missing_inherited_mp4` |
| `/apps/asmr-product/inputs/0/src` | `examples/asmr-product/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-product/input-image.jpg` | `present_source_asset` |
| `/apps/asmr-product/inputs/0/full` | `examples/asmr-product/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-product/input-image-full.jpg` | `present_source_asset` |
| `/apps/asmr-whisper/card` | `examples/asmr-whisper/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-whisper/card.mp4` | `missing_inherited_mp4` |
| `/apps/asmr-whisper/poster` | `examples/asmr-whisper/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-whisper/poster.jpg` | `present_source_asset` |
| `/apps/asmr-whisper/full` | `examples/asmr-whisper/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-whisper/full.mp4` | `missing_inherited_mp4` |
| `/apps/asmr-whisper/inputs/0/src` | `examples/asmr-whisper/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-whisper/input-image.jpg` | `present_source_asset` |
| `/apps/asmr-whisper/inputs/0/full` | `examples/asmr-whisper/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/asmr-whisper/input-image-full.jpg` | `present_source_asset` |
| `/apps/behind-the-scenes/card` | `examples/behind-the-scenes/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/behind-the-scenes/card.mp4` | `missing_inherited_mp4` |
| `/apps/behind-the-scenes/poster` | `examples/behind-the-scenes/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/behind-the-scenes/poster.jpg` | `present_source_asset` |
| `/apps/behind-the-scenes/full` | `examples/behind-the-scenes/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/behind-the-scenes/full.mp4` | `missing_inherited_mp4` |
| `/apps/behind-the-scenes/inputs/0/src` | `examples/behind-the-scenes/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/behind-the-scenes/input-image.jpg` | `present_source_asset` |
| `/apps/behind-the-scenes/inputs/0/full` | `examples/behind-the-scenes/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/behind-the-scenes/input-image-full.jpg` | `present_source_asset` |
| `/apps/billboard/card` | `examples/billboard/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/billboard/card.jpg` | `present_source_asset` |
| `/apps/billboard/full` | `examples/billboard/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/billboard/full.jpg` | `present_source_asset` |
| `/apps/billboard/inputs/0/src` | `examples/billboard/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/billboard/input-image.jpg` | `present_source_asset` |
| `/apps/billboard/inputs/0/full` | `examples/billboard/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/billboard/input-image-full.jpg` | `present_source_asset` |
| `/apps/breakdown/card` | `examples/breakdown/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/breakdown/card.jpg` | `present_source_asset` |
| `/apps/breakdown/full` | `examples/breakdown/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/breakdown/full.jpg` | `present_source_asset` |
| `/apps/breakdown/inputs/0/src` | `examples/breakdown/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/breakdown/input-image.jpg` | `present_source_asset` |
| `/apps/breakdown/inputs/0/full` | `examples/breakdown/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/breakdown/input-image-full.jpg` | `present_source_asset` |
| `/apps/brick-toy/card` | `examples/brick-toy/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/brick-toy/card.jpg` | `present_source_asset` |
| `/apps/brick-toy/full` | `examples/brick-toy/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/brick-toy/full.jpg` | `present_source_asset` |
| `/apps/brick-toy/inputs/0/src` | `examples/brick-toy/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/brick-toy/input-image.jpg` | `present_source_asset` |
| `/apps/brick-toy/inputs/0/full` | `examples/brick-toy/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/brick-toy/input-image-full.jpg` | `present_source_asset` |
| `/apps/bullet-time-scene/card` | `examples/bullet-time-scene/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-scene/card.mp4` | `missing_inherited_mp4` |
| `/apps/bullet-time-scene/poster` | `examples/bullet-time-scene/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-scene/poster.jpg` | `present_source_asset` |
| `/apps/bullet-time-scene/full` | `examples/bullet-time-scene/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-scene/full.mp4` | `missing_inherited_mp4` |
| `/apps/bullet-time-scene/inputs/0/src` | `examples/bullet-time-scene/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-scene/input-image.jpg` | `present_source_asset` |
| `/apps/bullet-time-scene/inputs/0/full` | `examples/bullet-time-scene/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-scene/input-image-full.jpg` | `present_source_asset` |
| `/apps/bullet-time-splash/card` | `examples/bullet-time-splash/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-splash/card.mp4` | `missing_inherited_mp4` |
| `/apps/bullet-time-splash/poster` | `examples/bullet-time-splash/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-splash/poster.jpg` | `present_source_asset` |
| `/apps/bullet-time-splash/full` | `examples/bullet-time-splash/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-splash/full.mp4` | `missing_inherited_mp4` |
| `/apps/bullet-time-splash/inputs/0/src` | `examples/bullet-time-splash/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-splash/input-image.jpg` | `present_source_asset` |
| `/apps/bullet-time-splash/inputs/0/full` | `examples/bullet-time-splash/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-splash/input-image-full.jpg` | `present_source_asset` |
| `/apps/bullet-time-white/card` | `examples/bullet-time-white/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-white/card.mp4` | `missing_inherited_mp4` |
| `/apps/bullet-time-white/poster` | `examples/bullet-time-white/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-white/poster.jpg` | `present_source_asset` |
| `/apps/bullet-time-white/full` | `examples/bullet-time-white/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-white/full.mp4` | `missing_inherited_mp4` |
| `/apps/bullet-time-white/inputs/0/src` | `examples/bullet-time-white/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-white/input-image.jpg` | `present_source_asset` |
| `/apps/bullet-time-white/inputs/0/full` | `examples/bullet-time-white/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/bullet-time-white/input-image-full.jpg` | `present_source_asset` |
| `/apps/burning-sunset/card` | `examples/burning-sunset/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/burning-sunset/card.jpg` | `present_source_asset` |
| `/apps/burning-sunset/full` | `examples/burning-sunset/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/burning-sunset/full.jpg` | `present_source_asset` |
| `/apps/burning-sunset/inputs/0/src` | `examples/burning-sunset/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/burning-sunset/input-image.jpg` | `present_source_asset` |
| `/apps/burning-sunset/inputs/0/full` | `examples/burning-sunset/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/burning-sunset/input-image-full.jpg` | `present_source_asset` |
| `/apps/cafe-60s/card` | `examples/cafe-60s/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cafe-60s/card.jpg` | `present_source_asset` |
| `/apps/cafe-60s/full` | `examples/cafe-60s/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cafe-60s/full.jpg` | `present_source_asset` |
| `/apps/cafe-60s/inputs/0/src` | `examples/cafe-60s/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cafe-60s/input-image.jpg` | `present_source_asset` |
| `/apps/cafe-60s/inputs/0/full` | `examples/cafe-60s/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cafe-60s/input-image-full.jpg` | `present_source_asset` |
| `/apps/camera-copy/card` | `examples/camera-copy/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-copy/card.mp4` | `missing_inherited_mp4` |
| `/apps/camera-copy/poster` | `examples/camera-copy/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-copy/poster.jpg` | `present_source_asset` |
| `/apps/camera-copy/full` | `examples/camera-copy/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-copy/full.mp4` | `missing_inherited_mp4` |
| `/apps/camera-copy/inputs/0/src` | `examples/camera-copy/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-copy/input-image.jpg` | `present_source_asset` |
| `/apps/camera-copy/inputs/0/full` | `examples/camera-copy/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-copy/input-image-full.jpg` | `present_source_asset` |
| `/apps/camera-copy/inputs/1/src` | `examples/camera-copy/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-copy/input-clip.jpg` | `present_source_asset` |
| `/apps/camera-copy/inputs/1/full` | `examples/camera-copy/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-copy/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/camera-moves/card` | `examples/camera-moves/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-moves/card.mp4` | `missing_inherited_mp4` |
| `/apps/camera-moves/poster` | `examples/camera-moves/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-moves/poster.jpg` | `present_source_asset` |
| `/apps/camera-moves/full` | `examples/camera-moves/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-moves/full.mp4` | `missing_inherited_mp4` |
| `/apps/camera-moves/inputs/0/src` | `examples/camera-moves/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-moves/input-image.jpg` | `present_source_asset` |
| `/apps/camera-moves/inputs/0/full` | `examples/camera-moves/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/camera-moves/input-image-full.jpg` | `present_source_asset` |
| `/apps/chameleon/card` | `examples/chameleon/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/chameleon/card.mp4` | `missing_inherited_mp4` |
| `/apps/chameleon/poster` | `examples/chameleon/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/chameleon/poster.jpg` | `present_source_asset` |
| `/apps/chameleon/full` | `examples/chameleon/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/chameleon/full.mp4` | `missing_inherited_mp4` |
| `/apps/chameleon/inputs/0/src` | `examples/chameleon/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/chameleon/input-image.jpg` | `present_source_asset` |
| `/apps/chameleon/inputs/0/full` | `examples/chameleon/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/chameleon/input-image-full.jpg` | `present_source_asset` |
| `/apps/character/card` | `examples/character/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character/card.jpg` | `present_source_asset` |
| `/apps/character/full` | `examples/character/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character/full.jpg` | `present_source_asset` |
| `/apps/character/inputs/0/src` | `examples/character/input-reference.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character/input-reference.jpg` | `present_source_asset` |
| `/apps/character/inputs/0/full` | `examples/character/input-reference-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character/input-reference-full.jpg` | `present_source_asset` |
| `/apps/character-3/card` | `examples/character-3/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-3/card.jpg` | `present_source_asset` |
| `/apps/character-3/full` | `examples/character-3/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-3/full.jpg` | `present_source_asset` |
| `/apps/character-3/inputs/0/src` | `examples/character-3/input-photo1.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-3/input-photo1.jpg` | `present_source_asset` |
| `/apps/character-3/inputs/0/full` | `examples/character-3/input-photo1-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-3/input-photo1-full.jpg` | `present_source_asset` |
| `/apps/character-3/inputs/1/src` | `examples/character-3/input-photo2.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-3/input-photo2.jpg` | `present_source_asset` |
| `/apps/character-3/inputs/1/full` | `examples/character-3/input-photo2-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-3/input-photo2-full.jpg` | `present_source_asset` |
| `/apps/character-3/inputs/2/src` | `examples/character-3/input-photo3.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-3/input-photo3.jpg` | `present_source_asset` |
| `/apps/character-3/inputs/2/full` | `examples/character-3/input-photo3-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-3/input-photo3-full.jpg` | `present_source_asset` |
| `/apps/character-swap/card` | `examples/character-swap/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-swap/card.jpg` | `present_source_asset` |
| `/apps/character-swap/full` | `examples/character-swap/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-swap/full.jpg` | `present_source_asset` |
| `/apps/character-swap/inputs/0/src` | `examples/character-swap/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-swap/input-image.jpg` | `present_source_asset` |
| `/apps/character-swap/inputs/0/full` | `examples/character-swap/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-swap/input-image-full.jpg` | `present_source_asset` |
| `/apps/character-swap/inputs/1/src` | `examples/character-swap/input-image2.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-swap/input-image2.jpg` | `present_source_asset` |
| `/apps/character-swap/inputs/1/full` | `examples/character-swap/input-image2-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/character-swap/input-image2-full.jpg` | `present_source_asset` |
| `/apps/cinema-studio/card` | `examples/cinema-studio/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cinema-studio/card.jpg` | `present_source_asset` |
| `/apps/cinema-studio/full` | `examples/cinema-studio/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cinema-studio/full.jpg` | `present_source_asset` |
| `/apps/cinema-video/card` | `examples/cinema-video/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cinema-video/card.mp4` | `missing_inherited_mp4` |
| `/apps/cinema-video/poster` | `examples/cinema-video/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cinema-video/poster.jpg` | `present_source_asset` |
| `/apps/cinema-video/full` | `examples/cinema-video/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cinema-video/full.mp4` | `missing_inherited_mp4` |
| `/apps/cloud-surf/card` | `examples/cloud-surf/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cloud-surf/card.mp4` | `missing_inherited_mp4` |
| `/apps/cloud-surf/poster` | `examples/cloud-surf/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cloud-surf/poster.jpg` | `present_source_asset` |
| `/apps/cloud-surf/full` | `examples/cloud-surf/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cloud-surf/full.mp4` | `missing_inherited_mp4` |
| `/apps/cloud-surf/inputs/0/src` | `examples/cloud-surf/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cloud-surf/input-image.jpg` | `present_source_asset` |
| `/apps/cloud-surf/inputs/0/full` | `examples/cloud-surf/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/cloud-surf/input-image-full.jpg` | `present_source_asset` |
| `/apps/color-grade/card` | `examples/color-grade/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/color-grade/card.jpg` | `present_source_asset` |
| `/apps/color-grade/full` | `examples/color-grade/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/color-grade/full.jpg` | `present_source_asset` |
| `/apps/color-grade/inputs/0/src` | `examples/color-grade/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/color-grade/input-image.jpg` | `present_source_asset` |
| `/apps/color-grade/inputs/0/full` | `examples/color-grade/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/color-grade/input-image-full.jpg` | `present_source_asset` |
| `/apps/comic-book/card` | `examples/comic-book/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/comic-book/card.jpg` | `present_source_asset` |
| `/apps/comic-book/full` | `examples/comic-book/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/comic-book/full.jpg` | `present_source_asset` |
| `/apps/comic-book/inputs/0/src` | `examples/comic-book/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/comic-book/input-image.jpg` | `present_source_asset` |
| `/apps/comic-book/inputs/0/full` | `examples/comic-book/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/comic-book/input-image-full.jpg` | `present_source_asset` |
| `/apps/commercial-faces/card` | `examples/commercial-faces/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/commercial-faces/card.jpg` | `present_source_asset` |
| `/apps/commercial-faces/full` | `examples/commercial-faces/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/commercial-faces/full.jpg` | `present_source_asset` |
| `/apps/commercial-faces/inputs/0/src` | `examples/commercial-faces/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/commercial-faces/input-image.jpg` | `present_source_asset` |
| `/apps/commercial-faces/inputs/0/full` | `examples/commercial-faces/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/commercial-faces/input-image-full.jpg` | `present_source_asset` |
| `/apps/create-image/card` | `examples/create-image/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/create-image/card.jpg` | `present_source_asset` |
| `/apps/create-image/full` | `examples/create-image/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/create-image/full.jpg` | `present_source_asset` |
| `/apps/depth-map/card` | `examples/depth-map/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/depth-map/card.jpg` | `present_source_asset` |
| `/apps/depth-map/full` | `examples/depth-map/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/depth-map/full.jpg` | `present_source_asset` |
| `/apps/depth-map/inputs/0/src` | `examples/depth-map/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/depth-map/input-image.jpg` | `present_source_asset` |
| `/apps/depth-map/inputs/0/full` | `examples/depth-map/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/depth-map/input-image-full.jpg` | `present_source_asset` |
| `/apps/dub/card` | `examples/dub/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/dub/card.mp4` | `missing_inherited_mp4` |
| `/apps/dub/poster` | `examples/dub/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/dub/poster.jpg` | `present_source_asset` |
| `/apps/dub/full` | `examples/dub/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/dub/full.mp4` | `missing_inherited_mp4` |
| `/apps/dub/inputs/0/src` | `examples/dub/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/dub/input-clip.jpg` | `present_source_asset` |
| `/apps/dub/inputs/0/full` | `examples/dub/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/dub/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/edit/card` | `examples/edit/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit/card.jpg` | `present_source_asset` |
| `/apps/edit/full` | `examples/edit/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit/full.jpg` | `present_source_asset` |
| `/apps/edit/inputs/0/src` | `examples/edit/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit/input-image.jpg` | `present_source_asset` |
| `/apps/edit/inputs/0/full` | `examples/edit/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit/input-image-full.jpg` | `present_source_asset` |
| `/apps/edit-text/card` | `examples/edit-text/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit-text/card.jpg` | `present_source_asset` |
| `/apps/edit-text/full` | `examples/edit-text/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit-text/full.jpg` | `present_source_asset` |
| `/apps/edit-text/inputs/0/src` | `examples/edit-text/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit-text/input-image.jpg` | `present_source_asset` |
| `/apps/edit-text/inputs/0/full` | `examples/edit-text/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/edit-text/input-image-full.jpg` | `present_source_asset` |
| `/apps/effects/card` | `examples/effects/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/poster` | `examples/effects/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/poster.jpg` | `present_source_asset` |
| `/apps/effects/full` | `examples/effects/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/full.mp4` | `missing_inherited_mp4` |
| `/apps/effects/inputs/0/src` | `examples/effects/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/input-image.jpg` | `present_source_asset` |
| `/apps/effects/inputs/0/full` | `examples/effects/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/input-image-full.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/angry/card` | `examples/effects/options/effect/angry/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/angry/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/angry/poster` | `examples/effects/options/effect/angry/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/angry/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/crying/card` | `examples/effects/options/effect/crying/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crying/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/crying/poster` | `examples/effects/options/effect/crying/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crying/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/laughing/card` | `examples/effects/options/effect/laughing/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/laughing/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/laughing/poster` | `examples/effects/options/effect/laughing/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/laughing/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/puppies/card` | `examples/effects/options/effect/puppies/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/puppies/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/puppies/poster` | `examples/effects/options/effect/puppies/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/puppies/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/cakeify/card` | `examples/effects/options/effect/cakeify/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/cakeify/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/cakeify/poster` | `examples/effects/options/effect/cakeify/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/cakeify/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/crush/card` | `examples/effects/options/effect/crush/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crush/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/crush/poster` | `examples/effects/options/effect/crush/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crush/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/deflate/card` | `examples/effects/options/effect/deflate/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/deflate/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/deflate/poster` | `examples/effects/options/effect/deflate/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/deflate/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/electrify/card` | `examples/effects/options/effect/electrify/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/electrify/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/electrify/poster` | `examples/effects/options/effect/electrify/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/electrify/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/explode/card` | `examples/effects/options/effect/explode/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/explode/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/explode/poster` | `examples/effects/options/effect/explode/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/explode/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/inflate/card` | `examples/effects/options/effect/inflate/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/inflate/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/inflate/poster` | `examples/effects/options/effect/inflate/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/inflate/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/rotate/card` | `examples/effects/options/effect/rotate/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/rotate/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/rotate/poster` | `examples/effects/options/effect/rotate/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/rotate/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/squish/card` | `examples/effects/options/effect/squish/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/squish/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/squish/poster` | `examples/effects/options/effect/squish/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/squish/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/orbit-360/card` | `examples/effects/options/effect/orbit-360/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/orbit-360/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/orbit-360/poster` | `examples/effects/options/effect/orbit-360/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/orbit-360/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/arc-shot/card` | `examples/effects/options/effect/arc-shot/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/arc-shot/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/arc-shot/poster` | `examples/effects/options/effect/arc-shot/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/arc-shot/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/bullet-time/card` | `examples/effects/options/effect/bullet-time/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/bullet-time/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/bullet-time/poster` | `examples/effects/options/effect/bullet-time/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/bullet-time/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/car-chase/card` | `examples/effects/options/effect/car-chase/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/car-chase/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/car-chase/poster` | `examples/effects/options/effect/car-chase/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/car-chase/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/crane-down/card` | `examples/effects/options/effect/crane-down/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crane-down/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/crane-down/poster` | `examples/effects/options/effect/crane-down/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crane-down/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/crane-over-head/card` | `examples/effects/options/effect/crane-over-head/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crane-over-head/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/crane-over-head/poster` | `examples/effects/options/effect/crane-over-head/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crane-over-head/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/crane-up/card` | `examples/effects/options/effect/crane-up/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crane-up/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/crane-up/poster` | `examples/effects/options/effect/crane-up/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crane-up/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/crash-zoom-in/card` | `examples/effects/options/effect/crash-zoom-in/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crash-zoom-in/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/crash-zoom-in/poster` | `examples/effects/options/effect/crash-zoom-in/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/crash-zoom-in/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/dolly-zoom/card` | `examples/effects/options/effect/dolly-zoom/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/dolly-zoom/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/dolly-zoom/poster` | `examples/effects/options/effect/dolly-zoom/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/dolly-zoom/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/hero-run/card` | `examples/effects/options/effect/hero-run/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/hero-run/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/hero-run/poster` | `examples/effects/options/effect/hero-run/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/hero-run/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/steam/card` | `examples/effects/options/effect/steam/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/steam/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/steam/poster` | `examples/effects/options/effect/steam/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/steam/poster.jpg` | `present_source_asset` |
| `/apps/effects/options/effect/money-rain/card` | `examples/effects/options/effect/money-rain/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/money-rain/card.mp4` | `missing_inherited_mp4` |
| `/apps/effects/options/effect/money-rain/poster` | `examples/effects/options/effect/money-rain/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/effects/options/effect/money-rain/poster.jpg` | `present_source_asset` |
| `/apps/expand-image/card` | `examples/expand-image/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/expand-image/card.jpg` | `present_source_asset` |
| `/apps/expand-image/full` | `examples/expand-image/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/expand-image/full.jpg` | `present_source_asset` |
| `/apps/expand-image/inputs/0/src` | `examples/expand-image/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/expand-image/input-image.jpg` | `present_source_asset` |
| `/apps/expand-image/inputs/0/full` | `examples/expand-image/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/expand-image/input-image-full.jpg` | `present_source_asset` |
| `/apps/extend-video/card` | `examples/extend-video/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/extend-video/card.mp4` | `missing_inherited_mp4` |
| `/apps/extend-video/poster` | `examples/extend-video/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/extend-video/poster.jpg` | `present_source_asset` |
| `/apps/extend-video/full` | `examples/extend-video/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/extend-video/full.mp4` | `missing_inherited_mp4` |
| `/apps/extend-video/inputs/0/src` | `examples/extend-video/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/extend-video/input-clip.jpg` | `present_source_asset` |
| `/apps/extend-video/inputs/0/full` | `examples/extend-video/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/extend-video/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/face-swap/card` | `examples/face-swap/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/face-swap/card.jpg` | `present_source_asset` |
| `/apps/face-swap/full` | `examples/face-swap/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/face-swap/full.jpg` | `present_source_asset` |
| `/apps/face-swap/inputs/0/src` | `examples/face-swap/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/face-swap/input-image.jpg` | `present_source_asset` |
| `/apps/face-swap/inputs/0/full` | `examples/face-swap/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/face-swap/input-image-full.jpg` | `present_source_asset` |
| `/apps/face-swap/inputs/1/src` | `examples/face-swap/input-image2.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/face-swap/input-image2.jpg` | `present_source_asset` |
| `/apps/face-swap/inputs/1/full` | `examples/face-swap/input-image2-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/face-swap/input-image2-full.jpg` | `present_source_asset` |
| `/apps/fashion-factory/card` | `examples/fashion-factory/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fashion-factory/card.jpg` | `present_source_asset` |
| `/apps/fashion-factory/full` | `examples/fashion-factory/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fashion-factory/full.jpg` | `present_source_asset` |
| `/apps/fashion-factory/inputs/0/src` | `examples/fashion-factory/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fashion-factory/input-image.jpg` | `present_source_asset` |
| `/apps/fashion-factory/inputs/0/full` | `examples/fashion-factory/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fashion-factory/input-image-full.jpg` | `present_source_asset` |
| `/apps/fashion-factory/inputs/1/src` | `examples/fashion-factory/input-image2.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fashion-factory/input-image2.jpg` | `present_source_asset` |
| `/apps/fashion-factory/inputs/1/full` | `examples/fashion-factory/input-image2-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fashion-factory/input-image2-full.jpg` | `present_source_asset` |
| `/apps/figure-3d/card` | `examples/figure-3d/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/figure-3d/card.jpg` | `present_source_asset` |
| `/apps/figure-3d/full` | `examples/figure-3d/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/figure-3d/full.jpg` | `present_source_asset` |
| `/apps/figure-3d/inputs/0/src` | `examples/figure-3d/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/figure-3d/input-image.jpg` | `present_source_asset` |
| `/apps/figure-3d/inputs/0/full` | `examples/figure-3d/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/figure-3d/input-image-full.jpg` | `present_source_asset` |
| `/apps/fridge-ad/card` | `examples/fridge-ad/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fridge-ad/card.jpg` | `present_source_asset` |
| `/apps/fridge-ad/full` | `examples/fridge-ad/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fridge-ad/full.jpg` | `present_source_asset` |
| `/apps/fridge-ad/inputs/0/src` | `examples/fridge-ad/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fridge-ad/input-image.jpg` | `present_source_asset` |
| `/apps/fridge-ad/inputs/0/full` | `examples/fridge-ad/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/fridge-ad/input-image-full.jpg` | `present_source_asset` |
| `/apps/game-styles/card` | `examples/game-styles/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/game-styles/card.jpg` | `present_source_asset` |
| `/apps/game-styles/full` | `examples/game-styles/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/game-styles/full.jpg` | `present_source_asset` |
| `/apps/game-styles/inputs/0/src` | `examples/game-styles/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/game-styles/input-image.jpg` | `present_source_asset` |
| `/apps/game-styles/inputs/0/full` | `examples/game-styles/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/game-styles/input-image-full.jpg` | `present_source_asset` |
| `/apps/genjutsu/card` | `examples/genjutsu/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/genjutsu/card.mp4` | `missing_inherited_mp4` |
| `/apps/genjutsu/poster` | `examples/genjutsu/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/genjutsu/poster.jpg` | `present_source_asset` |
| `/apps/genjutsu/full` | `examples/genjutsu/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/genjutsu/full.mp4` | `missing_inherited_mp4` |
| `/apps/genjutsu/inputs/0/src` | `examples/genjutsu/input-sheet.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/genjutsu/input-sheet.jpg` | `present_source_asset` |
| `/apps/genjutsu/inputs/0/full` | `examples/genjutsu/input-sheet-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/genjutsu/input-sheet-full.jpg` | `present_source_asset` |
| `/apps/giallo/card` | `examples/giallo/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giallo/card.jpg` | `present_source_asset` |
| `/apps/giallo/full` | `examples/giallo/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giallo/full.jpg` | `present_source_asset` |
| `/apps/giallo/inputs/0/src` | `examples/giallo/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giallo/input-image.jpg` | `present_source_asset` |
| `/apps/giallo/inputs/0/full` | `examples/giallo/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giallo/input-image-full.jpg` | `present_source_asset` |
| `/apps/giant-product/card` | `examples/giant-product/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giant-product/card.jpg` | `present_source_asset` |
| `/apps/giant-product/full` | `examples/giant-product/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giant-product/full.jpg` | `present_source_asset` |
| `/apps/giant-product/inputs/0/src` | `examples/giant-product/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giant-product/input-image.jpg` | `present_source_asset` |
| `/apps/giant-product/inputs/0/full` | `examples/giant-product/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/giant-product/input-image-full.jpg` | `present_source_asset` |
| `/apps/glitter-sticker/card` | `examples/glitter-sticker/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/glitter-sticker/card.jpg` | `present_source_asset` |
| `/apps/glitter-sticker/full` | `examples/glitter-sticker/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/glitter-sticker/full.jpg` | `present_source_asset` |
| `/apps/glitter-sticker/inputs/0/src` | `examples/glitter-sticker/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/glitter-sticker/input-image.jpg` | `present_source_asset` |
| `/apps/glitter-sticker/inputs/0/full` | `examples/glitter-sticker/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/glitter-sticker/input-image-full.jpg` | `present_source_asset` |
| `/apps/graffiti-ad/card` | `examples/graffiti-ad/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/graffiti-ad/card.jpg` | `present_source_asset` |
| `/apps/graffiti-ad/full` | `examples/graffiti-ad/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/graffiti-ad/full.jpg` | `present_source_asset` |
| `/apps/graffiti-ad/inputs/0/src` | `examples/graffiti-ad/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/graffiti-ad/input-image.jpg` | `present_source_asset` |
| `/apps/graffiti-ad/inputs/0/full` | `examples/graffiti-ad/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/graffiti-ad/input-image-full.jpg` | `present_source_asset` |
| `/apps/h3-photo/card` | `examples/h3-photo/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-photo/card.mp4` | `missing_inherited_mp4` |
| `/apps/h3-photo/poster` | `examples/h3-photo/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-photo/poster.jpg` | `present_source_asset` |
| `/apps/h3-photo/full` | `examples/h3-photo/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-photo/full.mp4` | `missing_inherited_mp4` |
| `/apps/h3-photo/inputs/0/src` | `examples/h3-photo/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-photo/input-image.jpg` | `present_source_asset` |
| `/apps/h3-photo/inputs/0/full` | `examples/h3-photo/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-photo/input-image-full.jpg` | `present_source_asset` |
| `/apps/h3-video/card` | `examples/h3-video/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-video/card.mp4` | `missing_inherited_mp4` |
| `/apps/h3-video/poster` | `examples/h3-video/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-video/poster.jpg` | `present_source_asset` |
| `/apps/h3-video/full` | `examples/h3-video/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/h3-video/full.mp4` | `missing_inherited_mp4` |
| `/apps/headshot/card` | `examples/headshot/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/headshot/card.jpg` | `present_source_asset` |
| `/apps/headshot/full` | `examples/headshot/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/headshot/full.jpg` | `present_source_asset` |
| `/apps/headshot/inputs/0/src` | `examples/headshot/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/headshot/input-image.jpg` | `present_source_asset` |
| `/apps/headshot/inputs/0/full` | `examples/headshot/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/headshot/input-image-full.jpg` | `present_source_asset` |
| `/apps/idol/card` | `examples/idol/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/idol/card.mp4` | `missing_inherited_mp4` |
| `/apps/idol/poster` | `examples/idol/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/idol/poster.jpg` | `present_source_asset` |
| `/apps/idol/full` | `examples/idol/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/idol/full.mp4` | `missing_inherited_mp4` |
| `/apps/idol/inputs/0/src` | `examples/idol/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/idol/input-image.jpg` | `present_source_asset` |
| `/apps/idol/inputs/0/full` | `examples/idol/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/idol/input-image-full.jpg` | `present_source_asset` |
| `/apps/image-effects/card` | `examples/image-effects/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/image-effects/card.jpg` | `present_source_asset` |
| `/apps/image-effects/full` | `examples/image-effects/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/image-effects/full.jpg` | `present_source_asset` |
| `/apps/image-effects/inputs/0/src` | `examples/image-effects/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/image-effects/input-image.jpg` | `present_source_asset` |
| `/apps/image-effects/inputs/0/full` | `examples/image-effects/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/image-effects/input-image-full.jpg` | `present_source_asset` |
| `/apps/inpaint/card` | `examples/inpaint/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/inpaint/card.jpg` | `present_source_asset` |
| `/apps/inpaint/full` | `examples/inpaint/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/inpaint/full.jpg` | `present_source_asset` |
| `/apps/inpaint/inputs/0/src` | `examples/inpaint/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/inpaint/input-image.jpg` | `present_source_asset` |
| `/apps/inpaint/inputs/0/full` | `examples/inpaint/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/inpaint/input-image-full.jpg` | `present_source_asset` |
| `/apps/inpaint/inputs/1/src` | `examples/inpaint/input-mask-full.png` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/inpaint/input-mask-full.png` | `present_source_asset` |
| `/apps/inpaint/inputs/1/full` | `examples/inpaint/input-mask-full.png` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/inpaint/input-mask-full.png` | `present_source_asset` |
| `/apps/j-magazine/card` | `examples/j-magazine/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-magazine/card.jpg` | `present_source_asset` |
| `/apps/j-magazine/full` | `examples/j-magazine/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-magazine/full.jpg` | `present_source_asset` |
| `/apps/j-magazine/inputs/0/src` | `examples/j-magazine/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-magazine/input-image.jpg` | `present_source_asset` |
| `/apps/j-magazine/inputs/0/full` | `examples/j-magazine/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-magazine/input-image-full.jpg` | `present_source_asset` |
| `/apps/j-poster/card` | `examples/j-poster/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-poster/card.jpg` | `present_source_asset` |
| `/apps/j-poster/full` | `examples/j-poster/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-poster/full.jpg` | `present_source_asset` |
| `/apps/j-poster/inputs/0/src` | `examples/j-poster/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-poster/input-image.jpg` | `present_source_asset` |
| `/apps/j-poster/inputs/0/full` | `examples/j-poster/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/j-poster/input-image-full.jpg` | `present_source_asset` |
| `/apps/japanese-show/card` | `examples/japanese-show/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/japanese-show/card.jpg` | `present_source_asset` |
| `/apps/japanese-show/full` | `examples/japanese-show/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/japanese-show/full.jpg` | `present_source_asset` |
| `/apps/japanese-show/inputs/0/src` | `examples/japanese-show/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/japanese-show/input-image.jpg` | `present_source_asset` |
| `/apps/japanese-show/inputs/0/full` | `examples/japanese-show/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/japanese-show/input-image-full.jpg` | `present_source_asset` |
| `/apps/kick-ad/card` | `examples/kick-ad/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/kick-ad/card.mp4` | `missing_inherited_mp4` |
| `/apps/kick-ad/poster` | `examples/kick-ad/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/kick-ad/poster.jpg` | `present_source_asset` |
| `/apps/kick-ad/full` | `examples/kick-ad/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/kick-ad/full.mp4` | `missing_inherited_mp4` |
| `/apps/kick-ad/inputs/0/src` | `examples/kick-ad/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/kick-ad/input-image.jpg` | `present_source_asset` |
| `/apps/kick-ad/inputs/0/full` | `examples/kick-ad/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/kick-ad/input-image-full.jpg` | `present_source_asset` |
| `/apps/macro-product/card` | `examples/macro-product/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-product/card.jpg` | `present_source_asset` |
| `/apps/macro-product/full` | `examples/macro-product/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-product/full.jpg` | `present_source_asset` |
| `/apps/macro-product/inputs/0/src` | `examples/macro-product/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-product/input-image.jpg` | `present_source_asset` |
| `/apps/macro-product/inputs/0/full` | `examples/macro-product/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-product/input-image-full.jpg` | `present_source_asset` |
| `/apps/macro-scene/card` | `examples/macro-scene/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-scene/card.jpg` | `present_source_asset` |
| `/apps/macro-scene/full` | `examples/macro-scene/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-scene/full.jpg` | `present_source_asset` |
| `/apps/macro-scene/inputs/0/src` | `examples/macro-scene/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-scene/input-image.jpg` | `present_source_asset` |
| `/apps/macro-scene/inputs/0/full` | `examples/macro-scene/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/macro-scene/input-image-full.jpg` | `present_source_asset` |
| `/apps/magic-button/card` | `examples/magic-button/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/magic-button/card.mp4` | `missing_inherited_mp4` |
| `/apps/magic-button/poster` | `examples/magic-button/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/magic-button/poster.jpg` | `present_source_asset` |
| `/apps/magic-button/full` | `examples/magic-button/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/magic-button/full.mp4` | `missing_inherited_mp4` |
| `/apps/magic-button/inputs/0/src` | `examples/magic-button/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/magic-button/input-image.jpg` | `present_source_asset` |
| `/apps/magic-button/inputs/0/full` | `examples/magic-button/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/magic-button/input-image-full.jpg` | `present_source_asset` |
| `/apps/mascot/card` | `examples/mascot/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mascot/card.jpg` | `present_source_asset` |
| `/apps/mascot/full` | `examples/mascot/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mascot/full.jpg` | `present_source_asset` |
| `/apps/mascot/inputs/0/src` | `examples/mascot/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mascot/input-image.jpg` | `present_source_asset` |
| `/apps/mascot/inputs/0/full` | `examples/mascot/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mascot/input-image-full.jpg` | `present_source_asset` |
| `/apps/melting-doodle/card` | `examples/melting-doodle/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/melting-doodle/card.mp4` | `missing_inherited_mp4` |
| `/apps/melting-doodle/poster` | `examples/melting-doodle/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/melting-doodle/poster.jpg` | `present_source_asset` |
| `/apps/melting-doodle/full` | `examples/melting-doodle/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/melting-doodle/full.mp4` | `missing_inherited_mp4` |
| `/apps/melting-doodle/inputs/0/src` | `examples/melting-doodle/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/melting-doodle/input-image.jpg` | `present_source_asset` |
| `/apps/melting-doodle/inputs/0/full` | `examples/melting-doodle/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/melting-doodle/input-image-full.jpg` | `present_source_asset` |
| `/apps/meme/card` | `examples/meme/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/meme/card.jpg` | `present_source_asset` |
| `/apps/meme/full` | `examples/meme/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/meme/full.jpg` | `present_source_asset` |
| `/apps/micro-beasts/card` | `examples/micro-beasts/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/micro-beasts/card.jpg` | `present_source_asset` |
| `/apps/micro-beasts/full` | `examples/micro-beasts/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/micro-beasts/full.jpg` | `present_source_asset` |
| `/apps/micro-beasts/inputs/0/src` | `examples/micro-beasts/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/micro-beasts/input-image.jpg` | `present_source_asset` |
| `/apps/micro-beasts/inputs/0/full` | `examples/micro-beasts/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/micro-beasts/input-image-full.jpg` | `present_source_asset` |
| `/apps/mixed-media/card` | `examples/mixed-media/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/poster` | `examples/mixed-media/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/full` | `examples/mixed-media/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/full.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/inputs/0/src` | `examples/mixed-media/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/input-clip.jpg` | `present_source_asset` |
| `/apps/mixed-media/inputs/0/full` | `examples/mixed-media/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/anime/card` | `examples/mixed-media/options/style/anime/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/anime/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/anime/poster` | `examples/mixed-media/options/style/anime/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/anime/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/claymation/card` | `examples/mixed-media/options/style/claymation/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/claymation/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/claymation/poster` | `examples/mixed-media/options/style/claymation/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/claymation/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/watercolor/card` | `examples/mixed-media/options/style/watercolor/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/watercolor/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/watercolor/poster` | `examples/mixed-media/options/style/watercolor/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/watercolor/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/comic-book/card` | `examples/mixed-media/options/style/comic-book/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/comic-book/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/comic-book/poster` | `examples/mixed-media/options/style/comic-book/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/comic-book/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/oil-painting/card` | `examples/mixed-media/options/style/oil-painting/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/oil-painting/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/oil-painting/poster` | `examples/mixed-media/options/style/oil-painting/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/oil-painting/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/brick-toy/card` | `examples/mixed-media/options/style/brick-toy/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/brick-toy/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/brick-toy/poster` | `examples/mixed-media/options/style/brick-toy/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/brick-toy/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/cyberpunk/card` | `examples/mixed-media/options/style/cyberpunk/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/cyberpunk/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/cyberpunk/poster` | `examples/mixed-media/options/style/cyberpunk/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/cyberpunk/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/paper-cutout/card` | `examples/mixed-media/options/style/paper-cutout/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/paper-cutout/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/paper-cutout/poster` | `examples/mixed-media/options/style/paper-cutout/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/paper-cutout/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/pencil-sketch/card` | `examples/mixed-media/options/style/pencil-sketch/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/pencil-sketch/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/pencil-sketch/poster` | `examples/mixed-media/options/style/pencil-sketch/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/pencil-sketch/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/film-noir/card` | `examples/mixed-media/options/style/film-noir/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/film-noir/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/film-noir/poster` | `examples/mixed-media/options/style/film-noir/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/film-noir/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/ukiyo-e/card` | `examples/mixed-media/options/style/ukiyo-e/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/ukiyo-e/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/ukiyo-e/poster` | `examples/mixed-media/options/style/ukiyo-e/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/ukiyo-e/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/stained-glass/card` | `examples/mixed-media/options/style/stained-glass/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/stained-glass/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/stained-glass/poster` | `examples/mixed-media/options/style/stained-glass/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/stained-glass/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/low-poly-3d/card` | `examples/mixed-media/options/style/low-poly-3d/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/low-poly-3d/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/low-poly-3d/poster` | `examples/mixed-media/options/style/low-poly-3d/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/low-poly-3d/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/charcoal/card` | `examples/mixed-media/options/style/charcoal/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/charcoal/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/charcoal/poster` | `examples/mixed-media/options/style/charcoal/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/charcoal/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/pop-art/card` | `examples/mixed-media/options/style/pop-art/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/pop-art/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/pop-art/poster` | `examples/mixed-media/options/style/pop-art/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/pop-art/poster.jpg` | `present_source_asset` |
| `/apps/mixed-media/options/style/felt-toy/card` | `examples/mixed-media/options/style/felt-toy/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/felt-toy/card.mp4` | `missing_inherited_mp4` |
| `/apps/mixed-media/options/style/felt-toy/poster` | `examples/mixed-media/options/style/felt-toy/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mixed-media/options/style/felt-toy/poster.jpg` | `present_source_asset` |
| `/apps/moodboard/card` | `examples/moodboard/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moodboard/card.jpg` | `present_source_asset` |
| `/apps/moodboard/full` | `examples/moodboard/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moodboard/full.jpg` | `present_source_asset` |
| `/apps/moodboard/inputs/0/src` | `examples/moodboard/input-style1.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moodboard/input-style1.jpg` | `present_source_asset` |
| `/apps/moodboard/inputs/0/full` | `examples/moodboard/input-style1-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moodboard/input-style1-full.jpg` | `present_source_asset` |
| `/apps/moodboard/inputs/1/src` | `examples/moodboard/input-style2.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moodboard/input-style2.jpg` | `present_source_asset` |
| `/apps/moodboard/inputs/1/full` | `examples/moodboard/input-style2-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moodboard/input-style2-full.jpg` | `present_source_asset` |
| `/apps/moodboard/inputs/2/src` | `examples/moodboard/input-style3.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moodboard/input-style3.jpg` | `present_source_asset` |
| `/apps/moodboard/inputs/2/full` | `examples/moodboard/input-style3-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moodboard/input-style3-full.jpg` | `present_source_asset` |
| `/apps/morph/card` | `examples/morph/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/poster` | `examples/morph/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/poster.jpg` | `present_source_asset` |
| `/apps/morph/full` | `examples/morph/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/full.mp4` | `missing_inherited_mp4` |
| `/apps/morph/inputs/0/src` | `examples/morph/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/input-image.jpg` | `present_source_asset` |
| `/apps/morph/inputs/0/full` | `examples/morph/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/input-image-full.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/renaissance/card` | `examples/morph/options/effect/renaissance/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/renaissance/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/renaissance/poster` | `examples/morph/options/effect/renaissance/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/renaissance/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/red-carpet/card` | `examples/morph/options/effect/red-carpet/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/red-carpet/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/red-carpet/poster` | `examples/morph/options/effect/red-carpet/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/red-carpet/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/younger-self/card` | `examples/morph/options/effect/younger-self/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/younger-self/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/younger-self/poster` | `examples/morph/options/effect/younger-self/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/younger-self/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/clones/card` | `examples/morph/options/effect/clones/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/clones/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/clones/poster` | `examples/morph/options/effect/clones/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/clones/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/cartoon/card` | `examples/morph/options/effect/cartoon/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/cartoon/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/cartoon/poster` | `examples/morph/options/effect/cartoon/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/cartoon/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/statue/card` | `examples/morph/options/effect/statue/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/statue/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/statue/poster` | `examples/morph/options/effect/statue/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/statue/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/old-age/card` | `examples/morph/options/effect/old-age/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/old-age/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/old-age/poster` | `examples/morph/options/effect/old-age/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/old-age/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/astronaut/card` | `examples/morph/options/effect/astronaut/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/astronaut/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/astronaut/poster` | `examples/morph/options/effect/astronaut/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/astronaut/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/knight/card` | `examples/morph/options/effect/knight/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/knight/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/knight/poster` | `examples/morph/options/effect/knight/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/knight/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/assassin/card` | `examples/morph/options/effect/assassin/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/assassin/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/assassin/poster` | `examples/morph/options/effect/assassin/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/assassin/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/baby/card` | `examples/morph/options/effect/baby/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/baby/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/baby/poster` | `examples/morph/options/effect/baby/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/baby/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/bride/card` | `examples/morph/options/effect/bride/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/bride/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/bride/poster` | `examples/morph/options/effect/bride/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/bride/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/classy/card` | `examples/morph/options/effect/classy/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/classy/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/classy/poster` | `examples/morph/options/effect/classy/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/classy/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/princess/card` | `examples/morph/options/effect/princess/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/princess/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/princess/poster` | `examples/morph/options/effect/princess/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/princess/poster.jpg` | `present_source_asset` |
| `/apps/morph/options/effect/robot-face/card` | `examples/morph/options/effect/robot-face/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/robot-face/card.mp4` | `missing_inherited_mp4` |
| `/apps/morph/options/effect/robot-face/poster` | `examples/morph/options/effect/robot-face/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/morph/options/effect/robot-face/poster.jpg` | `present_source_asset` |
| `/apps/moss-image/card` | `examples/moss-image/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moss-image/card.jpg` | `present_source_asset` |
| `/apps/moss-image/full` | `examples/moss-image/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/moss-image/full.jpg` | `present_source_asset` |
| `/apps/motion-transfer/card` | `examples/motion-transfer/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/motion-transfer/card.mp4` | `missing_inherited_mp4` |
| `/apps/motion-transfer/poster` | `examples/motion-transfer/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/motion-transfer/poster.jpg` | `present_source_asset` |
| `/apps/motion-transfer/full` | `examples/motion-transfer/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/motion-transfer/full.mp4` | `missing_inherited_mp4` |
| `/apps/motion-transfer/inputs/0/src` | `examples/motion-transfer/input-character.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/motion-transfer/input-character.jpg` | `present_source_asset` |
| `/apps/motion-transfer/inputs/0/full` | `examples/motion-transfer/input-character-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/motion-transfer/input-character-full.jpg` | `present_source_asset` |
| `/apps/motion-transfer/inputs/1/src` | `examples/motion-transfer/input-motion.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/motion-transfer/input-motion.jpg` | `present_source_asset` |
| `/apps/motion-transfer/inputs/1/full` | `examples/motion-transfer/input-motion-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/motion-transfer/input-motion-full.mp4` | `missing_inherited_mp4` |
| `/apps/mukbang/card` | `examples/mukbang/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mukbang/card.mp4` | `missing_inherited_mp4` |
| `/apps/mukbang/poster` | `examples/mukbang/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mukbang/poster.jpg` | `present_source_asset` |
| `/apps/mukbang/full` | `examples/mukbang/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mukbang/full.mp4` | `missing_inherited_mp4` |
| `/apps/mukbang/inputs/0/src` | `examples/mukbang/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mukbang/input-image.jpg` | `present_source_asset` |
| `/apps/mukbang/inputs/0/full` | `examples/mukbang/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mukbang/input-image-full.jpg` | `present_source_asset` |
| `/apps/mural/card` | `examples/mural/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mural/card.jpg` | `present_source_asset` |
| `/apps/mural/full` | `examples/mural/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mural/full.jpg` | `present_source_asset` |
| `/apps/mural/inputs/0/src` | `examples/mural/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mural/input-image.jpg` | `present_source_asset` |
| `/apps/mural/inputs/0/full` | `examples/mural/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/mural/input-image-full.jpg` | `present_source_asset` |
| `/apps/music/card` | `examples/music/card.png` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/music/card.png` | `present_source_asset` |
| `/apps/music/full` | `examples/music/full.mp3` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/music/full.mp3` | `present_source_asset` |
| `/apps/outfit-shot/card` | `examples/outfit-shot/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-shot/card.jpg` | `present_source_asset` |
| `/apps/outfit-shot/full` | `examples/outfit-shot/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-shot/full.jpg` | `present_source_asset` |
| `/apps/outfit-shot/inputs/0/src` | `examples/outfit-shot/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-shot/input-image.jpg` | `present_source_asset` |
| `/apps/outfit-shot/inputs/0/full` | `examples/outfit-shot/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-shot/input-image-full.jpg` | `present_source_asset` |
| `/apps/outfit-shot/inputs/1/src` | `examples/outfit-shot/input-image2.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-shot/input-image2.jpg` | `present_source_asset` |
| `/apps/outfit-shot/inputs/1/full` | `examples/outfit-shot/input-image2-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-shot/input-image2-full.jpg` | `present_source_asset` |
| `/apps/outfit-swap/card` | `examples/outfit-swap/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-swap/card.jpg` | `present_source_asset` |
| `/apps/outfit-swap/full` | `examples/outfit-swap/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-swap/full.jpg` | `present_source_asset` |
| `/apps/outfit-swap/inputs/0/src` | `examples/outfit-swap/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-swap/input-image.jpg` | `present_source_asset` |
| `/apps/outfit-swap/inputs/0/full` | `examples/outfit-swap/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-swap/input-image-full.jpg` | `present_source_asset` |
| `/apps/outfit-swap/inputs/1/src` | `examples/outfit-swap/input-image2.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-swap/input-image2.jpg` | `present_source_asset` |
| `/apps/outfit-swap/inputs/1/full` | `examples/outfit-swap/input-image2-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-swap/input-image2-full.jpg` | `present_source_asset` |
| `/apps/outfit-vending/card` | `examples/outfit-vending/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-vending/card.jpg` | `present_source_asset` |
| `/apps/outfit-vending/full` | `examples/outfit-vending/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-vending/full.jpg` | `present_source_asset` |
| `/apps/outfit-vending/inputs/0/src` | `examples/outfit-vending/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-vending/input-image.jpg` | `present_source_asset` |
| `/apps/outfit-vending/inputs/0/full` | `examples/outfit-vending/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/outfit-vending/input-image-full.jpg` | `present_source_asset` |
| `/apps/packshot/card` | `examples/packshot/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/packshot/card.jpg` | `present_source_asset` |
| `/apps/packshot/full` | `examples/packshot/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/packshot/full.jpg` | `present_source_asset` |
| `/apps/packshot/inputs/0/src` | `examples/packshot/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/packshot/input-image.jpg` | `present_source_asset` |
| `/apps/packshot/inputs/0/full` | `examples/packshot/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/packshot/input-image-full.jpg` | `present_source_asset` |
| `/apps/paint-app/card` | `examples/paint-app/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/paint-app/card.jpg` | `present_source_asset` |
| `/apps/paint-app/full` | `examples/paint-app/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/paint-app/full.jpg` | `present_source_asset` |
| `/apps/paint-app/inputs/0/src` | `examples/paint-app/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/paint-app/input-image.jpg` | `present_source_asset` |
| `/apps/paint-app/inputs/0/full` | `examples/paint-app/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/paint-app/input-image-full.jpg` | `present_source_asset` |
| `/apps/photodump/card` | `examples/photodump/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/photodump/card.jpg` | `present_source_asset` |
| `/apps/photodump/full` | `examples/photodump/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/photodump/full.jpg` | `present_source_asset` |
| `/apps/photodump/inputs/0/src` | `examples/photodump/input-photo.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/photodump/input-photo.jpg` | `present_source_asset` |
| `/apps/photodump/inputs/0/full` | `examples/photodump/input-photo-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/photodump/input-photo-full.jpg` | `present_source_asset` |
| `/apps/pixel-game/card` | `examples/pixel-game/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/pixel-game/card.jpg` | `present_source_asset` |
| `/apps/pixel-game/full` | `examples/pixel-game/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/pixel-game/full.jpg` | `present_source_asset` |
| `/apps/pixel-game/inputs/0/src` | `examples/pixel-game/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/pixel-game/input-image.jpg` | `present_source_asset` |
| `/apps/pixel-game/inputs/0/full` | `examples/pixel-game/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/pixel-game/input-image-full.jpg` | `present_source_asset` |
| `/apps/plushie/card` | `examples/plushie/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/plushie/card.jpg` | `present_source_asset` |
| `/apps/plushie/full` | `examples/plushie/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/plushie/full.jpg` | `present_source_asset` |
| `/apps/plushie/inputs/0/src` | `examples/plushie/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/plushie/input-image.jpg` | `present_source_asset` |
| `/apps/plushie/inputs/0/full` | `examples/plushie/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/plushie/input-image-full.jpg` | `present_source_asset` |
| `/apps/poster/card` | `examples/poster/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/poster/card.jpg` | `present_source_asset` |
| `/apps/poster/full` | `examples/poster/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/poster/full.jpg` | `present_source_asset` |
| `/apps/poster/inputs/0/src` | `examples/poster/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/poster/input-image.jpg` | `present_source_asset` |
| `/apps/poster/inputs/0/full` | `examples/poster/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/poster/input-image-full.jpg` | `present_source_asset` |
| `/apps/product-shot/card` | `examples/product-shot/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/product-shot/card.jpg` | `present_source_asset` |
| `/apps/product-shot/full` | `examples/product-shot/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/product-shot/full.jpg` | `present_source_asset` |
| `/apps/product-shot/inputs/0/src` | `examples/product-shot/input-product.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/product-shot/input-product.jpg` | `present_source_asset` |
| `/apps/product-shot/inputs/0/full` | `examples/product-shot/input-product-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/product-shot/input-product-full.jpg` | `present_source_asset` |
| `/apps/rap-video/card` | `examples/rap-video/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/rap-video/card.mp4` | `missing_inherited_mp4` |
| `/apps/rap-video/poster` | `examples/rap-video/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/rap-video/poster.jpg` | `present_source_asset` |
| `/apps/rap-video/full` | `examples/rap-video/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/rap-video/full.mp4` | `missing_inherited_mp4` |
| `/apps/rap-video/inputs/0/src` | `examples/rap-video/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/rap-video/input-image.jpg` | `present_source_asset` |
| `/apps/rap-video/inputs/0/full` | `examples/rap-video/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/rap-video/input-image-full.jpg` | `present_source_asset` |
| `/apps/recast/card` | `examples/recast/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/recast/card.mp4` | `missing_inherited_mp4` |
| `/apps/recast/poster` | `examples/recast/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/recast/poster.jpg` | `present_source_asset` |
| `/apps/recast/full` | `examples/recast/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/recast/full.mp4` | `missing_inherited_mp4` |
| `/apps/recast/inputs/0/src` | `examples/recast/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/recast/input-clip.jpg` | `present_source_asset` |
| `/apps/recast/inputs/0/full` | `examples/recast/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/recast/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/recast/inputs/1/src` | `examples/recast/input-character.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/recast/input-character.jpg` | `present_source_asset` |
| `/apps/recast/inputs/1/full` | `examples/recast/input-character-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/recast/input-character-full.jpg` | `present_source_asset` |
| `/apps/reframe/card` | `examples/reframe/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reframe/card.mp4` | `missing_inherited_mp4` |
| `/apps/reframe/poster` | `examples/reframe/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reframe/poster.jpg` | `present_source_asset` |
| `/apps/reframe/full` | `examples/reframe/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reframe/full.mp4` | `missing_inherited_mp4` |
| `/apps/reframe/inputs/0/src` | `examples/reframe/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reframe/input-clip.jpg` | `present_source_asset` |
| `/apps/reframe/inputs/0/full` | `examples/reframe/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reframe/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/relight/card` | `examples/relight/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/relight/card.jpg` | `present_source_asset` |
| `/apps/relight/full` | `examples/relight/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/relight/full.jpg` | `present_source_asset` |
| `/apps/relight/inputs/0/src` | `examples/relight/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/relight/input-image.jpg` | `present_source_asset` |
| `/apps/relight/inputs/0/full` | `examples/relight/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/relight/input-image-full.jpg` | `present_source_asset` |
| `/apps/remove-bg/card` | `examples/remove-bg/card.png` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/remove-bg/card.png` | `present_source_asset` |
| `/apps/remove-bg/full` | `examples/remove-bg/full.png` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/remove-bg/full.png` | `present_source_asset` |
| `/apps/remove-bg/inputs/0/src` | `examples/remove-bg/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/remove-bg/input-image.jpg` | `present_source_asset` |
| `/apps/remove-bg/inputs/0/full` | `examples/remove-bg/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/remove-bg/input-image-full.jpg` | `present_source_asset` |
| `/apps/renaissance/card` | `examples/renaissance/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/renaissance/card.jpg` | `present_source_asset` |
| `/apps/renaissance/full` | `examples/renaissance/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/renaissance/full.jpg` | `present_source_asset` |
| `/apps/renaissance/inputs/0/src` | `examples/renaissance/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/renaissance/input-image.jpg` | `present_source_asset` |
| `/apps/renaissance/inputs/0/full` | `examples/renaissance/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/renaissance/input-image-full.jpg` | `present_source_asset` |
| `/apps/render-3d/card` | `examples/render-3d/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/render-3d/card.jpg` | `present_source_asset` |
| `/apps/render-3d/full` | `examples/render-3d/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/render-3d/full.jpg` | `present_source_asset` |
| `/apps/render-3d/inputs/0/src` | `examples/render-3d/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/render-3d/input-image.jpg` | `present_source_asset` |
| `/apps/render-3d/inputs/0/full` | `examples/render-3d/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/render-3d/input-image-full.jpg` | `present_source_asset` |
| `/apps/reshoot/card` | `examples/reshoot/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reshoot/card.mp4` | `missing_inherited_mp4` |
| `/apps/reshoot/poster` | `examples/reshoot/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reshoot/poster.jpg` | `present_source_asset` |
| `/apps/reshoot/full` | `examples/reshoot/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reshoot/full.mp4` | `missing_inherited_mp4` |
| `/apps/reshoot/inputs/0/src` | `examples/reshoot/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reshoot/input-clip.jpg` | `present_source_asset` |
| `/apps/reshoot/inputs/0/full` | `examples/reshoot/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/reshoot/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/roller-coaster/card` | `examples/roller-coaster/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/roller-coaster/card.mp4` | `missing_inherited_mp4` |
| `/apps/roller-coaster/poster` | `examples/roller-coaster/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/roller-coaster/poster.jpg` | `present_source_asset` |
| `/apps/roller-coaster/full` | `examples/roller-coaster/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/roller-coaster/full.mp4` | `missing_inherited_mp4` |
| `/apps/roller-coaster/inputs/0/src` | `examples/roller-coaster/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/roller-coaster/input-image.jpg` | `present_source_asset` |
| `/apps/roller-coaster/inputs/0/full` | `examples/roller-coaster/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/roller-coaster/input-image-full.jpg` | `present_source_asset` |
| `/apps/sdr-hdr/card` | `examples/sdr-hdr/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sdr-hdr/card.mp4` | `missing_inherited_mp4` |
| `/apps/sdr-hdr/poster` | `examples/sdr-hdr/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sdr-hdr/poster.jpg` | `present_source_asset` |
| `/apps/sdr-hdr/full` | `examples/sdr-hdr/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sdr-hdr/full.mp4` | `missing_inherited_mp4` |
| `/apps/sdr-hdr/inputs/0/src` | `examples/sdr-hdr/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sdr-hdr/input-clip.jpg` | `present_source_asset` |
| `/apps/sdr-hdr/inputs/0/full` | `examples/sdr-hdr/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sdr-hdr/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/sfx/card` | `examples/sfx/card.png` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sfx/card.png` | `present_source_asset` |
| `/apps/sfx/full` | `examples/sfx/full.mp3` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sfx/full.mp3` | `present_source_asset` |
| `/apps/shots/card` | `examples/shots/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/shots/card.jpg` | `present_source_asset` |
| `/apps/shots/full` | `examples/shots/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/shots/full.jpg` | `present_source_asset` |
| `/apps/shots/inputs/0/src` | `examples/shots/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/shots/input-image.jpg` | `present_source_asset` |
| `/apps/shots/inputs/0/full` | `examples/shots/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/shots/input-image-full.jpg` | `present_source_asset` |
| `/apps/sketch-to-real/card` | `examples/sketch-to-real/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sketch-to-real/card.jpg` | `present_source_asset` |
| `/apps/sketch-to-real/full` | `examples/sketch-to-real/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sketch-to-real/full.jpg` | `present_source_asset` |
| `/apps/sketch-to-real/inputs/0/src` | `examples/sketch-to-real/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sketch-to-real/input-image.jpg` | `present_source_asset` |
| `/apps/sketch-to-real/inputs/0/full` | `examples/sketch-to-real/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/sketch-to-real/input-image-full.jpg` | `present_source_asset` |
| `/apps/skin-enhancer/card` | `examples/skin-enhancer/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/skin-enhancer/card.jpg` | `present_source_asset` |
| `/apps/skin-enhancer/full` | `examples/skin-enhancer/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/skin-enhancer/full.jpg` | `present_source_asset` |
| `/apps/skin-enhancer/inputs/0/src` | `examples/skin-enhancer/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/skin-enhancer/input-image.jpg` | `present_source_asset` |
| `/apps/skin-enhancer/inputs/0/full` | `examples/skin-enhancer/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/skin-enhancer/input-image-full.jpg` | `present_source_asset` |
| `/apps/smooth/card` | `examples/smooth/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/smooth/card.mp4` | `missing_inherited_mp4` |
| `/apps/smooth/poster` | `examples/smooth/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/smooth/poster.jpg` | `present_source_asset` |
| `/apps/smooth/full` | `examples/smooth/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/smooth/full.mp4` | `missing_inherited_mp4` |
| `/apps/smooth/inputs/0/src` | `examples/smooth/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/smooth/input-clip.jpg` | `present_source_asset` |
| `/apps/smooth/inputs/0/full` | `examples/smooth/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/smooth/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/speak/card` | `examples/speak/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/speak/card.mp4` | `missing_inherited_mp4` |
| `/apps/speak/poster` | `examples/speak/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/speak/poster.jpg` | `present_source_asset` |
| `/apps/speak/full` | `examples/speak/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/speak/full.mp4` | `missing_inherited_mp4` |
| `/apps/speak/inputs/0/src` | `examples/speak/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/speak/input-image.jpg` | `present_source_asset` |
| `/apps/speak/inputs/0/full` | `examples/speak/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/speak/input-image-full.jpg` | `present_source_asset` |
| `/apps/storm-creature/card` | `examples/storm-creature/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/storm-creature/card.mp4` | `missing_inherited_mp4` |
| `/apps/storm-creature/poster` | `examples/storm-creature/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/storm-creature/poster.jpg` | `present_source_asset` |
| `/apps/storm-creature/full` | `examples/storm-creature/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/storm-creature/full.mp4` | `missing_inherited_mp4` |
| `/apps/storm-creature/inputs/0/src` | `examples/storm-creature/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/storm-creature/input-image.jpg` | `present_source_asset` |
| `/apps/storm-creature/inputs/0/full` | `examples/storm-creature/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/storm-creature/input-image-full.jpg` | `present_source_asset` |
| `/apps/style-reference/card` | `examples/style-reference/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-reference/card.jpg` | `present_source_asset` |
| `/apps/style-reference/full` | `examples/style-reference/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-reference/full.jpg` | `present_source_asset` |
| `/apps/style-reference/inputs/0/src` | `examples/style-reference/input-style.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-reference/input-style.jpg` | `present_source_asset` |
| `/apps/style-reference/inputs/0/full` | `examples/style-reference/input-style-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-reference/input-style-full.jpg` | `present_source_asset` |
| `/apps/style-snap/card` | `examples/style-snap/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-snap/card.jpg` | `present_source_asset` |
| `/apps/style-snap/full` | `examples/style-snap/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-snap/full.jpg` | `present_source_asset` |
| `/apps/style-snap/inputs/0/src` | `examples/style-snap/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-snap/input-image.jpg` | `present_source_asset` |
| `/apps/style-snap/inputs/0/full` | `examples/style-snap/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/style-snap/input-image-full.jpg` | `present_source_asset` |
| `/apps/styles/card` | `examples/styles/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/styles/card.jpg` | `present_source_asset` |
| `/apps/styles/full` | `examples/styles/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/styles/full.jpg` | `present_source_asset` |
| `/apps/talking/card` | `examples/talking/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/talking/card.mp4` | `missing_inherited_mp4` |
| `/apps/talking/poster` | `examples/talking/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/talking/poster.jpg` | `present_source_asset` |
| `/apps/talking/full` | `examples/talking/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/talking/full.mp4` | `missing_inherited_mp4` |
| `/apps/talking/inputs/0/src` | `examples/talking/input-portrait.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/talking/input-portrait.jpg` | `present_source_asset` |
| `/apps/talking/inputs/0/full` | `examples/talking/input-portrait-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/talking/input-portrait-full.jpg` | `present_source_asset` |
| `/apps/transitions/card` | `examples/transitions/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/transitions/card.mp4` | `missing_inherited_mp4` |
| `/apps/transitions/poster` | `examples/transitions/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/transitions/poster.jpg` | `present_source_asset` |
| `/apps/transitions/full` | `examples/transitions/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/transitions/full.mp4` | `missing_inherited_mp4` |
| `/apps/transitions/inputs/0/src` | `examples/transitions/input-first.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/transitions/input-first.jpg` | `present_source_asset` |
| `/apps/transitions/inputs/0/full` | `examples/transitions/input-first-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/transitions/input-first-full.jpg` | `present_source_asset` |
| `/apps/transitions/inputs/1/src` | `examples/transitions/input-last.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/transitions/input-last.jpg` | `present_source_asset` |
| `/apps/transitions/inputs/1/full` | `examples/transitions/input-last-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/transitions/input-last-full.jpg` | `present_source_asset` |
| `/apps/truck-ad/card` | `examples/truck-ad/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/truck-ad/card.mp4` | `missing_inherited_mp4` |
| `/apps/truck-ad/poster` | `examples/truck-ad/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/truck-ad/poster.jpg` | `present_source_asset` |
| `/apps/truck-ad/full` | `examples/truck-ad/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/truck-ad/full.mp4` | `missing_inherited_mp4` |
| `/apps/truck-ad/inputs/0/src` | `examples/truck-ad/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/truck-ad/input-image.jpg` | `present_source_asset` |
| `/apps/truck-ad/inputs/0/full` | `examples/truck-ad/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/truck-ad/input-image-full.jpg` | `present_source_asset` |
| `/apps/try-on/card` | `examples/try-on/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/try-on/card.jpg` | `present_source_asset` |
| `/apps/try-on/full` | `examples/try-on/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/try-on/full.jpg` | `present_source_asset` |
| `/apps/try-on/inputs/0/src` | `examples/try-on/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/try-on/input-image.jpg` | `present_source_asset` |
| `/apps/try-on/inputs/0/full` | `examples/try-on/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/try-on/input-image-full.jpg` | `present_source_asset` |
| `/apps/try-on/inputs/1/src` | `examples/try-on/input-image2.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/try-on/input-image2.jpg` | `present_source_asset` |
| `/apps/try-on/inputs/1/full` | `examples/try-on/input-image2-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/try-on/input-image2-full.jpg` | `present_source_asset` |
| `/apps/ugc-shot/card` | `examples/ugc-shot/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ugc-shot/card.jpg` | `present_source_asset` |
| `/apps/ugc-shot/full` | `examples/ugc-shot/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ugc-shot/full.jpg` | `present_source_asset` |
| `/apps/ugc-shot/inputs/0/src` | `examples/ugc-shot/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ugc-shot/input-image.jpg` | `present_source_asset` |
| `/apps/ugc-shot/inputs/0/full` | `examples/ugc-shot/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/ugc-shot/input-image-full.jpg` | `present_source_asset` |
| `/apps/upscale/card` | `examples/upscale/card.png` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale/card.png` | `present_source_asset` |
| `/apps/upscale/full` | `examples/upscale/full.png` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale/full.png` | `present_source_asset` |
| `/apps/upscale/inputs/0/src` | `examples/upscale/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale/input-image.jpg` | `present_source_asset` |
| `/apps/upscale/inputs/0/full` | `examples/upscale/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale/input-image-full.jpg` | `present_source_asset` |
| `/apps/upscale-video/card` | `examples/upscale-video/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale-video/card.mp4` | `missing_inherited_mp4` |
| `/apps/upscale-video/poster` | `examples/upscale-video/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale-video/poster.jpg` | `present_source_asset` |
| `/apps/upscale-video/full` | `examples/upscale-video/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale-video/full.mp4` | `missing_inherited_mp4` |
| `/apps/upscale-video/inputs/0/src` | `examples/upscale-video/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale-video/input-clip.jpg` | `present_source_asset` |
| `/apps/upscale-video/inputs/0/full` | `examples/upscale-video/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/upscale-video/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/vfx-clean-plate/card` | `examples/vfx-clean-plate/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-clean-plate/card.mp4` | `missing_inherited_mp4` |
| `/apps/vfx-clean-plate/poster` | `examples/vfx-clean-plate/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-clean-plate/poster.jpg` | `present_source_asset` |
| `/apps/vfx-clean-plate/full` | `examples/vfx-clean-plate/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-clean-plate/full.mp4` | `missing_inherited_mp4` |
| `/apps/vfx-clean-plate/inputs/0/src` | `examples/vfx-clean-plate/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-clean-plate/input-clip.jpg` | `present_source_asset` |
| `/apps/vfx-clean-plate/inputs/0/full` | `examples/vfx-clean-plate/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-clean-plate/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/vfx-day-to-night/card` | `examples/vfx-day-to-night/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-day-to-night/card.mp4` | `missing_inherited_mp4` |
| `/apps/vfx-day-to-night/poster` | `examples/vfx-day-to-night/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-day-to-night/poster.jpg` | `present_source_asset` |
| `/apps/vfx-day-to-night/full` | `examples/vfx-day-to-night/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-day-to-night/full.mp4` | `missing_inherited_mp4` |
| `/apps/vfx-day-to-night/inputs/0/src` | `examples/vfx-day-to-night/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-day-to-night/input-clip.jpg` | `present_source_asset` |
| `/apps/vfx-day-to-night/inputs/0/full` | `examples/vfx-day-to-night/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-day-to-night/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/vfx-water/card` | `examples/vfx-water/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-water/card.mp4` | `missing_inherited_mp4` |
| `/apps/vfx-water/poster` | `examples/vfx-water/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-water/poster.jpg` | `present_source_asset` |
| `/apps/vfx-water/full` | `examples/vfx-water/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-water/full.mp4` | `missing_inherited_mp4` |
| `/apps/vfx-water/inputs/0/src` | `examples/vfx-water/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-water/input-clip.jpg` | `present_source_asset` |
| `/apps/vfx-water/inputs/0/full` | `examples/vfx-water/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/vfx-water/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/victory-card/card` | `examples/victory-card/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/victory-card/card.jpg` | `present_source_asset` |
| `/apps/victory-card/full` | `examples/victory-card/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/victory-card/full.jpg` | `present_source_asset` |
| `/apps/victory-card/inputs/0/src` | `examples/victory-card/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/victory-card/input-image.jpg` | `present_source_asset` |
| `/apps/victory-card/inputs/0/full` | `examples/victory-card/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/victory-card/input-image-full.jpg` | `present_source_asset` |
| `/apps/video/card` | `examples/video/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video/card.mp4` | `missing_inherited_mp4` |
| `/apps/video/poster` | `examples/video/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video/poster.jpg` | `present_source_asset` |
| `/apps/video/full` | `examples/video/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video/full.mp4` | `missing_inherited_mp4` |
| `/apps/video/inputs/0/src` | `examples/video/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video/input-image.jpg` | `present_source_asset` |
| `/apps/video/inputs/0/full` | `examples/video/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video/input-image-full.jpg` | `present_source_asset` |
| `/apps/video-remove-bg/card` | `examples/video-remove-bg/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-remove-bg/card.mp4` | `missing_inherited_mp4` |
| `/apps/video-remove-bg/poster` | `examples/video-remove-bg/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-remove-bg/poster.jpg` | `present_source_asset` |
| `/apps/video-remove-bg/full` | `examples/video-remove-bg/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-remove-bg/full.mp4` | `missing_inherited_mp4` |
| `/apps/video-remove-bg/inputs/0/src` | `examples/video-remove-bg/input-clip.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-remove-bg/input-clip.jpg` | `present_source_asset` |
| `/apps/video-remove-bg/inputs/0/full` | `examples/video-remove-bg/input-clip-full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-remove-bg/input-clip-full.mp4` | `missing_inherited_mp4` |
| `/apps/video-t2v/card` | `examples/video-t2v/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-t2v/card.mp4` | `missing_inherited_mp4` |
| `/apps/video-t2v/poster` | `examples/video-t2v/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-t2v/poster.jpg` | `present_source_asset` |
| `/apps/video-t2v/full` | `examples/video-t2v/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/video-t2v/full.mp4` | `missing_inherited_mp4` |
| `/apps/volcano-ad/card` | `examples/volcano-ad/card.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/volcano-ad/card.mp4` | `missing_inherited_mp4` |
| `/apps/volcano-ad/poster` | `examples/volcano-ad/poster.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/volcano-ad/poster.jpg` | `present_source_asset` |
| `/apps/volcano-ad/full` | `examples/volcano-ad/full.mp4` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/volcano-ad/full.mp4` | `missing_inherited_mp4` |
| `/apps/volcano-ad/inputs/0/src` | `examples/volcano-ad/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/volcano-ad/input-image.jpg` | `present_source_asset` |
| `/apps/volcano-ad/inputs/0/full` | `examples/volcano-ad/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/volcano-ad/input-image-full.jpg` | `present_source_asset` |
| `/apps/whats-next/card` | `examples/whats-next/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/whats-next/card.jpg` | `present_source_asset` |
| `/apps/whats-next/full` | `examples/whats-next/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/whats-next/full.jpg` | `present_source_asset` |
| `/apps/whats-next/inputs/0/src` | `examples/whats-next/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/whats-next/input-image.jpg` | `present_source_asset` |
| `/apps/whats-next/inputs/0/full` | `examples/whats-next/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/whats-next/input-image-full.jpg` | `present_source_asset` |
| `/apps/z-image/card` | `examples/z-image/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/z-image/card.jpg` | `present_source_asset` |
| `/apps/z-image/full` | `examples/z-image/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/z-image/full.jpg` | `present_source_asset` |
| `/apps/zooms/card` | `examples/zooms/card.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/zooms/card.jpg` | `present_source_asset` |
| `/apps/zooms/full` | `examples/zooms/full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/zooms/full.jpg` | `present_source_asset` |
| `/apps/zooms/inputs/0/src` | `examples/zooms/input-image.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/zooms/input-image.jpg` | `present_source_asset` |
| `/apps/zooms/inputs/0/full` | `examples/zooms/input-image-full.jpg` | `AnalyseFuture/references/workflow-studio/freefield/web/examples/zooms/input-image-full.jpg` | `present_source_asset` |

## Independent-review limits

This review read all 118 manifest records and all 643 path occurrences in the
original index, inspected the server load/merge code and media consumption code,
and counted existing source files. It did not launch the UI, make network requests,
decode videos/images, verify external lab claims, audit all upstream source lines,
or establish redistribution rights. A complete static path match is not a test
of generated media, model execution, voice quality or product functionality.
