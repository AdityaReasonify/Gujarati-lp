# -*- coding: utf-8 -*-
"""Agent 5 — attach verbatim + seed fields for std-6 ch-10 (સાથી મારે બાર)."""
import json, re, io, sys, collections

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch10"
struct = json.load(open(OUT + "/02_structure.json", encoding="utf-8"))
conv = json.load(open(OUT + "/04_converged.json", encoding="utf-8"))
norm = open(OUT + "/00_chapter_normalized.md", encoding="utf-8").read()

# ---- pull the printed verse lines out of 00_chapter_normalized.md ----------
# Only the [[કડી n]] blocks; markers, comments and every other block stay out.
lines = norm.split("\n")
kadi = collections.OrderedDict()
cur = None
in_comment = False
for ln in lines:
    s = ln.strip()
    if s.startswith("<!--"):
        in_comment = not s.endswith("-->")
        continue
    if in_comment:
        if s.endswith("-->"):
            in_comment = False
        continue
    m = re.match(r"^\[\[કડી (\d+)\]\]$", s)
    if m:
        cur = int(m.group(1)); kadi[cur] = []; continue
    if s.startswith("[["):            # any other marker closes the current કડી
        cur = None; continue
    if s == "":
        continue
    if cur is not None:
        kadi[cur].append(s)

assert list(kadi.keys()) == list(range(1, 16)), list(kadi.keys())
assert sum(len(v) for v in kadi.values()) == 30, sum(len(v) for v in kadi.values())

ATTRIB = "- રમણલાલ સોની"   # printed under the title on p. 63; goes to the LAST topic

def chunk(*ks, attrib=False):
    out = []
    for k in ks:
        out.extend(kadi[k])
    if attrib:
        out.append(ATTRIB)
    return "\n".join(out)

def wc(s):
    return len([w for w in s.split() if w.strip()])

# ---- authored seed fields --------------------------------------------------
D = {}

D["M1.S1.T1"] = dict(
    kadi=[1],
    modified="ઈડર ગામનો એક વાણિયો (વેપારી) છે. એનું નામ ધૂળો છે. સાંજ ઢળવા આવી ત્યારે એ પોતાના ગામથી કોટડા ગામે જવા નીકળે છે.",
    key_terms=[
        "વાણિયો — વેપાર કરનાર માણસ, વેપારી.",
        "ઈડર — ધૂળાનું ગામ, જ્યાંથી એ નીકળે છે.",
        "સમી સાંજ — સાંજ પડવાની વેળા, દિવસ આથમવાનો વખત.",
        "કોટડે — 'કોટડા ગામે'; કવિએ લય સાચવવા શબ્દનું રૂપ થોડું ટૂંકું કર્યું છે.",
        "નીકળ્યો — જવા માટે ઘરેથી રવાના થયો.",
    ])

D["M1.S1.T2"] = dict(
    kadi=[2],
    modified="રસ્તામાં અંધારું થઈ જાય છે અને ધૂળો સાચી વાટ (રસ્તો) છોડીને બીજા રસ્તે ચડી જાય છે. એ જંગલમાં ભૂલો પડે છે. એના દિલમાં ઉચાટ (ચિંતા) થાય છે.",
    key_terms=[
        "વાટ — રસ્તો.",
        "ઉચાટ — ચિંતા, ફિકર.",
        "ચડિયો — 'ચડ્યો'; કવિએ લય સાચવવા શબ્દનું રૂપ થોડું બદલ્યું છે, ભૂલ નથી.",
        "ભૂલો પડ્યો — રસ્તો ભૂલી જવો, ખોટા રસ્તે ચડી જવું.",
        "રસ્તે — રસ્તામાં; અહીં '-એ' પ્રત્યય 'માં'ના અર્થમાં આવ્યો છે.",
    ])

D["M1.S1.T3"] = dict(
    kadi=[3],
    modified="ભૂલો પડ્યા પછી પણ ધૂળો ડરી જતો નથી. એ મનમાં હિંમત રાખે છે અને પોતાની જાતને કહે છે કે પોતે ક્યારેય એકલો નથી, એની સાથે બાર સાથી છે.",
    key_terms=[
        "હિંમત ધરી — ડર છોડીને મન મક્કમ કર્યું.",
        "કદી — ક્યારેય.",
        "સાથી — સાથે રહેનાર, મદદ કરનાર.",
        "મારે — અહીં 'મારી પાસે' એ અર્થમાં આવ્યું છે; લયને કારણે આવું ટૂંકું રૂપ વપરાયું છે.",
        "મનમાં કર્યો વિચાર — મનમાં નક્કી કર્યું.",
    ])

D["M2.S2.T4"] = dict(
    kadi=[4],
    modified="એ જ વખતે પાસેની ઝાડી હાલે છે અને ચાર ચોર એકદમ સામે આવી જાય છે. તેઓ ધૂળાને ધમકી આપે છે કે તારી પાસે જે હોય તે અમને આપી દે.",
    key_terms=[
        "ઝાડી — ગીચ ઝાડ-ઝાંખરાં.",
        "સળવળી — હાલી, એમાં હલચલ થઈ.",
        "ચમક્યા — અહીં 'એકદમ સામે આવી ગયા, ઝબક્યા' એ અર્થમાં.",
        "ખબરદાર — સાવધાન !; ધમકી આપતી વખતે બોલાતો શબ્દ.",
        "એવે — 'એ વખતે'; કવિએ લય સાચવવા આવું ટૂંકું રૂપ વાપર્યું છે.",
    ])

D["M2.S2.T5"] = dict(
    kadi=[5],
    modified="ધૂળો ચોરોને સામો જવાબ આપે છે. એ કહે છે કે હું એકલો નથી, મારી સાથે બાર જણ નીકળ્યા છે, માટે થોડો વિવેક (સમજદારી) રાખજો.",
    key_terms=[
        "અલ્યા — 'એ ય !' જેવો સંબોધનનો તળપદો શબ્દ; સામેવાળાને બોલાવવા વપરાય છે.",
        "જણા — માણસો.",
        "કાંક — 'કંઈક'નું બોલચાલનું રૂપ.",
        "વિવેક — સમજદારી, સારું-નરસું પારખવાની સૂઝ.",
        "કરજો — કરો; આજ્ઞા આપતું માનવાચક રૂપ.",
    ])

D["M2.S3.T6"] = dict(
    kadi=[6],
    modified="ચોરો ધૂળાની વાત માનતા નથી. તેઓ મહેણું મારે છે કે નકામી વાત કાલે કરજે, આજે તો માલ આપી દે. એમ કહીને બે ડરામણા ચોર ધૂળા પર ધસી આવે છે.",
    key_terms=[
        "ટાયલી — નકામી, દોઢડહાપણભરી વાત.",
        "દઈ દે — આપી દે.",
        "માલ — સામાન, વસ્તુ; અહીં વેપારી પાસેની ચીજ-વસ્તુ.",
        "ઊમટ્યા — એકસાથે ધસી આવ્યા.",
        "વિકરાળ — ડરામણું, ભયાનક.",
    ])

D["M2.S3.T7"] = dict(
    kadi=[7],
    modified="ધૂળો કૂદીને પોતાનો કોથળો જોરથી ઘુમાવે છે. કોથળામાં તોલવાનાં કાટલાં ભરેલાં છે. એ કાટલાં ચોરોને ઉપરાછાપરી વાગે છે અને ધબ-ધબ અવાજ થાય છે.",
    key_terms=[
        "કોથળો — સામાન ભરવાની મોટી થેલી.",
        "કાટલાં — વજન; અમુક નક્કી વજનનું તોલવાનું સાધન.",
        "વીંઝે — જોરથી ઘુમાવે, ફેરવીને મારે.",
        "સબોસબ — ઉપરાછાપરી.",
        "ધબોધબ — મારનો 'ધબ ધબ' અવાજ સંભળાવતો શબ્દ.",
    ])

D["M2.S3.T8"] = dict(
    kadi=[8],
    modified="માર ખાઈને ચોરો ગુસ્સે થાય છે. તેઓ ધૂળા પર ઘા કરે છે, પણ ધૂળો એ ઘા અટકાવી દે છે. ચોરોને નવાઈ લાગે છે કે આ વેપારી લડવાના આવા દાવ ક્યાંથી શીખ્યો હશે.",
    key_terms=[
        "ખીજ્યા — ગુસ્સે થયા.",
        "ખાળે — અટકાવે, રોકે.",
        "ઘાવ — ઘા, પ્રહાર; મારવા માટે કરેલો હુમલો.",
        "દાવ — લડવાની આવડત, પેંતરો.",
        "રે — અહીં નવાઈ બતાવવા વપરાયેલો ઉદ્ગાર છે; એ લયનો શબ્દ છે.",
    ])

D["M2.S3.T9"] = dict(
    kadi=[9],
    modified="ધૂળો હવે અચકાયા વગર લડે છે. લડતાં લડતાં એ ફરી બોલે છે કે હું એકલો નથી, હવે તમને મારી ખરી તાકાત બતાવું છું.",
    key_terms=[
        "આઘુંપાછું ના જુએ — અચકાયા વગર, આગળ-પાછળનો વિચાર કર્યા વગર.",
        "જંગ — યુદ્ધ, લડાઈ.",
        "ખેલે — ખેલવું એટલે અહીં લડવું.",
        "રંગ — અહીં 'ખરી આવડત, પરાક્રમ'; 'રંગ બતાવવો' એટલે પોતાની તાકાત બતાવવી.",
        "નહિ — 'નહીં'નું કાવ્યમાં વપરાયેલું ટૂંકું રૂપ, ભૂલ નથી.",
    ])

D["M3.S4.T10"] = dict(
    kadi=[10, 11],
    modified="ધૂળામાં આટલું જોર જોઈને ચોરો ચમકી જાય છે. તેઓ વિચારે છે કે એકલા માણસમાં આટલી તાકાત છે, તો બાકીના બાર જણ છૂટશે ત્યારે આપણું આવી બનશે. એવું વિચારીને તેઓ બધા એકસાથે નાસી જાય છે, અને ધૂળો રાજી થાય છે.",
    key_terms=[
        "ચોંક્યા — ચમકી ગયા, નવાઈથી ડઘાઈ ગયા.",
        "જોર — તાકાત, બળ.",
        "ઘોર — અહીં 'આપણું આવી બન્યું, ખરાબ હાલત થશે' એ અર્થમાં આવ્યું છે.",
        "બી ગયા — બીક લાગી, ડરી ગયા.",
        "નાઠા — નાસી ગયા, ભાગી ગયા.",
        "હરખ્યો — રાજી થયો, ખુશ થયો.",
    ])

D["M3.S4.T11"] = dict(
    kadi=[12],
    modified="ચોર નાસી ગયા પછી ધૂળાને સાચી વાટ (રસ્તો) મળી જાય છે. જે ગામે જવું હતું ત્યાં એ પહોંચે છે. પોતાનું કામ પૂરું કરીને પછી જ એ ઘરે પાછો ફરે છે.",
    key_terms=[
        "વાટ જડી — રસ્તો મળી ગયો, રસ્તો હાથ લાગ્યો.",
        "જાવું'તું — 'જવું હતું'; બોલચાલમાં 'હતું' ટૂંકું થાય ત્યારે એની જગ્યાએ અપોસ્ટ્રોફી (') મુકાય છે.",
        "વળતો — પાછો ફરતાં, વળતી વખતે.",
        "પૂરું કરીને — પતાવીને, પૂરું કરી લીધા પછી.",
        "કામ — અહીં ધૂળાનું વેપારનું કામ.",
    ])

D["M3.S5.T12"] = dict(
    kadi=[13, 14, 15], attrib=True,
    modified="ધૂળાની આ વાત જાણીને બધાં બાળકો એને પૂછે છે કે તમારા બાર સાથી કોણ હતા, એમનાં નામ ગણાવો. ધૂળો ગણાવે છે — બે હાથ, બે આંખો, બે પગ, ચાર કાટલાં અને કોથળો; એમ દશ થયા. છેલ્લા બે સાથી હિંમત અને વિશ્વાસ છે, અને એ બે ન હોય તો બાકીના બધા નકામા થઈ જાય છે.",
    key_terms=[
        "વારતા — 'વાર્તા'નું કાવ્યમાં વપરાયેલું રૂપ; કવિએ લય સાચવવા આ રૂપ વાપર્યું છે.",
        "તમામ — બધા, સૌ.",
        "ગણાવો — એક પછી એક નામ દઈને કહો.",
        "પાય — પગ.",
        "દશ — 'દસ'નું કાવ્યમાં વપરાયેલું જૂનું રૂપ.",
        "વિશ્વાસ — ભરોસો; પોતાની જાત પર રહેલી શ્રદ્ધા.",
    ])

# ---- attach ---------------------------------------------------------------
order = []
seen_kadi = []
for mod in struct["modules"]:
    for seg in mod["segments"]:
        for t in seg["topics"]:
            tid = t["topic_id"]
            d = D[tid]
            ks = d["kadi"]
            seen_kadi.extend(ks)
            # provenance cross-check: 02_structure's kadi_markers must match
            want = ["કડી %d" % k for k in ks]
            assert t["provenance"]["kadi_markers"] == want, (tid, want, t["provenance"])
            oc = chunk(*ks, attrib=d.get("attrib", False))
            t["original_chunk"] = oc
            t["modified_chunk"] = d["modified"]
            t["word_count"] = {"original": wc(oc)}
            t["key_terms"] = d["key_terms"]
            t["primary_content_type"] = "image"
            t["secondary_content_type"] = None
            t["tertiary_content_type"] = None
            t["available_content_types"] = ["image"]
            order.append(tid)

assert sorted(seen_kadi) == list(range(1, 16)), sorted(seen_kadi)
assert len(order) == 12

# script + punctuation guards
BAD = re.compile(r"[ऀ-ॿ]|[A-Za-z]|।")
for mod in struct["modules"]:
    for seg in mod["segments"]:
        for t in seg["topics"]:
            for fld in ("original_chunk", "modified_chunk"):
                bad = BAD.findall(t[fld])
                assert not bad, (t["topic_id"], fld, bad)
            for kt in t["key_terms"]:
                assert " — " in kt, (t["topic_id"], kt)
                bad = BAD.findall(kt)
                assert not bad, (t["topic_id"], kt, bad)
                assert not re.search(r"\d", kt), (t["topic_id"], kt)
            assert 3 <= len(t["key_terms"]) <= 6, (t["topic_id"], len(t["key_terms"]))
            assert not re.search(r"\d", t["modified_chunk"]), t["topic_id"]

# every original_chunk line must exist verbatim in 00_chapter_normalized.md
for mod in struct["modules"]:
    for seg in mod["segments"]:
        for t in seg["topics"]:
            for ln in t["original_chunk"].split("\n"):
                assert ln in norm, (t["topic_id"], ln)

struct["notes"] = struct["notes"] + [
    "Agent 5 pass on the converged structure (04_converged.json verdict '%s', sha256 %s). Ids, names, objectives, concepts, provenance and every structural field are passed through untouched; only original_chunk, modified_chunk, word_count, key_terms and the four content-type fields were written." % (conv["verdict"], conv["sha256"]),
    "Verbatim. original_chunk copied line-for-line out of 00_chapter_normalized.md ([[…]] markers stripped) and verified against the 150 dpi renders _renders/page-1.png (printed folio 63) and page-2.png (folio 64), the verse lines re-read at 3x crop-zoom. All thirty printed lines are carried, fifteen કડી across twelve topics, no કડી split.",
    "The attribution line '- રમણલાલ સોની' is printed under the title at the top of folio 63, not at the foot of the poem. It is attached to the LAST topic's original_chunk (M3.S5.T12) as kathakavya.md §Explanation unit and reference/gujarati_verbatim.md rule 5 require, and as 02_structure.json notes instruct. Its printed position is recorded here rather than silently implied.",
    "content types: all twelve topics are reading scenes carrying verse a child reads, and kathakavya.md §Priors sets one image per narrative step, so every topic is primary_content_type 'image' with available_content_types ['image']; secondary and tertiary are null everywhere. No second medium is planned. The chapter prints no event-ordering સ્વાધ્યાય block, so kathakavya.md's one permitted 2d_tool is not earned — that call belongs to Agent 9 and is left untouched here.",
    "key_terms sit at five or six per topic (std-6 row of reference/shabd_gloss.md: 4–6, high in the 3–6 band). The chapter's printed શબ્દાર્થ box supplied વાટ, ઉચાટ, વિકરાળ, કાટલું, જંગ, પાય, સબોસબ, ખાળે where the word actually falls in that topic; the rest are Ring-2 L2 stopping points the box leaves out (વાણિયો, ઝાડી, સળવળી, ઊમટ્યા, વીંઝે, જણા, નાઠા, હરખ્યો, વળતો). The printed • રૂઢિપ્રયોગ block (ટાયલી કરવી, હાથ બતાવ્યો, દિલમાં ઉચાટ થવો) was NOT emptied into key_terms — it belongs to Agent 10 and the ભાષા-બોધ fields; only the bare word ટાયલી is glossed, in the topic where it is printed.",
    "The box's last entry 'રોકાણ - વાર, વિલંબ' glosses a word that appears nowhere in the poem (A1 records the same). Nothing was inferred from it, so 'વાર' in 'આપી દે આ વાર' is left unglossed rather than given a meaning the page does not settle.",
    "Every archaic, elided and dialect form printed on the page is carried unchanged and glossed rather than replaced: ચડિયો, એવે, અલ્યા, કાંક, નહિ, બી ગયા, જાવું'તું (the apostrophe is content), વારતા, દશ, પાય, સબોસબ, ધબોધબ, આઘુંપાછું, હરખ્યો, મારે.",
    "modified_chunk is a plain 'શું થઈ રહ્યું છે' restatement only — no ભાવ, no craft, no બોધ, no real-life link, and nothing that names the tally of the બાર સાથી before M3.S5.T12, so kathakavya.md hard gate 9 is not breached at this stage either.",
]

json.dump(struct, open(OUT + "/05_with_content.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

tb = {
    "chapter_id": struct["chapter_id"],
    "textbook_order": order,
    "source": "printed pages 63–64 (folio) = _renders/page-1.png, page-2.png, read off the render",
    "notes": [
        "The poem is printed as one continuous run of thirty lines. Folio 63 is set in two columns and is read DOWN each column, never across: left column = printed lines one to ten, right column (below the upper illustration) = printed lines eleven to twenty-one. Folio 64 carries the remaining nine lines in a single column.",
        "Printed order equals the logical order of 02_structure.json exactly; the list is emitted anyway so Agent 15 compares two real indexes instead of assuming they agree.",
        "Nothing between the chapters enters this list, and no apparatus or સ્વાધ્યાય block is in it: the blue પ્રવેશક box, the green શબ્દાર્થ box, the • રૂઢિપ્રયોગ block, the thirteen numbered blocks and the chapter-final riddle box are all excluded.",
    ],
}
json.dump(tb, open(OUT + "/05b_textbook_order.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

for tid in order:
    pass
print("topics:", len(order))
for mod in struct["modules"]:
    for seg in mod["segments"]:
        for t in seg["topics"]:
            print(t["topic_id"], t["word_count"]["original"], len(t["key_terms"]),
                  "|", t["original_chunk"].split("\n")[0][:40])
