# Paused standards — 2026-08-23 06:47 IST

std-7, std-8, std-9, std-10 were paused to let std-6 finish first.

Nothing is lost: all state derives from output files on disk. To resume any of them:

    cd /Users/aditya/Downloads/Gujarati-lp/scratch
    python3 args_for.py <STD> 3        # prints ready-to-use args, skipping completed chapters
    # then launch chapter-runner-optimized.js with those args

Known items carried into the resume:
- std-8 ch02: A1 transcribed ઈંદ્ર (long ઈ); print shows ઇંદ્ર (short ઇ). Corrected on disk
  2026-08-23 with provenance in 00_chapter_normalized.md; pre-fix backup at
  00_chapter_normalized.md.pre-indra-fix. A5 re-verifies on re-run.
- std-7 ch03 was at 10/14 (through A12) when paused.
- std-8 ch03 was at 13/14 (needs A15 only).
- Two spec conflicts still open, both needing a human decision:
  1. publication_chunk: agents/13 says byte-identical to original_chunk; agents/16 says the
     block as a whole with verbatim inside. They contradict.
  2. agents/07 section 2 vs reference/global_content_rules.md section 5 are jointly
     unsatisfiable for real_life_example nouns.
