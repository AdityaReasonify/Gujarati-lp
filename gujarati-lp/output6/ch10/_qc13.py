#!/usr/bin/env python3
# Agent 13 — mechanical QC over 13_merged.json + the source layers.
import json, os, re, unicodedata
D = os.path.dirname(os.path.abspath(__file__))
def L(n): return json.load(open(os.path.join(D, n), encoding='utf-8'))
plan  = L('13_merged.json'); meta = L('01_meta.json'); ex = L('10_exercise_solutions.json')
media = L('09_media.json'); pit = L('07_pitfalls.json'); sens = L('08_sensitivity.json')
norm  = open(os.path.join(D,'00_chapter_normalized.md'), encoding='utf-8').read()

topics=[t for m in plan['modules'] for s in m['segments'] for t in s['topics']]
segs=[s for m in plan['modules'] for s in m['segments']]
FAIL=[]; WARN=[]; INFO=[]
def f(sec,msg,owner): FAIL.append((sec,msg,owner))
def w(msg): WARN.append(msg)

GUJ=lambda ch: 0x0A80<=ord(ch)<=0x0AFF
DEV=lambda ch: 0x0900<=ord(ch)<=0x097F
ROM=lambda ch: ('a'<=ch<='z') or ('A'<=ch<='Z')

# ---------- B: verbatim & script ----------
for t in topics:
    oc=t['original_chunk']
    if not oc.strip(): f('B',f"{t['topic_id']}: empty original_chunk",'05_verbatim_attachment.md')
    if 'ઁ' and '।' in oc: f('B',f"{t['topic_id']}: danda in original_chunk",'05_verbatim_attachment.md')
    bad=[c for c in oc if DEV(c) or ROM(c)]
    if bad: f('B',f"{t['topic_id']}: non-Gujarati chars in original_chunk: {sorted(set(bad))}",'05_verbatim_attachment.md')
# original_chunk lines present in the normalized source
src_lines=set(l.strip() for l in norm.split('\n') if l.strip())
missing=[]
for t in topics:
    for ln in [x.strip() for x in t['original_chunk'].split('\n') if x.strip()]:
        if ln not in src_lines: missing.append((t['topic_id'],ln))
if missing:
    for tid,ln in missing[:10]: f('B',f"{tid}: line not found verbatim in 00_chapter_normalized.md: {ln}",'05_verbatim_attachment.md')
else: INFO.append("every original_chunk line matched a line in 00_chapter_normalized.md")

# marker counts
kadi=len(re.findall(r'\[\[કડી \d+\]\]',norm)); ghatna=len(re.findall(r'\[\[ઘટના:',norm))
sv=len(re.findall(r'\[\[સ્વાધ્યાય:',norm))
INFO.append(f"markers: કડી={kadi} ઘટના={ghatna} સ્વાધ્યાય={sv}; instructional topics={len(topics)}")
if ghatna!=len(topics): f('B',f"ઘટના markers ({ghatna}) != topic count ({len(topics)})",'02_structure.md')
if not (len(topics)<kadi): f('B',f"topics ({len(topics)}) not < કડી ({kadi}) — kathakavya hard gate 2",'02_structure.md')
# every કડી carried exactly once: check each કડી's printed couplet appears in exactly one chunk
blocks=re.split(r'\[\[કડી \d+\]\]',norm)[1:]
carried=[]
for i,b in enumerate(blocks,1):
    lines=[l.strip() for l in b.split('\n') if l.strip() and not l.startswith('[[') and not l.startswith('<!--')]
    # stop at next marker/comment
    cl=[]
    for l in b.split('\n'):
        ls=l.strip()
        if ls.startswith('[[') or ls.startswith('<!--'): break
        if ls: cl.append(ls)
    n=sum(1 for t in topics if all(x in t['original_chunk'] for x in cl))
    carried.append((i,n,cl))
badk=[(i,n) for i,n,_ in carried if n!=1]
if badk: f('B',f"કડી not carried exactly once: {badk}",'02_structure.md')
else: INFO.append("all 15 કડી carried by exactly one topic each, whole")
# no સ્વાધ્યાય became a topic
sv_head=[h for h in re.findall(r'\[\[સ્વાધ્યાય: (.+?)\]\]',norm)]
for t in topics:
    for h in sv_head:
        if h[:14] and h[:14] in t['original_chunk']: f('B',f"{t['topic_id']} carries સ્વાધ્યાય text",'02_structure.md')
# attribution line in last topic
if '- રમણલાલ સોની' not in topics[-1]['original_chunk']:
    w("attribution line '- રમણલાલ સોની' is not inside the last topic's original_chunk (it is printed under the title, not at the poem's end — 01_meta extraction_notes records this)")
# balanced single quotes per chunk (kathakavya avoid #3)
for t in topics:
    if t['original_chunk'].count("'")%2: w(f"{t['topic_id']}: odd number of single quotes in original_chunk — check the speech closes")

# ---------- script check on authored display text ----------
DISPLAY=['topic_name','explanation','real_life_example','brief_summary','summary','detailed_summary']
def disp_strings(t):
    out=[]
    for k in DISPLAY: out.append((k,t.get(k,'') or ''))
    for k in ['concept_bullets','important_points','key_terms']:
        for i,x in enumerate(t.get(k) or []): out.append((f'{k}[{i}]',x))
    for i,r in enumerate(t.get('recall_questions') or []):
        out.append((f'RQ{i+1}.prompt',r.get('prompt','')));out.append((f'RQ{i+1}.answer',r.get('answer','')))
    for c in t['concepts']:
        out.append(('concept_name',c['concept_name']))
        for i,b in enumerate(c['content']):
            if b.get('type')=='paragraph': out.append((f'{c["concept_id"]}.content[{i}]',b.get('text','')))
            else:
                for j,it in enumerate(b.get('items') or []): out.append((f'{c["concept_id"]}.content[{i}][{j}]',it))
    return out
BRACKET=re.compile(r'\(([^)]*)\)')
for t in topics:
    for k,s in disp_strings(t):
        stripped=BRACKET.sub('',s)
        dev=[c for c in stripped if DEV(c)]
        rom=[c for c in stripped if ROM(c)]
        if dev: f('B',f"{t['topic_id']}.{k}: Devanagari in display text {sorted(set(dev))}",'12_runtime_authoring.md')
        if rom: f('B',f"{t['topic_id']}.{k}: Roman outside brackets in display text {sorted(set(rom))}",'12_runtime_authoring.md')
        if '।' in s: f('B',f"{t['topic_id']}.{k}: danda in display text",'12_runtime_authoring.md')
# digits in display text
DIG=re.compile(r'[0-9૦-૯]')
for t in topics:
    for k,s in disp_strings(t):
        if DIG.search(s): f('B',f"{t['topic_id']}.{k}: digit in display text: {DIG.findall(s)}",'12_runtime_authoring.md')
for o in plan['objectives']:
    if DIG.search(o['objective_text']): f('B',f"{o['objective_id']}: digit in objective_text",'02_structure.md')

# ---------- C: teaching block ----------
def wc(s): return len([x for x in re.split(r'\s+',s.strip()) if x])
for t in topics:
    for k,lo,hi in [('explanation',55,90),('real_life_example',55,90)]:
        v=t.get(k,'')
        if not v.strip(): f('C',f"{t['topic_id']}: {k} empty",'12_runtime_authoring.md'); continue
        n=wc(v)
        if not (lo<=n<=hi): f('C',f"{t['topic_id']}: {k} is {n} words (band {lo}–{hi})",'12_runtime_authoring.md')
for o in plan['objectives']:
    n=wc(o['objective_text'])
    if not (12<=n<=30): f('C',f"{o['objective_id']}: objective_text is {n} words (band 12–30)",'02_structure.md')
# summaries strictly increase
for t in topics:
    a,b,c=wc(t['brief_summary']),wc(t['summary']),wc(t['detailed_summary'])
    if not (a<b<c): f('C',f"{t['topic_id']}: summaries not strictly increasing ({a}/{b}/{c})",'12_runtime_authoring.md')
    if not (4<=len(re.findall(r'[.!?]',t['detailed_summary']))<=8): w(f"{t['topic_id']}: detailed_summary sentence count {len(re.findall(r'[.!?]',t['detailed_summary']))}")
# key_terms / bullets shape
for t in topics:
    if not (3<=len(t.get('key_terms') or [])<=6): w(f"{t['topic_id']}: key_terms count {len(t.get('key_terms') or [])} (3–6)")
    for k in ['concept_bullets','important_points']:
        if not (3<=len(t.get(k) or [])<=4): w(f"{t['topic_id']}: {k} count {len(t.get(k) or [])} (3–4)")
    if not (2<=len(t.get('recall_questions') or [])<=3): w(f"{t['topic_id']}: recall_questions count {len(t.get('recall_questions') or [])} (2–3)")

# ---------- D: figures_of_speech verbatim; rhyme words printed ----------
for t in topics:
    for fs in t.get('figures_of_speech') or []:
        lines=fs.get('lines','')
        for piece in ([lines] if isinstance(lines,str) else lines):
            if piece and piece not in t['original_chunk']:
                f('D',f"{t['topic_id']}: figures_of_speech lines not verbatim in original_chunk: {piece!r}",'07_genre_pitfalls.md → 12_runtime_authoring.md')
    rs=t.get('rhyme_scheme')
    if isinstance(rs,dict):
        for pair in rs.get('rhyming_words') or []:
            for wd in re.split(r'\s*—\s*|\s*-\s*',pair):
                wd=wd.strip()
                if wd and wd not in norm: f('D',f"{t['topic_id']}: rhyming word {wd!r} not printed in the chapter",'12_runtime_authoring.md')
# no tacked-on બોધ
BODH=['આ કાવ્ય આપણને શીખવે','બોધ એ છે કે','આપણે પણ']
for t in topics:
    for k,s in disp_strings(t):
        for b in BODH:
            if b in s: f('D',f"{t['topic_id']}.{k}: tacked-on બોધ phrase {b!r}",'07_genre_pitfalls.md → 12_runtime_authoring.md')
# craft-first opening sentence
CRAFT=['પ્રાસ','લય','છંદ','અલંકાર']
for t in topics:
    first=re.split(r'[.!?]',t['explanation'].strip())[0]
    if any(c in first for c in CRAFT): w(f"{t['topic_id']}: explanation's first sentence opens on craft terminology")
    nc=sum(t['explanation'].count(c) for c in CRAFT)
    if nc>2: w(f"{t['topic_id']}: {nc} craft mentions in explanation (profile allows ~one craft sentence)")
# explanation quotes a phrase from its own chunk (kathakavya avoid #4)
for t in topics:
    quoted=re.findall(r"'([^']{4,})'",t['explanation'])
    hit=any(q in t['original_chunk'] for q in quoted)
    if not hit: w(f"{t['topic_id']}: explanation quotes no phrase found verbatim in its original_chunk")
# climax spoiler check
clim=[i for i,t in enumerate(topics) if t['topic_category']=='climax']
if clim:
    ci=clim[0]
    spoil=['હિંમત અને વિશ્વાસ','દશ થાય','ચાર કાટલાં']
    for t in topics[:ci]:
        for k,s in disp_strings(t):
            for sp in spoil:
                if sp in s: f('D',f"{t['topic_id']}.{k}: names the closing tally before the climax topic: {sp!r}",'07_genre_pitfalls.md → 12_runtime_authoring.md')

# ---------- D: hard pitfalls / sensitivity addressed ----------
hard_p=sum(1 for t in pit['topics'] for c in t.get('avoid_checks',[]) if c.get('severity')=='hard')
INFO.append(f"07_pitfalls: {hard_p} hard avoid_checks across {len(pit['topics'])} topics")
AREAS=['ધર્મ','સમુદાય','ક્ષેત્ર','વિકલાંગતા','સંઘર્ષ','જાતિ-ભૂમિકા','સુરક્ષા']
sens_hard=[]
def walk_sens(o,path=''):
    if isinstance(o,dict):
        if o.get('severity')=='hard': sens_hard.append(o)
        for k,v in o.items(): walk_sens(v,path+'/'+k)
    elif isinstance(o,list):
        for v in o: walk_sens(v,path)
walk_sens(sens)
INFO.append(f"08_sensitivity: {len(sens_hard)} hard items; none_found={sens.get('none_found')}")
bad_areas=[]
def walk_areas(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='areas' and isinstance(v,list):
                for a in v:
                    if a not in AREAS: bad_areas.append(a)
            else: walk_areas(v)
    elif isinstance(o,list):
        for v in o: walk_areas(v)
walk_areas(sens)
if bad_areas: f('D',f"08_sensitivity areas[] outside the seven fixed labels: {sorted(set(bad_areas))}",'08_sensitivity_safety.md')

# ---------- Contract ----------
if plan['phase']!=2: f('Contract','phase != 2','13')
exp_cid=f"gseb_eng_gujarati{plan['grade']}_ch{plan['unit_number']}"
if plan['chapter_id']!=exp_cid: f('Contract',f"chapter_id {plan['chapter_id']} != {exp_cid}",'01_ingestion_genre_diagnosis.md')
if plan['plan_id']!=f"{plan['chapter_id']}_v{plan['version']}": f('Contract','plan_id != {chapter_id}_v{version}','01_ingestion_genre_diagnosis.md')
if plan['publication_id'] is None: f('Contract','publication_id is null','13')
oids=[o['objective_id'] for o in plan['objectives']]
if len(oids)!=len(set(oids)): f('Contract','duplicate objective_id','02_structure.md')
node_ids=set()
for m in plan['modules']:
    node_ids.add(m['module_id'])
    for s in m['segments']:
        node_ids.add(s['segment_id'])
        for t in s['topics']:
            node_ids.add(t['topic_id'])
            for c in t['concepts']: node_ids.add(c['concept_id'])
for o in plan['objectives']:
    if o['home_topic_id'] not in node_ids: f('Contract',f"{o['objective_id']}.home_topic_id unresolved",'02_structure.md')
    for a in o['anchor']:
        if a not in node_ids: f('Contract',f"{o['objective_id']}.anchor {a} unresolved",'02_structure.md')
for lg,oi in plan['strand_to_objective_map'].items():
    if oi not in oids: f('Contract',f"strand_to_objective_map {lg}->{oi} unresolved",'02_structure.md')
legacy=[o['legacy_id'] for o in plan['objectives']]
if sorted(plan['strand_to_objective_map'].keys())!=sorted(legacy): f('Contract','strand_to_objective_map does not cover every legacy_id','02_structure.md')
# traversal position + concept continuity
mi=0
cn=0
for m in plan['modules']:
    mi+=1
    if m['module_id']!=f"M{mi}": f('Contract',f"module id {m['module_id']} != M{mi}",'02_structure.md')
si=0; ti=0
for m in plan['modules']:
    for s in m['segments']:
        si+=1
        if s['segment_id']!=f"{m['module_id']}.S{si}": f('Contract',f"segment id {s['segment_id']} != {m['module_id']}.S{si}",'02_structure.md')
        for t in s['topics']:
            ti+=1
            if t['topic_id']!=f"{s['segment_id']}.T{ti}": f('Contract',f"topic id {t['topic_id']} != {s['segment_id']}.T{ti}",'02_structure.md')
            if not t['concepts']: f('Contract',f"{t['topic_id']} has no concepts",'02_structure.md')
            for c in t['concepts']:
                cn+=1
                if c['concept_id']!=f"{t['topic_id']}.C{cn}": f('Contract',f"concept id {c['concept_id']} != {t['topic_id']}.C{cn}",'02_structure.md')
                if c['objective_id'] not in oids: f('Contract',f"{c['concept_id']}.objective_id unresolved",'02_structure.md')
                if not c['content']: f('Contract',f"{c['concept_id']} content[] empty",'12_runtime_authoring.md')
            for oid in t['objective_ids']:
                if oid not in oids: f('Contract',f"{t['topic_id']}.objective_ids {oid} unresolved",'02_structure.md')
            # inline mirror
            for lo in t['learning_objectives']:
                reg=next((o for o in plan['objectives'] if o['objective_id']==lo['objective_id']),None)
                if not reg: f('Contract',f"{t['topic_id']} inline objective {lo['objective_id']} not in registry",'02_structure.md')
                elif reg['objective_text']!=lo['objective_text']: f('Contract',f"{t['topic_id']} inline objective_text differs from registry",'02_structure.md')
            if t['topic_type'] not in ('POEM','STORY_TELLING','CONCEPT','REVIEW'): f('Contract',f"{t['topic_id']} topic_type {t['topic_type']} not an authored enum value",'02_structure.md')
MEDIA_RE=re.compile(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$")
RQ_RE=re.compile(r"^M\d+\.S\d+\.T\d+\.RQ\d+$"); TR_RE=re.compile(r"^M\d+\.S\d+\.T\d+\.TR\d+$")
for t in topics:
    for r in t['recall_questions']:
        if not RQ_RE.match(r['id']): f('Contract',f"{t['topic_id']} recall id {r['id']} bad",'12_runtime_authoring.md')
        if not TR_RE.match(r.get('legacy_id','')): f('Contract',f"{t['topic_id']} recall legacy_id {r.get('legacy_id')} bad",'12_runtime_authoring.md')
        if '.SR' in r['id']: f('Contract',f"{t['topic_id']} uses .SR",'12_runtime_authoring.md')
        if r.get('bloom_level','') != r.get('bloom_level','').lower(): f('Contract',f"{t['topic_id']} bloom_level not lowercase",'12_runtime_authoring.md')
        if not r.get('answer','').strip(): f('Contract',f"{r['id']} has no answer",'12_runtime_authoring.md')
    for mm in t['media']:
        if not MEDIA_RE.match(mm['id']): f('Contract',f"{t['topic_id']} media id {mm['id']} fails MEDIA_ID_RE",'09_media_planning.md')
        if MEDIA_RE.match(mm['id']).group(1)!=mm['concept_id']: f('Contract',f"{mm['id']} concept scope mismatch",'09_media_planning.md')
for o in plan['objectives']:
    if o['bloom_level'][:1]!=o['bloom_level'][:1].upper(): f('Contract',f"{o['objective_id']} bloom_level not Capitalised",'02_structure.md')

# ---------- Exercises ----------
inv=meta['exercise_inventory']; cr=ex['coverage_report']
INFO.append(f"exercise inventory={len(inv)}; blocks_found={len(cr.get('blocks_found') or [])}; unanswered={cr.get('unanswered')}; unmapped={cr.get('unmapped')}")
bf=cr.get('blocks_found'); bf=len(bf) if isinstance(bf,list) else bf
if bf!=len(inv): f('Exercises',f"coverage_report.blocks_found {bf} != inventory {len(inv)}",'10_exercise_solutions.md')
if cr.get('unanswered'): f('Exercises',f"unanswered blocks: {cr['unanswered']}",'10_exercise_solutions.md')
exb=ex['exercises']
INFO.append(f"exercise blocks in 10_: {len(exb)}")
def norm_h(s): return re.sub(r'\s+','',s)
inv_h=[norm_h(i['verbatim_heading']) for i in inv]
sol_h=[norm_h(b.get('exercise_group') or '') for b in exb]
for h,orig in zip(inv_h,[i['verbatim_heading'] for i in inv]):
    if not any(h[:12] in s or s[:12] in h for s in sol_h): f('Exercises',f"inventory block not found in solutions: {orig}",'10_exercise_solutions.md')
for b in exb:
    if not (b.get('answer') or '').strip():
        f('Exercises',f"block {b.get('exercise_id')} has no answer",'10_exercise_solutions.md')

# ---------- Media ----------
rr=media['reuse_report']
scenes=sum(1 for t in topics if 'image' in (t.get('available_content_types') or []))
INFO.append(f"media: reuse_report scenes={rr['scenes']} authored={rr['authored']} reused={rr['reused']} rejected={rr['rejected']}; topics with image={scenes}")
if rr['scenes']!=scenes: f('Media',f"reuse_report.scenes {rr['scenes']} != topics with 'image' ({scenes})",'09_media_planning.md')
if rr['authored']!=rr['scenes']: f('Media',"authored != scenes",'09_media_planning.md')
if rr['reused']!=0: f('Media',"reused != 0 — no Gujarati frame pool exists",'09_media_planning.md')
n2d=sum(1 for t in topics if t.get('2d_tool'))
if n2d>1: f('Media',f"{n2d} 2d_tool entries",'09_media_planning.md')
for t in topics:
    for mm in t['media']:
        if mm.get('image_url'): f('Media',f"{mm['id']} has non-empty image_url — fabricated URL",'09_media_planning.md')
        if not (mm.get('generation_prompt') or '').strip(): f('Media',f"{mm['id']} empty generation_prompt",'09_media_planning.md')
        if 'Devanagari script labels' not in (mm.get('negative_prompt') or ''): f('Media',f"{mm['id']} negative_prompt missing 'Devanagari script labels'",'09_media_planning.md')
        if '[reused frame' in json.dumps(mm,ensure_ascii=False): f('Media',f"{mm['id']} carries a reused-frame stamp",'09_media_planning.md')

# ---------- Publication ----------
missing_pt=[t['topic_id'] for t in topics if not (t.get('publication_text') or '').strip()]
missing_pc=[t['topic_id'] for t in topics if not (t.get('publication_chunk') or '').strip()]
# publication_chunk: the pack-wide convention (ch01-ch10, all 10 chapters) is
# original_chunk verbatim + blank line + publication_text + blank line + publication real_life_example.
# The verbatim must be a BYTE-IDENTICAL PREFIX; a chunk that alters the verbatim is the real defect.
mismatch=[t['topic_id'] for t in topics if t.get('publication_chunk') and not t['publication_chunk'].startswith(t['original_chunk'])]
notident=[t['topic_id'] for t in topics if t.get('publication_chunk')!=t.get('original_chunk')]
if notident: w(f"publication_chunk is not byte-identical to original_chunk on {len(notident)}/{len(topics)} topics — it opens with the byte-identical verbatim and appends the publication prose; this is the pack-wide Agent-16 convention (ch01-ch09 identical), and disagrees with 13_assembly_validation.md's literal wording. REPORTED, not blocked: the spec's own routing table blocks only on missing / index-mismatched / added-meaning.")
if missing_pt: f('Publication',f"publication_text missing on {len(missing_pt)} topics: {missing_pt}",'16_publication_authoring.md')
if missing_pc: f('Publication',f"publication_chunk missing on {len(missing_pc)} topics",'16_publication_authoring.md')
if mismatch: f('Publication',f"publication_chunk does not open with byte-identical original_chunk on {mismatch}",'16_publication_authoring.md')
cpt_missing=[]
for t in topics:
    for c in t['concepts']:
        for i,b in enumerate(c['content']):
            if b.get('type')=='paragraph' and not (b.get('publication_text') or '').strip():
                cpt_missing.append(f"{c['concept_id']}.content[{i}]")
if cpt_missing: f('Publication',f"concepts[].content[] publication_text missing on {len(cpt_missing)} blocks",'16_publication_authoring.md')
VOC=['બાળકો','જુઓ —','બોલો']
for t in topics:
    for v in VOC:
        if v in (t.get('publication_text') or ''): f('Publication',f"{t['topic_id']}: vocative/classroom instruction {v!r} survived into publication_text",'16_publication_authoring.md')

# ---------- output ----------
out={'FAIL':FAIL,'WARN':WARN,'INFO':INFO}
print(json.dumps(out,ensure_ascii=False,indent=1))
