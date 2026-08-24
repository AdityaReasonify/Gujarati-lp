# -*- coding: utf-8 -*-
import json, io, collections

parts = {}
for p in 'abcd':
    parts.update(json.load(io.open('/Users/aditya/Downloads/Gujarati-lp/scratch/part_%s.json'%p, encoding='utf-8')))

# typo fix in T2 correction
parts["M1.S1.T2"]["correction"] = parts["M1.S1.T2"]["correction"].replace("અેટલે","એટલે")

conv = json.load(io.open('/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch03/04_converged.json', encoding='utf-8'))
order = []
for m in conv['modules']:
    for s in m['segments']:
        for t in s['topics']:
            order.append(t['topic_id'])

missing = [t for t in order if t not in parts]
extra = [t for t in parts if t not in order]
assert not missing and not extra, (missing, extra)

chapter_level = [
 "The blue પ્રવેશપેટી calls this `આ એક વીરરસભરી પૌરાણિક કથા છે.` — it is taught as a કથા from end to end. No field anywhere in the plan verifies, dates, debunks or science-checks any event in it, and no field turns the મહાભારત into a discussion about belief or a comparative-religion lesson (`varta` gate 5, `global_content_rules.md` §10).",
 "The author slot on printed p. 11 prints only `- સંકલિત`, and the chapter carries no કવિ-પરિચય or લેખક-પરિચય box. No field may name an author, a compiler, a translator or a source text for this retelling — there is nothing printed to name (`no_hallucination_policy.md` §3).",
 "Both the writer of this plan and the child in the room already know the મહાભારત from television. Nothing outside the thirteen `original_chunk`s may enter: no seven-કોઠા count, no જયદ્રથનું વરદાન, no અર્જુનની પ્રતિજ્ઞા, no ઉત્તરા or પરીક્ષિત, no ગીતાનો ઉપદેશ, and no ending beyond યુધિષ્ઠિરના વાક્ય.",
 "The chapter runs on તત્સમ war-and-ritual vocabulary (`શિરસ્ત્રાણ`, `બાણશય્યા`, `વીરગતિ`, `ભગિની`, `પિતામહ`, `પ્રતિષ્ઠા`) and on જોડાક્ષર-dense proper names (`ધૃષ્ટદ્યુમ્ન`, `અશ્વત્થામા`, `કૃતવર્મા`, `ચક્રવ્યૂહ`) — the standing L2 hazard here. The printed શબ્દાર્થ box on p. 14 already glosses twenty-one of these words; use the book's own gloss wherever it exists rather than authoring a new one.",
 "All four printed રૂઢિપ્રયોગ in this chapter are figures that yield a plausible wrong sentence when read literally, and each one sits in a different topic: `પલ્લું ભારે થવું` (M2.S3.T6), `નેવે મૂકવું` and `યોજના ધૂળમાં મળવી` (M3.S6.T12), `આંખો મીંચી દેવી` (M3.S6.T13). Each is glossed in the topic where it occurs, in the book's own printed words.",
 "Std-7 ceiling: no અલંકાર, છંદ, રસ or સાહિત્યપ્રકાર label reaches the child anywhere in this plan. `વીરરસ` is printed only in the teacher-addressed પ્રવેશપેટી and stays there; the plan shows the પરાક્રમ and lets the child feel it unnamed (`profiles/students/std-7.md` §2, genre gate for std 6–8).",
 "The hero is killed on the page (printed p. 14) and a printed exercise sends the child to elders for the revenge story. Teach the ઘટના and the નિયમભંગ as the chapter tells them; the revenge frame never becomes a topic's lesson and never enters an `explanation`, a `concept_bullets` line or a `recall_questions[].answer` — it belongs to `exercise_solutions.json` alone."
]

out = collections.OrderedDict()
out["topics"] = [collections.OrderedDict([("topic_id", tid),
                                          ("avoid_checks", parts[tid]["avoid_checks"]),
                                          ("misconception", parts[tid]["misconception"]),
                                          ("correction", parts[tid]["correction"])]) for tid in order]
out["chapter_level"] = chapter_level

path = '/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch03/07_pitfalls.json'
with io.open(path,'w',encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write(u'\n')

# report
hard = sum(1 for t in out["topics"] for c in t["avoid_checks"] if c["severity"]=="hard")
soft = sum(1 for t in out["topics"] for c in t["avoid_checks"] if c["severity"]=="soft")
print('topics', len(out["topics"]), 'hard', hard, 'soft', soft, 'chapter_level', len(chapter_level))
for t in out["topics"]:
    assert all(c["profile"]=="varta" for c in t["avoid_checks"])
    assert t["misconception"] and t["correction"]
print('validated; wrote', path)
