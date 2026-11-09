# -*- coding: utf-8 -*-
"""The label layer for a painted sea chart: the shared parts of
regularia_map.py and countania_map.py, for the charts after them.

A chart module loads its measurements (sea_measure.py's JSON), lists its
harbours as (dot, three readings) and its captions, and calls svg(). The
three readings sit on one <text> as data-place / data-verb / data-past and
the page script (sea_lesson.NAMES_JS) swaps between them; the attribute
names are the first chart's, kept so one script serves the series.
"""
import json, os
from regularia_map import ratio, mix, ink_for, _poly_path as poly_path, _rect as rect_path

HERE = os.path.dirname(os.path.abspath(__file__))
SERIF = 'Fraunces,Georgia,serif'


def load(name):
    return json.load(open(os.path.join(HERE, name), encoding='utf-8'))


def shape_at(data, x, y):
    hits = [s for s in data['shapes']
            if s['bbox'][0] <= x <= s['bbox'][2] and s['bbox'][1] <= y <= s['bbox'][3]]
    if not hits:
        raise SystemExit('sea_overlay: no landmass measured at (%d, %d)' % (x, y))
    return min(hits, key=lambda s: s['area'])


def circle_path(x, y, r):
    return 'M %d %d a %d %d 0 1 0 %d 0 a %d %d 0 1 0 %d 0 Z' % (x - r, y, r, r, 2 * r, r, r, -2 * r)


def name(x, y, readings, ink, paint, size=19, anchor='middle', dx=0, dy=-14, fit=True, weight=600,
         halo=.3, cls='place-name'):
    """One harbour's words. readings = (first, second, third), each shown by
    one of the chart's three modes. fit: a long reading is set smaller."""
    a, b, c = readings
    return ('<text class="%s" x="%d" y="%d" text-anchor="%s" font-family="Inter,sans-serif" '
            'font-size="%s" font-weight="%s" fill="%s" stroke="%s" stroke-width="4" stroke-linejoin="round" '
            'paint-order="stroke" data-size="%s"%s data-place="%s" data-verb="%s" data-past="%s">%s</text>'
            % (cls, x + dx, y + dy, anchor, size, weight, ink, mix(paint, '#FFFFFF', halo) if halo >= 0 else mix(paint, '#000000', -halo),
               size, ' data-fit="1"' if fit else '', a, b, c, a))


def cap(x, y, text, ink, size=16, anchor='middle', face='Inter,sans-serif', weight=700, spacing='.08em', style='',
        halo=None):
    """A fixed caption. halo: a colour to outline it with, for a caption
    that sits on busy paint (the register summit)."""
    ring = (' stroke="%s" stroke-width="4" stroke-linejoin="round" paint-order="stroke"' % halo) if halo else ''
    return ('<text x="%d" y="%d" text-anchor="%s" font-family="%s" font-size="%s" font-weight="%s" '
            'letter-spacing="%s" fill="%s"%s%s>%s</text>'
            % (x, y, anchor, face, size, weight, spacing, ink, (' font-style="%s"' % style) if style else '', ring, text))


def hotspot(uid, key, d, aria):
    return ('<path id="%s-%s" class="land" tabindex="0" role="button" aria-label="%s" '
            'style="cursor:pointer" d="%s" fill="transparent" stroke="transparent" stroke-width="14"/>'
            % (uid, key, aria, d))


def svg(w, h, spots, captions, names):
    return '''<svg class="sail-chart sail-chart-overlay" viewBox="0 0 %d %d">
        %s
        <g class="chart-captions">
        %s
        </g>
        <g class="place-layer">
        %s
        </g>
      </svg>''' % (w, h, '\n        '.join(spots), '\n        '.join(captions), '\n        '.join(names))
