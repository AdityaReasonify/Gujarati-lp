#!/usr/bin/env python3
# Agent 04 validator for std-6 ch15 (nibandh_atmaparak, unit = પ્રસંગ / વિચારનો વળાંક)
import json, re, sys, unicodedata

BASE = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch15"
S = json.load(open(f"{BASE}/02_structure.json"))
M = json.load(open(f"{BASE}/01_meta.json"))
NORM = open(f"{BASE}/00_chapter_normalized.md").read()

g = {"genre_fidelity": [], "coverage": [], "objectives": []}
blocking = []
notes = []


def norm(s):
    s = unicodedata.normalize("NFC", s or "")
    return re.sub(r"\s+", " ", s).strip()


# ---- flatten tree ----
topics, segs, mods = [], [], []
for m in S.get("modules", []):
    mods.append(m)
    for s in m.get("segments", []):
        segs.append(s)
        for t in s.get("topics", []):
            topics.append(t)
tids = [t["topic_id"] for t in topics]
cids = [c["concept_id"] for t in topics for c in t.get("concepts", [])]

# ================= CHECK 1 : સ્વરૂપ fidelity =================
meta_unit = norm(M.get("explanation_unit"))
str_unit = norm(S.get("explanation_unit"))
if meta_unit != str_unit:
    blocking.append(f"explanation_unit mismatch: 01_meta='{meta_unit}' vs 02_structure='{str_unit}'")
    g["genre_fidelity"].append("explanation_unit does not match 01_meta.json")
slug = norm(S.get("genre"))
prof_slugs = [p.replace(".md", "") for p in M.get("active_genre_profiles", [])]
if slug not in prof_slugs:
    blocking.append(f"genre slug '{slug}' is not among 01_meta active_genre_profiles {prof_slugs}")
    g["genre_fidelity"].append("genre slug does not match the active profile")
if norm(S.get("teaching_lens")) != norm(M.get("teaching_lens")):
    notes.append("teaching_lens text differs between 01_meta.json and 02_structure.json")

# verse-unit marker parity (vacuous for this prose chapter, still counted)
for label, key in (("કડી", "kadi"), ("દુહો", "duha"), ("પદ", "pad")):
    n_mark = len(re.findall(r"\[\[" + label + r"\s", NORM))
    if n_mark:
        carriers = [t for t in topics if label in norm(t.get("source_span", {}).get("marker", ""))]
        if len(carriers) != n_mark:
            blocking.append(f"{label}: {n_mark} markers vs {len(carriers)} topics carrying them")
            g["genre_fidelity"].append(f"{label} marker/topic count unequal")
si = M.get("structure_inventory", {})
if si.get("kadi") or si.get("duha") or si.get("pad"):
    notes.append("structure_inventory reports verse units in a prose chapter — recheck")

# profile avoid list (nibandh_atmaparak, structural items owned by Agent 4)
climax = [t["topic_id"] for t in topics if norm(t.get("topic_category")) == "climax"]
if climax and "nibandh_atmaparak" in prof_slugs:
    blocking.append(f"profile avoid #2: topic_category 'climax' on {climax} — an આત્મપરક નિબંધ has પ્રસંગ, not પ્લોટ")
    g["genre_fidelity"].append("climax topic_category present")

AUTHORED = {"POEM", "STORY_TELLING", "CONCEPT", "REVIEW"}
bad_tt = sorted({t.get("topic_type") for t in topics} - AUTHORED)
if bad_tt:
    blocking.append(f"topic_type outside the authored enum: {bad_tt}")
    g["genre_fidelity"].append("bad topic_type value")
poemish = [t["topic_id"] for t in topics if t.get("topic_type") == "POEM"]
if poemish:
    blocking.append(f"POEM topic_type in a prose આત્મકથનાત્મક નિબંધ: {poemish}")

# numbers in display names (global rule 4)
for t in topics:
    if re.search(r"[0-9૦-૯]", t.get("topic_name", "")):
        blocking.append(f"{t['topic_id']}: digit in topic_name '{t['topic_name']}' (global rule 4)")
for s in segs:
    if re.search(r"[0-9૦-૯]", s.get("segment_name", "")):
        blocking.append(f"{s['segment_id']}: digit in segment_name '{s['segment_name']}'")

# ================= CHECK 2 : coverage =================
# reading scenes marked in 00_chapter_normalized.md
scene_re = re.compile(r"^\[\[(ફકરો\s*\d+|ઘટના:[^\]]*|પ્રસંગ:[^\]]*)\]\]", re.M)
scenes = [m.group(1) for m in scene_re.finditer(NORM)]
n_scenes = len(scenes)

APPARATUS = ("પ્રવેશપેટી", "શબ્દાર્થ", "રૂઢિપ્રયોગ", "ચિત્ર", "એકમ-શીર્ષક", "લેખક-નામ", "એકમ-સમાપ્તિ")

# no સ્વાધ્યાય became a topic
ex_heads = [norm(e["verbatim_heading"]) for e in M.get("exercise_inventory", [])]
ex_groups = [norm(e["group"]) for e in M.get("exercise_inventory", [])]
sv_hits = []
for t in topics:
    tn = norm(t.get("topic_name"))
    oc = norm(t.get("original_chunk")) + " " + norm(json.dumps(t.get("source_span", {}), ensure_ascii=False))
    mk = oc
    if "સ્વાધ્યાય" in mk or "સ્વાધ્યાય" in tn:
        sv_hits.append((t["topic_id"], "marker/name says સ્વાધ્યાય"))
        continue
    for h, gp in zip(ex_heads, ex_groups):
        if not h:
            continue
        if h in tn or (len(h) > 12 and h in oc):
            sv_hits.append((t["topic_id"], f"carries સ્વાધ્યાય heading '{h[:40]}' ({gp})"))
            break
if sv_hits:
    for tid, why in sv_hits:
        blocking.append(f"સ્વાધ્યાય cut as a topic — {tid}: {why}")
    g["coverage"].append("સ્વાધ્યાય block became a topic")

# A2 emits source_span markers; original_chunk is filled by a later agent.
body = NORM.split("\n---\n")[0]
body_n = norm(body)

# every topic must name markers that exist in the chapter BODY (never the સ્વાધ્યાય half)
body_markers = set(re.findall(r"\[\[([^\]]+)\]\]", body))
ex_half = NORM.split("\n---\n")[1] if "\n---\n" in NORM else ""
ex_markers = set(re.findall(r"\[\[([^\]]+)\]\]", ex_half))
body_order = [m.group(1) for m in re.finditer(r"\[\[([^\]]+)\]\]", body)]

def claimed(t):
    ss = t.get("source_span") or {}
    raw = " ".join(str(v) for k, v in ss.items() if k in ("marker", "markers", "spans")) or ""
    if isinstance(ss.get("markers"), list):
        raw += " " + " ".join(ss["markers"])
    return [bm for bm in body_markers if bm in raw], raw

unclaimed, order_pos = [], []
for t in topics:
    hits, raw = claimed(t)
    if not raw.strip():
        unclaimed.append((t["topic_id"], "source_span names no marker"))
        continue
    if not hits:
        stolen = [em for em in ex_markers if em in raw]
        if stolen:
            unclaimed.append((t["topic_id"], f"source_span points at a સ્વાધ્યાય marker: {stolen[:2]}"))
        else:
            unclaimed.append((t["topic_id"], f"source_span marker not found in the chapter body: {raw[:60]}"))
        continue
    order_pos.append(min(body_order.index(h) for h in hits))
if unclaimed:
    for tid, why in unclaimed:
        blocking.append(f"{tid}: {why}")
    g["coverage"].append("topic does not map onto a marked chapter-body scene")

if order_pos != sorted(order_pos):
    blocking.append("topics are not in reading order against 00_chapter_normalized.md")
    g["coverage"].append("topic order does not follow the chapter")

# every marked reading scene (ફકરો / ઘટના / પ્રસંગ) is claimed by some topic
all_raw = " ".join(claimed(t)[1] for t in topics)
missed = [sc for sc in scenes if sc not in all_raw]
if missed:
    blocking.append(f"reading scenes with no topic: {missed}")
    g["coverage"].append("uncovered reading scenes")

# pre-reading opener
opener = [t for t in topics if t.get("topic_type") == "CONCEPT" and norm(t.get("topic_category")) == "introduction"]
if not opener:
    notes.append("no CONCEPT/introduction pre-reading opener topic found — confirm the opener is a topic")

# ================= CHECK 3 : objectives + phase-2 id contract =================
objs = S.get("objectives", [])
oids = [o.get("objective_id") for o in objs]
if not objs:
    blocking.append("root objectives[] missing or empty")
    g["objectives"].append("no objectives registry")
if len(set(oids)) != len(oids):
    blocking.append(f"duplicate objective_id: {[o for o in oids if oids.count(o) > 1]}")
    g["objectives"].append("duplicate objective_id")
for o in objs:
    if not re.fullmatch(r"O\d+", o.get("objective_id", "")):
        blocking.append(f"objective_id not O{{n}}: {o.get('objective_id')}")
    if o.get("home_topic_id") not in tids:
        blocking.append(f"{o.get('objective_id')}: home_topic_id '{o.get('home_topic_id')}' resolves to no topic")
        g["objectives"].append("unresolved home_topic_id")
    for a in o.get("anchor", []):
        if a not in cids:
            blocking.append(f"{o.get('objective_id')}: anchor '{a}' resolves to no concept")
            g["objectives"].append("unresolved anchor")
    if o.get("strand") != "L":
        notes.append(f"{o.get('objective_id')}: strand '{o.get('strand')}' (expected L)")
    n_words = len(norm(o.get("objective_text")).split())
    if not (12 <= n_words <= 30):
        notes.append(f"{o.get('objective_id')}: objective_text is {n_words} words (contract says 12–30)")

# strand_to_objective_map covers every legacy_id exactly once
smap = S.get("strand_to_objective_map", {})
legacy = [o.get("legacy_id") for o in objs]
if sorted(smap.keys()) != sorted(legacy):
    blocking.append(f"strand_to_objective_map keys {sorted(smap.keys())} != legacy_ids {sorted(legacy)}")
    g["objectives"].append("strand_to_objective_map does not cover every legacy_id exactly once")
for o in objs:
    if smap.get(o.get("legacy_id")) != o.get("objective_id"):
        blocking.append(f"strand_to_objective_map[{o.get('legacy_id')}] != {o.get('objective_id')}")

# every topic has objective_ids resolving to the registry
for t in topics:
    ois = t.get("objective_ids") or []
    if not ois:
        blocking.append(f"{t['topic_id']}: no objective_ids")
        g["objectives"].append("topic without objective_ids")
    for oi in ois:
        if oi not in oids:
            blocking.append(f"{t['topic_id']}: objective_id '{oi}' not in the root registry")

# no phase-1 objective code anywhere
if re.search(r"M\d+\.S\d+\.T\d+\.P\d+", json.dumps(S, ensure_ascii=False)):
    blocking.append("phase-1 style M1.S1.T1.P1 objective code present (phase-2 forbids it)")
    g["objectives"].append("phase-1 objective code")

# id grammar: dotted, continuous, no restart
for i, m in enumerate(mods, 1):
    if m.get("module_id") != f"M{i}":
        blocking.append(f"module_id expected 'M{i}', got '{m.get('module_id')}'")
si_n = 0
ti_n = 0
ci_n = 0
for m in S.get("modules", []):
    for s in m.get("segments", []):
        si_n += 1
        exp = f"{m['module_id']}.S{si_n}"
        if s.get("segment_id") != exp:
            blocking.append(f"segment_id expected '{exp}', got '{s.get('segment_id')}'")
        for t in s.get("topics", []):
            ti_n += 1
            expt = f"{s.get('segment_id')}.T{ti_n}"
            if t.get("topic_id") != expt:
                blocking.append(f"topic_id expected '{expt}', got '{t.get('topic_id')}'")
            for c in t.get("concepts", []):
                ci_n += 1
                expc = f"{t.get('topic_id')}.C{ci_n}"
                if c.get("concept_id") != expc:
                    blocking.append(f"concept_id expected '{expc}', got '{c.get('concept_id')}' (c is chapter-continuous)")
            if len(t.get("concepts", [])) > 2:
                notes.append(f"{t['topic_id']}: {len(t['concepts'])} concepts — three means the cut is wrong")

print(json.dumps({
    "n_topics": len(topics), "n_segments": len(segs), "n_scenes_marked": n_scenes,
    "n_objectives": len(objs), "n_concepts": len(cids),
    "topic_ids": tids,
    "topic_names": [t.get("topic_name") for t in topics],
    "categories": [t.get("topic_category") for t in topics],
    "types": [t.get("topic_type") for t in topics],
    "blocking": blocking, "group_notes": g, "notes": notes,
}, ensure_ascii=False, indent=1))
