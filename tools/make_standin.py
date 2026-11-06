# -*- coding: utf-8 -*-
"""Make house style 2 stand-in pictures, and record what they stand in for.

    py tools/make_standin.py <folder> <slot> <motif> "<brief>" [--scheme warm] [--deck x.html]
    py tools/make_standin.py --sheet out.png [--scheme warm]   # every motif, to check by eye

Builders call ensure() instead, with every slot the deck needs; it renders
only what is missing and rewrites <folder>/standins.json, which is what
tools/standins.py reads to produce the shopping list.

A stand-in is <folder>/standin-<slot>.png: a transparent 1200x1200 cut-out,
which house style 2 stands on the paper beside the text (data-art="cutout").
The hero slot also gets standin-hero.jpg, a 2400x1350 card for the library
and for extract-palette.py --paper.

Replacing one: drop the real plate in as <folder>/<slot>.jpg (or a cut-out
<slot>.png) and re-run the builder. deck.plate() prefers it, the stand-in
stops being referenced, and tools/standins.py drops it from the list. Do NOT
delete the standin files by hand while a page still names them.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import standin_motifs as SM  # noqa: E402

ROOT = os.path.dirname(HERE)

_NODE = r'''
const { chromium } = require(process.argv[2]);
const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1200 } });
  for (const j of jobs) {
    await p.setViewportSize({ width: j.w, height: j.h });
    await p.setContent('<html><body style="margin:0;background:' + (j.bg || 'transparent') +
      '">' + j.html + '</body></html>');
    await p.screenshot({ path: j.out, omitBackground: !j.bg, type: j.out.endsWith('.jpg') ? 'jpeg' : 'png',
      ...(j.out.endsWith('.jpg') ? { quality: 88 } : {}) });
  }
  await b.close();
})();
'''


def _render(jobs):
    if not jobs:
        return
    pw = os.path.join(ROOT, 'node_modules', 'playwright').replace('\\', '/')
    with tempfile.TemporaryDirectory() as td:
        js = os.path.join(td, 'r.js')
        open(js, 'w', encoding='utf-8').write(_NODE)
        jf = os.path.join(td, 'jobs.json')
        json.dump(jobs, open(jf, 'w', encoding='utf-8'))
        subprocess.run(['node', js, pw, jf], check=True)


def _job_png(folder, slot, motif, scheme, blob):
    return dict(w=1200, h=1200, out=os.path.abspath(os.path.join(folder, 'standin-%s.png' % slot)),
                html=SM.svg(motif, scheme, blob, size=1200))


def _job_card(folder, motif, scheme):
    paper = SM.SCHEMES[scheme]['paper']
    fig = SM.svg(motif, scheme, 0, size=1250)
    html = ('<div style="width:2400px;height:1350px;position:relative;background:%s">'
            '<div style="position:absolute;left:1060px;top:50px">%s</div></div>' % (paper, fig))
    return dict(w=2400, h=1350, bg=paper,
                out=os.path.abspath(os.path.join(folder, 'standin-hero.jpg')), html=html)


def ensure(folder, slots, scheme='warm', deck=None, force=False):
    """slots: {slot: (motif, brief)}. Renders what is missing; records all.

    The brief is the shopping-list line for the REAL picture: a subject
    written as an idea, the way the Midjourney briefs are (see
    docs/ARTWORK-revamp-shopping-list.md "The style, stated once")."""
    os.makedirs(folder, exist_ok=True)
    side = os.path.join(folder, 'standins.json')
    rec = json.load(open(side, encoding='utf-8')) if os.path.exists(side) else {}
    jobs = []
    for n, (slot, (motif, brief)) in enumerate(slots.items()):
        assert motif in SM.M, 'unknown motif %r (have: %s)' % (motif, ', '.join(sorted(SM.M)))
        png = os.path.join(folder, 'standin-%s.png' % slot)
        old = rec.get(slot, {})
        if force or not os.path.exists(png) or old.get('motif') != motif or old.get('scheme') != scheme:
            jobs.append(_job_png(folder, slot, motif, scheme, n))
            if slot == 'hero':
                jobs.append(_job_card(folder, motif, scheme))
        rec[slot] = {'motif': motif, 'scheme': scheme, 'brief': brief,
                     'deck': deck or old.get('deck')}
    _render(jobs)
    json.dump(rec, open(side, 'w', encoding='utf-8', newline='\n'), indent=1, ensure_ascii=False)
    return rec


def sheet(out, scheme='warm'):
    names = sorted(SM.M)
    cells = ''.join('<div style="display:inline-block;width:300px;height:330px;text-align:center;'
                    'font:14px sans-serif">%s<br>%s</div>' % (SM.svg(m, scheme, i, size=300), m)
                    for i, m in enumerate(names))
    w = 300 * 6
    h = 330 * ((len(names) + 5) // 6)
    _render([dict(w=w, h=h, bg='#ffffff', out=os.path.abspath(out),
                  html='<div style="width:%dpx">%s</div>' % (w, cells))])


if __name__ == '__main__':
    a = sys.argv[1:]
    scheme = 'warm'
    if '--scheme' in a:
        scheme = a[a.index('--scheme') + 1]
        del a[a.index('--scheme'):a.index('--scheme') + 2]
    deck = None
    if '--deck' in a:
        deck = a[a.index('--deck') + 1]
        del a[a.index('--deck'):a.index('--deck') + 2]
    if a and a[0] == '--sheet':
        sheet(a[1], scheme)
    elif len(a) == 4:
        ensure(a[0], {a[1]: (a[2], a[3])}, scheme, deck)
    else:
        sys.exit(__doc__)
