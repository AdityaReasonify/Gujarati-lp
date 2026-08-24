#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload composed collages to `learning_plan_assets` and record the real publicUrls.

Same call and same bucket as classes 6 and 7 (`POST /api/topics/upload` via lp_sync's ApiClient);
the grade comes from the plan rather than a hardcoded constant.

**This uploads a named list, not a folder.** The class-6/7 uploaders glob `*.png` out of the
staging directory, which is safe only when one build owns that directory. It is not safe here:
on 2026-08-10 another build staged class-10 ch1/ch11/ch13 into the same tree while this work was
in progress, and a glob would have published someone else's in-flight assets under this run's
name. So the file list is derived from each chapter's `_collage.json` — exactly the media ids
this build composed, and nothing else. A staged file with no authored panels is reported and
skipped, never uploaded.

The bucket holds nothing from LP v1, so the 2026-08-04 overwrite — six live images destroyed
because a build wrote onto an id-based path inside v1's `topic-content-images`, with bucket
versioning off — cannot repeat here. The source frames live in that v1 bucket and are only READ.

What IS overwritten is this project's own earlier single-frame asset at the same media-id path.
That is deliberate: the plan's `image_url` then needs no change at all, so a half-finished run
leaves live plans pointing at valid images either way.

    python <script> ch04 [--dry-run]
    python <script>                  # every chapter with a _collage.json
"""
from __future__ import annotations

import io
import json
import os
import pathlib
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collage_build as cb  # noqa: E402

GCS_REL = "V2/cbse/cbse/english/class_%d/hindi/ch_%d"


def cli(base: str, argv=None):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    argv = list(sys.argv[1:] if argv is None else argv)
    dry = "--dry-run" in argv
    named = [a for a in argv if not a.startswith("-")]

    lp = os.path.abspath(os.path.join(base, "..", "..", "learning_plan_upload"))
    sys.path.insert(0, os.path.join(lp, "src"))
    from lp_sync.api_client import ApiClient      # noqa: E402
    from lp_sync.config import load_settings      # noqa: E402

    cfg = load_settings()
    bucket = cfg.bucket_name
    client = None if dry else ApiClient(cfg.base_url)

    have = cb.chapter_dirs(base)
    by_no = {int(re.fullmatch(r"ch(\d+)", d).group(1)): d for d in have}
    if named:
        chapters = [by_no[int(re.sub(r"\D", "", a))] for a in named]
    else:
        chapters = [d for d in have
                    if os.path.exists(os.path.join(base, d, "_collage.json"))]

    grand = skipped = 0
    for d in chapters:
        cdir = os.path.join(base, d)
        n = int(re.fullmatch(r"ch(\d+)", d).group(1))
        spec_path = os.path.join(cdir, "_collage.json")
        if not os.path.exists(spec_path):
            print("%-6s no _collage.json — not this build's chapter, skipped" % d)
            skipped += 1
            continue
        spec = json.load(open(spec_path, encoding="utf-8"))
        authored = {k for k in spec if not k.startswith("_")}
        plan = json.load(open(os.path.join(cdir, "learning_plan_logical.json"),
                              encoding="utf-8"))
        rel = GCS_REL % (plan["grade"], n)
        img_dir = os.path.join(cb.lp_data_root(base), rel, "image")

        wanted = []
        for t in cb.topics_of(plan):
            if t["topic_id"] not in authored:
                continue
            m = cb.image_media(t)
            f = os.path.join(img_dir, m["id"] + ".png")
            if not os.path.exists(f):
                raise SystemExit("%s %s: %s was never composed — run the builder first"
                                 % (d, t["topic_id"], os.path.basename(f)))
            wanted.append((m["id"], f))

        on_disk = {os.path.splitext(f)[0] for f in os.listdir(img_dir)
                   if f.endswith(".png")}
        extra = sorted(on_disk - {i for i, _ in wanted})
        print("== %s (class %d)  %d composites -> gs://%s/%s/image"
              % (d, plan["grade"], len(wanted), bucket, rel))
        if extra:
            print("   %d other file(s) in this folder are NOT part of this build and are "
                  "left alone: %s" % (len(extra), ", ".join(extra[:4])
                                      + (" …" if len(extra) > 4 else "")))

        urls_path = os.path.join(cdir, "_collage_urls.json")
        urls = json.load(open(urls_path, encoding="utf-8")) \
            if os.path.exists(urls_path) else {}
        for mid, f in wanted:
            kb = os.path.getsize(f) / 1024
            if dry:
                print("   would upload %-24s %6.0f KB" % (mid, kb))
                continue
            # lp_sync's upload_asset reads `.name` off its first argument — it takes a Path,
            # not a str. The class-6/7 uploaders got Paths for free from Path.glob(); this one
            # builds its list by media id, so the conversion has to be explicit.
            urls[mid] = client.upload_asset(pathlib.Path(f), rel + "/image", bucket)
            print("   %-24s %6.0f KB  -> %s" % (mid, kb, urls[mid]))
        grand += len(wanted)

        if not dry:
            json.dump(urls, open(urls_path, "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
            print("   wrote %s" % urls_path)

    print("\n%s %d composites across %d chapters%s"
          % ("DRY RUN —" if dry else "DONE —", grand, len(chapters) - skipped,
             "  (%d chapter(s) skipped)" % skipped if skipped else ""))
