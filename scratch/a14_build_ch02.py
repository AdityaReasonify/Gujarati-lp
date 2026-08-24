# -*- coding: utf-8 -*-
import json, re, collections, io, os

D = '/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch02'
merged = json.load(open(os.path.join(D, '13_merged.json')), object_pairs_hook=collections.OrderedDict)

# ---------------------------------------------------------------- 1. arrange
# Reading order = the merged structure's own order (05b_textbook_order.json confirms the
# printed sequence is identical). Nothing moves.
order_new = []
for mod in merged['modules']:
    for seg in mod['segments']:
        for top in seg['topics']:
            order_new.append(top['topic_id'])

# ---------------------------------------------------------------- 2. renumber
idmap = {}   # old id -> new id, for every node
m = s = t = c = 0
for mod in merged['modules']:
    m += 1
    new_m = 'M%d' % m
    idmap[mod['module_id']] = new_m
    for seg in mod['segments']:
        s += 1
        new_s = '%s.S%d' % (new_m, s)
        idmap[seg['segment_id']] = new_s
        for top in seg['topics']:
            t += 1
            new_t = '%s.T%d' % (new_s, t)
            idmap[top['topic_id']] = new_t
            for con in top['concepts']:
                c += 1
                idmap[con['concept_id']] = '%s.C%d' % (new_t, c)

def remap_node(i):
    if i is None:
        return None
    if i in idmap:
        return idmap[i]
    raise SystemExit('UNRESOLVED node id: %r' % i)

def remap_suffixed(i, pat):
    # '<node>.<SUFFIX><n>'  ->  '<newnode>.<SUFFIX><n>'
    mo = re.match(pat, i)
    if not mo:
        raise SystemExit('bad suffixed id: %r' % i)
    return remap_node(mo.group(1)) + '.' + mo.group(2)

RQ  = r'^(M\d+\.S\d+\.T\d+)\.(RQ\d+)$'
TR  = r'^(M\d+\.S\d+\.T\d+)\.(TR\d+)$'
SRQ = r'^(M\d+\.S\d+)\.(RQ\d+)$'
MED = r'^(M\d+\.S\d+\.T\d+\.C\d+)\.((?:IMG|VID|2D|3D|SIM)\d+)$'

# ---------------------------------------------------------------- 3. whitelist + emit
ROOT_ORDER = ['phase','board','subject','grade','level','version','ordering','author',
              'chapter_id','plan_id','chapter_name','unit_title','unit_number','topic_title',
              'topic_number','genre','teaching_lens','guiding_question','textbook','textbook_url',
              'textbook_pages','_activate','medium_id','subject_ref_id','publication_id',
              'chapter_master_id','estimated_time','english_plan_id','english_chapter_id',
              'objectives','strand_to_objective_map','modules']

TOPIC_ORDER = ['topic_id','topic_name','topic_type','topic_category','difficulty',
               'original_chunk','modified_chunk','word_count','explanation','real_life_example',
               'brief_summary','summary','detailed_summary','key_terms','concept_bullets',
               'important_points','figures_of_speech','rhyme_scheme','shabdarth','samanarthi',
               'vilom','vyakaran','objective_ids','learning_objectives','concepts',
               'recall_questions','media','2d_tool','publication_text','publication_chunk',
               'depends_on','source_topic_ids','estimated_exchanges','primary_content_type',
               'secondary_content_type','tertiary_content_type','available_content_types']

OBJ_ORDER = ['objective_id','legacy_id','strand','strand_name','objective_text','bloom_level',
             'home_topic_id','anchor','status','theme_category']
LO_ORDER  = OBJ_ORDER + ['image_examples']
CON_ORDER = ['concept_id','concept_name','objective_id','key_terms','content']
RQ_ORDER  = ['id','legacy_id','prompt','answer','difficulty','bloom_level']
MED_ORDER = ['id','type','subtype','title','description','image_url','aspect_ratio','concept_id',
             'home_concept_id','objective_id','image_category','teaching_notes','negative_prompt',
             'generation_prompt']

TOPIC_TYPE_MAP = {'POEM':'instructional','STORY_TELLING':'instructional','CONCEPT':'instructional',
                  'REVIEW':'summary','EXERCISE':'assessment'}

def pick(src, order):
    o = collections.OrderedDict()
    for k in order:
        if k in src:
            o[k] = src[k]
    return o

# --- objectives registry (O{n} and strand map are NOT renumbered) ---
objectives = []
for o in merged['objectives']:
    n = pick(o, OBJ_ORDER)
    n['home_topic_id'] = remap_node(o['home_topic_id'])
    n['anchor'] = [remap_node(a) for a in o['anchor']]
    objectives.append(n)
obj_by_id = {o['objective_id']: o for o in objectives}

modules = []
for mod in merged['modules']:
    nm = collections.OrderedDict()
    nm['module_id'] = remap_node(mod['module_id'])
    nm['module_name'] = mod['module_name']
    nm['difficult_words'] = mod.get('difficult_words', [])
    nm['overall_rhyme_scheme'] = mod.get('overall_rhyme_scheme')
    nm['segments'] = []
    for seg in mod['segments']:
        ns = collections.OrderedDict()
        ns['segment_id'] = remap_node(seg['segment_id'])
        ns['segment_name'] = seg['segment_name']
        if 'recall_questions' in seg:
            ns['recall_questions'] = [
                dict(pick(r, RQ_ORDER), id=remap_suffixed(r['id'], SRQ)) for r in seg['recall_questions']]
        ns['topics'] = []
        for top in seg['topics']:
            nt = pick(top, TOPIC_ORDER)
            nt['topic_id'] = remap_node(top['topic_id'])
            authored = top['topic_type']
            if authored not in TOPIC_TYPE_MAP:
                raise SystemExit('unknown authored topic_type %r' % authored)
            nt['topic_type'] = TOPIC_TYPE_MAP[authored]
            nt['objective_ids'] = list(top['objective_ids'])
            nt['learning_objectives'] = []
            for lo in top['learning_objectives']:
                r = obj_by_id[lo['objective_id']]
                n = pick(lo, LO_ORDER)
                # inline mirror = registry copy, character for character
                for k in OBJ_ORDER:
                    n[k] = r[k]
                n['image_examples'] = lo.get('image_examples', [])
                nt['learning_objectives'].append(pick(n, LO_ORDER))
            nt['concepts'] = []
            for con in top['concepts']:
                nc = pick(con, CON_ORDER)
                nc['concept_id'] = remap_node(con['concept_id'])
                nt['concepts'].append(nc)
            nt['recall_questions'] = []
            for r in top.get('recall_questions', []):
                nr = pick(r, RQ_ORDER)
                nr['id'] = remap_suffixed(r['id'], RQ)
                nr['legacy_id'] = remap_suffixed(r['legacy_id'], TR)
                nt['recall_questions'].append(nr)
            nt['media'] = []
            for md in top.get('media', []):
                nd = pick(md, MED_ORDER)
                nd['id'] = remap_suffixed(md['id'], MED)
                nd['concept_id'] = remap_node(md['concept_id'])
                nd['home_concept_id'] = remap_node(md['home_concept_id'])
                nt['media'].append(nd)
            nt['depends_on'] = [remap_node(x) for x in top.get('depends_on', [])]
            nt['source_topic_ids'] = [remap_node(x) for x in top.get('source_topic_ids', [])]
            ns['topics'].append(nt)
        nm['segments'].append(ns)
    modules.append(nm)

plan = collections.OrderedDict()
for k in ROOT_ORDER:
    if k in merged:
        plan[k] = merged[k]
plan['ordering'] = 'logical'
plan['genre'] = 'varta'                       # roster slug for the વાર્તા profile
plan['topic_title'] = merged['chapter_name']  # merged left it null
plan['objectives'] = objectives
plan['strand_to_objective_map'] = merged['strand_to_objective_map']
plan['modules'] = modules
plan = pick(plan, ROOT_ORDER)

assert len(plan) == 32, len(plan)

with io.open(os.path.join(D, 'learning_plan_logical.json'), 'w', encoding='utf-8') as f:
    json.dump(plan, f, ensure_ascii=False, indent=1)
    f.write('\n')

# ---------------------------------------------------------------- 4. covered_by_topics
ex_path = os.path.join(D, '10_exercise_solutions.json')
ex = json.load(open(ex_path), object_pairs_hook=collections.OrderedDict)
changed = 0
for e in ex['exercises']:
    new = [remap_node(x) for x in e.get('covered_by_topics', [])]
    if new != e.get('covered_by_topics', []):
        e['covered_by_topics'] = new
        changed += 1
if changed:
    with io.open(ex_path, 'w', encoding='utf-8') as f:
        json.dump(ex, f, ensure_ascii=False, indent=1)
        f.write('\n')
print('covered_by_topics entries rewritten:', changed)
print('identity renumber:', all(k == v for k, v in idmap.items()))
print('nodes:', len(idmap), 'modules/segments/topics/concepts =', m, s, t, c)
