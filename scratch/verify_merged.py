# -*- coding: utf-8 -*-
import json,re
D="/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch02/"
d=json.load(open(D+'13_merged.json',encoding='utf-8'))
meta=json.load(open(D+'01_meta.json',encoding='utf-8'))
F=[]
DEV=re.compile(r'[ऀ-ॿ]'); ROM=re.compile(r'[A-Za-z]'); DIG=re.compile(r'[0-9૦-૯]')
GU=re.compile(r'[઀-૿]')
sb=lambda s: re.sub(r'\([^)]*\)','',s or '')
topics=[t for m in d['modules'] for s in m['segments'] for t in s['topics']]
objs={o['objective_id']:o for o in d['objectives']}
ids=set(); cids=[]
def wcl(s): return len([x for x in re.split(r'\s+',(s or '').strip()) if GU.search(x) or re.search(r'\w',x)])
for m in d['modules']:
    ids.add(m['module_id'])
    for s in m['segments']:
        ids.add(s['segment_id'])
        for t in s['topics']:
            ids.add(t['topic_id'])
            for c in t['concepts']: ids.add(c['concept_id']); cids.append(c['concept_id'])
# 1 phase/plan/chapter ids
assert d['phase']==2
if d['plan_id']!=f"{d['chapter_id']}_v{d['version']}": F.append(('CONTRACT-1','A1','plan_id'))
if d['chapter_id']!=f"gseb_eng_gujarati{d['grade']}_ch{d['unit_number']}": F.append(('CONTRACT-1','A1','chapter_id'))
for t in topics:
    oc=t['original_chunk']
    if not oc.strip() or not GU.search(oc): F.append(('CONTRACT-2','A5',t['topic_id']+' chunk'))
    if DEV.search(sb(oc)) or ROM.search(sb(oc)) or '।' in oc: F.append(('CONTRACT-2','A5',t['topic_id']+' script'))
    if not t['concepts']: F.append(('CONTRACT-3','A2',t['topic_id']))
    for c in t['concepts']:
        if c['objective_id'] not in objs or not c['content']: F.append(('CONTRACT-3','A2',c['concept_id']))
    for lo in t['learning_objectives']:
        if lo['objective_text']!=objs[lo['objective_id']]['objective_text']: F.append(('CONTRACT-5','A2',t['topic_id']))
        if 'image_examples' not in lo: F.append(('CONTRACT-5','A2',t['topic_id']+' no image_examples'))
    for i,r in enumerate(t['recall_questions'],1):
        if r['id']!=f"{t['topic_id']}.RQ{i}" or r['legacy_id']!=f"{t['topic_id']}.TR{i}": F.append(('CONTRACT-6','A12',r['id']))
    for n in t['media']:
        if not re.match(r'^M\d+\.S\d+\.T\d+\.C\d+\.(IMG|VID|2D|3D|SIM)\d+$',n['id']): F.append(('CONTRACT-6','A9',n['id']))
        if n['concept_id'] not in ids: F.append(('CONTRACT-12','A9',n['id']))
        if n['image_url']!='' or not n['generation_prompt'].strip(): F.append(('CONTRACT-10','A9',n['id']))
    b,s2,dd=[wcl(t[k]) for k in ['brief_summary','summary','detailed_summary']]
    if not (b<s2<dd): F.append(('CONTRACT-8','A12',t['topic_id']+f' {b}/{s2}/{dd}'))
    if t['figures_of_speech']:
        for fo in t['figures_of_speech']:
            if fo['lines'] not in t['original_chunk']: F.append(('CONTRACT-11','A7/A12',t['topic_id']))
    for k in ['topic_name','explanation','real_life_example','brief_summary','summary','detailed_summary','publication_text']:
        if DIG.search(t[k] or ''): F.append(('CONTRACT-9','A12',f"{t['topic_id']}.{k}"))
    for k in ['concept_bullets','important_points']:
        for x in t[k]:
            if DIG.search(x): F.append(('CONTRACT-9','A12',f"{t['topic_id']}.{k}"))
    for r in t['recall_questions']:
        if DIG.search(r['prompt']) or DIG.search(r['answer']): F.append(('CONTRACT-9','A12',r['id']))
    for c in t['concepts']:
        for bl in c['content']:
            if DIG.search(bl.get('text','') or ''): F.append(('CONTRACT-9','A12',c['concept_id']))
            for it in bl.get('items',[]) or []:
                if DIG.search(it): F.append(('CONTRACT-9','A12',c['concept_id']+' item'))
            if DIG.search(bl.get('publication_text','') or ''): F.append(('CONTRACT-9','A16',c['concept_id']+' pub'))
    if not (55<=wcl(t['explanation'])<=90): F.append(('C-band','A12',f"{t['topic_id']} exp {wcl(t['explanation'])}"))
    if not (55<=wcl(t['real_life_example'])<=90): F.append(('C-band','A12',f"{t['topic_id']} rle {wcl(t['real_life_example'])}"))
    if t['topic_type'] not in ('POEM','STORY_TELLING','CONCEPT','REVIEW'): F.append(('ENUM','A2',t['topic_id']))
    if t['2d_tool'] is not None: F.append(('MEDIA','A9','2d_tool set'))
for o in d['objectives']:
    if o['home_topic_id'] not in ids: F.append(('CONTRACT-4','A2',o['objective_id']))
    for an in o['anchor']:
        if an not in ids: F.append(('CONTRACT-4','A2',o['objective_id']))
    if o['legacy_id'] not in d['strand_to_objective_map']: F.append(('CONTRACT-4','A2',o['legacy_id']))
    if not (12<=wcl(o['objective_text'])<=30): F.append(('C-band','A12',f"{o['objective_id']} {wcl(o['objective_text'])}"))
    if DIG.search(o['objective_text']): F.append(('CONTRACT-9','A12',o['objective_id']))
if [int(c.split('.C')[1]) for c in cids]!=list(range(1,len(cids)+1)): F.append(('CONTRACT-6','A2','concept counter'))
if d['publication_id'] is None: F.append(('CONTRACT','A13','publication_id null'))
print("MERGED-FILE FAILURES:",len(F))
for x in F: print("  ",x)
print("topics:",len(topics),"objectives:",len(d['objectives']),"concepts:",len(cids),
      "media:",sum(len(t['media']) for t in topics))
