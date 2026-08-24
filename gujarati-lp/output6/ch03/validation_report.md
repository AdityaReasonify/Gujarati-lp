# Validation Report — બાણ તો ત્યારે જ છૂટશે... (std 6, ch 3)

સ્વરૂપ: સંવાદ (`samvad_nibandh` પ્રમુખ + `natak_ekanki` સાથે લોડ) (confidence: high)   explanation unit: એક સંવાદ-ખંડ (વાતચીતનું એક પગલું / one stage-beat)
Topics: 9   Objectives: 9   Images: 0/9   Exercises: 17/17 blocks (48 entries, 0 unanswered, 1 unmapped)

**Re-QC after an owner re-run.** The previous pass failed A–D on one item — the hard સુરક્ષા rule
was not carried by the `M2.S4.T8` image prompt — and routed it to **A9**. `09_media.json` was
re-run (only that input changed; every other input file is older than the previous merge). This
pass re-merged all layers from source and re-ran the whole checklist mechanically.

Merged from `05_with_content.json` + `12_authoring.json` + `09_media.json` +
`16_publication.json` + `11_pages.json` + `01_meta.json` → `13_merged.json`
(31 root keys; `ordering` deliberately left to Agent 14/15).

The re-merge was rebuilt from the source layers and diffed against the previous `13_merged.json`:
**exactly four values differ**, all of them inside `M2.S4.T8.C8.IMG1` — `description`,
`teaching_notes`, `generation_prompt`, `negative_prompt`. Nothing else in the plan moved, so the
A/B/C findings below are the same assertions re-run on the same bytes, not a re-reading by eye.

---

## A–D (blocking)   **PASS**

The one blocker is closed. All twenty-two `severity:"hard"` topic checks in `07_pitfalls.json` and
the one hard chapter item in `08_sensitivity.json` now hold, asserted as strings against the merged
fields (55 mechanical assertions, 0 genuine failures — the two flags the coarse scan raised are
resolved as false positives under **D**).

### A — Diagnosis and lens   PASS

- સ્વરૂપ diagnosed off the rendered page with all four signals recorded in `genre_signals`
  (structure / theme / exercises / purpose), `genre_confidence: "high"`. The blue પ્રવેશપેટી is
  quoted as **evidence** (`આ સંવાદમાં ધ્યેયનું મહત્ત્વ રજૂ થયું છે`) and its verdict word `મહિમા`
  appears in no teaching field — mechanical scan, 0 hits.
- Explanation unit **એક સંવાદ-ખંડ** matches the roster on both loaded profiles: સંવાદ-નિબંધ's
  "one move of the argument" and નાટક/એકાંકી's "one stage-beat" coincide here, because every printed
  ખંડ completes exactly one move (પ્રશ્ન → જવાબ → ચુકાદો). Nine printed સંવાદ-ખંડ → nine topics,
  boundaries always on a complete વક્તા-વળાંક. Multi-paragraph turns under one speaker label
  (દ્રોણ's three paragraphs in `M1.S3.T7`, his blessing line in `M2.S4.T8`, the unlabelled
  `(એક સાથે)` line in `M1.S2.T3`) are **not** cut through.
- **A mixed chapter loaded every profile.** Both `samvad_nibandh.md` and `natak_ekanki.md` are
  active; the રંગસૂચના gate comes from the second, the argument-move gate from the first.
- ટેક n/a — this is ગદ્ય, `structure_inventory` records `kadi/duha/pad/tek_occurrences = 0` as a
  **measured** zero. The recurring question `તને શું શું દેખાય છે ?` is treated as the ટેક-like
  spine *inside* the beats it belongs to and was never lifted out as a topic of its own.
- **Apparatus did not become a reading scene.** The blue પ્રવેશપેટી, the શબ્દાર્થ gloss box, the
  chapter-final green વ્યાકરણ-પેટી `સંજ્ઞા વિશે જાણીએ` and all 17 સ્વાધ્યાય blocks sit in no
  `original_chunk`. Re-asserted mechanically: every non-blank line of every `original_chunk` is
  found in `00_chapter_normalized.md`, and **no `[[સ્વાધ્યાય: …]]` heading equals any topic name**
  (17 headings, 0 matches).
- `guiding_question` is derived from this chapter's own repeated question
  (`દ્રોણ દરેક કુમારને એક જ પ્રશ્ન પૂછે છે — 'તને શું શું દેખાય છે ?' — તો બાણ છોડવાની આજ્ઞા માત્ર
  અર્જુનને જ કેમ મળે છે ?`), and the nine explanations read in order answer it: four wrong answers
  (T4–T7), the right one (T8), the reason (T9).

### B — Verbatim and structure   PASS

- All nine `original_chunk`s are non-empty and unchanged by the merge (byte-identical to
  `05_with_content.json`; every content line found verbatim in `00_chapter_normalized.md`).
- **Script:** zero Devanagari, zero `।` and zero Roman characters in `original_chunk`s and in every
  authored display string — topic/module/segment/concept names, explanations, examples, all three
  summaries, bullets, important points, key terms, recall prompts and answers, every
  `concepts[].content[]` block and item, every `publication_text`, every `objective_text`,
  `chapter_name`, `unit_title`, `topic_title`, `guiding_question`, and the module `difficult_words`.
  Media `title`, `description` and `teaching_notes` were scanned on the same rule and are clean too.
  Roman survives only in `generation_prompt` / `negative_prompt` (an image model's input, never
  shown to a child), in ids and enum values, and in one root field — `teaching_lens`, reported under
  **Gaps** (item 6). `01_meta.json`'s `extraction_notes[]` records the one glyph that *looks*
  Devanagari at low dpi (`મેં`, three places), confirmed Gujarati at 250 dpi; no whitelist case
  applies to this chapter.
- **Nothing was corrected.** The printed oddities survive as printed: `દુરાધર` on one page against
  `દુરોધર` on the next; `સારું.. સારું..` (two dots) against `સારું... સારું,` (three); the unspaced
  `શી ખબર?` against the spaced `દેખાય છે ?`; the double space after `હવે બોલો,`; the missing
  પૂર્ણવિરામ before `)` in
  `(અર્જુન બાણ છોડે છે. રૂના બનાવેલા પંખીની આંખ વીંધાય છે, તે નીચે પડે છે)`; and the unfinished
  `બાણ તો ત્યારે જ છૂટશે, જ્યારે...`, which is also the chapter's title.
- **All bracketed રંગસૂચના stay inside the text**, brackets included — asserted string by string for
  the opening direction, the six parentheticals of `M1.S1.T2`, `(કુમારોમાં હસાહસ થાય છે.)` and
  `(સ્વગત)` in `M1.S3.T6`, `(યુધિષ્ઠિરને કશું સમજાતું નથી. તે નવાઈ પામી એક બાજુ ઊભો રહે છે.)` in
  `M1.S2.T4`, and the shot direction in `M2.S4.T8`. None was rewritten as narration, none dropped.
  `[[ચિત્ર: …]]` is a printed picture, not text, and correctly entered no chunk.
- **Marker accounting.** `00_chapter_normalized.md` prints 9 `[[સંવાદ: …]]` markers and 9 topics
  carry them, one to one. The 2 `[[રંગસૂચના: …]]` markers are governing directions folded into the
  topic that follows each. **17 `[[સ્વાધ્યાય: …]]` markers, 0 topics.**
- Ids consecutive; every `depends_on`, `source_topic_ids`, `home_topic_id`, `anchor[]`,
  `objective_ids`, media `concept_id` and recall id resolves against a node in `13_merged.json`
  (24 nodes).

### C — The teaching block   PASS

- All nine topics carry non-empty `explanation` **and** `real_life_example`.
- Word counts, measured on the merged file — all inside 55–90 / 12–30:

  | topic | explanation | real_life_example | brief < summary < detailed (chars) |
  |---|---|---|---|
  | M1.S1.T1 | 81 | 62 | 86 < 306 < 527 |
  | M1.S1.T2 | 80 | 68 | 93 < 298 < 595 |
  | M1.S2.T3 | 81 | 65 | 107 < 293 < 694 |
  | M1.S2.T4 | 87 | 62 | 97 < 316 < 590 |
  | M1.S2.T5 | 86 | 62 | 96 < 304 < 541 |
  | M1.S3.T6 | 81 | 65 | 104 < 327 < 600 |
  | M1.S3.T7 | 83 | 59 | 110 < 340 < 594 |
  | M2.S4.T8 | 87 | 61 | 91 < 303 < 700 |
  | M2.S4.T9 | 85 | 67 | 124 < 333 < 663 |

  `objective_text`: 16–21 words (O1 19, O2 20, O3 17, O4 20, O5 17, O6 21, O7 18, O8 16, O9 17).
  Bands remain **provisional until VERIFY-4**; nothing was widened and nothing needed trimming.
- **L2 calibration held.** Point-of-use glossing in every explanation, all glosses in Gujarati, no
  Hindi word standing in for a Gujarati one. The colloquial idioms A7 flagged as the standing L2
  hazard — `ચાડી ખાવી`, `ધૂળમાં મળવું`, `નિશાન સાધવું`, `નવાઈ પામવું`, `હાસ્તો`, `અલ્યા` — are
  glossed where they are printed, and `ધૂળમાં મળવું` also appears in the module's `difficult_words`
  (8 per module, inside the 5–10 band). `key_terms` 5–6 per topic; `concept_bullets` and
  `important_points` 4 each; 3 recall questions per topic, each with a real answer.
- `real_life_example` is Indian, concrete, single and within a std-6 child's reach, and the nine
  anchors do not repeat a domain: વર્ગમાં કસોટીની અટકળ / ઉત્તરાયણની ધાબા પરની ગૂંચ / શેરી-ક્રિકેટના
  નિયમ / આંબા નીચે પાકી કેરી શોધવી / બસ-સ્ટૅન્ડની ઉતાવળ / રિસેસના ડબ્બાની યાદી / કુંભારનો ચાકડો /
  લખોટીનું નિશાન / નવરાત્રિનો નવો તાલ. **Not one anchor puts a child near a bow, an arrow or a
  mace** (mechanical scan for `ધનુષ્ય`, `બાણ`, `ગદા`, `તીર` across all nine: 0 hits) — the safety
  item's `real_life_example` half.
- **Craft ceiling respected.** No craft label — અલંકાર, છંદ, ઉપમા, રૂપક, સજીવારોપણ, યમક — occurs in
  any display string, and `એકાંકી` occurs nowhere. `figures_of_speech: []` and `rhyme_scheme: null`
  on all nine, `overall_rhyme_scheme: null` on both modules — correct for ગદ્ય, and `[]` is the
  right answer, not an empty box.

### D — સ્વરૂપ essence   PASS  *(was the blocker; now closed)*

#### The hard સુરક્ષા item — closed

> `08_sensitivity.json` → `chapter_level` → area **સુરક્ષા**, `severity: "hard"`: keep the printed
> detail that the target was `રૂના બનાવેલા પંખી` — a cotton-made bird, not a live one — **in any
> explanation or image prompt for M2.S4.T8**, so the scene is never pictured as harming a real bird;
> and where an explanation must name the weapons, state that this is skill practised under a guru's
> supervision, not something to try at home.

Both halves are now met on `M2.S4.T8`, asserted string by string:

| where | evidence |
|---|---|
| `explanation`, `summary`, `detailed_summary`, `RQ3.answer`, `publication_text`, both concept paragraphs and the concept list | each names `રૂના બનાવેલા પંખી` (the list block: `રૂના પંખીની આંખ વીંધાય છે`) |
| media `description` | `નજર દૂરની ડાળીએ બાંધેલા રૂના બનાવેલા પંખીની લાલ આંખ પર જડાયેલી છે` |
| media `generation_prompt` | the target on the branch is `a small bird made of white cotton wadding, clearly a handmade stuffed model and not a living creature` … `No live bird appears anywhere in the picture, in the trees or in the sky` … `The arrow is still resting on the drawn string; nothing has been shot and nothing is hurt` |
| media `negative_prompt` | adds `live bird, real bird, bird in flight, wounded or bleeding bird, injured animal, blood, scattered feathers, arrow piercing a living creature, hunting scene` |
| media `teaching_notes` | names the cotton bird, cites the printed direction as the proof, and carries the supervision caution — `ધનુષ્ય-બાણ ગુરુની દેખરેખ નીચેની વિદ્યા છે, ઘરે અજમાવવાની રમત નહીં` |

`09_media.json`'s `notes[]` now also records the reasoning for the frames *before* the turn (below
under Media), so what remains is a reasoned, documented decision rather than an unaddressed item —
which is precisely what the previous pass said was missing.

#### The twenty-two topic checks — all hold

Re-asserted mechanically against the merged fields:

- **`M1.S1.T1`** — opening direction verbatim; `explanation` points at `વૃક્ષો` as the `ઝાડ` the
  પરીક્ષા will use; names `દુઃશાસન` with another કુમાર and carries both the printed fear line and
  the reply (`સદ્ભાગ્ય`). No unspoken interior state (`ને લાગ્યું`, `મનમાં થયું`, `ગભરાઈ ગય`,
  `ડરી ગય`: 0 hits).
- **`M1.S1.T2`** — all six parentheticals verbatim. No judging word on ભીમ (`તોછડો`, `ગુસ્સાખોર`,
  `ઉદ્ધત`, `ખરાબ`: 0 hits); `ડરપોક` / `ચુગલીખોર` appear only inside ભીમ's attributed speech.
- **`M1.S2.T3`** — no directive built on `બધાનો વારો આવશે.` (`ધીરજ રાખો`, `રાહ જોવી જોઈએ`,
  `ઉતાવળ ન કરો`: 0 hits); no judging word on દુર્યોધન; no lore used to account for the count.
- **`M1.S2.T4`** — both voices in `explanation`, દ્રોણનો બીજો પ્રશ્ન reported, યુધિષ્ઠિરનો જવાબ quoted
  in his printed words, closing direction verbatim.
- **`M1.S2.T5`** — no judging word on દુર્યોધન (`ઘમંડી`, `બડાઈખોર`, `સ્વાર્થી`, `ઉદ્ધત`: 0 hits);
  `ધીરજ` line reported as દ્રોણનું.
- **`M1.S3.T6`** — `(કુમારોમાં હસાહસ થાય છે.)` and `(સ્વગત)` verbatim and in position; no judging
  word on ભીમ; `explanation` lets his own list carry the humour (પંખી / વૃક્ષો / ફળ / આકાશ, all four
  present).
- **`M1.S3.T7`** — `દીર્ઘતાલ`, `દુરોધર`, `દુરાચાર`, `દુર્મુખ` all present as printed and `દુરાધર`
  absent from this topic, so the two spellings were not merged; the clause
  `એકલો અર્જુન ના, ના કહેવા હાથ હલાવે છે.` stays inside the `બધા :` turn; nothing added past the two
  printed signs of નિરાશા (`ગુસ્સો આવ્યો`, `ભરોસો ન રહ્યો`, `આશા હતી`: 0 hits).
- **`M2.S4.T8`** — both speakers named, the turn line `મને પંખીની માત્ર લાલ આંખ જ દેખાય છે.` quoted,
  the shot direction verbatim with its missing પૂર્ણવિરામ, and no unprinted reason for અર્જુનની
  સફળતા (`સૌથી હોશિયાર`, `પહેલેથી ખબર`, `ભગવાનની કૃપા`: 0 hits).
- **`M2.S4.T9`** — no directive to the child (`એકાગ્રતા રાખો`, `એકાગ્ર થવું જોઈએ`,
  `ધ્યેય નક્કી કરવું જોઈએ`: 0 hits); no `બોધ` / `સંદેશ` / `શિખામણ` / `ઉપદેશ` closer in any authored
  field; the unfinished line stays unfinished and is never completed with words the page does not
  print; the last words stay the કુમારો's, quoted as theirs.
- **Chapter-wide** — `કુરુક્ષેત્ર`, `ધૃતરાષ્ટ્ર`, `પાંડુના`, `કૃષ્ણ`, `મહાભારત`: **0 hits** across
  every display string and every media string, satisfying A7's chapter gate and `08`'s ધર્મ item.
  The soft સંઘર્ષ item holds: no કૌરવ-vs-પાંડવ rivalry is built anywhere.

#### Two coarse-scan flags, resolved as false positives

Both are recorded here rather than silently dropped:

1. **`વીંધ` without `રૂના` in `M1.S2.T3`, `M1.S2.T5`, `M2.S4.T9`.** These fields report the *rule*
   and the *claim* as printed — `હું જેને આદેશ કરું તેણે પક્ષીની આંખ વીંધવાની છે`,
   `આજ્ઞા આપો એટલે પંખીનું માથું વીંધી નાખું`, `આદેશ મળ્યો હોત તો અમે પણ આંખ વીંધી નાખત` — where the
   printed text itself says `પક્ષી` / `પંખી`; the reveal that the target is cotton is printed only
   inside `M2.S4.T8`'s own direction. Naming the cotton earlier would put words on the page that the
   page does not print. The hard item scopes `M2.S4.T8`, and every field there that describes the
   shot actually happening names the cotton bird.
2. **`હરીફાઈ` in `M1.S3.T6`.** It is ભીમ's own printed સ્વગત —
   `કંઈક ખાવાની હરીફાઈ હોત તો મેદાન મારી જાત !` — an eating-contest joke, not કૌરવ-પાંડવ rivalry.
   Likewise the single `નાટક` string in the plan sits in a `difficult_words` usage sentence for
   `ગદા` (`નાટકની તૈયારીમાં … પૂંઠાની ગદા`), not in any statement about this કૃતિ's form.

---

## E–G (reported)

### Contract invariants (F) — checked on `13_merged.json`

| # | invariant | result |
|---|---|---|
| 1 | `phase: 2`, `plan_id = {chapter_id}_v{version}`, `chapter_id = gseb_eng_gujarati6_ch3` | OK (board/medium segments provisional, VERIFY-1) |
| 2 | non-empty Gujarati-script `original_chunk` on every topic, no Roman/Devanagari/`।` | OK (9/9) |
| 3 | ≥1 concept per topic, valid `concept_id`, resolvable `objective_id`, non-empty `content[]` | OK (9 concepts, all with content) |
| 4 | root `objectives[]` complete and consistent; `strand_to_objective_map` covers every `legacy_id` | OK (L1→O1 … L9→O9; all `home_topic_id` and `anchor[]` resolve; no duplicate ids) |
| 5 | inline `learning_objectives[]` identical to the registry, character for character | OK (all nine fields compared per objective, plus `image_examples: []`) |
| 6 | `MEDIA_ID_RE` concept-scoped; recalls `RQ{n}` + `legacy_id` `TR{n}`; **no `.SR{n}`** | OK — 9 media ids `M….C{c}.IMG1`; 27 recalls, all `.RQ{n}`/`.TR{n}` |
| 6b | concept counter chapter-continuous | OK — `C1…C9`, one per topic, never restarting |
| 7 | no સ્વાધ્યાય block is a topic; every inventoried block answered | OK — 17 markers, 0 topics; `blocks_found` matches the 17-entry inventory as a set **and in printed order**; `unanswered: []` |
| 8 | three-tier summaries strictly increase | OK at topic level. No segment- or module-level summaries were authored, so nothing to check there |
| 9 | no numbers in display text | OK — digit scan (ASCII and `૦-૯`) over all display strings returns 0. Numerals survive only in ids, `word_count`, `textbook_pages` |
| 10 | one image per reading scene; ≤1 `2d_tool` | OK — 9 scenes, 9 images, `2d_tool: null` chapter-wide |
| 11 | `figures_of_speech` lines found verbatim | OK — `[]` on all nine (vacuously and correctly) |
| 12 | every reference survives renumbering | holds now; **re-assert after Agent 14** |

`topic_type` carries the authored enum `STORY_TELLING` on all nine topics. Per `phase2_contract.md`
that is correct for an intermediate file — Agents 02–13 keep the literary value and **Agents 14/15
map it at emit** (`STORY_TELLING → instructional`). `topic_category` runs
introduction ×2 → core ×4 → transition → climax → resolution. `bloom_level` is Capitalised in
`objectives[]` and lowercase in `recall_questions[]`, as the accepted reference plan has it.

Topic key set is exactly the contract's 31 keys plus the six permitted extras
(`figures_of_speech`, `rhyme_scheme`, `shabdarth`, `samanarthi`, `vilom`, `vyakaran`), identical on
all nine topics. Every working field was dropped: `source_markers`, `source_span`,
`source_lines_00_normalized`, pitfall notes, media reuse scores and `topic_id` off the media nodes,
validation flags, transcription notes. Root is the contract's 32 keys minus `ordering`, which is
Agent 14/15's to set.

### Publication (F)

Every topic has a non-empty `publication_text`; every `paragraph` block in `concepts[].content[]`
carries its `publication_text`, matched **by index** to `16_publication.json`'s
`concept_publication` (18 paragraph entries across 9 concepts; the 9 `list` blocks correctly emit
none). No vocative or classroom instruction survived (`બાળકો`, `જુઓ —`, `બોલો,`: 0 hits). Comparing
each `publication_text` against Agent 12's `explanation` shows de-classrooming only — no fact,
gloss or quoted line added or removed.

**One reported wording discrepancy between two specs, not a defect in the data.** This agent's spec
says `publication_chunk` must be "byte-identical to `original_chunk`"; `agents/16_publication_authoring.md`
defines it as "the publication-facing version of the topic's block **as a whole**", with the
verbatim `original_chunk` standing verbatim *inside* it and only the surrounding prose rewritten.
A16 built the second: on all nine topics `publication_chunk` **begins with the `original_chunk`
byte for byte** (verified character by character) and then appends two paragraphs — the publication
prose of the `explanation`, then of the `real_life_example`. The verbatim is untouched, which is the
rule both specs exist to protect, so this is **not** blocked. The previous pass reported this line
as "byte-identical", which was inaccurate; it is stated correctly here. **Owner for the wording:
the pack's spec files (13 vs 16), not this chapter.**

### Exercises (E)

`coverage_report.blocks_found` = **17** = `01_meta.json`'s `exercise_inventory`, entry for entry in
printed order (exact set and order match). `blocks_answered: 17`, `unanswered: []`. **48** entries
answered: each separately numbered printed question gets its own `EX` (blocks 1, 3, 4, 5, 7, 9, 13,
16) and each single-instruction block with blank lines or one grid is solved whole with every slot
filled in `values_filled_for_teaching` (blocks 2, 6, 8, 10, 11, 12, 14, 15, 17). Personal-opinion,
પ્રવૃત્તિ, પુસ્તકાલય and નાટ્યીકરણ items are answered as model answers rather than skipped. The
અનુવાદ block's answers are written in the medium of instruction on purpose and marked as such in
`teacher_note` — not a script failure.

`unmapped` carries **one** entry, reported and correctly not closed by invention: **EX41**
(`આપેલી બે સંજ્ઞાઓનો ઉપયોગ કરીને ઉદાહરણ મુજબ એક-એક વાક્ય બનાવો.`). None of its seven noun pairs, nor
its printed example, occurs in the સંવાદ — the block drills the appended green `સંજ્ઞા વિશે જાણીએ`
box, which is apparatus and correctly became no topic. A10 recorded the absence with its reasoning
and, for contrast, mapped block 15 because its list word `ઝાડ` *is* printed in દ્રોણ's mouth.

### Media (F)

`reuse_report`: `scenes: 9`, `authored: 9`, `reused: 0`, `rejected: []` — matching the nine topics
carrying `"image"` in `available_content_types`. Every node has `image_url: ""` **and** a real,
self-contained `generation_prompt`; no `[reused frame: …]` stamp anywhere, no fabricated URL. Every
`negative_prompt` carries `Devanagari script labels`. Each narrator bar names one exact printed
Gujarati line, and media `title` / `description` / `teaching_notes` are Gujarati script with no
digits. Recurring figures are held constant by repeating the appearance sentences rather than by
referring back, as the self-contained-prompt rule requires. `2d_tool: null` for the whole chapter,
with A9's reason recorded (a spoken સંવાદ offers nothing a child could operate).

**Reported, not blocking — the frames before the turn.** `M1.S2.T4`, `M1.S2.T5`, `M1.S3.T7` (and
the earlier `M1.S2.T3`, `M1.S3.T6`) still stage `a small brown bird on a high branch` far off in a
frame where a boy holds a nocked or part-drawn bow. The hard item scopes `M2.S4.T8` and is met
there; A9 has now recorded its reasoning for the earlier frames — the printed કુમારો call the target
`પક્ષી` from a distance and the text reveals it is `રૂના બનાવેલું` only inside `M2.S4.T8`'s own
direction, so naming the cotton earlier would pre-empt the printed reveal, and in every earlier
frame the bow is only drawn while દ્રોણ withholds the આદેશ, so nothing is shown being struck. That is
a reasoned, recorded decision and it is accepted as such. The residual point, for A9 to weigh at
its own discretion: the target *was* a cotton model all along, so a live bird in those frames
pictures something the page does not have, and a reader who takes the pitfall's "shows or implies"
clause chapter-wide would still want the branch target neutral (a small still shape, not a living
bird) in the four earlier frames. One clause per prompt would settle it and would cost no reveal.

### G — the seven usual mistakes

None present. The plan teaches the સંવાદ-ખંડ rather than સાર + બોધ + પ્રશ્નોત્તર; there is no verse
to merge or split; nothing printed was silently corrected (the two spellings of the boy's name, the
two- and three-dot ellipses and the unfinished last line all survive); no અલંકાર was named; the
anchors are std-6 and Gujarati; and the સ્વાધ્યાય is a separate, fully answered deliverable.

---

## Gaps

Honest absences, all recorded rather than filled:

1. **`publication_id` — must be resolved before upload.** The contract requires a non-null value, so
   `13_merged.json` carries the placeholder `1`, matching the pack's other chapters. **That is
   CBSE's publication row and it is NOT portable to GSEB.** The real row must be fetched from the
   education DB (**VERIFY-2**) before any Phase 8 run. Shipping `1` uploads clean and mis-files the
   plan.
2. **`chapter_master_id: null`** — mandatory for upload, fetched per chapter from the education DB
   (VERIFY-2), never derived by arithmetic. `upload_reference/chapter_master_map.json` is still
   provisional with every GSEB row null.
3. **`subject_ref_id` / `medium_id`: null** — server-injected; no GSEB subject record is confirmed.
4. **`chapter_id` / `plan_id` board and medium segments (`gseb`, `eng`) are provisional until
   VERIFY-1.** A wrong medium slot uploads clean and mis-files the plan.
5. **`textbook_url` is a local path** (`../Textbooks-pdf/std-6/ch-03-ban-to-tyare-j-chhutshe.pdf`) —
   the GSEB readers have no hosted URL; `11_pages.json` records this as its only gap.
   `textbook_pages: "14–21"` is **high** confidence (printed folio read off the renders of the first
   and last chapter page, agreeing with the manifest's `printed_start`).
6. **Roman slugs in two root fields — owner A1, reported not blocking.** `genre` carries the
   Gujarati label `સંવાદ` rather than a roster slug (`phase2_contract.md`'s root-key example wants a
   slug; A1 chose the book's own printed word, which the book uses twice, and A4 flagged the
   mismatch, leaving the emit-time decision to Agents 14/15). `teaching_lens` carries the profile
   slugs inside brackets —
   `તર્ક + દૃષ્ટિકોણ + જવાબદારી (samvad_nibandh, પ્રમુખ) — સાથે સંવાદ + રંગસૂચના + વળાંક (natak_ekanki, …)` —
   which is the permitted `ગુજરાતી (bracketed technical term)` shape and is teacher-facing
   provenance, never shown to a child. The previous pass reported "zero Roman in display", having
   not scanned `teaching_lens`; the corrected finding is recorded here. Note that
   `output6/ch01/13_merged.json` carries a slug in `genre`, so the pack is currently inconsistent —
   worth fixing at source, not here.
7. **`topic_title` was not authored anywhere.** It is one of the contract's root keys and no agent
   produces it, so it is set to the printed chapter name, matching `unit_title`. Flagged rather than
   passed off as supplied.
8. **`ordering` is absent by design** — Agent 14/15 sets it. `05b_textbook_order.json` records the
   printed order; when it matches the logical order, Agent 14/15 must raise
   `human_confirmation_required` per the contract.
9. **Uneven topic length — A2's and A4's note, carried here, never blocking.** `M1.S2.T4` and
   `M1.S2.T5` are short (four to six turns), `M1.S1.T2`, `M1.S3.T7` and `M2.S4.T9` long. That is the
   printed structure: the cycle of turns is deliberately repetitive and short. `M2` holds a single
   segment, deliberately, so the turn and its resolution are not buried among the failed turns.
10. **The સ્વરૂપ tension is open and was carried forward, not resolved by force.**
    `samvad_nibandh.md`'s strongest signal — an exercise block testing two sides of an argument — is
    absent from this chapter, and that profile's own near-miss table points this chapter at
    `natak_ekanki.md`; the genre index keeps `samvad_nibandh` dominant because the book labels
    itself `સંવાદ`. The cut therefore runs on stage-beat grain, which coincides here with "one move
    of the argument". **No two-sided argument structure was imposed** — there are not two sides,
    there are different answers to one question — and A7's chapter gate against calling this કૃતિ
    `નાટક` or `એકાંકી` holds.
11. **No કવિ-પરિચય or લેખક-પરિચય is printed** — the author slot reads only `- સંકલિત`. Not one
    biographical fact appears anywhere in the plan, and none may be added. A measured gap, not a
    hole to fill.
12. **Two `[[નોંધ: …]]` transcription notes** in `00_chapter_normalized.md` record printed
    irregularities in the exercise pages (underlined words in block 5; missing ✓ boxes beside items 3
    and 4 of block 7) and headings that say `પાંચ શબ્દો` above six printed slots (blocks 10 and 12).
    All are kept as printed by A10 and are not defects in this plan.
13. **`publication_chunk` composition** — the 13-vs-16 spec wording, recorded under **Publication**
    above. Data is correct under A16's contract; the two spec files should be reconciled.
14. **A9's live-bird staging in the frames before the turn** — reported under **Media** above as a
    reasoned, recorded decision with a residual point for A9's discretion. Not blocking.

No page render was opened by this agent: `00_chapter_normalized.md` and the upstream JSON answered
every question, and every `original_chunk` line was verified against that transcription.

---

## LP2 validator

<filled in Phase 8>

---

## Verdict

**A–D: PASS.** The single blocker from the previous run — the hard સુરક્ષા item unaddressed in the
`M2.S4.T8` image prompt — is closed by A9's re-run and verified here string by string, with A9's
reasoning for the surrounding frames now on record. All twelve `json_contract.md` invariants hold,
all 22 hard topic checks and the hard chapter item hold, and the exercise deliverable is complete
(17/17 blocks, 48 entries, 0 unanswered, 1 honestly unmapped). `13_merged.json` was re-merged from
source and differs from the previous merge only in the four `M2.S4.T8` media fields.

The run is complete as a plan, and it is **not yet uploadable**: `publication_id` still carries the
CBSE placeholder `1` and `chapter_master_id` is null, both pending VERIFY-2, and the board/medium
segments pend VERIFY-1. Those are recorded gaps, not authoring failures. Next: Agent 14.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- plan_id: gseb_eng_gujarati6_ch3_v1
- validation_errors: [] (none)
- message: "Valid"
- Result: PASS (validation only, no upload performed)
