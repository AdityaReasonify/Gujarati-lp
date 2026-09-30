import json

BASE = "/Users/aditya/Downloads/Gujarati-lp/gujarati-lp/output8/ch10"

# Recover the same old->new topic map used for the logical plan (identity here,
# but load from the renumbered file to stay generically correct).
merged_before = json.load(open(f"{BASE}/13_merged.json", encoding="utf-8"))
merged_after = json.load(open(f"{BASE}/_tmp_renumbered.json", encoding="utf-8"))

old_topic_ids = []
new_topic_ids = []
for mb, ma in zip(merged_before["modules"], merged_after["modules"]):
    for sb, sa in zip(mb["segments"], ma["segments"]):
        for tb, ta in zip(sb["topics"], sa["topics"]):
            old_topic_ids.append(tb["topic_id"])
            new_topic_ids.append(ta["topic_id"])
topic_map = dict(zip(old_topic_ids, new_topic_ids))
print("topic_map identity?", all(k == v for k, v in topic_map.items()))

# ---------- rewrite covered_by_topics inside 10_exercise_solutions.json ----------
ex_doc = json.load(open(f"{BASE}/10_exercise_solutions.json", encoding="utf-8"))

all_new_topic_ids = set(new_topic_ids)
changed = 0
for ex in ex_doc["exercises"]:
    cbt = ex.get("covered_by_topics") or []
    new_cbt = []
    for tid in cbt:
        new_tid = topic_map.get(tid)
        if new_tid is None:
            raise SystemExit(f"covered_by_topics id {tid!r} on {ex['exercise_id']} does not resolve to any known topic")
        if new_tid != tid:
            changed += 1
        new_cbt.append(new_tid)
    ex["covered_by_topics"] = new_cbt

# also rewrite unmapped[].exercise_id topic refs? unmapped entries reference exercise_id/reason only,
# no topic ids to rewrite. Leave as-is.

print(f"covered_by_topics entries rewritten: {changed} (0 expected under identity mapping)")

# assert every covered_by_topics id resolves against the final logical plan's topic set
final_plan = json.load(open(f"{BASE}/learning_plan_logical.json", encoding="utf-8"))
final_topic_ids = set()
for m in final_plan["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            final_topic_ids.add(t["topic_id"])

for ex in ex_doc["exercises"]:
    for tid in ex.get("covered_by_topics") or []:
        if tid not in final_topic_ids:
            raise SystemExit(f"post-rewrite covered_by_topics id {tid} not present in learning_plan_logical.json")

json.dump(ex_doc, open(f"{BASE}/10_exercise_solutions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("rewrote 10_exercise_solutions.json in place (covered_by_topics)")

# ---------- copy to exercise_solutions.json (the Phase-7 deliverable name) ----------
json.dump(ex_doc, open(f"{BASE}/exercise_solutions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("wrote exercise_solutions.json")
