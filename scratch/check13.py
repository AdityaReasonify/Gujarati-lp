import json,re,sys,unicodedata
D='/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch09/'
L=lambda f: json.load(open(D+f))
meta=L('01_meta.json'); base=L('05_with_content.json'); auth=L('12_authoring.json')
med=L('09_media.json'); pub=L('16_publication.json'); pages=L('11_pages.json')
ex=L('10_exercise_solutions.json'); pit=L('07_pitfalls.json'); sen=L('08_sensitivity.json')
norm=open(D+'00_chapter_normalized.md').read()

topics=[]
for m in base['modules']:
    for s in m['segments']:
        for t in s['topics']:
            topics.append((m,s,t))
print('topics',len(topics))

A={t['topic_id']:t for t in auth['topics']}
P={t['topic_id']:t for t in pub['topics']}
MED={}
for x in med['media']: MED.setdefault(x['topic_id'],[]).append(x)

def words(s): return len([w for w in re.split(r'\s+',s.strip()) if w])
GUJ=re.compile(r'[઀-૿]')
DEV=re.compile(r'[ऀ-ॿ]')
ROM=re.compile(r'[A-Za-z]')

issues=[]
def add(sec,msg): issues.append((sec,msg))

# --- B ---
for m,s,t in topics:
    tid=t['topic_id']; oc=t.get('original_chunk') or ''
    if not oc.strip(): add('B',f'{tid}: original_chunk empty')
    if DEV.search(oc): add('B',f'{tid}: Devanagari in original_chunk: '+repr(DEV.findall(oc)[:8]))
    r=ROM.findall(oc)
    if r: add('B',f'{tid}: Roman in original_chunk: '+repr(''.join(r)[:40]))
    if '।' in oc: add('B',f'{tid}: danda in original_chunk')
    if not GUJ.search(oc): add('B',f'{tid}: no Gujarati in original_chunk')
    wc=t.get('word_count',{}).get('original')
    if wc!=words(oc): add('B-soft',f'{tid}: word_count {wc} vs computed {words(oc)}')
# marker counts
mk=len(re.findall(r'\[\[માહિતી-ખંડ',norm))
print('markers માહિતી-ખંડ',mk,'topics',len(topics))
if mk!=len(topics): add('B',f'marker count {mk} != topics {len(topics)}')
sv=len(re.findall(r'\[\[સ્વાધ્યાય',norm))
print('markers સ્વાધ્યાય',sv,'inventory',len(meta['exercise_inventory']))

# --- C ---
for m,s,t in topics:
    tid=t['topic_id']; a=A.get(tid)
    if not a: add('C',f'{tid}: no authoring'); continue
    for f in ('explanation','real_life_example'):
        v=(a.get(f) or '').strip()
        if not v: add('C',f'{tid}: {f} empty'); continue
        w=words(v)
        if not (55<=w<=90): add('C',f'{tid}: {f} {w} words (band 55-90)')
    for f in ('brief_summary','summary','detailed_summary'):
        if not (a.get(f) or '').strip(): add('C',f'{tid}: {f} empty')
    b,su,de=len(a.get('brief_summary','')),len(a.get('summary','')),len(a.get('detailed_summary',''))
    if not (b<su<de): add('F',f'{tid}: summaries not strictly increasing ({b},{su},{de})')
for o in base['objectives']:
    w=words(o['objective_text'])
    if not (12<=w<=30): add('C',f"{o['objective_id']}: objective_text {w} words (band 12-30)")

# --- D: figures_of_speech verbatim ---
for m,s,t in topics:
    a=A.get(t['topic_id'],{})
    for fs in (a.get('figures_of_speech') or []):
        if fs.get('lines','') not in (t.get('original_chunk') or ''):
            add('D',f"{t['topic_id']}: figure lines not in original_chunk: {fs.get('lines')[:40]}")

# --- script check on authored display text ---
AUTH_FIELDS=['explanation','real_life_example','brief_summary','summary','detailed_summary']
def walk_strings(o,path=''):
    if isinstance(o,str): yield path,o
    elif isinstance(o,dict):
        for k,v in o.items(): yield from walk_strings(v,path+'.'+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): yield from walk_strings(v,path+f'[{i}]')
DIGIT=re.compile(r'[0-9૦-૯]')
disp_paths=('explanation','real_life_example','brief_summary','summary','detailed_summary','concept_bullets','important_points','topic_name','concept_name')
for m,s,t in topics:
    tid=t['topic_id']; a=A.get(tid,{})
    for f in AUTH_FIELDS+['concept_bullets','important_points']:
        v=a.get(f)
        for p,txt in walk_strings(v,f):
            if DEV.search(txt): add('B',f'{tid}.{p}: Devanagari in authored text: '+repr(DEV.findall(txt)[:5]))
            if DIGIT.search(txt): add('F',f'{tid}.{p}: digit in display text: '+repr(DIGIT.findall(txt)[:5])+' :: '+txt[:60])
    for rq in (a.get('recall_questions') or []):
        for f in ('prompt','answer'):
            txt=rq.get(f,'')
            if DIGIT.search(txt): add('F',f"{tid}.{rq.get('id')}.{f}: digit in display text: "+txt[:60])
            if DEV.search(txt): add('B',f"{tid}.{rq.get('id')}.{f}: Devanagari")
    if t.get('topic_name') and DIGIT.search(t['topic_name']): add('F',f'{tid}: digit in topic_name')

# --- contract ---
objids={o['objective_id'] for o in base['objectives']}
allnodes=set()
for m,s,t in topics:
    allnodes.add(m['module_id']); allnodes.add(s['segment_id']); allnodes.add(t['topic_id'])
    for c in t['concepts']: allnodes.add(c['concept_id'])
for o in base['objectives']:
    if o['home_topic_id'] not in allnodes: add('Contract',f"{o['objective_id']}: home_topic_id unresolved")
    for an in o['anchor']:
        if an not in allnodes: add('Contract',f"{o['objective_id']}: anchor {an} unresolved")
if len(objids)!=len(base['objectives']): add('Contract','duplicate objective_id')
smap=base['strand_to_objective_map']
for o in base['objectives']:
    if smap.get(o['legacy_id'])!=o['objective_id']: add('Contract',f"strand map missing {o['legacy_id']}")
if len(smap)!=len(base['objectives']): add('Contract','strand map size mismatch')
cn=0
for m,s,t in topics:
    for oid in t['objective_ids']:
        if oid not in objids: add('Contract',f"{t['topic_id']}: objective {oid} unresolved")
    if not t['concepts']: add('Contract',f"{t['topic_id']}: no concepts")
    for c in t['concepts']:
        cn+=1
        exp=f"{t['topic_id']}.C{cn}"
        if c['concept_id']!=exp: add('Contract',f"concept id {c['concept_id']} expected {exp}")
        if c.get('objective_id') not in objids: add('Contract',f"{c['concept_id']}: objective_id bad")
        ac=A.get(t['topic_id'],{})
        aconc={x['concept_id']:x for x in ac.get('concepts',[])}
        if c['concept_id'] not in aconc: add('Contract',f"{c['concept_id']}: no authored content")
        elif not aconc[c['concept_id']].get('content'): add('Contract',f"{c['concept_id']}: content[] empty")
    for rq in (A.get(t['topic_id'],{}).get('recall_questions') or []):
        if not re.fullmatch(re.escape(t['topic_id'])+r'\.RQ\d+',rq.get('id','')): add('Contract',f"{t['topic_id']}: bad recall id {rq.get('id')}")
        if not re.fullmatch(re.escape(t['topic_id'])+r'\.TR\d+',rq.get('legacy_id','')): add('Contract',f"{t['topic_id']}: bad legacy id {rq.get('legacy_id')}")
        if '.SR' in rq.get('id',''): add('Contract','SR id present')
        if not (rq.get('answer') or '').strip(): add('Contract',f"{t['topic_id']}: recall without answer")
MEDIA_ID_RE=re.compile(r"^(?P<c>M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)\d+$")
for x in med['media']:
    if not MEDIA_ID_RE.match(x['id']): add('Contract',f"media id bad {x['id']}")
    if x['id'].rsplit('.',1)[0]!=x['concept_id']: add('Contract',f"media {x['id']} concept mismatch")
    if x.get('image_url','')!='' : add('Media',f"media {x['id']}: non-empty image_url")
    if not (x.get('generation_prompt') or '').strip(): add('Media',f"media {x['id']}: empty generation_prompt")
    if 'Devanagari script labels' not in (x.get('negative_prompt') or ''): add('Media',f"media {x['id']}: negative_prompt lacks Devanagari script labels")
    if x['concept_id'] not in allnodes: add('Contract',f"media {x['id']}: concept not in plan")
scenes=[t['topic_id'] for m,s,t in topics if 'image' in (t.get('available_content_types') or [])]
rr=med['reuse_report']
print('scenes(available image)',len(scenes),'reuse_report',rr['scenes'],rr['authored'],rr['reused'])
if rr['scenes']!=len(scenes): add('Media',f"reuse_report.scenes {rr['scenes']} != topics with image {len(scenes)}")
if rr['authored']!=rr['scenes']: add('Media','authored != scenes')
if rr['reused']!=0: add('Media','reused != 0')
if set(MED)!=set(scenes): add('Media',f"media topics {sorted(set(MED)^set(scenes))} mismatch image scenes")
if med['2d_tool'] not in (None,): print('2d_tool present')

# --- publication ---
for m,s,t in topics:
    tid=t['topic_id']; p=P.get(tid)
    if not p: add('Pub',f'{tid}: no publication'); continue
    if not (p.get('publication_text') or '').strip(): add('Pub',f'{tid}: publication_text empty')
    if p.get('publication_chunk')!=t.get('original_chunk'):
        pc=p.get('publication_chunk') or ''
        oc=t.get('original_chunk') or ''
        add('Pub',f'{tid}: publication_chunk != original_chunk (starts_with_oc={pc.startswith(oc)}, len {len(pc)} vs {len(oc)})')
    a=A.get(tid,{})
    ac={x['concept_id']:x for x in a.get('concepts',[])}
    cps=p.get('concept_publication') or []
    # count paragraph blocks
    npara=sum(1 for c in a.get('concepts',[]) for b in c['content'] if b.get('type')=='paragraph')
    if len(cps)!=npara: add('Pub',f'{tid}: concept_publication {len(cps)} vs paragraph blocks {npara}')
    for e in cps:
        cid=e['concept_id']; idx=e['content_index']
        blocks=ac.get(cid,{}).get('content',[])
        if idx>=len(blocks) or blocks[idx].get('type')!='paragraph':
            add('Pub',f'{tid}: concept_publication index {cid}[{idx}] not a paragraph')
    for bad in ('બાળકો','જુઓ —','બોલો'):
        if bad in (p.get('publication_text') or ''): add('Pub',f'{tid}: vocative/instruction {bad} in publication_text')

# --- exercises ---
cr=ex['coverage_report']
print('coverage_report keys',list(cr.keys()))
print('blocks_found',cr.get('blocks_found'),'inventory',len(meta['exercise_inventory']),'unanswered',cr.get('unanswered'),'unmapped',cr.get('unmapped'))
if cr.get('blocks_found')!=len(meta['exercise_inventory']): add('E',f"blocks_found {cr.get('blocks_found')} != inventory {len(meta['exercise_inventory'])}")
if cr.get('unanswered'): add('E',f"unanswered: {cr.get('unanswered')}")
print('exercises n',len(ex['exercises']))

print()
for sec,msg in issues: print(sec,'|',msg)
print('TOTAL ISSUES',len(issues))
