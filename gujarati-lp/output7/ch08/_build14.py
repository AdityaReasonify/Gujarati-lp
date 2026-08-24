#!/usr/bin/env python3
"""Agent 14 — arrange, renumber, translate references, whitelist, emit learning_plan_logical.json."""
import json, os, re, collections

D = os.path.dirname(os.path.abspath(__file__))
p = lambda n: os.path.join(D, n)
merged = json.load(open(p('13_merged.json'), encoding='utf-8'))

# ---------- 1. arrange (reading order) + 2. renumber consecutively ----------
order = json.load(open(p('05b_textbook_order.json'), encoding='utf-8'))['textbook_order']

idmap = {}                      # old id -> new id  (every node level)
m_i = s_i = t_i = c_i = 0
traversal = []
for mod in merged['modules']:
    m_i += 1
    new_m = 'M%d' % m_i
    idmap[mod['module_id']] = new_m
    for seg in mod['segments']:
        s_i += 1
        new_s = '%s.S%d' % (new_m, s_i)
        idmap[seg['segment_id']] = new_s
        for top in seg['topics']:
            t_i += 1
            new_t = '%s.T%d' % (new_s, t_i)
            idmap[top['topic_id']] = new_t
            traversal.append(top['topic_id'])
            for con in top.get('concepts', []):
                c_i += 1
                idmap[con['concept_id']] = '%s.C%d' % (new_t, c_i)

assert traversal == order, 'merged traversal != reading order\n%s\n%s' % (traversal, order)
identity = all(k == v for k, v in idmap.items())

def newid(old):
    return idmap[old]

def remap_media(mid):
    """{concept_id}.{IMG|VID|2D|3D|SIM}{n}"""
    mm = re.match(r'^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$', mid)
    assert mm, 'bad media id %s' % mid
    return '%s.%s%s' % (newid(mm.group(1)), mm.group(2), mm.group(3))

def remap_rq(rid):
    """{node_id}.{RQ|TR}{n}"""
    mm = re.match(r'^(M\d+(?:\.S\d+)?(?:\.T\d+)?)\.(RQ|TR)(\d+)$', rid)
    assert mm, 'bad recall id %s' % rid
    return '%s.%s%s' % (newid(mm.group(1)), mm.group(2), mm.group(3))

# ---------- whitelists ----------
ROOT_KEYS = ['phase','board','subject','grade','level','version','ordering','chapter_id','plan_id',
             'author','_activate','medium_id','subject_ref_id','chapter_master_id','publication_id',
             'english_plan_id','english_chapter_id','estimated_time','textbook','textbook_url',
             'textbook_pages','unit_title','unit_number','topic_title','topic_number','chapter_name',
             'genre','teaching_lens','guiding_question','objectives','strand_to_objective_map','modules']
assert len(ROOT_KEYS) == 32 and len(set(ROOT_KEYS)) == 32

MODULE_KEYS  = ['module_id','module_name','difficult_words','overall_rhyme_scheme','segments']
SEGMENT_KEYS = ['segment_id','segment_name','brief_summary','summary','detailed_summary',
                'important_points','recall_questions','topics']
TOPIC_KEYS = ['topic_id','topic_name','topic_type','topic_category','difficulty','original_chunk',
              'modified_chunk','word_count','explanation','real_life_example','brief_summary',
              'summary','detailed_summary','key_terms','concept_bullets','important_points',
              'figures_of_speech','rhyme_scheme','shabdarth','samanarthi','vilom','vyakaran',
              'objective_ids','learning_objectives','concepts','recall_questions','media','2d_tool',
              'publication_text','publication_chunk','depends_on','source_topic_ids',
              'estimated_exchanges','primary_content_type','secondary_content_type',
              'tertiary_content_type','available_content_types']
OBJ_KEYS  = ['objective_id','legacy_id','strand','strand_name','objective_text','bloom_level',
             'home_topic_id','anchor','status','theme_category']
LO_KEYS   = ['objective_id','legacy_id','strand','strand_name','objective_text','bloom_level',
             'home_topic_id','anchor','theme_category','image_examples']
CON_KEYS  = ['concept_id','concept_name','objective_id','key_terms','content']
RQ_KEYS   = ['id','legacy_id','prompt','answer','difficulty','bloom_level']
SEG_RQ_KEYS = ['id','prompt','answer','difficulty','bloom_level']
MEDIA_KEYS= ['id','type','subtype','title','description','image_url','aspect_ratio','concept_id',
             'home_concept_id','objective_id','image_category','teaching_notes','negative_prompt',
             'generation_prompt']

dropped = collections.Counter()
def pick(src, keys, label):
    for k in src:
        if k not in keys:
            dropped['%s.%s' % (label, k)] += 1
    return {k: src[k] for k in keys if k in src}

TYPE_MAP = {'POEM':'instructional','STORY_TELLING':'instructional','CONCEPT':'instructional',
            'REVIEW':'summary','EXERCISE':'assessment',
            'instructional':'instructional','summary':'summary','assessment':'assessment'}

# ---------- root ----------
out = {}
for k in ROOT_KEYS:
    if k in merged:
        out[k] = merged[k]
out['phase'] = 2
out['ordering'] = 'logical'
out['version'] = merged.get('version', 1)
out['chapter_id'] = 'gseb_eng_gujarati%d_ch%d' % (merged['grade'], merged['unit_number'])
out['plan_id'] = '%s_v%d' % (out['chapter_id'], out['version'])
out['_activate'] = False
out['subject_ref_id'] = None
out['medium_id'] = None
out['english_plan_id'] = None
out['english_chapter_id'] = None

# DB ids from the registry — never invented.
reg = json.load(open(os.path.join(D, '..', '..', 'upload_reference', 'chapter_master_map.json'),
                     encoding='utf-8')).get(out['chapter_id']) or {}
out['chapter_master_id'] = reg.get('chapter_master_id', merged.get('chapter_master_id'))
out['publication_id'] = reg.get('publication_id') if reg.get('publication_id') is not None \
                        else merged.get('publication_id')

# ---------- objectives (O{n} NOT renumbered; their pointers ARE) ----------
objs = []
for o in merged['objectives']:
    o2 = pick(o, OBJ_KEYS, 'objective')
    o2['home_topic_id'] = newid(o2['home_topic_id'])
    o2['anchor'] = [newid(a) for a in (o2.get('anchor') or [])]
    objs.append(o2)
out['objectives'] = objs
out['strand_to_objective_map'] = merged['strand_to_objective_map']
reg_by_id = {o['objective_id']: o for o in objs}

# ---------- tree ----------
mods = []
for mod in merged['modules']:
    m2 = pick(mod, MODULE_KEYS, 'module')
    m2['module_id'] = newid(mod['module_id'])
    segs = []
    for seg in mod['segments']:
        s2 = pick(seg, SEGMENT_KEYS, 'segment')
        s2['segment_id'] = newid(seg['segment_id'])
        if 'recall_questions' in s2:
            rqs = []
            for r in s2['recall_questions']:
                r2 = pick(r, SEG_RQ_KEYS, 'segment.recall')
                r2['id'] = remap_rq(r['id'])
                assert '.SR' not in r2['id']
                rqs.append(r2)
            s2['recall_questions'] = rqs
        tops = []
        for top in seg['topics']:
            t2 = pick(top, TOPIC_KEYS, 'topic')
            t2['topic_id'] = newid(top['topic_id'])
            t2['topic_type'] = TYPE_MAP[top['topic_type']]
            t2['depends_on'] = [newid(x) for x in (top.get('depends_on') or [])]
            t2['source_topic_ids'] = [newid(x) for x in (top.get('source_topic_ids') or [])]
            los = []
            for lo in top.get('learning_objectives', []):
                l2 = pick(lo, LO_KEYS, 'learning_objective')
                root_o = reg_by_id[l2['objective_id']]
                # inline mirror must match the registry character for character
                for k in ('legacy_id','strand','strand_name','objective_text','bloom_level',
                          'home_topic_id','anchor','theme_category'):
                    l2[k] = root_o[k]
                l2['image_examples'] = lo.get('image_examples', [])
                los.append(l2)
            t2['learning_objectives'] = los
            cons = []
            for c in top.get('concepts', []):
                c2 = pick(c, CON_KEYS, 'concept')
                c2['concept_id'] = newid(c['concept_id'])
                cons.append(c2)
            t2['concepts'] = cons
            rqs = []
            for r in top.get('recall_questions', []):
                r2 = pick(r, RQ_KEYS, 'topic.recall')
                r2['id'] = remap_rq(r['id'])
                if 'legacy_id' in r2:
                    r2['legacy_id'] = remap_rq(r['legacy_id'])
                assert '.SR' not in r2['id']
                rqs.append(r2)
            t2['recall_questions'] = rqs
            meds = []
            for md in top.get('media', []):
                d2 = pick(md, MEDIA_KEYS, 'media')
                d2['id'] = remap_media(md['id'])
                d2['concept_id'] = newid(md['concept_id'])
                d2['home_concept_id'] = newid(md['home_concept_id'])
                meds.append(d2)
            t2['media'] = meds
            t2 = {k: t2[k] for k in TOPIC_KEYS if k in t2}
            tops.append(t2)
        s2['topics'] = tops
        segs.append({k: s2[k] for k in SEGMENT_KEYS if k in s2})
    m2['segments'] = segs
    mods.append({k: m2[k] for k in MODULE_KEYS if k in m2})
out['modules'] = mods

# ---------- 3. assert: every reference resolves ----------
node_ids, concept_ids, media_ids, rq_ids = set(), set(), set(), set()
for m in out['modules']:
    node_ids.add(m['module_id'])
    for s in m['segments']:
        node_ids.add(s['segment_id'])
        for r in s.get('recall_questions', []):
            rq_ids.add(r['id'])
        for t in s['topics']:
            node_ids.add(t['topic_id'])
            for c in t['concepts']:
                concept_ids.add(c['concept_id'])
            for x in t['media']:
                media_ids.add(x['id'])
            for r in t['recall_questions']:
                rq_ids.add(r['id'])
allids = node_ids | concept_ids

errs = []
def chk(cond, msg):
    if not cond: errs.append(msg)

# traversal position (the validator's own check)
mi = si = ti = ci = 0
for m in out['modules']:
    mi += 1; chk(m['module_id'] == 'M%d' % mi, 'module_id %s != M%d' % (m['module_id'], mi))
    for s in m['segments']:
        si += 1; exp = 'M%d.S%d' % (mi, si)
        chk(s['segment_id'] == exp, 'segment_id %s != %s' % (s['segment_id'], exp))
        for t in s['topics']:
            ti += 1; expt = '%s.T%d' % (exp, ti)
            chk(t['topic_id'] == expt, 'topic_id %s != %s' % (t['topic_id'], expt))
            for c in t['concepts']:
                ci += 1; expc = '%s.C%d' % (expt, ci)
                chk(c['concept_id'] == expc, 'concept_id %s != %s' % (c['concept_id'], expc))

seen_o = set()
for o in out['objectives']:
    chk(o['objective_id'] not in seen_o, 'duplicate objective %s' % o['objective_id'])
    seen_o.add(o['objective_id'])
    chk(o['home_topic_id'] in node_ids, 'stale home_topic_id %s on %s' % (o['home_topic_id'], o['objective_id']))
    for a in o['anchor']:
        chk(a in concept_ids, 'stale anchor %s on %s' % (a, o['objective_id']))
for lid, oid in out['strand_to_objective_map'].items():
    chk(oid in seen_o, 'strand map %s -> unknown %s' % (lid, oid))
for o in out['objectives']:
    chk(o['legacy_id'] in out['strand_to_objective_map'], 'legacy %s not in strand map' % o['legacy_id'])

for m in out['modules']:
    for s in m['segments']:
        for r in s.get('recall_questions', []):
            chk(re.match(r'^%s\.RQ\d+$' % re.escape(s['segment_id']), r['id']), 'bad seg recall %s' % r['id'])
        for t in s['topics']:
            chk(t['topic_type'] in ('instructional','summary','assessment'), 'bad topic_type %s' % t['topic_type'])
            chk(bool((t.get('original_chunk') or '').strip()), 'empty original_chunk on %s' % t['topic_id'])
            chk(len(t['concepts']) >= 1, 'no concepts on %s' % t['topic_id'])
            for oid in t['objective_ids']:
                chk(oid in seen_o, 'stale objective_ids %s on %s' % (oid, t['topic_id']))
            for lo in t['learning_objectives']:
                chk(lo['objective_id'] in seen_o, 'stale inline objective %s' % lo['objective_id'])
                chk(lo['objective_text'] == reg_by_id[lo['objective_id']]['objective_text'],
                    'inline mirror drift on %s' % t['topic_id'])
                chk(lo['home_topic_id'] in node_ids, 'stale inline home_topic_id on %s' % t['topic_id'])
                for a in lo['anchor']:
                    chk(a in concept_ids, 'stale inline anchor %s on %s' % (a, t['topic_id']))
            for c in t['concepts']:
                chk(c['objective_id'] in seen_o, 'stale concept objective %s' % c['objective_id'])
                chk(len(c.get('content') or []) > 0, 'empty concept content %s' % c['concept_id'])
            for r in t['recall_questions']:
                chk(re.match(r'^%s\.RQ\d+$' % re.escape(t['topic_id']), r['id']), 'bad recall %s' % r['id'])
                chk(re.match(r'^%s\.TR\d+$' % re.escape(t['topic_id']), r.get('legacy_id','')), 'bad legacy %s' % r.get('legacy_id'))
            for x in t['media']:
                chk(re.match(r'^M\d+\.S\d+\.T\d+\.C\d+\.(IMG|VID|2D|3D|SIM)\d+$', x['id']), 'bad media id %s' % x['id'])
                chk(x['concept_id'] in concept_ids, 'stale media concept_id %s' % x['concept_id'])
                chk(x['home_concept_id'] in concept_ids, 'stale media home_concept_id %s' % x['home_concept_id'])
                chk(x['id'].startswith(x['concept_id'] + '.'), 'media id not scoped to its concept: %s' % x['id'])
            for x in t['depends_on']:
                chk(x in node_ids, 'stale depends_on %s on %s' % (x, t['topic_id']))
            for x in t['source_topic_ids']:
                chk(x in node_ids, 'stale source_topic_ids %s on %s' % (x, t['topic_id']))

chk(out['publication_id'] is not None, 'publication_id is null — the server rejects null')
chk(out['plan_id'] == '%s_v%d' % (out['chapter_id'], out['version']), 'plan_id malformed')
out = {k: out[k] for k in ROOT_KEYS}
chk(list(out.keys()) == ROOT_KEYS, 'root key set/order drift: %s' % (set(ROOT_KEYS) ^ set(out.keys())))

# ---------- covered_by_topics rewrite in 10_exercise_solutions.json ----------
ex_path = p('10_exercise_solutions.json')
ex_raw = open(ex_path, encoding='utf-8').read()
ex = json.loads(ex_raw)
cov_changed = 0
cov_stale = []
for e in ex['exercises']:
    cov = e.get('covered_by_topics') or []
    new = []
    for cid in cov:
        n = idmap.get(cid)
        if n is None:
            cov_stale.append((e['exercise_id'], cid)); new.append(cid)
        else:
            if n != cid: cov_changed += 1
            new.append(n)
    if cov: e['covered_by_topics'] = new
for eid, cid in cov_stale:
    errs.append('covered_by_topics %s on %s resolves to no node' % (cid, eid))

if errs:
    print('HARD FAIL:'); [print('  -', e) for e in errs]; raise SystemExit(1)

json.dump(out, open(p('learning_plan_logical.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
if cov_changed:
    json.dump(ex, open(ex_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('identity renumber:', identity, '| ids remapped:', sum(1 for k,v in idmap.items() if k!=v))
print('modules %d segments %d topics %d concepts %d media %d topic-recalls %d'
      % (m_i, s_i, t_i, c_i, len(media_ids), len(rq_ids)))
print('root keys', len(out), '| topic keys', len(out['modules'][0]['segments'][0]['topics'][0]))
print('covered_by_topics rewritten:', cov_changed, '| stale:', len(cov_stale))
print('dropped working keys:', dict(dropped) or 'none')
print('topic_type ->', sorted({t['topic_type'] for m in out['modules'] for s in m['segments'] for t in s['topics']}))
print('ALL ASSERTIONS PASS')
