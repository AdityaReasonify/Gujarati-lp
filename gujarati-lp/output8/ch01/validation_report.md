# Validation Report — std 8, ch 01 જીવનજ્યોત
સ્વરૂપ: પ્રાર્થનાગીત (confidence: high)   explanation unit: એક કડી
Topics: 6   Objectives: 6   Images: 0/6   Exercises: 65/65 (13/13 blocks)

Deliverables: two — the plan (`13_merged.json`) and the exercise pack
(`10_exercise_solutions.json`). This unit prints a reading scene, so both ship.

## A–D (blocking)   **PASS**

Every hard item was checked mechanically against the merged plan, not asserted.

**A — diagnosis and lens.** સ્વરૂપ પ્રાર્થનાગીત, `genre_confidence: high`, four `genre_signals`
recorded off the render by A1. Explanation unit `એક કડી` matches the roster row for
ઊર્મિકાવ્ય-ગીત / લોકગીત / પ્રાર્થનાકાવ્ય ("one કડી, or one refrain-round where the song
cycles"): six topics = the standalone ટેક couplet + five printed કડી, none split, none merged.
ટેક handled as content, not repetition — `M1.S1.T1` teaches it once; the five કડી topics carry
it in `depends_on` and name the printed shorthand `પ્રભુ હે...` as the returning address without
re-teaching the couplet. The refrain's words never change in this chapter, so the
"changed-words ટેક" rule does not fire. Apparatus did not become a reading scene: the blue
પ્રવેશપેટી, the yellow શબ્દાર્થ box and the closing ચર્ચા-વિચારણા box are marked
`markers_deliberately_not_cut_as_topics` in `05_with_content.json`, and none of the three appears
as a topic. `guiding_question` is derived from this poem's own asking-verbs (રડવડતાં, ઝળહળતાં,
મઘમઘતાં, ગરજંતાં) and the six explanations read in order do answer it.

**B — verbatim and structure.** All six `original_chunk` non-empty, Gujarati script only —
zero Devanagari, zero Roman, zero `।` — verified codepoint-wise across U+0A80–0AFF. Every line
of every chunk was matched **verbatim as a string** against `00_chapter_normalized.md`; all
matched. Verse line breaks preserved (three lines per કડી, two for the ટેક); the printed refrain
shorthand `પ્રભુ હે...` is copied with its three dots and is nowhere expanded inside a chunk.
Poetic licence intact and uncorrected: `પ્રગટાવા`, `સાંકલડી`, `ટચૂકડી`, `નાનકડા`, `ફૂલડાં`,
`અમ`, the `વણ-` compounds, the inverted vocative `પ્રભુ હે`. `word_count.original` recomputed
from each chunk — all six agree exactly.

Marker accounting: `00_chapter_normalized.md` prints 6 reading markers (`[[ટેક]]`,
`[[કડી 1]]`…`[[કડી 5]]`) and 6 topics carry them, one each. 13 `[[સ્વાધ્યાય: …]]` blocks are
printed and **none** became a topic — every `source_marker` on the six topics is a reading
marker. Exercise block ten's embedded second poem (`મંદિર તારું વિશ્વ રૂપાળું`, જયંતીલાલ આચાર્ય)
stayed inside the exercise deliverable and was correctly not folded into the કડી chain.

**C — the teaching block.** Every topic has non-empty `explanation` and `real_life_example`.
Word counts, all inside the 55–90 band with no trimming required:

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 77 | 67 |
| M1.S2.T2 | 76 | 76 |
| M1.S2.T3 | 78 | 74 |
| M2.S3.T4 | 76 | 64 |
| M2.S3.T5 | 71 | 72 |
| M2.S4.T6 | 80 | 71 |

`objective_text` O1–O6: 19, 20, 23, 20, 20, 19 words — all inside 12–30. Glossing is at the
point of first use in every topic and the L2 bar is held low (ઝાઝું, ટચૂકડી, વેગે, તેજ, બાહુ,
સભર, ઉર, આભ, ભરચક, નીર all opened where they appear). Craft is named at the std-8 ceiling —
પ્રાસ, લય and પુનરાવર્તન in plain words, and **no** અલંકાર / છંદ / સમાસ label anywhere: a scan
for રૂપક, ઉપમા, સજીવારોપણ, પુનરુક્તિ, અનુપ્રાસ, ઉત્પ્રેક્ષા, છંદ, સમાસ, સંધિ, અલંકાર over every
authored field returns clean on all six topics.

**D — સ્વરૂપ essence.** `figures_of_speech` is `[]` on all six — the printed chapter names no
device and std 8 does not attach labels, so contract invariant 11 holds vacuously and nothing
was invented. `rhyme_scheme.rhyming_words` was checked word by word against each topic's own
chunk: જગાવો/જગાવો, જમાવો/બનાવો, બનાવો/ચલાવો, રચાવો/બનાવો, ઉડાવો/ઝરાવો — all present verbatim.
The second કડી correctly carries `rhyming_words: []` and states in its `note` that `ભરાવો` and
`આપો` do not rhyme. **That honest negative is the right answer and is recorded as a pass, not a
gap.**

No બોધ forced: a regex sweep for the exhortation shape `… જોઈએ` over every authored and
publication-facing field on all six topics returns **zero** hits. The printed exercise's
આપણે-phrasing is nowhere reproduced in the plan.

All 19 `severity: "hard"` items across `07_pitfalls.json` were verified in the field each names:

- First-sentence gates (6/6) — each `explanation` opens on that કડી's own asking verbs
  (જગાવો+જીવનજ્યોત / ઝાઝું જોર જમાવો / આંખે તેજ ભરાવો + બળ બાહુમાં આપો / રસથી સભર બનાવો +
  પીંછી તમારી ચલાવો / પંથ વિશાળ રચાવો + સાગર જેવું બનાવો / આભ વિશે જ ઉડાવો + ભરચક ધાર ઝરાવો),
  never on the condition, the picture or the ભાવ.
- `પ્રભુ હે` stands character-for-character inside `M1.S1.T1.explanation`, which also states
  that each later કડી prints the shorthand for the whole two-line ટેક.
- All five misconception corrections are present at the point the pitfall names, in the printed
  શબ્દાર્થ box's own words: જગાવો — પ્રગટાવો, પેટાવો ("કોઈને ઊંઘમાંથી ઉઠાડવાની વાત નથી");
  રડવડતાં — રખડતાં ("રડવાની વાત નથી"); વણ — વગર, opened twice side by side; મનનાં ફૂલડાં and
  પીંછી opened as the mind's own ("ફૂલ બગીચાનાં નથી"); ગરજંતાં — ગર્જના કરતાં; બલિદાન — ત્યાગ.
- The આપબળ reading stays a request made **to** પ્રભુ; no field says the poet manages without him.

`08_sensitivity.json` carries one item, `area: "ધર્મ"` — a valid member of the seven fixed
labels. Applied across all six topics: no authored field names a religion, sect or scripture the
chapter does not name, none compares traditions, none requires a child to profess belief. પ્રભુ
is glossed only as ઈશ્વર / ભગવાન (tradition-neutral dictionary synonyms) in `samanarthi`. Every
anchor sits in the child's own effort — રોટલી વણવી, સાયકલ, અંધારામાં આંખ ટેવાવી, મહેંદી, બસની
બેઠક, પરબ — and not one is an act of worship.

## E–G (reported)

**E — સ્વાધ્યાય and risk.** All 13 inventoried blocks answered; `blocks_found` = 13 =
inventory length; `unanswered` is empty; all 65 items carry a non-empty answer. Headings match
the inventory's `verbatim_heading` strings one-for-one. 16 items are marked
`is_model_answer: true` — the વાતચીત block, the personal-opinion items and પ્રવૃત્તિ are
answered with teaching values rather than skipped. Every `covered_by_topics` id resolves to a
real topic. Skill spread: grammar 19, vocabulary 18, reading comprehension 11, speaking 9,
literary device 7, writing 1.

**F — shape and media.** All 12 `json_contract.md` invariants hold on the merged plan:
`phase: 2`; `plan_id` = `{chapter_id}_v{version}`; `chapter_id` =
`gseb_eng_gujarati8_ch1`; every topic has ≥1 concept with a resolving `objective_id` and
non-empty `content[]`; the objectives registry is complete and consistent (6 unique ids, every
`home_topic_id` and `anchor[]` entry resolves, `strand_to_objective_map` covers L1–L6, single
strand `L`); every inline `learning_objectives[]` mirror matches its root `objective_text`
**character for character** and carries `image_examples: []`; concept ids are chapter-continuous
(`M1.S1.T1.C1` … `M2.S4.T6.C6`) — verified against the traversal, not just against each other;
recalls are `.RQ{n}` with `legacy_id` `.TR{n}` and **no `.SR{n}` anywhere**; media ids match
`MEDIA_ID_RE` concept-scoped; `publication_id` non-null; summaries strictly increase at every
topic (15<45<69, 16<48<76, 18<46<85, 17<51<87, 18<44<95, 17<51<109); no digit — Roman or
Gujarati — occurs in any name, explanation, example, summary, bullet, prompt or recall answer
(the કડી are named પહેલી, બીજી, ત્રીજી, ચોથી, છેલ્લી throughout).

`topic_type` is `POEM` on all six. That is correct for an Agent-13 intermediate file:
`phase2_contract.md` fixes the authored enum for Agents 02–13 and has Agents 14/15 map
`POEM → instructional` at emit. The closed server enum must appear in the emitted plans, and
nowhere earlier.

Bands from `field_shape_rules.md`, all held: `key_terms` 4–6 per topic (3–6); `concept_bullets`
and `important_points` 4 each (3–4); `recall_questions` 3 per topic (2–3), Bloom-laddered and
every set ending on analyze or evaluate; `difficult_words` 9 per module (5–10);
`estimated_exchanges` small integer strings ("3"/"4"/"5"); `bloom_level` lowercase in recalls and
Capitalised in `objectives[]` — the asymmetry is preserved as the contract requires.

**G — the seven usual mistakes.** None present. The plan teaches the સ્વરૂપ rather than
સાર+બોધ+પ્રશ્નોત્તર; no કડી merged and no પદ split; no licence silently corrected; no અલંકાર
named because the field existed; every `real_life_example` is single, Indian and inside std-8
reach; સ્વાધ્યાય was not cut as topics and the exercise deliverable is full.

## Media

`reuse_report`: scenes 6, authored 6, **reused 0**, rejected none — matching the 6 topics whose
`available_content_types` carry `"image"`. Every node carries `image_url: ""` **and** a real,
self-contained `generation_prompt` (964–1197 chars), as required while no Gujarati frame pool
exists. No `[reused frame: …]` stamp and no fabricated URL anywhere. Every `negative_prompt`
carries `Devanagari script labels`. `2d_tool` is `null` for the whole chapter (≤1 satisfied).
Media ids are concept-scoped and every `concept_id` / `home_concept_id` resolves.

The chapter-level hard media gate — no ઈશ્વર, deity figure or idol as a depicted subject — is
held, and held actively: the prompts carry no deity subject, and `M1.S1.T1.C1.IMG1` states
in-prompt "There is no temple, no shrine, no idol, no deity figure and no statue anywhere in the
picture", with the same exclusions repeated in every `negative_prompt`.

*Reported, non-blocking:* two narrator bars re-punctuate the line they quote —
`M1.S2.T3.C3.IMG1` renders `…બળ બાહુમાં આપો.` where the page prints `…આપો;`, and
`M2.S3.T5.C5.IMG1` renders `…પંથ વિશાળ રચાવો.` where the page prints `…રચાવો,`. The words are
exact; only the terminal mark differs. This touches no `original_chunk` and blocks nothing
(owner `09_media_planning.md` if it is worth a fix pass).

## Gaps

1. **`publication_id` is provisional and must not ship as written.** The contract requires a
   non-null value and `phase2_contract.md` states plainly that CBSE's `1` is **not portable** to
   GSEB. `1` is written here as the placeholder the shape demands. **VERIFY-2 must resolve the
   real GSEB publication row before the first Phase 8 upload.** This is not an A–D failure of
   this run; it is a hard precondition of upload.
2. **`chapter_master_id` is `null`.** Mandatory for upload, not discoverable from the LP2 API,
   fetched per chapter from the education DB (VERIFY-2). Never derived by arithmetic — the Hindi
   `355 − chapter number` pattern is CBSE provenance and does not transfer.
3. **`textbook` title is not confirmed off a rendered cover.** `01_meta.json` sets it `null` on
   purpose (the std-8 cover was not among the six supplied renders); the merged plan carries
   `11_pages.json`'s `"ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8"`, which comes from board-profile
   convention, not from a page. Fail-soft, carried, flagged. Owner `01_ingestion_genre_diagnosis.md`.
4. **`textbook_url` is a local path string** (`../Textbooks-pdf/std-8/ch-01-jivanjyot.pdf`) —
   the GSEB readers have no hosted URL. `textbook_pages` `1–6` is `confidence: medium`, read off
   the printed folios on page-1 and page-6 renders and agreeing with the manifest row.
5. **`topic_title` was derived, not authored.** No agent supplies it and the 32-key root list
   requires it; it is set to the printed chapter title `જીવનજ્યોત`. If GSEB expects something
   else, that is `01_ingestion_genre_diagnosis.md`'s field to set.
6. **`ordering` is deliberately absent** from `13_merged.json` — it is Agent 14/15's to set
   (`logical` / `textbook`), per this spec's own instruction. The 31 root keys written are the
   contract's 32 minus that one.
7. **Board and medium segments are PROVISIONAL until VERIFY-1.** `gseb_eng_gujarati8_ch1` uploads
   **clean** under a wrong medium and mis-files the plan silently — this is the failure that
   shipped all 23 Hindi plans under the wrong medium once. Confirm before the first upload.
8. **Reference-file correction outstanding** (raised by A1, carried by A4). The render prints the
   poet's name `ત્રિભુવનદાસ પુરુસોત્તમદાસ લુહાર` with **સ**, while
   `profiles/genres/prarthana_kavita.md` and `reference/corpus/std-8_inventory.md` both record
   `પુરુષોત્તમદાસ` with ષ. The printed form was kept, correctly. The reference files should be
   fixed; the plan should not.
9. **Typographic honesty flag** (A1): the refrain shorthand's trailing dots are transcribed as
   three full stops. At this raster three periods cannot be distinguished from a single U+2026
   glyph; the corpus inventory's own transcription was followed.
10. **Uneven topic length, non-blocking** (A2 → A4): `M1.S1.T1` holds two printed lines while
    every કડી topic holds three. That is the page's own shape — the refrain is printed standalone
    before the first કડી — and is reported, never repaired.
11. **`unmapped` exercises reported, not closed** (6 items, correctly): EX58–EX60 are the three
    ✓-MCQs on block ten's embedded second poem, and EX61–EX63 are the શબ્દકોશ-ક્રમ /
    ભાષાંતર / પ્રવૃત્તિ items whose words do not occur in this chapter's text. These are
    genuinely exercise-internal matter with no preparing topic. **No mapping was invented to
    empty the list**, and this is not a signal that the cut missed a scene.
12. **`publication_chunk` — a documented conflict between two specs, resolved in favour of the
    producing agent's, and surfaced here rather than routed as a failure.** This gate's spec says
    `publication_chunk` is "byte-identical to `original_chunk`". `agents/16_publication_authoring.md`
    says the opposite in its own §`publication_chunk`: it is "the publication-facing version of the
    topic's block **as a whole**", inside which "the verbatim `original_chunk` **stays verbatim**".
    The file follows its own spec: on all six topics `publication_chunk` is the `original_chunk`
    **byte-identical as a prefix** (verified, not eyeballed) followed by 633–735 characters of
    publication-facing prose. The verse is not rewritten, not reflowed, not re-punctuated, and its
    line breaks are intact. **The substantive invariant — the rewrite never touches verbatim — was
    tested and holds.** Blocking here would send `16_publication_authoring.md` back to undo what
    its own spec mandates, so it is not blocked. **The two specs should be reconciled by a human
    before the next chapter**; whichever wins, this chapter's data satisfies the stricter *intent*.
13. **The anchor-noun gate vs. the mandatory real-life anchor — read jointly, and reported.**
    `07_pitfalls.json` chapter-level §2 requires every concrete noun in any scene in `explanation`
    or `real_life_example` to occur in this chapter's `original_chunk` or its printed શબ્દાર્થ box;
    `global_content_rules.md` §5 simultaneously requires one concrete Indian anchor from the
    child's own life in every `real_life_example`, which no chapter's noun list can supply. Read
    literally and together the two are unsatisfiable. A12 named this in its notes and resolved it
    as "invent no scenery **for the poem**": every `explanation` is built strictly from chapter
    nouns, and the anchors sit in ordinary household and street life (રોટલી/વેલણ, સાયકલ/પેડલ,
    લાઇટ/ફળિયું, મહેંદી, બસની બેઠક, પરબ/માટલું). **Every noun the pitfalls name as a failure is
    verifiably absent** — no હોડી, દીવાદાંડી, તોફાન, માછીમાર or સઢ in the second કડી's topic; no
    છત્રી, ખેતર, ખેડૂત, વીજળી, મોર or ભીની માટી in the last. The resolution is defensible and is
    accepted for this run; **the pitfall's wording should be tightened so the next chapter does not
    have to reason its way out of it.**
14. **Attribution line sits in the FIRST topic, not the last** — correctly. `qc_checklist.md` §B
    expects `— કવિ/લેખકનું નામ` inside the last topic's chunk, which assumes a foot-of-poem
    byline. This page prints `- 'સુન્દરમ્'` at the **head**, under the title (A1 extraction note),
    so `M1.S1.T1` is where it belongs. Page-faithful, reported so it is not later mistaken for a
    misplacement.
15. **Context routing, reported not guessed.** The run context supplied
    `no_hallucination_policy.md` and `global_content_rules.md`. The other four documents this spec
    requires — `qc_checklist.md`, `json_contract.md`, `phase2_contract.md`,
    `field_shape_rules.md` — were **read in full from the repository**, not assumed; every band,
    invariant and roster row quoted above comes from those files as read. `agents/16_publication_authoring.md`
    was also read, to route gap 12 accurately rather than on this spec's wording alone.
16. **No page render was opened by this agent.** `00_chapter_normalized.md` answered every
    question this gate asked, including the layout facts (the standalone two-line ટેક, the five
    printed shorthand closings, the apparatus boxes, the head-of-poem byline), which A1 had
    already recorded in `extraction_notes[]`.

## LP2 validator

Not run — filled in Phase 8. Two values must be resolved **before** that call or it will fail on
shape regardless of this pass: `publication_id` (gap 1) and `chapter_master_id` (gap 2). The
board/medium segments (gap 7) will **not** fail the validator — they upload clean and mis-file
the plan, which is why they need a human check rather than a validator run.

---

**Verdict: A–D PASS.** No hard item blocks. Sixteen items are reported above, of which two are
genuine spec conflicts needing a human decision (gaps 12 and 13) and four are upload preconditions
(gaps 1, 2, 7, and the unhosted `textbook_url`). Nothing in this report is a partial pass presented
as a pass: the A–D gates were each executed mechanically against the merged plan and each returned
clean.

## LP2 validator

- Endpoint: POST https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate
- File: learning_plan_logical.json
- HTTP status: 200
- validation_errors (1):
  - root: 'publication_id' is required and must not be null
