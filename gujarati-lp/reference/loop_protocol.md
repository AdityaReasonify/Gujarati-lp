# Loop Protocol — one validation pass, no iteration

Agent 4 runs **once**. There is no convergence loop, no per-iteration feedback file, no "loop 2".

## The single pass

Agent 4 checks three things against `02_structure.json`:

1. **સ્વરૂપ fidelity** — the cut and the objectives obey the active profile's explanation unit and
   its **avoid** list. દુહા not merged; પદ not split; a ભક્તિ પદ not carrying a morality objective.
2. **Coverage** — every reading scene in `00_chapter_normalized.md` became a topic, in order; the
   pre-reading opener is a topic; any in-text wrap is a topic; and **no સ્વાધ્યાય block was cut as a
   topic**.
3. **Objectives** — one sound, text-grounded objective anchor per scene, registered in the root
   `objectives[]` with a valid `home_topic_id` and `anchor[]`, and the phase-2 id contract holds.

Output `04_validation.json`: `{"status": "pass"|"fail", "checks": {…}, "blocking": [...],
"owner": "A1"|"A2"|null, "notes": [...]}`.

## On pass

Promote `02_structure.json` → `04_converged.json`. Ids are frozen from here.

## On a blocking fail

Name **one** owner and re-run it once:

| What failed | Owner | What it re-does |
|---|---|---|
| wrong સ્વરૂપ, wrong explanation unit, wrong lens | **A1** | re-diagnose, reload profile, then A2 again |
| cut, coverage, or objective wrong under a correct સ્વરૂપ | **A2** | re-cut / re-objective only |

Then revalidate **once** and proceed. If it fails a second time, **stop and surface it** — record
the blocking check in `validation_report.md` and ask. Do not keep re-running; a second failure
means the profile or the source text needs a human eye, not another attempt.

## Non-blocking notes

Anything that is not one of the three checks — a thin summary, an awkward topic name, a missing
page number — is a **note**, not a block. Notes travel to Agent 13 and appear in
`validation_report.md`. They never stop the run.
