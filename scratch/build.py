# -*- coding: utf-8 -*-
import json, re, sys, os
HERE = "/Users/aditya/Downloads/Gujarati-lp/scratch"
sys.path.insert(0, HERE)
import part_a, part_b, part_c

T = {}
T.update(part_a.T); T.update(part_b.T); T.update(part_c.T)

SRC = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch15/05_with_content.json"
src = json.load(open(SRC))

order, chunks, concept_order = [], {}, {}
for m in src["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            order.append(t["topic_id"])
            chunks[t["topic_id"]] = t["original_chunk"]
            concept_order[t["topic_id"]] = [c["concept_id"] for c in t["concepts"]]

assert set(order) == set(T), (set(order) ^ set(T))

topics = []
for tid in order:
    v = T[tid]
    cons = []
    for cid in concept_order[tid]:
        blocks = v["concepts"][cid]
        content = []
        for kind, payload in blocks:
            if kind == "paragraph":
                content.append({"type": "paragraph", "text": payload})
            else:
                content.append({"type": "list", "items": payload})
        cons.append({"concept_id": cid, "content": content})
    rqs = []
    for i, (p, a, d, b) in enumerate(v["rq"], 1):
        rqs.append({"id": f"{tid}.RQ{i}", "legacy_id": f"{tid}.TR{i}",
                    "prompt": p, "answer": a, "difficulty": d, "bloom_level": b})
    topics.append({
        "topic_id": tid,
        "explanation": v["explanation"],
        "real_life_example": v["rle"],
        "brief_summary": v["brief"],
        "summary": v["summary"],
        "detailed_summary": v["detailed"],
        "concept_bullets": v["bullets"],
        "important_points": v["points"],
        "concepts": cons,
        "recall_questions": rqs,
        "estimated_exchanges": v["ex"],
        "shabdarth": [{"shabd": a, "arth": b, "prakar": c} for a, b, c in v["shabdarth"]],
        "samanarthi": [{"shabd": a, "samanarthi": b} for a, b in v["samanarthi"]],
        "vilom": [{"shabd": a, "vilom": b} for a, b in v["vilom"]],
        "vyakaran": [{"bindu": a, "udaharan": b, "note": c} for a, b, c in v["vyakaran"]],
        "figures_of_speech": [],
        "rhyme_scheme": None,
    })

modules = [{"module_id": mid,
            "difficult_words": [{"word": w, "meaning": mn, "example": ex} for w, mn, ex in dws],
            "overall_rhyme_scheme": None} for mid, dws in part_c.MODULES]

NOTES = [
 "Authored at tier ધોરણ (the run's default) for std 6. The std-6 + ધોરણ descriptor block — REGISTER (≤10–12 word sentences, at most one subordinate clause), QUESTIONING (literal wh- → why on stated content → prediction → reflection), PACING (≤4 new interacting elements, one new element per sentence) and the two std-6 ceilings (no craft labels; no theme extraction / no psychological metaphor) — was re-stated block by block, per profiles/students/std-6.md §5.2. Difficulty is pinned per block, not per session.",
 "CONTEXT ROUTING GAP, worked around rather than guessed at. The run context supplied no_hallucination_policy.md, global_content_rules.md, author.md, teaching_voice_gu.md, gujarat_cultural_anchors.md and field_shape_rules.md, but the agent spec also requires reference/teaching_block_format.md, reference/alankar_chhand.md, reference/shabd_gloss.md and reference/bhasha_bodh.md, plus profiles/students/std-6.md. All five exist in the pack and were read IN FULL from disk before authoring; nothing was inferred from their titles. Flagging the routing gap so the orchestrator can widen the bundle for Agent 12.",
 "GENRE GATES OBEYED (nibandh_atmaparak.md, Avoid 1–15). Every explanation opens with પાલુબેન as the grammatical subject of its first sentence, so no topic presents her day as unattributed fact (gate 1). No field asks or answers why a પાત્ર acted, and no વળાંક of plot is named (gate 2). No explanation, summary, bullet or recall answer closes on ‘આ પાઠ આપણને શીખવે છે…’ / ‘આપણે પણ … જોઈએ’ (gate 3). This chapter is not routed to the હાસ્ય sub-form, so gates 4–5 do not bite; nothing is labelled વ્યંગ or કટાક્ષ anywhere (also 07_pitfalls M2.S3.T7). No printed spoken form is corrected — દા’ડો, કો’કવાર, હારુ, ઘરાક, બોણી, વઢ, ટાઢો, બચુડિયાં, આયખું, ઢસરડા all stand as printed and are glossed with the printed form as headword (gate 7). No thought, motive or life-fact is attributed to any real named person beyond the page (gate 8). No proper noun, measure or number appears that is not in an original_chunk or the printed શબ્દાર્થ box (gate 9). Nothing is described as બિચારાં / ગરીબ / લાચાર / ‘આ લોકો’ (gate 14). figures_of_speech is [] on every topic (gate 15).",
 "PITFALL CORRECTIONS ARE PERFORMED IN THE FIELD EACH CHECK NAMES. M1.S1.T1 — the explanation states in its own words that ‘પાલુબેન વશરામભાઈ’ is one speaker's whole name, and NO field says whose name વશરામભાઈ is; the repetition ‘કામ, કામ ને કામ’ is never called દ્વિરુક્ત, પુનરુક્તિ or any device (the one દ્વિરુક્ત entry in this chapter is on ‘વાતવાતમાં’ at M4.S5.T11, a different word). M1.S1.T2 — ‘પેટનો ખાડો પૂરવો’ is glossed with the book's own printed meaning. M2.S2.T3 — ‘ઘરવાળા’ is glossed as (અહીં) પતિ, one person, not the whole household. M2.S2.T4 — મણ is glossed only as ‘વજન કરવાનું જૂનું માપ’; no kilo equivalent anywhere, and nothing is added about જમાપુર or દાણાપીઠ. M2.S3.T5 — ‘હાથમાં આવવું’ is restated as ‘મળવું’ beside the printed sentence. M2.S3.T6 — નાનકી is glossed as a name and the three children are counted from this chunk's own words; no reason for the worry is invented. M2.S3.T7 — ‘હારુ’ is glossed as ‘માટે’ at first use and the two printed sentences are put side by side. M3.S4.T8 — ‘દબાણ’ is glossed as ગેરકાયદે કબજો and the sentence is restated plainly. M3.S4.T9 — the ‘ ’ marks around ‘સેવા’ are pointed at as the signal that it is an organisation's name. M4.S5.T10 — આયખું and ઢસરડા are glossed and ‘પૂરું થયું’ is restated as ‘આટલાં વરસ વીતી ગયાં’, with the next printed sentence immediately following. M4.S5.T11 — the first sentence establishes that the closing words are પાલુબેનનાં and that પૃથાબેન is the listener.",
 "SENSITIVITY (08_sensitivity.json) applied as guidance, not censorship. M1.S1.T2 names both loads — the paid ધંધો and the ઘરકામ / ન્યાત duties — exactly as the paragraph does, with no rule about who ‘should’ do housework and no softening. M2.S2.T3's real_life_example deliberately says ‘ઘરમાં કોઈ’ rather than a mother, so the point stays her workload rather than a gender rule. M3.S4.T8 (severity hard) states no motive for the મ્યુનિસિપાલિટીવાળા, પોલીસ or દબાણ ખસેડવાવાળા, stages no villain, and its real_life_example carries the loss through a soaked notebook with no authority figure in it; no recall question asks the child to judge anyone. M3.S4.T9 keeps to the four printed things ‘સેવા’ did and adds no founding date, city or membership fact — and the printed Roman line is not reproduced anywhere, so it cannot be silently corrected. M4.S5.T10 keeps the night feeding as her own નિર્ધાર, with no pity register and no comment about anyone the paragraph does not name.",
 "SPELLING NOTE CARRIED FORWARD FROM AGENT 5, not silently resolved. The chapter prints ‘ઠૂસ’ (દીર્ઘ ૂ) in the body on folio 102 and ‘ઠુસ’ (હ્રસ્વ ુ) in the રૂઢિપ્રયોગ pre-block on folio 103; A5's original_chunk follows the printed body. Every field here that quotes the chunk uses the body form ‘ઠૂસ’, and the meaning given is the book's own printed one (‘ખૂબ જ થાકી જવું’). The pre-block's headword form is not reproduced, so neither printed spelling is presented as a correction of the other.",
 "ANCHOR LEDGER for real_life_example, kept as the chapter was authored (scene → bank domain → picture), per gujarat_cultural_anchors.md §3.4. T1 રોજિંદું જીવન / વર્ગમાં પહેલા દિવસનો પરિચય · T2 તહેવાર-ઉત્સવ / નવરાત્રિની મોડી રાત પછીની અધૂરી ઊંઘ · T3 ખાનપાન / પ્રવાસના દિવસે ભરાતો ડબ્બો · T4 રોજિંદું જીવન / રિસેસમાં નળ પાસેની દોડાદોડ · T5 કામ-આજીવિકા / એસ.ટી. બસના ડેપોએ વહેલા પહોંચવું · T6 રોજિંદું જીવન / શેરીની રમત ને નાના ભાઈ-બહેન પર જતી નજર · T7 ખાનપાન / ઈદની સેવૈયાની વાટકીમાંથી રાખી મૂકવું · T8 રોજિંદું જીવન / વરસાદમાં પલળેલી ચોપડી · T9 તહેવાર-ઉત્સવ / ઉત્તરાયણે ફિરકી પકડનાર · T10 ભૂગોળ-કુદરત / કૂંડામાં વાવેલા છોડને રાતે પાણી · T11 રોજિંદું જીવન / રમત સંકેલીને ‘કાલે પાછા’. No two consecutive scenes share a domain and no picture repeats; five of the bank's seven domains are used; more than one community's ઘર appears (ઈદની વાટકી as one lived moment, never a census sentence). Every anchor is one moment a std-6 child's own hands or ears were inside, and none needs its own gloss.",
 "STD-6 CEILINGS. No અલંકાર, છંદ, સમાસ, સંધિ, કૃદંત or નિપાત anywhere; figures_of_speech is [] and rhyme_scheme is null on all eleven topics (ગદ્ય), and overall_rhyme_scheme is null on all four modules. No field names the સાહિત્યપ્રકાર ‘આત્મકથનાત્મક નિબંધ’, નિબંધ, આત્મકથા or પ્રથમ પુરુષ as a label for the child. Every vyakaran bindu is inside the measured std-6 ladder (bhasha_bodh.md §Std 6): નામ, રૂઢિપ્રયોગ, ક્રિયાપદ, વચન, વિશેષણ, વાક્યના પ્રકારો, ઉપસર્ગ-પ્રત્યય, વિરામચિહ્નો, કાળ, દ્વિરુક્ત / રવાનુકારી શબ્દો — one entry per topic, as that file's std-6 row requires.",
 "MODULE difficult_words WAS AUTHORED EVEN THOUGH THIS IS ગદ્ય, and the decision is flagged for Agent 13. alankar_chhand.md treats difficult_words as a કાવ્ય extra that is [] for prose, while shabd_gloss.md and profiles/students/std-6.md §5.3 prescribe 6–8 module difficult_words per standard with no genre gate, as an L2 vocabulary field. The L2 reading gives the child more; the entries are 7/8/8/7, every word occurs in this chapter, every meaning is the sense this chapter uses, and every example sentence is fresh and everyday (never the chapter's own line). If Agent 13 reads the prose rule as binding, emptying these four arrays is safe and touches nothing else.",
 "EXERCISE BOUNDARY. No સ્વાધ્યાય block is answered here. Two topics name — in exactly one clause each, from 01_meta.json's exercise_inventory and never from a remembered list — the skill their block will ask for: M1.S1.T2 names finding sentences of the same meaning in the text (‘નીચેના જેવો અર્થ ધરાવતાં વાક્યો પાઠમાંથી શોધો.’) and M4.S5.T11 names writing someone else's દિનચર્યા (‘લારીમાં વસ્તુ વેચતા ફેરિયાની દિનચર્યા લખો.’). Neither clause describes HOW to write the form, and neither supplies an answer — profile Avoid gate 12 and the M2.S2.T3 / M4.S5.T11 pitfall checks. Recall prompts were also kept off the printed પ્રશ્નોત્તર wording wherever the printed question already covers the same ground.",
 "key_terms ARE AGENT 5's AND WERE NOT TOUCHED. They read correctly at 4–6 per topic, high in the 3–6 band as shabd_gloss.md prescribes for std 6, and every word that stops an L2 child in these chunks is covered. One observation, not a rewrite : M2.S3.T5's key_term for ‘હારુ’ at M2.S3.T7 explains the form via ‘સારુ’; 07_pitfalls' M2.S3.T7 check forbids offering a corrected form, so the glosses authored HERE (shabdarth, concept_bullets, inline) give only ‘હારુ — માટે’ without naming another spelling. Agent 13 may want to look at that one key_term string.",
 "objective_text was NOT rewritten anywhere; the eleven objectives in 05_with_content.json's registry are Agent 2's and read correctly for std 6 — they ask the child to find, list, order and explain the speaker's own printed words and name no craft term. No mismatch to route back to A2.",
 "No PNG render was opened. 00_chapter_normalized.md and 05_with_content.json's original_chunks answered every question this authoring needed; no layout or figure question arose.",
 "ONE DELIBERATE ‘જોઈએ’ IN CHILD-FACING TEXT, flagged so a mechanical scan does not misread it. M2.S3.T7's explanation quotes the chapter's own printed sentence ‘ટાઢો રોટલો પલાળવા કાંઈક જોઈએ ને !’ exactly as it stands in that topic's original_chunk. Profile Avoid gate 3 bars a closing rule-clause of the shape ‘આપણે પણ … જોઈએ’ that is NOT a verbatim quotation; this one is a verbatim quotation, it is mid-field rather than closing, and it is the speaker's own remark about her own breakfast. Every other ‘જોઈએ’ was rewritten out of the authored prose during drafting.",
 "Word bands measured before emit (whitespace tokens): explanation 70–88, real_life_example 60–68 — every field inside 55–90, sitting near the std-6 ધોરણ targets of ~60 and ~58. brief_summary < summary < detailed_summary strictly on all eleven topics. estimated_exchanges is a small integer as a string. tier and notes are working fields for Agent 13 to read and drop.",
]

out = {
    "agent": "12_runtime_authoring",
    "chapter_id": src["chapter_id"],
    "plan_id": src["plan_id"],
    "tier": "ધોરણ",
    "grade": 6,
    "topics": topics,
    "modules": modules,
    "notes": NOTES,
}

# ---------------- validation ----------------
errs, warns = [], []
DEV = re.compile(r"[ऀ-ॿ]")
ROM = re.compile(r"[A-Za-z]")
DIG = re.compile(r"[0-9]")

PROSE_KEYS = {"explanation","real_life_example","brief_summary","summary","detailed_summary",
              "concept_bullets","important_points","text","items","prompt","answer",
              "shabd","arth","samanarthi","vilom","bindu","udaharan","note",
              "word","meaning","example"}

def walk(o, path="", key=None):
    if isinstance(o, dict):
        for k, v2 in o.items(): yield from walk(v2, f"{path}.{k}", k)
    elif isinstance(o, list):
        for i, v2 in enumerate(o): yield from walk(v2, f"{path}[{i}]", key)
    elif isinstance(o, str):
        if key in PROSE_KEYS:
            yield path, o

BAD = ["જોઈએ", "આ પાઠ આપણને શીખવે", "બોધ એ છે", "બિચારાં", "બિચારી", "ગરીબ", "અભણ", "પછાત", "લાચાર", "આ લોકો",
       "અલંકાર", "છંદ", "સમાસ", "સંધિ", "કૃદંત", "નિપાત", "કટાક્ષ", "વ્યંગ", "સજીવારોપણ", "વર્ણાનુપ્રાસ",
       "આત્મકથા", "આત્મકથન", "પ્રથમ પુરુષ", "કેન્દ્રીય", "લેખિકા", "પુનરુક્તિ"]
for path, s in walk({"topics": topics, "modules": modules}):
    for b in BAD:
        if b in s: warns.append(f"BANNED '{b}' at {path}: {s[:80]}")

for t in topics:
    tid = t["topic_id"]
    for f, lo, hi in [("explanation", 55, 90), ("real_life_example", 55, 90)]:
        n = len(t[f].split())
        if not lo <= n <= hi: errs.append(f"{tid} {f} {n} out of band")
    b, sm, d = (len(t[x].split()) for x in ("brief_summary", "summary", "detailed_summary"))
    if not b < sm < d: errs.append(f"{tid} summaries not increasing {b}/{sm}/{d}")
    if not 3 <= len(t["concept_bullets"]) <= 4: errs.append(f"{tid} concept_bullets {len(t['concept_bullets'])}")
    if not 3 <= len(t["important_points"]) <= 4: errs.append(f"{tid} important_points {len(t['important_points'])}")
    if not 2 <= len(t["recall_questions"]) <= 3: errs.append(f"{tid} rq count")
    for rq in t["recall_questions"]:
        if rq["bloom_level"] != rq["bloom_level"].lower(): errs.append(f"{tid} bloom case")
        if rq["bloom_level"] not in {"remember","understand","apply","analyze","evaluate","create"}: errs.append(f"{tid} bloom vocab {rq['bloom_level']}")
        if rq["difficulty"] not in {"easy","medium","hard"}: errs.append(f"{tid} difficulty")
        if not rq["answer"].strip(): errs.append(f"{tid} empty answer")
    if not 3 <= len(t["shabdarth"]) <= 5: errs.append(f"{tid} shabdarth {len(t['shabdarth'])}")
    if len(t["samanarthi"]) > 2: errs.append(f"{tid} samanarthi {len(t['samanarthi'])}")
    if len(t["vilom"]) > 1: errs.append(f"{tid} vilom {len(t['vilom'])}")
    if len(t["vyakaran"]) != 1: errs.append(f"{tid} vyakaran {len(t['vyakaran'])}")
    if t["figures_of_speech"] != [] or t["rhyme_scheme"] is not None: errs.append(f"{tid} craft fields")
    # ભાષા-બોધ words must occur in this topic's chunk
    ch = chunks[tid]
    for e in t["shabdarth"]:
        head = e["shabd"].split()[0]
        if head not in ch: errs.append(f"{tid} shabdarth '{e['shabd']}' not in chunk")
    for e in t["samanarthi"]:
        if e["shabd"] not in ch: errs.append(f"{tid} samanarthi '{e['shabd']}' not in chunk")
    for e in t["vilom"]:
        if e["shabd"] not in ch: errs.append(f"{tid} vilom '{e['shabd']}' not in chunk")

BINDU_OK = {"નામ","સર્વનામ","વિશેષણ","ક્રિયાપદ","કાળ","વચન","જાતિ","રૂઢિપ્રયોગ","કહેવત","વિરામચિહ્નો",
            "જોડાક્ષર","ક્રિયાવિશેષણ","સંયોજક","વાક્યના પ્રકારો","ઉપસર્ગ-પ્રત્યય","દ્વિરુક્ત / રવાનુકારી શબ્દો",
            "શબ્દસમૂહ માટે એક શબ્દ","અનુસ્વાર","શબ્દકોશ ક્રમ"}
for t in topics:
    for e in t["vyakaran"]:
        if e["bindu"] not in BINDU_OK: errs.append(f"{t['topic_id']} bindu '{e['bindu']}' off-ladder")
PRAKAR_OK = {"તત્સમ","તદ્ભવ","દેશ્ય","આગત","કાવ્ય-રૂપ"}
for t in topics:
    for e in t["shabdarth"]:
        if e["prakar"] not in PRAKAR_OK: errs.append(f"{t['topic_id']} prakar {e['prakar']}")

for m in modules:
    n = len(m["difficult_words"])
    if not 5 <= n <= 10: errs.append(f"{m['module_id']} difficult_words {n}")

print("ERRORS:", len(errs))
for e in errs[:60]: print("  E", e)
print("WARNS:", len(warns))
for w in warns[:60]: print("  W", w)

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch15/12_authoring.json"
if not errs:
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("WROTE", OUT, os.path.getsize(OUT), "bytes")
else:
    print("NOT WRITTEN")
