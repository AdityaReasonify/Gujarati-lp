#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared phase-2 assembler for the Hindi pack.

A chapter supplies a content module (see output/ch05/content.py); this turns it into the two
plan orderings, 01_meta.json, and runs the local QC. Shape authority is
reference/phase2_contract.md — in particular the four rules the server rejected on the first run:

  publication_id must not be null · segment recalls are .RQ{n} not .SR{n}
  topic_type ∈ {instructional, summary, assessment} · concept numbers are CHAPTER-continuous
"""
import json
import os
import re
import sys

STRAND, STRAND_NAME = "L", "भाषा एवं साहित्य"

# the server's closed enum — literary विधा lives in root.genre, never here
TOPIC_TYPE = {"POEM": "instructional", "CONCEPT": "instructional",
              "STORY_TELLING": "instructional", "REVIEW": "summary",
              "EXERCISE": "assessment"}

NEG = ("photorealistic faces, anime style, western-only setting, Roman script labels, "
       "watermark, blurry, cluttered background, anachronistic objects")


def _words(s):
    return len([w for w in re.split(r"\s+", s or "") if w])


PANEL_NOTE = "पैनल क्रम से पढ़वाइए — बैज १ २ ३ पढ़ने का क्रम बताते हैं."


def load_collages(outdir="."):
    """Optional collage overlay for a chapter -> {topic_id: {url, panels}}.

    Needs BOTH files and they must agree, so a plan can never point at an image that was not
    uploaded:
      _collage.json       authored topic_id -> panels, in reading order
      _collage_urls.json  the publicUrls the server returned for those composites

    A topic listed in _collage.json whose image has not been uploaded yet is skipped with a
    warning and keeps its single anchor frame — a half-applied overlay is worse than none.
    See reference/collage_media.md.
    """
    spec_p = os.path.join(outdir, "_collage.json")
    urls_p = os.path.join(outdir, "_collage_urls.json")
    if not (os.path.exists(spec_p) and os.path.exists(urls_p)):
        return {}
    spec = json.load(open(spec_p, encoding="utf-8"))
    urls = json.load(open(urls_p, encoding="utf-8"))
    out = {}
    for tid, entry in spec.items():
        if tid.startswith("_"):
            continue
        panels = [f for f, _ in entry["panels"]]
        # media id is concept-scoped and the concept counter is chapter-continuous, so it
        # cannot be derived from the topic id alone — match on the id's topic prefix.
        hit = [k for k in urls if k.startswith(tid + ".C")]
        if not hit:
            print("   collage overlay: %s has panels but no uploaded image — keeping the "
                  "single frame" % tid)
            continue
        out[tid] = {"url": urls[hit[0]], "panels": panels}
    return out


def load_v2_urls(outdir="."):
    """Optional V2-asset overlay for a chapter -> {media_id: publicUrl}.

    Classes 6 and 7 own their art: every image sits under `learning_plan_assets/V2/…` at its
    concept-scoped media id. Classes 8 and 9 were built by reusing LP-v1 frames *in place*, so
    their plans pointed into `topic-content-images/Grade_N/…` under a v1 frame id — art the
    plan borrows rather than owns, and which breaks the moment v1 is moved or renumbered.

    `_migrate_v2.py` copies each borrowed frame to the chapter's own V2 folder and writes the
    publicUrls the server returned into `_v2_image_urls.json`. This hook makes `content.py`
    pick them up, so re-running a build cannot revert the plan to the v1 paths.

    The map is keyed by **media id** (`M1.S1.T1.C1.IMG1`), not by frame id: one v1 frame may be
    reused by two chapters, and each chapter gets its own copy at its own address.
    """
    p = os.path.join(outdir, "_v2_image_urls.json")
    if not os.path.exists(p):
        return {}
    return json.load(open(p, encoding="utf-8"))


def build_topic(t, seq, frames, cstart, collages=None, v2urls=None):
    """seq drives O{n}; cstart is the running CHAPTER-continuous concept number.

    A topic normally holds one concept. It may hold several when the passage genuinely moves in
    separable steps and must still stay one topic — a सूरदास पद is one continuous utterance that
    may not be split into topics (profiles/genres/bhakti_pad.md), but its argument moves in four
    turns, and the concept layer is where those turns belong.
    """
    oid = f"O{seq}"
    fr = frames[t["frame"]] if t.get("frame") else None

    parts = t.get("concepts")
    if not parts:                                    # the ordinary one-concept topic
        parts = [{"name": t["cname"], "blocks": [
            {"type": "paragraph", "text": t["expl"], "publication_text": t["expl"]},
            {"type": "paragraph", "text": t["rle"], "publication_text": t["rle"]},
            {"type": "list", "items": t["cb"]}]}]

    concepts, cid = [], None
    for i, p in enumerate(parts):
        n = cstart + i
        this_cid = f"{t['tid']}.C{n}"
        if cid is None:
            cid = this_cid                            # media and the anchor hang off the first
        concepts.append({"concept_id": this_cid, "concept_name": p["name"],
                         "objective_id": oid,
                         "key_terms": p.get("key_terms", t["kt"]),
                         "content": p["blocks"]})

    obj = {"objective_id": oid, "legacy_id": f"L{seq}", "strand": STRAND,
           "strand_name": STRAND_NAME, "objective_text": t["obj"],
           "bloom_level": t.get("bloom", "Understand"), "home_topic_id": t["tid"],
           "anchor": [cid], "theme_category": None}

    media = []
    if not fr and t.get("gen"):
        # No existing frame depicts this scene, so a prompt is authored and image_url stays ""
        # for a later generation pass (agents/09_media_planning.md). Class 8 needs this: eight of
        # its ten chapters carry an appended reading block whose scenes the old art never covered
        # — the आठवीं का झरोखे से was not in the cut those frames were drawn for.
        media.append({
            "id": f"{cid}.IMG1", "type": "image", "subtype": "illustration",
            "title": t["cname"], "description": t["bs"],
            "image_url": "", "aspect_ratio": "16:9",
            "concept_id": cid, "home_concept_id": cid, "objective_id": None,
            "image_category": "illustration",
            "teaching_notes": t.get("tn", "चित्र बनने तक पंक्तियाँ पढ़वाकर पूछिए कि बच्चों "
                                          "के मन में कौन-सा दृश्य बना।"),
            "negative_prompt": NEG, "generation_prompt": t["gen"]})
    if fr:
        note = t.get("tn", "चित्र दिखाकर पाठ पढ़वाइए, फिर पूछिए कि चित्र में कौन-सी "
                           "पंक्ति दिखाई दे रही है।")
        url, aspect = fr["url"], "16:9"
        v2 = (v2urls or {}).get(f"{cid}.IMG1")
        if v2:                    # this chapter's own V2 copy of the borrowed v1 frame
            url = v2
        col = (collages or {}).get(t["tid"])
        if col:                                   # this topic's slot holds a composite
            url = col["url"]
            aspect = {2: "3:4", 3: "9:16"}.get(len(col["panels"]), "16:9")
            note += " " + PANEL_NOTE + " [collage of: %s]" % ", ".join(col["panels"])
        elif v2:
            note += f" [reused frame: {fr['src_id']}, V2 copy]"
        else:
            note += f" [reused frame: {fr['src_id']}]"
        media.append({
            "id": f"{cid}.IMG1", "type": "image", "subtype": "illustration",
            "title": fr["title"], "description": t["bs"],
            "image_url": url, "aspect_ratio": aspect,
            "concept_id": cid, "home_concept_id": cid, "objective_id": None,
            "image_category": "illustration",
            "teaching_notes": note,
            "negative_prompt": NEG, "generation_prompt": ""})

    rqb = t.get("rq_bloom", ["remember", "understand", "analyze"])
    rqs = [{"id": f"{t['tid']}.RQ{i}", "legacy_id": f"{t['tid']}.TR{i}",
            "prompt": p, "answer": a, "difficulty": d,
            "bloom_level": rqb[i - 1] if i - 1 < len(rqb) else "understand"}
           for i, (p, a, d) in enumerate(t["rq"], 1)]

    topic = {
        "topic_id": t["tid"], "topic_name": t["name"],
        "topic_type": TOPIC_TYPE[t.get("ttype", "POEM")],
        "topic_category": t.get("cat", "core"), "difficulty": t.get("diff", "easy"),
        "original_chunk": t["chunk"], "modified_chunk": t["mod"],
        "word_count": {"original": _words(t["chunk"])},
        "explanation": t["expl"], "real_life_example": t["rle"],
        "brief_summary": t["bs"], "summary": t["sm"], "detailed_summary": t["ds"],
        "key_terms": t["kt"], "concept_bullets": t["cb"], "important_points": t["cb"],
        "figures_of_speech": t.get("fos", []), "rhyme_scheme": t.get("rhyme"),
        # भाषा-बोध — the Hindi counterpart of the English pack's simile/metaphor block.
        # अलंकार already lives in figures_of_speech; these four complete it.
        "shabdarth": t.get("shabdarth", []),      # glossary: शब्द / अर्थ / प्रकार
        "samanarthi": t.get("samanarthi", []),    # समानार्थी शब्द
        "vilom": t.get("vilom", []),              # विलोम शब्द
        "vyakaran": t.get("vyakaran", []),        # व्याकरण-बिंदु
        "objective_ids": [oid],
        "learning_objectives": [dict(obj, image_examples=[])],
        "concepts": concepts,
        "recall_questions": rqs, "media": media, "2d_tool": None,
        "publication_text": t["expl"], "publication_chunk": t["expl"],
        "depends_on": [], "source_topic_ids": [], "estimated_exchanges": "4",
        "primary_content_type": "image" if media else None,
        "secondary_content_type": None, "tertiary_content_type": None,
        "available_content_types": ["image"] if media else [],
    }
    return topic, dict(obj, status="taught"), len(concepts)


def build(spec, order):
    by_id = {t["tid"]: t for t in spec["topics"]}
    built, objectives = {}, []
    collages = spec.get("collages") or {}
    v2urls = spec.get("v2urls") or {}
    cnext = 1                                            # concept numbers run across the chapter
    for seq, t in enumerate(spec["topics"], 1):          # registry always in logical order
        node, reg, ncon = build_topic(t, seq, spec["frames"], cnext, collages, v2urls)
        cnext += ncon
        built[t["tid"]] = node
        objectives.append(reg)

    # Segments and modules follow `order` too, not their declaration order. Without this a
    # topic cannot move across a segment boundary, so learning_plan_textbook.json came out
    # byte-identical to the logical plan even when textbook_order was supplied — the
    # कवि-परिचय box is printed after the poem but taught before it, and that difference was
    # being silently dropped.
    pos = {tid: i for i, tid in enumerate(order)}
    seg_rank = {sid: min((pos[t["tid"]] for t in spec["topics"] if t["seg"] == sid), default=1 << 30)
                for sid in spec["segments"]}
    mod_rank = {mid: min((seg_rank[sid] for sid, s in spec["segments"].items() if s["mod"] == mid),
                         default=1 << 30)
                for mid in spec["modules"]}

    mods = []
    for mid, m in sorted(spec["modules"].items(), key=lambda kv: mod_rank[kv[0]]):
        segs = []
        for sid, s in sorted(spec["segments"].items(), key=lambda kv: seg_rank[kv[0]]):
            if s["mod"] != mid:
                continue
            tids = [tid for tid in order if by_id[tid]["seg"] == sid]
            if not tids:
                continue
            segs.append({
                "segment_id": sid, "segment_name": s["name"],
                "brief_summary": s["bs"], "summary": s["sm"], "detailed_summary": s["ds"],
                "important_points": s["ip"],
                # LP2 segment recalls are .RQ{n} — .SR{n} is LP v1's convention
                "recall_questions": [{"id": f"{sid}.RQ{i}", "prompt": p, "answer": a,
                                      "difficulty": d, "bloom_level": b}
                                     for i, (p, a, d, b) in enumerate(s["rq"], 1)],
                "topics": [built[tid] for tid in tids]})
        node = {"module_id": mid, "module_name": m["name"], "brief_summary": m["bs"],
                "summary": m["sm"], "detailed_summary": m["ds"],
                "important_points": m["ip"], "segments": segs}
        if m.get("dw"):
            node["difficult_words"] = m["dw"]
        if m.get("ors"):
            node["overall_rhyme_scheme"] = m["ors"]
        mods.append(node)

    plan = dict(spec["root"])
    plan["objectives"] = objectives
    plan["strand_to_objective_map"] = {o["legacy_id"]: o["objective_id"] for o in objectives}
    plan["modules"] = mods
    return plan


def emit(spec, outdir="."):
    # Picked up automatically so content.py stays the single source of truth — re-running it
    # after a collage run must not revert the plan to single anchor frames.
    spec.setdefault("collages", load_collages(outdir))
    spec.setdefault("v2urls", load_v2_urls(outdir))
    logical_order = [t["tid"] for t in spec["topics"]]
    textbook_order = spec.get("textbook_order") or logical_order

    logical = build(spec, logical_order)
    json.dump(logical, open(os.path.join(outdir, "learning_plan_logical.json"), "w",
                            encoding="utf-8"), ensure_ascii=False, indent=1)
    textbook = build(spec, textbook_order)
    textbook["ordering"] = "textbook"
    json.dump(textbook, open(os.path.join(outdir, "learning_plan_textbook.json"), "w",
                             encoding="utf-8"), ensure_ascii=False, indent=1)

    meta = {k: logical[k] for k in (
        "board", "grade", "subject", "level", "version", "chapter_id", "plan_id",
        "chapter_name", "unit_title", "unit_number", "topic_number", "textbook",
        "textbook_url", "chapter_master_id", "subject_ref_id", "genre", "teaching_lens",
        "guiding_question")}
    meta.update(spec.get("meta", {}))
    json.dump(meta, open(os.path.join(outdir, "01_meta.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    n_t = sum(len(s["topics"]) for m in logical["modules"] for s in m["segments"])
    n_i = sum(len(t["media"]) for m in logical["modules"] for s in m["segments"]
              for t in s["topics"])
    print(f"modules {len(logical['modules'])}  segments "
          f"{sum(len(m['segments']) for m in logical['modules'])}  topics {n_t}  "
          f"objectives {len(logical['objectives'])}  images {n_i}")
    return logical


def validate(path="learning_plan_logical.json", imagebygpt="../../../imagebyGPT"):
    """POST to the LP2 validator. Zero validation_errors or the run is not done."""
    sys.path.insert(0, imagebygpt)
    from lp_v1_api import _request
    PY = "https://staging.singularity-learn.com/agentapi/api"
    plan = json.load(open(path, encoding="utf-8"))
    payload = json.dumps(plan, ensure_ascii=False, indent=1).encode("utf-8")
    s, b = _request(f"{PY}/lp2/learning-plans/validate", method="POST",
                    multipart={"files": {"file": (os.path.basename(path), payload)}})
    errs = b.get("validation_errors") or []
    print(f"{os.path.basename(path)}: status {s} success {b.get('success')} errors {len(errs)}")
    for e in errs[:20]:
        print("   ", e)
    return not errs


def upload(path="learning_plan_logical.json", chapter_master_id=None, activate=True,
           imagebygpt="../../../imagebyGPT", force=False, created_by=""):
    """POST the plan. Returns True only when the server reports success.

    created_by is the numeric user id as a string ("199"). `lp2_plans.created_by` is a varchar
    and 1414 of 3143 plans carry one, but every Hindi plan this pack has ever uploaded left it
    null — which is why nobody could say who wrote the class-8 v2 plans on 2026-08-07. Pass it.

    force=True overwrites an existing plan_id in place. Without it the server answers HTTP 200
    with success:false, action:'validated_only' and the message "Plan '…' already exists" —
    which is easy to mistake for a pass, so always check the returned flag. Use force only to
    replace a plan you own and mean to replace; to keep the old one, bump plan_id/version
    instead.
    """
    sys.path.insert(0, imagebygpt)
    from lp_v1_api import _request
    PY = "https://staging.singularity-learn.com/agentapi/api"
    plan = json.load(open(path, encoding="utf-8"))
    cmid = chapter_master_id or plan["chapter_master_id"]
    plan.pop("_activate", None)          # the server owns these two
    plan.pop("created_by", None)
    payload = json.dumps(plan, ensure_ascii=False, indent=1).encode("utf-8")
    url = (f"{PY}/lp2/learning-plans/upload?activate={'true' if activate else 'false'}"
           f"{'&force=true' if force else ''}")
    fields = {"chapter_master_id": str(cmid)}
    if created_by:
        fields["created_by"] = str(created_by)
    s, b = _request(url, method="POST",
                    multipart={"files": {"file": (f"{plan['plan_id']}.json", payload)},
                               "fields": fields})
    # POST /upload returns HTTP 200 with success:false on a conflict — check the flag
    print(f"upload {plan['plan_id']}: status {s} success {b.get('success')} "
          f"action {b.get('action')} version {b.get('version')} active {b.get('is_active')}")
    if b.get("message") and not b.get("success"):
        print("   ", b["message"])
    if b.get("counts"):
        print("   counts", json.dumps(b["counts"], ensure_ascii=False))
    for e in (b.get("validation_errors") or [])[:20]:
        print("   ", e)
    return bool(b.get("success"))
