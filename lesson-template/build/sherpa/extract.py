# -*- coding: utf-8 -*-
"""Inventory the 26 Sherpa Tensing scrolling pages into JSON.

The shipped HTML was the only complete record of the family's content: the
thirteen clone-and-patch builders each held a slice of it, four camps had no
builder at all, and the route-timeline sections of camps one and two were
patched in by a post-processor. Before the family could be rebuilt as decks,
every explanation, example, table, diagram and question had to be lifted out
of the pages into one shape that a single builder can read (HOUSE-STYLE §10,
step 1: "This content is the asset; the markup is not").

Run once against the scrolling pages; the JSON in `content/` is the source
from then on. Re-running it against the decks would find nothing — the
markup it reads no longer exists there.

    python3 lesson-template/build/sherpa/extract.py          # all 26
    python3 lesson-template/build/sherpa/extract.py camp-03  # one
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content')

# slug -> shipped file. The slug is what the deck builder and the artwork
# folder use; the filename is the live URL and never changes (§10 step 8).
PAGES = {
    'camp-01': 'sherpa-tensing-camp-one-present-continuous.html',
    'camp-02': 'sherpa-tensing-camp-two-present-simple.html',
    'camp-03': 'sherpa-tensing-camp-three-past-simple.html',
    'camp-04': 'sherpa-tensing-camp-four-present-perfect.html',
    'camp-05': 'sherpa-tensing-camp-five-going-to.html',
    'camp-06': 'sherpa-tensing-camp-six-past-continuous.html',
    'camp-07': 'sherpa-tensing-camp-seven-future-simple.html',
    'camp-08': 'sherpa-tensing-camp-eight-present-perfect-continuous.html',
    'camp-09': 'sherpa-tensing-camp-nine-future-continuous.html',
    'camp-10': 'sherpa-tensing-camp-ten-past-perfect.html',
    'camp-11': 'sherpa-tensing-camp-eleven-past-perfect-continuous.html',
    'camp-12': 'sherpa-tensing-camp-twelve-future-perfect.html',
    'camp-13': 'sherpa-tensing-camp-thirteen-future-perfect-continuous.html',
    'descent-01': 'sherpa-tensing-descent-one-present-continuous-passive.html',
    'descent-02': 'sherpa-tensing-descent-two-present-simple-passive.html',
    'descent-03': 'sherpa-tensing-descent-three-past-simple-passive.html',
    'descent-04': 'sherpa-tensing-descent-four-present-perfect-passive.html',
    'descent-07': 'sherpa-tensing-descent-seven-future-simple-passive.html',
    'descent-08': 'sherpa-tensing-descent-eight-past-continuous-passive.html',
    'descent-09': 'sherpa-tensing-descent-nine-going-to-passive.html',
    'descent-10': 'sherpa-tensing-descent-ten-past-perfect-passive.html',
    'descent-12': 'sherpa-tensing-descent-twelve-future-perfect-passive.html',
    'cloud-used-to': 'sherpa-tensing-cloud-used-to.html',
    'cloud-be-used-to': 'sherpa-tensing-cloud-be-used-to.html',
    'cloud-causative': 'sherpa-tensing-cloud-causative.html',
}


def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()


def inner(s):
    """Collapse the generated indentation without touching the words."""
    return re.sub(r'\s+', ' ', s).strip()


def between(s, start_pat, end_pat, flags=re.S):
    m = re.search(start_pat, s, flags)
    if not m:
        return None
    e = re.search(end_pat, s[m.end():], flags)
    return s[m.end():m.end() + e.start()] if e else s[m.end():]


# ── JS data ────────────────────────────────────────────────────────────
def js_array_of_strings(body):
    """A JS array literal of double-quoted strings -> list."""
    body = body.strip()
    try:
        return json.loads('[' + body.rstrip(',') + ']') if not body.startswith('[') else json.loads(body)
    except json.JSONDecodeError:
        out = []
        for m in re.finditer(r'"((?:[^"\\]|\\.)*)"', body):
            out.append(json.loads('"' + m.group(1) + '"'))
        return out


def js_questions(s):
    m = re.search(r'\nvar questions = \[(.*?)\n\];', s, re.S)
    if not m:
        return []
    body = m.group(1)
    body = re.sub(r'(\n\s*)(prompt|hint|correct|options|explain)\s*:', r'\1"\2":', body)
    body = re.sub(r',(\s*[}\]])', r'\1', body)
    return json.loads('[' + body + ']')


def js_lists(s):
    """var xExamples = [...] and renderList("panel-x-list", xExamples)."""
    lists = {}
    for m in re.finditer(r'\nvar (\w+) = \[\n(.*?)\n\];', s, re.S):
        if m.group(1) == 'questions':
            continue
        lists[m.group(1)] = js_array_of_strings(m.group(2))
    panels = {}
    for m in re.finditer(r'renderList\("([^"]+)",\s*(\w+)\)', s):
        panels[m.group(1)] = lists.get(m.group(2), [])
    return panels


def js_results_messages(s):
    m = re.search(r'if \(score === questions\.length\) msg = "((?:[^"\\]|\\.)*)";\s*'
                  r'else if \(score >= questions\.length - 2\) msg = "((?:[^"\\]|\\.)*)";\s*'
                  r'else msg = "((?:[^"\\]|\\.)*)";', s)
    if not m:
        return None
    return [json.loads('"%s"' % g) for g in m.groups()]


def js_i18n(s):
    """Camps one and two carry a full I18N object; lift every language."""
    i = s.find('\nvar I18N = {')
    if i < 0:
        return None
    j = s.find('\n};', i)
    block = s[i:j]
    out = {}
    for lm in re.finditer(r'\n  ([a-z]{2}): \{', block):
        lang = lm.group(1)
        start = lm.end()
        end = block.find('\n  }', start)
        body = block[start:end]
        d = {}
        for km in re.finditer(r'\n    ([A-Za-z0-9_]+): "((?:[^"\\]|\\.)*)"', body):
            d[km.group(1)] = json.loads('"' + km.group(2) + '"')
        out[lang] = d
    return out


# ── HTML pieces ────────────────────────────────────────────────────────
CARD = re.compile(
    r'<div class="rule-card">\s*<h3[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>'
    r'(?:\s*<div class="ex"([^>]*)>(.*?)</div>)?\s*</div>', re.S)


def cards(block):
    out = []
    for h, p, exattrs, ex in CARD.findall(block):
        tr = re.search(r'data-tr="(\d+)"', exattrs or '')
        out.append(dict(head=inner(h), body=inner(p),
                        ex=inner(ex) if ex else None,
                        tr=int(tr.group(1)) if tr else None))
    return out


def table(block):
    head = [inner(x) for x in re.findall(r'<th(?:\s[^>]*)?>(.*?)</th>', block, re.S)]
    rows = []
    for tr in re.findall(r'<tr(?:\s[^>]*)?>(.*?)</tr>', re.search(r'<tbody>(.*?)</tbody>', block, re.S).group(1), re.S):
        rows.append([inner(x) for x in re.findall(r'<td(?:\s[^>]*)?>(.*?)</td>', tr, re.S)])
    return dict(head=head, rows=rows)


def charts(block):
    out = []
    for cw in re.findall(r'<div class="chart-wrap"[^>]*>(.*?)\n      </div>', block, re.S):
        h = re.search(r'<h3[^>]*>(.*?)</h3>', cw, re.S)
        note = re.search(r'<p class="chart-note"[^>]*>(.*?)</p>', cw, re.S)
        ex = re.search(r'<p class="example"[^>]*>(.*?)</p>', cw, re.S)
        t = table(cw) if '<table' in cw else None
        out.append(dict(head=inner(h.group(1)) if h else None,
                        note=inner(note.group(1)) if note else None,
                        table=t, example=inner(ex.group(1)) if ex else None))
    return out


def signal_boxes(block):
    out = []
    for sb in re.findall(r'<div class="signal-box">(.*?)</ul>\s*</div>', block, re.S):
        h = re.search(r'<h3[^>]*>(.*?)</h3>', sb, re.S)
        items = [inner(x) for x in re.findall(r'<li[^>]*>(.*?)</li>', sb, re.S)]
        out.append(dict(head=inner(h.group(1)), items=items))
    return out


def descent_panels_from_builders():
    """The eight passive_kit descents shipped with EMPTY interactive panels.

    `passive_kit.build()` writes `var exA = [\\n\\n];` into the page and then
    tries to fill it with a string replace that never matched, so every
    descent except three (which has its own builder) has two panel headings
    with nothing under them. The sentences exist — `panelA` / `panelB` in
    the three descent builders — so they are lifted from there. Measured on
    the live pages: `renderList(` appears on none of the eight."""
    import ast
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = {}
    for name in ('build_descent_a.py', 'build_descent_b.py', 'build_descent_c.py'):
        src = open(os.path.join(here, name), encoding='utf-8').read()
        for m in re.finditer(r"file='([^']+)'", src):
            fname = m.group(1)
            seg = src[m.end():]
            a = re.search(r'panelA=(\[.*?\]),\n', seg, re.S)
            b = re.search(r'panelB=(\[.*?\]),\n', seg, re.S)
            out[fname] = dict(A=ast.literal_eval(a.group(1)), B=ast.literal_eval(b.group(1)))
    return out


DESCENT_PANELS = None


def diagram_card(block, panels_js, fname=None):
    global DESCENT_PANELS
    dc = re.search(r'<div class="diagram-card">(.*?)\n      </div>\n', block, re.S)
    if not dc:
        return None
    dc = dc.group(1)
    intro = re.search(r'<p class="diagram-intro"[^>]*>(.*?)</p>', dc, re.S)
    svg = re.search(r'(<svg.*?</svg>)', dc, re.S)
    panels = []
    for pm in re.finditer(r'<div class="diagram-panel([^"]*)" id="([^"]+)">\s*<h4[^>]*>(.*?)</h4>\s*<ul id="([^"]+)">', dc, re.S):
        panels.append(dict(id=pm.group(2), cls=pm.group(1).strip(), head=inner(pm.group(3)),
                           items=panels_js.get(pm.group(4), [])))
    if panels and not any(p['items'] for p in panels):
        if DESCENT_PANELS is None:
            DESCENT_PANELS = descent_panels_from_builders()
        rec = DESCENT_PANELS.get(fname)
        if rec and len(panels) == 2:
            panels[0]['items'] = rec['A']
            panels[1]['items'] = rec['B']
            panels[0]['recovered'] = panels[1]['recovered'] = 'passive_kit panelA/panelB'
    # Camp four's "Three ropes to now" uses click-to-highlight bars instead of
    # panels: a heading, a rule and two examples each.
    bars = []
    for bm in re.finditer(r'<button class="use-bar" data-shape="([^"]+)"[^>]*>(.*?)</button>', block, re.S):
        body = bm.group(2)
        h4 = re.search(r'<h4[^>]*>(.*?)</h4>', body, re.S)
        p = re.search(r'<p[^>]*>(.*?)</p>', body, re.S)
        exs = [inner(x) for x in re.findall(r'\n\s*<span>(.*?)</span>', body, re.S)]
        bars.append(dict(shape=bm.group(1), head=inner(h4.group(1)), body=inner(p.group(1)) if p else None, examples=exs))
    d = dict(intro=inner(intro.group(1)) if intro else None,
             svg=svg.group(1) if svg else None, panels=panels)
    if bars:
        d['bars'] = bars
    return d


def route_links(block):
    return [(href, inner(txt)) for href, txt in
            re.findall(r'<a class="route-link" href="([^"]+)">(.*?)</a>', block, re.S)]


def freq_slider(block):
    words = [(w, int(v)) for w, v in
             re.findall(r'data-label="([^"]+)" data-value="(\d+)"', block)]
    examples = [inner(x) for x in re.findall(r'<div class="ft-example">(.*?)</div>', block, re.S)]
    rule = re.search(r'<div class="ft-rule">(.*?)</div>', block, re.S)
    return dict(words=words, examples=examples, rule=inner(rule.group(1)) if rule else None)


def sections(main, panels_js, fname=None):
    out = []
    parts = re.split(r'\n    <div class="camp" id="([^"]+)">', main)
    # parts[0] is everything before the first camp; then id, body, id, body…
    for sid, body in zip(parts[1::2], parts[2::2]):
        if sid in ('quiz', 'results-camp'):
            continue
        label = re.search(r'<div class="camp-label"[^>]*>(.*?)</div>', body, re.S)
        h2 = re.search(r'<h2[^>]*>(.*?)</h2>', body, re.S)
        sec = dict(id=sid, label=inner(label.group(1)) if label else None,
                   title=inner(h2.group(1)) if h2 else None)
        # a section-level note (the passive pages open "When to use it" with one)
        lead = re.search(r'</h2>\s*(?:<div class="lang-globe-wrap".*?</div></div>\s*)?<p class="chart-note"[^>]*>(.*?)</p>', body, re.S)
        if lead:
            sec['lead'] = inner(lead.group(1))
        grid = re.search(r'<div class="(rule-grid|form-grid)"[^>]*>(.*?)\n      </div>', body, re.S)
        if grid:
            sec['cards'] = cards(grid.group(2))
        ch = charts(body)
        if ch:
            sec['charts'] = ch
        sb = signal_boxes(body)
        if sb:
            sec['signals'] = sb
        dc = diagram_card(body, panels_js, fname)
        if dc:
            sec['diagram'] = dc
        # a section-level closing example, outside any chart-wrap
        tail = re.findall(r'\n      <p class="example"[^>]*>(.*?)</p>', body, re.S)
        if tail:
            sec['example'] = inner(tail[-1])
        rl = route_links(body)
        if rl:
            sec['links'] = rl
        if sid == 'freq-slider':
            sec['freq'] = freq_slider(body)
        out.append(sec)
    return out


def extract(slug, fname):
    s = open(os.path.join(ROOT, fname), encoding='utf-8').read()
    main = between(s, r'<main>', r'</main>')
    hero = between(main, r'<section class="hero" id="hero">', r'</section>')
    eyebrow = re.search(r'<span class="eyebrow"[^>]*>(.*?)</span>', hero, re.S)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', hero, re.S)
    lede = re.search(r'<p[^>]*>(.*?)</p>', hero, re.S)
    hero_svg = re.search(r'(<svg class="hero-diagram".*?</svg>|<svg class="ring-hero-svg".*?</svg>)', hero, re.S)
    hero_img = re.search(r'<img src="([^"]+)"[^>]*alt="([^"]*)"', hero)
    root = re.search(r':root\{(.*?)\}', s, re.S).group(1)
    palette = dict(re.findall(r'--([a-z-]+):\s*(#[0-9A-Fa-f]{6})', root))
    title = re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip()
    meta = re.search(r'<meta name="description" content="([^"]*)"', s)
    panels_js = js_lists(s)
    ex_tr = re.search(r'\nvar EX_TR = (\{.*?\});', s, re.S)
    tr_order = re.search(r'\nvar TR_ORDER = (\[.*?\]);', s)
    sid = re.search(r'var SHERPA_ID = "([^"]+)"', s)
    face = re.search(r'var SHERPA_FACE = "([^"]+)"', s)
    twin = re.search(r'var SHERPA_TWIN = (null|"[^"]+")', s)
    kind = slug.split('-')[0]
    d = dict(
        slug=slug, file=fname, kind=kind,
        number=int(slug.split('-')[1]) if slug.split('-')[1].isdigit() else None,
        title=html.unescape(title),
        description=html.unescape(meta.group(1)) if meta else None,
        sherpa_id=sid.group(1) if sid else None,
        face=face.group(1) if face else None,
        twin=json.loads(twin.group(1)) if twin else None,
        palette=palette,
        hero=dict(eyebrow=inner(eyebrow.group(1)), h1=inner(h1.group(1)),
                  lede=inner(lede.group(1)),
                  svg=hero_svg.group(1) if hero_svg else None,
                  img=dict(src=hero_img.group(1), alt=hero_img.group(2)) if hero_img else None),
        sections=sections(main, panels_js, fname),
        quiz=js_questions(s),
        results=js_results_messages(s),
        ex_tr=json.loads(ex_tr.group(1)) if ex_tr else {},
        tr_order=json.loads(tr_order.group(1)) if tr_order else [],
        i18n=js_i18n(s),
    )
    return d


def main():
    os.makedirs(OUT, exist_ok=True)
    want = sys.argv[1:] or list(PAGES)
    for slug in want:
        d = extract(slug, PAGES[slug])
        path = os.path.join(OUT, slug + '.json')
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        secs = ' '.join('%s[%s]' % (x['id'], ''.join(k[0] for k in ('cards', 'charts', 'signals', 'diagram', 'freq', 'links') if k in x))
                        for x in d['sections'])
        print('%-16s q=%2d ex_tr=%2d res=%s i18n=%s  %s' % (
            slug, len(d['quiz']), len(d['ex_tr']), 'y' if d['results'] else '-',
            ','.join(d['i18n']) if d['i18n'] else '-', secs))


if __name__ == '__main__':
    main()
