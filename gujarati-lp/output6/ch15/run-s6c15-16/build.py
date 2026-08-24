# -*- coding: utf-8 -*-
"""Agent 16 — publication authoring for std-6 ch-15 (લો, પાથરી મારી વાત).

publication_text  = the topic's teaching `explanation` with the classroom address removed.
publication_chunk = verbatim original_chunk (copied from 05_with_content.json, never retyped)
                    + publication_text + the reader-facing form of `real_life_example`.
concept_publication = one entry per `paragraph` block of 12_authoring.json concepts[].content[],
                    in Agent 12's own order, with that block's own index.
"""
import json, os, unicodedata

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch15"

with open(os.path.join(OUT, "05_with_content.json")) as f:
    C = json.load(f)
with open(os.path.join(OUT, "12_authoring.json")) as f:
    A = json.load(f)
with open(os.path.join(OUT, "00_chapter_normalized.md")) as f:
    NORM = f.read()

chunks = {t["topic_id"]: t["original_chunk"]
          for m in C["modules"] for s in m["segments"] for t in s["topics"]}

# ---------------------------------------------------------------- explanation
# Only T1 carries a vocative. T2 and T11 carry a forward-look at the સ્વાધ્યાય phrased
# as a promise to the class; it is turned into a plain statement about the book.
# Every other explanation was already free of classroom address and is carried across
# unchanged rather than reworded for its own sake.
EXPL_EDITS = {
    "M1.S1.T1": [("બાળકો, જુઓ — ", "")],
    "M1.S1.T2": [("સ્વાધ્યાયમાં આવો જ અર્થ ધરાવતાં વાક્યો પાઠમાંથી શોધવાનાં આવશે.",
                  "સ્વાધ્યાયમાં આવો જ અર્થ ધરાવતાં વાક્યો પાઠમાંથી શોધવાનાં આવે છે.")],
    "M4.S5.T11": [("સ્વાધ્યાયમાં આવી જ રીતે કોઈ બીજાની દિનચર્યા લખવાની આવશે.",
                   "સ્વાધ્યાયમાં આવી જ રીતે કોઈ બીજાની દિનચર્યા લખવાની આવે છે.")],
}

# ------------------------------------------------------- real_life_example → page
# Same single Gujarat anchor, same picture, same closing link to પાલુબેન; the second-person
# address to the child and the closing question are dropped. Nothing added.
RLE_PUB = {
"M1.S1.T1":
"નવા વર્ગમાં પહેલા દિવસે બેન કહે છે — ‘ઊભા થઈને પોતાનો પરિચય આપો.’ છોકરું ઊભું થાય, પોતાનું નામ કહે, "
"ને પછી કહે કે એને શું ગમે છે. બે-ત્રણ વાક્યમાં આખો પરિચય પૂરો થઈ જાય છે. પાલુબેન પણ પાઠની શરૂઆતમાં "
"આવું જ કરે છે — નામ, ધંધો, ને દિવસ કેવો જાય તે.",

"M1.S1.T2":
"નવરાત્રિની રાતે ફળિયામાં ગરબો મોડે સુધી ચાલે છે. તાળીના તાલમાં ખબર જ નથી પડતી કે અગિયાર ક્યારે વાગ્યા. "
"બીજા દિવસે સવારે નિશાળનો ઘંટ વાગે ત્યારે આંખો ઘેરાયા કરે છે ને પગ ભારે લાગે છે. અધૂરી ઊંઘ પછી શરીર કેવું "
"લાગે તે એ સવારે સમજાય છે. પાલુબેનની તો રોજની ઊંઘ આટલી જ છે.",

"M2.S2.T3":
"નિશાળના પ્રવાસનો દિવસ હોય ત્યારે ઘરમાં કોઈ સૌથી વહેલું ઊઠી જાય છે. તવા પર થેપલાં એક પછી એક ઊતરે છે, "
"બાજુમાં અથાણાની ચીર મુકાય છે, ને ડબ્બો ભરાઈને દફતરમાં ગોઠવાઈ જાય છે. છોકરાં ઊઠે ત્યારે તો બધું તૈયાર હોય. "
"પાલુબેન પણ અંધારામાં ઊઠીને છોકરાં માટે ને ઘરવાળા માટે આ જ કરે છે.",

"M2.S2.T4":
"રિસેસનો ઘંટ વાગે ને પાણીના નળ પાસે એકસાથે દસ-બાર જણ ભેગાં થઈ જાય છે. કોઈ આગળ ઘૂસે, કોઈ ‘મારો વારો’ "
"કહીને બૂમ પાડે, ને પવાલું હાથોહાથ ફરે. છેલ્લા જણનો વારો આવે ત્યાં તો બીજો ઘંટ વાગી જાય છે. એ થોડી "
"મિનિટોમાં બધું પતાવવાની જે દોડાદોડ થાય છે, તે માર્કેટની તડાતડી જેવી જ છે.",

"M2.S3.T5":
"ગામથી બહાર જવાનું હોય ત્યારે એસ.ટી. બસના ડેપો પર વહેલા પહોંચી જવું પડે છે. મોડા પહોંચનારની બારી પાસેની "
"સીટ ગઈ સમજો, ને આખો રસ્તો ઊભાં ઊભાં કાપવો પડે. જે વહેલો પહોંચે તેને જ સારી જગ્યા મળે છે. પાલુબેન પણ "
"એટલે જ છ વાગ્યા સુધીમાં પાથરણું ગોઠવી કાઢે છે.",

"M2.S3.T6":
"શેરીમાં લખોટી રમાતી હોય ને નાનું ભાઈ-બહેન ઓટલે બેઠું હોય. નિશાન લખોટી પર હોય, પણ કાન ઓટલા ભણી જ રહે છે. "
"થોડી થોડી વારે નજર ઊંચી થાય — બેઠું છે ને ? રમત ચાલુ રહે, છતાં મન વારે વારે ત્યાં પહોંચી જાય છે. "
"પાલુબેનના હાથ ત્રાજવે હોય ત્યારે એમનું મન પણ આમ જ ઘર ભણી જાય છે.",

"M2.S3.T7":
"ઈદની સવારે પડોશમાંથી સેવૈયાની વાટકી આવે છે. ઘરમાં સૌ થોડું થોડું લે, ને છોકરાંને પણ બહુ ભાવે. તોય એમાંથી "
"થોડું બીજી વાટકીમાં ઢાંકીને બાજુ પર મુકાય છે — નાનો ભાઈ નિશાળેથી આવે ત્યારે એને માટે. પોતાના ભાગમાંથી "
"કોઈક માટે રાખી મૂકવાની આ જ વાત પાલુબેનનાં ભજિયાંમાં પણ છે.",

"M3.S4.T8":
"વરસાદ આવે ને દફતર માથે મૂકીને ઘેર દોડાય, તોય ચોપડી પલળી જ જાય છે. ઘેર જઈને પાનાં છૂટાં પડાય, પંખા નીચે "
"સૂકવાય, તોય કેટલાંક પાનાં ચોંટી જાય છે. પછી એ પાઠ ફરી લખવો પડે, ને એમાં રમવાનો વખત જાય. વસ્તુ પણ ગઈ ને "
"વખત પણ ગયો. પાલુબેનનો માલ ખટારે ચડી જતો ત્યારે એમને પણ આવી બેવડી ખોટ પડતી.",

"M3.S4.T9":
"ઉત્તરાયણે ધાબે એકલા ઊભા રહેનારને એક હાથે દોર ને બીજા હાથે ફિરકી — બંને સાચવવાં અઘરાં પડે છે. પતંગ ઊંચે "
"જાય ત્યાં તો દોર ગૂંચવાય. ત્યાં કોઈ આવીને ફિરકી પકડી લે, ને એટલું જ થવાથી પતંગ સીધો ઊંચે ચડવા માંડે છે. "
"પતંગ તો પોતાનો જ રહે છે, પણ સાથ મળે એટલે કામ સહેલું થઈ જાય.",

"M4.S5.T10":
"ઉનાળે કૂંડામાં બી વાવ્યું હોય. આખો દિવસ રમીને સાંજે થાક લાગ્યો હોય, તોય યાદ આવે કે પાણી પાવાનું બાકી છે. "
"ઊઠીને લોટો ભરાય, માટીમાં ધીરે ધીરે પાણી રેડાય, ને એ પછી જ સૂવાનું થાય. હજી તો કંઈ ઊગ્યું નથી, છતાં રોજ "
"પાણી પડે છે. પાલુબેન થાકીને આવ્યા પછી પણ છોકરાં માટે ઊભાં થાય છે તે આવું જ છે.",

"M4.S5.T11":
"શેરીમાં અંધારું થવા માંડે ને કોઈ કહે, ‘હવે બસ !’ છેલ્લી ઓવર રમાય, થાંભલા પરથી સ્ટમ્પનું નિશાન ભૂંસાય, ને "
"બૅટ-બૉલ ભેગાં થાય. કોઈ પાણી પીવા દોડે, કોઈ ચંપલ શોધે. છૂટા પડતાં પહેલાં એટલું જ કહેવાય — ‘કાલે પાછા !’ "
"પાલુબેન પણ પાથરણું વાળીને એવી જ રીતે વિદાય લે છે.",
}

# ---------------------------------------------------------------------- build
topics = []
for at in A["topics"]:
    tid = at["topic_id"]

    pub_text = at["explanation"]
    for old, new in EXPL_EDITS.get(tid, []):
        assert old in pub_text, (tid, old)
        pub_text = pub_text.replace(old, new, 1)

    chunk = chunks[tid]                       # verbatim, copied — never retyped
    pub_chunk = chunk + "\n\n" + pub_text + "\n\n" + RLE_PUB[tid]

    cpub = []
    for cp in at["concepts"]:
        for i, b in enumerate(cp["content"]):
            if b["type"] == "paragraph":
                cpub.append({"concept_id": cp["concept_id"],
                             "content_index": i,
                             "publication_text": b["text"]})

    topics.append({"topic_id": tid,
                   "publication_text": pub_text,
                   "publication_chunk": pub_chunk,
                   "concept_publication": cpub})

# ------------------------------------------------------------------- asserts
def nfc(s):
    return unicodedata.normalize("NFC", s)

problems = []
for at, pt in zip(A["topics"], topics):
    tid = at["topic_id"]
    ch = chunks[tid]
    # verbatim survives untouched at the head of the chunk
    assert pt["publication_chunk"].startswith(ch + "\n\n"), tid
    # verbatim occurs, line by line, in Agent 1's transcription of the renders.
    # One documented exception: folio 102 prints થાકીને ઠૂસ (દીર્ઘ ૂ) in the running
    # paragraph while folio 103's રૂઢિપ્રયોગ box prints ઠુસ (હ્રસ્વ ુ). Agent 1's
    # transcription carries the box's form in both places; page-2.png, read at 16×,
    # shows the paragraph's mark to be the same દીર્ઘ ૂ as in સૂઈ two lines below.
    # Agent 5's original_chunk is therefore the form the page prints, and stands.
    for line in ch.split("\n"):
        probe = nfc(line.strip()).replace("ઠૂસ", "ઠુસ")
        if line.strip() and probe not in nfc(NORM):
            problems.append((tid, "chunk line not found in 00_chapter_normalized.md", line))
    # publication_text is not longer than the teaching block and adds no vocative
    for bad in ["બાળકો", "હવે વિચારો", "હવે ધ્યાનથી", "જુઓ —"]:
        if bad in pt["publication_text"]:
            problems.append((tid, "classroom address survives", bad))
    # no Devanagari daṇḍa, no Devanagari letters, no digits in display text
    for field in ("publication_text", "publication_chunk"):
        s = pt[field]
        if "।" in s:
            problems.append((tid, field, "danda"))
        for chx in s:
            if "ऀ" <= chx <= "ॿ":
                problems.append((tid, field, "devanagari " + chx))
    for chx in pt["publication_text"]:
        if chx.isdigit():
            problems.append((tid, "publication_text", "digit " + chx))
    # concept_publication index integrity
    want = [(c["concept_id"], i)
            for c in at["concepts"] for i, b in enumerate(c["content"])
            if b["type"] == "paragraph"]
    got = [(e["concept_id"], e["content_index"]) for e in pt["concept_publication"]]
    if want != got:
        problems.append((tid, "concept index mismatch", str(want), str(got)))
    for e in pt["concept_publication"]:
        src = [c for c in at["concepts"] if c["concept_id"] == e["concept_id"]][0]
        if src["content"][e["content_index"]]["text"] != e["publication_text"]:
            # allowed only if deliberately rewritten; none are for this chapter
            problems.append((tid, "concept text changed", e["concept_id"]))

print("PROBLEMS:", len(problems))
for p in problems:
    print("  ", p)

NOTES = [
 "publication_text is each topic's teaching `explanation` from 12_authoring.json rendered for a "
 "reader on a page: the classroom address is removed, every fact, gloss, quoted line, name and "
 "number-word is kept, and the length band is unchanged. Nothing was added. Only M1.S1.T1 carried "
 "a vocative (‘બાળકો, જુઓ —’). M1.S1.T2 and M4.S5.T11 each closed on a promise to the class about "
 "what the સ્વાધ્યાય will ask (‘…શોધવાનાં આવશે.’, ‘…લખવાની આવશે.’); both are stated as plain facts "
 "about the book (‘…આવે છે.’) rather than dropped, because the reading they carry is Agent 12's. "
 "The other eight explanations were already free of classroom address and are carried across "
 "unchanged rather than reworded for its own sake.",

 "publication_chunk = the topic's verbatim `original_chunk`, copied programmatically from "
 "05_with_content.json (never retyped, never reflowed, its printed paragraph breaks preserved), "
 "then the topic's publication_text, then the reader-facing form of `real_life_example`. This "
 "chapter is આત્મકથનાત્મક નિબંધ in પાલુબેનનો પોતાનો અવાજ, so the verbatim is running prose: the "
 "printed spoken forms (દા’ડો, કો’કવાર, હારુ, ઘરાક, બોણી, વઢ, ટાઢો, બચુડિયાનો, આયખું, ઢસરડા), the "
 "printed spacing before ? and !, the printed ellipsis at the end of M2.S2.T3's chunk and the "
 "‘સેવા’ quotation marks are all untouched. Every chunk line was checked, in this build, against "
 "Agent 1's transcription of the renders.",

 "ONE VERBATIM CONFLICT, resolved on the render rather than by preference. 05_with_content.json's "
 "M4.S5.T10 chunk reads ‘થાકીને ઠૂસ થઈ ગઈ હોઉં’ (દીર્ઘ ૂ) while 00_chapter_normalized.md reads ઠુસ "
 "(હ્રસ્વ ુ). _renders/page-2.png (folio 102) was opened and the two marks cropped at 16× : in the "
 "running paragraph the mark under ઠ is the same broad open દીર્ઘ ૂ that સૂઈ carries two lines "
 "below, while folio 103's bold રૂઢિપ્રયોગ box (‘થાકીને ઠુસ થઈ જવું’) prints the tight closed હ્રસ્વ "
 "ુ loop. The book itself is inconsistent between its paragraph and its idiom box; Agent 5's chunk "
 "matches the paragraph as printed and is carried unchanged, and Agent 1's transcription carries "
 "the box's form in both places. Flagged for QC — nothing in this agent's output was altered to "
 "paper over it, and no other agent's file was touched.",

 "The `real_life_example` rewrite drops the second-person address to the child and the closing "
 "question, and states the same single picture as a general observation. Every anchor stands as "
 "Agent 12 authored it — વર્ગમાં પરિચય, નવરાત્રિનો ગરબો, પ્રવાસના દિવસનાં થેપલાં, રિસેસનો નળ, "
 "એસ.ટી. ડેપોની બારી પાસેની સીટ, શેરીની લખોટી, ઈદની સેવૈયાની વાટકી, વરસાદમાં પલળેલી ચોપડી, "
 "ઉત્તરાયણની ફિરકી, કૂંડામાં વાવેલું બી, શેરી ક્રિકેટની છેલ્લી ઓવર — one picture each, nothing "
 "added, no anchor swapped.",

 "concept_publication carries one entry per `paragraph` block of 12_authoring.json's "
 "concepts[].content[], in Agent 12's order, with content_index = that block's own index in the "
 "array as Agent 12 left it (list blocks are skipped, never renumbered, never dropped). 26 entries "
 "over 13 concepts across 11 topics; the mapping is asserted against Agent 12's own blocks at "
 "build time. Every one of the 26 paragraphs was already publication-shaped — no vocative, no "
 "instruction to the class — so all 26 are carried unchanged; rewording them for its own sake "
 "would risk adding meaning the teaching block does not have.",

 "Gujarati script throughout; `.` as printed and no `।` anywhere; no Roman and no Devanagari "
 "outside the chapter's own printed words; no digits in display text. The std-6 ceiling is intact: "
 "no અલંકાર, છંદ or સમાસ label was introduced, and no બોધ or ઉપદેશ sentence was added at any close "
 "— the closing topic still ends on પાલુબેન's own ‘આવજો ત્યારે પૃથાબેન !’ as Agent 12 rendered it.",
]

out = {
    "agent": "16_publication_authoring",
    "chapter_id": A["chapter_id"],
    "plan_id": A["plan_id"],
    "grade": A["grade"],
    "tier": A["tier"],
    "topics": topics,
    "notes": NOTES,
}
print("topics:", len(topics), "concept_publication entries:",
      sum(len(t["concept_publication"]) for t in topics))
assert not problems, problems
with open(os.path.join(OUT, "16_publication.json"), "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("written")
