#!/usr/bin/env python3
"""Score text placement on a Block Camp deck against its own artwork.

Three questions, all answered by measurement:

  PLACEMENT   of the six placements the deck can express (left|right x
              top|center|bottom), is the one in use meaningfully busier under
              the text than the best one? Busy is local detail - standard
              deviation - not brightness: a villager and a wall can be the
              same colour, only one of them has detail. The score mixes the
              mean with the 90th percentile so a hot edge under one corner of
              a block counts, instead of being averaged away by the calm rest.

  BOX WIDTH   is a painted box far wider than the longest line inside it?

  GROUP WIDTH boxes that must match each other - options, drop targets, match
              cards - are judged as a group against the widest line in the
              group, so uniformity is kept but bloat is still caught.

Usage: python3 check-placement.py <deck.html> [more decks...]
"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
DUMP = os.path.join(HERE, 'dump-rects.js')
# Innes's own placement calls. A finding on a pinned slide is still REPORTED -
# the measurement is worth seeing - but it is marked as overruled, because the
# measurement cannot see a subject and he can.
PINS = json.load(open(os.path.join(HERE, 'pins.json')))

GRID       = 96      # detail map resolution
BETTER     = 1.30    # flag a placement when current/best >= this
TOO_WIDE   = 1.45    # flag a box when width / longest line >= this
MIN_BOX_W  = 0.10    # a narrow box that is too wide is not worth moving
P90_WEIGHT = 1.0     # how much a hot corner counts against a calm mean

# Boxes that must match their siblings; judged as a group, never alone.
# Boxes that must match their siblings: judged as a GROUP against the widest
# line in the group, so uniformity is kept but bloat is still caught.
GROUPED = {'.opt', '.match-item'}
# A drop target's width is a deliberate constant (see .sort-bins in the deck
# CSS): it has to hold the longest chip that can land in it, so its own label
# says nothing about how wide it should be. Checked by the chip gate instead.
EXEMPT = {'.sort-bin'}


def detail_map(path):
    im = Image.open(path).convert('L')
    w, h = im.size
    tw, th = 16, 9
    if w * th > h * tw:                       # crop sides, like background-size:cover
        nw = int(h * tw / th)
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:                                     # crop top and bottom
        nh = int(w * th / tw)
        im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    a = np.asarray(im.resize((GRID * 4, GRID * 4), Image.LANCZOS), dtype=np.float32)
    sd = a.reshape(GRID, 4, GRID, 4).std(axis=(1, 3))
    return sd / sd.max() if sd.max() else sd


def busy(sd, b):
    """How busy the artwork is under one ink box: mean plus a hot-spot term."""
    x0 = max(0, min(GRID - 1, int(b['x'] * GRID)))
    x1 = max(x0 + 1, min(GRID, int(round((b['x'] + b['w']) * GRID))))
    y0 = max(0, min(GRID - 1, int(b['y'] * GRID)))
    y1 = max(y0 + 1, min(GRID, int(round((b['y'] + b['h']) * GRID))))
    r = sd[y0:y1, x0:x1]
    return float(r.mean()) + P90_WEIGHT * float(np.percentile(r, 90))


def slot_score(sd, boxes):
    """Area-weighted busyness of a whole placement."""
    num = den = 0.0
    for b in boxes.values():
        a = b['w'] * b['h']
        num += busy(sd, b) * a
        den += a
    return num / den if den else 0.0


def check(deck):
    pins = PINS.get(os.path.basename(deck), {})
    raw = subprocess.run(['node', DUMP, deck], capture_output=True, text=True)
    if raw.returncode != 0:
        print(f'{deck}: dumper failed\n{raw.stderr[-800:]}', file=sys.stderr)
        return []
    data = json.loads(raw.stdout)
    root = os.path.dirname(os.path.abspath(deck))

    findings, cache = [], {}
    for s in data['slides']:
        bg = s.get('bg')
        sd = None
        if bg:
            p = os.path.join(root, bg)
            if p not in cache:
                cache[p] = detail_map(p) if os.path.exists(p) else None
            sd = cache[p]

        # ── placement ────────────────────────────────────────────────
        if sd is not None and s['slots']:
            cur = f"{s['side']}/{s['vpos'] or 'center'}"
            scores = {k: slot_score(sd, v) for k, v in s['slots'].items() if v}
            if cur in scores and scores[cur] > 0:
                best = min(scores, key=scores.get)
                if best != cur and scores[cur] / scores[best] >= BETTER:
                    pin = pins.get(str(s['index']))
                    findings.append(dict(
                        slide=s['index'],
                        kind='PLACEMENT (pinned)' if pin else 'PLACEMENT',
                        sel=s['type'],
                        detail=f"{cur} -> {best}   busy {scores[cur]:.3f} vs "
                               f"{scores[best]:.3f} (x{scores[cur]/scores[best]:.2f})"
                               + (f"  OVERRULED: {pin['why']}" if pin else ''),
                        bg=os.path.basename(bg), fix=best))

        # ── overflow ────────────────────────────────────────────────
        if s.get('overflow', 0) > 1:
            findings.append(dict(
                slide=s['index'], kind='OVERFLOW', sel=s['type'],
                detail=f"content paints {s['overflow']}px outside the canvas",
                bg=os.path.basename(bg) if bg else '', fix=''))

        # ── single box too wide ──────────────────────────────────────
        groups = {}
        for r in s['painted']:
            if r['sel'] in EXEMPT:
                continue
            if r['sel'] in GROUPED:
                groups.setdefault(r['sel'], []).append(r)
                continue
            if r['w'] < MIN_BOX_W or r['need'] <= 0:
                continue
            ratio = (r['w'] - r.get('pad', 0)) / r['need']
            if ratio >= TOO_WIDE:
                findings.append(dict(
                    slide=s['index'], kind='BOX TOO WIDE', sel=r['sel'],
                    detail=f"{r['w']*100:.0f}% of frame for text needing "
                           f"{r['need']*100:.0f}% plus {r.get('pad',0)*100:.0f}%"
                           f" padding (x{ratio:.2f})",
                    bg=os.path.basename(bg) if bg else '', fix=''))

        # ── group of boxes too wide ──────────────────────────────────
        for sel, rs in groups.items():
            w = max(r['w'] for r in rs)
            pad = max(r.get('pad', 0) for r in rs)
            need = max(r['need'] for r in rs)
            if w < MIN_BOX_W or need <= 0:
                continue
            ratio = (w - pad) / need
            if ratio >= TOO_WIDE:
                findings.append(dict(
                    slide=s['index'], kind='GROUP TOO WIDE', sel=sel,
                    detail=f"{len(rs)} boxes at {w*100:.0f}% of frame, widest "
                           f"line {need*100:.0f}% plus {pad*100:.0f}% padding"
                           f" (x{ratio:.2f})",
                    bg=os.path.basename(bg) if bg else '', fix=''))
    return findings


def main():
    total = 0
    for deck in sys.argv[1:]:
        fs = check(deck)
        print(f"\n=== {os.path.basename(deck)}  ({len(fs)} findings) ===")
        for f in sorted(fs, key=lambda f: (f['slide'], f['kind'])):
            print(f"  slide {f['slide']:<3} {f['kind']:<18} {f['sel']:<12}"
                  f" {f['detail']}  {f['bg']}")
        total += len(fs)
    print(f"\n{total} findings across {len(sys.argv)-1} deck(s)")


if __name__ == '__main__':
    main()
