import json,copy
D='/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch09/'
L=lambda f: json.load(open(D+f))
meta=L('01_meta.json'); base=L('05_with_content.json'); auth=L('12_authoring.json')
med=L('09_media.json'); pub=L('16_publication.json'); pages=L('11_pages.json')

A={t['topic_id']:t for t in auth['topics']}
AM={m['module_id']:m for m in auth['modules']}
P={t['topic_id']:t for t in pub['topics']}
MEDIA={}
for x in med['media']:
    y={k:v for k,v in x.items() if k!='topic_id'}
    MEDIA.setdefault(x['topic_id'],[]).append(y)
OBJ={o['objective_id']:o for o in base['objectives']}

TOPIC_KEYS=['media','2d_tool','summary','concepts','topic_id','key_terms','depends_on','difficulty',
 'topic_name','topic_type','word_count','explanation','brief_summary','objective_ids','modified_chunk',
 'original_chunk','topic_category','concept_bullets','detailed_summary','important_points',
 'publication_text','recall_questions','source_topic_ids','publication_chunk','real_life_example',
 'estimated_exchanges','learning_objectives','primary_content_type','tertiary_content_type',
 'secondary_content_type','available_content_types']
EXTRAS=['figures_of_speech','rhyme_scheme','shabdarth','samanarthi','vilom','vyakaran']

modules=[]
for m in base['modules']:
    mm={'module_id':m['module_id'],'module_name':m['module_name'],'segments':[]}
    am=AM.get(m['module_id'],{})
    mm['difficult_words']=am.get('difficult_words',[])
    mm['overall_rhyme_scheme']=am.get('overall_rhyme_scheme',None)
    for s in m['segments']:
        ss={'segment_id':s['segment_id'],'segment_name':s['segment_name'],'topics':[]}
        for t in s['topics']:
            tid=t['topic_id']; a=A[tid]; p=P[tid]
            out={}
            # concepts: base identity + authored content + publication_text by index
            acon={c['concept_id']:c for c in a.get('concepts',[])}
            cpub={}
            for e in p.get('concept_publication',[]):
                cpub.setdefault(e['concept_id'],{})[e['content_index']]=e['publication_text']
            concepts=[]
            for c in t['concepts']:
                cid=c['concept_id']
                content=copy.deepcopy(acon.get(cid,{}).get('content',[]))
                for i,blk in enumerate(content):
                    if blk.get('type')=='paragraph' and i in cpub.get(cid,{}):
                        blk['publication_text']=cpub[cid][i]
                concepts.append({'concept_id':cid,'concept_name':c['concept_name'],
                                 'objective_id':c['objective_id'],'key_terms':c.get('key_terms',[]),
                                 'content':content})
            lo=[]
            for oid in t['objective_ids']:
                o=copy.deepcopy(OBJ[oid]); o['image_examples']=[]; lo.append(o)
            vals={
              'media':MEDIA.get(tid,[]),
              '2d_tool':None,
              'summary':a['summary'],
              'concepts':concepts,
              'topic_id':tid,
              'key_terms':t['key_terms'],
              'depends_on':t.get('depends_on',[]),
              'difficulty':t['difficulty'],
              'topic_name':t['topic_name'],
              'topic_type':t['topic_type'],
              'word_count':t['word_count'],
              'explanation':a['explanation'],
              'brief_summary':a['brief_summary'],
              'objective_ids':t['objective_ids'],
              'modified_chunk':t['modified_chunk'],
              'original_chunk':t['original_chunk'],
              'topic_category':t['topic_category'],
              'concept_bullets':a['concept_bullets'],
              'detailed_summary':a['detailed_summary'],
              'important_points':a['important_points'],
              'publication_text':p['publication_text'],
              'recall_questions':a['recall_questions'],
              'source_topic_ids':t.get('source_topic_ids',[]),
              'publication_chunk':p['publication_chunk'],
              'real_life_example':a['real_life_example'],
              'estimated_exchanges':a['estimated_exchanges'],
              'learning_objectives':lo,
              'primary_content_type':t['primary_content_type'],
              'tertiary_content_type':t['tertiary_content_type'],
              'secondary_content_type':t['secondary_content_type'],
              'available_content_types':t['available_content_types'],
            }
            for k in TOPIC_KEYS: out[k]=vals[k]
            for k in EXTRAS:
                if k in a: out[k]=a[k]
            ss['topics'].append(out)
        mm['segments'].append(ss)
    modules.append(mm)

plan={
 'phase':2,
 'board':meta['board'],
 'subject':meta['subject'],
 'grade':meta['grade'],
 'level':meta['level'],
 'version':meta['version'],
 'chapter_id':meta['chapter_id'],
 'plan_id':meta['plan_id'],
 'author':'',
 '_activate':False,
 'medium_id':None,
 'subject_ref_id':None,
 'chapter_master_id':None,
 'publication_id':1,
 'estimated_time':1.5,
 'textbook':pages['textbook'],
 'textbook_url':pages['textbook_url'],
 'textbook_pages':pages['textbook_pages'],
 'unit_title':meta['unit_title'],
 'unit_number':meta['unit_number'],
 'topic_title':meta['chapter_name'],
 'topic_number':meta['topic_number'],
 'chapter_name':meta['chapter_name'],
 'genre':meta['genre'],
 'teaching_lens':meta['teaching_lens'],
 'guiding_question':meta['guiding_question'],
 'english_plan_id':None,
 'english_chapter_id':None,
 'objectives':base['objectives'],
 'strand_to_objective_map':base['strand_to_objective_map'],
 'modules':modules,
}
json.dump(plan,open(D+'13_merged.json','w'),ensure_ascii=False,indent=2)
print('root keys',len(plan))
print(sorted(plan.keys()))
tk=set()
for m in plan['modules']:
    for s in m['segments']:
        for t in s['topics']: tk|=set(t.keys())
print('topic keys union',sorted(tk))
print('topics',sum(len(s['topics']) for m in plan['modules'] for s in m['segments']))
print('media total',sum(len(t['media']) for m in plan['modules'] for s in m['segments'] for t in s['topics']))
