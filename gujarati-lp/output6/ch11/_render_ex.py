#!/usr/bin/env python3
"""Render exercise_solutions.json -> exercise_solutions.md (teacher-facing).

ch11 variant: `blocks_found` carries the eighteen printed verbatim headings while
`exercises[].exercise_group` carries the pack's short label, so the index pairs the two
by printed position (18 blocks : 18 entries, one-to-one) instead of matching strings.
`coverage_report.unmapped` here is a list of {exercise_id, exercise_group, reason} objects.
"""
import json, os

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

blocks = d['coverage_report']['blocks_found']
exs = d['exercises']
paired = len(blocks) == len(exs)
w('| id | ખંડ | છપાયેલું શીર્ષક |')
w('|---|---|---|')
for i, e in enumerate(exs):
    head = blocks[i].replace('|', '\\|') if paired else '—'
    w('| `%s` | %s | %s |' % (e['exercise_id'], e['exercise_group'].replace('|', '\\|'), head))
if not paired:
    w('')
    w('*(છપાયેલાં શીર્ષક %d, ઉકેલ-entries %d — એક-એકનો મેળ બેસતો નથી; નીચે Coverage report જુઓ.)*'
      % (len(blocks), len(exs)))
w('')
w('---')
w('')

for e in exs:
    w('## `%s` · %s' % (e['exercise_id'], e['exercise_group']))
    w('')
    w('**કૌશલ્ય:** %s' % e.get('skill', '—'))
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
    else:
        w('**તૈયારી કરાવતાં topics:** — (કોઈ વાચન-દૃશ્ય આ ખંડને તૈયાર કરતું નથી; કારણ Coverage report માં)')
    w('')
    w('---')
    w('')

cr = d['coverage_report']


def _name(x):
    if isinstance(x, dict):
        return '%s (%s)' % (x.get('exercise_id', '?'), x.get('exercise_group', ''))
    return str(x)


w('## Coverage report')
w('')
w('| | |')
w('|---|---|')
w('| છપાયેલા બ્લોક મળ્યા | %d |' % len(cr['blocks_found']))
w('| ઉકેલાયેલા બ્લોક | %d |' % len(cr['blocks_answered']))
w('| કુલ entries | %d |' % len(exs))
w('| બાકી (unanswered) | %s |' %
  (', '.join(_name(x) for x in cr['unanswered']) if cr['unanswered'] else '—'))
w('| topic સાથે ન જોડાયેલા (unmapped) | %s |' %
  (', '.join(_name(x) for x in cr['unmapped']) if cr['unmapped'] else '—'))
w('')
w('**છપાયેલા બ્લોક, છપાયેલા ક્રમમાં:**')
w('')
for b in cr['blocks_found']:
    w('- %s' % b)
w('')
if cr.get('unmapped'):
    w('**topic સાથે ન જોડવાનું કારણ:**')
    w('')
    for x in cr['unmapped']:
        if isinstance(x, dict):
            w('- **`%s` · %s** — %s' % (x.get('exercise_id', '?'), x.get('exercise_group', ''),
                                        x.get('reason', '')))
        else:
            w('- %s' % x)
    w('')
if cr.get('_note'):
    w('**નોંધ:** %s' % cr['_note'])
    w('')

open(p('exercise_solutions.md'), 'w', encoding='utf-8').write('\n'.join(L))
print('wrote exercise_solutions.md  (%d exercises, %d lines)' % (len(exs), len(L)))
