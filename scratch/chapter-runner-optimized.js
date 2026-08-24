export const meta = {
  name: 'gujarati-lp-chapter-runner-optimized',
  description: 'Resume-aware pipeline with invariant-first prompt ordering, tiered context routing, shared page renders and pre-resolved paths',
  phases: [{ title: 'Chapters', detail: 'groups of N chapters; dependency-parallel agents; completed stages skipped' }],
}

const GUJ = '/Users/aditya/Downloads/Gujarati-lp/gujarati-lp'
const PDFS = '/Users/aditya/Downloads/Gujarati-lp/Textbooks-pdf'
const STD = (args && args.std) || 6
const CHAPTERS = (args && args.chapters) || []
const CONC = (args && args.concurrency) || 3

const STEP_SCHEMA = { type: 'object', additionalProperties: false, required: ['ok','outputs','notes'], properties: {
  ok: {type:'boolean'}, outputs: {type:'array', items:{type:'string'}}, notes: {type:'array', items:{type:'string'}} } }
const VALID_SCHEMA = { type: 'object', additionalProperties: false, required: ['status','owner','notes'], properties: {
  status: {type:'string', enum:['pass','fail']}, owner: {type:['string','null'], enum:['A1','A2',null]}, notes: {type:'array', items:{type:'string'}} } }
const QC_SCHEMA = { type: 'object', additionalProperties: false, required: ['status','blockers','owner_reruns','notes'], properties: {
  status: {type:'string', enum:['pass','fail']}, blockers: {type:'array', items:{type:'string'}},
  owner_reruns: {type:'array', items:{type:'string'}}, notes: {type:'array', items:{type:'string'}} } }

// ── O1: INVARIANT PREFIX ───────────────────────────────────────────────────────
// Byte-identical for every agent of every chapter, so one cache entry serves the
// whole run instead of ~255 separate cache-creation events. Nothing here may
// reference a chapter, a path, or a spec — those live in the variable tail.
const INVARIANT = `You are executing ONE agent of the gujarati-lp pipeline (GSEB Gujarati second language).

CONSTITUTION — these outrank every instruction that follows.
- Never fabricate. [] and null are correct answers. An empty result beats an invented one.
- Verbatim Gujarati is TRANSCRIPTION from page renders, never recall, never paraphrase.
- Mechanism prose is English; all child-facing text is Gujarati script.
- Read your agent spec IN FULL before doing any work, and follow its inputs, outputs and do-nots exactly.
- Write ONLY your own declared output files. Never edit another agent's file. Other agents of this
  same chapter may be running CONCURRENTLY. Treat every file you did not declare as read-only input.
- A chapter may be RESUMED: outputs from earlier agents may already exist. Never redo another agent's work.
- Page renders are provided for you already rasterised. Do NOT re-run pdftoppm; read the PNGs that exist.
- Return ok=true only if every declared output file was actually written.

CONTEXT ROUTING: you are given exactly the policy documents your spec requires. If your spec cites a
document you were not given, say so in notes and stop rather than guessing at its contents.`

// ── O2: TIERED CONTEXT ROUTING ─────────────────────────────────────────────────
// Derived from what each spec actually cites. Tier 0 is the floor every agent gets.
const T0 = ['reference/no_hallucination_policy.md', 'reference/global_content_rules.md']
const NEEDS = {
  '01_ingestion_genre_diagnosis.md': [...T0, 'author.md'],
  '02_structure.md':                 [...T0, 'reference/explanation_unit_map.md', 'reference/teaching_lens_map.md'],
  '04_mapping_convergence.md':       [...T0, 'reference/loop_protocol.md', 'reference/explanation_unit_map.md', 'reference/naming_conventions.md', 'reference/phase2_contract.md'],
  '05_verbatim_attachment.md':       [...T0, 'author.md', 'reference/gujarati_verbatim.md', 'reference/shabd_gloss.md'],
  '07_genre_pitfalls.md':            [...T0, 'author.md'],
  '08_sensitivity_safety.md':        [...T0],
  '09_media_planning.md':            [...T0, 'author.md', 'reference/gujarat_cultural_anchors.md'],
  '10_exercise_solutions.md':        [...T0, 'author.md'],
  '11_pagination_source.md':         [...T0],
  '12_runtime_authoring.md':         [...T0, 'author.md', 'reference/teaching_voice_gu.md', 'reference/gujarat_cultural_anchors.md', 'reference/field_shape_rules.md'],
  // A13 named these four itself when they were missing — it read them off disk rather
  // than guessing, which is the stop-and-report clause working. Routing them removes
  // the rediscovery cost on every chapter.
  '13_assembly_validation.md':       [...T0, 'reference/qc_checklist.md', 'reference/json_contract.md', 'reference/phase2_contract.md', 'reference/field_shape_rules.md'],
  '14_logical_plan.md':              [...T0, 'reference/json_contract.md', 'reference/phase2_contract.md'],
  '15_textbook_plan.md':             [...T0],
  '16_publication_authoring.md':     [...T0, 'author.md', 'reference/teaching_voice_gu.md'],
}

// QC and validation agents name an owner loosely: "agents/12_authoring.md",
// "12_authoring.md", "A12". Only the leading two digits are reliable, so resolve
// on those and drop anything that does not map to a real spec file.
const SPECS = Object.keys(NEEDS)
const resolveSpec = (raw) => {
  const m = String(raw || '').match(/(\d\d)/)
  if (!m) return null
  return SPECS.find(x => x.startsWith(m[1])) || null
}

phase('Chapters')
const report = []

const runChapter = async (entry) => {
  const ch = entry.ch
  const done = new Set(entry.done || [])
  const skip = (s) => done.has(s)
  const chDir = `${GUJ}/output${STD}/ch${String(ch).padStart(2,'0')}`
  const renders = `${chDir}/_renders`
  const label = (a) => `s${STD}ch${String(ch).padStart(2,'0')}:${a}`

  // ── O4 + O5: deterministic preprocessing, once per chapter, on the cheap model.
  // Rasterise every page ONCE into a shared dir, and resolve the genre profile paths
  // up front so no downstream agent re-reads _genre_index.md to find them.
  const setup = await agent(`Phase 0 setup for gujarati-lp: std ${STD} chapter ${ch}.
1. Read ${PDFS}/std-${STD}/manifest.json, find the numbered chapter whose "no" is "${ch}"; note its "file" and title.
2. Create ${chDir}, ${renders} and ${GUJ}/book/ if missing; copy the chapter PDF into ${GUJ}/book/ unless already there.
3. Rasterise ONCE for the whole chapter: pdftoppm -png -r 150 <chapter.pdf> ${renders}/page
   Then verify the PNG count matches the PDF page count. These renders are SHARED by every agent
   of this chapter — no agent re-renders. If ${renders} already holds a full set, skip this step.
4. If ${chDir}/01_meta.json already exists, read its active_genre_profiles and resolve each to an
   absolute path under ${GUJ}/profiles/genres/. Otherwise return an empty list.
5. Update ${GUJ}/output${STD}/batch_state.json: set in_progress=${ch} (create the file if absent).
Return ok, outputs=[absolute chapter PDF path, title, "${renders}", <comma-joined absolute genre profile paths or "">], notes.`,
    { label: label('setup'), phase: 'Chapters', schema: STEP_SCHEMA, effort: 'low', model: 'sonnet' })
  if (!setup || !setup.ok) { return { ch, status: 'setup-failed' } }
  const pdf = setup.outputs[0]
  const genrePaths = (setup.outputs[3] || '').split(',').map(s => s.trim()).filter(Boolean)

  // Variable tail — everything that differs per agent goes AFTER the invariant block.
  const A = (spec, extra, opts) => {
    const docs = (NEEDS[spec] || T0).map(d => `${GUJ}/${d}`)
    const pixels = (opts && opts.pixels)
    const tail = `
── RUN CONTEXT ──
std ${STD}, chapter ${ch}, tier ધોરણ (default).
Output directory: ${chDir}
Page renders (already rasterised, shared, do not re-render): ${renders}
Source PDF (reference only): ${pdf}
${genrePaths.length ? `Active genre profile(s), already resolved — read these directly, do not consult profiles/genres/_genre_index.md:\n${genrePaths.map(p => '  ' + p).join('\n')}` : ''}

── READ THESE, IN FULL, BEFORE WORKING ──
Your agent spec: ${GUJ}/agents/${spec}
Policy documents your spec requires:
${docs.map(d => '  ' + d).join('\n')}

── SOURCE OF TRUTH FOR CHAPTER TEXT ──
${pixels
  ? `You need the pixels: read the PNGs in ${renders} directly. Cross-check anything you transcribe against the render.`
  : `Use ${chDir}/00_chapter_normalized.md — the verbatim transcription A1 produced from these renders. It is the authoritative chapter text. Read a PNG from ${renders} ONLY if you hit something the transcription cannot answer (a layout or figure question), and say in notes why you needed it.`}
${extra || ''}

Write your declared output files into ${chDir}.`
    return agent(INVARIANT + tail,
      { label: label(spec.slice(0,2)), phase: 'Chapters', schema: (opts && opts.schema) || STEP_SCHEMA,
        effort: (opts && opts.effort) || 'high', model: (opts && opts.model) || 'opus' })
  }

  // ---- Phase 1 ----
  if (!skip('A1')) {
    const a1 = await A('01_ingestion_genre_diagnosis.md',
      'Select the genre profile(s) via profiles/genres/_genre_index.md and record active_genre_profiles in 01_meta.json.',
      { pixels: true })
    if (!a1 || !a1.ok) { return { ch, status: 'A1-failed', notes: a1 && a1.notes } }
  }

  // ---- Wave 1: A2→A4 chain ∥ A11 ----
  const needChain = !skip('A4'), needA11 = !skip('A11')
  let a4res = { status: 'pass', owner: null, notes: [] }
  if (needChain || needA11) {
    const w = await parallel([
      async () => {
        if (!needChain) return { status: 'pass', owner: null, notes: [] }
        if (!skip('A2')) await A('02_structure.md', 'Read 00_chapter_normalized.md + 01_meta.json + the resolved genre profile(s) + reference/explanation_unit_map.md + reference/teaching_lens_map.md.', {})
        // ── O3: A4 no longer re-emits a byte-copy of 02_structure.json.
        let v = await A('04_mapping_convergence.md',
          `Emit 04_validation.json with your verdict. On pass, emit 04_converged.json as a CONVERGENCE RECORD, not a copy:
{"converged":true,"source":"02_structure.json","sha256":"<sha256 of 02_structure.json>","verdict":"pass","notes":[...]}.
Downstream agents read 02_structure.json for structure and 04_converged.json only to confirm convergence.
Do NOT duplicate the structure payload — it already exists on disk and copying it doubles every downstream read.`,
          { schema: VALID_SCHEMA })
        if (v && v.status === 'fail' && v.owner) {
          const notes = JSON.stringify(v.notes)
          if (v.owner === 'A1') {
            // reference/loop_protocol.md's A1 remedy is "re-diagnose, reload profile, THEN A2
            // again". Re-running A1 alone leaves 02_structure.json cut against the SUPERSEDED
            // diagnosis, so the validator re-checks byte-identical structure and fails a second
            // time — burning the one permitted retry. Proven on std-7 ch04 and ch06 (2026-08-24):
            // ch06's 02_structure.json had the same sha256 across both passes.
            await A('01_ingestion_genre_diagnosis.md',
              `RE-RUN after validation failure. Blocking notes: ${notes}. Fix exactly these, re-emit your outputs.`,
              { pixels: true })
            await A('02_structure.md',
              `RE-CUT against the CORRECTED 01_meta.json, which Agent 1 has just re-emitted. Its genre, active_genre_profiles, explanation_unit and teaching_lens may all have changed — re-read it and re-cut from scratch rather than adjusting the previous tree. The validator's blocking notes were: ${notes}`,
              {})
          } else {
            await A('02_structure.md',
              `RE-RUN after validation failure. Blocking notes: ${notes}. Fix exactly these, re-emit your outputs.`, {})
          }
          v = await A('04_mapping_convergence.md', 'REVALIDATION (second and final pass). Emit 04_validation.json and, on pass, the convergence record 04_converged.json.', { schema: VALID_SCHEMA })
        }
        return v
      },
      async () => { if (needA11) return A('11_pagination_source.md', '', { model: 'sonnet', effort: 'medium', pixels: true }); return null },
    ])
    if (needChain) a4res = w[0]
  }
  if (!a4res || a4res.status === 'fail') { return { ch, status: 'validation-failed', notes: a4res && a4res.notes } }

  // ---- Phase 4: verbatim (needs pixels by definition) ----
  if (!skip('A5')) {
    const a5 = await A('05_verbatim_attachment.md', 'Verbatim = transcription cross-checked against the 150 dpi renders.', { pixels: true })
    if (!a5 || !a5.ok) { return { ch, status: 'A5-failed', notes: a5 && a5.notes } }
  }

  // ---- Wave 2 ----
  const w2 = []
  if (!skip('A7')) w2.push(() => A('07_genre_pitfalls.md', '', {}))
  if (!skip('A8')) w2.push(() => A('08_sensitivity_safety.md', '', { model: 'sonnet', effort: 'medium' }))
  if (w2.length) await parallel(w2)

  // ---- Wave 3: A9 ∥ A10 ∥ (A12 → A16) ----
  // A12 reads 01/05/07/08 only — it cites NEITHER 09_media.json NOR 10_exercise_solutions.json
  // (verified: zero references in agents/12_runtime_authoring.md). A10 is the slowest stage in the
  // pipeline at ~36 min median, so gating A12 behind it added ~16 min to every chapter's critical
  // path for no dependency reason. Only A13 needs all three, and it still joins them below.
  const w3 = []
  if (!skip('A9')) w3.push(() => A('09_media_planning.md', 'Reuse step is dormant: every scene gets image_url:"" + authored generation_prompt.', {}))
  if (!skip('A10')) w3.push(() => A('10_exercise_solutions.md', 'Answer EVERY block in 01_meta.json exercise_inventory.', {}))
  w3.push(async () => {
    // A12 feeds A16, A13, A14 and A15. If it silently fails, QC fails on "12_authoring.json does
    // not exist" and every downstream agent burns a full run against missing input.
    if (!skip('A12')) {
      let a12 = await A('12_runtime_authoring.md', `Apply the std-${STD} ધોરણ tier descriptor from profiles/students/std-${STD}.md to every block you author.`, { effort: 'xhigh' })
      const wrote12 = a12 && a12.ok && (a12.outputs || []).some(o => String(o).includes('12_authoring.json'))
      if (!wrote12) {
        log(`ch${ch}: A12 did not report 12_authoring.json — retrying once before the authoring layer proceeds`)
        a12 = await A('12_runtime_authoring.md', `RETRY. The previous A12 run did not produce 12_authoring.json. Author it in full now: every topic needs explanation, real_life_example, summaries, concept_bullets, important_points and recall_questions. Apply the std-${STD} ધોરણ tier descriptor from profiles/students/std-${STD}.md.`, { effort: 'xhigh' })
        if (!a12 || !a12.ok) return { fatal: 'A12-failed', notes: a12 && a12.notes }
      }
    }
    // A16 feeds publication_text / publication_chunk into A13's merge. If it dies
    // terminally (429 exhaustion returns null), A13 merges empty publication fields and
    // reports a block — exactly what happened to std-6 ch10. Same guard as A12.
    if (!skip('A16')) {
      let a16 = await A('16_publication_authoring.md', '', {})
      const wrote16 = a16 && a16.ok && (a16.outputs || []).some(o => String(o).includes('16_publication.json'))
      if (!wrote16) {
        log(`ch${ch}: A16 did not report 16_publication.json — retrying once before QC`)
        a16 = await A('16_publication_authoring.md', 'RETRY. The previous A16 run did not produce 16_publication.json. Emit it in full now — every topic needs its publication_text and publication_chunk.', {})
        if (!a16 || !a16.ok) return { fatal: 'A16-failed', notes: a16 && a16.notes }
      }
    }
    return { fatal: null }
  })
  const w3res = await parallel(w3)
  const authFail = (w3res || []).find(r => r && r.fatal)
  if (authFail) return { ch, status: authFail.fatal, notes: authFail.notes }


  // ---- Phase 7 ----
  let a13 = { status: 'pass', blockers: [], owner_reruns: [], notes: [] }
  if (!skip('A13')) {
    a13 = await A('13_assembly_validation.md', 'Emit 13_merged.json + validation_report.md. Return fail if any hard (A-D) item blocks, listing blockers and the owner agent spec filename for each.', { schema: QC_SCHEMA })
    if (a13 && a13.status === 'fail' && a13.owner_reruns && a13.owner_reruns.length) {
      const owners = a13.owner_reruns.slice(0, 3).map(resolveSpec).filter(Boolean)
      const dropped = a13.owner_reruns.slice(0, 3).filter(x => !resolveSpec(x))
      if (dropped.length) log(`ch${ch}: QC named unresolvable owner(s) ${JSON.stringify(dropped)} — skipped`)
      if (owners.length) await parallel(owners.map(spec => () =>
        A(spec, `RE-RUN after QC failure. Blockers assigned to you: ${JSON.stringify(a13.blockers)}. Fix exactly these.`,
          { pixels: spec.startsWith('01') || spec.startsWith('05') })))
      a13 = await A('13_assembly_validation.md', 'RE-QC after owner re-runs (final pass). Emit updated 13_merged.json + validation_report.md.', { schema: QC_SCHEMA })
    }
  }
  if (!skip('A14')) await A('14_logical_plan.md', 'Emit learning_plan_logical.json. Then copy 10_exercise_solutions.json to exercise_solutions.json and render exercise_solutions.md.', {})
  // A15 (learning_plan_textbook.json) is DISABLED by request, 2026-08-23. Nothing consumes
  // its output: only agents/15 references it, and A13/A14/LP2 never read it. 05b_textbook_order
  // .json still comes from A5, so re-enabling later needs only this line back.
  // if (!skip('A15')) await A('15_textbook_plan.md', 'Emit learning_plan_textbook.json (raise human_confirmation_required if orders identical).', {})

  const v = await agent(`Phase 8 for gujarati-lp std ${STD} ch ${ch}: POST ${chDir}/learning_plan_logical.json as multipart field "file" to https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate (no auth; retry twice on network failure — staging DNS is flaky). Append the result (zero or listed validation_errors, or UNREACHABLE) to ${chDir}/validation_report.md under "## LP2 validator" and return ok=true only if validation_errors is empty. Do NOT upload — validation only.`,
    { label: label('lp2'), phase: 'Chapters', schema: STEP_SCHEMA, effort: 'low', model: 'sonnet' })

  const status = (a13 && a13.status === 'pass') ? ((v && v.ok) ? 'complete' : 'complete-lp2-pending') : 'qc-failed'
  await agent(`Update ${GUJ}/output${STD}/batch_state.json: move ${ch} from in_progress to done (status "${status}"), set in_progress null. Append one row to ${GUJ}/output${STD}/batch_report.md (create with a header table if missing): chapter ${ch} | status ${status} | qc ${a13 && a13.status} | lp2 ${v && v.ok}. Return ok.`,
    { label: label('state'), phase: 'Chapters', schema: STEP_SCHEMA, effort: 'low', model: 'sonnet' })
  log(`Chapter ${ch}: ${status}`)
  return { ch, status, qc: a13 && a13.status, lp2: v && v.ok, notes: ((a13 && a13.notes) || []).slice(0,3) }
}

const good = (r) => r && (r.status === 'complete' || r.status === 'complete-lp2-pending')
for (let i = 0; i < CHAPTERS.length; i += CONC) {
  const group = CHAPTERS.slice(i, i + CONC)
  log(`Running chapters ${group.map(g => g.ch).join(', ')} concurrently (${CONC}-way)`)
  const res = (await parallel(group.map(e => () => runChapter(e)))).filter(Boolean)
  report.push(...res)
  log(`Group done: ${res.map(r => r.ch + '=' + r.status).join(', ')}`)
  if (res.filter(good).length === 0) { log('ENTIRE GROUP FAILED — stopping batch'); break }
}
return { std: STD, report }
