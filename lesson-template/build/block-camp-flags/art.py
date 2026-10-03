"""Raise the Lookout, Phase B: Innes's two plates in, measured, out.

    py lesson-template/build/block-camp-flags/build.py --ingest   # clean + webps
    py lesson-template/build/block-camp-flags/build.py --trace    # storeys.json
    py lesson-template/build/block-camp-flags/build.py --proof    # trace proof sheet

docs/LOOKOUT-DESIGN.md sections 8 and 9. The two raw plates live in the
gitignored incoming/lookout/ (lookout.png: the finished nine-level tower on a
transparent ground; summit.png: the empty pad). Nothing here touches
tools/prep-artwork.py: that writes 16:9 JPEG and would drop the alpha.

--ingest  cleans the tower's alpha (ChatGPT leaves a faint haze over most of
          the frame: below 16 -> 0, above 240 -> 255, only the tower's own
          connected body and a 4 px margin round it kept, a 1 px erode, the
          soft edge's colour taken from the solid pixels beside it) and
          writes BlockCamp/lookout/:
            lookout.webp        768 x 1152, the clean tower, alpha
            lookout-ghost.webp  768 x 1152, the blueprint ghost: the same
                                pixels, grey, washed toward the summit's sky
                                at the height each row stands at, with
                                Sobel edge lines (design 9.2)
            lookout-sm.webp     the tower for the Results window
            summit.webp         1024 x 1536
            summit-768.webp     768 x 1152
            summit-sm.webp      the summit for the Results window
--trace   measures storeys.json (beside this file): the nine bands cut at the
          painted ring beams (a clip polygon each), the pad on summit.png and
          where the tower stands on it, the lip (the summit's own bushes and
          kerb in front of the tower foot), the contact shadow, and every
          anchor the code draws at: flags, lamps, tags, trim caps, the gold
          effects, the cradle, the eave. Plus the sha1 of both plates:
          build.py --check fails if either changes without a re-trace.
--proof   a PIL sheet of the trace (cuts, anchors, placement, ghost, the
          bands built one at a time) for review before shipping.

All coordinates in storeys.json are MASTER pixels (the 1024 x 1536 plates).
"""
import hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SRC_DIR = os.path.join(REPO, 'incoming', 'lookout')
SRC_TOWER = os.path.join(SRC_DIR, 'lookout.png')
SRC_SUMMIT = os.path.join(SRC_DIR, 'summit.png')
OUT_DIR = os.path.join(REPO, 'BlockCamp', 'lookout')
STOREYS_JSON = os.path.join(HERE, 'storeys.json')
CLEAN_PNG = os.path.join(SRC_DIR, 'lookout-clean.png')     # gitignored, for --trace / --proof

W, H = 1024, 1536
# what each output is, and its size: (file, width, quality)
# (file, width, quality, alpha quality)
OUTS = {
    'lookout': ('lookout.webp', 768, 84, 100),
    'ghost': ('lookout-ghost.webp', 768, 56, 62),
    'lookoutSm': ('lookout-sm.webp', 384, 72, 90),
    'summit': ('summit.webp', 1024, 82, None),
    'summit768': ('summit-768.webp', 768, 80, None),
    'summitSm': ('summit-sm.webp', 256, 62, None),
}
MIN_TOP = 0.06          # design 9: the tower's top must sit at least 6% of the plate below its top
HEADROOM = 0.10         # and we aim for 10%, so the beam has sky to rise into
BASE_OF_PAD = 0.70      # the stone base is this share of the pad's front width


def sha1(path):
    return hashlib.sha1(open(path, 'rb').read()).hexdigest()


def need_src():
    miss = [p for p in (SRC_TOWER, SRC_SUMMIT) if not os.path.exists(p)]
    if miss:
        raise SystemExit('missing %s - the raw plates live in the gitignored incoming/lookout/' %
                         ', '.join(os.path.relpath(p, REPO) for p in miss))


def _np():
    import numpy as np
    from PIL import Image
    from scipy import ndimage
    return np, Image, ndimage


# ── ingest ────────────────────────────────────────────────────────────────
def clean_alpha(rgba):
    """The tower alone, with its own soft edge (design 1, 'ChatGPT alpha is
    not clean'). Returns (rgba uint8, stats)."""
    np, Image, nd = _np()
    a = rgba[..., 3].astype(np.int32)
    before = {'partial': int(((a > 0) & (a < 255)).sum()), 'bbox': bbox(a > 0)}
    a[a < 16] = 0
    a[a > 240] = 255
    body = a >= 128
    lab, n = nd.label(body, structure=np.ones((3, 3)))
    if not n:
        raise SystemExit('lookout.png: no opaque body at all')
    sizes = nd.sum(body, lab, range(1, n + 1))
    keep = lab == (int(np.argmax(sizes)) + 1)
    # small solid pieces that touch the body's margin are the tower's too
    # (a lantern hook, a rope); anything further out is haze
    zone = nd.binary_dilation(keep, iterations=4)
    near = np.isin(lab, np.unique(lab[zone & body]))
    keep = keep | (near & body)
    zone = nd.binary_dilation(keep, iterations=4)
    a[~zone] = 0
    # erode 1 px: the outermost ring carries the ground ChatGPT painted on
    a = nd.minimum_filter(a, size=3)
    rgb = rgba[..., :3].astype(np.float64)
    solid = (a == 255).astype(np.float64)
    soft = (a > 0) & (a < 255)
    k = np.ones((5, 5))
    wsum = nd.convolve(solid, k, mode='constant')
    for c in range(3):
        csum = nd.convolve(rgb[..., c] * solid, k, mode='constant')
        ch = rgb[..., c]
        ok = soft & (wsum > 0)
        ch[ok] = csum[ok] / wsum[ok]
    rgb[a == 0] = 0
    out = np.dstack([np.clip(rgb, 0, 255), a]).astype(np.uint8)
    after = {'partial': int(soft.sum()), 'bbox': bbox(a > 0), 'opaque': int((a == 255).sum())}
    return out, {'before': before, 'after': after}


def bbox(mask):
    import numpy as np
    ys, xs = np.where(mask)
    if not len(xs):
        return None
    return [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]


def save_webp(im, name, width, q, aq=None):
    from PIL import Image
    w = width
    h = round(im.height * w / im.width)
    if (w, h) != im.size:
        im = im.resize((w, h), Image.LANCZOS)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, name)
    kw = {'quality': q, 'method': 6}
    if im.mode == 'RGBA':
        kw['alpha_quality'] = aq or 90
    im.save(path, 'WEBP', **kw)
    return path, os.path.getsize(path)


def ghost(rgba, sky_rows, blueprint):
    """The blueprint: the tower's own pixels, grey, washed 60% toward the sky
    colour the summit has at the plate row each tower row stands at, at a
    light alpha; then its Sobel edges (luminance and alpha) as lines in the
    BLUEPRINT token, stronger. One grid with the master: a ghost storey and a
    built one can never be out of register (design 9.2)."""
    np, Image, nd = _np()
    rgb = rgba[..., :3].astype(np.float64)
    a = rgba[..., 3].astype(np.float64) / 255
    lum = rgb @ [0.299, 0.587, 0.114]
    sky = np.asarray(sky_rows, dtype=np.float64)[:, None, :]          # H x 1 x 3
    # the fill is a soft wash (the lines carry the drawing), so it compresses
    grey = np.repeat(nd.gaussian_filter(lum, 1.4)[..., None], 3, axis=2)
    wash = grey * 0.4 + sky * 0.6
    # edges: on luminance (the block seams) and on alpha (the silhouette)
    sl = np.hypot(nd.sobel(lum * a, 0), nd.sobel(lum * a, 1))
    sa = np.hypot(nd.sobel(a, 0), nd.sobel(a, 1)) * 255
    e = np.clip(np.maximum(sl / 260.0, sa / 400.0), 0, 1)
    e = np.where(e > 0.28, np.clip((e - 0.28) / 0.4, 0, 1), 0)
    bp = np.array(blueprint, dtype=np.float64)[None, None, :]
    col = wash * (1 - e[..., None]) + bp * e[..., None]
    alpha = np.clip(a * 0.34 + e * 0.62 * np.minimum(1, a * 4), 0, 1)
    out = np.dstack([np.clip(col, 0, 255), alpha * 255]).astype(np.uint8)
    return out


def hexrgb(c):
    c = c.lstrip('#')
    return [int(c[i:i + 2], 16) for i in (0, 2, 4)]


# ── trace ─────────────────────────────────────────────────────────────────
# The summit's pad corners are read off a 2x crop and drawn on the --proof
# sheet; its rows (the back and front edge, the kerb) are measured. The left
# corners sit behind ChatGPT's bushes, so no edge detector finds them; the
# pad is the brief's "exact centre" square, and the measured right corners
# agree with these to within 10 px.
PAD_HINT = {'backL': 350, 'backR': 677, 'frontL': 265, 'frontR': 762}
FOOT_SINK = 6          # the foot stands this far below the kerb's top edge, behind the lip
LAMP_W = 26                            # master px: the lantern body, 3 cells wide
LAMP_H = round(5 * LAMP_W / 3)         # and 5 cells tall (lid, three of glass, foot)
TAG = 44                               # master px: a number tag
FLAG_H = 92                            # master px: the 16-cell flag sprite


def _masks(m):
    import numpy as np
    rgb = m[..., :3].astype(np.float64)
    a = m[..., 3].astype(np.float64)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    lum = rgb @ [0.299, 0.587, 0.114]
    mx, mn = rgb.max(2), rgb.min(2)
    sat = (mx - mn) / np.maximum(mx, 1)
    op = a >= 200
    return {
        'a': a, 'lum': lum, 'sat': sat, 'op': op,
        'wood': ((r - b) > 40) & (r > g) & (g > b) & op & ~((r > 200) & (g > 180)),
        'green': (g > r + 12) & (g >= b - 25) & op,
        'glass': (b > r + 15) & (b >= g) & op,
        'brass': (r > 150) & (g > 105) & (b < 90) & ((r - b) > 90) & op,
        'iron': (lum < 60) & (sat < 0.45) & op,
        'stone': (sat < 0.2) & (lum > 120) & op,
    }


def _beam_edges(M, top, bottom, min_h):
    """The bottom edges of the full-width timber beams (design 9.1: 'the
    builder proposes the cuts from the row profile'): rows under at least 12
    rows of timber across the bays' middle, where the light drops or the
    timber ends. From the foot up, an edge closer than min_h to the last one
    kept is the same beam's shadow or a deck plank, and is skipped."""
    import numpy as np
    x0, x1 = 380, 640
    prof = M['wood'][:, x0:x1].mean(1)
    L = np.where(M['op'], M['lum'], np.nan)
    with np.errstate(all='ignore'):
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            Lc = np.nanmean(L[:, x0:x1], 1)
    found = []
    for y in range(top + 12, bottom):
        if prof[y - 12:y].min() >= 0.8 and (Lc[y] < Lc[y - 3] - 22 or prof[y] < 0.6):
            if not found or y - found[-1] > 20:
                found.append(y)
    kept, last = [], bottom + 1
    for y in sorted(found, reverse=True):
        if last - y >= min_h:
            kept.append(y)
            last = y
    return sorted(kept), found


def _refine(M, y0, up=10, dn=14):
    """One cut, column by column: the strongest light-to-dark step under a
    timber or iron pixel near y0 (a beam's bottom face meeting the shadow
    under it), median-filtered so a cut follows the side face's lower beam
    and the corbels under the deck, not single pixels."""
    import numpy as np
    from scipy import ndimage as nd
    lum, op = M['lum'], M['op']
    beam = M['wood'] | ((M['sat'] < 0.32) & (lum > 45) & op)
    ys = np.arange(y0 - up, y0 + dn)
    G = (lum[ys - 1] - lum[ys + 1]) * beam[ys - 1]
    out = np.full(W, y0)
    for x in range(W):
        if not op[y0 - up:y0 + dn, x].any():
            continue
        col = G[:, x]
        i = int(np.argmax(col))
        if col[i] > 25:
            out[x] = ys[i]
    return nd.median_filter(out, size=21, mode='nearest')


def _runs(arr):
    """[[x0, x1, y], ...] for a per-column cut: one step per run of equal y
    (x1 exclusive)."""
    out, x = [], 0
    while x < len(arr):
        j = x
        while j + 1 < len(arr) and arr[j + 1] == arr[x]:
            j += 1
        out.append([int(x), int(j + 1), int(arr[x])])
        x = j + 1
    return out


def at(runs, x):
    for x0, x1, y in runs:
        if x0 <= x < x1:
            return y
    return runs[-1][2]


def _ext(M, y0, y1):
    """The opaque x extent of rows y0..y1."""
    import numpy as np
    xs = np.where(M['op'][y0:y1 + 1].any(0))[0]
    return int(xs.min()), int(xs.max())


def _box(M, key, box):
    """bbox and centroid of a material inside a search box (the region of
    each object on the frozen plate; the measurement is the pixels' own)."""
    import numpy as np
    x0, y0, x1, y1 = box
    sub = M[key][y0:y1, x0:x1]
    ys, xs = np.where(sub)
    if not len(xs):
        raise SystemExit('trace: no %s pixels in %r' % (key, box))
    return {'box': [int(x0 + xs.min()), int(y0 + ys.min()), int(x0 + xs.max()), int(y0 + ys.max())],
            'c': [int(round(x0 + xs.mean())), int(round(y0 + ys.mean()))]}


def _plates(M, top, bot):
    """The iron plates where a beam meets its posts: low-saturation blocks in
    the beam's rows. These carry the trim tier."""
    import numpy as np
    from scipy import ndimage as nd
    band = np.zeros(M['op'].shape, bool)
    band[top - 6:bot + 12] = True
    pl = (M['sat'] < 0.32) & (M['lum'] > 45) & (M['a'] >= 250) & band
    pl = nd.binary_opening(pl, iterations=1)
    lab, n = nd.label(pl)
    out = []
    for i, sl in enumerate(nd.find_objects(lab)):
        ys, xs = sl
        h, w = ys.stop - ys.start, xs.stop - xs.start
        area = int((lab[sl] == i + 1).sum())
        if area >= 240 and w >= 10 and 20 <= h <= 34 and area / (w * h) > 0.6:
            out.append([int(xs.start), int(ys.start), int(w), int(h)])
    return sorted(out)


def measure_pad(summit):
    """The pad on summit.png: its back and front edge rows (the strongest
    light-to-dark steps across its middle columns), the kerb under the front
    edge, the corners, and the darkest ground tone round it."""
    import numpy as np
    from scipy import ndimage as nd
    s = summit.astype(np.float64)
    lum = nd.uniform_filter(s @ [0.299, 0.587, 0.114], 3)
    c = lum[:, 430:600].mean(1)

    def edge(y0, y1):
        d = c[y0:y1 - 3] - c[y0 + 3:y1]
        return y0 + int(np.argmax(d)) + 2
    back, front = edge(1300, 1360), edge(1362, 1420)
    k = front + 2
    while k < front + 30 and c[k] < c[front - 3] - 25:
        k += 1
    P = PAD_HINT
    reg = s[back:k + 20, 200:830].reshape(-1, 3)
    l2 = reg @ [0.299, 0.587, 0.114]
    dk = reg[l2 <= np.percentile(l2, 4)].mean(0)
    return {'back': int(back), 'front': int(front), 'kerbBottom': int(k),
            'cx': round((P['frontL'] + P['frontR'] + P['backL'] + P['backR']) / 4, 1),
            'frontW': P['frontR'] - P['frontL'], 'backW': P['backR'] - P['backL'],
            'poly': [[P['backL'], int(back)], [P['backR'], int(back)], [P['frontR'], int(front)], [P['frontL'], int(front)]],
            'groundDk': '#%02x%02x%02x' % tuple(int(v) for v in dk)}


def sky_rows(summit, place):
    """For every master row of the tower, the summit's colour behind it at
    the plate row it stands at (a median across the tower's columns): what
    the ghost is washed toward."""
    import numpy as np
    s = summit.astype(np.float64)
    x0 = max(0, int(place['ox'] + place['s'] * 250))
    x1 = min(W, int(place['ox'] + place['s'] * 780))
    out = []
    for y in range(H):
        py = min(H - 1, max(0, int(round(place['oy'] + place['s'] * y))))
        out.append(np.median(s[py, x0:x1], axis=0))
    return out


def trace(clean, summit):
    """storeys.json: everything the renderer draws at, in master pixels."""
    import numpy as np
    from scipy import ndimage as nd
    M = _masks(clean)
    bb = bbox(M['a'] > 0)
    top, bottom = bb[1], bb[3]
    th = bottom - top + 1
    min_h = int(0.06 * th) + 1
    beams, proposed = _beam_edges(M, top, bottom, min_h)
    if len(beams) != 6:
        raise SystemExit('trace: expected 6 beam edges (five open levels and the deck), found %r of %r' % (beams, proposed))
    # above the highest beam: the deck (to the railing's top), the cabin (to
    # the roof's lowest course), the roof
    rf = np.full(W, -1)
    for x in range(W):
        col = np.where(M['green'][top + 100:top + 190, x])[0]
        if len(col):
            rf[x] = top + 100 + col.max() + 1
    roof_y = int(np.median(rf[rf > 0]))
    rf[rf < 0] = roof_y
    roof_cut = nd.median_filter(rf, size=9, mode='nearest')
    wf = M['wood'][:, 300:740].mean(1)
    rail = next(y for y in range(roof_y + 40, beams[0]) if wf[y] > 0.5)
    cuts = [_runs(roof_cut), _runs(np.full(W, rail))] + [_runs(_refine(M, y)) for y in beams]
    lines = [[[0, W, 0]]] + cuts + [[[0, W, H]]]
    cx = int(round((bb[0] + bb[2]) / 2))
    S = {}
    for i in range(9):
        n = 9 - i
        t, b = lines[i], lines[i + 1]
        S[n] = {'n': n, 'top': t, 'bot': b, 'y0': max(at(t, cx), top), 'y1': min(at(b, cx), bottom + 1)}

    # each open level's (and the deck's) floor beam: the solid timber rows
    # over its bottom cut
    beam_top = {}
    for n in range(2, 8):
        yb = S[n]['y1']
        col = M['wood'][yb - 45:yb, 380:590].mean(1)
        k = len(col) - 1
        while k > 0 and col[k - 1] >= 0.97:
            k -= 1
        beam_top[n] = yb - 45 + k
    caps = {n: [p for p in _plates(M, beam_top[n], S[n]['y1']) if p[1] < S[n]['y1'] + 14] for n in range(2, 8)}
    caps[8] = _plates(M, roof_y, roof_y + 26)
    # storey 1's caps are on its cornerstones: the beam over them is storey
    # 2's floor
    caps[1] = [[p[0], p[1] + p[3] + 2, p[2], p[3]] for p in caps[2] if p[2] >= 20]
    # storey 9's on the ends of the roof's lowest course
    gx = np.where(M['green'][roof_y - 24:roof_y - 4].any(0))[0]
    caps[9] = [[int(gx.min()), roof_y - 24, 22, 20], [int(gx.max()) - 21, roof_y - 24, 22, 20]]

    # lamps: an iron arm from the left end of the overhang over each storey
    lamps = {}
    lx, _ = _ext(M, S[2]['y1'] - 14, S[2]['y1'] - 1)
    lamps[1] = {'hook': [lx, S[1]['y0']], 'mode': 'hang'}
    for n in range(2, 7):
        # the outside of the left post (the deck's corbels over bay 6 reach
        # further out, and lamp 7 hangs there)
        lx, _ = _ext(M, S[n]['y0'] + 40, S[n]['y1'] - 40)
        lamps[n] = {'hook': [lx, S[n]['y0']], 'mode': 'hang'}
    deck = _box(M, 'wood', (230, S[7]['y0'] + 40, 360, S[7]['y0'] + 85))     # the deck floor's left end
    lamps[7] = {'hook': [deck['box'][0], deck['box'][3] + 1], 'mode': 'hang'}
    lx, _ = _ext(M, roof_y - 6, roof_y - 1)
    lamps[8] = {'hook': [lx + 8, at(cuts[0], lx + 8)], 'mode': 'hang'}
    gx2 = np.where(M['green'][roof_y - 48:roof_y - 28].any(0))[0]
    stand_x = int((gx.min() + gx2.min()) / 2)
    course_top = roof_y - 4
    while course_top > top and M['green'][course_top - 1, stand_x]:
        course_top -= 1
    lamps[9] = {'hook': [stand_x, course_top], 'mode': 'stand'}

    # flags: the pole's foot, on each storey's right corner
    flags = {}
    _, r1 = _ext(M, S[1]['y1'] - 60, S[1]['y1'] - 1)
    flags[1] = [r1 + 14, S[1]['y1'] - 1]
    for n in range(2, 7):
        _, rx = _ext(M, beam_top[n], S[n]['y1'] - 1)
        flags[n] = [rx + 8, beam_top[n] + 6]
    _, dr = _ext(M, deck['box'][1], deck['box'][3])
    # off the deck's end, low enough that its pole clears flag 8's foot
    flags[7] = [dr + 8, max(deck['box'][3], rail + FLAG_H + 6)]
    lan = _box(M, 'iron', (620, S[8]['y0'], 760, S[8]['y1']))                # the cabin's own lantern
    flags[8] = [lan['box'][2] + 14, rail]
    _, rr = _ext(M, roof_y - 24, roof_y - 4)
    flags[9] = [rr - 12, course_top]

    # the gold effects (design 4), each measured inside its object's region
    fx = {}
    fx[1] = _box(M, 'iron', (538, S[1]['y0'] + 20, 620, S[1]['y0'] + 110))           # the lantern by the door
    fx[2] = _box(M, 'wood', (455, S[2]['y0'] + 8, 500, S[2]['y0'] + 50))             # the pulley ring under the beam
    fx[3] = _box(M, 'iron', (505, S[3]['y0'] + 20, 600, S[3]['y1'] - 20))            # the fire basket
    fx[4] = _box(M, 'iron', (420, S[4]['y0'] + 60, 500, S[4]['y1'] - 20))            # the hearth's dark mouth
    st4 = _box(M, 'stone', (430, S[4]['y0'], 500, S[4]['y0'] + 60))                  # the chimney
    fx[4]['chimney'] = [int((st4['box'][0] + st4['box'][2]) / 2), st4['box'][1]]
    fx[5] = _box(M, 'wood', (415, S[5]['y0'] + 6, 480, S[5]['y0'] + 64))             # the big arrow
    tel = _box(M, 'brass', (380, S[6]['y0'] + 20, 560, S[6]['y1'] - 20))                  # the telescope
    fx[6] = {'box': tel['box'], 'c': tel['c'], 'lens': [tel['box'][0] + 3, tel['box'][1] + 9]}
    cairn = _box(M, 'stone', (270, S[7]['y0'] + 10, 352, S[7]['y0'] + 70))
    boots = _box(M, 'wood', (356, S[7]['y0'] + 30, 400, S[7]['y0'] + 60))
    fx[7] = {'cairn': [cairn['c'][0], cairn['box'][1]], 'box': cairn['box'], 'boots': boots['box']}
    g = M['glass'][S[8]['y0']:S[8]['y1'], :]
    lab, _n = nd.label(nd.binary_closing(g, iterations=2))
    wins = []
    for sl in nd.find_objects(lab):
        ys, xs = sl
        if (ys.stop - ys.start) > 30 and (xs.stop - xs.start) > 14:
            wins.append([int(xs.start), int(S[8]['y0'] + ys.start), int(xs.stop - xs.start), int(ys.stop - ys.start)])
    fx[8] = {'windows': sorted(wins), 'lantern': lan['c']}
    c0, c1 = _ext(M, top, top + 26)
    fx[9] = {'cradle': [c0, top, c1, top + 28], 'c': [int((c0 + c1) / 2), top]}

    # ── on the summit ──
    pad = measure_pad(summit)
    base_l, base_r = _ext(M, bottom - 30, bottom)
    base_w = base_r - base_l + 1
    foot = pad['front'] + FOOT_SINK
    s_pad = BASE_OF_PAD * pad['frontW'] / base_w
    s_head = (foot - HEADROOM * H) / (bottom + 1 - top)
    s = round(min(s_pad, s_head), 4)
    place = {'s': s, 'ox': round(pad['cx'] - s * (base_l + base_r + 1) / 2, 2), 'oy': round(foot - s * (bottom + 1), 2),
             'foot': foot, 'by': 'pad' if s_pad <= s_head else 'headroom'}
    place['top'] = round(place['oy'] + s * top, 1)
    if place['top'] < MIN_TOP * H:
        raise SystemExit('trace: the tower top sits %.1f%% below the plate top (the floor is %d%%)'
                         % (100 * place['top'] / H, 100 * MIN_TOP))
    # the lip: the summit's own kerb and bushes in front of the foot, as steps
    sk = summit.astype(np.float64)
    r, g2, b = sk[..., 0], sk[..., 1], sk[..., 2]
    gravel = (r > g2) & (g2 > b) & ((sk @ [0.299, 0.587, 0.114]) > 95)
    lx0 = int(place['ox'] + s * base_l) - 40
    lx1 = int(place['ox'] + s * (base_r + 1)) + 40
    tops = []
    for x in range(lx0, lx1):
        y = foot
        while y > pad['front'] - 22 and not gravel[y - 1, x] and not gravel[y - 2, x]:
            y -= 1
        tops.append(min(y, pad['front'] + 1))
    tops = nd.median_filter(np.array(tops), size=7, mode='nearest')
    lip = {'top': [[lx0 + a, lx0 + b2, y] for a, b2, y in _runs(tops)], 'bottom': pad['kerbBottom'] + 2}
    shadow = {'cx': round(pad['cx'] - 0.18 * s * base_w, 1), 'cy': foot - 3, 'rx': round(0.66 * s * base_w, 1),
              'ry': 16, 'colour': pad['groundDk']}

    # each storey's dust (the build-in): its own lit, middle and dark tones
    bm = band_masks({'storeys': [S[q] for q in S]})
    for n in range(1, 10):
        sel = bm[n] & M['op']
        px = clean[..., :3][sel].astype(np.float64)
        lu = px @ [0.299, 0.587, 0.114]
        S[n]['dust'] = ['#%02x%02x%02x' % tuple(int(c) for c in np.median(px[(lu >= np.percentile(lu, q - 8)) & (lu <= np.percentile(lu, q + 8))], axis=0))
                        for q in (25, 55, 85)]
    for n in range(1, 10):
        st = S[n]
        st['mid'] = [cx, int((st['y0'] + st['y1']) / 2)]
        st['h'] = st['y1'] - st['y0']
        st['x0'], st['x1'] = _ext(M, st['y0'], st['y1'] - 1)
        st['caps'], st['lamp'], st['flag'], st['fx'] = caps[n], lamps[n], flags[n], fx[n]
        if n in beam_top:
            st['beamTop'] = beam_top[n]
    lamp_left = min(S[n]['lamp']['hook'][0] - LAMP_W - 6 for n in S)
    _, eave_r = _ext(M, roof_y - 8, roof_y - 1)
    return {
        'note': 'GENERATED by build.py --trace from incoming/lookout/ (docs/LOOKOUT-DESIGN.md 9). Master pixels.',
        'src': {'lookout': sha1(SRC_TOWER), 'summit': sha1(SRC_SUMMIT)},
        'size': [W, H], 'bbox': bb, 'towerH': th, 'minStorey': min_h,
        'beams': beams, 'beamsProposed': proposed, 'roof': roof_y, 'rail': rail,
        'storeys': [S[n] for n in range(1, 10)],
        'pad': pad, 'place': place, 'lip': lip, 'shadow': shadow,
        'tagX': round(lamp_left - 12 - TAG / 2, 1), 'tag': TAG, 'lampW': LAMP_W, 'lampH': LAMP_H, 'flagH': FLAG_H,
        'eave': [eave_r, roof_y], 'cradle': fx[9]['cradle'], 'beacon': fx[9]['c'],
        'files': {k: 'BlockCamp/lookout/' + v[0] for k, v in OUTS.items()},
    }


# ── masks from the trace (proof and checks) ──────────────────────────────
def cut_rows(T):
    """Each band's [top, bottom) per column, as two int arrays of length W."""
    import numpy as np
    out = {}
    for st in T['storeys']:
        t = np.zeros(W, int)
        b = np.zeros(W, int)
        for x0, x1, y in st['top']:
            t[x0:x1] = y
        for x0, x1, y in st['bot']:
            b[x0:x1] = y
        out[st['n']] = (t, b)
    return out


def band_masks(T):
    import numpy as np
    ys = np.arange(H)[:, None]
    return {n: (ys >= t[None, :]) & (ys < b[None, :]) for n, (t, b) in cut_rows(T).items()}


def coverage(T, clean):
    """The design 9.7 gate on the pixels: every pixel of the cleaned tower
    falls in exactly one band. Returns (share covered once, pixels in two)."""
    import numpy as np
    bm = band_masks(T)
    a = clean[..., 3] > 0
    count = np.zeros(a.shape, int)
    for m in bm.values():
        count += m
    covered = float((a & (count == 1)).sum()) / float(a.sum())
    return covered, int((count > 1).sum())


# ── proof ────────────────────────────────────────────────────────────────
def proof(T, clean, ghost_img, summit, path):
    """A PIL sheet of the trace, for review before shipping (design 9.7):
    the tower on the pad with every cut, cap, lamp, flag, tag and effect
    point drawn; the ghost; four band states; each cut at 1:1."""
    import numpy as np
    from PIL import Image, ImageDraw
    pl = T['place']
    s = pl['s']
    bm = band_masks(T)
    tower = Image.fromarray(clean)
    gh = Image.fromarray(ghost_img).resize((W, H), Image.LANCZOS)

    def state(built):
        m = np.zeros((H, W), bool)
        for n in built:
            m |= bm[n]
        return Image.fromarray(np.where(m[..., None], np.array(tower), np.array(gh)).astype(np.uint8))

    def P(x, y):
        return (pl['ox'] + s * x, pl['oy'] + s * y)

    def on_summit(img, marks=False):
        base = Image.fromarray(summit).convert('RGBA')
        tw = img.resize((round(W * s), round(H * s)), Image.LANCZOS)
        base.alpha_composite(tw, (round(pl['ox']), round(pl['oy'])))
        lipm = Image.new('L', (W, H), 0)
        dl = ImageDraw.Draw(lipm)
        for x0, x1, y in T['lip']['top']:
            dl.rectangle([x0, y, x1 - 1, T['lip']['bottom']], fill=255)
        base.paste(Image.fromarray(summit).convert('RGBA'), (0, 0), lipm)
        if not marks:
            return base.convert('RGB')
        d = ImageDraw.Draw(base)
        for st in T['storeys']:
            pts = []
            for x0, x1, y in st['top']:
                pts += [P(x0, y), P(x1, y)]
            d.line(pts, fill=(0, 255, 0), width=1)
            for c in st['caps']:
                d.rectangle([P(c[0], c[1]), P(c[0] + c[2], c[1] + c[3])], outline=(255, 0, 255))
            hk = st['lamp']['hook']
            if st['lamp']['mode'] == 'hang':
                cxm = hk[0] - T['lampW'] / 2 - 4
                d.rectangle([P(cxm - T['lampW'] / 2, hk[1] + 4), P(cxm + T['lampW'] / 2, hk[1] + 4 + T['lampH'])], outline=(255, 255, 0))
            else:
                d.rectangle([P(hk[0] - T['lampW'] / 2, hk[1] - T['lampH']), P(hk[0] + T['lampW'] / 2, hk[1])], outline=(255, 255, 0))
            f = st['flag']
            cell = T['flagH'] / 16
            d.rectangle([P(f[0] - 3.5 * cell, f[1] - T['flagH']), P(f[0] + 11.5 * cell, f[1])], outline=(0, 255, 255))
            ty = st['mid'][1]
            d.rectangle([P(T['tagX'] - T['tag'] / 2, ty - T['tag'] / 2), P(T['tagX'] + T['tag'] / 2, ty + T['tag'] / 2)], outline=(255, 128, 0))
            d.text(P(T['tagX'] - 6, ty - 8), str(st['n']), fill=(255, 128, 0))
            fx = st['fx']
            for k in ('c', 'lens', 'chimney', 'cairn', 'lantern'):
                if k in fx:
                    x, y = P(*fx[k])
                    d.ellipse([x - 4, y - 4, x + 4, y + 4], outline=(255, 0, 0), width=2)
            for wdw in fx.get('windows', []):
                d.rectangle([P(wdw[0], wdw[1]), P(wdw[0] + wdw[2], wdw[1] + wdw[3])], outline=(255, 0, 0))
        d.polygon([tuple(p) for p in T['pad']['poly']], outline=(255, 255, 255))
        sh = T['shadow']
        d.ellipse([sh['cx'] - sh['rx'], sh['cy'] - sh['ry'], sh['cx'] + sh['rx'], sh['cy'] + sh['ry']], outline=(80, 80, 255))
        return base.convert('RGB')

    tiles = [('trace', on_summit(tower, True)), ('ghost: none built', on_summit(state([]))),
             ('storey 1', on_summit(state([1]))), ('free: 1-4', on_summit(state([1, 2, 3, 4]))),
             ('out of order: 1,2,5,7,9', on_summit(state([1, 2, 5, 7, 9]))), ('all nine', on_summit(state(range(1, 10))))]
    tw, th = 384, 576
    sheet = Image.new('RGB', (tw * 3 + 40, th * 2 + 80 + 4 * 88 + 10), (24, 28, 34))
    d = ImageDraw.Draw(sheet)
    for i, (name, im) in enumerate(tiles):
        x, y = 10 + (i % 3) * (tw + 10), 10 + (i // 3) * (th + 30)
        sheet.paste(im.resize((tw, th), Image.LANCZOS), (x, y + 18))
        d.text((x, y), name, fill=(230, 230, 230))
    bg = Image.new('RGBA', (W, H), (255, 0, 255, 255))
    bg.alpha_composite(tower)
    dd = ImageDraw.Draw(bg)
    for st in T['storeys']:
        pts = []
        for x0, x1, y in st['top']:
            pts += [(x0, y), (x1, y)]
        dd.line(pts, fill=(0, 255, 0), width=1)
    y0 = th * 2 + 80
    for i, st in enumerate(sorted(T['storeys'], key=lambda q: -q['n'])[:-1]):
        yb = st['y1']
        x = 10 + (i % 2) * 590
        yy = y0 + (i // 2) * 88
        sheet.paste(bg.crop((230, yb - 40, 800, yb + 40)).convert('RGB'), (x, yy))
        d.text((x + 4, yy + 2), 'cut %d/%d' % (st['n'], st['n'] - 1), fill=(255, 255, 255))
    sheet.save(path)
    return path


# ── the entry point build.py calls ──────────────────────────────────────
def load_sources():
    import numpy as np
    from PIL import Image
    need_src()
    return (np.array(Image.open(SRC_TOWER).convert('RGBA')),
            np.array(Image.open(SRC_SUMMIT).convert('RGB')))


def run(ingest, do_trace, do_proof, toks):
    """--ingest / --trace / --proof, sharing one clean pass and one trace
    (the ghost is washed by the sky behind each row, so it needs the
    placement the trace measures)."""
    from PIL import Image
    raw, summit = load_sources()
    clean, stats = clean_alpha(raw)
    Image.fromarray(clean).save(CLEAN_PNG)
    T = trace(clean, summit)
    cov, over = coverage(T, clean)
    T['coverage'], T['overlap'], T['alpha'] = round(cov, 5), over, stats
    ghost_img = ghost(clean, sky_rows(summit, T['place']), hexrgb(toks['BLUEPRINT']))
    report = ['alpha: %d partly transparent pixels -> %d; bbox %r -> %r'
              % (stats['before']['partial'], stats['after']['partial'], stats['before']['bbox'], stats['after']['bbox']),
              'bands: %s; coverage %.3f%%, overlap %d px; smallest storey %d px (floor %d)'
              % (', '.join('%d:%d-%d' % (q['n'], q['y0'], q['y1']) for q in T['storeys']), 100 * cov, over,
                 min(q['h'] for q in T['storeys']), T['minStorey']),
              'pad: back %d, front %d, centre %.1f, front width %d; tower x%.4f (%s), top at %.1f%% of the plate'
              % (T['pad']['back'], T['pad']['front'], T['pad']['cx'], T['pad']['frontW'], T['place']['s'],
                 T['place']['by'], 100 * T['place']['top'] / H)]
    if ingest:
        sizes = {}
        tim, gim, sim = Image.fromarray(clean), Image.fromarray(ghost_img), Image.fromarray(summit)
        for key, im in (('lookout', tim), ('ghost', gim), ('lookoutSm', tim), ('summit', sim),
                        ('summit768', sim), ('summitSm', sim)):
            name, wd, q, aq = OUTS[key]
            _, sz = save_webp(im, name, wd, q, aq)
            sizes[name] = sz
        report.append('wrote BlockCamp/lookout/: ' + ', '.join('%s %.1f KB' % (k, v / 1024) for k, v in sizes.items()))
    if do_trace:
        T['outputs'] = {}
        for k, v in OUTS.items():
            f = os.path.join(OUT_DIR, v[0])
            if not os.path.exists(f):
                raise SystemExit('trace: %s is missing - run --ingest first' % os.path.relpath(f, REPO))
            T['outputs'][k] = {'file': 'BlockCamp/lookout/' + v[0], 'w': v[1], 'h': round(H * v[1] / W), 'sha1': sha1(f)}
        open(STOREYS_JSON, 'w', encoding='utf-8', newline='\n').write(json.dumps(T, indent=1, ensure_ascii=False) + '\n')
        report.append('wrote ' + os.path.relpath(STOREYS_JSON, REPO))
    if do_proof:
        report.append('proof: ' + os.path.relpath(proof(T, clean, ghost_img, summit, os.path.join(SRC_DIR, 'proof-trace.png')), REPO))
    return report


# ── --check (no PIL needed: storeys.json, the files and their hashes) ───
def art_data(T):
    """What camp-lookout.js carries: the trace without its bookkeeping."""
    keep = ('size', 'bbox', 'towerH', 'place', 'lip', 'shadow', 'tagX', 'tag', 'lampW', 'lampH', 'flagH',
            'eave', 'cradle', 'beacon', 'rail', 'roof')
    out = {k: T[k] for k in keep}
    out['pad'] = {k: T['pad'][k] for k in ('back', 'front', 'kerbBottom', 'cx')}
    out['storeys'] = [{k: s[k] for k in ('n', 'top', 'bot', 'y0', 'y1', 'h', 'mid', 'x0', 'x1', 'caps', 'lamp', 'flag', 'fx', 'dust', 'beamTop') if k in s}
                      for s in T['storeys']]
    out['outputs'] = {k: {'file': o['file'], 'v': o['sha1'][:8]} for k, o in T['outputs'].items()}
    out['v'] = hashlib.sha1(json.dumps(out, sort_keys=True).encode()).hexdigest()[:8]
    return out


def _inside(pt, bb, m=0):
    return bb[0] - m <= pt[0] <= bb[2] + m and bb[1] - m <= pt[1] <= bb[3] + m


def check_art(T, have_src=None):
    """design 9.7: the bands tile the tower (each column's cuts strictly in
    order, nothing between them, the trace's own pixel count 99.5%+ and no
    overlap), no storey under 6% of the tower, every anchor inside the
    tower's box (flags and lamps hang just outside it, so they get a margin)
    and inside its own storey's rows, no two lamps or tags overlapping, the
    tower's top at least 6% below the plate's; the plates and the pictures
    unchanged since the trace."""
    bad = []
    if have_src is None:
        have_src = os.path.exists(SRC_TOWER) and os.path.exists(SRC_SUMMIT)
    if have_src:
        for k, p in (('lookout', SRC_TOWER), ('summit', SRC_SUMMIT)):
            if sha1(p) != T['src'][k]:
                bad.append('incoming/lookout/%s changed since the trace (sha1 %s, traced %s): re-run --ingest --trace'
                           % (os.path.basename(p), sha1(p)[:10], T['src'][k][:10]))
    for k, o in sorted(T.get('outputs', {}).items()):
        f = os.path.join(REPO, o['file'])
        if not os.path.exists(f):
            bad.append('%s is missing (run --ingest)' % o['file'])
        elif sha1(f) != o['sha1']:
            bad.append('%s is not the picture the trace measured (re-run --ingest --trace)' % o['file'])
    sts = sorted(T['storeys'], key=lambda s: -s['n'])
    if [s['n'] for s in sts] != list(range(9, 0, -1)):
        bad.append('storeys are not 9..1: %r' % [s['n'] for s in sts])
        return bad
    bb = T['bbox']
    cols = range(bb[0], bb[2] + 1)

    def row(runs, x):
        return at(runs, x)
    if any(row(sts[0]['top'], x) != 0 for x in (0, W // 2, W - 1)) or any(row(sts[-1]['bot'], x) != H for x in (0, W // 2, W - 1)):
        bad.append('the bands do not run from the plate top (storey 9) to its foot (storey 1)')
    for a, b in zip(sts, sts[1:]):
        if a['bot'] != b['top']:
            bad.append('storey %d ends where storey %d does not begin: a gap or an overlap' % (a['n'], b['n']))
    for s in sts:
        thin = [x for x in cols if row(s['bot'], x) <= row(s['top'], x)]
        if thin:
            bad.append('storey %d has no rows at x=%d..%d (its cuts cross)' % (s['n'], thin[0], thin[-1]))
        if s['h'] < 0.06 * T['towerH']:
            bad.append('storey %d is %d px, under 6%% of the tower (%d px)' % (s['n'], s['h'], T['towerH']))
    if T.get('coverage', 0) < 0.995 or T.get('overlap', 1):
        bad.append('the bands cover %.2f%% of the tower with %s px in two bands (needs 99.5%%, none)'
                   % (100 * T.get('coverage', 0), T.get('overlap')))
    for s in sts:
        n, y0, y1 = s['n'], s['y0'], s['y1']
        pts = [('cap', (c[0] + c[2] / 2, c[1] + c[3] / 2), 0, 16) for c in s['caps']]
        fx = s['fx']
        for k in ('c', 'lens', 'chimney', 'cairn', 'lantern'):
            if k in fx:
                pts.append(('effect ' + k, fx[k], 0, 2))
        for w in fx.get('windows', []):
            pts.append(('window', (w[0] + w[2] / 2, w[1] + w[3] / 2), 0, 0))
        pts.append(('lamp hook', s['lamp']['hook'], 40, 2))
        pts.append(('flag foot', s['flag'], 80, 2))
        for what, p, margin, slack in pts:
            if not _inside(p, bb, margin):
                bad.append('storey %d: %s %r is outside the tower box %r' % (n, what, list(p), bb))
            elif not (y0 - slack <= p[1] <= y1 + slack):
                bad.append('storey %d: %s %r is not in its rows %d-%d' % (n, what, list(p), y0, y1))
        if not s['caps']:
            bad.append('storey %d: no trim caps found' % n)
    # lamps and tags, as the renderer lays them out in master px
    rects = []
    for s in sts:
        hk, lw, lh = s['lamp']['hook'], T['lampW'], T['lampH']
        c = lw / 3                      # a lantern cell; a gold crown adds one above
        if s['lamp']['mode'] == 'stand':
            r = (hk[0] - lw / 2, hk[1] - lh - c, hk[0] + lw / 2, hk[1])
        else:
            r = (hk[0] - lw - c, hk[1], hk[0] - c, hk[1] + c + lh)
        rects.append(('lamp %d' % s['n'], r))
        t = T['tag']
        rects.append(('tag %d' % s['n'], (T['tagX'] - t / 2, s['mid'][1] - t / 2, T['tagX'] + t / 2, s['mid'][1] + t / 2)))
    for i, (na, a) in enumerate(rects):
        for nb, b in rects[i + 1:]:
            if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                bad.append('%s overlaps %s' % (na, nb))
    if T['place']['top'] < MIN_TOP * H:
        bad.append('the tower top sits %.1f%% below the plate top (needs %d%%)' % (100 * T['place']['top'] / H, 100 * MIN_TOP))
    return bad
