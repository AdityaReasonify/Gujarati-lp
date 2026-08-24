# QC Checklist (Step 8) — Agent 13's gate

Sections **A–D are hard fails** and block the run. **E–G are reported** in
`validation_report.md` and fixed where cheap.

## A — Diagnosis and lens (hard)
- [ ] विधा diagnosed from the four signals, recorded with `genre_signals` and `genre_confidence`.
- [ ] The **explanation unit matches the विधा** — दोहे one per topic, पद whole, छंद per topic,
      गद्य by घटना/तथ्य/तर्क.
- [ ] A mixed chapter loaded every profile and **cut each part under its own unit**.
- [ ] Reading the topics' explanations in order actually answers the `guiding_question`.

## B — Verbatim and structure (hard)
- [ ] Every topic has an exact Devanagari `original_chunk`; nothing paraphrased, transliterated,
      modernised, or "corrected" (`यमुन`, `नहिं`, `मातुभूमि` intact; कवि-छाप intact).
- [ ] Verse line breaks and मात्राएँ preserved; the attribution line kept.
- [ ] Every reading scene became a topic, in order; **no अभ्यास block became a topic**.
- [ ] Ids consecutive and every cross-reference resolves after Agent 14's renumber.

## C — The teaching block (hard)
- [ ] Every topic has `explanation` **and** `real_life_example`, both non-empty.
- [ ] `explanation` gives क्या हो रहा है + अर्थ, glosses hard words inline, and adds the deeper
      reading **only where the passage carries it**.
- [ ] `real_life_example` is **Indian, concrete, single, and within an eleven-year-old's
      experience** — not an adult's example, not an abstraction, not three examples.
- [ ] Voice: खड़ी बोली, second person, 55–90 words; `objective_text` 12–30 words.

## D — विधा essence (hard)
- [ ] The active profile's **avoid** list is not violated anywhere.
- [ ] No शिक्षा forced onto a text that does not carry one.
- [ ] A भक्ति पद keeps its भाव; a नीति दोहा keeps its दृष्टांत; a वीर-रस छंद keeps its ओज; a
      सांस्कृतिक description keeps the community's dignity and its real name.
- [ ] `figures_of_speech` names only devices genuinely in the lines; `[]` where there are none.

## E — अभ्यास and risk (reported)
- [ ] Every inventoried अभ्यास block answered, skill-tagged, mapped to topics.
- [ ] Personal-opinion items marked as model answers.
- [ ] Empty tables filled with teaching values.
- [ ] Sensitivity notes applied where the chapter touches religion, region, community, disability
      or war.

## F — Shape and media (reported)
- [ ] The 12 `json_contract.md` invariants hold.
- [ ] `publication_id` is set (not null); `topic_type` is `instructional`/`summary`/`assessment`;
      segment recalls are `.RQ{n}` not `.SR{n}`; concept numbers run chapter-continuous. These
      four were each rejected by the server on the first real run.
- [ ] One image per reading scene; ≤1 `2d_tool` per chapter.
- [ ] Reused images name their source frame; unmatched scenes carry a real `generation_prompt`.
- [ ] Three-tier summaries strictly increase; no numbers in display text.

## G — The seven mistakes a Hindi plan usually makes (reported)
1. सारांश + शिक्षा + प्रश्न-उत्तर instead of teaching the विधा.
2. दोहे merged into one "stanza" topic.
3. A पद split line by line.
4. A poetic licence silently corrected — `यमुन` printed as `यमुना`.
5. An अलंकार named because the field existed, not because it was there.
6. A `real_life_example` written for an adult, or set outside India.
7. अभ्यास cut as teaching topics, leaving the exercise deliverable half-empty.

## Verdict
`validation_report.md` records: विधा + confidence, the pass/fail of A–D with the failing item
named, the E–G notes, the media summary, and the LP2 validator result. **A run with any A–D
failure is not complete**, however good the rest looks.
