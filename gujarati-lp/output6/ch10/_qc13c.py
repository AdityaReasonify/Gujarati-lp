import json,os,re
D=os.path.dirname(os.path.abspath(__file__))
plan=json.load(open(os.path.join(D,'13_merged.json'),encoding='utf-8'))
topics=[t for m in plan['modules'] for s in m['segments'] for t in s['topics']]
def fields(t):
    o=[('explanation',t['explanation']),('real_life_example',t['real_life_example']),
       ('brief_summary',t['brief_summary']),('summary',t['summary']),('detailed_summary',t['detailed_summary']),
       ('topic_name',t['topic_name']),('publication_text',t['publication_text'])]
    for k in ('concept_bullets','important_points','key_terms'):
        for i,x in enumerate(t.get(k) or []): o.append((f'{k}[{i}]',x))
    for r in t['recall_questions']: o.append((r['id']+'.prompt',r['prompt'])); o.append((r['id']+'.answer',r['answer']))
    for c in t['concepts']:
        o.append((c['concept_id']+'.name',c['concept_name']))
        for kt in c.get('key_terms') or []: o.append((c['concept_id']+'.kt',kt))
        for i,b in enumerate(c['content']):
            if b.get('type')=='paragraph':
                o.append((f'{c["concept_id"]}.c{i}',b.get('text','')))
                if b.get('publication_text'): o.append((f'{c["concept_id"]}.c{i}.pub',b['publication_text']))
            for j,it in enumerate(b.get('items') or []): o.append((f'{c["concept_id"]}.c{i}[{j}]',it))
    return o
F=[]
# group-trait / caste words (hard 1, 18)
BAD=['વાણિયાઓ','વેપારીઓ','કંજૂસ','બીકણ','હિસાબી','જ્ઞાતિ','જાતિનો']
for t in topics:
    for k,s in fields(t):
        for b in BAD:
            if b in s: F.append(f"HARD-1/18 {t['topic_id']}.{k}: group-trait word {b!r}")
# printed-form preservation: repaired forms must not appear anywhere
REPAIR={'ચડ્યો':'ચડિયો','અરે':'અલ્યા','કંઈક':'કાંક','જવું હતું':"જાવું'તું",'નહીં':'નહિ','દેડકી':'ડેડકડી'}
for t in topics:
    for k,s in fields(t):
        for bad,good in REPAIR.items():
            for m in re.finditer(r"'[^']*'",s):
                if bad in m.group(0): F.append(f"MODERNISED {t['topic_id']}.{k}: {bad!r} inside a quotation (printed: {good})")
# reveal/spoiler gate: no topic before T12 names the tally
SPOIL=['કાટલાં','ચાર કાટલાં','દશ થાય','હિંમત અને વિશ્વાસ','બે હાથ','બે પાય']
order=[t['topic_id'] for t in topics]
for t in topics:
    if t['topic_id']=='M3.S6.T12': continue
    for k,s in fields(t):
        for sp in SPOIL:
            if sp in s and t['topic_id']!='M2.S4.T7': F.append(f"SPOILER {t['topic_id']}.{k}: {sp!r}")
# no gram/kilo value for કાટલાં
for t in topics:
    for k,s in fields(t):
        if re.search(r'(ગ્રામ|કિલો|કિ\.ગ્રા)',s): F.append(f"HARD-32 {t['topic_id']}.{k}: weight value stated")
# intro-box words must not appear in teaching
BOX=['વણિક','ઝઝૂમી','બુદ્ધિપૂર્વક']
for t in topics:
    for k,s in fields(t):
        for b in BOX:
            if b in s: F.append(f"CHAPTER-LEVEL {t['topic_id']}.{k}: intro-box word {b!r}")
# 'રોકાણ' must not be quoted as a poem word
for t in topics:
    for k,s in fields(t):
        if 'રોકાણ' in s: F.append(f"CHAPTER-LEVEL {t['topic_id']}.{k}: 'રોકાણ' (in શબ્દાર્થ box, in no printed line)")
# કાવ્યસ્વાતંત્ર્ય not used at std 6
for t in topics:
    for k,s in fields(t):
        if 'કાવ્યસ્વાતંત્ર્ય' in s: F.append(f"CHAPTER-LEVEL {t['topic_id']}.{k}: 'કાવ્યસ્વાતંત્ર્ય' at std 6")
# unresolved-until-T12 gate: 'સાથી મારે બાર' meaning not given early
for t in topics[:11]:
    for k,s in fields(t):
        if re.search(r'બાર સાથી (એટલે|એ)\s',s) or 'બાર સાથી કોણ છે તે' in s: F.append(f"REVEAL {t['topic_id']}.{k}")
print('\n'.join(F) if F else 'no findings')
