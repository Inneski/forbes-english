# -*- coding: utf-8 -*-
"""Build the IELTS landing page, `ielts.html`.

    python3 tools/build_ielts_hub.py            # all six IELTS pages; then tools/seo.py
    python3 tools/build_ielts_hub.py --check    # exit 1 if any of them is stale
    python3 tools/build_ielts_hub.py --palette  # re-derive the colours below

`tools/build_hubs.py` calls this too, so the normal pipeline keeps the page
current: add a lesson to `tools/ielts_routes.py`, run build_hubs, and the
landing page and its route page both pick it up with no hand edit.

WHY IT IS GENERATED. The page was hand-written, and every count on it went
stale in turn: Speaking said 1 lesson when there were 3 (fixed 2026-09-13),
then Reading said 3 on the card and 4 in the tag beside it. Nothing here is
typed twice any more:

- the routes' lessons, their order and their groups come from
  `tools/ielts_routes.py`, the source of truth for teaching order, which
  also builds the five route pages (`tools/build_ielts_routes.py`; until
  2026-09-25 this file parsed those pages, which were hand-written);
- Free or not comes from the catalogue (`seo.lessons()` — Supabase, or the
  cached `tools/lessons.json` when that is unreachable);
- each route's picture is the one its route page uses (same data);
- the Question Bank figures come from `tools/ielts_bank_data.py`.

WHAT IS NOT GENERATED. Everything in `ielts.html` outside the two fences is
hand-maintained, and two other builders depend on it: `tools/build_hubs.py`
and `tools/build_ielts_bank.py` lift the FIRST `<style>` block, the font
links and `<nav class="topband">` from this page to dress every grammar hub
and the Question Bank, and `tools/build_ielts_routes.py` lifts them for the
five route pages. So the old IELTS classes (.hero, .step, .track …) stay in
that first block even though no IELTS page uses them any more, and
everything this page needs lives in its own `ih-`-prefixed block, which the
lifters cannot see. Do not merge the two blocks. The route pages carry this
page's `ih-` block whole, so a change to it restyles them too.

THE PALETTE is derived from the pictures, not picked. `--palette` rebuilds
the recipe: every IELTS hero (`ielts-*/hero.jpg`, sorted) at 500x280 in a
6-wide montage, full rows only, then
    extract-palette.py <montage> --light   -> --ih-void … --ih-contrast
    extract-palette.py <montage>           -> --ih-ink …  (the dark bands)
    PIL MEDIANCUT, 8 colours               -> the art fields (--ih-sky …)
The art fields are fills and never carry small text unless the pairing is
in CONTRAST below, which `--check` measures.

COLOUR MEANS SOMETHING. Blue is the two papers you take in (Listening,
Reading); coral is the two you produce (Writing, Speaking); green is
vocabulary, which is marked inside the two coral ones. The test-to-scale
figure, the route numbers and the lesson lines all use the same code.
"""
import hashlib
import html
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo                                   # noqa: E402

ROOT = seo.ROOT
SITE = seo.SITE
PAGE = os.path.join(ROOT, 'ielts.html')
ART = 'ielts-hub'                            # web-sized derivatives live here

CSS_START, CSS_END = '<!-- IELTS-HUB-CSS:start -->', '<!-- IELTS-HUB-CSS:end -->'
BODY_START, BODY_END = '<!-- IELTS-HUB:start -->', '<!-- IELTS-HUB:end -->'

HERO_SRC = 'ielts-essay/hero.jpg'
HERO_ALT = ('Illustration of a flag on a hilltop under a tall pink-edged cloud, '
            'and far below it a lone figure walking up the slope towards it')
BANK_SRC = 'ielts-question-bank/hero.jpg'

# The routes, in order: number, name, colour family and the landing page's
# own copy. The lessons and each route page's copy are in
# tools/ielts_routes.py. Everything countable is counted from there.
ROUTES = [
    dict(key='writing', hub='ielts-writing.html', name='Writing', family='prod',
         meta='Task 1 &amp; Task 2',
         pitch='Task 1 comes first on the paper, so it comes first here &mdash; '
               'but Task 2 carries twice the marks, and that is where the hours '
               'should go. All five essay types, the two paragraphs that decide '
               'Task Achievement, band 9 models taken apart, and a timed studio '
               'that exports for marking.',
         pos='18% 50%'),
    dict(key='speaking', hub='ielts-speaking.html', name='Speaking', family='prod',
         meta='Parts 1, 2 &amp; 3 &middot; both modules',
         pitch='Eleven to fourteen minutes, three parts, one examiner, and the '
               'same test on both modules. Parts 1 and 2 first: answering at '
               'length without waffling, and filling the two minutes of the '
               'long turn, which is where most candidates come unstuck.',
         pos='40% 50%'),
    dict(key='listening', hub='ielts-listening.html', name='Listening', family='recv',
         meta='With recordings &middot; both modules',
         pitch='Every recording is played once, so reading the questions before '
               'the audio starts matters more than anything you do while it '
               'runs. The mechanics first, then the four sections, one lesson '
               'each, each playing its recording once as the test does &mdash; '
               'and a drills deck for numbers and spelling.',
         pos='40% 50%'),
    dict(key='reading', hub='ielts-reading.html', name='Reading', family='recv',
         meta='40 questions &middot; both modules',
         pitch='The question types are the same on both modules, and the '
               'difficulty is technique rather than vocabulary. True, False, '
               'Not Given first, because it is the type candidates find hardest '
               'to call: they answer from what they know instead of from what '
               'the passage says.',
         pos='60% 50%'),
    dict(key='vocabulary', hub='ielts-vocabulary.html', name='Vocabulary', family='lex',
         meta='Feeds Speaking &amp; Writing',
         pitch='Lexical Resource is a quarter of the Speaking mark and a quarter '
               'of the Writing mark. The descriptors ask for less common words '
               'used accurately, not rare ones: words you have to use, not '
               'words you have to read.',
         pos='55% 50%'),
]

# "Already know where the marks go?" — a symptom, and the lesson that answers
# it. Each line is paraphrased from that lesson's own description in
# tools/ielts_routes.py; keep it that way, so the promise is one the lesson keeps.
SYMPTOMS = [
    ('My Task 1 report keeps turning into an opinion.',
     'forbes-english-ielts-academic-writing-part1.html'),
    ('I never know what belongs in the overview.',
     'forbes-english-ielts-intro-overview-part7.html'),
    ('I can&rsquo;t tell which kind of essay the question wants.',
     'forbes-english-ielts-writing-lab-part2.html'),
    ('I know the shape of the essay and have nothing to say.',
     'ielts-question-bank.html'),
    ('I run dry forty seconds into the two-minute long turn.',
     'forbes-english-ielts-speaking-part1-2.html'),
    ('In Part 3 I answer about my own life, not the general case.',
     'forbes-english-ielts-speaking-part3.html'),
    ('I can&rsquo;t decide between False and Not Given.',
     'forbes-english-ielts-reading-tfng.html'),
    ('In Section 3 I lose track of who said what.',
     'forbes-english-ielts-listening-s3.html'),
    ('I hear the answer, then write it down wrong.',
     'forbes-english-ielts-listening-drills.html'),
    ('I know plenty of words, but my vocabulary band doesn&rsquo;t move.',
     'forbes-english-ielts-lexical-resource.html'),
]

# Text-on-fill pairs the page actually uses, measured by --check.
CONTRAST = [
    ('night', 'sky', 4.5, 'hero copy on the sky scrim, chooser copy'),
    ('accent-bright', 'sky', 3.0, 'hero H1 "Academic" (large)'),
    ('ink-text', 'slate-deep', 4.5, 'Listening block'),
    ('night', 'sky-deep', 4.5, 'Reading block'),
    ('ink-text', 'accent', 4.5, 'Writing block, Free pills, free dots'),
    ('night', 'coral', 4.5, 'Speaking block'),
    ('text', 'paper', 4.5, 'body copy'),
    ('text', 'card', 4.5, 'lesson titles in the routes'),
    ('text-dim', 'paper', 4.5, 'secondary copy'),
    ('text-dim', 'card', 4.5, 'secondary copy on cards and in the routes'),
    ('accent', 'paper', 4.5, 'kickers'),
    ('accent', 'card', 4.5, 'routes kicker; Writing/Speaking numbers and lines'),
    ('slate-deep', 'card', 4.5, 'Listening/Reading numbers and lines, scale key'),
    ('contrast', 'card', 4.5, 'Vocabulary number and line'),
    ('contrast', 'paper', 4.5, 'brace label'),
    ('ink-text', 'ink', 4.5, 'closing band'),
    ('ink-text-dim', 'ink', 4.5, 'closing band secondary'),
    ('ink-accent', 'ink', 4.5, 'closing band kicker'),
    ('ink-accent', 'night', 4.5, 'Question Bank kicker'),
    ('ink-text-dim', 'night', 4.5, 'Question Bank copy'),
    # Focus rings: WCAG 1.4.11 wants 3:1 against what the ring sits on.
    ('accent', 'paper', 3.0, 'focus ring on paper'),
    ('accent', 'card', 3.0, 'focus ring in the routes'),
    ('night', 'sky', 3.0, 'focus ring in the hero and the chooser'),
    ('ink-accent', 'ink', 3.0, 'focus ring on the closing band'),
]

PALETTE = {
    # extract-palette.py <montage> --light
    'void': '#d8c6ac', 'surface': '#e1d6c4', 'surface2': '#dccdb8',
    'border': '#965c4a', 'text': '#2a1711', 'text-dim': '#5e392e',
    'accent': '#ac2f0a', 'accent-bright': '#821e01', 'accent-dim': '#e56e4b',
    'secondary': '#38505a', 'contrast': '#095340',
    # extract-palette.py <montage>
    'ink': '#0b0e0b', 'ink-surface': '#161a16', 'ink-surface2': '#1f251f',
    'ink-border': '#a87a6c', 'ink-text': '#f5f3f2', 'ink-text-dim': '#bfaaa3',
    'ink-accent': '#e2a998',
    # the montage quantised (MEDIANCUT, 8), most to least common
    'sky': '#a7b8b7', 'sky-deep': '#89a5ac', 'night': '#121510',
    'slate-deep': '#3f4b4e', 'cream': '#cfc8bb', 'coral': '#bd8b7d',
    'slate': '#627c85', 'rose': '#beaba2',
}
# Mixed, not picked: the page paper and the card, lifted from the derived
# surface towards the derived light text. Resolved here so --check can
# measure them; the CSS spells out the same color-mix().
MIX = {'paper': ('surface', 'ink-text', 0.62), 'card': ('surface', 'ink-text', 0.30)}


def esc(s):
    return html.escape(s, quote=True)


WORDS = ('zero one two three four five six seven eight nine ten eleven twelve '
         'thirteen fourteen fifteen sixteen seventeen eighteen nineteen').split()
TENS = 'twenty thirty forty fifty sixty seventy eighty ninety'.split()


def words(n):
    if n < 20:
        return WORDS[n]
    t, u = divmod(n, 10)
    return TENS[t - 2] + ('-' + WORDS[u] if u else '')


def plural(n, one, many=None):
    return one if n == 1 else (many or one + 's')


LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']


def level_span(levels):
    """'C1', or 'B2&ndash;C1': from the lowest level any lesson starts at to
    the highest any reaches. A level may itself be a span ('B2-C1')."""
    lo = hi = None
    for l in levels:
        ix = [LEVELS.index(x) for x in re.findall(r'[ABC][12]', l or '')]
        if ix:
            lo = min(ix) if lo is None else min(lo, min(ix))
            hi = max(ix) if hi is None else max(hi, max(ix))
    if lo is None:
        return ''
    return LEVELS[lo] if lo == hi else '%s&ndash;%s' % (LEVELS[lo], LEVELS[hi])


# ── the routes' lessons ───────────────────────────────────────────────
def short_title(t):
    """'IELTS Academic Writing: The Report' -> 'The Report', here and on
    the route pages."""
    return re.sub(r'^IELTS [^:]+:\s*', '', t.strip())


def read_route(r):
    """The route's lessons and picture, from tools/ielts_routes.py — the
    same data the route pages are built from."""
    from ielts_routes import ROUTES as DATA
    d = next((x for x in DATA if x['hub'] == r['hub']), None)
    if d is None:
        sys.exit('! %s is not in tools/ielts_routes.py' % r['hub'])
    groups = [dict(h=t['h'], stops=[dict(file=l['file'], title=short_title(l['title']))
                                    for l in t['lessons']])
              for t in d['tracks'] if t['lessons']]
    if not groups:
        sys.exit('! %s: no lessons in tools/ielts_routes.py' % r['hub'])
    return dict(r, art=d['art'], art_alt=d['art_alt'], groups=groups,
                stops=[s for g in groups for s in g['stops']])


def produces(f):
    """Does the deck end with the learner producing language? The house
    activation stage is a data-type="activate" slide; the Writing Studio is
    nothing but textareas. Two older Writing decks have neither, and the
    page says so rather than claiming every lesson does."""
    p = os.path.join(ROOT, f)
    if not os.path.exists(p):
        return True
    src = open(p, encoding='utf-8', errors='ignore').read()
    return 'data-type="activate"' in src or '<textarea' in src


def load(rows):
    """The five routes, each lesson annotated with access and position."""
    cat = {x['file']: x for x in rows}
    routes, missing = [], []
    for r in ROUTES:
        r = read_route(r)
        for i, s in enumerate(r['stops']):
            row = cat.get(s['file'])
            if row is None:
                missing.append(s['file'])
            s.update(n=i + 1, free=bool(row) and row.get('access') != 'pro',
                     level=(row or {}).get('level') or '',
                     full=seo.clean(row['title'] if row else s['title']),
                     produces=produces(s['file']), route=r)
        routes.append(r)
    for f in missing:
        print('  ! %s is on a route page but not in the catalogue; shown as '
              'subscriber-only' % f)
    return routes


def facts(routes):
    """The claims the copy makes about the whole set, measured, not assumed."""
    stops = [s for r in routes for s in r['stops']]
    f = dict(total=len(stops), free=sum(1 for s in stops if s['free']),
             firsts=all(r['stops'][0]['free'] for r in routes),
             silent=[s for s in stops if not s['produces']])
    if not f['firsts']:
        print('  ! the first lesson is not free on: %s — the page copy adapts, '
              'but tools/seo.py, index.html and library.html still say it is'
              % ', '.join(r['name'] for r in routes if not r['stops'][0]['free']))
    return f


def bank_numbers():
    from ielts_bank_data import TOPICS, TYPES
    return (sum(len(t['prompts']) for t in TOPICS), len(TOPICS),
            [v[0] for v in TYPES.values()])


# ── pictures ──────────────────────────────────────────────────────────
# Every derived picture is named <stem>-<hash>.jpg, the hash taken over its
# inputs (source bytes and settings). Change a route's picture, or
# re-render a hero, and the name changes, so the HTML changes, --check says
# STALE, and a rebuild writes the new file and deletes the superseded one.
# The route pages use the same files, which is why the six IELTS pages are
# always built together (build_ielts_routes.build_all).
# (Fixed names would keep serving the old picture with nothing to notice.)
# PIL's JPEG encoder is deterministic, so the same inputs give the same
# bytes on any machine and a rebuild makes no diff.
STATE = {'check': False, 'missing': []}


def _sha(*parts):
    h = hashlib.sha1()
    for p in parts:
        h.update(p if isinstance(p, bytes) else str(p).encode('utf-8'))
    return h.hexdigest()[:8]


def _emit(stem, key, make):
    """Return the published path for <stem>-<key>.jpg, writing it with
    make(path) if absent and pruning older <stem>-*.jpg. In check mode,
    write and delete nothing; record a missing file as stale."""
    out = '%s/%s-%s.jpg' % (ART, stem, key)
    path = os.path.join(ROOT, out)
    if os.path.exists(path):
        return out
    if STATE['check']:
        STATE['missing'].append(out)
        return out
    os.makedirs(os.path.dirname(path), exist_ok=True)
    make(path)
    print('  wrote %s (%d KB)' % (out, os.path.getsize(path) // 1024))
    for old in os.listdir(os.path.join(ROOT, ART)):
        if re.fullmatch(re.escape(stem) + r'-[0-9a-f]{8}\.jpg', old) and old != os.path.basename(path):
            os.remove(os.path.join(ROOT, ART, old))
            print('  removed superseded %s/%s' % (ART, old))
    return out


def derive(src, stem, width, quality=80):
    """A web-sized copy of `src` in ielts-hub/."""
    data = open(os.path.join(ROOT, src), 'rb').read()

    def make(path):
        from PIL import Image
        im = Image.open(io.BytesIO(data)).convert('RGB')
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        im.save(path, 'JPEG', quality=quality, optimize=True, progressive=True)
    return _emit(stem, _sha(data, width, quality), make)


def mosaic(routes, images):
    """Every lesson's picture, in route order, as one image for the closing
    band. One request instead of two dozen."""
    files = [images.get(s['file']) for r in routes for s in r['stops']]
    # The illustrated series only. Four Writing lessons still carry the
    # older, darker covers in IELTS/, which read as a different set.
    files = [f for f in files if f and re.match(r'ielts-[^/]+/hero\.jpg$', f)
             and os.path.exists(os.path.join(ROOT, f))]
    if not files:
        return None
    cols, w, h = 8, 320, 180
    datas = [open(os.path.join(ROOT, f), 'rb').read() for f in files]

    def make(path):
        from PIL import Image
        rows_n = -(-len(files) // cols)
        m = Image.new('RGB', (cols * w, rows_n * h), PALETTE['ink'])
        for i, d in enumerate(datas):
            im = Image.open(io.BytesIO(d)).convert('RGB')
            im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            top = max(0, (im.height - h) // 2)
            m.paste(im.crop((0, top, w, top + h)), ((i % cols) * w, (i // cols) * h))
        m.save(path, 'JPEG', quality=72, optimize=True, progressive=True)
    return _emit('series', _sha(cols, w, h, *files, *datas), make)


# ── the page ──────────────────────────────────────────────────────────
def css():
    v = '\n'.join('  --ih-%s: %s;' % (k, c) for k, c in PALETTE.items())
    return CSS.replace('/*PALETTE*/', v)


CSS = r"""<style id="ielts-hub-css">
/* The IELTS landing page. Generated by tools/build_ielts_hub.py — edit it
   there. Colours: see that file's docstring. Every class is ih- prefixed so
   nothing here collides with the shared block above, which other pages
   inherit. */
body.ih {
/*PALETTE*/
  --ih-paper: color-mix(in srgb, var(--ih-surface) 62%, var(--ih-ink-text));
  --ih-card:  color-mix(in srgb, var(--ih-surface) 30%, var(--ih-ink-text));
  --ih-line:  color-mix(in srgb, var(--ih-border) 34%, transparent);
  --ih-shadow: color-mix(in srgb, var(--ih-night) 18%, transparent);
  --ih-recv:  var(--ih-slate-deep);
  --ih-prod:  var(--ih-accent);
  --ih-lex:   var(--ih-contrast);
  --ih-max: 1240px;
  --ih-gut: clamp(16px, 4vw, 48px);
  background: var(--ih-paper);
  color: var(--ih-text);
  font-variant-numeric: lining-nums;
}
:where(.ih) a { color: inherit; }
.ih :where(main) a:focus-visible { outline: 3px solid var(--ih-accent); outline-offset: 3px; }
.ih-hero a:focus-visible, .ih-diag a:focus-visible { outline-color: var(--ih-night); }
.ih-close a:focus-visible { outline-color: var(--ih-ink-accent); }
.ih-vh { position: absolute; width: 1px; height: 1px; margin: -1px; padding: 0; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
.ih-wrap { max-width: var(--ih-max); margin: 0 auto; padding: 0 var(--ih-gut); }
.ih-kicker {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .16em; text-transform: uppercase; font-size: .8rem;
  color: var(--ih-accent); margin: 0 0 12px;
}
.ih-h2 {
  font-family: 'Playfair Display', serif; font-weight: 900;
  font-size: clamp(2.1rem, 4.6vw, 3.4rem); line-height: 1.02; letter-spacing: -.012em;
  margin: 0 0 16px; color: var(--ih-text); text-wrap: balance;
}
.ih-sechead { max-width: 64ch; }
.ih-sechead p { font-size: 1.1rem; line-height: 1.62; color: var(--ih-text-dim); margin: 0; }
.ih-btn {
  display: inline-flex; align-items: center; gap: .5em;
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .09em; text-transform: uppercase; font-size: .92rem;
  text-decoration: none; padding: 13px 22px; border-radius: 999px;
  background: var(--ih-night); color: var(--ih-ink-text);
  border: 2px solid var(--ih-night);
  transition: background .18s ease, border-color .18s ease, transform .18s ease;
}
.ih-btn:hover { background: var(--ih-accent-bright); border-color: var(--ih-accent-bright); transform: translateY(-1px); }
.ih-btn-quiet { background: transparent; color: var(--ih-night); }
.ih-btn-quiet:hover { background: var(--ih-night); color: var(--ih-ink-text); border-color: var(--ih-night); }
.ih-btn-sm { padding: 10px 18px; font-size: .84rem; }
.ih-pill {
  display: inline-block; font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .1em; text-transform: uppercase; font-size: .68rem; line-height: 1;
  padding: 4px 8px 3px; border-radius: 999px; white-space: nowrap;
  background: var(--ih-accent); color: var(--ih-ink-text);
}

/* ── hero ── */
.ih-hero {
  position: relative; isolation: isolate; overflow: hidden;
  min-height: clamp(580px, 86vh, 820px); display: grid; align-items: start;
  background: var(--ih-sky);
}
.ih-hero-img {
  position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%;
  object-fit: cover; object-position: 30% 62%;
  animation: ih-settle 2.6s cubic-bezier(.2,.7,.2,1) backwards;
}
@keyframes ih-settle { from { transform: scale(1.07); } to { transform: none; } }
.ih-hero::after {
  content: ''; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(90deg, transparent 32%,
    color-mix(in srgb, var(--ih-sky) 60%, transparent) 56%,
    color-mix(in srgb, var(--ih-sky) 82%, transparent) 100%);
}
.ih-hero-in {
  width: 100%; max-width: var(--ih-max); margin: 0 auto;
  padding: clamp(40px, 7vh, 80px) var(--ih-gut) 48px;
  display: grid; grid-template-columns: 1fr minmax(0, 580px);
}
.ih-hero-copy { grid-column: 2; color: var(--ih-night); }
.ih-hero .ih-kicker { color: var(--ih-night); }
.ih-h1 {
  font-family: 'Playfair Display', serif; font-weight: 900;
  font-size: clamp(3.3rem, min(7.6vw, 11vh), 6.4rem); line-height: .92; letter-spacing: -.022em;
  margin: 0 0 22px; color: var(--ih-night);
}
.ih-h1 em { display: block; font-style: normal; color: var(--ih-accent-bright); }
.ih-lede { font-size: clamp(1.08rem, 1.5vw, 1.22rem); line-height: 1.58; margin: 0 0 24px; max-width: 34em; text-wrap: pretty; }
.ih-stats {
  list-style: none; margin: 0 0 30px; padding: 16px 0 0; display: flex; flex-wrap: wrap; gap: 14px 30px;
  border-top: 1px solid color-mix(in srgb, var(--ih-night) 30%, transparent);
}
.ih-stats li { display: flex; align-items: baseline; gap: 8px; }
.ih-stats b {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 800; font-size: 2.5rem; line-height: .9;
}
.ih-stats span { font-size: .95rem; line-height: 1.3; max-width: 16em; text-wrap: balance; }
.ih-stats .ih-stat-free b { color: var(--ih-accent-bright); }
.ih-ctas { display: flex; flex-wrap: wrap; gap: 12px; }
@media (max-width: 880px) {
  .ih-hero { display: block; min-height: 0; background: var(--ih-paper); }
  .ih-hero-img { position: relative; z-index: auto; height: auto; aspect-ratio: 16 / 10; object-position: 22% 60%; }
  .ih-hero::after { display: none; }
  .ih-hero-in { grid-template-columns: 1fr; padding-top: 30px; padding-bottom: 44px; }
  .ih-hero-copy { grid-column: 1; }
}

/* ── the test, to scale ── */
.ih-test { padding: clamp(64px, 9vw, 124px) 0 clamp(56px, 8vw, 104px); }
.ih-scale {
  margin: clamp(34px, 5vw, 52px) 0 0;
  display: grid; column-gap: 5px; row-gap: 12px;
  grid-template-columns: 30fr 10fr 60fr 60fr 7fr 14fr;
}
.ih-seg {
  container-type: inline-size; position: relative; overflow: hidden;
  min-height: clamp(168px, 17vw, 214px); border-radius: 12px; padding: 14px 14px 13px;
  display: flex; flex-direction: column; justify-content: space-between; gap: 8px;
  text-decoration: none;
  transition: transform .2s ease, box-shadow .2s ease;
  animation: ih-grow .9s cubic-bezier(.2,.7,.2,1) backwards; transform-origin: left center;
}
.ih-seg:nth-child(2) { animation-delay: .06s; } .ih-seg:nth-child(3) { animation-delay: .12s; }
.ih-seg:nth-child(4) { animation-delay: .18s; } .ih-seg:nth-child(6) { animation-delay: .26s; }
@keyframes ih-grow { from { transform: scaleX(.2); opacity: 0; } to { transform: none; opacity: 1; } }
a.ih-seg:hover { transform: translateY(-4px); box-shadow: 0 16px 30px var(--ih-shadow); }
.ih-seg-name {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .12em; text-transform: uppercase; font-size: .8rem; line-height: 1.1;
}
.ih-seg-min {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 800; line-height: .86;
  font-size: clamp(1.25rem, 34cqi, 2.8rem); letter-spacing: -.01em; white-space: nowrap;
}
.ih-seg-min small { font-size: .34em; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; margin-left: .25em; }
.ih-seg-fact { font-size: .84rem; line-height: 1.35; margin: 0; }
.ih-seg-l { background: var(--ih-slate-deep); color: var(--ih-ink-text); }
.ih-seg-r { background: var(--ih-sky-deep); color: var(--ih-night); }
.ih-seg-w { background: var(--ih-accent); color: var(--ih-ink-text); padding: 0; flex-direction: row; gap: 0; }
.ih-seg-s {
  color: var(--ih-night); padding: 14px 10px 13px;
  background: linear-gradient(90deg, var(--ih-coral) 0 78%, color-mix(in srgb, var(--ih-coral) 45%, transparent) 78%);
}
.ih-seg-x {
  color: var(--ih-text); border: 2px dashed color-mix(in srgb, var(--ih-slate-deep) 55%, transparent);
  background: repeating-linear-gradient(135deg,
    color-mix(in srgb, var(--ih-slate-deep) 16%, transparent) 0 6px, transparent 6px 12px);
  padding: 12px 8px; animation-delay: .03s;
}
.ih-seg-x .ih-seg-min { font-size: clamp(1rem, 36cqi, 2rem); }
.ih-seg-x .ih-seg-fact { font-size: .74rem; }
.ih-task {
  container-type: inline-size; flex: 0 0 calc(var(--m) * 100% / 60); min-width: 0; padding: 14px 14px 13px;
  display: flex; flex-direction: column; justify-content: space-between; gap: 8px;
}
.ih-task + .ih-task { border-left: 2px dashed color-mix(in srgb, var(--ih-ink-text) 55%, transparent); }
.ih-seg-s .ih-seg-min { font-size: clamp(1.1rem, 40cqi, 2.8rem); }
.ih-gap { align-self: stretch; min-height: clamp(168px, 17vw, 214px); position: relative; }
.ih-gap::before {
  content: ''; position: absolute; left: 50%; top: 10px; bottom: 10px;
  border-left: 2px dotted color-mix(in srgb, var(--ih-text) 45%, transparent);
}
.ih-brace {
  grid-column: 4 / 7; position: relative; padding: 14px 4px 0;
  border-top: 3px solid var(--ih-lex); text-decoration: none; color: var(--ih-text);
  font-size: .95rem; line-height: 1.45;
}
.ih-brace::before, .ih-brace::after {
  content: ''; position: absolute; top: -12px; width: 3px; height: 12px; background: var(--ih-lex);
}
.ih-brace::before { left: 0; } .ih-brace::after { right: 0; }
.ih-brace b { color: var(--ih-lex); font-family: 'Barlow Condensed', sans-serif; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; font-size: .86rem; margin-right: .4em; }
.ih-brace:hover span { text-decoration: underline; text-underline-offset: 3px; }
.ih-scale-note { grid-column: 1 / 4; font-size: .9rem; line-height: 1.5; color: var(--ih-text-dim); margin: 0; padding-top: 14px; }
.ih-keyed { white-space: nowrap; }
.ih-key { display: inline-block; width: 1.3em; height: .8em; border-radius: 2px; vertical-align: -.05em; margin: 0 .3em 0 .1em; }
.ih-key-recv { background: linear-gradient(90deg, var(--ih-slate-deep) 50%, var(--ih-sky-deep) 50%); }
.ih-key-prod { background: linear-gradient(90deg, var(--ih-accent) 50%, var(--ih-coral) 50%); }
/* Stacked: a block per row, its HEIGHT the paper's length at 4px a minute.
   The horizontal layout needs about 1040px before the Speaking column can
   hold its own name; below that it clipped, so it stacks instead. */
@media (max-width: 1040px) {
  .ih-scale { grid-template-columns: 1fr; row-gap: 5px; }
  .ih-seg, .ih-task { min-height: calc(var(--m) * 4px); padding-top: 10px; padding-bottom: 10px; }
  .ih-seg { flex-direction: row; align-items: flex-end; justify-content: space-between; gap: 16px; transform-origin: top center; }
  .ih-seg > div:not(.ih-task), .ih-task > div { display: grid; gap: 4px; align-content: start; align-self: stretch; }
  .ih-seg-min { font-size: 2.4rem; text-align: right; }
  .ih-seg-w { flex-direction: column; align-items: stretch; gap: 0; padding: 0; }
  .ih-task { flex: none; flex-direction: row; align-items: flex-end; justify-content: space-between; gap: 16px; }
  .ih-task + .ih-task { border-left: 0; border-top: 2px dashed color-mix(in srgb, var(--ih-ink-text) 55%, transparent); }
  .ih-task .ih-seg-min { font-size: 2.4rem; }
  .ih-seg-x { padding: 8px 14px; align-items: center; }
  .ih-seg-x .ih-seg-min { font-size: 1.5rem; }
  .ih-seg-x .ih-seg-fact { font-size: .84rem; }
  .ih-seg-s .ih-seg-min { font-size: 2rem; }
  .ih-gap { min-height: 18px; }
  .ih-gap::before { left: 20px; right: 20px; top: 50%; bottom: auto; border-left: 0; border-top: 2px dotted color-mix(in srgb, var(--ih-text) 45%, transparent); }
  .ih-seg-s { background: linear-gradient(180deg, var(--ih-coral) 0 78%, color-mix(in srgb, var(--ih-coral) 45%, transparent) 78%); }
  .ih-brace, .ih-scale-note { grid-column: 1; }
  .ih-brace { margin-top: 14px; }
  @keyframes ih-grow { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
}

/* ── routes ── */
.ih-routes { padding: clamp(64px, 9vw, 120px) 0 clamp(40px, 6vw, 80px); background: var(--ih-card); border-top: 1px solid var(--ih-line); }
.ih-routes-head { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 400px); gap: 28px clamp(32px, 6vw, 96px); align-items: end; margin-bottom: clamp(8px, 2vw, 20px); }
.ih-routes-head .ih-sechead p + p { margin-top: 12px; }
.ih-jump { list-style: none; margin: 0; padding: 0; border-top: 2px solid var(--ih-text); }
.ih-jump li { --ih-route: var(--ih-prod); }
.ih-jump li[data-family="recv"] { --ih-route: var(--ih-recv); }
.ih-jump li[data-family="lex"] { --ih-route: var(--ih-lex); }
.ih-jump a {
  display: grid; grid-template-columns: 44px 1fr auto; align-items: baseline; gap: 12px;
  padding: 11px 2px; border-bottom: 1px solid var(--ih-line); text-decoration: none;
}
.ih-jump-n { font-family: 'Barlow Condensed', sans-serif; font-weight: 800; font-size: 1.5rem; line-height: 1; color: var(--ih-route); }
.ih-jump-name { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.24rem; }
.ih-jump-c { font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; font-size: .78rem; color: var(--ih-text-dim); }
.ih-jump a:hover .ih-jump-name { text-decoration: underline; text-decoration-color: var(--ih-route); text-decoration-thickness: 2px; text-underline-offset: 4px; }
@media (max-width: 980px) { .ih-routes-head { grid-template-columns: 1fr; } }
.ih-route {
  --ih-route: var(--ih-prod);
  display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr);
  gap: clamp(26px, 4.4vw, 68px); align-items: stretch;
  padding: clamp(40px, 5.4vw, 72px) 0; border-bottom: 1px solid var(--ih-line);
  scroll-margin-top: 12px;
}
.ih-route:last-child { border-bottom: 0; }
.ih-route[data-family="recv"] { --ih-route: var(--ih-recv); }
.ih-route[data-family="lex"] { --ih-route: var(--ih-lex); }
.ih-route:nth-of-type(even) .ih-route-art { order: 2; }
.ih-route-art {
  position: relative; display: block; min-height: 380px; border-radius: 16px; overflow: hidden;
  box-shadow: 0 22px 48px var(--ih-shadow); background: var(--ih-sky);
}
.ih-route-art img {
  position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;
  transition: transform 1.4s cubic-bezier(.2,.7,.2,1);
}
.ih-route:hover .ih-route-art img { transform: scale(1.045); }
.ih-route-head { display: flex; align-items: flex-end; gap: 18px; margin-bottom: 18px; }
.ih-route-num {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 800; line-height: .78;
  font-size: clamp(3.6rem, 6.4vw, 5.6rem); color: var(--ih-route); letter-spacing: -.02em;
}
.ih-route-meta {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .12em;
  text-transform: uppercase; font-size: .8rem; color: var(--ih-text-dim); margin: 0 0 4px;
}
.ih-route-name {
  font-family: 'Playfair Display', serif; font-weight: 900; line-height: 1;
  font-size: clamp(2.3rem, 4.2vw, 3.3rem); margin: 0;
}
.ih-route-name a { text-decoration: none; }
.ih-route-name a:hover { text-decoration: underline; text-decoration-color: var(--ih-route); text-decoration-thickness: 3px; text-underline-offset: 6px; }
.ih-route-pitch { font-size: 1.05rem; line-height: 1.64; color: var(--ih-text-dim); margin: 0 0 24px; max-width: 60ch; }
.ih-groups { display: grid; gap: 18px 36px; margin-bottom: 26px; }
.ih-groups.ih-two { grid-template-columns: 1fr 1fr; }
.ih-group-h {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .12em; line-height: 1.3;
  text-transform: uppercase; font-size: .76rem; color: var(--ih-text-dim); margin: 0 0 6px 40px;
}
.ih-stops { list-style: none; margin: 0; padding: 0; position: relative; }
.ih-stops::before {
  content: ''; position: absolute; left: 13px; top: 20px; bottom: 20px; width: 2px;
  background: color-mix(in srgb, var(--ih-route) 50%, transparent);
}
.ih-stop a {
  display: grid; grid-template-columns: 28px minmax(0, 1fr); gap: 12px; align-items: center;
  padding: 6px 8px 6px 0; text-decoration: none; border-radius: 8px;
}
.ih-dot {
  position: relative; z-index: 1; width: 28px; height: 28px; border-radius: 50%;
  display: grid; place-items: center; background: var(--ih-card);
  border: 2px solid var(--ih-route); color: var(--ih-text);
  font-family: 'Barlow Condensed', sans-serif; font-weight: 800; font-size: .86rem;
  transition: background .15s ease, color .15s ease, transform .15s ease;
}
.ih-free .ih-dot { background: var(--ih-accent); border-color: var(--ih-accent); color: var(--ih-ink-text); }
.ih-stop-t { font-size: .99rem; line-height: 1.32; }
.ih-stop-t .ih-pill { margin-left: 6px; vertical-align: 2px; }
.ih-stop a:hover .ih-stop-t { text-decoration: underline; text-decoration-color: var(--ih-route); text-decoration-thickness: 2px; text-underline-offset: 3px; }
.ih-stop a:hover .ih-dot { transform: scale(1.12); }
.ih-route-go { display: flex; flex-wrap: wrap; align-items: center; gap: 12px 22px; }
.ih-textlink {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .09em;
  text-transform: uppercase; font-size: .86rem; text-decoration: none;
  border-bottom: 2px solid var(--ih-route); padding-bottom: 2px;
}
.ih-textlink:hover { color: var(--ih-accent-bright); }
@media (max-width: 900px) {
  .ih-route { grid-template-columns: 1fr; }
  .ih-route:nth-of-type(even) .ih-route-art { order: 0; }
  .ih-route-art { min-height: 0; aspect-ratio: 16 / 9; }
}
@media (max-width: 620px) { .ih-groups.ih-two { grid-template-columns: 1fr; } }

/* ── already know where the marks go ── */
.ih-diag { background: var(--ih-sky); color: var(--ih-night); padding: clamp(64px, 9vw, 120px) 0; }
.ih-diag .ih-kicker, .ih-diag .ih-h2 { color: var(--ih-night); }
.ih-diag .ih-sechead p { color: var(--ih-night); }
.ih-qs { list-style: none; margin: clamp(30px, 4vw, 44px) 0 0; padding: 0; display: grid; grid-template-columns: 1fr 1fr; column-gap: clamp(28px, 4.4vw, 64px); }
.ih-q a {
  display: grid; gap: 8px; align-content: start; padding: 20px 0 20px; text-decoration: none; height: 100%;
  border-top: 1px solid color-mix(in srgb, var(--ih-night) 26%, transparent);
}
.ih-q-said {
  font-family: 'Playfair Display', serif; font-weight: 700; font-size: clamp(1.1rem, 1.7vw, 1.3rem);
  line-height: 1.3; text-wrap: pretty;
}
.ih-q-said::before { content: '\201C'; } .ih-q-said::after { content: '\201D'; }
.ih-q-go { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 10px; font-size: .95rem; }
.ih-q-where {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .1em; text-transform: uppercase; font-size: .78rem;
}
.ih-q-title { font-weight: 700; }
.ih-q a:hover .ih-q-title { text-decoration: underline; text-underline-offset: 3px; }
.ih-q a:hover .ih-q-arrow { transform: translateX(4px); }
.ih-q-arrow { display: inline-block; transition: transform .15s ease; }
@media (max-width: 760px) { .ih-qs { grid-template-columns: 1fr; } }

/* ── question bank ── */
.ih-bank { padding: clamp(64px, 9vw, 120px) 0 0; }
.ih-bank-card {
  display: grid; grid-template-columns: minmax(0, 6fr) minmax(0, 5fr);
  border-radius: 18px; overflow: hidden; text-decoration: none;
  background: var(--ih-night); color: var(--ih-ink-text);
  box-shadow: 0 24px 54px var(--ih-shadow);
}
.ih-bank-art { position: relative; min-height: 360px; }
.ih-bank-art img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 48% 70%; transition: transform 1.4s cubic-bezier(.2,.7,.2,1); }
.ih-bank-card:hover .ih-bank-art img { transform: scale(1.04); }
.ih-bank-copy { padding: clamp(28px, 4vw, 52px); display: flex; flex-direction: column; justify-content: center; gap: 14px; }
.ih-bank-copy .ih-kicker { color: var(--ih-ink-accent); margin: 0; }
.ih-bank-copy h2 { font-family: 'Playfair Display', serif; font-weight: 900; font-size: clamp(2rem, 3.6vw, 2.8rem); line-height: 1.04; margin: 0; color: var(--ih-ink-text); }
.ih-bank-copy p { margin: 0; line-height: 1.6; color: var(--ih-ink-text-dim); font-size: 1.02rem; }
.ih-bank-copy p b { color: var(--ih-ink-text); }
.ih-types { display: flex; flex-wrap: wrap; gap: 6px; list-style: none; margin: 0; padding: 0; }
.ih-types li {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .08em;
  text-transform: uppercase; font-size: .74rem; padding: 5px 10px; border-radius: 999px;
  border: 1px solid color-mix(in srgb, var(--ih-ink-text) 30%, transparent);
}
.ih-bank-copy .ih-btn { align-self: flex-start; margin-top: 6px; background: var(--ih-ink-text); border-color: var(--ih-ink-text); color: var(--ih-night); }
.ih-bank-card:hover .ih-btn { background: var(--ih-ink-accent); border-color: var(--ih-ink-accent); }
@media (max-width: 860px) {
  .ih-bank-card { grid-template-columns: 1fr; }
  .ih-bank-art { min-height: 0; aspect-ratio: 16 / 9; }
}

/* ── notes ── */
.ih-notes { padding: clamp(40px, 6vw, 72px) 0 clamp(64px, 9vw, 112px); }
.ih-notes-grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(16px, 2.4vw, 28px); }
.ih-note { background: var(--ih-card); border: 1px solid var(--ih-line); border-radius: 16px; padding: clamp(22px, 3vw, 34px); }
.ih-note h3 { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.36rem; margin: 0 0 10px; color: var(--ih-text); }
.ih-note p { margin: 0; line-height: 1.64; color: var(--ih-text-dim); }
.ih-note p + p { margin-top: 10px; }
.ih-note strong, .ih-note em { color: var(--ih-text); font-weight: 700; font-style: normal; }
@media (max-width: 760px) { .ih-notes-grid { grid-template-columns: 1fr; } }

/* ── closing band ── */
.ih-close { position: relative; isolation: isolate; overflow: hidden; background: var(--ih-ink); color: var(--ih-ink-text); }
.ih-close-art { position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; object-fit: cover; }
.ih-close::after {
  content: ''; position: absolute; inset: 0; z-index: -1;
  background: radial-gradient(ellipse 70% 90% at 50% 50%, color-mix(in srgb, var(--ih-ink) 93%, transparent) 30%, color-mix(in srgb, var(--ih-ink) 62%, transparent) 100%);
}
.ih-close-in { padding: clamp(72px, 10vw, 140px) var(--ih-gut); max-width: 860px; margin: 0 auto; text-align: center; }
.ih-close .ih-kicker { color: var(--ih-ink-accent); }
.ih-close .ih-h2 { color: var(--ih-ink-text); }
.ih-close p { font-size: 1.1rem; line-height: 1.62; color: var(--ih-ink-text-dim); margin: 0 auto 30px; max-width: 54ch; }
.ih-close .ih-ctas { justify-content: center; }
.ih-close .ih-btn { background: var(--ih-ink-text); border-color: var(--ih-ink-text); color: var(--ih-ink); }
.ih-close .ih-btn:hover { background: var(--ih-ink-accent); border-color: var(--ih-ink-accent); }
.ih-close .ih-btn-quiet { background: transparent; color: var(--ih-ink-text); border-color: color-mix(in srgb, var(--ih-ink-text) 55%, transparent); }
.ih-close .ih-btn-quiet:hover { background: var(--ih-ink-text); color: var(--ih-ink); }

@media (prefers-reduced-motion: reduce) {
  .ih *, .ih *::before, .ih *::after { animation: none !important; transition: none !important; }
}
</style>"""


def hero(routes, f):
    free_line = ('free &mdash; the first lesson on every route' if f['firsts'] and f['free'] == len(routes)
                 else 'free, including the first lesson on every route' if f['firsts']
                 else 'free, no sign-in')
    return """<header class="ih-hero" aria-labelledby="ih-h1">
  <img class="ih-hero-img" src="%(hero)s" srcset="%(hero_sm)s 1000w, %(hero)s 2000w" sizes="100vw"
       width="2000" height="1120" alt="%(alt)s" fetchpriority="high">
  <div class="ih-hero-in">
    <div class="ih-hero-copy">
      <p class="ih-kicker">Exam route &middot; %(span)s &middot; the Academic module</p>
      <h1 class="ih-h1" id="ih-h1">IELTS <em>Academic</em></h1>
      <p class="ih-lede">Writing, Speaking, Listening, Reading, and the vocabulary that feeds two of them &mdash; %(nroutes_w)s routes, each in the order it should be taught.</p>
      <ul class="ih-stats">
        <li><b>%(total)d</b><span>%(lessons)s</span></li>
        <li><b>%(nroutes)d</b><span>routes</span></li>
        <li class="ih-stat-free"><b>%(free)d</b><span>%(free_line)s</span></li>
      </ul>
      <div class="ih-ctas">
        <a class="ih-btn" href="#routes">Choose a route <span aria-hidden="true">&darr;</span></a>
        <a class="ih-btn ih-btn-quiet" href="#test">The test, to scale</a>
      </div>
    </div>
  </div>
</header>""" % dict(hero=HERO_SRC, hero_sm=derive(HERO_SRC, 'hero-1000', 1000, 82),
                   alt=esc(HERO_ALT), total=f['total'], lessons=plural(f['total'], 'lesson'),
                   free=f['free'], free_line=free_line,
                   nroutes=len(routes), nroutes_w=words(len(routes)),
                   span=level_span([s['level'] for r in routes for s in r['stops']]))


def test_to_scale(routes):
    by = {r['key']: r for r in routes}

    def n(k):
        c = len(by[k]['stops'])
        return '%d %s' % (c, plural(c, 'lesson'))
    return """<section class="ih-test" id="test" aria-labelledby="ih-test-h">
  <div class="ih-wrap">
    <div class="ih-sechead">
      <p class="ih-kicker">The exam</p>
      <h2 class="ih-h2" id="ih-test-h">The test, to scale</h2>
      <p>Four papers, about two hours and forty-five minutes. Listening, Reading and Writing are sat back to back with no break between them; Speaking is face to face with an examiner, and may fall on a different day.</p>
    </div>
    <div class="ih-scale">
      <a class="ih-seg ih-seg-l" href="#listening" style="--m:30" aria-label="Listening: 30 minutes, 4 sections, 40 questions, each recording heard once. %(l)s on the Listening route.">
        <div><span class="ih-seg-name">Listening</span><p class="ih-seg-fact">4 sections &middot; 40 questions &middot; each recording heard once</p></div>
        <span class="ih-seg-min">30<small>min</small></span>
      </a>
      <div class="ih-seg ih-seg-x" style="--m:10" role="note" aria-label="Plus 10 minutes to transfer Listening answers, on the paper test only.">
        <p class="ih-seg-fact">on paper</p>
        <span class="ih-seg-min">+10</span>
      </div>
      <a class="ih-seg ih-seg-r" href="#reading" style="--m:60" aria-label="Reading: 60 minutes, 3 sections, 40 questions, no transfer time. %(r)s on the Reading route.">
        <div><span class="ih-seg-name">Reading</span><p class="ih-seg-fact">3 sections &middot; 40 questions &middot; no time at the end to transfer anything</p></div>
        <span class="ih-seg-min">60<small>min</small></span>
      </a>
      <a class="ih-seg ih-seg-w" href="#writing" style="--m:60" aria-label="Writing: 60 minutes. Task 1, about 20 minutes, at least 150 words. Task 2, about 40 minutes, at least 250 words, twice the marks of Task 1. %(w)s on the Writing route.">
        <div class="ih-task" style="--m:20">
          <div><span class="ih-seg-name">Writing: Task&nbsp;1</span><p class="ih-seg-fact">at least 150 words</p></div>
          <span class="ih-seg-min">~20<small>min</small></span>
        </div>
        <div class="ih-task" style="--m:40">
          <div><span class="ih-seg-name">Task&nbsp;2</span><p class="ih-seg-fact">at least 250 words &middot; twice the marks of Task&nbsp;1</p></div>
          <span class="ih-seg-min">~40<small>min</small></span>
        </div>
      </a>
      <div class="ih-gap" style="--m:7" aria-hidden="true"></div>
      <a class="ih-seg ih-seg-s" href="#speaking" style="--m:14" aria-label="Speaking: 11 to 14 minutes, 3 parts, face to face. %(s)s on the Speaking route.">
        <div><span class="ih-seg-name">Speaking</span><p class="ih-seg-fact">3 parts</p></div>
        <span class="ih-seg-min">11&ndash;14</span>
      </a>
      <p class="ih-scale-note">Drawn to scale: every block is as long as the paper is. <span class="ih-keyed"><span class="ih-key ih-key-recv"></span>Blues</span> for the two papers you take in, <span class="ih-keyed"><span class="ih-key ih-key-prod"></span>reds</span> for the two you produce. The hatched ten minutes are for copying Listening answers onto the answer sheet, and only the paper test has them.</p>
      <a class="ih-brace" href="#vocabulary"><b>Vocabulary</b> <span>Lexical Resource is a quarter of the Writing mark and a quarter of the Speaking mark &mdash; %(v)s &rarr;</span></a>
    </div>
  </div>
</section>""" % dict(l=n('listening'), r=n('reading'), w=n('writing'), s=n('speaking'),
                     v=n('vocabulary'))


def stop_html(s):
    return ('          <li class="ih-stop%s"><a href="%s"><span class="ih-dot">%d</span>'
            '<span class="ih-stop-t">%s%s</span></a></li>'
            % (' ih-free' if s['free'] else '', seo.quote(s['file']), s['n'], s['title'],
               ' <span class="ih-pill">Free</span>' if s['free'] else ''))


def route_html(i, r):
    count = len(r['stops'])
    first_free = next((s for s in r['stops'] if s['free']), None)
    many = len(r['groups']) > 1
    groups = []
    for g in r['groups']:
        groups.append('      <div class="ih-group">%s\n        <ol class="ih-stops">\n%s\n        </ol>\n      </div>'
                      % ('\n        <h4 class="ih-group-h">%s</h4>' % g['h'] if many else '',
                         '\n'.join(stop_html(s) for s in g['stops'])))
    art = derive(r['art'], 'route-%s' % r['key'], 1200)
    go = []
    if first_free:
        go.append('<a class="ih-btn ih-btn-sm" href="%s">Start free: %s <span aria-hidden="true">&rarr;</span></a>'
                  % (seo.quote(first_free['file']), first_free['title']))
    go.append('<a class="ih-textlink" href="%s">The %s route, lesson by lesson</a>'
              % (r['hub'], r['name']))
    return """  <article class="ih-route" id="%(key)s" data-family="%(family)s" aria-labelledby="ih-r-%(key)s">
    <a class="ih-route-art" href="%(hub)s" tabindex="-1" aria-hidden="true">
      <img src="%(art)s" alt="" loading="lazy" decoding="async" style="object-position:%(pos)s">
    </a>
    <div class="ih-route-body">
      <div class="ih-route-head">
        <span class="ih-route-num" aria-hidden="true">%(num)02d</span>
        <div>
          <p class="ih-route-meta">%(count)d %(lessons)s &middot; %(meta)s</p>
          <h3 class="ih-route-name" id="ih-r-%(key)s"><a href="%(hub)s">%(name)s</a></h3>
        </div>
      </div>
      <p class="ih-route-pitch">%(pitch)s</p>
      <div class="ih-groups%(two)s">
%(groups)s
      </div>
      <div class="ih-route-go">%(go)s</div>
    </div>
  </article>""" % dict(r, num=i + 1, count=count, lessons=plural(count, 'lesson'),
                       art=art, groups='\n'.join(groups), go=''.join(go),
                       two=' ih-two' if many and count >= 8 else '')


def routes_html(routes, f):
    jump = '\n'.join(
        '        <li data-family="%s"><a href="#%s"><span class="ih-jump-n">%02d</span>'
        '<span class="ih-jump-name">%s</span><span class="ih-jump-c">%d %s</span></a></li>'
        % (r['family'], r['key'], i + 1, r['name'], len(r['stops']),
           plural(len(r['stops']), 'lesson')) for i, r in enumerate(routes))
    free = (' The first lesson on every route is free, with no sign-in.' if f['firsts']
            else ' Lessons marked Free need no sign-in.')
    if not f['silent']:
        decks = ('Every lesson is a click-through deck, scored where scoring teaches '
                 'something, and ends with language you produce rather than recognise.')
    else:
        decks = ('Every lesson is a click-through deck, scored where scoring teaches '
                 'something. All but %s end with language you produce rather than '
                 'recognise.' % words(len(f['silent'])))
    return """<section class="ih-routes" id="routes" aria-labelledby="ih-routes-h">
  <div class="ih-wrap">
    <div class="ih-routes-head">
      <div class="ih-sechead">
        <p class="ih-kicker">%(n_w)s routes</p>
        <h2 class="ih-h2" id="ih-routes-h">Pick a route. Walk it in order.</h2>
        <p>Each route is ordered: the later lessons assume the earlier ones, so start at the top of one and work down rather than picking lessons at random.%(free)s</p>
        <p>%(decks)s</p>
      </div>
      <ol class="ih-jump" aria-label="Jump to a route">
%(jump)s
      </ol>
    </div>
%(routes)s
  </div>
</section>""" % dict(n_w=words(len(routes)).capitalize(), jump=jump, free=free, decks=decks,
                     routes='\n'.join(route_html(i, r) for i, r in enumerate(routes)))


def symptoms_html(routes):
    stops = {s['file']: s for r in routes for s in r['stops']}
    items = []
    for said, f in SYMPTOMS:
        if f == 'ielts-question-bank.html':
            where, title, free = 'Reference', 'Question Bank &amp; Ideas', True
        elif f in stops:
            s = stops[f]
            where, title, free = '%s %d' % (s['route']['name'], s['n']), s['title'], s['free']
        else:
            print('  ! symptom list names %s, which is on no route page; dropped' % f)
            continue
        items.append("""      <li class="ih-q"><a href="%s">
        <span class="ih-q-said">%s</span>
        <span class="ih-q-go"><span class="ih-q-arrow" aria-hidden="true">&rarr;</span><span class="ih-q-where">%s</span> <span class="ih-q-title">%s</span>%s</span>
      </a></li>""" % (seo.quote(f), said, where, title,
                      ' <span class="ih-pill">Free</span>' if free else ''))
    return """<section class="ih-diag" id="start" aria-labelledby="ih-diag-h">
  <div class="ih-wrap">
    <div class="ih-sechead">
      <p class="ih-kicker">Where the marks go</p>
      <h2 class="ih-h2" id="ih-diag-h">Already know what is costing you?</h2>
      <p>Every route runs in order, but you do not have to start at the top of all %s. If you can name the problem, one of these answers it.</p>
    </div>
    <ul class="ih-qs">
%s
    </ul>
  </div>
</section>""" % (words(len(routes)), '\n'.join(items))


def bank_html():
    n, t, types = bank_numbers()
    return """<section class="ih-bank" aria-labelledby="ih-bank-h">
  <div class="ih-wrap">
    <a class="ih-bank-card" href="ielts-question-bank.html">
      <div class="ih-bank-art"><img src="%(art)s" alt="" loading="lazy" decoding="async"></div>
      <div class="ih-bank-copy">
        <p class="ih-kicker">Free &middot; no sign-in</p>
        <h2 id="ih-bank-h">Question Bank &amp; Ideas</h2>
        <p><b>%(n)d Task&nbsp;2 questions across %(t)d topics</b> &mdash; artificial intelligence, gentrification, energy and immigration included &mdash; filterable by topic and by essay type, and under each topic, arguments for both sides. For when you know the shape and have nothing to say &mdash; keep it open while you write.</p>
        <ul class="ih-types">%(types)s</ul>
        <span class="ih-btn">Open the question bank <span aria-hidden="true">&rarr;</span></span>
      </div>
    </a>
  </div>
</section>""" % dict(art=derive(BANK_SRC, 'bank', 1200), n=n, t=t,
                     types=''.join('<li>%s</li>' % esc(x) for x in types))


def notes_html(routes):
    # Plain string order puts every level below C1 ('A1'..'B2', 'A2-C1',
    # 'B2-C1') before 'C1', and C1-and-up after it: the split wanted here.
    below = [s for r in routes for s in r['stops'] if s['level'] and s['level'] < 'C1']
    pitch = 'The whole set is C1'
    if below:
        pitch = 'Everything is C1 except %s' % ', '.join(
            '<em>%s</em> on the %s route, which starts at %s'
            % (s['title'], s['route']['name'], s['level'][:2]) for s in below)
    return """<section class="ih-notes" aria-labelledby="ih-notes-h">
  <h2 class="ih-vh" id="ih-notes-h">Before you start</h2>
  <div class="ih-wrap ih-notes-grid">
    <div class="ih-note">
      <h3>Sitting General Training?</h3>
      <p><strong>This is the Academic module.</strong> Speaking and Listening are identical on General Training, and Reading uses the same question types &mdash; but GT Task 1 is a letter, not a report, so the Task 1 lessons will not match a GT paper. Task 2 is the same on both.</p>
    </div>
    <div class="ih-note">
      <h3>Teaching this rather than sitting it?</h3>
      <p>The Writing route runs as a course; the Model Answer Vault works on its own as a marking clinic, and the Writing Studio exports a learner&rsquo;s planning notes and final essay as a plain text file for correction. Speaking is built for pairs.</p>
      <p>%s &mdash; bring a strong B2 class and expect to slow down.</p>
    </div>
  </div>
</section>""" % pitch


def close_html(routes, f, series):
    art = ('<img class="ih-close-art" src="%s" alt="" loading="lazy" decoding="async">\n  ' % series
           if series else '')
    pro = f['total'] - f['free']
    if f['free']:
        head = '%s %s free. Pro opens the other %s.' % (
            words(f['free']).capitalize() if f['free'] < 100 else f['free'],
            'lesson is' if f['free'] == 1 else 'lessons are',
            words(pro) if pro < 100 else pro)
    else:
        head = 'Every lesson here comes with Pro.'
    lead = ('The first lesson on every route costs nothing and needs no account. '
            if f['firsts'] else 'Lessons marked Free cost nothing and need no account. ')
    return """<section class="ih-close" aria-labelledby="ih-close-h">
  %s<div class="ih-close-in">
    <p class="ih-kicker">Forbes English Pro</p>
    <h2 class="ih-h2" id="ih-close-h">%s</h2>
    <p>%sPro is every lesson on the site &mdash; IELTS and everything else &mdash; with new ones as they are published.</p>
    <div class="ih-ctas">
      <a class="ih-btn" href="pricing.html">Plans and prices <span aria-hidden="true">&rarr;</span></a>
      <a class="ih-btn ih-btn-quiet" href="library.html#cat=IELTS">Every IELTS lesson in the library</a>
    </div>
  </div>
</section>""" % (art, head, lead)


def ld(routes):
    lessons = [s for r in routes for s in r['stops']]
    return {'@context': 'https://schema.org', '@graph': [
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/index.html'},
            {'@type': 'ListItem', 'position': 2, 'name': 'IELTS Academic'}]},
        {'@type': 'ItemList', 'name': 'IELTS Academic lessons, in teaching order',
         'numberOfItems': len(lessons),
         'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1,
              'url': '%s/%s' % (SITE, seo.quote(s['file'])), 'name': s['full']}
             for i, s in enumerate(lessons)]}]}


def body(rows, images):
    routes = load(rows)
    f = facts(routes)
    parts = ['<main>', hero(routes, f), test_to_scale(routes),
             routes_html(routes, f), symptoms_html(routes), bank_html(),
             notes_html(routes), close_html(routes, f, mosaic(routes, images)),
             '</main>',
             '<script type="application/ld+json">%s</script>'
             % json.dumps(ld(routes), ensure_ascii=False, separators=(',', ':'))]
    return '\n'.join(parts), routes, f


def fence(src, start, end, content, after):
    """Replace a fenced region, or create it once at `after` (a regex whose
    match end is the insertion point) — the first run on the hand-written
    page."""
    block = '%s\n%s\n%s' % (start, content, end)
    if start in src and end in src:
        return re.sub(re.escape(start) + '.*?' + re.escape(end), lambda _: block, src,
                      count=1, flags=re.S)
    m = re.search(after, src, re.S)
    if not m:
        sys.exit('! ielts.html: cannot place %s' % start)
    return src[:m.end()] + '\n' + block + src[m.end():]


def build(rows=None, images=None, check=False):
    """Rewrite ielts.html. With check=True write nothing at all (not the
    page, not a picture, not the catalogue cache) and return whether a
    rebuild would change anything."""
    STATE.update(check=check, missing=[])
    if rows is None:
        rows, source = seo.lessons(write_cache=not check)
        print('  lessons: %d (from %s)' % (len(rows), source))
    if images is None:
        images = seo.lesson_images()
    src = open(PAGE, encoding='utf-8').read()
    main_html, routes, f = body(rows, images)
    new = fence(src, CSS_START, CSS_END, css(), r'<style>.*?</style>')
    if BODY_START not in new:
        # First run: everything between the nav and </body> was the old
        # hand-written page. It is replaced, not kept alongside.
        new = re.sub(r'(</nav>\n).*?(</body>)', lambda m: m.group(1) + '\n' + m.group(2),
                     new, count=1, flags=re.S)
    new = fence(new, BODY_START, BODY_END, main_html, r'</nav>\n')
    new = re.sub(r'<body[^>]*>', '<body class="ih">', new, count=1)
    stale = new != src or bool(STATE['missing'])
    if not check and new != src:
        open(PAGE, 'w', encoding='utf-8', newline='\n').write(new)
    for m in STATE['missing']:
        print('  ! %s would be written' % m)
    print('  ielts.html: %d routes, %d lessons, %d free%s' % (
        len(routes), f['total'], f['free'],
        (' — STALE' if check else ' — rewritten') if stale else ' — unchanged'))
    return stale


# ── --palette and --check ─────────────────────────────────────────────
def palette():
    import glob
    import subprocess
    import tempfile
    from PIL import Image
    fs = sorted(glob.glob(os.path.join(ROOT, 'ielts-*', 'hero.jpg')))
    W, H, cols = 500, 280, 6
    full = len(fs) // cols
    m = Image.new('RGB', (cols * W, full * H))
    for i, f in enumerate(fs[:full * cols]):
        m.paste(Image.open(f).convert('RGB').resize((W, H)), ((i % cols) * W, (i // cols) * H))
    tmp = os.path.join(tempfile.gettempdir(), 'ielts-series-montage.jpg')
    m.save(tmp, quality=92)
    tool = os.path.join(ROOT, 'lesson-template', 'extract-palette.py')
    for flag in (['--light'], []):
        print(subprocess.run([sys.executable, tool, tmp] + flag, capture_output=True,
                             text=True, encoding='utf-8').stdout)
    q = m.resize((600, 300)).quantize(colors=8, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()
    print('/* art fields: MEDIANCUT 8 */')
    for c, i in sorted(q.getcolors(), reverse=True):
        print('  #%02x%02x%02x' % tuple(pal[i * 3:i * 3 + 3]))


def _lum(h):
    h = h.lstrip('#')
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def _mix(a, b, t):
    a, b = a.lstrip('#'), b.lstrip('#')
    return '#' + ''.join('%02x' % round(int(a[i:i + 2], 16) * t + int(b[i:i + 2], 16) * (1 - t))
                         for i in (0, 2, 4))


def contrast_report():
    col = dict(PALETTE)
    for k, (a, b, t) in MIX.items():
        col[k] = _mix(PALETTE[a], PALETTE[b], t)
    bad = 0
    for fg, bg, need, what in CONTRAST:
        la, lb = _lum(col[fg]), _lum(col[bg])
        r = (max(la, lb) + 0.05) / (min(la, lb) + 0.05)
        ok = r >= need
        bad += not ok
        print('  %-14s on %-11s %5.2f:1 (min %.1f) %s  %s'
              % (fg, bg, r, need, 'PASS' if ok else 'FAIL', what))
    return bad


if __name__ == '__main__':
    if '--palette' in sys.argv:
        palette()
        sys.exit(0)
    check = '--check' in sys.argv
    failures = contrast_report()
    # The route pages share this page's pictures; building one alone can
    # prune a picture the others still show. Build all six.
    import build_ielts_routes
    stale, refused = build_ielts_routes.build_all(check=check, force='--force' in sys.argv)
    if refused:
        sys.exit(2)
    if failures:
        sys.exit('! %d contrast pair(s) fail' % failures)
    if check and stale:
        sys.exit(1)
