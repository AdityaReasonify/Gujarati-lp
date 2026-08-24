#!/usr/bin/env python3
# Agent 13 — merge every layer onto 05_with_content.json into one phase-2 plan.
import json, os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
def L(n): return json.load(open(os.path.join(D, n), encoding='utf-8'))

meta   = L('01_meta.json')
base   = L('05_with_content.json')
auth   = L('12_authoring.json')
media  = L('09_media.json')
pages  = L('11_pages.json')
pub    = L('16_publication.json') if os.path.exists(os.path.join(D,'16_publication.json')) else None

auth_by_tid  = {t['topic_id']: t for t in auth['topics']}
auth_mod     = {m['module_id']: m for m in auth['modules']}
media_by_cid = {}
for m in media['media']:
    media_by_cid.setdefault(m['concept_id'], []).append(m)
pub_by_tid = {}
if pub:
    for t in (pub.get('topics') or []):
        pub_by_tid[t['topic_id']] = t

TOPIC_KEYS = ["media","2d_tool","summary","concepts","topic_id","key_terms","depends_on",
 "difficulty","topic_name","topic_type","word_count","explanation","brief_summary",
 "objective_ids","modified_chunk","original_chunk","topic_category","concept_bullets",
 "detailed_summary","important_points","publication_text","recall_questions",
 "source_topic_ids","publication_chunk","real_life_example","estimated_exchanges",
 "learning_objectives","primary_content_type","tertiary_content_type",
 "secondary_content_type","available_content_types"]
POEM_EXTRA = ["figures_of_speech","rhyme_scheme"]
BHASHA = ["shabdarth","samanarthi","vilom","vyakaran"]

obj_by_id = {o['objective_id']: o for o in base['objectives']}

modules = []
first_topic = True
for mod in base['modules']:
    am = auth_mod.get(mod['module_id'], {})
    nm = {"module_id": mod['module_id'], "module_name": mod['module_name'], "segments": []}
    if 'difficult_words' in am: nm['difficult_words'] = am['difficult_words']
    if 'overall_rhyme_scheme' in am: nm['overall_rhyme_scheme'] = am['overall_rhyme_scheme']
    for seg in mod['segments']:
        ns = {"segment_id": seg['segment_id'], "segment_name": seg['segment_name'], "topics": []}
        for t in seg['topics']:
            a = auth_by_tid.get(t['topic_id'], {})
            p = pub_by_tid.get(t['topic_id'], {})
            aconcepts = {c['concept_id']: c for c in a.get('concepts', [])}
            pconcepts = {c['concept_id']: c for c in (p.get('concepts') or [])}
            concepts = []
            for c in t['concepts']:
                ac = aconcepts.get(c['concept_id'], {})
                content = [dict(x) for x in ac.get('content', [])]
                pc = pconcepts.get(c['concept_id'], {})
                pcontent = pc.get('content') or []
                for i, blk in enumerate(content):
                    if blk.get('type') == 'paragraph':
                        blk['publication_text'] = (pcontent[i].get('publication_text','')
                                                   if i < len(pcontent) else "")
                nc = {"concept_id": c['concept_id'], "concept_name": c['concept_name'],
                      "objective_id": c['objective_id'], "key_terms": c.get('key_terms', []),
                      "content": content}
                md = media_by_cid.get(c['concept_id'])
                concepts.append(nc)
            nt = {}
            nt['topic_id']        = t['topic_id']
            nt['topic_name']      = t['topic_name']
            nt['topic_type']      = t['topic_type']
            nt['topic_category']  = t['topic_category']
            nt['difficulty']      = t.get('difficulty')
            nt['depends_on']      = t.get('depends_on', [])
            nt['source_topic_ids']= t.get('source_topic_ids', [])
            nt['objective_ids']   = t['objective_ids']
            nt['learning_objectives'] = [dict(obj_by_id[o], image_examples=[]) for o in t['objective_ids']]
            nt['original_chunk']  = t['original_chunk']
            nt['modified_chunk']  = t['modified_chunk']
            nt['word_count']      = t['word_count']
            nt['key_terms']       = t.get('key_terms', [])
            nt['primary_content_type']   = t.get('primary_content_type')
            nt['secondary_content_type'] = t.get('secondary_content_type')
            nt['tertiary_content_type']  = t.get('tertiary_content_type')
            nt['available_content_types']= t.get('available_content_types', [])
            nt['explanation']     = a.get('explanation', "")
            nt['real_life_example'] = a.get('real_life_example', "")
            nt['brief_summary']   = a.get('brief_summary', "")
            nt['summary']         = a.get('summary', "")
            nt['detailed_summary']= a.get('detailed_summary', "")
            nt['concept_bullets'] = a.get('concept_bullets', [])
            nt['important_points']= a.get('important_points', [])
            nt['recall_questions']= a.get('recall_questions', [])
            nt['estimated_exchanges'] = a.get('estimated_exchanges', "")
            nt['concepts']        = concepts
            nt['media']           = [dict((k, v) for k, v in mm.items() if k != 'topic_id')
                                     for c in t['concepts'] for mm in media_by_cid.get(c['concept_id'], [])]
            nt['2d_tool']         = media.get('2d_tool') if first_topic else None
            nt['publication_text']  = p.get('publication_text', "")
            nt['publication_chunk'] = p.get('publication_chunk', "")
            for k in POEM_EXTRA:
                if k in a: nt[k] = a[k]
            for k in BHASHA:
                if k in a: nt[k] = a[k]
            first_topic = False
            ns['topics'].append(nt)
        nm['segments'].append(ns)
    modules.append(nm)

plan = {
    "phase": 2,
    "board": meta['board'],
    "subject": meta['subject'],
    "grade": meta['grade'],
    "level": meta['level'],
    "version": meta['version'],
    "chapter_id": meta['chapter_id'],
    "plan_id": meta['plan_id'],
    "chapter_name": meta['chapter_name'],
    "unit_title": meta['unit_title'],
    "unit_number": meta['unit_number'],
    "topic_title": meta['unit_title'],
    "topic_number": meta['topic_number'],
    "genre": base['genre'],   # slug per phase2_contract; 01_meta records the printed label
    "teaching_lens": meta['teaching_lens'],
    "guiding_question": meta['guiding_question'],
    "textbook": pages['textbook'],
    "textbook_url": pages['textbook_url'],
    "textbook_pages": pages['textbook_pages'],
    "author": "",
    "_activate": False,
    "medium_id": None,
    "subject_ref_id": None,
    "english_plan_id": None,
    "english_chapter_id": None,
    "estimated_time": 1.5,
    "publication_id": 1,   # provisional pack value; VERIFY-2 owns the real GSEB row
    "chapter_master_id": meta.get('chapter_master_id'),
    "objectives": base['objectives'],
    "strand_to_objective_map": base['strand_to_objective_map'],
    "modules": modules,
}
json.dump(plan, open(os.path.join(D, '13_merged.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print("wrote 13_merged.json; topics =", sum(len(s['topics']) for m in modules for s in m['segments']))
print("publication layer present:", bool(pub))
