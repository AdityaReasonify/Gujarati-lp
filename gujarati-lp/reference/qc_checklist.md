# QC Checklist (Step 8) — Agent 13's gate

Sections **A–D are hard fails** and block the run. **E–G are reported** in
`validation_report.md` and fixed where cheap.

> **Provisional items this checklist enforces WITH their warnings.** The word-count bands in §C are
> carried over from the first-language pack and await **VERIFY-4**; the `chapter_id` board/medium
> segments in §F await **VERIFY-1**. §A's roster is **no longer provisional**: all five inventories
> (`reference/corpus/std-6_inventory.md` … `std-10_inventory.md`) are complete and were read off
> rendered pages, and the roster below is the seventeen profiles in `profiles/genres/`, indexed by
> `profiles/genres/_genre_index.md`. Author to these rules as written; when a verification lands, the
> file that owns the fact is fixed first and this one follows.

## A — Diagnosis and lens (hard)
- [ ] સ્વરૂપ diagnosed from the four signals **off the rendered page** (the PDFs are image-only),
      recorded with `genre_signals` and `genre_confidence`; where the blue intro box or the
      કૃતિ-પરિચય named the form, that line is quoted — as evidence, never as the verdict.
- [ ] The **explanation unit matches the સ્વરૂપ**, per this roster — one line per profile file, and
      a form not named here is a **sub-form** held by one of them (`profiles/genres/_genre_index.md`):
      પદ/ભજન — one whole પદ, never split · દુહો/છપ્પો/મુક્તક/હાઈકુ/શ્લોક-સંચય — one printed piece per
      topic, never merged · ગઝલ — one શેર · સૉનેટ — one ભાવ-ખંડ, the ચોટ never split, never cut
      couplet-wise · ઊર્મિકાવ્ય-ગીત / લોકગીત / પ્રાર્થનાકાવ્ય — one કડી, or one refrain-round where the
      song cycles · કથાકાવ્ય — one વાર્તા-પગલું cut at a printed કડી boundary · અછાંદસ — one
      વિચાર-એકમ · ઉખાણું/શબ્દરમત — one piece, and a list-shaped set is ONE topic · વાર્તા (લોકકથા,
      પૌરાણિક કથા, લઘુકથા, નવલકથાખંડ સહિત) — one ઘટના · ચરિત્ર/રેખાચિત્ર/પ્રસંગકથા — one પ્રસંગ or one
      printed person-section · આત્મપરક/લલિત નિબંધ (સંસ્મરણ, આત્મકથાખંડ, હાસ્યનિબંધ/હાસ્યલેખ સહિત) —
      one પ્રસંગ કે વિચારનો એક વળાંક, and in the હાસ્ય sub-form one રમૂજ-વળાંક never cut from its setup ·
      સંવાદ-નિબંધ / વિચારપ્રધાન નિબંધ — one move of the argument · માહિતીપ્રદ-સાંસ્કૃતિક ગદ્ય —
      one માહિતી-ખંડ · પત્ર/પ્રવાસ — one પડાવ · નાટક/એકાંકી — one stage-beat.
- [ ] **ટેક handled as content, not repetition:** an identical ટેક taught at first occurrence and
      referenced after; a changed-words ટેક a topic at **each** occurrence, naming what changed.
- [ ] A mixed chapter loaded every profile and **cut each part under its own unit** — the appended
      "ગાઈએ" poem, verse quoted inside a ચરિત્ર, a લઘુકાવ્યો page of દુહા + મુક્તક + હાઈકુ.
- [ ] **Apparatus did not become a reading scene:** the blue intro box, the શબ્દાર્થ / શબ્દ-સમજૂતી
      box, the રૂઢિપ્રયોગ / કહેવત pre-blocks, the chapter-final green ભાષા-બોધ box,
      ભાષા-અભિવ્યક્તિ and શિક્ષકની ભૂમિકા are teacher-addressed matter. Std 9–10's કવિ/લેખક-પરિચય
      and કૃતિ-પરિચય, printed **for the student**, may be a CONCEPT topic.
- [ ] The revision checkpoints (આગળ વધતાં પહેલાં, પૂર્ણ કરતાં પહેલાં) and the std 9–10 વ્યાકરણ
      એકમો carry **no topics at all** — they hold no reading text.
- [ ] `guiding_question` derived from THIS chapter, never copied from the profile — and reading the
      topics' explanations in order actually answers it.

## B — Verbatim and structure (hard)
- [ ] Every topic has an exact **Gujarati-script** `original_chunk` (U+0A80–0AFF), **transcribed from
      the rendered page**; nothing paraphrased, transliterated, modernised, or "corrected"
      (`મ્હારે`, `ઓતર`, `દખ્ખણ`, `ડેડકડી`, `વજોગણ`, `લો'તાં` intact; the છાપ intact —
      `બાઈ મીરાં કે…`, `ભણે નરસૈંયો`).
- [ ] **No Roman and no Devanagari** anywhere outside bracketed technical terms —
      `સજીવારોપણ (personification)` is the only permitted shape.
- [ ] **Printed non-Gujarati script is quoted content, and is whitelisted, not purged.** The measured
      cases: std-8 P4 વિવિધા ભારતી prints Sanskrit, Hindi, Marathi and old Punjabi-Hindi verse in
      Devanagari with a Gujarati સમજૂતી under each; std-9 V2–V4 print ગુજરાતી/हिन्दी/English
      comparison tables and a trilingual કહેવત table; std-9 ch 9 carries Roman English dialogue
      lines; std-10 ch 11 sets "Wall to wall" inside the verse and std-10 ch 7's own શબ્દ-સમજૂતી
      prints the Roman word "line". Each is copied exactly as printed, recorded in
      `extraction_notes[]`, and never replaced by a Gujarati rendering — a script-purity failure
      raised against one of these is a false positive.
- [ ] માત્રા, અનુસ્વાર, ચંદ્રબિંદુ and જોડાક્ષર (`ક્ષ જ્ઞ ત્ર શ્ર દ્વ`) preserved; `ળ`/`લ` and
      `શ`/`ષ`/`સ` not levelled into each other; the printed `.` full stop kept and **no `।`
      introduced anywhere**.
- [ ] Verse line breaks preserved and two-column verse read **down each column, never across**; the
      printed refrain shorthand (`- એક જ.`, `– સમી સાંજની`) copied as printed, not expanded; the
      attribution line `— કવિ/લેખકનું નામ` inside the **last** topic's `original_chunk`.
- [ ] Corruption told from licence: a moved or detached માત્રા (`િક` for `કિ`, `છ ે` for `છે`) is an
      extraction bug that was re-read off the render — never taught as a poet's form.
- [ ] Header furniture never entered the text: the chapter-number box, the QR badge and its Latin
      code string, the running footers.
- [ ] Every reading scene became a topic, in order; **no સ્વાધ્યાય block became a topic**; every
      `[[…]]` marker count equals the count of topics carrying it.
- [ ] Ids consecutive and every cross-reference resolves after Agent 14's renumber.

## C — The teaching block (hard)
- [ ] Every topic has `explanation` **and** `real_life_example`, both non-empty.
- [ ] `explanation` gives શું થઈ રહ્યું છે + અર્થ, glosses hard words **at the point of first use**,
      and adds the deeper reading **only where the passage carries it**.
- [ ] **L2 calibration held:** glossing density up and the "everyday word, skip it" bar down — a word
      an L2 child would hesitate on (`આભ`, `હામ`, `વેળા`) is glossed even though it is ordinary
      Gujarati; one new thing per sentence; the gloss is in Gujarati; no Hindi word standing in for a
      Gujarati one.
- [ ] `real_life_example` is **Indian, concrete, single, and inside this standard's reach** — ઘર,
      વર્ગખંડ, શેરી, રમત at std 6; ઉત્તરાયણ, મેળો, ST બસ, ખેતર-કૂવો in the middle stds; પોતાના
      નિર્ણય, સમાજ at std 10. Not an adult's example, not an abstraction, not three examples — and
      not an anchor that needs its own glossary.
- [ ] Voice: સરળ બોલચાલની **શિષ્ટ ગુજરાતી**, second person, **55–90 words**; `objective_text`
      **12–30 words**. ⚠ Bands provisional until VERIFY-4 — **trim prose to the band, never widen the
      band to fit the prose.**
- [ ] Craft named only where this standard may name it: પ્રાસ as a *sound* at std 6–7; structure as
      play at std 8; the named અલંકાર canon from std 9; છંદ **only** at std 10.

## D — સ્વરૂપ essence (hard)
- [ ] The active profile's **avoid** list is not violated anywhere.
- [ ] **No બોધ forced** onto a text that does not carry one, and no explanation that turns into
      ઉપદેશ. If the conclusion could be printed on a classroom poster, it is wrong.
- [ ] A ભક્તિ પદ keeps its ભાવ; a દુહો keeps its દૃષ્ટાંત; a લોકગીત keeps its તળપદી diction and its
      occasion; a ગઝલ's શેર stay independent of one another; a સૉનેટ's ચોટ stays whole and its turn
      is named where it happens; an ઉખાણું keeps its answer out of everything but the recall answer;
      a હાસ્યલેખ stays funny; a
      વીરરસ-કથા keeps its ઓજ; a સાંસ્કૃતિક description keeps the community's dignity and its real
      name (ડાંગ, રબારી, ભરવાડ, કચ્છ — never "tribal people").
- [ ] `figures_of_speech` names only devices genuinely in the lines, quoting words found verbatim in
      that topic's `original_chunk`; `[]` where there are none.

## E — સ્વાધ્યાય and risk (reported)
- [ ] Every inventoried સ્વાધ્યાય block answered, skill-tagged, mapped to the topics that prepare it
      — std 6–8's numbered blocks (વાતચીત always first) through the standing
      **નીચેનાં વાક્યોનો તમારી પ્રથમ ભાષામાં અનુવાદ કરો**, and std 10's four-tier ladder
      (✓-વિકલ્પ → એક-એક વાક્યમાં → બે-ત્રણ વાક્યમાં → સવિસ્તર) plus વિદ્યાર્થી-પ્રવૃત્તિ and
      ભાષા-અભિવ્યક્તિ. Headings come from `01_meta.json`'s inventory, matched fuzzily —
      લખો/આપો, વાક્યમાં/વાક્યોમાં and સવિસ્તર/સવિસ્તાર drift chapter to chapter.
- [ ] Personal-opinion, પ્રવૃત્તિ, જૂથકાર્ય and teacher-addressed items marked as model answers —
      answered with teaching values, never skipped as "not answerable".
- [ ] Empty tables and printed grids filled with teaching values.
- [ ] Unmapped blocks reported as unmapped; a mapping was never invented to close the report.
- [ ] Sensitivity notes applied where the chapter touches ધર્મ, સમુદાય, ક્ષેત્ર, વિકલાંગતા, સંઘર્ષ,
      જાતિ-ભૂમિકા or સુરક્ષા — flagged and guided, never censored.

## F — Shape and media (reported)
- [ ] The 12 `json_contract.md` invariants hold.
- [ ] `publication_id` is set (not null); `topic_type` is `instructional`/`summary`/`assessment`;
      segment recalls are `.RQ{n}` not `.SR{n}`; concept numbers run chapter-continuous. These four
      were each rejected by the server on the first real run of the parallel Hindi pack — they are
      **shape**, not board values, so they carry to GSEB unchanged.
- [ ] `chapter_id` is `gseb_eng_gujarati{grade}_ch{unit_number}` and `plan_id` is
      `{chapter_id}_v{version}`. ⚠ The board/medium segments are provisional until VERIFY-1: a wrong
      medium uploads **clean** and mis-files the plan.
- [ ] One image per reading scene; ≤1 `2d_tool` per chapter.
- [ ] **No Gujarati frame pool exists yet** — every scene carries `image_url: ""` **and** a real,
      self-contained `generation_prompt`, and `reuse_report` reports `reused: 0`. Once a pool exists,
      a reused image names its source frame in `teaching_notes`.
- [ ] `negative_prompt` carries `Devanagari script labels`; a narrator bar names the **exact**
      Gujarati string to render.
- [ ] Three-tier summaries strictly increase; **no numbers in display text** — `બીજી કડીમાં`, never
      `કડી 2માં`.

## G — The seven mistakes a Gujarati plan usually makes (reported)
1. સાર + બોધ + પ્રશ્નોત્તર instead of teaching the સ્વરૂપ.
2. દુહા merged into one "કડી" topic — a લઘુકાવ્યો page of independent poems fused into one poem.
3. A પદ split line by line, or its ટેક lifted out as a topic of its own.
4. A poetic licence silently corrected — `ડેડકડી` printed as `દેડકી`, `ઓતર` as `ઉત્તર`,
   `મ્હારે` as `મારે`.
5. An અલંકાર named because the field existed, not because it was there.
6. A `real_life_example` written for an adult, set outside India, or pitched at std 10 inside a
   std-6 plan.
7. સ્વાધ્યાય cut as teaching topics, leaving the exercise deliverable half-empty.

## Verdict
`validation_report.md` records: **સ્વરૂપ: <genre> (confidence)**, the pass/fail of A–D with the
failing item named, the E–G notes, the media summary, and the LP2 validator result. **A run with any
A–D failure is not complete**, however good the rest looks — and a partial pass is never presented
as a pass.
