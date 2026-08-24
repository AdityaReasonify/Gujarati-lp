# Collage media — several frames in one phase-2 image slot

> **⚠ DORMANT — this whole workflow is inactive for gujarati-lp until a Gujarati frame pool exists.**
> There is no v1 Gujarati plan corpus, no rendered frame library, and therefore nothing to
> composite. Agent 9 authors a `generation_prompt` per scene and leaves `image_url: ""`; its
> `reuse_report` is emitted with `reused: 0` and `rejected: []`. Nothing in this file may be run,
> and no `_collage.json` may be authored, before a pool of generated frames exists per chapter.
> The document is kept **as doctrine**: it is the accumulated method — what to author, what to
> check, what never to do — so that the first Gujarati collage pass starts from the finished
> discipline instead of rediscovering it. Every path, id and DB segment below that is marked
> VERIFY-2-pending must be resolved against the live server before the first upload.

Phase 2 gives each topic **one** image (`M{m}.S{s}.T{t}.C{c}.IMG1`). A topic often has two or
three visual beats — a કડી that turns twice, an ઘટના with a before and an after. Rather than pick
one frame and waste the rest, the frames that belong to that topic are composited into a single
picture that reads in story order.

This fits phase 2 better than it fitted LP v1. v1 gave a topic two slots, so a collage competed
with a second picture; phase 2's single slot is exactly what a numbered composite is for.

## Why the workflow is dormant, and what would wake it

| precondition | state |
|---|---|
| a per-chapter frame pool (generated images with stems and titles) | does not exist |
| `[reused frame: …]` stamps in `teaching_notes` to seed panel 1 from | do not exist — nothing has shipped |
| asset-path segments for the V2 tree | VERIFY-2 pending |
| narrator-bar convention confirmed on Gujarati frames | unverified — letterboxing depends on it |
| Gujarati digits present in the compositor's badge font | unverified — check before the first build |

Until the first row is true, the correct output of Agent 9 is an authored prompt and an empty
`image_url`; the worklist of empty slots lives in `EMPTY_IMAGE_URLS_class6_to_10.md`.

**Rule that survives dormancy: never reuse a composite built against a different topic cut.**
A composite is bound to the cut it was authored for. If the cut changes — a કડી that was one topic
becomes two, a પદ that was split gets joined back — the old composite straddles the new boundary
and shows the child pictures for lines they have not read yet. Recompose from frames; never
re-point a stale composite. The same holds for any composite inherited from another pipeline
generation: its filename may embed ids this pack does not have, and its panel boundaries were
decided against someone else's topics.

## The panel list is authored, never scored

`output{N}/<chapter>/_collage.json` maps `topic_id` → panels **in reading order**, each with the
frame's own title quoted so the choice is checkable without opening images:

```jsonc
"M2.S4.T8": {
  "why": "કડીના પોતાના ક્રમમાં — પહેલાં નદીકાંઠે સવાર, પછી હોડી, પછી સામે કાંઠે દીવો",
  "panels": [["scene_02_img_02", "નદીકાંઠે સવાર"],
             ["scene_05_img_01", "હોડી હંકારતો નાવિક"],
             ["scene_05_img_03", "સામે કાંઠે દીવો"]]}
```

`why` is written in Gujarati, one line, and says why *these* panels in *this* order. It is the
only part of the file a reviewer can check without opening a single image, so it must name the
beats, not restate the topic.

**Automatic selection is not an option.** Scoring a chapter-wide pool against topic text has
failed repeatedly in the pack this ports from: topics were handed frames drawn for an unrelated
episode, and one stanza was handed the frames drawn for the stanza before it. The failure is not a
tuning problem — a scorer has no way to know that a picture drawn early in a chapter is the only
one that shows a character who matters late.

Frame stems carry a clock (`scene_NN_img_MM`) and that clock is the reliable *default* order —
**and even it has exceptions.** A stanza's first panel may legitimately come from a much earlier
scene because that is simply where the needed picture is. An authored list absorbs that; a rule
cannot.

2–3 panels is the working band. `PANEL_MAX` is 4; beyond that panels are too small to read.

## The output path bug — check it before believing a build succeeded

The single most expensive mistake in this tooling family is a builder that resolves its output
directory by counting `..` segments:

```python
LP_DATA = os.path.abspath(os.path.join(HERE, "..", "..", "learning_plan_upload", "data"))
```

If the checkout sits *beside* `lp-pipeline` rather than inside it, that path does not exist —
and **nothing errors**. `os.makedirs` creates the phantom tree, every composite is written into
it, the build prints its usual success table, and the sync step later finds no images because it
is looking in the real tree. The identical one-directory-too-shallow mistake has bitten more than
one script in the pack this ports from, and was caught only because someone opened a composed file
and found a single untouched frame.

**Resolve by searching upward for the checkout's `run.py`, never by assuming a depth.** The
Gujarati builders (`output6/_build_collages6.py` … `output10/_build_collages10.py`) must use the
upward-search resolver from the start; there are no legacy copies in this pack to protect, so
there is no reason for a hard-coded depth to exist anywhere.

**Cheap check after any collage build:** open one composed file. A real collage is ~1148 px wide
and 2–4 panels tall with Gujarati ordinal badges. If it is a single un-badged frame at the pool's
native size, you are looking at a source frame and the build wrote somewhere else.

## Composition rules, inherited and non-negotiable

* **Letterbox, never crop.** Frames carry a light narrator bar along the bottom holding one line
  of Gujarati. Cropping to a common aspect ratio cuts the caption off. *Confirm the Gujarati
  frames actually carry that bar before the first build* — the rule is inherited from a pool that
  had one, and letterboxing is only obviously right when there is a caption to protect.
* **Gujarati ordinal badges (૧ ૨ ૩ ૪).** A 2×2 grid has no reading order without them. Devanagari
  digits must not appear — they are as wrong here as Devanagari in `original_chunk`. Verify that
  the compositor's badge font actually contains U+0AE7–U+0AEA before the first run; a missing
  glyph renders as a box and silently ships an unreadable badge.
* **Downscale before compositing.** `PANEL_W = 1100`. Pasting panels at their native generated
  size produces 5–14 MB composites. At 1100 the narrator bar still reads and a 2-panel stack lands
  near 2.4 MB — in line with the ~2–2.9 MB the platform's other V2 images already run at.

Verify margins after a run: the outer `MARGIN` rows/columns must be pure white (luminance 255).
If they are not, something cropped.

## Where the files go

```
learning_plan_upload/data/V2/{board}/{publication}/{medium}/class_{N}/gujarati/ch_<n>/image/<media_id>.png
        ↓  POST /api/topics/upload, bucket=learning_plan_assets
https://media.singularity-learn.com/learning_plan_assets/V2/.../ch_<n>/image/<media_id>.png
```

That is the sync tool's own tree (`V2/board/publication/medium/class_N/subject/ch_N`) and phase 2's
own bucket.

> **⚠ VERIFY-2 pending — every segment except `class_{N}`, `gujarati` and `image` is unresolved.**
> `{board}`, `{publication}` and `{medium}` must come from the GSEB DB rows and a post-upload
> readback, never from analogy. **Do not assume the Hindi pack's `english` medium folder** — that
> was a verified quirk of that corpus (its server reported medium `eng` while its `chapter_id`
> carried `hin`), and precedents show the slot varies by board. Resolve it once, record it in
> `profiles/boards/gseb_gujarati.md`, and let every other file read it from there.

**The bucket holds nothing from any v1 pipeline, and nothing here may ever write to one.** This
pipeline only ever *reads* frames from a v1 bucket. The rule exists because it has already been
broken once elsewhere: a build wrote onto an id-based path inside a v1 bucket that had versioning
switched off, live images were overwritten, and there was no generation to roll back to. Read-only
from v1, write-only to `learning_plan_assets`.

**Write the URL the server returned, never one you built.** The uploader records each `publicUrl`
in `_collage_urls.json` and `--repoint` reads from there; a hand-built CDN string is a guess that
looks like a fact.

## Runbook (dormant — do not run before a frame pool exists)

Every standard shares one implementation in `lib/` behind a per-standard wrapper. The chapter
argument is optional; omit it to do every chapter that has a `_collage.json`.

```bash
cd gujarati-learning-plan/output9
python _build_collages9.py --sheet ch06      # topics + anchor frames + the whole frame pool
python _build_collages9.py --seed  ch06      # starting _collage.json from the anchors — see below
#   author output9/ch06/_collage.json from the sheet
python _build_collages9.py         ch06      # compose + collage_review.html — nothing uploaded
#   open output9/ch06/collage_review.html — topic text beside each composite
python _upload_collages9.py --dry-run        # confirm the exact file list
python _upload_collages9.py                  # -> learning_plan_assets, records real publicUrls
python _patch_collages9.py --dry-run         # full before/after for every live media
python _patch_collages9.py                   # patch the LIVE plans in place
python _build_collages9.py --repoint --no-compose   # bring the repo's own copies in line
python _verify_collages9.py                  # read live back, five checks per collage
```

The review sheet is not optional. A composite is judged against the topic's own text, side by
side; a panel list that reads fine in JSON can still show the wrong beat.

### `--seed` — unavailable until something has shipped

`--seed` reads the `[reused frame: M1.S1.T2.O1.E4, V2 copy]` stamp a shipped media carries in its
`teaching_notes` and writes a `_collage.json` with that frame as panel 1 of every topic, so the
authoring pass **adds** the beats a topic was missing instead of re-deriving the one already chosen
and verified.

**No Gujarati plan has shipped, so no stamp exists and `--seed` has nothing to read.** It becomes
available only after a first generation-and-upload pass. When it does: it is a starting point, not
an answer — the `why` fields come back empty and the panel order still has to be decided against
the topic's own text.

The bracketed stamps `[reused frame: …]` and `[collage of: …]` stay **English inside the brackets**
even though the surrounding `teaching_notes` sentence is Gujarati. The tooling parses them with
regexes; translating them breaks seeding and patching.

## The overlay lives in the assembler

`assemble.load_collages()` reads `_collage.json` + `_collage_urls.json` from the chapter folder and
`emit()` applies it, so **re-running the content build keeps the collage URLs**.

Both files are required and must agree. A topic with authored panels whose image has not been
uploaded is skipped with a warning and keeps its single anchor frame — a half-applied overlay is
worse than none, because it looks finished.

## Two guards that pay for themselves

The builder refuses to run if either holds:

* **A topic with an image has no panels authored.** Silent single frames in an otherwise collaged
  chapter look like an oversight because they usually are one.
* **A topic that is image-free by design has panels authored.** Some topics have no relevant frame
  in their chapter at all — an author-introduction scene, a purely language-study passage, a topic
  whose content is a list rather than a picture. Giving them one quietly undoes a deliberate
  decision made upstream by Agent 9.

The first guard is also the only thing that catches a mistyped module number in an authored file
(`M1.S3.T5` written for `M2.S3.T5`), which otherwise produces a chapter silently missing a collage.

## The shared builder

The algorithm lives in `lib/` and the per-standard scripts are argument lists. Two copies of one
algorithm diverge in exactly three places — how a panel name resolves to a URL, where the chapter
directory lives, and how the grade is discovered — so five copies were never written:

| | |
|---|---|
| `lib/collage.py` | the compositor — letterbox, badges (૧ ૨ ૩ ૪), downscale |
| `lib/collage_build.py` | guards, anchor parsing, compose loop, review sheet, `--repoint` |
| `lib/collage_cli.py` | the `--sheet` / `--seed` / build command line |
| `lib/collage_upload.py` | uploads a **named list**, never a folder glob |
| `lib/collage_patch.py` | fetches the live plan, edits two fields, puts it back |
| `lib/collage_verify.py` | five checks per collage against what is actually live |

Two properties of the shared code that a per-class script tends to lose:

* **Panel names resolve through `_images.json`, per standard.** A pool may be keyed by the
  `scene_NN_img_MM` stem (flat folder) or by media id (CDN path embeds an older cut's
  module/segment, so one chapter spans several folders). The resolver is a pool property, not a
  build-time assumption — record which form each Gujarati pool uses when it is built.
* **The uploader takes a named list, not a glob.** A `*.png` glob publishes whatever else happens
  to be staged in the same tree — including another process's in-flight assets. The file list comes
  from each chapter's `_collage.json`; anything else in the folder is reported and left alone.

### Why the live plans are patched rather than re-uploaded

Once a plan is live, the plan this repo builds may no longer be the live plan — a later version
carrying different media can have been uploaded over it. Re-uploading the repo's copy would
silently revert that. `_patch_collages*.py` therefore fetches whatever is live and edits only what
a collage actually changes:

* `aspect_ratio` — **3:4 for a 2-panel stack, 9:16 for 3, 1:1 for a 2×2 grid.** Left at 16:9 the
  player letterboxes a tall image into a wide box and the panels stop being readable.
* `teaching_notes` — the `[reused frame: …]` stamp becomes the panel sentence plus
  `[collage of: …]`, keeping the authored teacher-facing Gujarati sentence in front of it.
* `image_url` — **not touched.** The composite goes to the same media-id path the plan already
  points at, so the URL is right by construction and a half-finished run still leaves every live
  plan pointing at a valid image.

Confirm after any patch that nothing else moved: other media types on the same topics must still
be present and unchanged.

## Collage when it is possible, not collage always

Where a topic has only one picture in the whole chapter, it gets that one picture — a single panel,
no badge. A topic padded with a near-duplicate frame reads worse than a single honest one. Each
single carries its reason in its `why` field, in Gujarati, so a reviewer can tell a deliberate
single from a forgotten one.

Pool size, not authoring effort, decides how many singles a chapter has. A pool with barely more
frames than the chapter has કડી will produce singles no matter how well the panels are authored;
that is a generation-pass gap to record, not a collage failure to fix.

### Where a four-panel grid earns its place

`PANEL_MAX` is 4 and the working band is still 2–3, but four is right when the topic is itself an
enumeration the child is meant to count:

* a કડી built as a widening ladder — ઘર → શેરી → ગામ → ધરતી — where losing a rung loses the poem's
  movement;
* a chain of ઉપમાઓ, each a separate picture, where the point is that they keep coming;
* a ગદ્ય anecdote whose fourth beat *is* the conclusion, so a three-panel version stops before the
  turn.

If the fourth panel is there because a fourth good frame existed, it does not earn its place.

## Gaps

Counts and the full worklist of empty image slots live in `EMPTY_IMAGE_URLS_class6_to_10.md`,
generated by `_empty_images_report.py`. Until a frame pool exists, every image-bearing topic in
std 6–10 appears there with an authored `generation_prompt` and an empty `image_url` — that is the
expected state, not a defect.
