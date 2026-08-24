export const meta = {
  name: 'gujarati-grounding-opus-pass',
  description: 'Upgrade the Fable-authored cultural grounding content to Opus quality, without duplicating or weakening rules',
  phases: [{ title: 'Upgrade' }, { title: 'Verify' }],
}

const GUJ = '/Users/aditya/Downloads/Gujarati-lp/gujarati-lp'
const BANK = `${GUJ}/reference/gujarat_cultural_anchors.md`

const FILE_SCHEMA = { type: 'object', additionalProperties: false, required: ['file','key_decisions','open_questions'], properties: {
  file: {type:'string'}, key_decisions: {type:'array', items:{type:'string'}}, open_questions: {type:'array', items:{type:'string'}} } }

const COMMON = `You are improving the gujarati-lp pack (GSEB Gujarati second language, std 6-10) at ${GUJ}.

CONTEXT: the Gujarat cultural-grounding change set has ALREADY been applied end to end by an earlier, weaker model. The anchor bank exists at ${BANK} and is already cited from author.md, reference/teaching_voice_gu.md, agents/09_media_planning.md, agents/12_runtime_authoring.md and profiles/students/std-6..10.md. Your job is a QUALITY UPGRADE of that existing prose, not a re-application of the change set.

HARD RULES:
- This is an EDIT-IN-PLACE upgrade. NEVER add a second copy of a section that already exists. Before writing, read the file and locate the existing grounding text; improve THAT text in place with surgical Edits.
- Do NOT weaken or restate any existing constraint: the no-hallucination gates, verbatim rules, the one-real_life_example-per-scene rule, the 55-90 word band, the tier descriptors and every band already in the file stay exactly as they are.
- Mechanism prose stays English; all child-facing example text stays Gujarati script.
- Anchors stay INCLUSIVE across the whole state (Saurashtra, Kutch, North/Central/South, coastal, tribal - ડાંગ/ભીલ/રાઠવા, urban and rural) and across communities (Hindu, Muslim - વ્હોરા/ખોજા/મેમણ, Jain, Parsi, Christian, Sikh). Never "Gujarati = businessman", never every festival Hindu, never a community reduced to a costume.
- Age-ladder holds: std 6-7 immediate and sensory; std 9-10 may reach civic/abstract.

WHAT "BETTER" MEANS HERE: sharper and more concrete Gujarati example sentences; anchors that carry the FEELING of a text rather than decorating it; worked examples whose BAD counterpart fails for a clearly-named reason; decision procedures a tutor can actually follow; no padding, no restating a rule already stated elsewhere in the pack. If a section is already good, say so and leave it alone - returning "no change needed" is a correct outcome.`

phase('Upgrade')
const TARGETS = [
  { key: 'bank', prompt: `Upgrade ${BANK} itself. Read it fully first. Focus on: (a) the worked examples section - each model real_life_example opening must be genuinely good Gujarati prose a std-6 child would recognise, with its BAD counterpart failing for a named reason (decorative / adult / generic-Indian / stereotyping); (b) the "how to choose one" decision procedure - make it a procedure someone can execute, not advice; (c) coverage gaps or any entry that is a bare noun with no note on what feeling it can carry. Keep the file's structure and its "supplies material, changes no rule" stance.` },
  { key: 'voice+author+agents', prompt: `Upgrade the grounding sections ONLY inside these four files: ${GUJ}/reference/teaching_voice_gu.md, ${GUJ}/author.md, ${GUJ}/agents/12_runtime_authoring.md, ${GUJ}/agents/09_media_planning.md. Read each and locate the cultural-anchoring text already added. Improve the calibration samples in teaching_voice_gu.md (good vs bad must teach something, not just differ), tighten commitment 3 in author.md, and make the anchor-selection instructions in agents/12 and the Gujarati visual-world instructions in agents/09 concrete enough that an agent cannot produce generic output while following them. Do not restructure the files.` },
  { key: 'students', prompt: `Upgrade the "Cultural anchoring for this standard" subsections and the anchor lines inside the tier prompt blocks across all five files ${GUJ}/profiles/students/std-6.md through std-10.md. Read std-6 and std-10 fully first to feel the ladder. Make each file's anchor examples genuinely specific to that age band and clearly different from its neighbours - std-6 must not read like std-10 with words swapped. Keep every existing tier descriptor, band and prompt intact; additive/surgical edits only. Return one report covering all five files.` },
]

const upgraded = await parallel(TARGETS.map(t => () =>
  agent(`${COMMON}\n\n${t.prompt}\n\nReturn the structured report (file = the file or files you edited; key_decisions = what you changed and what you deliberately left alone).`,
    { label: `opus:${t.key}`, phase: 'Upgrade', schema: FILE_SCHEMA, effort: 'high', model: 'opus' })))

phase('Verify')
const check = await agent(`Verify the cultural-grounding content in ${GUJ} after an Opus quality pass. (1) Run: python3 ${GUJ}/check_pack.py - it must exit 0; fix any dangling citation. (2) Confirm NO section was duplicated by the upgrade pass - specifically check reference/gujarat_cultural_anchors.md, reference/teaching_voice_gu.md, author.md, agents/09_media_planning.md, agents/12_runtime_authoring.md and profiles/students/std-6..10.md for repeated headings or repeated near-identical paragraphs, and remove any duplicate you find. (3) Confirm no no-hallucination, verbatim, one-example or word-band rule was weakened or dropped. (4) Confirm the anchor bank is still inclusive across regions and communities. Report what you checked, what you fixed, and the final check_pack exit status.`,
  { label: 'verify-opus-pass', phase: 'Verify', schema: FILE_SCHEMA, effort: 'high', model: 'fable' })

return { upgraded: upgraded.filter(Boolean).map(u => u.file), check }
