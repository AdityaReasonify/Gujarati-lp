# Validation Report — ધોરણ 6, એકમ 6 — સંસ્કારે સર્જ્યું સ્વર્ગ

સ્વરૂપ: માહિતીપ્રદ ગદ્ય (સંવાદ-શૈલી) — `mahitiprad_gadya.md` પ્રમુખ, `samvad_nibandh.md` નો બે-અવાજનો
gate લોડ (confidence: **low**, as A1 recorded)
explanation unit: એક માહિતી-ખંડ (તથ્ય-ગુચ્છ) — સીમા વક્તા-વળાંક પર નહીં, તથ્ય-પગલા પર

Topics: 8 (M1 = 4 · M2 = 4)   Objectives: 8   Images: 0/0   Exercises: 16/16 blocks, 77 solution
entries, `unanswered: []`

> **Images reads `0/0`, not `0/8`.** The honest zero here is the *authored* count as well as the
> reused one: `09_media.json` does not exist. Eight topics carry `available_content_types: ["image"]`,
> so **eight scenes are owed and none is authored**.

---

## A–D (blocking)   **FAIL**

**The run is not complete.** Three of the seven merge layers this agent folds were never written, so
three of the four blocking sections cannot be evaluated at all — not "passed with gaps", **not
evaluated**. What follows separates what was actually checked from what could not be.

### Blocking failures, with owners

| # | Failing item | Section | Owner |
|---|---|---|---|
| 1 | `12_authoring.json` **does not exist**. Every topic's `explanation`, `real_life_example`, three summaries, `concept_bullets`, `important_points`, `recall_questions`, `concepts[].content[]`, the module's `difficult_words`, `estimated_exchanges` and the ભાષા-બોધ extras are unwritten. §C cannot be run: 0/8 topics have an `explanation`, 0/8 have a `real_life_example`. | C | `agents/12_authoring.md` |
| 2 | `09_media.json` **does not exist**. Eight reading scenes declare `"image"` in `available_content_types`; zero media nodes exist. No `reuse_report` to check `scenes`/`authored`/`reused` against, no `generation_prompt`, no `negative_prompt`. | F (and the merge itself) | `agents/09_media_planning.md` |
| 3 | `16_publication.json` **does not exist**. 0/8 topics have `publication_text`; 0/8 have `publication_chunk`; there are no `concept_publication` blocks to index-match against `concepts[].content[]` (which are themselves empty, per failure 1). | Publication | `agents/16_publication_authoring.md` |
| 4 | Root `teaching_lens` carries **bare Roman script inside a Gujarati sentence**: `…samvad_nibandh નો બે-અવાજનો gate લોડ કર્યો છે…`. `gate` is not a bracketed technical term, and the profile slugs `mahitiprad_gadya` / `samvad_nibandh` are build vocabulary, not a lens a teacher reads. §B's script rule ("no Roman … outside bracketed technical terms — `સજીવારોપણ (personification)` is the only permitted shape") is a hard item and this is the one shipped display field that violates it. `01_meta.json`'s `extraction_notes[]` does **not** whitelist it — it is not printed content. Not repaired here: this is A1's field. | B | `agents/01_chapter_prep.md` |

Failure 4 is cheap — a Gujarati lens string, e.g. `તથ્ય + પરંપરા + જિજ્ઞાસા` (the form the sibling
std-6 chapters ship), with the two-voice gate recorded in a working field rather than in the lens.
Failures 1–3 are the pipeline simply not having reached those agents: `output6/progress.json` records
ch 6 as `A1 A2 A4 A11 A5 A7 A8 A10` done, with **A9, A12 and A16 absent**, while chapters 1–5 all
record the full fourteen. Nothing is wrong with the work that exists; three agents have not run.

### What WAS checked, and holds

**A — diagnosis and lens (checkable; holds, with one open question carried forward).**
`genre_signals` (four signals) and `genre_confidence` are recorded in `01_meta.json` off the rendered
pages, and the blue પ્રવેશપેટી's own words `આ સંવાદ પ્રકારનો એકમ છે` are quoted **as evidence**, not
used as the verdict. The declared explanation unit and the unit actually used are the same string
(`એક માહિતી-ખંડ`). Apparatus stayed apparatus — પ્રવેશપેટી, the શબ્દાર્થ gloss box, the રૂઢિપ્રયોગ and
કહેવતો bullet lists, the two `[[ચિત્ર]]` markers and the chapter-final yellow ગુજરાતી શબ્દકોશ ક્રમ box
all sit in `not_cut_as_topics` and carry no topic. `guiding_question` is derived from this chapter's
own printed chain (સૂકોભઠ વિસ્તાર → વૃક્ષારોપણ → ઉછેર → નક્ષત્ર-વન → શાળાનું ઉપવન) and reading T1→T8
in order answers it. Zero `[[કડી]]` / `[[દુહો]]` / `[[પદ]]` markers, zero ટેક occurrences — the
verse-specific A-items are satisfied vacuously, not waived.

**B — verbatim and structure (checkable half; holds except failure 4).**
All 8 `original_chunk`s are non-empty. Programmatic check: **zero** Devanagari codepoints, **zero**
Roman characters, **zero** `।` in any chunk. Every chunk, whitespace-normalised, is found **verbatim
inside `00_chapter_normalized.md`** — seven as one contiguous run, and M2.S3.T6 as two contiguous runs
(normalized lines 65+67 and 71+73) because the printed page-36 photograph interrupts the column
between them; A5's `attachment_notes[]` states exactly this and the excluded line 69 is a `[[ચિત્ર]]`
marker, not text. **That is not a verbatim defect and is not raised as one.**
Marker arithmetic: `[[સંવાદ: …]]` = **8** in `00_chapter_normalized.md`, and the 8 topics carry those
8 marker strings, one each, all 8 distinct and all 8 found in the normalized file.
`[[સ્વાધ્યાય: …]]` = **16** = `exercise_inventory` length, and **no સ્વાધ્યાય block became a topic** —
every topic's marker is a `[[સંવાદ]]`. Header furniture (`[[શીર્ષક-પટ્ટી]]`, `[[લેખક-સ્લોટ]]`, the QR
badge) entered no chunk. Ids run consecutively by traversal: M1–M2, M1.S1–M2.S4, T1–T8.
Every `word_count.original` equals the measured word count of its own chunk (86/107/75/103/164/72/38/56).

**C — the teaching block.  NOT EVALUABLE.** 0/8 `explanation`, 0/8 `real_life_example`. The only §C
field that exists is `objective_text`, and all 8 measure **18–24 words**, inside the 12–30 band with
no band widened. `key_terms` are 6 per topic on all 8, at the top of the std-6 `shabd_gloss.md` band.

**D — સ્વરૂપ essence.  NOT EVALUABLE.** `07_pitfalls.json` carries **26 `severity: "hard"` items**
across the eight topics; every one of them is a constraint on `explanation`, `real_life_example`, a
summary, a `concept_bullets` line or a `recall_questions[].answer` — i.e. on fields that do not yet
exist. They cannot be confirmed addressed and are **not** recorded as passing.
The two D-items that do not depend on authoring **do** hold: `figures_of_speech` is `[]` on all 8
topics and `rhyme_scheme` is `null` on all 8 (the correct std-6 ગદ્ય answer), so the
"lines found verbatim in `original_chunk`" check passes with nothing invented to fill a field.
`08_sensitivity.json` carries exactly one item — M2.S3.T6, area **ધર્મ**, severity **soft** (a
matched string from the seven fixed labels), `chapter_level: []`. **No hard sensitivity item exists**,
so §D's sensitivity half is clear; the soft ધર્મ guidance (નક્ષત્ર-વન taught as a real સરકારી યોજના
rooted in tradition — neither theology nor debunking, and the exam-success line kept as a village
elder's proud remark, never restated as fact) is **carried to A12 as an outstanding instruction**.

**Contract — the 12 invariants.** Ten hold as merged; two are open on the missing layers.
Holding: `phase: 2`; `plan_id` = `gseb_eng_gujarati6_ch6_v1` = `{chapter_id}_v{version}`;
`chapter_id` = `gseb_eng_gujarati6_ch6`. Every topic has ≥1 concept with a resolvable `objective_id`.
Registry: 8 unique `objective_id`s, all 8 `home_topic_id`s and all 11 `anchor[]` entries resolve to
real nodes, `strand_to_objective_map` covers L1–L8, every topic's `objective_ids` resolve. Inline
`learning_objectives[]` mirrors match the root registry **character for character on every field**
(verified programmatically, `image_examples: []` added). Concept counter is **chapter-continuous**
C1…C11 with no restart inside a topic and no restart at the M2 boundary. `publication_id` non-null.
`topic_type` is the authored enum (`CONCEPT` ×8) for A14 to map at emit. No digits — Latin or
Gujarati — in any `topic_name`, `concept_name`, `key_terms` entry or other authored display text.
**Open:** invariant 3's "non-empty `content[]`" fails on **11/11 concepts** (A12), and invariants 6
and 10's media clauses have nothing to check (A9). Invariant 12 is A14's, after this gate.

**Exercises — the one deliverable that is complete.** `coverage_report.blocks_found` is
**16 entries = `exercise_inventory` length**, entry-for-entry the inventory's `verbatim_heading` list
in printed order; `blocks_answered` is the same 16; `unanswered: []`. 77 solution entries.
Personal-opinion, જૂથકાર્ય, જોડીકાર્ય and the સુલેખન / નામ-અક્ષર blocks are answered as model answers
rather than skipped, and the standing L2 અનુવાદ block is answered in the medium of instruction and
marked as such. `unmapped` carries **18 items** — reported, not emptied (see §E).

---

## E–G (reported)

- **E — સ્વાધ્યાય.** Complete, as above. The 18 `unmapped` items are **argued, not invented away**,
  and every one names the book's own gap rather than a missed cut: block 8's `આ———મ = આશ્રમ` asks
  for a જોડાક્ષર word the reading text never prints (it occurs only inside સ્વાધ્યાય's own
  શબ્દક્રમ block), and all sixteen minimal pairs of block 9 (શરત/સરત, શાપ/સાપ, રાશ/રાસ, …) are
  absent from the reading text by design — the heading itself sends the child to the શબ્દકોશ, and
  the exercise descends from the teacher-addressed પ્રવેશપેટી, which is not a reading scene.
  Sensitivity: one soft ધર્મ item, flagged and guided, not censored.
- **F — shape and media.** Ten of the twelve invariants hold (above). `chapter_id` /`plan_id` shape
  is correct; segment recalls do not exist in this chapter and no `.SR{n}` id appears anywhere.
  Media cannot be reported — the layer is absent.
- **G — the seven usual mistakes.** Four are already excluded by the structure that exists: nothing
  merged that the page prints separately (8 markers → 8 topics, and 8 < 25 quoted speaker turns, so
  `mahitiprad_gadya.md`'s avoid-gate 2 holds); no verse exists to split or to mis-correct; no
  અલંકાર named; **no સ્વાધ્યાય block cut as a topic**, so the exercise deliverable is not
  half-empty. The remaining three (સાર+બોધ+પ્રશ્નોત્તર instead of the સ્વરૂપ; an adult or
  non-Indian `real_life_example`; a poetic licence corrected) live entirely in the authoring layer
  and are **untestable until A12 runs**.
- **Reported, non-blocking — `genre` field format.** Root `genre` carries A1's Gujarati name
  `માહિતીપ્રદ ગદ્ય (સંવાદ-શૈલી)` rather than a profile slug. The pack is already inconsistent here
  across std-6 (ch01/ch04 emit slugs, ch02/ch03/ch05 emit Gujarati names); carried through unchanged
  rather than repaired. Owner if the emit layer needs the slug: `agents/01_chapter_prep.md`.
- **Reported, non-blocking — `genre_confidence: "low"`.** Carried openly from A1 and re-stated by
  A4. A4 measured the consequence and it is small: the eight boundaries also fall between
  `samvad_nibandh.md`'s four argument moves (T1 સ્થાપના · T2–T3 પડકાર/પ્રશ્ન · T4–T7 પુરાવો ·
  T8 માગણી), so re-routing to `samvad_nibandh` as dominant **would not move a single boundary** —
  only module/segment names and the weighting of the objectives. Recorded, not blocked.

## Media

**No `reuse_report` exists.** `09_media.json` was never written. Eight topics carry
`available_content_types: ["image"]`, so the expected report is `scenes: 8, authored: 8, reused: 0`
with `image_url: ""` and a real self-contained `generation_prompt` on every node, and
`Devanagari script labels` in every `negative_prompt`. **Nothing was fabricated to stand in for it:**
`media` is `[]` and `2d_tool` is `null` on all 8 topics in `13_merged.json`, which is the honest
empty, not a claim that the chapter needs no images. Rejected frames: none — no pool exists to
reject from. A9's two visual cues are already sitting in the normalized file: the drawn illustration
on printed page 34 (a boy planting a sapling with a ખુરપી, a girl watering from a ઝારી) and the
aerial photograph of the નક્ષત્ર-વન garden on printed page 36.

## Gaps

- **Three merge layers absent** — `09_media.json`, `12_authoring.json`, `16_publication.json`. This
  is the reason for the FAIL and it is the whole of it; see the table above.
- `textbook_url` is a **local path** (`../Textbooks-pdf/std-6/ch-06-sanskare-sarjyu-swarg.pdf`) —
  the GSEB readers have no hosted URL. Carried verbatim from `11_pages.json`'s own gap note.
- `textbook_pages: "34–40"` at confidence **high**, read off the printed folios on renders of the
  first and last PDF pages (printed_start 34, offset N+11). **No pagination gap.**
- `chapter_master_id: null` and `publication_id: 1`. `upload_reference/chapter_master_map.json` is
  provisional — no GSEB row has been fetched, so `publication_id` here is the CBSE-derived value the
  sibling std-6 chapters already carry, kept **only** because the contract rejects null. Both must
  be resolved from the education DB at **VERIFY-2** before any upload; neither may be derived by
  arithmetic.
- `chapter_id`'s board and medium segments (`gseb` / `eng`) are **provisional until VERIFY-1**. A
  wrong medium segment uploads clean and mis-files the plan.
- `medium_id` and `subject_ref_id` are `null` by contract (server-injected). `english_plan_id` and
  `english_chapter_id` are `null` because a Gujarati chapter has no English twin — no twin was
  invented to fill them.
- `ordering: null` — Agent 14/15's field, deliberately not set here.
- Carried from A4's `notes[]`, non-blocking: **uneven topic weight.** M1.S1 holds a single topic;
  M2.S3.T5 holds the chapter's longest single paragraph (one speaker turn, eight-plus unfamiliar
  tree names, 164 words); M2.S4.T7 holds only two turns (38 words). This is the printed page's own
  shape and evening it out would have split a fact-step. Reported, never blocking — but A12 should
  expect T5 to need the heaviest glossing in the chapter and T7 the lightest.
- Carried from A4's `notes[]`, non-blocking: **O2's `objective_text` compresses** the chapter's
  printed `રોજ વહેલી સવારે અને સાંજે` to `રોજ સવાર-સાંજ`. Same fact, no invention — but A12 should
  carry the **printed** wording into the teaching fields, not the compression.
- `learning_objectives[]` was **composed at this merge** by mirroring the root registry object and
  appending `image_examples: []`. That is the deterministic mirror the server performs itself
  (`lp2_chapters.py`) and `lp_sync/patcher.py` re-does locally — it is not authoring, and it is
  recorded here rather than passed off silently.
- Working fields dropped at merge, as required: `markers`, `source_lines_00_normalized`,
  `genre_signals`, `genre_confidence`, `active_genre_profiles`, `explanation_unit`,
  `structure_inventory`, `exercise_inventory`, `extraction_notes`, `cut_summary`,
  `not_cut_as_topics`, `notes`, `attachment_notes`, `converged_from`. `13_merged.json` carries the
  32 root contract keys and nothing else.
- **A render was not opened this pass.** Every question this gate raised was answerable from
  `00_chapter_normalized.md`, `01_meta.json` and the intermediate JSONs — including the one apparent
  verbatim discontinuity (M2.S3.T6), which the normalized file's own line numbering and A5's
  `attachment_notes[]` resolve without a PNG.

## LP2 validator

**Not run.** Blocked twice over: this plan does not pass A–D, and even a complete plan cannot be
submitted until VERIFY-1 fixes the `chapter_id` board/medium segments and VERIFY-2 supplies
`chapter_master_id` and the GSEB `publication_id`.
`POST /api/lp2/learning-plans/validate` must return zero `validation_errors` before this plan ships.

---

## Verdict

**FAIL — A–D blocked.** Re-run `agents/09_media_planning.md`, `agents/12_authoring.md` and
`agents/16_publication_authoring.md` (in that dependency order — A16 rewrites what A12 writes), fix
root `teaching_lens` in `agents/01_chapter_prep.md`, then call this gate again. Everything upstream
of those four — A1's transcription, A2/A4's cut and id freeze, A5's verbatim, A7's pitfalls, A8's
sensitivity scan, A10's complete exercise deliverable, A11's pagination — is sound and does **not**
need re-running.
