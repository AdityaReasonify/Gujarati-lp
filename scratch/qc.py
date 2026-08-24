# -*- coding: utf-8 -*-
import json, re, sys, unicodedata
D="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch02/"
L=lambda f: json.load(open(D+f, encoding='utf-8'))
meta=L('01_meta.json'); base=L('05_with_content.json'); auth=L('12_authoring.json')
med=L('09_media.json'); pub=L('16_publication.json'); pit=L('07_pitfalls.json')
sen=L('08_sensitivity.json'); exs=L('10_exercise_solutions.json'); pg=L('11_pages.json')
val4=L('04_validation.json')
norm=open(D+'00_chapter_normalized.md',encoding='utf-8').read()

FAIL=[]; WARN=[]; INFO=[]
def f(sec,owner,msg): FAIL.append((sec,owner,msg))
def w(sec,msg): WARN.append((sec,msg))

topics=[]
for m in base['modules']:
    for s in m['segments']:
        for t in s['topics']: topics.append((m['module_id'],s['segment_id'],t))
T={t['topic_id']:t for _,_,t in topics}
A={t['topic_id']:t for t in auth['topics']}
P={t['topic_id']:t for t in pub['topics']}
print("TOPICS:",len(topics))

# ---------- B ----------
DEV=re.compile(r'[ऀ-ॿ]'); ROM=re.compile(r'[A-Za-z]')
GUJ=re.compile(r'[઀-૿]')
def strip_brackets(s): return re.sub(r'\([^)]*\)','',s)
for tid,t in T.items():
    oc=t.get('original_chunk','')
    if not oc.strip(): f('B','A5',f'{tid}: original_chunk empty')
    if not GUJ.search(oc): f('B','A5',f'{tid}: original_chunk has no Gujarati')
    sb=strip_brackets(oc)
    if DEV.search(sb): f('B','A5',f'{tid}: Devanagari in original_chunk: '+repr(DEV.findall(sb)[:5]))
    if ROM.search(sb): f('B','A5',f'{tid}: Roman in original_chunk: '+repr(ROM.findall(sb)[:5]))
    if '।' in oc: f('B','A5',f'{tid}: danda U+0964 in original_chunk')
# markers
mk=re.findall(r'\[\[([^\]:]+):',norm)
from collections import Counter
c=Counter(mk)
reading=c.get('ઘટના',0)+c.get('સંવાદ',0)
print("markers:",dict(c),"reading=",reading)
if reading!=len(topics): f('B','A2',f'reading markers {reading} != topics {len(topics)}')
sv=c.get('સ્વાધ્યાય',0)
names=[t['topic_name'] for _,_,t in topics]
for n in names:
    if 'સ્વાધ્યાય' in n: f('B','A2','સ્વાધ્યાય became a topic: '+n)
# no danda anywhere authored
for tid,a in A.items():
    for k in ['explanation','real_life_example','brief_summary','summary','detailed_summary']:
        if '।' in (a.get(k) or ''): f('B','A12',f'{tid}.{k}: danda')

# ---------- C ----------
def wc(s): return len([x for x in re.split(r'\s+',s.strip()) if x])
for tid in T:
    a=A.get(tid)
    if not a: f('C','A12',f'{tid}: no authoring block'); continue
    for k in ['explanation','real_life_example']:
        v=(a.get(k) or '').strip()
        if not v: f('C','A12',f'{tid}: {k} empty'); continue
        n=wc(v)
        if not (55<=n<=90): f('C','A12',f'{tid}: {k} = {n} words (band 55-90)')
for o in base['objectives']:
    n=wc(o['objective_text'])
    if not (12<=n<=30): f('C','A12',f"{o['objective_id']}: objective_text = {n} words (band 12-30)")

# ---------- D ----------
hard_p=[]
for tp in pit['topics']:
    for it in tp.get('pitfalls',tp.get('items',[])) if isinstance(tp,dict) else []:
        if it.get('severity')=='hard': hard_p.append((tp.get('topic_id'),it))
print("hard pitfalls(topic-level):",len(hard_p))
for tid in T:
    a=A.get(tid,{})
    for fo in a.get('figures_of_speech') or []:
        lines=fo.get('lines','')
        if lines and lines not in T[tid]['original_chunk']:
            f('D','A7/A12',f'{tid}: figures_of_speech lines not verbatim in original_chunk: '+lines[:40])
AREAS={'ધર્મ','સમુદાય','ક્ષેત્ર','વિકલાંગતા','સંઘર્ષ','જાતિ-ભૂમિકા','સુરક્ષા'}
for blk in sen['topics']+sen['chapter_level']:
    for ar in blk.get('areas',[]):
        if ar not in AREAS: f('D','A8',f'sensitivity area not in fixed seven: {ar}')

# ---------- Contract ----------
if base.get('chapter_id')!=meta['chapter_id']: f('CONTRACT','A1','chapter_id mismatch 01 vs 05')
exp_cid=f"gseb_eng_gujarati{meta['grade']}_ch{meta['unit_number']}"
if meta['chapter_id']!=exp_cid: f('CONTRACT','A1',f"chapter_id {meta['chapter_id']} != {exp_cid}")
if meta['plan_id']!=f"{meta['chapter_id']}_v{meta['version']}": f('CONTRACT','A1','plan_id malformed')
objs={o['objective_id']:o for o in base['objectives']}
allids=set(T)|{c['concept_id'] for _,_,t in topics for c in t['concepts']}|{s for _,s,_ in topics}
if len(objs)!=len(base['objectives']): f('CONTRACT','A2','duplicate objective_id')
for o in base['objectives']:
    if o['home_topic_id'] not in T: f('CONTRACT','A2',f"{o['objective_id']} home_topic_id unresolved")
    for an in o['anchor']:
        if an not in allids: f('CONTRACT','A2',f"{o['objective_id']} anchor unresolved {an}")
sm=base['strand_to_objective_map']
for o in base['objectives']:
    if o['legacy_id'] not in sm: f('CONTRACT','A2',f"legacy_id {o['legacy_id']} missing from strand map")
for tid,t in T.items():
    for oid in t['objective_ids']:
        if oid not in objs: f('CONTRACT','A2',f'{tid} objective_ids unresolved {oid}')
    if not t['concepts']: f('CONTRACT','A2',f'{tid} has no concepts')
    for cpt in t['concepts']:
        if not re.match(r'^M\d+\.S\d+\.T\d+\.C\d+$',cpt['concept_id']): f('CONTRACT','A2',f'bad concept_id {cpt["concept_id"]}')
        if cpt.get('objective_id') not in objs: f('CONTRACT','A2',f'{cpt["concept_id"]} objective_id unresolved')
# concept continuity
cn=[int(cpt['concept_id'].split('.C')[1]) for _,_,t in topics for cpt in t['concepts']]
if cn!=list(range(1,len(cn)+1)): f('CONTRACT','A2',f'concept counter not chapter-continuous: {cn}')
# traversal ids
segs=[]; 
for m in base['modules']:
    for s in m['segments']: segs.append(s['segment_id'])
if segs!=[f'M{i}.S{j}' for i,j in [(1,1),(1,2),(2,3),(3,4)]]: INFO.append('segment ids: '+str(segs))
tn=[int(t['topic_id'].split('.T')[1]) for _,_,t in topics]
if tn!=list(range(1,len(tn)+1)): f('CONTRACT','A2',f'topic counter not continuous {tn}')
# recall ids
MEDIA_ID_RE=re.compile(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$")
for tid,a in A.items():
    for i,rq in enumerate(a.get('recall_questions') or [],1):
        if rq['id']!=f'{tid}.RQ{i}': f('CONTRACT','A12',f"bad recall id {rq['id']}")
        if rq.get('legacy_id')!=f'{tid}.TR{i}': f('CONTRACT','A12',f"bad legacy_id {rq.get('legacy_id')}")
        if '.SR' in rq['id']: f('CONTRACT','A12','SR id found')
        if not (rq.get('answer') or '').strip(): f('CONTRACT','A12',f"{rq['id']} empty answer")
# summaries increase
for tid,a in A.items():
    b1,s1,d1=[wc(a.get(k) or '') for k in ['brief_summary','summary','detailed_summary']]
    if not (b1<s1<d1): f('CONTRACT','A12',f'{tid} summaries not strictly increasing: {b1}/{s1}/{d1}')
# numbers in display text
DIG=re.compile(r'[0-9૦-૯]')
def chk_digits(tid,label,s):
    if s and DIG.search(s): f('CONTRACT','A12',f'{tid} {label}: digit in display text -> '+repr(s[max(0,DIG.search(s).start()-25):DIG.search(s).start()+15]))
for _,_,t in topics: chk_digits(t['topic_id'],'topic_name',t['topic_name'])
for o in base['objectives']: chk_digits(o['objective_id'],'objective_text',o['objective_text'])
for tid,a in A.items():
    for k in ['explanation','real_life_example','brief_summary','summary','detailed_summary']:
        chk_digits(tid,k,a.get(k) or '')
    for k in ['concept_bullets','important_points']:
        for x in a.get(k) or []: chk_digits(tid,k,x)
    for rq in a.get('recall_questions') or []:
        chk_digits(tid,'RQ.prompt',rq.get('prompt','')); chk_digits(tid,'RQ.answer',rq.get('answer',''))
    for cpt in a.get('concepts') or []:
        for cc in cpt.get('content') or []:
            chk_digits(tid,'concept.text',cc.get('text','') or '')
            for it in cc.get('items') or []: chk_digits(tid,'concept.item',it)
for mm in auth['modules']:
    for dw in mm.get('difficult_words') or []:
        chk_digits(mm['module_id'],'difficult_words',dw.get('example',''))
# script check on authored text
def chk_script(tid,label,s):
    sb=strip_brackets(s or '')
    if DEV.search(sb): f('B','A12',f'{tid} {label}: Devanagari -> '+repr(DEV.findall(sb)[:4]))
    if ROM.search(sb): f('B','A12',f'{tid} {label}: Roman -> '+repr(ROM.findall(sb)[:4]))
for tid,a in A.items():
    for k in ['explanation','real_life_example','brief_summary','summary','detailed_summary']: chk_script(tid,k,a.get(k))
for _,_,t in topics: chk_script(t['topic_id'],'topic_name',t['topic_name'])

# ---------- Exercises ----------
inv=meta['exercise_inventory']; cr=exs['coverage_report']
print("coverage_report:",json.dumps(cr,ensure_ascii=False)[:400])
if cr.get('blocks_found')!=len(inv): f('EXERCISE','A10',f"blocks_found {cr.get('blocks_found')} != inventory {len(inv)}")
if cr.get('unanswered'): f('EXERCISE','A10',f"unanswered: {cr['unanswered']}")
for e in exs['exercises']:
    if not str(e.get('answer','')).strip() and not e.get('answers'): f('EXERCISE','A10',f"exercise {e.get('id')} empty answer")

# ---------- Media ----------
rr=med['reuse_report']
img_scenes=[t['topic_id'] for _,_,t in topics if 'image' in (t.get('available_content_types') or [])]
if rr['scenes']!=len(img_scenes): f('MEDIA','A9',f"reuse_report.scenes {rr['scenes']} != image scenes {len(img_scenes)}")
if rr['authored']!=rr['scenes']: f('MEDIA','A9','authored != scenes')
if rr['reused']!=0: f('MEDIA','A9','reused != 0')
concept_ids={c['concept_id'] for _,_,t in topics for c in t['concepts']}
for mn in med['media']:
    if not MEDIA_ID_RE.match(mn['id']): f('MEDIA','A9',f"media id fails MEDIA_ID_RE: {mn['id']}")
    if mn['concept_id'] not in concept_ids: f('MEDIA','A9',f"media concept_id unresolved {mn['concept_id']}")
    if mn.get('image_url','')!='': f('MEDIA','A9',f"{mn['id']} non-empty image_url (fabricated)")
    if not (mn.get('generation_prompt') or '').strip(): f('MEDIA','A9',f"{mn['id']} empty generation_prompt")
    if 'Devanagari script labels' not in (mn.get('negative_prompt') or ''): f('MEDIA','A9',f"{mn['id']} negative_prompt missing 'Devanagari script labels'")
    if '[reused frame' in json.dumps(mn,ensure_ascii=False): f('MEDIA','A9',f"{mn['id']} reused-frame stamp")
if len(med['media'])!=rr['scenes']: w('MEDIA',f"media nodes {len(med['media'])} vs scenes {rr['scenes']}")

# ---------- Publication ----------
VOC=['બાળકો','જુઓ —','બોલો']
for tid in T:
    p=P.get(tid)
    if not p: f('PUB','A16',f'{tid}: no publication block'); continue
    if not (p.get('publication_text') or '').strip(): f('PUB','A16',f'{tid}: publication_text empty')
    if p.get('publication_chunk')!=T[tid]['original_chunk']:
        f('PUB','A16',f"{tid}: publication_chunk NOT byte-identical to original_chunk (len {len(p.get('publication_chunk',''))} vs {len(T[tid]['original_chunk'])}; starts_with_original={p.get('publication_chunk','').startswith(T[tid]['original_chunk'])})")
    # index match against authoring content
    ac={c['concept_id']:c.get('content',[]) for c in A[tid].get('concepts',[])}
    got={}
    for cp in p.get('concept_publication',[]):
        got.setdefault(cp['concept_id'],set()).add(cp['content_index'])
    for cid,content in ac.items():
        para={i for i,cc in enumerate(content) if cc.get('type')=='paragraph'}
        g=got.get(cid,set())
        if g!=para: f('PUB','A16',f'{tid}/{cid}: concept_publication indices {sorted(g)} != paragraph indices {sorted(para)}')
        for cp in p.get('concept_publication',[]):
            if cp['concept_id']==cid and cp['content_index']>=len(content): f('PUB','A16',f'{tid}/{cid}: content_index {cp["content_index"]} out of range')
    for v in VOC:
        if v in (p.get('publication_text') or ''): f('PUB','A16',f'{tid}: vocative/classroom instruction in publication_text: {v}')
        for cp in p.get('concept_publication',[]):
            if v in cp.get('publication_text',''): f('PUB','A16',f"{tid}/{cp['concept_id']}[{cp['content_index']}]: vocative {v}")

print()
print("=== FAILURES (%d) ==="%len(FAIL))
for s,o,m in FAIL: print(f"[{s}] owner={o} :: {m}")
print()
print("=== WARN (%d) ==="%len(WARN))
for s,m in WARN: print(f"[{s}] {m}")
print("INFO:",INFO)
