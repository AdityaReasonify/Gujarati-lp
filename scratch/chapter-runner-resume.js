export const meta = {
  name: 'gujarati-lp-chapter-runner-resume',
  description: 'Resume the gujarati-lp pipeline: skip per-chapter stages already on disk, run chapters in concurrent groups',
  phases: [{ title: 'Chapters', detail: 'groups of N chapters concurrently; independent agents inside each chapter also run concurrently; completed stages skipped' }],
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

const base = (ch, chDir, pdf, extra) => `You are executing ONE agent of the gujarati-lp pipeline (GSEB Gujarati second language). Pack root: ${GUJ}. Run context: std ${STD}, chapter ${ch}, tier ધોરણ (default). Chapter source PDF: "${pdf}" — IMAGE-ONLY, render pages with pdftoppm -png -r 150 into a scratch subdir named run-s${STD}c${ch}-<your agent number> and Read the PNGs (you read Gujarati). Output directory: ${chDir} (create if missing; prior agents' outputs are there).

Other agents of this same chapter may be running CONCURRENTLY: write ONLY your own declared output files, never edit another agent's file, and keep your scratch subdir unique to you.

MANDATORY reading before work: your agent spec file (below) IN FULL, plus ${GUJ}/author.md, ${GUJ}/reference/no_hallucination_policy.md, ${GUJ}/reference/global_content_rules.md, ${GUJ}/reference/teaching_voice_gu.md. Follow the spec exactly — its inputs, its outputs, its do-nots. Never fabricate; [] and null are correct answers; verbatim Gujarati is transcription from renders. ${extra || ''}

This chapter is being RESUMED: some earlier agents' outputs already exist in ${chDir}. Treat any file you did not declare as read-only input. Do not redo another agent's work.

Write your declared output files into ${chDir}. Return ok=true only if every declared output was written.`

phase('Chapters')
const report = []

const runChapter = async (entry) => {
  const ch = entry.ch
  const done = new Set(entry.done || [])
  const skip = (s) => done.has(s)
  const chDir = `${GUJ}/output${STD}/ch${String(ch).padStart(2,'0')}`
  const label = (a) => `s${STD}ch${String(ch).padStart(2,'0')}:${a}`

  const setup = await agent(`Phase 0 setup for gujarati-lp run: std ${STD} chapter ${ch}. Read ${PDFS}/std-${STD}/manifest.json, find the numbered chapter whose "no" is "${ch}", note its "file" and title. Create directory ${chDir} and ${GUJ}/book/ if missing; copy the chapter PDF from ${PDFS}/std-${STD}/ into ${GUJ}/book/ (skip the copy if it is already there). Update ${GUJ}/output${STD}/batch_state.json: read it if it exists (else start {"std":${STD},"done":[],"in_progress":null,"pending":[]}), set in_progress=${ch}, write it back. Return ok, outputs=[the chapter PDF's ABSOLUTE path in Textbooks-pdf, the title], notes.`,
    { label: label('setup'), phase: 'Chapters', schema: STEP_SCHEMA, effort: 'low', model: 'sonnet' })
  if (!setup || !setup.ok) { return { ch, status: 'setup-failed' } }
  const pdf = setup.outputs[0]

  const A = (spec, extra, opts) => agent(base(ch, chDir, pdf, extra) + `\n\nYour agent spec: ${GUJ}/agents/${spec}`,
    { label: label(spec.slice(0,2)), phase: 'Chapters', schema: (opts && opts.schema) || STEP_SCHEMA,
      effort: (opts && opts.effort) || 'high', model: (opts && opts.model) || 'opus' })

  // ---- Phase 1 (critical path) ----
  if (!skip('A1')) {
    const a1 = await A('01_ingestion_genre_diagnosis.md', 'Also load the genre profile(s) your diagnosis selects from profiles/genres/ (via profiles/genres/_genre_index.md) and record active_genre_profiles in 01_meta.json.', {})
    if (!a1 || !a1.ok) { return { ch, status: 'A1-failed', notes: a1 && a1.notes } }
  } else { log(`ch${ch}: skip A1 (on disk)`) }

  // ---- Wave 1: A2→A4 chain ∥ A11 ----
  const needChain = !skip('A4'), needA11 = !skip('A11')
  let a4res = { status: 'pass', owner: null, notes: [] }
  if (needChain || needA11) {
    const waveRes = await parallel([
      async () => {
        if (!needChain) return { status: 'pass', owner: null, notes: [] }
        if (!skip('A2')) await A('02_structure.md', 'Read 00_chapter_normalized.md + 01_meta.json + the active genre profile(s) + reference/explanation_unit_map.md + reference/teaching_lens_map.md.', {})
        let v = await A('04_mapping_convergence.md', 'Emit 04_validation.json AND (on pass) 04_converged.json. Return status/owner per your spec.', { schema: VALID_SCHEMA })
        if (v && v.status === 'fail' && v.owner) {
          const spec = v.owner === 'A1' ? '01_ingestion_genre_diagnosis.md' : '02_structure.md'
          await A(spec, `RE-RUN after validation failure. The validator's blocking notes: ${JSON.stringify(v.notes)}. Fix exactly these, re-emit your outputs.`, {})
          v = await A('04_mapping_convergence.md', 'REVALIDATION (second and final pass). Emit 04_validation.json and on pass 04_converged.json.', { schema: VALID_SCHEMA })
        }
        return v
      },
      async () => { if (needA11) return A('11_pagination_source.md', '', { model: 'sonnet', effort: 'medium' }); return null },
    ])
    if (needChain) a4res = waveRes[0]
  } else { log(`ch${ch}: skip A2/A4/A11 (on disk)`) }
  if (!a4res || a4res.status === 'fail') { return { ch, status: 'validation-failed', notes: a4res && a4res.notes } }

  // ---- Phase 4: verbatim ----
  if (!skip('A5')) {
    const a5 = await A('05_verbatim_attachment.md', 'Verbatim = transcription cross-checked against renders at 150 dpi.', {})
    if (!a5 || !a5.ok) { return { ch, status: 'A5-failed', notes: a5 && a5.notes } }
  } else { log(`ch${ch}: skip A5 (on disk)`) }

  // ---- Wave 2: A7 ∥ A8 ----
  const w2 = []
  if (!skip('A7')) w2.push(() => A('07_genre_pitfalls.md', '', {}))
  if (!skip('A8')) w2.push(() => A('08_sensitivity_safety.md', '', { model: 'sonnet', effort: 'medium' }))
  if (w2.length) await parallel(w2)

  // ---- Wave 3: A9 ∥ A10 ----
  const w3 = []
  if (!skip('A9')) w3.push(() => A('09_media_planning.md', 'Reuse step is dormant: every scene gets image_url:"" + authored generation_prompt.', {}))
  if (!skip('A10')) w3.push(() => A('10_exercise_solutions.md', 'Answer EVERY block in 01_meta.json exercise_inventory.', {}))
  if (w3.length) await parallel(w3)

  // ---- Phase 6 ----
  if (!skip('A12')) await A('12_runtime_authoring.md', `Apply the std-${STD} ધોરણ tier descriptor from profiles/students/std-${STD}.md to every block you author.`, { effort: 'xhigh' })
  if (!skip('A16')) await A('16_publication_authoring.md', '', {})

  // ---- Phase 7: QC gate ----
  let a13 = { status: 'pass', blockers: [], owner_reruns: [], notes: [] }
  if (!skip('A13')) {
    a13 = await A('13_assembly_validation.md', 'Emit 13_merged.json + validation_report.md. Return status fail if any hard (A-D) item blocks, listing blockers and the owner agent spec filename for each.', { schema: QC_SCHEMA })
    if (a13 && a13.status === 'fail' && a13.owner_reruns && a13.owner_reruns.length) {
      await parallel(a13.owner_reruns.slice(0, 3).map(spec => () =>
        A(spec, `RE-RUN after QC failure. Blockers assigned to you: ${JSON.stringify(a13.blockers)}. Fix exactly these.`, {})))
      a13 = await A('13_assembly_validation.md', 'RE-QC after owner re-runs (final pass). Emit updated 13_merged.json + validation_report.md.', { schema: QC_SCHEMA })
    }
  }
  if (!skip('A14')) await A('14_logical_plan.md', 'Emit learning_plan_logical.json. Then copy 10_exercise_solutions.json to exercise_solutions.json and render exercise_solutions.md.', {})
  if (!skip('A15')) await A('15_textbook_plan.md', 'Emit learning_plan_textbook.json (raise human_confirmation_required if orders identical).', {})

  // ---- Phase 8: LP2 validator ----
  const v = await agent(`Phase 8 for gujarati-lp std ${STD} ch ${ch}: POST ${chDir}/learning_plan_logical.json as multipart field "file" to https://staging.singularity-learn.com/agentapi/api/lp2/learning-plans/validate (no auth; retry twice on network failure — staging DNS is flaky). Append the result (zero or listed validation_errors, or UNREACHABLE) to ${chDir}/validation_report.md under "## LP2 validator" and return ok=true only if validation_errors is empty (ok=false with the errors in notes otherwise; UNREACHABLE is ok=false with note). Do NOT upload — validation only.`,
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
  if (res.filter(good).length === 0) {
    log('ENTIRE GROUP FAILED — stopping batch; the pack needs a fix before more chapters are spent')
    break
  }
}
return { std: STD, report }
