# -*- coding: utf-8 -*-
import json, copy
D="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch02/"
L=lambda f: json.load(open(D+f, encoding='utf-8'))
meta=L('01_meta.json'); base=L('05_with_content.json'); auth=L('12_authoring.json')
med=L('09_media.json'); pub=L('16_publication.json'); pg=L('11_pages.json')

A={t['topic_id']:t for t in auth['topics']}
P={t['topic_id']:t for t in pub['topics']}
AM={m['module_id']:m for m in auth['modules']}
MEDIA={}
for n in med['media']: MEDIA.setdefault(n['topic_id'],[]).append(n)
MEDIA_KEYS=["id","type","subtype","title","description","image_url","aspect_ratio",
            "concept_id","home_concept_id","objective_id","image_category",
            "teaching_notes","negative_prompt","generation_prompt"]

objs={o['objective_id']:o for o in base['objectives']}

plan={
 "phase": 2,
 "board": meta['board'],
 "subject": meta['subject'],
 "grade": meta['grade'],
 "level": meta['level'],
 "version": meta['version'],
 "chapter_id": meta['chapter_id'],
 "plan_id": meta['plan_id'],
 "author": "",
 "_activate": False,
 "medium_id": None,
 "subject_ref_id": None,
 "english_plan_id": None,
 "english_chapter_id": None,
 "chapter_master_id": meta['chapter_master_id'],   # null — VERIFY-2, never invented
 "publication_id": 1,                              # PROVISIONAL — VERIFY-2 must replace before upload
 "estimated_time": 1.5,
 "textbook": pg['textbook'],
 "textbook_url": pg['textbook_url'],
 "textbook_pages": pg['textbook_pages'],
 "chapter_name": meta['chapter_name'],
 "unit_title": meta['unit_title'],
 "unit_number": meta['unit_number'],
 "topic_title": meta['chapter_name'],
 "topic_number": meta['topic_number'],
 "genre": base['genre'],                           # roster slug 'varta' (01_meta holds the Gujarati label)
 "teaching_lens": meta['teaching_lens'],
 "guiding_question": meta['guiding_question'],
 "objectives": copy.deepcopy(base['objectives']),
 "strand_to_objective_map": copy.deepcopy(base['strand_to_objective_map']),
 "modules": [],
}

TOPIC_ORDER=["topic_id","topic_name","topic_type","topic_category","difficulty",
 "objective_ids","learning_objectives","original_chunk","modified_chunk","publication_chunk",
 "word_count","key_terms","explanation","real_life_example","publication_text",
 "brief_summary","summary","detailed_summary","concept_bullets","important_points",
 "recall_questions","concepts","media","2d_tool","figures_of_speech","rhyme_scheme",
 "shabdarth","samanarthi","vilom","vyakaran","estimated_exchanges",
 "depends_on","source_topic_ids","primary_content_type","secondary_content_type",
 "tertiary_content_type","available_content_types"]

for m in base['modules']:
    am=AM.get(m['module_id'],{})
    mo={"module_id":m['module_id'],"module_name":m['module_name'],
        "difficult_words":copy.deepcopy(am.get('difficult_words',[])),
        "overall_rhyme_scheme":am.get('overall_rhyme_scheme',None),
        "segments":[]}
    for s in m['segments']:
        so={"segment_id":s['segment_id'],"segment_name":s['segment_name'],"topics":[]}
        for t in s['topics']:
            tid=t['topic_id']; a=A[tid]; p=P[tid]
            cp={}
            for c in p.get('concept_publication',[]):
                cp[(c['concept_id'],c['content_index'])]=c['publication_text']
            acon={c['concept_id']:c.get('content',[]) for c in a.get('concepts',[])}
            concepts=[]
            for c in t['concepts']:
                cid=c['concept_id']
                content=[]
                for i,blk in enumerate(acon.get(cid,[])):
                    nb=copy.deepcopy(blk)
                    if nb.get('type')=='paragraph' and (cid,i) in cp:
                        nb['publication_text']=cp[(cid,i)]
                    content.append(nb)
                concepts.append({"concept_id":cid,"concept_name":c['concept_name'],
                                 "objective_id":c['objective_id'],
                                 "key_terms":c.get('key_terms',[]),
                                 "content":content})
            media=[{k:n[k] for k in MEDIA_KEYS} for n in MEDIA.get(tid,[])]
            lo=[]
            for oid in t['objective_ids']:
                o=copy.deepcopy(objs[oid]); o['image_examples']=[]; lo.append(o)
            to={
              "topic_id":tid,"topic_name":t['topic_name'],"topic_type":t['topic_type'],
              "topic_category":t['topic_category'],"difficulty":t['difficulty'],
              "objective_ids":t['objective_ids'],"learning_objectives":lo,
              "original_chunk":t['original_chunk'],"modified_chunk":t['modified_chunk'],
              "publication_chunk":p['publication_chunk'],
              "word_count":t['word_count'],"key_terms":t['key_terms'],
              "explanation":a['explanation'],"real_life_example":a['real_life_example'],
              "publication_text":p['publication_text'],
              "brief_summary":a['brief_summary'],"summary":a['summary'],
              "detailed_summary":a['detailed_summary'],
              "concept_bullets":a['concept_bullets'],"important_points":a['important_points'],
              "recall_questions":copy.deepcopy(a['recall_questions']),
              "concepts":concepts,"media":media,"2d_tool":med['2d_tool'],
              "figures_of_speech":a.get('figures_of_speech',[]),
              "rhyme_scheme":a.get('rhyme_scheme',None),
              "shabdarth":a.get('shabdarth',[]),"samanarthi":a.get('samanarthi',[]),
              "vilom":a.get('vilom',[]),"vyakaran":a.get('vyakaran',[]),
              "estimated_exchanges":a['estimated_exchanges'],
              "depends_on":t['depends_on'],"source_topic_ids":[],
              "primary_content_type":t['primary_content_type'],
              "secondary_content_type":t['secondary_content_type'],
              "tertiary_content_type":t['tertiary_content_type'],
              "available_content_types":t['available_content_types'],
            }
            so['topics'].append({k:to[k] for k in TOPIC_ORDER})
        mo['segments'].append(so)
    plan['modules'].append(mo)

json.dump(plan,open(D+'13_merged.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print("root keys:",len(plan))
print("topics:",sum(len(s['topics']) for m in plan['modules'] for s in m['segments']))
# post-merge assertions
import re
oc_src={}
for m in base['modules']:
    for s in m['segments']:
        for t in s['topics']: oc_src[t['topic_id']]=t['original_chunk']
bad=0
for m in plan['modules']:
    for s in m['segments']:
        for t in s['topics']:
            if t['original_chunk']!=oc_src[t['topic_id']]: print("MERGE ERROR chunk mutated",t['topic_id']); bad+=1
            for lo in t['learning_objectives']:
                if lo['objective_text']!=objs[lo['objective_id']]['objective_text']: print("MIRROR MISMATCH",t['topic_id']); bad+=1
            for c in t['concepts']:
                for i,b2 in enumerate(c['content']):
                    if b2.get('type')=='paragraph' and 'publication_text' not in b2:
                        print("MISSING pub_text",c['concept_id'],i); bad+=1
for k in ['markers','source_lines_00_normalized','notes','cut_summary','reuse_report','severity']:
    if k in json.dumps(plan): print("WORKING FIELD LEAKED:",k); bad+=1
print("assertion failures:",bad)
