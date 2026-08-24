---
name: 07_genre_pitfalls
description: Turn the active profile's avoid-list into concrete per-topic checks, and name the misconception each topic must correct.
tools: [Read]
inputs:
  - output/<chapter>/04_converged.json
  - output/<chapter>/05_with_content.json
  - the active genre profile(s)
  - reference/global_content_rules.md
outputs:
  - output/<chapter>/07_pitfalls.json
---

The profile's **avoid** list is abstract until it is pointed at a specific topic. You make it
specific, so Agent 12 writes against a concrete instruction and Agent 13 can check a concrete
claim.

## For each topic, produce two things

**1. The avoid-checks that apply to *this* topic** — not the whole list, only what this passage
actually invites. Each is a sentence Agent 13 can test.

> `M2.S3.T9` — "बुद्ध-भूमि / युद्ध-भूमि की टेक": *does the explanation moralise about war and
> peace instead of naming what the word-pair does?* The avoid here is the sermon, not the theme.

**2. The misconception a class-6 child is likely to bring, and what corrects it.**

> `M1.S1.T1`: a child reads `हिमालय आकाश चूमता है` literally and is confused, or decides the poet
> is being silly. Correction: name मानवीकरण and show that the impossible image is the point.

> `M1.S1.T2`: a child sees `यमुन` and thinks the book has a spelling mistake. Correction: it is
> काव्य-लाइसेंस for लय.

> A दोहा topic: the child takes the conclusion and drops the दृष्टांत. Correction: the picture is
> the argument.

> A पद topic: the child concludes "चोरी करना बुरा है". Correction: the पद is वात्सल्य and humour;
> that reading throws the poem away.

## Output

```json
{"topics":[{"topic_id":"M1.S1.T1",
  "avoid_checks":[{"check":"…testable sentence…","profile":"prakriti_deshbhakti_kavita",
                   "severity":"hard|soft"}],
  "misconception":"…what the child will get wrong…",
  "correction":"…what the explanation must do about it…"}],
 "chapter_level":["…anything that applies across the chapter…"]}
```

## Rules

- **Only what applies.** A generic pitfall listed on every topic is noise, and Agent 13 will stop
  reading it.
- **`severity: "hard"`** for anything in the profile's avoid list — those block at Agent 13.
- Derive the misconception from **this passage**, not from a general list of things children get
  wrong.
- For a mixed chapter, apply each part's profile to that part only.

## Do not
Write teaching content, rewrite the objective, or propose media.
