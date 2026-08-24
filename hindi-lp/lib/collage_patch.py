#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch LIVE plans so their media describe the composites, without touching anything else.

    python <script> --dry-run     # show every change, write nothing
    python <script>               # patch, validate, re-upload
    python <script> ch02 ch05     # just these

Why this fetches the live plan instead of uploading the one in this repo
-----------------------------------------------------------------------
For nine of the ten class-8 chapters the plan this repo builds is **not** the live plan. On
2026-08-07 someone uploaded a `…_chN_v2` of each that adds a video per topic; those are
`is_active = True` and our v1s are inactive. Class-10 ch8 is in the same shape. Re-uploading the
local plan would take those videos out of circulation while reporting `success: true`.

So this does the opposite of a rebuild: it **fetches whatever is live**, edits only the two
fields a collage changes, and puts it back under the same plan_id. Videos, topics, text, and
every other byte pass through untouched. This is `output8/_patch_v2_images.py` generalised —
that script fixed `image_url`; this one fixes what the composites changed.

What actually changes, and what deliberately does not
-----------------------------------------------------
* `aspect_ratio` — a 2-panel stack is 3:4, a 3-panel stack 9:16, a 2x2 grid 1:1. Leaving these
  at 16:9 makes the player letterbox a tall image into a wide box and the panels go unreadable.
* `teaching_notes` — the old `[reused frame: X, V2 copy]` stamp becomes the panel-order sentence
  plus `[collage of: …]`. The teacher-facing sentence in front of it is preserved; it was
  authored per topic and says something the panel note does not.
* `image_url` — **not touched.** The composite was uploaded to the same media-id path the plan
  already points at, so the URL is correct by construction. Rewriting it would mean asserting a
  URL rather than reading one, which is how the class-8/9 plans ended up pointing into the v1
  bucket in the first place.

Guards, because this writes to live plans:

  * only `type == "image"` media are considered; a video URL is never touched
  * only media ids whose topic has authored panels are considered
  * an id that is missing from the live plan is reported, not silently skipped
  * a media already carrying the right aspect_ratio and note is counted as a no-op
  * the plan is validated after patching and is not uploaded if validation fails
  * `--dry-run` prints the full before/after for every change
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collage_build as cb  # noqa: E402

PY = "https://staging.singularity-learn.com/agentapi/api"

# Stamp the edit. Every Hindi plan uploaded before 2026-08-07 left `created_by` null, which is
# exactly why those v2 uploads could not be traced to anyone. 199 = prince+1@reasonify.in.
CREATED_BY = os.environ.get("LP_CREATED_BY", "199")


def cli(base: str, argv=None):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    argv = list(sys.argv[1:] if argv is None else argv)
    dry = "--dry-run" in argv
    named = [a for a in argv if not a.startswith("-")]

    imagebygpt = os.path.abspath(os.path.join(base, "..", "..", "imagebyGPT"))
    sys.path.insert(0, imagebygpt)
    sys.path.insert(0, os.path.join(base, "..", "lib"))
    import assemble                                 # noqa: E402
    from lp_v1_api import _request                  # noqa: E402

    have = cb.chapter_dirs(base)
    by_no = {int(re.fullmatch(r"ch(\d+)", d).group(1)): d for d in have}
    chapters = ([by_no[int(re.sub(r"\D", "", a))] for a in named] if named else
                [d for d in have if os.path.exists(os.path.join(base, d, "_collage.json"))])

    tot_changed = tot_noop = tot_missing = 0
    uploaded, failed = [], []

    for d in chapters:
        cdir = os.path.join(base, d)
        spec_path = os.path.join(cdir, "_collage.json")
        if not os.path.exists(spec_path):
            print("%-6s no _collage.json — not this build's chapter, skipped" % d)
            continue
        urls_path = os.path.join(cdir, "_collage_urls.json")
        if not os.path.exists(urls_path):
            print("%-6s no _collage_urls.json — composites not uploaded yet, skipped" % d)
            continue
        spec = json.load(open(spec_path, encoding="utf-8"))
        uploaded_ids = set(json.load(open(urls_path, encoding="utf-8")))

        local = json.load(open(os.path.join(cdir, "learning_plan_logical.json"),
                               encoding="utf-8"))
        # media id -> panels, via the local plan's topic->media mapping. The id is
        # concept-scoped and the concept counter is chapter-continuous, so it cannot be
        # derived from the topic id alone.
        want = {}
        for t in cb.topics_of(local):
            entry = spec.get(t["topic_id"])
            if not entry or t["topic_id"].startswith("_"):
                continue
            m = cb.image_media(t)
            if m and m["id"] in uploaded_ids:
                want[m["id"]] = [p for p, _ in entry["panels"]]

        cid = local["chapter_id"]
        s, body = _request("%s/lp2/learning-plans/chapter/%s?include_json=true" % (PY, cid))
        try:
            plan = body["data"]["plan"]["planJson"]
            meta = body["data"]["plan"]
        except Exception:
            print("%-6s could not read live plan: %s" % (d, str(body)[:160]))
            failed.append(d)
            continue

        print("\n=== %s  live plan %s  version %s  active %s"
              % (d, plan.get("plan_id"), meta.get("version"), meta.get("isActive")))

        changed = noop = 0
        seen = set()
        for t in cb.topics_of(plan):
            for m in t.get("media", []):
                if m.get("type", "image") != "image":
                    continue                       # never touch a video/tool entry
                panels = want.get(m["id"])
                if not panels:
                    continue
                seen.add(m["id"])
                new_ar = cb.ASPECT.get(len(panels), "16:9")
                new_note = cb.panel_note(m.get("teaching_notes", ""), panels)
                if m.get("aspect_ratio") == new_ar and m.get("teaching_notes") == new_note:
                    noop += 1
                    continue
                if dry:
                    print("   %-22s %d panels" % (m["id"], len(panels)))
                    print("      aspect  - %s\n              + %s"
                          % (m.get("aspect_ratio"), new_ar))
                    print("      note    - %s\n              + %s"
                          % ((m.get("teaching_notes") or "")[-90:], new_note[-90:]))
                m["aspect_ratio"] = new_ar
                m["teaching_notes"] = new_note
                changed += 1

        missing = [k for k in want if k not in seen]
        for k in missing:
            print("   MISSING in live plan: %s" % k)

        print("   %d to change · %d already correct · %d in map but absent from plan"
              % (changed, noop, len(missing)))
        tot_changed += changed
        tot_noop += noop
        tot_missing += len(missing)

        if dry or not changed:
            continue

        tmp = os.path.join(cdir, "_patched_live_plan.json")
        json.dump(plan, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        if not assemble.validate(tmp, imagebygpt=imagebygpt):
            print("   VALIDATION FAILED — not uploading")
            failed.append(d)
            continue
        ok = assemble.upload(tmp, chapter_master_id=plan["chapter_master_id"],
                             activate=True, imagebygpt=imagebygpt, force=True,
                             created_by=CREATED_BY)
        (uploaded if ok else failed).append(d)

    print("\n%s  changed %d · already correct %d · absent %d"
          % ("DRY RUN —" if dry else "DONE —", tot_changed, tot_noop, tot_missing))
    if uploaded:
        print("   uploaded: %s" % " ".join(uploaded))
    if failed:
        print("   FAILED:   %s" % " ".join(failed))
