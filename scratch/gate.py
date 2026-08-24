import json,re
D='/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch07'
p=json.load(open(D+'/13_merged.json'))
ts=[t for m in p['modules'] for s in m['segments'] for t in s['topics']]
T={t['topic_id']:t for t in ts}
def fields(t):
    o=[t['explanation'],t['real_life_example'],t['brief_summary'],t['summary'],t['detailed_summary'],t['publication_text']]
    o+=t['concept_bullets']+t['important_points']
    o+=[q['prompt'] for q in t['recall_questions']]+[q['answer'] for q in t['recall_questions']]
    o+=[b['text'] for c in t['concepts'] for b in c['content'] if b['type']=='paragraph']
    o+=[b.get('publication_text','') for c in t['concepts'] for b in c['content'] if b['type']=='paragraph']
    o+=[i for c in t['concepts'] for b in c['content'] if b['type']=='list' for i in b['items']]
    o+=[t['topic_name']]+[c['concept_name'] for c in t['concepts']]
    o+=[t['rhyme_scheme'].get('note','') if t['rhyme_scheme'] else '']
    return [x for x in o if x]
ALL=[(t['topic_id'],x) for t in ts for x in fields(t)]
ALL+=[('M1.overall_rhyme_scheme',p['modules'][0]['overall_rhyme_scheme'])]
ALL+=[(o['objective_id'],o['objective_text']) for o in p['objectives']]

def hits(words,label):
    h=[(tid,wd,s[:90]) for tid,s in ALL for wd in words if wd in s]
    print(('FAIL' if h else 'ok  '),label, h[:6])

hits(['જોઈએ'],'slogan gate (જોઈએ)')
hits(['જીવાણુ','જંતુ','બૅક્ટેરિયા','બેક્ટેરિયા','વાઇરસ','વાયરસ','ચેપ','રોગપ્રતિકારક','મલેરિયા','ડેન્ગ્યુ'],'over-scientifying')
hits(['સરકાર','પક્ષ','યોજના','ઝુંબેશ','સેના','સરહદ','રાષ્ટ્રધ્વજ','તિરંગો','ધ્વજવંદન','વલ્લભભાઈ','પટેલ','સ્વચ્છ ભારત'],'political framing')
hits(['સજીવારોપણ','રૂપક','અતિશયોક્તિ','વર્ણાનુપ્રાસ','પુનરુક્તિ','ઉપમા','અનુપ્રાસ','માત્રામેળ','અલંકાર','છંદ','યમક','શ્લેષ'],'std-6 naming ceiling (અલંકાર/છંદ)')
hits(['કડી 1','કડી 2','કડી 3','કડી 4','કડી 5','કડી 6','ટેક 1','કડી ૧','કડી ૨'],'numbered કડી in display text')
hits(['સ્વચ્છતા ત્યાં પ્રભુતા'],'placard text quoted as verse')

# picture-before-feeling
def first_sent(s): return re.split(r'(?<=[.?!])\s',s.strip())[0]
req={'M1.S1.T1':['ઘર','આંગણ-શેરી','ઉકરડો','વાળઝૂડ'],
     'M1.S2.T3':['શહેર','ગામ','માખી-મચ્છર'],
     'M2.S3.T4':['મનથી','નિર્મળ','ઊંચ-નીચ','ભેદ','વેર-ઝેર']}
for tid,ws in req.items():
    fs=first_sent(T[tid]['explanation'])
    print(('ok  ' if any(w in fs for w in ws) else 'FAIL'),'picture-before-feeling',tid,'|',fs[:80])
# craft
craft={'M1.S1.T1':['કરીએ','રાખીએ','દઈએ','ચોખ્ખાઈના સરદાર અમે સહુ'],
       'M1.S1.T2':['ચકચક','ઝગમગ','ચક-ચક','ઝગ-મગ','તાં'],
       'M1.S2.T3':['થાશે','ફરશે','માખી-મચ્છર'],
       'M2.S3.T4':['રહીએ','ભૂલીએ','કરીએ','ઊંચ-નીચ','વેર-ઝેર'],
       'M2.S4.T5':['ચાલશે','લહેરાશે','થાશે','શે'],
       'M2.S4.T6':['ચોખ્ખાઈ આપણી','દેશભક્તિ','પ્રાણશક્તિ','ક્તિ']}
for tid,ws in craft.items():
    e=T[tid]['explanation']
    print(('ok  ' if any(w in e for w in ws) else 'FAIL'),'craft named',tid)
# modernisation: થશે must not be quoted as the poem's word
for tid,s in ALL:
    for m in re.finditer(r"'([^']*)'",s):
        if 'થશે' in m.group(1) and 'થાશે' not in m.group(1):
            print('CHECK quoted થશે',tid,m.group(1))
# poster test T6
t6=T['M2.S4.T6']; printed=['ચોખ્ખાઈ','દેશભક્તિ','પ્રાણશક્તિ','ઘર ઘર','પયગામ','સરદાર']
def last_sent(s):
    parts=[x for x in re.split(r'(?<=[.?!])\s',s.strip()) if x]; return parts[-1]
for lbl,s in [('explanation',t6['explanation']),('detailed_summary',t6['detailed_summary'])]+[(q['id'],q['answer']) for q in t6['recall_questions']]:
    ls=last_sent(s)
    print(('ok  ' if any(w in ls for w in printed) else 'FAIL'),'poster test',lbl,'|',ls[:70])
