# GSEB ગુજરાતી (દ્વિતીય ભાષા) — board profile

Decides **ids, the reader, the grade-band language, and where the source PDF comes from**, for
std 6–10.

Three facts frame every section below.

- **The sources are local files.** One PDF per unit under `../Textbooks-pdf/std-N/`, split from one
  scanned book per standard, indexed by that directory's `manifest.json`. There is no bucket, no
  download step, no LP-v1 plan corpus and no frame pool to reuse from.
- **All five books are image-only.** No text layer exists anywhere in std 6, 7, 8, 9 or 10. Every
  fact in this file was read off a page rendered with `pdftoppm`. Verbatim work is *transcription*,
  never extraction — see §The text layer.
- **The DB ids are unverified and the word bands are provisional.** Nothing here has been checked
  against the live server (VERIFY-1, VERIFY-2) and no Gujarati chapter has yet been authored or
  measured (VERIFY-4). Both facts are restated where they bite.

The measured authority behind this file is `reference/corpus/std-{6,7,8,9,10}_inventory.md`. Where
this profile and an inventory disagree, the inventory wins — it is the transcription; this is the
summary.

## Reader

| Std | Printed title (`textbook` root field) | Teaching chapters | Other units in the book | Source directory |
|---|---|---|---|---|
| 6 | **ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 6** — ગુજરાત રાજ્ય શાળા પાઠ્યપુસ્તક મંડળ, ગાંધીનગર ✓ (read off the cover spread) | **15** | 2 revision checkpoints (R1 after ch 7, R2 after ch 15) + 1 પૂરકવાચન section holding 4 pieces | `../Textbooks-pdf/std-6/` |
| 7 | **ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 7** — same publisher ✓ (read off the cover) | **15** | R1, R2 + 4 પૂરકવાચન units + શબ્દસીડી board-game appendix | `../Textbooks-pdf/std-7/` |
| 8 | ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 8 — **cover not read yet**; confirm before writing it into `textbook` | **15** | R1, R2 + 4 પૂરક વાચન units | `../Textbooks-pdf/std-8/` |
| 9 | ગુજરાતી (દ્વિતીય ભાષા), ધોરણ 9 — **cover not read yet**; confirm before writing it into `textbook` | **23** | 4 વ્યાકરણ એકમો interleaved (V1–V4) + 4 પૂરક વાચન units. **No revision blocks** — annual volume | `../Textbooks-pdf/std-9/` |
| 10 | **ગુજરાતી (દ્વિતીય ભાષા) ધોરણ 10** ✓ (cover + verso footer) | **18** | 6 વ્યાકરણ એકમો interleaved + 5 પૂરક વાચન units. Board year — see §SSC weighting | `../Textbooks-pdf/std-10/` |

Read the counts this way:

- **A "teaching chapter" is a numbered unit with a reading text.** Revision units (આગળ વધતાં પહેલાં,
  પૂર્ણ કરતાં પહેલાં), વ્યાકરણ એકમો and the શબ્દસીડી appendix carry **no reading text at all** — they are
  exercise and apparatus material end to end, and the pack's standing rule applies: exercises are
  never topics, Agent 10 owns them.
- **પૂરક વાચન is the opposite case.** It is reading matter with (at most) a શબ્દાર્થ box and **no
  exercises**. If a પૂરક unit is ever built, it is all reading scenes and an almost empty
  `exercise_solutions.json` — say so in `01_meta.json` rather than inventing blocks.
- **Decide explicitly what a run ships.** Std 9 is 23 chapters or 31 units; std 10 is 18 or 29.
  Numbering the ones you skip is not the same as deciding to skip them, and the Hindi pack's
  three silently-absent class-10 chapters are the precedent for what that costs.

### Where each std's `unit_number`, pages and url come from

| Field | Value | Note |
|---|---|---|
| `textbook` | the printed title above | Gujarati script, exactly as the cover prints it |
| `textbook_url` | the local path string, e.g. `../Textbooks-pdf/std-6/ch-04-avyo-mehulo.pdf` | There is no hosted URL yet. Agent 11 records that as a `gaps[]` entry and drops confidence accordingly — an honest gap, not a defect |
| `textbook_pages` | the **printed** folio range (`22–27`) | Not the pdf page range. The pdf range is for rendering only |
| `unit_number` | the printed chapter number | Revision / વ્યાકરણ / પૂરક units have no printed chapter number — they need an explicit decision before they can carry one |
| `estimated_time` | 1.5 at std 6–8; **review at std 9–10** (2 is plausible, the Hindi pack used 2 at its board year) | The author's own field, not the server's |

### printed → pdf offset, per standard

Every unit's own `manifest.json` row carries `printed_start` and the exact `pdf_start`/`pdf_end`;
these constants only exist as a cross-check on it.

| Std | printed page N = pdf page | verified at |
|---|---|---|
| 6 | N + 11 | manifest, spot-checked across the book |
| 7 | N + 13 | chs 1, 8, 15 and પૂરકવાચન — held at every spot-check |
| 8 | N + 12 | manifest |
| 9 | N + 4 | manifest |
| 10 | N + 5 | manifest |

> **Page 1 of the render is the proof of WHICH chapter — never the filename.**
> These filenames are *ours*: `ch-04-avyo-mehulo.pdf` was produced by a split, and a split is
> exactly the kind of step that can be one unit out. A romanised filename cannot tell you what the
> page prints, and the manifest's `title_gu` is a transcription like any other — std 10's ch-18 row
> already carries one wrong poet name (§Corrections log). So: render page 1, read the number box
> and the title, and only then attach the chapter to a plan. The same rule settles a page range:
> the folio printed on the page beats the arithmetic.

## Grade-band language

### How to read every number in this section

**Nothing here is a measurement.** No Gujarati chapter has been authored yet, so no `explanation`
has been counted. Every figure below is a **PROVISIONAL TARGET** derived from the research findings
in `PEDAGOGY.md` §1–§2 (cognitive stage, L2 method, the three-tier spread) and from what the five
corpus inventories actually show the books doing. All of it is pending **VERIFY-4**.

Two rules govern what happens when the measurements arrive, and both are paid for by the Hindi
pack:

1. **Measure the first chapter of every standard before authoring the second.** In hindi-lp, class
   10 was calibrated against class 7 and skipped the two rungs in between. The result was an
   inversion — class 9 shipped at a median of 165 `explanation` words against class 10's 132 — and
   because each grade sat inside its *own* stated band, nothing looked broken until the two bands
   were laid side by side. It is still unresolved there. It survived because a **target was left
   standing where a measurement belonged**.
2. **Keep targets and measurements in separate tables** (§Targets vs measurements below) and
   **trim the prose to the band, never widen the band to the prose.**

The binding contract is `reference/field_shape_rules.md`: `explanation` and `real_life_example`
**55–90 words**, `objective_text` **12–30**. The per-standard targets below sit *inside* that
band; they do not replace it. If measurement shows std 9–10 analysis genuinely cannot be carried
in 90 words, that is a VERIFY-4 finding — resolved by amending the brief and then
`field_shape_rules.md`, never by quietly running long.

### The five dials — all PROVISIONAL

| | std 6 (~11) | std 7 (~12) | std 8 (~13) | std 9 (~14) | std 10 (~15) |
|---|---|---|---|---|---|
| `explanation` **target median** (band 55–90) | ~60 | ~65 | ~72 | ~82 | ~88 |
| `real_life_example` **target median** (band 55–90) | ~58 | ~62 | ~68 | ~75 | ~78 |
| **sentence length** inside `explanation` | ≤10–12 words; simple or compound, at most one subordinate clause | up to two clauses | two-clause complex; reported speech fine | multi-clause acceptable | denser તત્સમ / જોડાક્ષર register — decode the conjunct, do not dodge the word |
| **`real_life_example` reach** | ઘર, વર્ગખંડ, શેરી, રમત — only what this child has done | શાળા, મહોલ્લો, બજાર, તહેવાર (ઉત્તરાયણ, નવરાત્રિ) | ગામ કે શહેર, ખેતર-કૂવો, ST બસ, મેળો — a situation, not only a memory | કામ કરતાં મોટેરાં, સમાચાર, જવાબદારી — may be an *idea*, not only a scene | પોતાના નિર્ણય, ભવિષ્યની પસંદગી, સમાજ |
| **craft naming** | **notice only, never name.** Point at the પ્રાસ and the લય; the words the voice may use are શબ્દ, વાક્ય, નામ, ક્રિયા | notice, and name the *word class* only after the pattern has been seen (ક્રિયાપદ, કાળ) | structure as play — હાઈકુની 5-7-5 ચાલ, દુહાની માત્રા-ચાલ. **Still no** અલંકાર / છંદ / સમાસ label | **the switch.** સાહિત્યપ્રકાર tag + the seven અલંકાર + સંધિ, સમાસ, કૃદંત, નિપાત. **No** છંદ, **no** કર્તરિ/કર્મણિ | + છંદ (std-10 only), the five added અલંકાર, કર્તરિ→કર્મણિ→ભાવે→પ્રેરક |
| **the closing question** | શું થયું? કોણે શું કર્યું? કેવું લાગ્યું? તમે હો તો શું કરો? | + કેમ કર્યું હશે? પછી શું થશે? પાત્રની જગ્યાએ હો તો? | + બોધ તમારા શબ્દોમાં; બીજો અંત; જો… તો શું થાત? | + કઈ પંક્તિ પરથી કહો છો? — a theme claim **with** the line quoted; કટાક્ષ may be examined | + આ વાત આજે ટકે છે? બે કૃતિની સરખામણી; મૂલ્યાંકન |

**Constant at every band, and not negotiable at any of them:** Gujarati script throughout
(U+0A80–U+0AFF); Roman only inside brackets on first use of a technical term —
`સજીવારોપણ (personification)`; second-person teacher voice; no lecturing and no ઉપદેશ; no assumed
prior knowledge of the literary form; and `original_chunk` exactly as printed, archaic and
dialectal forms included. Full calibration in `reference/teaching_voice_gu.md`.

The L2 dials are constant too and they are the reason this ladder is *not* the Hindi one: glossing
density is higher at every band, and the "everyday word, skip it" bar is lower at every band. An L2
child stops on words a first-language child walks past. The books agree — **every std-6 chapter
ends with `નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો.` (15/15 measured)** and every chapter of every
standard prints a શબ્દાર્થ / શબ્દ-સમજૂતી box *before* its exercises.

### Std 6 — the bottom rung

What the measured book adds to the table above:

- **`figures_of_speech` is `[]` for essentially every topic, and that is the correct answer.**
  Naming an અલંકાર is outside the syllabus until std 9 (`PEDAGOGY.md` §1, std-8 DON'T list). The
  temptation is highest here because the poems look simple enough to decorate.
- **પ્રાસ is the one exception, and it is noticing, not naming.** The book asks for it directly —
  ch 1's intro box says `પ્રાસયુક્ત શબ્દોથી પણ પરિચિત કરવાં`. So `rhyme_scheme` may be filled honestly
  where the poem rhymes; `figures_of_speech` still stays `[]`.
- **The grammar ladder stops early.** Measured, in teaching order: જોડાક્ષર (ch 2) → સંજ્ઞા (ch 3) →
  વિશેષણ (ch 4) → ક્રિયાપદ + ત્રણ કાળ (ch 5) → વાક્યના પ્રકારો (ch 7) → વિરામચિહ્નો (ch 9), with
  phonics (શ/ષ/સ, ર/ળ, ળ/ડ) anchored in ch 6. **સંધિ, સમાસ, કૃદંત and નિપાત do not appear at std 6** —
  do not let an objective or a gloss reach for them.
- **The exercise apparatus is large and it is where the L2 work lives.** 15/15 chapters carry
  વાતચીત as block 1 and the first-language translation block at the end; ch 2 alone runs **19**
  numbered blocks. `exercise_solutions.json` is produced with the chapter, not after the class.

### Std 7 — one step up, same series

- **Counterfactual questions are the std-7 signature** — `જો … હોત તો ?` appears in chs 3, 6, 7, 8,
  10 and 12. That is the band's real new capacity (motive inference on familiar content), and
  recall questions should reach it.
- **The grammar spiral is explicit on the page**: ch 3's box says `આપણે ગયા વર્ષે સંજ્ઞા વિશે શીખી ગયા
  છીએ` and completes the six types. Objectives must not re-teach std-6 ground as if it were new.
- The first-language translation block drops to **10/15** chapters — present, no longer universal.
- ch 14 વીર ભામાશા is the **only** drama unit in the book: the એકાંકી profile gets exactly one
  chapter's worth of use at this standard.

### Std 8 — the pivot

- Interpretation becomes fair (motive, alternative endings, બોધ in the student's own words) and
  explicit grammar rules arrive **after** the encounter, not before it.
- **Still no named devices.** ch 10 is a ગઝલ with a real છાપ (`'આદિલ'` in the મક્તા) and ch 7 is a
  લગ્નગીત; both are to be *experienced* and quoted, not labelled. The છાપ is verse text — never
  present it as a technical term.
- The book's own apparatus supports this: 11/15 chapters carry a રૂઢિપ્રયોગ pre-block and 8/15 a
  શબ્દસમૂહ માટે એક શબ્દ pre-block, but nothing anywhere names an અલંકાર.

### Std 9 — the analysis switch, and the apparatus changes with it

This is where the reader's page stops looking like std 6–8 (§સ્વાધ્યાય block names). Three
consequences for authoring:

- **Naming starts here, from the line first.** Encounter → name → apply. The book pre-names craft
  itself in its ભાષા-અભિવ્યક્તિ bullets (ch 1 names વક્રોક્તિ; ch 3 prints a two-column પ્રાસ list), and
  ch 4's own MCQ asks the student to choose the સાહિત્યપ્રકાર (નવલકથાખંડ / નવલિકા / નિબંધ / નાટક). That
  is evidence the craft question is fair — it is not permission to name a device the page does not
  carry.
- **Scope ceiling, and it is a hard one:** સંધિ, સમાસ, કૃદંત, નિપાત, વિરામચિહ્નો, the seven અલંકાર —
  and **no છંદ, no voice transformation, no બહુવ્રીહિ/દ્વિગુ**. Those are std 10.
- **The book has no revision blocks.** Std 6–8 have two checkpoints each; std 9 is an annual volume
  with none. Spaced review has to be scheduled by the plan, not inherited from the book.

### Std 10 — the board year

- છંદ enters (std-10 only), five more અલંકાર are added, and કર્તરિ→કર્મણિ→ભાવે→પ્રેરક is the signature
  grammar skill. See §SSC weighting for what that does to the deliverables.
- The register is denser: તત્સમ and જોડાક્ષર-heavy. The right move for a weak reader is to break the
  conjunct open (`સ્ + ત = સ્ત`), not to swap the word for an easier one.
- **Never let the model supply a છંદ name, an અલંકાર name or a poet attribution from memory.** Two
  source discrepancies are already on record in the research (મંદાક્રાન્તા and હરિણી syllable counts),
  and Gujarati sits at the bottom of the Indic resource ladder. Only what the provided page carries
  counts (`reference/no_hallucination_policy.md`).

### Targets vs measurements — keep these apart

Nothing has been measured. This table exists so that a target can never be mistaken for one: fill
the right-hand columns **only** from counted, shipped chapters, and state how many chapters each
median is over.

| Std | `explanation` target | `explanation` **measured** (chapters, median, span) | `real_life_example` target | `real_life_example` **measured** |
|---|---|---|---|---|
| 6 | ~60 (band 55–90) | *not measured* | ~58 | *not measured* |
| 7 | ~65 | *not measured* | ~62 | *not measured* |
| 8 | ~72 | *not measured* | ~68 | *not measured* |
| 9 | ~82 | *not measured* | ~75 | *not measured* |
| 10 | ~88 | *not measured* | ~78 | *not measured* |

When a standard's first chapter is measured: write the numbers into the measured columns, keep the
target column as it was, and — if they disagree — say so here in one line with the chapter id. A
target quietly overwritten by a measurement is how a ladder stops being evidence.

## Ids

```
chapter_id = {board}_{medium}_{subject}{grade}_ch{unit_number}   → gseb_eng_gujarati6_ch1
plan_id    = {chapter_id}_v{version}                             → gseb_eng_gujarati6_ch1_v1
subject    = "Gujarati"      board = "gseb"      level = "standard"
```

> **⚠ PROVISIONAL — `gseb` and `eng` are UNVERIFIED (VERIFY-1).**
>
> The form above is **reasoned from the Hindi precedent, not read from the live server.** VERIFY-1
> must resolve the real GSEB board and medium segments against the server **before the first
> upload**. When it lands, `reference/naming_conventions.md` is corrected first and this file
> second; every other file inherits the corrected form.
>
> **`{medium}` is the medium of instruction — not the subject language.** The subject sits in the
> `{subject}` slot, so a Gujarati chapter reads `gseb_`**`eng`**`_gujarati6_ch1`. Writing
> `gseb_guj_gujarati6_ch1` by analogy with the subject is wrong **and does not surface as an
> error**: the server parses this segment into a real `medium` DB column, the upload succeeds, and
> the plan goes live registered under the wrong medium. All 23 Hindi plans shipped that way once
> and had to be re-uploaded. The slot genuinely varies across boards — `bseap_tel_sci7_ch2` carries
> medium `tel` — so `eng` is a guess until it is read.
>
> Two independent cross-checks, either of which would have caught the Hindi failure. **Both must be
> re-run for GSEB:**
> 1. **Enumerate the live corpus's medium usage** — what mediums actually exist for GSEB rows, not
>    what the Hindi corpus used.
> 2. **Read the asset-bucket path segments** — `V2/{board}/{publication}/{medium}/class_{N}/gujarati/ch_{n}/image/`
>    keeps medium and subject in separate segments. The Hindi bucket said `english` in the medium
>    slot and `hindi` in the subject slot; that was a *verified quirk of that corpus*, never a rule
>    to copy.
>
> After any upload, `GET /api/lp2/learning-plans/chapter/{chapter_id}` echoes `medium` and
> `subject` back. **Read them** (VERIFY-5).

`plan_id` has **no `_standard_` segment**; the server assigns the real version — what you write is
the intention. Output directories are `output6/ … output10/` with zero-padded chapter folders
(`ch01`), per `reference/naming_conventions.md`.

### Which root ids the author sets, and which the server does

**The author sets exactly two: `chapter_master_id` and `publication_id`.** Both come from
`upload_reference/chapter_master_map.json`, which carries only those two per chapter (plus `path`).

For GSEB **neither value exists yet.** No row in this profile's chapter tables can be filled in
until VERIFY-2 fetches them from the education DB:

- `chapter_master_id` is **required for LP2 upload and is not discoverable from the plan API.** It
  must be fetched, never invented and never extrapolated. The Hindi arithmetic (`355 − chapter`,
  `476 − chapter`, and class 7 running *upwards* with two strays) does not transfer, and its own
  grades disagree with each other — which is precisely why it is not a formula.
- `publication_id` is **required and must not be null.** The GSEB publication row must be looked
  up; the Hindi value `1` is provenance, not a portable fact.
- **A phase-1 dump carries `chapter_master_id: 0`.** Read the id from the map, never from the dump.

**`subject_ref_id` and `medium_id` belong to the server, not to the plan.** They sit in the
volatile-keys list the local↔remote comparison drops precisely because the server fills them, and
the LP2 validator accepts `null`. **Write `null` for both** unless a real GSEB subject record is in
hand — and if one is, send its real values, because a real value survives the round trip while an
invented one is a hazard. Reading a shipped plan back and copying the number it returns is the
trap: in the Hindi corpus those readbacks were 84, 78, 85 across three consecutive grades, which
looks like a table to copy and follows no pattern at all.

## Std-6 chapter table

| # | chapter (printed title) | `chapter_master_id` | printed pp | file in `../Textbooks-pdf/std-6/` | pdf pp | સ્વરૂપ prior — **diagnose, don't assume** |
|---|---|---|---|---|---|---|
| 1 | એક જ ડાળનાં પંખી | — | 1–5 | `ch-01-ek-j-dalna-pankhi.pdf` | 12–16 | ઊર્મિકાવ્ય-ગીત (બાળગીત, ટેક-આધારિત) ✓ — the intro box calls it કાવ્ય and prescribes ગાન |
| 2 | ચોટડૂક | — | 6–13 | `ch-02-chotaduk.pdf` | 17–24 | વાર્તા (રમૂજકથા / જાદુઈ બાળવાર્તા) ✓ — the book's જોડાક્ષર-teaching anchor |
| 3 | બાણ તો ત્યારે જ છૂટશે... | — | 14–21 | `ch-03-ban-to-tyare-j-chhutshe.pdf` | 25–32 | સંવાદ (નાટ્યરૂપ સંવાદ, near-એકાંકી) ✓ — speaker labels + directions in ( ) |
| 4 | આવ્યો મેહુલો | — | 22–27 | `ch-04-avyo-mehulo.pdf` | 33–38 | લોકગીત (વર્ષા-લોકગીત) ✓ — the author slot prints **લોકગીત**, not a name |
| 5 | વીજળીરાણી | — | 28–33 | `ch-05-vijalirani.pdf` | 39–44 | માહિતીપ્રદ વાર્તા (વિજ્ઞાનકથા inside a દાદાજીની વાર્તા frame) ✓ *(medium-high)* |
| 6 | સંસ્કારે સર્જ્યું સ્વર્ગ | — | 34–40 | `ch-06-sanskare-sarjyu-swarg.pdf` | 45–51 | સંવાદ-કથા ✓ — quoted dialogue inside prose; the book's શ/ષ/સ · ર/ળ pronunciation chapter |
| 7 | ચોખ્ખાઈના સરદાર | — | 41–44 | `ch-07-chokhkhaina-sardar.pdf` | 52–55 | કૂચગીત (ગીત sub-form named by the book) ✓ — ટેક + 6 કડી, two columns |
| R1 | આગળ વધતાં પહેલાં | — | 45–49 | `revision-01-agal-vadhata-pahela.pdf` | 56–60 | revision unit — સ્વાધ્યાય only, no lesson text. **Never a topic** |
| 8 | મામાનો પત્ર | — | 50–54 | `ch-08-mamano-patra.pdf` | 61–65 | પત્ર ✓ — a personal letter carrying a ચરિત્ર-પ્રસંગ inside it |
| 9 | ગરવી ગુજરાતનો ગરબો | — | 55–62 | `ch-09-garvi-gujaratno-garbo.pdf` | 66–73 | સાંસ્કૃતિક માહિતી-કથા ✓ — first-person frame + quoted dialogue |
| 10 | સાથી મારે બાર | — | 63–67 | `ch-10-sathi-mare-bar.pdf` | 74–78 | કથાકાવ્ય / કથાગીત ✓ — the book prints **both** labels |
| 11 | કામની મજા ને મજાનું કામ | — | 68–78 | `ch-11-kamni-maja-ne-majanu-kam.pdf` | 79–89 | ઘરેલુ વાર્તા ✓ — dialogue-rich; shared-housework values |
| 12 | અજબગજબનો મેળો | — | 79–84 | `ch-12-ajabgajabno-melo.pdf` | 90–95 | માહિતીપ્રદ નિબંધ / સાંસ્કૃતિક વર્ણન ✓ — expository, no story frame, real photographs |
| 13 | સૂર્ય સુધી પહોંચાય ? | — | 85–91 | `ch-13-surya-sudhi-pahonchay.pdf` | 96–102 | વાર્તા-માં-વાર્તા ✓ — classroom frame + embedded પૌરાણિક કથા |
| 14 | એક છોકરો રિસાણો | — | 92–100 | `ch-14-ek-chhokro-risano.pdf` | 103–111 | સંવાદ ✓ — speaker-labelled domestic dialogue, no stage opener |
| 15 | લો, પાથરી મારી વાત | — | 101–107 | `ch-15-lo-pathri-mari-vat.pdf` | 112–118 | આત્મકથનાત્મક નિબંધ ✓ — a working woman's spoken self-account |
| R2 | પૂર્ણ કરતાં પહેલાં | — | 108–112 | `revision-02-purna-karta-pahela.pdf` | 119–123 | revision unit — સ્વાધ્યાય only. **Never a topic** |
| P1 | પૂરકવાચન | — | 113–118 (+ cover spread) | `purak-01-purak-vachan.pdf` | 124–130 | પૂરકવાચન: 4 independent pieces (2 કાવ્યો, 1 પ્રવાસ-માહિતી નિબંધ, 1 ઉખાણાં set) ✓ — **no exercises at all** |

Every row's genre was confirmed on a rendered page and every chapter's સ્વાધ્યાય pages were read in
full (`reference/corpus/std-6_inventory.md`, 18 of 18 units). **The સ્વરૂપ column is still a prior,
not a verdict** — Agent 1 diagnoses from the four signals in the text and may disagree.

The single best genre signal on a std-6 page is the **blue intro box**, which names the form in the
book's own words (`આ એક રસપ્રદ રમૂજકથા છે`, `આ એક સુંદર લોકગીત છે`, `અહીં 'કૂચગીત' દ્વારા…`). It is
teacher-addressed apparatus — evidence for the diagnosis, never a reading scene, never a topic.

**ch 4 carries a second poem.** After the exercises, a yellow `ગાઈએ` box prints a whole different
poem (`મેહુલો` – ત્રિભુવન વ્યાસ) for singing. It is appended **reading matter**, not an exercise and
not part of the લોકગીત: cut it under its own unit or leave it out deliberately, but do not let it
merge into ch 4's verse.

## Std-7 chapter table

| # | chapter (printed title) | `chapter_master_id` | printed pp | file in `../Textbooks-pdf/std-7/` | pdf pp | સ્વરૂપ prior — **diagnose, don't assume** |
|---|---|---|---|---|---|---|
| 1 | સુંદર સુંદર | — | 1–4 | `ch-01-sundar-sundar.pdf` | 14–17 | ઊર્મિકાવ્ય-ગીત (પ્રકૃતિગીત) ✓ — one ધ્રુવપંક્તિ closes every કડી, identical each time |
| 2 | ત્રણ સવાલ | — | 5–10 | `ch-02-tran-saval.pdf` | 18–23 | વાર્તા (ચાતુર્યકથા) ✓ — court dialogue with speaker labels |
| 3 | ચક્રવ્યૂહ તૂટ્યો પણ... | — | 11–18 | `ch-03-chakravyuh-tutyo-pan.pdf` | 24–31 | વાર્તા (વીરરસભરી પૌરાણિક કથા) ✓ — the book's own label |
| 4 | ટીપાંની સફર | — | 19–24 | `ch-04-tipani-safar.pdf` | 32–37 | માહિતીપ્રદ વાર્તા (સંવાદ-શૈલી વિજ્ઞાનકથા) ✓ — સજીવારોપણ throughout; **mixed** વાર્તા + માહિતી |
| 5 | આપણે ભરોસે | — | 25–29 | `ch-05-aapne-bharose.pdf` | 38–42 | ઊર્મિકાવ્ય-ગીત (શ્રમ / આત્મનિર્ભરતાનું ગીત) ✓ — હાલીએ, છઈએ, કો' as printed |
| 6 | જો કરી જાંબુએ | — | 30–36 | `ch-06-jo-kari-jambue.pdf` | 43–49 | હાસ્યલેખ / રમૂજી પ્રસંગકથા ✓ — repetition-with-escalation is the comic engine |
| 7 | એક માણસનું સૈન્ય | — | 37–44 | `ch-07-ek-manasnu-sainya.pdf` | 50–57 | ચરિત્ર-પ્રસંગ / સાહસકથા ✓ — રણછોડ પગી; war content → flag-and-guide (Agent 8) |
| R1 | આગળ વધતાં પહેલાં | — | 45–49 | `rev-01-aagal-vadhta-pahela.pdf` | 58–62 | revision unit — exercises only. **Never a topic** |
| 8 | સાદ વરત્યો | — | 50–56 | `ch-08-saad-vartyo.pdf` | 63–69 | લોકકથા (સૌરાષ્ટ્રી; 'સૌરાષ્ટ્રની રસધાર') ✓ — the intro box *orders* the તળપદા શબ્દો taught |
| 9 | અલ્લક દલ્લક | — | 57–62 | `ch-09-allak-dallak.pdf` | 70–75 | ઊર્મિકાવ્ય-ગીત (રાધા-કૃષ્ણ રાસલીલા) ✓ — coined echo-words carry the poem |
| 10 | ભાઈબંધી | — | 63–70 | `ch-10-bhaibandhi.pdf` | 76–83 | વાર્તા (માણસ અને પ્રાણી વચ્ચેની સ્નેહકથા) ✓ |
| 11 | અંધેરી નગરી | — | 71–76 | `ch-11-andheri-nagari.pdf` | 84–89 | કથાકાવ્ય (19મી સદી, દલપતરામ) ✓ — old Gujarati kept exactly as printed |
| 12 | બે રૂપિયા | — | 77–84 | `ch-12-be-rupiya.pdf` | 90–97 | વાર્તા (પ્રામાણિકતાની સામાજિક-ભાવ કથા) ✓ |
| 13 | ટૅક્સીને ફૂટી પાંખો ! | — | 85–92 | `ch-13-taxine-futi-pankho.pdf` | 98–105 | વિજ્ઞાન-કલ્પનકથા ✓ |
| 14 | વીર ભામાશા | — | 93–98 | `ch-14-vir-bhamasha.pdf` | 106–111 | એકાંકી-નાટક ✓ — **the book's only drama unit** |
| 15 | સોનાનો કિલ્લો | — | 99–105 | `ch-15-sonano-killo.pdf` | 112–118 | પ્રવાસવર્ણન / નિબંધ ✓ — printed as a model essay |
| R2 | પૂર્ણ કરતાં પહેલાં | — | 106–111 | `rev-02-purna-karta-pahela.pdf` | 119–124 | revision unit — exercises only. **Never a topic** |
| P1 | ચાલો, નિબંધ લખીએ... | — | 112–113 | `purak-01-chalo-nibandh-lakhie.pdf` | 125–126 | માર્ગદર્શક લેખ (નિબંધ કેમ લખવો) ✓ — instructional prose, **not** a reading scene |
| P2 | સમજણ તે આપણા બેની | — | 114 | `purak-02-samjan-te-aapna-beni.pdf` | 127–127 | ઊર્મિકાવ્ય-ગીત (સહિયારાપણાનું બાળગીત) ✓ |
| P3 | રામરાજ્યનાં મોતી | — | 115–118 | `purak-03-ramrajyana-moti.pdf` | 128–131 | પૌરાણિક વાર્તા (દૃષ્ટાંતકથા) ✓ |
| P4 | કાલે | — | 119 | `purak-04-kale.pdf` | 132–132 | ઊર્મિકાવ્ય-ગીત (ભવિષ્ય-આશાનું બાળગીત) ✓ |
| A1 | શબ્દસીડી (નિયમો અને રમત-પાટિયું) | — | 120 (+ duplicate scans, back cover) | `99-shabdsidi.pdf` | 133–140 | શબ્દસીડી board game — appendix, not a chapter; pdf 134–139 are duplicate scans |

All 22 units recorded, every genre confirmed on a render, every સ્વાધ્યાય page read
(`reference/corpus/std-7_inventory.md`).

Two page-level traps in this book: ch 6 prints **two consecutive blocks both numbered `10.`**
(printed pp. 34–35), and ch 8's numbering **jumps 3 → 5** with no block 4 visible. Inventory what
the page shows, not what the sequence implies — a "missing" block 4 that was never printed is not
an unanswered block.

## Std-8 chapter table

| # | chapter (printed title) | `chapter_master_id` | printed pp | file in `../Textbooks-pdf/std-8/` | pdf pp | સ્વરૂપ prior — **diagnose, don't assume** |
|---|---|---|---|---|---|---|
| 1 | જીવનજ્યોત | — | 1–6 | `ch-01-jivanjyot.pdf` | 13–18 | પ્રાર્થનાગીત (ગીત) ✓ — refrain printed as an ellipsis; expand only against the page |
| 2 | ત્યાગવીર દધીચિ | — | 7–14 | `ch-02-tyagvir-dadhichi.pdf` | 19–26 | પૌરાણિક કથા (વાર્તા) ✓ |
| 3 | મારી વ્યાયામસાધના | — | 15–26 | `ch-03-mari-vyayamsadhana.pdf` | 27–38 | હાસ્યનિબંધ ✓ — quotes નરસિંહ inside the essay |
| 4 | જબરી મધમાખી | — | 27–35 | `ch-04-jabri-madhmakhi.pdf` | 39–47 | વિસ્મયકથા (વાર્તા) ✓ — deliberate English medical vocabulary (the intro says so) |
| 5 | બાનો વાડો | — | 36–45 | `ch-05-bano-vado.pdf` | 48–57 | લલિતનિબંધ ✓ — with a વ્યક્તિચિત્ર layer (બા) |
| 6 | પીડ પરાઈ જાણે રે ! | — | 46–52 | `ch-06-pid-parai-jane-re.pdf` | 58–64 | ચરિત્રલેખ (નરસિંહ મહેતા) ✓ — carries the છાપ line “ભણે નરસૈયો…” inside modern prose |
| 7 | કંકોતરી | — | 53–58 | `ch-07-kankotari.pdf` | 65–70 | લગ્નગીત (લોકગીત) ✓ — the author slot prints **લોકગીત** |
| R1 | આગળ વધતાં પહેલાં... | — | 59–63 | `review-1-agal-vadhta-pahela.pdf` | 71–75 | revision unit — exercises only. **Never a topic** |
| 8 | જીવતી દીવાદાંડી | — | 64–71 | `ch-08-jivti-divadandi.pdf` | 76–83 | સાહસકથા (ચરિત્રાત્મક) ✓ |
| 9 | શતરંગી ભારત | — | 72–80 | `ch-09-shatrangi-bharat.pdf` | 84–92 | વાર્તારૂપ સંવાદ (સાંસ્કૃતિક / informational) ✓ |
| 10 | હલેસે હલેસે | — | 81–84 | `ch-10-halese-halese.pdf` | 93–96 | ગઝલ ✓ — રદીફ ‘દરિયો’; છાપ ‘આદિલ’ stands **inside** the મક્તા, it is verse, not a label |
| 11 | જામફળ અને જલેબી | — | 85–93 | `ch-11-jamfal-ane-jalebi.pdf` | 97–105 | આત્મકથા-ખંડ (સંસ્મરણ) ✓ |
| 12 | ક્ષિતિ | — | 94–107 | `ch-12-kshiti.pdf` | 106–119 | નાટક (એકાંકી) ✓ — its સ્વાધ્યાય embeds a *different* play excerpt (never a chapter scene) |
| 13 | લીલી નજર | — | 108–113 | `ch-13-lili-najar.pdf` | 120–125 | પ્રેરણાદાયી સંવેદનકથા (વાર્તા) ✓ |
| 14 | નિયમો કોના માટે ? | — | 114–122 | `ch-14-niyamo-kona-mate.pdf` | 126–134 | ઘટના-સંવાદ (civic/traffic frame narrative) ✓ |
| 15 | પોર્ટરના પંજામાં | — | 123–132 | `ch-15-portarna-panjama.pdf` | 135–144 | હાસ્યપ્રસંગ / આત્મકથાત્મક પ્રસંગ ✓ |
| R2 | પૂર્ણ કરતાં પહેલાં... | — | 133–137 | `review-2-purna-karta-pahela.pdf` | 145–149 | revision unit — exercises only. **Never a topic** |
| P1 | ભુલભુલામણી | — | 138 | `purak-01-bhulbhulamani.pdf` | 150–150 | બાળકાવ્ય / ગીત ✓ *(medium-high)* — single page |
| P2 | જીવનમાં વ્યવસ્થિતતા | — | 139–140 | `purak-02-jivanma-vyavasthitata.pdf` | 151–152 | ચિંતનાત્મક નિબંધ ✓ |
| P3 | સોમનાથ, સાસણ ને સાવજ ! | — | 141–145 | `purak-03-somnath-sasan-ne-savaj.pdf` | 153–157 | પ્રવાસનિબંધ (કાલ્પનિક પ્રવાસ, dialogue-carried) ✓ |
| P4 | વિવિધા ભારતી | — | 146–148 | `purak-04-vividha-bharti.pdf` | 158–160 | શ્લોક / પદ-સંચય with Gujarati સમજૂતી ✓ — **quotes Devanagari verse**; the script check must allow quoted blocks |

All 21 units recorded (`reference/corpus/std-8_inventory.md`). Numbering defects here too: ch 14
jumps **5 → 7**, and chs 2 and 12 each print **two headings numbered `2.`** (the (અ)/(બ) split).

**P4 વિવિધા ભારતી quotes Sanskrit, Hindi, Marathi and old Punjabi verse in Devanagari.** That is
printed content in a Gujarati reader, so the script-purity check must treat a quoted verse block as
legitimate rather than as a contamination — the rule is *no Devanagari outside bracketed technical
terms **and quoted printed text***.

## Std-9 chapter table

| # | chapter (printed title) | `chapter_master_id` | printed pp | file in `../Textbooks-pdf/std-9/` | pdf pp | સ્વરૂપ prior — **diagnose, don't assume** |
|---|---|---|---|---|---|---|
| 1 | છપ્પા | — | 1–2 | `ch-01-chhappa.pdf` | 5–6 | છપ્પા (અખો; મધ્યકાલીન જ્ઞાનમાર્ગી કટાક્ષ) ✓ — છાપ ‘અખા’ inside the verse; 2 excerpts only |
| 2 | પરોપકારી મનુષ્યો | — | 3–7 | `ch-02-paropkari-manushyo.pdf` | 7–11 | હાસ્યનિબંધ ✓ — Parsi and Marwadi speech quoted verbatim |
| 3 | જ્યાં જ્યાં વસે એક ગુજરાતી | — | 8–10 | `ch-03-jyan-jyan-vase-ek-gujarati.pdf` | 12–14 | ઊર્મિકાવ્ય-ગીત (અસ્મિતા-ગીત) ✓ — **changed-words ટેક** at open and close |
| 4 | સિંહનું મૃત્યુ | — | 11–14 | `ch-04-sinhnu-mrutyu.pdf` | 15–18 | નવલકથા-અંશ ('અકૂપાર') ✓ — sustained ગીર બોલી in dialogue; the MCQ itself tests the પ્રકાર |
| 5 | તું તારા દિલનો દીવો | — | 15–16 | `ch-05-tu-tara-dilno-divo.pdf` | 19–20 | ઊર્મિકાવ્ય-ગીત (પ્રેરક / આત્મશક્તિ) ✓ — refrain closes every કડી |
| 6 | ભાષા જાય તો સંસ્કૃતિ જાય | — | 17–20 | `ch-06-bhasha-jay-to-sanskruti-jay.pdf` | 21–24 | ચિંતનાત્મક નિબંધ (ભાષા–સંસ્કૃતિ) ✓ — no તળપદા block; શિષ્ટ પ્રમાણભૂત ગદ્ય |
| V1 | વ્યાકરણ : એકમ-1 (સમાનાર્થી, વિરુદ્ધાર્થી, સ્વર-વ્યંજન, જોડણી) | — | 21–29 | `vyakaran-01-ekam-1.pdf` | 25–33 | વ્યાકરણ એકમ ✓ — apparatus, **not** a chapter; answers printed inline |
| 7 | નવસર્જનની વાટે | — | 30–31 | `ch-07-navsarjanni-vate.pdf` | 34–35 | ઊર્મિકાવ્ય-ગીત (પ્રગતિ/ઉત્સાહ ગીત) ✓ |
| 8 | આભાર | — | 32–34 | `ch-08-aabhar.pdf` | 36–38 | સૉનેટ ✓ — the intro defines the fourteen-line form; the MCQ's own answer is સોનેટ |
| 9 | પારખું | — | 35–43 | `ch-09-parkhu.pdf` | 39–47 | હળવું એકાંકી ✓ — the MCQ's own answer names it |
| 10 | એ લોકો | — | 44–46 | `ch-10-e-loko.pdf` | 48–50 | અછાંદસ / મુક્ત છંદ (સામાજિક કટાક્ષ-આક્રોશ કાવ્ય) ✓ |
| 11 | વારસાગત | — | 47–49 | `ch-11-varsagat.pdf` | 51–53 | લઘુકથા ✓ — the intro names the સાહિત્યપ્રકાર outright |
| V2 | વ્યાકરણ : એકમ-2 (લિંગ, વચન, અનુગ, નામયોગી, સંધિ) | — | 50–65 | `vyakaran-02-ekam-2.pdf` | 54–69 | વ્યાકરણ એકમ ✓ — apparatus, **not** a chapter; opens with a ગુજરાતી/हिन्दी/English comparison table (whitelisted printed content) |
| 12 | તો જાણું | — | 66–68 | `ch-12-to-janu.pdf` | 70–72 | ઊર્મિકાવ્ય-ગીત (કૃષ્ણપ્રેમ/ગોપીભાવ, લોકગીત-સ્પર્શ; modern poet) ✓ |
| 13 | ઘડવૈયા | — | 69–72 | `ch-13-ghadvaiya.pdf` | 73–76 | પ્રસંગકથા / રેખાચિત્ર (ચરિત્ર-પ્રસંગ family) ✓ — the book's own labels |
| 14 | મારું તારું ! | — | 73–75 | `ch-14-maru-taru.pdf` | 77–79 | ગઝલ ✓ — the intro says "આ રચના ગઝલ સ્વરૂપની છે"; no રદીફ, કાફિયા family alone |
| 15 | સો ટચનું સોનું | — | 76–79 | `ch-15-so-tachnu-sonu.pdf` | 80–83 | સંસ્મરણ / પ્રેરક પ્રસંગકથા (અનૂદિત — Sudha Murty) ✓ |
| 16 | ગોકુળમાં આવો તો | — | 80–82 | `ch-16-gokulma-aavo-to.pdf` | 84–86 | ઊર્મિકાવ્ય-ગીત (કાવ્યરૂપ પત્ર — રાધાનો કૃષ્ણને) ✓ |
| 17 | છબી ભીતરની | — | 83–86 | `ch-17-chhabi-bhitarni.pdf` | 87–90 | પ્રવાસ-અનુભવકથન / સંસ્મરણ ✓ — three anecdotes under printed sub-heads |
| V3 | વ્યાકરણ : એકમ-3 (વિશેષણ, ક્રિયાવિશેષણ, સંયોજક, વિરામચિહ્નો) | — | 87–96 | `vyakaran-03-ekam-3.pdf` | 91–100 | વ્યાકરણ એકમ ✓ — apparatus, **not** a chapter |
| 18 | દીકરીની વિદાય | — | 97–98 | `ch-18-dikrini-viday.pdf` | 101–102 | ઊર્મિકાવ્ય-ગીત (કરુણ/વિદાય ગીત) ✓ |
| 19 | પંખીલોક | — | 99–102 | `ch-19-pankhilok.pdf` | 103–106 | લલિત નિબંધ ✓ — the intro itself says "લલિત રીતે" |
| 20 | હરિ ! આવોને | — | 103–104 | `ch-20-hari-aavone.pdf` | 107–108 | લોકગીત (ભક્તિ-આતિથ્ય) ✓ — devotional yet `સંકલિત`, no છાપ |
| 21 | પ્રાણીઓનું ગોકુળ | — | 105–109 | `ch-21-pranionu-gokul.pdf` | 109–113 | અનુભવ-કથન / સંસ્મરણ (અનૂદિત — મરાઠીમાંથી) ✓ |
| 22 | લઘુકાવ્યો | — | 110–112 | `ch-22-laghukavyo.pdf` | 114–116 | **mixed** — દુહો, મુક્તક, હાઈકુ under one head, per-section credits ✓ |
| 23 | પ્રેરક પ્રસંગો | — | 113–115 | `ch-23-prerak-prasango.pdf` | 117–119 | પ્રેરક પ્રસંગ સંકલન (ચરિત્ર-પ્રસંગ family; three પ્રસંગ) ✓ |
| V4 | વ્યાકરણ : એકમ-4 (સમાસ, શબ્દસમૂહ માટે એક શબ્દ, રૂઢિપ્રયોગ, કહેવત) | — | 116–127 | `vyakaran-04-ekam-4.pdf` | 120–131 | વ્યાકરણ એકમ ✓ — apparatus, **not** a chapter; trilingual કહેવત table (whitelisted printed content) |
| P1 | એટલામાં રાજી ! | — | 128 | `purak-01-etlama-raji.pdf` | 132–132 | પૂરક વાચન: ઊર્મિકાવ્ય-ગીત (પ્રકૃતિ-આનંદ) ✓ — શબ્દાર્થ only, **no સ્વાધ્યાય** |
| P2 | અભિનય સમ્રાટ : ઉપેન્દ્ર ત્રિવેદી | — | 129–130 | `purak-02-abhinay-samrat-upendra-trivedi.pdf` | 133–134 | પૂરક વાચન: ચરિત્રનિબંધ ✓ — શબ્દાર્થ only, **no સ્વાધ્યાય** |
| P3 | ઉપમન્યુ | — | 131–134 | `purak-03-upmanyu.pdf` | 135–138 | પૂરક વાચન: પૌરાણિક કથા ✓ — શબ્દાર્થ only, **no સ્વાધ્યાય** |
| P4 | જન્મી રહેલા બાળક અને ભગવાન વચ્ચેનો સંવાદ ! | — | 135–136 | `purak-04-janmi-rahela-balak-ane-bhagwan.pdf` | 139–140 | પૂરક વાચન: સંવાદ-લેખ (dialogue-form essay — **not** a stage play: no directions, narrated speech tags) ✓ |

All 31 units recorded, every genre confirmed on a rendered page, every સ્વાધ્યાય page read
(`reference/corpus/std-9_inventory.md`, `Status: 31 of 31 units recorded — COMPLETE`). The
સ્વરૂપ column is still a prior, not a verdict — Agent 1 diagnoses from the four signals on the
rendered page and may disagree.

Std 9's page is laid out differently from std 6–8 and the difference is structural, not cosmetic:
author line + `(સમય : …)` era line under the title → **લેખક/કવિ-પરિચય before the text** → the text →
**શબ્દ-સમજૂતી** with sub-heads → a **printed સ્વાધ્યાય banner** → **વિદ્યાર્થી-પ્રવૃત્તિ** →
**ભાષા-અભિવ્યક્તિ** → **શિક્ષકની ભૂમિકા**. The last one is addressed to the teacher and belongs to
neither deliverable; the કવિ-પરિચય is printed biography — use only what it prints, and never add a
poet fact from memory (`reference/no_hallucination_policy.md`).

## Std-10 chapter table

| # | chapter (printed title) | `chapter_master_id` | printed pp | file in `../Textbooks-pdf/std-10/` | pdf pp | સ્વરૂપ prior — **diagnose, don't assume** |
|---|---|---|---|---|---|---|
| 1 | મોરલી | — | 1–3 | `ch-01-morli.pdf` | 6–8 | પદ-ભજન (કૃષ્ણભક્તિ) ✓ ✓સ્વા — છાપ “બાઈ મીરાં કે…”; refrain cue right-aligned per line |
| 2 | શરણાઈના સૂર | — | 4–11 | `ch-02-sharnai-na-sur.pdf` | 9–16 | ટૂંકીવાર્તા ✓ — embedded લગ્નગીત couplets in quotes |
| 3 | પ્રયાણ | — | 12–14 | `ch-03-prayan.pdf` | 17–19 | હાસ્ય-નવલકથાખંડ ('ભદ્રંભદ્ર') ✓ |
| vyakaran-1 | વ્યાકરણ : એકમ 1 સમાનાર્થી, વિરુદ્ધાર્થી, જોડણી | — | 15–19 | `vyakaran-01-samanarthi-virudhdharthi-jodni.pdf` | 20–24 | વ્યાકરણ એકમ ✓ — apparatus, not a chapter |
| 4 | જીવન અંજલિ થાજો | — | 20–22 | `ch-04-jivan-anjali-thajo.pdf` | 25–27 | પ્રાર્થનાકાવ્ય (ગીત) ✓ — ધ્રુવપંક્તિ repeats; લો'તાં apostrophe-elision on the page |
| 5 | શ્વેતક્રાંતિના પ્રણેતાઓ | — | 23–28 | `ch-05-shvetkranti-na-pranetao.pdf` | 28–33 | ચરિત્ર / રેખાચિત્ર (સંકલિત) ✓ — sectioned biography; QR box intrudes into para 1 |
| 6 | સામગ્રી તો સમાજની છે ને ! *(manifest prints `?` — settle on the render, see Corrections log)* | — | 29–31 | `ch-06-samagri-to-samaj-ni-chhe-ne.pdf` | 34–36 | પ્રસંગકથા (અનુભવકથન) ✓ |
| vyakaran-2 | વ્યાકરણ : એકમ 2 સંધિ, સમાસ | — | 32–38 | `vyakaran-02-sandhi-samas.pdf` | 37–43 | વ્યાકરણ એકમ ✓ — recycles chapter sentences as examples |
| 7 | જીવમાં જીવ આવ્યો | — | 39–41 | `ch-07-jivma-jiv-avyo.pdf` | 44–46 | સૉનેટ (મંદાક્રાન્તા) ✓ — verse set with wide letter-spacing (OCR inserts spurious spaces) |
| 8 | સૂરજ તો બધે જ સરખો | — | 42–45 | `ch-08-suraj-to-badhe-j-sarkho.pdf` | 47–50 | હાસ્યનિબંધ ✓ ✓સ્વા — code-mixing inside the dialogue |
| 9 | હાથ મેળવીએ | — | 46–48 | `ch-09-hath-melvie.pdf` | 51–53 | ઊર્મિકાવ્ય ✓ |
| vyakaran-3 | વ્યાકરણ : એકમ 3 રૂઢિપ્રયોગ, કહેવત | — | 49–50 | `vyakaran-03-rudhiprayog-kahevat.pdf` | 54–55 | વ્યાકરણ એકમ ✓ |
| 10 | નથી | — | 51–57 | `ch-10-nathi.pdf` | 56–62 | ટૂંકીવાર્તા ✓ |
| 11 | દીવાનખાનામાં | — | 58–60 | `ch-11-divankhanama.pdf` | 63–65 | અછાંદસ / આધુનિક ઊર્મિકાવ્ય ✓ — English words inside the line (“Wall to wall કારપેટ…”) |
| 12 | ઝબક જ્યોત | — | 61–69 | `ch-12-jhabak-jyot.pdf` | 66–74 | એકાંકી ✓ — speaker labels + parenthetical stage directions; drama-aware parsing needed |
| vyakaran-4 | વ્યાકરણ : એકમ 4 વાક્યપ્રકાર, વિશેષણ | — | 70–79 | `vyakaran-04-vakyaprakar-visheshan.pdf` | 75–84 | વ્યાકરણ એકમ ✓ — કર્તરિ/કર્મણિ/ભાવે/પ્રેરક; longest unit in the book |
| 13 | ક્યાં રે વાગી | — | 80–82 | `ch-13-kya-re-vagi.pdf` | 85–87 | લોકગીત ✓ ✓સ્વા — author slot prints **લોકગીત**; “– સમી સાંજની” sits right of each line |
| 14 | જેઠીબાઈ | — | 83–87 | `ch-14-jethibai.pdf` | 88–92 | લોકકથા (કચ્છી ઐતિહાસિક) ✓ |
| 15 | તે બેસે અહીં | — | 88–90 | `ch-15-te-bese-ahi.pdf` | 93–95 | ગઝલ ✓ — રદીફ ‘તે બેસે અહીં’, taught શેર-wise |
| vyakaran-5 | વ્યાકરણ : એકમ 5 વિરામચિહ્નો, વાર્તાલેખન | — | 91–94 | `vyakaran-05-viramchihno-vartalekhan.pdf` | 96–99 | વ્યાકરણ એકમ ✓ |
| 16 | પ્રાણનો મિત્ર | — | 95–98 | `ch-16-pranno-mitra.pdf` | 100–103 | અનુવાદિત વાર્તા (બંગાળી → ગુજરાતી) ✓ ✓સ્વા — full 5-block word apparatus |
| 17 | ટિફિન | — | 99–101 | `ch-17-tiffin.pdf` | 104–106 | લઘુકથા ✓ |
| 18 | લઘુકાવ્યો *(દુહા · મુક્તક · હાઈકુ)* | — | 102–106 | `ch-18-laghukavyo.pdf` | 107–111 | લઘુકાવ્ય-સંચય: દુહા, મુક્તક, હાઈકુ ✓ — multi-poet; **no chapter-number box** on page 1 |
| vyakaran-6 | વ્યાકરણ : એકમ 6 અહેવાલલેખન, સંક્ષેપીકરણ, અર્થવિસ્તાર, નિબંધલેખન | — | 107–111 | `vyakaran-06-ahevallekhan-sankshepikaran.pdf` | 112–116 | વ્યાકરણ એકમ (લેખન-કૌશલ્યો) ✓ |
| purak-1 | ભારતીય સંસ્કૃતિના જ્યોતિર્ધર | — | 112–113 | `purak-01-bharatiya-sanskruti-na-jyotirdhar.pdf` | 117–118 | ચરિત્રનિબંધ (પૂરક વાચન) ✓ |
| purak-2 | અનોખું મૈત્રીપર્વ | — | 114–116 | `purak-02-anokhu-maitriparv.pdf` | 119–121 | પ્રાણીકથા / નિબંધ-કથન ✓ |
| purak-3 | સત્યવ્રત | — | 117–120 | `purak-03-satyavrat.pdf` | 122–125 | બોધકથા / વાર્તા ✓ |
| purak-4 | બહેન સૌની લાડકી | — | 121–123 | `purak-04-bahen-sauni-ladki.pdf` | 126–128 | પ્રસંગકથા (હળવી શૈલી) ✓ |
| purak-5 | દીવડો | — | 124–125 | `purak-05-divdo.pdf` | 129–130 | ગીત (લોકઢાળ) ✓ |

All 29 units recorded and **every chapter's સ્વાધ્યાય read in full**
(`reference/corpus/std-10_inventory.md`, `Status: 29 of 29 units recorded — COMPLETE`; the ✓સ્વા
marks record the four chapters read first, in the sampling pass). The measured banner set is
near-fixed with real deviations — ch 5 prints a **3-tier ladder with no બે-ત્રણ વાક્ય tier**, chs
12 and 14 print the MCQ heading as "નીચેના પ્રશ્નોમાં…", and the લખો/આપો · સવિસ્તર/સવિસ્તાર drift
runs throughout — so the set is a strong prior and still not a substitute for Agent 10: read the
chapter's own banners before assigning blocks.

> **The પ્રકાર tag is not on the chapter opener.** `manifest.json` prints titles like
> `મોરલી (પદ) – મીરાંબાઈ` and `શરણાઈના સૂર (ટૂંકીવાર્તા) – ચુનીલાલ મડિયા`, but the rendered opener shows
> the **bare title** — the tag comes from the book's index, not the page. Treat it exactly as this
> profile's સ્વરૂપ column is treated: a prior with decent provenance, confirmed on the render or not
> used. (The Hindi pack's badge/banner confusion is the same failure in the other direction: the
> same words meant a genre badge on one page and an exercise heading on another, and only the
> render told them apart.)

**The author slot is not always an author.** ch 5 prints `સંકલિત`, ch 13 prints `લોકગીત` — a genre
label standing where a name usually stands — and ch 18 prints its poets' names *below each poem*
with no chapter-number box on the page at all. Std 6's ch 4 and std 8's ch 7 do the same thing with
`લોકગીત`. Never parse the slot as a name.

## સ્વાધ્યાય block names — per reader, as measured

Which list applies is decided by the **book**, not by the grade band, and the two families here are
genuinely different apparatus. Do not carry std-6 habits into a std-10 run.

### Std 6, 7 and 8 — the activity-first family

**No chapter in any of these three books prints a `સ્વાધ્યાય` banner.** Numbered pink headings begin
directly after the શબ્દાર્થ box. This is the single most important mechanical fact about the family:
**a pipeline keying on a "સ્વાધ્યાય" heading finds nothing.** Key on the numbered headings — in
practice on `1. વાતચીત` — and note that the books' own intro boxes nonetheless *call* the block
સ્વાધ્યાય, which is why the pack keeps the term.

Headings are re-worded per chapter rather than drawn from a fixed printed list, so what follows are
**families with measured frequencies**, not a template to fill:

| Block family (typical printed wording) | std 6 | std 7 | std 8 |
|---|---|---|---|
| વાતચીત — oral warm-up, **always block 1** | 15/15 | 15/15 | 15/15 |
| નીચેના પ્રશ્નોના ઉત્તર / જવાબ લખો. | 15/15 (+R1, R2) | 15/15 | 15/15 |
| **નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો.** — the L2 signature block | 15/15 | 10/15 | 15/15, **always the last numbered item** (ભાષાંતર chs 1–4, અનુવાદ chs 5–15) |
| શબ્દાર્થ box, before the exercises | 15/15 + પૂરકવાચન | 15/15 + P2–P4 | 15/15 + P1–P4 |
| ખાલી જગ્યા પૂરો (word-bank / paragraph cloze) | 12 + R1, R2 | ~9 | ~10 |
| ઉદાહરણ મુજબ… — the workhorse pattern-drill frame | every chapter, 2–5× | frequent | chs 4, 6, 7, 9, 12 |
| વાક્યો બનાવો (given words or word-pairs) | 10 | frequent | frequent |
| MCQ — ✓ કરો / સૌથી નજીકનો અર્થ / યોગ્ય વિકલ્પ | 8 | 5 | 8 (અ/બ/ક or અ/બ/ક/ડ) |
| જોડકાં જોડો / બે ભાગ જોડીને વાક્ય બનાવો | chs 3, 8, 9, 13, 14, 15 + R2 | 5 | — |
| ઘટનાક્રમ મુજબ ગોઠવો | chs 2, 13, 15 + R2 | chs 3, 7, 13 | — |
| કોણ બોલ્યું / કોણ બોલી શકે ? | chs 6, 8, 14 | chs 2, 3, 8, 10, 11 | — |
| શબ્દો આડાઅવળા → વાક્ય ફરીથી લખો | chs 5, 6, 8, 9, 12 | ch 6 | chs 1, 5, 6 |
| પ્રશ્ન બનાવો (કૌંસના શબ્દથી) | ch 3 | 8/15 | chs 3, 7, 8, 13 |
| ચિત્રવર્ણન — illustration or a real photograph | chs 4, 9, 14 + R1 | 6/15 | realia: જાહેરાત, બિલ, કંકોતરી, ટ્રાફિક ચિહ્નો (chs 3, 6, 7, 14) |
| નિબંધ / પત્ર / ફકરો / સંવાદ લખો | chs 3, 7, 8, 10, 12, 14, 15 | chs 5, 12, 15 | chs 8, 9, 11, 13, 15 |
| performance — સમૂહગાન, મુખરવાચન, નાટ્યીકરણ, અભિનય | 10 chapters | scattered | પ્રવૃત્તિ (chs 1, 7) |
| (જૂથકાર્ય) / (જોડીકાર્ય) tags | chs 1, 4, 6, 8, 11, 12 + R1 | ~10 | timed પ્રવૃત્તિ chs 2, 5, 15 |
| રૂઢિપ્રયોગ pre-block | chs 5, 6, 8, 10, 13, 15 | 8/15 (+P3) | 11/15 |
| શબ્દસમૂહ માટે એક શબ્દ pre-block | — | — | 8/15 |
| કહેવત pre-block | ch 6 only | — | ch 15 only |
| chapter-final grammar box with a printed topic banner | chs 2, 3, 4, 5, 7, 9 | 8/15 | — (grammar rides inside the exercises) |
| ચર્ચા-વિચારણા (yellow box, blue tab) | — | — | **15/15**, chapter-final |

**Four things in this family are not exercises and must not be answered as if they were:**

1. **The blue intro box** (std 6, 7, 8) is written *to the teacher* — `…કરાવવું`, `…ધ્યાન દોરવું`. It
   is the best genre signal on the page and it is apparatus. Inventory it, never solve it.
2. **Teacher-addressed items inside the numbered list.** Std 6 ch 1 block 12 begins
   `વિદ્યાર્થીઓનાં જૂથ પાડી…`, ch 5 block 6 begins `વર્ગમાં બેઠેલા વિદ્યાર્થીઓને વર્તુળમાં બેસાડો.` They are
   numbered like exercises and addressed to the teacher; record them, answer them as teaching
   notes, and never write a child's answer for them.
3. **Appended reading matter.** Std 6 ch 4's `ગાઈએ` poem; the fun boxes (humour, ઉખાણું, palindromes,
   name games); std 8 ch 12's second play excerpt and std 8 ch 1's embedded poem — the last two sit
   *inside* exercise blocks and belong to Agent 10 as exercise-internal material, never as chapter
   scenes.
4. **The QR badge.** Every chapter opener carries a QR block with a 6-character code
   (`2921F8`, `YSMSA7`, `E6C3E6`, `Z6R3F4` …). It is furniture: record it if useful, never treat it
   as content, and expect it to pollute the title zone of a render.

**Deliberate wrong-language exercises exist** — std 6 ch 6 block 13 (a child's mispronounced speech
to be corrected), R1 block 9 (misspelled conjuncts), R2 block 2. These are **content to transcribe
exactly as printed**, not extraction defects. Never "fix" them at ingestion.

### Std 9 and 10 — the exam-mirroring family

Both books **do** print a `સ્વાધ્યાય` banner, and the block set is close to fixed.

**Std 9**, per chapter, in order:

- **શબ્દ-સમજૂતી** (before the banner) with sub-heads as the chapter needs them: સમાનાર્થી/શબ્દાર્થ ·
  વિરુદ્ધાર્થી · તળપદા શબ્દો · રૂઢિપ્રયોગ · શબ્દસમૂહ માટે એક શબ્દ.
- **સ્વાધ્યાય** — a short answer-length ladder: `પ્રશ્નની નીચે આપેલા વિકલ્પોમાંથી સાચો વિકલ્પ પસંદ કરી ખરાની
  (✓) નિશાની કરો :` (3–5 MCQ, options (A)–(D)) → `બે-ત્રણ વાક્યોમાં ઉત્તર લખો :` →
  `પાંચ-છ` or `છ-સાત વાક્યોમાં ઉત્તર લખો :`. ch 2 adds a `કારણ આપો :` block.
- **વિદ્યાર્થી-પ્રવૃત્તિ** — student activities (not always present; ch 2 has none).
- **ભાષા-અભિવ્યક્તિ** — quote-led craft commentary. This is the block that pre-names devices.
- **શિક્ષકની ભૂમિકા** — teacher-addressed prose. **Neither a topic nor an exercise.**

**Std 10**, per chapter (verified on chs 1, 8, 13, 16):

- **શબ્દ-સમજૂતી** → **સમાનાર્થી શબ્દો / શબ્દાર્થ** → as the chapter needs: **તળપદા શબ્દો** ·
  **વિરુદ્ધાર્થી શબ્દો** · **રૂઢિપ્રયોગો** · **કહેવત** · **શબ્દસમૂહ માટે એક શબ્દ**.
- **સ્વાધ્યાય** — the four-tier board ladder: ✓-MCQ → `એક-એક વાક્યમાં ઉત્તર` → `બે-ત્રણ વાક્યમાં ઉત્તર` →
  `સવિસ્તર ઉત્તર`.
- **વિદ્યાર્થી-પ્રવૃત્તિ** → **ભાષા-અભિવ્યક્તિ** → **શિક્ષકની ભૂમિકા**.

> **Match these banners fuzzily.** The wording micro-varies chapter to chapter and the variation is
> printed, not scanned wrong: લખો vs આપો · વાક્યમાં vs વાક્યોમાં · **સવિસ્તર vs સવિસ્તાર** ·
> વિદ્યાર્થી પ્રવૃત્તિ vs વિદ્યાર્થી-પ્રવૃત્તિ. Std 9 ch 3 prints the singular `નીચેના પ્રશ્નનો…` where its
> neighbours print the plural, and ch 6 drops the `નીચેના પ્રશ્નોના` prefix entirely. `prompt_verbatim`
> copies what the page prints; the *matcher* is what tolerates the drift.

**વ્યાકરણ એકમો are apparatus, not chapters** (std 9: V1–V4; std 10: six units). They carry no
literature, they weave their exercises into the exposition, and std 9's V1 **prints its own answers
inline** (`ઉત્તર જોઈએ :`). They also recycle sentences from the literature chapters as examples —
cross-references, not new content. And V1 puts un-bracketed Roman on the page
(`English Alphabet`, `Dictionary`, `Authorisation`): that is printed content, transcribed as
printed, and the one legitimate exception to the Roman-only-in-brackets rule for `original_chunk`.

## The text layer — image-only in all five books

**There is no text layer in any std 6–10 PDF.** Not a corrupted one, not a legacy-encoded one:
none. Every page must be rendered and read. This makes the pack's verbatim discipline simpler to
state and harder to shortcut — the rendered printed page is the sole authority, and there is
nothing to cross-check it against (no v1 corpus exists for Gujarati).

**Rendering practice, measured:** `pdftoppm` at **100 dpi** is legible for body text and exercises;
**150–200 dpi** is needed for author lines, small glosses and tight conjuncts. At 100 dpi ધ/ઘ and
ળ/ય are genuinely confusable — std 7's ch 6 author read as `ઘોકાઈ` at 100 dpi and resolved to
`ધોકાઈ` at 200. Delete per-unit renders as each unit is recorded; a stale batch from an interrupted
session was found once and the discipline is what prevented it recurring.

**Defect catalogue — built fresh from these books, and it will grow:**

| # | What it looks like | Where measured | What to do |
|---|---|---|---|
| 1 | `મેં` renders with a Devanagari-looking glyph (`में`) | std 6 ch 3; std 8 ch 3; std 9 chs 2, 4 | Transcribe as `મેં`. It is an anusvāra + e-mātrā at low dpi, not Devanagari |
| 2 | Two-column verse with (or without) a divider rule | std 6 ch 7, P1 | Read columns **down**, never across |
| 3 | Refrain printed as shorthand + ellipsis (`— એક જ.`, `પ્રભુ હે…`, `– હો ભેરુ.`) | std 6 chs 1, 7; std 7 ch 5; std 8 chs 1, 7 | The ellipsis means *repeat the refrain*. `original_chunk` transcribes **what is printed**; expand only against page evidence |
| 4 | Refrain cue typeset to the right of each line (`– સમી સાંજની`) | std 10 ch 13 | Must not be merged into the verse line |
| 5 | Verse set with wide per-character letter-spacing | std 10 ch 7 (સૉનેટ) | OCR inserts spurious spaces; a human read is the only fix |
| 6 | QR block + 6-char code intruding into the title zone or the intro box | all books; std 10 ch 5 wraps text around it | Read around it; never transcribe the code as content |
| 7 | Printed numbering defects | std 7 ch 6 (two `10.`), ch 8 (3 → 5); std 8 ch 14 (5 → 7), chs 2 & 12 (two `2.`) | Inventory what is printed. A never-printed block is not an unanswered block |
| 8 | Mixed numeral scripts in one list (`1., ૨., 3.`) | std 8 chs 2, 12, 13 | Transcribe as printed |
| 9 | Answer-line prefixes that look like serials (`જ.` = જવાબ) and ruled blank lines | std 8 chs 8, 9; R2 | Ruled lines are not em-dashes |
| 10 | Devanagari quoted deliberately inside the Gujarati reader | std 8 P4 | Legitimate printed content; the purity check allows quoted blocks |
| 11 | Roman-script islands printed by the book | std 6 ch 15 (`Assocoation`, sic), R2 (`Hello/Hi`); std 9 V1; std 10 chs 8, 11 | Transcribe as printed, typo included |
| 12 | Spaced question mark (`પહોંચાય ?`) and spaced exclamation | all books | A printed convention, not a defect. **The full stop is `.`** — the book teaches it as પૂર્ણવિરામ (std 7 ch 2's વિરામચિહ્નો table). Never introduce `।` |
| 13 | Duplicate scan pages inside a split file | std 7 `99-shabdsidi.pdf` pdf 134–139 | Unique content is pdf 133 and 140 only |

## SSC board-exam weighting — std 10

Std 10 is a board year and the exercise deliverable stops being polish.

- **The paper is 80 external + 20 internal, roughly 30 % objective items, in four sections:**
  **વિભાગ A ગદ્ય (20) · B પદ્ય (20) · C વ્યાકરણ (20) · D લેખન (20)**.
  ⚠ **[thin]** — this skeleton comes from the research summary (`PEDAGOGY.md` §1, std 10) and the
  SL-specific mark split is **not verified**. Ingest the official *10th Gujarati (S.L.) Blueprint*
  PDF from gseb.org before hard-coding any number here.
- **The book is built to that shape.** Six વ્યાકરણ એકમો interleaved through the reader feed section C
  directly (સમાનાર્થી/વિરુદ્ધાર્થી/જોડણી · સંધિ-સમાસ · રૂઢિપ્રયોગ-કહેવત · વાક્યપ્રકાર-વિશેષણ ·
  વિરામચિહ્નો-વાર્તાલેખન · અહેવાલલેખન-સંક્ષેપીકરણ-અર્થવિસ્તાર-નિબંધલેખન), and every chapter's સ્વાધ્યાય runs
  the four-tier answer ladder the paper uses.
- **What this means for the pack:** `exercise_solutions.json` is produced **with** the chapter, not
  after the class, and is at least as important as the teaching plan at this band. The ladder tier
  is part of the answer — a `સવિસ્તર` item answered at `એક વાક્ય` length is a wrong answer, not a
  short one.
- **Board convention: idiom, proverb and objective items are drawn "from the textbook."** So the
  per-chapter રૂઢિપ્રયોગ / કહેવત / શબ્દસમૂહ માટે એક શબ્દ inventories are exam material, not decoration.
  Harvest them per chapter; never source them from a generic list.
- **Human review gates auto-generated assessment items** at this band — purely linguistic MCQ and
  matching items, and anything involving છંદ syllable counts, are not auto-publishable
  (`PEDAGOGY.md` §4.7).

## Corrections log

Every correction to this file gets a line: **what changed · the date · the page evidence.** The
Hindi pack's log entries do not transfer; the practice does. A correction without page evidence is
a guess with a date on it.

| Date | What | Evidence | Status |
|---|---|---|---|
| 2026-08-22 | Std-10 ch 18's manifest names the poet **ઝિલિપ ક્લાર્ક**; the printed page reads **ફિલિપ ક્લાર્ક** (Philip Clark) | render of printed pp. 102–106 (`reference/corpus/std-10_inventory.md` §3) | **Open** — fix the manifest; this profile deliberately carries no poet names, so nothing here inherits the error |
| 2026-08-22 | Std-10 ch 6: manifest prints `સામગ્રી તો સમાજની છે ને ?`, the inventory's printed-title column reads `સામગ્રી તો સમાજની છે ને !` | conflict between `manifest.json` and the ch-6 render (printed p. 29) | **Open** — settle on a fresh render before the title goes into `chapter_name` |
| 2026-08-22 | Std-9 inventory status line says "8 of 31 units recorded"; seven unit records exist (ch 1–6, V1) | `reference/corpus/std-9_inventory.md` | **Closed** (2026-08-22) — the inventory was completed the same day (`Status: 31 of 31 units recorded — COMPLETE`); this profile's std-9 table was backfilled from it |
