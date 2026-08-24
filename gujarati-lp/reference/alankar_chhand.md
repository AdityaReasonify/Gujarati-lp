# અલંકાર અને છંદ — the craft analysis (કાવ્ય topics only)

Fills the topic-level `figures_of_speech[]` and `rhyme_scheme`, and the module-level
`difficult_words[]` and `overall_rhyme_scheme`. For ગદ્ય these are `[]` / `null`, except that a
genuine અલંકાર in prose may still be listed — GSEB's own ભાષા-અભિવ્યક્તિ box does exactly that
(std 10, પ્રાણનો મિત્ર: `ઝાડ નિર્લજ્જની જેમ ખૂબ વધી ગયું`).

> **The one rule that outranks the rest: never invent an અલંકાર to fill the field.** If a કડી has
> none, `figures_of_speech` is `[]`. A named device that is not in the lines is a hard fail at
> Agent 13 — it teaches the child something untrue about the text.

> **The second rule, specific to GSEB: do not name a device the child's standard has not been
> taught.** GSEB Gujarati (દ્વિતીય ભાષા) starts named-device identification at **std 9**. Std 6–8
> children meet અલંકાર in the text and never in a label. Naming one early is not "extra value" —
> it is off-syllabus vocabulary dropped on an L2 reader.

## The grade gate — notice at 6–8, name at 9–10

| ધોરણ | What the child does with craft | What the JSON carries | GSEB evidence |
|---|---|---|---|
| 6–7 | **hears** it: પ્રાસ, લય, ટેક, repeated sounds | `figures_of_speech: []`; `rhyme_scheme` filled | std 6 intro box: `પ્રાસયુક્ત શબ્દોથી પણ પરિચિત કરવાં`; std 7 સ્વાધ્યાય `નીચેના શબ્દો સાથે પ્રાસવાળા શબ્દો શોધીને લખો.` |
| 8 | hears it + counts pattern as play (હાઈકુ 5-7-5, દુહાની ચાલ) | `figures_of_speech: []`; `rhyme_scheme` filled, pattern named plainly | std 8 સ્વાધ્યાય `સરખા પ્રાસવાળા શબ્દો લખો.`; `કાવ્યમાં વપરાયેલા પ્રાસવાળા શબ્દો શોધીને લખો.` |
| 9 | **names** seven અલંકાર | `figures_of_speech` may carry a `device` from the std-9 canon | std-9 canon (below); ભાષા-અભિવ્યક્તિ boxes pre-name craft (અખાના છપ્પા: વિરોધાભાસનાં પ્રતીકો ઘુવડ-સૂર્ય, હીરો-પથ્થર) |
| 10 | names twelve અલંકાર **and** છંદ | `device` from the std-10 canon; છંદ named in `rhyme_scheme.note` / `overall_rhyme_scheme` | std-10 chapter intro itself names the metre: `તે ભાવને કવિએ આ સોનેટમાં મંદાક્રાન્તા છંદમાં પ્રગટ કર્યો છે` |

**What "notice, don't name" looks like in practice.** At std 6–8 the device still gets taught —
inside `explanation`, in ordinary words, pointing at the line:

> બાળકો, જુઓ — `મેહુલે માંડ્યાં મંડાણ` બોલી જુઓ. `મ` `મ` `મ` — ત્રણેય શબ્દ એક જ અવાજથી શરૂ થાય છે,
> ને એટલે લીટી ઢોલ જેવી સંભળાય છે.

That is the whole teaching. The word **વર્ણાનુપ્રાસ** does not appear, and `figures_of_speech`
stays `[]`. Trying to smuggle the label into `key_terms` or a recall answer is the same violation.

## અલંકાર a reader of THIS standard can actually see

**Std 6–8 — the four an L2 child can genuinely see, taught unnamed.** These are the ones worth
pointing at; the rest are invisible at this age even when present.

| What it does | What to look for | Corpus line |
|---|---|---|
| the same sound returning | નજીક નજીકના શબ્દોમાં એક જ ધ્વનિ | std 6 વરસાદ-ગીત: `મેહુલે માંડ્યાં મંડાણ`, `ધોરીએ લીધાં ધુરી-ધોંસરી` |
| a thing behaving like a person | નિર્જીવ કે પ્રાણી માણસનું કામ કરે | std 6: `ડેડકડી દિયે આશિષ` |
| one thing called another | સરખામણીનો શબ્દ વગર જ `આ તે આ છે` | std 6: `આવ્યો ધરતીનો ધણી મેહુલો રે !` |
| a sound-word invented for the ear | અર્થ કરતાં અવાજ મોટો | std 7 રાસ-ગીત: `અલ્લક દલ્લક, ઝાંઝરઝલ્લક`, `ઢમ્મક ઢમ્મક` |

**Std 9 — the seven named અલંકાર.** Name only from this list; anything outside it is off-syllabus.

| અલંકાર | The tell on the line |
|---|---|
| **વર્ણાનુપ્રાસ** | એક જ વર્ણ નજીકના શબ્દોમાં પાછો આવે |
| **પ્રાસસાંકળી** | એક લીટીનો છેડો બીજી લીટીના આરંભ સાથે સાંકળે |
| **ઉપમા** | સરખામણીનો શબ્દ છપાયેલો છે — `જેવું`, `સમાન`, `પેઠે`, `-શું` |
| **રૂપક** | સરખામણીનો શબ્દ નથી; ઉપમેય **જ** ઉપમાન બની જાય |
| **ઉત્પ્રેક્ષા** | `જાણે` / `શું` — કવિ કલ્પના કરે કે એક વસ્તુ બીજી હોય |
| **વ્યતિરેક** | ઉપમેયને ઉપમાનથી **ચડિયાતું** કહેવાય |
| **અતિશયોક્તિ** | વાત બની શકે એથી આગળ વધારીને કહેવાય |

**Std 10 — the same seven plus five.** (GSEB std-10 count: ૪ શબ્દાલંકાર + ૮ અર્થાલંકાર.)

| અલંકાર | The tell on the line |
|---|---|
| **યમક** | એક જ શબ્દ પાછો આવે, પણ દરેક વખતે જુદા અર્થમાં |
| **શ્લેષ** | એક જ શબ્દ એક સાથે બે અર્થ ઊંચકે |
| **અનન્વય** | ઉપમાન મળે જ નહિ — `એના જેવું તો એ જ` |
| **વ્યાજસ્તુતિ** | વખાણમાં નિંદા, કે નિંદામાં વખાણ |
| **સજીવારોપણ** (personification) | નિર્જીવને લાગણી કે માણસનું વર્તન અપાય |

**The marker is a clue, not a verdict.** `જેમ` in `ઝાડ નિર્લજ્જની જેમ ખૂબ વધી ગયું` looks like
ઉપમા, but what the line actually does is give a tree a person's shamelessness — the book's own
ભાષા-અભિવ્યક્તિ box reads it as સજીવારોપણ. Read the line, then choose. If two labels are both
arguable and the printed page does not settle it, write `[]` and teach the effect in `explanation`.

**L2 adjustment.** A comparison only lands if the child knows **both** sides of it. Before naming
an ઉપમા or રૂપક, check that the ઉપમાન is glossed — `ધણી`, `નિર્લજ્જ`, `વજોગણ` are not free words
for a second-language reader. Gloss at point of use (`shabd_gloss.md`), then name the device.

Entry shape — quote the **exact words from this કડી**, never a paraphrase:

```json
{"device": "સજીવારોપણ", "lines": "ઝાડ નિર્લજ્જની જેમ ખૂબ વધી ગયું",
 "note": "ઝાડને શરમ હોય જ નહિ, છતાં લેખક એને નિર્લજ્જ કહે છે — ઝાડ જાણે માણસ બની જાય છે."}
```

Agent 13 searches `lines` inside that topic's `original_chunk` byte for byte. A tidied-up quote,
a joined line-break, or a `.` you added is a failed check.

## છંદ, લય અને પ્રાસ

`rhyme_scheme` per કાવ્ય topic:

```json
{"pattern": "AAB, પછી ટેક", "rhyming_words": ["ઊંચે — નીચે"],
 "note": "કડીની પહેલી બે લીટીના છેડા સરખા સંભળાય છે, ને પછી ટેક પાછી આવે છે — ગાવામાં ઝૂલો બેસે છે."}
```

- Name the **પ્રાસ** honestly. A near-rhyme is a near-rhyme — say so in the `note`:
  `રાજા — ખાજાં` (std 7, અંધેર નગરી) is not an exact match; the anusvāra differs, and the note
  should say the ear accepts it even though the letters do not.
- **અછાંદસ / મુક્ત પંક્તિ** is a real answer, not a failure: std 10 `દીવાનખાનામાં` and
  `હાથ મેળવીએ` have no repeating pattern. Write `{"pattern": "અછાંદસ", "rhyming_words": [], "note": …}`
  and say in the note that the poet drops પ્રાસ deliberately. `null` is for ગદ્ય.
- **ટેક / ધ્રુવપંક્તિ** is described, not scanned. Quote it once, say what returning does:
  std 6 `એક જ ડાળનાં પંખી, / અમે સહુ એક જ ડાળનાં પંખી.`; std 7 `વિભુ હશે તો કેવા સુંદર, એવું થાતું મુજ
  મનમાં`; std 10 `મારું જીવન અંજલિ થાજો !`. Where the page prints a shorthand repeat marker
  (`- એક જ.`, `- હો ભેરુ.`, `– સમી સાંજની`), that marker is verbatim text — copy it, do not expand it.
- **છંદ is std-10 only.** Below std 10 do not name a છંદ even when you can recognise it. At std 10
  the ten in scope are ૭ અક્ષરમેળ (અનુષ્ટુપ, ઇન્દ્રવજ્રા, ઉપજાતિ, વંશસ્થ, મંદાક્રાન્તા, શિખરિણી,
  હરિણી) and ૩ માત્રામેળ (દોહરો, સોરઠો, ચોપાઈ).
- **Never write a માત્રા or અક્ષર count this pack has not verified.** Model-recalled Gujarati
  prosody is unreliable and two source discrepancies are already on record (મંદાક્રાન્તા 17 vs 14,
  હરિણી 17 vs 16). Two sources are admissible: the chapter's own printed intro
  (`…આ સોનેટમાં મંદાક્રાન્તા છંદમાં…`) and a human-verified registry. Absent both, name the શેપ the
  child can see — line count, where the તુક falls — and stop.

## Gujarati form facts — say each once, at module level

| સ્વરૂપ | What the page shows | Say once in `overall_rhyme_scheme` | Corpus witness |
|---|---|---|---|
| **દુહો / દોહરો** | બે છપાયેલી લીટી, ચાર ચરણ; તુક લીટીના છેડે | એક દુહો = આખી એક વાત; પહેલી લીટીનું ચિત્ર, બીજી લીટીની શિખામણ | std 10 ch-18 `કડવા હોય લીમડા, પણ શીતલ એની છાંય`; std 8 R1 `સિદ્ધિ તેને જઈ વરે જે, પરસેવે ન્હાય.` |
| **સોરઠો** | દુહાનું ઊલટું — તુક પહેલા/ત્રીજા ચરણને છેડે | દુહાની ભાઈબંધ ચાલ, પણ તુકની જગ્યા ફરી જાય છે | *not yet witnessed in this corpus — provisional* |
| **ચોપાઈ** | ચાર સરખાં ચરણ, ચાલતી કથાની ચાલ | વારતા આગળ ચલાવવા માટેનો છંદ | *not yet witnessed in this corpus — provisional* |
| **છપ્પો** | છ પંક્તિનું કટાક્ષ-કાવ્ય; છાપ પંક્તિની અંદર | એક છપ્પો = એક પૂરી દલીલ, છેલ્લે ચોટ | std 9 ch-01 અખાના છપ્પા (પાઠમાં ૩ અને ૪ પંક્તિના અંશ છપાયા છે — જે છપાયું છે તે જ સાચું) |
| **ઝૂલણા** | લાંબી લીટી, ગાવામાં ઝૂલો | ગાવા માટે બંધાયેલો છંદ | *not yet witnessed in this corpus — provisional* |
| **ગઝલ** | શેર (બે-બે લીટીના સ્વતંત્ર એકમ); દરેક શેરને છેડે એક જ **રદીફ**; છેલ્લા શેર(મક્તા)માં કવિની **છાપ** | દરેક શેર પોતાની રીતે પૂરો; રદીફ પાછી આવે એ જ ગઝલની ચાલ | std 8 ch-10 રદીફ `દરિયો`, મક્તા `તમે જાળ નાખ્યા કરો રોજ 'આદિલ', પરંતુ કદીયે ન પકડાય દરિયો.`; std 10 ch-15 રદીફ `તે બેસે અહીં` |
| **ગીત / પદ** | ટેક (ધ્રુવપંક્તિ) + કડી; ગાવા માટે | ટેક દરેક કડી પછી પાછી આવે છે — એ જ ગીતનો ધબકાર | std 7 `હો ભેરુ મારા, આપણે ભરોસે આપણે હાલીએ...`; std 10 લોકગીત `સમી સાંજની જી રે, વજોગણ ક્યાં રે વાગી !` |

The poet's **છાપ** is verse, never a label: `બાઈ મીરાં કે પ્રભુ ગિરિધરના ગુણ, દર્શન થકી દુઃખ ભાંગે
છે.` stays inside `original_chunk` (`gujarati_verbatim.md`). Name it in `explanation` as the poet
signing the song — do not list it as an અલંકાર.

## કાવ્ય-રૂપ — poetic licence, not a mistake

Where a કવિ bends a word for લય — `ન્હાય` for `નહાય`, `લો'તાં` for `લૂછતાં`, `છઈએ` for `છીએ` —
that belongs in the topic's `explanation` and in `key_terms`, and it is **કાવ્ય-કલા, not a printing
error**. Say so explicitly; an L2 child will otherwise read it as a mistake and "correct" it in
their own writing. The same holds for medieval and તળપદા forms (`પહાણ`, `સનાન`, `મારગ`, `થૈ`) —
gloss them, never modernise them. The pack-wide rule is in `gujarati_verbatim.md`; this file only
adds that at std 9–10 the licence is often the craft point itself, and may be worth a `note`.

## Module-level closing pair

- **`difficult_words`** — 5–10 words from the whole chapter, each
  `{"word": …, "meaning": <student-friendly, concrete>, "example": <a FRESH everyday sentence, not
  the poem's own line>}`. Lead with words the child will meet again (`shabd_gloss.md`). For an L2
  reader the bar sits lower than a first-language pack's: `ધણી`, `આશિષ`, `મારગ` earn a slot.
- **`overall_rhyme_scheme`** — the whole poem's pattern plus the effect, plus any chapter-wide ટેક,
  plus (std 10 only, and only with a source) the છંદ. This is where the form fact goes **once**.

## How deep to go

Name the અલંકાર, quote the words, say **what it does** in one line. That is the whole job. Do not

- name anything at all below std 9 — at std 6–8 the effect goes in `explanation`, unlabelled;
- list every possible device in a કડી (one or two that genuinely do work);
- write a છંદ-શાસ્ત્ર lecture on માત્રા counting for an L2 reader of any standard;
- state a છંદ or a syllable count from memory — printed intro or verified registry, or nothing;
- keep the label without the effect — `"વર્ણાનુપ્રાસ છે"` alone teaches nothing;
- use a number in display prose: `બીજી કડીમાં`, never `કડી 2માં`.

## Provisional — carries its warning

- **The device ladder above is the measured GSEB scope-and-sequence**, and it supersedes the
  shorthand in PORTING_BRIEF §4.5, which places શ્લેષ/યમક at lower standards and સજીવારોપણ below
  std 9. Measured placement: **std 9** = વર્ણાનુપ્રાસ, પ્રાસસાંકળી, ઉપમા, રૂપક, ઉત્પ્રેક્ષા,
  વ્યતિરેક, અતિશયોક્તિ; **std 10 adds** યમક, શ્લેષ, અનન્વય, વ્યાજસ્તુતિ, સજીવારોપણ.
- **સોરઠો, ચોપાઈ and ઝૂલણા are unwitnessed** in the std 6–10 corpus inventories so far. સોરઠો and
  ચોપાઈ are in the std-10 છંદ canon; ઝૂલણા is not, and appears here only as a form an old પદ may
  turn out to use. Do not build a topic on any of the three until a rendered page shows one.
- **The std-9 inventory has since completed** (31 of 31 — `reference/corpus/std-9_inventory.md`).
  Its ભાષા-અભિવ્યક્તિ boxes pre-name devices beyond the std-9 canon above (યમક, સજીવારોપણ,
  વક્રોક્તિ, વિરોધાભાસ appear in std-9 chapter apparatus). Those boxes are teacher-facing
  evidence, not licence: the child-facing ladder above stands, and a device the box names is
  still only written into `figures_of_speech` when it sits inside this standard's canon AND is
  verified on the chapter's own lines. Reconciling the ladder against the completed inventory is
  an open VERIFY-4-class review item.
- **All માત્રા/અક્ષર counts are registry-gated** pending a human-verified prosody registry
  (PEDAGOGY: two discrepancies already logged). Until it exists, this file states no count.
