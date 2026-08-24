# -*- coding: utf-8 -*-
import re, sys, json

GU = re.compile(r'[઀-૿]')

def words(s):
    return [t for t in s.split() if GU.search(t)]

def wc(s):
    return len(words(s))

def check_topic(t, forbidden=(), fields_forbidden=()):
    tid = t["topic_id"]
    out = []
    for f in ("explanation", "real_life_example"):
        n = wc(t[f])
        flag = "OK " if 55 <= n <= 90 else "BAD"
        out.append("%s %s %s %d" % (flag, tid, f, n))
    b, s, d = wc(t["brief_summary"]), wc(t["summary"]), wc(t["detailed_summary"])
    flag = "OK " if b < s < d else "BAD"
    out.append("%s %s summaries %d<%d<%d" % (flag, tid, b, s, d))
    for f in ("concept_bullets", "important_points"):
        n = len(t[f])
        out.append(("OK " if 3 <= n <= 4 else "BAD") + " %s %s n=%d" % (tid, f, n))
    n = len(t["recall_questions"])
    out.append(("OK " if 2 <= n <= 3 else "BAD") + " %s recall n=%d" % (tid, n))
    for i, q in enumerate(t["recall_questions"], 1):
        ok = q["id"] == "%s.RQ%d" % (tid, i) and q["legacy_id"] == "%s.TR%d" % (tid, i)
        ok = ok and q["bloom_level"] == q["bloom_level"].lower()
        ok = ok and q["difficulty"] in ("easy", "medium", "hard")
        ok = ok and q["answer"].strip()
        out.append(("OK " if ok else "BAD") + " %s %s" % (tid, q["id"]))
    n = len(t["shabdarth"])
    out.append(("OK " if 3 <= n <= 5 else "BAD") + " %s shabdarth n=%d" % (tid, n))
    n = len(t["samanarthi"])
    out.append(("OK " if 0 <= n <= 2 else "BAD") + " %s samanarthi n=%d" % (tid, n))
    n = len(t["vilom"])
    out.append(("OK " if 0 <= n <= 1 else "BAD") + " %s vilom n=%d" % (tid, n))
    n = len(t["vyakaran"])
    out.append(("OK " if n == 1 else "BAD") + " %s vyakaran n=%d" % (tid, n))
    # forbidden scan
    blob = " ".join([t[f] for f in fields_forbidden if isinstance(t.get(f), str)])
    for f in fields_forbidden:
        v = t.get(f)
        if isinstance(v, list):
            blob += " " + " ".join(v)
    blob += " " + " ".join(q["answer"] for q in t["recall_questions"])
    for w in forbidden:
        if w in blob:
            out.append("BAD %s FORBIDDEN '%s'" % (tid, w))
    # daNDa / devanagari / roman
    allblob = json.dumps(t, ensure_ascii=False)
    if "।" in allblob:
        out.append("BAD %s contains danda" % tid)
    if re.search(r'[ऀ-ॿ]', allblob):
        out.append("BAD %s contains devanagari" % tid)
    if re.search(r'\d', re.sub(r'"(topic_id|id|legacy_id|concept_id)": "[^"]*"', '', allblob)):
        out.append("WARN %s digit in text" % tid)
    return out
