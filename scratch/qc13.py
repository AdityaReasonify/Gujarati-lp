import json,os,re,unicodedata
D='/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch07'
L=lambda f: json.load(open(os.path.join(D,f)))
plan=L('13_merged.json'); meta=L('01_meta.json'); base=L('05_with_content.json')
auth=L('12_authoring.json'); ex=L('10_exercise_solutions.json'); med=L('09_media.json')
pit=L('07_pitfalls.json'); sen=L('08_sensitivity.json')
norm=open(os.path.join(D,'00_chapter_normalized.md')).read()
FAIL=[];WARN=[];INFO=[]
def f(sec,msg,owner): FAIL.append((sec,msg,owner))
def w(msg): WARN.append(msg)

topics=[t for m in plan['modules'] for s in m['segments'] for t in s['topics']]
segs=[s for m in plan['modules'] for s in m['segments']]

# ---- markers
mk=re.findall(r'\[\[(કડી|દુહો|પદ|ઘટના)[^\]]*\]\]',norm)
kadi=len(re.findall(r'\[\[કડી\s',norm)); tek=len(re.findall(r'\[\[ટેક\]\]',norm))
carr={}
for bt in [t for m in base['modules'] for s in m['segments'] for t in s['topics']]:
    for x in bt.get('markers',[]): carr[x]=carr.get(x,0)+1
INFO.append(f'markers in 00: કડી={kadi} ટેક={tek}; markers carried by topics={sum(carr.values())} {sorted(carr)}')
if kadi!=len([k for k in carr if k.startswith('[[કડી')]): f('B',f'કડી marker count {kadi} != topics carrying કડી markers {len([k for k in carr if k.startswith("[[કડી")])}','02_structure.md')
sv=re.findall(r'\[\[સ્વાધ્યાય[^\]]*\]\]',norm)
INFO.append(f'સ્વાધ્યાય markers in 00: {len(sv)}')
for bt in [t for m in base['modules'] for s in m['segments'] for t in s['topics']]:
    for x in bt.get('markers',[]):
        if 'સ્વાધ્યાય' in x: f('B',f'{bt["topic_id"]} carries a સ્વાધ્યાય marker','02_structure.md')

# ---- script checks
GUJ=lambda ch: 0x0A80<=ord(ch)<=0x0AFF
DEV=re.compile(r'[ऀ-ॿ]')
ROM=re.compile(r'[A-Za-z]')
DIG=re.compile(r'[0-9૦-૯]')
DANDA='।'
def strip_bracketed(s): return re.sub(r'\([^)]*\)','',s)
display_fields=['topic_name','explanation','real_life_example','brief_summary','summary',
                'detailed_summary','publication_text']
def walk_strings(o,path=''):
    if isinstance(o,str): yield path,o
    elif isinstance(o,list):
        for i,v in enumerate(o): yield from walk_strings(v,f'{path}[{i}]')
    elif isinstance(o,dict):
        for k,v in o.items(): yield from walk_strings(v,f'{path}.{k}')


# Script check runs on child-facing display text only. Provenance/enum/id fields are Roman by design.
def child_facing(plan):
    out=[]
    for t in [x for m in plan['modules'] for sg in m['segments'] for x in sg['topics']]:
        tid=t['topic_id']
        for k in ['topic_name','explanation','real_life_example','brief_summary','summary',
                  'detailed_summary','publication_text','modified_chunk']:
            out.append((f'{tid}.{k}',t[k] or ''))
        for k in ['key_terms','concept_bullets','important_points']:
            for i,v in enumerate(t[k]): out.append((f'{tid}.{k}[{i}]',v))
        for i,rq in enumerate(t['recall_questions']):
            out.append((f'{rq["id"]}.prompt',rq['prompt'])); out.append((f'{rq["id"]}.answer',rq['answer']))
        for c in t['concepts']:
            out.append((f'{c["concept_id"]}.concept_name',c['concept_name']))
            for i,v in enumerate(c['key_terms']): out.append((f'{c["concept_id"]}.key_terms[{i}]',v))
            for i,b in enumerate(c['content']):
                if b['type']=='paragraph':
                    out.append((f'{c["concept_id"]}.content[{i}].text',b['text']))
                    if b.get('publication_text'): out.append((f'{c["concept_id"]}.content[{i}].publication_text',b['publication_text']))
                else:
                    for j,it in enumerate(b['items']): out.append((f'{c["concept_id"]}.content[{i}].items[{j}]',it))
        for g in (t['figures_of_speech'] or []):
            for k,v in g.items(): out.append((f'{tid}.figures_of_speech.{k}',str(v)))
        if t['rhyme_scheme']:
            for k,v in t['rhyme_scheme'].items():
                out.append((f'{tid}.rhyme_scheme.{k}',v if isinstance(v,str) else ' '.join(v)))
        for grp in ['shabdarth','samanarthi','vilom','vyakaran']:
            for i,e in enumerate(t[grp]):
                for k,v in e.items():
                    out.append((f'{tid}.{grp}[{i}].{k}',v if isinstance(v,str) else ' '.join(v)))
        for mn in t['media']:
            out.append((f'{mn["id"]}.title',mn['title'])); out.append((f'{mn["id"]}.description',mn['description']))
    for m in plan['modules']:
        out.append((f'{m["module_id"]}.module_name',m['module_name']))
        out.append((f'{m["module_id"]}.overall_rhyme_scheme',m['overall_rhyme_scheme'] or ''))
        for i,dw in enumerate(m['difficult_words']):
            for k,v in dw.items(): out.append((f'{m["module_id"]}.difficult_words[{i}].{k}',v))
        for sg in m['segments']: out.append((f'{sg["segment_id"]}.segment_name',sg['segment_name']))
    for o in plan['objectives']:
        out.append((f'{o["objective_id"]}.objective_text',o['objective_text']))
        out.append((f'{o["objective_id"]}.strand_name',o['strand_name']))
    for k in ['chapter_name','unit_title','topic_title','teaching_lens','guiding_question']:
        out.append(('root.'+k,plan[k]))
    return out

for path,s_ in child_facing(plan):
    if DANDA in s_: f('B',f'danda U+0964 in {path}','05_verbatim_attachment.md')
    t=strip_bracketed(s_)
    if DEV.search(t): f('B',f'Devanagari in {path}: {DEV.findall(t)[:5]}','12_runtime_authoring.md')
    if ROM.search(t): f('B',f'Roman in {path}: {"".join(ROM.findall(t)[:20])}','12_runtime_authoring.md')

for t in [x for m in plan['modules'] for sg in m['segments'] for x in sg['topics']]:
    for k in ['original_chunk','publication_chunk']:
        v=t[k]
        if DANDA in v: f('B',f'danda in {t["topic_id"]}.{k}','05_verbatim_attachment.md')
        if DEV.search(v): f('B',f'Devanagari in {t["topic_id"]}.{k}','05_verbatim_attachment.md')
        if ROM.search(v): f('B',f'Roman in {t["topic_id"]}.{k}','05_verbatim_attachment.md')

# digits in authored display text
def digcheck(t):
    for name in ['topic_name','explanation','real_life_example','brief_summary','summary','detailed_summary','publication_text']:
        if DIG.search(t[name] or ''): f('F',f'{t["topic_id"]}.{name} has a digit','12_runtime_authoring.md')
    for k in ['concept_bullets','important_points']:
        for i,v in enumerate(t[k]):
            if DIG.search(v): f('F',f'{t["topic_id"]}.{k}[{i}] has a digit','12_runtime_authoring.md')
    for i,rq in enumerate(t['recall_questions']):
        for k in ('prompt','answer'):
            if DIG.search(rq[k]): f('F',f'{t["topic_id"]}.recall_questions[{i}].{k} has a digit','12_runtime_authoring.md')
    for c in t['concepts']:
        if DIG.search(c['concept_name']): f('F',f'{c["concept_id"]}.concept_name has a digit','02_structure.md')
        for i,b in enumerate(c['content']):
            if b['type']=='paragraph':
                if DIG.search(b['text']): f('F',f'{c["concept_id"]}.content[{i}].text has a digit','12_runtime_authoring.md')
                if DIG.search(b.get('publication_text','')): f('F',f'{c["concept_id"]}.content[{i}].publication_text has a digit','16_publication_authoring.md')
            else:
                for j,it in enumerate(b['items']):
                    if DIG.search(it): f('F',f'{c["concept_id"]}.content[{i}].items[{j}] has a digit','12_runtime_authoring.md')
for o in plan['objectives']:
    if DIG.search(o['objective_text']): f('F',f'{o["objective_id"]}.objective_text has a digit','02_structure.md')

# ---- B: original_chunk non-empty, verbatim present in normalized
normlines=norm
for t in topics:
    oc=t['original_chunk']
    if not oc.strip(): f('B',f'{t["topic_id"]} empty original_chunk','05_verbatim_attachment.md')
    for ln in [x for x in oc.split('\n') if x.strip()]:
        if ln not in normlines: f('B',f'{t["topic_id"]} line not found in 00_chapter_normalized.md: {ln!r}','05_verbatim_attachment.md')
    digcheck(t)

# ---- C bands
def wc(s): return len([x for x in re.split(r'\s+',s.strip()) if x])
for t in topics:
    for k,lo,hi in [('explanation',55,90),('real_life_example',55,90)]:
        if not (t[k] or '').strip(): f('C',f'{t["topic_id"]}.{k} empty','12_runtime_authoring.md')
        n=wc(t[k])
        if not lo<=n<=hi: f('C',f'{t["topic_id"]}.{k} {n} words (band {lo}-{hi})','12_runtime_authoring.md')
    n=wc(t['publication_text'])
    if not 55<=n<=90: w(f'{t["topic_id"]}.publication_text {n} words (teaching band 55-90)')
for o in plan['objectives']:
    n=wc(o['objective_text'])
    if not 12<=n<=30: f('C',f'{o["objective_id"]}.objective_text {n} words (band 12-30)','02_structure.md')

# ---- summaries strictly increasing
for t in topics:
    a,b,c=wc(t['brief_summary']),wc(t['summary']),wc(t['detailed_summary'])
    if not (a<b<c): f('F',f'{t["topic_id"]} summaries not strictly increasing: {a}/{b}/{c}','12_runtime_authoring.md')

# ---- D: figures_of_speech lines verbatim in chunk
for t in topics:
    for i,g in enumerate(t['figures_of_speech'] or []):
        if g.get('lines','') not in t['original_chunk']:
            f('D',f'{t["topic_id"]}.figures_of_speech[{i}] lines not verbatim in original_chunk','07_genre_pitfalls.md')
INFO.append('figures_of_speech counts: '+str({t['topic_id']:len(t['figures_of_speech'] or []) for t in topics}))

# ---- D: sensitivity hard items
SEV7=[c for tp in pit['topics'] for c in tp['avoid_checks'] if c['severity']=='hard']
INFO.append(f'07 hard avoid_checks: {len(SEV7)}; soft: {len([c for tp in pit["topics"] for c in tp["avoid_checks"] if c["severity"]!="hard"])}')
hard8=[x for x in sen['topics'] if x.get('severity')=='hard']
INFO.append(f'08 hard items: {len(hard8)}; soft: {len(sen["topics"])-len(hard8)}')
AREAS={'ધર્મ','સમુદાય','ક્ષેત્ર','વિકલાંગતા','સંઘર્ષ','જાતિ-ભૂમિકા','સુરક્ષા'}
for x in sen['topics']:
    for a in x['areas']:
        if a not in AREAS: f('D',f'08 area not in fixed seven: {a}','08_sensitivity_safety.md')
for x in sen['chapter_level']:
    if x['area'] not in AREAS: f('D',f'08 chapter area not in fixed seven: {x["area"]}','08_sensitivity_safety.md')

# ---- contract invariants
if plan['phase']!=2: f('F','phase != 2','13')
if plan['plan_id']!=f"{plan['chapter_id']}_v{plan['version']}": f('F','plan_id != chapter_id_vN','01_ingestion_genre_diagnosis.md')
if plan['chapter_id']!=f"gseb_eng_gujarati{plan['grade']}_ch{plan['unit_number']}": f('F','chapter_id grammar','01_ingestion_genre_diagnosis.md')
if plan['publication_id'] is None: w('publication_id is null (server rejects null)')
oids={o['objective_id'] for o in plan['objectives']}
if len(oids)!=len(plan['objectives']): f('F','duplicate objective_id','02_structure.md')
tids={t['topic_id'] for t in topics}
cids={c['concept_id'] for t in topics for c in t['concepts']}
for o in plan['objectives']:
    if o['home_topic_id'] not in tids: f('F',f'{o["objective_id"]} home_topic_id unresolved','02_structure.md')
    for a in o['anchor']:
        if a not in cids: f('F',f'{o["objective_id"]} anchor {a} unresolved','02_structure.md')
for lid,oid in plan['strand_to_objective_map'].items():
    if oid not in oids: f('F',f'strand map {lid}->{oid} unresolved','02_structure.md')
lids={o['legacy_id'] for o in plan['objectives']}
if lids!=set(plan['strand_to_objective_map']): f('F','strand_to_objective_map does not cover every legacy_id','02_structure.md')
# concept-continuous + inline mirror + ids
OBJ={o['objective_id']:o for o in plan['objectives']}
cn=0; sn=0; tn=0
MEDIA_ID_RE=re.compile(r'^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$')
for mi,m in enumerate(plan['modules'],1):
    if m['module_id']!=f'M{mi}': f('F',f'module_id {m["module_id"]} != M{mi}','04_mapping_convergence.md')
    for s in m['segments']:
        sn+=1
        if s['segment_id']!=f'M{mi}.S{sn}': f('F',f'segment_id {s["segment_id"]} != M{mi}.S{sn}','04_mapping_convergence.md')
        for t in s['topics']:
            tn+=1
            if t['topic_id']!=f'{s["segment_id"]}.T{tn}': f('F',f'topic_id {t["topic_id"]} != {s["segment_id"]}.T{tn}','04_mapping_convergence.md')
            if not t['concepts']: f('F',f'{t["topic_id"]} has no concepts','02_structure.md')
            for c in t['concepts']:
                cn+=1
                if c['concept_id']!=f'{t["topic_id"]}.C{cn}': f('F',f'concept_id {c["concept_id"]} != {t["topic_id"]}.C{cn}','04_mapping_convergence.md')
                if c['objective_id'] not in oids: f('F',f'{c["concept_id"]} objective_id unresolved','02_structure.md')
                if not c['content']: f('F',f'{c["concept_id"]} empty content[]','12_runtime_authoring.md')
            for oid in t['objective_ids']:
                if oid not in oids: f('F',f'{t["topic_id"]} objective_ids {oid} unresolved','02_structure.md')
            mirr={x['objective_id']:x for x in t['learning_objectives']}
            if set(mirr)!=set(t['objective_ids']): f('F',f'{t["topic_id"]} learning_objectives mirror mismatch','02_structure.md')
            for oid,x in mirr.items():
                if x['objective_text']!=OBJ[oid]['objective_text']: f('F',f'{t["topic_id"]} inline mirror text drift for {oid}','02_structure.md')
                if 'image_examples' not in x: f('F',f'{t["topic_id"]} mirror missing image_examples','13')
            for i,rq in enumerate(t['recall_questions'],1):
                if rq['id']!=f'{t["topic_id"]}.RQ{i}': f('F',f'{t["topic_id"]} recall id {rq["id"]}','12_runtime_authoring.md')
                if rq['legacy_id']!=f'{t["topic_id"]}.TR{i}': f('F',f'{t["topic_id"]} recall legacy id {rq["legacy_id"]}','12_runtime_authoring.md')
                if '.SR' in rq['id']: f('F','SR id used','12_runtime_authoring.md')
                if not rq['answer'].strip(): f('F',f'{rq["id"]} empty answer','12_runtime_authoring.md')
            if t['topic_type'] not in ('POEM','STORY_TELLING','CONCEPT','REVIEW'):
                f('F',f'{t["topic_id"]} topic_type {t["topic_type"]} not in authored enum','02_structure.md')
            for mn in t['media']:
                if not MEDIA_ID_RE.match(mn['id']): f('F',f'media id {mn["id"]} fails MEDIA_ID_RE','09_media_planning.md')
                if MEDIA_ID_RE.match(mn['id']).group(1)!=mn['concept_id']: f('F',f'media {mn["id"]} concept mismatch','09_media_planning.md')
                if mn['image_url']!='': f('F',f'media {mn["id"]} non-empty image_url (no Gujarati frame pool)','09_media_planning.md')
                if not (mn['generation_prompt'] or '').strip(): f('F',f'media {mn["id"]} empty generation_prompt','09_media_planning.md')
                if 'Devanagari script labels' not in (mn['negative_prompt'] or ''): f('F',f'media {mn["id"]} negative_prompt missing Devanagari script labels','09_media_planning.md')
                if '[reused frame' in json.dumps(mn,ensure_ascii=False): f('F',f'media {mn["id"]} reused-frame stamp','09_media_planning.md')
# segment recall ids (none authored here)
for s in segs:
    for rq in s.get('recall_questions',[]) or []:
        if '.SR' in rq.get('id',''): f('F','segment recall uses SR','12_runtime_authoring.md')

# 2d_tool count
tools={json.dumps(t['2d_tool'],ensure_ascii=False) for t in topics if t['2d_tool']}
if len(tools)>1: f('F','more than one 2d_tool in chapter','09_media_planning.md')
INFO.append(f'2d_tool: {med["2d_tool"]}')

# ---- media reuse report
scenes=[t for t in topics if 'image' in (t['available_content_types'] or [])]
rr=med['reuse_report']
if rr['scenes']!=len(scenes): f('F',f'reuse_report.scenes {rr["scenes"]} != image-scene topics {len(scenes)}','09_media_planning.md')
if rr['authored']!=rr['scenes']: f('F','reuse_report.authored != scenes','09_media_planning.md')
if rr['reused']!=0: f('F','reuse_report.reused != 0','09_media_planning.md')
nimg=sum(len(t['media']) for t in topics)
if nimg!=len(scenes): f('F',f'{nimg} media nodes vs {len(scenes)} image scenes','09_media_planning.md')

# ---- exercises
inv=[e['verbatim_heading'] for e in meta['exercise_inventory']]
cr=ex['coverage_report']
if len(cr['blocks_found'])!=len(inv): f('E',f'blocks_found {len(cr["blocks_found"])} != inventory {len(inv)}','10_exercise_solutions.md')
if cr['unanswered']: f('E',f'unanswered blocks: {cr["unanswered"]}','10_exercise_solutions.md')
def norm_h(s): return re.sub(r'[\s\.\'‘’]','',s)
missing=[h for h in inv if not any(norm_h(h)[:18]==norm_h(b)[:18] for b in cr['blocks_found'])]
if missing: f('E','inventory headings not in blocks_found: '+str(missing),'10_exercise_solutions.md')
for e in ex['exercises']:
    if not str(e.get('answer','')).strip(): f('E',f'{e["exercise_id"]} empty answer','10_exercise_solutions.md')
INFO.append(f'exercises: {len(ex["exercises"])} items, blocks {len(cr["blocks_found"])}/{len(inv)}, unmapped {len(cr["unmapped"])}')

# ---- publication
for t in topics:
    if not t['publication_text'].strip(): f('P',f'{t["topic_id"]} empty publication_text','16_publication_authoring.md')
    if t['original_chunk'] not in t['publication_chunk']:
        f('P',f'{t["topic_id"]} publication_chunk does not carry original_chunk verbatim','16_publication_authoring.md')
    for bad in ['બાળકો','જુઓ —','બોલો']:
        if bad in t['publication_text']: f('P',f'{t["topic_id"]} publication_text carries classroom address {bad!r}','16_publication_authoring.md')
    npar=len([b for c in t['concepts'] for b in c['content'] if b['type']=='paragraph'])
    npub=len([b for c in t['concepts'] for b in c['content'] if b['type']=='paragraph' and b.get('publication_text')])
    if npar!=npub: f('P',f'{t["topic_id"]} concept publication_text {npub}/{npar} paragraph blocks','16_publication_authoring.md')
# concept_publication count vs paragraphs
pubf=L('16_publication.json')
tot_cp=sum(len(x['concept_publication']) for x in pubf['topics'])
tot_par=sum(len([b for c in t['concepts'] for b in c['content'] if b['type']=='paragraph']) for t in topics)
if tot_cp!=tot_par: f('P',f'concept_publication entries {tot_cp} != paragraph blocks {tot_par}','16_publication_authoring.md')

# ---- key_terms band
for t in topics:
    n=len(t['key_terms'])
    if not 3<=n<=6: w(f'{t["topic_id"]} key_terms {n} (3-6)')
    for k in ('concept_bullets','important_points'):
        n=len(t[k])
        if not 3<=n<=4: w(f'{t["topic_id"]}.{k} {n} lines (3-4)')
    n=len(t['recall_questions'])
    if not 2<=n<=3: w(f'{t["topic_id"]} recall_questions {n} (2-3)')
for m in plan['modules']:
    n=len(m['difficult_words'])
    if not 5<=n<=10: w(f'{m["module_id"]} difficult_words {n} (5-10)')

print('=== FAIL ===')
for s,m,o in FAIL: print(f'[{s}] {m}   -> {o}')
print('=== WARN ===')
for m in WARN: print('-',m)
print('=== INFO ===')
for m in INFO: print('-',m)
