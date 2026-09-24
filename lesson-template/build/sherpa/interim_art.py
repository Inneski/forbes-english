# -*- coding: utf-8 -*-
"""Interim artwork for the Sherpa Tensing decks — the set that ships until
the commission in docs/ARTWORK-sherpa-tensing.md replaces it, slot for slot.

    py lesson-template/build/sherpa/interim_art.py --textures   # 14 textures
    py lesson-template/build/sherpa/interim_art.py camp-03      # one hero
    py lesson-template/build/sherpa/interim_art.py              # all heroes

Two kinds of file, both into SherpaTensing/:

  * **hero-<slug>.jpg** (1600 x 900) — the page's own timeline diagram, the
    one picture each camp already had, set on its paper over a faint contour
    field in the camp's colour. It is a cover the palette tool can read
    honestly: the accent it derives is the tense colour, which is what the
    route map has been teaching learners to associate with that tense.
  * **bg-<face>-<role>.jpg** (1600 x 900) — one texture per section role,
    one light set for both faces (each deck multiplies it onto its colour).
    Procedural, low-contrast, no subject: a texture under a text plate needs
    nothing in it that competes with the words (HOUSE-STYLE §5).

The precedent is Holding the Line, which shipped on interim SVG plates and
had them swapped for the commissioned set with no change to the builder.
"""
import io
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT = os.path.join(ROOT, 'SherpaTensing')
CONTENT = os.path.join(HERE, 'content')
W, H = 1600, 900
ROLES = ['briefing', 'building', 'fork', 'markers', 'stage', 'climb', 'view']

rng = np.random.default_rng(7)


def hex_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# ── noise ─────────────────────────────────────────────────────────────
def value_noise(w, h, cells, seed):
    r = np.random.default_rng(seed)
    g = r.random((cells + 1, int(cells * w / h) + 2))
    img = Image.fromarray((g * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return np.asarray(img).astype(np.float32) / 255.0


def fbm(w, h, seed, base=6, octaves=4, gain=0.5):
    out = np.zeros((h, w), np.float32)
    amp, tot = 1.0, 0.0
    for o in range(octaves):
        out += amp * value_noise(w, h, base * (2 ** o), seed + o * 97)
        tot += amp
        amp *= gain
    return out / tot


def compose(base, ink, alpha):
    """alpha: (H, W) in 0..1 -> RGB image of ink over base."""
    a = np.clip(alpha, 0, 1)[..., None]
    b = np.array(base, np.float32)[None, None, :]
    i = np.array(ink, np.float32)[None, None, :]
    return Image.fromarray(np.clip(b * (1 - a) + i * a, 0, 255).astype(np.uint8))


def grain(seed, amount=0.05):
    r = np.random.default_rng(seed)
    return (r.random((H, W)).astype(np.float32) - 0.5) * amount


# ── the seven roles ──────────────────────────────────────────────────
def contours(seed, strength=0.34, freq=9.0, width=0.055):
    n = fbm(W, H, seed, base=3, octaves=3)
    frac = (n * freq) % 1.0
    line = np.clip((width - np.abs(frac - 0.5 * width * 2)) / width, 0, 1)
    line = (frac < width).astype(np.float32)
    line = np.asarray(Image.fromarray((line * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.9))) / 255.0
    return line * strength


def briefing(seed):
    return contours(seed, 0.30) + np.abs(grain(seed + 1, 0.10))


def building(seed):
    """Stacked blocks: a brick grid with a shade of its own per block."""
    r = np.random.default_rng(seed)
    bh, bw = 90, 210
    a = np.zeros((H, W), np.float32)
    for row, y in enumerate(range(-bh, H + bh, bh)):
        off = (bw // 2) if row % 2 else 0
        for x in range(-bw + off, W + bw, bw):
            shade = 0.05 + r.random() * 0.13
            a[max(0, y):y + bh - 4, max(0, x):x + bw - 5] = shade
    mortar = (a == 0).astype(np.float32) * 0.30
    return a + mortar + grain(seed + 2, 0.06)


def fork(seed):
    """Two hatch directions meeting at a soft seam: the path that splits."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    left = ((xx + yy) % 34 < 2.2).astype(np.float32)
    right = ((xx - yy) % 34 < 2.2).astype(np.float32)
    seam = np.clip((xx - W * 0.5) / 180.0 + 0.5, 0, 1)
    seam = seam * seam * (3 - 2 * seam)
    a = left * (1 - seam) + right * seam
    a = np.asarray(Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))) / 255.0
    return a * 0.26 + np.abs(grain(seed + 3, 0.08))


def markers(seed):
    """Cairn stones: scattered dots, denser towards the foot of the frame."""
    r = np.random.default_rng(seed)
    im = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(im)
    for _ in range(2600):
        y = H * (1 - r.random() ** 1.6)
        x = r.random() * W
        rad = 1.5 + r.random() ** 2 * 7
        d.ellipse([x - rad, y - rad * 0.8, x + rad, y + rad * 0.8], fill=int(90 + r.random() * 120))
    a = np.asarray(im.filter(ImageFilter.GaussianBlur(0.6))).astype(np.float32) / 255.0
    return a * 0.40 + np.abs(grain(seed + 4, 0.07))


def stage(seed):
    """Graph paper with a horizon line: the timeline's own furniture."""
    yy, xx = np.mgrid[0:H, 0:W]
    fine = ((xx % 40 == 0) | (yy % 40 == 0)).astype(np.float32) * 0.16
    heavy = ((xx % 200 == 0) | (yy % 200 == 0)).astype(np.float32) * 0.18
    horizon = ((yy >= 640) & (yy <= 642)).astype(np.float32) * 0.45
    return fine + heavy + horizon + np.abs(grain(seed + 5, 0.06))


def climb(seed):
    """Scree: a dense field of small angular flecks."""
    n = fbm(W, H, seed, base=48, octaves=2, gain=0.6)
    gy, gx = np.gradient(n)
    edge = np.clip(np.hypot(gx, gy) * 26, 0, 1)
    fleck = (n > 0.58).astype(np.float32) * 0.07
    return edge * 0.10 + fleck + np.abs(grain(seed + 6, 0.06))


def view(seed):
    """High cloud: the calm one, for the activation stage."""
    n = fbm(W, H, seed, base=2, octaves=5, gain=0.55)
    n = (n - n.min()) / (n.max() - n.min() + 1e-6)
    return (1 - n) * 0.34 + np.abs(grain(seed + 7, 0.05))


GEN = dict(briefing=briefing, building=building, fork=fork, markers=markers,
           stage=stage, climb=climb, view=view)

FACES = {
    # face: (base, ink, how much of the ink alpha to keep). One set since
    # 2026-09-24: the decks dye it in their own colour, so a night set that
    # was dark to begin with would only have turned the descents muddy.
    'day': ((243, 237, 227), (72, 69, 64), 1.0),
}


def textures():
    os.makedirs(OUT, exist_ok=True)
    for face, (base, ink, keep) in FACES.items():
        for i, role in enumerate(ROLES):
            a = GEN[role](100 + i) * keep
            img = compose(base, ink, a)
            path = os.path.join(OUT, 'bg-%s-%s.jpg' % (face, role))
            img.save(path, 'JPEG', quality=80, optimize=True)
            print('%s  %dx%d  %d KB' % (os.path.relpath(path, ROOT), W, H, os.path.getsize(path) // 1024))


# ── heroes ────────────────────────────────────────────────────────────
WRAP = '''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&display=swap" rel="stylesheet">
<style>
  html,body{margin:0;width:%(w)dpx;height:%(h)dpx;overflow:hidden;background:%(paper)s}
  :root{--paper:transparent}
  .field{position:absolute;inset:0;background:url('%(field)s') center/cover;opacity:%(fop)s}
  .dia{position:absolute;left:50%%;top:50%%;transform:translate(-50%%,-50%%);width:%(dw)dpx}
  .dia svg{width:100%%;height:auto;display:block}
  .dia img{width:100%%;height:auto;display:block}
  .diagram-caption{font-family:'DM Sans',sans-serif;font-weight:700;font-size:15px;letter-spacing:.04em}
  .dg-reveal,.dg-reveal-1{opacity:1}
  text{font-family:'DM Sans',sans-serif}
</style></head><body>
<div class="field"></div>
<div class="dia">%(dia)s</div>
</body></html>'''


def hero(slug):
    """Render the page's diagram over a contour field in its own accent."""
    import subprocess
    c = json.load(open(os.path.join(CONTENT, slug + '.json'), encoding='utf-8'))
    pal = c['palette']
    paper = pal.get('paper', '#FDF7F5')
    accent = hex_rgb(pal.get('accent', '#888888'))
    dark = c['kind'] == 'descent'
    base = hex_rgb(paper)
    field = compose(base, accent, contours(int(sum(accent)) + 11, 0.42 if dark else 0.30, freq=7.0, width=0.06))
    fpath = os.path.join(HERE, '_field.png')
    field.save(fpath)
    h = c['hero']
    if h['svg']:
        dia = h['svg'].replace('Inter, sans-serif', "'DM Sans', sans-serif")
        dia = dia.replace('fill="var(--paper)"', 'fill="none"')
        dw = 1180
    else:
        dia = '<img src="file:///%s" alt="">' % os.path.join(ROOT, h['img']['src']).replace('\\', '/')
        dw = 760
    html = WRAP % dict(w=W, h=H, paper=paper, field='file:///' + fpath.replace('\\', '/'),
                       fop='1', dw=dw, dia=dia)
    tmp = os.path.join(HERE, '_hero.html')
    png = os.path.join(HERE, '_hero.png')
    open(tmp, 'w', encoding='utf-8').write(html)
    subprocess.run(['node', os.path.join(HERE, 'render_hero.js'), tmp, png], check=True)
    img = Image.open(png).convert('RGB')
    path = os.path.join(OUT, 'hero-%s.jpg' % slug)
    img.save(path, 'JPEG', quality=86, optimize=True)
    for f in (tmp, fpath, png):
        os.remove(f)
    print('%s  %dx%d  %d KB' % (os.path.relpath(path, ROOT), W, H, os.path.getsize(path) // 1024))


def heroes(slugs):
    os.makedirs(OUT, exist_ok=True)
    for slug in slugs:
        hero(slug)


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--textures' in sys.argv:
        textures()
    if args or '--textures' not in sys.argv:
        slugs = args or sorted(f[:-5] for f in os.listdir(CONTENT) if f.endswith('.json'))
        heroes(slugs)
