# -*- coding: utf-8 -*-
"""Build the grammar landing page, `grammar.html`.

    python3 tools/build_hubs.py                  # builds it with the topic pages; then tools/seo.py
    python3 tools/build_grammar_hub.py --check   # measure every text-on-fill pair; exit 1 on a failure
    python3 tools/build_grammar_hub.py --palette # re-derive the colours below from the hero

`tools/build_hubs.py` calls `render()` for the page body and its style
block, so the normal pipeline keeps it current: add a lesson to the
catalogue, run build_hubs, and every count on this page follows.

WHY IT IS ITS OWN FILE. Innes, 2026-09-26: *"redesign this
forbesenglish.com/grammar so it looks cool like my IELTS hub, or Sherpa
Hub or Block Camp hub with colour coded tenses"*. Until then grammar.html
was three paragraphs and nineteen white cards in the topic pages' chrome.
It is now a landing page in the IELTS hub's family — full-bleed hero, the
counts, one signature figure, chapters — and the figure is the tense code:
the twelve tenses as a grid of time by shape, plus going to, each square
in its tense colour.

THE TENSE COLOURS ARE READ OFF THE ROUTE MAP, NOT TYPED HERE.
`sherpa-tensing-route-map.html` is where the site publishes a colour per
tense (HOUSE-STYLE §5a), and it was recoloured three times in September;
`lesson-template/tense-palette.css` and Block Camp still carry older values
by design (see HANDOFF 2026-09-26). This page follows the map: each camp's
`--c` fill and `--k` ink are lifted from the guide's own grid with a regex
(`tense_colours()`), the ink is measured on the fill on every build, and a
tense the map has no colour for is reported rather than guessed.

THE PAGE PALETTE is derived from the hero, not picked: `--palette` runs
    extract-palette.py "Sherpa Tensing/hero-route-map.jpg" --light  -> paper side
    extract-palette.py "Sherpa Tensing/hero-route-map.jpg"          -> the dark bands
    PIL MEDIANCUT, 8 colours                                        -> the art fields
and prints the block to paste over PALETTE. The hero is the Sherpa ridge
because that picture is where the tense colours come from: the route up
the mountain is the route through the tenses.

PICTURES. Each topic card carries its hub's own hero (topics.hero — the
first free lesson's picture) as a web-sized copy in `grammar-hub/`, named
by a hash of its inputs like the IELTS hub's derivatives: change the
source and the name changes, the old copy is pruned, and the HTML diff
shows it. The hero and the two route plates are served as they are.

CLAIMS ARE COUNTED, NOT TYPED. Lesson counts, level spans and Free on
every square, card and plate come from the catalogue; a tense with one
lesson opens that lesson instead of a hub that would bury it.
"""
import glob
import hashlib
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo                                   # noqa: E402
import topics                                # noqa: E402

ROOT = seo.ROOT
SITE = seo.SITE
ART = 'grammar-hub'                          # web-sized card pictures live here
ROUTE_MAP = 'sherpa-tensing-route-map.html'

HERO = 'Sherpa Tensing/hero-route-map.jpg'
HERO_ALT = ('A staircase cut into the snow of a mountain ridge, climbing towards '
            'a distant peak under a pale pink and blue sky')
HERO_OG = '/' + seo.quote(HERO)              # seo.py puts this on the og:image
SHERPA_ART = 'Sherpa Tensing/sherpa-day.jpg'
BLOCKCAMP_ART = 'BlockCamp/hub-hero.jpg'

# ── the tense grid ────────────────────────────────────────────────────
# A tense is a time and a shape. `hub` is the topic page a square opens;
# `pattern` narrows that hub's lessons to the one tense (the future hub
# holds five forms; the past perfect hub holds its continuous too), and
# `minus` takes a sibling's lessons back out. `form` is the model sentence
# in CAPS, the house rule for grammar tokens. `key` is the route map's name
# for the tense, which is where its colour comes from.
TIMES = [('past', 'Past'), ('present', 'Present'), ('future', 'Future')]
SHAPES = [('simple', 'Simple'), ('continuous', 'Continuous'),
          ('perfect', 'Perfect'), ('perfect-continuous', 'Perfect continuous')]
CELLS = [
    dict(time='present', shape='simple', key='present-simple', name='Present Simple',
         form='I BUILD', hub='present-simple'),
    dict(time='present', shape='continuous', key='present-continuous', name='Present Continuous',
         form='I AM BUILDING', hub='present-continuous'),
    dict(time='present', shape='perfect', key='present-perfect', name='Present Perfect',
         form='I HAVE BUILT', hub='present-perfect'),
    dict(time='present', shape='perfect-continuous', key='present-perfect-continuous',
         name='Present Perfect Continuous', form='I HAVE BEEN BUILDING',
         hub='present-perfect-continuous'),
    dict(time='past', shape='simple', key='past-simple', name='Past Simple',
         form='I BUILT', hub='past-simple'),
    dict(time='past', shape='continuous', key='past-continuous', name='Past Continuous',
         form='I WAS BUILDING', hub='past-continuous'),
    dict(time='past', shape='perfect', key='past-perfect', name='Past Perfect',
         form='I HAD BUILT', hub='past-perfect', minus=r'past perfect continuous'),
    dict(time='past', shape='perfect-continuous', key='past-perfect-continuous',
         name='Past Perfect Continuous', form='I HAD BEEN BUILDING',
         hub='past-perfect', pattern=r'past perfect continuous'),
    dict(time='future', shape='simple', key='future-simple', name='Future Simple',
         form='I WILL BUILD', hub='future-tenses',
         pattern=r'future simple|future-simple|\bwill\b'),
    dict(time='future', shape='continuous', key='future-continuous', name='Future Continuous',
         form='I WILL BE BUILDING', hub='future-tenses', pattern=r'future continuous'),
    dict(time='future', shape='perfect', key='future-perfect', name='Future Perfect',
         form='I WILL HAVE BUILT', hub='future-tenses',
         pattern=r'future perfect', minus=r'future perfect continuous'),
    dict(time='future', shape='perfect-continuous', key='future-perfect-continuous',
         name='Future Perfect Continuous', form='I WILL HAVE BEEN BUILDING',
         hub='future-tenses', pattern=r'future perfect continuous'),
    # Not a tense, taught as one: the thirteenth square, under the future.
    dict(time='future', shape='going-to', key='going-to', name='Going to',
         form='I AM GOING TO BUILD', hub='future-tenses', pattern=r'going to|going-to'),
]
# Which tense colour a topic page wears (build_hubs.topic_page). The future
# hub covers five forms and takes will's colour; the review hub has none.
TOPIC_COLOUR = {
    'present-simple': 'present-simple', 'present-continuous': 'present-continuous',
    'past-simple': 'past-simple', 'past-continuous': 'past-continuous',
    'present-perfect': 'present-perfect',
    'present-perfect-continuous': 'present-perfect-continuous',
    'past-perfect': 'past-perfect', 'future-tenses': 'future-simple',
}

# ── palette ───────────────────────────────────────────────────────────
PALETTE = {
    # extract-palette.py "Sherpa Tensing/hero-route-map.jpg" --light
    'void': '#d8bdac', 'surface': '#e1cfc4', 'surface2': '#dcc5b8',
    'border': '#965c4a', 'text': '#2a1711', 'text-dim': '#5e392e',
    'accent': '#963619', 'accent-bright': '#70230b', 'accent-dim': '#d27457',
    'secondary': '#abc2c3', 'contrast': '#175e4d',
    # extract-palette.py "Sherpa Tensing/hero-route-map.jpg"
    'ink': '#0e1112', 'ink-surface': '#181e1f', 'ink-surface2': '#21292b',
    'ink-border': '#968c89', 'ink-text': '#f5f3f2', 'ink-text-dim': '#bfaaa3',
    'ink-accent': '#d8b7ad',
    # the hero quantised (MEDIANCUT, 8), most to least common
    'sky': '#a7b8b9', 'sky-deep': '#7e989d', 'snow': '#d3b8af', 'rock': '#1c2223',
    'slate': '#55686d', 'stone': '#a0a2a0', 'mist': '#c2c0bb', 'cloud': '#d2cbc3',
}
# Mixed, not picked: the paper and the card, the derived surface lifted
# towards the derived light text. Resolved here so --check can measure
# them; the CSS spells out the same color-mix().
MIX = {'paper': ('surface', 'ink-text', 0.62), 'card': ('surface', 'ink-text', 0.30)}

# Text-on-fill pairs the page uses, measured on every build. The tense
# squares are measured separately, one per tense, in tense_colours().
CONTRAST = [
    ('ink', 'sky', 4.5, 'hero copy on the sky scrim'),
    ('accent-bright', 'sky', 3.0, 'hero H1 emphasis (large)'),
    ('text', 'paper', 4.5, 'body copy'),
    ('text', 'card', 4.5, 'card titles'),
    ('text-dim', 'paper', 4.5, 'secondary copy'),
    ('text-dim', 'card', 4.5, 'secondary copy on cards'),
    ('accent', 'paper', 4.5, 'kickers, links'),
    ('accent', 'card', 4.5, 'kickers on cards'),
    ('accent-bright', 'paper', 3.0, 'H2 emphasis (large)'),
    ('ink-text', 'ink', 4.5, 'review bar, closing band'),
    ('ink-text-dim', 'ink', 4.5, 'closing band secondary'),
    ('ink-accent', 'ink', 4.5, 'closing band kicker'),
    ('ink-text', 'rock', 4.5, 'route plate copy over the scrim'),
    ('ink-accent', 'rock', 4.5, 'route plate kicker and link'),
    # Focus rings: WCAG 1.4.11 wants 3:1 against what the ring sits on.
    ('accent', 'paper', 3.0, 'focus ring on paper'),
    ('ink', 'sky', 3.0, 'focus ring in the hero'),
    ('ink-accent', 'ink', 3.0, 'focus ring on the closing band'),
]

STATE = {'keep': set()}


def esc(s):
    return html.escape(s, quote=True)


# ── colour maths ──────────────────────────────────────────────────────
def _lum(h):
    h = h.lstrip('#')
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def _ratio(a, b):
    la, lb = _lum(a), _lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def _mix(a, b, t):
    a, b = a.lstrip('#'), b.lstrip('#')
    return '#' + ''.join('%02x' % round(int(a[i:i + 2], 16) * t + int(b[i:i + 2], 16) * (1 - t))
                         for i in (0, 2, 4))


def colours():
    col = dict(PALETTE)
    for k, (a, b, t) in MIX.items():
        col[k] = _mix(PALETTE[a], PALETTE[b], t)
    return col


_KEY = re.compile(r'sherpa-tensing-camp-[a-z]+-([a-z-]+)\.html" style="--c:(#[0-9A-Fa-f]{6});'
                  r'--k:(#[0-9A-Fa-f]{6})"')


def tense_colours(quiet=False):
    """{tense key: (fill, ink)} read off the route map's guide grid. The
    ink is the map's own, re-measured here on the fill; if it no longer
    clears 4.5:1 the better of the two inks is used and the swap is
    reported, because the squares carry small text."""
    src = open(os.path.join(ROOT, ROUTE_MAP), encoding='utf-8').read()
    out = {}
    for key, fill, ink in _KEY.findall(src):
        if key in out:
            continue
        best = max((ink, '#1A1206', '#FFFFFF'), key=lambda k: _ratio(k, fill))
        if _ratio(ink, fill) < 4.5:
            if not quiet:
                print('  ! %s: the map\'s ink %s is %.2f:1 on %s; using %s (%.2f:1)'
                      % (key, ink, _ratio(ink, fill), fill, best, _ratio(best, fill)))
            ink = best
        out[key] = (fill, ink)
    missing = [c['key'] for c in CELLS if c['key'] not in out]
    if missing and not quiet:
        print('  ! %s has no colour for: %s — those squares get the page ink'
              % (ROUTE_MAP, ', '.join(missing)))
    return out


# ── pictures ──────────────────────────────────────────────────────────
def _sha(*parts):
    h = hashlib.sha1()
    for p in parts:
        h.update(p if isinstance(p, bytes) else str(p).encode('utf-8'))
    return h.hexdigest()[:8]


def web_copy(src_rel, stem, width=640, quality=82):
    """A web-sized JPEG of `src_rel` in grammar-hub/, named by its inputs.
    Returns the site-relative path. PIL's encoder is deterministic, so a
    rebuild from the same inputs makes no diff."""
    from PIL import Image
    src = os.path.join(ROOT, src_rel.lstrip('/'))
    data = open(src, 'rb').read()
    name = '%s-%s.jpg' % (stem, _sha(data, width, quality))
    rel = '%s/%s' % (ART, name)
    STATE['keep'].add(name)
    out = os.path.join(ROOT, ART, name)
    if not os.path.exists(out):
        os.makedirs(os.path.join(ROOT, ART), exist_ok=True)
        im = Image.open(src).convert('RGB')
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        im.save(out, 'JPEG', quality=quality, optimize=True, progressive=True)
    return rel


def prune():
    """Delete grammar-hub/*.jpg that this build did not produce."""
    gone = []
    for p in glob.glob(os.path.join(ROOT, ART, '*.jpg')):
        if os.path.basename(p) not in STATE['keep']:
            os.remove(p)
            gone.append(os.path.basename(p))
    return gone


# ── the catalogue, sliced ─────────────────────────────────────────────
def _hay(r):
    hay = ('%s %s' % (r.get('title') or '', r.get('file') or '')).lower()
    return hay.replace('—', ' ').replace('–', ' ')


def cell_rows(cell, allm):
    pool = allm[cell['hub']]
    if cell.get('pattern'):
        pool = [r for r in pool if re.search(cell['pattern'], _hay(r))]
    if cell.get('minus'):
        pool = [r for r in pool if not re.search(cell['minus'], _hay(r))]
    return pool


def free_of(rows):
    return sum(1 for r in rows if r.get('access') != 'pro')


def span(rows):
    return topics.level_span(rows).replace(' to ', '&ndash;') or 'All levels'


def plural(n, one, many=None):
    return '%d %s' % (n, one if n == 1 else (many or one + 's'))


def family(rows, *prefixes):
    return [r for r in rows if r['file'].startswith(prefixes)]


# ── the page ──────────────────────────────────────────────────────────
CSS = """
<!-- GRAMMAR-HUB-CSS:start -->
<style id="grammar-hub-css">
/* The grammar landing page. Generated by tools/build_grammar_hub.py — edit
   it there. Colours: see that file's docstring. Every class is gh- prefixed
   so nothing here collides with the shared block above. */
body.gh {
%(tokens)s
  --gh-paper: color-mix(in srgb, var(--gh-surface) 62%%, var(--gh-ink-text));
  --gh-card:  color-mix(in srgb, var(--gh-surface) 30%%, var(--gh-ink-text));
  --gh-line:  color-mix(in srgb, var(--gh-border) 34%%, transparent);
  --gh-shadow: color-mix(in srgb, var(--gh-ink) 18%%, transparent);
  --gh-max: 1240px;
  --gh-gut: clamp(16px, 4vw, 48px);
  background: var(--gh-paper);
  color: var(--gh-text);
  font-variant-numeric: lining-nums;
}
:where(.gh) a { color: inherit; }
.gh :where(main) a:focus-visible { outline: 3px solid var(--gh-accent); outline-offset: 3px; }
.gh-hero a:focus-visible { outline-color: var(--gh-ink); }
.gh-close a:focus-visible, .gh-review:focus-visible, .gh-route:focus-visible { outline-color: var(--gh-ink-accent); }
.gh-vh { position: absolute; width: 1px; height: 1px; margin: -1px; padding: 0; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
.gh-wrap { max-width: var(--gh-max); margin: 0 auto; padding: 0 var(--gh-gut); }
.gh-kicker {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .16em; text-transform: uppercase; font-size: .8rem;
  color: var(--gh-accent); margin: 0 0 12px;
}
.gh-h2 {
  font-family: 'Playfair Display', serif; font-weight: 900;
  font-size: clamp(2rem, 4.4vw, 3.2rem); line-height: 1.02; letter-spacing: -.012em;
  margin: 0 0 16px; color: var(--gh-text); text-wrap: balance;
}
.gh-h2 em { font-style: normal; color: var(--gh-accent-bright); }
.gh-sechead { max-width: 64ch; }
.gh-sechead p { font-size: 1.1rem; line-height: 1.62; color: var(--gh-text-dim); margin: 0; }
.gh-sechead p + p { margin-top: 12px; }
.gh-sechead em { font-style: italic; color: var(--gh-text); }
.gh-btn {
  display: inline-flex; align-items: center; gap: .5em;
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .09em; text-transform: uppercase; font-size: .92rem;
  text-decoration: none; padding: 13px 22px; border-radius: 999px;
  background: var(--gh-ink); color: var(--gh-ink-text);
  border: 2px solid var(--gh-ink);
  transition: background .18s ease, border-color .18s ease, transform .18s ease;
}
.gh-btn:hover { background: var(--gh-accent-bright); border-color: var(--gh-accent-bright); transform: translateY(-1px); }
.gh-btn-quiet { background: transparent; color: var(--gh-ink); }
.gh-btn-quiet:hover { background: var(--gh-ink); color: var(--gh-ink-text); border-color: var(--gh-ink); }
.gh-pill {
  display: inline-block; font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .1em; text-transform: uppercase; font-size: .68rem; line-height: 1;
  padding: 4px 8px 3px; border-radius: 999px; white-space: nowrap;
  background: color-mix(in srgb, var(--gh-text) 8%%, transparent); color: var(--gh-text-dim);
}
.gh-pill-free { background: var(--gh-accent); color: var(--gh-ink-text); }

/* ── hero: the ridge, copy over the sky ── */
.gh-hero {
  position: relative; isolation: isolate; overflow: hidden;
  min-height: clamp(560px, 84vh, 800px); display: grid; align-items: center;
  background: var(--gh-sky);
}
.gh-hero-img {
  position: absolute; inset: 0; z-index: -2; width: 100%%; height: 100%%;
  object-fit: cover; object-position: 68%% 50%%;
  animation: gh-settle 2.6s cubic-bezier(.2,.7,.2,1) backwards;
}
@keyframes gh-settle { from { transform: scale(1.06); } to { transform: none; } }
.gh-hero::after {
  content: ''; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(90deg,
    color-mix(in srgb, var(--gh-sky) 90%%, transparent) 0%%,
    color-mix(in srgb, var(--gh-sky) 80%%, transparent) 46%%,
    color-mix(in srgb, var(--gh-sky) 30%%, transparent) 68%%,
    transparent 84%%);
}
.gh-hero-in {
  width: 100%%; max-width: var(--gh-max); margin: 0 auto;
  padding: clamp(40px, 7vh, 80px) var(--gh-gut) 56px;
  display: grid; grid-template-columns: minmax(0, 600px) 1fr;
}
.gh-hero-copy { color: var(--gh-ink); }
.gh-hero .gh-kicker { color: var(--gh-ink); }
.gh-h1 {
  font-family: 'Playfair Display', serif; font-weight: 900;
  font-size: clamp(3rem, min(7vw, 10.5vh), 5.8rem); line-height: .94; letter-spacing: -.022em;
  margin: 0 0 22px; color: var(--gh-ink); text-wrap: balance;
}
.gh-h1 em { font-style: normal; color: var(--gh-accent-bright); }
.gh-lede { font-size: clamp(1.08rem, 1.5vw, 1.22rem); line-height: 1.58; margin: 0 0 24px; max-width: 34em; text-wrap: pretty; }
.gh-stats {
  list-style: none; margin: 0 0 30px; padding: 16px 0 0; display: flex; flex-wrap: wrap; gap: 14px 30px;
  border-top: 1px solid color-mix(in srgb, var(--gh-ink) 30%%, transparent);
}
.gh-stats li { display: flex; align-items: baseline; gap: 8px; }
.gh-stats b { font-family: 'Barlow Condensed', sans-serif; font-weight: 800; font-size: 2.5rem; line-height: .9; }
.gh-stats span { font-size: .95rem; line-height: 1.3; max-width: 16em; text-wrap: balance; }
.gh-stats .gh-stat-free b { color: var(--gh-accent-bright); }
.gh-ctas { display: flex; flex-wrap: wrap; gap: 12px; }
@media (max-width: 880px) {
  .gh-hero { display: block; min-height: 0; background: var(--gh-paper); }
  .gh-hero-img { position: relative; z-index: auto; height: auto; aspect-ratio: 16 / 10; object-position: 50%% 60%%; }
  .gh-hero::after { display: none; }
  .gh-hero-in { grid-template-columns: 1fr; padding-top: 30px; padding-bottom: 44px; }
  .gh-hero-copy, .gh-hero .gh-kicker { color: var(--gh-text); }
  .gh-h1 { color: var(--gh-text); }
  .gh-stats { border-top-color: var(--gh-line); }
  .gh-btn-quiet { color: var(--gh-text); border-color: var(--gh-text); }
}

/* ── the tense code: time across, shape down ── */
.gh-tenses { padding: clamp(64px, 9vw, 120px) 0 clamp(48px, 7vw, 88px); }
.gh-grid {
  display: grid; grid-template-columns: minmax(92px, 132px) repeat(3, minmax(0, 1fr));
  gap: 8px; margin: clamp(30px, 4.6vw, 48px) 0 0;
}
.gh-th, .gh-sh, .gh-cell { grid-column: var(--gc); grid-row: var(--gr); order: var(--o); }
.gh-th {
  text-align: center; padding: 0 0 6px; margin: 0;
  font-family: 'Barlow Condensed', sans-serif; font-weight: 800; letter-spacing: .18em;
  text-transform: uppercase; font-size: .92rem; color: var(--gh-text);
}
.gh-th::after {
  content: ''; display: block; height: 3px; margin-top: 8px; border-radius: 2px;
  background: color-mix(in srgb, var(--gh-text) 22%%, transparent);
}
.gh-th.gh-now::after { background: var(--gh-accent); }
.gh-th small { display: block; font-weight: 600; letter-spacing: .1em; font-size: .7rem; color: var(--gh-text-dim); margin-top: 2px; }
.gh-sh {
  display: flex; align-items: center; justify-content: flex-end; text-align: right;
  padding-right: 12px; margin: 0; line-height: 1.2;
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .12em;
  text-transform: uppercase; font-size: .74rem; color: var(--gh-text-dim);
}
.gh-cell {
  container-type: inline-size; position: relative;
  display: flex; flex-direction: column; gap: 4px;
  min-height: clamp(108px, 11vw, 132px); padding: 14px 14px 12px; border-radius: 12px;
  background: var(--c); color: var(--k); text-decoration: none;
  transition: transform .2s ease, box-shadow .2s ease;
  animation: gh-grow .8s cubic-bezier(.2,.7,.2,1) backwards; animation-delay: var(--d, 0s);
}
@keyframes gh-grow { from { transform: translateY(10px); opacity: 0; } to { transform: none; opacity: 1; } }
.gh-cell:hover { transform: translateY(-4px); box-shadow: 0 16px 30px var(--gh-shadow); }
.gh-cell-name {
  font-family: 'Playfair Display', serif; font-weight: 700; margin-bottom: auto; padding-bottom: 10px;
  font-size: clamp(1rem, 9cqi, 1.28rem); line-height: 1.15; text-wrap: balance;
}
.gh-cell-form {
  display: block; font-family: 'Barlow Condensed', sans-serif; font-weight: 800; letter-spacing: .06em;
  font-size: clamp(.92rem, 8.4cqi, 1.2rem); line-height: 1.05; opacity: .92;
}
.gh-cell-meta { display: block; font-size: .8rem; line-height: 1.35; opacity: .9; margin-top: 2px; }
.gh-cell-meta b { font-weight: 700; }
.gh-cell-where { display: block; font-size: .74rem; opacity: .8; }
.gh-cell-off { --c: var(--gh-mist); --k: var(--gh-text); }
.gh-key { font-size: .9rem; line-height: 1.5; color: var(--gh-text-dim); margin: 18px 0 0; max-width: 68ch; }
.gh-review {
  display: grid; grid-template-columns: auto minmax(0, 1fr) auto; align-items: center; gap: 12px 22px;
  margin: 26px 0 0; padding: 18px 24px; border-radius: 12px; text-decoration: none;
  background: var(--gh-ink); color: var(--gh-ink-text);
  transition: transform .18s ease, box-shadow .18s ease;
}
.gh-review:hover { transform: translateY(-2px); box-shadow: 0 16px 30px var(--gh-shadow); }
.gh-review b { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.25rem; }
.gh-review span { color: var(--gh-ink-text-dim); font-size: .98rem; line-height: 1.4; }
.gh-review .gh-go {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .1em;
  text-transform: uppercase; font-size: .84rem; color: var(--gh-ink-accent); white-space: nowrap;
}
@media (max-width: 680px) {
  .gh-grid { grid-template-columns: 1fr; gap: 6px; }
  .gh-th, .gh-cell { grid-column: 1; grid-row: auto; }
  .gh-sh { display: none; }
  .gh-th { text-align: left; margin-top: 18px; }
  .gh-th:first-child { margin-top: 0; }
  .gh-cell { min-height: 0; display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 2px 12px; align-items: baseline; padding: 11px 14px; }
  .gh-cell-name { grid-column: 1; margin: 0; padding: 0; font-size: 1.06rem; }
  .gh-cell-form { grid-column: 2; font-size: .95rem; text-align: right; }
  .gh-cell-meta { grid-column: 1 / -1; }
  .gh-review { grid-template-columns: 1fr; }
}

/* ── every topic ── */
.gh-topics { padding: clamp(56px, 8vw, 104px) 0 clamp(40px, 6vw, 72px); background: var(--gh-card); border-top: 1px solid var(--gh-line); border-bottom: 1px solid var(--gh-line); }
.gh-group { margin-top: clamp(36px, 5vw, 56px); }
.gh-group-h {
  display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap;
  padding-bottom: 10px; margin: 0 0 18px; border-bottom: 2px solid var(--gh-text);
}
.gh-group-h h3 { font-family: 'Playfair Display', serif; font-weight: 700; font-size: clamp(1.4rem, 2.6vw, 1.8rem); margin: 0; }
.gh-group-h span { font-size: .95rem; color: var(--gh-text-dim); }
.gh-cards { list-style: none; margin: 0; padding: 0; display: grid; gap: 16px; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); }
.gh-card {
  --c: var(--gh-accent);
  position: relative; display: flex; flex-direction: column; height: 100%%;
  background: var(--gh-paper); border: 1px solid var(--gh-line); border-radius: 14px; overflow: hidden;
  text-decoration: none; color: inherit; box-shadow: 0 2px 10px var(--gh-shadow);
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.gh-card::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 5px; background: var(--c); z-index: 2; }
.gh-card:hover { transform: translateY(-4px); box-shadow: 0 18px 36px var(--gh-shadow); border-color: color-mix(in srgb, var(--c) 60%%, transparent); }
.gh-thumb { aspect-ratio: 16 / 9; overflow: hidden; background: var(--gh-sky-deep); }
.gh-thumb img { width: 100%%; height: 100%%; object-fit: cover; display: block; transition: transform .6s ease; }
.gh-card:hover .gh-thumb img { transform: scale(1.05); }
.gh-card-body { display: flex; flex-direction: column; gap: 6px; padding: 14px 16px 16px; flex: 1; }
.gh-card-body h4 { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.14rem; line-height: 1.25; margin: 0; }
.gh-card-body p { font-size: .92rem; line-height: 1.5; color: var(--gh-text-dim); margin: 0; }
.gh-card-meta { display: flex; flex-wrap: wrap; gap: 6px; margin-top: auto; padding-top: 8px; }
.gh-swatch { display: inline-block; width: .8em; height: .8em; border-radius: 3px; background: var(--c); vertical-align: -.05em; margin-right: .45em; }
.gh-plates { list-style: none; margin: 0; padding: 0; display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
.gh-plates .gh-card { --c: var(--gh-contrast); }
.gh-plates .gh-thumb { aspect-ratio: 16 / 10; }
.gh-plates .gh-card-body h4 { font-size: 1.28rem; }
@media (max-width: 900px) and (min-width: 521px) {
  .gh-plates .gh-card { flex-direction: row; }
  .gh-plates .gh-thumb { width: 38%%; aspect-ratio: auto; flex: none; }
}

/* ── two routes through the tenses ── */
.gh-routes { padding: clamp(56px, 8vw, 104px) 0 clamp(24px, 4vw, 40px); }
.gh-route-list { list-style: none; margin: clamp(26px, 4vw, 40px) 0 0; padding: 0; display: grid; gap: 16px; grid-template-columns: 1fr 1fr; }
.gh-route {
  position: relative; isolation: isolate; overflow: hidden;
  display: flex; flex-direction: column; justify-content: flex-end; gap: 8px;
  min-height: clamp(340px, 30vw, 380px); padding: clamp(18px, 2.6vw, 28px);
  border-radius: 16px; text-decoration: none; color: var(--gh-ink-text);
  box-shadow: 0 18px 40px var(--gh-shadow);
  transition: transform .18s ease, box-shadow .18s ease;
}
.gh-route:hover { transform: translateY(-3px); box-shadow: 0 26px 52px var(--gh-shadow); }
.gh-route img { position: absolute; inset: 0; z-index: -2; width: 100%%; height: 100%%; object-fit: cover; transition: transform 1.4s cubic-bezier(.2,.7,.2,1); }
.gh-route:hover img { transform: scale(1.04); }
.gh-route::before {
  content: ''; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(180deg, transparent 0%%,
    color-mix(in srgb, var(--gh-rock) 30%%, transparent) 16%%,
    color-mix(in srgb, var(--gh-rock) 90%%, transparent) 40%%,
    color-mix(in srgb, var(--gh-rock) 96%%, transparent) 100%%);
}
.gh-route .gh-kicker { color: var(--gh-ink-accent); margin: 0; }
.gh-route h3 { font-family: 'Playfair Display', serif; font-weight: 900; font-size: clamp(1.6rem, 3vw, 2.2rem); line-height: 1.02; margin: 0; }
.gh-route p { margin: 0; font-size: .98rem; line-height: 1.5; color: var(--gh-ink-text); max-width: 46ch; }
.gh-route p b { font-weight: 700; }
.gh-route-go { font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; font-size: .84rem; color: var(--gh-ink-accent); margin-top: 4px; }
@media (max-width: 760px) { .gh-route-list { grid-template-columns: 1fr; } }

/* ── notes ── */
.gh-notes { padding: clamp(24px, 4vw, 40px) 0 clamp(64px, 9vw, 112px); }
.gh-notes-grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(16px, 2.4vw, 28px); }
.gh-note { background: var(--gh-card); border: 1px solid var(--gh-line); border-radius: 16px; padding: clamp(22px, 3vw, 34px); }
.gh-note h3 { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.36rem; margin: 0 0 10px; color: var(--gh-text); }
.gh-note p { margin: 0; line-height: 1.64; color: var(--gh-text-dim); }
.gh-note p + p { margin-top: 10px; }
.gh-note strong { color: var(--gh-text); font-weight: 700; }
.gh-note a { color: var(--gh-accent); font-weight: 700; }
@media (max-width: 760px) { .gh-notes-grid { grid-template-columns: 1fr; } }

/* ── closing band ── */
.gh-close { position: relative; isolation: isolate; overflow: hidden; background: var(--gh-ink); color: var(--gh-ink-text); }
.gh-close-art { position: absolute; inset: 0; z-index: -2; width: 100%%; height: 100%%; object-fit: cover; object-position: 50%% 30%%; }
.gh-close::after {
  content: ''; position: absolute; inset: 0; z-index: -1;
  background: radial-gradient(ellipse 70%% 90%% at 50%% 50%%, color-mix(in srgb, var(--gh-ink) 93%%, transparent) 30%%, color-mix(in srgb, var(--gh-ink) 66%%, transparent) 100%%);
}
.gh-close-in { padding: clamp(72px, 10vw, 140px) var(--gh-gut); max-width: 860px; margin: 0 auto; text-align: center; }
.gh-close .gh-kicker { color: var(--gh-ink-accent); }
.gh-close .gh-h2 { color: var(--gh-ink-text); }
.gh-close .gh-h2 em { color: var(--gh-ink-accent); }
.gh-close p { font-size: 1.1rem; line-height: 1.62; color: var(--gh-ink-text-dim); margin: 0 auto 30px; max-width: 54ch; }
.gh-close .gh-ctas { justify-content: center; }
.gh-close .gh-btn { background: var(--gh-ink-text); border-color: var(--gh-ink-text); color: var(--gh-ink); }
.gh-close .gh-btn:hover { background: var(--gh-ink-accent); border-color: var(--gh-ink-accent); }
.gh-close .gh-btn-quiet { background: transparent; color: var(--gh-ink-text); border-color: color-mix(in srgb, var(--gh-ink-text) 55%%, transparent); }
.gh-close .gh-btn-quiet:hover { background: var(--gh-ink-text); color: var(--gh-ink); }

@media (prefers-reduced-motion: reduce) {
  .gh *, .gh *::before, .gh *::after { animation: none !important; transition: none !important; }
}
</style>
<!-- GRAMMAR-HUB-CSS:end -->
"""


def css():
    tokens = '\n'.join('  --gh-%s: %s;' % (k, v) for k, v in PALETTE.items())
    return CSS % {'tokens': tokens}


def _cell(cell, rows, tc, i):
    col = tc.get(cell['key'])
    style = '--c:%s;--k:%s;' % col if col else ''
    cls = 'gh-cell' if col else 'gh-cell gh-cell-off'
    own = cell['hub'] == cell['key']
    n, free = len(rows), free_of(rows)
    hub = topics.BY_SLUG[cell['hub']]
    if own:
        href, where = topics.hub_url(cell['hub']), ''
    elif n == 1:
        href = seo.quote(rows[0]['file'])
        where = 'one lesson &middot; opens it'
    else:
        href = topics.hub_url(cell['hub'])
        where = 'in %s' % esc(hub['name'])
    if n:
        meta = '<b>%s</b> &middot; %s' % (plural(n, 'lesson'), span(rows))
        if free:
            meta += ' &middot; %d free' % free
    else:
        meta = 'no lesson yet'
    if where:
        meta += '<span class="gh-cell-where">%s</span>' % where
    gc = {'past': 2, 'present': 3, 'future': 4}[cell['time']]
    gr = [s for s, _ in SHAPES].index(cell['shape']) + 2 if cell['shape'] != 'going-to' else 6
    order = gc * 10 + gr
    label = '%s: %s' % (cell['name'], cell['form'].capitalize())
    return ('<a class="%s" href="%s" style="%s--gc:%d;--gr:%d;--o:%d;--d:%.2fs" aria-label="%s">'
            '<span class="gh-cell-name" aria-hidden="true">%s</span>'
            '<span class="gh-cell-form" aria-hidden="true">%s</span>'
            '<span class="gh-cell-meta">%s</span></a>'
            % (cls, href, style, gc, gr, order, .05 * i, esc(label),
               esc(cell['name']), esc(cell['form']), meta))


def _card(t, rows, images, colour=None):
    n, free = len(rows), free_of(rows)
    hero = topics.hero(rows, images)
    thumb = ('<span class="gh-thumb"><img src="%s" alt="" loading="lazy" width="640" height="360"></span>'
             % esc(web_copy(hero, t['slug'])) if hero else '<span class="gh-thumb"></span>')
    desc = t['desc'] or ('The IELTS Academic route: Writing, Speaking, Listening, Reading '
                         'and the vocabulary that feeds them.')
    desc = desc.split(': ', 1)[-1] if ': ' in desc else desc
    style = ' style="--c:%s"' % colour[0] if colour else ''
    swatch = '<span class="gh-swatch" aria-hidden="true"></span>' if colour else ''
    pills = ['<span class="gh-pill">%s</span>' % span(rows),
             '<span class="gh-pill">%s</span>' % plural(n, 'lesson')]
    if free:
        pills.append('<span class="gh-pill gh-pill-free">%d free</span>' % free)
    return ('<li><a class="gh-card" href="%s"%s>%s<span class="gh-card-body">'
            '<h4>%s%s</h4><p>%s</p><span class="gh-card-meta">%s</span></span></a></li>'
            % (topics.hub_url(t['slug']), style, thumb, swatch, esc(t['name']),
               esc(seo.trim(desc, 150)), ''.join(pills)))


def render(rows, images, allm):
    """(css, body, json-ld) for grammar.html. `rows` are the finished
    lessons, `allm` topics.members() of them."""
    tc = tense_colours()
    listed = [t for t in topics.TOPICS if allm[t['slug']]]
    files = {r['file'] for t in listed for r in allm[t['slug']]}
    free_files = {r['file'] for t in listed for r in allm[t['slug']] if r.get('access') != 'pro'}
    tense_topics = [t for t in listed if t['group'] == 'Tenses']
    grammar_topics = [t for t in listed if t['group'] == 'Grammar']
    skill_topics = [t for t in listed if t['group'] == 'Skills']
    review = allm['tense-review']
    sherpa = family(rows, 'sherpa-tensing-')
    blockcamp = family(rows, 'blockcamp-', 'block-camp/')
    tense_lessons = {r['file'] for t in tense_topics for r in allm[t['slug']]}

    b = []
    # ── hero ──
    b.append('''<main>
<header class="gh-hero" aria-labelledby="gh-h1">
  <img class="gh-hero-img" src="%s" width="1200" height="672" alt="%s" fetchpriority="high">
  <div class="gh-hero-in">
    <div class="gh-hero-copy">
      <p class="gh-kicker">Grammar &middot; A1 to C2 &middot; %s</p>
      <h1 class="gh-h1" id="gh-h1">English grammar, <em>by topic</em></h1>
      <p class="gh-lede">Every grammar lesson on the site, shelved by the point it teaches. Each topic page explains the rule in plain sentences, then lists the lessons that drill it, by level, free ones first.</p>
      <ul class="gh-stats">
        <li><b>%d</b><span>lessons</span></li>
        <li><b>%d</b><span>topics</span></li>
        <li class="gh-stat-free"><b>%d</b><span>free &mdash; no sign-in</span></li>
      </ul>
      <div class="gh-ctas">
        <a class="gh-btn" href="#tenses">The tenses, in colour <span aria-hidden="true">&darr;</span></a>
        <a class="gh-btn gh-btn-quiet" href="level-checker.html">Find your level</a>
      </div>
    </div>
  </div>
</header>''' % (esc(seo.quote(HERO)), esc(HERO_ALT), plural(len(listed), 'topic'),
                len(files), len(listed), len(free_files)))

    # ── the tense code ──
    b.append('''<section class="gh-tenses" id="tenses" aria-labelledby="gh-tenses-h">
  <div class="gh-wrap">
    <div class="gh-sechead">
      <p class="gh-kicker">The tense code</p>
      <h2 class="gh-h2" id="gh-tenses-h">Twelve tenses, <em>one colour each</em></h2>
      <p>A tense is a time and a shape: three times across, four shapes down, and one square more for <em>going to</em>, which is not a tense but is taught as one. Each wears the colour it has on the Sherpa Tensing route map, so once you know the code a lesson&rsquo;s colour tells you its tense before you read its title.</p>
    </div>
    <nav class="gh-grid" aria-label="The tenses, by time and shape">''')
    for i, (key, name) in enumerate(TIMES):
        now = ' gh-now' if key == 'present' else ''
        sub = {'past': 'then', 'present': 'now', 'future': 'later'}[key]
        b.append('      <p class="gh-th%s" style="--gc:%d;--gr:1;--o:%d" aria-hidden="true">%s<small>%s</small></p>'
                 % (now, i + 2, (i + 2) * 10, name, sub))
    for j, (key, name) in enumerate(SHAPES):
        b.append('      <p class="gh-sh" style="--gc:1;--gr:%d" aria-hidden="true">%s</p>' % (j + 2, name))
    b.append('      <p class="gh-sh" style="--gc:1;--gr:6" aria-hidden="true">+ one more</p>')
    cell_counts = {}
    for i, cell in enumerate(CELLS):
        crow = cell_rows(cell, allm)
        cell_counts[cell['key']] = len(crow)
        b.append('      ' + _cell(cell, crow, tc, i))
    b.append('''    </nav>
    <p class="gh-key">A square opens the topic page for its tense &mdash; the rule in plain sentences, then every lesson on it by level &mdash; or, where one lesson stands alone, that lesson. The same colours mark the camps on the <a href="sherpa-tensing-route-map.html">Sherpa Tensing route map</a> and the units in <a href="block-camp.html">Block Camp</a>.</p>
    <a class="gh-review" href="tense-review.html">
      <b>All of them at once</b>
      <span>Tense review and scored grammar tests &mdash; every tense side by side, the time signals that choose between them, and tests that name the lesson to go back to. %s, %d free.</span>
      <span class="gh-go">Open &rarr;</span>
    </a>
  </div>
</section>''' % (plural(len(review), 'lesson'), free_of(review)))

    # ── every topic ──
    b.append('''<section class="gh-topics" id="topics" aria-labelledby="gh-topics-h">
  <div class="gh-wrap">
    <div class="gh-sechead">
      <p class="gh-kicker">Every topic</p>
      <h2 class="gh-h2" id="gh-topics-h">Shelved by the <em>point it teaches</em></h2>
      <p>The tenses first, in the order a learner meets them; then the passive, the modals, prepositions, conditionals and the rest, which sit alongside; then the skills built on all of it. Every lesson is a 16:9 deck that opens in the browser &mdash; the rule on the slide, then practice, then a speaking task, with a language switcher for the explanations.</p>
    </div>''')
    for title, group, note, cls in (
            ('Tenses', tense_topics, 'in teaching order &middot; the colour is the tense', 'gh-cards'),
            ('Grammar', grammar_topics, 'the points that sit alongside the tenses', 'gh-cards'),
            ('Skills', skill_topics, 'built on all of it', 'gh-plates')):
        gfiles = {r['file'] for t in group for r in allm[t['slug']]}
        b.append('    <div class="gh-group">\n      <div class="gh-group-h"><h3>%s</h3><span>%s &middot; %s</span></div>\n      <ul class="%s">'
                 % (title, plural(len(gfiles), 'lesson'), note, cls))
        for t in sorted(group, key=lambda x: x['order']):
            colour = tc.get(TOPIC_COLOUR.get(t['slug'], ''))
            b.append('        ' + _card(t, allm[t['slug']], images, colour))
        b.append('      </ul>\n    </div>')
    b.append('  </div>\n</section>')

    # ── two routes ──
    b.append('''<section class="gh-routes" id="routes" aria-labelledby="gh-routes-h">
  <div class="gh-wrap">
    <div class="gh-sechead">
      <p class="gh-kicker">Two routes through the tenses</p>
      <h2 class="gh-h2" id="gh-routes-h">Or climb them <em>in order</em></h2>
      <p>Two courses take the tenses one at a time, in teaching order, with a map that shows where you are. Both wear the colour code above.</p>
    </div>
    <ul class="gh-route-list">
      <li><a class="gh-route" href="sherpa-tensing-route-map.html">
        <img src="%s" alt="" loading="lazy" width="1200" height="672">
        <p class="gh-kicker">Sherpa Tensing &middot; %s</p>
        <h3>Thirteen camps up, nine back down</h3>
        <p>Every tense as a camp on the way up the mountain, in the active voice, then the same camps in the passive on the way down. <b>%s, %d free.</b></p>
        <span class="gh-route-go">Open the route map &rarr;</span>
      </a></li>
      <li><a class="gh-route" href="block-camp.html">
        <img src="%s" alt="" loading="lazy" width="1600" height="900">
        <p class="gh-kicker">Block Camp &middot; %s</p>
        <h3>The same trail, block by block</h3>
        <p>A voxel-built world: the tenses two parts each, the passive on the far side of the watchtower, and branching adventures with a grammar point built into the plot. <b>%s, %d free.</b></p>
        <span class="gh-route-go">Walk into camp &rarr;</span>
      </a></li>
    </ul>
  </div>
</section>''' % (esc(seo.quote(SHERPA_ART)), span(sherpa), plural(len(sherpa), 'lesson'), free_of(sherpa),
                esc(seo.quote(BLOCKCAMP_ART)), span(blockcamp), plural(len(blockcamp), 'lesson'), free_of(blockcamp)))

    # ── notes ──
    b.append('''<section class="gh-notes" aria-label="Notes">
  <div class="gh-wrap">
    <div class="gh-notes-grid">
      <div class="gh-note">
        <h3>Teaching this?</h3>
        <p>Every deck is built to be presented from: big type, one idea a slide, the rule stated before it is practised, and a speaking task at the end. Open a free one on the projector and see whether it suits your room before you pay for anything.</p>
        <p><a href="pricing.html">Plans &amp; what&rsquo;s free &rarr;</a></p>
      </div>
      <div class="gh-note">
        <h3>Looking for one lesson in particular?</h3>
        <p>The library lists every lesson on the site, filterable by level, topic and whether it is free, with a picture for each so a class can pick by eye. <strong>Exam English</strong> has its own landing page: <a href="ielts.html">IELTS Academic</a>, five routes in teaching order.</p>
        <p><a href="library.html">Open the library &rarr;</a></p>
      </div>
    </div>
  </div>
</section>''')

    # ── closing band ──
    b.append('''<section class="gh-close" aria-labelledby="gh-close-h">
  <img class="gh-close-art" src="%s" alt="" loading="lazy" width="1200" height="672">
  <div class="gh-close-in">
    <p class="gh-kicker">Not sure of your level?</p>
    <h2 class="gh-h2" id="gh-close-h">Six questions a level, <em>then a lesson</em></h2>
    <p>The Level Checker is free and adaptive: it tests the tenses from A1 up, stops when it knows, and names the lesson to open first.</p>
    <div class="gh-ctas">
      <a class="gh-btn" href="level-checker.html">Take the Level Checker</a>
      <a class="gh-btn gh-btn-quiet" href="#tenses">Back to the tenses</a>
    </div>
  </div>
</section>
</main>''' % esc(seo.quote(HERO)))

    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': '%s/index.html' % SITE},
            {'@type': 'ListItem', 'position': 2, 'name': 'Grammar', 'item': '%s/grammar.html' % SITE}]},
        {'@type': 'ItemList', 'name': 'English grammar topics',
         'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1,
              'url': '%s/%s' % (SITE, topics.hub_url(t['slug'])), 'name': t['name']}
             for i, t in enumerate(listed)]}]}
    gone = prune()
    print('  grammar.html: %d topics, %d lessons (%d free); tense squares: %s%s'
          % (len(listed), len(files), len(free_files),
             ' '.join('%s=%d' % (k, v) for k, v in cell_counts.items()),
             '; pruned %s' % ', '.join(gone) if gone else ''))
    return css(), '\n'.join(b), ld


# ── --palette and --check ─────────────────────────────────────────────
def palette():
    import subprocess
    from PIL import Image
    src = os.path.join(ROOT, HERO)
    tool = os.path.join(ROOT, 'lesson-template', 'extract-palette.py')
    for flag in (['--light'], []):
        print(subprocess.run([sys.executable, tool, src] + flag, capture_output=True,
                             text=True, encoding='utf-8').stdout)
    m = Image.open(src).convert('RGB').resize((600, 336))
    q = m.quantize(colors=8, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()
    print('/* art fields: MEDIANCUT 8 */')
    for c, i in sorted(q.getcolors(), reverse=True):
        print('  #%02x%02x%02x' % tuple(pal[i * 3:i * 3 + 3]))


def contrast_report():
    col = colours()
    bad = 0
    for fg, bg, need, what in CONTRAST:
        r = _ratio(col[fg], col[bg])
        ok = r >= need
        bad += not ok
        print('  %-14s on %-8s %5.2f:1 (min %.1f) %s  %s'
              % (fg, bg, r, need, 'PASS' if ok else 'FAIL', what))
    for key, (fill, ink) in tense_colours().items():
        r = _ratio(ink, fill)
        ok = r >= 4.5
        bad += not ok
        print('  %-26s %s on %s %5.2f:1 (min 4.5) %s' % (key, ink, fill, r, 'PASS' if ok else 'FAIL'))
    return bad


if __name__ == '__main__':
    if '--palette' in sys.argv:
        palette()
        sys.exit(0)
    failures = contrast_report()
    if failures:
        sys.exit('! %d contrast pair(s) fail' % failures)
    if '--check' not in sys.argv:
        print('  ok — build the page with: python tools/build_hubs.py')
