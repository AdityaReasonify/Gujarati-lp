#!/usr/bin/env python3
"""Agent 14 — arrange in reading order, renumber consecutively, translate every
reference, apply the phase-2 whitelist, emit learning_plan_logical.json.

Also rewrites covered_by_topics in 10_exercise_solutions.json under the same map.
"""
import json, re, sys, os, collections

D = os.path.dirname(os.path.abspath(__file__))
p = lambda n: os.path.join(D, n)

merged = json.load(open(p('13_merged.json'), encoding='utf-8'))

# ---------------------------------------------------------------- 1. arrange
# Reading order = the merged structure's own traversal order (05b_textbook_order.json
# records the printed order and matches it exactly; Agent 15 owns the printed file).
order = json.load(open(p('05b_textbook_order.json'), encoding='utf-8'))['textbook_order']

# ------------------------------------------------- 2. renumber consecutively
idmap = {}          # old id -> new id, every level
mi = si = ti = ci = 0
plan_modules = []
for mod in merged['modules']:
    mi += 1
    new_m = 'M%d' % mi
    idmap[mod['module_id']] = new_m
    segs = []
    for seg in mod['segments']:
        si += 1
        new_s = '%s.S%d' % (new_m, si)
        idmap[seg['segment_id']] = new_s
        tops = []
        for top in seg['topics']:
            ti += 1
            new_t = '%s.T%d' % (new_s, ti)
            idmap[top['topic_id']] = new_t
            for con in top.get('concepts') or []:
                ci += 1
                idmap[con['concept_id']] = '%s.C%d' % (new_t, ci)
            tops.append(top)
        segs.append((seg, tops))
    plan_modules.append((mod, segs))

# ----------------------------------------------------- 3. translate refs
NODE_RE = re.compile(r'M\d+\.S\d+\.T\d+\.C\d+|M\d+\.S\d+\.T\d+|M\d+\.S\d+|M\d+')

def tr(old):
    """Translate a bare node id. Unknown ids are a hard fail."""
    if old is None:
        return None
    if old not in idmap:
        sys.exit('FATAL: stale reference %r resolves to no node' % old)
    return idmap[old]

def tr_list(xs):
    return [tr(x) for x in (xs or [])]

MEDIA_RE = re.compile(r'^(?P<cid>M\d+\.S\d+\.T\d+\.C\d+)\.(?P<sfx>IMG|VID|2D|3D|SIM)(?P<n>\d+)$')

# ------------------------------------------------------- 4. the whitelist
TOPIC_KEYS = [
    'topic_id', 'topic_name', 'topic_type', 'topic_category', 'difficulty',
    'word_count', 'estimated_exchanges', 'objective_ids', 'learning_objectives',
    'key_terms', 'depends_on', 'source_topic_ids',
    'original_chunk', 'modified_chunk', 'publication_chunk', 'publication_text',
    'explanation', 'real_life_example',
    'brief_summary', 'summary', 'detailed_summary',
    'concept_bullets', 'important_points',
    'concepts', 'recall_questions', 'media', '2d_tool',
    'primary_content_type', 'secondary_content_type', 'tertiary_content_type',
    'available_content_types',
    # કાવ્ય extras
    'figures_of_speech', 'rhyme_scheme',
    # ભાષા-બોધ extras (romanized key names, as the server stores them)
    'shabdarth', 'samanarthi', 'vilom', 'vyakaran',
]
MODULE_KEYS = ['module_id', 'module_name', 'difficult_words', 'overall_rhyme_scheme', 'segments']
SEGMENT_KEYS = ['segment_id', 'segment_name', 'recall_questions', 'topics']
CONCEPT_KEYS = ['concept_id', 'concept_name', 'objective_id', 'key_terms', 'content']
OBJECTIVE_KEYS = ['objective_id', 'legacy_id', 'strand', 'strand_name', 'objective_text',
                  'bloom_level', 'home_topic_id', 'anchor', 'status', 'theme_category']
MEDIA_KEYS = ['id', 'type', 'subtype', 'title', 'description', 'image_url', 'aspect_ratio',
              'concept_id', 'home_concept_id', 'objective_id', 'image_category',
              'teaching_notes', 'negative_prompt', 'generation_prompt']

def pick(src, keys):
    return {k: src[k] for k in keys if k in src}

# ------------------------------------------------ 5. topic_type at emit
TYPE_MAP = {
    'POEM': 'instructional', 'STORY_TELLING': 'instructional', 'CONCEPT': 'instructional',
    'REVIEW': 'summary', 'EXERCISE': 'assessment',
    # already-mapped values pass through
    'instructional': 'instructional', 'summary': 'summary', 'assessment': 'assessment',
}

# ---------------------------------------------------------------- build
out_modules = []
for mod, segs in plan_modules:
    m = pick(mod, MODULE_KEYS)
    m['module_id'] = tr(mod['module_id'])
    out_segs = []
    for seg, tops in segs:
        s = pick(seg, SEGMENT_KEYS)
        new_s = tr(seg['segment_id'])
        s['segment_id'] = new_s
        # segment recalls: {segment_id}.RQ{n} — never .SR{n}
        if s.get('recall_questions'):
            for n, rq in enumerate(s['recall_questions'], 1):
                rq['id'] = '%s.RQ%d' % (new_s, n)
                if 'legacy_id' in rq:
                    rq['legacy_id'] = '%s.TR%d' % (new_s, n)
        out_tops = []
        for top in tops:
            new_t = tr(top['topic_id'])
            t = pick(top, TOPIC_KEYS)
            t['topic_id'] = new_t
            t['topic_type'] = TYPE_MAP[top['topic_type']]
            t['objective_ids'] = list(top.get('objective_ids') or [])
            t['depends_on'] = tr_list(top.get('depends_on'))
            t['source_topic_ids'] = tr_list(top.get('source_topic_ids'))
            # inline objective mirrors
            los = []
            for lo in top.get('learning_objectives') or []:
                o = pick(lo, OBJECTIVE_KEYS)
                o['home_topic_id'] = tr(lo.get('home_topic_id'))
                o['anchor'] = tr_list(lo.get('anchor'))
                o['image_examples'] = lo.get('image_examples', [])
                los.append(o)
            t['learning_objectives'] = los
            # concepts
            cons = []
            for con in top.get('concepts') or []:
                c = pick(con, CONCEPT_KEYS)
                c['concept_id'] = tr(con['concept_id'])
                cons.append(c)
            t['concepts'] = cons
            # topic recalls
            rqs = []
            for n, rq in enumerate(top.get('recall_questions') or [], 1):
                r = dict(rq)
                r['id'] = '%s.RQ%d' % (new_t, n)
                r['legacy_id'] = '%s.TR%d' % (new_t, n)
                rqs.append(r)
            t['recall_questions'] = rqs
            # media — concept-scoped ids
            meds = []
            for md in top.get('media') or []:
                mm = MEDIA_RE.match(md['id'])
                if not mm:
                    sys.exit('FATAL: bad media id %r' % md['id'])
                x = pick(md, MEDIA_KEYS)
                x['concept_id'] = tr(md['concept_id'])
                x['home_concept_id'] = tr(md.get('home_concept_id'))
                x['id'] = '%s.%s%s' % (tr(mm.group('cid')), mm.group('sfx'), mm.group('n'))
                meds.append(x)
            t['media'] = meds
            out_tops.append({k: t[k] for k in TOPIC_KEYS if k in t})
        s['topics'] = out_tops
        out_segs.append({k: s[k] for k in SEGMENT_KEYS if k in s})
    m['segments'] = out_segs
    out_modules.append({k: m[k] for k in MODULE_KEYS if k in m})

# root objectives registry — O{n} is NOT renumbered, but its pointers are
objectives = []
for o in merged['objectives']:
    x = pick(o, OBJECTIVE_KEYS)
    x['home_topic_id'] = tr(o['home_topic_id'])
    x['anchor'] = tr_list(o.get('anchor'))
    objectives.append(x)

# ---------------------------------------------------------- 6. root fields
ROOT_ORDER = ['board', 'genre', 'grade', 'level', 'phase', 'author', 'modules', 'plan_id',
              'subject', 'version', 'ordering', 'textbook', '_activate', 'medium_id',
              'chapter_id', 'objectives', 'unit_title', 'topic_title', 'unit_number',
              'chapter_name', 'textbook_url', 'topic_number', 'teaching_lens',
              'estimated_time', 'publication_id', 'subject_ref_id', 'textbook_pages',
              'english_plan_id', 'guiding_question', 'chapter_master_id',
              'english_chapter_id', 'strand_to_objective_map']

version = merged.get('version', 1)
chapter_id = merged['chapter_id']          # gseb_eng_gujarati6_ch10 (PROVISIONAL, VERIFY-1)

cmm = json.load(open(os.path.join(D, '..', '..', 'upload_reference',
                                  'chapter_master_map.json'), encoding='utf-8'))
row = cmm.get(chapter_id) or {}

plan = {
    'phase': 2,
    'board': merged['board'],
    'subject': merged['subject'],
    'grade': merged['grade'],
    'level': merged['level'],
    'version': version,
    'ordering': 'logical',
    'chapter_id': chapter_id,
    'plan_id': '%s_v%s' % (chapter_id, version),
    'chapter_name': merged['chapter_name'],
    'unit_title': merged['unit_title'],
    'unit_number': merged['unit_number'],
    'topic_title': merged['topic_title'],
    'topic_number': merged['topic_number'],
    'genre': merged['genre'],
    'teaching_lens': merged['teaching_lens'],
    'guiding_question': merged['guiding_question'],
    'textbook': merged['textbook'],
    'textbook_url': merged['textbook_url'],
    'textbook_pages': merged['textbook_pages'],
    'author': merged.get('author', ''),
    '_activate': False,
    'medium_id': None,                     # server-injected
    'subject_ref_id': None,                # server-injected
    'english_plan_id': None,               # no English twin
    'english_chapter_id': None,
    'estimated_time': merged.get('estimated_time', 1.5),
    # chapter_master_id / publication_id come from chapter_master_map.json — never invented.
    # The GSEB rows are still null there (VERIFY-2); merged carries the pack's provisional
    # non-null publication_id (the server rejects null) and it is used only as a fallback.
    'chapter_master_id': row.get('chapter_master_id', merged.get('chapter_master_id')),
    'publication_id': row.get('publication_id') or merged.get('publication_id'),
    'objectives': objectives,
    'strand_to_objective_map': dict(merged['strand_to_objective_map']),
    'modules': out_modules,
}
plan = {k: plan[k] for k in ROOT_ORDER}

# ------------------------------------------------------------ 7. assertions
errs = []
mods, segs_, tops_, cons_ = set(), set(), set(), set()
mi = si = ti = ci = 0
for m in plan['modules']:
    mi += 1
    if m['module_id'] != 'M%d' % mi: errs.append('module_id %s' % m['module_id'])
    mods.add(m['module_id'])
    for s in m['segments']:
        si += 1
        if s['segment_id'] != 'M%d.S%d' % (mi, si): errs.append('segment_id %s' % s['segment_id'])
        segs_.add(s['segment_id'])
        for t in s['topics']:
            ti += 1
            exp = 'M%d.S%d.T%d' % (mi, si, ti)
            if t['topic_id'] != exp: errs.append('topic_id %s != %s' % (t['topic_id'], exp))
            tops_.add(t['topic_id'])
            for c in t['concepts']:
                ci += 1
                expc = '%s.C%d' % (exp, ci)
                if c['concept_id'] != expc: errs.append('concept_id %s != %s' % (c['concept_id'], expc))
                cons_.add(c['concept_id'])

objids = {o['objective_id'] for o in plan['objectives']}
objtext = {o['objective_id']: o['objective_text'] for o in plan['objectives']}
if len(objids) != len(plan['objectives']): errs.append('duplicate objective_id')
for o in plan['objectives']:
    if o['home_topic_id'] not in tops_: errs.append('stale home_topic_id %s' % o['home_topic_id'])
    for a in o['anchor']:
        if a not in cons_: errs.append('stale anchor %s' % a)
for lid, oid in plan['strand_to_objective_map'].items():
    if oid not in objids: errs.append('strand map -> %s' % oid)
for o in plan['objectives']:
    if o['legacy_id'] not in plan['strand_to_objective_map']:
        errs.append('legacy_id %s not in strand map' % o['legacy_id'])

GUJ = re.compile(r'[઀-૿]')
DEVA = re.compile(r'[ऀ-ॿ]')
for m in plan['modules']:
    for s in m['segments']:
        for rq in s.get('recall_questions') or []:
            if not re.match(r'^%s\.RQ\d+$' % re.escape(s['segment_id']), rq['id']):
                errs.append('segment recall id %s' % rq['id'])
        for t in s['topics']:
            tid = t['topic_id']
            if t['topic_type'] not in ('instructional', 'summary', 'assessment'):
                errs.append('topic_type %s' % t['topic_type'])
            if not (t.get('original_chunk') or '').strip(): errs.append('empty original_chunk %s' % tid)
            if not GUJ.search(t.get('original_chunk', '')): errs.append('non-Gujarati chunk %s' % tid)
            if DEVA.search(t.get('original_chunk', '')): errs.append('Devanagari in chunk %s' % tid)
            if not t['concepts']: errs.append('no concepts %s' % tid)
            for c in t['concepts']:
                if c['objective_id'] not in objids: errs.append('concept objective %s' % c['objective_id'])
                if not c.get('content'): errs.append('empty concept content %s' % c['concept_id'])
            for oid in t['objective_ids']:
                if oid not in objids: errs.append('stale objective_ids %s @ %s' % (oid, tid))
            for lo in t['learning_objectives']:
                if lo['objective_id'] not in objids:
                    errs.append('stale inline objective %s' % lo['objective_id'])
                elif lo['objective_text'] != objtext[lo['objective_id']]:
                    errs.append('inline mirror drift %s @ %s' % (lo['objective_id'], tid))
                if lo['home_topic_id'] not in tops_: errs.append('inline home %s' % lo['home_topic_id'])
                for a in lo['anchor']:
                    if a not in cons_: errs.append('inline anchor %s' % a)
            for n, rq in enumerate(t['recall_questions'], 1):
                if rq['id'] != '%s.RQ%d' % (tid, n): errs.append('recall id %s' % rq['id'])
                if rq['legacy_id'] != '%s.TR%d' % (tid, n): errs.append('recall legacy %s' % rq['legacy_id'])
            for md in t['media']:
                mm = MEDIA_RE.match(md['id'])
                if not mm: errs.append('media id %s' % md['id']); continue
                if mm.group('cid') != md['concept_id']: errs.append('media concept scope %s' % md['id'])
                if md['concept_id'] not in cons_: errs.append('stale media concept_id %s' % md['concept_id'])
                if md.get('home_concept_id') not in cons_: errs.append('stale home_concept_id %s' % md['id'])
                if not md.get('image_url') and not md.get('generation_prompt'):
                    errs.append('media with neither url nor prompt %s' % md['id'])
            for x in t['depends_on']:
                if x not in tops_: errs.append('stale depends_on %s @ %s' % (x, tid))
            for x in t['source_topic_ids']:
                if x not in tops_: errs.append('stale source_topic_ids %s @ %s' % (x, tid))
            b, sm, dt = t.get('brief_summary', ''), t.get('summary', ''), t.get('detailed_summary', '')
            if not (len(b) < len(sm) < len(dt)):
                errs.append('summaries not increasing %s (%d/%d/%d)' % (tid, len(b), len(sm), len(dt)))
            for fs in t.get('figures_of_speech') or []:
                for ln in (fs.get('lines') or []):
                    if ln.strip() and ln.strip() not in t['original_chunk']:
                        errs.append('figure line not in chunk %s: %s' % (tid, ln[:30]))
            extra = [k for k in t if k not in TOPIC_KEYS]
            if extra: errs.append('non-whitelist topic key %s @ %s' % (extra, tid))

if len(plan) != 32: errs.append('root key count %d' % len(plan))
if plan['phase'] != 2: errs.append('phase')
if plan['ordering'] != 'logical': errs.append('ordering')
if plan['plan_id'] != '%s_v%s' % (plan['chapter_id'], plan['version']): errs.append('plan_id')
if plan['publication_id'] is None: errs.append('publication_id is null — server rejects it')
if '_standard_' in plan['plan_id']: errs.append('_standard_ segment in plan_id')

# traversal order must equal the recorded reading order
traversal = [t['topic_id'] for m in plan['modules'] for s in m['segments'] for t in s['topics']]
if traversal != [idmap[x] for x in order]:
    errs.append('traversal != 05b reading order')

# no numbers in display text
NUMWORD = re.compile(r'(કડી|પ્રશ્ન|સ્વાધ્યાય|ટેક|દુહો|પંક્તિ|મુદ્દો)\s*[\d૦-૯]')
def scan(txt, where):
    if isinstance(txt, str) and NUMWORD.search(txt): errs.append('number in display text @ %s' % where)
for m in plan['modules']:
    scan(m['module_name'], m['module_id'])
    for s in m['segments']:
        scan(s['segment_name'], s['segment_id'])
        for t in s['topics']:
            for k in ('topic_name', 'explanation', 'real_life_example', 'brief_summary',
                      'summary', 'detailed_summary'):
                scan(t.get(k), '%s.%s' % (t['topic_id'], k))
            for bl in (t.get('concept_bullets') or []) + (t.get('important_points') or []):
                scan(bl, t['topic_id'])
            for rq in t['recall_questions']:
                scan(rq.get('prompt'), rq['id'])
                scan(rq.get('answer'), rq['id'])
        for rq in s.get('recall_questions') or []:
            scan(rq.get('prompt'), rq['id'])
            scan(rq.get('answer'), rq['id'])

if errs:
    print('ASSERTION FAILURES (%d):' % len(errs))
    for e in errs[:80]:
        print('  -', e)
    sys.exit(1)

json.dump(plan, open(p('learning_plan_logical.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)

# ------------------------- covered_by_topics rewrite in 10_exercise_solutions.json
raw_before = open(p('10_exercise_solutions.json'), encoding='utf-8').read()
ex = json.loads(raw_before)
before = json.dumps(ex, ensure_ascii=False, sort_keys=True)
changed = 0
for e in ex['exercises']:
    old = e.get('covered_by_topics') or []
    new = [tr(x) for x in old]
    if new != old: changed += 1
    e['covered_by_topics'] = new
    for x in new:
        if x not in tops_: sys.exit('FATAL: covered_by_topics stale %s' % x)
ex['plan_id'] = plan['plan_id']
ex['chapter_id'] = plan['chapter_id']
after = json.dumps(ex, ensure_ascii=False, sort_keys=True)
if after != before:
    json.dump(ex, open(p('10_exercise_solutions.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)
    print('    10_exercise_solutions.json REWRITTEN')
else:
    print('    10_exercise_solutions.json unchanged (id map is the identity) — left untouched')

print('OK  modules=%d segments=%d topics=%d concepts=%d objectives=%d media=%d'
      % (mi, si, ti, ci, len(objectives),
         sum(len(t['media']) for m in plan['modules'] for s in m['segments'] for t in s['topics'])))
print('    covered_by_topics rewritten in %d exercise entries (id map is identity)' % changed)
print('    root keys=%d  plan_id=%s' % (len(plan), plan['plan_id']))
