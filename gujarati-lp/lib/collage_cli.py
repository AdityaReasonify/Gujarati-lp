#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The command line the class-8/9/10 collage builders share.

    <script> ch04 ch05        # compose those chapters + write review sheets
    <script>                  # every chapter that has a _collage.json
    <script> --seed ch04      # write a starting _collage.json from the anchor frames
    <script> --sheet ch04     # print the frame sheet an author picks panels from
    <script> --repoint        # patch the built plans to the composites (after upload)
    <script> --no-compose     # skip compositing; useful with --repoint alone
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collage_build as cb  # noqa: E402


def _sheet(cdir, full=False):
    """Topics on the left, the whole frame pool on the right — one screen to author from."""
    plan = json.load(open(os.path.join(cdir, "learning_plan_logical.json"), encoding="utf-8"))
    pool = json.load(open(os.path.join(cdir, "_images.json"), encoding="utf-8"))
    ch = os.path.basename(cdir)
    print("=" * 100)
    print("%s  %s   (class %d, %d frames in pool)"
          % (ch, plan.get("chapter_name", ""), plan["grade"], len(pool)))
    print("=" * 100)

    print("\n--- topics to author, with the frame each already shows ---")
    for t in cb.topics_of(plan):
        m = cb.image_media(t)
        if not m:
            print("  %-14s %-40s (no media — image-free by design)"
                  % (t["topic_id"], (t.get("topic_name") or "")[:40]))
            continue
        if not m.get("image_url"):
            print("  %-14s %-40s (EMPTY image_url — awaiting generation, skip)"
                  % (t["topic_id"], (t.get("topic_name") or "")[:40]))
            continue
        chunk = (t.get("original_chunk") or "").strip().replace("\n", " / ")
        print("  %-14s %-40s anchor=%s" % (t["topic_id"], (t.get("topic_name") or "")[:40],
                                           cb.anchor_of(m)))
        print("        %s" % (chunk if full else chunk[:150] + ("…" if len(chunk) > 150 else "")))

    print("\n--- %d frames in the pool: name -> what it depicts ---" % len(pool))
    for k, v in pool.items():
        desc = v.get("title") or ""
        prm = v.get("prompt") or ""
        if prm:
            desc = ("%s — %s" % (desc, prm)) if desc else prm
        print("  %-22s %s" % (k, desc if full else desc[:150] + ("…" if len(desc) > 150 else "")))
    print("\npanel names for _collage.json = the left column above\n")


def cli(base: str, argv=None):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    argv = list(sys.argv[1:] if argv is None else argv)
    flags = {a for a in argv if a.startswith("-")}
    named = [a for a in argv if not a.startswith("-")]

    # ch4 and ch04 both name the same chapter; resolve against what is actually on disk
    have = cb.chapter_dirs(base)
    by_no = {int(re.fullmatch(r"ch(\d+)", d).group(1)): d for d in have}
    if named:
        chapters = []
        for a in named:
            n = int(re.sub(r"\D", "", a))
            if n not in by_no:
                raise SystemExit("no built chapter %s under %s" % (a, base))
            chapters.append(by_no[n])
    else:
        chapters = [d for d in have
                    if os.path.exists(os.path.join(base, d, "_collage.json"))
                    or "--seed" in flags]

    for d in chapters:
        cdir = os.path.join(base, d)
        n = int(re.fullmatch(r"ch(\d+)", d).group(1))
        if "--sheet" in flags:
            _sheet(cdir, full="--full" in flags)
            continue
        if "--seed" in flags:
            spec = cb.seed_spec(cdir)
            if spec is None:
                print("%-6s no _images.json — no art to reuse, nothing to collage" % d)
                continue
            if not spec:
                print("%-6s every image_url is empty — awaiting generation, skipped" % d)
                continue
            out = os.path.join(cdir, "_collage.json")
            if os.path.exists(out) and "--force" not in flags:
                print("%-6s _collage.json exists — not overwriting (use --force)" % d)
                continue
            json.dump(spec, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            blank = sum(1 for v in spec.values() if not v["panels"])
            print("%-6s seeded %d topics -> %s%s"
                  % (d, len(spec), out, "  (%d with no resolvable anchor)" % blank if blank else ""))
            continue
        print("==", d)
        cb.build(cdir, n, compose="--no-compose" not in flags,
                 repoint="--repoint" in flags, quiet="--quiet" in flags)
