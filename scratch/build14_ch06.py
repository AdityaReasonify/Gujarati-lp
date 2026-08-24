#!/usr/bin/env python3
# Agent 14 — arrange, renumber, translate references, emit learning_plan_logical.json
# plus the covered_by_topics rewrite in 10_exercise_solutions.json, its copy, and the md render.
import json, collections, os, sys, re, shutil

D = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output6/ch06"
OD = collections.OrderedDict

def load(p):
    with open(os.path.join(D, p), encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=OD)

merged = load("13_merged.json")
order  = load("05b_textbook_order.json")

# ---------------------------------------------------------------- 1. arrange
# The reading sequence is the merged tree's own traversal; 05b confirms the printed
# order is identical to it, so no re-arrangement is required.
trav = []
for m in merged["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            trav.append(t["topic_id"])
assert trav == list(order["textbook_order"]), (trav, order["textbook_order"])

# ------------------------------------------------- 2. renumber consecutively
idmap = {}          # old id -> new id, for modules, segments, topics, concepts
mi = si = ti = ci = 0
for m in merged["modules"]:
    mi += 1
    new_m = "M%d" % mi
    idmap[m["module_id"]] = new_m
    for s in m["segments"]:
        si += 1
        new_s = "%s.S%d" % (new_m, si)
        idmap[s["segment_id"]] = new_s
        for t in s["topics"]:
            ti += 1
            new_t = "%s.T%d" % (new_s, ti)
            idmap[t["topic_id"]] = new_t
            for c in t["concepts"]:
                ci += 1
                new_c = "%s.C%d" % (new_t, ci)
                idmap[c["concept_id"]] = new_c

def mid(old):
    if old is None:
        return None
    if old not in idmap:
        sys.exit("STALE REFERENCE: %r resolves to no node" % (old,))
    return idmap[old]

# ------------------------------------------------------ 3. root objectives[]
obj_text = {}
objectives = []
for o in merged["objectives"]:
    n = OD()
    n["objective_id"]  = o["objective_id"]      # O{n} — never renumbered
    n["legacy_id"]     = o["legacy_id"]         # L{n} — moves with its objective
    n["strand"]        = o["strand"]
    n["strand_name"]   = o["strand_name"]
    n["objective_text"] = o["objective_text"]
    n["bloom_level"]   = o["bloom_level"]
    n["home_topic_id"] = mid(o["home_topic_id"])
    n["anchor"]        = [mid(a) for a in o["anchor"]]
    n["status"]        = o["status"]
    n["theme_category"] = o.get("theme_category")
    obj_text[o["objective_id"]] = o["objective_text"]
    objectives.append(n)
obj_ids = {o["objective_id"] for o in objectives}

TOPIC_TYPE = {"POEM": "instructional", "STORY_TELLING": "instructional",
              "CONCEPT": "instructional", "REVIEW": "summary",
              "EXERCISE": "assessment"}

TOPIC_KEYS = ["topic_id", "topic_name", "topic_type", "topic_category", "difficulty",
              "original_chunk", "modified_chunk", "word_count", "explanation",
              "real_life_example", "brief_summary", "summary", "detailed_summary",
              "key_terms", "concept_bullets", "important_points", "figures_of_speech",
              "rhyme_scheme", "shabdarth", "samanarthi", "vilom", "vyakaran",
              "objective_ids", "learning_objectives", "concepts", "recall_questions",
              "media", "2d_tool", "publication_text", "publication_chunk", "depends_on",
              "source_topic_ids", "estimated_exchanges", "primary_content_type",
              "secondary_content_type", "tertiary_content_type", "available_content_types"]
MEDIA_KEYS = ["id", "type", "subtype", "title", "description", "image_url", "aspect_ratio",
              "concept_id", "home_concept_id", "objective_id", "image_category",
              "teaching_notes", "negative_prompt", "generation_prompt"]

warn = []
media_re = re.compile(r"^(M\d+\.S\d+\.T\d+\.C\d+)\.(IMG|VID|2D|3D|SIM)(\d+)$")

def build_lo(o):
    n = OD()
    for k in ["objective_id", "legacy_id", "strand", "strand_name", "objective_text",
              "bloom_level"]:
        n[k] = o[k]
    n["home_topic_id"] = mid(o["home_topic_id"])
    n["anchor"] = [mid(a) for a in o["anchor"]]
    n["status"] = o["status"]
    n["theme_category"] = o.get("theme_category")
    n["image_examples"] = o.get("image_examples", []) or []
    # keep the inline mirror identical to the registry, character for character
    if n["objective_text"] != obj_text[n["objective_id"]]:
        warn.append("inline objective_text for %s differed from the registry; "
                    "registry text kept" % n["objective_id"])
        n["objective_text"] = obj_text[n["objective_id"]]
    return n

modules = []
for m in merged["modules"]:
    nm = OD()
    nm["module_id"]   = mid(m["module_id"])
    nm["module_name"] = m["module_name"]
    nm["difficult_words"] = m.get("difficult_words", [])
    nm["overall_rhyme_scheme"] = m.get("overall_rhyme_scheme")
    segs = []
    for s in m["segments"]:
        ns = OD()
        ns["segment_id"]   = mid(s["segment_id"])
        ns["segment_name"] = s["segment_name"]
        if s.get("recall_questions"):
            rqs = []
            for i, r in enumerate(s["recall_questions"], 1):
                nr = OD(r)
                nr["id"] = "%s.RQ%d" % (ns["segment_id"], i)   # RQ, never SR
                if "legacy_id" in nr:
                    nr["legacy_id"] = "%s.TR%d" % (ns["segment_id"], i)
                rqs.append(nr)
            ns["recall_questions"] = rqs
        tops = []
        for t in s["topics"]:
            nt = OD()
            new_t = mid(t["topic_id"])
            for k in TOPIC_KEYS:
                if k not in t:
                    if k in ("figures_of_speech", "key_terms", "concept_bullets",
                             "important_points", "depends_on", "source_topic_ids",
                             "media", "available_content_types", "shabdarth",
                             "samanarthi", "vilom", "vyakaran"):
                        nt[k] = []
                    else:
                        nt[k] = None
                    warn.append("topic %s had no %s; emitted as default" % (new_t, k))
                    continue
                nt[k] = t[k]
            nt["topic_id"]   = new_t
            nt["topic_type"] = TOPIC_TYPE[t["topic_type"]]
            nt["depends_on"] = [mid(x) for x in (t.get("depends_on") or [])]
            nt["source_topic_ids"] = [mid(x) for x in (t.get("source_topic_ids") or [])]
            for oid in nt["objective_ids"]:
                if oid not in obj_ids:
                    sys.exit("topic %s points at unknown objective %s" % (new_t, oid))
            nt["learning_objectives"] = [build_lo(o) for o in t["learning_objectives"]]

            cons = []
            for c in t["concepts"]:
                nc = OD()
                nc["concept_id"]   = mid(c["concept_id"])
                nc["concept_name"] = c["concept_name"]
                nc["objective_id"] = c["objective_id"]
                if nc["objective_id"] not in obj_ids:
                    sys.exit("concept %s points at unknown objective %s"
                             % (nc["concept_id"], nc["objective_id"]))
                nc["key_terms"] = c.get("key_terms", [])
                nc["content"]   = c["content"]
                if not nc["content"]:
                    sys.exit("concept %s has empty content[]" % nc["concept_id"])
                cons.append(nc)
            nt["concepts"] = cons

            rqs = []
            for i, r in enumerate(t.get("recall_questions") or [], 1):
                nr = OD()
                nr["id"]         = "%s.RQ%d" % (new_t, i)
                nr["legacy_id"]  = "%s.TR%d" % (new_t, i)
                for k in ["prompt", "answer", "difficulty", "bloom_level"]:
                    nr[k] = r.get(k)
                rqs.append(nr)
            nt["recall_questions"] = rqs

            meds = []
            for md in (t.get("media") or []):
                nmd = OD()
                for k in MEDIA_KEYS:
                    nmd[k] = md.get(k)
                mm = media_re.match(md["id"])
                if not mm:
                    sys.exit("media id %r is not concept-scoped" % md["id"])
                nmd["id"] = "%s.%s%s" % (mid(mm.group(1)), mm.group(2), mm.group(3))
                nmd["concept_id"]      = mid(md["concept_id"])
                nmd["home_concept_id"] = mid(md["home_concept_id"]) \
                    if md.get("home_concept_id") else nmd["concept_id"]
                if not nmd["image_url"] and not nmd["generation_prompt"]:
                    warn.append("media %s has neither image_url nor generation_prompt"
                                % nmd["id"])
                meds.append(nmd)
            nt["media"] = meds
            tops.append(nt)
        ns["topics"] = tops
        segs.append(ns)
    nm["segments"] = segs
    modules.append(nm)

# ------------------------------------------------------------- 4. root fields
grade = merged["grade"]
unit  = merged["unit_number"]
chapter_id = "gseb_eng_gujarati%d_ch%d" % (grade, unit)      # PROVISIONAL — VERIFY-1
version = merged.get("version", 1)

plan = OD()
plan["phase"]            = 2
plan["board"]            = "gseb"
plan["subject"]          = merged["subject"]
plan["grade"]            = grade
plan["level"]            = merged["level"]
plan["version"]          = version
plan["ordering"]         = "logical"
plan["author"]           = merged.get("author", "")
plan["chapter_id"]       = chapter_id
plan["plan_id"]          = "%s_v%d" % (chapter_id, version)
plan["chapter_name"]     = merged["chapter_name"]
plan["unit_title"]       = merged["unit_title"]
plan["unit_number"]      = unit
plan["topic_title"]      = merged["topic_title"]
plan["topic_number"]     = merged["topic_number"]
plan["genre"]            = "mahitiprad_gadya"   # roster slug; samvad_nibandh is the second gate
plan["teaching_lens"]    = merged["teaching_lens"]
plan["guiding_question"] = merged["guiding_question"]
plan["textbook"]         = merged["textbook"]
plan["textbook_url"]     = merged["textbook_url"]
plan["textbook_pages"]   = merged["textbook_pages"]
plan["_activate"]        = False
plan["medium_id"]        = None                 # server-injected
plan["subject_ref_id"]   = None                 # server-injected
plan["publication_id"]   = merged["publication_id"]
plan["chapter_master_id"] = merged["chapter_master_id"]
plan["estimated_time"]   = merged["estimated_time"]
plan["english_plan_id"]  = None
plan["english_chapter_id"] = None
plan["objectives"]       = objectives
plan["strand_to_objective_map"] = merged["strand_to_objective_map"]
plan["modules"]          = modules

ROOT32 = ["board", "genre", "grade", "level", "phase", "author", "modules", "plan_id",
          "subject", "version", "ordering", "textbook", "_activate", "medium_id",
          "chapter_id", "objectives", "unit_title", "topic_title", "unit_number",
          "chapter_name", "textbook_url", "topic_number", "teaching_lens",
          "estimated_time", "publication_id", "subject_ref_id", "textbook_pages",
          "english_plan_id", "guiding_question", "chapter_master_id",
          "english_chapter_id", "strand_to_objective_map"]
assert set(plan.keys()) == set(ROOT32), (set(plan) ^ set(ROOT32))
assert len(plan) == 32

# ------------------------------------------------- 5. assert: nothing is stale
nodes = set()
for m in plan["modules"]:
    nodes.add(m["module_id"])
    for s in m["segments"]:
        nodes.add(s["segment_id"])
        for t in s["topics"]:
            nodes.add(t["topic_id"])
            for c in t["concepts"]:
                nodes.add(c["concept_id"])
errs = []
def need(x, where):
    if x not in nodes:
        errs.append("%s -> %s" % (where, x))

for o in plan["objectives"]:
    need(o["home_topic_id"], "objectives[%s].home_topic_id" % o["objective_id"])
    for a in o["anchor"]:
        need(a, "objectives[%s].anchor" % o["objective_id"])
for lid, oid in plan["strand_to_objective_map"].items():
    if oid not in obj_ids:
        errs.append("strand_to_objective_map[%s] -> %s" % (lid, oid))
for o in plan["objectives"]:
    if o["legacy_id"] not in plan["strand_to_objective_map"]:
        errs.append("strand_to_objective_map is missing %s" % o["legacy_id"])

mi = si = ti = ci = 0
for m in plan["modules"]:
    mi += 1
    assert m["module_id"] == "M%d" % mi, m["module_id"]
    for s in m["segments"]:
        si += 1
        assert s["segment_id"] == "M%d.S%d" % (mi, si), s["segment_id"]
        for r in s.get("recall_questions", []):
            assert r["id"].startswith(s["segment_id"] + ".RQ"), r["id"]
        for t in s["topics"]:
            ti += 1
            assert t["topic_id"] == "%s.T%d" % (s["segment_id"], ti), t["topic_id"]
            assert t["topic_type"] in ("instructional", "summary", "assessment")
            assert t["original_chunk"] and t["original_chunk"].strip()
            assert t["concepts"]
            for x in t["depends_on"]:
                need(x, "%s.depends_on" % t["topic_id"])
            for x in t["source_topic_ids"]:
                need(x, "%s.source_topic_ids" % t["topic_id"])
            for lo in t["learning_objectives"]:
                need(lo["home_topic_id"], "%s.learning_objectives.home_topic_id" % t["topic_id"])
                for a in lo["anchor"]:
                    need(a, "%s.learning_objectives.anchor" % t["topic_id"])
                assert lo["objective_text"] == obj_text[lo["objective_id"]]
            for c in t["concepts"]:
                ci += 1
                assert c["concept_id"] == "%s.C%d" % (t["topic_id"], ci), c["concept_id"]
            for r in t["recall_questions"]:
                assert r["id"].startswith(t["topic_id"] + ".RQ"), r["id"]
                assert r["legacy_id"].startswith(t["topic_id"] + ".TR"), r["legacy_id"]
            for md in t["media"]:
                mm = media_re.match(md["id"])
                assert mm, md["id"]
                need(mm.group(1), "media %s" % md["id"])
                need(md["concept_id"], "media %s .concept_id" % md["id"])
                need(md["home_concept_id"], "media %s .home_concept_id" % md["id"])
            # three-tier summaries strictly increase
            a, b, c2 = (len(t["brief_summary"] or ""), len(t["summary"] or ""),
                        len(t["detailed_summary"] or ""))
            if not (a < b < c2):
                warn.append("topic %s summaries do not strictly increase (%d/%d/%d)"
                            % (t["topic_id"], a, b, c2))

if errs:
    sys.exit("STALE REFERENCES:\n  " + "\n  ".join(errs))

with open(os.path.join(D, "learning_plan_logical.json"), "w", encoding="utf-8") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)
    f.write("\n")

# ------------------------------- 6. covered_by_topics rewrite + exercise copy
ex = load("10_exercise_solutions.json")
changed = 0
for e in ex["exercises"]:
    old = e.get("covered_by_topics") or []
    new = [mid(x) for x in old]
    if new != old:
        changed += 1
    e["covered_by_topics"] = new
ex["plan_id"] = plan["plan_id"]
ex["chapter_id"] = plan["chapter_id"]
with open(os.path.join(D, "10_exercise_solutions.json"), "w", encoding="utf-8") as f:
    json.dump(ex, f, ensure_ascii=False, indent=2)
    f.write("\n")
shutil.copyfile(os.path.join(D, "10_exercise_solutions.json"),
                os.path.join(D, "exercise_solutions.json"))

print("topics=%d concepts=%d media=%d objectives=%d covered_rewrites=%d"
      % (ti, ci, sum(len(t["media"]) for m in plan["modules"] for s in m["segments"]
                     for t in s["topics"]), len(objectives), changed))
for w in warn:
    print("WARN:", w)
