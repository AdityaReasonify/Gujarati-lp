# DESIGN BRIEF — gujarati-lp (parallel pack to hindi-lp)

**Audience.** Independent authoring agents, each writing exactly ONE file of the new `gujarati-lp` pack. You will NOT read any hindi-lp file except the single one you are porting. Everything shared — pipeline shape, contracts, id grammar, canonical Gujarati decisions — is in THIS brief. Where this brief and your source file disagree on a shared invariant, this brief wins (several hindi-lp files carry known stale errors, listed in §2 and §4).

**The one-sentence mission.** hindi-lp teaches CBSE Hindi literature through its genre (विधा) instead of the failure default "summary + moral + Q&A". gujarati-lp does the same for **GSEB Gujarati (second language), std 6–10**, with textbook sources as **local PDFs in `../Textbooks-pdf/std-N/`**, everything child-facing in **Gujarati script (Unicode U+0A80–U+0AFF)**, and the same LP2 phase-2 server contract byte-for-byte.

---

## 1. Pipeline overview

### 1.1 What the pack is

A prompt-pack: an `orchestrator.md` controller that dispatches numbered agent specs (`agents/NN_*.md`), parametrized by genre profiles (`profiles/genres/`), a board profile (`profiles/boards/`), and reference docs (`reference/`), producing per chapter four deliverables:

1. `learning_plan_logical.json` (primary)
2. `learning_plan_textbook.json`
3. `exercise_solutions.json` (+ rendered `.md`)
4. `validation_report.md`

Quality comes from the agents; integrity from the orchestrator. Motto and anti-pattern carry over verbatim.

### 1.2 Agent roster (note: there are NO agents 03 or 06 — the gaps are intentional; keep the numbering)

| # | File | Role | Output |
|---|------|------|--------|
| 01 | `agents/01_ingestion_genre_diagnosis.md` | Ingest + normalize verbatim + diagnose genre + inventory સ્વાધ્યાય | `00_chapter_normalized.md`, `01_meta.json` |
| 02 | `agents/02_structure.md` | Cut Module→Segment→Topic→Concept by explanation unit; build objectives[] registry | `02_structure.json` |
| 04 | `agents/04_mapping_convergence.md` | Single structure-validation pass; freeze ids on pass | `04_validation.json`, `04_converged.json` |
| 05 | `agents/05_verbatim_attachment.md` | Attach exact verbatim `original_chunk`, `modified_chunk` seed, `key_terms`; textbook order index | `05_with_content.json`, `05b_textbook_order.json` |
| 07 | `agents/07_genre_pitfalls.md` | Instantiate genre avoid-list as testable per-topic checks + misconceptions | `07_pitfalls.json` |
| 08 | `agents/08_sensitivity_safety.md` | Flag-and-guide sensitive content (never censor); always emits | `08_sensitivity.json` |
| 09 | `agents/09_media_planning.md` | One image per reading scene; ≤1 `2d_tool`/chapter; concept-scoped ids | `09_media.json` |
| 10 | `agents/10_exercise_solutions.md` | Sole home of textbook exercises; every block answered, skill-tagged, mapped | `10_exercise_solutions.json` |
| 11 | `agents/11_pagination_source.md` | Textbook name + page range; fail-soft, never blocks | `11_pages.json` |
| 12 | `agents/12_runtime_authoring.md` | All teaching prose: explanation, real_life_example, summaries, recall, craft fields | `12_authoring.json` |
| 13 | `agents/13_assembly_validation.md` | Merge + full QC gate; names owner on hard fail | `13_merged.json`, `validation_report.md` |
| 14 | `agents/14_logical_plan.md` | Reading order, consecutive renumber, reference translation, key whitelist | `learning_plan_logical.json` |
| 15 | `agents/15_textbook_plan.md` | Same nodes, printed order (in practice same sequence + flag) | `learning_plan_textbook.json` |
| 16 | `agents/16_publication_authoring.md` | Publication-register rewrite (runs parallel to 12) | `16_publication.json` |

### 1.3 Phases and data flow

- **Phase 0 Setup** — create `output{N}/<chapter>/` (see §3.7 for directory convention); version defaults 1; copy the chapter PDF from `../Textbooks-pdf/std-N/` into `book/` (no download — GSEB sources are local files).
- **Phase 1** — Agent 1: ingestion + genre diagnosis. Load matching genre profile(s) from `profiles/genres/`, dominant-first. If `genre_confidence: "low"`, STOP and ask before anything else runs.
- **Phase 2** — Agent 2 cuts the tree and builds the objectives registry; Agent 4 runs ONE validation pass (genre fidelity is a hard gate; full reading-scene coverage; one sound text-grounded objective anchor per scene; phase-2 id contract). On PASS promote `02_structure.json` → `04_converged.json`. On blocking fail: name ONE owner (A1 = genre/unit/lens wrong; A2 = cut/coverage/objectives wrong), re-run that owner once, revalidate once. Second failure → stop and surface to a human. No loop.
- **Phase 3 Freeze** — `04_converged.json` canonical; M/S/T/C ids and objectives[] frozen; ids renumbered consecutively only at Agent 14.
- **Phase 4** — Agent 5 verbatim attachment. Hard rule: complete verbatim Gujarati script, nothing dropped, paraphrased, or transliterated.
- **Phase 5** — Agents 7, 8, 9, 10 (needs 7's output), 11.
- **Phase 6** — Agent 12 and Agent 16 in parallel.
- **Phase 7** — Agent 13 merge + QC (hard fails block); Agent 14 → logical plan; Agent 15 → textbook plan (raise `human_confirmation_required` if orders identical); copy `10_exercise_solutions.json` → `exercise_solutions.json` (+ render `.md`).
- **Phase 8 (never skipped)** — POST the plan to the LP2 validator (§2.5). Zero `validation_errors` or the run is not done. Fix the pack/plan, never the validator. Upload is a separate, explicitly-requested step.

Orchestrator reading order: `author.md` first, then reference files in this order: `no_hallucination_policy.md`, `genre_diagnosis.md`, `teaching_lens_map.md`, `explanation_unit_map.md`, `teaching_block_format.md`, `gujarati_verbatim.md`, `alankar_chhand.md`, `shabd_gloss.md`, `teaching_voice_gu.md`, `global_content_rules.md`, `naming_conventions.md`, `phase2_contract.md`, `loop_protocol.md`, `json_contract.md`, `qc_checklist.md`. Every authoring agent additionally receives: `author.md` + `no_hallucination_policy.md` + `global_content_rules.md` + `teaching_voice_gu.md`.

### 1.4 File map of `output{N}/<chapter>/`

`00_chapter_normalized.md`, `01_meta.json`, `02_structure.json`, `04_validation.json`, `04_converged.json`, `05_with_content.json`, `05b_textbook_order.json`, `07_pitfalls.json`, `08_sensitivity.json`, `09_media.json`, `10_exercise_solutions.json`, `11_pages.json`, `12_authoring.json`, `16_publication.json`, `13_merged.json`, `validation_report.md`, `learning_plan_logical.json`, `learning_plan_textbook.json`, `exercise_solutions.json` (+ `.md`).

### 1.5 Issue-routing table (orchestrator §N4 — keep structure exactly)

wrong genre/lens/unit → A1; merged units (two દુહા joined / પદ split) → A1→A2; wrong board/grade/plan_id → A1; wrong topic cut → A2→A4; bad objective/anchor → A2→A4; explanation flattens the genre or ભાવ missing/overdone → A7→A12; missing/paraphrased/transliterated verbatim → A5; અલંકાર named but not present → A12→A13 (drop it; `[]` is correct); wrong Gujarati voice → A12 vs `teaching_voice_gu.md`; media mismatch → A9; exercise unanswered/unmapped/cut-as-topic → A10 (+A2); summaries/bullets/recall → A12; publication text → A16; merge/extra fields/QC → A13; LP2 validation_errors → A13→named owner; ordering/non-consecutive ids → A14/A15. Always re-run the minimal set, then A13→A14→A15, re-QC, then Phase 8.

---

## 2. Invariants — must be IDENTICAL in the Gujarati pack

These are server-verified mechanisms. Do not "improve" them, do not translate JSON keys, do not change id formats.

### 2.1 Phase-2 contract

**Root: `phase: 2` (literal), exactly these 32 root keys, all present:**
`board genre grade level phase author modules plan_id subject version ordering textbook _activate medium_id chapter_id objectives unit_title topic_title unit_number chapter_name textbook_url topic_number teaching_lens estimated_time publication_id subject_ref_id textbook_pages english_plan_id guiding_question chapter_master_id english_chapter_id strand_to_objective_map`

Sample values for Gujarati: `board: "gseb"` (VERIFY-1, §7), `subject: "Gujarati"`, `grade: 6..10`, `level: "standard"`, `ordering: "logical"` (`"textbook"` in the textbook plan), `author: ""`, `_activate: false` (server-owned), `medium_id: null` and `subject_ref_id: null` (server-injected; write null unless a real GSEB subject record is confirmed), `publication_id` non-null (server rejects null; GSEB's publication row must be looked up — VERIFY-2), `chapter_master_id` from `upload_reference/chapter_master_map.json` (required for upload; GSEB rows must be fetched, never invented), `estimated_time: 1.5` (review per grade), `english_plan_id`/`english_chapter_id`: null (a Gujarati chapter has no English twin — never invent one).

**Objectives = a plan-level registry. No per-topic objective pair. Ever.**
Each `objectives[]` entry: `objective_id "O{n}"`, `legacy_id "L{n}"`, `strand "L"`, `strand_name "ભાષા અને સાહિત્ય"`, `objective_text` (12–30 Gujarati words, grounded in THIS scene, could fit no other chapter), `bloom_level` (Capitalised here, e.g. "Understand"), `home_topic_id "M1.S1.T1"`, `anchor: ["M1.S1.T1.C1"]`, `status: "taught"`, `theme_category: null`. Root `strand_to_objective_map` maps every `L{n}` → `O{n}`. Every topic carries `objective_ids: ["O1"]` plus an inline mirror in `learning_objectives[]` (same object + `image_examples: []`); the mirrored `objective_text` must match the registry **character for character**. There is NO `M1.S1.T1.P1`-style objective code anywhere (that is the English pack's phase-1 convention).

**Concept layer.** Every topic has `concepts[]`: `{concept_id, concept_name, objective_id, key_terms[], content: [{type:"paragraph", text, publication_text} | {type:"list", items[]}]}`. One concept is normal; two only when the topic genuinely does two separable things; wanting three means the cut is wrong.

**Id grammar (frozen after Agent 4; renumbered consecutively only by Agent 14):**

| Node | Format | Rule |
|---|---|---|
| Module | `M{m}` | |
| Segment | `M{m}.S{s}` | s runs across the WHOLE chapter, never restarts |
| Topic | `M{m}.S{s}.T{t}` | t runs across the whole chapter, never restarts |
| Concept | `M{m}.S{s}.T{t}.C{c}` | **c is chapter-continuous** (M1.S2.T3 carries .C3, not .C1); server rejects per-topic restart |
| Objective | `O{n}` (+ `legacy_id L{n}`) | flat registry; NOT renumbered by Agent 14 |
| Topic recall | `{topic_id}.RQ{n}` with `legacy_id {topic_id}.TR{n}` | bloom_level lowercase |
| Segment recall | `{segment_id}.RQ{n}` | **RQ, never .SR{n}** — SR is LP v1; the server rejects it. (hindi json_contract.md invariant 6 contains a stale SR line — do NOT copy it) |
| Media | `{concept_id}.{IMG|VID|2D|3D|SIM}{n}` | concept-scoped; `MEDIA_ID_RE = ^(?P<concept_id>M\d+\.S\d+\.T\d+\.C\d+)\.(?P<suffix>IMG|VID|2D|3D|SIM)(?P<n>\d+)$`; topic-scoped `M1.S1.T1.IMG1` is rejected |

**Topic: exactly these 31 keys:**
`media 2d_tool summary concepts topic_id key_terms depends_on difficulty topic_name topic_type word_count explanation brief_summary objective_ids modified_chunk original_chunk topic_category concept_bullets detailed_summary important_points publication_text recall_questions source_topic_ids publication_chunk real_life_example estimated_exchanges learning_objectives primary_content_type tertiary_content_type secondary_content_type available_content_types`
Poem topics add `figures_of_speech[]` and `rhyme_scheme`; the module adds `difficult_words[]` and `overall_rhyme_scheme`. Optional ભાષા-બોધ extras per topic (accepted and stored by the server; keep the romanized key names): `shabdarth`, `samanarthi`, `vilom`, `vyakaran`.

**`topic_type` in EMITTED deliverables is the closed server enum `instructional | summary | assessment`.** Intermediate files (Agents 02–13) use the authored enum `POEM | STORY_TELLING | CONCEPT | REVIEW`; mapping at emit: POEM/STORY_TELLING/CONCEPT → instructional, REVIEW → summary, EXERCISE → assessment. (hindi phase2_contract.md has an internal contradiction here; the validator-confirmed closed enum stands — write the Gujarati file without the contradiction.) `topic_category` is free text: `introduction / core / climax / transition / resolution`. Genre lives in root `genre`, never in topic_type.

**Media node keys:** `id, type:"image", subtype:"illustration", title, description, image_url:"" (until generated), aspect_ratio:"16:9", concept_id, home_concept_id, objective_id:null, image_category:"illustration", teaching_notes, negative_prompt, generation_prompt` (generation_prompt empty ONLY when image_url is a reused frame; both empty = defect).

**Ordering constraint.** LP2 validates ids against traversal position, so a genuinely re-sequenced textbook plan cannot validate. Emit BOTH plans in the logical sequence; record the true printed order via `05b_textbook_order.json` and raise `{human_confirmation_required: true, reason: "textbook order is identical to logical order", checked: "05b_textbook_order.json matches the logical traversal exactly"}` when orders match. Never renumber to defeat this; never pretend orders were compared when they were not.

### 2.2 Field-shape rules (identical bands; language becomes Gujarati)

| Field | Shape |
|---|---|
| `objective_text` | string, 12–30 words, a goal, Gujarati |
| `explanation` | 55–90 words, teacher voice, inline glosses at point of first use, deeper reading only where the passage carries it |
| `real_life_example` | 55–90 words, exactly ONE Indian anchor inside the child's experience, may end on a question |
| `brief_summary` / `summary` / `detailed_summary` | 1 sentence / 2–3 / 4–6 — **strictly increasing**, three depths of ONE account |
| `key_terms` | string[], `"શબ્દ — અર્થ"` em-dash format, 3–6 per topic |
| `concept_bullets` / `important_points` | string[], keyword-first `"કીવર્ડ — gloss"`, 3–4 lines |
| `recall_questions` | 2–3 per topic, Bloom-laddered, each with a real model answer; exact shape `{"id":"M1.S1.T1.RQ1","legacy_id":"M1.S1.T1.TR1","prompt","answer","difficulty":"easy|medium|hard","bloom_level":"remember|understand|apply|analyze|evaluate|create"}` (lowercase here vs Capitalised in objectives — keep the asymmetry, it is in the accepted reference plan) |
| `figures_of_speech` | `[{device, lines, note}]`; `lines` quotes EXACT words from that topic's `original_chunk`; `[]` is a correct, complete answer |
| `rhyme_scheme` | `{pattern, rhyming_words[], note}` or null for prose |
| `difficult_words` | module-level, 5–10, `{word, meaning, example}` — example is a FRESH everyday sentence, never the poem's line |
| `word_count` | `{"original": <int>}` from original_chunk |
| `estimated_exchanges` | small integer as a string, e.g. `"4"` |
| `2d_tool` | string or null; at most one per chapter |

Image `generation_prompt` is self-contained (setting, characters + fixed appearance, action, mood, style; never "the previous scene"/chapter name). Standing conventions: soft digital watercolour, vibrant textbook illustration style, 16:9, Indian setting by default; narrator bar carries one line of **Gujarati in Gujarati script**, naming the exact string. `negative_prompt` minimum: `photorealistic faces, anime style, western-only setting, Roman script labels, Devanagari script labels, watermark, blurry, cluttered background, anachronistic objects` (Devanagari added for the Gujarati pack). **Empty is a legitimate value** — `[]`/null beat invention, always.

### 2.3 Naming conventions and plan identity

`chapter_id = {board}_{medium}_{subject}{grade}_ch{unit_number}`, all lowercase. Provisional Gujarati form: **`gseb_eng_gujarati{grade}_ch{N}`** — the medium slot is the medium of instruction, NOT the subject language, and is the single most dangerous silent-failure item: a wrong value uploads clean but registers under the wrong medium DB column (this once mis-filed all 23 Hindi plans). **VERIFY-1 (§7) must resolve the real GSEB board/medium segments against the live server before the first upload.** `plan_id = {chapter_id}_v{version}`, no `_standard_` segment; server assigns the real version. Names (module/segment/topic) are descriptive, never numbered. No numbers in any display text (`"બીજી કડીમાં"`, never `"કડી 2માં"`); numbers only in ids and provenance fields.

### 2.4 Loop protocol (Agent 4 — verbatim mechanism)

One pass, three blocking check groups (genre fidelity / coverage / objectives+id contract), output shape `{"status":"pass|fail","checks":{genre_fidelity:{pass,notes[]},coverage:{pass,scenes,topics,notes[]},objectives:{pass,count,notes[]}},"blocking":[],"owner":"A1"|"A2"|null,"notes":[]}`. Pass → promote to `04_converged.json`, ids frozen. Fail → ONE owner, one re-run, one revalidation; second failure → stop and surface. Notes are not blocks: thin names, uneven lengths travel to Agent 13 as notes and never stop the run.

### 2.5 Validator and upload endpooints (LP2, staging)

Base `https://staging.singularity-learn.com/agentapi`, **no auth**. Endpoints:
- `POST /api/lp2/learning-plans/validate` (multipart `file=plan.json` → `validation_errors[]`; Phase 8 gate: zero errors)
- `POST /api/lp2/learning-plans/upload` (multipart + `chapter_master_id`, `created_by`; query `activate`, `force`)
- `PUT /api/lp2/learning-plans/chapter/{id}`; `POST /api/lp2/learning-plans/approve-draft {"plan_id":…}` (NOT v1's `draft_plan_id`)
- `GET /api/lp2/learning-plans/chapter/{chapter_id}?include_json=true` (plan at `body["data"]["plan"]["planJson"]`; read version/isActive off `data["plan"]`)
- `POST /api/topics/upload` (assets → `publicUrl`; bucket `learning_plan_assets`)

Six traps (keep all): no auth header; approve-draft key name; upload returns HTTP 200 with `success:false` on conflict — always check the flag; server assigns version; duplicate plan_id → 200 + empty validation_errors + `action:"validated_only"` + success:false — use `&force=true` or bump version; GET nests three deep. Staging DNS is flaky — retry 2–3×. Server-volatile keys (never diff, never hand-set): `plan_id, version, _activate, subject_ref_id, medium_id, chapter_master_id, created_by`. **Set `CREATED_BY`** on uploads (Hindi left it null and authorship was lost).

### 2.6 Standing rules (orchestrator rules 0–10, all kept)

`author.md` is design-logic authority; diagnose genre first; single validation pass with one owner re-run; verbatim before explanation (reject topics missing exact Gujarati-script `original_chunk`); genre-essence avoid-list is a hard gate enforced at A2/A4/A7/A12/A13; the two deliverables always ship together; freeze ids after validation, A14 renumbers; never fabricate (no invented અલંકાર or poet detail; `[]` is a valid answer); report progress at phase boundaries; one objective anchor per scene, one image per reading scene, ≤1 tool per chapter; the phase-2 contract is authoritative — any output failing it is a bug in the pack. Teaching vs testing separate: સ્વાધ્યાય blocks are NEVER topics; Agent 10 owns them.

---

## 3. Canonical Gujarati substitutions — apply these consistently in every file

### 3.1 Script rules
- Base script: **Gujarati, Unicode U+0A80–U+0AFF**. The purity check becomes: no Roman AND no Devanagari characters outside bracketed technical terms, e.g. `સજીવારોપણ (personification)`.
- No transliteration anywhere: not into Roman, not into Devanagari.
- Diacritics are content: માત્રા, અનુસ્વાર, ચંદ્રબિંદુ, હલંત/જોડાક્ષર (conjuncts like ક્ષ, જ્ઞ, ત્ર, શ્ર, દ્વ) exactly as printed. Gujarati has **no nukta** in normal use — drop the Hindi ज़/क़ examples; the load-bearing distinctions instead: ળ vs લ, શ/ષ/સ, anusvāra presence.
- Punctuation exactly as printed: GSEB Gujarati readers use `.` full stop — the Hindi "। not ." rule is **inverted**; never introduce `।`.
- Never "fix" the poet: archaic/dialectal/medieval Gujarati forms (સૌરાષ્ટ્રી, ચારણી, old Gujarati of નરસિંહ/મીરાં/અખો) stay as printed and get explained, not corrected. The poet's છાપ (signature, e.g. "ભણે નરસૈંયો", "મીરાં કહે") is part of the verse; the "— કવિ/લેખકનું નામ" attribution line belongs inside the LAST topic's original_chunk.
- Corruption-vs-licence tell: corruption = moved/swapped matra from a broken PDF text layer; genuine poetic licence changes the word/syllable count. The rendered printed page is the only authority; expect a fresh defect catalog for Gujarati legacy fonts (Shruti/Saumil/Terafont-class reordering bugs).

### 3.2 Vocabulary table (use these terms; be consistent)

| Concept (Hindi term) | Gujarati pack term |
|---|---|
| विधा (genre) | સ્વરૂપ (genre); JSON field stays `genre` |
| छंद (stanza unit) | કડી (stanza); છંદ = metre |
| दोहा | દુહો (also છપ્પો, સોરઠો where the text is one) |
| पद | પદ / ભજન |
| टेक (refrain) | ટેક / ધ્રુવપંક્તિ |
| घटना / स्मृति / तथ्य / तर्क | ઘટના / સ્મૃતિ / તથ્ય / તર્ક |
| अलंकार / तुक / लय / भाव | અલંકાર / પ્રાસ / લય / ભાવ |
| कवि-छाप | છાપ |
| शिक्षा (moral) | બોધ / શિખામણ; moralising = ઉપદેશ |
| अभ्यास (exercises) | **સ્વાધ્યાય** |
| भाषा की बात | ભાષા-બોધ / વ્યાકરણ block (exact headings per book, §3.4) |
| खड़ी बोली (register) | માનક/શિષ્ટ ગુજરાતી |
| word classes | તત્સમ / તદ્ભવ / દેશ્ય / આગત (ફારસી-અરબી, અંગ્રેજી) / કાવ્ય-રૂપ (poetic licence) |

### 3.3 Structural markers in `00_chapter_normalized.md`
One `[[…]]` marker line ABOVE the block it labels, never inside text: `[[કડી 1]]`, `[[દુહો 3]]`, `[[પદ 1]]`, `[[ટેક]]`, `[[ઘટના: …]]`, `[[સંવાદ: …]]`, `[[કવિ-પરિચય]]`/`[[લેખક-પરિચય]]`, `[[સ્વાધ્યાય: <exact printed sub-heading>]]`. Markers are scaffolding — stripped before anything is copied into `original_chunk`.

### 3.4 Exercise blocks
GSEB books use **સ્વાધ્યાય** with sub-blocks (typically: નીચેના પ્રશ્નોના ઉત્તર લખો, ખાલી જગ્યા પૂરો, જોડકાં જોડો, સમાનાર્થી/વિરુદ્ધાર્થી શબ્દો, રૂઢિપ્રયોગ, વાક્યપ્રયોગ, પ્રવૃત્તિ). **Do not assume this list**: Agent 1 inventories the exact printed headings per chapter from the rendered page (`exercise_inventory[{group, items, verbatim_heading}]`), and the board profile records the per-series banner inventory as it is actually measured. GSEB exercises weight grammar/writing more heavily than the CBSE reader — the mechanism (never a topic; Agent 10 answers everything) is unchanged.

### 3.5 Voice
`teaching_voice_gu.md`: second person, teacher-to-class, opener style **"બાળકો, જુઓ —"**; simple spoken શિષ્ટ ગુજરાતી, short sentences; Roman only in brackets for technical terms. Age anchor is **parameterized by standard** (std 6–10 ≈ ages 11–15), never a fixed "eleven-year-old". **Second-language calibration**: glossing density is higher and the "skip everyday words" bar lower than a first-language pack — an L2 child stops on more words; word-count bands (55–90 / 12–30) carry over but must be re-validated against measured GSEB chapters (VERIFY-4), and targets vs measurements are recorded separately. Real-life anchors: Indian, concrete, single, inside the child's world — Gujarat-flavoured anchors natural (શેરી ક્રિકેટ, ઉત્તરાયણ/પતંગ, ગરબા-નવરાત્રિ, મેળો, ST બસ, ખેતર-કૂવો, નર્મદા), scope stays India.

### 3.6 Sources
Textbooks are **local PDFs**: `../Textbooks-pdf/std-N/` for N in 6..10 (Gujarat State Board of School Textbooks; Gujarati દ્વિતીય ભાષા series). The board profile maps std+chapter → local file. `textbook` root field = the GSEB reader's printed title in Gujarati script per standard; `textbook_url` = the local path string until a hosted URL exists (record as a gap in `11_pages.json`, confidence accordingly). There is **no v1 plan corpus and no frame pool** for Gujarati: Agent 1's v1 cross-check is dropped (rendered page is sole authority), Agent 9's reuse step is dormant (author-only prompts), collage tooling ports but stays dormant until a Gujarati frame pool exists.

### 3.7 Ids, directories, DB values
- `chapter_id`: provisional `gseb_eng_gujarati{grade}_ch{N}` (§2.3, VERIFY-1). `subject: "Gujarati"`.
- Output directories: **normalize to `output6/ … output10/`**, chapters `ch01`-style zero-padded (drop hindi-lp's asymmetric `output` = class 6 and `ch4` class-10 quirks).
- Asset path template: `V2/{board}/{publication}/{medium}/class_{N}/gujarati/ch_{n}/image/{media_id}.png` under bucket `learning_plan_assets`; concrete segments resolved at VERIFY-2 — the Hindi pack's `english` medium folder was a verified quirk, **never assume it**. Always record the server-returned `publicUrl`; never hand-build a CDN string.
- `chapter_master_id`, `publication_id`, `subject_ref_id`, `medium_id`: fetched/confirmed from the education DB or post-upload readback; the Hindi values (354, 355−N, publication 1, subject_ref 84/90) do NOT transfer.
- Latin-script conventions that check_pack.py depends on: orchestrator refers to agents as `Agent N` / `AN` (Latin); genre profile filenames are ASCII lowercase slugs (`[a-z][a-z_]+\.md`); agents keep `NN_name.md` with frontmatter `name:` == filename stem plus `description:`, `inputs:`, `outputs:`.
- Machine-parsed English stamps stay English inside brackets: `[reused frame: …]`, `[collage of: …]` in `teaching_notes` (collage tooling regexes match them).

### 3.8 Renamed files (everything else keeps its hindi-lp path/name)
- hindi-lp's `devanagari_verbatim.md` (in its reference dir) → **`reference/gujarati_verbatim.md`**
- hindi-lp's `teaching_voice_hi.md` (in its reference dir) → **`reference/teaching_voice_gu.md`**
- hindi-lp's `cbse_hindi.md` (in its boards dir) → **`profiles/boards/gseb_gujarati.md`**
- hindi-lp's `hindi_learning_plan_skeleton.json` (in its schema dir) → **`schema/gujarati_learning_plan_skeleton.json`**
- `profiles/genres/*.md` → new Gujarati roster (§5); `alankar_chhand.md`, `shabd_gloss.md`, `bhasha_bodh.md` keep their names (terms transliterate identically).
Every file that cites a renamed path must cite the NEW name — `check_pack.py` fails on dangling in-pack paths.

---

## 4. Per-file porting spec

Legend — **KEEP** = mechanism identical, port verbatim (translate prose examples only where flagged). **RE-AUTHOR** = content must be rebuilt from GSEB sources. Every file also applies §3 substitutions globally (script, vocabulary, markers, voice, sources, ids).

### 4.1 Root files

**`orchestrator.md`** — KEEP: the entire phase skeleton 0–8, agent numbering/dispatch model, single-validation-pass protocol, freeze-then-renumber discipline, two-deliverable rule, the output file map (§1.4), the N4 routing table (§1.5), per-scene teaching block (objective/explanation/real_life_example), one-image/≤1-tool limits, phase-2 callout, LP2 endpoint usage, standing rules 0–10. RE-AUTHOR: "what the user gives you" = chapter file path OR std (6–10) + chapter number resolved via `profiles/boards/gseb_gujarati.md` to a local PDF in `../Textbooks-pdf/std-N/` (Phase 0 copies into `book/`, no download; chapter counts per standard from the board profile, not "1–13"); the teaching-model callout's genre examples become Gujarati (per-scene block per કડી/દુહો/પદ/ઘટના; સ્વાધ્યાય blocks are NOT topics); reference reading order uses the renamed files (§3.8); all Devanagari terms → Gujarati (§3.2). Keep `Agent N`/`AN` Latin references (check_pack).

**`author.md`** — KEEP: the five commitments (genre decides everything; exact words before explanation; explain then land it in the child's world; name the craft only where it works; teaching and testing are separate deliverables), the anti-pattern (સાર + બોધ + પ્રશ્નોત્તર), the accepted tensions, one-example/one-image disciplines, "[] is a correct answer". RE-AUTHOR: the genre inventory and its arguments rebuilt on Gujarati forms (દુહો = complete two-line argument; પદ = one sung utterance with ટેક; ગઝલ શેર-wise; વાર્તા by ઘટના etc.); looks-wrong-but-right examples from actual GSEB texts (medieval forms, છાપ lines) replacing यमुन/नहिं/खायो; craft example in Gujarati (સજીવારોપણ line); exercise names → સ્વાધ્યાય; register re-derived explicitly for **L2 learners, std 6–10** (not copied from first-language grades 6–8); note the 55–90 band is kept but flagged for L2 re-validation.

**`check_pack.py`** — KEEP verbatim (script-agnostic): path-resolution check, agent frontmatter check, orchestrator↔agent-number cross-check (`Agent(s) N` / `AN` regexes), genre-index↔profile-files bidirectional check, schema JSON parse. Only edit: docstring anecdote. The pack must satisfy its hard-coded layout (§3.7 Latin conventions).

**`_empty_images_report.py`** — KEEP: walk `modules→segments→topics→media`, empty-vs-filled split, host audit (every non-empty URL on `learning_plan_assets`), report layout (Summary table, wrong-bucket warning, The list, Prompts and target URLs), output name `EMPTY_IMAGE_URLS_class6_to_10.md`. RE-AUTHOR: `GRADES = [(6,"output6"),(7,"output7"),(8,"output8"),(9,"output9"),(10,"output10")]`; V2 URL template segments from VERIFY-2 (never copy `cbse/cbse/english/...hindi`); drop all Hindi-run history prose (unbuilt-chapter lists, collage-pass dates, `output10/_stage_assets.py`).

### 4.2 Agents (all keep frontmatter shape: `name`, `description`, `tools`, `inputs`, `outputs`)

**01_ingestion_genre_diagnosis.md** — KEEP: mechanism (ingest → verify extraction → normalize with markers-above-blocks → four-signal diagnosis → સ્વાધ્યાય inventory → emit meta; honesty about uncertainty; low confidence + a question is the correct output; do-not list). RE-AUTHOR: source = local PDF via board profile (no URL fetch); extraction checks with Gujarati conjuncts/matras (ક્ષ જ્ઞ ત્ર; reordered vowel-sign forms; joined verse lines); punctuation rule per §3.1; **drop the imagebyGPT v1 cross-check** — rendered page is sole authority; `01_meta.json` exact fields kept: `board, grade, subject, level, version, chapter_id, plan_id, chapter_name, unit_title, unit_number, topic_number, textbook, textbook_url, chapter_master_id, subject_ref_id, genre, genre_signals{structure,theme,exercises,purpose}, genre_confidence, active_genre_profiles, teaching_lens, guiding_question, explanation_unit, structure_inventory, exercise_inventory[{group,items,verbatim_heading}], extraction_notes[]` — values per §3.7 (id forms, GSEB textbook title, null DB ids until confirmed); `structure_inventory` counts Gujarati units (કડી, દુહા, પદ, ઘટના, ટેક occurrences); verse sub-diagnosis by unit length before theme (two-line self-contained → દુહો; sung પદ with ટેક → પદ; else કડી/છંદ); `guiding_question` derived from THIS chapter, never copied from the profile.

**02_structure.md** — KEEP: everything — unit-driven cutting, ids per §2.1, chapter-wide counters, root objectives[] registry with the exact objective object, `strand_to_objective_map`, one-concept-normal, topic_type/topic_category authored enums, no-numbers-in-names, exercises-never-topics, empty concepts[] shells, original_chunk stays empty, chapter-specific objective quality bar. RE-AUTHOR: genre→unit table (one દુહો per topic never merged; one પદ whole never split; one કડી per topic; changed-words ટેક is a topic at each occurrence; prose by ઘટના/સ્મૃતિ/તથ્ય/તર્ક); `strand_name: "ભાષા અને સાહિત્ય"`; objective examples in Gujarati ("કવિતાને સમજવી" fails; a chapter-specific સજીવારોપણ objective passes); difficulty calibrated per std 6–10 L2.

**04_mapping_convergence.md** — KEEP: the whole §2.4 protocol, three blocking check groups, marker-count equality checks (markers vs topics carrying them), exercise-never-topic cross-check against `exercise_inventory`, objectives/id-contract checks, output shape, owner table (A1 vs A2), notes-vs-blocks. RE-AUTHOR: only marker vocabulary (`[[દુહો]]`/`[[પદ]]`/`[[ટેક]]`/`[[કડી]]`) and the terms સ્વરૂપ/સ્વાધ્યાય.

**05_verbatim_attachment.md** — KEEP: copy-never-compose; stop-if-unclean; verse line breaks preserved; attribution line → LAST topic; strip `[[…]]` markers; `modified_chunk` = 2–4-sentence plain "what is happening" seed (no deeper reading, no અલંકાર, no real-life link); `key_terms` 3–6 in `"શબ્દ — અર્થ"` form; content-type fields (`primary/secondary/tertiary_content_type`, `available_content_types`; image-bearing scene = "image", text-only = null/[]); `word_count.original`; emit `05b_textbook_order.json` always. RE-AUTHOR: script checklist per §3.1 (માત્રા/અનુસ્વાર/ચંદ્રબિંદુ/જોડાક્ષર; no nukta; `.` not `।`); never-correct-the-poet and છાપ examples from GSEB texts; key_terms taxonomy તત્સમ/તદ્ભવ/આગત/કાવ્ય-રૂપ with an explicit L2 policy: the "skip everyday words" bar sits LOWER (more everyday Gujarati words genuinely stop an L2 child).

**07_genre_pitfalls.md** — KEEP: per-topic instantiation of avoid-lists into testable sentences; misconception+correction derived from THIS passage; output shape `{topics:[{topic_id, avoid_checks:[{check, profile, severity:"hard|soft"}], misconception, correction}], chapter_level:[]}`; hard severity blocks at A13; only-what-applies noise rule; per-part profiles in mixed chapters. RE-AUTHOR: worked examples from the Gujarati canon (નરસિંહ/મીરાં પદ, Gujarati દુહા, GSEB personification lines); profile slugs = the Gujarati roster's; misconception guidance gains an **L2 layer**: comprehension-level errors and Hindi/Gujarati false-friend confusions, per grade.

**08_sensitivity_safety.md** — KEEP: flag-and-guide never censor; output `{topics:[{topic_id, areas[], caution, guidance, severity}], chapter_level:[{area, guidance}], none_found}`; ALWAYS emit (empty = `{"topics":[],"chapter_level":[],"none_found":true}`); hard severity blocks at A13; guides how, never whether. RE-AUTHOR: framing names the GSEB reader series; typical instances from Gujarat (devotional પદ/ભજન across Hindu/Jain/Swaminarayan/sufi traditions; આદિવાસી communities of Gujarat named by their own names — ડાંગ, રબારી, ભરવાડ; Kutch/Saurashtra practices; historical episodes); standardize area labels in Gujarati script (ધર્મ, સમુદાય, ક્ષેત્ર, વિકલાંગતા, સંઘર્ષ, જાતિ-ભૂમિકા, સુરક્ષા) so A13 matches consistently.

**09_media_planning.md** — KEEP: one image per reading scene; ≤1 `2d_tool`; media ids `{concept_id}.IMG{n}`; media node shape (§2.1); output `{media:[…], "2d_tool":{topic_id, spec}, reuse_report:{scenes, reused, authored, rejected[]}}`; the one-sentence depiction test; same-chapter-only reuse principle and pool-size lesson (kept as doctrine); self-contained prompt rules and negative_prompt baseline (§2.2); per-genre image guidance PRINCIPLE (image the concrete scene, not the moral). RE-AUTHOR: **no Gujarati frame pool exists — Step 1 (reuse) is dormant**: every scene gets `image_url:""` + authored `generation_prompt`; `reuse_report` still emitted with `reused: 0` and `rejected: []`; drop the imagebyGPT scoring imports (Devanagari tokenizer is inapplicable); narrator-bar = exact Gujarati string; per-genre guidance rewritten for the Gujarati roster (દુહો → the દૃષ્ટાંત not the moral; પદ → relationship, domestic and warm, not iconographic; વાર્તા → the moment of choice, consistent likeness; સંવાદ/એકાંકી → both parties/the stage).

**10_exercise_solutions.md** — KEEP: sole-home rule; per-item shape `{exercise_id:"EX{n}", exercise_group, skill:"reading comprehension|vocabulary|grammar|literary device|speaking|listening|writing|values", prompt_verbatim, answer, explanation, acceptable_alternatives[], values_filled_for_teaching, teacher_note, is_model_answer, covered_by_topics[]}`; rules 1–8 (verbatim prompt incl. options; answer from the chapter; MCQ both-sides explanation; model answers marked; fill printed grids; map to preparing scenes, report unmapped never invent; language-study items still map; obey 07 avoid-lists); `coverage_report{blocks_found, blocks_answered, unanswered, unmapped}`; skipped block = hard fail at A13. RE-AUTHOR: block names = the સ્વાધ્યાય inventory (§3.4, from `01_meta.json`, never assumed); example items in Gujarati; grammar categories per GSEB (સંધિ, સમાસ, કૃદંત, નિપાત, રૂઢિપ્રયોગ…).

**11_pagination_source.md** — KEEP: fail-soft contract; source priority (printed folio in the local PDF → 01_meta fields + board profile → publisher contents page); output `{textbook, textbook_url, textbook_pages, source, confidence:"high|medium|low", gaps[]}`; never guess — empty range is fine, wrong range is not. RE-AUTHOR: board profile path → `profiles/boards/gseb_gujarati.md`; textbook example = GSEB title; tertiary source = Gujarat State Board of School Textbooks contents page; `textbook_url` = local path per §3.6.

**12_runtime_authoring.md** — KEEP: full field inventory and bands (§2.2); concepts[].content[] paragraph/list blocks; strictly-increasing summaries; RQ{n}/TR{n}; `estimated_exchanges` string; figures_of_speech exact-quote + []-is-correct (invented device = hard fail); rhyme_scheme honesty about near-rhymes; module `difficult_words` (fresh example sentences) + `overall_rhyme_scheme`; pitfalls/sensitivity obligations (ignored hard item blocks at 13); objective_text ownership stays with A2 (note errors, never rewrite); do-nots incl. no numbers in display text ("બીજી કડીમાં" never "કડી 2માં") and no forced બોધ. RE-AUTHOR: refs → `teaching_voice_gu.md`, Gujarati `alankar_chhand.md`/`shabd_gloss.md`; voice opener "બાળકો, જુઓ —"; terminology કાવ્ય/છંદ/ભાવ/પ્રાસ; age framing parameterized per standard; L2 glossing density per §3.5.

**13_assembly_validation.md** — KEEP: merge order (fold 12, 9, 16, 11, root fields from 01 onto `05_with_content.json`); drop working fields — only contract keys survive; QC split A–D blocking / E–G reported; mechanical checks (every original_chunk non-empty; marker-count equality; explanation AND real_life_example non-empty and in band; every hard 07/08 item addressed; figures_of_speech lines found verbatim in original_chunk; every inventoried exercise block answered); the 12 json_contract invariants; routing table (verbatim → A5; genre essence/invented અલંકાર/uncorrected misconception → A7→A12; prose fields → A12; media → A9; exercises → A10; structure/ids → A2→A4); never fixes authoring itself; report template with header, counts, `## A–D`, `## E–G`, `## Media`, `## Gaps`, `## LP2 validator`; partial pass never presented as pass. RE-AUTHOR: script check = "no Roman or Devanagari outside bracketed terms, base script Gujarati (U+0A80–0AFF)"; markers per §3.3; report header label "સ્વરૂપ: <genre> (confidence)".

**14_logical_plan.md** — KEEP: everything — arrange in reading order; renumber M/S/T/C consecutively (chapter-wide s/t/c counters, c chapter-continuous); build old→new map FIRST, then translate ALL references: `objectives[].home_topic_id`, `objectives[].anchor[]`, inline `learning_objectives[]`, `topic.objective_ids`, `recall_questions[].id/.legacy_id`, segment `recall_questions[].id`, `media[].id/.concept_id/.home_concept_id`, `concepts[].concept_id/.objective_id`, `depends_on`, `source_topic_ids`, `covered_by_topics` in the exercise deliverable; assert no stale reference (hard fail); O{n}/strand_to_objective_map NOT renumbered; whitelist = phase-2 keys + poetry extras (`figures_of_speech, rhyme_scheme, difficult_words, overall_rhyme_scheme`); root fields `ordering:"logical", phase:2`, DB fields per §3.7; emitted topic_type = closed server enum (§2.1). RE-AUTHOR: only id/DB values and the null english_plan_id/english_chapter_id rule restated for Gujarati.

**15_textbook_plan.md** — KEEP entirely: same nodes, same ids, `ordering:"textbook"`; platform-limit workaround (always emit logical sequence; true printed order in the flag); `human_confirmation_required` semantics; do-nots. Cosmetic: "કડી by કડી" phrasing.

**16_publication_authoring.md** — KEEP: rewrite contract (drop vocatives and direct instructions; keep every fact/gloss/reading; same script, register family, length band; ADDED meaning = bug); verbatim original_chunk stays verbatim inside `publication_chunk`; output `{topics:[{topic_id, publication_text, publication_chunk, concept_publication:[{concept_id, content_index, publication_text}]}]}` with index-matched concept blocks. RE-AUTHOR: example table in Gujarati ("બાળકો, જુઓ —" dropped, declarative rephrasing); "Keep it Gujarati script"; "not formal literary Gujarati — the reader is still a std-N child"; refs → `teaching_voice_gu.md`, `gujarati_verbatim.md`.

### 4.3 Reference — contract cluster

**`phase2_contract.md`** — KEEP: everything in §2.1/§2.5 (32 root keys, 31 topic keys, objective model + mirror rule, concept layer, id grammar incl. chapter-continuous c, RQ-not-SR, MEDIA_ID_RE, closed topic_type enum written WITHOUT the hindi file's internal contradiction, ordering constraint, media node shape, upload API + six traps, retry discipline, volatile keys). RE-AUTHOR: all values (board/subject/chapter_id forms per §3.7; textbook/teaching_lens/guiding_question examples in Gujarati; strand_name ભાષા અને સાહિત્ય); the "read this box first" table restated with GSEB-verified facts once VERIFY-1/2 complete — every CBSE-specific verified fact (eng medium, 355−N, publication 1, subject_ref 84/90) is provenance, not portable; the Gujarati pack re-verifies its first chapter against the validator the same way.

**`phase2_fetch.md`** — KEEP: endpoint + both bases, no auth, three-deep envelope (`body["data"]["plan"]["planJson"]`), planJson string-guard, include_json habit, both client patterns (lp_sync ApiClient; stdlib helper), retries, all seven traps, VOLATILE_TOP_LEVEL_KEYS diffing, modules→segments→topics walk, "read the server's copy" principle. RE-AUTHOR: id examples and the chapterMasterId table built from GSEB ids (enumerate `GET /chapters`, filter for the GSEB board value); re-verify the medium slot by reading the echoed `medium`/`subject` fields; verify-script inventory becomes Gujarati (`output6/_verify6.py` … per §3.7 directories, five grade loops).

**`json_contract.md`** — KEEP: all 12 invariants as mechanisms + whitelist + server-as-final-gate. RE-AUTHOR/FIX: (1) id pattern → GSEB form; (2) "non-empty **Gujarati-script** original_chunk, no Roman and no Devanagari outside bracketed terms"; (6) segment recalls written correctly as `.RQ{n}` — do NOT copy the hindi file's stale `.SR{n}` line; (7) સ્વાધ્યાય never a topic + full coverage; (9) Gujarati example strings; schema path → `schema/gujarati_learning_plan_skeleton.json`.

**`field_shape_rules.md`** — KEEP: §2.2 wholesale (types, bands, recall shape with bloom-case asymmetry, self-contained prompts, empty-is-legitimate). RE-AUTHOR: language = Gujarati; templates `"શબ્દ — અર્થ"`/keyword-first; narrator bar = Gujarati line; negative_prompt gains "Devanagari script labels"; ગદ્ય/છંદ terms; flag (not silently change) that bands await L2 re-validation (VERIFY-4).

**`naming_conventions.md`** — KEEP: §2.3 + the Agent-14 translation list + Agent-15 ids-stay rule + topic_type enum + no-`_standard_` + server-assigned version. RE-AUTHOR: segments gseb/gujarati{grade}; the medium-slot post-mortem retold as a WARNING with the two cross-checks (enumerate the corpus's medium usage; read the asset-bucket path segments) to be re-run for GSEB (VERIFY-1); strand name Gujarati.

**`qc_checklist.md`** — KEEP: A–D hard / E–G reported split; all of §B verbatim-fidelity discipline; §C teaching-block checks; §D genre-essence + no-forced-બોધ + empty figures_of_speech; §E exercise/sensitivity reporting; §F the 12 invariants + four server-rejected shape items (publication_id non-null, closed topic_type, segment `.RQ{n}`, chapter-continuous c) + media/summary/number rules; verdict format. RE-AUTHOR: §A genre layer on the Gujarati taxonomy; §B script wording per §3.1 with Gujarati archaic-form examples; §C voice = શિષ્ટ ગુજરાતી, age per standard, L2 calibration; §G seven habitual mistakes re-derived (items 4–7 carry: silently corrected licence, અલંકાર named for the field, adult/foreign example, exercises cut as topics; items 1–3 substitute Gujarati genres: સાર+બોધ+પ્રશ્નોત્તર default, દુહા merged, પદ split).

**`loop_protocol.md`** — KEEP verbatim (§2.4). RE-AUTHOR: only example vocabulary (દુહા not merged, પદ not split, ભક્તિ પદ not carrying a morality objective).

### 4.4 Reference — pedagogy cluster

**`genre_diagnosis.md`** — KEEP: four signals (A structure — verse sub-typed by UNIT LENGTH BEFORE THEME; B theme as tie-breaker; C exercise types reveal intent; D purpose); routing-tree form; conflicting signals → `genre_confidence:"low"` + surface; mixed-chapter protocol; the recorded-fields list for `01_meta.json`. RE-AUTHOR: the taxonomy and routing targets = the Gujarati roster (§5.3); signal-C exercise names from GSEB books; theme categories per GSEB (દેશભક્તિ, ભક્તિ, પ્રકૃતિ, હાસ્ય, ચરિત્ર…); all examples from GSEB chapters.

**`teaching_lens_map.md`** — KEEP: lens-per-genre table concept; one guiding question derived per chapter; the three agent responsibilities (A2 lens-serving objectives, A12 explanation through the lens, A13 sequence answers the guiding question); "the lens is not a template". RE-AUTHOR: whole table rebuilt on the Gujarati roster with Gujarati lens formulas (e.g. વાર્તા → ઘટના + પાત્ર + વળાંક; ભક્તિ-પદ → ભાવ + સંબંધ + લોકભાષાની મીઠાશ) and model guiding questions in Gujarati; consider an added language-acquisition dimension for L2 (vocabulary/usage alongside appreciation).

**`explanation_unit_map.md`** — KEEP: unit-per-genre mapping concept; the 5 hard cutting rules (exact verbatim; hook belongs to NEXT topic; single-theme topics with content-decided split/join — never for દુહો or પદ; સ્વાધ્યાય never a topic; changed-words ટેક = own topic each time, identical ટેક taught once then referenced); the "two units English has no name for" essay pattern (rewrite for દુહો and પદ); authored topic_type/topic_category enums (English values verbatim). RE-AUTHOR: table rows for the Gujarati roster; examples from GSEB texts; exercise names per §3.4.

**`teaching_block_format.md`** — KEEP: anchor-first linear block; the three parts in order (original_chunk → explanation carrying both layers → one real_life_example); migration note (old O1 વ્યાખ્યા → explanation, O2 દૃષ્ટિકોણ → real_life_example; NO per-topic objective pair); field-by-field table (all JSON names unchanged); strictly-increasing summaries; gradual release; name the સ્વાધ્યાય skill a topic prepares. RE-AUTHOR: examples in Gujarati; refs to renamed files; age per standard.

**`teaching_voice_gu.md`** (new name) — Most heavily re-authored file; see §3.5 for the binding decisions. KEEP: second-person teacher stance; bands 55–90/12–30; one-example rule; end-on-a-question device; Roman-only-in-brackets; no-numbers; no-ઉપદેશ/no-flattening; good/bad anchor criteria; calibration-samples section (write new Gujarati samples).

**`global_content_rules.md`** — KEEP rules 1–9 and 11 with §3 substitutions (script, block names, renamed refs, Gujarati ordinal examples, id schemes verbatim). RE-AUTHOR rule 10 on Gujarat's own communities/traditions (same dignity/accuracy principle: real names, never "tribal people"; devotional texts as literature with a living tradition; no comparative-religion turn).

**`no_hallucination_policy.md`** — KEEP all three rules + per-field empty-beats-invented list + fail-soft A11 + surface-gaps-as-success. Substitutions only: illustrative names → Gujarati-pack ones; refs → `gujarati_verbatim.md`; opinion-block name → the GSEB equivalent; અલંકાર/પ્રાસ terms; કવિ-પરિચય boxes: only what is printed.

**`exercise_alignment.md`** — KEEP: two-deliverables-together; per-item JSON + skill enum (English values); topic-id mapping; coverage_report; all seven rules; the A1/A10/A4/A13 responsibility chain. RE-AUTHOR: block-taxonomy table from the actual GSEB સ્વાધ્યાય apparatus per standard (inventoried, not translated from Hindi); grammar rows per GSEB syllabus; Gujarati example items.

### 4.5 Reference — language cluster

**`gujarati_verbatim.md`** (new name) — KEEP: six absolute rules as mechanisms (no transliteration; never fix the poet; diacritics are content; line breaks are structure; attribution line inside last topic; punctuation as printed); extraction-check workflow; rendered-page-is-authority; corruption-vs-licence tell; the `[[marker]]` scheme. RE-AUTHOR: every example per §3.1/§3.3 (Gujarati conjuncts, no nukta, `.` not `।`, GSEB extraction defect catalog built fresh, છાપ/dialect examples from Gujarati poets); drop the Hindi corpus notes and the v1 cross-check path entirely.

**`alankar_chhand.md`** — KEEP: no-invention top rule; JSON shapes (`{device, lines, note}`; `{pattern, rhyming_words, note}`; `{word, meaning, example}`); per-topic vs module split; depth guidance (name + quote + effect; 1–2 devices; no prosody lectures). RE-AUTHOR: device table from GSEB's own taught અલંકાર ladder per standard (વર્ણાનુપ્રાસ, ઉપમા, રૂપક, સજીવારોપણ, શ્લેષ, યમક at lower stds; ઉત્પ્રેક્ષા, વ્યતિરેક, અનન્વય at 9–10) with GSEB corpus examples; form facts for Gujarati (દુહો, છપ્પો, સોરઠો, ચોપાઈ, ઝૂલણા, ગઝલ, ગીત/પદ with ટેક); "a reader of THIS standard can actually see" framing per grade, L2-adjusted.

**`shabd_gloss.md`** — KEEP: stopping-point criterion; meet-again prioritization; concrete-not-dictionary style; point-of-use glossing; `"શબ્દ — અર્થ"` format; keyword-first bullets; printed-glossary trap (evidence, not source). RE-AUTHOR: taxonomy → તત્સમ/તદ્ભવ/દેશ્ય/આગત/કાવ્ય-રૂપ; nukta instruction replaced by ળ/લ, શ/ષ/સ, anusvāra distinctions; standard-form target = માનક ગુજરાતી; **L2 recalibration is the point**: an L2 child stops on far more everyday words — thresholds set per std band from measured chapters; Gujarati poetic-licence model sentence.

**`bhasha_bodh.md`** — KEEP: five-field schema with romanized keys (`shabdarth [{shabd, arth, prakar}]`, `samanarthi [{shabd, samanarthi[]}]`, `vilom [{shabd, vilom}]`, `vyakaran [{bindu, udaharan, note}]`, plus figures_of_speech); from-THIS-chunk rule; []-is-correct, vilom-emptiest; prepare-don't-compete sourcing; per-topic bands (3–6 / 2–4 / 0–3 / 2–3); sidecar `_bhasha_bodh.py` BB-dict merge mechanism; pattern-over-word rule for archaic-language chapters. RE-AUTHOR: `prakar` values → તત્સમ/તદ્ભવ/દેશ્ય/આગત/કાવ્ય-રૂપ; vyakaran allowed-list per GSEB grammar syllabus (નામ, સર્વનામ, વિશેષણ, ક્રિયાપદ, કાળ, વચન, જાતિ, સંધિ, સમાસ, કૃદંત, નિપાત, રૂઢિપ્રયોગ/કહેવત); ALL grade-ladder tables re-measured from GSEB std 6–10 સ્વાધ્યાય blocks (the Hindi class 3–5 measurements have no counterpart; L2 ladders run behind first-language ones); medieval-Gujarati section (નરસિંહ, મીરાં, અખો, પ્રેમાનંદ) with pattern glosses.

**`collage_media.md`** — KEEP as doctrine: one image slot per topic (`{concept_id}.IMG1`); authored-never-scored `_collage.json` (`topic_id → {why, panels:[[stem, title]]}` in reading order); PANEL_W≈1100, PANEL_MAX=4, 2–3 band; letterbox-never-crop; ordinal badges; white-margin/size checks; upward-search path resolver; named-list uploads never globs; record server publicUrl; assembler overlay with both files agreeing; the two guards; patch-not-reupload discipline with aspect map (2-stack 3:4, 3-stack 9:16, 2×2 1:1); collage-when-possible; never reuse a composite built against a different cut; never write to any v1 bucket. RE-AUTHOR: badges → Gujarati numerals ૧ ૨ ૩ ૪; mark the whole workflow **dormant until a Gujarati frame pool exists** (no v1 pools, no `[reused frame:]` stamps to seed from); upload path per VERIFY-2; drop Hindi shipped-state tables and incident history (keep the safeguards they motivated); `why` fields in Gujarati.

### 4.6 Profiles

**`profiles/boards/gseb_gujarati.md`** (replaces `cbse_hindi.md`) — Copy the SKELETON section-for-section; re-author all content from GSEB sources. Sections: (1) Reader table — GSEB Gujarati (દ્વિતીય ભાષા) reader per std 6–10, chapter counts, source = local files `../Textbooks-pdf/std-N/<file>.pdf` (per-chapter file table replaces the bucket-key tables; keep the discipline: page 1 of the render is the proof of WHICH chapter, never the filename). (2) Grade-band language — per-std comparison tables (explanation band, example reach, craft-naming ladder, closing-question ladder, sentence length) with **measured medians, L2-fresh**: measure the first chapter of every standard before authoring the second; record targets vs measurements separately so inversions can't hide; trim to band, never widen. Constants at every band: Gujarati script throughout, Roman in brackets on first technical use, second-person teacher voice, no lecturing, verbatim exactly as printed. (3) Ids — §2.3/§3.7 verbatim incl. the medium-slot warning and the two-author-ids rule (`chapter_master_id` + `publication_id` from the map; `subject_ref_id`/`medium_id` null unless a real record exists; never invented; dumps carry 0). (4+) Per-std chapter tables (# | chapter | chapter_master_id | pages | genre-prior with "diagnose, don't assume" caveat, ✓ = confirmed on rendered page). Text-layer defect catalog built fresh (render every page and read it). સ્વાધ્યાય banner inventory per reader, read off renders (reading-matter blocks vs exercises vs teacher-addressed blocks vs badges distinguished). SSC board-exam weighting note for std 10. Port the practice of logging every correction with date and page evidence — not the Hindi log entries.

**`profiles/genres/_genre_index.md`** — KEEP: the mechanism — four-signal routing; ASCII decision tree, VERSE split by unit length before theme, negative tests first; a one-line HARD constraint per branch; ordering-rationale paragraphs (write them only from actual Gujarati pilot evidence — port the habit, not the paragraphs); Master table columns `Profile | Lens | Explanation unit | Emphasise | Avoid (hard gate)`, one row per profile; the 5-step mixed-chapter protocol (genre:"mixed" dominant-first; load every profile; each part cut under its OWN unit; each part's lens/avoid to that part only, dominant sets guiding_question; A7+A13 verify no part lost its essence); the closing 4 bullets. RE-AUTHOR: the roster (§5.3) with ASCII slugs; appended-reading-matter conventions per GSEB books (the "block that looks like exercises but is a reading scene" rule, instantiated from actual books).

**Genre profile files** (each on the §5 template; write only after the pilot inventory fixes the roster):
- `varta.md` (વાર્તા; from hindi `kahani.md`) — near-total carry-over: unit = one ઘટના (small arc; typical shape પરિચય → ગૂંચ → સંઘર્ષ → વળાંક → પરિણામ); emphasise the turn, why a character chooses, dialogue as character, theme demonstrated never appended; avoid summary-only teaching, tacked-on બોધ, judging a sympathetic character, spoiling the turn early; media = the moment of choice, consistent likeness; recall remember/understand/analyze ladder.
- `duha_chhappa.md` (from `niti_doha.md`) — one દુહો/છપ્પો = one topic, never merged, no exceptions; extra section "How a દુહો is built, and therefore how it is taught" (line 1 picture from ordinary life → line 2 turn into a rule; explanation follows that shape); છાપ preserved; hard gates: merging (checked at A4), શિખામણ without the દૃષ્ટાંત, moral lecture, modernising medieval forms, invented biography; media shows the દૃષ્ટાંત not the moral; state the Gujarati form's own metre facts (દુહો/છપ્પો/સોરઠો), not 13+11.
- `pad_bhajan.md` (from `bhakti_pad.md`) — one પદ whole, never split; ટેક quoted inside the topic, never its own topic; છાપ line stays; lead hard gate: "if the explanation's conclusion could be printed on a classroom poster, it is wrong"; no dialect correction; no theology/comparative religion; media = relationship, warm/domestic, NOT iconographic portrait; keep the Sensitivity paragraph (board-agnostic); re-anchor to નરસિંહ/મીરાં/દયારામ.
- `urmikavya_geet.md` (from `prakriti_deshbhakti_kavita.md`; also the verse fallback) — unit = one કડી; **changed-words ટેક is a topic at each occurrence** (teach what changed), identical ટેક taught once; lens ચિત્ર + ભાવ + અલંકાર; hard gates: slogans (the poem earns feeling through pictures — so must the explanation), over-scientifying nature, skipping craft, literal reading of figurative lines, political framing (the land, not the state); one image per કડી showing THAT કડી's picture.
- `natak_ekanki.md` (from `ekanki.md`) — unit = one stage-beat (boundary: entrance/exit, sound/object arriving, change in what a character knows/wants); four cutting rules (header is its own topic; never cut mid-exchange or split a speech from its governing direction; long exchange stays ONE topic — internal turns go in concepts[]; a single line can be a topic when a direction makes it the turn); stage directions are TEXT, kept verbatim inside original_chunk; no narrator, no interior states; nine hard gates kept; header-fields table and સ્વાધ્યાય/અભિનય task names from the actual GSEB plays; the double-author-then-merge practice is worth keeping.
- Port `sakhi.md` only if a witness-stance chapter exists (અખા-છપ્પા etc.); what ports regardless: the lens-split METHOD (same unit, different lens → separate profile routed on the tell, citing the textbook's own introductory prose) and the SAFETY pattern (any couplet whose literal reading is unsafe gets a named hard gate covering topics, prompts, and recall answers).
- Remaining candidates (final roster from the pilot inventory, VERIFY-3): `gazal.md`, `sonnet.md`, `haiku.md`, `mukt_chhand_kavita.md`, `prarthana_kavita.md`, `lok_geet.md`, `nibandh.md` (લલિત/આત્મપરક), `charitra_prasang.md`, `sansmaran.md`, `pravas_varnan.md`, `patra_lekhan.md`, `diary.md`, `samvad_nibandh.md`, `soochnatmak_sanskritik.md`, `hasya_lekh.md`, `sakshatkar.md`, `bhashan.md`. Create a profile only for forms the corpus actually contains; delete-don't-stub.

### 4.7 Schemas

**`schema/gujarati_learning_plan_skeleton.json`** — TYPE-EXAMPLE mirroring §2.1/§2.2 exactly: keep every key, id scheme, enum, band note, poem-only/prose-only rules, no-hallucination comments. Change values: board/subject/ids per §3.7; textbook line = GSEB reader title; strand_name ભાષા અને સાહિત્ય; all placeholder prose in Gujarati script; `subject_ref_id: null`; `publication_id`: the verified GSEB value (VERIFY-2). Placeholders are shapes, never content to copy.

**`schema/exercise_solutions_skeleton.json`** — KEEP whole shape (root `_comment, plan_id, chapter_id, subject, grade, chapter_name`; `exercises[]` per §4.2/A10; `coverage_report` with `_note`). Change: subject "Gujarati", GSEB id examples, `exercise_group` examples = real સ્વાધ્યાય headings in Gujarati script (from the books, not translated from Hindi).

### 4.8 lib/

**`assemble.py`** — KEEP: entire assembler (spec shape, build_topic/build/emit, O{seq}/L{seq} generation, chapter-continuous concept counter `cstart`, segment/module ranking by min topic position, collage/V2 overlay hooks with prefix-matched url keys, 01_meta emission with its 17 root keys + spec.meta, validate()/upload() incl. the success:false-on-conflict check and popped `_activate`/`created_by`, TOPIC_TYPE mapping {POEM,CONCEPT,STORY_TELLING→instructional; REVIEW→summary; EXERCISE→assessment}). Change: `STRAND_NAME = "ભાષા અને સાહિત્ય"`; `PANEL_NOTE` and default teaching_notes fallback strings → Gujarati (keep the bracketed English stamps `[reused frame: …]`/`[collage of: …]` intact — tooling regexes parse them); NEG gains "Devanagari script labels"; keep romanized ભાષા-બોધ keys; per-chapter constants come from the spec root, not this file.

**`_chunks.py`** — carries over 100% verbatim (UTF-8, script-agnostic).

**`collage.py`** — KEEP letterbox-never-crop, authored-panel-list, downscale-on-composite. Change ordinal badge glyphs to **૧ ૨ ૩ ૪**; verify Gujarati frames carry the narrator-bar convention before relying on letterboxing.

**`collage_build.py` / `collage_cli.py` / `collage_upload.py` / `collage_patch.py` / `collage_verify.py`** — KEEP verbatim (guards, seeding via the `[reused frame: …]` stamp, --repoint reads `_collage_urls.json` never asserts, named-list uploads, minimal live patching of aspect_ratio+teaching_notes only, five verify checks incl. byte-equality). Dependencies: the English stamp format must stay stable; the patch panel-order sentence uses the Gujarati PANEL_NOTE. All dormant until a Gujarati frame pool exists.

### 4.9 upload_reference/

**`chapter_master_map.json`** — KEEP shape (`{chapter_id: {chapter_master_id, path, publication_id}}`, `_`-prefixed keys ignored). RE-AUTHOR content entirely: GSEB rows fetched from the education DB (EDUCATIONDB_URL / fetch-chapters flow) — never invented; `path` per §3.7 template (precedents show the medium slot varies: `bseap_tel_sci7_ch2 → V2/bseap/cbse/telugu/class_7/science/ch_2`); `publication_id` = the verified GSEB publication row.

**`env.example`** — KEEP five vars (`PYTHON_BASE_URL`, `BUCKET_NAME=learning_plan_assets`, `CREATED_BY`, `LOG_LEVEL`, `EDUCATIONDB_URL`). Notes: **CREATED_BY must be set** for Gujarati runs; EDUCATIONDB_URL will be needed (no GSEB rows exist yet); fresh GCP `config.json` on the authoring machine.

---

## 5. Genre-profile template (the exact skeleton every Gujarati genre profile follows)

```markdown
# <genre name in Gujarati script>

> (optional) Provenance: written from <GSEB std-N chapter(s) actually read>.

## Diagnosis signals
<what the text and its સ્વાધ્યાય look like; the tell that routes here;
 for near-miss forms add a table: looks like | but | tell>

## Lens
**<two-to-three-term bold formula, Gujarati>**

## Guiding question
*<one italic model question in Gujarati — a SHAPE to derive from, each chapter derives its own>*

## Explanation unit — **one <X>**
<the atomic unit one topic holds; join/split rules; refrain (ટેક) handling where relevant>

## Emphasise
- <bullets: what the explanation must foreground>

## Avoid (hard gate)
- <bullets: machine-enforced constraints — Agent 7 instantiates them, Agent 13 blocks on them,
   structural ones (e.g. never merge two દુહા) checked at Agent 4>

## Priors
**Media** — <image-per-unit composition rule: the concrete scene, never the moral>
**સ્વાધ્યાય** — <expected exercise types and how topics prepare them>
**Language** — <register + glossing policy; cite reference/shabd_gloss.md and reference/gujarati_verbatim.md>
**Sensitivity** — <only where the form needs it, e.g. devotional પદ>

## Recall priors
<Bloom distribution per unit: one remember, one understand, one apply/analyze/evaluate — stated for THIS form>
```

Optional extra sections are allowed and encouraged when the form demands them (e.g. "How a દુહો is built, and therefore how it is taught"; a near-miss routing table; a named safety gate). Filenames: ASCII lowercase `[a-z_]` slugs. Every profile must appear in `_genre_index.md`'s tree AND master table (check_pack enforces both directions). Roster is fixed by the pilot inventory (VERIFY-3); hindi-lp carried ~24 profiles — expect a different, corpus-driven number.

---

## 6. Porting checklist, ordered by dependency

**Stage 0 — Ground truth (blocks everything)**
1. Inventory `../Textbooks-pdf/std-N/` (N=6..10): per-std chapter list, printed titles, page ranges, genre priors, સ્વાધ્યાય banner inventory — all read off RENDERED pages; start the text-layer defect catalog.
2. VERIFY-1: server id convention (board/medium segments) — enumerate `GET /chapters`, inspect any existing GSEB rows, read echoed medium/subject.
3. VERIFY-2: GSEB DB rows — publication_id, chapter_master_ids (education DB), asset-path segments.
4. Fix the canonical vocabulary/decisions of §3 (they are proposed here as canon; amend ONLY via this brief, then all authors inherit).

**Stage 1 — Constitution (no dependencies among themselves; everything cites them)**
5. `author.md` → 6. `reference/no_hallucination_policy.md` → 7. `reference/gujarati_verbatim.md` → 8. `reference/global_content_rules.md` → 9. `reference/naming_conventions.md` → 10. `reference/phase2_contract.md` → 11. `reference/json_contract.md` → 12. `reference/field_shape_rules.md` → 13. `reference/loop_protocol.md` → 14. `reference/phase2_fetch.md`.

**Stage 2 — Pedagogy references (need Stage 0 inventory + Stage 1)**
15. `reference/genre_diagnosis.md` · 16. `reference/teaching_lens_map.md` · 17. `reference/explanation_unit_map.md` · 18. `reference/teaching_block_format.md` · 19. `reference/teaching_voice_gu.md` · 20. `reference/shabd_gloss.md` · 21. `reference/alankar_chhand.md` · 22. `reference/bhasha_bodh.md` (ladder tables re-measured; VERIFY-4) · 23. `reference/exercise_alignment.md` · 24. `reference/qc_checklist.md` · 25. `reference/collage_media.md`.

**Stage 3 — Profiles (need Stages 0–2)**
26. `profiles/boards/gseb_gujarati.md` (VERIFY-3 feeds it) · 27. genre profiles on the §5 template (pilot-read chapters first) · 28. `profiles/genres/_genre_index.md` (LAST of the profiles — it indexes the final roster; ordering-rationale paragraphs added as pilot evidence accumulates).

**Stage 4 — Agents (need Stages 1–3; author in pipeline order)**
29. `agents/01_…` → 30. `02_…` → 31. `04_…` → 32. `05_…` → 33. `07_…` → 34. `08_…` → 35. `09_…` → 36. `10_…` → 37. `11_…` → 38. `12_…` → 39. `16_…` → 40. `13_…` → 41. `14_…` → 42. `15_…`.

**Stage 5 — Controller + machine files**
43. `orchestrator.md` (needs every agent + reference name final) · 44. `schema/gujarati_learning_plan_skeleton.json` · 45. `schema/exercise_solutions_skeleton.json` · 46. `lib/assemble.py` · 47. `lib/collage.py` + `collage_build/cli/upload/patch/verify.py` + `_chunks.py` · 48. `upload_reference/chapter_master_map.json` + `env.example` · 49. `_empty_images_report.py` · 50. `check_pack.py`.

**Stage 6 — Prove it**
51. `python check_pack.py` → exit 0. · 52. Pilot chapter end-to-end (std 6, one verse + one prose chapter) through Phase 8: zero `validation_errors`. · 53. VERIFY-5: after first upload, GET the chapter back — echoed medium/subject correct, plan at `data.plan.planJson`, record `data.chapterMasterId`. · 54. Re-measure word-count bands from the pilot (VERIFY-4) and reconcile the board profile's targets vs measurements.

---

## 7. Verification gates (no assumption survives contact with the server)

- **VERIFY-1 (blocks first upload):** GSEB `chapter_id` board + medium segments, confirmed from the live server (enumerate/fetch, read echoes) — never reasoned out. A wrong medium uploads CLEAN and mis-files the plan.
- **VERIFY-2:** publication_id, chapter_master_id per chapter, subject_ref_id/medium_id policy, asset-path segments (`V2/…/class_N/gujarati/ch_n/`) — from DB/readback, not arithmetic (the Hindi 355−N formulas do not transfer).
- **VERIFY-3:** genre roster + સ્વાધ્યાય block inventory from rendered GSEB pages (Stage 0.1) before any profile or exercise doc is authored.
- **VERIFY-4:** word-count bands and grammar/gloss ladders re-measured for L2 std 6–10; targets vs measurements recorded separately.
- **VERIFY-5:** post-upload readback per §2.5; every asset URL HEAD-checked; every non-empty image_url on `learning_plan_assets`.
- **Standing rule:** anything in this brief marked "provisional" is written into pack files WITH its warning box, and the file that resolves it (`naming_conventions.md` / board profile) is updated first when verification lands.

— End of brief. —
