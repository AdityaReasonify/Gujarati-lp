#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase-2 collage compositor — several existing frames into one topic image.

Phase 2 gives each topic exactly ONE image slot (`M{m}.S{s}.T{t}.C{c}.IMG1`), while a topic
often has two or three visual beats. Rather than generate anything, the frames that already
belong to that topic are composited into a single picture that reads in story order.

Adapted from `imagebyGPT/collage_images.py`, which was written for the LP v1 two-objective
spine. Three rules are carried over verbatim because each cost real damage to learn:

  * **Letterbox, never crop.** Every source frame carries a light-yellow narrator bar along its
    bottom edge. Cropping to a common aspect ratio cuts the bar off and the picture loses its
    caption.
  * **Gujarati ordinal badges (૧ ૨ ૩ ૪).** Reading order has to be stated, not guessed —
    a 2x2 grid is ambiguous without them.
  * **Panels come in story order, from an authored list.** Scoring a chapter-wide pool put
    stanza 4's waterfalls on stanza 5. `_collage.json` names the frames per topic by hand.

What this adds over the v1 version: **downscale on composite.** The v1 collages went up at
5–14 MB because panels were pasted at their native 2048x1152. Each panel is now capped at
`PANEL_W` before compositing, which is still legible (the narrator bar reads fine at ~1100 px)
and lands a 2-panel stack near the ~2 MB the platform's other V2 images already run at.

Dormant in this pack until a Gujarati frame pool exists — there is nothing to composite yet
(reference/collage_media.md). Two things to confirm before the first live run: that the
generated Gujarati frames really do carry a narrator bar along the bottom edge (letterboxing
exists to protect it — with no bar, the rule still holds but for a different reason), and that
the resolved font renders ૧ ૨ ૩ ૪ rather than tofu.
"""
from __future__ import annotations

import hashlib
import io
import os
import time
from typing import List, Optional, Sequence

import requests
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------- layout knobs
PANEL_W = 1100     # each panel is scaled to this width before compositing
MARGIN = 24        # white border around the whole collage
GUTTER = 16        # white gap between panels
RADIUS = 18        # rounded corner on each panel card
BORDER = 3         # panel outline
BG = (255, 255, 255)
BORDER_COLOUR = (214, 206, 190)   # warm grey, sits quietly against the art

BADGE_R = 30       # ordinal badge radius (scaled down with the panels)
BADGE_BG = (255, 250, 205)        # the same lemon chiffon the narrator bars use
BADGE_FG = (0, 0, 0)
BADGE_PAD = 16

GU_DIGITS = ["૧", "૨", "૩", "૪", "૫", "૬"]
PANEL_MAX = 4      # beyond four the panels are too small to read — prune first

# Must be a face that actually carries U+0AE6–U+0AEF, or every badge renders as tofu.
_FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Gujarati Sangam MN.ttc",
    "/System/Library/Fonts/Supplemental/GujaratiMT.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansGujarati-Regular.ttf",
    "C:/Windows/Fonts/Nirmala.ttf",
    "C:/Windows/Fonts/shruti.ttf",
]

DEFAULT_CACHE = os.path.join("_src_cache")


def _font(size: int) -> ImageFont.FreeTypeFont:
    for path in _FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def fetch(url: str, cache_dir: str = DEFAULT_CACHE, timeout: int = 120,
          tries: int = 5) -> str:
    """Download a source frame, cached by URL. Local paths pass straight through.

    The CDN is intermittently unwell — a 502, a connect timeout and a read timeout have all
    been seen mid-chapter, each time succeeding on a plain re-run. A chapter is 20-70 fetches,
    so a 1-in-50 flake is close to one failure per chapter; retrying here is what keeps a
    compose from dying two thirds of the way through and throwing away the work.
    """
    if os.path.exists(url):
        return url
    os.makedirs(cache_dir, exist_ok=True)
    stem = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    local = os.path.join(cache_dir, "%s_%s" % (stem, os.path.basename(url)))
    if os.path.exists(local) and os.path.getsize(local) > 0:
        return local
    last = None
    for attempt in range(tries):
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            Image.open(io.BytesIO(resp.content))   # reject anything that is not an image
            with open(local, "wb") as fh:
                fh.write(resp.content)
            return local
        except Exception as exc:                   # timeout, 5xx, truncated body
            last = exc
            if attempt == tries - 1:
                break
            wait = 2 ** attempt                    # 1, 2, 4, 8 s
            print("      retry %d/%d in %ds (%s) %s"
                  % (attempt + 1, tries - 1, wait, type(exc).__name__,
                     os.path.basename(url)))
            time.sleep(wait)
    raise RuntimeError("could not fetch %s after %d tries: %r" % (url, tries, last))


def _rounded_mask(size, radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([(0, 0), (size[0] - 1, size[1] - 1)],
                                           radius=radius, fill=255)
    return mask


def _paste_panel(canvas: Image.Image, panel: Image.Image, box, ordinal: Optional[int]):
    """Drop one panel onto the canvas as a rounded card with an ordinal badge."""
    x, y, w, h = box
    # letterbox rather than crop — the narrator bar must stay in frame
    fitted = Image.new("RGB", (w, h), BG)
    scale = min(w / panel.width, h / panel.height)
    new = panel.resize((max(1, round(panel.width * scale)),
                        max(1, round(panel.height * scale))), Image.LANCZOS)
    fitted.paste(new, ((w - new.width) // 2, (h - new.height) // 2))

    canvas.paste(fitted, (x, y), _rounded_mask((w, h), RADIUS))
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle([(x, y), (x + w - 1, y + h - 1)],
                           radius=RADIUS, outline=BORDER_COLOUR, width=BORDER)

    if ordinal is not None and ordinal <= len(GU_DIGITS):
        cx, cy = x + BADGE_PAD + BADGE_R, y + BADGE_PAD + BADGE_R
        draw.ellipse([(cx - BADGE_R, cy - BADGE_R), (cx + BADGE_R, cy + BADGE_R)],
                     fill=BADGE_BG, outline=BADGE_FG, width=2)
        glyph = GU_DIGITS[ordinal - 1]
        font = _font(int(BADGE_R * 1.25))
        l, t, r, b = draw.textbbox((0, 0), glyph, font=font)
        draw.text((cx - (r + l) / 2, cy - (b + t) / 2), glyph, font=font, fill=BADGE_FG)


def layout_for(n: int) -> str:
    return {1: "landscape",
            2: "portrait, 2 vertical panels",
            3: "portrait, 3 vertical panels",
            4: "square, 2x2 grid"}.get(n, "landscape")


def compose(sources: Sequence[str], out_path: str,
            cache_dir: str = DEFAULT_CACHE, badges: bool = True,
            panel_w: int = PANEL_W) -> str:
    """Build the collage and write it to out_path. Returns out_path.

    1 panel  -> the frame itself, downscaled to panel_w, no badge
    2 panels -> vertical stack
    3 panels -> vertical stack of three
    4 panels -> 2x2 grid, reading left-to-right then down
    """
    if not sources:
        raise ValueError("compose() needs at least one source")
    if len(sources) > PANEL_MAX:
        raise ValueError("%d panels exceeds PANEL_MAX=%d; prune first"
                         % (len(sources), PANEL_MAX))

    panels = []
    for s in sources:
        im = Image.open(fetch(s, cache_dir)).convert("RGB")
        if im.width > panel_w:                       # downscale before compositing
            h = max(1, round(im.height * panel_w / im.width))
            im = im.resize((panel_w, h), Image.LANCZOS)
        panels.append(im)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)

    if len(panels) == 1:
        panels[0].save(out_path, "PNG", optimize=True)
        return out_path

    cw = max(p.width for p in panels)
    ch = max(p.height for p in panels)
    cols, rows = (2, 2) if len(panels) == 4 else (1, len(panels))

    width = MARGIN * 2 + cols * cw + (cols - 1) * GUTTER
    height = MARGIN * 2 + rows * ch + (rows - 1) * GUTTER
    canvas = Image.new("RGB", (width, height), BG)

    for i, panel in enumerate(panels):
        r, c = divmod(i, cols)
        x = MARGIN + c * (cw + GUTTER)
        y = MARGIN + r * (ch + GUTTER)
        _paste_panel(canvas, panel, (x, y, cw, ch), i + 1 if badges else None)

    canvas.save(out_path, "PNG", optimize=True)
    return out_path
