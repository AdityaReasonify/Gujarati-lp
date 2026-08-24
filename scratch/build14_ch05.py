#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agent 14 — arrange, renumber, translate references, whitelist, emit.

std 6 / ch05 / વીજળીરાણી.
"""
import json
import re
import shutil
import sys
from collections import OrderedDict

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch05"
MERGED = OUT + "/13_merged.json"
EXSRC = OUT + "/10_exercise_solutions.json"

# ---------------------------------------------------------------- key orders
ROOT_ORDER = ['phase', 'board', 'subject', 'grade', 'level', 'version', 'ordering',
              'author', 'chapter_id', 'plan_id', 'chapter_name', 'unit_title',
              'unit_number', 'topic_title', 'topic_number', 'genre', 'teaching_lens',
              'guiding_question', 'textbook', 'textbook_url', 'textbook_pages',
              '_activate', 'medium_id', 'subject_ref_id', 'publication_id',
              'chapter_master_id', 'estimated_time', 'english_plan_id',
              'english_chapter_id', 'objectives', 'strand_to_objective_map', 'modules']

MOD_ORDER = ['module_id', 'module_name', 'difficult_words', 'overall_rhyme_scheme', 'segments']
SEG_ORDER = ['segment_id', 'segment_name', 'topics']
TOP_ORDER = ['topic_id', 'topic_name', 'topic_type', 'topic_category', 'difficulty',
             'original_chunk', 'modified_chunk', 'word_count', 'explanation',
             'real_life_example', 'brief_summary', 'summary', 'detailed_summary',
             'key_terms', 'concept_bullets', 'important_points', 'figures_of_speech',
             'rhyme_scheme', 'shabdarth', 'samanarthi', 'vilom', 'vyakaran',
             'objective_ids', 'learning_objectives', 'concepts', 'recall_questions',
             'media', '2d_tool', 'publication_text', 'publication_chunk', 'depends_on',
             'source_topic_ids', 'estimated_exchanges', 'primary_content_type',
             'secondary_content_type', 'tertiary_content_type', 'available_content_types']
OBJ_ORDER = ['objective_id', 'legacy_id', 'strand', 'strand_name', 'objective_text',
             'bloom_level', 'home_topic_id', 'anchor', 'status', 'theme_category']
LO_ORDER = OBJ_ORDER + ['image_examples']
CON_ORDER = ['concept_id', 'concept_name', 'objective_id', 'key_terms', 'content']
RQ_ORDER = ['id', 'legacy_id', 'prompt', 'answer', 'difficulty', 'bloom_level']
MEDIA_ORDER = ['id', 'type', 'subtype', 'title', 'description', 'image_url',
               'aspect_ratio', 'concept_id', 'home_concept_id', 'objective_id',
               'image_category', 'teaching_notes', 'negative_prompt', 'generation_prompt']

TOPIC_TYPE_MAP = {'POEM': 'instructional', 'STORY_TELLING': 'instructional',
                  'CONCEPT': 'instructional', 'REVIEW': 'summary',
                  'EXERCISE': 'assessment'}

MEDIA_ID_RE = re.compile(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$")

problems = []


def pick(src, order, where):
    """Whitelist + canonical order. Reports any key dropped or missing."""
    out = OrderedDict()
    for k in order:
        if k in src:
            out[k] = src[k]
    extra = [k for k in src if k not in order]
    if extra:
        problems.append("dropped keys at %s: %s" % (where, extra))
    missing = [k for k in order if k not in src]
    if missing:
        problems.append("missing keys at %s: %s" % (where, missing))
    return out


# ------------------------------------------------------------------ 1. load
with open(MERGED, encoding="utf-8") as fh:
    plan = json.load(fh)

# ------------------------------------------- 2. arrange + 3. build id map
# Reading order == the merged traversal (confirmed against 05b_textbook_order.json,
# whose textbook_order matches the merged traversal exactly and whose
# matches_logical_order flag is true).
idmap = {}
m_i = s_i = t_i = c_i = 0
for mod in plan['modules']:
    m_i += 1
    new_m = "M%d" % m_i
    idmap[mod['module_id']] = new_m
    for seg in mod['segments']:
        s_i += 1
        new_s = "%s.S%d" % (new_m, s_i)
        idmap[seg['segment_id']] = new_s
        for top in seg['topics']:
            t_i += 1
            new_t = "%s.T%d" % (new_s, t_i)
            idmap[top['topic_id']] = new_t
            for con in top['concepts']:
                c_i += 1
                idmap[con['concept_id']] = "%s.C%d" % (new_t, c_i)

NODE_IDS = set(idmap.values())


def tr(old, where):
    if old is None:
        return None
    if old not in idmap:
        problems.append("UNRESOLVED id %r at %s" % (old, where))
        return old
    return idmap[old]


def tr_media(old, where):
    """{concept_id}.{TYPE}{n} -> translated concept id + same suffix."""
    mm = MEDIA_ID_RE.match(old or "")
    if not mm:
        problems.append("media id does not match MEDIA_ID_RE: %r at %s" % (old, where))
        return old
    return "%s.%s%s" % (tr(mm.group(1), where), mm.group(2), mm.group(3))


def tr_recall(old, where, expect_suffix):
    """{node_id}.RQ{n} / {node_id}.TR{n}."""
    mm = re.match(r"^(M\d+\.S\d+(?:\.T\d+)?)\.(RQ|TR|SR)(\d+)$", old or "")
    if not mm:
        problems.append("recall id malformed: %r at %s" % (old, where))
        return old
    if mm.group(2) == 'SR':
        problems.append("LP-v1 .SR recall id found (server rejects): %r at %s" % (old, where))
    return "%s.%s%s" % (tr(mm.group(1), where), expect_suffix, mm.group(3))


# ------------------------------------------- 4. rewrite the tree
new_modules = []
for mod in plan['modules']:
    nm = dict(mod)
    nm['module_id'] = idmap[mod['module_id']]
    new_segs = []
    for seg in mod['segments']:
        ns = dict(seg)
        ns['segment_id'] = idmap[seg['segment_id']]
        # segment-level recall questions, if the pack ever emits them
        if seg.get('recall_questions'):
            ns['recall_questions'] = [
                dict(rq, id=tr_recall(rq['id'], 'seg %s' % ns['segment_id'], 'RQ'),
                     **({'legacy_id': tr_recall(rq['legacy_id'], 'seg', 'TR')}
                        if rq.get('legacy_id') else {}))
                for rq in seg['recall_questions']]
        new_tops = []
        for top in seg['topics']:
            nt = dict(top)
            where = top['topic_id']
            nt['topic_id'] = idmap[top['topic_id']]
            nt['topic_type'] = TOPIC_TYPE_MAP.get(top['topic_type'], top['topic_type'])
            if nt['topic_type'] not in ('instructional', 'summary', 'assessment'):
                problems.append("topic_type not in server enum at %s: %r"
                                % (where, nt['topic_type']))
            nt['depends_on'] = [tr(x, where + '.depends_on') for x in (top.get('depends_on') or [])]
            nt['source_topic_ids'] = [tr(x, where + '.source_topic_ids')
                                      for x in (top.get('source_topic_ids') or [])]
            # objective_ids / learning_objectives: O{n} are NOT renumbered,
            # but the home_topic_id / anchor inside the inline mirror are.
            nt['learning_objectives'] = [
                pick(OrderedDict(
                    lo,
                    home_topic_id=tr(lo.get('home_topic_id'), where + '.lo.home_topic_id'),
                    anchor=[tr(a, where + '.lo.anchor') for a in (lo.get('anchor') or [])],
                ), LO_ORDER, where + '.learning_objectives')
                for lo in (top.get('learning_objectives') or [])]
            nt['concepts'] = [
                pick(OrderedDict(con, concept_id=idmap[con['concept_id']]),
                     CON_ORDER, where + '.concepts')
                for con in top['concepts']]
            nt['recall_questions'] = [
                pick(OrderedDict(
                    rq,
                    id=tr_recall(rq['id'], where + '.rq', 'RQ'),
                    legacy_id=tr_recall(rq['legacy_id'], where + '.rq', 'TR')
                    if rq.get('legacy_id') else None),
                    RQ_ORDER, where + '.recall_questions')
                for rq in (top.get('recall_questions') or [])]
            nt['media'] = [
                pick(OrderedDict(
                    md,
                    id=tr_media(md['id'], where + '.media'),
                    concept_id=tr(md.get('concept_id'), where + '.media.concept_id'),
                    home_concept_id=tr(md.get('home_concept_id'),
                                       where + '.media.home_concept_id')),
                    MEDIA_ORDER, where + '.media')
                for md in (top.get('media') or [])]
            new_tops.append(pick(nt, TOP_ORDER, where))
        ns['topics'] = new_tops
        new_segs.append(pick(ns, SEG_ORDER, ns['segment_id']))
    nm['segments'] = new_segs
    new_modules.append(pick(nm, MOD_ORDER, nm['module_id']))

# ------------------------------------------- 5. root objectives registry
new_objs = []
for o in plan['objectives']:
    no = OrderedDict(o)
    no['home_topic_id'] = tr(o.get('home_topic_id'), 'objectives.%s.home_topic_id' % o['objective_id'])
    no['anchor'] = [tr(a, 'objectives.%s.anchor' % o['objective_id'])
                    for a in (o.get('anchor') or [])]
    new_objs.append(pick(no, OBJ_ORDER, 'objectives.%s' % o['objective_id']))

# ------------------------------------------- 6. root fields
grade = plan['grade']
unit = plan['unit_number']
chapter_id = "gseb_eng_gujarati%d_ch%d" % (grade, unit)
version = plan.get('version') or 1

root = OrderedDict(plan)
root['phase'] = 2
root['ordering'] = "logical"
root['chapter_id'] = chapter_id
root['plan_id'] = "%s_v%d" % (chapter_id, version)
root['version'] = version
root['genre'] = "mahitiprad_gadya"      # roster slug (profiles/genres/mahitiprad_gadya.md)
root['english_plan_id'] = None
root['english_chapter_id'] = None
root['subject_ref_id'] = None
root['medium_id'] = None
root['_activate'] = False
root['objectives'] = new_objs
root['modules'] = new_modules

# DB fields — upload_reference/chapter_master_map.json is the only source.
with open("/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/upload_reference/chapter_master_map.json",
          encoding="utf-8") as fh:
    cmm = json.load(fh)
row = cmm.get(chapter_id) or {}
root['chapter_master_id'] = row.get('chapter_master_id')
if row.get('publication_id') is not None:
    root['publication_id'] = row['publication_id']
# else: keep whatever Agent 13 carried; never invent a value here.

plan_out = pick(root, ROOT_ORDER, 'root')

# ------------------------------------------- 7. assertions
def assert_plan(p):
    ids = set()
    m_i = s_i = t_i = c_i = 0
    topic_ids, concept_ids = set(), set()
    for mod in p['modules']:
        m_i += 1
        assert mod['module_id'] == "M%d" % m_i, ("module id", mod['module_id'])
        for seg in mod['segments']:
            s_i += 1
            exp = "M%d.S%d" % (m_i, s_i)
            assert seg['segment_id'] == exp, ("segment id", seg['segment_id'], exp)
            for top in seg['topics']:
                t_i += 1
                exp_t = "%s.T%d" % (exp, t_i)
                assert top['topic_id'] == exp_t, ("topic id", top['topic_id'], exp_t)
                topic_ids.add(exp_t)
                for con in top['concepts']:
                    c_i += 1
                    exp_c = "%s.C%d" % (exp_t, c_i)
                    assert con['concept_id'] == exp_c, ("concept id", con['concept_id'], exp_c)
                    concept_ids.add(exp_c)
    ids = topic_ids | concept_ids
    obj_ids = {o['objective_id'] for o in p['objectives']}

    for o in p['objectives']:
        assert o['home_topic_id'] in topic_ids, ("stale home_topic_id", o)
        for a in o['anchor']:
            assert a in concept_ids, ("stale anchor", o['objective_id'], a)
        assert o['legacy_id'] in p['strand_to_objective_map'], ("legacy_id unmapped", o)
        assert p['strand_to_objective_map'][o['legacy_id']] == o['objective_id']
    assert len(obj_ids) == len(p['objectives']), "duplicate objective_id"

    reg = {o['objective_id']: o for o in p['objectives']}
    seen_media, seen_rq = set(), set()
    for mod in p['modules']:
        for seg in mod['segments']:
            for top in seg['topics']:
                tid = top['topic_id']
                assert top['topic_type'] in ('instructional', 'summary', 'assessment')
                for x in top['depends_on'] + top['source_topic_ids']:
                    assert x in ids, ("stale ref", tid, x)
                for oid in top['objective_ids']:
                    assert oid in obj_ids, ("stale objective_ids", tid, oid)
                for lo in top['learning_objectives']:
                    r = reg[lo['objective_id']]
                    assert lo['objective_text'] == r['objective_text'], ("mirror drift", tid)
                    assert lo['home_topic_id'] == r['home_topic_id'], ("mirror home drift", tid)
                    assert lo['anchor'] == r['anchor'], ("mirror anchor drift", tid)
                    assert lo['home_topic_id'] in topic_ids
                    for a in lo['anchor']:
                        assert a in concept_ids
                assert top['concepts'], ("no concepts", tid)
                for con in top['concepts']:
                    assert con['objective_id'] in obj_ids, ("stale concept objective", tid)
                    assert con['content'], ("empty concept content", tid)
                    assert con['concept_id'].startswith(tid + "."), ("concept not under topic", tid)
                for rq in top['recall_questions']:
                    assert re.match(r"^%s\.RQ\d+$" % re.escape(tid), rq['id']), ("rq id", rq['id'])
                    assert re.match(r"^%s\.TR\d+$" % re.escape(tid), rq['legacy_id']), rq['legacy_id']
                    assert rq['id'] not in seen_rq
                    seen_rq.add(rq['id'])
                for md in top['media']:
                    mm = MEDIA_ID_RE.match(md['id'])
                    assert mm, ("media id", md['id'])
                    assert mm.group(1) in concept_ids, ("media concept missing", md['id'])
                    assert md['concept_id'] in concept_ids
                    assert md['home_concept_id'] in concept_ids
                    assert md['id'] not in seen_media
                    seen_media.add(md['id'])
                    assert md['image_url'] or md['generation_prompt'], ("media both empty", md['id'])
                assert re.search(r'[઀-૿]', top['original_chunk'] or ''), ("no Gujarati chunk", tid)
                # three-tier summaries strictly increase
                a, b, c = (len(top['brief_summary']), len(top['summary']),
                           len(top['detailed_summary']))
                if not (a < b < c):
                    problems.append("summaries do not strictly increase at %s (%d/%d/%d)"
                                    % (tid, a, b, c))
    return dict(modules=m_i, segments=s_i, topics=t_i, concepts=c_i,
                objectives=len(obj_ids), media=len(seen_media), recall=len(seen_rq))


stats = assert_plan(plan_out)

# no numbers in display text (soft report)
NUMWORD = re.compile(r'(કડી|પ્રશ્ન|સ્વાધ્યાય|ટૉપિક|ખંડ|દુહો|પદ)\s*\d')
for mod in plan_out['modules']:
    for seg in mod['segments']:
        for top in seg['topics']:
            for f in ('topic_name', 'explanation', 'real_life_example', 'brief_summary',
                      'summary', 'detailed_summary'):
                if NUMWORD.search(top.get(f) or ''):
                    problems.append("number in display text: %s.%s" % (top['topic_id'], f))

# ------------------------------------------- 8. exercise deliverable
with open(EXSRC, encoding="utf-8") as fh:
    ex = json.load(fh)

changed = 0
for e in ex['exercises']:
    new = []
    for t in e.get('covered_by_topics') or []:
        n = tr(t, 'exercise %s.covered_by_topics' % e['exercise_id'])
        if n != t:
            changed += 1
        new.append(n)
    e['covered_by_topics'] = new
for u in ex['coverage_report'].get('unmapped') or []:
    pass  # unmapped carries no node ids

if changed:
    with open(EXSRC, 'w', encoding='utf-8') as fh:
        json.dump(ex, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

# every covered_by_topics id must resolve in the emitted plan
tids = {t['topic_id'] for m in plan_out['modules'] for s in m['segments'] for t in s['topics']}
for e in ex['exercises']:
    for t in e['covered_by_topics']:
        assert t in tids, ("stale covered_by_topics", e['exercise_id'], t)

# ------------------------------------------- 9. write
if problems:
    print("PROBLEMS:")
    for p in problems:
        print("  -", p)

with open(OUT + "/learning_plan_logical.json", "w", encoding="utf-8") as fh:
    json.dump(plan_out, fh, ensure_ascii=False, indent=2)
    fh.write("\n")

shutil.copyfile(EXSRC, OUT + "/exercise_solutions.json")

print("stats:", stats)
print("covered_by_topics ids rewritten:", changed)
print("identity renumber:", all(k == v for k, v in idmap.items()))
