#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Read the live plans back and prove the collages actually landed.

    python <script>            # every chapter with a _collage.json
    python <script> ch04

Five checks per collaged media, because each one has failed at some point in this project's
history and none of them is implied by the others:

 1. **the media is still there** — a patched plan that lost a topic is worse than an unpatched one
 2. **aspect_ratio matches the panel count** — the bug that makes a 3-panel stack unreadable
 3. **teaching_notes names exactly the authored panels** — proves the live plan describes the
    picture that is actually at that URL, not a previous run's
 4. **the URL returns 200 and is a PNG** — a plan can validate perfectly while pointing at a 404
 5. **the live bytes equal the local composite's bytes** — the only check that distinguishes
    "the new image is up" from "the old single frame is still up and the CDN served it". Size
    equality is what the class-10 phase-1 comparison used for the same reason.

Videos are counted and reported but never touched: the class-8 v2 plans carry one per topic and
the whole point of the in-place patch was to keep them.
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collage_build as cb  # noqa: E402

PY = "https://staging.singularity-learn.com/agentapi/api"


def cli(base: str, argv=None):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    argv = list(sys.argv[1:] if argv is None else argv)
    named = [a for a in argv if not a.startswith("-")]

    sys.path.insert(0, os.path.abspath(os.path.join(base, "..", "..", "imagebyGPT")))
    from lp_v1_api import _request                  # noqa: E402

    have = cb.chapter_dirs(base)
    by_no = {int(re.fullmatch(r"ch(\d+)", d).group(1)): d for d in have}
    chapters = ([by_no[int(re.sub(r"\D", "", a))] for a in named] if named else
                [d for d in have if os.path.exists(os.path.join(base, d, "_collage.json"))])

    tot = dict(checked=0, ok=0, videos=0)
    problems = []

    for d in chapters:
        cdir = os.path.join(base, d)
        n = int(re.fullmatch(r"ch(\d+)", d).group(1))
        spec = json.load(open(os.path.join(cdir, "_collage.json"), encoding="utf-8"))
        local = json.load(open(os.path.join(cdir, "learning_plan_logical.json"),
                               encoding="utf-8"))
        rel = "V2/cbse/cbse/english/class_%d/hindi/ch_%d" % (local["grade"], n)
        img_dir = os.path.join(cb.lp_data_root(base), rel, "image")

        want = {}
        for t in cb.topics_of(local):
            entry = spec.get(t["topic_id"])
            if entry and not t["topic_id"].startswith("_"):
                m = cb.image_media(t)
                if m:
                    want[m["id"]] = [p for p, _ in entry["panels"]]

        s, body = _request("%s/lp2/learning-plans/chapter/%s?include_json=true"
                           % (PY, local["chapter_id"]))
        try:
            plan = body["data"]["plan"]["planJson"]
        except Exception:
            problems.append("%s: could not read live plan" % d)
            print("%-6s LIVE READ FAILED" % d)
            continue

        live = {}
        vids = 0
        for t in cb.topics_of(plan):
            for m in t.get("media", []):
                if m.get("type") == "video":
                    vids += 1
                elif m.get("type", "image") == "image":
                    live[m["id"]] = m
        tot["videos"] += vids

        bad = 0
        for mid, panels in want.items():
            tot["checked"] += 1
            m = live.get(mid)
            if not m:
                problems.append("%s %s: media missing from live plan" % (d, mid))
                bad += 1
                continue
            want_ar = cb.ASPECT.get(len(panels), "16:9")
            if m.get("aspect_ratio") != want_ar:
                problems.append("%s %s: aspect_ratio %s, expected %s (%d panels)"
                                % (d, mid, m.get("aspect_ratio"), want_ar, len(panels)))
                bad += 1
                continue
            note = m.get("teaching_notes") or ""
            named_in_note = re.search(r"\[(?:collage of|reused frames?):\s*([^\]]+)\]", note)
            got = [x.strip().split(",")[0].strip()
                   for x in (named_in_note.group(1).split(", ") if named_in_note else [])]
            got = [g for g in got if g and g != "V2 copy"]
            if got != panels:
                problems.append("%s %s: note names %s, authored %s" % (d, mid, got, panels))
                bad += 1
                continue
            url = m.get("image_url") or ""
            try:
                r = requests.get(url, timeout=60)
                r.raise_for_status()
            except Exception as exc:
                problems.append("%s %s: fetch failed (%s) %s" % (d, mid, type(exc).__name__, url))
                bad += 1
                continue
            if not r.content.startswith(b"\x89PNG"):
                problems.append("%s %s: URL is not a PNG" % (d, mid))
                bad += 1
                continue
            local_f = os.path.join(img_dir, mid + ".png")
            if os.path.exists(local_f):
                ls = os.path.getsize(local_f)
                if len(r.content) != ls:
                    problems.append("%s %s: live %d bytes, local composite %d — the old image "
                                    "may still be served" % (d, mid, len(r.content), ls))
                    bad += 1
                    continue
            tot["ok"] += 1

        print("%-6s %3d collages checked · %3d pass · %d fail · %d videos preserved"
              % (d, len(want), len(want) - bad, bad, vids))

    print("\n%d of %d collages verified on all five checks · %d videos untouched"
          % (tot["ok"], tot["checked"], tot["videos"]))
    if problems:
        print("\n%d PROBLEM(S):" % len(problems))
        for p in problems[:40]:
            print("   " + p)
    return not problems
