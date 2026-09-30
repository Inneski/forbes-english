# -*- coding: utf-8 -*-
"""The paint for sea_charts.py: everything that makes a coded chart look like
an old engraved one, and none of the words.

Nothing here is decoration for its own sake. The terrain is the grammar where
it can be: the countable shore is planted in orchards, tree by tree, in rows
you could count; the uncountable shore is wheat and dune, stuff you can only
measure. Regularia's fields are a grid. The irregular islands each get their
own landmark (a bell tower, a castle keep, a windmill, a wreck on the reef).

Every glyph is kept off the words. terrain() is given the boxes the labels
will occupy and never plants inside them, so the painted chart stays readable
once the label layer goes on top of it.

    rings()    water lines drawn parallel to every coast, as engraved charts do
    hatch()    short strokes along the coast, pointing inland: the cliffs
    terrain()  orchards, wheat, hills, fields, scattered clear of the labels
"""
import html
import math
import random
import re

INK = '#3A2A1C'            # sepia: coasts, hatching, glyphs
RING_INK = '#3E7384'       # the water lines
TREE = '#6E7F45'
PAPER = '#EADCBB'          # the margin outside the ruled border
FRAME = 9                  # inset of the ruled border


# ─────────────────────────────────────────────────────────────────────
# geometry
# ─────────────────────────────────────────────────────────────────────

def inside(pts, x, y):
    """Ray casting: is (x, y) inside the polygon pts?"""
    hit = False
    j = len(pts) - 1
    for i, (xi, yi) in enumerate(pts):
        xj, yj = pts[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            hit = not hit
        j = i
    return hit


def coast_dist(pts, x, y):
    """Distance to the nearest visible coast vertex. The roughened coasts are
    dense enough that a vertex is never far from the true edge."""
    return min(math.hypot(px - x, py - y) for px, py in pts if -12 <= px <= 1012)


def text_box(x, y, text, size, anchor='middle', k=0.6, pad=5):
    """A generous box for a line of text whose baseline is at y."""
    n = len(html.unescape(re.sub(r'<[^>]+>', '', text)))
    w = n * size * k
    x0 = x - w / 2 if anchor == 'middle' else (x if anchor == 'start' else x - w)
    return (x0 - pad, y - size - pad, x0 + w + pad, y + pad * .7)


def place_boxes(items, size=11):
    """The boxes a harbour label and its dot will take up."""
    out = []
    for x, y, name in items:
        out.append(text_box(x, y - 8, name, size))
        out.append((x - 6, y - 6, x + 6, y + 6))
    return out


def _clear(box, avoid):
    a0, b0, a1, b1 = box
    return not any(a0 < c1 and c0 < a1 and b0 < d1 and d0 < b1 for c0, d0, c1, d1 in avoid)


# ─────────────────────────────────────────────────────────────────────
# the sheet: parchment, grain, a ruled border
# ─────────────────────────────────────────────────────────────────────

DEFS = '''<filter id="sc-relief" x="0" y="0" width="100%" height="100%">
      <feMorphology in="SourceAlpha" operator="erode" radius="2" result="e"/>
      <feGaussianBlur in="e" stdDeviation="6" result="b"/>
      <feComposite in="SourceAlpha" in2="b" operator="out" result="band"/>
      <feFlood flood-color="#3A2A1C" flood-opacity=".30"/>
      <feComposite in2="band" operator="in" result="shade"/>
      <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="shade"/></feMerge>
    </filter>
    <filter id="sc-blotch" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency=".007 .01" numOctaves="4" seed="11"/>
      <feColorMatrix type="matrix" values="0 0 0 0 .42  0 0 0 0 .30  0 0 0 0 .14  0 0 0 2.2 -.9"/>
    </filter>
    <filter id="sc-grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="5"/>
      <feColorMatrix type="matrix" values="0 0 0 0 .30  0 0 0 0 .22  0 0 0 0 .10  0 0 0 1.4 -.55"/>
    </filter>
    ''' + ('<clipPath id="sc-frame"><rect x="%d" y="%d" width="%d" height="%d"/></clipPath>'
           % (FRAME, FRAME, 1000 - 2 * FRAME, 660 - 2 * FRAME))


def sheet_open():
    """Parchment margin, then everything else clipped to the ruled border."""
    return ('<rect x="0" y="0" width="1000" height="660" fill="%s"/>\n  '
            '<g clip-path="url(#sc-frame)">' % PAPER)


def sheet_close():
    """Close the clip, age the whole sheet, then rule the border with a
    chequered degree band, as on an Admiralty chart."""
    out = ['</g>',
           '<rect x="0" y="0" width="1000" height="660" filter="url(#sc-blotch)" opacity=".30"/>',
           '<rect x="0" y="0" width="1000" height="660" filter="url(#sc-grain)" opacity=".22"/>']
    f, o = FRAME, 4
    band = []
    for x in range(f, 1000 - f, 25):
        if (x // 25) % 2:
            band.append('M %d %d h 25 v %d h -25 Z M %d %d h 25 v %d h -25 Z'
                        % (x, o, f - o, x, 660 - f, f - o))
    for y in range(f, 660 - f, 25):
        if (y // 25) % 2:
            band.append('M %d %d v 25 h %d v -25 Z M %d %d v 25 h %d v -25 Z'
                        % (o, y, f - o, 1000 - f, y, f - o))
    out.append('<path d="%s" fill="%s" opacity=".75"/>' % (' '.join(band), INK))
    out.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" stroke-width="1.5"/>'
               % (f, f, 1000 - 2 * f, 660 - 2 * f, INK))
    out.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" stroke-width=".9"/>'
               % (o, o, 1000 - 2 * o, 660 - 2 * o, INK))
    return '\n  '.join(out)


# ─────────────────────────────────────────────────────────────────────
# water
# ─────────────────────────────────────────────────────────────────────

def rings(coasts, dists=(7, 15, 25), uid='sc'):
    """Water lines parallel to every coast at once. Each ring is a white stroke
    a hair wider than a black stroke of the same path, used as a mask: that
    leaves exactly the line at distance d from the nearest shore, and where two
    coasts come close their rings merge the way real soundings do."""
    paths = ''.join('<path d="%s"/>' % c for c in coasts)
    out = []
    for i, d in enumerate(dists):
        mid = '%s-ring%d' % (uid, i)
        out.append('<mask id="%s" maskUnits="userSpaceOnUse" x="0" y="0" width="1000" height="660">'
                   '<g fill="none" stroke-linejoin="round" stroke="#fff" stroke-width="%.1f">%s</g>'
                   '<g fill="none" stroke-linejoin="round" stroke="#000" stroke-width="%.1f">%s</g>'
                   '</mask>' % (mid, 2 * d + 1.3, paths, 2 * d, paths))
        out.append('<rect x="0" y="0" width="1000" height="660" fill="%s" opacity="%.2f" mask="url(#%s)"/>'
                   % (RING_INK, .55 - .12 * i, mid))
    return '\n  '.join(out)


def swell(x, y, s=1.0):
    """A small engraved wave mark."""
    return ('<path d="M %.1f %.1f q %.1f %.1f %.1f 0 q %.1f %.1f %.1f 0 M %.1f %.1f q %.1f %.1f %.1f 0" '
            'fill="none" stroke="%s" stroke-width=".9" stroke-linecap="round" opacity=".55"/>'
            % (x, y, 4 * s, -4 * s, 8 * s, 4 * s, -4 * s, 8 * s,
               x + 5 * s, y + 5 * s, 3 * s, -3 * s, 6 * s, RING_INK))


# ─────────────────────────────────────────────────────────────────────
# land
# ─────────────────────────────────────────────────────────────────────

def hatch(pts, seed, step=3.1):
    """Short strokes from the coast inland, every few pixels: engraved cliffs.
    Each segment works out which side is land by testing a point just off it."""
    rng = random.Random(seed)
    out = []
    n = len(pts)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        if (a[0] < -8 and b[0] < -8) or (a[0] > 1008 and b[0] > 1008):
            continue
        dx, dy = b[0] - a[0], b[1] - a[1]
        seg = math.hypot(dx, dy)
        if seg < 1:
            continue
        nx, ny = -dy / seg, dx / seg
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        if not inside(pts, mx + nx * 2.5, my + ny * 2.5):
            nx, ny = -nx, -ny
        k = max(1, int(seg // step))
        for j in range(k):
            t = (j + rng.random() * .6) / k
            px, py = a[0] + dx * t, a[1] + dy * t
            if not (0 <= px <= 1000 and 0 <= py <= 660):
                continue
            ln = rng.uniform(2.5, 8)
            out.append('M%.1f %.1fl%.1f %.1f' % (px, py, nx * ln, ny * ln))
    return ('<path d="%s" stroke="%s" stroke-width=".7" stroke-linecap="round" opacity=".5" fill="none"/>'
            % (''.join(out), INK))


def tree(x, y, s=1.0, fill=TREE):
    return ('<path d="M%.1f %.1fv%.1f" stroke="%s" stroke-width=".8"/>'
            '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width=".7"/>'
            % (x, y - 1, 3.5 * s, INK, x, y - 3.4 * s, 3 * s, fill, INK))


def pine(x, y, s=1.0, fill='#5C6E3C'):
    return ('<path d="M%.1f %.1fl%.1f %.1fl%.1f %.1fz" fill="%s" stroke="%s" stroke-width=".7" '
            'stroke-linejoin="round"/>' % (x - 3.2 * s, y, 3.2 * s, -9 * s, 3.2 * s, 9 * s, fill, INK))


def mountain(x, y, s=1.0, fill='#E9DDC0'):
    """A peak with its eastern face in shadow and three hatch strokes."""
    l, t, r = (x - 9 * s, y), (x - s, y - 11 * s), (x + 9 * s, y)
    return ('<path d="M%.1f %.1fL%.1f %.1fL%.1f %.1fZ" fill="%s" fill-opacity=".55" stroke="%s" '
            'stroke-width=".8" stroke-linejoin="round"/>'
            '<path d="M%.1f %.1fL%.1f %.1fL%.1f %.1fZ" fill="%s" opacity=".22"/>'
            '<path d="M%.1f %.1fl%.1f %.1fM%.1f %.1fl%.1f %.1fM%.1f %.1fl%.1f %.1f" stroke="%s" '
            'stroke-width=".6" opacity=".6"/>'
            % (l[0], l[1], t[0], t[1], r[0], r[1], fill, INK,
               t[0], t[1], r[0], r[1], x + 1.5 * s, y, INK,
               x + 1 * s, y - 7 * s, 2.5 * s, 3 * s, x + 3 * s, y - 4.5 * s, 2.5 * s, 3 * s,
               x + 5 * s, y - 2 * s, 2 * s, 2 * s, INK))


def house(x, y, s=1.0):
    return ('<path d="M%.1f %.1fh%.1fv%.1fh%.1fz" fill="#F4EAD5" stroke="%s" stroke-width=".7"/>'
            '<path d="M%.1f %.1fl%.1f %.1fl%.1f %.1fz" fill="#9C4A30" stroke="%s" stroke-width=".7" '
            'stroke-linejoin="round"/>'
            % (x - 3 * s, y, 6 * s, -4 * s, -6 * s, INK,
               x - 4 * s, y - 4 * s, 4 * s, -3.5 * s, 4 * s, 3.5 * s, INK))


def tuft(x, y, s=1.0):
    """A little stand of wheat: the uncountable shore is stuff, not things."""
    return ('<path d="M%.1f %.1fv%.1fM%.1f %.1fv%.1fM%.1f %.1fv%.1fM%.1f %.1fv%.1f" stroke="#8C6A1C" '
            'stroke-width=".8" stroke-linecap="round" opacity=".75"/>'
            % (x - 3 * s, y, -4 * s, x - 1 * s, y + 1, -5 * s, x + 1 * s, y, -4.5 * s,
               x + 3 * s, y + 1, -4 * s))


def dune(x, y, s=1.0):
    return ('<path d="M%.1f %.1fq%.1f %.1f %.1f 0M%.1f %.1fq%.1f %.1f %.1f 0" fill="none" stroke="%s" '
            'stroke-width=".7" opacity=".55"/>'
            % (x - 8 * s, y, 7 * s, -6 * s, 14 * s, x - 4 * s, y + 3 * s, 5 * s, -4 * s, 10 * s, INK))


def rock(x, y, r, fill='#9A8C7A'):
    return ('<path d="M%.1f %.1fL%.1f %.1fL%.1f %.1fL%.1f %.1fZ" fill="%s" stroke="%s" '
            'stroke-width="1" stroke-linejoin="round"/><path d="M%.1f %.1fL%.1f %.1fL%.1f %.1fZ" '
            'fill="%s" opacity=".25"/>'
            % (x - r, y + r * .6, x - r * .4, y - r * .8, x + r * .5, y - r * .6, x + r, y + r * .6,
               fill, INK, x + r * .5, y - r * .6, x + r, y + r * .6, x, y + r * .6, INK))


# glyph -> (draw, half-width, height above the anchor)
KINDS = {
    'tree': (tree, 4, 8), 'pine': (pine, 4, 10), 'mountain': (mountain, 10, 12),
    'house': (house, 5, 9), 'tuft': (tuft, 4, 6), 'dune': (dune, 9, 5),
}

# terrain -> how each grid cell is filled: [(glyph, chance)], regular rows?
TERRAIN = {
    # countable: orchards in exact rows, the odd farmhouse, every one separate
    'orchard': ([('tree', .82), ('house', .06)], True),
    # uncountable: wheat and sand, which you measure and cannot count
    'wheat': ([('tuft', .5), ('dune', .07), ('tree', .02)], False),
    'hills': ([('mountain', .26), ('tree', .22), ('pine', .12)], False),
    # Regularia is tidy: sparse trees and farms on the grid it already has
    'fields': ([('tree', .16), ('house', .08)], True),
}


def orchards(pts, avoid, seed, cell=50, margin=12):
    """The countable shore: square orchards of exactly nine trees, set apart
    with a farmhouse here and there. You could count every one."""
    rng = random.Random(seed)
    vis = [p for p in pts if -12 <= p[0] <= 1012]
    x0, x1 = 14, min(986, max(p[0] for p in vis))
    y0, y1 = max(14, min(p[1] for p in pts)), min(646, max(p[1] for p in pts))
    out = []
    y = y0 + 6
    while y < y1:
        x = x0 + 6
        while x < x1:
            roll = rng.random()
            if roll < .62:
                box = (x - 2, y - 8, x + 22, y + 18)
                corners = [(box[0], box[1]), (box[2], box[1]), (box[0], box[3]), (box[2], box[3])]
                if (all(inside(pts, cx, cy) and coast_dist(pts, cx, cy) > margin for cx, cy in corners)
                        and _clear(box, avoid)):
                    out.extend(tree(x + i * 9, y + j * 9 + 4, .8) for j in range(3) for i in range(3))
            elif roll < .74:
                box = (x + 4, y, x + 16, y + 12)
                if (inside(pts, x + 10, y + 10) and coast_dist(pts, x + 10, y + 10) > margin
                        and _clear(box, avoid)):
                    out.append(house(x + 10, y + 10))
            x += cell
        y += cell * .82
    return ''.join(out)


def terrain(pts, kind, avoid, seed, spacing=17, margin=12):
    """Fill a landmass with its terrain, clear of the labels and the coast."""
    if kind == 'orchard':
        return orchards(pts, avoid, seed)
    rng = random.Random(seed)
    table, rows = TERRAIN[kind]
    vis = [p for p in pts if -12 <= p[0] <= 1012]
    x0, x1 = max(14, min(p[0] for p in vis) - 20), min(986, max(p[0] for p in vis))
    y0, y1 = max(14, min(p[1] for p in pts)), min(646, max(p[1] for p in pts))
    out = []
    y, row = y0 + spacing / 2, 0
    while y < y1:
        x = x0 + (0 if rows or row % 2 == 0 else spacing / 2)
        while x < x1:
            gx = x if rows else x + rng.uniform(-5, 5)
            gy = y if rows else y + rng.uniform(-4, 4)
            roll, acc, pick = rng.random(), 0, None
            for glyph, chance in table:
                acc += chance
                if roll < acc:
                    pick = glyph
                    break
            if pick:
                draw, hw, h = KINDS[pick]
                box = (gx - hw, gy - h, gx + hw, gy + 2)
                if (inside(pts, gx, gy) and coast_dist(pts, gx, gy) > margin
                        and _clear(box, avoid)):
                    s = 1.0 if rows else rng.uniform(.85, 1.15)
                    out.append(draw(gx, gy, s))
            x += spacing
        y += spacing * .78
        row += 1
    return ''.join(out)


# ─────────────────────────────────────────────────────────────────────
# landmarks: each one is placed by hand, and its box is kept clear
# ─────────────────────────────────────────────────────────────────────

def lighthouse(x, y):
    return ('<path d="M%.1f %.1fL%.1f %.1fL%.1f %.1fL%.1f %.1fZ" fill="#F4EAD5" stroke="%s" stroke-width=".8"/>'
            '<path d="M%.1f %.1fh%.1fM%.1f %.1fh%.1f" stroke="#A8412E" stroke-width="2.2"/>'
            '<rect x="%.1f" y="%.1f" width="5" height="4" fill="#E8C35A" stroke="%s" stroke-width=".7"/>'
            '<path d="M%.1f %.1fl3.5 -3l3.5 3z" fill="%s"/>'
            % (x - 4, y, x - 2.5, y - 16, x + 2.5, y - 16, x + 4, y, INK,
               x - 3.4, y - 5, 6.8, x - 2.9, y - 11, 5.8, x - 2.5, y - 20, INK, x - 3.5, y - 20, INK))


def bell_tower(x, y):
    return ('<rect x="%.1f" y="%.1f" width="8" height="14" fill="#F1E3C6" stroke="%s" stroke-width=".8"/>'
            '<path d="M%.1f %.1fl5 -8l5 8z" fill="#8C3F2B" stroke="%s" stroke-width=".8" stroke-linejoin="round"/>'
            '<path d="M%.1f %.1fa2 2.4 0 0 1 4 0v3h-4z" fill="#C79A3A" stroke="%s" stroke-width=".6"/>'
            % (x - 4, y - 14, INK, x - 5, y - 14, INK, x - 2, y - 7, INK))


def windmill(x, y):
    return ('<path d="M%.1f %.1fL%.1f %.1fL%.1f %.1fL%.1f %.1fZ" fill="#F1E3C6" stroke="%s" stroke-width=".8"/>'
            '<path d="M%.1f %.1fl-7 -7M%.1f %.1fl7 -7M%.1f %.1fl-7 7M%.1f %.1fl7 7" stroke="%s" '
            'stroke-width="2.2" stroke-linecap="round" opacity=".85"/>'
            % (x - 4, y, x - 2.5, y - 12, x + 2.5, y - 12, x + 4, y, INK,
               x, y - 12, x, y - 12, x, y - 12, x, y - 12, INK))


def keep(x, y):
    return ('<path d="M%.1f %.1fv-14h2.5v2h2v-2h3v2h2v-2h2.5v14z" fill="#E6D8BC" stroke="%s" '
            'stroke-width=".8" stroke-linejoin="round"/><path d="M%.1f %.1fv-4a1.5 1.5 0 0 1 3 0v4z" fill="%s"/>'
            % (x - 6, y, INK, x - 1.5, y, INK))


def wreck(x, y):
    return ('<path d="M%.1f %.1fq8 5 18 -3l-2 -4q-8 5 -15 1z" fill="#6B4A2E" stroke="%s" stroke-width=".8"/>'
            '<path d="M%.1f %.1fl4 -13M%.1f %.1fl-2 -8" stroke="%s" stroke-width="1.3"/>'
            % (x - 9, y, INK, x - 1, y - 2, x + 5, y - 4, INK))


def crates(x, y):
    out = []
    for dx, dy in ((0, 0), (6, 0), (3, -5)):
        out.append('<rect x="%.1f" y="%.1f" width="5.5" height="5" fill="#B98B55" stroke="%s" stroke-width=".7"/>'
                   % (x + dx - 6, y + dy - 5, INK))
    return ''.join(out)


def mill(x, y):
    return windmill(x, y)


LANDMARKS = {'lighthouse': (lighthouse, 5, 22), 'bell': (bell_tower, 6, 23), 'windmill': (windmill, 9, 20),
             'keep': (keep, 7, 15), 'wreck': (wreck, 10, 15), 'crates': (crates, 7, 11), 'mill': (mill, 9, 20)}


def landmark_boxes(marks):
    return [(x - LANDMARKS[k][1] - 3, y - LANDMARKS[k][2] - 3, x + LANDMARKS[k][1] + 3, y + 3)
            for k, x, y in marks]


def landmarks(marks):
    return ''.join(LANDMARKS[k][0](x, y) for k, x, y in marks)


# ─────────────────────────────────────────────────────────────────────
# the instruments: compass rose, ship, serpent
# ─────────────────────────────────────────────────────────────────────

def compass_rose(cx, cy, r=36):
    """A sixteen-point rose, each point split into a lit and a shaded half."""
    out = ['<circle cx="%d" cy="%d" r="%d" fill="#F6EEDC" opacity=".8"/>' % (cx, cy, r + 4),
           '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="1"/>' % (cx, cy, r + 4, INK),
           '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width=".6"/>' % (cx, cy, r, INK)]
    ticks = []
    for k in range(32):
        a = k * math.pi / 16
        r0 = r if k % 4 else r - 3
        ticks.append('M%.1f %.1fL%.1f %.1f' % (cx + math.sin(a) * r0, cy - math.cos(a) * r0,
                                             cx + math.sin(a) * (r + 4), cy - math.cos(a) * (r + 4)))
    out.append('<path d="%s" stroke="%s" stroke-width=".6"/>' % (''.join(ticks), INK))
    for count, length, width, dark, light in ((8, r * .5, 2.6, '#6E7F86', '#F4EAD5'),
                                              (4, r * .72, 4.2, '#2B4A57', '#F4EAD5'),
                                              (4, r * .98, 5.6, '#2B4A57', '#E3B26A')):
        offset = math.pi / 8 if count == 8 else (math.pi / 4 if length < r * .8 else 0)
        step = 2 * math.pi / count
        for k in range(count):
            a = offset + k * step
            tip = (cx + math.sin(a) * length, cy - math.cos(a) * length)
            left = (cx + math.sin(a - math.pi / 2) * width, cy - math.cos(a - math.pi / 2) * width)
            right = (cx + math.sin(a + math.pi / 2) * width, cy - math.cos(a + math.pi / 2) * width)
            for side, fill in ((left, dark), (right, light)):
                out.append('<path d="M%d %dL%.1f %.1fL%.1f %.1fZ" fill="%s" stroke="%s" stroke-width=".6" '
                           'stroke-linejoin="round"/>' % (cx, cy, tip[0], tip[1], side[0], side[1], fill, INK))
    out.append('<circle cx="%d" cy="%d" r="2.4" fill="#E3B26A" stroke="%s" stroke-width=".6"/>' % (cx, cy, INK))
    # the fleur-de-lis over north
    fx, fy = cx, cy - r - 6
    out.append('<path d="M%.1f %.1fc-1.6 -3 -1 -6 0 -8c1 2 1.6 5 0 8zM%.1f %.1fc-3 0 -5 -2 -4.5 -4.5c1.5 1 3 2 4.5 4.5z'
               'M%.1f %.1fc3 0 5 -2 4.5 -4.5c-1.5 1 -3 2 -4.5 4.5z" fill="%s"/>'
               % (fx, fy, fx, fy, fx, fy, INK))
    return '<g class="compass">%s</g>' % ''.join(out)


def galleon(x, y, s=1.0):
    """A three-masted ship; (x, y) is the top of the mainmast."""
    body = ('<path d="M-34 40C-30 50 -20 54 0 54L22 54C32 52 38 44 40 36L-34 40Z" fill="#6B4A2E" stroke="%(i)s" stroke-width="1.1"/>'
            '<path d="M-34 40L-37 29L-22 29L-22 40Z" fill="#7C5836" stroke="%(i)s" stroke-width="1"/>'
            '<path d="M-31 46L36 42" stroke="#E3B26A" stroke-width="1.1"/>'
            '<path d="M-14 40V4M6 40V-2M24 38V12M38 37L54 28" stroke="%(i)s" stroke-width="1.4"/>'
            '<path d="M-24 10Q-14 14 -4 10L-5 30Q-14 33 -23 30Z" fill="#F4EAD5" stroke="%(i)s" stroke-width=".9"/>'
            '<path d="M-5 4Q6 8 17 4L16 31Q6 34 -4 31Z" fill="#F4EAD5" stroke="%(i)s" stroke-width=".9"/>'
            '<path d="M17 16Q24 19 31 16L30 32Q24 34 18 32Z" fill="#F4EAD5" stroke="%(i)s" stroke-width=".9"/>'
            '<path d="M39 35L52 29L40 26Z" fill="#F4EAD5" stroke="%(i)s" stroke-width=".8"/>'
            '<path d="M6 -2L15 1L6 4Z" fill="#A8412E"/>'
            '<path d="M-40 56q5 -3 10 0q5 3 10 0q5 -3 10 0q5 3 10 0q5 -3 10 0q5 3 10 0q5 -3 10 0q5 3 10 0" '
            'fill="none" stroke="%(r)s" stroke-width="1" opacity=".7"/>') % {'i': INK, 'r': RING_INK}
    return '<g class="ship" transform="translate(%s %s) scale(%s)">%s</g>' % (x, y, s, body)


def serpent(x, y, s=1.0):
    """Here be nouns."""
    body = ('<path d="M0 0q6 -14 12 0M16 0q5 -11 10 0M30 0q4 -8 8 0" fill="none" stroke="#3E6B55" '
            'stroke-width="3.2" stroke-linecap="round"/>'
            '<path d="M-2 0q-2 -12 6 -14q6 -1 7 3q-5 -2 -8 1q-3 3 -1 10" fill="#5B8A6E" stroke="%s" '
            'stroke-width=".8"/><circle cx="4" cy="-11" r=".9" fill="%s"/>'
            '<path d="M-6 3q22 -3 48 0" fill="none" stroke="%s" stroke-width=".9" opacity=".6"/>'
            % (INK, INK, RING_INK))
    return '<g class="serpent" transform="translate(%s %s) scale(%s)">%s</g>' % (x, y, s, body)
