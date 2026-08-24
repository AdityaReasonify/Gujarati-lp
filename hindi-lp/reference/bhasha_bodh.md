# भाषा-बोध — शब्दार्थ, समानार्थी, विलोम, व्याकरण और अलंकार

The English pack teaches craft through simile and metaphor. Hindi needs more than that: a class-6
Hindi lesson is expected to build **शब्द-भंडार** as well as read the text. These five fields do
that, per topic.

| field | what it carries |
|---|---|
| `figures_of_speech` | **अलंकार** — the English `simile/metaphor` slot (`reference/alankar_chhand.md`) |
| `shabdarth` | **glossary** — `{shabd, arth, prakar}`; `prakar` ∈ तत्सम / तद्भव / देशज / उर्दू-मूल / काव्य-रूप |
| `samanarthi` | **समानार्थी शब्द** — `{shabd, samanarthi: [...]}` |
| `vilom` | **विलोम शब्द** — `{shabd, vilom}` |
| `vyakaran` | **व्याकरण-बिंदु** — `{bindu, udaharan, note}` |

## The one rule that governs all five

**The word must occur in THIS topic's `original_chunk`.** These fields build vocabulary *from the
text the child just read* — they are not a general Hindi word-list bolted onto a poem. A
समानार्थी for a word the chapter never uses teaches nothing and cannot be checked.

Everything in `reference/no_hallucination_policy.md` applies. `[]` is a correct answer:
- a topic whose words are all everyday → `shabdarth: []`
- no word with a worthwhile synonym → `samanarthi: []`
- **`vilom` is the emptiest by nature** — most nouns have no true opposite. Give विलोम only where
  one genuinely exists (उजाला–अँधेरा, निर्भीक–भीरु, हार–जीत), never a forced pair like चेतक–?

## Sourcing

The textbook usually asks for these itself, and that is the best source:
- ch11 has a **समानार्थी शब्द** exercise (हय / अश्व / घोड़ा; रण / युद्ध / समर)
- ch5 has **शब्द-संपदा** and **शब्द एक अर्थ अनेक**
- ch1 has **शब्दों के रूप** (शब्द-युग्म) and भूमि-compounds
- ch3 has **अनेक शब्दों के लिए एक शब्द** (जलधर)

Where the chapter's own अभ्यास names a set, use it — the plan then prepares the exercise instead
of competing with it (`reference/exercise_alignment.md`).

## व्याकरण — keep it to what the passage shows

A `vyakaran` entry names a grammar point the passage **demonstrates**, with its example from the
text: संज्ञा (व्यक्तिवाचक/जातिवाचक), सर्वनाम, विशेषण, क्रिया, काल, वचन, लिंग, उपसर्ग-प्रत्यय,
संधि, समास, शब्द-युग्म, निपात, मुहावरा.

Two or three per topic at most. This is a literature lesson that also builds language — not a
grammar chapter. If the chapter has a real व्याकरण section, that belongs to Agent 10.

## Shape

```json
"shabdarth":  [{"shabd": "अरि", "arth": "शत्रु", "prakar": "तत्सम"}],
"samanarthi": [{"shabd": "घोड़ा", "samanarthi": ["हय", "अश्व", "तुरंग"]}],
"vilom":      [{"shabd": "निर्भीक", "vilom": "भीरु"}],
"vyakaran":   [{"bindu": "व्यक्तिवाचक संज्ञा", "udaharan": "चेतक, राणा प्रताप",
                "note": "किसी एक ही व्यक्ति या प्राणी का नाम व्यक्तिवाचक संज्ञा कहलाता है।"}]
```

3–6 `shabdarth`, 2–4 `samanarthi`, 0–3 `vilom`, 2–3 `vyakaran` per topic is the working band.
These are extras beyond the phase-2 contract; the LP2 validator accepts them and the server
stores them — **verified end-to-end**: all 133 topics across the 13 class-6 chapters were uploaded
and read back with `shabdarth` intact (`output/_verify_all.py`).

## Where to put it in the chapter's own files

Chapters written after this rule carry the four fields inline in each topic dict. Chapters written
before it got a **sidecar** — `output/<chapter>/_bhasha_bodh.py`, a `BB` dict keyed by `topic_id` —
merged in just above `SPEC`:

```python
from _bhasha_bodh import BB   # needs sys.path.insert(0, HERE)
for _t in TOPICS:
    _t.update(BB[_t["tid"]])
```

Keep the sidecar even after the fact. It leaves the authored teaching text untouched, and it puts
every word of a chapter's language material on one screen where a Hindi teacher can check it in
one pass — which is exactly how it should be reviewed. `output/_patch_bhasha_bodh.py` adds the two
lines to a `content.py` that lacks them.

## Class 3 (वीणा) — the block is not about words yet; it is about letters and sounds

This is the finding that matters most for the primary grades, and it is the one a reader coming
down from class 5 will get wrong. **Class 3's भाषा की बात is largely वर्ण, मात्रा and ध्वनि work** —
below the vocabulary level entirely. Measured across all eighteen chapters (the pages carrying a
भाषा की बात or शब्दों का खेल banner, plus the page after):

| category | chapters | what to put in the plan |
|---|---|---|
| **वर्ण · मात्रा · अक्षर** | **8** — ch1, 2, 3, 4, 5, 7, 10, 13 | one `vyakaran` entry naming the letter or मात्रा **with the chapter's own word**. This is the block's centre of gravity at class 3 |
| **तुकांत शब्द** | 3 — ch2, 4, 10 | `vyakaran`, `bindu: "तुक"`, `udaharan` = the printed rhyme pair. Say the two words together; do not analyse the rhyme |
| **विलोम** | 2 — ch4, 6 | `vilom`, from the chunk, one pair |
| **शब्दार्थ / मिलान** | 2 — ch1, 4 | `shabdarth` with `prakar` |
| **विराम चिह्न** | 2 — ch9, 14 | `vyakaran` |
| **संज्ञा** | 1 — ch12 | `vyakaran`, naming the part of speech with the chapter's own example |
| **मुहावरे** | 1 — ch14 | `vyakaran`, `udaharan` = the printed line |
| **वचन** | 1 — ch4 | `vyakaran` |

**What is out of range at this band**, and asking for it is a defect rather than a bonus: विशेषण,
सर्वनाम and क्रिया identification as graded tasks, लिंग, समास, संधि, प्रत्यय, तत्सम/तद्भव sorting,
and every class-8-to-10 demand. The book asks for none of them. **समानार्थी does not appear at all**
at class 3 — do not add it because class 5 has it.

Keep it to **one entry per topic** at this grade, and prefer whatever the chapter's own block is
heading towards. `figures_of_speech` is `[]` for very nearly every class-3 topic and that is the
correct answer — `profiles/boards/cbse_hindi.md` §Class 3.

> **The scan under-reports and cannot do otherwise.** Class 3's banners are graphics beside their
> block and many items are pictures with no text layer at all, so this table is a floor, not a
> census. Read the block off the render before answering it.

## Class 4 (वीणा) — the block turns into parts of speech, and that is the whole change

The same measurement over all thirteen class-4 chapters shows the ladder's next rung clearly:
**वर्ण work almost disappears (1 chapter, ch10) and शब्द-भेद takes over.**

| category | chapters | what to put in the plan |
|---|---|---|
| **विशेषण** | **4** — ch8, 10, 12, 13 | one `vyakaran` entry, part of speech named **with the chapter's own example** |
| **संज्ञा** | 3 — ch3, 10, 13 | same |
| **विलोम** | 3 — ch4, 10, 12 | `vilom`, from the chunk |
| **मुहावरे** | 3 — ch5, 9, 11 | `vyakaran`, `bindu: "मुहावरा"`, `udaharan` = the printed line |
| **वचन** | 2 — ch8, 9 | `vyakaran` |
| **लिंग** | 2 — ch3, 13 | `vyakaran` — new at this grade, absent at class 3 |
| **विराम चिह्न** | 2 — ch5, 11 | `vyakaran` |
| **क्रिया** | 1 — ch3 | `vyakaran` |
| **शब्दार्थ / मिलान** | 1 — ch2 | `shabdarth` with `prakar` |

**Out of range at class 4**: समास, संधि, प्रत्यय, तत्सम/तद्भव/देशज/आगत sorting, सकर्मक vs अकर्मक,
पदबंध. वीणा class 4 asks for none of them. **समानार्थी is still absent** — it arrives at class 5.

Two entries per topic at most, as at class 5. `शब्द-पिटारा` and `शब्द खेल` are this grade's extra
banners and they belong to the same block for Agent 10's purposes.

So the measured ladder across the series is **वर्ण/मात्रा → शब्द-भेद → मुहावरे और समास**, one rung
per grade, and it is worth stating because it is not a difficulty ladder — it is a change of unit.

## Class 5 (वीणा) — the block is vocabulary noticing, and it quotes the chapter at you

वीणा's **भाषा की बात** is the closest fit in the whole corpus to the rule at the top of this file,
and for a structural reason: **it almost always quotes the chapter's own sentence and then asks
about a word in it.** ch6 prints four lines of the poem and asks the child to underline the मुहावरा
inside them; ch2 prints *"तीसरी मूर्ति भी उड़ गई।"* and asks which word is the संज्ञा; ch7 prints
*"विलायती खेलों में सबसे बड़ा ऐब है…"* and names विलायती, बड़ा and महँगे as the विशेषण. So the
source is never a general word-list — it is the passage, and the plan's job is to prepare the
exercise rather than compete with it (`reference/exercise_alignment.md`).

Measured across all twelve chapters, वीणा asks for exactly these and nothing beyond them:

| category | where it appears | what to put in the plan |
|---|---|---|
| **समानार्थी** | ch1 (नभ, हवा, पेड़, फूल, दुनिया), ch4, ch11 | `samanarthi`, standard Hindi, from the chunk |
| **विलोम** | ch1, ch9 | `vilom` — and this stays the emptiest field |
| **शब्दार्थ / मिलान** | ch11 (शिलाखंड, गुफा, कुंड, भिक्षु) | `shabdarth` with `prakar` |
| **संज्ञा · विशेषण · सर्वनाम · क्रिया** identification | ch2, ch6, ch7, ch10 | one `vyakaran` entry naming the part of speech **with the chapter's own example** |
| **विराम चिह्न** | ch2, ch10 | `vyakaran` — and note वीणा teaches it by printing a passage stripped of them |
| **मुहावरे** | ch5, ch6, ch11 | `vyakaran`, `bindu: "मुहावरा"`, `udaharan` = the printed line |
| **द्विरुक्ति** (ठिठुर-ठिठुरकर) and particles like **'भर'** | ch3 | `vyakaran` — small, precise, and unique to this reader |
| **वचन**, **उद्धरण चिह्न** | ch4 | `vyakaran` |
| **अनेक शब्दों के लिए एक शब्द** | ch8 | `vyakaran` |
| **simple समास** (विश्रामगृह = विश्राम + गृह) | ch11 | `vyakaran`, broken open once |

**What is out of range at this band**, and asking for it is a defect rather than a bonus:
संधि, तत्सम/तद्भव/देशज/आगत sorting as a graded task, प्रत्यय formation, सकर्मक vs अकर्मक क्रिया,
and पदबंध. Those are class-8-to-10 demands (§Class 10 in `profiles/boards/cbse_hindi.md`); वीणा
does not ask for any of them and neither should the plan.

Keep it to **two entries per topic at most**, and prefer the one the chapter's own block is
heading towards. `figures_of_speech` is `[]` for most class-5 topics and that is the correct
answer — `profiles/boards/cbse_hindi.md` §Class 5.

## Old-language chapters carry the most weight here

For ब्रजभाषा (ch9 सूरदास) and अवधी-ब्रज दोहे (ch5 रहीम) this is not a vocabulary extra — it *is*
the reading aid. There, `shabdarth` must give the खड़ी बोली form of every archaic word
(`पठायो` → भेजा, `पतियायो` → विश्वास किया), `prakar` says `ब्रज`, and one `vyakaran` entry should
name the pattern rather than the single word — e.g. "ब्रज में भूतकाल की क्रिया 'यो' पर समाप्त होती
है, खड़ी बोली में 'या' पर." A child who learns the pattern reads the next पद unaided.

Keep `samanarthi` and `vilom` in standard Hindi even when `shabdarth` is in ब्रज — the child needs
to hold both forms side by side, and that contrast is the lesson.
