#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print a chapter's topics with their full original_chunk. Authoring aid, nothing more.

    python lib/_chunks.py output8/ch02
"""
import io, json, os, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
d = sys.argv[1]
p = json.load(open(os.path.join(d, "learning_plan_logical.json"), encoding="utf-8"))
print("%s — %s (class %d)" % (d, p.get("chapter_name"), p["grade"]))
for m in p["modules"]:
    for s in m["segments"]:
        for t in s["topics"]:
            im = next((x for x in t.get("media", []) if x.get("type", "image") == "image"), None)
            tag = "" if im and im.get("image_url") else "   [no art]"
            print("\n%s  %s%s" % (t["topic_id"], t.get("topic_name"), tag))
            print("   " + (t.get("original_chunk") or "").strip().replace("\n", "\n   "))
