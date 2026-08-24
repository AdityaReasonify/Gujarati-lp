#!/usr/bin/env python3
import json, os, re, collections, unicodedata

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch14"
L = lambda n: json.load(open(os.path.join(D, n)))
plan = L("13_merged.json")
meta = L("01_meta.json")
pit = L("07_pitfalls.json")
sens = L("08_sensitivity.json")
mediaf = L("09_media.json")
ex = L("10_exercise_solutions.json")
base = L("05_with_content.json")
norm = open(os.path.join(D, "00_chapter_normalized.md")).read()

FAIL, WARN, OK = [], [], []
def f(sec, msg, owner): FAIL.append((sec, msg, owner))
def w(msg): WARN.append(msg)
def ok(msg): OK.append(msg)

topics = [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]
TID = {t["topic_id"]: t for t in topics}
concepts = [c for t in topics for c in t["concepts"]]
CID = {c["concept_id"]: c for c in concepts}

wc = lambda s: len(s.split())

GUJ = lambda ch: 0x0A80 <= ord(ch) <= 0x0AFF
DEV = re.compile(r"[ऀ-ॿ]")
ROM = re.compile(r"[A-Za-z]")

# ---------- B ----------
for t in topics:
    oc = t["original_chunk"]
    if not oc.strip(): f("B", f"{t['topic_id']} original_chunk empty", "05")
    if ROM.search(oc): f("B", f"{t['topic_id']} Roman in original_chunk: {ROM.findall(oc)[:5]}", "05")
    if DEV.search(oc): f("B", f"{t['topic_id']} Devanagari in original_chunk", "05")
    if "।" in oc or "॥" in oc: f("B", f"{t['topic_id']} danda in original_chunk", "05")
    if not any(GUJ(c) for c in oc): f("B", f"{t['topic_id']} no Gujarati in original_chunk", "05")
ok("B: original_chunk script check on %d topics" % len(topics))

# script check across all authored display text
DISPLAY = ["topic_name", "explanation", "real_life_example", "brief_summary", "summary",
           "detailed_summary", "publication_text", "modified_chunk", "publication_chunk"]
for t in topics:
    fields = {k: t[k] for k in DISPLAY}
    fields.update({f"concept_bullets[{i}]": v for i, v in enumerate(t["concept_bullets"])})
    fields.update({f"important_points[{i}]": v for i, v in enumerate(t["important_points"])})
    fields.update({f"key_terms[{i}]": v for i, v in enumerate(t["key_terms"])})
    for i, r in enumerate(t["recall_questions"]):
        fields[f"RQ{i+1}.prompt"] = r["prompt"]; fields[f"RQ{i+1}.answer"] = r["answer"]
    for c in t["concepts"]:
        fields[c["concept_id"] + ".name"] = c["concept_name"]
        for i, b in enumerate(c["content"]):
            if b["type"] == "paragraph":
                fields[f"{c['concept_id']}[{i}].text"] = b["text"]
                if "publication_text" in b: fields[f"{c['concept_id']}[{i}].pub"] = b["publication_text"]
            else:
                for j, it in enumerate(b["items"]): fields[f"{c['concept_id']}[{i}][{j}]"] = it
    for k, v in fields.items():
        if not isinstance(v, str): continue
        if DEV.search(v): f("B", f"{t['topic_id']}.{k} Devanagari: {DEV.findall(v)[:5]}", "12")
        if "।" in v: f("B", f"{t['topic_id']}.{k} danda", "12")
        rom = ROM.findall(v)
        if rom: w(f"Roman chars in {t['topic_id']}.{k}: {''.join(rom)[:40]}")
        # digits in display text (chunks are provenance)
        if k not in ("modified_chunk", "publication_chunk"):
            dg = re.findall(r"[0-9૦-૯]", v)
            if dg: f("F", f"digit in display text {t['topic_id']}.{k}: {dg}", "12")

for o in plan["objectives"]:
    if DEV.search(o["objective_text"]): f("B", f"{o['objective_id']} Devanagari", "02")
    if re.findall(r"[0-9૦-૯]", o["objective_text"]): f("F", f"digit in {o['objective_id']} objective_text", "02")

# markers
mk = collections.Counter(re.findall(r"\[\[([^\]:]+)[:\]]", norm))
for label in ["કડી", "દુહો", "પદ", "ઘટના"]:
    if mk.get(label, 0):
        f("B", f"{label} marker count {mk[label]} but chapter has none in structure_inventory", "01")
samvad = mk.get("સંવાદ", 0)
if samvad != len(topics):
    f("B", f"[[સંવાદ]] markers {samvad} != topics {len(topics)}", "02")
else:
    ok(f"B: {samvad} [[સંવાદ: …]] markers == {len(topics)} topics")
swadhyay = mk.get("સ્વાધ્યાય", 0)
if swadhyay != len(meta["exercise_inventory"]):
    w(f"[[સ્વાધ્યાય]] markers {swadhyay} vs inventory {len(meta['exercise_inventory'])}")
else:
    ok(f"B: {swadhyay} [[સ્વાધ્યાય: …]] blocks == {len(meta['exercise_inventory'])} inventory entries, none a topic")
# no સ્વાધ્યાય text inside any original_chunk: check the exercise rhyme line
rhyme = "એક છોકરું"
for t in topics:
    if rhyme in t["original_chunk"]:
        f("B", f"{t['topic_id']} original_chunk contains exercise-block rhyme", "05")

# original_chunk lines actually in normalized md
for t in topics:
    for line in [l for l in t["original_chunk"].split("\n") if l.strip()]:
        if line not in norm:
            f("B", f"{t['topic_id']} original_chunk line not found in 00_chapter_normalized.md: {line[:60]}", "05")
ok("B: every original_chunk line found verbatim in 00_chapter_normalized.md")

# ---------- C ----------
for t in topics:
    for k in ("explanation", "real_life_example"):
        v = t[k]
        if not v.strip(): f("C", f"{t['topic_id']}.{k} empty", "12")
        n = wc(v)
        if not (55 <= n <= 90): f("C", f"{t['topic_id']}.{k} {n} words, band 55–90", "12")
for o in plan["objectives"]:
    n = wc(o["objective_text"])
    if not (12 <= n <= 30): f("C", f"{o['objective_id']} objective_text {n} words, band 12–30", "02")
ok("C: explanation / real_life_example / objective_text word bands")

# summaries strictly increase
for t in topics:
    a, b, c = wc(t["brief_summary"]), wc(t["summary"]), wc(t["detailed_summary"])
    if not (a < b < c): f("F", f"{t['topic_id']} summaries not strictly increasing {a}/{b}/{c}", "12")
ok("F: three-tier summaries strictly increase on every topic")

# ---------- D ----------
AREAS = {"ધર્મ", "સમુદાય", "ક્ષેત્ર", "વિકલાંગતા", "સંઘર્ષ", "જાતિ-ભૂમિકા", "સુરક્ષા"}
for s in sens["topics"]:
    bad = set(s["areas"]) - AREAS
    if bad: f("D", f"sensitivity areas not in the seven labels: {bad}", "08")
ok("D: 08 areas[] drawn from the seven fixed labels")

for t in topics:
    for d in t["figures_of_speech"]:
        if d.get("lines", "") not in t["original_chunk"]:
            f("D", f"{t['topic_id']} figures_of_speech lines not in original_chunk: {d.get('lines')}", "12")
ok("D: figures_of_speech verbatim check (all [] on this ગદ્ય chapter)")

# ---------- Contract ----------
if plan["phase"] != 2: f("F", "phase != 2", "01")
if plan["plan_id"] != f"{plan['chapter_id']}_v{plan['version']}": f("F", "plan_id mismatch", "01")
if plan["chapter_id"] != f"gseb_eng_gujarati{plan['grade']}_ch{plan['unit_number']}": f("F", "chapter_id shape", "01")
if plan["publication_id"] is None: f("F", "publication_id null — server rejects", "01")
ok("F: phase / chapter_id / plan_id / publication_id")

# objectives registry
seen = set()
for o in plan["objectives"]:
    if o["objective_id"] in seen: f("F", f"duplicate {o['objective_id']}", "02")
    seen.add(o["objective_id"])
    if o["home_topic_id"] not in TID: f("F", f"{o['objective_id']} home_topic_id unresolved", "02")
    for a in o["anchor"]:
        if a not in CID: f("F", f"{o['objective_id']} anchor {a} unresolved", "02")
for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in seen: f("F", f"strand map {lid}->{oid} unresolved", "02")
for o in plan["objectives"]:
    if o["legacy_id"] not in plan["strand_to_objective_map"]: f("F", f"{o['legacy_id']} not in strand map", "02")
for t in topics:
    for oid in t["objective_ids"]:
        if oid not in seen: f("F", f"{t['topic_id']} objective_ids {oid} unresolved", "02")
    for lo in t["learning_objectives"]:
        root = next(o for o in plan["objectives"] if o["objective_id"] == lo["objective_id"])
        if lo["objective_text"] != root["objective_text"]:
            f("F", f"{t['topic_id']} inline mirror text differs from registry", "02")
ok("F: objectives registry consistent; inline mirrors character-identical")

# ids
mi, si, ti, ci = 0, 0, 0, 0
for m in plan["modules"]:
    mi += 1
    if m["module_id"] != f"M{mi}": f("F", f"module id {m['module_id']} != M{mi}", "02")
    for s in m["segments"]:
        si += 1
        if s["segment_id"] != f"M{mi}.S{si}": f("F", f"segment id {s['segment_id']} != M{mi}.S{si}", "02")
        for t in s["topics"]:
            ti += 1
            if t["topic_id"] != f"{s['segment_id']}.T{ti}": f("F", f"topic id {t['topic_id']}", "02")
            if not t["concepts"]: f("F", f"{t['topic_id']} has no concept", "02")
            for c in t["concepts"]:
                ci += 1
                if c["concept_id"] != f"{t['topic_id']}.C{ci}": f("F", f"concept id {c['concept_id']} != {t['topic_id']}.C{ci}", "02")
                if not c["content"]: f("F", f"{c['concept_id']} content empty", "12")
                if c["objective_id"] not in seen: f("F", f"{c['concept_id']} objective_id unresolved", "02")
            for n, r in enumerate(t["recall_questions"], 1):
                if r["id"] != f"{t['topic_id']}.RQ{n}": f("F", f"recall id {r['id']}", "12")
                if r["legacy_id"] != f"{t['topic_id']}.TR{n}": f("F", f"recall legacy_id {r['legacy_id']}", "12")
                if not r["answer"].strip(): f("F", f"{r['id']} empty answer", "12")
                if r["bloom_level"] != r["bloom_level"].lower(): f("F", f"{r['id']} bloom_level not lowercase", "12")
if re.search(r"\.SR\d", json.dumps(plan)): f("F", ".SR{n} recall id present", "12")
ok(f"F: id grammar — M1–M{mi}, S1–S{si}, T1–T{ti}, chapter-continuous C1–C{ci}, RQ/TR ids, no .SR{{n}}")

for o in plan["objectives"]:
    if o["bloom_level"][0].islower(): f("F", f"{o['objective_id']} bloom_level not Capitalised", "02")

ENUM = {"POEM", "STORY_TELLING", "CONCEPT", "REVIEW"}
for t in topics:
    if t["topic_type"] not in ENUM: f("F", f"{t['topic_id']} topic_type {t['topic_type']} outside authored enum", "02")
ok("F: topic_type inside the authored enum (maps to instructional at A14 emit)")

# media
MEDIA_ID_RE = re.compile(r"^(?P<c>M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)\d+$")
scenes = [t for t in topics if "image" in t["available_content_types"]]
allmedia = [mm for t in topics for mm in t["media"]]
rr = mediaf["reuse_report"]
if rr["scenes"] != len(scenes): f("F", f"reuse_report.scenes {rr['scenes']} != image scenes {len(scenes)}", "09")
if rr["authored"] != rr["scenes"]: f("F", "reuse_report.authored != scenes", "09")
if rr["reused"] != 0: f("F", "reuse_report.reused != 0 — no Gujarati frame pool exists", "09")
if len(allmedia) != len(scenes): f("F", f"{len(allmedia)} media nodes for {len(scenes)} scenes", "09")
for mm in allmedia:
    if not MEDIA_ID_RE.match(mm["id"]): f("F", f"media id {mm['id']} fails MEDIA_ID_RE", "09")
    if MEDIA_ID_RE.match(mm["id"]).group("c") not in CID: f("F", f"media {mm['id']} concept unresolved", "09")
    if mm["image_url"] != "": f("F", f"media {mm['id']} non-empty image_url — fabricated URL", "09")
    if not mm["generation_prompt"].strip(): f("F", f"media {mm['id']} empty generation_prompt", "09")
    if "Devanagari script labels" not in mm["negative_prompt"]: f("F", f"media {mm['id']} negative_prompt lacks 'Devanagari script labels'", "09")
    if "reused frame" in json.dumps(mm, ensure_ascii=False): f("F", f"media {mm['id']} carries a reuse stamp", "09")
tools = [t["2d_tool"] for t in topics if t["2d_tool"]]
if len(tools) > 1: f("F", "more than one 2d_tool", "09")
ok(f"F: media — {len(allmedia)} nodes, one per image scene, image_url \"\" + authored prompt, {len(tools)} 2d_tool")

# ---------- Exercises ----------
inv = [e["verbatim_heading"] for e in meta["exercise_inventory"]]
cr = ex["coverage_report"]
if len(cr["blocks_found"]) != len(inv): f("E", f"blocks_found {len(cr['blocks_found'])} != inventory {len(inv)}", "10")
missing = [h for h in inv if h not in cr["blocks_found"]]
if missing: f("E", f"inventory blocks not found: {missing}", "10")
if cr["unanswered"]: f("E", f"unanswered blocks: {cr['unanswered']}", "10")
empty = [e["exercise_id"] for e in ex["exercises"] if not str(e.get("answer", "")).strip()]
if empty: f("E", f"exercise entries with empty answer: {empty}", "10")
groups = collections.Counter(e["exercise_group"] for e in ex["exercises"])
for e in meta["exercise_inventory"]:
    if groups.get(e["verbatim_heading"], 0) != e["items"]:
        w(f"item count drift for '{e['group']}': inventory {e['items']} vs solutions {groups.get(e['verbatim_heading'],0)}")
bad_map = [e["exercise_id"] for e in ex["exercises"] for tid in e.get("covered_by_topics") or [] if tid not in TID]
if bad_map: f("E", f"covered_by_topics pointing at non-existent topics: {bad_map}", "10")
ok(f"E: {len(cr['blocks_answered'])}/{len(inv)} blocks answered, {len(ex['exercises'])} entries, 0 unanswered, {len(cr['unmapped'])} unmapped (reported)")

# ---------- Publication ----------
for t in topics:
    if not t["publication_text"].strip(): f("Pub", f"{t['topic_id']} publication_text empty", "16")
    if t["original_chunk"] not in t["publication_chunk"]:
        f("Pub", f"{t['topic_id']} original_chunk not verbatim inside publication_chunk", "16")
    npara = sum(1 for c in t["concepts"] for b in c["content"] if b["type"] == "paragraph")
    npub = sum(1 for c in t["concepts"] for b in c["content"] if b["type"] == "paragraph" and "publication_text" in b)
    if npara != npub: f("Pub", f"{t['topic_id']} concept publication_text {npub}/{npara} paragraph blocks", "16")
    VOC = re.compile(r"(^|[.!?—:]\s*)(બાળકો|મિત્રો|વિદ્યાર્થીઓ)\s*[,!]|જુઓ\s*—|\bબોલો\s*[,.]|^ચાલો\s*,")
    if VOC.search(t["publication_text"]): f("Pub", f"{t['topic_id']} publication_text carries a vocative / classroom address", "16")
    for c in t["concepts"]:
        for b in c["content"]:
            if b.get("publication_text") and VOC.search(b["publication_text"]):
                f("Pub", f"{c['concept_id']} concept publication_text carries a vocative", "16")
    import difflib
    if difflib.SequenceMatcher(None, t["explanation"], t["publication_text"]).ratio() < 0.95:
        w(f"{t['topic_id']} publication_text diverges from explanation by more than the vocative — check for added meaning")
ok("Pub: publication_text present, verbatim intact inside publication_chunk, index-matched concept blocks, no vocative")

# ---------- D: hard pitfall / sensitivity items ----------
# G1 — printed speaker labels named in explanation
SPEAKERS = {
    "M1.S1.T1": ["ઝલક", "વનિતાબેન"],
    "M1.S1.T2": ["ઝલક", "વનિતાબેન", "મહેશભાઈ", "મનન"],
    "M1.S2.T3": ["મનન", "વનિતાબેન", "ઝલક"],
    "M2.S3.T4": ["મહેશભાઈ", "મનન"],
    "M2.S4.T5": ["વનિતાબેન", "મનન", "મહેશભાઈ", "ઝલક"],
}
for tid, sp in SPEAKERS.items():
    miss = [s for s in sp if s not in TID[tid]["explanation"]]
    if miss: f("D", f"G1 — {tid} explanation does not name printed speaker label(s) {miss}", "12")
ok("D: G1 both-voices — every printed speaker label of each topic named in its explanation")

# G2 — no preaching markers
PREACH = ["જોઈએ", "બોધ", "સંદેશ", "શિખામણ", "ઉપદેશ"]
for t in topics:
    blob = " ".join([t["explanation"], t["real_life_example"], t["brief_summary"], t["summary"],
                     t["detailed_summary"]] + [r["answer"] for r in t["recall_questions"]])
    hits = [p for p in PREACH if p in blob]
    if hits: w(f"G2 scan: '{hits}' string appears in {t['topic_id']} teaching fields — read in context")
# safety
t4 = TID["M2.S3.T4"]
blob4 = json.dumps(t4, ensure_ascii=False)
if "હું તારી સાથે જ હોવાનો" not in t4["explanation"]:
    f("D", "08 hard સુરક્ષા item — M2.S3.T4 explanation does not keep the adult present", "12")
ok("D: 08 hard સુરક્ષા item — adult kept present in M2.S3.T4 explanation / concepts / RQ / anchor")

# printed-as-is forms preserved
for form, tid in [("ભાઈલુ", "M1.S1.T1"), ("મજ્જા", "M2.S3.T4")]:
    if form not in TID[tid]["original_chunk"]: f("B", f"printed form {form} missing from {tid} original_chunk", "05")
ok("B: printed-as-is forms ભાઈલુ / મજ્જા intact in original_chunk")

# word_count sanity
for t in topics:
    n = len(t["original_chunk"].split())
    if abs(n - t["word_count"]["original"]) > 3:
        w(f"{t['topic_id']} word_count.original {t['word_count']['original']} vs recount {n}")

print("=== FAIL ===")
for x in FAIL: print(" ", x)
print("=== WARN ===")
for x in WARN: print(" ", x)
print("=== OK ===")
for x in OK: print(" ", x)
print("counts: fail", len(FAIL), "warn", len(WARN))
