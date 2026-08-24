# -*- coding: utf-8 -*-
import json, io, os, re, hashlib

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch01"
P12 = os.path.join(OUT, "12_authoring.json")

raw12 = io.open(P12, "rb").read()
H12 = hashlib.sha256(raw12).hexdigest()[:12]
a12 = json.loads(raw12.decode("utf-8"))
with io.open(os.path.join(OUT, "05_with_content.json"), encoding="utf-8") as f:
    c05 = json.load(f)

chunks = {}
for m in c05["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            chunks[t["topic_id"]] = t["original_chunk"]

PUB_TEXT = {
"M1.S1.T1": (
"એક જ ડાળ પર બેઠેલાં પંખી પોતે બોલે છે. 'અમે સહુ' એટલે અમે બધાં. પછી એ કહે છે — "
"'વિહરીએ કદી આભમાં ઊંચે,'. વિહરીએ એટલે આનંદથી ફરીએ, ને આભ એટલે આકાશ. ઊડી-ઊડીને પાછાં એ જ ડાળે "
"નીચે આવે છે. કલ્લોલ એટલે આનંદનો કિલકિલાટ; એ ચાલુ જ રહે છે. 'ઊંચે' ને 'નીચે' — બંનેના છેડા "
"સરખા સંભળાય છે. પંક્તિને છેડે '- એક જ.' છપાયું છે. એ ગાનારને કહે છે કે "
"'અમે સહુ એક જ ડાળનાં પંખી.' પાછું ગાવાનું છે."
),
"M1.S1.T2": (
"પંખી કહે છે કે સુખમાં ને દુઃખમાં અમે સાથે જ રહીએ છીએ. પછી એ પોતે કબૂલ કરે છે: "
"'લડીએ, વઢીએ, કદી જુદાં જ થઈએ,'. વઢીએ એટલે તકરાર કરીએ. ઝઘડો થાય છે, ને કોઈ વાર છૂટાં પણ પડી "
"જવાય છે. છેલ્લી પંક્તિ વાત ફેરવે છે — 'તોયે નિરંતર રહેતાં સંપી.' — તોયે એટલે તોપણ, નિરંતર એટલે સતત. "
"'રહીએ' ને 'થઈએ' — બંનેના છેડા સરખા સંભળાય છે."
),
"M1.S2.T3": (
"'ધરતીને ખોળે બાળ અમે સહુ,' — બાળ એટલે બાળક. કવિ ચિત્ર દોરે છે — મા ખોળામાં બેસાડે તેમ ધરતી "
"સૌને ખોળે લે છે. બોલનારાં પંખી પોતે છે. પછી એ સૌ સાથે મળીને કુદરત-ગાન, એટલે કુદરતનું ગીત, ગાય છે. "
"છેલ્લી પંક્તિમાં 'જીવન કેરા' આવે છે. કેરા એટલે '-નાં'; કાવ્યમાં આ ઢબ એમ ને એમ સચવાઈ છે. "
"સંગી એટલે સાથી. 'અમે સહુ' બંને પંક્તિને છેડે ફરી સંભળાય છે."
),
}

PUB_ANCHOR = {
"M1.S1.T1": (
"ઉત્તરાયણે સવારથી આખું ઘર એક જ ધાબે ભેગું થાય છે. પતંગ ઊંચે ચડે ત્યારે સૌની નજર આકાશમાં ચોંટે છે. "
"કપાયેલો પતંગ નીચે ઊતરે ત્યારે આખા ધાબે બૂમાબૂમ થાય છે. કોઈ દોર પકડે, કોઈ ફિરકી ફેરવે; હસવાનો "
"અવાજ દિવસભર બંધ થતો નથી. નાનાં-મોટાં સૌ એ જ ધાબે, સાંજ સુધી. પંખી જે એક ડાળની વાત કરે છે તે "
"ડાળ આ ધાબા જેવી છે."
),
"M1.S1.T2": (
"શેરીમાં થાંભલાના સ્ટમ્પે ક્રિકેટ રમાતું હોય ને 'આઉટ છે, નથી !' પર ઝઘડો પડે છે. કોઈ બૅટ મૂકીને ઘેર "
"ચાલ્યું જાય, કોઈ મોઢું ચડાવીને ઓટલે બેસી જાય. પણ થોડી વારમાં જ કોઈ બૂમ પાડે છે — 'ચાલો, દાવ ફરી !' "
"ને એ જ ટોળી પાછી થાંભલા પાસે ભેગી થઈ જાય છે. પંખીની વાત પણ આવી જ છે."
),
"M1.S2.T3": (
"સવારે પ્રાર્થનાસભામાં આખી શાળા મેદાનમાં હરોળબંધ ઊભી રહે છે. પગ નીચે એ જ ધૂળિયું મેદાન, ને માથે "
"ખુલ્લું આકાશ. પહેલી હરોળનાં નાનાં બાળકોથી માંડીને છેલ્લી હરોળ સુધી સૌનો એક જ સૂર ઊપડે છે. "
"પ્રાર્થના પૂરી થાય પછી સૌ સાથે જ વર્ગ ભણી ચાલવા માંડે છે. કડીમાં પંખી પણ આ રીતે જ સૌ સાથે ગાય છે "
"ને સાથે ચાલે છે."
),
}

# keyed by (concept_id, content_index) — one entry per `paragraph` block in 12_authoring.json
CONCEPT_PUB = {
("M1.S1.T1.C1", 0): (
"કાવ્યની શરૂઆતમાં જ બે પંક્તિની ટેક છપાઈ છે — 'એક જ ડાળનાં પંખી, અમે સહુ એક જ ડાળનાં પંખી.' "
"બોલનારાં પંખી પોતે છે, અને 'અમે સહુ' એટલે અમે બધાં. એક ડાળ પર બેઠેલાં આ પંખી પોતાની ઓળખ પોતે "
"આપે છે."
),
("M1.S1.T1.C1", 1): (
"કડીને છેડે છપાયેલું '- એક જ.' આખી ટેકનો ટૂંકો સંકેત છે. ગાનારે ત્યાં અટકીને "
"'અમે સહુ એક જ ડાળનાં પંખી.' પાછું ગાવાનું હોય છે. એટલે આ પંક્તિ આખા કાવ્યમાં વારેવારે કાને પડે છે."
),
("M1.S1.T1.C2", 0): (
"પહેલી કડીમાં ઉડાનનું ચિત્ર છે. પંખી કહે છે 'વિહરીએ કદી આભમાં ઊંચે,' — વિહરીએ એટલે આનંદથી ફરીએ, "
"ને આભ એટલે આકાશ. પછી 'ઊડી-ઊડી કદી આવીએ નીચે,' — ઊડતાં ઊડતાં પાછાં એ જ ડાળે નીચે આવે છે."
),
("M1.S1.T1.C2", 1): (
"આ ઊંચે-નીચેની અવરજવર વચ્ચે તેમનો કલ્લોલ, એટલે આનંદનો કિલકિલાટ, અટકતો નથી. એટલે એ ઉમંગી, એટલે "
"ઉત્સાહી, રહે છે. 'ઊંચે' ને 'નીચે' — બંનેના છેડા સરખા સંભળાય છે, ને પંક્તિ ગાવામાં ઝૂલો બેસે છે."
),
("M1.S1.T2.C3", 0): (
"આ કડી ત્રણ ડગલે ચાલે છે. પહેલી પંક્તિમાં પંખી કહે છે કે સુખમાં ને દુઃખમાં અમે સાથે જ રહીએ છીએ. "
"બીજી પંક્તિ કંઈ છુપાવતી નથી — 'લડીએ, વઢીએ, કદી જુદાં જ થઈએ,' — વઢીએ એટલે તકરાર કરીએ."
),
("M1.S1.T2.C3", 1): (
"ત્રીજી પંક્તિ આખી વાત ફેરવે છે — 'તોયે નિરંતર રહેતાં સંપી.' — તોયે એટલે તોપણ, ને નિરંતર એટલે સતત. "
"ઝઘડો થાય છે એ ખરું, પણ સંપ તૂટતો નથી. 'રહીએ' ને 'થઈએ' — બંનેના છેડા સરખા સંભળાય છે."
),
("M1.S2.T3.C4", 0): (
"છેલ્લી કડીમાં ચિત્ર મોટું થાય છે. 'ધરતીને ખોળે બાળ અમે સહુ,' — બાળ એટલે બાળક. મા ખોળામાં બેસાડે "
"તેમ ધરતી સૌને ખોળે લે છે, એવું ચિત્ર કવિ દોરે છે; ખોળે બેઠેલાં એ બાળ એટલે પંખી પોતે."
),
("M1.S2.T3.C4", 1): (
"પછી 'કરીએ કુદરત-ગાન અમે સહુ' — સૌ સાથે મળીને કુદરતનું ગીત ગાય છે. છેલ્લી પંક્તિમાં "
"'જીવન કેરા પ્રવાસનાં સંગી' આવે છે: કેરા એટલે '-નાં', ને સંગી એટલે સાથી. 'અમે સહુ' બંને પંક્તિને છેડે "
"પાછું આવે છે — એ જ શબ્દો ફરી કાને પડે છે."
),
}

topics_out = []
for t in a12["topics"]:
    tid = t["topic_id"]
    pub_text = PUB_TEXT[tid]
    pub_chunk = chunks[tid] + "\n\n" + pub_text + "\n\n" + PUB_ANCHOR[tid]
    cps = []
    for c in t["concepts"]:
        cid = c["concept_id"]
        for i, b in enumerate(c.get("content", [])):
            if b.get("type") != "paragraph":
                continue
            cps.append({"concept_id": cid, "content_index": i,
                        "publication_text": CONCEPT_PUB[(cid, i)]})
    topics_out.append({"topic_id": tid,
                       "publication_text": pub_text,
                       "publication_chunk": pub_chunk,
                       "concept_publication": cps})

doc = {
 "agent": "16_publication_authoring",
 "chapter_id": a12["chapter_id"],
 "plan_id": a12["plan_id"],
 "grade": a12["grade"],
 "tier": a12["tier"],
 "topics": topics_out,
 "notes": [
  "publication_text is the reader-facing rewrite of each topic's teaching explanation in 12_authoring.json: the vocative 'બાળકો, જુઓ —' and the direct instructions ('બોલી જુઓ', 'મોટેથી બોલી જુઓ', 'પાછું ગાઓ') are dropped and each such sentence is closed as a statement. Every fact, gloss, quoted line and sound observation of the teaching block survives; nothing was added.",
  "Nothing was dropped in the rewrite: the point-of-use glosses ('અમે સહુ', વિહરીએ, આભ, કલ્લોલ, ઉમંગી, વઢીએ, તોયે, નિરંતર, બાળ, કુદરત-ગાન, કેરા, સંગી), the unlabelled sound observations (ઊંચે/નીચે, રહીએ/થઈએ, the returning 'અમે સહુ') and the refrain shorthand '- એક જ.' explained in the first topic only are all carried across unchanged in substance.",
  "publication_chunk = the verbatim original_chunk from 05_with_content.json, copied programmatically (its line breaks, commas, વિસર્ગ, જોડાક્ષર and the trailing '- એક જ.' refrain shorthand untouched, never retyped), then the topic's publication_text, then the topic's real-life anchor rendered as continuous reader prose. No verse line was reflowed, modernised or corrected.",
  "The anchor paragraph inside publication_chunk keeps the same single picture as 12_authoring.json's real_life_example (ઉત્તરાયણનું ધાબું / શેરીમાં થાંભલાના સ્ટમ્પે ક્રિકેટ / શાળાની પ્રાર્થનાસભા), with the closing question to the child removed and the one second-person verb settled into narration. No new detail, place or claim was introduced.",
  "concept_publication carries one entry per 'paragraph' block in 12_authoring.json's concepts[].content[], in order, matched by content_index. Each of the four concepts has two paragraph blocks, at index 0 and index 1; the 'list' block at index 2 is untouched, and no block was renumbered, reordered or dropped.",
  "Authored against the 12_authoring.json revision with sha256 prefix " + H12 + ". An earlier revision of that file (two content blocks per concept, different anchors) was read first during this run; it was re-read and every field here was re-authored against the current one, then the hash re-checked after writing.",
  "Register held at the std-6 ધોરણ level: short sentences, the same simple શિષ્ટ ગુજરાતી, same length band as the teaching fields — no shift to formal literary register and no lowering of the gloss density an L2 reader needs.",
  "Checked mechanically over every display string: Gujarati script only, no Devanagari character, no Roman letter, no digit, and the printed પૂર્ણવિરામ '.' throughout — the Devanagari danda does not occur anywhere in the file.",
  "No અલંકાર, છંદ or પ્રાસ label appears (std-6 ceiling held, as in Agent 12), and no fact about the poet is stated — the rendered page prints only the name line and no કવિ-પરિચય.",
  "Verbatim re-verified for this agent against a fresh 150 dpi render of the chapter's opening page: the three original_chunk values in 05_with_content.json match the printed કડીઓ exactly, so they were reused as-is."
 ]
}

path = os.path.join(OUT, "16_publication.json")
with io.open(path, "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)
    f.write("\n")

# ---------------- checks ----------------
blob = json.dumps(doc, ensure_ascii=False)
assert "।" not in blob and "॥" not in blob, "danda found"
dev = [ch for ch in blob if "ऀ" <= ch <= "ॿ"]
assert not dev, ("devanagari", dev[:10])

disp = []
for t in topics_out:
    disp += [t["publication_text"], t["publication_chunk"]]
    disp += [c["publication_text"] for c in t["concept_publication"]]
for s in disp:
    bad = [ch for ch in s if ("a" <= ch.lower() <= "z") or ch.isdigit()]
    assert not bad, ("roman/digit", bad[:10], s[:60])

for tid, ch in chunks.items():
    pc = [t for t in topics_out if t["topic_id"] == tid][0]["publication_chunk"]
    assert pc.startswith(ch + "\n\n"), tid
    assert ch in pc

# every teaching paragraph block has exactly one publication entry, same order
for t12, tout in zip(a12["topics"], topics_out):
    exp = []
    for c in t12["concepts"]:
        for i, b in enumerate(c["content"]):
            if b["type"] == "paragraph":
                exp.append((c["concept_id"], i))
    got = [(c["concept_id"], c["content_index"]) for c in tout["concept_publication"]]
    assert exp == got, (t12["topic_id"], exp, got)

def wc(s):
    return len([w for w in re.split(r"\s+", s.strip())
                if re.search(r"[઀-૿]", w)])

for t12, tout in zip(a12["topics"], topics_out):
    print(t12["topic_id"],
          "expl", wc(t12["explanation"]), "->", wc(tout["publication_text"]),
          "| rle", wc(t12["real_life_example"]),
          "| chunk", wc(tout["publication_chunk"]))
    for c12 in t12["concepts"]:
        for i, b in enumerate(c12["content"]):
            if b["type"] != "paragraph":
                continue
            print("   ", c12["concept_id"], i, wc(b["text"]), "->",
                  wc(CONCEPT_PUB[(c12["concept_id"], i)]))

assert hashlib.sha256(io.open(P12, "rb").read()).hexdigest()[:12] == H12, \
    "12_authoring.json changed while this agent was writing"
print("12_authoring sha", H12, "stable")
print("WROTE", path, os.path.getsize(path))
