# Validation Report — std 7, ch 15 સોનાનો કિલ્લો
સ્વરૂપ: patra_pravas — પ્રવાસવર્ણન shape (confidence: high)   explanation unit: એક પડાવ
Topics: 7   Objectives: 7   Images: 0/7   Exercises: 11/11 blocks, 59/59 items

**RE-QC after owner re-run (final pass).** The single A–D blocker of the previous pass —
`publication_chunk` carrying authored prose around the verbatim in all seven topics — was routed to
`16_publication_authoring.md`, and Agent 16 has re-run. This pass re-merges from the refreshed layer
and re-runs the whole checklist.

Merged file: `13_merged.json` — 31 root keys (all of the contract's 32 except `ordering`, which is
Agent 14/15's to set), 2 modules, 4 segments, 7 topics, 10 concepts, 7 media nodes, 1 `2d_tool`.

## A–D (blocking)   **PASS**

### The re-run item, verified

`16_publication.json` now sets `publication_chunk` to the verbatim and nothing else. Verified
programmatically across all seven topics: `publication_chunk == original_chunk`, character for
character — line breaks, the six quoted verse lines in M2.S3.T4, the printed `જેસલરમેર` in M2.S4.T7
and the unclosed opening `‘` in M2.S4.T6 all intact. And `original_chunk` in `13_merged.json` is
itself byte-identical to `05_with_content.json`'s: the merge reflowed, re-spaced and re-punctuated
nothing. Agent 16's note records the change as a trim of the added prefix and suffix, not a
re-authoring, and the diff confirms exactly that.

A full structural diff of this merge against the previous one shows **one** change class and no
other: the seven `publication_chunk` values. Everything that passed last time is byte-identical
this time.

### The rest of A–D, re-run in full

- **A** — સ્વરૂપ diagnosed off the rendered page with `genre_signals` and `genre_confidence: high`;
  the explanation unit **એક પડાવ** matches the patra_pravas roster line (પત્ર/પ્રવાસ — one પડાવ).
  Seven `[[પડાવ: …]]` markers in `00_chapter_normalized.md`, seven topics, one-to-one. Apparatus
  stayed out: the પ્રવેશપેટી, the શબ્દાર્થ box, the `[[આટલું જાણીએ]]` box, the three `[[ચિત્ર]]`
  captions and all eleven `[[સ્વાધ્યાય]]` blocks opened no topic — checked by substring against
  every સ્વાધ્યાય block's own text. `guiding_question` is derived from this chapter's own પડાવ
  sequence. The chapter is not mixed; the six quoted verse lines are a digression held inside
  M2.S3.T4 as its second concept, per the profile's "a digression stays inside its પડાવ".
- **B** — all seven `original_chunk`s non-empty and Gujarati-script (U+0A80–0AFF); **zero**
  Devanagari and zero Roman characters outside brackets in any chunk, any `explanation`,
  `real_life_example`, summary, bullet, `concept_bullets`/`important_points` line, recall prompt or
  answer, concept `content[]` block or `objective_text`; no `।` and no `॥` anywhere. Marker counts
  `[[કડી]]`/`[[દુહો]]`/`[[પદ]]`/`[[ઘટના]]` are all **0** — a measured zero for a ગદ્ય
  પ્રવાસવર્ણન, matching `01_meta.json`'s `structure_inventory` — and 0 topics carry them. Ids
  consecutive against traversal position: `M1`, `M1.S1`…`M2.S4`, `T1`…`T7`, `C1`…`C10`
  chapter-continuous, no restart inside a topic.
- **C** — every topic has non-empty `explanation` **and** `real_life_example`; all fourteen inside
  the 55–90 band and all seven `objective_text` inside 12–30. No band was widened. Every
  `brief_summary` < `summary` < `detailed_summary` by word count; every recall question carries a
  real answer; `key_terms` 5–6 per topic, inside the 3–6 band; `recall_questions` 2–3 per topic.
- **D** — `figures_of_speech` is `[]` in all seven topics (std-7 label ceiling), so contract
  invariant 11 is vacuously clean: there is no `lines` string to find, and none was invented to fill
  the field. `rhyme_scheme` null in every topic and `overall_rhyme_scheme` null in both modules —
  correct for prose; Agent 12 declined to assert a pattern for the six quoted lines, which is the
  right answer under `no_hallucination_policy.md` §3. All **21** `severity: "hard"` `avoid_checks`
  in `07_pitfalls.json` plus its six chapter-level notes were checked. Spot-checks passed: the
  country beyond `બીજા દેશની સરહદ` is unnamed, the three films' director is unnamed, `આ શહેરના
  રાજવી` is unnamed and undated, and no અલંકાર/છંદ/સમાસ label reaches any child-facing field.
  `08_sensitivity.json` carries **no hard item** (three soft — areas `ક્ષેત્ર` ×2 and
  `જાતિ-ભૂમિકા`, all on the fixed seven-label list, matched as strings); each is honoured: the
  M2.S4.T6 appearance sentences and the `બીજા રાજ્યની સ્ત્રીઓ` comparison survive **only** inside
  the verbatim, never in an authored field.
- **Publication (re-checked in full)** — every topic has a non-empty `publication_text`;
  `concept_publication` blocks match `concepts[].content[]` **by index and by count** (the index set
  equals the paragraph-block index set for all ten concepts, no out-of-range index, `list` blocks
  correctly left alone); no vocative or classroom instruction survives — `બાળકો`, `જુઓ —`, `બોલો`
  and a wider sweep (`શોધો`, `મોટેથી`, `હવે ધ્યાનથી`, `ધ્યાન રાખો`, …) all return zero across
  `publication_text` and every `content[].publication_text`; no digit, no Roman, no Devanagari in
  any publication display field.

**Meaning added?** No. Diffed each `publication_text` against Agent 12's `explanation`
character-by-character: six of seven are pure deletions of the address/imperative (`બાળકો, જુઓ — `,
`હવે એક વાત પકડી રાખો`, `હવે જુઓ —`). The one substantive substitution is M2.S4.T6, where the
closing exercise instruction `પછી ‘કારણ આપો :’માં આ જ કારણ લખવાનું આવશે.` is replaced by
`વર્ણનની સાથે જ લેખક પોતાનો મત મૂકી દે છે.` — a reading that already stands in that same topic's
`important_points` (`લેખકનો મત — …`). No new fact, place, figure or name enters; gate 4 still holds.
One more is a spelling alignment inside a quotation (M2.S3.T4 / C6: `જોષી` → `જોશી`, matching the
form printed immediately before the quotation on p. 100 — see the drift table below).

## E–G (reported)

- **E — exercises.** All eleven inventoried blocks answered, 59 items, `unanswered: []`.
  `blocks_found` matches `01_meta.json`'s `exercise_inventory` heading for heading (fuzzy match,
  no drift found) and in printed order; `items` totals in the inventory sum to 59, equal to the
  solutions count. **`unmapped` holds 6 groups (18 items) and stays unmapped** — reported, never
  closed by an invented mapping: `વાતચીત` EX4 (ઊંટ — in the printed pictures only, not in the
  reading text); the connective drill's EX15 (પોખરણ occurs nowhere in the chapter); the region-trait
  grid EX26–EX32 (built entirely on outside general knowledge); the unseen-paragraph block EX34–EX39
  (સાબરમતી નદી, self-contained exercise matter); EX54 (word pair ઊંટ/વાદળ); and the જાહેરાત
  document-literacy items EX56–EX58. Each carries a stated reason. This is the correct outcome for a
  std-7 exercise page whose grammar and document blocks are deliberately general.
- **F — shape.** All 12 `json_contract.md` invariants hold: `phase: 2`; `plan_id` =
  `{chapter_id}_v{version}`; `chapter_id` = `gseb_eng_gujarati7_ch15`; every `original_chunk`
  non-empty Gujarati; every topic ≥1 concept with a resolving `objective_id` and non-empty
  `content[]`; objective ids unique, every `home_topic_id` and every `anchor[]` id resolving to a
  real node, `strand_to_objective_map` covering L1–L7, every topic's `objective_ids` resolving;
  inline `learning_objectives[]` mirrors matching the root registry **character for character**
  (0 mismatches) and each carrying `image_examples: []`; every media id matching `MEDIA_ID_RE`
  concept-scoped with chapter-continuous `.C{c}`; recalls `{topic_id}.RQ{n}` with `legacy_id`
  `{topic_id}.TR{n}` and `bloom_level` lowercase — **no `.SR{n}` anywhere in the file**, and no
  segment recalls exist; no સ્વાધ્યાય block a topic; summaries strictly increasing; **no digit in
  any display text** (`બીજી કડીમાં`-style throughout) while `original_chunk` and `word_count` keep
  their numerals as provenance — `word_count.original` recomputed from each chunk and matching in
  all seven topics; every `depends_on` and `source_topic_ids` resolving. `publication_id` is
  non-null (see Gaps 2). `topic_type` in `13_merged.json` is deliberately the **authored** enum
  (CONCEPT ×2, STORY_TELLING ×4, REVIEW ×1) per `phase2_contract.md`; the closed server enum
  (`instructional`/`summary`/`assessment`) is Agent 14/15's mapping at emit and was **not** applied
  here. `ordering` is likewise left unset for Agent 14.
- **F — media.** `reuse_report`: `scenes: 7`, `authored: 7`, `reused: 0`, `rejected: []` — matching
  the 7 topics carrying `"image"` in `available_content_types`. Every node has `image_url: ""`
  **and** a real self-contained `generation_prompt` (1046–1360 chars); no `[reused frame: …]` stamp
  anywhere; every `negative_prompt` carries `Devanagari script labels`. Exactly one `2d_tool` in the
  chapter (પડાવ-પટ્ટી route strip, on M2.S4.T7), and the strip names only stops the chapter prints.
  Where a topic has two concepts the image is homed on the photographable one (M1.S2.T3→C3,
  M2.S3.T4→C5, M2.S3.T5→C8). Media working fields (`topic_id`) were dropped at merge; only the
  contract's 14 media keys survive.
- **G — the seven usual mistakes.** None found. No સાર+બોધ substitution; no merging of independent
  pieces (there are none — this is continuous prose); no પદ split; no licence "corrected" (see the
  drift table); no device named because the field existed; `real_life_example` anchors are std-7,
  Indian and one per topic (ફળિયું, કુંભારનો ચાકડો, વાવનાં પગથિયાં, આંગણું, મહેમાનને છાશ,
  શેરી-ગરબો, શાળાના પ્રવાસનો દરિયો); no સ્વાધ્યાય became a topic.
- **Minor, non-blocking (unchanged from the previous pass).** `09_media.json`'s M1.S2.T3
  `teaching_notes` uses the word *અલંકાર* inside a teacher-facing instruction **not** to name it
  ("અલંકારનું નામ પાડ્યા વગર…"). Teacher matter, not child-facing text, so the std-7 label ceiling
  is not breached — but it is the one place the word survives into a shipped field. Owner if it is
  to go: `09_media_planning.md`.
- **Minor, new this pass — quote-mark inconsistency.** Eighteen authored strings quote a chapter
  phrase with ASCII `'…'` while Agent 12's fields use typographic `‘…’`: the seven `objective_text`
  values (and their inline mirrors) from A2/A4, `guiding_question`, and several `teaching_notes`
  from A9. Cosmetic, no verbatim touched, no rule broken — reported so a later typographic pass can
  level it. Owners: `04_*` (objectives, `guiding_question`) and `09_media_planning.md`.
- **Carried from Agent 4's `notes[]`, reported not blocking.** (i) M2.S4.T7 is typed `REVIEW`; a
  reading of it as a plain final પડાવ (`STORY_TELLING`) is defensible — A2/A4's call stands, because
  the paragraph does close the chapter on its own value judgment. (ii) Topic lengths are uneven
  (three topics run one printed paragraph, three run three; M2.S4.T7 is shortest at 38 words) — a
  property of the essay, not of the cut. (iii) M1.S2 is a single-topic segment, and A2's reason (the
  fort and its કોતરણી are the essay's centre and the source of the chapter title) is sound.

### The two Gate-7 "live drift" hard items, resolved in Agent 5's favour (carried forward)

`07_pitfalls.json` raised two hard checks asserting that `05_with_content.json`'s `original_chunk`
had drifted from `00_chapter_normalized.md`. **The polarity is reversed: the transcription is the
one that is wrong.** In the previous pass I verified Agent 5's render-re-read claims directly
against `_renders/page-2.png` and `_renders/page-3.png` at 3–4× crop — the only reason a PNG was
opened in this run of the pipeline, because the disputed characters are exactly what a transcription
cannot adjudicate about itself. Neither `00_chapter_normalized.md` nor `05_with_content.json` has
changed since, so the finding is carried unaltered and no PNG was re-opened this pass.

| Place | `00_chapter_normalized.md` | printed page (verified) | in `13_merged.json` |
|---|---|---|---|
| p. 100, M2.S3.T4 | `કવિ યોગેશ જોષી` | **`કવિ યોગેશ જોશી`** (શ, no dot) | `જોશી` — correct |
| p. 100, verse line 4 | `ઊડી ઊતરી ગયેલી` | **`ઊડે ઊતરી ગયેલી`** (ે above ડ, matching `ઝૂરે`) | `ઊડે` — correct |
| p. 101, M2.S4.T7 | `જેસલમેર જેટલું` | **`જેસલરમેર જેટલું`** (extra ર — a printed GSEB typo) | `જેસલરમેર` — correct |
| throughout | ASCII `'` ×27 | typographic `‘ … ’` (U+2018/2019) | curly ×7 in chunks — correct |

Both hard items are **discharged**, and the repair belongs to the transcription, not to the plan —
routed to `01_ingestion_genre_diagnosis.md` as Gap 1. The book prints the poet's surname two
different ways on the same page; that is a printed inconsistency to report to the class, never to
level. No authored field carries `જેસલરમેર`, and Agent 12's fields use `જેસલમેર` — as the gate
requires.

## Media
`scenes 7 / authored 7 / reused 0 / rejected 0`. Reuse is dormant: no Gujarati frame pool exists, so
`Images` reads **0/7** by design, not by omission. All seven prompts are Rajasthan/Jaisalmer-faithful
— `gujarat_cultural_anchors.md` was read and deliberately **not** drawn from, since the chapter is
not set in Gujarat. No real named person is depicted (not the writer, not the three poets). The
M2.S3.T5 instruments are drawn only as far as drawing requires — no string count, no construction
detail — per pitfall gate 4; the M2.S4.T6 frame shows only રંગબેરંગી કપડાં and ગાવું, no garment the
chapter does not name.

## Gaps
1. **`00_chapter_normalized.md` needs four repairs** (owner `01_ingestion_genre_diagnosis.md`):
   `જોષી`→`જોશી` at the quotation lead-in on p. 100, `ઊડી`→`ઊડે` in verse line 4,
   `જેસલમેર`→`જેસલરમેર` on p. 101, and the 27 ASCII `'` restored to `‘ ’`. All four are
   render-verified above. The plan itself is correct; only the pipeline's stated source-of-truth
   file is behind. **This does not block the deliverables**, but it must be fixed before that file
   is used as evidence for anything else.
2. **`publication_id` is `1` and is PROVISIONAL and almost certainly wrong.** The contract requires
   non-null, and `1` is **CBSE's publication row**, explicitly recorded as not portable. It must be
   replaced by the GSEB row from the education DB (**VERIFY-2**) before any upload. Left as-is here
   only because `13_assembly_validation.md` requires a non-null value at merge.
3. **`chapter_master_id` is `null`** and is mandatory for upload. The GSEB row is fetched from the
   education DB into `upload_reference/chapter_master_map.json` (VERIFY-2) — never derived, never
   invented, so it is left null and reported.
4. **`textbook_url` is a local path** (`../Textbooks-pdf/std-7/ch-15-sonano-killo.pdf`); the GSEB
   readers have no hosted URL. Carried verbatim from `11_pages.json`, whose own `gaps[]` says the
   same. `textbook_pages: "99–105"`, confidence high, read off the printed folios on renders 1 and 7.
5. **`chapter_id` / `plan_id` board and medium segments remain provisional until VERIFY-1.**
   `gseb_eng_gujarati7_ch15` uploads clean even if the medium slot is wrong, and mis-files the plan.
6. **Root `genre` disagrees between files.** `01_meta.json` carries the Gujarati label
   `પ્રવાસવર્ણન-નિબંધ`; `05_with_content.json` and `04_validation.json` carry the slug
   `patra_pravas`. `phase2_contract.md` wants the roster **slug**, so `13_merged.json` writes
   `patra_pravas`. Reported, not blocking; owner `01_ingestion_genre_diagnosis.md` if the meta field
   should be normalised.
7. **Two root keys were filled at merge, not authored.** `topic_title` is set to the printed chapter
   title `સોનાનો કિલ્લો` (no agent produces it), and `estimated_time` is `1.5` from the contract's
   worked example. Both should be confirmed by A1 / the grade review rather than inherited silently.
8. **Printed-page facts to report to the class, never to correct** (already carried by A1/A4/A5):
   the શબ્દાર્થ box glosses `વ્યૂહાત્મક` as *સર્વ સ્થળે ફેલાઈને રહેલું વિશાળ* and `સહેલાણી` as
   *આનંદી માણસ*, neither of which fits the sentence the word stands in; three of its entries
   (તળપ્રદેશ, કર્ણપ્રિય, પરિધાન) occur nowhere in the chapter. Glosses were taken from the
   sentence's own sense; the printed box is untouched.
9. **`ordering` is absent from `13_merged.json` by design** — Agent 14/15 sets it, per spec.
10. **Six unmapped exercise groups (18 items) stand unmapped**, with reasons — see E above. Not a
    defect; recorded so nobody later "closes" it with an invented mapping.

## LP2 validator
Not run (Phase 8). `POST /api/lp2/learning-plans/validate` must return zero `validation_errors`
before upload, and cannot pass while Gaps 2 and 3 stand.

---

**A–D pass. This run is complete as far as this gate goes**, and `13_merged.json` is ready for
Agent 14. It is *not* ready to upload: Gaps 2 and 3 are unresolved values that only VERIFY-1/VERIFY-2
can supply, and Gap 1 leaves the pipeline's stated source-of-truth transcription behind the plan it
produced. Those are named absences, not silent ones.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati7_ch15_v1
- validation_errors: [] (none)
- message: "Valid"
