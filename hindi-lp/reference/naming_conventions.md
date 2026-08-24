# Naming Conventions (IDs) — phase 2

Full field-by-field authority is `reference/phase2_contract.md`. This is the id summary.

## Hierarchy (dotted, globally continuous, no gaps after Agent 14)

| Level | Pattern | Example |
|---|---|---|
| Module | `M{m}` | `M1` |
| Segment | `M{m}.S{s}` | `M1.S2` |
| Topic | `M{m}.S{s}.T{t}` | `M1.S2.T3` |
| Concept | `M{m}.S{s}.T{t}.C{c}` — **`c` is chapter-continuous** | `M1.S2.T3.C3` |

`m/s/t/c` **all** run across the whole chapter and never restart. With one concept per topic the
concept number equals the topic number: `M1.S2.T3` carries `M1.S2.T3.C3`. (An earlier version of
this file said `c` restarts inside its topic — the validator rejects that.)

## Objectives — a root registry, not a per-topic code

- `objective_id` is `O{n}`, unique across the plan, living in the root `objectives[]`.
- `legacy_id` is `L{n}`, and `strand_to_objective_map` maps `L{n} → O{n}`.
- Hindi literature uses the single strand `L` / `भाषा एवं साहित्य`.
- A topic points at its objective(s) with `objective_ids: ["O1"]` and mirrors the object inline in
  `learning_objectives[]`.

There is **no `M1.S1.T1.P1`-style objective code** in phase 2. That is the English pack's phase-1
convention.

## Recall questions

- Topic level: `{topic_id}.RQ{n}`, with `legacy_id` `{topic_id}.TR{n}`.
- Segment level: `{segment_id}.RQ{n}` — **`RQ`, not `SR`.**

`.SR{n}` is the LP **v1** convention and LP2 rejects it:
`expected id='M1.S1.RQ1', got 'M1.S1.SR1'`. Carrying a v1 habit into LP2 is the specific trap
here — the two systems disagree, and only the LP2 validator's word counts.

## Media

`{concept_id}.{TYPE}{n}` where TYPE ∈ `IMG` `VID` `2D` `3D` `SIM`.
Example `M1.S1.T1.C1.IMG1`. **Concept-scoped** — a topic-scoped media id is rejected.

## Plan identity

- `chapter_id = {board}_{medium}_{subject}{grade}_ch{unit_number}`, lowercase.
  Class-6 Hindi: `cbse_eng_hindi6_ch1`.
- **`{medium}` is the medium of instruction — not the subject language. It is `eng`.**
  The subject goes in the `{subject}` slot, so a Hindi chapter reads `cbse_`**`eng`**`_hindi6_ch1`:
  medium `eng`, subject `hindi`. Writing `cbse_hin_hindi6_ch1` is wrong, and wrong in a way that
  does not surface as an error — the server **parses this segment into a real `medium` DB column**
  and the upload succeeds, so the plan simply goes live registered under the wrong medium. All 23
  Hindi plans shipped that way once and had to be re-uploaded under corrected ids.
  Two independent cross-checks, either of which would have caught it:
  * every other plan in the corpus uses `eng` — there is no non-`eng` medium anywhere;
  * the asset bucket path already says it — `V2/{board}/{publication}/`**`english`**`/class_7/`**`hindi`**`/ch_9/image/`
    has medium and subject in separate segments, and medium is `english`.
  After any upload, `GET /lp2/learning-plans/chapter/{chapter_id}` echoes `medium` and `subject`
  back. Read them.
- `plan_id = {chapter_id}_v{version}` — **no `_standard_` segment.**
- The server assigns the real version on upload; what you write is the intention.
- `publication_id` is **required and must not be null** (`1` for class-6 Hindi).
- `topic_type` is the closed enum `instructional` | `summary` | `assessment` — literary genre goes
  in root `genre`, not here.

## Renumbering (Agent 14)

Agent 14 arranges by the reading sequence, renumbers M/S/T/C consecutively along the traversal,
and **translates every surviving reference** — media ids, recall ids, `objectives[].anchor`,
`home_topic_id`, `objective_ids`, `depends_on`, `source_topic_ids`. A renumber that leaves a stale
anchor is a hard fail. Agent 15 reorders the same renumbered nodes into printed order: ids stay,
sequence changes.
