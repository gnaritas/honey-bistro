#!/usr/bin/env python3
"""og.png 1200x630 — The Honey Bistro — warm honey poster.
Ink-brown field, amber rules, hexcomb flanks, serif brand. Shop identity only."""
from PIL import Image, ImageDraw, ImageFont
import os, math

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

INK = (34, 21, 10); INK2 = (53, 34, 17); CREAM = (248, 241, 224); HONEY = (204, 132, 21)
SAND = (178, 154, 112); AMBER_DIM = (96, 62, 24)

def font(paths, size):
    bases = ["/System/Library/Fonts/Supplemental/", "/System/Library/Fonts/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size)
                except Exception: pass
    return ImageFont.load_default()

serif = lambda s: font(["Iowan Old Style.ttc", "Palatino.ttc", "Georgia.ttf", "Times New Roman.ttf"], s)
sans = lambda s: font(["Futura.ttc", "HelveticaNeue.ttc", "HelveticaNeue.ttc", "Arial.ttf"], s)

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# lower band + rules
d.rectangle([0, 496, W, H], fill=INK2)
d.rectangle([0, 0, W, 7], fill=HONEY)
d.rectangle([0, H-7, W, H], fill=HONEY)

def center(text, f, y, fill, tracking=0):
    if tracking:
        widths = [d.textbbox((0,0), ch, font=f)[2]-d.textbbox((0,0), ch, font=f)[0] for ch in text]
        tw = sum(widths) + tracking*(len(text)-1)
        x = (W-tw)/2
        for ch,w in zip(text,widths):
            bb = d.textbbox((0,0), ch, font=f)
            d.text((x - bb[0], y), ch, font=f, fill=fill)
            x += w + tracking
        return tw
    bb = d.textbbox((0,0), text, font=f)
    d.text(((W-(bb[2]-bb[0]))/2 - bb[0], y), text, font=f, fill=fill)
    return bb[2]-bb[0]

# hexcomb flanks — pointy-top hexagons, dim amber outlines, drawn in side lanes only
def hexpath(cx, cy, r):
    pts = []
    for i in range(6):
        a = math.radians(60*i - 90)
        pts.append((cx + r*math.cos(a), cy + r*math.sin(a)))
    return pts
for cx, cy in [(72, 96),(72,200),(72,304),(72,408),(136,148),(136,252),(136,356),
               (1128,96),(1128,200),(1128,304),(1128,408),(1064,148),(1064,252),(1064,356),
               (72,520),(1128,520)]:
    d.polygon(hexpath(cx, cy, 52), outline=AMBER_DIM, width=3)

def measure(text, f, tracking=0):
    if tracking:
        return sum(d.textbbox((0,0), ch, font=f)[2]-d.textbbox((0,0), ch, font=f)[0] for ch in text) + tracking*(len(text)-1)
    bb = d.textbbox((0,0), text, font=f)
    return bb[2]-bb[0]

def fit(text, maker, sizes, maxw, tracking=0):
    m = 0
    for s in sizes:
        m = measure(text, maker(s), tracking)
        if m <= maxw: return s, m
    return sizes[-1], m

# kicker
ks, kw = fit("S A V O Y  ·  I L L I N O I S  —  O P E N I N G  J A N U A R Y  2 0 2 7", sans, (21, 19, 17, 15), 824, 3)
center("S A V O Y  ·  I L L I N O I S  —  O P E N I N G  J A N U A R Y  2 0 2 7", sans(ks), 66, HONEY, tracking=3)
# brand
bs, bw = fit("The Honey Bistro", serif, (96, 88, 80), 800)
center("The Honey Bistro", serif(bs), 150, CREAM)
# tagline
ts, tw = fit("Breakfast & brunch, with a little touch of honey.", serif, (40, 36, 32, 28), 824)
center("Breakfast & brunch, with a little touch of honey.", serif(ts), 300, (216, 188, 140))
# divider diamond
d.polygon([(W/2-9, 386),(W/2, 377),(W/2+9, 386),(W/2, 395)], fill=HONEY)
# lower band lines
center("501 Commerce Drive  ·  from the owners of Star 57 Diner, Tuscola", sans(23), 520, SAND, tracking=2)
center("7 a.m. – 3 p.m. planned  ·  daily", sans(19), 560, (140, 120, 90), tracking=2)

# clearance check: text column vs hexcomb lanes (hex rightmost 1128+52=1180; brand width check)
assert bw < 880, f"brand text {bw}px too wide for center lane (hexcomb lane starts 1180)"
img.save(OUT, "PNG")
print("wrote", OUT, os.path.getsize(OUT), "bytes; brand width", bw)
