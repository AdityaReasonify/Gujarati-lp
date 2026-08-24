# विधा Profiles — master index (diagnosis + routing)

Entry point after Agent 1 reads a chapter. Routes the four diagnosis signals
(`reference/genre_diagnosis.md`) to a profile, which then parametrizes Agents 2/5/7/9/10/12.

> ⚠️ Every named text below is illustrative, not data. Diagnose from YOUR chapter's structure,
> theme, and अभ्यास — never from a sample. (`reference/no_hallucination_policy.md`)

## Decision tree

```
START: read structure (A), theme (B), अभ्यास (C), purpose (D).

Is the text in verse?  ── YES → sub-diagnose by UNIT LENGTH FIRST:
│   ├─ NO metre, NO rhyme, NO repeating unit; line lengths vary freely
│   │      → mukt_chhand_kavita.md          (HARD: cut by भाव-खंड; invent no छंद)
│   ├─ SIX lines, where line 2's last foot repeats as line 3's first, AND the
│   │   last word of line 6 equals the first word of line 1
│   │      → kundaliya.md                  (HARD: all six lines = ONE topic)
│   ├─ two-line self-contained units in a MIXED sant dialect (सधुक्कड़ी / पचमेल खिचड़ी); the
│   │   turn in line 2 goes INWARD; theme = अनुभव-ज्ञान, निर्गुण, गुरु-शिष्य — not conduct
│   │      → sakhi.md                      (HARD: one साखी = one topic; never as usable advice)
│   ├─ the छंद run in SEQUENCE and cannot be reordered; two speakers with no speaker
│   │   tags; a plot with a मोड़; the अभ्यास asks what happened and why
│   │      → bal_katha_kavita.md           (HARD: cut on the turn, never mid-turn)
│   ├─ a टेक that repeats UNCHANGED after every छंद; the छंद can be REORDERED freely;
│   │   and either the poem is performed (a game, a chant, a clap) or its images are
│   │   impossible on purpose (उलटबाँसी / गप्प)
│   │      → bal_khel_geet.md              (HARD: टेक stays with its छंद, never its own topic;
│   │                                       never explain a nonsense image straight-faced)
│   ├─ two-line self-contained units, each its own picture + turn, कवि-छाप in the line,
│   │   theme = नीति/व्यवहार, अभ्यास asks भाव-स्पष्ट करो per couplet
│   │      → niti_doha.md                  (HARD: one दोहा = one topic)
│   ├─ runs of चौपाई each closed by a centred दोहा, named characters speaking
│   │   without speaker tags, a कथावाचक reporting between the speeches
│   │      → chaupai_doha_samvad.md        (HARD: unit = one विनिमय; never cross a दोहा)
│   ├─ a sung पद with a टेक, a भक्त or देवता speaking, ब्रज/अवधी forms
│   │      → bhakti_pad.md                 (HARD: भाव, not a morality lesson)
│   ├─ addressed to God in the second person and ASKING; a returning epithet
│   │   (करुणामय, प्रभु); asks for strength rather than rescue — 'not this, but this'
│   │      → prarthana_kavita.md           (HARD: never cut a petition in half)
│   ├─ equal छंद each closing on the SAME unchanged line; addressed to the READER in the
│   │   imperative (विचार लो, उठो, चलो); named पुराण/इतिहास figures cited one line each as proof
│   │      → niti_upadesh_kavita.md        (HARD: one छंद = one topic; teach the टेक ONCE)
│   ├─ MANY equal small स्तबक (30+), strict rhyme, but the स्तबक RUN ON — a portrait
│   │   or a remembered speech spans three or four of them; speaker separated from
│   │   the people he is remembering; addresses a सावन / हवा / बादल that cannot answer
│   │      → smriti_virah_geet.md            (HARD: cut by भाव-खंड, never per स्तबक)
│   ├─ speed, charge, a horse or warrior, ओज in the rhythm, वीरता theme
│   │      → vir_ras_kavita.md
│   └─ nature, land, season, a call to the country, first-person feeling
│          → prakriti_deshbhakti_kavita.md
│
└─ PROSE → what moves it?
    ├─ a पात्र (± अवधि/समय/स्थान) header; bracketed directions; no narrator
    │      → ekanki.md                     (HARD: रंग-संकेत are text and mark the cut)
    ├─ named speakers in two columns; questions asked and answered
    │      → sakshatkar.md                 (HARD: प्रश्न + उत्तर = ONE topic)
    ├─ one voice to an audience present at an occasion; ends by asking
    │      → bhashan_uddabodhan.md         (HARD: one-sided BY FORM — do not score it as an essay)
    ├─ salutation + sign-off; first person moving through places in order
    │      → yatra_vrittant_patra.md       (HARD: cut by पड़ाव; never reorder)
    ├─ a date as the heading; clock times inside; the writer does not know the ending
    │      → diary.md                      (HARD: cut by the clock, never by theme)
    ├─ plot, characters, a turn                          → kahani.md
    ├─ a real person remembering; a life in sequence     → sansmaran.md
    ├─ facts, a custom, a dance, a place, a practice     → soochnatmak_sanskritik.md
    ├─ one 'मैं' arguing with ITSELF; attempts that fail; self-mocking humour
    │      → lalit_atmaparak_nibandh.md  (HARD: cut by विचार-पड़ाव at the writer's own question)
    ├─ a critic arguing for someone ELSE's work in the third person; anecdotes cited as proof
    │   rather than told; counter-facts admitted; अभ्यास asks 'आप कहाँ तक सहमत हैं'
    │      → samiksha_vyaktichitra.md    (HARD: one-sidedness is the FORM, never a defect)
    └─ two voices arguing; an essay making a case        → samvad_nibandh.md
```

Verse is sub-diagnosed **by unit length before theme**, because getting the unit wrong breaks the
cut and nothing downstream recovers.

**मुक्त छंद is tested before every other verse branch, and the test is a negative one.** Each of
the other verse profiles asks "is the unit six lines / two lines / a पद / a छंद?" — and मुक्त छंद
answers no to all of them, then falls through to whichever thematic profile is nearest, which
proceeds to cut it "छंद-wise" into छंद the page does not contain. Ask *is there a repeating unit
at all?* first, and route on the absence.

**स्मृति-विरह गीत is tested right after मुक्त छंद, and the test is the mirror of it.** मुक्त छंद
asks *is there a repeating unit at all?* This profile asks the next question: *is the unit of sense
the same size as the unit of metre?* A long गीत in strict 16-मात्रा तुकांत स्तबक answers **no** —
one portrait or one remembered speech spans three or four स्तबक — and a छंद-wise profile reaching
it first would emit one topic per स्तबक (fifty of them for कक्षा 9's *घर की याद*) and cut every
portrait in three. Route on the mismatch, not on the theme.

**चौपाई-दोहा संवाद is tested before दोहा and before पद, for the same reason कुंडलिया is.** A
रामचरितमानस excerpt *contains* दोहे, so a दोहा-first test matches one, takes its two lines, and
abandons the चौपाई run it was closing — leaving a couplet that is unreadable on its own. Ask
first whether the दोहा is **self-contained**; if it is closing a run of चौपाइयाँ, this is the
profile. Its unit is neither the दोहा nor the चौपाई but the **विनिमय** they carry.

**साखी is tested before दोहा, and the two are the same shape on purpose.** स्पर्श's own
पाठ-प्रवेश says it outright — *"'साखी' वस्तुत: दोहा छंद ही है"* — so a दोहा-first test matches and
nothing about the unit goes wrong. What goes wrong is the **lens**: `niti_doha` reads for
*अनुभव की सीख*, "the सीख the child can use", and half a साखी set has no usable instruction in it.
`जब मैं था तब हरि नहीं` and `बिरह भुवंगम तन बसै` either collapse under that question or force an
invented answer — and on `हम घर जाल्या आपणाँ, लिया मुराड़ा हाथि` the invented answer is not merely
wrong but unsafe to put in front of a fifteen-year-old. Route on the **direction of the turn**:
outward to conduct is नीति, inward to the reader's own mind is साखी. The dialect is the visible
tell — सधुक्कड़ी mixes Avadhi, Rajasthani, Bhojpuri and Punjabi in one line.

**बाल कथा/संवाद-कविता is tested before दोहा and before the two thematic verse branches.** It is
the third profile caught in the same net as `prarthana_kavita` and `niti_upadesh_kavita`: छंद-based
verse whose engine is not imagery, falling through to `prakriti_deshbhakti_kavita` because that is
where the verse branch bottoms out. The दोहा test is the nearer miss and the more damaging one —
कक्षा 5's *चतुर चित्रकार* is written in couplets with the दोहा's comma caesura and closing rhyme, so
`niti_doha` matches on shape, and its hard gate (one दोहा = one complete unit of advice) would cut a
story into twenty two-line topics with no story in any of them. The couplets here are **incomplete
on purpose**: each hands the plot to the next. Two tests settle it, and both are positive:
**can the छंद be reordered without breaking anything, and is anyone speaking?** A sequence that
cannot be reordered, plus two untagged speakers, is this profile; its unit is one **beat or one
speaker's turn**, which may be one couplet or three.

**बाल खेल-गीत is tested immediately after it, and before `niti_upadesh_kavita` — which is its
nearest miss, not `prakriti_deshbhakti_kavita`.** Both विधा are equal छंद closing on the same
unchanged line, and both address their reader in the imperative, so the टेक test that separates
`niti_upadesh_kavita` from the imagery branch cannot separate these two: कक्षा 3's *रस्साकशी*
(*जोर लगाओ, हेई सा! / हेई सा! भई, हेई सा!*) satisfies every clause of the नीति entry as written.
The separating question is **what the imperative asks for — a change in how you live, or a movement
of your body right now.** *विचार लो कि मर्त्य हो* is the first; *पैर गड़ा कर, पीठ अड़ाओ* is the
second. `niti_upadesh_kavita` also cites named पुराण/इतिहास figures one line each as proof, and a
खेल-गीत cites nothing, because it is not arguing.

Two further tests, either of which is sufficient on its own: **can the छंद be reordered** (in
नीति-उपदेश the argument accumulates and they cannot; in a खेल-गीत they can), and **is any image
impossible on purpose** — कक्षा 3's *सुनो भई गप्प* has a river drowning in a boat and a donkey up a
date palm, and a profile that explains those as pictures produces an explanation that reports them
as facts. That is the failure this profile exists to prevent, and it is why the हार्ड gate names it.

**कुंडलिया is tested before दोहा, and the order is not arbitrary.** A कुंडलिया *opens* with a
दोहा, so a दोहा-first test matches it, takes the first two lines, and abandons the remaining four
— destroying both joins that define the form. Check for the six-line ring first; only if it is
absent is a two-line unit a complete poem.

Likewise **साक्षात्कार is tested before कहानी and संवाद**: an interview has two voices and can
read like dialogue, but its unit is the प्रश्न-उत्तर pair, not a plot beat or an argument strand.

**एकांकी is tested before all three of those, and before कहानी.** A play, an interview and an
essay-dialogue all show named speakers, so a साक्षात्कार-first test matches the play and starts
hunting for questions; and a play has a plot and a turn, so a कहानी-first test matches it and
starts summarising. Both then drop the रंग-संकेत, because neither profile has anywhere to put them
— and the directions are where the play keeps its plot. The tell is unambiguous and comes before
any of this: **a `पात्र` list and bracketed directions.** Nothing else in the pack has either.
Route on the apparatus, not on the presence of dialogue. Its unit is a **stage-beat**: a stretch
held together by one situation, ending on an entrance, an exit, a sound, or a change in what
someone knows or wants.

**प्रार्थना-कविता is tested after `bhakti_pad` and before the two thematic verse branches.** It is
the only विधा in the pack whose addressee is God *and* whose form is not a पद, so `bhakti_pad`
takes it on theme and then looks for a टेक, a छाप and ब्रज forms that are not there. Reaching
`prakriti_deshbhakti_kavita` instead is worse in a quieter way: that profile builds feeling out of
**pictures**, and a prayer poem builds it out of **grammar** — negation, condition, contrast — so
the chapter comes out hunting imagery it does not contain. The positive test is one sentence long:
**does the poem refuse the obvious request and ask for something harder instead?**

**नीति/उपदेश-कविता is tested immediately after it, and it is caught by the same net.** It too is
छंद-based verse with no pictures, so it too falls through to `prakriti_deshbhakti_kavita` — and
there it meets a टेक rule that is the exact inverse of what it needs. That profile says *teach what
the टेक changed*; in this विधा the टेक **never changes** (मनुष्यता closes all eight छंद on the same
line, word for word) and what changes is the argument in front of it. Following the borrowed rule
yields eight topics explaining one sentence. `niti_doha` is the other near miss: same lens, wrong
unit — a दोहा is complete in two lines, while here the claim does not close until the टेक lands on
line six. Two tests settle it: **does every छंद end on the same line, and is the reader being
given instructions?**

**डायरी is tested before संस्मरण**, which is the mirror of the same mistake. Both are first person
and both look back, so संस्मरण matches — and then imports hindsight the diarist did not have,
re-orders the day by theme, and cuts by जीवन-चरण instead of by the clock. Check for **a date as the
heading and clock times inside the text** first; only if the remembering is shaped by knowing how
it turned out is it a संस्मरण.

**भाषण is tested before निबंध** for the mirror-image reason: a speech is one-sided *by form*, and
`samvad_nibandh`'s avoid-list rejects exactly that. Reaching the essay profile first means marking
the form's defining property as a defect.

**ललित/आत्मपरक निबंध is tested before `samvad_nibandh` for that same reason, and after
`sansmaran`.** It is one voice with no opponent, so `samvad_nibandh` scores its defining property
as one-sided preaching; and it thinks about a problem in the present tense rather than remembering
a life, so it is not संस्मरण. The test is a positive one: **does the essay argue with itself?**
A sequence of attempts that fail, marked off by the writer's own rhetorical questions
(`पर लिखूँ कैसे?`, `तब क्या किया जाए?`), with humour at the writer's own expense — that is this
profile, and its unit is the **विचार-पड़ाव**.

## Master table

| Profile | Lens | Explanation unit | Emphasise | Avoid (hard gate) |
|---|---|---|---|---|
| **kundaliya** | चक्र + नीति + दृष्टांत | **one कुंडलिया (6 lines)** | the two joins — दोहा's last foot reopening the रोला, and the poem's first word returning as its last | splitting it; teaching the दोहा alone; reducing the poem to its proverb |
| **sakhi** | साक्षी + अनुभव + अंतर्दृष्टि | **one साखी (2 lines)** | साखी = साक्षी = प्रत्यक्ष ज्ञान, taught before the first couplet; अनुभव over शास्त्र; सधुक्कड़ी as an object of study; the turn going inward | reading a साखी as usable advice — above all `हम घर जाल्या`, which must never read literally; merging साखियाँ; correcting the dialect; a lesson on religion or biography |
| **bal_katha_kavita** | घटना + संवाद + तुक | **one छंद-इकाई — one beat, or one speaker's turn** | who is speaking (there are no tags), what happens next in the poem's own order, the तुक heard before it is named, the joke, the मोड़ named once | cutting mid-turn or splitting a couplet; prose-summarising the poem; a tacked-on शिक्षा; naming अलंकार the poem does not carry; reading a couplet as self-contained advice |
| **bal_khel_geet** | लय + दोहराव + खेल | **one छंद-इकाई — one stanza with its टेक, or one call-and-response turn** | the beat said out loud, the टेक that never changes, the joke named as a joke, what the body is doing, the rhyme pair heard before it is named | explaining a nonsense image straight-faced; extracting a शिक्षा from a chant; printing the टेक once or cutting it into its own topic; naming अलंकार; adding a fact the page lacks |
| **niti_doha** | अनुभव की सीख + दृष्टांत | **one दोहा** | the everyday picture, the turn in line 2, the सीख the child can use | merging दोहे; giving the सीख without the दृष्टांत; a moral lecture |
| **chaupai_doha_samvad** | प्रसंग + पात्र + वचन | **one संवाद-विनिमय, अपनी चौपाई-दोहा इकाई के भीतर** | who is speaking (the tags are dropped), the many names of one person, the caesura inside the चौपाई, the दोहा as clincher, अवधी as an object of study | one दोहा per topic; one चौपाई per topic; a whole run as one topic when it holds two exchanges; splitting a speech from its reply; retelling it as prose |
| **bhakti_pad** | भाव + संबंध + लोक-भाषा | **one पद** | वात्सल्य/भक्ति, the speaker's voice, ब्रज sweetness, the टेक | flattening it into "lying is wrong"; correcting ब्रज to खड़ी बोली |
| **mukt_chhand_kavita** | भाव + बिंब + गति | **one भाव-खंड** | the line-break as the craft, the बिंब, who addresses whom, plain words doing heavy work | inventing छंद; naming अलंकार that are not there; prose-summarising the poem; one line per topic |
| **smriti_virah_geet** | स्मृति + बिंब + संबोधन | **one भाव-खंड (छंद-समूह)** | the gap between what is felt and what is sent; ध्वन्यात्मक doubling as weather; the doubled rhyme; the conditional `होगा`; nature as messenger | one स्तबक per topic; splitting a portrait or a remembered speech; reading `मस्त हूँ मैं` literally; turning it into a biography or a patriotic lesson |
| **prakriti_deshbhakti_kavita** | चित्र + भाव + अलंकार | **one छंद** | imagery, the अलंकार doing work, the टेक's changes, pride without slogan | slogans; over-scientifying nature; skipping the craft |
| **vir_ras_kavita** | ओज + गति + चरित्र | **one छंद** | rhythm as speed, the animal/warrior's courage, sound | glorifying violence; reducing it to a history date-list |
| **kahani** | घटना + पात्र + मोड़ | **one घटना** | the turn, why a character chooses, show-don't-tell | summary-only; a tacked-on शिक्षा |
| **sansmaran** | स्मृति + स्वर + मूल्य | **one स्मृति / जीवन-चरण** | the 'मैं' voice, the remembered detail, what the life shows | a date-list; preaching; turning memoir into biography |
| **soochnatmak_sanskritik** | तथ्य + परंपरा + जिज्ञासा | **one तथ्य / प्रथा** | the practice in its own terms, accurate community names, curiosity | exoticising; "tribal people"; turning it into a Science lesson |
| **samvad_nibandh** | तर्क + दृष्टिकोण + ज़िम्मेदारी | **one तर्क / exchange** | both sides, the responsibility asked of the reader | one-sided preaching; flattening the opposing voice |
| **lalit_atmaparak_nibandh** | आत्म-स्वर + पड़ाव + विनोद | **one विचार-पड़ाव** | the self-deprecating 'मैं'; irony named; the turn where the essay stops preparing and becomes the essay; the frame closing on its first image | judging one-sidedness as a fault; turning the essay into a निबंध-लेखन checklist; dropping the quoted verse or anecdote; a tacked-on शिक्षा |
| **sakshatkar** | प्रश्न + उत्तर + व्यक्ति | **one प्रश्न-उत्तर जोड़ा** | what the question is doing, the answering voice kept intact, anecdotes and verse inside an answer | splitting Q from A; dropping the question and summarising the answer; moralising the person |
| **ekanki** | संवाद + रंग-संकेत + मोड़ | **one stage-beat (दृश्य-प्रसंग / संवाद-खंड)** | रंग-संकेत as text and as the cut marks, the exposition device, subtext, dramatic irony, the closing line that repeats an earlier one, the single room as constraint, performability | supplying a narrator or retelling it as a story; dropping or narrating the stage directions; cutting mid-exchange or by page; a tacked-on शिक्षा |
| **diary** | दिन + दृष्टि + दस्तावेज़ | **one प्रसंग of the day, in clock order** | seen versus heard, the exact times, real people named as the text names them | hindsight; re-ordering the day by theme; turning the entry into a history lesson |
| **prarthana_kavita** | याचना + शर्त + आत्मबल | **one छंद, or one complete petition** | the refusal as the argument, the returning address, grammar doing the work of imagery, self-reliance inside devotion | cutting a petition in half; reading the refusal as doubt; a tacked-on शिक्षा; inventing pictures the poem lacks |
| **niti_upadesh_kavita** | सीख + दृष्टांत + टेक | **one छंद, closed by its टेक** | the unchanging टेक taught once then referenced, दृष्टांत as evidence rather than story, the imperative mood, the rhyme reaching the टेक every time, the turn from claim to command | splitting a छंद; re-explaining the टेक every topic; reducing a छंद to a one-line moral; retelling the दृष्टांत as mythology; reading सुमृत्यु as a call to die |
| **samiksha_vyaktichitra** | दावा + प्रमाण + व्यक्ति | **one समीक्षा-प्रसंग (दावा + उसे कमाने वाला प्रमाण)** | naming the move — asserting or paying; counter-facts as the spine; praise taught as a claim that may be disputed; quoted work and dialect kept exactly | scoring one-sidedness as a fault; dramatising a cited anecdote into a scene; turning it into a biography or filmography; presenting the verdict as fact |
| **bhashan_uddabodhan** | अपील + दृष्टि + सौंपना | **one अपील / तर्क-सोपान** | the rhetoric named, the occasion and date, what the listener is asked to give up | judging it as an essay for being one-sided; sloganising; turning it into a biography |
| **yatra_vrittant_patra** | पड़ाव + दृष्टि + संबोधन | **one पड़ाव** | the traveller's eye, the addressee, simile as the tool, old Hindi as an object of study | cutting by subject instead of by stop; reordering; dropping the salutation/sign-off; modernising the prose |

## Mixed chapters

Common in मल्हार — गोल is संस्मरण **plus** a सूचनात्मक description of डाँडी-गोथा **plus** a short
कहानी. When it happens:

1. `genre: "mixed"` in `01_meta.json`, parts listed **dominant first**.
2. Load **every** matching profile, dominant first.
3. **Cut each part under its own explanation unit.** The appended poem is cut छंद-wise even though
   the dominant part is cut घटना-wise. Do not flatten to one unit.
4. Apply each part's lens and avoid-list **to that part only**. The dominant विधा sets the
   chapter's `guiding_question`; a sub-part keeps its own engine question for its topics.
5. Agents 7 and 13 check that no part lost its essence to the dominant template.

**In मल्हार class 8 the mixed chapter is the norm, not the exception** — eight of ten chapters end
with a `झरोखे से` or `पढ़ने के लिए` block carrying a second, complete text with its own author line
(`CLASS8_PLAN.md` §2.2). Those blocks are **reading scenes, not अभ्यास**: they are text, they carry
attribution, and the chapter's own साझी समझ compares them against the main reading. Agent 10 keeps
the exercise blocks; the appended text goes to Agent 2 under the rule above. A one-box अंश is one
topic; a seven-page appended कहानी is cut घटना-wise like any other.

## Most important

- Route by **all four signals**; let theme break ties; surface low confidence before drafting.
- For verse, **unit length is diagnosed before theme** — दोहा and पद are units English has no
  name for, and they are where a generic pipeline fails.
- Each profile's **avoid** list is a hard constraint enforced by Agents 7 and 13, not advice.
- A mixed chapter loads multiple profiles and keeps each part's own unit.
