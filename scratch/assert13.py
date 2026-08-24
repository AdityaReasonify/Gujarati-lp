import json,re,collections
D='/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch03/'
d=json.load(open(D+'13_merged.json',encoding='utf-8'))
meta=json.load(open(D+'01_meta.json',encoding='utf-8'))
base=json.load(open(D+'05_with_content.json',encoding='utf-8'))
R=[]
def chk(n,c,t,det=''):
    R.append((n,'OK' if c else 'FAIL',t,det))

T=[t for m in d['modules'] for s in m['segments'] for t in s['topics']]
ids={t['topic_id'] for t in T}
cids={c['concept_id'] for t in T for c in t['concepts']}
segids={s['segment_id'] for m in d['modules'] for s in m['segments']}

# 1
chk(1, d['phase']==2 and d['plan_id']==f"{d['chapter_id']}_v{d['version']}" and d['chapter_id']==f"gseb_eng_gujarati{d['grade']}_ch{d['unit_number']}", 'phase/plan_id/chapter_id grammar', d['chapter_id']+' / '+d['plan_id'])
# 2
GUJ=re.compile(r'[઀-૿]'); BAD=re.compile(r'[A-Za-zऀ-ॿ]|।')
b2=[t['topic_id'] for t in T if not t['original_chunk'].strip() or not GUJ.search(t['original_chunk']) or BAD.search(t['original_chunk'])]
chk(2, not b2, 'original_chunk non-empty, Gujarati-only, no danda', str(b2))
# 3
b3=[]
for t in T:
    if not t['concepts']: b3.append(t['topic_id'])
    for c in t['concepts']:
        if not re.match(r'^M\d+\.S\d+\.T\d+\.C\d+$',c['concept_id']): b3.append(c['concept_id']+':idgrammar')
        if c['objective_id'] not in {o['objective_id'] for o in d['objectives']}: b3.append(c['concept_id']+':obj')
        if not c['content']: b3.append(c['concept_id']+':emptycontent')
chk(3, not b3, 'every topic >=1 concept, valid id, resolvable objective, non-empty content', str(b3))
# 4
objids=[o['objective_id'] for o in d['objectives']]
b4=[]
if len(objids)!=len(set(objids)): b4.append('dup objective_id')
for o in d['objectives']:
    if o['home_topic_id'] not in ids: b4.append(o['objective_id']+':home')
    for a in o['anchor']:
        if a not in cids: b4.append(o['objective_id']+':anchor '+a)
for o in d['objectives']:
    if d['strand_to_objective_map'].get(o['legacy_id'])!=o['objective_id']: b4.append(o['legacy_id']+':map')
for t in T:
    for oid in t['objective_ids']:
        if oid not in objids: b4.append(t['topic_id']+':objref')
chk(4, not b4, 'objectives registry complete and consistent', str(b4))
# 5
REG={o['objective_id']:o for o in d['objectives']}
b5=[]
for t in T:
    if len(t['learning_objectives'])!=len(t['objective_ids']): b5.append(t['topic_id']+':count')
    for lo in t['learning_objectives']:
        r=REG[lo['objective_id']]
        if lo['objective_text']!=r['objective_text']: b5.append(t['topic_id']+':text')
        for k in ['legacy_id','strand','strand_name','bloom_level','home_topic_id','anchor','status','theme_category']:
            if lo[k]!=r[k]: b5.append(t['topic_id']+':'+k)
        if lo.get('image_examples')!=[]: b5.append(t['topic_id']+':image_examples')
chk(5, not b5, 'inline learning_objectives mirror registry char-for-char', str(b5))
# 6
MEDIA_ID_RE=re.compile(r'^(?P<c>M\d+\.S\d+\.T\d+\.C\d+)\.(?P<s>IMG|VID|2D|3D|SIM)(?P<n>\d+)$')
b6=[]
for t in T:
    for m in t['media']:
        mm=MEDIA_ID_RE.match(m['id'])
        if not mm: b6.append(m['id'])
        elif mm.group('c')!=m['concept_id'] or m['concept_id'] not in cids: b6.append(m['id']+':concept')
    for i,q in enumerate(t['recall_questions']):
        if q['id']!=f"{t['topic_id']}.RQ{i+1}": b6.append(q['id'])
        if q['legacy_id']!=f"{t['topic_id']}.TR{i+1}": b6.append(q['legacy_id'])
        if '.SR' in q['id']: b6.append(q['id']+':SR')
chk(6, not b6, 'MEDIA_ID_RE concept-scoped; RQ{n}/TR{n}; no .SR{n}', str(b6))
# concept continuity
cc=[c['concept_id'] for t in T for c in t['concepts']]
expect=[f"{t['topic_id']}.C{i+1}" for i,t in enumerate(T)]
chk('6b', cc==expect, 'concept numbering chapter-continuous', str(cc) if cc!=expect else '')
# 7
inv=[b['verbatim_heading'] for b in meta['exercise_inventory']]
ex=json.load(open(D+'10_exercise_solutions.json',encoding='utf-8'))
cr=ex['coverage_report']
names={t['topic_name'] for t in T}
chk(7, set(cr['blocks_found'])==set(inv) and len(cr['blocks_found'])==len(inv) and cr['unanswered']==[] and not (names & set(inv)),
    'no સ્વાધ્યાય block is a topic; every inventoried block answered',
    f"found {len(cr['blocks_found'])}/{len(inv)}, unanswered {len(cr['unanswered'])}, unmapped {len(cr['unmapped'])}")
# 8
b8=[t['topic_id'] for t in T if not (len(t['brief_summary'])<len(t['summary'])<len(t['detailed_summary']))]
chk(8, not b8, 'three-tier summaries strictly increase', str(b8))
# 9
DIG=re.compile(r'[0-9૦-૯]')
b9=[]
for t in T:
    fields=[('topic_name',t['topic_name'])]+[(k,t[k]) for k in ['explanation','real_life_example','brief_summary','summary','detailed_summary']]
    for k in ['concept_bullets','important_points']: fields+= [(k,x) for x in t[k]]
    for q in t['recall_questions']: fields+=[('rq',q['prompt']),('rq',q['answer'])]
    for c in t['concepts']:
        for bl in c['content']:
            if bl['type']=='paragraph': fields+=[('cc',bl['text']),('cc',bl['publication_text'])]
            else: fields+=[('cc',x) for x in bl.get('items',[])]
    fields+=[('publication_text',t['publication_text'])]
    for k,v in fields:
        if DIG.search(v): b9.append(t['topic_id']+':'+k)
for o in d['objectives']:
    if DIG.search(o['objective_text']): b9.append(o['objective_id'])
for m in d['modules']:
    if DIG.search(m['module_name']): b9.append(m['module_id'])
    for s in m['segments']:
        if DIG.search(s['segment_name']): b9.append(s['segment_id'])
chk(9, not b9, 'no numbers in display text', str(b9))
# 10
scenes=[t for t in T if 'image' in t['available_content_types']]
imgs=[m for t in T for m in t['media'] if m['type']=='image']
tools=[t['topic_id'] for t in T if t['2d_tool']]
b10=[m['id'] for m in imgs if m['image_url']!='' or not m['generation_prompt'].strip() or 'Devanagari script labels' not in m['negative_prompt']]
chk(10, len(scenes)==len(imgs)==9 and not tools and not b10, 'one image per scene, image_url "" + real generation_prompt, <=1 2d_tool',
    f"scenes {len(scenes)} images {len(imgs)} tools {len(tools)} bad {b10}")
# 11
b11=[]
for t in T:
    for f in t['figures_of_speech']:
        if f['lines'] not in t['original_chunk']: b11.append(t['topic_id']+':'+f.get('device',''))
chk(11, not b11, 'figures_of_speech lines verbatim in original_chunk ([] on all 9)', str(b11))
# 12
allids=ids|cids|segids|{m['module_id'] for m in d['modules']}
b12=[]
for t in T:
    for x in t['depends_on']+t['source_topic_ids']:
        if x not in allids: b12.append(t['topic_id']+':'+x)
chk(12, not b12, 'every internal reference resolves (re-assert after A14)', str(b12))
# publication
b=[]
for t in T:
    if not t['publication_text'].strip(): b.append(t['topic_id']+':empty')
    if not t['publication_chunk'].startswith(t['original_chunk']): b.append(t['topic_id']+':verbatim')
    for v in ['બાળકો','જુઓ —','બોલો']:
        if v in t['publication_text']: b.append(t['topic_id']+':voc '+v)
chk('pub', not b, 'publication_text present, verbatim intact inside publication_chunk, no vocative', str(b))
# topic keys
KEYS=set(['media','2d_tool','summary','concepts','topic_id','key_terms','depends_on','difficulty','topic_name','topic_type','word_count','explanation','brief_summary','objective_ids','modified_chunk','original_chunk','topic_category','concept_bullets','detailed_summary','important_points','publication_text','recall_questions','source_topic_ids','publication_chunk','real_life_example','estimated_exchanges','learning_objectives','primary_content_type','tertiary_content_type','secondary_content_type','available_content_types'])
EXTRA=set(['figures_of_speech','rhyme_scheme','shabdarth','samanarthi','vilom','vyakaran'])
b=[]
for t in T:
    k=set(t.keys())
    if k-(KEYS|EXTRA): b.append(t['topic_id']+':extra '+str(k-(KEYS|EXTRA)))
    if KEYS-k: b.append(t['topic_id']+':missing '+str(KEYS-k))
chk('keys', not b, 'topic carries exactly the 31 contract keys + 6 extras, no working fields', str(b))
ROOT=set(['board','genre','grade','level','phase','author','modules','plan_id','subject','version','textbook','_activate','medium_id','chapter_id','objectives','unit_title','topic_title','unit_number','chapter_name','textbook_url','topic_number','teaching_lens','estimated_time','publication_id','subject_ref_id','textbook_pages','english_plan_id','guiding_question','chapter_master_id','english_chapter_id','strand_to_objective_map'])
missing=ROOT-set(d.keys()); extra=set(d.keys())-ROOT
chk('root', not missing and not extra and 'ordering' not in d, 'root keys = contract 32 minus `ordering` (A14/15 sets it)', f'missing {missing} extra {extra}')
chk('pubid', d['publication_id'] is not None, 'publication_id non-null (provisional placeholder)', str(d['publication_id']))

for n,st,t,det in R:
    print(f'{str(n):5s} {st:4s} {t}' + (f'  [{det}]' if det else ''))
print()
print('FAILS:',[n for n,st,_,_ in R if st=='FAIL'])
