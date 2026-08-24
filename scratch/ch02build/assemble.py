# -*- coding: utf-8 -*-
import sys, json, io
sys.path.insert(0, '/Users/aditya/Downloads/Gujarati-lp/scratch/ch02build')
from p1 import T1, T2, T3
from p2 import T4, T5
from p3 import T6, T7
from p4 import T8, T9, MODULES

TOPICS = [T1, T2, T3, T4, T5, T6, T7, T8, T9]

NOTES = [
 "Authored at tier ધોરણ (the run default) for std 7. The std-7 descriptor block from profiles/students/std-7.md — REGISTER (at most one subordinate clause), QUESTIONING (literal wh- → motive inference → prediction / in-character hypothetical), PACING (≤4 new interacting elements, one new element per sentence), GLOSSING (તળપદા and new words glossed inline in Gujarati) — plus the std-7 ceilings (no સ્વરૂપ label handed to the child, no અલંકાર/છંદ/સમાસ term) was re-injected for every topic, not once for the session. `tier` is recorded here as provenance only; it is a working field and never enters the plan.",
 "CONTEXT ROUTING GAP, recorded rather than guessed around: the run context supplied five policy documents (no_hallucination_policy.md, global_content_rules.md, author.md, teaching_voice_gu.md, gujarat_cultural_anchors.md). The agent spec additionally requires profiles/genres/varta.md, profiles/students/std-7.md, reference/teaching_block_format.md, reference/alankar_chhand.md, reference/shabd_gloss.md, reference/bhasha_bodh.md and reference/field_shape_rules.md. All seven exist in the repository and were read in full from their canonical paths; nothing was authored from memory of them. Flagging the mismatch between the run's routing list and the spec's input list for the orchestrator.",
 "ગદ્ય chapter (વાર્તા — the blue intro box calls it a ચાતુર્યકથા; that word is the teacher box's and is never handed to the child). Not one line of verse is printed in the unit (01_meta structure_inventory kadi/duha/pad = 0), so `rhyme_scheme` is null on all nine topics and `overall_rhyme_scheme` is null on all three modules. `figures_of_speech` is [] on all nine topics — that is both the ગદ્ય answer and the std 6–8 grade gate (alankar_chhand.md; std-7 profile §5.4 fixes it to [] at every tier). These are correct answers, not gaps.",
 "The word 'ઉપમા' appears in 08_sensitivity.json's guidance ('the girl's clever ઉપમા'). It is not used in any authored field: ઉપમા is a std-9 અલંકાર name and naming it at std 7 would break the craft ceiling. The same idea is carried in ordinary words — 'સામો સવાલ', 'સરખામણી', 'કરી બતાવવું', 'બાળાની રીત'. The sensitivity intent is fully honoured; only its label is avoided.",
 "Belief gate (07 chapter_level item 1 + 08 chapter_level ધર્મ): no field of any topic states that ભગવાન છે or નથી, compares faiths, or checks the three demonstrations against science. The દૂધ-માખણ chain, the દીવો-પ્રકાશ answer and the ઋતુચક્ર list are all reported as the answers the બાળા gives in the સભા. 08's own instruction for M2.S3.T6 was followed literally: `real_life_example` uses an everyday hidden-but-real thing (મીઠું dissolved in a cooking pot), not a religious parallel.",
 "જાતિ-ભૂમિકા gate (08 chapter_level): the girl is the active reasoner in every explanation, concept block and recall answer — she asks for the દૂધ and the દીવો, she puts the counter-question, she asks the સભા to swap seats. Nowhere is she 'a cute child who gave a sweet answer', and M3.S4.T9 seats her in the રાજસભા alongside her father as his equal.",
 "Speaker discipline (07 chapter_level items 2–3): every quoted line in the teaching names its speaker. Two attributions are load-bearing and are stated explicitly — 'પહેલો / બીજો / ત્રીજો' are the order of the questions and not three speakers (M1.S1.T3), and 'દીવાનો પ્રકાશ તો ચારે દિશામાં જ પડેને !' is spoken by મહારાજ, not by the બાળા (M2.S3.T7). One girl under six printed labels is handled by naming her plainly as the કવિની દીકરી / બાળા in the teaching prose while quoting the page's own words wherever the page is quoted.",
 "Spoiler ledger (varta avoid 4, climax = M2.S3.T6): દૂધ, માખણ, દીવો, પ્રકાશ, 'ચારે દિશામાં', સિંહાસન, પ્રધાનજી, અદલાબદલી, કવિબાળા, દીકરી and 'રાજસભામાં સામેલ' were machine-checked against every pre-climax field named in 07 (explanation, summary, detailed_summary, concept_bullets, recall answers, plus real_life_example for M1.S1.T1). Zero hits. દીકરી appears only from M1.S2.T4 onward, where the printed chunk introduces her, and never with a statement that she will answer.",
 "Anchor domain ledger, one line per scene (gujarat_cultural_anchors.md §3.4 rotation): T1 લોકકલા/તહેવાર — શેરીનો ગરબો, નવા માટે જગ્યા કરતું કૂંડાળું; T2 રોજિંદું જીવન (રમત) — શેરી ક્રિકેટ, 'બે બોલ નાખી બતાવ'; T3 ભૂગોળ-કુદરત — ચોમાસાની સાંજે વીજળી ને નાના ભાઈના ત્રણ સવાલ; T4 કામ-આજીવિકા — બજારના દરજી પાસે મુકાયેલું કપડું; T5 રોજિંદું જીવન (ઘર) — સાયકલની ઊતરેલી ચેઇન નાની બહેને ચડાવી; T6 ખાનપાન (રસોડું) — શાકમાં ઓગળેલું મીઠું; T7 રોજિંદું જીવન (શાળા) — એક ખૂણે લટકતો ઘંટ, અવાજ બધે; T8 કામ-આજીવિકા — ગામને પાદરે રોજ એક જ સમયે આવતી એસ.ટી. બસ; T9 રોજિંદું જીવન (ઘર) — સામેથી નાની બહેનનું નામ લેવું. No domain repeats adjacently, no picture repeats, only one festival anchor in nine, and every anchor is a moment with a before and an after in it (std-7.md §2's own test), not a place-description.",
 "Every anchor was delete-tested (§3.6) and every one is built of words a std-7 child already owns — no anchor needs its own gloss. Scope stays India; no anchor asserts a fact about the text, the poet or the chapter.",
 "Agent 5's `key_terms` were read and not touched: all nine topics carry 5–6 entries, inside the 3–6 band, and each list covers the words that actually stop the child in that chunk. No rewrite is requested. Inline glossing inside `explanation` runs at 2–3 per topic, the std-7 figure in shabd_gloss.md, and repeats the glossed word inside the same field or the concept blocks so the child meets it twice.",
 "`objective_text` was not written or altered by this agent; the registry in 05_with_content.json is intact and no objective looked wrong on reading.",
 "ભાષા-બોધ caps observed for std 7 (bhasha_bodh.md): shabdarth 4–5 per topic (never [] in this L2 pack), samanarthi 1–2, vilom 0–1 and empty on four topics where no honest opposite exists, vyakaran exactly one entry per topic. Every headword occurs in that topic's own `original_chunk` (verb entries appear there in inflected form — પારખી, વલોવાતી, સમાયો, સળગાવી, બિરાજશો, મૂંઝાયો). `bindu` values stay inside the std-7 ladder — વિરામચિહ્નો (this chapter's own chapter-final grammar box, so five topics feed it: પૂર્ણવિરામ, પ્રશ્નવિરામ, ઉદ્ગારચિહ્ન, અલ્પવિરામ, અવતરણચિહ્ન), નામ, કાળ, સર્વનામ, વાક્યના પ્રકારો. No સંધિ, સમાસ, કૃદંત, નિપાત or પ્રયોગ.",
 "Module `difficult_words` are authored even though this is ગદ્ય: field_shape_rules.md lists the field at module level without a genre restriction, and shabd_gloss.md's std-7 row asks for 6–8 per module. M1 has 8, M2 has 7, M3 has 8. Every `example` is a fresh everyday sentence written for this field — none is a line from the chapter.",
 "Exercise preparation (teaching_block_format.md 'gradual release'), using only headings printed in 01_meta's exercise_inventory: M1.S2.T5's explanation names the speaker-identification task ('નીચેનાં વાક્યો કોણ બોલ્યું હશે એ લખો.'), M2.S3.T6's names the process-writing task ('દૂધમાંથી માખણ બનવાની પ્રક્રિયા લખો.'), and M2.S3.T7's names the direction activity. The teaching sets the skill up; no exercise is answered here — that is Agent 10's deliverable.",
 "Field shapes measured before emitting, counting only whitespace-separated tokens that contain a Gujarati letter: `explanation` runs 79–89 words and `real_life_example` 60–74, all inside 55–90; brief < summary < detailed on every topic, at 1 / 2–3 / 4–6 sentences; concept_bullets and important_points 4 lines each; recall 2–3 per topic with ids {topic_id}.RQ{n} and legacy_id {topic_id}.TR{n}, lowercase bloom_level, every one with a real model answer.",
 "Recall ladder is the std-7 one and stops where the standard stops: remember → motive inference → (on the topics carrying the turn and the resolution) analyze. No unstated-theme question, no device-effect question, no abstract-proposition debate. 24 questions across nine topics (9 remember, 10 understand, 5 analyze).",
 "No render was opened. 00_chapter_normalized.md answered every question this agent had, including the flush-left speaker labels and the two uncaptioned court illustrations."
]

out = {
 "agent": "12_runtime_authoring",
 "chapter_id": "gseb_eng_gujarati7_ch2",
 "plan_id": "gseb_eng_gujarati7_ch2_v1",
 "tier": "ધોરણ",
 "grade": 7,
 "topics": TOPICS,
 "modules": MODULES,
 "notes": NOTES
}

path = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output7/ch02/12_authoring.json"
with io.open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("written", path)
