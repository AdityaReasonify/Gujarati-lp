export const meta = {
  name: 'gujarati-cultural-grounding',
  description: 'Add a Gujarat cultural anchor bank and wire it through voice, authoring, media and tier prompts',
  phases: [
    { title: 'Anchor bank', detail: 'author reference/gujarat_cultural_anchors.md' },
    { title: 'Wire in', detail: 'voice + author.md, agent 12, agent 09, student tier prompts' },
    { title: 'Check', detail: 'check_pack + dangling-reference sweep' },
  ],
}

const GUJ = '/Users/aditya/Downloads/Gujarati-lp/gujarati-lp'
const BANK = `${GUJ}/reference/gujarat_cultural_anchors.md`

const COMMON = `You are editing the gujarati-lp pack (GSEB Gujarati second language, std 6-10) at ${GUJ}. Goal of this change set: make everything the pipeline GENERATES feel specifically GUJARATI — Gujarat's own festivals, landscape, livelihoods, crafts, folk forms and everyday child life — instead of generic-Indian. Mechanism prose stays English; all child-facing example text is Gujarati script.

Non-negotiables that this change must NOT weaken:
- No-hallucination rules and verbatim rules are untouched. A cultural anchor illustrates the text's FEELING; it never adds claims about the text, the poet, or the chapter.
- Still exactly ONE real_life_example per scene, still inside the child's own experience, still in band (55-90 words).
- Anchors must be INCLUSIVE of the whole state, not one slice: Saurashtra, Kutch, North/Central/South Gujarat, coastal and tribal (ડાંગ, ભીલ, રાઠવા), urban (અમદાવાદ, સુરત, વડોદરા, રાજકોટ) and rural; and of communities — Hindu, Muslim (વ્હોરા, ખોજા, મેમણ), Jain, Parsi (સુરત/નવસારી), Christian, Sikh. Never imply "Gujarati = businessman", never make every festival a Hindu one, never reduce a community to a costume.
- Age-ladder the anchors: std 6-7 immediate and sensory (પતંગ, વરસાદ, આંબો, શેરી ક્રિકેટ); std 9-10 may reach civic/abstract (સ્થળાંતર, ઉદ્યોગ, પર્યાવરણ, નર્મદા યોજના).`

const FILE_SCHEMA = { type: 'object', additionalProperties: false, required: ['file','key_decisions','open_questions'], properties: {
  file: {type:'string'}, key_decisions: {type:'array', items:{type:'string'}}, open_questions: {type:'array', items:{type:'string'}} } }

phase('Anchor bank')
const bank = await agent(`${COMMON}

Your file: ${BANK} — a NEW reference doc: the Gujarat cultural anchor bank that Agents 9, 12 and 16 draw on. First read ${GUJ}/reference/teaching_voice_gu.md and ${GUJ}/reference/global_content_rules.md so your file agrees with them, and skim two corpus inventories in ${GUJ}/reference/corpus/ so your anchors match what these books actually talk about.

Structure the file as:
1. **Why this file exists** — a child recognises their own world faster than a generic one; an anchor from Gujarat's own life makes the text land. Plus the anti-stereotype and inclusivity rules above.
2. **The anchor bank**, organised by domain, each entry in Gujarati script with a one-line note on what feeling/idea it can carry and which std band it suits. Cover at least: તહેવાર-ઉત્સવ (ઉત્તરાયણ-પતંગ, નવરાત્રિ-ગરબા, દિવાળી-બેસતું વર્ષ, હોળી-ધુળેટી, રથયાત્રા, ઈદ, પર્યુષણ, નાતાલ, તરણેતર/ભવનાથ/વૌઠાનો મેળો); ખાનપાન (થેપલા, ઢોકળા, ખાખરા, ઊંધિયું, બાજરીનો રોટલો, છાશ, શ્રીખંડ); ભૂગોળ-કુદરત (નર્મદા, સાબરમતી, ગિરનાર, સાપુતારા, કચ્છનું સફેદ રણ, ગીરનું જંગલ અને સિંહ, દરિયાકિનારો, વાવ, ખેતર-કૂવો, ચોમાસું); કામ-આજીવિકા (ખેડૂત, માલધારી-રબારી-ભરવાડ, માછીમાર, અગરિયા, વણકર, સુરતનો હીરા-કાપડ ઉદ્યોગ, દૂધમંડળી, ST બસ, ફેરિયો); હસ્તકલા (પટોળા, બાંધણી, કચ્છી ભરત, અજરખ, રોગાન, માટીકામ, ડાંગનું વાંસકામ); લોકકલા (ગરબા, રાસ, ભવાઈ, ડાયરો, ભજન, દુહા, લોકગીત); બાળકનું રોજિંદું જીવન (શેરી ક્રિકેટ, પતંગ-ફિરકી, લખોટી, ગિલ્લી-દંડા, સાયકલ, નિશાળનો રિસેસ, બળદગાડું, આંગણું); વ્યક્તિ-સંદર્ભ used ONLY when the chapter itself invites it (ગાંધીજી, સરદાર પટેલ, નરસિંહ મહેતા, મીરાંબાઈ, મેઘાણી, વિક્રમ સારાભાઈ).
3. **How to choose one** — a short decision procedure: match the text's FEELING first, then the child's std band, then vary across a chapter so every scene is not a festival; prefer the ordinary (વરસાદ, રિસેસ, આંગણું) over the spectacular.
4. **Worked examples** — 4-5 short model real_life_example openings in Gujarati (one verse, one story, one prose/essay, one દુહો), each showing the anchor doing real work, with a matched BAD version and one line on why it fails (decorative, adult, generic-Indian, or stereotyping).
5. **Anti-patterns** — the tokenism list, plus "no anchor at all is better than a forced one".

Return the structured report.`,
  { label: 'write:gujarat_cultural_anchors.md', phase: 'Anchor bank', schema: FILE_SCHEMA, effort: 'high', model: 'fable' })

phase('Wire in')
const EDITS = [
  { key: 'voice+author', prompt: `Edit TWO existing files so they route to the new anchor bank at ${BANK} (read it first):
(1) ${GUJ}/reference/teaching_voice_gu.md — in its real-life-anchor section, make Gujarat-specific anchoring the DEFAULT rather than a permitted flavour: cite the bank as the source, keep the one-anchor rule and the bands, and add 2-3 fresh Gujarati calibration samples (good vs bad) that show a Gujarat anchor carrying a feeling. Also add one short paragraph on register: natural spoken શિષ્ટ ગુજરાતી may use everyday Gujarati idiom the child hears at home, while staying standard.
(2) ${GUJ}/author.md — in commitment 3 (explain, then land it in the child's own world), state that the child is a Gujarati child and the anchor comes from Gujarat's own life, citing the bank; keep the commitment's existing argument and length. Use Edit for surgical changes; do not rewrite either file wholesale.` },
  { key: 'agent12', prompt: `Edit ${GUJ}/agents/12_runtime_authoring.md (read it and ${BANK} first). Changes: real_life_example must be chosen from the Gujarat anchor bank's domains using its decision procedure (cite reference/gujarat_cultural_anchors.md by path); add the vary-across-the-chapter rule so a chapter's scenes do not all land on festivals; add the std-band ladder for anchor abstraction; keep every existing band, the one-example rule, the no-hallucination and no-forced-બોધ rules untouched. Also note that concept prose and recall questions may use Gujarat-familiar situations for their scenarios where that helps comprehension. Surgical Edits only.` },
  { key: 'agent09', prompt: `Edit ${GUJ}/agents/09_media_planning.md (read it and ${BANK} first). Changes: every authored generation_prompt must depict a recognisably GUJARATI visual world where the scene allows — architecture (પોળનું મકાન, નળિયાંવાળું ઘર, વાવ, ચબૂતરો), dress (કેડિયું-ધોતિયું, ચણિયાચોળી, કચ્છી ભરતકામ, સાદો શર્ટ-પેન્ટ for a modern classroom), landscape (ખેતર, ગિરનાર, દરિયાકિનારો, રણ, ચોમાસું), objects (બળદગાડું, માટલું, પતંગ-ફિરકી, ST બસ) — chosen to fit the chapter's own setting, never bolted on when the text is set elsewhere. Add: when the chapter is NOT set in Gujarat, keep the setting faithful to the text (fidelity beats flavour). Keep the self-contained-prompt rules, the one-image-per-scene limit, the narrator-bar Gujarati string rule, and extend the negative_prompt baseline with "generic Bollywood styling, north-Indian-only architecture" alongside the existing entries. Surgical Edits only.` },
  { key: 'students', prompt: `Edit all five files ${GUJ}/profiles/students/std-6.md … std-10.md (read one fully plus ${BANK} first). In EACH file: add a short "Cultural anchoring for this standard" subsection naming which anchor domains suit this std band (sensory/immediate at 6-7 → civic/abstract at 9-10) with 3-4 concrete Gujarati examples per file, and add one line to each of the three tier prompt blocks instructing the tutor to anchor examples in Gujarat's own world per reference/gujarat_cultural_anchors.md, with the સહાય tier using the most familiar/concrete anchors and પ્રગત able to handle less common ones. Keep every existing tier descriptor, band and prompt intact — additive edits only. Return one report covering all five files.` },
]

const wired = []
for (let i = 0; i < EDITS.length; i += 2) {
  const wave = await parallel(EDITS.slice(i, i + 2).map(e => () =>
    agent(`${COMMON}\n\n${e.prompt}\n\nReturn the structured report (file = the file or files you edited).`,
      { label: `edit:${e.key}`, phase: 'Wire in', schema: FILE_SCHEMA, effort: 'high', model: 'fable' })))
  wired.push(...wave)
  log(`Wire-in wave ${i / 2 + 1}/2 done`)
}

phase('Check')
const check = await agent(`Verify the cultural-grounding change set in ${GUJ}. (1) Run: python3 ${GUJ}/check_pack.py — it must exit 0; if a path is dangling because the new reference/gujarat_cultural_anchors.md is cited wrongly anywhere, fix the citing file. (2) Confirm every file that now cites the anchor bank uses its real path. (3) Spot-check that no edit weakened a no-hallucination, verbatim, one-example or band rule — read the changed sections of agents/12, agents/09 and reference/teaching_voice_gu.md and report anything that reads as a loosened constraint (fix it if clearly wrong). (4) Confirm the anchor bank itself is inclusive per the rules (regions, communities, urban+rural) and flag any stereotyping you find. Return what you checked, what you fixed, and the final check_pack exit status.`,
  { label: 'verify-cultural-changeset', phase: 'Check', schema: FILE_SCHEMA, effort: 'high', model: 'fable' })

return { bank: bank && bank.file, wired: wired.filter(Boolean).map(w => w.file), check }