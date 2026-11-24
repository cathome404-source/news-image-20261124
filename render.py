#!/usr/bin/env python3
"""Render the one-page newspaper for 24 November 2026.

Reads stories.json (the only source of story text), draws a 1024x1024
newspaper with PIL primitives only, writes entry.png.
Deterministic: no clock, no randomness, no network.
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"
W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (17, 17, 17)
RED = (185, 28, 28)
NAVY = (31, 56, 100)
GREY = (90, 86, 76)
LIGHT_LINE = (205, 198, 182)
BADGE_FILL = {
    "CONFIRMED": (30, 122, 52),
    "OFFICIAL": (31, 56, 100),
    "REPORTED": (154, 107, 0),
    "CLAIM": None,  # outline style
}
CLAIM_COL = (194, 65, 12)

with open(ROOT / "stories.json", encoding="utf-8") as fh:
    DATA = json.load(fh)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


SERIF_B = "DejaVuSerif-Bold.ttf"
SANS = "DejaVuSans.ttf"
SANS_B = "DejaVuSans-Bold.ttf"


def wrap(d, text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_lines(d, text, names, sizes, max_w, max_lines):
    """Try font sizes descending; return (font, lines) fitting max_lines."""
    for size in sizes:
        fnt = font(names, size)
        lines = wrap(d, text, fnt, max_w)
        if len(lines) <= max_lines:
            return fnt, lines
    fnt = font(names, sizes[-1])
    return fnt, wrap(d, text, fnt, max_w)[:max_lines]


def draw_lines(d, lines, x, y, fnt, color, leading=None):
    if leading is None:
        leading = fnt.size + 2
    for line in lines:
        d.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def draw_tracked(d, text, x, y, fnt, color, track=2):
    cx = x
    for ch in text:
        d.text((cx, y), ch, font=fnt, fill=color)
        cx += d.textlength(ch, font=fnt) + track
    return cx


def centered_tracked_width(d, text, fnt, track=2):
    w = sum(d.textlength(c, font=fnt) + track for c in text) - track
    return w


def badge(d, x, y, label):
    fnt = font(SANS_B, 10)
    tw = d.textlength(label, font=fnt)
    bw, bh = int(tw) + 10, 14
    fill = BADGE_FILL[label]
    if fill is None:
        d.rounded_rectangle([x, y, x + bw, y + bh], radius=3,
                            outline=CLAIM_COL, width=1)
        d.text((x + 5, y + 2), label, font=fnt, fill=CLAIM_COL)
    else:
        d.rounded_rectangle([x, y, x + bw, y + bh], radius=3, fill=fill)
        d.text((x + 5, y + 2), label, font=fnt, fill=(255, 255, 255))
    return bw


# ---------------------------------------------------------------- illustrations
def scene_bg(d, x, y, w, h, bg):
    d.rectangle([x, y, x + w, y + h], fill=bg)


def art_scales(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (232, 222, 196))
    cx, cy = x + w // 2, y + h // 2 + 4
    d.line([cx - 34, cy - 26, cx + 34, cy - 26], fill=(120, 90, 30), width=4)
    d.line([cx, cy - 26, cx, cy + 18], fill=(120, 90, 30), width=4)
    d.polygon([(cx - 34, cy - 26), (cx - 48, cy - 6), (cx - 20, cy - 6)],
              fill=(180, 140, 40))
    d.polygon([(cx + 34, cy - 26), (cx + 20, cy - 6), (cx + 48, cy - 6)],
              fill=(180, 140, 40))
    d.rectangle([cx - 4, cy + 18, cx + 4, cy + 24], fill=(120, 90, 30))
    d.rectangle([cx - 26, cy + 24, cx + 26, cy + 28], fill=(120, 90, 30))
    d.ellipse([cx - 6, cy - 34, cx + 6, cy - 22], fill=(180, 140, 40))


def art_globe(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (206, 226, 232))
    cx, cy = x + w // 2 - 14, y + h // 2
    d.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], fill=(70, 130, 180))
    d.ellipse([cx - 18, cy - 24, cx - 2, cy - 8], fill=(90, 170, 110))
    d.ellipse([cx + 4, cy + 6, cx + 22, cy + 24], fill=(90, 170, 110))
    d.arc([cx - 30, cy - 30, cx + 30, cy + 30], 200, 340, fill=(255, 255, 255), width=2)
    fx = x + w - 52
    d.rectangle([fx, cy + 2, fx + 44, cy + 26], fill=(120, 120, 120))
    d.polygon([(fx, cy + 2), (fx + 10, cy - 10), (fx + 20, cy + 2)], fill=(100, 100, 100))
    d.polygon([(fx + 22, cy + 2), (fx + 32, cy - 12), (fx + 42, cy + 2)], fill=(100, 100, 100))
    for sx, sy, r in ((fx + 8, cy - 14, 5), (fx + 22, cy - 20, 6), (fx + 36, cy - 16, 4)):
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(150, 150, 150))
    d.line([cx + 24, cy - 26, cx + 44, cy + 4], fill=RED, width=4)


def art_ship(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (200, 222, 235))
    cy = y + h // 2 + 8
    for i, wy in enumerate((cy + 18, cy + 26, cy + 34)):
        d.line([x + 6, wy, x + w - 6, wy], fill=(70, 130, 180), width=3)
    d.polygon([(x + 14, cy), (x + w - 40, cy), (x + w - 52, cy + 16),
               (x + 26, cy + 16)], fill=(90, 90, 100))
    d.rectangle([x + 34, cy - 16, x + 62, cy], fill=(120, 120, 130))
    d.line([x + 48, cy - 30, x + 48, cy - 16], fill=(90, 90, 100), width=3)
    d.polygon([(x + 48, cy - 30), (x + 66, cy - 24), (x + 48, cy - 18)], fill=RED)
    dx, dy = x + w - 34, y + 14
    d.ellipse([dx - 12, dy - 4, dx + 12, dy + 4], fill=(60, 60, 60))
    d.line([dx - 8, dy + 4, dx - 8, dy + 10], fill=(60, 60, 60), width=2)
    d.line([dx + 8, dy + 4, dx + 8, dy + 10], fill=(60, 60, 60), width=2)
    d.ellipse([dx - 3, dy - 3, dx + 3, dy + 3], fill=RED)


def art_radar(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (214, 228, 214))
    cx, cy = x + w // 2 - 16, y + h // 2 + 10
    d.line([cx, cy, cx, cy + 18], fill=(70, 90, 70), width=4)
    d.pieslice([cx - 26, cy - 34, cx + 26, cy + 18], 180, 360, fill=(120, 160, 120))
    d.line([cx - 26, cy - 8, cx + 26, cy - 8], fill=(70, 90, 70), width=3)
    d.line([cx, cy - 8, cx + 18, cy - 26], fill=(70, 90, 70), width=3)
    dx, dy = x + w - 30, y + 16
    d.ellipse([dx - 11, dy - 3, dx + 11, dy + 3], fill=(60, 60, 60))
    d.line([dx, dy - 10, dx, dy - 3], fill=(60, 60, 60), width=2)
    d.ellipse([dx - 3, dy - 3, dx + 3, dy + 3], fill=RED)


def art_skyline(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (226, 214, 196))
    base = y + h
    for bx, bw, bh in ((x + 4, 22, 34), (x + 28, 18, 48), (x + 48, 24, 30),
                       (x + 74, 18, 52), (x + 94, 22, 36)):
        d.rectangle([bx, base - bh, bx + bw, base], fill=(90, 90, 110))
    d.polygon([(x + 4, y + 6), (x + 30, y + 26), (x + 44, y + 4),
               (x + 70, y + 30), (x + 96, y + 8)], fill=(220, 120, 60))
    d.line([x + 8, y + 8, x + 34, y + 28], fill=(200, 60, 30), width=2)
    d.line([x + 48, y + 6, x + 74, y + 32], fill=(200, 60, 30), width=2)
    d.ellipse([x + 30, y + 24, x + 38, y + 32], fill=(250, 200, 60))
    d.ellipse([x + 70, y + 28, x + 78, y + 36], fill=(250, 200, 60))


def art_satellite(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (24, 32, 54))
    cx, cy = x + w // 2, y + h + 34
    d.ellipse([cx - 42, cy - 42, cx + 42, cy + 42], fill=(70, 130, 180))
    d.arc([cx - 42, cy - 42, cx + 42, cy + 42], 200, 340,
          fill=(255, 255, 255), width=2)
    d.ellipse([cx - 20, cy - 38, cx - 2, cy - 24], fill=(90, 170, 110))
    sx, sy = x + w // 2, y + h // 2 - 8
    d.rectangle([sx - 30, sy - 7, sx - 10, sy + 7], fill=(200, 170, 60))
    d.rectangle([sx + 10, sy - 7, sx + 30, sy + 7], fill=(200, 170, 60))
    d.line([sx - 30, sy, sx - 10, sy], fill=(150, 120, 40), width=1)
    d.line([sx + 10, sy, sx + 30, sy], fill=(150, 120, 40), width=1)
    d.rectangle([sx - 10, sy - 9, sx + 10, sy + 9], fill=(220, 220, 220))
    d.line([sx, sy + 9, sx + 12, sy + 20], fill=(220, 220, 220), width=2)
    d.ellipse([sx + 10, sy + 18, sx + 16, sy + 24], fill=(240, 160, 40))


def art_chip(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (222, 228, 222))
    cx, cy = x + w // 2, y + h // 2
    for i in range(5):
        px = cx - 24 + i * 12
        d.line([px, cy - 30, px, cy - 22], fill=(150, 150, 150), width=3)
        d.line([px, cy + 22, px, cy + 30], fill=(150, 150, 150), width=3)
        py = cy - 24 + i * 12
        d.line([cx - 30, py, cx - 22, py], fill=(150, 150, 150), width=3)
        d.line([cx + 22, py, cx + 30, py], fill=(150, 150, 150), width=3)
    d.rectangle([cx - 22, cy - 22, cx + 22, cy + 22], fill=(40, 60, 40))
    d.rectangle([cx - 12, cy - 12, cx + 12, cy + 12], fill=(90, 170, 110))
    d.line([cx - 12, cy, cx + 12, cy], fill=(40, 60, 40), width=2)


def art_rocket(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (214, 224, 238))
    cx = x + w // 2
    d.polygon([(cx - 10, y + 12), (cx, y + 2), (cx + 10, y + 12)], fill=RED)
    d.rectangle([cx - 10, y + 12, cx + 10, y + 44], fill=(230, 230, 230))
    d.rectangle([cx - 10, y + 30, cx + 10, y + 38], fill=(70, 130, 180))
    d.polygon([(cx - 10, y + 44), (cx - 18, y + 56), (cx - 10, y + 52)], fill=RED)
    d.polygon([(cx + 10, y + 44), (cx + 18, y + 56), (cx + 10, y + 52)], fill=RED)
    d.polygon([(cx - 4, y + 44), (cx, y + 60), (cx + 4, y + 44)], fill=(240, 160, 40))
    d.line([x + 8, y + h - 18, cx - 22, y + h - 18], fill=(120, 120, 120), width=5)
    d.line([cx + 22, y + h - 18, x + w - 8, y + h - 18], fill=(120, 120, 120), width=5)
    d.line([cx - 22, y + h - 18, cx - 22, y + h - 8], fill=(120, 120, 120), width=4)
    d.line([cx + 22, y + h - 18, cx + 22, y + h - 8], fill=(120, 120, 120), width=4)


def art_mountains(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (222, 232, 224))
    d.polygon([(x + 4, y + h - 6), (x + 30, y + 8), (x + 56, y + h - 6)],
              fill=(110, 130, 150))
    d.polygon([(x + 40, y + h - 6), (x + 72, y + 16), (x + 104, y + h - 6)],
              fill=(80, 100, 125))
    d.polygon([(x + 24, y + 8), (x + 30, y + 8), (x + 36, y + 8),
               (x + 33, y + 16), (x + 27, y + 16)], fill=(255, 255, 255))
    for wy in (y + 14, y + 24, y + 34):
        d.line([x + w - 34, wy, x + w - 10, wy], fill=RED, width=2)
        d.line([x + w - 30, wy - 3, x + w - 26, wy + 3], fill=RED, width=2)
        d.line([x + w - 20, wy - 3, x + w - 16, wy + 3], fill=RED, width=2)


def art_helicopter(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (228, 224, 210))
    cx, cy = x + w // 2, y + h // 2 - 4
    d.line([cx - 40, cy - 18, cx + 40, cy - 18], fill=(60, 60, 60), width=3)
    d.ellipse([cx - 18, cy - 12, cx + 14, cy + 6], fill=(70, 90, 120))
    d.line([cx + 14, cy - 4, cx + 38, cy - 10], fill=(70, 90, 120), width=4)
    d.line([cx + 34, cy - 16, cx + 34, cy - 2], fill=(70, 90, 120), width=3)
    d.line([cx - 8, cy + 6, cx - 2, cy + 20], fill=(60, 60, 60), width=3)
    d.line([cx + 6, cy + 6, cx + 12, cy + 20], fill=(60, 60, 60), width=3)
    d.line([cx - 8, cy + 20, cx + 12, cy + 20], fill=(60, 60, 60), width=3)
    d.ellipse([cx - 30, cy + 22, cx - 18, cy + 34], fill=(200, 180, 60))
    d.ellipse([cx + 18, cy + 22, cx + 30, cy + 34], fill=(200, 180, 60))


def art_ruin(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (232, 220, 208))
    d.rectangle([x + 8, y + 10, x + 52, y + h - 8], fill=(150, 140, 125))
    d.polygon([(x + 8, y + 10), (x + 30, y + 2), (x + 52, y + 10)], fill=(120, 110, 95))
    d.line([x + 30, y + 10, x + 22, y + 26], fill=(90, 80, 70), width=3)
    d.line([x + 22, y + 26, x + 34, y + 40], fill=(90, 80, 70), width=3)
    d.rectangle([x + 18, y + 30, x + 28, y + 40], fill=(60, 55, 45))
    d.polygon([(x + 62, y + h - 8), (x + 84, y + 22), (x + 106, y + h - 8)],
              fill=(190, 170, 130))
    d.line([x + 84, y + 22, x + 84, y + h - 8], fill=(150, 130, 95), width=2)


def art_flags(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (222, 228, 236))
    cx, cy = x + w // 2, y + h // 2
    d.line([cx - 34, cy - 24, cx - 34, cy + 24], fill=(90, 90, 90), width=3)
    d.line([cx + 34, cy - 24, cx + 34, cy + 24], fill=(90, 90, 90), width=3)
    d.polygon([(cx - 34, cy - 24), (cx - 6, cy - 24), (cx - 6, cy - 6),
               (cx - 34, cy - 6)], fill=(70, 90, 160))
    for sy in range(cy - 22, cy - 8, 5):
        d.ellipse([cx - 30, sy, cx - 26, sy + 3], fill=(255, 255, 255))
    d.polygon([(cx + 6, cy - 24), (cx + 34, cy - 24), (cx + 34, cy - 6),
               (cx + 6, cy - 6)], fill=(200, 60, 60))
    d.polygon([(cx + 6, cy - 24), (cx + 20, cy - 15), (cx + 6, cy - 6)], fill=(255, 255, 255))
    d.line([cx - 14, cy + 12, cx + 14, cy + 12], fill=(90, 140, 80), width=3)
    d.line([cx - 20, cy + 18, cx + 20, cy + 18], fill=(90, 140, 80), width=3)


def art_fire(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (236, 224, 210))
    base = y + h - 6
    d.rectangle([x + 8, base - 30, x + w - 8, base], fill=(130, 130, 130))
    d.rectangle([x + 14, base - 42, x + 34, base - 30], fill=(110, 110, 110))
    d.rectangle([x + w - 40, base - 38, x + w - 18, base - 30], fill=(110, 110, 110))
    for fx, fh in ((x + 22, 26), (x + 52, 32), (x + 82, 24)):
        d.polygon([(fx - 10, base - 30), (fx, base - 30 - fh),
                   (fx + 10, base - 30)], fill=(240, 120, 30))
        d.polygon([(fx - 5, base - 30), (fx, base - 30 - fh + 12),
                   (fx + 5, base - 30)], fill=(250, 200, 60))


def art_hospital(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (220, 232, 230))
    d.rectangle([x + 10, y + 12, x + w - 34, y + h - 8], fill=(240, 240, 240))
    d.rectangle([x + 10, y + 12, x + w - 34, y + 22], fill=(70, 130, 180))
    for wy in range(y + 30, y + h - 10, 10):
        d.rectangle([x + 18, wy, x + 28, wy + 6], fill=(120, 160, 200))
        d.rectangle([x + 34, wy, x + 44, wy + 6], fill=(120, 160, 200))
    px, py = x + w - 18, y + 18
    d.ellipse([px - 12, py - 12, px + 12, py + 12], fill=RED)
    d.rectangle([px - 2, py - 7, px + 2, py + 7], fill=(255, 255, 255))
    d.rectangle([px - 7, py - 2, px + 7, py + 2], fill=(255, 255, 255))


def art_football(d, x, y, w, h):
    scene_bg(d, x, y, w, h, (120, 180, 110))
    d.rectangle([x, y + h - 10, x + w, y + h], fill=(90, 150, 85))
    d.line([x + 8, y + 8, x + w - 8, y + 8], fill=(255, 255, 255), width=2)
    for gx in (x + 14, x + w - 14):
        d.line([gx, y + 8, gx, y + 20], fill=(255, 255, 255), width=2)
    cx, cy = x + w // 2, y + h // 2 + 4
    r = 16
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255),
              outline=(60, 60, 60), width=2)
    d.polygon([(cx, cy - 7), (cx + 7, cy - 2), (cx + 4, cy + 6),
               (cx - 4, cy + 6), (cx - 7, cy - 2)], fill=(30, 30, 30))
    d.line([cx, cy - 7, cx, cy - r], fill=(30, 30, 30), width=2)
    d.line([cx + 7, cy - 2, cx + r, cy - 4], fill=(30, 30, 30), width=2)
    d.line([cx - 7, cy - 2, cx - r, cy - 4], fill=(30, 30, 30), width=2)
    d.line([cx + 4, cy + 6, cx + 10, cy + r], fill=(30, 30, 30), width=2)
    d.line([cx - 4, cy + 6, cx - 10, cy + r], fill=(30, 30, 30), width=2)


ART = {
    "scales": art_scales, "globe": art_globe, "ship": art_ship,
    "radar": art_radar, "skyline": art_skyline, "satellite": art_satellite,
    "chip": art_chip, "rocket": art_rocket, "mountains": art_mountains,
    "helicopter": art_helicopter, "ruin": art_ruin, "flags": art_flags,
    "fire": art_fire, "hospital": art_hospital, "football": art_football,
}

# ---------------------------------------------------------------- continents
NA = [(-168, 66), (-140, 70), (-125, 71), (-110, 68), (-95, 69), (-85, 66),
      (-80, 73), (-70, 62), (-65, 60), (-55, 47), (-60, 45), (-70, 42),
      (-75, 35), (-80, 32), (-81, 26), (-90, 21), (-97, 16), (-94, 17),
      (-86, 12), (-83, 9), (-79, 9), (-92, 14), (-105, 20), (-110, 23),
      (-114, 29), (-120, 34), (-125, 40), (-124, 48), (-135, 58),
      (-150, 60), (-165, 60)]
GL = [(-55, 60), (-45, 60), (-40, 64), (-30, 68), (-22, 70), (-25, 76),
      (-40, 80), (-58, 76), (-60, 70)]
SA = [(-79, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12), (-72, -18),
      (-70, -23), (-70, -30), (-72, -37), (-73, -44), (-74, -52),
      (-70, -55), (-65, -55), (-68, -50), (-65, -45), (-62, -40),
      (-57, -35), (-52, -32), (-48, -28), (-41, -23), (-35, -9),
      (-35, -6), (-42, 0), (-50, 0), (-55, 5), (-60, 8), (-70, 10), (-77, 8)]
AF = [(-17, 15), (-17, 21), (-15, 27), (-10, 31), (-5, 35), (0, 36),
      (10, 37), (11, 34), (20, 32), (30, 31), (32, 31), (35, 28),
      (37, 22), (39, 18), (43, 11), (48, 11), (51, 10), (46, 5),
      (41, 0), (40, -5), (40, -10), (36, -18), (32, -26), (28, -33),
      (20, -35), (17, -32), (15, -27), (12, -18), (12, -10), (9, 4),
      (4, 6), (-8, 5), (-13, 8), (-17, 12)]
EU = [(-10, 36), (-9, 38), (-9, 43), (-2, 44), (-1, 46), (-4, 48),
      (-2, 50), (0, 51), (3, 53), (8, 57), (10, 59), (5, 60), (5, 62),
      (12, 65), (18, 69), (25, 71), (30, 70), (32, 68), (40, 68),
      (45, 66), (48, 62), (44, 58), (40, 55), (38, 52), (35, 48),
      (30, 46), (28, 44), (23, 40), (22, 37), (18, 38), (15, 38),
      (12, 42), (8, 44), (3, 43), (-1, 38)]
AS = [(30, 70), (45, 68), (60, 69), (75, 72), (90, 75), (105, 77),
      (120, 74), (135, 72), (150, 70), (162, 69), (170, 66), (178, 64),
      (170, 60), (162, 56), (158, 51), (155, 55), (150, 59), (142, 59),
      (141, 50), (140, 44), (135, 43), (130, 42), (127, 39), (126, 38),
      (121, 37), (120, 31), (122, 27), (118, 24), (110, 20), (108, 17),
      (105, 9), (103, 7), (100, 6), (98, 10), (94, 16), (91, 22),
      (88, 22), (85, 19), (80, 15), (77, 8), (74, 12), (70, 20),
      (66, 25), (61, 25), (57, 26), (53, 26), (50, 29), (48, 30),
      (50, 26), (54, 24), (57, 25), (59, 22), (55, 17), (48, 14),
      (44, 13), (42, 15), (39, 21), (36, 28), (34, 28), (30, 36),
      (27, 37), (26, 39), (23, 40), (27, 41), (30, 46), (32, 48),
      (35, 50), (38, 55), (35, 60), (30, 65)]
AU = [(113, -22), (114, -30), (115, -35), (120, -34), (129, -32),
      (132, -32), (137, -35), (140, -38), (145, -38), (150, -37),
      (153, -32), (153, -27), (150, -22), (146, -19), (142, -11),
      (137, -12), (135, -15), (132, -12), (130, -13), (126, -14),
      (122, -17), (118, -20)]
CONTINENTS = [NA, GL, SA, AF, EU, AS, AU]


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 14
    cw = W - 2 * mx  # 996
    y = 6

    # ---- masthead (78) ----
    kicker = font(SANS_B, 11)
    kw = centered_tracked_width(d, DATA["title"], kicker, 3)
    draw_tracked(d, DATA["title"], (W - kw) / 2, y, kicker, RED, 3)
    y += 16
    date_f = font(SERIF_B, 38)
    dw = d.textlength(DATA["date"], font=date_f)
    d.text(((W - dw) / 2, y), DATA["date"], font=date_f, fill=INK)
    y += 44
    d.line([mx, y, W - mx, y], fill=RED, width=2)
    y += 4
    sub_f = font(SANS, 13)
    for line in wrap(d, DATA["subheadline"], sub_f, cw):
        lw = d.textlength(line, font=sub_f)
        d.text(((W - lw) / 2, y), line, font=sub_f, fill=INK)
        y += 15
    # masthead ends ~84; force cursor
    y = 89

    # ---- UTC strip (30) ----
    d.rectangle([mx, y, W - mx, y + 30], fill=NAVY)
    lab = font(SANS_B, 11)
    d.text((mx + 10, y + 9), "THE DAY IN UTC", font=lab, fill=(255, 255, 255))
    lab_w = d.textlength("THE DAY IN UTC", font=lab) + 22
    parts = "  ·  ".join(
        "%s — %s" % (p[0], p[1]) for p in DATA["utc_parts"])
    pf = font(SANS, 11)
    plines = wrap(d, parts, pf, cw - lab_w - 8)
    py = y + 3
    for line in plines[:2]:
        d.text((mx + lab_w, py), line, font=pf, fill=(255, 255, 255))
        py += 13
    y = 124

    # ---- numbers strip (44) ----
    d.text((mx, y), "THE DAY IN NUMBERS", font=font(SANS_B, 11), fill=INK)
    y += 13
    cell_w = cw // 6
    for i, (num, cap) in enumerate(DATA["numbers"]):
        cx = mx + i * cell_w
        nf = font(SANS_B, 21)
        d.text((cx, y), num, font=nf, fill=RED)
        cf = font(SANS, 10)
        d.text((cx, y + 22), cap, font=cf, fill=INK)
        if i:
            d.line([cx - 6, y + 2, cx - 6, y + 28], fill=LIGHT_LINE, width=1)
    y = 173

    # ---- big 3 (162) ----
    big = [s for s in DATA["stories"] if s["n"] <= 3]
    col_w = (cw - 20) // 3
    for i, s in enumerate(big):
        x0 = mx + i * (col_w + 10)
        d.rectangle([x0, y, x0 + col_w, y + 76], fill=(235, 230, 218))
        ART[s["art"]](d, x0, y, col_w, 76)
        d.rectangle([x0, y, x0 + col_w, y + 4], fill=RED)
        d.text((x0, y + 80), str(s["n"]), font=font(SANS_B, 15), fill=RED)
        hf, hlines = fit_lines(d, s["headline"], SANS_B, [17, 16, 15, 14],
                               col_w - 22, 2)
        draw_lines(d, hlines, x0 + 22, y + 80, hf, INK, 19)
        df = font(SANS, 12)
        dlines = wrap(d, s["deck"], df, col_w)[:2]
        draw_lines(d, dlines, x0, y + 80 + 40, df, INK, 14)
        by = y + 80 + 40 + 28
        bw = badge(d, x0, by, s["badge"])
        sf = font(SANS, 10)
        d.text((x0 + bw + 5, by + 2),
               "%s · %s" % (s["region"], s["source"]), font=sf, fill=GREY)
    y = 340

    # ---- medium 12 (3 rows x 104) ----
    med = [s for s in DATA["stories"] if 4 <= s["n"] <= 15]
    mcol = (cw - 30) // 4
    for row in range(3):
        ry = y + row * 104
        for col in range(4):
            s = med[row * 4 + col]
            x0 = mx + col * (mcol + 10)
            d.rectangle([x0, ry, x0 + mcol, ry + 50], fill=(235, 230, 218))
            ART[s["art"]](d, x0, ry, mcol, 50)
            d.rectangle([x0, ry, x0 + mcol, ry + 3], fill=RED)
            hy = ry + 54
            d.text((x0, hy), str(s["n"]), font=font(SANS_B, 12), fill=RED)
            hf, hlines = fit_lines(d, s["headline"], SANS_B, [13, 12],
                                   mcol - 18, 2)
            draw_lines(d, hlines, x0 + 18, hy, hf, INK, 15)
            by = ry + 54 + 32
            bw = badge(d, x0, by, s["badge"])
            sf = font(SANS, 10)
            src = "%s · %s" % (s["region"], s["source"])
            sw = d.textlength(src, font=sf)
            if sw > mcol - bw - 5:
                sf = font(SANS, 9)
            d.text((x0 + bw + 5, by + 2), src, font=sf, fill=GREY)
    y = 657

    # ---- ALSO ON (180) ----
    d.text((mx, y), "ALSO ON", font=font(SANS_B, 13), fill=INK)
    d.line([mx, y + 16, W - mx, y + 16], fill=INK, width=1)
    ay = y + 20
    acol = (cw - 20) // 3
    also = [s for s in DATA["stories"] if s["n"] >= 16]
    nf = font(SANS_B, 11)
    tf = font(SANS, 11)
    for col in range(3):
        for r in range(7):
            s = also[col * 7 + r]
            x0 = mx + col * (acol + 10)
            ry = ay + r * 23
            num = "%d · " % s["n"]
            d.text((x0, ry), num, font=nf, fill=RED)
            nw = d.textlength(num, font=nf)
            rest = "%s — %s" % (s["headline"], s["source"])
            lines = wrap(d, rest, tf, acol - nw)[:2]
            draw_lines(d, lines, x0 + nw, ry, tf, INK, 12)
    y = 842

    # ---- map + DATE CHECK (120) ----
    map_w = 460
    map_x = mx
    d.text((map_x, y), "WHERE IT HAPPENED", font=font(SANS_B, 12), fill=INK)
    d.text((map_x + map_w + 14, y), "DATE CHECK — NOT TODAY, SO NOT IN THE NEWS",
           font=font(SANS_B, 12), fill=RED)
    my = y + 16
    mh = 104
    d.rectangle([map_x, my, map_x + map_w, my + mh], fill=(214, 226, 232))
    lon0, lon1, lat0, lat1 = -170, 180, -56, 84
    def proj(lon, lat):
        px = map_x + (lon - lon0) / (lon1 - lon0) * map_w
        py = my + (lat1 - lat) / (lat1 - lat0) * mh
        return px, py
    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=(196, 190, 160), outline=(150, 144, 118))
    pf = font(SANS_B, 9)
    for pin in DATA["map_pins"]:
        px, py = proj(pin["lon"], pin["lat"])
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                  outline=(255, 255, 255), width=1)
        label = str(pin["n"])
        tw = d.textlength(label, font=pf)
        d.text((px - tw / 2, py - 5), label, font=pf, fill=(255, 255, 255))
    # DATE CHECK box
    dx = map_x + map_w + 14
    dw = W - mx - dx
    d.rectangle([dx, my, dx + dw, my + mh], outline=RED, width=1)
    d.rectangle([dx, my, dx + dw, my + 16], fill=RED)
    d.text((dx + 6, my + 3), "LEFT OUT ON PURPOSE", font=font(SANS_B, 10),
           fill=(255, 255, 255))
    df = font(SANS, 10)
    ly = my + 20
    for item in DATA["date_check"]:
        lines = wrap(d, "• " + item, df, dw - 12)[:2]
        ly = draw_lines(d, lines, dx + 6, ly, df, INK, 12)
        ly += 2
    y = 967

    # ---- footer (40) ----
    ff = font(SANS, 10)
    fy = y
    for line in wrap(d, DATA["footer_sources"], ff, cw):
        d.text((mx, fy), line, font=ff, fill=GREY)
        fy += 11
    for line in wrap(d, DATA["legend"], ff, cw):
        d.text((mx, fy), line, font=ff, fill=GREY)
        fy += 11
    for line in wrap(d, DATA["footer_note"], ff, cw):
        d.text((mx, fy), line, font=ff, fill=GREY)
        fy += 11

    img.save(ROOT / "entry.png", optimize=True)
    print("wrote", ROOT / "entry.png")


if __name__ == "__main__":
    render()
