# Validation Report — std 8, પૂરક03 · સોમનાથ, સાસણ ને સાવજ ! (`gseb_eng_gujarati8_ch18`)
સ્વરૂપ: પ્રવાસવર્ણન / પ્રવાસ-નિબંધ (કાલ્પનિક પ્રવાસ) (confidence: high)   explanation unit: એક પડાવ

Topics: 9   Objectives: 9   Images: 0/9 (reused/authored; 9 scenes, all authored prompts, no frame pool)   Exercises: 9/9 items answered, 2/2 blocks (`blocks_found` 2 = inventory length 2)

Deliverables: this unit prints a reading scene, so two ship: the plan (`13_merged.json`) and the exercise pack (`10_exercise_solutions.json`). The exercise pack passes on its own (below).

**VERDICT: A–D PASS. The run is complete at this gate. D-3 (the only blocker of the previous gate) is closed on disk.** One spec-conflict flag (Flag 1, `publication_chunk`) and a short list of soft observations are reported below; none is an A–D item and none is hidden. Downstream files (`learning_plan_logical.json`, `exercise_solutions.json/.md`) predate this merge and must be re-emitted by Agent 14/15 (see Gaps).

This is the re-gate after Agent 9 re-ran. `09_media.json` was rewritten at 22:28, after the previous gate's merge (22:13), and `11_pages.json` now exists (22:21). `13_merged.json` was re-built from the layers on disk: 31 root keys, 2 modules, 4 segments, 9 topics, 14 concepts (`C1`–`C14`), 27 recall questions, 32 `concept_publication` entries, 9 media nodes, one `2d_tool`; 325,538 bytes. The layer files were hashed before and after the write and did not change under it (01, 05, 07, 08, 09, 10, 11, 12, 16, 05b, 04). Diffed against the previous merge it differs in **exactly 26 fields, all inside `media[]`** (Agent 9 re-authored all nine nodes: the T1, T2, T3, T4, T5, T6, T7, T8 and T9 `generation_prompt` / `negative_prompt`, plus `title`, `description` or `teaching_notes` on five of them). Every other byte, including every `original_chunk`, every A5, A12 and A16 field and the root block, is identical to the merge the previous gate read, and `original_chunk` is byte-identical to `05_with_content.json` on all nine. `ordering` is deliberately not written (Agent 14/15's key).

98 scripted checks were run on the written file and the layers, plus a read of every authored field of all nine topics against the `07_pitfalls.json` and `08_sensitivity.json` hard rows: 97 pass, 1 flags (Flag 1, a spec conflict, not an A–D item). Four further hits on the first run of my own script were false positives and were corrected in the script, not waved through: the substring `ટેક` inside `ટેકરા` (ખાડા-ટેકરાવાળો); the printed `બહારના ભાગમાં` (cattle, T6 and O6) and `જંગલી પશુ-પક્ષીઓ` (animals, T8 `modified_chunk`); the printed `સરકારે … જળકુંડ` in T8's chunk and A5's `modified_chunk` (no A12 or A16 field says it, so nothing praises or judges the સરકાર); and ids and enums (`O1`, `image`) caught by the Roman-script scan.

---

## A–D (blocking)   **PASS**

Sections A, B, C, D and the 12 contract invariants all pass.

### D-3 — closed (verified on disk, not taken from the owner's note)

`09_media.json` → `M2.S4.T9.C14.IMG1` no longer names the place `ઉતારે` refers to. `description` is now `ઉતારે નાહી-ધોઈને તાજાં થયેલાં સૌ એક લાંબા મેજ પર દહીં, થેપલાં ને ભાખરીનો નાસ્તો કરે છે, ને અનેરી થેપલાંનો કટકો દહીંમાં બોળે છે.` (no `આંબાવાડિયા`); the `generation_prompt` sets the meal under a clay-tile roof beside a neem tree outside a plain whitewashed one-storey lodging, with no resort, no tents, no mango grove and no forest-edge scenery, and the `negative_prompt` now bars `canvas camp shelters`, `fruit orchard`, `forest-edge scenery`; `teaching_notes` says in Gujarati that the page never prints which place `ઉતારે` is, so the picture shows no identifiable place. `07_pitfalls.json` M2.S4.T9 hard item 2 holds in every field of the topic: the string `આંબાવાડિયાના ઉતારે` occurs nowhere in the merged file (it still occurs in the stale `learning_plan_logical.json`, see Gaps). The boy pausing mid-bite to listen toward the trees, which the page does not print, is also gone.

### What passed (mechanically, then by reading)

**A.** સ્વરૂપ diagnosed from the four signals (`structure`, `theme`, `exercises`, `purpose`) off the render, `genre_confidence: high`, the blue પ્રવેશપેટી quoted as evidence, not as the verdict. Unit `એક પડાવ` matches `patra_pravas.md`; not a mixed chapter. The પ્રવેશપેટી, the two uncaptioned photographs, the શબ્દાર્થ box and both unnumbered pre-blocks are apparatus and none became a topic or a name (scripted over names, chunks, concept, segment and module names). No revision checkpoint or વ્યાકરણ unit lies in these pages. `guiding_question` is this chapter's own (`અનેરી અને આરવ દાદા સાથે સોમનાથથી ગીર સુધી …`), not a profile string, and the nine explanations read in order answer it. Avoid 1: `05b_textbook_order.json` equals the logical traversal exactly, and every explanation's opening names its stop (M1.S1.T1 names who travels with whom; M2.S4.T8's opening is an instruction that names `સફારીમાં`, see E–G). Avoid 3 in its story-internal form: M1.S1.T1 names `અનેરી અને આરવ પોતાના દાદા સાથે`, says `કોઈ લેખક … ‘હું’ કહીને વાત કરતા નથી`, and carries the register feature (`દાદુ`, `ઉમળકાથી`, the closing `કેમ ?`) in `concept_bullets`. Avoid 2, 6 and 9 do not apply (no letter furniture, no artists).

**B.** All nine `original_chunk` are non-empty and Gujarati script only (U+0A80–0AFF plus whitespace, ASCII punctuation, curly quotes, dashes): zero Roman, zero Devanagari, zero `।` / U+0964 / U+0965 anywhere in the 325 KB file. **The nine chunks, joined and whitespace-collapsed, equal the printed reading text of `00_chapter_normalized.md` exactly** (nothing dropped, repeated or reordered). Every printed defect is still in the chunks, uncorrected: the unclosed `‘‘હા દાદુ !` quote, the missing full stops (`પહોંચ્યાં`, `લીધો`, `માંડી`), `કહ્યું;`, `મે’માનો`, `શંકરભાઈ`, the unopened closing `’’` after `પહોંચાડે.`, `કહ્યું કે,‘‘`. `word_count.original` recomputed and agrees (147, 110, 73, 69, 212, 269, 100, 246, 30). Marker counts: `[[કડી]]`, `[[દુહો]]`, `[[પદ]]`, `[[ઘટના]]`, `[[ટેક]]` are all 0 in the transcription and 0 topics carry them; five `[[પડાવ]]` markers stand for nine topics (a marker can sit only at a printed paragraph boundary, and the fourth marker's one paragraph covers three stops; Agent 4 verified every marker has at least one topic in source order). No `[[સ્વાધ્યાય]]` block, exercise prompt or heading text occurs in any chunk or name. Ids are consecutive `T1`–`T9`, segments `S1`–`S4`, modules `M1`, `M2`. 283 quoted strings in the authored fields were checked against their own chunks: each is a verbatim substring, an ellipsis-joined excerpt, a single-word gloss (`થોડું`, `હું`, `ભાં-ભાં`, `જોવું`), a grammar form discussed in a `vyakaran` note, a quotation of the opening lines of M1.S1.T1 inside M2.S4.T9 (07 permits it and `depends_on` records it), or the child's own imagined speech inside a `real_life_example` (`માફ કરજો`, `આવો, બેસો, ચાખો.`, `આપણી બસ આવી !`, `આવી ગયું !`), none of which claims to be the chapter's. The idiom `લીન થઈ જવું` in M2.S3.T5 is the printed pre-block's own idiom, named as a skill the topic prepares, never as a line of the reading.

**C.** Every topic has non-empty `explanation` and `real_life_example`. Word counts inside 55–90 under **both** counting methods (whitespace tokens / tokens excluding bare dashes); nothing trimmed, nothing widened:

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

`objective_text` O1–O9: 29, 28, 26, 26, 27, 25, 29, 23, 29 words (12–30). `key_terms` 5–6 per topic (3–6), `concept_bullets` and `important_points` 4 each (3–4), 3 recall questions per topic (2–3), `estimated_exchanges` a small integer string. Summaries strictly increase on characters and words in all nine; sentence counts brief 1, summary 3 (T9: 2), detailed 6 (T7, T9: 5), inside the 1 / 2–3 / 4–6 shape. Craft ceiling (std 8): zero અલંકાર, છંદ, સમાસ, ઉપમા, રૂપક, ઉત્પ્રેક્ષા, અતિશયોક્તિ, સજીવારોપણ, પ્રાસ, યમક, શ્લેષ, વક્રોક્તિ, સાહિત્યપ્રકાર, `દુહો` or `પ્રવાસનિબંધ` in any A12 or A16 field; the four lines that invite a label are noticed in plain words (`દાદા દૂધને શાની સાથે સરખાવે છે ?`, which printed words show આરવનો ઉમંગ, the `દર્શને` joke, the closing `મનમાં … સંઘરીને`). The only `છંદ` in the file is the substring of the printed `દુહાછંદનું ગાન` / `દુહાછંદની રમઝટ` in M2.S3.T5's `modified_chunk`, which 07 M2.S3.T5 hard item 3 permits.

**D.** `figures_of_speech` is `[]` and `rhyme_scheme` is `null` on all nine, so contract invariant 11 holds vacuously and nothing was invented. `08_sensitivity.json` area labels are all from the seven fixed labels (ધર્મ, ક્ષેત્ર, સુરક્ષા, સમુદાય). Zero `જોઈએ`, `ઉપદેશ`, `ફરજ`, `શીખવે`, `બોધ`, `આપણે પણ` in any authored field. The closing sentence of every `explanation`, `detailed_summary` and recall `answer` (27 + 9 + 9, printed and read) names a person, object or act in that topic's chunk; none closes on a rule. No pity, community or generic label anywhere (`બિચારા`, `લાચાર`, `અપંગ`, `આ લોકો`, `આફ્રિકન`, `વિદેશી`, `ગામડિયા`, `પછાત`, `અભણ`, `આદિવાસી`: none in an authored field). `સીદી` appears only as મકદુમભાઈ's own word, and every claim about it is attributed to him (`મકદુમભાઈ કહે છે …`, `એમ તેઓ કહે છે`). No `ગંગા` / `યમુના` / `પ્રયાગ`; no job for શંકરદાનભાઈ (no `ભોમિયો`, no `ગાઈડ` in M2.S3.T4); nothing in M1.S2.T2 says the family reached ભાલકાતીર્થ, saw the ગીતામંદિર or bathed; no other-faith rite beside M1.S2.T2 or M1.S2.T3; no relative but દાદા in M1.S1.T1; the words that occur in no chunk (the four pre-block answers `વામકુક્ષિ`, `જીર્ણોદ્ધાર`, `ક્ષિતિજ`, `જીવાદોરી`, and the four શબ્દાર્થ-box headwords `ભોમિયો`, `બેલડી`, `સ્થંભ`, `લટાર`, plus the orphan `પુનર્વસવાટ`) appear in no authored field. A token-level scan of every Gujarati word in the authored fields that occurs in no chunk and nowhere else in the unit's printed text found no destination detail, place, person, film, price, year or figure the chunks do not print (what remains is inflection, synonym lists such as `સમુદ્ર`, `ઝરો`, `નિર્ઝર`, and the child-world words of the `real_life_example` fields). The hard rows of `07_pitfalls.json` and `08_sensitivity.json` were checked one by one and are honoured in the authored, publication and A5 layers: M1.S2.T2 and M1.S2.T3 (ધર્મ: told as દાદા's and રાજેશભાઈ's words, three river names only as printed, no ritual doctrine, `આરતીનો લાભ` glossed as taking part), M2.S3.T6 (સુરક્ષા + ક્ષેત્ર: the reassurance attributed to `ત્યાં રહેનારા`, `લગભગ` and `કોઈ વાર` kept, ચેતનાબેન's `ગભરાટ` set beside it with no verdict, `જાતે અજમાવવાની નહિ` said in the teacher's voice, no field says the lions entered the yard or the house, ચેતનાબેન given no relation, `real_life_example` a power cut on a ફળિયું ઓટલો, not an animal), M2.S4.T7 (સમુદાય: both parts of the answer, `પણ` glossed, nothing added about the community), M2.S4.T8 (the reply attributed to મકદુમભાઈ, `એવું લાગે છે` kept, no figure beyond the page) and M2.S4.T9 (see D-3). The soft rows (M2.S3.T5 ક્ષેત્ર, M2.S4.T8 સુરક્ષા) are honoured too: the hosts' speech is quoted as printed (`મે’માનો`, `આંઈ ઢોલિયે`, `હંધાય હારું`, `લ્યો તમે કહો તો`, `હાલ્યા આવો`), દાદા gives the meaning and does not correct, and no word of theirs is called ખોટું or અશુદ્ધ.

**Contract (12 invariants).** (1) `phase: 2`, `plan_id` = `{chapter_id}_v1`, `chapter_id` `gseb_eng_gujarati8_ch18`, `unit_number` 18, `topic_number` 18; `chapter_name` equals the printed title. (2) as B. (3) 14 concepts `C1`–`C14`, chapter-continuous, each with a registry-resolving `objective_id` inside its topic's `objective_ids` and non-empty `content[]`. (4) registry: unique ids, every `home_topic_id` and `anchor` resolves, `strand_to_objective_map` covers L1–L9, every topic's `objective_ids` resolve. (5) all nine inline mirrors match the registry character for character. (6) media ids match `MEDIA_ID_RE` with real concept ids; recalls `{topic}.RQ{n}` with `legacy_id` `.TR{n}`, no `.SR` anywhere; `publication_id` is 1 (non-null, provisional); `topic_type` is the authored `STORY_TELLING` on all nine, which Agent 14/15 maps to `instructional` at emit (the same convention as the sibling plans, which carry `POEM`, `STORY_TELLING` or `CONCEPT` in `13_merged.json`; the emitted logical plan already carries `instructional`). (7) no સ્વાધ્યાય topic; inventory answered. (8) summaries strictly increase. (9) zero digits (ASCII or Gujarati) in any authored display field, media titles, descriptions and teaching notes included, and zero `કડી 2`-style references. (10) see Media. (11) vacuous. (12) the one `depends_on` (`M2.S4.T9` → `M1.S1.T1`) resolves; `source_topic_ids` are empty.

**Exercises.** Both inventoried blocks (`શબ્દસમૂહ માટે એક શબ્દ આપો.`, 8 items; `રૂઢિપ્રયોગ :`, 1 item) appear in `10_exercise_solutions.json` with their headings character for character, including the space before the colon. `coverage_report.blocks_found` has 2 entries and equals the inventory length; `unanswered` is `[]`; item counts match (8 + 1). `unmapped` is **reported, not emptied**: EX3 વામકુક્ષિ, EX5 જીર્ણોદ્ધાર, EX7 ક્ષિતિજ, EX8 જીવાદોરી occur in no reading sentence and no mapping was invented. EX9 maps by meaning only (`લીન થઈ જવું` ↔ `મગ્ન`), and the file says so. All nine answers are printed on the page, so none is a model answer. The four unmapped words appear in no authored field of the plan.

**Publication.** Every topic has `publication_text` (equal to `16_publication.json`). `publication_chunk` begins with `original_chunk` **byte for byte** on all nine, then a blank line, the rewritten explanation (equal to `publication_text` on 9 of 9), a blank line, the rewritten example. `concept_publication` matches the paragraph blocks of `concepts[].content[]` by index and by count on every concept (32 entries over 14 concepts); list blocks carry none. No `બાળકો`, `જુઓ`, `બોલો`, `વાંચો`, `યાદ કરો`, `તમને`, `તમારા`, `તમારી` survives in any `publication_text`; no Roman, Devanagari or `।` in any publication field. Token audit by A16 (read again here): the only words added in the rewrite are `પાઠમાં`, `પડે`, `શરૂઆતમાં`, `આ`, `બે`, `વાતો`, all connectives for removed imperatives. No meaning added. The one literal-spec shortfall is Flag 1.

---

## E–G (reported)

- **E — exercises and risk.** Answered 9/9 items in 2/2 blocks; sensitivity notes applied in the authored layer as guided (flagged, not censored). Personal-opinion items: none printed. The four unmapped items are reported above.
- **F — shape and media.** The 12 invariants hold. `chapter_id` is the synthetic ch18 the run context requires (purak lesson 3 continuing after std 8's 15 numbered chapters and after purak01 as ch16; provenance is in `01_meta.json` `extraction_notes`). `gseb` / `eng` are still the provisional VERIFY-1 segments. `ordering` is not written; `05b_textbook_order.json` equals the logical traversal, so **A14/A15 should raise `{human_confirmation_required: true, reason: "textbook order is identical to logical order"}`**, which is the correct output for this form, not a defect.
- **G — the seven mistakes.** None present: not a સાર + બોધ + પ્રશ્નોત્તર (explanations are stop-first and no બોધ is forced); no દુહા merged and no પદ split; no ટેક (none printed); no poetic licence corrected (`મે’માનો`, `હંધાય`, `હારું`, `હાવજ`, `આંઈ`, `હાલ્યા` all kept); no અલંકાર named; no adult or foreign `real_life_example` (મેળાની આગલી રાત, શેરી ક્રિકેટ, પહેલું ઝાપટું, છકડો, ઈદની સેવૈયા, લાઇટ ગયેલી રાતે ઓટલો, એસ.ટી. ડેપો, ટેન્કરની સવાર, નાતાલનું કૅરલ; no domain repeats its predecessor); no સ્વાધ્યાય cut as a topic.

### Flag 1 — `publication_chunk` shape (spec conflict; not an A–D item; corrected evidence this time)

Taken literally, this spec's *"`publication_chunk` is byte-identical to `original_chunk`"* fails on **9 of 9** (`publication_chunk` = `original_chunk` + rewritten explanation + rewritten example). What is protected, that the verbatim is never touched, holds on 9 of 9 (byte-exact prefix). Agent 16's spec says *"The verbatim `original_chunk` stays verbatim **inside** it"* (`agents/16_publication_authoring.md`, `## publication_chunk`), and Agent 16 did exactly that, so the specs conflict and the failure type (missing, index-mismatched, added meaning) that this spec routes to A16 is not the one found. **Correction to the previous report, which said the whole shipped corpus follows A16's append shape:** read from the sibling `output8/*/16_publication.json` and `13_merged.json` files (read-only), the append shape is used by the verse plans (ch01, ch07, ch10, purak01) but **all eight prose plans (ch02, ch03, ch05, ch08, ch11, ch13, ch14, ch15) carry `publication_chunk` identical to `original_chunk`**, as this spec reads. purak03 is prose and so departs from its prose siblings. I have not raised it as a blocker for the same reason as before (a re-route would send A16 against its own spec, and the failure is not in the routed list), but the orchestrator should decide. If strict identity is wanted for this prose unit: A16 re-run with `publication_chunk := original_chunk` and `publication_text` unchanged, then A13 re-merge; nothing else moves.

### Observations (none blocking)

  - **M2.S3.T6, the third hedge.** `07` lists three hedges for the hosts' reassurance: `લગભગ`, `કોઈ વાર` and `ક્યારેય … ઉપાડી જાય`. The A12 and A16 fields carry the first two (explanation, detailed summary, `important_points`, RQ3, the second concept's paragraph) and never the third; the calf clause appears only in A5's `modified_chunk`. The `summary` carries `માણસને ન વતાવે` beside `લગભગ` only (no `કોઈ વાર`), and no A12 or A16 field carries the calf clause at all. Every field that carries `માણસને ન વતાવે` or the buffalo arrangement attributes it to `ત્યાં રહેનારા`, none states it as a fact about lions, and the explanation says plainly `જાતે અજમાવવાની નહિ`, so this gate reads the hedge list as the hedges each field's own quotation reaches, and does not raise it as a hard miss. It is the nearest thing to one in the plan. If the orchestrator reads 07's list as per-field, the minimal fix is one clause in M2.S3.T6's explanation or RQ3 answer (A12, then A16 re-mirrors `publication_text`), with the explanation already at 85 of 90 words so the clause must be paid for by a trim, never a wider band.
  - **M2.S3.T6's name** `… સિંહ સાથેની નિરાંત`. All printed words and clear of `આંગણે`, but `સિંહ સાથેની` can be read as ease beside a lion, whereas the page's `નિરાંતે જમ્યાં` is the dinner after the lions were seen. Soft, given `08`'s સુરક્ષા row; a name built only from the dinner and the family (`સિંહ-પરિવાર અને વાળુ`) would not carry that suggestion if A2 is ever re-run.
  - **M2.S4.T8's explanation opens on an instruction**, `સફારીમાં ત્રણ ભાગ જુદા પાડો.`, which names the safari but not a particular stop. It passes profile Avoid 1 (the safari is the matter), and A16's rewrite makes it a statement.
  - **A5 `key_terms` gaps that 07's CORR asked for** (soft, deliberately left by A5, still open): M1.S2.T2 has no `જરા — અહીં શિકારીનું નામ, ‘થોડું’ નહીં` and its `પસ્તાવો — પોતાની ભૂલ માટે …` says `ભૂલ`, which the chunk never says of જરા (the authored fields use `કરેલી વાત માટે`); M2.S3.T4 has no `ને — અહીં ‘અને’`. A12 handled both in prose, bullets and recall. Both topics already hold six key terms, so a fix means swapping one out.
  - **Narrator bars vs the chunk.** All nine narrator strings are verbatim substrings of their own topic's chunk (scripted), and the exact string is named in each prompt. Three are fragments trimmed before the verb or the printed final mark (M1.S1.T1 `અમદાવાદની ખુશનુમા સવાર` vs printed `… સવાર હતી.`; M2.S3.T5 `ફીણવાળું શેડકઢું દૂધ`; M2.S4.T9 `દહીં, થેપલાં, ભાખરીનો નાસ્તો` vs printed `… નાસ્તો કર્યો.`); the other six are whole printed clauses.
  - **Pacing.** M2.S4.T9 (30 words) and M1.S2.T3 (73 words, the evening આરતી rides as the second concept) are short and M2.S3.T6 (269 words) is long; uneven length, reported by Agent 4, never a block.
  - **દર્શન** is glossed as `આદર કે નવાઈથી જોવું` in two topics and plain `જોવું` in two; compatible (A16 noted it).
  - **Root `genre`** is Agent 1's descriptive Gujarati string, as in the other std-8 plans; the contract's example shows a roster slug, and `output7/ch15` carries `patra_pravas`. The corpus is not consistent; not blocked. Root `topic_title` is set to the unit title, as in every sibling plan, because `01_meta.json` carries no `topic_title` and the contract lists the key.
  - **Marker accounting.** Five `[[પડાવ]]` markers stand for nine topics (above). The profile's rule (cut by stop, never by paragraph) is what the nine topics follow.

## Media

`reuse_report`: **scenes 9, reused 0, authored 9, rejected []**. Scenes equal the nine topics whose `available_content_types` carry `"image"`; one node per topic, ids `M1.S1.T1.C1.IMG1`, `M1.S2.T2.C2.IMG1`, `M1.S2.T3.C4.IMG1`, `M2.S3.T4.C6.IMG1`, `M2.S3.T5.C8.IMG1`, `M2.S3.T6.C9.IMG1`, `M2.S4.T7.C11.IMG1`, `M2.S4.T8.C12.IMG1`, `M2.S4.T9.C14.IMG1`, each matching `MEDIA_ID_RE` and naming a real concept of its own topic. Every node has `image_url: ""` **and** a non-empty `generation_prompt` (no `[reused frame: …]` stamp anywhere); every `negative_prompt` carries `Devanagari script labels` (and `Roman script labels`). **One `2d_tool`** in the chapter, a route strip on M2.S4.T9 (null on every other topic); it names nine stops in the text's own order between two `અમદાવાદ` ends, and every printed line it quotes is verbatim in the chunks (scripted). Six of the nine card labels are verbatim printed words; three (`ભોજદે ગામનું રિસૉર્ટ`, `શંકરદાનનું ઘર`, `સાસણનું કાઉન્ટર`) are composed from printed words (`ભોજદે ગામના એક રિસૉર્ટ`, `આ આપણું ઘર`, `સાસણ … કાઉન્ટર`) and add no stop the text does not name; reported for A9 to see, not blocking. No real person is authored into any image; the two real photographs (a golden-stone temple, p.141; a lion, lioness and cubs, p.143) are page matter and no prompt copies them. Media titles, descriptions and teaching notes carry no digit and no Latin letter.

What the re-write changed, in short: T9 loses the resort (D-3); T6's title and description now say the guests watch from the ઢોલિયો and `teaching_notes` states that the page does not say where the lions were and that the painter keeps them far off, not in the yard or house, because `વાડામાં આવી જાય તો` is ચેતનાબેન's fear and not an event; T5 no longer hangs pictures on a wall (the chunk says only `આ ચિત્રો જોયાં ? આ અહીંની કળા છે`) and bars `pictures hung on the wall`; T4's `only a local can lead you` mood line is gone; T3's `ઘૂંટણ સુધીના` is out of the description. Soft remainders, per the profile Priors ("the scene as the text describes it and nothing more"), reported and not gated against 07's prose rules: T3's prompt still has the children wading to the knees; T6's prompt chooses an evening hour and a position for the lions (far across open ground at the tree line) that the chunk does not print, which its own `teaching_notes` says; T4's rider is drawn as a lean middle-aged host in an embroidered-collar shirt, a cast choice for a man the chunk gives no description. A9 may revisit any of these.

## Gaps

- **`11_pages.json` now exists** (A11, confidence medium). Its `textbook_pages` (`141–145`, printed folios read off the page-number bars of renders 1 and 5, matching the 5-page PDF and the board-profile row) and `textbook_url` (`../Textbooks-pdf/std-8/purak-03-somnath-sasan-ne-savaj.pdf`, a local path; no hosted URL exists) are the values merged; they equal `01_meta.json`'s. Fail-soft: never a block.
- **`textbook` is `null`.** The std-8 cover has not been read and the board profile marks the title unconfirmed; nothing was composed. Sibling plans are inconsistent (some carry `ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8`; `ch03`, `ch04`, `purak01` carry `null`); this unit follows the latter.
- **`chapter_master_id: null`** by design (no real GSEB master row exists for a પૂરક unit under a synthetic ch18 identity; never invented). **`publication_id: 1`** and `estimated_time: 1.5` are the corpus defaults, provisional until VERIFY-2 and a per-grade review. `medium_id`, `subject_ref_id`, `english_plan_id`, `english_chapter_id` are `null`; a Gujarati chapter has no English twin.
- **`- સંકલિત` is in no `original_chunk`.** Agent 5 ruled it a compilation credit printed under the title, not a writer's name and not at the foot (the same ruling as the sibling prose plans, whose last chunks also carry no credit), and it stays in `00_chapter_normalized.md`. The checklist assumes an attribution line in the last topic; for a credit with no name this is page-faithful. If the orchestrator rules that a printed credit must travel with the text, Agent 5 offered the one-line alternative (head of M1.S1.T1's chunk, `word_count.original` 147 → 149).
- **One letter read from glyph shape.** Agent 1 transcribed long `ઈ` (not `ઇ`) in ઈંતેજારી, મોટરસાઈકલ, ડ્રાઈવર, ગાઈડ, આઈડિયા, ઈન્ટરવ્યૂ from the glyph; Agent 5 re-checked ઈંતેજારી, આઈડિયા and શંકરદાનભાઈ on 3x–4x crops but states that ગાઈડ and ડ્રાઈવર on p.144 were read at 1x and in a partly cut crop. The std-8 inventory's `ઇંતેજારી` (short ઇ) disagrees with the page; the page wins. No render was opened in this pass: `00_chapter_normalized.md` answered every question.
- **The dash between phrase and answer** in the eight one-word items varies in stroke weight on the page; Agent 1's single `–` is kept (Agent 10 noted it). A weight difference, not a different character.
- **Stale downstream files.** `learning_plan_logical.json`, `exercise_solutions.json` and `exercise_solutions.md` (all 22:18) were emitted from the previous merge. `learning_plan_logical.json` still carries the pre-D-3 T9 media (`આંબાવાડિયાના ઉતારે …`, the mango-grove prompt) and the older media text of the other eight nodes. Agent 14/15 must re-emit from this `13_merged.json`; `10_exercise_solutions.json` itself did not change.
- **Context routing.** All six policy documents this spec cites and the `patra_pravas` profile were routed and read in full. To confirm Flag 1 this pass read `agents/16_publication_authoring.md` and the sibling `output8/*` publication and merged files (read-only); it did not edit or re-run anything of A16's or anyone else's. Nothing else the spec cites was missing.
- **Agent 4's `notes[]` (all reported, none blocking):** the evening આરતી as a second concept rather than a topic; uneven topic lengths; the cut at `લીધો` / `બીજે દિવસે` with no printed full stop between; `topic_type` `STORY_TELLING` on all nine, mapped at emit.

## Routing

No A–D blocker, so nothing is routed. Not re-run, and not needed: A1, A2, A4, A5, A7, A8, A10, A11, A12, A16. Re-run needed downstream: **A14/A15** (re-emit `learning_plan_logical.json`, the textbook plan if one is emitted, and `exercise_solutions.json/.md` from this merge), then Phase 8. Two optional routes are the orchestrator's call and are not part of this verdict: Flag 1 (A16 sets `publication_chunk := original_chunk`, then A13 re-merge) and the M2.S3.T6 third hedge (A12 then A16).

## LP2 validator

Filled in Phase 8. The previous record is kept below as history; it was taken on `learning_plan_logical.json` built from the **previous** merge (the one that still carried the D-3 media), so it is **not evidence for this merge**. It must be re-run on the re-emitted plan.

Validation attempt 1 (2026-10-06 22:18, previous merge):

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

**Verdict (previous merge):** Valid — validation_errors is empty.

Validation attempt 2 (2026-10-06 22:44, current merge):

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

**Verdict (current merge):** Valid — validation_errors is empty.
