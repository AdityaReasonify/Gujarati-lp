# अलंकार और छंद — the craft analysis (काव्य topics only)

Fills the topic-level `figures_of_speech[]` and `rhyme_scheme`, and the module-level
`difficult_words[]` and `overall_rhyme_scheme`. For गद्य these are `[]` / `null`, except that a
genuine अलंकार in prose may still be listed.

> **The one rule that outranks the rest: never invent an अलंकार to fill the field.** If a छंद has
> none, `figures_of_speech` is `[]`. A named device that is not in the lines is a hard fail at
> Agent 13 — it teaches the child something untrue about the text.

## अलंकार a class-6 reader can actually see

| अलंकार | What to look for | Example from class-6 मल्हार |
|---|---|---|
| **अनुप्रास** | the same ध्वनि returning across nearby words | `झरने अनेक झरते` — the `झ` returns and you hear the waterfall |
| **मानवीकरण** | a निर्जीव thing doing a living thing's act | `हिमालय आकाश चूमता है`; `सिंधु … झूमता है` |
| **उपमा** | an explicit comparison — `सा`, `जैसा`, `समान` | `करुणा के अश्रु-सी वर्षा` |
| **रूपक** | the thing *is* the other, no comparison word | `स्वर्ण-भूमि` — the land *is* gold |
| **श्लेष** | one word carrying two meanings at once | `जग को दिया दिखाया` — `दिया` = दीपक and = दिखा दिया |
| **पुनरुक्ति** | a word deliberately repeated | `पग-पग`, `वह … मेरी` returning through the टेक |
| **यमक** | the same word repeated in different senses | (rarer at this level; name it only if unmistakable) |

Entry shape — quote the **exact words from this छंद**, never a paraphrase:

```json
{"device": "श्लेष", "lines": "जग को दिया दिखाया",
 "note": "'दिया' के दो अर्थ एक साथ — दीपक भी, और 'दिखा दिया' भी।"}
```

## छंद, लय और तुक

`rhyme_scheme` per काव्य topic:

```json
{"pattern": "AABB", "rhyming_words": ["चूमता — झूमता"],
 "note": "दूसरी और चौथी पंक्ति का तुक मिलता है, जिससे पढ़ने में झूला-सी लय बनती है।"}
```

- Name the **तुकांत** honestly. A near-rhyme is a near-rhyme — say so in the `note`.
- **दोहा** — two lines, 13+11 मात्राएँ per line, the तुक at the end of each line. Say this once in
  the module's `overall_rhyme_scheme`; do not repeat the metre lecture on every दोहा.
- **पद** — has a टेक plus अंतरा, sung; note the refrain, not a strict pattern.
- Where a कवि bends a word for लय — `यमुन` for `यमुना` — that belongs in the topic's
  `explanation` and in `key_terms`, and it is **काव्य-कला, not a mistake**. Say so explicitly; a
  class-6 child will otherwise read it as a printing error.

## Module-level closing pair

- **`difficult_words`** — 5–10 words from the whole chapter, each
  `{"word": …, "meaning": <student-friendly, concrete>, "example": <a FRESH everyday sentence, not
  the poem's own line>}`. Lead with words the child will meet again (`shabd_gloss.md`).
- **`overall_rhyme_scheme`** — the whole poem's pattern plus the effect, and any chapter-wide टेक.

## How deep to go

Name the अलंकार, quote the words, say **what it does** in one line. That is the whole job. Do not
- list every possible device in a छंद (one or two that genuinely do work);
- write a छंद-शास्त्र lecture on मात्रा counting for an eleven-year-old;
- keep the label without the effect — `"अनुप्रास है"` alone teaches nothing.
