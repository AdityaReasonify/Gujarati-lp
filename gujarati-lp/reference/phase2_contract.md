# Phase-2 Contract — the exact shape this pack emits

> Authority: the LP2 server validator's own error messages. The mechanisms below were verified
> during the Hindi (CBSE) run — against a real accepted plan
> (`learning_plan_upload/data/V2/.../cbse_eng_englishgrammar5_ch1.json`), the id regexes in
> `learning_plan_upload/src/lp_sync/config.py`, **and — decisively — the validator itself.**
> Mechanisms carry unchanged into this pack. **Values do not**: every GSEB-specific value
> (board/medium segments, `publication_id`, `chapter_master_id`, subject records) is
> **provisional until VERIFY-1/VERIFY-2** resolve it against the live server, and this pack
> re-verifies its own first chapter against the validator the same way the Hindi pack did.

## Read this box before anything else

Four rules below were originally inferred from the sample plan and were **wrong**. The LP2
validator rejected the first Hindi chapter with 27 errors and named all four. The server is the
authority; when this file and the validator disagree, the validator is right. Rows 1–4 are
validator-verified **mechanisms** — they carry into the Gujarati pack as they stand. Row 5 is a
mechanism (the medium slot fails silently) whose GSEB **value** is still provisional.

| # | The mistake | The rule |
|---|---|---|
| 1 | `publication_id: null` | **`publication_id` is required and must not be null.** The Hindi pack used `1` — that is **CBSE's publication row, not portable**. The GSEB publication row must be looked up in the education DB (**VERIFY-2**) before the first Phase 8 run. |
| 2 | Segment recalls numbered `.SR{n}` | **LP2 segment recalls are `{segment_id}.RQ{n}`.** `.SR{n}` is LP **v1**'s convention. Carrying a v1 habit into LP2 is exactly the trap this pack warns about elsewhere. |
| 3 | `topic_type: "POEM"` / `"CONCEPT"` | **`topic_type` is a closed enum: `instructional` \| `summary` \| `assessment`.** Literary genre does **not** live here. |
| 4 | `concept_id` restarting at `.C1` in every topic | **The concept counter is chapter-continuous**, like M/S/T — `M1.S1.T1.C1`, `M1.S2.T2.C2`, `M1.S3.T5.C5`. |
| 5 | A wrong medium segment in `chapter_id` | **The medium slot is the medium of instruction, NOT the subject language — and a wrong value does not fail loudly.** It uploads clean and goes live under the wrong medium DB column; all 23 Hindi plans shipped that way once (`cbse_hin_…` instead of the server's `cbse_eng_…`). The Gujarati provisional form is **`gseb_eng_gujarati{grade}_ch{N}`** — both the board and medium segments **must be confirmed against the live server (VERIFY-1) before the first upload**, never reasoned out. Full account in `reference/naming_conventions.md`. |

This is **not** the English pack's shape and **not** the LP v1 shape. Three things differ and each
one will be rejected by the server if you get it wrong: the **objective model**, the **concept
layer**, and the **id grammar**.

## Root keys (32, all present)

```
board  genre  grade  level  phase  author  modules  plan_id  subject  version  ordering
textbook  _activate  medium_id  chapter_id  objectives  unit_title  topic_title  unit_number
chapter_name  textbook_url  topic_number  teaching_lens  estimated_time  publication_id
subject_ref_id  textbook_pages  english_plan_id  guiding_question  chapter_master_id
english_chapter_id  strand_to_objective_map
```

For std-6 Gujarati (provisional ids per VERIFY-1/2 — see the box above):

```jsonc
"phase": 2,                       // the literal marker — never omit
"board": "gseb",                  // PROVISIONAL — confirm the server's board segment (VERIFY-1)
"subject": "Gujarati",
"grade": 6,
"level": "standard",
"ordering": "logical",            // "textbook" in learning_plan_textbook.json
"chapter_id": "gseb_eng_gujarati6_ch1",   // PROVISIONAL medium slot — rule 5 above (VERIFY-1)
"plan_id":    "gseb_eng_gujarati6_ch1_v1",
"author": "",
"_activate": false,               // the server sets this; lp_sync strips it before sending
"medium_id": null,                // server-injected — leave null unless a real GSEB subject record gives it
"subject_ref_id": null,           // server-injected — see the note below
"chapter_master_id": null,        // REQUIRED for upload; GSEB row fetched from the education DB
                                  // into upload_reference/chapter_master_map.json (VERIFY-2) —
                                  // never invented, never derived by arithmetic
"publication_id": null,           // the server REJECTS null (rule 1) — fill with the verified GSEB
                                  // publication row (VERIFY-2) before Phase 8; CBSE's 1 does not transfer
"estimated_time": 1.5,            // review per grade
"textbook": "ગુજરાતી (દ્વિતીય ભાષા) | ધોરણ 6",   // the reader's PRINTED title per standard, read off
                                  // the rendered title page — profiles/boards/gseb_gujarati.md is the map
"textbook_url": "../Textbooks-pdf/std-6/<chapter>.pdf",  // local path string until a hosted URL
                                  // exists — record the gap in 11_pages.json
"textbook_pages": "",
"unit_title": "…", "unit_number": 1, "topic_title": "…", "topic_number": 1,
"chapter_name": "…",              // the printed chapter title, Gujarati script, exactly as rendered
"genre": "urmikavya_geet",        // slug from the Gujarati genre roster
"teaching_lens": "…",             // from the genre profile, Gujarati
"guiding_question": "…",          // derived from THIS chapter, Gujarati — never copied from the profile
"english_plan_id": null, "english_chapter_id": null,   // no English twin for a Gujarati chapter
"objectives": [ … ],
"strand_to_objective_map": {"L1": "O1", "L2": "O2", …}
```

`english_plan_id` / `english_chapter_id` exist because phase 2 was first used to carry English
plans forward. A Gujarati chapter has no English twin — leave them `null`, do not invent one.

### The author sets two root ids; the server sets the rest

`chapter_master_id` and `publication_id` come from
`upload_reference/chapter_master_map.json`, which stores only those two per chapter — and for
GSEB its rows are **fetched from the education DB** (`EDUCATIONDB_URL` / the fetch-chapters
flow), never invented. **`subject_ref_id` and `medium_id` are server-injected** — they are
listed in `lp_sync/config.py:VOLATILE_TOP_LEVEL_KEYS` beside `plan_id`, `version` and
`_activate`, which is exactly the set of keys the local↔remote comparison drops because the
server owns them. Reference V2 plans on disk carry them as `null`.

The trap is that a *shipped* plan read back from the API shows them filled — the Hindi corpus
came back `subject_ref_id: 84` for class 6, `78` for class 7, `85` for class 8. That looks like
a lookup table. It is not: the values follow no derivable pattern, they are **CBSE Hindi rows
with no GSEB counterpart**, and copying one into a new plan means guessing at a value the server
is about to overwrite anyway. Write `null` and let the server fill it.

Where a **real subject record** exists, send the real values instead of `null` — the Hindi run
confirmed a genuine value survives the round trip (class 9 sent `91` and got `91` back
unnormalised). Only an *invented* value is a hazard. No GSEB subject record is confirmed yet;
until one is (VERIFY-2 / post-upload readback), `null` is the only correct value.
`profiles/boards/gseb_gujarati.md` §Ids records whatever GSEB rows verification lands.

## The objective model — a plan-level registry, not per-topic pairs

This is the biggest departure. There is **no per-topic objective pair**. Objectives live once at
the root and topics point at them.

```jsonc
"objectives": [{
  "objective_id": "O1",
  "legacy_id": "L1",
  "strand": "L",
  "strand_name": "ભાષા અને સાહિત્ય",
  "objective_text": "…one concise goal, 12–30 Gujarati words, grounded in THIS scene —
                     it could fit no other chapter…",
  "bloom_level": "Understand",          // capitalised here, lowercase in recall_questions
  "home_topic_id": "M1.S1.T1",
  "anchor": ["M1.S1.T1.C1"],            // concept ids this objective is taught at
  "status": "taught",
  "theme_category": null
}]
```

`strand_to_objective_map` maps every `legacy_id` to its `objective_id`. Gujarati literature uses
the single strand **`L` — ભાષા અને સાહિત્ય** throughout, exactly as the reference plan does with
its single strand.

Each topic carries `objective_ids: ["O1"]` **and** a mirrored inline copy in
`learning_objectives[]` — the same object plus `"image_examples": []`. The server performs this
mirror itself (`lp2_chapters.py`), and `lp_sync/patcher.py:93-122` re-does it locally so a drifted
inline copy does not fork a needless version. **Keep the two texts identical, character for
character.**

There is **no `M1.S1.T1.P1`-style objective code anywhere** in a phase-2 plan — that is the
English pack's phase-1 convention.

### Where the two-objective spine went

Earlier v1-style work gave each topic O1 વ્યાખ્યા + O2 દૃષ્ટિકોણ. Phase 2 has no such pair. The
teaching survives as **fields on the topic**, which is where it always belonged:

| v1 idea | phase-2 field |
|---|---|
| O1 વ્યાખ્યા — what the passage says and means | **`explanation`** |
| O2 દૃષ્ટિકોણ — the anchor inside the child's Indian life | **`real_life_example`** |

Do not try to reproduce two objectives per topic. It fails validation and it was never the point —
the point was explanation followed by a real-life anchor.

## The concept layer

Every topic carries `concepts[]`. A short scene has one concept; a topic doing two distinct things
may have two. Wanting three means the cut is wrong.

```jsonc
"concepts": [{
  "concept_id": "M1.S1.T1.C1",
  "concept_name": "…",
  "objective_id": "O1",
  "key_terms": ["…"],
  "content": [
    {"type": "paragraph", "text": "…", "publication_text": "…"},
    {"type": "list", "items": ["…", "…"]}
  ]
}]
```

## Id grammar

| Level | Pattern | Example |
|---|---|---|
| Module / Segment / Topic | `M{m}` / `M{m}.S{s}` / `M{m}.S{s}.T{t}` | `M1.S1.T1` |
| Concept | `M{m}.S{s}.T{t}.C{c}` — **`c` is chapter-continuous** | `M1.S2.T3.C3` |
| Objective | `O{n}` (root registry) | `O1` |
| Topic recall | `{topic_id}.RQ{n}` + `legacy_id` `{topic_id}.TR{n}` | `M1.S1.T1.RQ1` |
| Segment recall | `{segment_id}.RQ{n}` — **`RQ`, not `SR`** | `M1.S1.RQ1` |
| Media | `{concept_id}.{IMG\|VID\|2D\|3D\|SIM}{n}` | `M1.S1.T1.C1.IMG1` |

`s` and `t` run across the WHOLE chapter and never restart. `c` does **not** restart inside a
topic either. With one concept per topic the concept number equals the topic number, so
`M1.S2.T3` carries `M1.S2.T3.C3`. The validator checks this exactly and reports
`expected concept_id='M1.S2.T3.C3', got 'M1.S2.T3.C1'`.

Ids are frozen at Agent 4's pass and renumbered consecutively only by Agent 14. `O{n}` and
`strand_to_objective_map` are **not** renumbered.

## topic_type — a closed enum, and genre is not in it

In the **emitted deliverables** (`learning_plan_logical.json`, `learning_plan_textbook.json`)
`topic_type` is the closed server enum:

| value | use for |
|---|---|
| `instructional` | every reading scene — a કડી, a દુહો, a પદ, a ઘટના, a કવિ-પરિચય |
| `summary` | an in-text wrap or review block |
| `assessment` | an assessment block (not used by this pack — સ્વાધ્યાય is a separate deliverable) |

`POEM`, `STORY_TELLING`, `CONCEPT`, `REVIEW` are **rejected by the server**. Those are the
pipeline's *authored* values: intermediate files (Agents 02–13) carry
`POEM | STORY_TELLING | CONCEPT | REVIEW` because the cut and the QC gates need the literary
distinction. Agents 14/15 map them at emit — and only the closed enum ever leaves the pack:

```
POEM, STORY_TELLING, CONCEPT  →  instructional
REVIEW                        →  summary
EXERCISE                      →  assessment      (defensive only — સ્વાધ્યાય is never a topic)
```

The સ્વરૂપ (genre) lives in root `genre`, never in `topic_type`; the finer role lives in
`topic_category` (`introduction` / `core` / `climax` / `transition` / `resolution`), which is
free text.

Media ids are **concept-scoped, not topic-scoped** — `config.py:25-28` enforces:

```python
MEDIA_ID_RE = re.compile(
    r"^(?P<concept_id>M\d+\.S\d+\.T\d+\.C\d+)\.(?P<suffix>IMG|VID|2D|3D|SIM)(?P<n>\d+)$")
```

A topic-scoped `M1.S1.T1.IMG1` — the English pack's convention — is rejected.

`plan_id = {chapter_id}_v{N}`. There is **no `_standard_` segment** in a phase-2 plan id, unlike
v1's `…_standard_v4` forms. The server assigns the real version.

## Ordering — LP2 has only one

The validator checks ids against **traversal position**, not just against each other:

```
modules[0].segments[0]: expected segment_id='M1.S1', got 'M1.S2'
```

So a `learning_plan_textbook.json` that re-sequences nodes is rejected unless it is renumbered —
and renumbering makes its ids differ from the logical plan, which defeats the point of a second
ordering ("same nodes, same ids, printed order").

**Consequence: LP2 cannot carry a separate textbook ordering.** Emit both files with the same
(logical) sequence; record the true printed order in `05b_textbook_order.json`; and when the two
orders match, raise in the run report:

```jsonc
{"human_confirmation_required": true,
 "reason": "textbook order is identical to logical order",
 "checked": "05b_textbook_order.json matches the logical traversal exactly"}
```

Do not try to defeat this by renumbering — a teacher matching the printed book against the plan
would then find two different id sets for the same chapter. And never pretend the orders were
compared when they were not.

## Media node

```jsonc
{"id": "M1.S1.T1.C1.IMG1", "type": "image", "subtype": "illustration",
 "title": "…", "description": "…", "image_url": "", "aspect_ratio": "16:9",
 "concept_id": "M1.S1.T1.C1", "home_concept_id": "M1.S1.T1.C1", "objective_id": null,
 "image_category": "illustration", "teaching_notes": "…",
 "negative_prompt": "…", "generation_prompt": "…"}
```

`image_url` stays `""` until the image is generated. `generation_prompt` may be empty ONLY when
`image_url` carries a reused frame; both empty is a defect. (No Gujarati frame pool exists yet,
so in this pack every media node carries an authored `generation_prompt` — reuse is dormant.)

## Topic keys (31)

```
media  2d_tool  summary  concepts  topic_id  key_terms  depends_on  difficulty  topic_name
topic_type  word_count  explanation  brief_summary  objective_ids  modified_chunk
original_chunk  topic_category  concept_bullets  detailed_summary  important_points
publication_text  recall_questions  source_topic_ids  publication_chunk  real_life_example
estimated_exchanges  learning_objectives  primary_content_type  tertiary_content_type
secondary_content_type  available_content_types
```

Poem topics additionally carry `figures_of_speech[]` and `rhyme_scheme` (see
`reference/alankar_chhand.md`); the module carries `difficult_words[]` and `overall_rhyme_scheme`.
A topic may also carry the optional ભાષા-બોધ extras — `shabdarth`, `samanarthi`, `vilom`,
`vyakaran` — which the server accepts and stores; **keep the romanized key names** (see
`reference/bhasha_bodh.md`).

`topic_type` here follows the split above: authored enum (`POEM` / `STORY_TELLING` / `CONCEPT` /
`REVIEW`) in the intermediate files, closed server enum in the emitted plans via the Agent-14/15
mapping. (The reference plan shows `"instructional"` throughout because it *is* an emitted
phase-2 plan — the emitted Gujarati plans look the same after the mapping.)

## Upload — LP2, no auth

Base `https://staging.singularity-learn.com/agentapi`. Use
`learning_plan_upload/src/lp_sync/` rather than writing a client.

```
POST /api/lp2/learning-plans/validate            multipart file=plan.json  → validation_errors[]
POST /api/lp2/learning-plans/upload              multipart + chapter_master_id, created_by
PUT  /api/lp2/learning-plans/chapter/{id}        JSON body (update path)
POST /api/lp2/learning-plans/approve-draft       {"plan_id": "…"}
GET  /api/lp2/learning-plans/chapter/{id}?include_json=true
POST /api/topics/upload                          multipart assets → publicUrl
```

Six traps, each of which has bitten someone:

1. **No auth header.** The LP2 client sends none. Do not copy v1's bearer/cookie handling.
2. **`approve-draft` takes `{"plan_id": …}`.** LP v1 takes `{"draft_plan_id": …}`. Sending the v1
   key here fails.
3. **`POST /upload` returns HTTP 200 with `success: false`** on a conflict. Check the flag, not
   the status code.
4. **The server assigns the version.** The `version` you write is an intention, not a request.
5. **Re-uploading the same `plan_id` is refused, and the refusal looks like a pass.** You get
   HTTP 200, `validation_errors: []`, and `action: "validated_only"` — the plan validated and was
   *not stored*. The only tell is `success: false` and
   `message: "Plan '…' already exists. Use force=true to overwrite."` Append **`&force=true`** to
   overwrite in place (`action` then comes back `"replaced"`), or bump `plan_id`/`version` to keep
   the old one. `assemble.upload(..., force=True)` does the former.
6. **`GET …?include_json=true` nests the plan three deep.** It is
   `body["data"]["plan"]["planJson"]`, with `version` / `isActive` on `body["data"]["plan"]`.
   Guessing at `body["data"]["raw_json"]` silently yields zero topics and looks like an empty
   chapter. The per-grade verify scripts (`output6/_verify6.py` … `output10/_verify10.py`) walk
   the correct path; `reference/phase2_fetch.md` has the full envelope.

**Staging DNS is flaky.** `getaddrinfo failed` appears at random, roughly once per few dozen
calls, and is not an API error — wrap every call in a retry and try two or three times before
believing anything.

**Server-volatile keys — never diff them, never hand-set them:** `plan_id`, `version`,
`_activate`, `subject_ref_id`, `medium_id`, `chapter_master_id`, `created_by`. The server owns
all seven; a local↔remote comparison that includes them reports phantom drift.

**Set `CREATED_BY`** (from `upload_reference/env.example`) on every upload. The Hindi runs left
it null and authorship was lost — do not repeat that.

Asset bucket is `learning_plan_assets` (v1 used `topic-content-images`). `chapter_master_id` is
mandatory for upload and is **not discoverable from the LP2 API** — it comes from
`upload_reference/chapter_master_map.json`, whose GSEB rows are fetched from the education DB
(the `chapterMaster` read in `fetch_chapters.py`). The Hindi class-6 corpus happened to follow
**`355 − chapter number`** — that arithmetic is CBSE provenance and does **not** transfer; GSEB
ids are fetched per chapter (VERIFY-2), never derived, never invented.
