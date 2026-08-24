#!/usr/bin/env python3
# Agent 14 — arrange, renumber, translate references, emit learning_plan_logical.json
import json, re, sys, copy, collections

OUT = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch03"
merged = json.load(open(f"{OUT}/13_merged.json", encoding="utf-8"))

# ---------- 1. arrange (reading order = merged structure order) + 2. renumber ----------
idmap = {}          # old -> new  (structural nodes)
m_i = 0; s_i = 0; t_i = 0; c_i = 0
for mod in merged["modules"]:
    m_i += 1
    new_m = f"M{m_i}"
    idmap[mod["module_id"]] = new_m
    for seg in mod["segments"]:
        s_i += 1
        new_s = f"{new_m}.S{s_i}"
        idmap[seg["segment_id"]] = new_s
        for top in seg["topics"]:
            t_i += 1
            new_t = f"{new_s}.T{t_i}"
            idmap[top["topic_id"]] = new_t
            for con in top.get("concepts", []):
                c_i += 1
                new_c = f"{new_t}.C{c_i}"
                idmap[con["concept_id"]] = new_c

def mp(old):
    if old is None:
        return None
    if old not in idmap:
        raise SystemExit(f"STALE REFERENCE: {old!r} resolves to no node")
    return idmap[old]

# ---------- key whitelists ----------
ROOT_KEYS = ["phase","board","subject","grade","level","version","ordering","author",
             "chapter_id","plan_id","chapter_name","unit_title","unit_number","topic_title",
             "topic_number","genre","teaching_lens","guiding_question","textbook","textbook_url",
             "textbook_pages","_activate","medium_id","subject_ref_id","publication_id",
             "chapter_master_id","estimated_time","english_plan_id","english_chapter_id",
             "objectives","strand_to_objective_map","modules"]

TOPIC_KEYS = ["topic_id","topic_name","topic_type","topic_category","difficulty",
              "original_chunk","modified_chunk","word_count","explanation","real_life_example",
              "brief_summary","summary","detailed_summary","key_terms","concept_bullets",
              "important_points","figures_of_speech","rhyme_scheme","shabdarth","samanarthi",
              "vilom","vyakaran","objective_ids","learning_objectives","concepts",
              "recall_questions","media","2d_tool","publication_text","publication_chunk",
              "depends_on","source_topic_ids","estimated_exchanges","primary_content_type",
              "secondary_content_type","tertiary_content_type","available_content_types"]
MODULE_KEYS = ["module_id","module_name","difficult_words","overall_rhyme_scheme","segments"]
SEGMENT_KEYS = ["segment_id","segment_name","topics"]

TOPIC_TYPE_MAP = {"POEM":"instructional","STORY_TELLING":"instructional","CONCEPT":"instructional",
                  "REVIEW":"summary","EXERCISE":"assessment",
                  "instructional":"instructional","summary":"summary","assessment":"assessment"}

def order(d, keys, where):
    extra = [k for k in d if k not in keys]
    if extra:
        print(f"  dropped from {where}: {extra}")
    return {k: d[k] for k in keys if k in d}

RQ_RE = re.compile(r"^(?P<node>M\d+\.S\d+(?:\.T\d+)?)\.(?P<kind>RQ|TR)(?P<n>\d+)$")
MEDIA_RE = re.compile(r"^(?P<c>M\d+\.S\d+\.T\d+\.C\d+)\.(?P<sfx>IMG|VID|2D|3D|SIM)(?P<n>\d+)$")

def remap_rq(rid, owner_new, kind_expected, idx):
    m = RQ_RE.match(rid)
    if not m:
        raise SystemExit(f"bad recall id {rid!r}")
    mp(m.group("node"))                      # must resolve
    return f"{owner_new}.{kind_expected}{idx}"

def remap_media(mid, concept_new, idx_by_sfx):
    m = MEDIA_RE.match(mid)
    if not m:
        raise SystemExit(f"bad media id {mid!r} (must be concept-scoped)")
    mp(m.group("c"))
    sfx = m.group("sfx")
    idx_by_sfx[sfx] += 1
    return f"{concept_new}.{sfx}{idx_by_sfx[sfx]}"

# ---------- 3. translate every reference ----------
plan = {k: merged[k] for k in merged if k != "modules"}
plan["ordering"] = "logical"

# root objectives: O{n} / L{n} are NOT renumbered; their tree pointers are
for ob in plan["objectives"]:
    ob["home_topic_id"] = mp(ob["home_topic_id"])
    ob["anchor"] = [mp(a) for a in ob.get("anchor", [])]
OBJ_BY_ID = {o["objective_id"]: o for o in plan["objectives"]}

new_modules = []
for mod in merged["modules"]:
    mod = copy.deepcopy(mod)
    mod["module_id"] = mp(mod["module_id"])
    new_segs = []
    for seg in mod["segments"]:
        seg["segment_id"] = mp(seg["segment_id"])
        # segment-level recalls (none in this chapter, handled defensively): {segment_id}.RQ{n}
        if seg.get("recall_questions"):
            for i, rq in enumerate(seg["recall_questions"], 1):
                rq["id"] = remap_rq(rq["id"], seg["segment_id"], "RQ", i)
                if rq.get("legacy_id"):
                    rq["legacy_id"] = remap_rq(rq["legacy_id"], seg["segment_id"], "TR", i)
        new_tops = []
        for top in seg["topics"]:
            old_t = top["topic_id"]
            top["topic_id"] = mp(old_t)
            top["topic_type"] = TOPIC_TYPE_MAP[top["topic_type"]]
            top["depends_on"] = [mp(x) for x in top.get("depends_on", [])]
            top["source_topic_ids"] = [mp(x) for x in top.get("source_topic_ids", [])]
            for i, rq in enumerate(top.get("recall_questions", []), 1):
                rq["id"] = remap_rq(rq["id"], top["topic_id"], "RQ", i)
                rq["legacy_id"] = remap_rq(rq["legacy_id"], top["topic_id"], "TR", i)
            for oid in top.get("objective_ids", []):
                if oid not in OBJ_BY_ID:
                    raise SystemExit(f"topic {top['topic_id']} points at unknown objective {oid}")
            for lo in top.get("learning_objectives", []):
                reg = OBJ_BY_ID[lo["objective_id"]]
                lo["home_topic_id"] = reg["home_topic_id"]
                lo["anchor"] = list(reg["anchor"])
                if lo["objective_text"] != reg["objective_text"]:
                    raise SystemExit(f"inline objective text drift on {top['topic_id']}")
            for con in top.get("concepts", []):
                con["concept_id"] = mp(con["concept_id"])
                if con["objective_id"] not in OBJ_BY_ID:
                    raise SystemExit(f"concept {con['concept_id']} bad objective")
            concept_new_ids = [c["concept_id"] for c in top.get("concepts", [])]
            per_concept = collections.defaultdict(lambda: collections.defaultdict(int))
            for md in top.get("media", []):
                old_c = md["concept_id"]
                new_c = mp(old_c)
                md["concept_id"] = new_c
                md["home_concept_id"] = mp(md["home_concept_id"])
                md["id"] = remap_media(md["id"], new_c, per_concept[new_c])
                if md.get("objective_id") is not None and md["objective_id"] not in OBJ_BY_ID:
                    raise SystemExit(f"media {md['id']} bad objective")
                if new_c not in concept_new_ids:
                    raise SystemExit(f"media {md['id']} not under its own topic")
            if top.get("2d_tool"):
                td = top["2d_tool"]
                if isinstance(td, dict) and td.get("concept_id"):
                    td["concept_id"] = mp(td["concept_id"])
                if isinstance(td, dict) and td.get("id"):
                    td["id"] = remap_media(td["id"], td["concept_id"],
                                           collections.defaultdict(int))
            new_tops.append(order(top, TOPIC_KEYS, f"topic {top['topic_id']}"))
        seg["topics"] = new_tops
        new_segs.append(order(seg, SEGMENT_KEYS, f"segment {seg['segment_id']}"))
    mod["segments"] = new_segs
    new_modules.append(order(mod, MODULE_KEYS, f"module {mod['module_id']}"))
plan["modules"] = new_modules

# ---------- genre: roster slug (A13 left the emit-time decision here) ----------
GENRE_SLUG = {"સંવાદ": "samvad_nibandh"}
if plan["genre"] in GENRE_SLUG:
    print(f"  genre {plan['genre']!r} -> {GENRE_SLUG[plan['genre']]!r} (roster slug)")
    plan["genre"] = GENRE_SLUG[plan["genre"]]

plan = order(plan, ROOT_KEYS, "root")
assert len(plan) == 32, f"root keys = {len(plan)}"
assert plan["phase"] == 2 and plan["ordering"] == "logical"
assert plan["plan_id"] == f"{plan['chapter_id']}_v{plan['version']}"

# ---------- 4. assert: no id anywhere resolves to a dead node ----------
node_ids, concept_ids, topic_ids = set(), set(), set()
for mod in plan["modules"]:
    node_ids.add(mod["module_id"])
    for seg in mod["segments"]:
        node_ids.add(seg["segment_id"])
        for top in seg["topics"]:
            node_ids.add(top["topic_id"]); topic_ids.add(top["topic_id"])
            for con in top["concepts"]:
                node_ids.add(con["concept_id"]); concept_ids.add(con["concept_id"])

errors = []
# traversal-position check (the validator's own rule)
mi = si = ti = ci = 0
for mod in plan["modules"]:
    mi += 1
    if mod["module_id"] != f"M{mi}": errors.append(f"module {mod['module_id']} != M{mi}")
    for seg in mod["segments"]:
        si += 1
        exp = f"M{mi}.S{si}"
        if seg["segment_id"] != exp: errors.append(f"segment {seg['segment_id']} != {exp}")
        for top in seg["topics"]:
            ti += 1
            expt = f"{exp}.T{ti}"
            if top["topic_id"] != expt: errors.append(f"topic {top['topic_id']} != {expt}")
            for con in top["concepts"]:
                ci += 1
                expc = f"{expt}.C{ci}"
                if con["concept_id"] != expc: errors.append(f"concept {con['concept_id']} != {expc}")
            for rq in top["recall_questions"]:
                if not rq["id"].startswith(top["topic_id"] + ".RQ"): errors.append(f"recall {rq['id']}")
                if not rq["legacy_id"].startswith(top["topic_id"] + ".TR"): errors.append(f"recall legacy {rq['legacy_id']}")
                if ".SR" in rq["id"]: errors.append(f"v1 recall id {rq['id']}")
            for md in top["media"]:
                m = MEDIA_RE.match(md["id"])
                if not m: errors.append(f"media id {md['id']}")
                elif m.group("c") not in concept_ids: errors.append(f"media {md['id']} dead concept")
                if md["concept_id"] not in concept_ids: errors.append(f"media {md['id']} concept_id dead")
                if md["home_concept_id"] not in concept_ids: errors.append(f"media {md['id']} home dead")
            for x in top["depends_on"] + top["source_topic_ids"]:
                if x not in node_ids: errors.append(f"{top['topic_id']} points at dead {x}")
            for oid in top["objective_ids"]:
                if oid not in OBJ_BY_ID: errors.append(f"{top['topic_id']} dead objective {oid}")
for ob in plan["objectives"]:
    if ob["home_topic_id"] not in topic_ids: errors.append(f"{ob['objective_id']} dead home_topic_id")
    for a in ob["anchor"]:
        if a not in concept_ids: errors.append(f"{ob['objective_id']} dead anchor {a}")
for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in OBJ_BY_ID: errors.append(f"strand map {lid} -> dead {oid}")
for ob in plan["objectives"]:
    if plan["strand_to_objective_map"].get(ob["legacy_id"]) != ob["objective_id"]:
        errors.append(f"strand map misses {ob['legacy_id']}")
# every id-shaped token in the whole document must resolve
TOKEN = re.compile(r"M\d+(?:\.S\d+)?(?:\.T\d+)?(?:\.C\d+)?(?:\.(?:IMG|VID|2D|3D|SIM|RQ|TR)\d+)?")
def scan(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items(): scan(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o): scan(v, f"{path}[{i}]")
    elif isinstance(o, str) and re.fullmatch(TOKEN, o):
        base = re.sub(r"\.(?:IMG|VID|2D|3D|SIM|RQ|TR)\d+$", "", o)
        if base not in node_ids: errors.append(f"dangling id {o} at {path}")
if errors:
    print("\n".join(errors)); sys.exit("HARD FAIL: stale references")
scan(plan)
if errors:
    print("\n".join(errors)); sys.exit("HARD FAIL: dangling ids")

# summaries strictly increase (json_contract 8) — report only
for mod in plan["modules"]:
    for seg in mod["segments"]:
        for top in seg["topics"]:
            a, b, c = (len(top["brief_summary"]), len(top["summary"]), len(top["detailed_summary"]))
            if not a < b < c: print(f"  WARN summary tiers {top['topic_id']}: {a},{b},{c}")

json.dump(plan, open(f"{OUT}/learning_plan_logical.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(f"wrote learning_plan_logical.json  modules={len(plan['modules'])} topics={ti} concepts={ci}")

# ---------- 5. covered_by_topics in 10_exercise_solutions.json ----------
ex_path = f"{OUT}/10_exercise_solutions.json"
ex_raw = open(ex_path, encoding="utf-8").read()
ex = json.loads(ex_raw)
changed = 0
for x in ex["exercises"]:
    new = []
    for tid in x["covered_by_topics"]:
        n = mp(tid)
        if n != tid: changed += 1
        new.append(n)
    x["covered_by_topics"] = new
    for t in new:
        if t not in topic_ids: sys.exit(f"HARD FAIL: covered_by_topics {t} dead ({x['exercise_id']})")
if changed:
    json.dump(ex, open(ex_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"rewrote {changed} covered_by_topics ids in 10_exercise_solutions.json")
    open(f"{OUT}/exercise_solutions.json", "w", encoding="utf-8").write(
        open(ex_path, encoding="utf-8").read())
else:
    print("covered_by_topics: renumbering is identity — 10_exercise_solutions.json untouched")
    open(f"{OUT}/exercise_solutions.json", "w", encoding="utf-8").write(ex_raw)
print("wrote exercise_solutions.json (byte copy of 10_exercise_solutions.json)")
