import json,os,re
D=os.path.dirname(os.path.abspath(__file__))
L=lambda n: json.load(open(os.path.join(D,n),encoding='utf-8'))
plan=L('13_merged.json'); pub=L('16_publication.json'); auth=L('12_authoring.json')
topics=[t for m in plan['modules'] for s in m['segments'] for t in s['topics']]
pubt={t['topic_id']:t for t in pub['topics']}
out=[]
# 1 publication_chunk prefix exactness + composition
for t in topics:
    oc,pc=t['original_chunk'],t['publication_chunk']
    if not pc.startswith(oc): out.append(('FAIL',f"{t['topic_id']}: publication_chunk does not open with byte-identical original_chunk"))
    tail=pc[len(oc):]
    if not tail.startswith('\n\n'): out.append(('WARN',f"{t['topic_id']}: tail separator not blank line"))
    if t['publication_text'] not in pc: out.append(('WARN',f"{t['topic_id']}: publication_text not contained in publication_chunk"))
# 2 concept publication index/count match
for t in topics:
    pt=pubt.get(t['topic_id'],{})
    pcs={c['concept_id']:c for c in pt.get('concepts',[])}
    cp=pt.get('concept_publication',[])
    npara=0
    for c in t['concepts']:
        src=pcs.get(c['concept_id'])
        if src is None: out.append(('FAIL',f"{c['concept_id']}: no publication concept entry")); continue
        if len(src['content'])!=len(c['content']):
            out.append(('FAIL',f"{c['concept_id']}: publication content count {len(src['content'])} != plan {len(c['content'])}"))
        for i,b in enumerate(c['content']):
            if b.get('type')=='paragraph':
                npara+=1
                if not (b.get('publication_text') or '').strip(): out.append(('FAIL',f"{c['concept_id']}.content[{i}]: empty publication_text"))
            else:
                if 'publication_text' in b: out.append(('WARN',f"{c['concept_id']}.content[{i}]: publication_text on a non-paragraph block"))
    ncp=len([x for x in cp])
    if ncp!=npara: out.append(('FAIL',f"{t['topic_id']}: concept_publication entries {ncp} != paragraph blocks {npara}"))
    for e in cp:
        cc=next((c for c in t['concepts'] if c['concept_id']==e['concept_id']),None)
        if cc is None: out.append(('FAIL',f"concept_publication points at unknown {e['concept_id']}")); continue
        i=e['content_index']
        if i>=len(cc['content']) or cc['content'][i].get('type')!='paragraph':
            out.append(('FAIL',f"{e['concept_id']}.content_index {i} is not a paragraph block"))
        elif cc['content'][i].get('publication_text')!=e['publication_text']:
            out.append(('FAIL',f"{e['concept_id']}.content[{i}] publication_text != concept_publication entry"))
# 3 vocative sweep across ALL publication surfaces
VOC=['બાળકો','જુઓ —','બોલો','જુઓ,','ચાલો,']
for t in topics:
    fields=[('publication_text',t['publication_text']),('publication_chunk_tail',t['publication_chunk'][len(t['original_chunk']):])]
    for c in t['concepts']:
        for i,b in enumerate(c['content']):
            if b.get('publication_text'): fields.append((f"{c['concept_id']}.content[{i}]",b['publication_text']))
    for k,s in fields:
        for v in VOC:
            if v in s: out.append(('FAIL' if v in ('બાળકો','જુઓ —','બોલો') else 'WARN',f"{t['topic_id']}.{k}: vocative {v!r}"))
# 4 root keys
NEED=set("board genre grade level phase author modules plan_id subject version textbook _activate medium_id chapter_id objectives unit_title topic_title unit_number chapter_name textbook_url topic_number teaching_lens estimated_time publication_id subject_ref_id textbook_pages english_plan_id guiding_question chapter_master_id english_chapter_id strand_to_objective_map".split())
miss=NEED-set(plan.keys()); extra=set(plan.keys())-NEED-{'ordering'}
if miss: out.append(('FAIL',f"root keys missing: {sorted(miss)}"))
if extra: out.append(('FAIL',f"unexpected root keys: {sorted(extra)}"))
if 'ordering' in plan: out.append(('WARN',"'ordering' present — Agent 14/15 owns it"))
# 5 topic key whitelist
TK=set("media 2d_tool summary concepts topic_id key_terms depends_on difficulty topic_name topic_type word_count explanation brief_summary objective_ids modified_chunk original_chunk topic_category concept_bullets detailed_summary important_points publication_text recall_questions source_topic_ids publication_chunk real_life_example estimated_exchanges learning_objectives primary_content_type tertiary_content_type secondary_content_type available_content_types figures_of_speech rhyme_scheme shabdarth samanarthi vilom vyakaran".split())
for t in topics:
    ex=set(t)-TK; mi=set("topic_id topic_name topic_type original_chunk explanation real_life_example concepts media".split())-set(t)
    if ex: out.append(('FAIL',f"{t['topic_id']}: non-contract topic keys {sorted(ex)}"))
    if mi: out.append(('FAIL',f"{t['topic_id']}: missing topic keys {sorted(mi)}"))
# 6 module extras
for m in plan['modules']:
    out.append(('INFO',f"{m['module_id']}: difficult_words={len(m.get('difficult_words') or [])} overall_rhyme_scheme={'yes' if m.get('overall_rhyme_scheme') else 'no'}"))
    if not (5<=len(m.get('difficult_words') or [])<=10): out.append(('WARN',f"{m['module_id']}: difficult_words count out of 5–10"))
# 7 working-field sweep
BAD=re.compile(r'"(avoid_checks|match_score|reuse_score|validation_flags|transcription_note|pitfall|severity|confidence|notes)"')
s=json.dumps(plan,ensure_ascii=False)
hits=sorted(set(BAD.findall(s)))
if hits: out.append(('FAIL',f"working fields carried into 13_merged.json: {hits}"))
# 8 word_count sanity
for t in topics:
    wc=t.get('word_count')
    if not isinstance(wc,dict) or 'original' not in wc: out.append(('FAIL',f"{t['topic_id']}: word_count shape"))
# 9 figures_of_speech / rhyme_scheme presence
out.append(('INFO',f"figures_of_speech present on {sum(1 for t in topics if 'figures_of_speech' in t)}/{len(topics)}; all empty: {all(not t.get('figures_of_speech') for t in topics)}"))
out.append(('INFO',f"rhyme_scheme present on {sum(1 for t in topics if t.get('rhyme_scheme'))}/{len(topics)}"))
out.append(('INFO',f"bhasha extras: {sorted({k for t in topics for k in ('shabdarth','samanarthi','vilom','vyakaran') if k in t})}"))
out.append(('INFO',f"2d_tool values: {sorted({str(t.get('2d_tool')) for t in topics})}"))
for lv,msg in out: print(lv,'|',msg)
