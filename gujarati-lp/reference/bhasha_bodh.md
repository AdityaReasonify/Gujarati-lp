# ભાષા-બોધ — શબ્દાર્થ, સમાનાર્થી, વિરુદ્ધાર્થી, વ્યાકરણ અને અલંકાર

The English pack teaches craft through simile and metaphor. Gujarati needs more than that, and a
**second-language** Gujarati reader needs more again: a GSEB ગુજરાતી (દ્વિતીય ભાષા) chapter is
expected to build **શબ્દભંડોળ** as well as be read. Every measured chapter in stds 6–10 ends with a
**શબ્દાર્થ** box before its exercises, and stds 6 and 8 close every single chapter with
"નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો." — the book is telling you, 15 times out of 15,
that word-meaning is half the lesson. These five fields do that work, per topic.

| field | what it carries |
|---|---|
| `figures_of_speech` | **અલંકાર** — the English `simile/metaphor` slot (`reference/alankar_chhand.md`) |
| `shabdarth` | **glossary** — `{shabd, arth, prakar}`; `prakar` ∈ તત્સમ / તદ્ભવ / દેશ્ય / આગત / કાવ્ય-રૂપ |
| `samanarthi` | **સમાનાર્થી શબ્દો** — `{shabd, samanarthi: [...]}` |
| `vilom` | **વિરુદ્ધાર્થી શબ્દો** — `{shabd, vilom}` |
| `vyakaran` | **વ્યાકરણ-બિંદુ** — `{bindu, udaharan, note}` |

**The key names stay romanized.** `shabdarth`, `samanarthi`, `vilom`, `vyakaran` are JSON keys on the
topic object, accepted and stored by the LP2 server (`reference/phase2_contract.md`). Do not translate
them, do not rename `vilom` to `virudhdharthi`. Only the *values* are Gujarati script.

## The one rule that governs all five

**The word must occur in THIS topic's `original_chunk`.** These fields build vocabulary *from the
text the child just read* — they are not a general Gujarati word-list bolted onto a કાવ્ય. A
સમાનાર્થી for a word the chapter never uses teaches nothing and cannot be checked.

The chapter-end **શબ્દાર્થ** box covers the whole chapter, not your topic. Filter it: a word from the
box that appears in a *different* topic's chunk belongs to that topic, not this one.

Everything in `reference/no_hallucination_policy.md` applies. `[]` is a correct answer:
- a topic whose words are all everyday → `shabdarth: []`
- no word with a worthwhile synonym → `samanarthi: []`
- **`vilom` is the emptiest by nature** — most nouns have no true opposite. Give વિરુદ્ધાર્થી only
  where one genuinely exists (સંશય–પ્રતીતિ, હાર–જીત, અજવાળું–અંધારું), never a forced pair like
  મોરલી–?

**One L2 exception to "empty is fine": `shabdarth` almost never returns `[]`.** The bar for "everyday
word" sits far lower for a second-language child than for the Hindi pack's first-language reader —
an L2 std-6 child stops on words a first-language child walks past. `reference/shabd_gloss.md` owns
that threshold; this file only says: do not use `[]` on `shabdarth` as a shortcut.

## Sourcing — the book asks for this itself, and that is the best source

Measured across the corpus inventories (the per-standard files in `reference/corpus/`), the GSEB readers
carry a standing word apparatus that hands you these fields:

| printed block | where it is measured | feeds |
|---|---|---|
| **શબ્દાર્થ** box (green/yellow, at text-end before exercises) | 15/15 chapters at stds 6, 7, 8, + all પૂરકવાચન items | `shabdarth` |
| **રૂઢિપ્રયોગ** pre-block (glossed idiom list) | std 6: chs 5, 6, 8, 10, 13, 15 · std 7: 8/15 · std 8: 11/15 + P3 · std 10: per chapter | `vyakaran` (`bindu: "રૂઢિપ્રયોગ"`) |
| **શબ્દસમૂહ માટે એક શબ્દ** pre-block | std 8: 8/15 (chs 2, 6, 8, 10, 11, 13, 14, 15) + P3 · std 9: 7/23 chapters + V4 · std 10: 14/18 | `vyakaran` |
| **કહેવત** pre-block | std 6 ch 6 (the book's only one) · std 8 ch 15 · std 9 chs 9, 13 · std 10 chs 8, 18 | `vyakaran` (`bindu: "કહેવત"`) |
| **સમાનાર્થી શબ્દો / વિરુદ્ધાર્થી શબ્દો** boxes printed per chapter | **std 9–10** — part of the fixed end-matter run (std 9: 23/23 and 22/23 chapters; std 10: 18/18 and 16/18) | `samanarthi`, `vilom` |
| **તળપદા શબ્દો** box | std 9: ~12/23 · std 10: 14/18 (chapter-dependent); std 7 chs 8, 9 as an exercise task | `shabdarth` with `prakar: "દેશ્ય"` |
| **ભાષા-અભિવ્યક્તિ** commentary paragraph | **std 9–10** — after સ્વાધ્યાય, in every chapter of both readers (23/23, 18/18) | `vyakaran`, `figures_of_speech` |
| chapter-final green **grammar box** | std 6: chs 2, 3, 4, 5, 7, 9 · std 7: chs 2, 3, 4, 6, 8, 10, 11, 12 | `vyakaran` |

Where the chapter's own સ્વાધ્યાય or apparatus names a set, use it — the plan then **prepares** the
exercise instead of competing with it (`reference/exercise_alignment.md`). Agent 1 records the exact
printed headings in `01_meta.json`'s `exercise_inventory`; read them there, never from this table's
frequencies, which are a corpus prior and not a promise about your chapter.

**The printed-glossary trap** (`reference/shabd_gloss.md`): the શબ્દાર્થ box is *evidence* that the
book thought a word hard — it is not the source of your gloss and not a list to copy wholesale. Write
the meaning a std-N child can use, in the context this chunk uses the word.

**std 10 is the gift case.** Its fixed end-matter run — શબ્દ-સમજૂતી → સમાનાર્થી શબ્દો/શબ્દાર્થ →
[તળપદા શબ્દો | વિરુદ્ધાર્થી શબ્દો | રૂઢિપ્રયોગો | કહેવત | શબ્દસમૂહ માટે એક શબ્દ] — prints four of these
five fields for you. The **ભાષા-અભિવ્યક્તિ** paragraph goes further and does this file's job in prose:
ch 1 discusses the repetition of 'વાગે છે' and the ક્રિયાપદ + 'છે' rhythm; ch 13 discusses the
'જી રે' લોકપરંપરા, the ધ્રુવપંક્તિ, and a question printed with an ઉદ્ગારચિહ્ન; ch 16 discusses
personification. Read it, take the point it names, then attach it to the topic whose chunk carries the
line. Do not paste the paragraph — it is teacher-addressed apparatus, not a topic.

## વ્યાકરણ — keep it to what the passage shows

A `vyakaran` entry names a grammar point the passage **demonstrates**, with its example from the text.

**Canonical `bindu` vocabulary** — the GSEB grammar syllabus, and a closed list for this field:
નામ · સર્વનામ · વિશેષણ · ક્રિયાપદ · કાળ · વચન · જાતિ · સંધિ · સમાસ · કૃદંત · નિપાત ·
રૂઢિપ્રયોગ / કહેવત.

**Measured GSEB additions**, admitted only in a standard whose own book teaches them (see the ladders
below): વિરામચિહ્નો · જોડાક્ષર · ક્રિયાવિશેષણ · સંયોજક · વાક્યના પ્રકારો · ઉપસર્ગ-પ્રત્યય ·
દ્વિરુક્ત / રવાનુકારી શબ્દો · શબ્દસમૂહ માટે એક શબ્દ · પ્રયોગ · અનુસ્વાર · શબ્દકોશ ક્રમ.

If a `bindu` is in neither list, you are inventing a syllabus. Fix the entry or drop it.

Two notes on wording. **જાતિ** is the canonical key word; the books print **લિંગ** on the banner
(std 7 ch 4 "સંજ્ઞાનાં લિંગ અને પ્રકાર"). Use the printed word in `udaharan`/`note` and the canonical
word in `bindu`. **દેશ્ય** is the canonical `prakar`; the books say **તળપદું**. Same treatment.

Two or three per topic at most. This is a literature lesson that also builds language — not a
grammar chapter. **If the chapter has a real વ્યાકરણ section, it belongs to Agent 10**, and at stds 9
and 10 that is not a hypothetical: those readers carry standalone વ્યાકરણ એકમો between the literature
chapters (std 9: four units; std 10: six). Those units are not chapters and never become topics.

## Shape

Worked from std 8 ch 3 **મારી વ્યાયામસાધના** — every word below is in that chapter's measured
શબ્દાર્થ / રૂઢિપ્રયોગ apparatus or in the નરસિંહ line the essay quotes:

```json
"shabdarth":  [{"shabd": "શકટ", "arth": "ગાડું", "prakar": "તત્સમ"},
               {"shabd": "શ્વાન", "arth": "કૂતરો", "prakar": "તત્સમ"},
               {"shabd": "જયમ", "arth": "જેમ", "prakar": "કાવ્ય-રૂપ"},
               {"shabd": "ઉસ્તાદ", "arth": "કુશળ ગુરુ", "prakar": "આગત"}],
"samanarthi": [{"shabd": "પ્રતીતિ", "samanarthi": ["ખાતરી", "વિશ્વાસ"]}],
"vilom":      [{"shabd": "સંશય", "vilom": "પ્રતીતિ"}],
"vyakaran":   [{"bindu": "રૂઢિપ્રયોગ", "udaharan": "અખાડા કરવા",
                "note": "'અખાડો' એટલે કુસ્તી કરવાની જગ્યા, પણ 'અખાડા કરવા' એટલે ગણકારવું નહિ. રૂઢિપ્રયોગનો અર્થ શબ્દોના સીધા અર્થથી જુદો હોય છે."}]
```

Notice what makes this correct: `સંશય` and `પ્રતીતિ` both stand in the same printed શબ્દાર્થ box, so
the વિરુદ્ધાર્થી pair is the book's own, not a dictionary's; and the `note` explains the idiom the
book already glossed rather than replacing it.

Punctuation inside these strings follows `reference/gujarati_verbatim.md`: `.` full stop, **never
`।`**, no Devanagari and no Roman outside brackets for a technical term.

**3–6 `shabdarth`, 2–4 `samanarthi`, 0–3 `vilom`, 2–3 `vyakaran`** per topic is the contract band.
Per-standard working caps inside that band are in the ladders below.

> **⚠ Provisional — end-to-end storage not yet proven for this pack.** These four keys are extras
> beyond the phase-2 contract. `reference/phase2_contract.md` states the LP2 validator accepts them
> and the server stores them; that was verified for the Hindi pack, not for this one. **No Gujarati
> chapter has been uploaded yet.** The first pilot upload must read the chapter back
> (`GET /api/lp2/learning-plans/chapter/{chapter_id}?include_json=true`, plan at
> `data.plan.planJson`) and confirm `shabdarth` survives — that is part of VERIFY-5. Until it does,
> author the fields but do not cite them as verified anywhere.

## Where to put it in the chapter's own files

Chapters written with this rule in force carry the four fields inline in each topic dict. A chapter
authored before it, or one whose language material a teacher wants to review in one pass, gets a
**sidecar** — `output{N}/<chapter>/_bhasha_bodh.py`, a `BB` dict keyed by `topic_id` — merged in just
above `SPEC`:

```python
from _bhasha_bodh import BB   # needs sys.path.insert(0, HERE)
for _t in TOPICS:
    _t.update(BB[_t["tid"]])
```

Directories follow `reference/naming_conventions.md`: `output6/` … `output10/`, chapters zero-padded `ch01`.
`output{N}/_patch_bhasha_bodh.py` adds the two lines to a `content.py` that lacks them.

Keep the sidecar even after the fact. It leaves the authored teaching text untouched, and it puts
every word of a chapter's language material on one screen where a Gujarati teacher can check it in
one pass — which is exactly how it should be reviewed.

---

# Grade ladders — what each standard's book actually asks for

> **⚠ ALL FIVE TABLES ARE PROVISIONAL (VERIFY-4).** They are assembled from the Stage-0 corpus
> inventories — now **complete for all five standards** (`reference/corpus/std-6_inventory.md` …
> `std-10_inventory.md`, every chapter's સ્વાધ્યાય and word apparatus read) — but the tables were
> drafted while std 9 and std 10 were still partial and have not been fully recalibrated against
> the completed records. The per-topic caps are targets, not measurements. Every table must be re-measured from
> the GSEB સ્વાધ્યાય blocks and grammar boxes of the standard it describes, and the result recorded
> in `profiles/boards/gseb_gujarati.md` §Std N with targets and measurements kept separately so an
> inversion cannot hide. **Read the block off the render before answering it.**

**The Hindi pack's class 3–5 ladders have no counterpart here and must not be reasoned from.** Two
concrete traps. In the Hindi reader the synonym field arrives only at class 5, whereas GSEB Gujarati
asks for **સમાનાર્થી / વિરુદ્ધાર્થી from std 6** (chs 4, 9, 12, 13) — the L2 ladder is not simply
"one rung behind" a first-language one. And the Hindi class-3 letters-and-syllables band has no
analogue here at all: std 6 is already doing જોડાક્ષર, સંજ્ઞા, વિશેષણ and કાળ. What std 6 *does*
share with that band is a script rung — the શ/ષ/સ and ળ/લ/ડ phonics of ch 6 — but it sits alongside
word-class work, not below it.

### Per-topic working caps (targets)

| std | `shabdarth` | `samanarthi` | `vilom` | `vyakaran` | `figures_of_speech` |
|---|---|---|---|---|---|
| 6 | 3–5 | 0–2 | 0–1 | **1** | `[]` |
| 7 | 3–5 | 1–2 | 0–1 | **1** | `[]` |
| 8 | 4–6 | 2–3 | 0–2 | 1–2 | `[]` |
| 9 | 4–6 | 2–4 | 0–3 | 2–3 | 0–2, from the std-9 અલંકાર canon |
| 10 | 4–6 | 2–4 | 0–3 | 2–3 | 0–2, from the std-10 અલંકાર canon |

`shabdarth` never runs at the bottom of its band, at any standard: that is the L2 calibration.
`vyakaran` runs at **one entry per topic through std 7** and reaches the full 2–3 only at std 9, when
the named canon begins.

## Std 6 — word class, કાળ, phonics · **no સંધિ, no સમાસ, no કૃદંત, no નિપાત**

Measured across all 15 chapters + R1 + R2. The ladder, in the book's own teaching order:

| category | where it appears | what to put in the plan |
|---|---|---|
| **જોડાક્ષર** formation and decomposition | ch 2 (anchor; repaired again in R1) | `vyakaran`, `udaharan` = a જોડાક્ષર word from the chunk |
| **નામ (સંજ્ઞા)** — વ્યક્તિવાચક / જાતિવાચક / સમૂહવાચક | ch 3 box, recalled R2 | `vyakaran`, part of speech named **with the chapter's own word** |
| **વિશેષણ** — વિકારી/અવિકારી, noun agreement | ch 4 box; agreement drills chs 6, 11, R1, R2 | `vyakaran` |
| **ક્રિયાપદ + ત્રણ કાળ** | ch 5 box; transformation R1, R2; routine-writing chs 14, 15 | `vyakaran`, `bindu: "કાળ"` |
| **વાક્યના પ્રકારો** — વિધાન / પ્રશ્નાર્થ / ઉદ્ગાર | ch 7 box, recalled ch 14 | `vyakaran` |
| **વિરામચિહ્નો** — અલ્પવિરામ, અવતરણચિહ્ન | ch 9 box; drills ch 10, R2 | `vyakaran` |
| **ઉચ્ચારભેદ phonics** — શ/ષ/સ, છ, ક્ષ, શ્ર; ર/ળ; ળ/ડ minimal pairs | ch 6 (anchor); repair passages R1, R2 | `vyakaran`; this is std 6's script-level rung, and the load-bearing Gujarati distinction |
| **વચન** morphology | ch 5 | `vyakaran` |
| **ઉપસર્ગ-પ્રત્યય** — -તા/-આઈ, -ખોર, -કાર, -વાન/-માન, -પૂર્વક, -નાર, -વાળા, -વાસી, અણ-/પ્ર- | chs 3, 7, 8, 11, 12, 13 — the largest strand by volume | `vyakaran`; break one word open, do not table the whole family |
| **દ્વિરુક્ત / રવાનુકારી શબ્દો** | chs 2, 5, 7, 11, 12, 13 | `vyakaran`; say the pair, do not analyse it |
| **સમાનાર્થી / વિરુદ્ધાર્થી** | chs 4, 9, 12, 13 | `samanarthi` / `vilom`, from the chunk |
| **તળપદા vs માનક** + diminutive-affection forms (ડેડકડી, ગાવલડી) | ch 4, taught as માધુર્ય | `shabdarth`, `prakar: "દેશ્ય"` or `"કાવ્ય-રૂપ"` |
| **રૂઢિપ્રયોગ** (pre-blocks) and one **કહેવત** pair | chs 5, 6, 8, 10, 13, 15; કહેવત ch 6 only | `vyakaran`, `udaharan` = the printed line |
| **શબ્દકોશ ક્રમ** | ch 6 chart; used chs 13, R2 | `vyakaran` — a skill, one entry, no more |

**Out of range at std 6**, and asking for it is a defect rather than a bonus: **સંધિ, સમાસ, કૃદંત,
નિપાત** — the inventory states flatly that they do not appear; also અલંકાર and છંદ naming, પ્રયોગ
(voice), and every std-9-to-10 demand. `figures_of_speech` is `[]` for effectively every std-6 topic
and that is the correct answer — the craft is still taught, in plain words, inside `explanation`
(`reference/alankar_chhand.md`, `profiles/boards/gseb_gujarati.md` §Std 6).

Keep it to **one `vyakaran` entry per topic** at this grade, and prefer whatever the chapter's own
grammar box is heading towards.

> The **L1-translation block** — "નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો." — is printed in
> **15/15 std-6 chapters**. It is the sharpest statement of what `shabdarth` is for in this pack: the
> `arth` must be a meaning the child can actually render in their first language. Concrete, one
> sense, the sense this chunk uses. Not a dictionary chain.

## Std 7 — the same rungs, completed; still no સંધિ/સમાસ/કૃદંત/નિપાત

Measured across all 15 chapters. Eight chapters carry a chapter-final green grammar box with a
printed topic banner, each fed by one to three exercises inside the same chapter's સ્વાધ્યાય:

| category | where it appears | what to put in the plan |
|---|---|---|
| **વિરામચિહ્નો** — પૂર્ણવિરામ, અલ્પવિરામ, પ્રશ્નવિરામ, ઉદ્ગારચિહ્ન, અવતરણચિહ્ન, ગુરુવિરામ | ch 2 box | `vyakaran`. The book itself teaches `.` as પૂર્ણવિરામ — on-page confirmation of `reference/gujarati_verbatim.md` rule 6 |
| **નામ (સંજ્ઞા)** completed to six types (+ દ્રવ્યવાચક, ભાવવાચક, ક્રિયાવાચક) | ch 3 box | `vyakaran` — the box says "ગયા વર્ષે શીખી ગયા છીએ"; do not re-teach std-6 ground as new |
| **જાતિ (લિંગ) અને વચન**, વિકારી/અવિકારી, વિભક્તિ પ્રત્યયો, નામ vs નામપદ | ch 4 box | `vyakaran` |
| **સર્વનામ** — પુરુષવાચક, પ્રશ્નવાચક, દર્શક, સાપેક્ષ, સમય/સ્થાનવાચક, સમૂહવાચક | ch 6 box | `vyakaran` |
| **ક્રિયાવિશેષણ** — રીત/કારણ/સ્થાન/સમય | ch 8 box | `vyakaran` |
| **વાક્યના પ્રકારો** extended to six (+ નિર્દેશાર્થ, આજ્ઞાર્થ, વિધ્યર્થ) | ch 10 box | `vyakaran` |
| **કાળ અને સહાયકારક રૂપો** ('છે') | ch 11 box | `vyakaran` |
| **હકારવાચક / નકારવાચક વાક્યરચના** across three tenses | ch 12 box | `vyakaran` |
| **રૂઢિપ્રયોગ** boxes (+ P3 "કહેવતો / રૂઢિપ્રયોગ") | 8/15: chs 3, 7, 8, 9, 10, 11, 12, 13 | `vyakaran`, `udaharan` = the printed line |
| **તળપદા શબ્દો** as an explicit teaching target | chs 8, 9 (ch 8's intro box mandates it) | `shabdarth`, `prakar: "દેશ્ય"` |
| **polysemy / synonym-register discrimination** | ch 7 | `samanarthi`, and say *which* sense the chunk uses |
| **ઉપસર્ગ-પ્રત્યય** | R2 blocks 3, 15, 16; શબ્દસીડી rules 80/90 | `vyakaran` |
| **જોડાક્ષર** hunt | ch 11 ex 10 | `vyakaran` |
| **દ્વિરુક્ત / રવાનુકારી** sound-words | chs 4, 9 | `vyakaran` |
| **શબ્દકોશ ક્રમ** | chs 7, 8, 14, R2 | `vyakaran` |

**Out of range at std 7**: સંધિ, સમાસ, કૃદંત, નિપાત, પ્રયોગ (voice), અલંકાર and છંદ naming. The book
asks for none of them; neither should the plan. `figures_of_speech` stays `[]`.

Still **one `vyakaran` entry per topic**. Std 7's own signature is the counterfactual question
("જો … હોત તો ?", chs 3, 6, 7, 8, 10, 12) — that shapes `recall_questions`, not this file.

## Std 8 — the pivot: patterns get named, but still no સંધિ/સમાસ/કૃદંત/નિપાત/અલંકાર

Measured across all 15 chapters. Std 8 is where `PEDAGOGY.md` §1 puts the method switch — "name it
after you've met it" — and where the corpus shows the grammar work leaving the chapter-final box and
spreading into the સ્વાધ્યાય itself:

| category | measured site | what to put in the plan |
|---|---|---|
| **કાળ** — compound-verb tense naming; present→past paragraph conversion | ch 2 §9; ch 3 §4 | `vyakaran` |
| **પ્રયોગ (voice)** — -થી ability passive, -થી impersonal, દ્વારા-passive | ch 4 §9; ch 6 §4; ch 7 §10 | `vyakaran`. New at std 8, and the on-ramp to std 10's voice transformation |
| **સંયોજક** | ch 6 §11; ch 13 §11; ch 15 §6 | `vyakaran` |
| **અનુસ્વાર** minimal pairs — ભાંગી/ભાગી, જંગ-જગ, વંદન-વદન | ch 5 §4 | `vyakaran`. The load-bearing script distinction, drilled explicitly |
| **જોડાક્ષર / સંયુક્તાક્ષર** hunts and expansion | ch 2 §4; ch 8 §4 | `vyakaran` |
| **દ્વિરુક્ત-રવાનુકારી** — ગણગણાટ, ઝગમગાટ | ch 1 §7 | `vyakaran` |
| **જાતિ / વચન** agreement — ખોલ્યો / ખોલી / ખોલ્યું; singular↔plural substitution | ch 1 §9; ch 8 §5 | `vyakaran`, `bindu: "જાતિ"` or `"વચન"` per what the item drills |
| **વાક્યના પ્રકારો** — વિધાન/ઉદ્ગાર/આશ્ચર્ય/ઇચ્છા/સંદેહ wheel; rhetorical→plain | ch 12 §9; ch 9 §4 | `vyakaran` |
| **ઉપસર્ગ-પ્રત્યય** — મહા-; agentive -જ્ઞ/-ક/-ચર/-પાલ/-સ્થ/-ધર grid; word-inside-word | ch 2 §10; ch 12 §6; ch 11 §10 | `vyakaran`; one word broken open |
| **સમાનાર્થી / પર્યાય** | R2 §2; ch 9 §9 (રંગ-compounds) | `samanarthi` |
| **વિરુદ્ધાર્થી** via prefix-repair | ch 3 §6 | `vilom` — and this is still the emptiest field |
| **polysemy / homograph** — ઉપાધિ, રસ, ભેટ; અખાડામાં vs અખાડા કરવા | ch 4 §5; ch 3 §10 | `shabdarth` (name the sense) or `vyakaran` (`bindu: "રૂઢિપ્રયોગ"`) |
| **નામ-વર્ગીકરણ** — વ્યક્તિ/સામાન્ય/વસ્તુ/સમૂહ/અનુભૂતિ | ch 15 §10બ | `vyakaran` |
| **રૂઢિપ્રયોગ** pre-blocks; **કહેવત**; **શબ્દસમૂહ માટે એક શબ્દ** | 11/15 · ch 15 · 8/15 | `vyakaran` |
| **પ્રાસ** rhyme hunts; **ભાવસૂચક શબ્દો** mood-labeling | ch 1 §4, ch 10 §8; ch 2 §8 | `vyakaran` for પ્રાસ; `rhyme_scheme` owns the pattern (`reference/alankar_chhand.md`) |
| **શબ્દકોશ** ordering and use | ch 1 §11; ch 4 §§4–6 | `vyakaran` |

**Out of range at std 8**: **સંધિ, સમાસ, કૃદંત, નિપાત, and all અલંકાર/છંદ labels.** `PEDAGOGY.md` §1
is explicit — named-device identification starts at std 9. Std 8 may *count* structure playfully
(હાઈકુ 5-7-5, દુહાની માત્રા) without naming a device. `figures_of_speech` is `[]` at std 8, and a
plan that names ઉપમા here has broken the grade gate, not enriched it.

Two entries per topic at most. Note ch 6 and ch 3 both quote **નરસિંહ** inside modern prose — see the
medieval section below; those topics carry more `shabdarth` weight than the chapters around them.

## Std 9 — the named canon begins · **now measured**

> The std-9 inventory is complete (`reference/corpus/std-9_inventory.md`, 31 of 31 units, every
> સ્વાધ્યાય and શબ્દ-સમજૂતી block read off rendered pages), and it **confirms** the વ્યાકરણ-એકમ
> table below — V1 સમાનાર્થી/વિરુદ્ધાર્થી/સ્વર-વ્યંજન/જોડણી, V2 લિંગ/વચન/અનુગ/નામયોગી/સંધિ,
> V3 વિશેષણ/ક્રિયાવિશેષણ/સંયોજક/વિરામચિહ્નો, V4 સમાસ/શબ્દસમૂહ/રૂઢિપ્રયોગ/કહેવત — in the printed
> placements shown. Per-chapter frequencies now live in the inventory's consolidated findings;
> Agent 1's per-chapter inventory remains the authority for any single chapter.

The reader carries **four standalone વ્યાકરણ એકમો** between the literature chapters. Those units are
Agent 10 territory and are never cut as topics, but their contents define the std-9 canon:

| વ્યાકરણ એકમ | printed contents | what it licenses in `vyakaran` |
|---|---|---|
| **એકમ 1** (after ch 6) | સમાનાર્થી, વિરુદ્ધાર્થી, સ્વર-વ્યંજન, જોડણી | `samanarthi`, `vilom` move to full band here |
| **એકમ 2** (after ch 11) | **લિંગ, વચન, અનુગ, નામયોગી, સંધિ** | `bindu: "જાતિ"`, `"વચન"`, **`"સંધિ"` — first appearance in the whole ladder** |
| **એકમ 3** (after ch 17) | વિશેષણ, ક્રિયાવિશેષણ, સંયોજક, વિરામચિહ્નો | `vyakaran` |
| **એકમ 4** (after ch 23) | **સમાસ**, શબ્દસમૂહ માટે એક શબ્દ, રૂઢિપ્રયોગ, કહેવત | **`"સમાસ"` — first appearance**; સમાસ entries must show the વિગ્રહ |

`PEDAGOGY.md` adds, for the 9–10 વ્યાકરણ track: **કૃદંત** (6 suffix signatures) and **નિપાત**
(4 types) — the last two members of the canonical `bindu` list to unlock — and states the std-9
**અલંકાર canon as seven**: વર્ણાનુપ્રાસ, પ્રાસસાંકળી, ઉપમા, રૂપક, ઉત્પ્રેક્ષા, વ્યતિરેક, અતિશયોક્તિ.

**Std 9 is where `figures_of_speech` stops being `[]` by default.** Two hard limits carry over from
`reference/alankar_chhand.md` unchanged: name a device only where it is actually present, and quote
the exact words from that topic's `original_chunk` in `lines`. **Out of range at std 9**: **છંદ**,
બહુવ્રીહિ and દ્વિગુ સમાસ, and voice transformation — those are std 10. A std-9 plan that names a
છંદ has exceeded the syllabus.

Also new at std 9 and worth an entry where the chapter's own front apparatus supplies it: the
chapter-front **તળપદા શબ્દો** glossary, taught as study equipment rather than decoration.

## Std 10 — full canon, board-mirrored · **now measured across all 18 chapters**

> The std-10 inventory is complete (`reference/corpus/std-10_inventory.md`, 29 of 29 units, every
> chapter's apparatus read). The banner run below held in all 18 chapters; the per-chapter mix is
> measured — તળપદા શબ્દો 14/18, વિરુદ્ધાર્થી 16/18, રૂઢિપ્રયોગો 14/18, કહેવત 2/18, શબ્દસમૂહ માટે
> એક શબ્દ 14/18 — and remains chapter-dependent: read THIS chapter's blocks off the render.

The measured fixed run per chapter: **શબ્દ-સમજૂતી · સમાનાર્થી શબ્દો/શબ્દાર્થ · [તળપદા શબ્દો |
વિરુદ્ધાર્થી શબ્દો | રૂઢિપ્રયોગો | કહેવત | શબ્દસમૂહ માટે એક શબ્દ] · સ્વાધ્યાય · વિદ્યાર્થી-પ્રવૃત્તિ ·
ભાષા-અભિવ્યક્તિ · શિક્ષકની ભૂમિકા.** Four of the five fields are printed for you; the fifth
(`vyakaran`) is usually named for you in ભાષા-અભિવ્યક્તિ.

The reader also carries **six standalone વ્યાકરણ એકમો** — એકમ 1 સમાનાર્થી/વિરુદ્ધાર્થી/જોડણી ·
એકમ 2 **સંધિ, સમાસ** · એકમ 3 **રૂઢિપ્રયોગ, કહેવત** · એકમ 4 વાક્યપ્રકાર, વિશેષણ · એકમ 5 વિરામચિહ્નો,
વાર્તાલેખન · એકમ 6 અહેવાલલેખન, સંક્ષેપીકરણ, અર્થવિસ્તાર, નિબંધલેખન. Same rule: Agent 10's, never
topics. Note that એકમ 2 and એકમ 5 **recycle sentences from the literature chapters** as grammar
examples (જેઠીબાઈ, શરણાઈના સૂર) — cross-references, not new reading matter.

Per `PEDAGOGY.md` §1 Std 10, three things open at this standard and nowhere earlier:
- **છંદ** — 7 અક્ષરમેળ (અનુષ્ટુપ, ઇન્દ્રવજ્રા, ઉપજાતિ, વંશસ્થ, મંદાક્રાન્તા, શિખરિણી, હરિણી) + 3
  માત્રામેળ (દોહરો, સોરઠો, ચોપાઈ). This belongs to `alankar_chhand.md` and the module's
  `overall_rhyme_scheme`, not to `vyakaran`. **Never trust a recalled છંદ label or syllable count** —
  the report already logs two source discrepancies (મંદાક્રાન્તા, હરિણી). Count on the quoted line
  or say nothing.
- **અલંકાર expands** to 4 શબ્દાલંકાર + 8 અર્થાલંકાર, adding અનન્વય, શ્લેષ, વ્યાજસ્તુતિ, સજીવારોપણ,
  યમક to the std-9 seven.
- **પ્રયોગ / voice transformation** (કર્તરિ → કર્મણિ → ભાવે → પ્રેરક) — std 10's signature grammar
  skill, and a legitimate `bindu` when the chunk shows the form.

**Sourcing discipline at std 10, from the board's own convention:** idiom, proverb and MCQ items are
drawn "from the textbook". Never source રૂઢિપ્રયોગ or કહેવત entries from a general list — the ones
that count are the ones printed in this chapter's apparatus.

---

# Medieval Gujarati — where this file stops being an extra and becomes the reading aid

For chapters in or quoting **જૂની ગુજરાતી** — નરસિંહ મહેતા (15th c.), મીરાંબાઈ (16th c.), અખો
(17th c.), પ્રેમાનંદ (17th c.) — `shabdarth` is not vocabulary enrichment. It *is* how the child gets
into the line at all, and an L2 child gets nothing without it.

**What the corpus actually contains** (measured, and the honest limits):

| poet | measured presence | evidence level |
|---|---|---|
| **નરસિંહ મહેતા** | std 8 ch 6 (ચરિત્રલેખ *about* him, quoting five પદ lines with છાપ inside modern prose); std 8 ch 3 quotes "હું કરું, હું કરું એ જ અજ્ઞાનતા, શકટનો ભાર જયમ શ્વાન તાણે." inside an essay | **page-verified** |
| **મીરાંબાઈ** | std 10 ch 1 **મોરલી** — a whole પદ, the book's opening chapter, source line "('મીરાંનાં શ્રેષ્ઠ પદ'માંથી)", છાપ "બાઈ મીરાં કે પ્રભુ ગિરિધરના ગુણ, દર્શન થકી દુઃખ ભાંગે છે." | **page-verified** |
| **અખો** | std 9 ch 1 **છપ્પા** | **manifest title only — unverified.** The std-9 inventory does not exist |
| **પ્રેમાનંદ** | none confirmed in the measured stds 6, 7, 8, 10 inventories | **not measured.** `PEDAGOGY.md` mentions bhakti verse at std 8 ("સુદામો દીઠા શ્રીકૃષ્ણદેવ રે"), which the std-8 inventory does not corroborate. **Do not assume a પ્રેમાનંદ chapter exists; if one is found, inventory it first** |

## The pattern rule

**Name the pattern, not only the word.** One `shabdarth` per archaic word gets the child through
*this* line. One `vyakaran` entry naming the pattern gets them through the *next* પદ unaided — and
that is the whole return on this section.

Three patterns are attested on rendered pages and may be stated as taught facts:

| pattern | attested line | the `vyakaran` entry |
|---|---|---|
| **ભણે = કહે** in the છાપ line | "ભણે નરસૈયો એનું દર્શન કરતાં કુળ એકોતેર તાર્યાં રે!" (std 8 ch 6) | `bindu: "ક્રિયાપદ"` — જૂની ગુજરાતીમાં 'ભણવું' એટલે 'કહેવું'. પદને અંતે કવિ પોતાનું નામ મૂકે તેને છાપ કહે છે. |
| **જયમ = જેમ** | "શકટનો ભાર જયમ શ્વાન તાણે." (std 8 ch 3) | `bindu: "નિપાત"` or a plain `shabdarth` with `prakar: "કાવ્ય-રૂપ"` — the comparison word keeps its old form for the લય |
| **થકી = થી** | "દર્શન થકી દુઃખ ભાંગે છે." (std 10 ch 1) | `bindu: "નામયોગી"`-family point at std 9+; a `shabdarth` entry at lower standards |

**Every other archaic gloss must be read off the page before it is written.** There is no medieval
Gujarati wordlist in this pack and none is to be reconstructed from memory: an invented gloss on a
600-year-old line is exactly the failure `reference/no_hallucination_policy.md` exists to stop, and
it is unfalsifiable to a reader who does not already know the poet. If the render does not settle a
word, gloss the words it does settle and leave the rest — `[]` and a short list both beat a guess.

## Rules for a medieval chapter

1. **`prakar` for archaic forms is `"કાવ્ય-રૂપ"`**, not `"દેશ્ય"` and not `"તદ્ભવ"`. `"દેશ્ય"` is for
   તળપદા/dialect forms the book itself flags (std 10 ch 1's own in-text glosses "થૈ થઈ, મારગ માર્ગ"
   are exactly this — the book gives you the pair; use it).
2. **Never modernise.** `reference/gujarati_verbatim.md` rule 2 is absolute: the archaic form stays in
   `original_chunk` and gets **explained** in `shabdarth`, never corrected there or anywhere else.
   The છાપ line — "ભણે નરસૈંયો", "બાઈ મીરાં કે" — is verse, not a byline; it is never trimmed and never
   moved into a metadata field.
3. **Keep `samanarthi` and `vilom` in માનક ગુજરાતી even when `shabdarth` is medieval.** The child
   needs to hold both forms side by side, and that contrast is the lesson.
4. **The corruption tell still applies.** A moved or detached માત્રા is an extraction bug, not the
   poet (`reference/gujarati_verbatim.md`). Do not gloss a bug as an archaism — that teaches a child
   the poet wrote something the poet did not write.
5. **Do not turn the પદ into theology.** `profiles/genres/pad_bhajan.md` owns that gate; this file
   only notes that a `note` field explaining ગિરિધર or વૃંદાવન stays at the level of "who the poet is
   singing to", one line, no comparative religion.
6. **A છપ્પો is six lines and one argument.** If std 9 ch 1 (અખો) turns out to be what the title says,
   each છપ્પો is its own topic and is never merged with the next — `profiles/genres/duha_chhappa.md`
   enforces that at Agent 4, and this file simply expects the archaic load per topic to be high:
   `shabdarth` at the top of its band, one pattern-level `vyakaran` entry, `samanarthi`/`vilom`
   thin or empty.
