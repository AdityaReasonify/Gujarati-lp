#!/usr/bin/env python3
# Agent 13 — merge every layer onto 05_with_content.json into one phase-2 plan.
import json, collections, os

D = os.path.dirname(os.path.abspath(__file__))
L = lambda n: json.load(open(os.path.join(D, n), encoding='utf-8'))

meta = L('01_meta.json')
base = L('05_with_content.json')
auth = L('12_authoring.json')
media = L('09_media.json')
pub  = L('16_publication.json')
pages = L('11_pages.json')

auth_by = {t['topic_id']: t for t in auth['topics']}
pub_by  = {t['topic_id']: t for t in pub['topics']}
mod_by  = {m['module_id']: m for m in auth['modules']}
media_by = collections.defaultdict(list)
for m in media['media']:
    media_by[m['concept_id']].append(m)

MEDIA_KEYS = ['id','type','subtype','title','description','image_url','aspect_ratio',
              'concept_id','home_concept_id','objective_id','image_category',
              'teaching_notes','negative_prompt','generation_prompt']

obj_by = {o['objective_id']: o for o in base['objectives']}

TOPIC_KEYS = ['media','2d_tool','summary','concepts','topic_id','key_terms','depends_on',
    'difficulty','topic_name','topic_type','word_count','explanation','brief_summary',
    'objective_ids','modified_chunk','original_chunk','topic_category','concept_bullets',
    'detailed_summary','important_points','publication_text','recall_questions',
    'source_topic_ids','publication_chunk','real_life_example','estimated_exchanges',
    'learning_objectives','primary_content_type','tertiary_content_type',
    'secondary_content_type','available_content_types']
EXTRA_KEYS = ['figures_of_speech','rhyme_scheme','shabdarth','samanarthi','vilom','vyakaran']

modules = []
for m in base['modules']:
    am = mod_by.get(m['module_id'], {})
    segs = []
    for s in m['segments']:
        tops = []
        for t in s['topics']:
            tid = t['topic_id']
            a = auth_by[tid]
            p = pub_by[tid]
            # concepts: base shape + authored content, publication_text matched BY INDEX
            acon = {c['concept_id']: c for c in a.get('concepts', [])}
            cpub = collections.defaultdict(dict)
            for cp in p.get('concept_publication', []):
                cpub[cp['concept_id']][cp['content_index']] = cp['publication_text']
            concepts = []
            tmedia = []
            for c in t['concepts']:
                cid = c['concept_id']
                content = []
                for i, blk in enumerate(acon.get(cid, {}).get('content', [])):
                    nb = dict(blk)
                    if nb.get('type') == 'paragraph' and i in cpub[cid]:
                        nb['publication_text'] = cpub[cid][i]
                    content.append(nb)
                concepts.append({
                    'concept_id': cid,
                    'concept_name': c['concept_name'],
                    'objective_id': c['objective_id'],
                    'key_terms': c.get('key_terms', []),
                    'content': content,
                })
                for md in media_by.get(cid, []):
                    tmedia.append({k: md[k] for k in MEDIA_KEYS})
            lo = []
            for oid in t['objective_ids']:
                o = dict(obj_by[oid]); o['image_examples'] = []
                lo.append(o)
            nt = {
                'topic_id': tid,
                'topic_name': t['topic_name'],
                'topic_type': t['topic_type'],
                'topic_category': t['topic_category'],
                'difficulty': t['difficulty'],
                'depends_on': t['depends_on'],
                'source_topic_ids': [],
                'objective_ids': t['objective_ids'],
                'learning_objectives': lo,
                'key_terms': t['key_terms'],
                'word_count': {'original': t['word_count']['original']},
                'original_chunk': t['original_chunk'],
                'modified_chunk': t['modified_chunk'],
                'explanation': a['explanation'],
                'real_life_example': a['real_life_example'],
                'brief_summary': a['brief_summary'],
                'summary': a['summary'],
                'detailed_summary': a['detailed_summary'],
                'concept_bullets': a['concept_bullets'],
                'important_points': a['important_points'],
                'recall_questions': a['recall_questions'],
                'estimated_exchanges': a['estimated_exchanges'],
                'figures_of_speech': a['figures_of_speech'],
                'rhyme_scheme': a['rhyme_scheme'],
                'shabdarth': a['shabdarth'],
                'samanarthi': a['samanarthi'],
                'vilom': a['vilom'],
                'vyakaran': a['vyakaran'],
                'concepts': concepts,
                'media': tmedia,
                '2d_tool': None,
                'publication_text': p['publication_text'],
                'publication_chunk': p['publication_chunk'],
                'primary_content_type': t['primary_content_type'],
                'secondary_content_type': t['secondary_content_type'],
                'tertiary_content_type': t['tertiary_content_type'],
                'available_content_types': t['available_content_types'],
            }
            tops.append(nt)
        segs.append({'segment_id': s['segment_id'], 'segment_name': s['segment_name'],
                     'topics': tops})
    modules.append({'module_id': m['module_id'], 'module_name': m['module_name'],
                    'difficult_words': am.get('difficult_words', []),
                    'overall_rhyme_scheme': am.get('overall_rhyme_scheme', None),
                    'segments': segs})

plan = {
    'phase': 2,
    'board': meta['board'],
    'subject': meta['subject'],
    'grade': meta['grade'],
    'level': meta['level'],
    'version': meta['version'],
    'chapter_id': meta['chapter_id'],
    'plan_id': meta['plan_id'],
    'author': '',
    '_activate': False,
    'medium_id': None,
    'subject_ref_id': None,
    'chapter_master_id': meta.get('chapter_master_id'),
    'publication_id': 1,
    'estimated_time': 1.5,
    'english_plan_id': None,
    'english_chapter_id': None,
    'textbook': meta['textbook'],
    'textbook_url': meta['textbook_url'],
    'textbook_pages': pages.get('textbook_pages', ''),
    'chapter_name': meta['chapter_name'],
    'unit_title': meta['unit_title'],
    'unit_number': meta['unit_number'],
    'topic_title': meta['chapter_name'],
    'topic_number': meta['topic_number'],
    'genre': base['genre'],
    'teaching_lens': meta['teaching_lens'],
    'guiding_question': meta['guiding_question'],
    'objectives': base['objectives'],
    'strand_to_objective_map': base['strand_to_objective_map'],
    'modules': modules,
}

with open(os.path.join(D, '13_merged.json'), 'w', encoding='utf-8') as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
    f.write('\n')

nt = sum(len(s['topics']) for m in modules for s in m['segments'])
nc = sum(len(t['concepts']) for m in modules for s in m['segments'] for t in s['topics'])
nm = sum(len(t['media']) for m in modules for s in m['segments'] for t in s['topics'])
print('root keys', len(plan), '| topics', nt, '| concepts', nc, '| media', nm)
