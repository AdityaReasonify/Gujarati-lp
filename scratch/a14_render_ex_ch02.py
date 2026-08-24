# -*- coding: utf-8 -*-
import json, io, os, shutil, collections

D = '/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch02'
src = os.path.join(D, '10_exercise_solutions.json')
dst = os.path.join(D, 'exercise_solutions.json')
shutil.copyfile(src, dst)

d = json.load(open(dst), object_pairs_hook=collections.OrderedDict)
ex = d['exercises']
cov = d['coverage_report']

# consecutive runs of exercise_group == the printed blocks, in printed order
runs = []
for e in ex:
    if not runs or runs[-1]['group'] != e['exercise_group']:
        runs.append({'group': e['exercise_group'], 'items': []})
    runs[-1]['items'].append(e)

found = cov.get('blocks_found', [])
if len(found) == len(runs):
    for r, h in zip(runs, found):
        r['heading'] = h
else:
    for r in runs:
        r['heading'] = None

o = []
w = o.append
w('# સ્વાધ્યાય — ઉકેલ')
w('')
w('**પાઠ:** %s  ' % d['chapter_name'])
w('**વિષય:** %s · **ધોરણ:** %s  ' % (d['subject'], d['grade']))
w('**chapter_id:** `%s` · **plan_id:** `%s`' % (d['chapter_id'], d['plan_id']))
w('')
w('> આ પાઠના છાપેલા દરેક સ્વાધ્યાય-બ્લોકના ઉકેલ અહીં જ છે. સ્વાધ્યાય કદી teaching topic નથી —')
w('> `learning_plan_logical.json` તેને ભણાવતું નથી, આ ફાઇલ તેને ઉકેલે છે.')
w('')
w('## અનુક્રમ')
w('')
for r in runs:
    w('- %s — %d' % ((r['heading'] or r['group']).replace('\n', ' '), len(r['items'])))
w('')

for r in runs:
    w('---')
    w('')
    w('## %s' % (r['heading'] or r['group']).replace('\n', ' '))
    w('')
    w('*ખંડ-પ્રકાર: %s*' % r['group'])
    w('')
    for e in r['items']:
        w('### `%s` · %s' % (e['exercise_id'], e['skill']))
        w('')
        w('**પ્રશ્ન (છપાયેલો):**')
        w('')
        for ln in e['prompt_verbatim'].split('\n'):
            w('> %s' % ln)
        w('')
        w('**ઉત્તર:**')
        w('')
        for ln in str(e['answer']).split('\n'):
            w(ln)
        w('')
        if e.get('values_filled_for_teaching'):
            w('**ભરેલી જગ્યાઓ / કોષ્ટક:**')
            w('')
            v = e['values_filled_for_teaching']
            if isinstance(v, list):
                for it in v:
                    w('- %s' % it)
            else:
                for ln in str(v).split('\n'):
                    w(ln)
            w('')
        if e.get('explanation'):
            w('**સમજૂતી:** %s' % e['explanation'].replace('\n', ' '))
            w('')
        if e.get('acceptable_alternatives'):
            w('**બીજા સ્વીકાર્ય ઉત્તર:**')
            w('')
            for a in e['acceptable_alternatives']:
                w('- %s' % str(a).replace('\n', ' '))
            w('')
        if e.get('is_model_answer'):
            w('*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*')
            w('')
        if e.get('teacher_note'):
            w('**શિક્ષક માટે:** %s' % e['teacher_note'].replace('\n', ' '))
            w('')
        if e.get('covered_by_topics'):
            w('**તૈયારી કરાવતાં topics:** %s' % ', '.join('`%s`' % x for x in e['covered_by_topics']))
            w('')

w('---')
w('')
w('## Coverage report')
w('')
w('| | |')
w('|---|---|')
w('| છપાયેલા બ્લોક મળ્યા | %d |' % len(cov.get('blocks_found', [])))
w('| ઉકેલાયેલા બ્લોક | %d |' % len(cov.get('blocks_answered', [])))
w('| કુલ entries | %d |' % len(ex))
w('| બાકી (unanswered) | %s |' % (', '.join(cov['unanswered']) if cov.get('unanswered') else '—'))
w('| મેપ ન થયેલા (unmapped) | %s |' % (', '.join(cov['unmapped']) if cov.get('unmapped') else '—'))
w('')
w('**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**')
w('')
for b in cov.get('blocks_found', []):
    w('- %s' % b.replace('\n', ' '))
w('')
if cov.get('_note'):
    w('**નોંધ:** %s' % cov['_note'].replace('\n', ' '))
    w('')

md = '\n'.join(o).rstrip() + '\n'
with io.open(os.path.join(D, 'exercise_solutions.md'), 'w', encoding='utf-8') as f:
    f.write(md)
print('exercises:', len(ex), 'blocks:', len(runs), 'md bytes:', len(md.encode('utf-8')))
