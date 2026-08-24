# विधा Diagnosis (Step 1) — read four signals, then decide

Diagnose from **your** chapter. Never from a sample, never from the title alone.

## The four signals

**A — Structure.** Is the text in पंक्तियाँ with तुक and लय, or in paragraphs?
If verse: how long is one unit — two lines (दोहा), four (छंद), or a whole song with a टेक (पद)?
If prose: does it move by घटना, by स्मृति, by तथ्य, or by संवाद?

**B — Unit / chapter theme.** What is this chapter *for* in the reader — देशभक्ति, नीति, भक्ति,
वीरता, प्रेरणा, संस्कृति, पर्यावरण? Signal B breaks ties: a poem in a नीति section is a नीति
lesson even if it could be read as nature description.

**C — अभ्यास.** The exercises reveal what the book thinks it taught. Questions about तुकांत and
अलंकार say काव्य-कला. Questions about "क्या होता अगर" say कहानी. Questions asking the child to
recall a custom say सूचनात्मक. Questions about शब्द-युग्म and मुहावरे say भाषा की बात.

**D — Purpose.** What does the text *do* — sing, teach a नीति, remember a life, describe a
practice, argue a case, tell a story?

## Routing

```
Is the text in verse?  ── YES → sub-diagnose by UNIT LENGTH first:
│   ├─ two-line self-contained units, each with its own image and turn, कवि-छाप in the line
│   │      → niti_doha.md            (HARD: one दोहा = one topic, never merge)
│   ├─ a sung पद with a टेक, a देवता or भक्त speaking, ब्रज/अवधी forms
│   │      → bhakti_pad.md           (HARD: do not flatten to a morality lesson)
│   ├─ charge, speed, a horse or a warrior, ओज in the rhythm
│   │      → vir_ras_kavita.md
│   └─ nature, the land, a season, a call to the country, first-person feeling
│          → prakriti_deshbhakti_kavita.md
│
└─ PROSE → what moves it?
    ├─ a plot with characters and a turn                      → kahani.md
    ├─ a real person remembering, or a life told in sequence  → sansmaran.md
    ├─ facts, a custom, a dance, a place, a practice          → soochnatmak_sanskritik.md
    └─ two voices arguing, or an essay making a case          → samvad_nibandh.md
```

If signals conflict, set `genre_confidence: "low"`, record the conflict in `01_meta.json`, and
**surface it before drafting.**

## Mixed chapters — common in मल्हार

A मल्हार chapter often carries a main text **plus** an appended piece of a different विधा: गोल
(संस्मरण) ends with the डाँडी-गोथा description (सूचनात्मक) and a separate short story; हार की जीत
carries a short poem. When that happens:

1. `genre: "mixed"`, parts listed **dominant first**.
2. **Load every matching profile**, dominant first.
3. **Cut each part under its own explanation unit** — the appended poem is cut छंद-wise even
   though the dominant part is cut घटना-wise. Do not flatten to one unit.
4. Apply each part's lens and avoid-list **to that part only**.
5. Agents 7 and 13 check that no part lost its essence to the dominant विधा's template.

## What must be recorded in `01_meta.json`

`genre`, `genre_signals` (what each of A–D showed), `genre_confidence`, `teaching_lens`,
`guiding_question`, `explanation_unit`, `active_genre_profiles`, plus the structural inventory
(how many छंद / दोहे / पद / घटनाएँ) and the **अभ्यास inventory** — every अभ्यास block found, so
Agent 10 can answer all of them and Agent 4 can confirm none was cut as a topic.
