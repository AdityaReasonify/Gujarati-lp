# Explanation Unit Map (Step 3) — विधा → how the text is cut into teaching blocks

The विधा decides the **explanation unit**: the natural chunk of text that becomes one teaching
topic. This is how Agent 2 cuts the chapter and what `original_chunk` holds per topic. Cutting a
कहानी by घटना but a कविता by छंद is the whole point — **do not use one template for all.**

| विधा | Explanation unit | One topic = | Notes |
|---|---|---|---|
| **प्रकृति / देशभक्ति काव्य** | **छंद-wise** | one छंद (4 lines typically) | keep line breaks verbatim; a returning टेक is its own topic at each occurrence when its words change |
| **नीति-काव्य / दोहा** | **दोहा-wise** | **one दोहा — two lines, complete in itself** | never merge two दोहे into one topic, however short |
| **भक्ति-पद** | **पद-wise** | one पद (the whole song) | the पद is one utterance; do not split it by line |
| **वीर-रस काव्य** | **छंद-wise** | one छंद | the rhythm carries the charge; keep the छंद whole |
| **कहानी** | **घटना-wise** | one plot beat | follow the story's turns, not paragraph counts |
| **संस्मरण / जीवनी** | **स्मृति / जीवन-चरण-wise** | one remembered episode or life stage | a memoir moves by memory, not by clock |
| **सूचनात्मक / सांस्कृतिक गद्य** | **तथ्य / प्रथा-wise** | one fact, custom or practice | the prose wraps a fact; the fact is the topic |
| **संवाद / निबंध** | **तर्क-wise** | one strand of the argument, or one exchange that completes a thought | keep both speakers' words verbatim |

## The two units English has no name for

**दोहा.** A दोहा is a complete poem in two lines — a self-contained thought with its own image and
its own turn. रहीम के दोहे is not one poem in stanzas; it is a *collection* of independent poems
printed together. Treating it "stanza-wise" the way an English pack would fuses couplets that
share nothing but a page. **One दोहा = one topic, always**, even when it is shorter than the
explanation that follows it.

**पद.** A पद is one devotional song, sung as a whole. Splitting it by line breaks the utterance —
the child-Krishna's whole defence in मैया मैं नहिं माखन खायो is one continuous speech and reads as
one. **One पद = one topic**, even when it runs longer than a छंद.

## Hard rules for cutting (Agent 2 + Agent 5)

1. **Exact text first.** Every topic carries the verbatim Devanagari passage in `original_chunk`.
   Nothing dropped, paraphrased, or transliterated (`reference/devanagari_verbatim.md`).
2. **A pre-topic hook belongs to the NEXT topic.** A line that introduces the next छंद opens
   *that* topic, not the tail of the previous one.
3. **Single-theme topics.** One छंद / दोहा / पद / घटना per topic. If a छंद does two clearly
   different things it may split; if two very short छंद do one thing they may join — decide from
   the content, and never for दोहा or पद.
4. **Topics are reading scenes + pre-reading only; अभ्यास is NOT a topic.** The textbook blocks —
   **मेरी समझ से**, **सोच-विचार के लिए**, **भाषा की बात**, **कविता की रचना**, **आपकी बात**,
   **मिलकर करें मिलान** — are handled solely by Agent 10 in `exercise_solutions.json`, mapped to
   the reading scenes that prepare them. Cutting them as topics is a hard fail.
5. **The टेक (refrain) is content, not repetition to skip.** Where a टेक returns with **changed
   words** — मातृभूमि's पुण्य/स्वर्ण → धर्म/कर्म → युद्ध/बुद्ध — each occurrence is its own topic
   and the teaching names *what changed*. Where a टेक returns **identical**, teach it at first
   occurrence and reference it afterwards.

## topic_type
- `POEM` — a छंद / दोहा / पद being read and explained.
- `STORY_TELLING` — a narrative घटना or remembered episode.
- `CONCEPT` — pre-reading, a taught idea, a fact, a लेखक-परिचय box.
- `REVIEW` — an in-text summary or value wrap. (अभ्यास is never a topic.)

`topic_category` is a finer descriptive label: `introduction` / `core` / `climax` / `transition` /
`resolution` — descriptive, never a number.
