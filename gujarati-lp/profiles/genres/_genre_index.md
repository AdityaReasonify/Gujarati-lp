# સ્વરૂપ Profiles — master index (diagnosis + routing)

Entry point after Agent 1 reads a chapter. Routes the four diagnosis signals
(`reference/genre_diagnosis.md`) to a profile, which then parametrizes Agents 2/5/7/9/10/12.

> ⚠️ Every named chapter below is **evidence from the measured corpus, not data for your chapter**.
> The GSEB PDFs are image-only, so every fact cited here was transcribed from a rendered page
> (`reference/corpus/std-6_inventory.md` … `std-10_inventory.md`). Diagnose from YOUR chapter's
> structure, theme, સ્વાધ્યાય and purpose — never from a sample, and never from a title.
> (`reference/no_hallucination_policy.md`)

## Decision tree

```
START: read structure (A), theme (B), સ્વાધ્યાય (C), purpose (D).

Is the text in verse?  ── YES → sub-diagnose by UNIT LENGTH FIRST, negative tests first:
│   ├─ NO repeating unit anywhere — no ટેક, no કડી of equal length, no couplet pairing;
│   │   line lengths vary freely and the printed gaps are uneven
│   │      → mukt_chhand_kavita.md   (HARD: cut by વિચાર-એકમ; invent no કડી and no ટેક)
│   ├─ the piece WITHHOLDS its subject — a blank answer-box under it, an 'હું' that is not a
│   │   person, a clue printed to rule a guess out; and the pieces shuffle freely
│   │      → ukhanu_ramatgeet.md     (HARD: the answer never leaves the recall answer)
│   ├─ exactly FOURTEEN lines, one continuous argument, a turn in the last two — no ટેક, no
│   │   returning line-end word, a modern dated poet
│   │      → sonnet.md               (HARD: the ચોટ is never split; never cut couplet-wise)
│   ├─ the units run in SEQUENCE and cannot be reordered — named characters, speech carried
│   │   inside the line by કહે / બોલ્યો, a result at the end, and no ટેક
│   │      → kathakavya.md           (HARD: cut by વાર્તા-પગલું at a કડી boundary, never કડી-wise)
│   ├─ a SET of two-line units under one title by one poet, bound by a રદીફ that returns at
│   │   the line-ends or by one કાફિયા family; no ટેક anywhere
│   │      → gazal.md                (HARD: one શેર = one topic; no story running across શેર)
│   ├─ each printed piece is complete in itself and the next owes it nothing — દુહો, છપ્પો,
│   │   સોરઠો, મુક્તક, હાઈકુ, printed one after another under one head
│   │      → duha_chhappa.md         (HARD: one printed piece = one topic, never merged)
│   ├─ a sung પદ with a ટેક, a medieval ભક્ત poet, and a છાપ inside the verse
│   │      → pad_bhajan.md           (HARD: one પદ whole — ભાવ, never a morality lesson)
│   ├─ the author slot prints `- લોકગીત` or `સંકલિત` where a name would go; an occasion
│   │   (વર્ષા, લગ્ન, આતિથ્ય), તળપદા forms, and a સમૂહગાન instruction
│   │      → lok_geet.md             (HARD: no poet is ever named for the song)
│   ├─ second person to પ્રભુ — or to a life-ideal — and ASKING: an asking verb in the
│   │   આજ્ઞાર્થ/વિધ્યર્થ, a returning vocative, strength asked for instead of rescue
│   │      → prarthana_kavita.md     (HARD: never cut between the asking and what is asked for)
│   └─ a ટેક plus કડી of roughly equal length, a modern named poet, and a feeling built out
│       of pictures — the verse fallback
│          → urmikavya_geet.md       (HARD: a changed-words ટેક is a topic at each occurrence)
│
└─ PROSE → what moves it?
    ├─ a `પાત્રો` box, or speaker labels in label position, PLUS રંગસૂચના in round brackets
    │      → natak_ekanki.md         (HARD: રંગસૂચના are text, and they mark the cut)
    ├─ a salutation to a named reader with a signature-and-relationship at the end, OR
    │   material ordered by where the writer stopped (it fails the reorder test)
    │      → patra_pravas.md         (HARD: cut by પડાવ; never reorder, never drop the sign-off)
    ├─ third person about a REAL person with dates, places and honours on the page; one
    │   episode shows one quality
    │      → charitra_prasang.md     (HARD: name the printed act before naming the quality)
    ├─ first person where the 'હું' IS the subject — a day, an attempt that fails, a thing
    │   that is gone, a joke at the writer's own expense
    │      → nibandh_atmaparak.md    (HARD: the speaker is the subject of the first sentence)
    ├─ two voices arguing, or one voice making a case somebody could disagree with
    │      → samvad_nibandh.md       (HARD: report both sides; never issue a directive)
    ├─ drop the frame and the payload still stands — facts, a process, a practice, a how-to
    │      → mahitiprad_gadya.md     (HARD: cut by માહિતી-ખંડ, never by speaker turn)
    └─ drop the frame and the chapter is gone — પાત્રો, a chain of ઘટના, a વળાંક
           → varta.md                (HARD: cut by ઘટના; no tacked-on બોધ)
```

**One printed exception inside the drama branch.** The apparatus routes to `natak_ekanki.md`, but
where the book prints its own label **સંવાદ** rather than નાટક — std-6 ch 3 બાણ તો ત્યારે જ છૂટશે…
("આ **સંવાદ**માં…", closing task "આ એકમને વર્ગમાં **સંવાદ સ્વરૂપે** રજૂ કરો.") and std-6 ch 14
એક છોકરો રિસાણો, which carries speaker labels and not one bracketed direction — `samvad_nibandh.md`
is dominant and `natak_ekanki.md` loads alongside it for the explanation unit and for the
directions-are-text gate. The book's own label decides; a performance task never does.

Verse is sub-diagnosed **by unit length before theme**, because getting the unit wrong breaks the
cut and nothing downstream recovers. દુહો, પદ and શેર are units English has no name for, and a
generic pipeline fails on exactly them.

**અછાંદસ is tested before every other verse branch, and the test is a negative one.** Each of the
other verse profiles asks "is the unit two lines / a પદ / a કડી / a શેર?" — and અછાંદસ answers no to
all of them, then falls through to whichever thematic profile is nearest, which proceeds to cut it
કડી-wise into કડી the page does not contain. std-9 ch 10 એ લોકો prints four uneven verse-paragraphs
(3 / 4 / 2 lines and a hanging line) and nothing that returns; its own કવિ-પરિચય carries the form
word (`'પ્રબલગતિ' મુખ્યત્વે ગદ્યકાવ્યોનો સંગ્રહ`) because the intro box does not. Ask
*શું અહીં કોઈ પુનરાવર્તિત એકમ છે ખરો?* first, and route on the absence.

**ઉખાણું is tested immediately after it, and it is the mirror of the same question.** અછાંદસ asks
whether a unit repeats; this profile asks whether the piece is **hiding** something. Its nearest
miss is not a neighbouring form but the fallback itself: short rhymed lines in a child's vocabulary,
printed among poems, and `urmikavya_geet.md`'s lens (ચિત્ર + ભાવ + અલંકાર) will send the explanation
hunting a ભાવ that is not in the piece. std-6 P1 item 4 ચતુર કરો વિચાર ! prints seven riddles, each
closed by an **empty answer-box**, with no author line anywhere — the page is asking the child, not
telling the reader. Two further tests, either sufficient: the pieces shuffle without loss, and the
title addresses a solver.

**સૉનેટ is tested third, because its test is a count and counting is cheaper than judging.** No other
form in this corpus is fixed at a line count. Two branches would otherwise take it: the અછાંદસ test
above asks whether any unit repeats and a સૉનેટ answers no — but its lines do not vary freely and its
gaps are not uneven, which is the rest of that branch's test; and `gazal.md` matches on the printing,
because std-10 ch 7 જીવમાં જીવ આવ્યો sets its fourteen મંદાક્રાન્તા lines as seven couplets and a
ગઝલ's શેર look exactly like that. The tell is what binds them: a ગઝલ's couplets are independent and
tied by a returning રદીફ or one કાફિયા family, while these fourteen lines are **one sentence-movement**
with a turn in the last two and nothing returning at the line-ends. std-9 ch 8 આભાર is the other
setting of the same form — fourteen continuous lines, no stanza break, run-on syntax — and its own
કૃતિ-પરિચય defines the form ("ચૌદ પંક્તિની મર્યાદા… અંતિમ બે પંક્તિઓમાં… અસરકારક ચોટ"), while its
MCQ block makes the child choose સોનેટ against ગઝલ, ઊર્મિકાવ્ય and પદ. The books name the confusable
set themselves.

**કથાકાવ્ય is tested before દુહો and before the ગીત branches.** std-7 ch 11 અંધેરી નગરી is written
in rhymed couplets that carry a બોધ, so `duha_chhappa.md` matches on shape — and its hard gate
(one printed piece = one complete topic) would cut the poem into dozens of two-line advice topics
with no story in any of them. These couplets are **incomplete on purpose**: each hands the plot to
the next. std-6 ch 10 સાથી મારે બાર is the other direction of the same error — it reads as a બાળગીત
until ધૂળો, the four ચોર and the closing tally are noticed. Two positive tests settle it, and the
books hand them over: **can the કડી be reordered, and is anyone speaking?** Both chapters print a
verse→prose retelling block ("આ એક કથાગીત છે. તેને વાર્તા સ્વરૂપે લખો.") and a speaker-attribution
block; a poem that gets both is telling you it has a plot.

**ગઝલ is tested before દુહો/મુક્તક, because one શેર lifted out of a ગઝલ is indistinguishable from a
મુક્તક — the SET is the tell.** std-8 ch 10 હલેસે હલેસે runs the રદીફ `દરિયો` to the end of every
શેર and signs `'આદિલ'` in the last one; std-9 ch 14 મારું તારું ! has no રદીફ at all and is bound by
a rhyme family alone (મારું, તારું, સહિયારું, હારું, પ્યારું, ખારું). Absence of a રદીફ never routes
a poem away from ગઝલ, and absence of a તખલ્લુસ never does either. std-10 ch 15 તે બેસે અહીં is the
third measured chapter and runs the રદીફ `તે બેસે અહીં` to the end of all five શેર with no છાપ at all.
Through std 9 the books never print the words શેર, રદીફ or કાફિયા — **their word is પ્રાસ**, and the
rhyme-hunt block is the કાફિયા taught under another name; **std 10 prints all three**, and ch 15's
ભાષા-અભિવ્યક્તિ block defines them outright.

**પદ is tested before લોકગીત and before પ્રાર્થના, and its tell is cheap and decisive: a medieval
ભક્ત poet AND a છાપ inside the verse.** Sung, a returning line and a devotional address are shared
by half the verse corpus, so any one of them alone routes nothing. std-9 ch 20 હરિ ! આવોને is
devotional, second-person and even asks — and it is a લોકગીત, because the author slot prints
`સંકલિત`, there is no કવિ-પરિચય and no છાપ. std-10 ch 4 જીવન અંજલિ થાજો and std-8 ch 1 જીવનજ્યોત
address પ્રભુ with a returning refrain — and are પ્રાર્થના, because the poets are modern, dated and
sign nothing. Drop the છાપ and drop the ભક્ત and the unit is almost always ગીત, લોકગીત or
પ્રાર્થનાગીત.

**પ્રાર્થના is tested before the fallback, and its gate is the exact inverse of the fallback's.**
`urmikavya_geet.md` requires the first sentence of every explanation to name something in the કડી
that can be seen, heard or counted; `prarthana_kavita.md` requires it to name what the કડી **asks
for**. A prayer builds feeling out of **grammar** — the optative થાજો, the returning vocative
"પ્રભુ હે…", the વણ- privative compounds વણદીવે and વણજહાજે — not out of pictures, and an agent
carrying the ઊર્મિકાવ્ય lens into such a chapter goes hunting imagery that is not there and supplies
it. The positive test is one sentence long: **does the poem ask to be spent rather than spared?**

**નાટક is tested before સંવાદ-નિબંધ and before વાર્તા, and the tell is the apparatus, not the
presence of dialogue.** A play has two voices, so an argument-first test matches it and starts
hunting positions; a play has a plot and a turn, so a વાર્તા-first test matches it and starts
summarising. Both then drop the રંગસૂચના, because neither profile has anywhere to put them — and
`(અધવચથી અટકાવી)`, `(પોક મૂકે છે.)`, `(સહુ મેવાડનો જય ગજાવે છે. પડદો પડે છે.)` are where the play
keeps its plot. Route on the `પાત્રો` box, the label-position speaker names and the bracketed
directions. `samvad_nibandh.md` carries the same rule as a machine gate in the other direction: any
label-position speaker tag or parenthetical direction found where it is dominant is a blocking
reroute.

**પત્ર/પ્રવાસ is tested before ચરિત્ર-પ્રસંગ and before માહિતીપ્રદ ગદ્ય, on the reorder test.**
A માહિતીપ્રદ chapter is organised by subject and could be printed in another order — the ગરબો/ગરબી
ભેદ does not have to precede the list of લોકનૃત્યો. A પ્રવાસવર્ણન could not, because the order **is**
the journey: ધોરડો cannot be reached before ખાવડા. A પત્ર could not either, because the salutation
cannot follow the news. std-6 ch 8 મામાનો પત્ર is the case that decides the order of the tests: it
carries a full ચરિત્ર-પ્રસંગ about two real painters **inside** a letter whose frame is not
removable — sender block, "પ્રિય પ્રાચી,", "- વિવેકમામાનાં આશિષ" — and the letter's own સ્વાધ્યાય
asks the child to write the reply. The outer form decides the cut, the lens and the writing task.

**The person test separates ચરિત્ર-પ્રસંગ from આત્મપરક નિબંધ, and it is run before either is
accepted.** Ask who the 'હું' of the *running prose* is. If it is the writer, the chapter is
`nibandh_atmaparak.md` however admirable the person being described — std-9 ch 15 સો ટચનું સોનું,
std-9 ch 17 છબિ ભીતરની, std-8 ch 3 મારી વ્યાયામસાધના and std-10 ch 6 સામગ્રી તો સમાજની છે ને ! all
put a real person and a real incident on the page in the first person. A **quoted** 'હું' is normal
in `charitra_prasang.md` and routes nothing: std-10 ch 5 opens on a quoted memoir block and hides its
own writer at the end as `(આલેખન : રમેશચંદ્ર ડી. પંડ્યા)`. The other half of that profile's tell is
truth furniture — dates, places, institutions, honours. A વાર્તા does not carry a death date, and a
પૌરાણિક figure with no date and no archive (std-8 ch 2 ત્યાગવીર દધીચિ, std-9 P3 ઉપમન્યુ) leaves the
truth-claim gates nothing to bite on and goes to `varta.md`.

**આત્મપરક/લલિત નિબંધ is tested before સંવાદ-નિબંધ, for the mirror-image reason.** A લલિત નિબંધ is
one voice with no opponent, and `samvad_nibandh.md`'s hard gates score exactly that as one-sided
preaching and a flattened opponent — marking the form's defining property as a defect. The split
inside the word "નિબંધ" is therefore stated positively: **is the subject the writer's own
experience, or a claim somebody could disagree with?** std-8 ch 5 બાનો વાડો and std-9 ch 19 પંખીલોક
are the first (the book calls them લલિતનિબંધ); std-9 ch 6 ભાષા જાય તો સંસ્કૃતિ જાય and std-8 P2
જીવનમાં વ્યવસ્થિતતા are the second — delete the 'હું' and the case still stands, developed by તર્ક.

**માહિતીપ્રદ ગદ્ય is tested before વાર્તા, on the drop-the-frame test.** Remove the frame and ask
what is lost. In a વાર્તા the story goes with it and nothing is left; here the payload stands —
the water still evaporates, rises, condenses and falls. std-6 ch 5 વીજળીરાણી is a grandfather's
bedtime tale about the grid, std-7 ch 4 ટીપાંની સફર is the જલચક્ર told by talking raindrops (its
intro box says **વાર્તા** and the chapter is still cut here — the noun names the manner, the verb
names the payload), std-8 ch 9 શતરંગી ભારત is cultural fact delivered by a child's questions. A
વાર્તા-first test takes all three and teaches a plot that is not there, then asks why a character
chose. What is absent confirms it: none of these chapters prints an event-ordering block or a
counterfactual, the two સ્વાધ્યાય blocks that mark a વાર્તા.

## Master table

| Profile | Lens | Explanation unit | Emphasise | Avoid (hard gate) |
|---|---|---|---|---|
| **mukt_chhand_kavita** | ચિત્ર + મૌન + પંક્તિ-ભંગ | **one વિચાર-એકમ** | the પંક્તિ-ભંગ as the craft; બિંબ over અલંકાર; who speaks, to whom, about whom; પુનરાવર્તન as spine; everyday words doing heavy work; the વ્યંગ held as વ્યંગ | naming a છંદ; inventing કડી; imposing a ટેક on an anaphora; "fixing" the line breaks; a non-empty `rhyming_words`; one line per topic; a tacked-on બોધ; supplying a real-world target the page leaves unnamed |
| **ukhanu_ramatgeet** | સંકેત + રમત + અનુમાન | **one ઉખાણું / one piece** (a list-shaped શબ્દરમત set is ONE topic) | the clue quoted first; the disguise named as a disguise; the one line that closes the door; the blank answer-box pointed at; the sound heard before it is named; what the child does with it | giving the answer away; asserting an answer the page does not print; an explanation that does not end on a question; straight-faced encyclopedia description; બોધ; a science lesson about the answer; merging two pieces; a chapter-final fun box cut as a topic |
| **kathakavya** | ઘટના + પાત્ર + વળાંક | **one વાર્તા-પગલું**, boundaries always at a printed કડી end | who is speaking (there are no tags); what happens next in the poem's own order; the turn named once; why the character chooses; the પ્રાસ heard before it is named; the joke; the old words as the poem's own | splitting a કડી; cutting કડી-wise instead of step-wise; ending mid-episode; prose-summarising the poem; a tacked-on બોધ; craft terminology opening the explanation; treating a couplet as self-contained advice; spoiling the turn; reading the satire as being about a community |
| **sonnet** | બંધ + વળાંક + ભાવની ઘનતા | **one ભાવ-ખંડ (movement)** — two to four in a chapter, one where the poem is one unbroken move | the fourteen-line frame, once, in the child's terms; the turn named in the topic that carries it; the long sentence walking across the printed lines; the dense word doing a whole line's work; sound as content (પુનરાવર્તન, રવાનુકારી, દ્વિરુક્ત); whether the title earns itself | couplet-wise or line-pair-wise cutting; a split ચોટ; a cut through a sentence; an invented ટેક or કડી; a છંદ named where the page does not print one (and none below std 10); the ચોટ turned into a બોધ; invented craft; form-parts named as અલંકાર; modernising the poet; letter-spacing carried into the verbatim |
| **gazal** | શેર + રદીફ-કાફિયા + મિજાજ | **one શેર** | the શેર standing on its own two feet; the returning word named in every topic; the picture in line one and the turn in line two; metaphor held as metaphor; the poem's મિજાજ; દ્વિરુક્ત forms as લય | merging or splitting a શેર; a story or causal chain across શેર; a topic that never names the return; reading મયખાનું-vocabulary literally or romanticising it; inventing a ટેક; naming રદીફ/કાફિયા/છાપ as an અલંકાર; moving the તખલ્લુસ out of the verse |
| **duha_chhappa** | અનુભવની શિખામણ + દૃષ્ટાંત | **one printed piece, always** (દુહો · છપ્પો · મુક્તક · હાઈકુ) | the દૃષ્ટાંત named plainly before any moral language; the turn word; the ચોટ; the કટાક્ષ where the book names it; compression; usability in the child's own month; for a હાઈકુ, the picture and the quiet after it | merging two pieces; the શિખામણ without the દૃષ્ટાંત; a moral lecture; બોધ-language imported onto a હાઈકુ; reading a satiric છપ્પો straight; modernising મધ્યકાલીન forms; losing the છાપ; invented biography; media that shows the moral |
| **pad_bhajan** | ભાવ + સંબંધ + લોકભાષાની મીઠાશ | **one પદ, whole** | ભાવ above all; the speaker's voice and her signature; the relationship as household nearness; the chosen sound of the archaic forms; the ટેક and what returning does | flattening it into a morality lesson (poster test); splitting the પદ; making the ટેક its own topic or concept; losing the છાપ; correcting the poet to માનક ગુજરાતી; theology or comparative religion; iconographic media |
| **lok_geet** | કંઠ + ધ્રુવપંક્તિ + લોકજીવન | **one કડી, or one refrain-round** | the occasion, concretely; the group voice (આપણે, not "the poet"); the તળપદો શબ્દ as the thing itself; what each round adds to the list; the ટેક's returning, once; sound as content; cultural furniture explained plainly | hunting a change in an unchanged ટેક; naming an author for the song; standardising the dialect; deleting જી રે / રે ! / the refrain shorthand; expanding the refrain inside the verbatim; a tacked-on બોધ; a custom lecture; merging the appended ગાઈએ-box poem |
| **prarthana_kavita** | યાચના + સંબોધન + આત્મબળ | **one કડી of the petition** | what is asked, in the poet's own verb; the direction of the asking — to be spent, not spared; the repeated address; grammar doing the work of imagery; આત્મબળ inside devotion; the પ્રાસ the સ્વાધ્યાય will ask for | turning the prayer into a moral; cutting a petition in half; an explanation that opens on scene or ભાવ instead of the asking; supplied imagery; paraphrasing away the vocative; reading the asking as doubt; theology; a deity depicted in an image |
| **urmikavya_geet** | ચિત્ર + ભાવ + અલંકાર | **one કડી** (verse fallback; holds કૂચગીત) | the picture before the feeling; અલંકાર that is doing work; the ટેક's movement across the poem; પ્રાસ and લય; sound-words as content; scale, and the child's smallness before it | slogans; an explanation that states the ભાવ first; over-scientifying nature; skipping the craft; invented craft; literal reading of a figurative line; political framing (the land, not the state); the refrain shorthand expanded inside the verbatim |
| **natak_ekanki** | સંવાદ + રંગસૂચના + વળાંક | **one stage-beat** (દૃશ્ય-પ્રસંગ / સંવાદ-ખંડ) | રંગસૂચના as text and as the cut marks; the exposition device; subtext; dramatic irony; a closing line that returns an earlier phrase; the single room as constraint; register and આરોહ-અવરોહ; performability | a supplied narrator or an unspoken interior state; dropped or narrated રંગસૂચના; reassigned speech; dropping or absorbing the header; cutting through a governed pair; topic inflation on one talkative situation; a tacked-on બોધ; an exercise-embedded script cut as text |
| **patra_pravas** | પડાવ + દૃષ્ટિ + સંબોધન | **one પડાવ** (a place, or one matter the letter turns to) | the eye, not the encyclopaedia; the addressee and the relationship named in the chapter's own words; the writer's opinions attributed to the writer; comparison as the traveller's tool; loan and local words as objects of study; place and practice with respect | cutting by subject or reordering the journey; dropping the salutation or the sign-off; leaving the addressee unnamed; inventing a destination detail; a travel-guide or geography lesson; a letter turned into biography; a tacked-on બોધ; pity-framing; a cloze reply-letter or a printed જાહેરાત cut as a topic |
| **charitra_prasang** | પ્રસંગ + સ્વભાવ + મૂલ્ય | **one જીવન-પ્રસંગ**, or one printed person-section | the verb in the first sentence; the concrete means (પગેરું, સગડ, સહકારી મંડળી, તખ્તો); what the act cost; the person's own quoted words; the honour as a consequence, placed after the act; the second payload where the intro box names one | invented dialogue or biography; dramatised interiority; hagiography — a quality named before the act that earned it; biography-by-chronology; merging or splitting a printed person-section; first-person slippage; the writer's era line read as the subject's; jingoism; pity-framing; a printed ચમત્કાર asserted or debunked |
| **nibandh_atmaparak** | સ્વર + પ્રસંગ + પોતાની જાત પરની નજર | **one પ્રસંગ, અથવા વિચારનો એક વળાંક** | the voice, quoted; the admission that the attempt failed; the turn where mood or treatment changes; where the laugh lands, in one clause; the concrete object; the spoken register as craft; the essay's own sentence-craft, once | flattening the voice into unattributed information; converting the essay into a plotted story with a moral; a tacked-on બોધ; explaining or apologising for the joke; inverting the irony; ascribing a first-person admission to a chapter that has none; correcting the spoken register; inventing interiority for a real named person; cutting by page or by a person's name; losing the closing gesture and its credits |
| **samvad_nibandh** | તર્ક + દૃષ્ટિકોણ + જવાબદારી | **one move of the argument** | both sides, fairly; the move each turn makes — objecting, conceding, giving evidence, asking; what the text asks of the reader, attributed to the text; સજીવારોપણ where a non-human speaks; everyday reasoning; the abstract words glossed at first use | a one-voice summary of a two-voice passage; preaching — any second-person directive to the child; a flattened opponent; quoted speech converted to reported speech; guilt laid on the child or the family; topics cut on fact boundaries (reroute); a speaker-labelled script routed here (reroute) |
| **mahitiprad_gadya** | તથ્ય + પરંપરા + જિજ્ઞાસા | **one માહિતી-ખંડ** (holds the માર્ગદર્શક લેખ sub-form) | the fact in the first sentence; concrete detail — materials, movements, timing; the practice in its own terms; the frame as craft, in one sentence; curiosity, not distance; the child's own મેળો, ગરબા or meter box; comparison with both sides equal | re-teaching the frame as a વાર્તા; cutting by speaker turn, page or paragraph; adding facts the chapter does not carry; turning it into a Science lesson; substituting a familiar equivalent for a practice's printed name; exoticising or a generic label for a named community; a living practice put into the past; ranking cultures; a tacked-on બોધ |
| **varta** | ઘટના + પાત્ર + વળાંક | **one ઘટના** | the turn, named once and marked `climax`; why a character chooses; બતાવવું, કહી દેવું નહીં; dialogue as character; the theme as something the story demonstrates; the teller's marks in a લોકકથા or પૌરાણિક કથા | summary-only teaching; a tacked-on બોધ; judging a character the story treats with sympathy; spoiling the turn early; debunking or verifying a પૌરાણિક કથા; standardising a લોકકથા's dialect; narrating what an excerpt does not contain |

**No chapter may match two rows of this table.** Where a chapter genuinely matches two, that is a
mixed chapter (below) or a `genre_confidence: "low"` output with the disagreement named — never a
silent choice.

## Forms the books name that do NOT have their own profile

GSEB intro boxes name their સ્વરૂપ generously, and the roster is deliberately smaller than that
vocabulary. Each row below is a **sub-form** held by a profile: same unit, same lens, and only the
Media / Language / Sensitivity priors move.

| Form as the book names it | Held by | What moves |
|---|---|---|
| લોકકથા · પૌરાણિક કથા · ટૂંકીવાર્તા · લઘુકથા · નવલકથાખંડ · દૃષ્ટાંતકથા · પ્રાણીકથા · ચાતુર્યકથા · વિજ્ઞાન-કલ્પનકથા · અનુવાદિત વાર્તા | `varta` | register and Media priors; the excerpt rule for a નવલકથાખંડ |
| છપ્પો · સોરઠો · મુક્તક · હાઈકુ · શ્લોક કે પદનો સંકલિત સંચય | `duha_chhappa` | a હાઈકુ carries an extra gate against બોધ-language; a compiled સંચય (std-8 P4 વિવિધા ભારતી — ગીતાના શ્લોક, કબીરના દોહા, મનાચે શ્લોક, નાનકની પંક્તિઓ, each with its own Gujarati સમજૂતી) is a set of independent pieces, one topic each, and its printed Devanagari verse is quoted content the script check must whitelist |
| કૂચગીત · બાળગીત · પ્રકૃતિગીત · વિદાયગીત | `urmikavya_geet` | the slogan gate bites hardest on a કૂચગીત |
| લગ્નગીત · વર્ષા-લોકગીત · આતિથ્યગીત | `lok_geet` | the round is the unit where the song cycles a list |
| શબ્દરમત · તુકબંદી *(unmeasured)* | `ukhanu_ramatgeet` | a list-shaped word-play set is one topic, not eight |
| રેખાચિત્ર · ચરિત્રનિબંધ · પ્રસંગકથા · સાહસકથા built on a real life · ચરિત્રલેખ | `charitra_prasang` | printed person-heads carry the cut; ચમત્કાર content carries its own gate |
| સંસ્મરણ · આત્મકથાખંડ · આત્મકથનાત્મક નિબંધ · લલિતનિબંધ · હાસ્યનિબંધ · હાસ્યલેખ · રમૂજી પ્રસંગકથા · અનુભવકથા | `nibandh_atmaparak` | the હાસ્ય and સંસ્મરણ sections of that file govern |
| પ્રવાસવર્ણન · પ્રવાસ-નિબંધ · પત્રલેખન | `patra_pravas` | a place is a પડાવ and a પત્રખંડ is a પડાવ |
| સૂચનાત્મક/સાંસ્કૃતિક ગદ્ય · માહિતીપ્રદ નિબંધ · માર્ગદર્શક લેખ · સંવાદ-શૈલી વિજ્ઞાનકથા | `mahitiprad_gadya` | a માર્ગદર્શક લેખ keeps the printed step order and the second-person address |
| વિચારપ્રધાન / ચિંતનાત્મક નિબંધ · સંવાદ-લેખ | `samvad_nibandh` | an essay strand is a move; a સંવાદ exchange is a move |
| હળવું એકાંકી · ઐતિહાસિક નાટક · સામાજિક નાટક | `natak_ekanki` | comic timing and dramatic irony in the હળવું sub-form |

> ⚠️ **Roster status — VERIFY-3 closed for the roster itself.** All five inventories
> (`reference/corpus/std-6_inventory.md` … `std-10_inventory.md`) are complete and were read off
> rendered pages, and this index, the seventeen profile files in this directory and the four sibling
> reference files that route by slug (`reference/genre_diagnosis.md`,
> `reference/teaching_lens_map.md`, `reference/explanation_unit_map.md`, `reference/qc_checklist.md`)
> now name the **same roster in both directions**. સોનેટ has its own file at last — `sonnet.md`, fixed by
> std-9 ch 8 આભાર and std-10 ch 7 જીવમાં જીવ આવ્યો ("મંદાક્રાન્તા છંદમાં" per its intro) — and
> `urmikavya_geet.md`'s provisional landing for it is deleted.
>
> What is still open is **diagnosis, not the roster**: તુકબંદી is unmeasured, so a piece diagnosed as
> one is a first and Agent 1 says so in `extraction_notes[]`; std-8 ch 9 શતરંગી ભારત is a
> **two-profile candidate** (`mahitiprad_gadya` vs `samvad_nibandh`); and std-8 ch 14
> નિયમો કોના માટે ? is **unrouted** — five printed દૃશ્ય of civic ઘટના read aloud from a ડાયરી inside a
> frame narration, with `varta` and `mahitiprad_gadya` both arguable. Agent 1 decides each on the
> rendered page and records the doubt in `genre_confidence`. The files in this directory remain the
> routing authority: any file naming a profile that is not in this index is corrected in the same
> commit.

## Appended reading matter — what is a scene, what is apparatus

GSEB chapters carry more boxed matter than the CBSE readers do, and the boxes are the commonest
source of a wrong cut. The measured convention (`reference/corpus/std-6_inventory.md` …
`std-10_inventory.md`):

**1. A block is a reading scene only if it is inside the numbered reading sequence, carries its own
attribution or its own શબ્દાર્થ, and asks the child nothing.** Everything else is apparatus.

**2. પૂરકવાચન / પૂરક વાચન units are reading matter with no numbered exercises.** std-6 P1 (4 numbered
items), std-7 P1–P4, std-8 P1–P4, std-9 P1–P4, std-10 P1–P5 print a pink or oval **પૂરકવાચન** banner,
the text, and a gloss box — no numbered સ્વાધ્યાય, no વિદ્યાર્થી-પ્રવૃત્તિ, no ભાષા-અભિવ્યક્તિ, no
શિક્ષકની ભૂમિકા. Usually the gloss box is a lone શબ્દાર્થ; std-8 P3 also prints a
"શબ્દસમૂહ માટે એક શબ્દ આપો." block of eight items and a one-item રૂઢિપ્રયોગ block, which are Agent
10's. An empty `exercise_inventory` here is a **measured fact, not a gap**, and is recorded as such
in `01_meta.json`. Each numbered item is diagnosed on its own: std-6 P1 holds two
poems, an informational travel essay and a riddle set under one banner, which is `genre: "mixed"`
with four profiles active. std-8 P4 વિવિધા ભારતી is the other anthology of this kind and it routes
whole to `duha_chhappa.md`: four sections (ગીતાના શ્લોક, કબીરના દોહા, રામદાસના મનાચે શ્લોક,
નાનકની પંક્તિઓ), each a self-contained piece carrying its own Gujarati સમજૂતી, `- સંકલિત` in the
author slot and no સ્વાધ્યાય at all. Its verse is printed in **Devanagari**, in four languages — that
is quoted content, whitelisted for the script-purity check (`reference/qc_checklist.md` §B), copied
as printed into `original_chunk`, and never replaced by the Gujarati સમજૂતી that follows it.

**3. Chapter-final boxes are appended matter and are never topics** — in this profile or any other.
Measured kinds: the green **grammar** box with its own banner ("વિશેષણ વિશે જાણીએ",
"ક્રિયાપદ અને કાળ વિશે જાણીએ", "વિરામચિહ્નો"); **fun** boxes (the ગોલુ riddle box of std-6 ch 10 and
std-7 ch 7, the humour box of std-6 ch 5 and std-7 ch 2, "શબ્દોની ફેરકૂદરડી", the P1 palindrome box,
name-games, std-7's શબ્દસીડી board-game page); and pre-blocks (**રૂઢિપ્રયોગ**, કહેવત) printed after
the શબ્દાર્થ box. They go to `extraction_notes[]`; where one asks the child to do something it goes
to Agent 10 (`reference/exercise_alignment.md`).

**4. The one box that IS reading matter — and still is not part of its chapter.** std-6 ch 4 prints
a yellow **ગાઈએ** box holding a second complete poem with its own poet ("મેહુલો" - ત્રિભુવન વ્યાસ)
beside the main લોકગીત. It is text, it carries attribution, and it is nevertheless **not** part of
the લોકગીત: no topic's `original_chunk` may contain a line of it, and no `key_terms`,
`figures_of_speech` or `rhyme_scheme` entry may be drawn from it (`lok_geet.md` hard gate). Record it
in `extraction_notes[]`; if it is ever taught, it is its own unit under its own profile.

**5. A block that looks like reading matter and is an exercise.** Text printed **inside** a
સ્વાધ્યાય block belongs to Agent 10 however much of it there is, and no `original_chunk` may contain
a line of it: std-8 ch 12's whole second play-excerpt (`સ્થળ : પાટણ`, જગડુશા); std-8 ch 1's second
prayer poem "મંદિર તારું વિશ્વ રૂપાળું" - જયંતીલાલ આચાર્ય with three MCQs on it; std-8 ch 10's quoted
poems by રજની મહેતા, સુરેશ દલાલ and સુન્દરમ્; std-8 ch 6's ગાંધીજી letter and mock bill; the mock
advertisements of std-8 chs 3 and 14; std-7 ch 15's printed પ્રવાસ જાહેરાત; std-6 ch 8's cloze reply
letter; std-8 R1's દુહો printed as a વિચારવિસ્તાર seed.

**6. Teacher-addressed apparatus is neither a scene nor an exercise.** The blue intro box (the best
single genre signal in the books — evidence, never a verdict), શિક્ષકની ભૂમિકા, ભાષા-અભિવ્યક્તિ,
વિદ્યાર્થી-પ્રવૃત્તિ and the ચર્ચા-વિચારણા box are recorded in `extraction_notes[]` and must not
enter Agent 10's coverage as exercise blocks — though પ્રવૃત્તિ items that address the child do.
Their prose is evidence about the chapter and is never copied into an `explanation`
(`duha_chhappa.md`'s paraphrase gate).

**7. Whole units that carry no reading scene at all.** The revision units (std-6 R1/R2, std-7 R1/R2,
std-8 R1/R2 — "આગળ વધતાં પહેલાં", "પૂર્ણ કરતાં પહેલાં") and the વ્યાકરણ એકમો (std-9 V1–V4, std-10
V1–V6) are assessment and grammar apparatus: no topic-cutting, no profile, Agent-10-style handling
only. Front matter, the cover spread rendered at the end of std-6's P1 PDF, and the back-cover
board-game are not reading matter either.

## Mixed chapters

A chapter is mixed when two complete texts, or two complete forms, sit inside one unit — std-9 ch 22
લઘુકાવ્યો prints દુહો, મુક્તક and હાઈકુ under one head with star rules and per-section credits;
std-6 P1 holds four independent pieces under one પૂરકવાચન banner; std-9 ch 23 પ્રેરક પ્રસંગો holds
three પ્રસંગ under an umbrella head. When it happens:

1. `genre: "mixed"` in `01_meta.json`, parts listed **dominant first**.
2. Load **every** matching profile, dominant first.
3. **Cut each part under its own explanation unit.** The હાઈકુ is one topic under
   `duha_chhappa.md`'s one-piece rule even where the dominant part is cut ઘટના-wise; an appended
   poem is cut કડી-wise even where the dominant part is prose. Do not flatten to one unit.
4. Apply each part's lens and avoid-list **to that part only**. The dominant સ્વરૂપ sets the
   chapter's `guiding_question`; a sub-part keeps its own engine question for its own topics.
5. Agents 7 and 13 check that no part lost its essence to the dominant template.

**Not every embedded form makes a mixed chapter.** Where the outer form still decides the cut, the
lens and the writing task the book sets, `genre` stays singular and the inner content is recorded in
`genre_signals.theme`: std-6 ch 8's ચરિત્ર-પ્રસંગ inside a પત્ર, std-8 P3's quoted family dialogue
inside a પ્રવાસનિબંધ, std-6 ch 13's classroom frame around an embedded પૌરાણિક કથા (two ઘટના, two
topics, one profile), std-8 ch 6's નરસિંહ પદ lines quoted inside prose about his life (the quoted
lines keep `pad_bhajan.md`'s never-correct and gloss rules inside their prose topic). Where the inner
content is strong enough that the outer frame stops deciding the cut, the protocol above applies and
the decision is recorded in `genre_confidence` — never made silently.

## Most important

- Route by **all four signals**; let theme break ties; surface low confidence before drafting.
- For verse, **unit length is diagnosed before theme** — દુહો, પદ and શેર are units English has no
  name for, and they are where a generic pipeline fails.
- Each profile's **avoid** list is a hard constraint enforced by Agents 7 and 13 — and the structural
  ones by Agent 4, before ids freeze — not advice.
- A mixed chapter loads multiple profiles and keeps each part's own unit.
