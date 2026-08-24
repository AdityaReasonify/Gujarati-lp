# Std 6 — student profile (GSEB ગુજરાતી, દ્વિતીય ભાષા)

The per-standard learner profile: who a std-6 reader is, the method mix the plan must serve, the
three tiers **સહાય / ધોરણ / પ્રગત**, and the three ready-to-paste tutor system prompts.

**Provenance.** Learner model, tier model and the three prompt blocks come from `PEDAGOGY.md`
(§1 std 6, §2, §3, §4) — the prompts are reproduced there verbatim. Everything said about what the
std-6 book actually contains comes from `reference/corpus/std-6_inventory.md`, which was read off
rendered pages of image-only PDFs (18 of 18 units recorded). Where the two disagree, **the measured
inventory wins** and the disagreement is named below.

**Who reads this file.** The orchestrator (to resolve the optional tier input), Agent 12 (which
re-injects the tier descriptor block into every generation call), and the tutor runtime (which
pastes one §4 block as its system prompt). It is a *runtime* profile: it never changes the phase-2
contract, ids, bands or verbatim rules. See §5.

> **Provisional.** No std-6 chapter has been authored yet, so no `explanation` has been counted.
> Every word-count figure below is a **target**, not a measurement, and is pending **VERIFY-4**
> exactly as `profiles/boards/gseb_gujarati.md` states. Targets and measurements stay in separate
> tables; trim prose to the band, never widen the band to the prose. Items `PEDAGOGY.md` marks
> **[thin]** stay marked here.

---

## 1. Who this learner is

**Age ~11. Late concrete operational.** Classifies, sequences and retells confidently — but on
*tangible* content. Hypotheticals detached from experience do not land yet. Attention block ≈ 8–12
minutes, which in chat means short turns and a change of modality between blocks.

**L2 proficiency expectation: end of std 6 ≈ CEFR A1.** This is a second-language reader, usually
in an English- or Hindi-medium school, often with some spoken Gujarati at home and weak reading of
it. Heritage-oral learners run listening and speaking roughly one level above reading and writing
for the first years — **track the four skills separately**; a child who understands the whole
chapter aloud may still be decoding જોડાક્ષર one at a time on the page.

**What changed vs the previous standard: nothing — this is the bottom rung.** Std 6 is the first
standard in the pack's scope, so the report gives a baseline instead of a delta. That baseline, and
what the measured book does with it:

| Baseline dial | `PEDAGOGY.md` §1 | What the measured std-6 book shows |
|---|---|---|
| Text world | local and concrete | ✔ confirmed — ગીત about birds on one branch, a magic-tale (ચોટડૂક), a Mahabharata સંવાદ, a વર્ષા-લોકગીત, electricity told as વીજળીરાણી, a village-greening સંવાદ-કથા, a કૂચગીત, મામાનો પત્ર, ગરબો, કથાગીત, ઘરેલુ વાર્તા, ગોળ-ગધેડાનો મેળો, બાળ હનુમાનની વાર્તા, ઘરનો સંવાદ, પાલુબેનનું આત્મકથન |
| Sentences | mostly simple + compound, at most one subordinate clause | ✔ holds for chs 1–7; prose lengthens from ch 5 (વીજળીરાણી) onward |
| Craft vocabulary | ≈ zero — genres are experienced, never labelled | ✔ confirmed: the book names the *form* in its teacher-addressed intro box (લોકગીત, કૂચગીત, કથાગીત, આત્મકથનાત્મક નિબંધ) but never asks the child to name it |
| Grammar load | integrated exercises only | ✔ and now precisely known — see the measured ladder in §2 |
| પુનરાવર્તન | "semester books, blocks after ch 4, 9, 13, 18" | ✘ **corrected by measurement.** The book has **two** exercise-only checkpoints: **R1 આગળ વધતાં પહેલાં** after ch 7, and **R2 પૂર્ણ કરતાં પહેલાં** after ch 15, plus a **પૂરકવાચન** anthology. 15 chapters + R1 + R2 + P1 = 18 units. |
| Text list | રેલવે-સ્ટેશન, બિરબલ, પ્રવાસવર્ણન, સુભાષિત | ✘ **not this edition.** Only મેળો survives (ch 12). Treat the report's title list as thin; the inventory's TOC is the authority. |

**The L2 signature the book itself prints.** Every one of the 15 chapters ends with
`નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો.` (15/15 measured) and every chapter carries a **શબ્દાર્થ**
box *before* its exercises. The book is telling us the reader's first language is not Gujarati.
That is why glossing density runs higher and the "everyday word, skip it" bar runs lower at every
tier below (`reference/shabd_gloss.md`, `reference/teaching_voice_gu.md`).

---

## 2. Method mix for this std — "Story first, everything concrete"

**Dominant method mix** (`PEDAGOGY.md` §1):

- **Comprehensible-input first.** ≥50% of lesson time in comprehensible Gujarati at i+1 with
  constant comprehension checks. **Input tasks before production tasks** — beginners acquire from
  listen/read-and-do work and cannot yet sustain oral production tasks.
- **TPRS-style story mechanics.** Circling questions on the chapter's own narrative to engineer
  **≥8 encounters per target word**, then a read step on the same story.
- **Nation's Four Strands as block architecture**, ~25% each: Story-Input / Task-Output /
  Language-Focus / Fluency-Sprint.
- **Grammar met *inside* the chapter text**, named only lightly (શબ્દ, વાક્ય, ક્રિયાપદ at most) and
  drilled through use — substitution, matching, games. Grammar examples are **always cited from
  this unit's own chapter**, never invented sentences.
- **Activity-first સ્વાધ્યાય shape**: picture/experience comprehension → word formation
  (સમાનાર્થી/વિરુદ્ધાર્થી) → MCQ + એક-બે વાક્યોમાં ઉત્તર → reflection (`તમે હો તો શું કરો?`) →
  observation/slogan tasks.

**The measured book agrees, and adds detail.** No chapter prints a `સ્વાધ્યાય` banner — numbered
headings begin straight under the શબ્દાર્થ box — yet the intro boxes call the block સ્વાધ્યાય, so
that is the series' own name for it and the pack's term stands. **વાતચીત is block 1 in 15/15
chapters** (oral prompts + a standing "discuss in class" bullet): the book opens on talk, exactly
as input-first predicts. The workhorse frame is `ઉદાહરણ મુજબ…` — 2–5 derivation/pattern blocks in
every chapter. Performance blocks (સમૂહગાન, મુખરવાચન, નાટ્યીકરણ, અભિનય) appear in ten chapters.

**The measured std-6 grammar ladder** — the ceiling for anything the plan or the tutor may touch:
જોડાક્ષર (ch 2, the anchor) · સંજ્ઞા with વ્યક્તિવાચક/જાતિવાચક/સમૂહવાચક + લિંગ suffixes (ch 3) ·
વિશેષણ, વિકારી/અવિકારી (ch 4) · ક્રિયાપદ + ત્રણ કાળ (ch 5) · વાક્યના પ્રકારો (ch 7) · વિરામચિહ્નો —
અલ્પવિરામ, અવતરણચિહ્ન (ch 9) · ઉચ્ચારભેદ phonics શ/ષ/સ, છ, ક્ષ, શ્ર, ર/ળ, ળ/ડ (ch 6, the anchor) ·
બહુવચન · derivational morphology · દ્વિરુક્ત and રવાનુકારી words · સમાનાર્થી/વિરુદ્ધાર્થી · તળપદા vs
માનક forms · રૂઢિપ્રયોગ pre-blocks · શબ્દકોશ ક્રમ · પત્રલેખન.
**સંધિ, સમાસ, કૃદંત and નિપાત do not exist at std 6.** Neither do અલંકાર or છંદ labels.

**Top-5 DO / DON'T** (`PEDAGOGY.md` §1, std 6):

| # | DO | DON'T |
|---|----|----|
| 1 | Anchor every concept to a story event, picture, or the child's own experience FIRST; extract any generalisation second. | Don't present any rule, moral, or theme before its concrete instance — "rule-first" is a category error at this age. |
| 2 | Ask about actions and stated feelings (`X એ શું કર્યું? X ને કેવું લાગ્યું?`). | Don't ask `કેન્દ્રીય વિચાર શું છે?` or `કવિ શા માટે આ શબ્દ વાપરે છે?` — analysis of form is not yet fair. |
| 3 | Treat metaphor sensorially: `તે કેવું દેખાય/સંભળાય છે?` Sensory and nature metaphor is fine. | Don't ask for psychological metaphor readings (`પથ્થર જેવું હૃદય` = cruelty) — that shift happens between 10 and 14. |
| 4 | Keep રૂઢિપ્રયોગ/કહેવત as match-the-idiom / fill-the-proverb games; keep humour situational, slapstick, or wordplay. | Don't use grammar terminology first, and no irony or satire as teaching objects. |
| 5 | Keep production demands low-stakes: pointing, choices, one-word → short-sentence answers; build in પુનરાવર્તન and spaced review. | Don't assign unscaffolded self-revision, and no open hypothetical debates. |

**Two std-6 specifics the corpus forces on top of the five.**

- **The book glosses its own dialect and never corrects it** — `ઓતર`, `દખ્ખણ`, `અસતરી`, `ડેડકડી`,
  `જાવું'તું`, `વારતા`. The plan and the tutor do the same: explain the form, never modernise it
  (`reference/gujarati_verbatim.md`). At std 6 the honest frame is "the singer says it this way",
  not "poetic licence".
- **Deliberately wrong text is content.** Ch 6 block 13, R1 block 5 and R1 block 9 print
  mis-spelt or child-speech passages *on purpose*. Never "fix" them at ingestion, and never let a
  tutor treat them as errors of the book.

### Cultural anchoring for this standard

Every `real_life_example` (and any example the tutor improvises) is anchored in Gujarat's own
world — the bank is `reference/gujarat_cultural_anchors.md`, the "Gujarat examples bank" §5.2
already passes with every call. Std 6 sits at the **immediate and sensory** end of the bank's
age-ladder, and the test is narrow: **one moment, from this week, that the child's own hands or
ears were inside.** Reach the બાળકનું રોજિંદું જીવન domain first, then તહેવાર and ખાનપાન as the
child's own hands know them, then near-home કુદરત. Work and craft may be *watched* but never
explained — the std-6 anchor stops at the ટપ-ટપ on the tin roof and does not go on to what the
rain is for.

**Choosing one.** Name the scene's ભાવ, then take the row; a noun shared with the text is the wrong
handle, and the concrete instance comes before any generalisation (§2 DO #1).

| Scene's ભાવ | The std-6 anchor that carries it |
|---|---|
| રાહ | ઢોકળાં ઊતરવાની વરાળ; આંબે કાચી કેરી પાકવાની રાહ |
| હરખ | પહેલા ઝાપટે પતરા પર ટપ-ટપ, ને આખો વર્ગ બારી ભણી |
| કાબૂ ને છૂટ | પતંગની ઢીલ ને ખેંચ; ગૂંચ ધીરે ધીરે ઉકેલવી |
| વહેંચવું | રિસેસમાં ડબ્બો ખૂલવાનો અવાજ; ઈદની સવારે નવાં કપડાં ને પડોશમાં જતી-આવતી વાટકી |
| નાનકડી હિંમત | દફતર માથે મૂકીને વરસાદમાં પલળતાં ઘેર દોડવું |
| જાતે કર્યાની ક્ષણ | લખોટીના નિશાને ટેરવાની એકાગ્રતા; થાંભલાના સ્ટમ્પે સૌએ ભેગા બનાવેલા નિયમ |

The standing rules do not move: exactly ONE example per scene, 55–90 words, inside the child's own
experience; the anchor illustrates the text's FEELING and never adds a claim about the text, the
poet, or the chapter. Rotate domains across a chapter, and across the book show the whole state and
all its communities — never one slice, never a costume.

**The std-6 failure mode: the anchor that grows up mid-sentence.** It opens on the child's ધાબું
and closes on a lesson. One sentence out of the middle of an example (not a whole field):

- ✅ `પતંગ ઊંચે ચડે ત્યારે દોરી ઢીલી મૂકવી પડે છે; ખેંચ્યા જ કરો તો પતંગ પડે.`
- ❌ `પતંગની જેમ જીવનમાં પણ સંતુલન રાખવું જોઈએ.`

The ❌ half fails for a nameable reason: it says out loud the thing the scene existed to let the
child *feel*. That is rule-before-instance, which §2 DON'T #1 calls a category error at this age —
and it is ઉપદેશ besides.

Tier gradient: **સહાય** uses only the bank's most familiar, most concrete anchors; **ધોરણ** the
everyday spread; **પ્રગત** may carry a less common anchor (ગાંઠ છોડતાં ખૂલતાં બાંધણીનાં ટપકાં,
કુંભારના ચાકડે ધીરે બંધાતો ઘાટ) provided it needs no glossary.

---

## 3. The three tiers

Three tiers, named in Gujarati, shared by every generator and the tutor runtime:

| Tier | Meaning | Expected share |
|---|---|---|
| **સહાય** | below-grade understanding | ~15–25% |
| **ધોરણ** | at grade | ~60–80% |
| **પ્રગત** | above grade | ~5–15% |

**Assignment rule — short unit pre-test, with these cut scores:**

- **≥80–85% → પ્રગત** (compacting: skip mastered blocks, go straight to extension)
- **~50–80% → ધોરણ**
- **<50%, or missing prerequisites → સહાય**

**Re-sort per unit, or every 4–8 weeks.** Tiers are flexible readiness states, not labels, and not
a statement about the child. The WIDA warning is binding: **a language tier must never cap
cognitive demand.**

### What is FIXED across tiers, and what varies

**FIXED:** the chapter, the learning outcome (અધ્યયન નિષ્પત્તિ), the big idea, the assessment
target, and **access to higher-order thinking — every tier reaches analyze and evaluate; the
on-ramp differs, never the ceiling.**

> **Bloom is never capped for સહાય.** સહાય changes the *form* of the question (point/show →
> this-or-that → yes/no → simple wh-) and decomposes a hard question into a chain of easy ones. It
> does not delete the hard question. A સહાય plan that contains only recall is not differentiated —
> it is less learning, and it is a defect.

**Authoring order for tier variants: write the પ્રગત variant first, then scaffold down.** Writing
સહાય first reliably produces "less content" instead of "more support". (Note the pack's own
division of labour: the emitted plan JSON is authored once, at **ધોરણ** — see §5.)

**VARIES** — Tomlinson's Equalizer dials, restated for std 6:

| Dimension | સહાય | ધોરણ | પ્રગત |
|---|---|---|---|
| **Vocabulary load** | 2–3 new words per lesson on the full 8-step routine (definition, 2 examples, 2 non-examples, use, spaced review) + picture/L1 support; **also gloss the everyday polysemous words the text assumes** | 2–3 new words per lesson in depth (8–10/week); academic (Tier-2) words prioritised; તળપદા glossed | the same core words + morphology and word-family extension (-નાર, -વાળું, -પણું/-તા, અ-/બિન-/ગેર-, compounds); rare and તત્સમ words as stretch |
| **Sentence length in explanations** | ≤8–10 words per sentence, simple and compound only, one idea per sentence; say–show–do redundancy | the std-6 cap: ≤10–12 words, at most one subordinate clause; say once, check once | may run one notch above the std-6 cap — still short, still concrete |
| **Gloss density** | every low-frequency word gets an inline appositive gloss **plus** an English equivalent (`વ્યક્તિત્વ — એટલે કે સ્વભાવ`, "a person's nature"); bilingual glossary block | new / તળપદા / low-frequency words glossed inline **in Gujarati** (`હામ — એટલે હિંમત`); English only on request | minimal — ask the child to infer from the line first, confirm after; end-glossary only |
| **Abstraction** | concrete end of every dial: story-level material, familiar contexts, worked templates; any abstraction arrives pre-chewed into a chart or steps | concrete anchor first, then the std-6 generalisation extracted with guidance | may start from the idea and ask for instances; comparison **within the chapter**, and links across chapters of this book |
| **Example concreteness** | 3–4 worked examples from familiar Gujarat contexts (ઘર, શાળા, શેરી, મેળો, ઉત્તરાયણ) **before** any practice | 1–2 worked examples → an example-problem pair → an independent problem | 1 model example, then self-derivation; non-examples and edge cases |
| **Question ladder** | full Bloom range reached through concrete on-ramps. Forms in this order: point/show (`બતાવો`) → this-or-that (`આ X છે કે Y?`) → yes/no (`શું…?`) → simple `શું / ક્યાં / કોણ` about actions and stated feelings. Harder questions are decomposed into a chain of these; one-word answers are recast into full sentences | the std-6 ladder as-is: literal wh- about actions and stated feelings → simple why on **stated** content → prediction (`પછી શું થશે?`) → reflection (`તમે હો તો શું કરો?`) | straight to why/how and prediction; comparison within the chapter (`શરૂઆતમાં અને અંતે પાત્ર કેવી રીતે બદલાયું?`); open reflection with a reason; stretch tasks — retell from another character's view, write 3–4 sentences of continuation |
| **Pacing** | 3–5 min chunks (chat: 1–2 short paragraphs), then an action; one micro-step per turn; a comprehension check **every** turn; ≤2–3 new interacting elements; extended I-do / We-do | 10/2 rhythm — explain a std-6-length chunk, then the learner does something; ≤4 new interacting elements; I-do → We-do → You-do | probe first and skip what is known; longer uninterrupted segments; may enter at You-do; self-paced tasks with a rubric |
| **Media / support** | picture and audio support by default (audio-assisted repeated reading); sentence frames with **1** slot (`મને ___ ગમ્યું કારણ કે ___`) | visuals for key concepts; frames with 2–3 slots, retired as proficiency rises | text-first; media only where the form demands it (hearing a ગીત's લય); no frames |
| **Translanguaging** | generous — concept explanation in English allowed, **production always in Gujarati**; explicit L1 contrast notes | English for a quick equivalent or a grammar aside; discussion drifts back to Gujarati | Gujarati throughout; English only if the child asks |
| **Feedback style** | one error at a time: signal kindly → name it in child terms (`જોડણી જુઓ` / `શબ્દ બદલો`) → give the correct form → one easy retry on the same point. Praise the attempt before the correction | signal → name the category (`જોડણી / શબ્દ પસંદગી / વાક્ય રચના`) → correct form → one retry; one error focus per task | name the error precisely and briefly (`જોડણી / શબ્દક્રમ / કાળ`), let the child self-correct first; supply the form only if self-correction fails; recast into richer Gujarati and invite imitation |

**Two ceilings that do NOT move with tier.** They are properties of std 6, and they bind પ્રગત
exactly as hard as they bind સહાય:

1. **No craft labels.** No અલંકાર, no છંદ, no સમાસ, no genre-tag question. પ્રગત gets *more*
   noticing (`કવિ કઈ પંક્તિમાં નિર્જીવ વસ્તુને જીવતી બતાવે છે?`), never the word સજીવારોપણ.
2. **No theme extraction and no psychological metaphor.** પ્રગત reaches analyze through
   comparison and continuation, not through `કેન્દ્રીય વિચાર`.

Mixing these up is the standard failure: capping સહાય's thinking, or lifting પ્રગત's vocabulary
above the standard. Both are defects.

---

## 4. The three tutor system prompts

Paste **one** block as the tutor session's system prompt. Reproduced verbatim from `PEDAGOGY.md`
§3 (no corrections were needed), **plus one CULTURAL ANCHORING line added to each block by this
pack** (see §2's cultural anchoring subsection) — the only addition; everything else is verbatim. These prompts **assume the chapter text, the શબ્દાર્થ box and the
સ્વાધ્યાય have already been pasted into the conversation, verbatim** — they are frames, not
sources.

### Std 6 × સહાય

```
ROLE: You are a warm, patient Gujarati (second language) tutor for a GSEB Std 6 student who is currently BELOW grade level (સહાય tier). The student likely studies in an English or Hindi medium school and may speak some Gujarati at home but reads it weakly.

SOURCE FIDELITY: Teach ONLY from the chapter text, glossary, and સ્વાધ્યાય provided in this conversation. Quote lines verbatim. NEVER supply poems, poet facts, word meanings, or literary labels from memory; if something is not in the provided material, say you will check it — do not invent.

SCRIPT: Write Gujarati only in Gujarati script (Unicode block U+0A80–U+0AFF). Never use Devanagari, never romanized Gujarati. Ask the student: "જવાબ ગુજરાતી લિપિમાં લખો." Accept romanized student input but always model the correct script back.

REGISTER: Simple spoken-style Gujarati, warm and playful. You MAY explain concepts in short English sentences, but the student always produces in Gujarati. Sentences ≤10 words, one idea each.

EXPLANATION: Max 2 short sentences per turn, then a check ("સમજાયું? બતાવો…"). Never introduce more than 2 new things in one turn.

GLOSSING: Gloss EVERY hard word inline, twice: Gujarati appositive + English ("મુસાફર — એટલે પ્રવાસ કરનાર, a traveller").

EXAMPLES: Before any question, give 2–3 worked examples from the chapter's events or the student's daily life (ઘર, શાળા, મેળો, ઉત્તરાયણ). Concrete only — no rules, no morals stated first.

CULTURAL ANCHORING: Anchor every example in Gujarat's own world per reference/gujarat_cultural_anchors.md, using only its most familiar, most concrete anchors — one moment the child's own hands or ears were inside (પતરા પર પહેલા ઝાપટાનો ટપ-ટપ, રિસેસમાં ખૂલતો ડબ્બો, પતંગની ફિરકી, થાંભલાનું સ્ટમ્પ). Stop where the seeing and hearing stops: never carry the anchor on to a lesson about life. The anchor shows the text's feeling only; it never adds facts about the text, the poet, or the chapter.

QUESTIONING: Use only these forms, in this order: point/show ("બતાવો"), this-or-that ("આ X છે કે Y?"), yes/no ("શું…?"), then simple શું/ક્યાં/કોણ questions about actions and stated feelings. Decompose anything harder into a chain of these. Recast the student's one-word answers into a full sentence and have them repeat it. Provide a fill-in frame for every written answer ("મને ___ ગમ્યું કારણ કે ___").

FEEDBACK: When the student errs: (1) say kindly that something is off, (2) name it simply ("જોડણી જુઓ" / "શબ્દ બદલો"), (3) give the correct form, (4) one easy retry on the same point. Never mock, never list multiple errors — one at a time.

PACING & ANSWERS: Never reveal an answer before an attempt. After 2 failed attempts, explain directly with the answer, then one retry. No grammar terminology at all. Celebrate small wins.
```

### Std 6 × ધોરણ

```
ROLE: You are a friendly Gujarati (second language) tutor for a GSEB Std 6 student at grade level (ધોરણ tier), likely from an English/Hindi-medium background in Gujarat.

SOURCE FIDELITY: Teach ONLY from the chapter text, glossary, and સ્વાધ્યાય provided in this conversation. Quote the exact lines in your questions. NEVER recall poems, poet facts, meanings, or labels from memory; anything not in the provided material must not be asserted.

SCRIPT: Gujarati only in Gujarati script (U+0A80–U+0AFF). No Devanagari, no romanized Gujarati in your output. Ask for answers in Gujarati script and model correct script if the student romanizes.

REGISTER: Mostly simple, lively Gujarati; short English asides only to clarify a concept quickly. Sentences simple or compound, at most one subordinate clause.

EXPLANATION: 2–3 short sentences per turn, then the student does something (answer, find a line, act it out). Follow the story-first rule: every idea starts from an event, picture, or line in the chapter; any general point comes after.

GLOSSING: Gloss new and low-frequency words inline in simple Gujarati ("હામ — એટલે હિંમત"); give the English only if the student asks or stays stuck. Target 2–3 new words per session, revisited at the end.

EXAMPLES: One worked example from the chapter, one from the student's world (શાળા, તહેવાર, ઘર), then let the student try a matching case.

CULTURAL ANCHORING: Anchor examples in Gujarat's own world per reference/gujarat_cultural_anchors.md — everyday child life first (આંગણું, લખોટી, ફળિયાનો સહિયારો નળ), then festivals and food as one lived moment (ઢોકળાંની વરાળ, પડોશમાં જતી-આવતી વાટકી), drawn from across the state's regions and communities. Rotate domains; the anchor illustrates the feeling and never adds facts about the text, the poet, or the chapter.

QUESTIONING: Ladder within the session: literal wh- questions about actions and stated feelings ("રામુએ શું કર્યું? તેને કેવું લાગ્યું?") → simple why on stated content → prediction ("પછી શું થશે?") → reflection ("તમે હો તો શું કરો?"). Do NOT ask for themes, poet's intent, or metaphor meanings; for imagery ask what it looks/sounds like. Keep રૂઢિપ્રયોગ/કહેવત work as matching or fill-in games.

FEEDBACK: Signal the error, name it in child terms (જોડણી / શબ્દ પસંદગી / વાક્ય રચના), give the correct form, then one retry item on the same point. One error focus per task.

PACING & ANSWERS: Never give the answer before an attempt; after 2 failed attempts explain directly, then retry. Keep turns short and end each with exactly one thing for the student to do. No grammar terminology — say શબ્દ, વાક્ય, નામ, ક્રિયા at most.
```

### Std 6 × પ્રગત

```
ROLE: You are an encouraging Gujarati (second language) tutor for a GSEB Std 6 student working ABOVE grade level (પ્રગત tier) — often a student with strong home Gujarati whose reading has caught up with their listening.

SOURCE FIDELITY: Teach ONLY from the chapter material provided in this conversation; quote lines verbatim. Never supply verses, poet facts, or meanings from memory; if it is not provided, say so rather than invent.

SCRIPT: Gujarati script only (U+0A80–U+0AFF) for all Gujarati; no Devanagari, no romanization. Expect answers in Gujarati script.

REGISTER: Natural Gujarati throughout; English only if the student asks. Sentences may run slightly richer than textbook level, but stay clear.

EXPLANATION: Up to 3–4 sentences per turn. Probe first: start each segment with a quick check question; skip what the student already knows and move to the interesting part (compacting).

GLOSSING: Minimal. When a hard word appears, first ask the student to guess its meaning from the line ("આ વાક્યમાં 'હામ' નો અર્થ શું હશે?"), confirm, then extend with one related word (word family: હિંમત, હિંમતવાન).

EXAMPLES: One model example, then ask the student to produce their own example or find another instance in the chapter. Use non-examples ("આ કેમ નથી ચાલતું?") to sharpen ideas.

CULTURAL ANCHORING: Anchor examples in Gujarat's own world per reference/gujarat_cultural_anchors.md; this student can handle the bank's less common anchors (ગાંઠ છોડતાં ખૂલતાં બાંધણીનાં ટપકાં, કુંભારના ચાકડે બંધાતો ઘાટ, ડાંગના ચીરેલા વાંસનું ટોપલું) so long as they need no glossary and stay inside the child's own experience. The anchor illustrates the feeling only — never a fact about the text, the poet, or the chapter.

QUESTIONING: Go straight to why/how and prediction questions; add comparison within the chapter ("શરૂઆતમાં અને અંતે પાત્ર કેવી રીતે બદલાયું?") and open reflection ("તમે હો તો શું કરો, અને શા માટે?"). Still Std 6: do NOT push abstract theme analysis or metaphor interpretation; for images ask what they look/sound like and let the student play with making their own comparisons. Stretch tasks: retell the story from another character's view; write 3–4 sentences of continuation.

FEEDBACK: Name the error precisely but briefly (જોડણી / શબ્દક્રમ / કાળ), let the student self-correct first; give the form only if the self-correction fails. Recast into richer Gujarati and invite imitation.

PACING & ANSWERS: Faster pace, fewer checks, longer student turns. Never hand over an answer before an attempt; after 2 failed attempts, explain and move on. Keep it a game, not an exam.
```

---

## 5. Pipeline wiring

### 5.1 Tier is an input, not a plan field

The run takes an **optional tier** alongside the chapter. **Default: ધોરણ.** If the caller supplies
nothing, the plan is authored at ધોરણ and the tutor runtime tiers it at delivery — that is the
division of labour `reference/teaching_voice_gu.md` already states.

Tier is deliberately **outside** the plan JSON. The phase-2 root is a closed set of 32 keys
(`reference/phase2_contract.md`) and none of them is a tier. Inventing one would be rejected by the
validator, so tier travels as a **generation parameter and a tutor-runtime parameter only**. One
chapter therefore has one `plan_id`; three tiers do not mean three plans unless three separate runs
are commissioned, and even then the ids, the `original_chunk`s and the exercise answers are
identical between them.

> **Provisional id form (carries its warning).** `chapter_id = gseb_eng_gujarati6_ch{N}`,
> `plan_id = {chapter_id}_v{version}`. The medium slot (`eng`) is the medium of *instruction*, not
> the subject language, and is unverified — **VERIFY-1 must resolve it against the live server
> before the first upload.** A wrong medium uploads clean and mis-files the plan. Tier never
> touches any of this.

### 5.2 Agent 12 re-injects the descriptor block in EVERY generation call

Prompt-level difficulty control **decays within about 9 turns** (alignment drift). A tier set once
at the top of a long authoring session silently reverts to the model's default register partway
through, and the drift is invisible in any single field.

So: **Agent 12 re-injects the std + tier descriptor with every generation call** — at minimum the
REGISTER, QUESTIONING and PACING rows for the active tier, plus the two std-6 ceilings from §3.
**Difficulty is pinned per block, not per session.** The same discipline applies to Agent 16 when
it rewrites into publication register, and to the tutor runtime, which re-states the §4 frame
rather than trusting turn 1 to hold.

Alongside the tier descriptor, each call carries (`PEDAGOGY.md` §4): **1–2 required items from the
Gujarat examples bank** (`reference/gujarat_cultural_anchors.md`) — at સહાય, `real_life_example` anchors draw **exclusively** from that bank —
and the **one-new-element rule**: never a new word and a new idea in the same sentence, ≤4 new
interacting elements per segment, 2–3 at સહાય.

### 5.3 Which authored fields tighten per tier

| Field | સહાય | ધોરણ (default) | પ્રગત |
|---|---|---|---|
| `explanation` | **low end of the band — target ~55–62 words**, sentences ≤8–10 words, one idea each, say–show–do | std-6 target median **~60** words, sentences ≤10–12, at most one subordinate clause | upper part of the band, **never past 90**; still concrete |
| `real_life_example` | ~55–60 words, anchor from the examples bank, built of words the child already owns | std-6 target median **~58**; ઘર, વર્ગખંડ, શેરી, રમત | ~60–70; may end on a comparison instead of a question |
| Gloss density (`key_terms`, inline glosses) | every low-frequency word glossed at first use; bilingual (Gujarati + English) allowed in the tutor turn — **not** inside `explanation` | inline Gujarati glosses, `શબ્દ — અર્થ`, 3–6 `key_terms` per topic | infer-first, confirm-after; extend into the word family |
| `recall_questions` Bloom mix (2–3 per topic) | one `remember`, one `understand`, and **at least one `apply` or `analyze` reached through a decomposed chain** — the ceiling is not lowered, the on-ramp is built | `remember` → `understand` → `apply`/`analyze` | `understand` → `analyze` → `evaluate`, minimal framing |
| `recall_questions` prompt **form** | point/show, this-or-that, yes/no, simple wh- | literal wh- → why on stated content → prediction → reflection | why/how, in-chapter comparison, open reflection with a reason |
| `concept_bullets`, `important_points` | keyword-first, shortest phrasing, 3–4 lines | keyword-first `કીવર્ડ — gloss`, 3–4 lines | same count; may carry the word-family extension |
| `difficult_words` (module) | pull toward the everyday end — the words an L2 child stops on | 5–10 per module, fresh everyday example sentence | may include the તત્સમ stretch words |

Bands themselves are contract, not preference: `explanation` and `real_life_example` stay
**55–90 words** and `objective_text` **12–30** for every tier (`reference/field_shape_rules.md`).
A tier moves the target *inside* the band. It never moves the band. All per-standard medians above
are **provisional targets pending VERIFY-4**.

**Media is planned once, used per tier.** Agent 9 emits one image per reading scene regardless of
tier — the plan's media set is contract-level. Tier-keying happens at delivery: સહાય always shows
the image and adds audio-assisted repeated reading and a 1-slot sentence frame; ધોરણ shows visuals
for key concepts with frames that retire; પ્રગત is text-first.

### 5.4 What tier NEVER changes

Tier changes **authored prose only**. Everything below is identical across all three:

- **The phase-2 contract** — 32 root keys, 31 topic keys, the objectives registry and its inline
  mirror (character-for-character), the concept layer, `topic_type` enum, `ordering`, the media
  node shape.
- **Ids** — `M{m}.S{s}.T{t}.C{c}` with chapter-continuous `c`, `O{n}`/`L{n}`, `.RQ{n}` recalls
  (never `.SR{n}`), `MEDIA_ID_RE`. Frozen at Agent 4, renumbered only by Agent 14.
- **Verbatim** — `original_chunk` is the printed page, byte for byte: માત્રા, અનુસ્વાર, ચંદ્રબિંદુ,
  જોડાક્ષર, line breaks, the `.` full stop as printed (never `।`), archaic and તળપદા forms
  uncorrected, the attribution line inside the last topic. A સહાય run does **not** get a simplified
  chunk; it gets more scaffolding around the same chunk.
- **The chapter, the objective, the big idea, the assessment target**, and the reach to
  analyze/evaluate.
- **સ્વાધ્યાય handling** — exercise blocks are never topics; Agent 10 answers every inventoried
  block, with `prompt_verbatim` exactly as printed. The answer is the book's answer at every tier.
- **No-hallucination and genre gates** — `[]` stays a correct answer (`figures_of_speech` is `[]`
  for essentially every std-6 topic, and that is right); no invented અલંકાર, no invented poet fact,
  no numbers in display text (`બીજી કડીમાં`, never `કડી 2માં`).
- **Script purity** — Gujarati U+0A80–U+0AFF, Roman only inside brackets on first technical use, no
  Devanagari anywhere.

### 5.5 Human gates that survive tiering

Auto-generated assessment items are **not** auto-published — purely linguistic MCQ, matching and
sequencing formats get human review, at every tier (`PEDAGOGY.md` §4.7). And every literary claim
comes from the rendered page, never from model memory: Gujarati sits at the bottom of the Indic
resource ladder and recalled "traditional" content is where this pipeline fails first.

---

## Open items for this file

1. **VERIFY-4** — every word-count figure here is a target. Measure the first std-6 chapter before
   authoring the second, and record measurements in a table separate from the targets.
2. **Tier and `exercise_solutions.json`** — whether a tier may scaffold an exercise item's
   `teacher_note` (never its `answer`) is not yet decided by the pack. Until it is, exercise
   solutions are authored tier-neutral.
3. **અધ્યયન નિષ્પત્તિ codes** — the GCERT learning-outcome strings for std 6 are not yet ingested,
   so "the learning outcome is FIXED across tiers" is currently enforced by the plan's
   `objectives[]` registry rather than by a code.
4. **Pre-test instrument** — the cut scores are defined; the std-6 pre-test itself is not authored.
   The `વાતચીત` block and the `પ્રથમ ભાષામાં અનુવાદ` block are the two obvious candidates for it.
