# Teaching Lens Map (Step 2) — સ્વરૂપ → the lens that teaches it

The **lens** is the question the whole chapter is taught through. It is set once at Agent 1 from
the diagnosed સ્વરૂપ, recorded in `01_meta.json` as `teaching_lens` + `guiding_question`, and every
`explanation` afterwards serves it.

A Gujarati (દ્વિતીય ભાષા) plan carries **two** lenses at once. The literary lens is the one above —
what this form does and how the child is to read it. Alongside it runs a **ભાષા-લક્ષ્ય**: the
vocabulary and usage this form naturally teaches an L2 reader. Appreciation and acquisition are
taught in the same breath, never as two separate lessons; the fourth column of each table below is
the second lens, not an optional extra.

## પદ્ય

One row per profile file in `profiles/genres/`; the **Lens** column is the formula printed in that
file and in `profiles/genres/_genre_index.md`'s master table, and it is stated in exactly those terms.

| સ્વરૂપ (profile) | Lens | Guiding question (the engine) | ભાષા-લક્ષ્ય (L2) |
|---|---|---|---|
| **ઊર્મિકાવ્ય / ગીત** (`urmikavya_geet` — verse fallback; holds કૂચગીત, બાળગીત, પ્રકૃતિગીત, વિદાયગીત) | ચિત્ર + ભાવ + લય | *કવિ કયાં ચિત્રો બતાવીને આ ભાવ જગાડે છે?* | ચિત્ર-શબ્દો (રંગ, ધ્વનિ, વિશેષણ); ટેકની પુનરાવૃત્તિ બોલવા-ગાવામાં |
| **પ્રાર્થના-કાવ્ય / પ્રાર્થનાગીત** (`prarthana_kavita`) | યાચના + સંબોધન + આત્મબળ | *કવિ પ્રભુ પાસે શું માગે છે — અને એ માગણી કવિ પોતાના વિશે શું કહી જાય છે?* | આજ્ઞાર્થ-પ્રાર્થનાનાં રૂપો (થાજો, દેજો); સંબોધન; વણ- privative જોડ (વણદીવે, વણજહાજે) |
| **ભક્તિ-પદ / ભજન** (`pad_bhajan`) | ભાવ + સંબંધ + લોકભાષાની મીઠાશ | *ભક્ત અને ભગવાન વચ્ચેનો આ સંબંધ કેવો છે?* | મધ્યકાલીન/તળપદાં રૂપો ઓળખવાં — સુધારવાં નહિ; છાપ-પંક્તિ વાંચતાં આવડવું |
| **દુહો / છપ્પો / મુક્તક / હાઈકુ / શ્લોક-સંચય** (`duha_chhappa`) | અનુભવની શિખામણ + દૃષ્ટાંત | *કવિ રોજિંદા જીવનના કયા દૃશ્યથી જીવનની વાત કહે છે?* | કહેવત-જેવી ટૂંકી વાક્યરચના; વિરોધી જોડ (કડવા ↔ શીતલ); કટાક્ષનો સૂર પકડવો (અખાના છપ્પા) |
| **લોકગીત** (`lok_geet`) | કંઠ + ધ્રુવપંક્તિ + લોકજીવન | *આ ગીત કયા પ્રસંગે, કોણ, અને કેમ ગાય છે?* | તળપદા શબ્દો (વજોગણ, સૈયર); પૂરક ઉચ્ચાર-ટુકડા ("જી રે") ઓળખવા |
| **કથાકાવ્ય / કથાગીત** (`kathakavya`) | ઘટના + પાત્ર + વળાંક | *આ કડીઓમાં શું બન્યું, અને એ કોણ કહે છે?* | ઘટના-ક્રમના જોડાણ-શબ્દો (પછી, ત્યારે, આખરે); ભૂતકાળનાં ક્રિયાપદ |
| **ગઝલ** (`gazal`) | શેર + રદીફ-કાફિયા + મિજાજ | *દરેક શેર પોતાની રીતે કઈ એક વાત પૂરી કરે છે?* | રદીફની પુનરાવૃત્તિથી વાક્યભાત; આગત (ફારસી-અરબી) શબ્દો |
| **સૉનેટ** (`sonnet`) | બંધ + વળાંક + ભાવની ઘનતા | *ચૌદ પંક્તિમાં ભાવ ક્યાં વળાંક લે છે?* | તત્સમ શબ્દભંડોળ; લાંબા વાક્યને પંક્તિઓમાં પકડવું |
| **અછાંદસ / મુક્તછંદ** (`mukt_chhand_kavita`) | ચિત્ર + મૌન + પંક્તિ-ભંગ | *પંક્તિ અહીં જ કેમ તૂટે છે?* | બોલચાલની ગુજરાતી કાવ્યમાં; આગત અંગ્રેજી શબ્દોનું મિશ્રણ |
| **ઉખાણું / શબ્દરમત / રમતગીત** (`ukhanu_ramatgeet`) | સંકેત + રમત + અનુમાન | *આ ઉખાણું શું છુપાવે છે, અને કઈ ચાવી આપણને એની નજીક લઈ જાય છે?* | વસ્તુ-વર્ણનનાં વિશેષણ; અનુમાનની ભાષા (હશે, લાગે છે); ધ્વનિ-રમત |

**Why the ઊર્મિકાવ્ય row says લય where the profile says અલંકાર.** `urmikavya_geet.md` and the index
print the lens as **ચિત્ર + ભાવ + અલંકાર**; in a sung ગીત the craft usually reaches the child through
the ear first, so લય and પ્રાસ occupy that same third slot. Both wordings name the same third term —
*the craft this કડી actually carries* — and the profile records the difference deliberately. Name
whichever of the three is present; never all three by habit.

## ગદ્ય અને નાટ્ય

| સ્વરૂપ (profile) | Lens | Guiding question (the engine) | ભાષા-લક્ષ્ય (L2) |
|---|---|---|---|
| **વાર્તા** (`varta` — ટૂંકીવાર્તા, લઘુકથા, લોકકથા, પૌરાણિક કથા, દૃષ્ટાંતકથા, પ્રાણીકથા, નવલકથાખંડ) | ઘટના + પાત્ર + વળાંક | *પાત્રની કઈ પસંદગી વાર્તાને વળાંક આપે છે?* | ભૂતકાળનાં ક્રિયાપદ; સંવાદમાં સંબોધન; ક્રમ-જોડાણ શબ્દો; લોકકથામાં પ્રાદેશિક તળપદાં રૂપો (સૌરાષ્ટ્રી, કચ્છી) અને રૂઢિપ્રયોગ |
| **ચરિત્ર / રેખાચિત્ર / પ્રસંગકથા** (`charitra_prasang`) | પ્રસંગ + સ્વભાવ + મૂલ્ય | *કયા પ્રસંગોએ આ વ્યક્તિને યાદ રાખવા જેવી બનાવી?* | વિશેષણથી સ્વભાવ વર્ણવવો; વ્યવસાય-શબ્દો; તારીખ-સ્થળ-સન્માનની ભાષા |
| **આત્મપરક / લલિત નિબંધ** (`nibandh_atmaparak` — સંસ્મરણ, આત્મકથાખંડ, હાસ્યનિબંધ, હાસ્યલેખ, અનુભવકથા) | સ્વર + પ્રસંગ + પોતાની જાત પરની નજર | *લેખક પોતાની જ વાત કરતાં કરતાં પોતાના વિશે શું કબૂલી લે છે?* | પ્રથમ પુરુષ એકવચન; ભૂતકાળ ↔ વર્તમાનનો ફેરબદલ; બોલચાલનાં સંબોધનો અને રૂઢિપ્રયોગ; અતિશયોક્તિની ભાત (હાસ્યમાં) |
| **પત્ર / પ્રવાસ** (`patra_pravas`) | પડાવ + દૃષ્ટિ + સંબોધન | *લખનાર કોને કહે છે, અને એ અહીં જ કેમ થોભે છે?* | પત્રનાં માળખાગત રૂપો (સંબોધન, વિનંતી, સમાપન); આદરવાચક બહુવચન; સ્થળ-દિશા અને માપ-આકારનાં વિશેષણ |
| **સંવાદ-નિબંધ / વિચારપ્રધાન નિબંધ** (`samvad_nibandh`) | તર્ક + દૃષ્ટિકોણ + જવાબદારી | *બંને પક્ષ શું કહે છે, અને એ મારી પાસે શું માગે છે?* | સહમતિ-અસહમતિનાં રૂપો (એ ખરું, પણ…); કારણવાચી જોડાણ (કારણ કે, તેથી, છતાં); મુદ્દાસર લખવાની ભાત |
| **માહિતીપ્રદ / સાંસ્કૃતિક ગદ્ય** (`mahitiprad_gadya` — માર્ગદર્શક લેખ સહિત) | તથ્ય + પરંપરા + જિજ્ઞાસા | *આ પરંપરા કે હકીકત આપણને આપણા દેશ વિશે શું કહે છે?* | વર્ણનાત્મક વર્તમાનકાળ; સંખ્યા-માપના શબ્દો; પારિભાષિક તત્સમ; સૂચનાનો ક્રમ (પહેલાં, પછી, છેલ્લે) |
| **એકાંકી / નાટક** (`natak_ekanki`) | સંવાદ + રંગસૂચના + વળાંક | *જે મંચ પર બતાવી ન શકાય, તે વાત સંવાદ અને રંગસૂચના દ્વારા પ્રેક્ષક સુધી કેવી રીતે પહોંચે છે?* | આજ્ઞાર્થ અને પ્રશ્નાર્થનાં ટૂંકાં વાક્યો; મંચ-શબ્દાવલિ |

**Roster note (VERIFY-3, closed).** These seventeen rows are the whole roster: one row per file in
`profiles/genres/`, checked in both directions against `profiles/genres/_genre_index.md` by
`check_pack.py`. Four rows this file used to carry are gone because the measured corpus folded them:
**સાખી-છપ્પા** collapsed into `duha_chhappa` — std-9 ch 1 છપ્પા (અખો) is measured as દૃષ્ટાંત + કટાક્ષ,
which that profile already holds and gates; **સંસ્મરણ** and **હાસ્યલેખ** collapsed into
`nibandh_atmaparak`, which carries a section for each; **લોકકથા** collapsed into `varta`;
**પ્રવાસવર્ણન** and **પત્ર** merged as `patra_pravas`; **હાઈકુ** landed in `duha_chhappa`; and the
લલિત half of the old નિબંધ row went to `nibandh_atmaparak` while its વિચારપ્રધાન half stayed with
`samvad_nibandh`. The ખંડકાવ્ય row this file once anticipated was never needed: std-9 ch 4
સિંહનું મૃત્યુ is measured as a **નવલકથા-અંશ** in prose, not a narrative poem.

## The second lens — language acquisition

The literary lens says what the chapter means; the ભાષા-લક્ષ્ય says what the child can now *do* with
Gujarati because of it. For an L2 reader the two are not in competition — the words are the way into
the ભાવ, and the ભાવ is what makes the words stick.

- The ભાષા-લક્ષ્ય is **derived from this chapter's own words**, exactly as the guiding question is.
  "તળપદા શબ્દો" is not a ભાષા-લક્ષ્ય; "ગોવાળિયાના જીવનના તળપદા શબ્દો જે આ ગીતમાં આવે છે" is.
- It sets what `key_terms` and the inline glosses in `explanation` prioritise — the words a child will
  meet again, not every hard word on the page (`reference/shabd_gloss.md`).
- It never displaces the literary lens. An explanation that turns into a vocabulary list has lost the
  chapter; an explanation that never glosses has lost the child. Both are failures of the same rule.
- Grammar naming follows the standard, not the lens (`bhasha_bodh.md`). The ભાષા-લક્ષ્ય may be
  "ભૂતકાળનાં ક્રિયાપદ" at std 6 and still be taught without ever saying the word "કાળ".

## Craft-naming gate by standard

The lens formula is the **author's** vocabulary. How much of it reaches the child is fixed by
standard, and the gate is hard:

- **Std 6–8** — the form is *experienced*, never labelled. Teach ચિત્ર, ભાવ, ટેક, ઘટના, વળાંક through
  what happens in the text; do **not** name અલંકાર, છંદ, સમાસ, or the સાહિત્યપ્રકાર itself. A std-7
  explanation may say "કવિ નિર્જીવ વાદળને જીવતું બતાવે છે" — it may not say "સજીવારોપણ".
- **Std 9–10** — naming is the year's work. The પ્રકાર tag, the named અલંકાર set, and (std 10 only)
  છંદ are fair game, always in the order encounter → name → apply, and always from a line quoted out
  of this chapter's `original_chunk`.
- The lens does not change across standards; only its visible vocabulary does. Lowering the lens
  itself ("std 6 doesn't need the વળાંક") is the error this gate exists to stop.

## How the lens is used

- **Agent 2** writes objectives that serve the lens — an objective that could belong to any
  chapter is a bad objective. Where the ભાષા-લક્ષ્ય is load-bearing for the scene, it may be the
  objective's subject, but it is still written about **this** text's words.
- **Agent 12** writes each `explanation` through the lens. In a દુહો the explanation ends at the
  શિખામણ; in a ભક્તિ-પદ it ends at the ભાવ, and a શિખામણ forced onto it is a hard fail. Glosses ride
  inside that same explanation at point of first use — never appended as a word-list after it.
- **Agent 13** checks that the chapter's `guiding_question` is actually answered by the sequence
  of topics — if reading all the explanations in order does not answer it, the lens or the cut is
  wrong.
- **Agent 10** tags each સ્વાધ્યાય item's `skill` and maps it back to the scenes that prepare it. The
  literary lens prepares the comprehension and પ્રકાર items; the ભાષા-લક્ષ્ય prepares the
  શબ્દાર્થ/સમાનાર્થી/વિરુદ્ધાર્થી/રૂઢિપ્રયોગ items. A chapter whose word-work items map to nothing is
  a signal that the second lens was never set.

In a mixed chapter (`genre: "mixed"`) every part is taught under its own lens; only the dominant
સ્વરૂપ sets the chapter's single `guiding_question`. See `profiles/genres/_genre_index.md`.

## The lens is not a template

Two chapters of the same સ્વરૂપ have the same lens but different guiding questions, because the
question is derived from **this** text. `એક જ ડાળનાં પંખી` and `સુંદર સુંદર` are both ઊર્મિકાવ્ય-ગીત;
one asks what keeps a group one, the other asks what makes an ordinary morning worth singing about.
The same holds for the second lens: both are ગીત, but one hands the child the words of સંપ and
સાથ, the other the words of પ્રકૃતિનું સૌંદર્ય. Deriving either question from the profile instead of
from the chapter is the mistake this file exists to prevent.
