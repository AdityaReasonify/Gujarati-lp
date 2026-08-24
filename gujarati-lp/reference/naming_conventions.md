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
the Hindi pack's file said `c` restarts inside its topic — the validator rejects that.)

## Objectives — a root registry, not a per-topic code

- `objective_id` is `O{n}`, unique across the plan, living in the root `objectives[]`.
- `legacy_id` is `L{n}`, and `strand_to_objective_map` maps `L{n} → O{n}`.
- Gujarati literature uses the single strand `L` / `ભાષા અને સાહિત્ય`.
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
  Std-6 Gujarati: `gseb_eng_gujarati6_ch1`.

> **⚠ PROVISIONAL — the `gseb` and `eng` segments are UNVERIFIED (VERIFY-1).**
> The form `gseb_eng_gujarati{grade}_ch{N}` is reasoned from the Hindi precedent, not read from
> the live server. VERIFY-1 must resolve the real GSEB board and medium segments against the
> server **before the first upload** — enumerate/fetch existing rows and read the echoes; never
> reason the segments out. A wrong medium uploads CLEAN and mis-files the plan. When
> verification lands, update THIS file first; every other file inherits the corrected form.

- **`{medium}` is the medium of instruction — not the subject language.**
  The subject goes in the `{subject}` slot, so a Gujarati chapter reads `gseb_`**`eng`**`_gujarati6_ch1`:
  medium `eng` (provisional), subject `gujarati`. Writing `gseb_guj_gujarati6_ch1` by analogy with
  the subject would be wrong, and wrong in a way that does not surface as an error — the server
  **parses this segment into a real `medium` DB column** and the upload succeeds, so the plan
  simply goes live registered under the wrong medium. All 23 Hindi plans shipped that way once
  (`cbse_hin_…` instead of `cbse_eng_…`) and had to be re-uploaded under corrected ids.
  Two independent cross-checks, either of which would have caught it — **both must be re-run for
  GSEB as part of VERIFY-1**:
  * enumerate the live corpus's medium usage — in the Hindi case every other plan used `eng` and
    no non-`eng` medium existed anywhere; for GSEB, read what mediums actually exist before
    trusting `eng` (precedents show the slot varies: `bseap_tel_sci7_ch2` carries medium `tel`);
  * read the asset-bucket path segments — `V2/{board}/{publication}/{medium}/class_{N}/gujarati/ch_{n}/image/`
    has medium and subject in separate segments; the Hindi bucket said **`english`** in the medium
    slot and **`hindi`** in the subject slot. The GSEB segments come from VERIFY-2 readback, never
    from analogy.
  After any upload, `GET /lp2/learning-plans/chapter/{chapter_id}` echoes `medium` and `subject`
  back. Read them.
- `plan_id = {chapter_id}_v{version}` — **no `_standard_` segment.**
- The server assigns the real version on upload; what you write is the intention.
- `publication_id` is **required and must not be null** (the GSEB publication row must be looked
  up — VERIFY-2; the Hindi value `1` does not transfer).
- `topic_type` is the closed enum `instructional` | `summary` | `assessment` — literary genre goes
  in root `genre`, not here.

## Directories

Output lives in `output{N}/<chapter>/` with **`N` written for every standard: `output6` …
`output10`**, and chapter directories zero-padded `ch01`-style. (The Hindi pack's asymmetries —
bare `output` for its lowest class, unpadded `ch4` — are dropped; do not reproduce them.)

## Names and display text — no numbers

Module, segment and topic **names are descriptive, never numbered**: "કડી 2" is not a name, and
neither is "Topic 3". Numbers live only in ids and provenance fields
(`textbook_pages`, `unit_number`, …). Inside display prose the same rule holds: write
"બીજી કડીમાં", never "કડી 2માં".

## Renumbering (Agent 14)

Agent 14 arranges by the reading sequence, renumbers M/S/T/C consecutively along the traversal,
and **translates every surviving reference** — media ids, recall ids, `objectives[].anchor`,
`home_topic_id`, `objective_ids`, `depends_on`, `source_topic_ids`. A renumber that leaves a stale
anchor is a hard fail. (`O{n}` and `strand_to_objective_map` are **not** renumbered.) Agent 15
reorders the same renumbered nodes into printed order: ids stay, sequence changes.
