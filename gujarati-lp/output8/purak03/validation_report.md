# Validation Report — std 8, પૂરક03 · સોમનાથ, સાસણ ને સાવજ ! (`gseb_eng_gujarati8_ch18`)
સ્વરૂપ: પ્રવાસવર્ણન / પ્રવાસ-નિબંધ (કાલ્પનિક પ્રવાસ) (confidence: high)   explanation unit: એક પડાવ

Topics: 9   Objectives: 9   Images: 0/9 (reused/authored; 9 scenes, all authored prompts, no frame pool)   Exercises: 9/9 items answered, 2/2 blocks (`blocks_found` 2 = inventory length 2)

Deliverables: this unit prints a reading scene, so two ship: the plan (`13_merged.json`) and the exercise pack (`10_exercise_solutions.json`). The exercise pack passes on its own (below).

**VERDICT: NOT COMPLETE. One hard blocker remains (D-3, owner A9). This is a failing run and is not presented as a pass.**

This is the re-QC pass after the owner re-runs. Of the three blockers the previous gate raised, **D-1 (the `આંગણે` names) and D-2 (A5's `key_terms` / `modified_chunk`, four sub-items) are closed and verified on disk. D-3 is unchanged**: `09_media.json` was last written at 21:16:40, before the previous gate (21:49), so Agent 9 was not re-run and the T9 media node is exactly as the previous gate found it. No other agent was running against this chapter during this pass (no process or file under `output8/purak03` changed after 22:05:08, apart from this gate's own two outputs).

`13_merged.json` was re-merged from the layers now on disk (31 root keys, 2 modules, 4 segments, 9 topics, 14 concepts, 27 recall questions, 32 `concept_publication` entries, 9 media nodes, one `2d_tool`). Diffed against the previous merge it differs in **exactly ten fields, all A5's and all expected**: `topic_name` of M2.S3.T5 and M2.S3.T6; `modified_chunk` of M1.S2.T3, M2.S3.T5, M2.S3.T6, M2.S4.T8; `key_terms[1]`, `key_terms[5]`, `concepts[C4].key_terms[1]`, `concepts[C5].key_terms[0]` of M1.S2.T3. Every other byte is unchanged, and every `original_chunk` is byte-identical to `05_with_content.json`. The merge carries the D-3 defect as found: A13 merges and gates, it does not repair. It is **not shippable** until D-3 closes. `ordering` is deliberately not written (Agent 14/15's key).

65 scripted checks were run on the merged file and the layers, plus a line-by-line reading of every authored field of all nine topics against the `07_pitfalls.json` and `08_sensitivity.json` hard rows: 64 pass, 1 flags, and the flag is a false positive (Flag 3 below). It is not a blocker.

---

## A–D (blocking)   **FAIL** — one item: D-3

Sections A, B, C and the 12 contract invariants pass. D passes except for D-3.

### D-3 (hard) — M2.S4.T9 media names the place `ઉતારે` refers to (owner: A9; unchanged since the previous gate)

`09_media.json` → `M2.S4.T9.C14.IMG1`:
- `description`: `આંબાવાડિયાના ઉતારે નાહી-ધોઈને તાજાં થયેલાં સૌ …`
- `generation_prompt`: `Breakfast under the mango trees at a forest-edge resort in Saurashtra … Small canvas tents sit in the shade behind the trees …`

`07_pitfalls.json`, M2.S4.T9, hard item 2 (Gates 4 and 5): *"the chunk does not say which place 'ઉતારે' is (the resort or the house), so no field names it."* The page says only `સૌ પાછાં ઉતારે આવ્યાં`. M2.S3.T4 says they stayed (`રોકાયાં`) at a tent-and-mango-grove resort, but M2.S3.T5–T6 end with `બધાં જલદી સૂઈ ગયાં` after the evening at શંકરદાનનું ઘર and the page never says where they slept, so it never says which place they returned to. The media layer makes it the resort in both the Gujarati `description` and the English prompt. The teaching fields (A12, A16) respect the item and gloss `ઉતારે` only as `જ્યાં મુસાફરો રોકાયા હોય તે જગા`.

Minimal remedy (A9 only; no other layer reads these two strings): set the scene somewhere the page leaves open (a plain lodging courtyard, no resort, no tents, no mango grove) and drop `આંબાવાડિયાના` from `description`. The `title` (`ઉતારે દહીં, થેપલાં ને ભાખરીનો નાસ્તો`) is already clean. While A9 is in the node, the same pass may also drop the boy pausing mid-bite to listen toward the trees, which the page does not print (soft, see "Media"). After A9 writes, A13 only needs to re-run the merge and the checks; nothing else in the plan moves.

### Closed since the previous gate (verified on disk, not taken from the owners' notes)

**D-1 — `આંગણે` in two topic names: CLOSED.** `02_structure.json` and `04_converged.json` are byte-identical (sha256 `4dc657f6…`, equal to `04_validation.json`'s `validated_sha256`, status `pass`, `blocking: []`); `05_with_content.json` equals `04_converged.json` on every structural field (ids, names, objectives, difficulty, `depends_on`, segment and module names, concept ids/names/objective ids; scripted compare, zero differences). The two names now read `શંકરદાનના ઘરે ઢોલિયો, દૂધ ને ગાન` (M2.S3.T5) and `સિંહ-પરિવાર અને સિંહ સાથેની નિરાંત` (M2.S3.T6); ids unchanged. The string `આંગણે` occurs in no authored field, name, media node or publication field of the merged plan (the only `આંગણામાં` is the child's own first-rain picture in M1.S2.T3's `real_life_example`, unrelated). One soft remark on the new T6 name is under E–G.

**D-2 — A5's seeds: CLOSED, all four.**
- (a) M1.S2.T3: the two rite definitions and the `જેમ મંદિરમાં દેવનાં દર્શન` example are gone. `key_terms` now carries `આરતીનો લાભ લીધો — અહીં, આરતીમાં હાજર રહીને ભાગ લીધો; ‘લાભ’ એટલે અહીં નફો નહીં, ભાગ લેવાનો મોકો` (a gloss of the printed phrase, which occurs in the chunk, not of the rite) and `દર્શન — આદરથી જોવું તે`; the `modified_chunk` bracket now glosses the phrase. No field explains the deity, આરતી or સ્નાન beyond the chunk. The three river names stay attributed (`એમ રાજેશભાઈ કહે છે`).
- (b) M2.S3.T5: the bracket after `દુહાછંદ` is removed; the word now stands only inside the printed phrases `દુહાછંદનું ગાન` and `દુહાછંદની રમઝટ`. The one bracket nearby glosses `રમઝટ`, not a form of verse.
- (c) M2.S3.T6: the `modified_chunk` now says `ત્યાં રહેનારા કહે છે કે …` (not the passive), and carries all three printed hedges: `દિવસે તો લગભગ ન આવે`, `રાતના કોઈ વાર આવી જાય`, `ક્યારેય (કોઈ વાર) ગાયનું વાછરડું ઉપાડી જાય`. `સિંહણને બે બચ્ચાં પણ સાથે છે` is now શંકરદાન's printed line, so no sentence says where the lions were.
- (d) M2.S4.T8: the stream reply now reads `રાજેશભાઈ મકદુમભાઈને પૂછે છે … અને મકદુમભાઈ જવાબમાં કહે છે કે …`; the guide's remark keeps `એવું લાગે છે`.

---

### What passed (mechanically, from the merged file and the layers; then by reading)

**A.** સ્વરૂપ diagnosed with the four `genre_signals`, `genre_confidence: high`, the blue પ્રવેશપેટી quoted as evidence only. Unit `એક પડાવ` matches `patra_pravas.md`. Mixed-chapter protocol not needed. The પ્રવેશપેટી, the two photographs, the શબ્દાર્થ box and both unnumbered pre-blocks are apparatus; none became a topic. No revision checkpoint or વ્યાકરણ unit is in these pages. `guiding_question` is derived from this chapter and the nine explanations in order answer it. Avoid 1 holds: `05b_textbook_order.json` equals the logical traversal exactly (scripted compare), and every explanation's first sentence names its stop (M2.S4.T8's is an instruction naming `સફારીમાં`, see E–G). Avoid 3 holds in its story-internal form in the first topic: `અનેરી અને આરવ પોતાના દાદા સાથે`, `કોઈ લેખક તમને ‘હું’ કહીને વાત કરતા નથી`, and the register feature `દાદુ` / `ઉમળકાથી` / the closing `કેમ ?` in `concept_bullets`.

**B.** All nine `original_chunk` are non-empty, Gujarati script only (U+0A80–0AFF plus whitespace and punctuation), zero Roman, zero Devanagari, zero `।` anywhere in the 323 KB file (whole-file scan; the only Latin letters outside the English prompt fields are the `O` of the objective ids). The merge left every chunk byte-identical to `05_with_content.json`. **The nine chunks, joined and whitespace-collapsed, equal the printed reading text of `00_chapter_normalized.md` exactly** (nothing dropped, repeated or reordered). Every printed defect is still in the chunk, uncorrected: the unclosed `‘‘હા દાદુ !` quote, the missing full stops (`પહોંચ્યાં`, `લીધો`, `માંડી`), `કહ્યું;`, `મે’માનો`, `શંકરભાઈ`, the unopened closing `’’` after `પહોંચાડે.`, `કહ્યું કે,‘‘`. `word_count.original` recomputed and agrees (147, 110, 73, 69, 212, 269, 100, 246, 30). Marker counts: `[[કડી]]`, `[[દુહો]]`, `[[પદ]]`, `[[ઘટના]]`, `[[ટેક]]` are all 0 in the transcription, so 0 topics carry them; five `[[પડાવ]]` markers stand for nine topics (see E–G). No `[[સ્વાધ્યાય]]` block, no exercise phrase and no apparatus text appears in any chunk or topic name. 283 quoted strings in the authored fields were checked against their own chunks: every one is a verbatim substring, a single-word gloss, an ellipsis-joined excerpt of two printed sentences, a quotation of the opening lines of M1.S1.T1 inside M2.S4.T9 (07 permits it and `depends_on` records it), or the child's own imagined speech inside a `real_life_example` (for example `આપણી બસ આવી !`, `જાઓ, રમો.`), none of which claims to be the chapter's.

**C.** Every topic has non-empty `explanation` and `real_life_example`. Word counts inside 55–90 under **both** counting methods (whitespace tokens / tokens excluding bare dashes):

| topic | explanation | real_life_example |
|---|---|---|
| M1.S1.T1 | 88 / 83 | 61 / 60 |
| M1.S2.T2 | 84 / 77 | 71 / 71 |
| M1.S2.T3 | 82 / 78 | 72 / 70 |
| M2.S3.T4 | 63 / 59 | 73 / 72 |
| M2.S3.T5 | 74 / 71 | 60 / 59 |
| M2.S3.T6 | 85 / 83 | 60 / 59 |
| M2.S4.T7 | 80 / 74 | 78 / 77 |
| M2.S4.T8 | 80 / 74 | 68 / 67 |
| M2.S4.T9 | 78 / 72 | 65 / 64 |

`objective_text` O1–O9: 29, 28, 26, 26, 27, 25, 29, 23, 29 words (12–30). Nothing trimmed or widened. `key_terms` 5–6 per topic (3–6 band), `concept_bullets` and `important_points` 4 each (3–4), 2–3 recall questions per topic, `estimated_exchanges` a small integer string. Craft ceiling (std 8): zero અલંકાર, છંદ, સમાસ, ઉપમા, રૂપક, ઉત્પ્રેક્ષા, અતિશયોક્તિ, સજીવારોપણ, પ્રાસ, યમક, શ્લેષ, વક્રોક્તિ, સાહિત્યપ્રકાર, `દુહો` or `પ્રવાસનિબંધ` in any A12 or A16 field; the four lines that invite a label are noticed in plain words (`દાદા દૂધને શાની સાથે સરખાવે છે ?`, which printed words show આરવનો ઉમંગ, the `દર્શને` joke, the closing `મનમાં … સંઘરીને`). The only scripted hit is Flag 3.

**D (everything except D-3).** Zero `જોઈએ`, `ઉપદેશ`, `ફરજ`, `શીખવે` in any field. The closing sentence of every `explanation`, `detailed_summary` and recall `answer` names a person, object or act in that topic's chunk (printed and read for all 9 × 5); none closes on a rule. No pity, community or generic label (`બિચારા`, `લાચાર`, `અપંગ`, `આ લોકો`, `આફ્રિકન`, `વિદેશી`, `ગામડિયા`, `પછાત`, `અભણ`): zero in any authored field (the hit on `જંગલી` is the printed `જંગલી પશુ-પક્ષીઓ` in M2.S4.T8's `modified_chunk`, about animals). `સીદી` is used only as મકદુમભાઈ's own word and every claim about it is attributed to him. No `ગંગા`/`યમુના`/`પ્રયાગ`; no job for શંકરદાનભાઈ (no `ભોમિયો`, no `ગાઈડ` in M2.S3.T4); nothing in M1.S2.T2 says the family reached ભાલકાતીર્થ, saw the ગીતામંદિર or bathed; no other-faith rite beside M1.S2.T2 or M1.S2.T3; no relative but દાદા in M1.S1.T1. A token-level scan of the 368 distinct words in the teaching fields that do not occur verbatim in the chapter found no destination detail, place, person, film, price or figure that the chunks do not print (what remains is Gujarati inflection and the child-world words of the `real_life_example` fields). M2.S3.T6 says plainly in the teacher's voice that this is how those who live in the Gir tell it and is `જાતે અજમાવવાની નહિ`, keeps `લગભગ` / `કોઈ વાર`, sets ચેતનાબેન's `ગભરાટ` beside it with no verdict, and its `real_life_example` is a power cut on a ફળિયું ઓટલો, not an animal. `figures_of_speech` is `[]` on all nine, so contract invariant 11 holds vacuously and nothing was invented. `08_sensitivity.json`'s four hard rows (M1.S2.T2 ધર્મ, M1.S2.T3 ધર્મ, M2.S3.T6 સુરક્ષા + ક્ષેત્ર, M2.S4.T7 સમુદાય) are honoured in the authored, publication and, after D-2, the A5 layers; the area labels in `08` are all from the seven fixed labels (ધર્મ, ક્ષેત્ર, સુરક્ષા, સમુદાય). The one hedge question is under E–G.

**Contract (12 invariants).** (1) `phase: 2`, `plan_id` = `{chapter_id}_v1`, `chapter_id` `gseb_eng_gujarati8_ch18`, `unit_number` 18, `topic_number` 18; `chapter_name` equals the printed title. (2) as B. (3) 14 concepts `C1`–`C14`, chapter-continuous, each with a registry-resolving `objective_id` inside its topic's `objective_ids` and non-empty `content[]`. (4) registry: unique ids, every `home_topic_id` and `anchor` resolves, `strand_to_objective_map` covers L1–L9, every topic's `objective_ids` resolve. (5) all nine inline mirrors match the registry character for character. (6) media ids match `MEDIA_ID_RE` with real concept ids; recalls `{topic}.RQ{n}` with `legacy_id` `.TR{n}`, no `.SR` anywhere; `publication_id` is 1 (non-null, provisional); `topic_type` is the authored `STORY_TELLING` on all nine, which Agent 14 maps to `instructional` (same convention as the sibling `output8/purak01` plan, which carries `POEM`). (7) no સ્વાધ્યાય topic; inventory answered. (8) summaries strictly increase on characters, words and sentences in every topic (brief 1 sentence; summary 3 (T9: 2); detailed 6 (T7, T9: 5); inside the 1 / 2–3 / 4–6 shape). (9) zero digits (ASCII or Gujarati) in any authored display field and zero `કડી 2`-style references. (10) see Media. (11) vacuous. (12) the one `depends_on` (`M2.S4.T9` → `M1.S1.T1`) resolves; `source_topic_ids` are empty.

**Exercises.** Both inventoried blocks (`શબ્દસમૂહ માટે એક શબ્દ આપો.`, 8 items; `રૂઢિપ્રયોગ :`, 1 item) appear in `10_exercise_solutions.json` with their headings character for character, including the space before the colon. `coverage_report.blocks_found` has 2 entries and equals the inventory length; `unanswered` is `[]`; item counts match (8 + 1). `unmapped` is **reported, not emptied**: EX3 વામકુક્ષિ, EX5 જીર્ણોદ્ધાર, EX7 ક્ષિતિજ, EX8 જીવાદોરી occur in no reading sentence, and no mapping was invented. EX9 maps by meaning only (`લીન થઈ જવું` ↔ `મગ્ન`), and the file says so. All nine answers are printed on the page, so none is a model answer. These four unmapped words appear in no authored field of the plan (checked).

**Publication.** Every topic has `publication_text`. `publication_chunk` begins with `original_chunk` **byte for byte** on all nine, then the rewritten explanation, then the rewritten example; the middle equals `publication_text`. `concept_publication` matches the paragraph blocks of `concepts[].content[]` by index and by count on every concept (32 entries); list blocks carry none. Token audit of the rewrite against the explanation: the only words dropped are `બાળકો`, `જુઓ`, `તમને`, `ધ્યાનથી`, `વાંચો`, `પાડો`, `કરો` and `શરૂઆત` (which becomes `શરૂઆતમાં`), and the only words added are `પાઠમાં`, `પડે`, `શરૂઆતમાં`, `આ`, `બે`, `વાતો`. No `બાળકો`, `જુઓ`, `બોલો`, `વાંચો`, `યાદ કરો` survives. No meaning added.

**Flag 1 (spec conflict, not a blocker).** Taken literally, agent 13's *"`publication_chunk` is byte-identical to `original_chunk`"* fails on **0 of 9**. Agent 16's spec, which owns the field, says the opposite shape: *"The verbatim `original_chunk` stays verbatim **inside** it"* (`agents/16_publication_authoring.md`, `## publication_chunk`), and Agent 16 did exactly that. The whole shipped corpus follows it, and the property both specs exist to protect (the verse is never touched) holds on 9 of 9 as a byte-exact prefix. Routing it to A16 would send A16 into a loop against its own spec, so it is **not raised as a blocker**. If the orchestrator wants the literal reading enforced, spec 16 has to change first.

**Flag 2 (false positive).** The vocative scan hit `તમે` in `M2.S3.T5.C8` content index 1 (and its publication twin), inside the printed host line `‘લ્યો તમે કહો તો અમે ગાઈએ !’`. That is quoted speech, copied as printed; the forbidden tokens are the narrator's `બાળકો`, `જુઓ —`, `બોલો`, `વાંચો`, and none occurs.

**Flag 3 (false positive).** The craft-ceiling scan hit `છંદ` in `M2.S3.T5.modified_chunk`. It is the substring of the printed word `દુહાછંદ` inside the printed phrases `દુહાછંદનું ગાન` and `દુહાછંદની રમઝટ`, which `07_pitfalls.json` M2.S3.T5 hard item 3 permits and which D-2(b) deliberately left standing. No form is named or explained.

---

## E–G (reported)

- **E — exercises and risk.** Answered 9/9 items; sensitivity notes applied in the authored layer as guided (flagged, not censored). Personal-opinion items: none printed. The four unmapped items are reported above.
- **F — shape and media.** The 12 invariants hold except where D-3 applies. `chapter_id` is the synthetic ch18 the run context requires (purak lesson 3 continuing after std 8's 15 numbered chapters and after purak01 as ch16; provenance is in `01_meta.json` `extraction_notes`). `gseb` / `eng` are still the provisional VERIFY-1 segments. `ordering` is not written; `05b_textbook_order.json` equals the logical traversal, so **A14/A15 should raise `{human_confirmation_required: true, reason: "textbook order is identical to logical order"}`**, which is the correct output for this form, not a defect.
- **G — the seven mistakes.** None present: not a સાર + બોધ + પ્રશ્નોત્તર (explanations are stop-first and no બોધ is forced); no દુહા merged and no પદ split; no ટેક (none); no poetic licence corrected (`મે’માનો`, `હંધાય`, `હારું`, `હાવજ`, `આંઈ`, `હાલ્યા` all kept); no અલંકાર named; no adult or foreign `real_life_example` (મેળાની આગલી રાત, શેરી ક્રિકેટ, પહેલું ઝાપટું, છકડો, ઈદની સેવૈયા, લાઇટ ગયેલી રાતે ઓટલો, એસ.ટી. ડેપો, ટેન્કરની સવાર, નાતાલનું કૅરલ; no domain repeats its predecessor); no સ્વાધ્યાય cut as a topic.
- **Observations, none blocking.**
  - **M2.S3.T6, the third hedge.** `07` lists three hedges for the hosts' reassurance: `લગભગ`, `કોઈ વાર` and `ક્યારેય … ઉપાડી જાય`. The A12 and A16 fields carry the first two (explanation, detailed summary, `important_points`, RQ3, the second concept's paragraph) and never the third; the calf clause appears only in A5's `modified_chunk`, now fixed there. Every field that carries `માણસને ન વતાવે` or the buffalo arrangement attributes it to `ત્યાં રહેનારા` and sits beside the stated hedge and the plain `જાતે અજમાવવાની નહિ` caution, and none states it as a fact about lions, so this gate reads the hedge list as the hedges each field's own quotation reaches, and does not raise it. A12's own note records the same reading (`keeps 'લગભગ' and 'કોઈ વાર'`). If the orchestrator reads 07's list as per-field, the minimal fix is one clause in M2.S3.T6's explanation or RQ3 answer (A12, then A16 re-mirrors `publication_text`); it is the orchestrator's call, not repaired here.
  - **M2.S3.T6's new name** `… સિંહ સાથેની નિરાંત`. All printed words, and it clears the `આંગણે` item, but `સિંહ સાથેની` can be read as ease beside a lion, whereas the page's `નિરાંતે જમ્યાં` is the dinner after the lions were seen. Soft, given `08`'s સુરક્ષા row. If A2 is ever re-run for another reason, a name built only from the dinner and the family (`સિંહ-પરિવાર અને વાળુ`, all printed words) would not carry that suggestion.
  - **M2.S4.T8's explanation opens on an instruction**, `સફારીમાં ત્રણ ભાગ જુદા પાડો.`, which names the safari but not a particular stop. It passes profile Avoid 1 (the safari is the matter), and A16's rewrite makes it a statement.
  - **A5 `key_terms` gaps that 07's CORR asked for** (soft, deliberately left by A5 and still open): M1.S2.T2 has no `જરા — અહીં શિકારીનું નામ, ‘થોડું’ નહીં` and its `પસ્તાવો — પોતાની ભૂલ માટે …` says `ભૂલ`, which the chunk never says of જરા (the authored fields use `કરેલી વાત માટે`); M2.S3.T4 has no `ને — અહીં ‘અને’`. A12 handled both in prose, bullets and recall. `સોમનાથદાદા` is not a key term (glossed in the second concept). Both topics already hold six key terms, so a fix means swapping one out.
  - **Narrator bars vs the chunk.** All nine narrator strings are verbatim substrings of their own topic's chunk (scripted); four are trimmed before the verb or lack the printed final mark (M1.S1.T1 `અમદાવાદની ખુશનુમા સવાર` vs printed `… સવાર હતી.`; M2.S3.T4 without the printed ` !`; M2.S3.T5 and M2.S4.T9 trimmed before the verb). The exact string to render is named in each prompt, as required.
  - **Pacing.** M2.S4.T9 (30 words) and M1.S2.T3 (73 words, the evening આરતી rides as the second concept) are short and M2.S3.T6 (269 words) is long; uneven length, reported by Agent 4 as a note, never a block.
  - **દર્શન** is glossed as `આદર કે નવાઈથી જોવું` in two topics and plain `જોવું` in two; compatible (A16 noted it).
  - **Root `genre`** is Agent 1's descriptive Gujarati string (`પ્રવાસવર્ણન / પ્રવાસ-નિબંધ (કાલ્પનિક પ્રવાસ)`), as in the other std-8 plans; the contract's example shows a roster slug, and `output7/ch15` carries `patra_pravas`. The corpus is not consistent; not blocked.
  - **Marker accounting.** Five `[[પડાવ]]` markers stand for nine topics (a marker can sit only at a printed paragraph boundary, and the fourth marker's one paragraph covers three stops). Agent 4 verified every marker has at least one topic in source order. The profile's rule (cut by stop, never by paragraph) is what the nine topics follow.

## Media

`reuse_report`: **scenes 9, reused 0, authored 9, rejected []**. Scenes equal the nine topics whose `available_content_types` carry `"image"`; one node per topic, ids `M1.S1.T1.C1.IMG1`, `M1.S2.T2.C2.IMG1`, `M1.S2.T3.C4.IMG1`, `M2.S3.T4.C6.IMG1`, `M2.S3.T5.C8.IMG1`, `M2.S3.T6.C9.IMG1`, `M2.S4.T7.C11.IMG1`, `M2.S4.T8.C12.IMG1`, `M2.S4.T9.C14.IMG1`, each matching `MEDIA_ID_RE` and naming a real concept. Every node has `image_url: ""` **and** a non-empty `generation_prompt` (no `[reused frame: …]` stamp anywhere); every `negative_prompt` carries `Devanagari script labels`. **One `2d_tool`** in the chapter, a route strip on M2.S4.T9 (null on every other topic); it names nine stops in the text's own order between two `અમદાવાદ` ends, and all eleven printed lines it quotes are verbatim in the chunks (scripted). Six of the nine card labels are verbatim printed words; three (`ભોજદે ગામનું રિસૉર્ટ`, `શંકરદાનનું ઘર`, `સાસણનું કાઉન્ટર`) are composed from printed words (`ભોજદે ગામના એક રિસૉર્ટ`, `આ આપણું ઘર`, `સાસણ … કાઉન્ટર`) and add no stop the text does not name; reported for A9 to see, not blocking. No real person is authored into any image; the two real photographs (a golden-stone temple, p.141; a lion, lioness and cubs, p.143) are page matter and no prompt copies them. **The only media blocker is D-3.**

Soft, profile Priors ("the scene as the text describes it and nothing more"), reported and not gated against 07's prose rules: M2.S3.T5's prompt hangs hand-painted pictures and embroidery on the verandah wall (the chunk says only `આ ચિત્રો જોયાં ? આ અહીંની કળા છે`); M2.S3.T6's prompt puts a thorn fence, dusk and the lions far beyond it (the chunk places the lions nowhere, and the prompt is careful that none is inside the fence or the house); M2.S3.T4's mood line says `only a local can lead you`; M1.S2.T3 has knee-deep water and stone steps; M2.S4.T9 has the boy pausing mid-bite. A9 may drop any of them in the same pass as D-3.

## Gaps

- **`11_pages.json` does not exist.** Spec 13 makes that fail-soft (a gap, never a block). `textbook_url` (`../Textbooks-pdf/std-8/purak-03-somnath-sasan-ne-savaj.pdf`, a local path, no hosted URL exists) and `textbook_pages` (`141–145`) were taken from `01_meta.json`, where Agent 1 recorded them from the printed folios. They are **not** Agent 11's confirmed values. If A11 is run it should confirm or replace them.
- **`textbook` is `null`.** The board profile records the std-8 cover as unread; nothing was invented. Sibling plans are inconsistent (some carry `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8`, `ch03`, `ch04`, `purak01` carry `null`); this unit follows the latter.
- **`chapter_master_id: null`** by design (no real GSEB master row exists for a પૂરક unit under a synthetic ch18 identity). **`publication_id: 1`** and `estimated_time: 1.5` are the corpus defaults, provisional until VERIFY-2 and a per-grade review. `medium_id`, `subject_ref_id`, `english_plan_id`, `english_chapter_id` are `null`; a Gujarati chapter has no English twin.
- **`- સંકલિત` is in no `original_chunk`.** Agent 5 ruled it a compilation credit printed under the title, not a writer's name and not at the foot (the same ruling as `output7/ch03` and `output8/ch14`), and it stays in `00_chapter_normalized.md`. The checklist assumes an attribution line in the last topic; for a credit with no name this is page-faithful. If the orchestrator rules that a printed credit must travel with the text, Agent 5 offered the one-line alternative (head of M1.S1.T1's chunk, `word_count.original` 147 → 149).
- **One letter read from glyph shape.** Agent 1 transcribed long `ઈ` (not `ઇ`) in ઈંતેજારી, મોટરસાઈકલ, ડ્રાઈવર, ગાઈડ, આઈડિયા, ઈન્ટરવ્યૂ from the glyph; Agent 5 re-checked ઈંતેજારી, આઈડિયા and શંકરદાનભાઈ on 3x–4x crops, but states that ગાઈડ and ડ્રાઈવર on p.144 were read at 1x and in a partly cut crop. The inventory's `ઇંતેજારી` (short ઇ) disagrees with the page; the page wins. No render was opened in this pass: `00_chapter_normalized.md` answered every question.
- **The dash between phrase and answer** in the eight one-word items varies in stroke weight on the page; Agent 1's single `–` is kept (Agent 10 noted it). A weight difference, not a different character.
- **Context routing.** The run routed no `teaching_voice_gu.md`, `gujarati_verbatim.md` or `author.md` to this gate (this spec does not cite them). To confirm the `publication_chunk` flag this pass grepped `agents/16_publication_authoring.md` (read-only) for what the owning spec requires; it did not edit or re-run anything of A16's. Nothing else in the spec cited a document that was not given.
- **Agent 4's `notes[]` (all reported, none blocking):** the evening આરતી as a second concept rather than a topic; uneven topic lengths; the cut at `લીધો` / `બીજે દિવસે` with no printed full stop between; `topic_type` `STORY_TELLING` on all nine, mapped at emit. (Its `આંગણે` note is now closed as D-1.)
- **Run history worth knowing.** A2, A4 and A5 were dispatched together for the previous gate's blockers; A4's own note records that A2 rewrote `02_structure.json` while A4 was reading, and that A5 therefore had to wait for the final write. This pass confirmed the outcome rather than the sequence: the three files agree (hashes above) and the names in `05_with_content.json` equal the converged ones.

## Routing

| blocker | owner (agent spec) | note |
|---|---|---|
| D-3 | `09_media_planning.md` | M2.S4.T9 `description` and `generation_prompt` only; may also drop the soft scenery items above in the same pass |

Not re-run, and not needed: A1, A2, A4, A5, A7, A8, A10, A11 (optional, see Gaps), A12, A16 (D-1 and D-2 are closed and none of their fields echo `આંગણે` or read A9's two strings). After A9 writes `09_media.json`, A13 is called again; the merge script and the scripted checks are repeatable and only the T9 media node changes. The two soft items an orchestrator might choose to route (the T6 third hedge to A12 then A16; the two A5 `key_terms` gaps to A5) are listed under E–G and are not part of this verdict.

## LP2 validator

Validation attempt 1 (2026-10-06 22:18):

Request: POST to `https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate` with multipart file `learning_plan_logical.json`

Response (HTTP 200):
```json
{
  "success": true,
  "action": "validated_only",
  "plan_id": "gseb_eng_gujarati8_ch18_v1",
  "version": null,
  "phase": null,
  "is_active": null,
  "is_draft": null,
  "counts": null,
  "diff": null,
  "publication_id": null,
  "publication_name": null,
  "validation_errors": [],
  "message": "Valid"
}
```

**Verdict:** Valid — validation_errors is empty.
