#!/usr/bin/env python3
"""Render exercise_solutions.json -> exercise_solutions.md (teacher-facing)."""
import json, os, collections

D = os.path.dirname(os.path.abspath(__file__))
p = lambda n: os.path.join(D, n)
d = json.load(open(p('exercise_solutions.json'), encoding='utf-8'))

L = []
w = L.append
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
counts = collections.Counter(e['exercise_group'] for e in d['exercises'])
for g in d['coverage_report']['blocks_found']:
    w('- %s — %d' % (g, counts.get(g, 0)))
w('')
w('---')
w('')

last = None
for e in d['exercises']:
    g = e['exercise_group']
    if g != last:
        w('## %s' % g)
        w('')
        last = g
    w('### `%s` · %s' % (e['exercise_id'], e['skill']))
    w('')
    w('**પ્રશ્ન (છપાયેલો):**')
    w('')
    for ln in (e.get('prompt_verbatim') or '').split('\n'):
        w('> %s' % ln if ln.strip() else '>')
    w('')
    w('**ઉત્તર:**')
    w('')
    w(e.get('answer') or '')
    w('')
    if (e.get('values_filled_for_teaching') or '').strip():
        w('**ભરેલી જગ્યાઓ / કોષ્ટક:**')
        w('')
        w(e['values_filled_for_teaching'])
        w('')
    if (e.get('explanation') or '').strip():
        w('**સમજૂતી:** %s' % e['explanation'])
        w('')
    alts = [a for a in (e.get('acceptable_alternatives') or []) if str(a).strip()]
    if alts:
        w('**બીજા સ્વીકાર્ય ઉત્તર:**')
        w('')
        for a in alts:
            w('- %s' % a)
        w('')
    if e.get('is_model_answer'):
        w('*(નમૂનારૂપ ઉત્તર — એક શક્ય જવાબ, એકમાત્ર જવાબ નહિ.)*')
        w('')
    if (e.get('teacher_note') or '').strip():
        w('**શિક્ષક માટે:** %s' % e['teacher_note'])
        w('')
    cov = e.get('covered_by_topics') or []
    if cov:
        w('**તૈયારી કરાવતાં topics:** %s' % ', '.join('`%s`' % c for c in cov))
        w('')
    w('---')
    w('')

cr = d['coverage_report']
w('## Coverage report')
w('')
w('| | |')
w('|---|---|')
w('| છપાયેલા બ્લોક મળ્યા | %d |' % len(cr['blocks_found']))
w('| ઉકેલાયેલા બ્લોક | %d |' % len(cr['blocks_answered']))
w('| કુલ entries | %d |' % len(d['exercises']))
def _flat(xs):
    """unanswered/unmapped may hold plain block names or {exercise_ids, exercise_group, reason}."""
    out = []
    for x in xs or []:
        if isinstance(x, dict):
            ids = ', '.join(x.get('exercise_ids') or [])
            out.append('%s (%s)' % (x.get('exercise_group', ''), ids) if ids
                       else str(x.get('exercise_group', '')))
        else:
            out.append(str(x))
    return out

unans, unmap = _flat(cr['unanswered']), _flat(cr['unmapped'])
w('| બાકી (unanswered) | %s |' % (str(len(unans)) if unans else '—'))
w('| મેપ ન થયેલા (unmapped) | %s |' % (str(len(unmap)) if unmap else '—'))
w('')
w('**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**')
w('')
for b in cr['blocks_found']:
    w('- %s' % b)
w('')
if unans:
    w('**બાકી રહેલા બ્લોક:**')
    w('')
    for x in unans:
        w('- %s' % x)
    w('')
if cr['unmapped']:
    w('**મેપ ન થયેલા items — નોંધ્યા છે, બનાવટી મેપિંગ કર્યું નથી:**')
    w('')
    for x in cr['unmapped']:
        if isinstance(x, dict):
            w('- **%s** — `%s`' % (x.get('exercise_group', ''),
                                   '`, `'.join(x.get('exercise_ids') or [])))
            if x.get('reason'):
                w('  - %s' % x['reason'])
        else:
            w('- %s' % x)
    w('')
if cr.get('_note'):
    w('**નોંધ:** %s' % cr['_note'])
    w('')

open(p('exercise_solutions.md'), 'w', encoding='utf-8').write('\n'.join(L))
print('wrote exercise_solutions.md  (%d exercises, %d lines)' % (len(d['exercises']), len(L)))
