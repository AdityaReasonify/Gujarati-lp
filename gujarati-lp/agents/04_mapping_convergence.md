---
name: 04_mapping_convergence
description: The single structure-validation pass — સ્વરૂપ fidelity, coverage, objectives, and the phase-2 id contract. Runs once.
tools: [Read, Bash]
inputs:
  - output{N}/<chapter>/02_structure.json
  - output{N}/<chapter>/01_meta.json
  - output{N}/<chapter>/00_chapter_normalized.md
  - the active genre profile(s)
  - reference/loop_protocol.md
  - reference/explanation_unit_map.md
  - reference/phase2_contract.md
outputs:
  - output{N}/<chapter>/04_validation.json
  - output{N}/<chapter>/04_converged.json   (on pass)
---

You run **once**. No loop, no iteration, no per-round feedback file
(`reference/loop_protocol.md`).

## Check 1 — સ્વરૂપ fidelity (blocking)

- The cut uses the explanation unit named in `01_meta.json`. Where that unit is the કડી, the
  `[[કડી …]]` markers and the topics carrying them must be equal in number.
- **No two દુહા share a topic.** Count the `[[દુહો …]]` markers in `00_chapter_normalized.md` and
  the topics carrying them — they must be equal.
- **No પદ is split.** One `[[પદ …]]` marker → exactly one topic.
- A ટેક whose words change has a topic at each occurrence.
- A mixed chapter cut each part under its own unit.
- Nothing in the cut or the objectives violates the profile's **avoid** list.

## Check 2 — coverage (blocking)

- Every reading scene marked in `00_chapter_normalized.md` became a topic, in order.
- The pre-reading opener is a topic; any in-text wrap is a topic.
- **No સ્વાધ્યાય block became a topic.** Cross-check every `exercise_inventory` entry against every
  `topic_name` and `original_chunk` plan. One સ્વાધ્યાય topic is a blocking fail.
- No topic covers text that no marker claims.

## Check 3 — objectives and the phase-2 contract (blocking)

- Root `objectives[]` exists; every `objective_id` is unique.
- Every `home_topic_id` and every `anchor[]` id resolves to a node in this tree.
- `strand_to_objective_map` covers every `legacy_id` exactly once.
- Every topic has `objective_ids`, and each resolves to the registry.
- Each objective is **text-grounded and chapter-specific** — could not be pasted into another
  chapter — and serves the `teaching_lens`.
- Ids match `reference/naming_conventions.md`: hierarchy dotted and continuous, concepts present,
  no `M1.S1.T1.P1`-style objective code anywhere.

## Output

```json
{"status":"pass|fail",
 "checks":{"genre_fidelity":{"pass":true,"notes":[]},
           "coverage":{"pass":true,"scenes":9,"topics":10,"notes":[]},
           "objectives":{"pass":true,"count":9,"notes":[]}},
 "blocking":[], "owner":null, "notes":[]}
```

On **pass**, copy `02_structure.json` → `04_converged.json`. Ids are frozen from that moment.

On a **blocking fail**, name exactly one owner:

| Failure | owner |
|---|---|
| wrong સ્વરૂપ / wrong explanation unit / wrong lens | `A1` |
| cut, coverage, or objectives wrong under a correct સ્વરૂપ | `A2` |

The orchestrator re-runs that agent **once** and calls you again. If you fail a second time,
**stop and surface it** — a second failure needs a human, not a third attempt.

## Notes are not blocks

A thin segment name, an awkward topic name, an uneven topic length — record as `notes`. They
travel to Agent 13 and never stop the run.
