#!/usr/bin/env python3
"""Soft aerial clouds, drawn from noise: white, transparent-edged PNGs for a layer
that drifts across a page, the way the English Heritage myths map does it.

    python tools/make_clouds.py <out-dir> [--count 3] [--seed 1]

Innes, 2026-09-26: "get aerial shot of clouds moving in the background like in
the https://mythsmap.english-heritage.org.uk/ ... can you make ones like
that?" Their three cloud images are English Heritage's artwork, so these are
our own, made from nothing but numbers: nothing is traced or sampled.

HOW. A cloud seen from above is a cluster of round lobes with fractal,
wispy edges, lit from one side. So: the silhouette is a union of soft
gaussian lobes of random size along a lazy spine; it is eroded and
feathered by fractal noise (several octaves of smoothed random grids);
alpha is a smoothstep of that density, so the core is dense and the rim
thins into wisps; the shading takes the light from the upper left off the
density's own slope, cool grey on the shadow side, warm white on top.
"""
import argparse
import os
import numpy as np
from PIL import Image

W, H = 820, 448


def noise(rng, w, h, octaves=6, base=4):
    """Fractal value noise in [0, 1]: random grids, each smoothed up to size."""
    acc = np.zeros((h, w), np.float32)
    amp, total = 1.0, 0.0
    for o in range(octaves):
        gw, gh = base * 2 ** o + 1, max(2, int(base * 2 ** o * h / w) + 1)
        g = rng.random((gh, gw)).astype(np.float32)
        layer = np.asarray(Image.fromarray((g * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC), np.float32) / 255
        acc += amp * layer
        total += amp
        amp *= 0.5
    return acc / total


def smoothstep(a, b, x):
    t = np.clip((x - a) / (b - a), 0, 1)
    return t * t * (3 - 2 * t)


def blur(a, r):
    """Gaussian-ish blur by down- and up-sampling (fast, and smooth enough for light)."""
    h, w = a.shape
    k = max(1, int(r))
    small = Image.fromarray(np.clip(a * 255, 0, 255).astype(np.uint8)).resize((max(2, w // k), max(2, h // k)), Image.BILINEAR)
    return np.asarray(small.resize((w, h), Image.BICUBIC), np.float32) / 255


def cloud(seed, cw=1000, ch=600):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:ch, 0:cw].astype(np.float32)
    lobes = []                                   # (cx, cy, r)
    # 1. big lobes along a lazy spine, largest in the middle
    n = int(rng.integers(5, 8))
    for i in range(n):
        t = i / (n - 1)
        r = (55 + 70 * np.sin(np.pi * (0.15 + 0.7 * t))) * rng.uniform(0.8, 1.1)
        lobes.append((cw * (0.2 + 0.6 * t) + rng.normal(0, 14), ch * 0.56 + rng.normal(0, 16) - 0.25 * r, r))
    # 2. puffs budding on the upper rim of each big lobe
    for cx, cy, r in list(lobes):
        for _ in range(3):
            ang = rng.uniform(np.pi * 1.05, np.pi * 1.95)              # the upper half
            lobes.append((cx + np.cos(ang) * r * 0.7, cy + np.sin(ang) * r * 0.7, r * rng.uniform(0.35, 0.6)))
    # domain warp: bend the whole field by noise, so no lobe stays a circle
    wx = noise(rng, cw, ch, octaves=5, base=5) - 0.5
    wy = noise(rng, cw, ch, octaves=5, base=5) - 0.5
    xw, yw = xx + 70 * wx, yy + 55 * wy
    dens = np.zeros((ch, cw), np.float32)
    for cx, cy, r in lobes:                                          # a sum: lobes merge
        dens += np.exp(-(((xw - cx) ** 2) + ((yw - cy) ** 2) * 1.2) / (2 * (r * 0.7) ** 2))
    dens = np.tanh(dens * 1.1)
    # a flatter base: cumulus seen from above still sits on a level underside
    dens *= smoothstep(ch * 0.80, ch * 0.62, yy) * 0.3 + 0.7
    fine = noise(rng, cw, ch, octaves=7, base=10)
    billow = noise(rng, cw, ch, octaves=6, base=16)
    d = dens * (0.66 + 0.5 * fine + 0.16 * billow)
    # a long ramp: dense core, edges that thin out rather than stop
    alpha = 0.94 * smoothstep(0.16, 0.78, d) ** 1.25
    # light from the upper left: the blurred density against itself shifted toward the light;
    # a small blur picks out each puff, a larger one gives the mass its roundness
    lit = np.zeros_like(d)
    for rad, sh, k in ((6, 5, 3.2), (18, 14, 2.0)):
        db = blur(d, rad)
        lit += k * (db - np.roll(np.roll(db, sh, axis=0), sh, axis=1))
    lit = np.clip(0.55 + lit, 0, 1)
    core = blur(d, 40)                                   # deep inside is brighter than the rim
    shade = 0.70 + 0.24 * lit + 0.08 * smoothstep(0.3, 0.8, core) + 0.04 * (fine - 0.5)
    shade = shade + 0.18 * (1 - smoothstep(0.1, 0.6, alpha))   # no dark fringe where it thins
    shade = np.clip(shade, 0.64, 1.0)
    r = 255 * shade
    g = 255 * np.clip(shade * 0.997 + 0.003, 0, 1)
    b = 255 * np.clip(shade * 1.015 + 0.018, 0, 1)
    rgba = np.dstack([r, g, b, alpha * 255]).clip(0, 255).astype(np.uint8)
    ys, xs = np.nonzero(rgba[..., 3] > 3)
    return Image.fromarray(rgba, 'RGBA').crop((max(0, xs.min() - 12), max(0, ys.min() - 12),
                                               min(cw, xs.max() + 12), min(ch, ys.max() + 12)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('--count', type=int, default=3)
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for i in range(a.count):
        im = cloud(a.seed * 100 + i)
        p = os.path.join(a.out, 'cloud-%d.png' % (i + 1))
        im.save(p, optimize=True)
        print('  %s  %dx%d  %d KB' % (p, im.width, im.height, os.path.getsize(p) // 1024))


if __name__ == '__main__':
    main()
