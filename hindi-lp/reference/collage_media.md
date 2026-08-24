# Collage media — several frames in one phase-2 image slot

> **Extended to classes 8, 9 and 10 on 2026-08-10.** Previously only classes 6 and 7 collaged;
> 8, 9 and 10 attached exactly one frame per topic while 600+ frames sat idle in their pools.
> 289 composites now cover every image-bearing topic in those three grades, all verified live.
> See *The shared builder* and *As shipped* below.

Phase 2 gives each topic **one** image (`M{m}.S{s}.T{t}.C{c}.IMG1`). A topic often has two or
three visual beats. Rather than pick one frame and waste the rest, the frames that belong to
that topic are composited into a single picture that reads in story order.

This fits phase 2 better than it fitted LP v1. v1 gave a topic two slots, so a collage competed
with a second picture; phase 2's single slot is exactly what a numbered composite is for.

## Why the v1 collages could not simply be reused

`imagebyGPT/doc/HINDI6_V3.md` describes 16 collages built for LP v1 (6 for ch1, 10 for ch2 —
the v3 build never ran further). They are live, and they are the wrong shape for phase 2:

| | built v3 | phase-2 plan |
|---|---|---|
| ch1 | 4 topics | 10 topics |
| ch2 | 11 topics | 13 topics |

v3's `M1.S1.T1.O1.E1` is a 4-panel collage covering *हिमालय और पवित्र नदियों का वैभव*. In the
phase-2 cut that is **two** topics — `M1.S2.T2` (हिमालय/सिंधु) and `M1.S2.T3` (गंगा/यमुन/त्रिवेणी).
One collage straddles two topics, so attaching it to either shows the child pictures for a छंद
they have not read. They were also 5–14 MB each, and their filenames embed v1 objective ids
(`.O1.E1`) that phase 2 does not have.

**Rule: never reuse a composite built against a different topic cut.** Recompose from frames.

## The panel list is authored, never scored

`output/<chapter>/_collage.json` maps `topic_id` → panels **in reading order**, each with the
frame's v1 title quoted so the choice is checkable without opening images:

```jsonc
"M2.S4.T8": {
  "why": "छंद अपने ही क्रम में — रघुपति और सीता, फिर वंशी, फिर गीता",
  "panels": [["scene_02_img_02", "राम, सीता और कृष्ण"],
             ["scene_10_img_02", "श्रीकृष्ण की बांसुरी"],
             ["scene_10_img_04", "गीता का उपदेश"]]}
```

Scoring a chapter-wide pool has failed twice and both failures are in the record: ch2's
डाँडी-गोथा topics were handed hockey-brawl frames, and stanza 5 was handed the frames drawn for
stanza 4. The `scene_NN_img_MM` clock is the reliable order — **and even it has exceptions.**
ch1's रघुपति stanza takes its first panel from `scene_02` because that is simply where the
राम-सीता picture is. An authored list absorbs that; a rule cannot.

2–3 panels is the working band. `PANEL_MAX` is 4; beyond that panels are too small to read.

## The output path bug — check it before believing a build succeeded

**`output/_build_collages.py` (class 6) and `output7/_build_collages7.py` (class 7) both resolve**

```python
LP_DATA = os.path.abspath(os.path.join(HERE, "..", "..", "learning_plan_upload", "data"))
```

**which is `lp-pipeline/learning_plan_upload` — a directory that does not exist.** The checkout
sits *beside* `lp-pipeline`, not inside it. Nothing errors: `os.makedirs` creates the phantom
tree, every composite is written into it, the build prints its usual success table, and lp_sync
later finds no images because it is looking in the real tree. This is the identical
one-directory-too-shallow mistake `output5/_stage_assets.py` documents in its own header, and it
bit again on the class-3 build (2026-08-14, caught only because a composed file was opened and
turned out to be a single 2048×1152 frame — the staged anchor, untouched).

`output3/_build_collages3.py` fixes it by **searching upward for the checkout's `run.py`** rather
than assuming a depth, which is what `_stage_assets.py` already does. Copy that resolver; do not
copy the two-dots line.

**The two older scripts still carry the bug.** They are left as they are because classes 6 and 7
already shipped and may have been built on a layout where the shallow path was right — but on
this layout they are wrong, and a re-run would silently produce nothing. Fix them before any
re-run: it is one function.

**Cheap check after any collage build:** open one composed file. A real collage is ~1148 px wide
and 2–4 panels tall with Devanagari ordinal badges. If it is 2048×1152, you are looking at a
single frame and the build wrote somewhere else.

## Composition rules, inherited and non-negotiable

* **Letterbox, never crop.** Every frame carries a light-yellow narrator bar along its bottom.
  Cropping to a common aspect ratio cuts the caption off.
* **Devanagari ordinal badges (१ २ ३ ४).** A 2×2 grid has no reading order without them.
* **Downscale before compositing.** `PANEL_W = 1100`. The v1 collages went up at 5–14 MB
  because panels were pasted at native 2048×1152. At 1100 the narrator bar still reads and a
  2-panel stack lands near 2.4 MB — in line with the ~2–2.9 MB the platform's other V2 images
  already run at.

Verify margins after a run: the outer `MARGIN` rows/columns must be pure white (luminance 255).
If they are not, something cropped.

## Where the files go — and why this cannot repeat 4 Aug

```
learning_plan_upload/data/V2/cbse/cbse/english/class_6/hindi/ch_<N>/image/<media_id>.png
        ↓  POST /api/topics/upload, bucket=learning_plan_assets
https://media.singularity-learn.com/learning_plan_assets/V2/.../ch_<N>/image/<media_id>.png
```

That is lp_sync's own tree (`V2/board/publication/medium/class_N/subject/ch_N`, validated in
`lp_sync/scanner.py`) and phase 2's own bucket. **It holds nothing from LP v1.** The 4 Aug
incident — six live images destroyed, bucket versioning off, no generation to roll back to —
happened because a build wrote onto an id-based path inside v1's `topic-content-images`.
Nothing in this pipeline can reach that bucket: it only ever *reads* frames from it.

The medium segment is `english` (the server reports medium `eng` for these chapters) and the
subject segment is `hindi`, matching both the existing V2 tree and v1's `Grade_6/english/hindi/`
CDN layout — not the `hin` that appears inside the chapter_id.

**Write the URL the server returned, never one you built.** `_upload_collages.py` records each
`publicUrl` in `_collage_urls.json` and `_build_collages.py --repoint` reads from there; a
hand-built CDN string is a guess.

## Runbook

Classes 6 and 7 each have their own scripts (below). Classes 8, 9 and 10 share one implementation
in `lib/` behind a per-class wrapper — see *The shared builder* further down.

```bash
cd hindi-learning-plan/output
python _frame_sheet.py ch04              # topics + anchors + the chapter's frames, in clock order
#   author output/ch04/_collage.json from that sheet
python _build_collages.py ch04           # compose + collage_review.html — nothing uploaded
#   open output/ch04/collage_review.html — topic text beside each composite
python _upload_collages.py ch04 --dry-run    # confirm target path
python _upload_collages.py ch04              # -> learning_plan_assets, records real publicUrls
python _rebuild_all.py                       # every builder re-runs; overlay is picked up
python _reupload_bhasha_bodh.py ch04         # validate both orderings + upload (force=True)
python _verify_collages.py ch04              # read the plan back, fetch every image
```

For classes 8, 9 and 10 the same five steps are one script each, and the chapter argument is
optional (omit it to do every chapter that has a `_collage.json`):

```bash
cd hindi-learning-plan/output9
python _build_collages9.py --sheet ch06      # topics + anchor frames + the whole frame pool
python _build_collages9.py --seed  ch06      # starting _collage.json from the anchors — see below
#   author output9/ch06/_collage.json from the sheet
python _build_collages9.py         ch06      # compose + collage_review.html — nothing uploaded
python _upload_collages9.py --dry-run        # confirm the exact file list
python _upload_collages9.py                  # -> learning_plan_assets, records real publicUrls
python _patch_collages9.py --dry-run         # full before/after for every live media
python _patch_collages9.py                   # patch the LIVE plans in place
python _build_collages9.py --repoint --no-compose   # bring the repo's own copies in line
python _verify_collages9.py                  # read live back, five checks per collage
```

Class 10 needs `python _pull_images10.py` once before any of this — its frame pool is built from
the cached v1 plans in `output10/v1/` rather than fetched.

### `--seed` — the anchor frame is already known

Classes 8, 9 and 10 all shipped one frame per topic and recorded which one in the media's
`teaching_notes` as `[reused frame: M1.S1.T2.O1.E4, V2 copy]`. `--seed` reads that stamp and
writes a `_collage.json` with it as panel 1 of every topic, so the authoring pass **adds** the
beats a topic was missing instead of re-deriving the one already chosen and verified. It is a
starting point, not an answer: the `why` fields come back empty and the panel order still has to
be decided against the topic's own text.

`_build_collages.py --repoint --no-compose` still exists for patching an already-built plan in
place, and it writes **both** orderings. It is no longer the normal path — see below.

## The overlay lives in the assembler

`assemble.load_collages()` reads `_collage.json` + `_collage_urls.json` from the chapter folder
and `emit()` applies it, so **re-running `content.py` keeps the collage URLs**. `build_ch01.py`
(the pilot's bespoke builder) imports the same function.

Both files are required and must agree. A topic with authored panels whose image has not been
uploaded is skipped with a warning and keeps its single anchor frame — a half-applied overlay
is worse than none.

## Two guards that have already caught mistakes

`_build_collages.py` refuses to run if either holds:

* **A topic with an image has no panels authored.** Silent single frames in an otherwise
  collaged chapter look like an oversight because they are one.
* **A topic that is image-free by design has panels authored.** ch2's four डाँडी-गोथा topics,
  ch8's लेखिका-परिचय and मूँगा-सिल्क topics, and ch13's लेखक-परिचय have no relevant frame in
  their chapter at all. Giving them one would quietly undo a deliberate decision.

The first guard also caught two mistyped module numbers in ch11's authored file
(`M1.S3.T5` for `M2.S3.T5`), which would otherwise have produced a chapter silently missing
two collages.

## The shared builder — classes 8, 9 and 10

Classes 6 and 7 are two copies of one algorithm differing in three places: how a panel name
resolves to a URL, where the chapter directory lives, and how the grade is discovered. Classes
8–10 would have made it five copies, so the algorithm moved to `lib/` and the per-class scripts
became argument lists:

| | |
|---|---|
| `lib/collage.py` | the compositor — letterbox, badges, downscale. Unchanged, shared by all five classes |
| `lib/collage_build.py` | guards, anchor parsing, compose loop, review sheet, `--repoint` |
| `lib/collage_cli.py` | the `--sheet` / `--seed` / build command line |
| `lib/collage_upload.py` | uploads a **named list**, never a folder glob |
| `lib/collage_patch.py` | fetches the live plan, edits two fields, puts it back |
| `lib/collage_verify.py` | five checks per collage against what is actually live |

`output/_build_collages.py` and `output7/_build_collages7.py` were deliberately left alone. They
are shipped and verified; rewriting them to prove a refactor is how a working chapter breaks.

Two things the shared code does that the class-6/7 scripts do not:

* **Panel names resolve through `_images.json` for every class.** Class 10's pool is keyed by the
  `scene_NN_img_MM` stem (its frames sit in one flat folder, like class 6); classes 8 and 9 are
  keyed by v1 media id (their CDN path embeds the old cut's module/segment, so one chapter spans
  several folders). `_pull_images10.py` builds class 10's pool from `output10/v1/`.
* **The uploader takes a named list, not a glob.** On 2026-08-10 another build staged class-10
  ch1/ch11/ch13 into the same `learning_plan_upload/data` tree while this work was in progress. A
  `*.png` glob would have published someone else's in-flight assets. The file list now comes from
  each chapter's `_collage.json`, and anything else in the folder is reported and left alone.

### Why the live plans are patched rather than re-uploaded

For nine of ten class-8 chapters — and class-10 ch8 — the plan this repo builds is **not** the
live plan: a v2 carrying a video per topic was uploaded on 2026-08-07 and is the active one.
`_patch_collages*.py` therefore fetches whatever is live and edits only what a collage changes:

* `aspect_ratio` — 3:4 for a 2-panel stack, 9:16 for 3, 1:1 for a 2×2 grid. Left at 16:9 the
  player letterboxes a tall image into a wide box and the panels stop being readable.
* `teaching_notes` — the `[reused frame: …]` stamp becomes the panel sentence plus
  `[collage of: …]`, keeping the authored teacher-facing sentence in front of it.
* `image_url` — **not touched.** The composite went to the same media-id path the plan already
  pointed at, so the URL is right by construction and a half-finished run still leaves every
  live plan pointing at a valid image.

All 66 class-8 videos were confirmed present after the patch.

## As shipped — classes 6 to 10

| class | chapters | composites | panels | distribution | avg size |
|---|---|---|---|---|---|
| 6 | 13 | 125 | 303 | 75×2p · 44×3p · 5×4p · 1 single | ~2.7 MB |
| 7 | 10 | 94 | 219 | 54×2p · 28×3p · 5×4p · 7 single | ~2.6 MB |
| 8 | 10 | 79 | 208 | 30×2p · 48×3p · 1×4p | ~2.7 MB |
| 9 | 11 | 127 | 308 | 50×2p · 64×3p · 1×4p · 12 single | ~2.6 MB |
| 10 | 10 | 83 | 206 | 43×2p · 37×3p · 2×4p · 1 single | ~2.9 MB |
| **total** | **54** | **508** | **1244** | | |

Class 6's single-panel case is ch10's `M1.S2.T6` — the एक-वाक्य topic *"इन बगुलों में हंस कहाँ
छिपा हुआ है"*. One sentence, one picture, no badge.

The 12 singles in class 9 are almost all in ch11 (झाँसी की रानी) and ch12 (घर की याद), and they
are a pool problem rather than a choice: 31 frames for 19 छंद and 30 for 17. Where a छंद has
only one picture in the whole chapter it gets that one picture. **"Collage when it is possible"
is the rule, not "collage always"** — a topic padded with a near-duplicate frame reads worse than
a single honest one, and each of those singles carries its reason in the `why` field.

### Where a four-panel grid earns its place

`PANEL_MAX` is 4 and the working band is still 2–3, but four is right when the topic is itself an
enumeration the child is meant to count:

* class 8 ch9 `M2.S2.T3` — *आदमी का अनुपात*'s ladder: घर → मुहल्ला → नगर → पृथ्वी.
* class 9 ch8 `M1.S1.T2` — रैदास's chain of उपमाएँ: चंदन-पानी, घन-मोर, चंद-चकोर, दीपक-बाती.
* class 10 ch12 `M3.S4.T9` and `M3.S4.T11` — both निबंध anecdotes whose fourth beat *is* the
  conclusion (माँ's day-long रोज़ा; the silent pigeon behind the new wire mesh).

### Not covered

| | why |
|---|---|
| class 8 — 25 topics | `image_url` empty; authored `generation_prompt` awaiting a generation pass |
| class 9 — 31 topics, incl. all 16 of ch4 | same, and ch4 (लता मंगेशकर साक्षात्कार) has no frame pool at all |
| class 10 — ch1, ch10, ch11, ch13 | not cut yet; ch1/ch11/ch13 were being built by another process on 2026-08-10 |

Counts and the full worklist live in `EMPTY_IMAGE_URLS_class6_to_10.md`.
