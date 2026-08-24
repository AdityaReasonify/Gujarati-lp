# Burnt-in text defects in the Hindi frame art — the fix list

> **One file, one job.** Every frame found to carry **incorrect Devanagari burnt into the image**
> goes here, with what it says and what it should say, so a later regeneration pass has a work
> list rather than a hunt. Companion to `EMPTY_IMAGE_URLS_class6_to_10.md`, which lists the
> opposite problem — media nodes with no image at all.
>
> Last updated 2026-08-14, after class-3 ch8 and ch10 shipped.

## ⚠ A second, worse defect: frames that belong to a different chapter

**Found 2026-08-14 while checking class-3 ch5 आम का पेड़.** Two of its 27 frames are not
mis-worded — they are **pictures of another story entirely**:

| frame | v1 title | v1 `description` | what the file actually shows |
|---|---|---|---|
| `ch5/scene_02_img_01` | प्रकृति, धैर्य और मेहनत का सन्देश | *"Two children … looking at a thought bubble depicting their smiling grandfather. A basket of mangoes sits on a wooden table."* | a sea and a ship, captioned **"निकोबारियों का विश्वास है कि प्राचीन काल में ये दोनों द्वीप एक ही थे…"** |
| `ch5/scene_04_img_01` | आम का आनंद | *"A young boy … eating a ripe yellow mango, juice dripping from his mouth."* | a Nicobari village, a bare-chested young man carrying firewood, captioned **"तताँरा एक नेक और मददगार इंसान था…"** |

That is **तताँरा-वामीरो कथा**, a class-10 text. It has no character, place or object in common
with a class-3 story about a boy planting a mango stone.

**Why this matters more than a misspelling, and why nothing already in the pack catches it:**

* The filename, the title, the `description`, the `generation_prompt` and the
  `instructions_for_student` all agree with each other — and all disagree with the pixels. A
  scan of every class-3 and class-4 plan for `तताँरा|वामीरो|निकोबार` returns **zero hits**,
  because the contamination is in the delivered file, not in any field describing it.
* The URL returns **HTTP 200**. This is `CLASS7_PLAN.md`'s ch3 trap — right path, wrong content,
  a clean 200 — repeating one level down, at the asset instead of the PDF.
* **Phase 1 ships both frames**, on topic `M1.S1.T1`. Wherever ch5's v1 plan is live, a class-3
  child is being shown a Nicobari folk tale captioned as a mango story.

**The consequence for this pack: the "prose is safe" shortcut is dead.** ch8's 11/11 clean
result was evidence about *spelling*, and spelling is a property of frames that quote text.
Identity is a property of every frame. **Look at every frame you are about to ship, in every
chapter, prose or verse.** `output3/_frame_check3.py` makes it about ten minutes a chapter —
it fetches the frames, stacks their caption bars into one strip, and lays the frames out 3-up.
The caption strip alone found both of these in one read.

> **Re-crop before believing a defect, too.** In the first caption strip ch5's `scene_26` read
> `इतन सालों` and looked like a dropped मात्रा. At full size it reads `इतने सालों` — the strip's
> downscale had eaten the े. That is the same "re-crop before believing it" rule §6.1 states for
> nuqtas, and it applies to reading defects *in* as well as out.

## What the defect is

Class-3 (and, on present evidence, class-4) frames are **generated teaching slides, not plain
illustrations**. Each carries:

* a light-yellow **narrator caption bar** along the bottom,
* often a **speech bubble** quoting or paraphrasing the text,
* a SINGULARITY watermark.

The art itself is good. The problem is the lettering: some frames misspell the very passage they
illustrate. **This cannot be repaired by `_TITLE_FIX` or any metadata map — it is pixels.** Class
10 shipped five misspellings of its hero through frame *titles* and that is on record as a defect
this pack exists to prevent; a misspelling inside the image is worse, because nothing downstream
can reach it.

## The pattern, and it is the useful part

27 frames have been read at full size — 11 in class-3 ch8, 16 in class-3 ch10.

| chapter | विधा | frames read | clean | minor | defective |
|---|---|---|---|---|---|
| class-3 ch8 चतुर गीदड़ | एकांकी (prose) | 11 | **11** | 0 | **0** |
| class-3 ch10 रस्साकशी | three poems (verse) | 16 | 9 | 1 | **6** |
| class-3 ch5 आम का पेड़ | कहानी (prose) | 27 | 24 | 1 | **2 — both foreign, see above** |

**Every defect sits in a frame that tries to reproduce the text's own words.** Frames that gloss
a term (`झुंड`, `खाट`, `जोश-खरोश`, `ट्रैफिक जाम`), or that simply narrate the scene in the third
person, are correct — including all eleven of ch8's, whose five speech bubbles quote the play
*verbatim* and correctly drop the bracketed रंग-संकेत.

**So verse is where the generator slips, and verse chapters are where the check must run.**
For class 3 that is **ch1, ch2, ch4, ch10, ch11, ch15, ch18**.

---

## The fix list

`source` is the phase-1 frame in `topic-content-images`, which is what a regeneration pass would
replace. `shipped as` is the phase-2 copy in `learning_plan_assets` that is live now; replacing
the source is not enough — the phase-2 copy has to be re-synced afterwards.

### class 3 · ch10 रस्साकशी — 6 defective, 1 minor

Source prefix: `https://media.singularity-learn.com/topic-content-images/Grade_3/english/hindi/ch10/`

| frame | where the text is | burnt in | should read | shipped as |
|---|---|---|---|---|
| `scene_01_img_01` | title card **and** its caption bar | **रसकशी** · **ट्फ़ैरिक जाम** (caption: **ट्फ़ौकि जाम**) | रस्साकशी · ट्रैफिक जाम | *not used* |
| `scene_03_img_01` | in-image credit block + caption | **परवधिधि** · **'मत'** · `माालती देवीं द्वाराा` | परिवर्धित · 'मत्त' · मालती देवी द्वारा | *not used* |
| `scene_05_img_01` | caption bar | **इंटें** | ईंटें | `M1.S1.T1.C1.IMG1` |
| `scene_05_img_01` | speech bubble | *सिर पर एक पूरी रेलगाड़ी उठा रखी है* — a paraphrase, not the line | सिर पर धर ली रेल। | `M1.S1.T1.C1.IMG1` |
| `scene_11_img_01` | caption bar | **हईसा** | हेई सा | `M2.S2.T5.C5.IMG1` |
| `scene_12_img_01` | speech bubble (quotes छंद 1) | **हई सा** ×3 | हेई सा | `M2.S2.T4.C4.IMG1` |
| `scene_14_img_01` | scroll (quotes छंद 4) | **सिल हुए** · **हई सा** ×3 | सफल हुए · हेई सा | `M2.S2.T7.C7.IMG1` |
| `scene_07_img_01` | caption bar | **खजूरलगते** *(minor — missing space, no wrong letter)* | खजूर लगते | `M1.S1.T2.C2.IMG1` |

**Clean in ch10** (no action): `scene_02`, `04`, `06`, `08`, `09`, `10`, `13`, `15`, `16`.

> **`हेई सा` is the single highest-value fix in the file.** It is the poem's टेक, it appears in
> three separate frames, and the plan teaches the child that the word has no meaning and exists
> only as the beat you pull on. A picture spelling it `हईसा`/`हई सा` beside that lesson is the
> worst case here.

### class 3 · ch5 आम का पेड़ — 2 foreign frames, 1 minor

Source prefix: `https://media.singularity-learn.com/topic-content-images/Grade_3/english/hindi/ch5/`

| frame | where the text is | burnt in | should read | shipped as |
|---|---|---|---|---|
| `scene_02_img_01` | caption bar | **निकोबारियों का विश्वास है कि प्राचीन काल में ये दोनों द्वीप एक ही थे…** — a different chapter | a picture of this story | *not used* |
| `scene_04_img_01` | caption bar | **तताँरा एक नेक और मददगार इंसान था…** — a different chapter | a picture of this story | *not used* |
| `scene_24_img_01` | caption bar | **हंसी** *(minor — anusvāra for candrabindu; वीणा prints हँसे on p35)* | हँसी | `M1.S2.T6.C6.IMG1` |

Both foreign frames are **replace, not re-word** — there is no correct caption for them, because
the picture itself is wrong. The other 24 captions are correct third-person narration, and
`scene_05`'s thought bubble quotes the story exactly (*ऐसे ही आम मैं अपने बगीचे में लगाऊँगा।*).

Two frame titles in this chapter are English placeholders — `scene_23_img_01` is **"Scene 48"**
and `scene_24_img_02` is **"Scene 52"** — and `scene_22_img_02` carries a Latin word inside a
Devanagari title (**"पिता और बच्चों का joyful पल"**). None is used as an anchor in the shipped cut.

### class 3 · ch8 चतुर गीदड़ — none

All 11 shipped frames pass. Captions are correct third-person summaries; all five speech bubbles
quote the play verbatim.

One thing that is **not** a defect and should not be "fixed": the art spells **बिल्कुल** where
वीणा prints **बिलकुल** (`scene_21`, `scene_27`). Both are current standard Hindi.

Separately, and not a text defect: **`scene_23_img_01` carries the English placeholder title
`Scene 23`** instead of a Devanagari name. It is unused in the shipped cut. `assemble.build_topic`
copies a frame title into the published `media.title` verbatim, so this must be fixed before that
frame is ever used.

---

## Not yet checked

Everything below is unread. **Absence from the fix list above is not a pass.**

| class | chapters | frames | status |
|---|---|---|---|
| 3 | ch1, 2, 4, 11, 15, 18 — the remaining **verse** chapters | ~150 | unread — misspellings live here |
| 3 | ch3, 6, 7, 9, 12, 13, 14, 16, 17 — prose | ~370 | unread. **The "prose is safe" shortcut is withdrawn** — ch5 is prose and served two frames from another chapter |
| 4 | all 13 | 715 | unread; one control frame from class-3 ch16 was clean |
| 5–10 | all | ~2,400 | unread. These classes shipped reuse-only with frames of the **same generated kind**, so the defect may be there too and nobody has looked |

**How to check a chapter, cheaply.** Fetch the frames the cut actually uses (one per topic), crop
the bottom ~14 % of each into one stacked strip to read the caption bars, then view the frames
downscaled 3-up to catch speech bubbles. About ten minutes a chapter. The two sheets for ch8 are
kept at `output3/ch08/_frames/_captions.png` and `_sheet.png` as the worked example.

## When these are regenerated

1. Fix the source frame in `topic-content-images` — that is what every class's plans point at.
2. Re-run the class's `_stage_assets.py` for the affected chapters; it re-fetches the source.
3. `run.py sync <chapter_id>` to re-upload the phase-2 copy into `learning_plan_assets`.
   **Step 3 is not optional** — the live plan serves the phase-2 copy, so fixing only the source
   leaves the wrong picture on screen.
4. Re-read the frame and move its row out of this file.
