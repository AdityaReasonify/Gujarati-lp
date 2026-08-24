#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Give classes 8 and 9 their own copy of the LP-v1 art they currently borrow.

    python _migrate_v2.py output8            # whole grade
    python _migrate_v2.py output9 ch06       # one chapter
    python _migrate_v2.py output8 --dry-run  # list what would move, touch nothing

Classes 6 and 7 own their art: every image sits in `learning_plan_assets` under
`V2/cbse/cbse/english/class_{N}/hindi/ch_{n}/image/{media_id}.png`, named by the phase-2
concept-scoped media id. Classes 8 and 9 were built by reusing LP-v1 frames **in place**, so
their plans point into `topic-content-images/Grade_N/…/{frame_id}.png` — art the plan borrows
rather than owns, and which breaks the moment v1 is moved or renumbered.

What this does, per chapter:

  1. reads `learning_plan_logical.json` and finds every media node still on `topic-content-images`
  2. downloads those bytes
  3. re-uploads each one to the chapter's own V2 folder under its **media id**
  4. writes `_v2_image_urls.json` — {media_id: publicUrl} exactly as the server returned it

Re-running `content.py` then picks that file up through `assemble.load_v2_urls()`, so a rebuild
cannot revert the plan to the v1 paths. The plan itself is not touched here; run content.py and
`_upload9.py` / `_upload8.py` afterwards.

**Direction matters, and it is one-way.** This only ever READS `topic-content-images` and only
ever WRITES `learning_plan_assets`. It never writes to the v1 bucket. That is deliberate: the
2026-08-04 incident destroyed six live images because a build wrote onto an id-based path inside
`topic-content-images`, and that bucket has versioning off with no generation to roll back to.
The v1 originals are left exactly where they are — this makes a copy, it does not move anything.

Empty `image_url`s (authored prompts awaiting generation) are skipped and counted; they have no
source to copy. `EMPTY_IMAGE_URLS_class6_to_9.md` is the worklist for those.
"""
import io
import json
import os
import re
import sys
import glob
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
LP = HERE.parent / "learning_plan_upload"
sys.path.insert(0, str(LP / "src"))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from lp_sync.api_client import ApiClient          # noqa: E402
from lp_sync.config import load_settings          # noqa: E402

DRY = "--dry-run" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("-")]
if not args:
    sys.exit(__doc__)
BASE = args[0]
ONLY = set(args[1:])

GRADE = {"output": 6, "output7": 7, "output8": 8, "output9": 9}[BASE]
V1_HOST_MARK = "topic-content-images"
FOLDER = "V2/cbse/cbse/english/class_%d/hindi/ch_%d/image"

STAGE = Path(os.environ.get("TEMP", "/tmp")) / "v2_migrate" / BASE
STAGE.mkdir(parents=True, exist_ok=True)

cfg = load_settings()
BUCKET = cfg.bucket_name
client = None if DRY else ApiClient(cfg.base_url)


def fetch(url, dest):
    """Download once; a staged file is reused so a re-run after a failure is cheap."""
    if dest.exists() and dest.stat().st_size > 0:
        return dest.stat().st_size
    req = urllib.request.Request(url, headers={"User-Agent": "lp-migrate/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    if not data:
        raise IOError("empty body from %s" % url)
    dest.write_bytes(data)
    return len(data)


chapters = sorted(glob.glob(str(HERE / BASE / "ch*" / "learning_plan_logical.json")),
                  key=lambda p: int(re.search(r"ch0*(\d+)", p).group(1)))

grand_moved = grand_empty = grand_already = 0
for path in chapters:
    chdir = Path(path).parent
    if ONLY and chdir.name not in ONLY:
        continue
    n = int(re.search(r"ch0*(\d+)", chdir.name).group(1))
    plan = json.load(open(path, encoding="utf-8"))

    todo, empty, already = [], 0, 0
    for m in plan.get("modules", []):
        for s in m.get("segments", []):
            for t in s.get("topics", []):
                for im in t.get("media", []):
                    url = im.get("image_url") or ""
                    if not url:
                        empty += 1
                    elif V1_HOST_MARK in url:
                        todo.append((im["id"], url))
                    else:
                        already += 1

    folder = FOLDER % (GRADE, n)
    print("\n== %s  %s" % (chdir.name, plan.get("chapter_name", "")))
    print("   %d to copy · %d already V2 · %d empty (no source)" % (len(todo), already, empty))
    if not todo:
        grand_empty += empty
        grand_already += already
        continue
    print("   -> gs://%s/%s" % (BUCKET, folder))

    out_path = chdir / "_v2_image_urls.json"
    urls = json.load(open(out_path, encoding="utf-8")) if out_path.exists() else {}

    for media_id, src in todo:
        if media_id in urls:
            print("   %-22s already migrated" % media_id)
            continue
        name = "%s.png" % media_id
        staged = STAGE / chdir.name / name
        staged.parent.mkdir(parents=True, exist_ok=True)
        if DRY:
            print("   %-22s <- %s" % (media_id, src.rsplit("/", 1)[-1]))
            continue
        size = fetch(src, staged)
        public = client.upload_asset(staged, folder, BUCKET, dest_filename=name)
        urls[media_id] = public
        print("   %-22s %6.0f KB  -> %s" % (media_id, size / 1024, public))

    if not DRY:
        json.dump(urls, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("   wrote %s  (%d entries)" % (out_path.name, len(urls)))

    grand_moved += len(todo)
    grand_empty += empty
    grand_already += already

print("\n%s  copied %d · already V2 %d · empty %d"
      % ("DRY RUN —" if DRY else "DONE —", grand_moved, grand_already, grand_empty))
if not DRY:
    print("Next: re-run each chapter's content.py, then _upload%d.py to push the new URLs live."
          % GRADE)
