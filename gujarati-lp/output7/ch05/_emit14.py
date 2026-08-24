#!/usr/bin/env python3
"""Agent 14 — arrange in reading order, renumber M/S/T/C consecutively, translate every
reference, apply the phase-2 whitelist, map topic_type, emit learning_plan_logical.json.
Then copy 10_exercise_solutions.json -> exercise_solutions.json and render the .md."""
import json, os, re, collections

D = os.path.dirname(os.path.abspath(__file__))
p = lambda n: os.path.join(D, n)
J = lambda n: json.load(open(p(n), encoding='utf-8'))

src = J('13_merged.json')
ex = J('10_exercise_solutions.json')

# ---------------------------------------------------------------- 1. arrange
# Reading order = the merged structure's own traversal, confirmed identical to the
# printed order recorded in 05b_textbook_order.json (checked below).
modules = src['modules']

# ---------------------------------------------------- 2. renumber consecutively
idmap = {}          # old id -> new id, every level
m = s = t = c = 0
plan_modules = []
for M in modules:
    m += 1
    new_M = 'M%d' % m
    idmap[M['module_id']] = new_M
    for S in M['segments']:
        s += 1
        new_S = '%s.S%d' % (new_M, s)
        idmap[S['segment_id']] = new_S
        for T in S['topics']:
            t += 1
            new_T = '%s.T%d' % (new_S, t)
            idmap[T['topic_id']] = new_T
            for C in T['concepts']:
                c += 1
                idmap[C['concept_id']] = '%s.C%d' % (new_T, c)

# every recall / media id is a suffix on a node id -> derive, do not guess
def remap(old):
    """Translate any dotted id whose longest node prefix is in idmap."""
    if not isinstance(old, str):
        return old
    parts = old.split('.')
    for k in range(len(parts), 0, -1):
        head = '.'.join(parts[:k])
        if head in idmap:
            return '.'.join([idmap[head]] + parts[k:])
    return old

def remap_list(xs):
    return [remap(x) for x in (xs or [])]

# ------------------------------------------------------ 3. topic_type mapping
TT = {'POEM': 'instructional', 'STORY_TELLING': 'instructional',
      'CONCEPT': 'instructional', 'REVIEW': 'summary', 'EXERCISE': 'assessment',
      'instructional': 'instructional', 'summary': 'summary', 'assessment': 'assessment'}

# --------------------------------------------------------- 4. the whitelists
TOPIC_KEYS = [
    'topic_id', 'topic_name', 'topic_type', 'topic_category', 'difficulty',
    'original_chunk', 'modified_chunk', 'word_count',
    'explanation', 'real_life_example',
    'brief_summary', 'summary', 'detailed_summary',
    'key_terms', 'concept_bullets', 'important_points',
    'figures_of_speech', 'rhyme_scheme',                    # કાવ્ય extras
    'shabdarth', 'samanarthi', 'vilom', 'vyakaran',          # ભાષા-બોધ extras
    'objective_ids', 'learning_objectives', 'concepts', 'recall_questions',
    'media', '2d_tool', 'publication_text', 'publication_chunk',
    'depends_on', 'source_topic_ids', 'estimated_exchanges',
    'primary_content_type', 'secondary_content_type', 'tertiary_content_type',
    'available_content_types',
]
MEDIA_KEYS = ['id', 'type', 'subtype', 'title', 'description', 'image_url',
              'aspect_ratio', 'concept_id', 'home_concept_id', 'objective_id',
              'image_category', 'teaching_notes', 'negative_prompt', 'generation_prompt']
CONCEPT_KEYS = ['concept_id', 'concept_name', 'objective_id', 'key_terms', 'content']
RQ_KEYS = ['id', 'legacy_id', 'prompt', 'answer', 'difficulty', 'bloom_level']
SEG_RQ_KEYS = ['id', 'prompt', 'answer', 'difficulty', 'bloom_level']
OBJ_KEYS = ['objective_id', 'legacy_id', 'strand', 'strand_name', 'objective_text',
            'bloom_level', 'home_topic_id', 'anchor', 'status', 'theme_category']
LO_KEYS = ['objective_id', 'legacy_id', 'strand', 'strand_name', 'objective_text',
           'bloom_level', 'home_topic_id', 'anchor', 'theme_category', 'image_examples']
MOD_KEYS = ['module_id', 'module_name', 'difficult_words', 'overall_rhyme_scheme', 'segments']
SEG_KEYS = ['segment_id', 'segment_name', 'topics']

pick = lambda o, ks: {k: o[k] for k in ks if k in o}

# --------------------------------------------------------------- build tree
out_modules = []
for M in modules:
    mo = collections.OrderedDict()
    mo['module_id'] = idmap[M['module_id']]
    mo['module_name'] = M['module_name']
    if 'difficult_words' in M:
        mo['difficult_words'] = M['difficult_words']
    if 'overall_rhyme_scheme' in M:
        mo['overall_rhyme_scheme'] = M['overall_rhyme_scheme']
    segs = []
    for S in M['segments']:
        so = collections.OrderedDict()
        so['segment_id'] = idmap[S['segment_id']]
        so['segment_name'] = S['segment_name']
        for k in ('brief_summary', 'summary', 'detailed_summary', 'important_points'):
            if k in S:
                so[k] = S[k]
        if S.get('recall_questions'):
            # segment recalls are {segment_id}.RQ{n} — never .SR{n}
            rqs = []
            for i, r in enumerate(S['recall_questions'], 1):
                ro = pick(r, SEG_RQ_KEYS)
                ro['id'] = '%s.RQ%d' % (so['segment_id'], i)
                rqs.append({k: ro[k] for k in SEG_RQ_KEYS if k in ro})
            so['recall_questions'] = rqs
        tops = []
        for T in S['topics']:
            to = collections.OrderedDict()
            for k in TOPIC_KEYS:
                if k not in T:
                    continue
                v = T[k]
                if k == 'topic_id':
                    v = idmap[T['topic_id']]
                elif k == 'topic_type':
                    v = TT[v]
                elif k in ('depends_on', 'source_topic_ids'):
                    v = remap_list(v)
                elif k == 'learning_objectives':
                    v = [dict(pick(lo, LO_KEYS),
                              home_topic_id=remap(lo.get('home_topic_id')),
                              anchor=remap_list(lo.get('anchor')),
                              image_examples=lo.get('image_examples', []))
                         for lo in v]
                    v = [{kk: o[kk] for kk in LO_KEYS if kk in o} for o in v]
                elif k == 'concepts':
                    nv = []
                    for C in v:
                        co = pick(C, CONCEPT_KEYS)
                        co['concept_id'] = idmap[C['concept_id']]
                        nv.append({kk: co[kk] for kk in CONCEPT_KEYS if kk in co})
                    v = nv
                elif k == 'recall_questions':
                    nv = []
                    for i, r in enumerate(v, 1):
                        ro = pick(r, RQ_KEYS)
                        ro['id'] = '%s.RQ%d' % (idmap[T['topic_id']], i)
                        ro['legacy_id'] = '%s.TR%d' % (idmap[T['topic_id']], i)
                        nv.append({kk: ro[kk] for kk in RQ_KEYS if kk in ro})
                    v = nv
                elif k == 'media':
                    nv = []
                    for md in v:
                        mo2 = pick(md, MEDIA_KEYS)
                        mo2['id'] = remap(md['id'])
                        mo2['concept_id'] = remap(md.get('concept_id'))
                        mo2['home_concept_id'] = remap(md.get('home_concept_id'))
                        nv.append({kk: mo2[kk] for kk in MEDIA_KEYS if kk in mo2})
                    v = nv
                to[k] = v
            tops.append(to)
        so['topics'] = tops
        segs.append(so)
    mo['segments'] = segs
    out_modules.append(mo)

# ------------------------------------------------- objectives registry (flat)
objectives = []
for o in src['objectives']:
    oo = pick(o, OBJ_KEYS)
    oo['home_topic_id'] = remap(o.get('home_topic_id'))
    oo['anchor'] = remap_list(o.get('anchor'))
    objectives.append({k: oo[k] for k in OBJ_KEYS if k in oo})

# ------------------------------------------------------------- 5. root fields
version = src.get('version') or 1
grade = src['grade']
unit_number = src['unit_number']
chapter_id = 'gseb_eng_gujarati%d_ch%d' % (grade, unit_number)
plan_id = '%s_v%d' % (chapter_id, version)

plan = collections.OrderedDict()
plan['phase'] = 2
plan['board'] = src['board']
plan['subject'] = src['subject']
plan['grade'] = grade
plan['level'] = src['level']
plan['version'] = version
plan['ordering'] = 'logical'
plan['author'] = src.get('author', '')
plan['chapter_id'] = chapter_id
plan['plan_id'] = plan_id
plan['chapter_name'] = src['chapter_name']
plan['unit_title'] = src['unit_title']
plan['unit_number'] = unit_number
plan['topic_title'] = src['topic_title']
plan['topic_number'] = src['topic_number']
plan['genre'] = 'urmikavya_geet'          # roster slug (active genre profile)
plan['teaching_lens'] = src['teaching_lens']
plan['guiding_question'] = src['guiding_question']
plan['textbook'] = src['textbook']
plan['textbook_url'] = src['textbook_url']
plan['textbook_pages'] = src['textbook_pages']
plan['_activate'] = False
plan['medium_id'] = None                  # server-injected
plan['subject_ref_id'] = None             # server-injected
plan['publication_id'] = src.get('publication_id')   # non-null; PROVISIONAL (VERIFY-2)
plan['chapter_master_id'] = None          # fetched from the education DB (VERIFY-2)
plan['estimated_time'] = src['estimated_time']
plan['english_plan_id'] = None
plan['english_chapter_id'] = None
plan['objectives'] = objectives
plan['strand_to_objective_map'] = src['strand_to_objective_map']
plan['modules'] = out_modules

ROOT_32 = ['board', 'genre', 'grade', 'level', 'phase', 'author', 'modules', 'plan_id',
           'subject', 'version', 'ordering', 'textbook', '_activate', 'medium_id',
           'chapter_id', 'objectives', 'unit_title', 'topic_title', 'unit_number',
           'chapter_name', 'textbook_url', 'topic_number', 'teaching_lens',
           'estimated_time', 'publication_id', 'subject_ref_id', 'textbook_pages',
           'english_plan_id', 'guiding_question', 'chapter_master_id',
           'english_chapter_id', 'strand_to_objective_map']
assert set(plan) == set(ROOT_32), (set(ROOT_32) ^ set(plan))

# ------------------------------------- covered_by_topics rewrite in 10_exercise
n_cov = 0
for e in ex['exercises']:
    if e.get('covered_by_topics'):
        new = remap_list(e['covered_by_topics'])
        if new != e['covered_by_topics']:
            n_cov += 1
        e['covered_by_topics'] = new
ex['plan_id'] = plan_id
ex['chapter_id'] = chapter_id

# =========================================================== ASSERTIONS
NODE = set()
CONC = set()
for M in plan['modules']:
    NODE.add(M['module_id'])
    for S in M['segments']:
        NODE.add(S['segment_id'])
        for T in S['topics']:
            NODE.add(T['topic_id'])
            for C in T['concepts']:
                NODE.add(C['concept_id']); CONC.add(C['concept_id'])
errs = []

# id grammar / traversal position
mi = si = ti = ci = 0
for M in plan['modules']:
    mi += 1
    if M['module_id'] != 'M%d' % mi: errs.append('module_id %s' % M['module_id'])
    for S in M['segments']:
        si += 1
        if S['segment_id'] != 'M%d.S%d' % (mi, si): errs.append('segment_id %s' % S['segment_id'])
        for T in S['topics']:
            ti += 1
            exp_t = 'M%d.S%d.T%d' % (mi, si, ti)
            if T['topic_id'] != exp_t: errs.append('topic_id %s != %s' % (T['topic_id'], exp_t))
            for C in T['concepts']:
                ci += 1
                exp_c = '%s.C%d' % (exp_t, ci)
                if C['concept_id'] != exp_c: errs.append('concept_id %s != %s' % (C['concept_id'], exp_c))

OBJ_IDS = {o['objective_id'] for o in plan['objectives']}
if len(OBJ_IDS) != len(plan['objectives']): errs.append('duplicate objective_id')
for o in plan['objectives']:
    if o['home_topic_id'] not in NODE: errs.append('objective %s home_topic_id stale' % o['objective_id'])
    for a in o['anchor']:
        if a not in NODE: errs.append('objective %s anchor %s stale' % (o['objective_id'], a))
for lg, oid in plan['strand_to_objective_map'].items():
    if oid not in OBJ_IDS: errs.append('strand map %s -> %s missing' % (lg, oid))
lgs = {o['legacy_id'] for o in plan['objectives']}
if lgs != set(plan['strand_to_objective_map']): errs.append('strand map does not cover every legacy_id')

MEDIA_RE = re.compile(r'^M\d+\.S\d+\.T\d+\.C\d+\.(IMG|VID|2D|3D|SIM)\d+$')
GU = re.compile(r'[઀-૿]')
LATIN = re.compile(r'[A-Za-z]')
DEVA = re.compile(r'[ऀ-ॿ]')
n2d = 0
for M in plan['modules']:
    for S in M['segments']:
        for i, r in enumerate(S.get('recall_questions', []), 1):
            if r['id'] != '%s.RQ%d' % (S['segment_id'], i): errs.append('seg rq %s' % r['id'])
        for T in S['topics']:
            tid = T['topic_id']
            if T['topic_type'] not in ('instructional', 'summary', 'assessment'):
                errs.append('topic_type %s' % T['topic_type'])
            if set(T) - set(TOPIC_KEYS): errs.append('%s extra keys %s' % (tid, set(T) - set(TOPIC_KEYS)))
            oc = T.get('original_chunk') or ''
            if not GU.search(oc): errs.append('%s original_chunk not Gujarati' % tid)
            if LATIN.search(oc) or DEVA.search(oc): errs.append('%s original_chunk foreign script' % tid)
            if not T.get('concepts'): errs.append('%s no concepts' % tid)
            for C in T['concepts']:
                if C['objective_id'] not in OBJ_IDS: errs.append('%s concept objective_id stale' % tid)
                if not C.get('content'): errs.append('%s concept empty content' % tid)
            for oid in T['objective_ids']:
                if oid not in OBJ_IDS: errs.append('%s objective_ids stale' % tid)
            for lo in T['learning_objectives']:
                root = [o for o in plan['objectives'] if o['objective_id'] == lo['objective_id']]
                if not root: errs.append('%s inline objective missing from registry' % tid); continue
                root = root[0]
                if lo['objective_text'] != root['objective_text']:
                    errs.append('%s inline objective_text drift' % tid)
                if lo['home_topic_id'] != root['home_topic_id'] or lo['anchor'] != root['anchor']:
                    errs.append('%s inline anchor drift' % tid)
                for a in lo['anchor']:
                    if a not in NODE: errs.append('%s inline anchor %s stale' % (tid, a))
            for i, r in enumerate(T['recall_questions'], 1):
                if r['id'] != '%s.RQ%d' % (tid, i): errs.append('rq id %s' % r['id'])
                if r['legacy_id'] != '%s.TR%d' % (tid, i): errs.append('rq legacy %s' % r['legacy_id'])
            for md in T['media']:
                if not MEDIA_RE.match(md['id']): errs.append('media id %s' % md['id'])
                if not md['id'].startswith(md['concept_id'] + '.'): errs.append('media %s not under its concept' % md['id'])
                if md['concept_id'] not in CONC: errs.append('media concept_id %s stale' % md['concept_id'])
                if md['home_concept_id'] not in CONC: errs.append('media home_concept_id stale')
                if not md.get('image_url') and not (md.get('generation_prompt') or '').strip():
                    errs.append('media %s has neither url nor prompt' % md['id'])
            if T.get('2d_tool'): n2d += 1
            for d_ in T['depends_on'] + T['source_topic_ids']:
                if d_ not in NODE: errs.append('%s depends_on/source %s stale' % (tid, d_))
            b, sm, dl = T['brief_summary'], T['summary'], T['detailed_summary']
            if not (len(b) < len(sm) < len(dl)): errs.append('%s summaries not increasing' % tid)
            for fos in T.get('figures_of_speech') or []:
                if fos.get('lines') and fos['lines'] not in oc:
                    errs.append('%s figure_of_speech lines not in chunk' % tid)
if n2d > 1: errs.append('more than one 2d_tool')

# no numbers in display text
DIGIT = re.compile(r'[0-9૦-૯]')
def scan(node, path):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in ('topic_name', 'module_name', 'segment_name', 'explanation',
                     'real_life_example', 'brief_summary', 'summary', 'detailed_summary',
                     'concept_bullets', 'important_points', 'prompt', 'answer',
                     'concept_name', 'objective_text'):
                for txt in ([v] if isinstance(v, str) else (v if isinstance(v, list) else [])):
                    if isinstance(txt, str) and DIGIT.search(txt):
                        errs.append('digit in display text %s.%s: %s' % (path, k, txt[:60]))
            if isinstance(v, (dict, list)):
                scan(v, path + '.' + k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            scan(v, '%s[%d]' % (path, i))
scan(plan['modules'], 'modules')
scan(plan['objectives'], 'objectives')

# every exercise covered_by_topics id resolves
for e in ex['exercises']:
    for cid in e.get('covered_by_topics') or []:
        if cid not in NODE: errs.append('exercise %s covered_by_topics %s stale' % (e['exercise_id'], cid))

# printed-order cross-check
order = J('05b_textbook_order.json')['textbook_order']
logical = [T['topic_id'] for M in plan['modules'] for S in M['segments'] for T in S['topics']]
mapped_printed = [remap(x) for x in order]
same_order = (mapped_printed == logical)

# no stale id anywhere in the emitted document
ANY = re.compile(r'M\d+\.S\d+(?:\.T\d+)?(?:\.C\d+)?(?:\.(?:RQ|TR|IMG|VID|2D|3D|SIM)\d+)?')
blob = json.dumps(plan, ensure_ascii=False)
for hit in set(ANY.findall(blob)):
    base = re.sub(r'\.(RQ|TR|IMG|VID|2D|3D|SIM)\d+$', '', hit)
    if base not in NODE:
        errs.append('stale id in document: %s' % hit)

if errs:
    print('ASSERTION FAILURES (%d):' % len(errs))
    for e_ in errs: print('  -', e_)
    raise SystemExit(1)

json.dump(plan, open(p('learning_plan_logical.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
json.dump(ex, open(p('10_exercise_solutions.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
json.dump(ex, open(p('exercise_solutions.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)

print('OK  modules=%d segments=%d topics=%d concepts=%d objectives=%d' %
      (mi, si, ti, ci, len(plan['objectives'])))
print('    id map is identity: %s' % all(k == v for k, v in idmap.items()))
print('    covered_by_topics entries rewritten: %d' % n_cov)
print('    printed order == logical order: %s' % same_order)
