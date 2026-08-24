#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared phase-2 collage builder — the class-6/7 build behaviour, minus the copy-paste.

`output/_build_collages.py` (class 6) and `output7/_build_collages7.py` (class 7) are two copies
of one algorithm that differ in three places: how a panel name resolves to a URL, where the
chapter directory lives, and how the grade is discovered. Classes 8, 9 and 10 would have made
five copies of it, so the algorithm moved here and the per-class scripts became argument lists.
The two existing scripts are deliberately left alone — they are shipped and verified, and
rewriting them to prove a refactor is how a working chapter breaks.

Everything the copies agreed on is preserved exactly:

  * **Letterbox, never crop** and **Devanagari ordinal badges** — inherited from `collage.py`.
  * **Both guards.** A topic with an image but no authored panels fails the run; a topic that is
    image-free by design but has panels authored also fails. Each has already caught a real
    mistake (ch11's mistyped module numbers, ch2's डाँडी-गोथा topics).
  * **Panels are named, never scored.** Scoring a chapter-wide pool put stanza 4's waterfalls on
    stanza 5. The panel list is authored per topic and this file only resolves it.
  * **Write the URL the server returned.** `--repoint` reads `_collage_urls.json`; it warns and
    falls back to the constructed path rather than pretending a guess is a fact.

What is new here, and only because classes 8-10 need it:

  * **`anchor_of()`** — the frame a topic already uses, parsed out of its `teaching_notes`
    `[reused frame: X, V2 copy]` stamp. Classes 8, 9 and 10 all shipped one frame per topic and
    recorded which, so panel 1 of every authored list is already known and does not have to be
    rediscovered. `seed_spec()` turns that into a starting `_collage.json`.
  * **Chapter directories are matched loosely.** Classes 6-9 use `ch04`; class 10 uses `ch4`.
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collage  # noqa: E402

GCS_REL = "V2/cbse/cbse/english/class_%d/hindi/ch_%d"
CDN = "https://media.singularity-learn.com/learning_plan_assets/%s/image/%s.png"
PANEL_NOTE = "पैनल क्रम से पढ़वाइए — बैज १ २ ३ पढ़ने का क्रम बताते हैं."

# `[reused frame: M1.S1.T2.O1.E4, V2 copy]` (classes 8/9) or `[reused frame: scene_04_img_01]`
# (class 10). The comma-tail is optional because class 10 never had a V2 copy to stamp.
ANCHOR = re.compile(r"\[reused frames?:\s*([^,\]]+?)\s*(?:,[^\]]*)?\]")
ASPECT = {1: "16:9", 2: "3:4", 3: "9:16", 4: "1:1"}


def lp_data_root(here: str) -> str:
    return os.path.abspath(os.path.join(here, "..", "..", "learning_plan_upload", "data"))


def chapter_dirs(base: str):
    """Every chapter directory holding a built plan, in chapter order. ch04 and ch4 both match."""
    out = []
    for d in os.listdir(base):
        m = re.fullmatch(r"ch(\d+)", d)
        if m and os.path.exists(os.path.join(base, d, "learning_plan_logical.json")):
            out.append((int(m.group(1)), d))
    return [d for _, d in sorted(out)]


def topics_of(plan):
    return [t for m in plan["modules"] for s in m["segments"] for t in s["topics"]]


def anchor_of(media) -> str | None:
    """The single frame this media already shows, as recorded when it was first attached."""
    m = ANCHOR.search(media.get("teaching_notes") or "")
    return m.group(1).strip() if m else None


def image_media(topic):
    """The topic's image media, if any. A video in the same list is never a collage target."""
    for m in topic.get("media", []):
        if m.get("type", "image") == "image":
            return m
    return None


# ------------------------------------------------------------------ seeding an authored file
def seed_spec(cdir: str):
    """A `_collage.json` skeleton: every image-bearing topic, its anchor frame as panel 1.

    This is a starting point for authoring, not an answer. It encodes only what is already true —
    which frame the topic shows today — so that the authoring pass adds beats rather than
    re-deriving the one that was already chosen and verified.

    Returns None for a chapter with no frame pool at all. Class 9's ch04 (the लता मंगेशकर
    interview) is the real case: all 16 of its topics carry an authored `generation_prompt` and
    an empty `image_url`, and the old cut left no art behind to reuse. There is nothing to
    collage there, and saying so is different from failing.
    """
    plan = json.load(open(os.path.join(cdir, "learning_plan_logical.json"), encoding="utf-8"))
    ipath = os.path.join(cdir, "_images.json")
    if not os.path.exists(ipath):
        return None
    pool = json.load(open(ipath, encoding="utf-8"))
    spec = {}
    for t in topics_of(plan):
        m = image_media(t)
        if not m or not m.get("image_url"):
            continue                       # empty slot awaiting generation — nothing to collage
        a = anchor_of(m)
        title = (pool.get(a) or {}).get("title", "") if a else ""
        spec[t["topic_id"]] = {"why": "", "panels": [[a, title]] if a and a in pool else []}
    return spec


# ------------------------------------------------------------------------------- the build
def build(cdir: str, ch_no: int, compose=True, repoint=False, quiet=False):
    spec = json.load(open(os.path.join(cdir, "_collage.json"), encoding="utf-8"))
    pool = json.load(open(os.path.join(cdir, "_images.json"), encoding="utf-8"))
    plan_path = os.path.join(cdir, "learning_plan_logical.json")
    plan = json.load(open(plan_path, encoding="utf-8"))
    grade = plan["grade"]
    rel = GCS_REL % (grade, ch_no)

    topics = topics_of(plan)
    by_id = {t["topic_id"]: t for t in topics}
    authored = {k: v for k, v in spec.items() if not k.startswith("_")}

    unknown = sorted(set(authored) - set(by_id))
    if unknown:
        raise SystemExit("%s: _collage.json names topics not in the plan: %s"
                         % (os.path.basename(cdir), unknown))

    # A topic whose image_url is empty has no art to composite; it is not "image-bearing" for
    # the purposes of the guards, or every chapter with a pending generation would fail to build.
    with_media = {t["topic_id"] for t in topics
                  if (image_media(t) or {}).get("image_url")}
    missing = sorted(with_media - set(authored))
    if missing:
        raise SystemExit("%s: these topics have an image but no panels authored: %s"
                         % (os.path.basename(cdir), missing))
    intruder = sorted(set(authored) - with_media)
    if intruder:
        raise SystemExit("%s: these topics are image-free by design — remove their panels "
                         "from _collage.json: %s" % (os.path.basename(cdir), intruder))
    for tid, entry in authored.items():
        if not entry.get("panels"):
            raise SystemExit("%s %s: authored with zero panels" % (os.path.basename(cdir), tid))
        for pid, _ in entry["panels"]:
            if pid not in pool:
                raise SystemExit("%s %s: panel '%s' is not in _images.json — re-run the "
                                 "pull, or fix the id" % (os.path.basename(cdir), tid, pid))
        seen = [p for p, _ in entry["panels"]]
        if len(set(seen)) != len(seen):
            raise SystemExit("%s %s: the same frame appears twice: %s"
                             % (os.path.basename(cdir), tid, seen))

    out_dir = os.path.join(lp_data_root(os.path.dirname(cdir)), rel, "image")
    cache = os.path.join(cdir, "_src_cache")
    urls_path = os.path.join(cdir, "_collage_urls.json")
    known = json.load(open(urls_path, encoding="utf-8")) if os.path.exists(urls_path) else {}

    rows, total, panels_used = [], 0, 0
    for tid in [t["topic_id"] for t in topics if t["topic_id"] in authored]:
        entry, topic = authored[tid], by_id[tid]
        media_id = image_media(topic)["id"]
        srcs = [pool[p]["url"] for p, _ in entry["panels"]]
        out = os.path.join(out_dir, media_id + ".png")
        if compose:
            collage.compose(srcs, out, cache_dir=cache)
        size = os.path.getsize(out)
        total += size
        panels_used += len(srcs)
        url = known.get(media_id) or CDN % (rel, media_id)
        if repoint and media_id not in known:
            print("   WARNING %s: no uploaded URL on record, using constructed path" % media_id)
        rows.append({"tid": tid, "media_id": media_id, "name": topic["topic_name"],
                     "why": entry.get("why", ""), "panels": entry["panels"],
                     "kb": size / 1024, "local": out, "url": url})
        if not quiet:
            print("   %-14s %-24s %d panels  %6.0f KB"
                  % (tid, media_id, len(srcs), size / 1024))

    write_review(cdir, os.path.basename(cdir), plan, rows)

    if repoint:
        patch = {r["media_id"]: r for r in rows}
        for fname in ("learning_plan_logical.json", "learning_plan_textbook.json"):
            fpath = os.path.join(cdir, fname)
            if not os.path.exists(fpath):
                continue
            doc = plan if fname == "learning_plan_logical.json" else \
                json.load(open(fpath, encoding="utf-8"))
            done = 0
            for t in topics_of(doc):
                for m in t.get("media", []):
                    r = patch.get(m["id"])
                    if not r or m.get("type", "image") != "image":
                        continue
                    m["image_url"] = r["url"]
                    m["aspect_ratio"] = ASPECT.get(len(r["panels"]), "16:9")
                    m["teaching_notes"] = panel_note(m.get("teaching_notes", ""), r["panels"])
                    done += 1
            json.dump(doc, open(fpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print("   repointed %d media entries in %s" % (done, fname))

    dist = {}
    for r in rows:
        dist[len(r["panels"])] = dist.get(len(r["panels"]), 0) + 1
    print("   %s: %d collages, %d panels, %.1f MB, avg %.0f KB  [%s]"
          % (os.path.basename(cdir), len(rows), panels_used, total / 1048576,
             total / 1024 / max(1, len(rows)),
             " ".join("%dp:%d" % (k, dist[k]) for k in sorted(dist))))
    return rows


def panel_note(note: str, panels) -> str:
    """Rewrite the media's stamp for a composite, idempotently.

    The old `[reused frame: X, V2 copy]` stamp is replaced rather than appended to — re-running
    a build must not grow the note each time — but the teacher-facing sentence in front of it is
    always kept, because it was authored per topic and says something the panel note does not.

    `panels` may be the authored `[id, title]` pairs or a bare list of ids; the builder has the
    titles to hand and the live-plan patcher does not, and the note only ever uses the ids.
    """
    ids = [p[0] if isinstance(p, (list, tuple)) else p for p in panels]
    body = (note or "").split(PANEL_NOTE)[0]
    body = re.sub(r"\s*\[(reused frames?|collage of):[^\]]*\]", "", body).rstrip()
    if len(ids) == 1:
        return "%s [reused frame: %s, V2 copy]" % (body, ids[0])
    return "%s %s [collage of: %s]" % (body, PANEL_NOTE, ", ".join(ids))


def write_review(cdir, ch, plan, rows):
    by_id = {t["topic_id"]: t for t in topics_of(plan)}
    h = ["<!doctype html><meta charset='utf-8'><title>%s collages</title>" % ch,
         "<style>body{font-family:Nirmala UI,Segoe UI,sans-serif;max-width:1100px;",
         "margin:2rem auto;padding:0 1rem;line-height:1.6}",
         "h1{border-bottom:3px solid #d6cebe;padding-bottom:.3rem}",
         "section{display:grid;grid-template-columns:1fr 340px;gap:1.5rem;",
         "border-top:1px solid #e5e0d5;padding:1.5rem 0}",
         "img{width:100%;border:1px solid #d6cebe;border-radius:8px}",
         "pre{white-space:pre-wrap;background:#fdfbf5;padding:.8rem;border-radius:6px;",
         "border:1px solid #eee6d8;font-family:inherit;font-size:.95rem}",
         ".why{color:#6b5f4a;font-style:italic}.meta{color:#8a8071;font-size:.85rem}",
         "code{background:#f4f0e6;padding:1px 5px;border-radius:3px}</style>",
         "<h1>%s — %s <small>(class %d)</small></h1>"
         % (ch, plan.get("chapter_name", ""), plan["grade"]),
         "<p class='meta'>%d collages. कुछ भी upload नहीं हुआ — यह जाँच के लिए है।</p>"
         % len(rows)]
    for r in rows:
        t = by_id[r["tid"]]
        srcs = "<br>".join("%d <code>%s</code> — %s" % (i + 1, f, d)
                           for i, (f, d) in enumerate(r["panels"]))
        h.append("<section><div><h3>%s — %s</h3>" % (r["tid"], r["name"]))
        h.append("<pre>%s</pre>" % (t.get("original_chunk") or ""))
        h.append("<p class='why'>%s</p>" % r["why"])
        h.append("<p class='meta'>%s<br><br><code>%s</code> · %.0f KB</p>"
                 % (srcs, r["media_id"], r["kb"]))
        h.append("</div><div><img src='%s'></div></section>"
                 % os.path.relpath(r["local"], cdir).replace("\\", "/"))
    p = os.path.join(cdir, "collage_review.html")
    io.open(p, "w", encoding="utf-8").write("\n".join(h))
    print("   review: %s" % p)
