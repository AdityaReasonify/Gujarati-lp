# Phase-2 Contract — the exact shape this pack emits

> Authority, verified against a real accepted plan
> (`learning_plan_upload/data/V2/.../cbse_eng_englishgrammar5_ch1.json`), the id regexes in
> `learning_plan_upload/src/lp_sync/config.py`, **and — decisively — the server validator's own
> error messages.**

## Read this box before anything else

Four rules below were originally inferred from the sample plan and were **wrong**. The LP2
validator rejected the first Hindi chapter with 27 errors and named all four. The server is the
authority; when this file and the validator disagree, the validator is right.

| # | The mistake | The rule |
|---|---|---|
| 1 | `publication_id: null` | **`publication_id` is required and must not be null.** Use `1`. |
| 2 | Segment recalls numbered `.SR{n}` | **LP2 segment recalls are `{segment_id}.RQ{n}`.** `.SR{n}` is LP **v1**'s convention. Carrying a v1 habit into LP2 is exactly the trap this pack warns about elsewhere. |
| 3 | `topic_type: "POEM"` / `"CONCEPT"` | **`topic_type` is a closed enum: `instructional` \| `summary` \| `assessment`.** Literary genre does **not** live here. |
| 4 | `concept_id` restarting at `.C1` in every topic | **The concept counter is chapter-continuous**, like M/S/T — `M1.S1.T1.C1`, `M1.S2.T2.C2`, `M1.S3.T5.C5`. |
| 5 | `chapter_id: "cbse_hin_hindi6_ch1"` | **The medium segment is `eng`, not `hin`** — `cbse_eng_hindi6_ch1`. Checked against the live server: `GET /api/lp2/learning-plans/chapter/cbse_eng_hindi6_ch1` returns the shipped class-6 plan and the `cbse_hin_…` form 404s. `chapter_master_map.json` uses `cbse_eng_…` for every grade. This one does **not** fail loudly — it uploads clean and goes live under the wrong medium; all 23 Hindi plans shipped that way once. Full account in `reference/naming_conventions.md`. |

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

For class-6 Hindi:

```jsonc
"phase": 2,                       // the literal marker — never omit
"board": "cbse",
"subject": "Hindi",
"grade": 6,
"level": "standard",
"ordering": "logical",            // "textbook" in learning_plan_textbook.json
"chapter_id": "cbse_eng_hindi6_ch1",
"plan_id":    "cbse_eng_hindi6_ch1_v1",
"author": "",
"_activate": false,               // the server sets this; lp_sync strips it before sending
"medium_id": null,                // server-injected — leave null unless a subject record gives it
"subject_ref_id": null,           // server-injected — see the note below
"chapter_master_id": 354,         // ch1; REQUIRED for upload, not discoverable from the API
"publication_id": 1,              // required, must not be null — see rule 1 above
"estimated_time": 1.5,
"textbook": "मल्हार | हिन्दी पाठ्यपुस्तक | कक्षा 6",
"textbook_url": "<the chapter PDF url>",
"textbook_pages": "",
"unit_title": "…", "unit_number": 1, "topic_title": "…", "topic_number": 1,
"chapter_name": "मातृभूमि",
"genre": "prakriti_deshbhakti_kavita",
"teaching_lens": "…",             // from the genre profile
"guiding_question": "…",
"english_plan_id": null, "english_chapter_id": null,   // no English twin for a Hindi chapter
"objectives": [ … ],
"strand_to_objective_map": {"L1": "O1", "L2": "O2", …}
```

`english_plan_id` / `english_chapter_id` exist because phase 2 was first used to carry English
plans forward. A Hindi chapter has no English twin — leave them `null`, do not invent one.

### The author sets two root ids; the server sets the rest

`chapter_master_id` and `publication_id` come from
`learning_plan_upload/chapter_master_map.json`, which stores only those two per chapter.
**`subject_ref_id` and `medium_id` are server-injected** — they are listed in
`lp_sync/config.py:VOLATILE_TOP_LEVEL_KEYS` beside `plan_id`, `version` and `_activate`, which is
exactly the set of keys the local↔remote comparison drops because the server owns them. Both
reference V2 plans on disk carry them as `null`.

The trap is that a *shipped* plan read back from the API shows them filled — Hindi class 6 comes
back `subject_ref_id: 84`, class 7 `78`, class 8 `85`. That looks like a lookup table. It is not:
the values follow no derivable pattern, and copying one into a new plan means guessing at a value
the server is about to overwrite anyway. Write `null` and let the server fill it.

Where a **real subject record** exists, send the real values instead of `null` — class-10 Hindi is
`subject_ref_id: 90`, `medium_id: 1`. Class 9 confirms a genuine value survives the round trip:
`91` was sent and `91` came back unnormalised. Only an *invented* value is a hazard.
`profiles/boards/cbse_hindi.md` §Ids has the class-10 subject record in full.

## The objective model — a plan-level registry, not per-topic pairs

This is the biggest departure. There is **no per-topic objective pair**. Objectives live once at
the root and topics point at them.

```jsonc
"objectives": [{
  "objective_id": "O1",
  "legacy_id": "L1",
  "strand": "L",
  "strand_name": "भाषा एवं साहित्य",
  "objective_text": "…one concise goal, ~12–30 words…",
  "bloom_level": "Understand",          // capitalised here, lowercase in recall_questions
  "home_topic_id": "M1.S1.T1",
  "anchor": ["M1.S1.T1.C1"],            // concept ids this objective is taught at
  "status": "taught",
  "theme_category": null
}]
```

`strand_to_objective_map` maps every `legacy_id` to its `objective_id`. Hindi literature uses the
single strand **`L` — भाषा एवं साहित्य** throughout, exactly as the reference plan does.

Each topic carries `objective_ids: ["O1"]` **and** a mirrored inline copy in
`learning_objectives[]` — the same object plus `"image_examples": []`. The server performs this
mirror itself (`lp2_chapters.py`), and `lp_sync/patcher.py:93-122` re-does it locally so a drifted
inline copy does not fork a needless version. **Keep the two texts identical.**

### Where the two-objective spine went

Earlier Hindi work gave each topic O1 व्याख्या + O2 दृष्टिकोण. Phase 2 has no such pair. The
teaching survives as **fields on the topic**, which is where it always belonged:

| v1 idea | phase-2 field |
|---|---|
| O1 व्याख्या — what the passage says and means | **`explanation`** |
| O2 दृष्टिकोण — the class-6 Indian-life anchor | **`real_life_example`** |

Do not try to reproduce two objectives per topic. It fails validation and it was never the point —
the point was explanation followed by a real-life anchor.

## The concept layer

Every topic carries `concepts[]`. A short scene has one concept; a topic doing two distinct things
may have two.

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

`c` does **not** restart inside a topic. With one concept per topic the concept number equals the
topic number, so `M1.S2.T3` carries `M1.S2.T3.C3`. The validator checks this exactly and reports
`expected concept_id='M1.S2.T3.C3', got 'M1.S2.T3.C1'`.

## topic_type — a closed enum, and genre is not in it

| value | use for |
|---|---|
| `instructional` | every reading scene — a छंद, a दोहा, a पद, a घटना, a कवि-परिचय |
| `summary` | an in-text wrap or review block |
| `assessment` | an assessment block (not used by this pack — अभ्यास is a separate deliverable) |

`POEM`, `STORY_TELLING`, `CONCEPT`, `REVIEW` are **rejected**. Those are LP v1's literary types.
The विधा lives in root `genre` and the finer role in `topic_category` (`introduction` / `core` /
`climax` / `transition` / `resolution`), which is free text.

Media ids are **concept-scoped, not topic-scoped** — `config.py:25-28` enforces:

```python
MEDIA_ID_RE = re.compile(
    r"^(?P<concept_id>M\d+\.S\d+\.T\d+\.C\d+)\.(?P<suffix>IMG|VID|2D|3D|SIM)(?P<n>\d+)$")
```

A topic-scoped `M1.S1.T1.IMG1` — the English pack's convention — is rejected.

`plan_id = {chapter_id}_v{N}`. There is **no `_standard_` segment** in a phase-2 plan id, unlike
v1's `hindi6_ch1_standard_v4`.

## Ordering — LP2 has only one

The validator checks ids against **traversal position**, not just against each other:

```
modules[0].segments[0]: expected segment_id='M1.S1', got 'M1.S2'
```

So a `learning_plan_textbook.json` that re-sequences nodes is rejected unless it is renumbered —
and renumbering makes its ids differ from the logical plan, which defeats the point of a second
ordering ("same nodes, same ids, printed order").

**Consequence: LP2 cannot carry a separate textbook ordering.** Emit both files with the same
sequence and raise `human_confirmation_required` in the run report, recording what the printed
order actually is. Do not try to defeat this by renumbering — a teacher matching the printed book
against the plan would then find two different id sets for the same chapter.

## Media node

```jsonc
{"id": "M1.S1.T1.C1.IMG1", "type": "image", "subtype": "illustration",
 "title": "…", "description": "…", "image_url": "", "aspect_ratio": "16:9",
 "concept_id": "M1.S1.T1.C1", "home_concept_id": "M1.S1.T1.C1", "objective_id": null,
 "image_category": "illustration", "teaching_notes": "…",
 "negative_prompt": "…", "generation_prompt": "…"}
```

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

`topic_type` for Hindi literature: `POEM` / `STORY_TELLING` / `CONCEPT` / `REVIEW`. (The reference
plan uses `"instructional"` because it is a grammar chapter — do not copy that for literature.)

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
   chapter. `output/_verify_all.py` walks the correct path.

**Staging DNS is flaky.** `getaddrinfo failed` appears at random, roughly once per few dozen
calls, and is not an API error — retry two or three times before believing anything. Both
`_verify_all.py` and `_reupload_bhasha_bodh.py` wrap every call in a retry for this reason.

Asset bucket is `learning_plan_assets` (v1 used `topic-content-images`). `chapter_master_id` is
mandatory for upload and is **not discoverable from the LP2 API** — it comes from
`chapter_master_map.json` or the `chapterMaster` read in `fetch_chapters.py`. For class-6 Hindi it
is simply **`355 − chapter number`** (ch1 = 354 … ch13 = 342), confirmed against the v1
`chapter_index()` listing for all 13.
