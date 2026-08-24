# Explanation Unit Map (Step 3) — સ્વરૂપ → how the text is cut into teaching blocks

The સ્વરૂપ decides the **explanation unit**: the natural chunk of text that becomes one teaching
topic. This is how Agent 2 cuts the chapter and what `original_chunk` holds per topic. Cutting a
વાર્તા by ઘટના but a ગીત by કડી is the whole point — **do not use one template for all.**

The GSEB readers carry **no text layer**: the unit is read off the **rendered page**, and the page
hands you most of the cut (refrain shorthand, `દૃશ્ય એક :` labels, numbered person-sections,
two-column verse). Read the layout before deciding the unit.

## પદ્ય — verse

One row per profile file in `profiles/genres/`; the unit named here is the unit that file's
"Explanation unit" section defines, and `profiles/genres/_genre_index.md` is the routing authority.

| સ્વરૂપ (profile slug) | Explanation unit | One topic = | Notes |
|---|---|---|---|
| **ઊર્મિકાવ્ય / ગીત** (`urmikavya_geet`) | **કડી-wise** | one કડી | the verse fallback; holds કૂચગીત, બાળગીત, પ્રકૃતિગીત, વિદાયગીત. Keep line breaks and the printed refrain-shorthand exactly as set (std-6 ch 1 `- એક જ.`, std-7 ch 5 `- હો ભેરુ.`) |
| **લોકગીત / લગ્નગીત** (`lok_geet`) | **કડી- / રાઉન્ડ-wise** | one કડી, or one refrain-round where the song cycles | std-8 ch 7 કંકોતરી cycles કાકા → મામા → માસી on an identical refrain: the **round** is the unit; std-6 ch 4 આવ્યો મેહુલો, std-9 ch 20 હરિ ! આવોને, std-10 ch 13 ક્યાં રે વાગી |
| **પ્રાર્થનાકાવ્ય** (`prarthana_kavita`) | **કડી-wise** | one કડી of the petition, with the ધ્રુવપંક્તિ quoted inside it | never cut between the asking and what is asked for (std-10 ch 4 જીવન અંજલિ થાજો, ધ્રુવપંક્તિ "મારું જીવન અંજલિ થાજો !"; std-8 ch 1 જીવનજ્યોત) |
| **પદ / ભજન** (`pad_bhajan`) | **પદ-wise** | **one પદ — the whole sung utterance** | never split by line; ટેક quoted inside the topic, છાપ line stays (std-10 ch 1 મોરલી) |
| **દુહો / છપ્પો / મુક્તક / હાઈકુ** (`duha_chhappa`) | **piece-wise** | **one printed piece, complete in itself** | never merge two pieces into one topic, however short (std-9 ch 22 and std-10 ch 18 લઘુકાવ્યો; std-9 ch 1 છપ્પા). A compiled શ્લોક/પદ-સંચય is the same shape: std-8 P4 વિવિધા ભારતી prints four traditions' verse in Devanagari with a Gujarati સમજૂતી under each — one piece, one topic, the printed script kept |
| **ગઝલ** (`gazal`) | **શેર-wise** | one શેર (two lines, one complete turn) | the રદીફ returns every શેર and is not a ટેક; the મક્તા carrying the છાપ is its own topic (std-8 ch 10 હલેસે હલેસે, છાપ 'આદિલ'; std-9 ch 14 મારું તારું !; std-10 ch 15 તે બેસે અહીં) |
| **સૉનેટ** (`sonnet`) | **ભાવ-ખંડ-wise** | one movement — two to four in a chapter; all fourteen lines where the poem is one unbroken move | never couplet-wise: std-10 ch 7 જીવમાં જીવ આવ્યો sets fourteen મંદાક્રાન્તા lines as seven couplets and is still one argument. The closing ચોટ is never split and never buried (std-9 ch 8 આભાર) |
| **કથાકાવ્ય / કથાગીત** (`kathakavya`) | **ઘટના-wise, cut at a printed કડી boundary** | one વાર્તા-પગલું, ending where the કડી ends | two grains at once: cut like a વાર્તા, teach like verse (પ્રાસ, લય). std-6 ch 10 સાથી મારે બાર, std-7 ch 11 અંધેરી નગરી |
| **અછાંદસ / મુક્ત છંદ** (`mukt_chhand_kavita`) | **વિચાર-એકમ-wise** | one thought-block between the printed line-gaps | no કડી to count — the white space is the boundary (std-9 ch 10 એ લોકો, std-10 ch 11 દીવાનખાનામાં) |
| **ઉખાણું / શબ્દરમત** (`ukhanu_ramatgeet`) | **piece-wise** | one ઉખાણું; a list-shaped શબ્દરમત set is ONE topic, not eight | the answer never leaves the recall answer (std-6 P1 item 4 ચતુર કરો વિચાર !, seven riddles each closed by an empty answer-box) |

## ગદ્ય અને નાટ્ય — prose and drama

| સ્વરૂપ (profile slug) | Explanation unit | One topic = | Notes |
|---|---|---|---|
| **વાર્તા / લઘુકથા / લોકકથા** (`varta`) | **ઘટના-wise** | one plot beat | follow the story's turns, not paragraph counts (std-6 ch 2 ચોટડૂક, std-7 ch 2 ત્રણ સવાલ, std-10 ch 2 શરણાઈના સૂર; a લઘુકથા like std-10 ch 17 ટિફિન or std-9 ch 12 તો જાણું may hold only two or three beats in all). A લોકકથા keeps its dialect as printed and gets it explained (std-7 ch 8 સાદ વરત્યો, std-10 ch 14 જેઠીબાઈ) |
| **સંવાદ-નિબંધ / વિચારપ્રધાન નિબંધ** (`samvad_nibandh`) | **argument-move-wise** | one move of the argument — objecting, conceding, giving evidence, asking | an essay strand is a move and a સંવાદ exchange is a move; never cut mid-exchange, and keep both speakers' words verbatim with their labels (std-6 ch 3 બાણ તો ત્યારે જ છૂટશે..., std-6 ch 14 એક છોકરો રિસાણો, std-9 P4 જન્મી રહેલા બાળક…; std-9 ch 6 ભાષા જાય તો સંસ્કૃતિ જાય, std-8 P2 જીવનમાં વ્યવસ્થિતતા) |
| **નાટક / એકાંકી** (`natak_ekanki`) | **stage-beat-wise** | one beat: an entrance or exit, an object or sound arriving, a change in what a character knows or wants | the પાત્રો list + opening scene-note is its own topic; stage directions in કૌંસ are TEXT, kept inside `original_chunk` (std-7 ch 14 વીર ભામાશા, std-8 ch 12 ક્ષિતિ, std-9 ch 9 પારખું, std-10 ch 12 ઝબક જ્યોત) |
| **ચરિત્ર / રેખાચિત્ર / પ્રસંગકથા** (`charitra_prasang`) | **જીવન-પ્રસંગ-wise** | one episode, or one printed person-section | std-10 ch 5 શ્વેતક્રાંતિના પ્રણેતાઓ prints `(1) ત્રિભુવનદાસ પટેલ` — the section headings ARE the cut; medieval verse quoted inside the prose (std-8 ch 6 પીડ પરાઈ જાણે રે !) stays inside its prose topic, it does not become a પદ topic |
| **આત્મપરક / લલિત નિબંધ** (`nibandh_atmaparak`) | **પ્રસંગ-wise, અથવા વિચારના વળાંક-wise** | one remembered episode, or one turn of the essay's thought | holds સંસ્મરણ, આત્મકથાખંડ, લલિતનિબંધ and the હાસ્ય sub-form. A memoir moves by memory, not by clock (std-8 ch 11 જામફળ અને જલેબી, std-6 ch 15 લો, પાથરી મારી વાત, std-9 ch 17 છબિ ભીતરની, std-9 ch 21 પ્રાણીઓનું ગોકુળ). In the હાસ્ય sub-form the unit is the **comic turn** — never cut a joke from its setup: std-7 ch 6 જો કરી જાંબુએ repeats one temptation down a chain of couriers and each courier is one topic (std-8 ch 3 મારી વ્યાયામસાધના, std-9 ch 2 પરોપકારી મનુષ્યો, std-10 ch 8 સૂરજ તો બધે જ સરખો). std-8 ch 5 બાનો વાડો is a **લલિતનિબંધ** by its own intro box and is cut here, not તર્ક-wise |
| **માહિતીપ્રદ / સાંસ્કૃતિક ગદ્ય** (`mahitiprad_gadya`) | **માહિતી-ખંડ-wise** | one fact, custom or practice | the prose wraps a fact; the fact is the topic. When the information is carried by talking characters, cut by the **fact-step**, not by speaker (std-7 ch 4 ટીપાંની સફર walks the જલચક્ર; std-6 ch 9 ગરવી ગુજરાતનો ગરબો, std-6 ch 12 અજબગજબનો મેળો, std-8 ch 9 શતરંગી ભારત). The માર્ગદર્શક લેખ sub-form keeps the printed step order and the second-person address (std-7 P1 ચાલો, નિબંધ લખીએ...) |
| **પત્ર / પ્રવાસ** (`patra_pravas`) | **પડાવ-wise** | one place the traveller stops at, or one matter the letter turns to | never reorder the journey and never drop the salutation or the sign-off. A place is a પડાવ (std-7 ch 15 સોનાનો કિલ્લો, std-8 P3 સોમનાથ, સાસણ ને સાવજ !, std-6 P1 કચ્છ નહિ દેખા તો કુછ નહિ દેખા !) and a પત્રખંડ is a પડાવ (std-6 ch 8 મામાનો પત્ર, whose ચરિત્ર-પ્રસંગ sits **inside** a letter frame that is not removable) |

**Roster status (VERIFY-3, closed).** These seventeen rows are built from **all five** measured
corpus inventories (`reference/corpus/std-6_inventory.md` … `std-10_inventory.md`), every unit read
off a rendered page. One row per profile file, checked in both directions against
`profiles/genres/_genre_index.md` by `check_pack.py`. A profile exists only for a form the corpus
actually contains (delete-don't-stub) — which is why લોકકથા, સંસ્મરણ, હાસ્યલેખ, હાઈકુ, પ્રવાસવર્ણન and
પત્ર have no rows of their own: they are sub-forms, held by the profile named beside them in the
index's fold table. The rows are still **priors**: Agent 1 decides the unit from the rendered page,
never from this table.

## The two units English has no name for

**દુહો.** A દુહો is a complete poem in two lines — a self-contained thought with its own picture and
its own turn. Line one puts something ordinary in front of you, line two turns it into a rule:
`"કડવા હોય લીમડા, પણ શીતલ એની છાંય"` (std-10 ch 18) is finished where it stops; nothing before or
after it is needed. A લઘુકાવ્યો chapter that prints દુહા, મુક્તક and હાઈકુ under one chapter number
is a *collection* of independent poems sharing a page, not one poem in stanzas. Treating it
"stanza-wise" the way an English pack would fuses poems that share nothing but a page. **One દુહો =
one topic, always**, even when it is shorter than the explanation that follows it. The same holds
for a છપ્પો and for a મુક્તક — and for the seed દુહો a revision block quotes (std-8 R1:
`"સિદ્ધિ તેને જઈ વરે જે, પરસેવે ન્હાય."`), which is a whole poem even inside an exercise.

**પદ.** A પદ is one devotional song, sung through as one utterance to one listener. Splitting it by
line breaks the utterance. મીરાંનું **મોરલી** (std-10 ch 1) is one address to કૃષ્ણ from its first
line to its છાપ — `"બાઈ મીરાં કે પ્રભુ ગિરિધરના ગુણ, દર્શન થકી દુઃખ ભાંગે છે."` — and the
refrain-cue `વૃંદાવન.` set to the right of every line is the સૂર the whole song hangs on, not a
division in it. **One પદ = one topic**, even when it runs longer than a કડી. The ટેક is quoted
inside that topic and is never a topic of its own; the છાપ is part of the verse, not an attribution;
the printed `— કવિનું નામ` line belongs inside the LAST topic's `original_chunk`.

## Hard rules for cutting (Agent 2 + Agent 5)

1. **Exact text first.** Every topic carries the verbatim Gujarati-script passage in `original_chunk`,
   **transcribed from the rendered page** (the PDFs are image-only). Nothing dropped, paraphrased, or
   transliterated; માત્રા, અનુસ્વાર, ચંદ્રબિંદુ and જોડાક્ષર exactly as printed; `.` as printed,
   never `।` (`gujarati_verbatim.md`).
2. **A pre-topic hook belongs to the NEXT topic.** A line that introduces the next કડી or the next
   ઘટના opens *that* topic, not the tail of the previous one.
3. **Single-theme topics.** One કડી / દુહો / પદ / ઘટના per topic. If a કડી does two clearly
   different things it may split; if two very short કડી do one thing they may join — decide from
   the content, and **never for દુહો or પદ**.
4. **Topics are reading scenes + pre-reading only; સ્વાધ્યાય is NOT a topic.** The exercise
   apparatus — std 6–8's numbered blocks (**વાતચીત** always first, **નીચેના પ્રશ્નોના જવાબ લખો**,
   **ખાલી જગ્યા પૂરો**, **જોડકાં જોડો**, **ઉદાહરણ મુજબ…**, **નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં
   અનુવાદ કરો**, **પ્રવૃત્તિ**, **ચર્ચા-વિચારણા**) and std 10's printed **સ્વાધ્યાય** banner with
   its four-tier ladder (✓-વિકલ્પ → એક-એક વાક્યમાં → બે-ત્રણ વાક્યમાં → સવિસ્તર) plus
   **વિદ્યાર્થી-પ્રવૃત્તિ**, **ભાષા-અભિવ્યક્તિ** and **શિક્ષકની ભૂમિકા** — is handled solely by
   Agent 10 in `exercise_solutions.json`, mapped to the reading scenes that prepare it. The exact
   printed headings come from Agent 1's `exercise_inventory`, per chapter, never assumed from this
   list. Cutting any of them as a topic is a hard fail. Three consequences worth stating:
   - **Apparatus is not a reading scene.** The blue intro box, the શબ્દાર્થ box, the રૂઢિપ્રયોગ /
     કહેવત pre-blocks and the chapter-final green grammar box (`સંજ્ઞા વિશે જાણીએ`,
     `ક્રિયાવિશેષણ`, `વિરામચિહ્નો`…) are teacher-addressed matter: they feed `key_terms`,
     ભાષા-બોધ and Agent 10 — not topics. Prose printed **for the student** does become a CONCEPT
     topic: std 10 opens each chapter with an unlabeled કવિ/લેખક-પરિચય + કૃતિ-પરિચય paragraph.
   - **Appended reading matter is reading matter, but not part of this chapter's unit chain.** The
     "ગાઈએ" box carrying a whole second poem (std-6 ch 4, ત્રિભુવન વ્યાસનું 'મેહુલો'), poems by
     other poets quoted inside exercises (std-8 ch 10), the second play-text embedded in an exercise
     (std-8 ch 12, પાટણ દરબાર) — never fold these into the chapter's કડી or ઘટના chain.
   - **Whole units carry no reading text at all.** The revision checkpoints (**આગળ વધતાં પહેલાં**,
     **પૂર્ણ કરતાં પહેલાં**) and std 9–10's **વ્યાકરણ એકમો** are exercise-only: no topics, Agent 10
     territory end to end.
5. **The ટેક (refrain) is content, not repetition to skip.** Where a ટેક returns with **changed
   words**, each occurrence is its own topic and the teaching names *what changed*. Where a ટેક
   returns **identical**, teach it at first occurrence and reference it afterwards — this is the
   measured common case in these readers (std-6 ch 1 `- એક જ.`, std-7 ch 1 "વિભુ હશે તો કેવા સુંદર,
   એવું થાતું મુજ મનમાં", std-7 ch 5 `- હો ભેરુ.`, std-10 ch 4 "મારું જીવન અંજલિ થાજો !",
   std-10 ch 13 `– સમી સાંજની`). Two riders:
   - **The printed shorthand is verbatim.** GSEB verse abbreviates a returning refrain to an
     ellipsis form (`- એક જ.`, `આવ્યો...`, `... કંકોતરી...`, `– સમી સાંજની` set to the right of the
     line). Copy it into `original_chunk` exactly as printed; expanding it to the full refrain line
     is composing, and Agent 5 rejects it.
   - **A changed-words ટેક is measured, and it is a topic at each occurrence.** std-9 ch 3
     જ્યાં જ્યાં વસે એક ગુજરાતી opens `જ્યાં જ્યાં વસે એક ગુજરાતી / ત્યાં ત્યાં સદાકાળ ગુજરાત`, returns
     as `જ્યાં જ્યાં બોલાતી ગુજરાતી / ત્યાં ત્યાં ગુર્જરીની મહોલાત`, then weaves the lines into the
     closing જયઘોષ; std-7 P2 સમજણ તે આપણા બેની re-shapes its refrain with the shared thing's gender
     (`…તે આપણા બેનો` → `…તે આપણા બેનું` → `…તે આપણા બેની`). Each return is a new claim: teach **what
     changed** (`profiles/genres/urmikavya_geet.md`).

## What the rendered page tells you about the unit

- **Refrain shorthand** marks the કડી boundary — the કડી ends where the ellipsis-refrain sits.
- **Two-column verse** (std-6 ch 7 ચોખ્ખાઈના સરદાર; std-6 P1 રંગ રંગ વાદળિયાં, with a printed
  divider rule) is read **down each column, never across**. A cut made across the columns produces
  topics that are not poems.
- **Printed labels hand you the cut for free:** `દૃશ્ય એક :` … `દૃશ્ય પાંચ :` (std-8 ch 14, five
  ઘટના), `પાત્રો :` and `(પડદો પડે છે)` in an એકાંકી, `(1) ત્રિભુવનદાસ પટેલ` in a રેખાચિત્ર.
- **Header furniture is not text:** the chapter-number box, the QR badge and its Latin code string,
  running footers. They never enter `original_chunk`.
- **Mixed chapters** (an anthology page; verse quoted inside a ચરિત્ર; a science fact carried by
  dialogue) route to `genre: "mixed"`, dominant-first: each part is cut under **its own** unit.

## topic_type
- `POEM` — a કડી / દુહો / પદ / શેર being read and explained.
- `STORY_TELLING` — a narrative ઘટના or a remembered સ્મૃતિ.
- `CONCEPT` — pre-reading, a taught idea, a fact, a કવિ-પરિચય / લેખક-પરિચય printed for the student.
- `REVIEW` — an in-text summary or value wrap. (સ્વાધ્યાય is never a topic.)

These are the **authored** values, used by Agents 02–13. At emit, Agent 14/15 map them to the closed
server enum: POEM / STORY_TELLING / CONCEPT → `instructional`, REVIEW → `summary`,
EXERCISE → `assessment`.

`topic_category` is a finer descriptive label: `introduction` / `core` / `climax` / `transition` /
`resolution` — descriptive, never a number.
