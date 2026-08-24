# -*- coding: utf-8 -*-
import json, re, sys, collections
D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch01/"
p = json.load(open(D + "learning_plan_logical.json", encoding="utf-8"))
ex = json.load(open(D + "10_exercise_solutions.json", encoding="utf-8"))
fail = []
def chk(cond, msg):
    if not cond: fail.append(msg)

ROOT32 = set("""board genre grade level phase author modules plan_id subject version ordering
textbook _activate medium_id chapter_id objectives unit_title topic_title unit_number
chapter_name textbook_url topic_number teaching_lens estimated_time publication_id
subject_ref_id textbook_pages english_plan_id guiding_question chapter_master_id
english_chapter_id strand_to_objective_map""".split())
chk(set(p.keys()) == ROOT32, "root keys mismatch: extra %s missing %s"
    % (sorted(set(p)-ROOT32), sorted(ROOT32-set(p))))
chk(len(p) == 32, "root key count %d" % len(p))
chk(p["phase"] == 2, "phase")
chk(p["ordering"] == "logical", "ordering")
chk(p["chapter_id"] == "gseb_eng_gujarati%s_ch%s" % (p["grade"], p["unit_number"]), "chapter_id form")
chk(p["plan_id"] == "%s_v%s" % (p["chapter_id"], p["version"]), "plan_id form")
chk("_standard_" not in p["plan_id"], "plan_id has _standard_")
chk(p["english_plan_id"] is None and p["english_chapter_id"] is None, "english twin not null")
chk(p["subject_ref_id"] is None and p["medium_id"] is None, "server-injected not null")
chk(p["_activate"] is False, "_activate")

# ---- traversal + id grammar ----
node_ids, topic_ids, concept_ids = set(), set(), set()
mi = si = ti = ci = 0
for m in p["modules"]:
    mi += 1
    chk(m["module_id"] == "M%d" % mi, "module id %s at %d" % (m["module_id"], mi))
    node_ids.add(m["module_id"])
    for s in m["segments"]:
        si += 1
        want = "M%d.S%d" % (mi, si)
        chk(s["segment_id"] == want, "segment %s expected %s" % (s["segment_id"], want))
        node_ids.add(s["segment_id"])
        for q in s.get("recall_questions", []):
            chk(re.match(r"^%s\.RQ\d+$" % re.escape(s["segment_id"]), q["id"]),
                "segment recall id %s" % q["id"])
        for t in s["topics"]:
            ti += 1
            wt = "%s.T%d" % (want, ti)
            chk(t["topic_id"] == wt, "topic %s expected %s" % (t["topic_id"], wt))
            node_ids.add(t["topic_id"]); topic_ids.add(t["topic_id"])
            chk(t["topic_type"] in ("instructional", "summary", "assessment"),
                "topic_type %s" % t["topic_type"])
            chk(len(t) == len([k for k in t]), "dup")
            chk(bool(t["original_chunk"].strip()), "empty original_chunk %s" % wt)
            chk(re.search(r"[઀-૿]", t["original_chunk"]), "no gujarati %s" % wt)
            chk(len(t["concepts"]) >= 1, "no concepts %s" % wt)
            for c in t["concepts"]:
                ci += 1
                wc = "%s.C%d" % (wt, ci)
                chk(c["concept_id"] == wc, "concept %s expected %s" % (c["concept_id"], wc))
                node_ids.add(c["concept_id"]); concept_ids.add(c["concept_id"])
                chk(bool(c["content"]), "empty concept content %s" % wc)
            for q in t["recall_questions"]:
                chk(re.match(r"^%s\.RQ\d+$" % re.escape(wt), q["id"]), "topic recall id %s" % q["id"])
                if "legacy_id" in q:
                    chk(re.match(r"^%s\.TR\d+$" % re.escape(wt), q["legacy_id"]),
                        "recall legacy_id %s" % q["legacy_id"])
            for md in t["media"]:
                chk(re.match(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)\d+$", md["id"]),
                    "media id %s" % md["id"])
                chk(md["id"].rsplit(".", 1)[0] in concept_ids, "media concept scope %s" % md["id"])
                chk(md.get("concept_id") in concept_ids, "media concept_id %s" % md["id"])
                chk(md.get("home_concept_id") in concept_ids, "media home_concept_id %s" % md["id"])
                chk(bool(md.get("image_url")) or bool(md.get("generation_prompt")),
                    "media both empty %s" % md["id"])

# ---- objectives registry ----
reg = {o["objective_id"]: o for o in p["objectives"]}
chk(len(reg) == len(p["objectives"]), "duplicate objective_id")
for o in p["objectives"]:
    chk(re.match(r"^O\d+$", o["objective_id"]), "objective_id form %s" % o["objective_id"])
    chk(o["home_topic_id"] in topic_ids, "stale home_topic_id %s" % o["home_topic_id"])
    for a in o["anchor"]:
        chk(a in node_ids, "stale anchor %s (O=%s)" % (a, o["objective_id"]))
    chk("image_examples" not in o, "root objective carries image_examples")
for lg, oid in p["strand_to_objective_map"].items():
    chk(oid in reg, "strand map -> unknown %s" % oid)
chk(set(p["strand_to_objective_map"].keys()) == set(o["legacy_id"] for o in p["objectives"]),
    "strand map does not cover every legacy_id")

# ---- topic-level references + inline mirror ----
for m in p["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            for oid in t["objective_ids"]:
                chk(oid in reg, "stale objective_ids %s on %s" % (oid, t["topic_id"]))
            chk([o["objective_id"] for o in t["learning_objectives"]] == t["objective_ids"],
                "inline mirror != objective_ids on %s" % t["topic_id"])
            for o in t["learning_objectives"]:
                r = reg[o["objective_id"]]
                chk(o["objective_text"] == r["objective_text"],
                    "mirror text drift %s" % o["objective_id"])
                chk(o["home_topic_id"] == r["home_topic_id"] and o["anchor"] == r["anchor"],
                    "mirror anchor drift %s" % o["objective_id"])
                chk("image_examples" in o, "inline mirror missing image_examples")
            for d in t["depends_on"]:
                chk(d in node_ids, "stale depends_on %s on %s" % (d, t["topic_id"]))
            for d in t["source_topic_ids"]:
                chk(d in node_ids, "stale source_topic_ids %s on %s" % (d, t["topic_id"]))
            for c in t["concepts"]:
                chk(c["objective_id"] in reg, "concept objective_id %s" % c["objective_id"])
            # summaries strictly increase
            a, b, cc = t["brief_summary"], t["summary"], t["detailed_summary"]
            chk(len(a) < len(b) < len(cc), "summaries not increasing on %s (%d/%d/%d)"
                % (t["topic_id"], len(a), len(b), len(cc)))

# ---- exercise deliverable ----
for e in ex["exercises"]:
    for tid in e.get("covered_by_topics") or []:
        chk(tid in topic_ids, "exercise %s -> stale topic %s" % (e["exercise_id"], tid))

# ---- no authored enum leaked ----
blob = json.dumps(p, ensure_ascii=False)
for bad in ('"POEM"', '"STORY_TELLING"', '"CONCEPT"', '"REVIEW"', '.SR1', '.SR2'):
    chk(bad not in blob, "leaked %s" % bad)

# ---- no forbidden numbered display text ----
NUMPAT = re.compile(r"(કડી|પ્રશ્ન|સ્વાધ્યાય|ટૉપિક|ટોપિક)\s*[0-9૦-૯]")
def scan(o, path):
    if isinstance(o, str):
        if NUMPAT.search(o): fail.append("numbered display text at %s: %s" % (path, o[:60]))
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in ("topic_id","segment_id","module_id","concept_id","id","legacy_id",
                     "home_topic_id","anchor","objective_ids","depends_on","source_topic_ids",
                     "textbook_pages","textbook_url","textbook","chapter_id","plan_id"): continue
            scan(v, path + "/" + k)
    elif isinstance(o, list):
        for i, v in enumerate(o): scan(v, path + "[%d]" % i)
scan(p, "")

print("topics=%d segments=%d modules=%d concepts=%d objectives=%d"
      % (ti, si, mi, ci, len(reg)))
if fail:
    print("FAIL (%d)" % len(fail))
    for f in fail: print("  -", f)
    sys.exit(1)
print("ALL ASSERTIONS PASS")
