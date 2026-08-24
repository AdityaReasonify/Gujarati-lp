#!/usr/bin/env python3
# Agent 13 — mechanical QC over 13_merged.json
import json, re, os, unicodedata, collections

D = os.path.dirname(os.path.abspath(__file__))
L = lambda n: json.load(open(os.path.join(D, n), encoding='utf-8'))
plan = L('13_merged.json')
meta = L('01_meta.json')
ex   = L('10_exercise_solutions.json')
pit  = L('07_pitfalls.json')
sen  = L('08_sensitivity.json')
media9 = L('09_media.json')
norm = open(os.path.join(D, '00_chapter_normalized.md'), encoding='utf-8').read()

topics = [t for m in plan['modules'] for s in m['segments'] for t in s['topics']]
FAIL, WARN, OK = [], [], []
def f(x): FAIL.append(x)
def w(x): WARN.append(x)

GUJ = lambda ch: 0x0A80 <= ord(ch) <= 0x0AFF
DEVA = lambda ch: 0x0900 <= ord(ch) <= 0x097F
ROMAN = lambda ch: ('A' <= ch <= 'Z') or ('a' <= ch <= 'z')

print('=== B: verbatim & script ===')
for t in topics:
    oc = t['original_chunk']
    if not oc.strip(): f('B: empty original_chunk %s' % t['topic_id'])
    dev = sorted({c for c in oc if DEVA(c)})
    rom = sorted({c for c in oc if ROMAN(c)})
    if dev: f('B: Devanagari in original_chunk %s: %r' % (t['topic_id'], dev))
    if rom: f('B: Roman in original_chunk %s: %r' % (t['topic_id'], rom))
    if '।' in oc: f('B: danda in original_chunk %s' % t['topic_id'])
    # every line present verbatim in 00_chapter_normalized.md
    for ln in oc.split('\n'):
        if ln.strip() and ln not in norm:
            f('B: chunk line not found in 00_chapter_normalized.md (%s): %r' % (t['topic_id'], ln[:70]))
    n = len(oc.split())
    if n != t['word_count']['original']:
        w('B: word_count.original %s = %d, whitespace tokens = %d' % (t['topic_id'], t['word_count']['original'], n))
print('  chunks checked:', len(topics))

# markers
mk = lambda p: len(re.findall(re.escape(p), norm))
print('  markers: ghatna %d | kadi %d | duho %d | pad %d | svadhyay %d | danda %d'
      % (mk('[[ઘટના:'), mk('[[કડી'), mk('[[દુહો'), mk('[[પદ'), mk('[[સ્વાધ્યાય:'), norm.count('।')))
if mk('[[કડી') or mk('[[દુહો') or mk('[[પદ'):
    f('B: unexpected verse markers')

# no svadhyay text became a topic
sv_heads = re.findall(r'\[\[સ્વાધ્યાય: (.+?)\]\]', norm)
for t in topics:
    for h in sv_heads:
        if h[:30] and h[:30] in t['original_chunk']:
            f('B: svadhyay heading inside topic chunk %s' % t['topic_id'])

print('=== script sweep over authored display text ===')
DISPLAY = ['topic_name','explanation','real_life_example','brief_summary','summary',
           'detailed_summary','publication_text','publication_chunk']
def walk_display(t):
    for k in DISPLAY:
        yield k, t[k]
    for k in ['concept_bullets','important_points','key_terms']:
        for i,v in enumerate(t[k]): yield '%s[%d]'%(k,i), v
    for i,r in enumerate(t['recall_questions']):
        yield 'rq[%d].prompt'%i, r['prompt']; yield 'rq[%d].answer'%i, r['answer']
    for c in t['concepts']:
        yield 'concept_name', c['concept_name']
        for i,b in enumerate(c['content']):
            if 'text' in b: yield 'content[%d].text'%i, b['text']
            if 'publication_text' in b: yield 'content[%d].pub'%i, b['publication_text']
            for j,it in enumerate(b.get('items',[])): yield 'content[%d].items[%d]'%(i,j), it
    for md in t['media']:
        for k in ['title','description','teaching_notes','generation_prompt','negative_prompt']:
            yield 'media.'+k, md[k]

BRACKET = re.compile(r'\([^)]*\)')
for t in topics:
    for k, v in walk_display(t):
        if not isinstance(v,str): continue
        stripped = BRACKET.sub('', v)
        dev = sorted({c for c in stripped if DEVA(c)})
        if dev: f('SCRIPT: Devanagari in %s %s: %r' % (t['topic_id'], k, dev))
        if k in ('media.generation_prompt','media.negative_prompt'): continue
        rom = sorted({c for c in stripped if ROMAN(c)})
        if rom: w('SCRIPT: Roman outside brackets in %s %s: %r' % (t['topic_id'], k, rom))
        if '।' in v: f('SCRIPT: danda in %s %s' % (t['topic_id'], k))

print('=== digits in display text ===')
DIG = re.compile(r'[0-9૦-૯]')
for t in topics:
    for k, v in walk_display(t):
        if not isinstance(v,str): continue
        if k in ('media.generation_prompt','media.negative_prompt'): continue
        m = DIG.findall(v)
        if m: f('DIGIT: %s %s -> %r  ...%s...' % (t['topic_id'], k, m, v[max(0,v.find(m[0])-30):v.find(m[0])+30]))

print('=== C: bands ===')
for t in topics:
    e, r = len(t['explanation'].split()), len(t['real_life_example'].split())
    st = 'OK' if 55<=e<=90 else 'FAIL'
    st2= 'OK' if 55<=r<=90 else 'FAIL'
    print('  %-10s explanation %3d %s | real_life %3d %s' % (t['topic_id'], e, st, r, st2))
    if not (55<=e<=90): f('C: explanation out of band %s = %d' % (t['topic_id'], e))
    if not (55<=r<=90): f('C: real_life_example out of band %s = %d' % (t['topic_id'], r))
    if not t['explanation'].strip(): f('C: empty explanation %s'%t['topic_id'])
    if not t['real_life_example'].strip(): f('C: empty real_life_example %s'%t['topic_id'])
    b,s,d = len(t['brief_summary'].split()), len(t['summary'].split()), len(t['detailed_summary'].split())
    if not (b < s < d): f('C: summaries not strictly increasing %s (%d,%d,%d)'%(t['topic_id'],b,s,d))
print('  objective_text words:', end=' ')
for o in plan['objectives']:
    n = len(o['objective_text'].split()); print('%s=%d'%(o['objective_id'],n), end=' ')
    if not (12<=n<=30): f('C: objective_text out of band %s = %d' % (o['objective_id'], n))
print()

print('=== D: figures_of_speech verbatim ===')
for t in topics:
    for fs in t['figures_of_speech']:
        lines = fs.get('lines','')
        for piece in ([lines] if isinstance(lines,str) else lines):
            if piece and piece not in t['original_chunk']:
                f('D: figures_of_speech.lines not verbatim in %s: %r' % (t['topic_id'], piece[:60]))
print('  fos counts:', {t['topic_id']: len(t['figures_of_speech']) for t in topics})
print('  rhyme_scheme:', {t['topic_id']: t['rhyme_scheme'] for t in topics})

print('=== Contract invariants ===')
if plan['phase'] != 2: f('CONTRACT: phase != 2')
exp_cid = 'gseb_eng_gujarati%d_ch%d' % (plan['grade'], plan['unit_number'])
if plan['chapter_id'] != exp_cid: f('CONTRACT: chapter_id %s != %s' % (plan['chapter_id'], exp_cid))
if plan['plan_id'] != '%s_v%s' % (plan['chapter_id'], plan['version']): f('CONTRACT: plan_id')
if plan['publication_id'] is None: f('CONTRACT: publication_id is null')
ids = set()
for m in plan['modules']:
    for s in m['segments']:
        for t in s['topics']: ids.add(t['topic_id']); ids.update(c['concept_id'] for c in t['concepts'])
# traversal position
mi=0
for m in plan['modules']:
    mi+=1
    if m['module_id']!='M%d'%mi: f('CONTRACT: module_id %s at pos %d'%(m['module_id'],mi))
si=0; ti=0; ci=0
for m in plan['modules']:
    for s in m['segments']:
        si+=1
        if s['segment_id']!='%s.S%d'%(m['module_id'],si): f('CONTRACT: segment_id %s at pos %d'%(s['segment_id'],si))
        for t in s['topics']:
            ti+=1
            if t['topic_id']!='%s.T%d'%(s['segment_id'],ti): f('CONTRACT: topic_id %s at pos %d'%(t['topic_id'],ti))
            if not t['concepts']: f('CONTRACT: topic without concepts %s'%t['topic_id'])
            for c in t['concepts']:
                ci+=1
                if c['concept_id']!='%s.C%d'%(t['topic_id'],ci): f('CONTRACT: concept_id %s expected %s.C%d'%(c['concept_id'],t['topic_id'],ci))
                if not c['content']: f('CONTRACT: empty concept content %s'%c['concept_id'])
                if c['objective_id'] not in {o['objective_id'] for o in plan['objectives']}: f('CONTRACT: concept objective_id unresolved %s'%c['concept_id'])
oids = {o['objective_id'] for o in plan['objectives']}
if len(oids)!=len(plan['objectives']): f('CONTRACT: duplicate objective_id')
for o in plan['objectives']:
    if o['home_topic_id'] not in ids: f('CONTRACT: home_topic_id unresolved %s'%o['objective_id'])
    for a in o['anchor']:
        if a not in ids: f('CONTRACT: anchor unresolved %s -> %s'%(o['objective_id'],a))
legacy = {o['legacy_id'] for o in plan['objectives']}
if set(plan['strand_to_objective_map'].keys()) != legacy: f('CONTRACT: strand_to_objective_map keys != legacy_ids')
for k,v in plan['strand_to_objective_map'].items():
    if v not in oids: f('CONTRACT: strand map value %s unresolved'%v)
obj_by = {o['objective_id']: o for o in plan['objectives']}
for t in topics:
    for oid in t['objective_ids']:
        if oid not in oids: f('CONTRACT: topic objective_ids unresolved %s %s'%(t['topic_id'],oid))
    lo = {l['objective_id']: l for l in t['learning_objectives']}
    if set(lo)!=set(t['objective_ids']): f('CONTRACT: inline mirror set mismatch %s'%t['topic_id'])
    for oid,l in lo.items():
        if l['objective_text'] != obj_by[oid]['objective_text']: f('CONTRACT: inline mirror text drift %s %s'%(t['topic_id'],oid))
        if 'image_examples' not in l: f('CONTRACT: inline mirror missing image_examples %s'%t['topic_id'])
    for dep in t['depends_on']:
        if dep not in ids: f('CONTRACT: depends_on unresolved %s -> %s'%(t['topic_id'],dep))
    if t['topic_type'] not in ('POEM','STORY_TELLING','CONCEPT','REVIEW'): f('CONTRACT: topic_type %s'%t['topic_type'])
MEDIA_ID_RE = re.compile(r'^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$')
RQ_RE = re.compile(r'^M\d+\.S\d+\.T\d+\.RQ\d+$')
TR_RE = re.compile(r'^M\d+\.S\d+\.T\d+\.TR\d+$')
for t in topics:
    for md in t['media']:
        if not MEDIA_ID_RE.match(md['id']): f('CONTRACT: media id %s'%md['id'])
        if md['concept_id'] not in ids: f('CONTRACT: media concept_id unresolved %s'%md['id'])
    for r in t['recall_questions']:
        if not RQ_RE.match(r['id']): f('CONTRACT: recall id %s'%r['id'])
        if '.SR' in r['id'] or '.SR' in r.get('legacy_id',''): f('CONTRACT: .SR id %s'%r['id'])
        if not TR_RE.match(r.get('legacy_id','')): f('CONTRACT: recall legacy_id %s'%r.get('legacy_id'))
        if r['bloom_level']!=r['bloom_level'].lower(): f('CONTRACT: bloom_level not lowercase %s'%r['id'])
        if not r['answer'].strip(): f('CONTRACT: empty recall answer %s'%r['id'])
for o in plan['objectives']:
    if o['bloom_level'][:1]!=o['bloom_level'][:1].upper(): f('CONTRACT: objective bloom not capitalised %s'%o['objective_id'])
tools = [t['2d_tool'] for t in topics if t['2d_tool']]
if len(tools)>1: f('CONTRACT: %d 2d_tools'%len(tools))
print('  2d_tool count:', len(tools))

print('=== Media ===')
rr = media9['reuse_report']
scenes = sum(1 for t in topics if 'image' in t['available_content_types'])
print('  reuse_report:', rr, '| topics with image:', scenes)
if rr['scenes']!=scenes: f('MEDIA: reuse_report.scenes %d != topics with image %d'%(rr['scenes'],scenes))
if rr['authored']!=rr['scenes']: f('MEDIA: authored != scenes')
if rr['reused']!=0: f('MEDIA: reused != 0')
for t in topics:
    for md in t['media']:
        if md['image_url']!='': f('MEDIA: non-empty image_url %s'%md['id'])
        if not md['generation_prompt'].strip(): f('MEDIA: empty generation_prompt %s'%md['id'])
        if 'reused frame' in md.get('teaching_notes',''): f('MEDIA: reused-frame stamp %s'%md['id'])
        if 'Devanagari script labels' not in md['negative_prompt']: f('MEDIA: negative_prompt lacks Devanagari script labels %s'%md['id'])

print('=== Publication ===')
pub = L('16_publication.json')
pub_by = {t['topic_id']: t for t in pub['topics']}
for t in topics:
    if not t['publication_text'].strip(): f('PUB: empty publication_text %s'%t['topic_id'])
    if t['original_chunk'] not in t['publication_chunk']:
        f('PUB: original_chunk NOT byte-identical inside publication_chunk %s'%t['topic_id'])
    npar = sum(1 for c in t['concepts'] for b in c['content'] if b.get('type')=='paragraph')
    ncp  = len(pub_by[t['topic_id']]['concept_publication'])
    got  = sum(1 for c in t['concepts'] for b in c['content'] if 'publication_text' in b)
    if npar!=ncp or got!=ncp: f('PUB: index/count mismatch %s paragraphs=%d concept_publication=%d attached=%d'%(t['topic_id'],npar,ncp,got))
    for k in ['publication_text','publication_chunk']:
        for bad in ['બાળકો','જુઓ —','બોલો']:
            if bad in t[k]: w('PUB: vocative/instruction %r in %s %s'%(bad,t['topic_id'],k))
    for c in t['concepts']:
        for b in c['content']:
            if 'publication_text' in b:
                for bad in ['બાળકો','જુઓ —','બોલો']:
                    if bad in b['publication_text']: w('PUB: vocative %r in concept pub %s'%(bad,c['concept_id']))

print('=== Exercises ===')
inv = meta['exercise_inventory']
cr = ex['coverage_report']
print('  inventory %d | blocks_found %s | answered %s | unanswered %s | unmapped %s'
      % (len(inv), len(cr.get('blocks_found') or []), len(cr.get('blocks_answered') or []), cr.get('unanswered'), len(cr.get('unmapped') or [])))
bf = cr.get('blocks_found'); bfn = len(bf) if isinstance(bf,list) else bf
if bfn != len(inv): f('EX: blocks_found %s != inventory %d'%(bfn,len(inv)))
if cr.get('unanswered'): f('EX: unanswered %s'%cr.get('unanswered'))

print('=== D: hard pitfalls / sensitivity ===')
hard = [(t['topic_id'], c) for t in pit['topics'] for c in t['avoid_checks'] if c['severity']=='hard']
print('  pitfall hard items:', len(hard), '| soft:', sum(1 for t in pit['topics'] for c in t['avoid_checks'] if c['severity']!='hard'))
sh = [t for t in sen['topics'] if t.get('severity')=='hard']
print('  sensitivity hard items:', len(sh), [t['topic_id'] for t in sh])
AREAS = {'ધર્મ','સમુદાય','ક્ષેત્ર','વિકલાંગતા','સંઘર્ષ','જાતિ-ભૂમિકા','સુરક્ષા'}
for t in sen.get('topics',[]):
    for a in (t.get('areas') or []):
        if a not in AREAS: f('SENS: area label not in fixed seven: %r'%a)

print()
print('#### FAIL (%d)' % len(FAIL))
for x in FAIL: print('  -', x)
print('#### WARN (%d)' % len(WARN))
for x in WARN: print('  -', x)
