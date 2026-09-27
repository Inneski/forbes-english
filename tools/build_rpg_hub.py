# -*- coding: utf-8 -*-
"""Build the role-playing games landing page, `rpg.html`.

    python3 tools/build_hubs.py                # builds it with the other hubs; then tools/seo.py
    python3 tools/build_rpg_hub.py --check     # measure every text-on-fill pair; exit 1 on a failure
    python3 tools/build_rpg_hub.py --palette   # re-derive the colours below from the hero

`tools/build_hubs.py` calls `render()` for the page body and its style
block, so the normal pipeline keeps it current: add an RPG to the
catalogue (with a picture in library.html's LESSON_IMAGES), run
build_hubs, and it is on this page with its level and Free/Pro.

WHY IT EXISTS. Innes, 2026-09-26, on the library's hero band: *"RPGS
deserves an equal button with IELTS, Block Camp & Sherpa ... RPGs should
have a hub too."* Until then the RPGs were a category filter on the
library and a collection card; the Block Camp half had a hub
(`block-camp.html`) and the story games — Sherlock, Thornwick, the
Kraken, Wild Frame, the Parisian Conquest — had nothing. This page is
the RPG hub in the IELTS / grammar landing-page family: full-bleed hero,
the counts, how a game works, the free ones, every game by level, the
two neighbours (Block Camp and the classroom roleplays), notes, a
closing band.

WHICH LESSONS ARE RPGS is the library's own rule, ported verbatim from
`detectCategories()` in library.html (`RPG_PATTERN` below, plus anything
under `block-camp/`), so this page and the library's "Role Playing
Games" filter always agree. A game whose title says nothing about being
one — the Scarlet Star, Thornwick — is caught by name there, and so here.

WHAT EACH CARD SAYS. The Block Camp adventures already have blurbs and
grammar chips in `lesson-template/build/block-camp-hub/build.py`
(`ADVENTURES`); they are imported, not retyped. The story games have
theirs in `GAMES` below, written from each page's own cover copy. Level
and Free/Pro come from the catalogue for both — the Block Camp table
still marks The Last Bounty Pro, the catalogue says Free, and the
catalogue is what the Worker enforces.

THE PALETTE is derived from the hero, not picked (HOUSE-STYLE §4):
    extract-palette.py Sherlock/hero.jpg --light  -> the paper side
    extract-palette.py Sherlock/hero.jpg          -> the dark bands
    PIL MEDIANCUT, 8 colours                      -> the art fields
`--palette` prints the recipe again. Every text-on-fill pair the page
uses is in CONTRAST and measured on every build.

PICTURES. Card covers are web-sized JPEGs in `rpg-hub/`, named by a hash
of their inputs like the grammar hub's: change a cover and the name
changes, the old copy is pruned, and the HTML diff shows it. The hero is
served as it is (it is also the share image). The closing band's mosaic
is built from the covers the same way.
"""
import glob
import hashlib
import html
import importlib.util
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo                                   # noqa: E402
import topics                                # noqa: E402

ROOT = seo.ROOT
SITE = seo.SITE
ART = 'rpg-hub'                              # web-sized pictures live here
PAGE = 'rpg.html'

HERO = 'Sherlock/hero.jpg'
HERO_ALT = ('Flat-vector illustration of Sherlock Holmes in a deerstalker, pipe in '
            'his mouth, looking over the collar of a blue coat against a coral ground')
HERO_OG = '/' + seo.quote(HERO)              # seo.py puts this on the og:image

# The library's rule for the "Role Playing Games" category, verbatim
# (detectCategories in library.html). Keep the two in step.
RPG_PATTERN = re.compile(
    r'\brpg\b|role[\s_-]?playing|career quest|falcon racing|parisian conquest|'
    r'wild frame|thornwick|sherlock|scarlet star')
BLOCK_CAMP_DIR = 'block-camp/'
BLOCK_CAMP_HUB = os.path.join(ROOT, 'lesson-template', 'build', 'block-camp-hub', 'build.py')

# ── the story games ───────────────────────────────────────────────────
# file -> (title, blurb, grammar chips). Written from each page's own cover
# and briefing copy; the level and Free/Pro are the catalogue's.
GAMES = {
    'sherlock-scarlet-star.html': (
        'The Scarlet Star',
        'Recover the artefact, solve the murder, outsmart Moriarty. Every deduction is a '
        'past modal or a line of reported speech; you start with three lives, earn '
        'Deduction Points, and need four clue cards for the best ending.',
        ('Past Modals', 'Reported Speech')),
    'thornwick-deduction.html': (
        'The Thornwick Deduction',
        'A murder in a locked study in Hampstead and forty-seven chances to say exactly '
        'how sure you are. You work the case beside Holmes, who accepts <em>must have</em>, '
        '<em>can&rsquo;t have</em> and <em>might have</em> only when the evidence earns them.',
        ('Modals of Deduction',)),
    'kraken-black-tide-rpg.html': (
        'The Kraken: A Tale of the Deep',
        'Ten o&rsquo;clock on a West Highland sea loch, the light nearly gone, and '
        'something in the deep water at the mouth of the Narrows. A creel boat, an uncle '
        'and his nephew, and every question asking what has happened and what has been '
        'happening. Click the glowing object in each scene to read.',
        ('Present Perfect',)),
    'stranger-gears-rpg.html': (
        'Stranger Gears: The Last Broadcast',
        'Three drivers, three confessions, and a signal from the Upside Down that knows '
        'what each of them is trying not to say. Halloway, 97.3 FM, 21:40 &mdash; and at '
        '02:17 one of you chooses who gets home. Every step back through the night is a '
        'past modal.',
        ('Past Modals',)),
    'Race Day - The Falcon Racing Story (B1 F1 RPG).html': (
        'Race Day: The Falcon Racing Story',
        'You are Alex, twenty-three, a rookie driver for Falcon Racing, and this is your '
        'first Grand Prix weekend, at Monza. Present simple against present continuous in '
        'the commentary, first conditionals on the pit wall, and a team-confidence score '
        'that decides how the race ends.',
        ('Present Simple vs Continuous', 'First Conditional')),
    'wild-frame.html': (
        'Wild Frame',
        'Ten years, one camera. A documentary filmmaker&rsquo;s career built one storm, '
        'one pitch and one grammar checkpoint at a time: eleven chapters, sixteen '
        'checkpoints, four endings, about two hours.',
        ('Mixed Grammar',)),
    'wild-frame-part-2.html': (
        'Wild Frame Part II: The Palace Set',
        'Your first film found its ending. Now a gothic thriller wants you on set at '
        'Biester Palace, filming the story behind its story &mdash; new crew, new grammar, '
        'and a lead actor harder to read than the script. It starts by asking how Part One '
        'ended.',
        ('Mixed Grammar',)),
    'forbes-dnd-rpg.html': (
        'The Parisian Conquest',
        'Business English as a dungeon crawl. Choose a class, roll your stats &mdash; '
        'Eloquence, Gravitas, Cultural IQ, Resilience &mdash; and take your agency through '
        'five dungeons, from the cold call to the throne room, to win the French market. '
        'Your weapons are words.',
        ('Business English', 'Negotiation')),
    'forbes-dnd-rpg-part2.html': (
        'The Parisian Conquest II: The Long Winter',
        'You won the account; now keep it. Five more dungeons for the twelve months after '
        'the pitch: saying no without damage, delivering bad news before it is discovered, '
        'defending numbers that missed, and asking for more when you have not been perfect.',
        ('Business English',)),
}

# ── palette ───────────────────────────────────────────────────────────
PALETTE = {
    # extract-palette.py Sherlock/hero.jpg --light
    'void': '#bacaca', 'surface': '#ced7d7', 'surface2': '#c4d0d0',
    'border': '#96524a', 'text': '#2a1411', 'text-dim': '#5e332e',
    'accent': '#ac1200', 'accent-bright': '#790d00', 'accent-dim': '#f04a37',
    'secondary': '#07466d', 'contrast': '#075538',
    # extract-palette.py Sherlock/hero.jpg
    'ink': '#090c0e', 'ink-surface': '#12181c', 'ink-surface2': '#1a2329',
    'ink-border': '#a84a3f', 'ink-text': '#f5f2f2', 'ink-text-dim': '#bfa6a3',
    'ink-accent': '#e97264',
    # the hero quantised (MEDIANCUT, 8), most to least common
    'night': '#010406', 'coral': '#ee756a', 'navy': '#10293d', 'coral-deep': '#e06d5a',
    'coral-2': '#ed7469', 'deep': '#030e15', 'plum': '#5c515e', 'coral-light': '#ef796e',
}
# Mixed, not picked: the paper and the card, the derived surface lifted
# towards the derived light text. Resolved here so --check can measure
# them; the CSS spells out the same color-mix().
MIX = {'paper': ('surface', 'ink-text', 0.62), 'card': ('surface', 'ink-text', 0.30)}

# Text-on-fill pairs the page uses, measured on every build.
CONTRAST = [
    ('navy', 'coral', 4.5, 'hero copy on the coral scrim'),
    ('accent-bright', 'coral', 3.0, 'hero H1 emphasis (large)'),
    ('text', 'paper', 4.5, 'body copy'),
    ('text', 'card', 4.5, 'card titles'),
    ('text-dim', 'paper', 4.5, 'secondary copy'),
    ('text-dim', 'card', 4.5, 'secondary copy on cards'),
    ('accent', 'paper', 4.5, 'kickers, links'),
    ('accent', 'card', 4.5, 'kickers on cards'),
    ('accent-bright', 'paper', 3.0, 'H2 emphasis (large)'),
    ('ink-text', 'accent', 4.5, 'Free pill'),
    ('ink-text', 'secondary', 4.5, 'Block Camp pill'),
    ('ink-text', 'contrast', 4.5, 'Story pill'),
    ('ink-text', 'ink', 4.5, 'step numbers, closing band'),
    ('ink-text-dim', 'ink', 4.5, 'closing band secondary'),
    ('ink-accent', 'ink', 4.5, 'closing band kicker'),
    ('ink-text', 'navy', 4.5, 'plate copy over the scrim'),
    ('ink-accent', 'navy', 4.5, 'plate kicker and link'),
    ('ink-text', 'night', 4.5, 'free plate copy over the scrim'),
    ('ink-accent', 'night', 4.5, 'free plate kicker'),
    # Focus rings: WCAG 1.4.11 wants 3:1 against what the ring sits on.
    ('accent', 'paper', 3.0, 'focus ring on paper'),
    ('navy', 'coral', 3.0, 'focus ring in the hero'),
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


# ── pictures ──────────────────────────────────────────────────────────
def _sha(*parts):
    h = hashlib.sha1()
    for p in parts:
        h.update(p if isinstance(p, bytes) else str(p).encode('utf-8'))
    return h.hexdigest()[:8]


def _save(name, make):
    """Write rpg-hub/<name> from make() unless it is already there; keep
    it from the prune either way. Returns the site-relative path."""
    STATE['keep'].add(name)
    out = os.path.join(ROOT, ART, name)
    if not os.path.exists(out):
        os.makedirs(os.path.join(ROOT, ART), exist_ok=True)
        make(out)
    return '%s/%s' % (ART, name)


def web_copy(src_rel, stem, width=640, quality=82):
    """A web-sized JPEG of `src_rel` in rpg-hub/, named by its inputs.
    PIL's encoder is deterministic, so a rebuild from the same inputs
    makes no diff."""
    from PIL import Image
    src = os.path.join(ROOT, src_rel.lstrip('/'))
    data = open(src, 'rb').read()
    name = '%s-%s.jpg' % (stem, _sha(data, width, quality))

    def make(out):
        im = Image.open(src).convert('RGB')
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        im.save(out, 'JPEG', quality=quality, optimize=True, progressive=True)
    return _save(name, make)


def mosaic(covers, cols=6, rows=3, cell=(256, 144), quality=72):
    """The covers tiled `cols` wide, full rows only, for the closing band."""
    from PIL import Image
    covers = covers[:cols * rows]
    datas = [open(os.path.join(ROOT, c), 'rb').read() for c in covers]
    name = 'mosaic-%s.jpg' % _sha(*datas, cols, rows, cell, quality)

    def make(out):
        w, h = cell
        sheet = Image.new('RGB', (cols * w, rows * h), PALETTE['ink'])
        for i, c in enumerate(covers):
            im = Image.open(os.path.join(ROOT, c)).convert('RGB')
            s = max(w / im.width, h / im.height)
            im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
            left, top = (im.width - w) // 2, (im.height - h) // 2
            sheet.paste(im.crop((left, top, left + w, top + h)), ((i % cols) * w, (i // cols) * h))
        sheet.save(out, 'JPEG', quality=quality, optimize=True, progressive=True)
    return _save(name, make), rows * cell[1]


def prune():
    """Delete rpg-hub/*.jpg that this build did not produce."""
    gone = []
    for p in glob.glob(os.path.join(ROOT, ART, '*.jpg')):
        if os.path.basename(p) not in STATE['keep']:
            os.remove(p)
            gone.append(os.path.basename(p))
    return gone


# ── the games ─────────────────────────────────────────────────────────
def _hay(r):
    return ('%s %s' % (r.get('title') or '', r.get('file') or '')).lower()


def is_rpg(r):
    return bool(RPG_PATTERN.search(_hay(r))) or r['file'].startswith(BLOCK_CAMP_DIR)


def block_camp_table():
    """{file: (title, blurb, grammar chips)} from the Block Camp hub's
    ADVENTURES, so the two pages tell the same story about each game."""
    spec = importlib.util.spec_from_file_location('block_camp_hub', BLOCK_CAMP_HUB)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return {href: (title, desc, tuple(gram)) for href, _img, title, desc, gram, *_ in mod.ADVENTURES}


def plural(n, one, many=None):
    return '%d %s' % (n, one if n == 1 else (many or one + 's'))


WORDS = ('zero one two three four five six seven eight nine ten eleven twelve '
         'thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty').split()


def words(n):
    if n < len(WORDS):
        return WORDS[n]
    if n < 30:
        return 'twenty-' + WORDS[n - 20]
    return str(n)


def band(level):
    """Which chapter a level string ('A1-A2', 'B1', 'C1') files under."""
    lo = (level or '').split('-')[0]
    if lo in ('A1', 'A2'):
        return 0
    if lo in ('B1', 'B2'):
        return 1
    return 2


BANDS = [('A1&ndash;A2', 'Beginner', 'Short scenes, one tense each, and the answer explained when you miss it.'),
         ('B1&ndash;B2', 'Intermediate', 'Longer stories with more at stake: modals of deduction, the perfect tenses, a career.'),
         ('C1', 'Advanced', 'Business English with dice: the language of winning an account, and of keeping one.')]


def load(rows, images):
    """The games on the page: every catalogue row the library calls an
    RPG that is finished (has a picture), with its copy and cover."""
    bc = block_camp_table()
    games = []
    for r in rows:
        if not is_rpg(r) or seo.coming_soon(r, images):
            continue
        f = r['file']
        if f in bc:
            title, blurb, gram = bc[f]
            world = 'block-camp'
        elif f in GAMES:
            title, blurb, gram = GAMES[f]
            world = 'story'
        else:
            title, blurb, gram, world = seo.page_title(r), '', (), 'story'
            print('  ! %s is an RPG with no entry in GAMES (tools/build_rpg_hub.py); '
                  'carded with its title only' % f)
        games.append(dict(file=f, title=title, blurb=blurb, gram=gram, world=world,
                          level=r.get('level') or '', free=r.get('access') != 'pro',
                          cover=images[f], band=band(r.get('level'))))
    games.sort(key=lambda g: (g['band'], topics.level_key(g['level'].split('-')[0]),
                              not g['free'], g['title'].lower()))
    return games


# ── the page ──────────────────────────────────────────────────────────
CSS = """
<!-- RPG-HUB-CSS:start -->
<style id="rpg-hub-css">
/* The role-playing games landing page. Generated by tools/build_rpg_hub.py —
   edit it there. Colours: see that file's docstring. Every class is rh-
   prefixed so nothing here collides with the shared block above. */
body.rh {
%(tokens)s
  --rh-paper: color-mix(in srgb, var(--rh-surface) 62%%, var(--rh-ink-text));
  --rh-card:  color-mix(in srgb, var(--rh-surface) 30%%, var(--rh-ink-text));
  --rh-line:  color-mix(in srgb, var(--rh-border) 34%%, transparent);
  --rh-shadow: color-mix(in srgb, var(--rh-ink) 18%%, transparent);
  --rh-max: 1240px;
  --rh-gut: clamp(16px, 4vw, 48px);
  background: var(--rh-paper);
  color: var(--rh-text);
  font-variant-numeric: lining-nums;
}
:where(.rh) a { color: inherit; }
.rh :where(main) a:focus-visible { outline: 3px solid var(--rh-accent); outline-offset: 3px; }
.rh-hero a:focus-visible { outline-color: var(--rh-navy); }
.rh-close a:focus-visible, .rh-plate:focus-visible, .rh-free-card:focus-visible { outline-color: var(--rh-ink-accent); }
.rh-vh { position: absolute; width: 1px; height: 1px; margin: -1px; padding: 0; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
.rh-wrap { max-width: var(--rh-max); margin: 0 auto; padding: 0 var(--rh-gut); }
.rh-kicker {
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .16em; text-transform: uppercase; font-size: .8rem;
  color: var(--rh-accent); margin: 0 0 12px;
}
.rh-h2 {
  font-family: 'Playfair Display', serif; font-weight: 900;
  font-size: clamp(2rem, 4.4vw, 3.2rem); line-height: 1.02; letter-spacing: -.012em;
  margin: 0 0 16px; color: var(--rh-text); text-wrap: balance;
}
.rh-h2 em { font-style: normal; color: var(--rh-accent-bright); }
.rh-sechead { max-width: 64ch; }
.rh-sechead p { font-size: 1.1rem; line-height: 1.62; color: var(--rh-text-dim); margin: 0; }
.rh-sechead p + p { margin-top: 12px; }
.rh-sechead em { font-style: italic; color: var(--rh-text); }
.rh-btn {
  display: inline-flex; align-items: center; gap: .5em;
  font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .09em; text-transform: uppercase; font-size: .92rem;
  text-decoration: none; padding: 13px 22px; border-radius: 999px;
  background: var(--rh-navy); color: var(--rh-ink-text);
  border: 2px solid var(--rh-navy);
  transition: background .18s ease, border-color .18s ease, transform .18s ease;
}
.rh-btn:hover { background: var(--rh-accent-bright); border-color: var(--rh-accent-bright); transform: translateY(-1px); }
.rh-btn-quiet { background: transparent; color: var(--rh-navy); }
.rh-btn-quiet:hover { background: var(--rh-navy); color: var(--rh-ink-text); border-color: var(--rh-navy); }
.rh-pill {
  display: inline-block; font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: .1em; text-transform: uppercase; font-size: .68rem; line-height: 1;
  padding: 4px 8px 3px; border-radius: 999px; white-space: nowrap;
  background: color-mix(in srgb, var(--rh-text) 8%%, transparent); color: var(--rh-text-dim);
}
.rh-pill-free { background: var(--rh-accent); color: var(--rh-ink-text); }
.rh-pill-bc { background: var(--rh-secondary); color: var(--rh-ink-text); }
.rh-pill-story { background: var(--rh-contrast); color: var(--rh-ink-text); }

/* ── hero: Holmes, copy over the coral ── */
.rh-hero {
  position: relative; isolation: isolate; overflow: hidden;
  min-height: clamp(520px, 78vh, 760px); display: grid; align-items: center;
  background: var(--rh-coral);
}
.rh-hero-img {
  position: absolute; inset: 0; z-index: -2; width: 100%%; height: 100%%;
  object-fit: cover; object-position: 72%% 50%%;
  animation: rh-settle 2.6s cubic-bezier(.2,.7,.2,1) backwards;
}
@keyframes rh-settle { from { transform: scale(1.06); } to { transform: none; } }
.rh-hero::after {
  content: ''; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(90deg,
    color-mix(in srgb, var(--rh-coral) 94%%, transparent) 0%%,
    color-mix(in srgb, var(--rh-coral) 86%%, transparent) 44%%,
    color-mix(in srgb, var(--rh-coral) 30%%, transparent) 64%%,
    transparent 80%%);
}
.rh-hero-in {
  width: 100%%; max-width: var(--rh-max); margin: 0 auto;
  padding: clamp(40px, 7vh, 80px) var(--rh-gut) 56px;
  display: grid; grid-template-columns: minmax(0, 600px) 1fr;
}
.rh-hero-copy { color: var(--rh-navy); }
.rh-hero .rh-kicker { color: var(--rh-navy); }
.rh-h1 {
  font-family: 'Playfair Display', serif; font-weight: 900;
  font-size: clamp(2.8rem, min(6.4vw, 10vh), 5.4rem); line-height: .96; letter-spacing: -.022em;
  margin: 0 0 22px; color: var(--rh-navy); text-wrap: balance;
}
.rh-h1 em { font-style: normal; color: var(--rh-accent-bright); }
.rh-lede { font-size: clamp(1.08rem, 1.5vw, 1.22rem); line-height: 1.58; margin: 0 0 24px; max-width: 34em; text-wrap: pretty; }
.rh-stats {
  list-style: none; margin: 0 0 30px; padding: 16px 0 0; display: flex; flex-wrap: wrap; gap: 14px 30px;
  border-top: 1px solid color-mix(in srgb, var(--rh-navy) 30%%, transparent);
}
.rh-stats li { display: flex; align-items: baseline; gap: 8px; }
.rh-stats b { font-family: 'Barlow Condensed', sans-serif; font-weight: 800; font-size: 2.5rem; line-height: .9; }
.rh-stats span { font-size: .95rem; line-height: 1.3; max-width: 16em; text-wrap: balance; }
.rh-stats .rh-stat-free b { color: var(--rh-accent-bright); }
.rh-ctas { display: flex; flex-wrap: wrap; gap: 12px; }
@media (max-width: 880px) {
  .rh-hero { display: block; min-height: 0; background: var(--rh-paper); }
  .rh-hero-img { position: relative; z-index: auto; height: auto; aspect-ratio: 16 / 9; object-position: 60%% 50%%; }
  .rh-hero::after { display: none; }
  .rh-hero-in { grid-template-columns: 1fr; padding-top: 30px; padding-bottom: 44px; }
  .rh-hero-copy, .rh-hero .rh-kicker { color: var(--rh-text); }
  .rh-h1 { color: var(--rh-text); }
  .rh-stats { border-top-color: var(--rh-line); }
  .rh-btn-quiet { color: var(--rh-text); border-color: var(--rh-text); }
}

/* ── how a game works: three steps ── */
.rh-how { padding: clamp(56px, 8vw, 104px) 0 clamp(40px, 6vw, 72px); }
.rh-steps { list-style: none; margin: clamp(26px, 4vw, 40px) 0 0; padding: 0; display: grid; gap: 16px; grid-template-columns: repeat(3, minmax(0, 1fr)); counter-reset: rh-step; }
.rh-step {
  position: relative; background: var(--rh-card); border: 1px solid var(--rh-line); border-radius: 16px;
  padding: clamp(20px, 2.6vw, 28px); padding-top: 64px; counter-increment: rh-step;
}
.rh-step::before {
  content: counter(rh-step); position: absolute; top: 18px; left: 20px;
  width: 34px; height: 34px; border-radius: 50%%; display: grid; place-items: center;
  font-family: 'Barlow Condensed', sans-serif; font-weight: 800; font-size: 1.1rem;
  background: var(--rh-ink); color: var(--rh-ink-text);
}
.rh-step h3 { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.36rem; margin: 0 0 8px; }
.rh-step p { margin: 0; line-height: 1.6; color: var(--rh-text-dim); }
.rh-step em { font-style: italic; color: var(--rh-text); }
@media (max-width: 760px) { .rh-steps { grid-template-columns: 1fr; } }

/* ── the free ones: picture plates ── */
.rh-free { padding: clamp(40px, 6vw, 72px) 0 clamp(48px, 7vw, 88px); }
.rh-free-list { list-style: none; margin: clamp(26px, 4vw, 40px) 0 0; padding: 0; display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.rh-free-card {
  position: relative; isolation: isolate; overflow: hidden;
  display: flex; flex-direction: column; justify-content: flex-end; gap: 6px;
  min-height: clamp(260px, 26vw, 320px); padding: clamp(16px, 2.2vw, 22px);
  border-radius: 16px; text-decoration: none; color: var(--rh-ink-text);
  box-shadow: 0 14px 32px var(--rh-shadow);
  transition: transform .18s ease, box-shadow .18s ease;
}
.rh-free-card:hover { transform: translateY(-3px); box-shadow: 0 22px 44px var(--rh-shadow); }
.rh-free-card img { position: absolute; inset: 0; z-index: -2; width: 100%%; height: 100%%; object-fit: cover; transition: transform 1.4s cubic-bezier(.2,.7,.2,1); }
.rh-free-card:hover img { transform: scale(1.04); }
.rh-free-card::before {
  content: ''; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(180deg, transparent 0%%,
    color-mix(in srgb, var(--rh-night) 30%%, transparent) 30%%,
    color-mix(in srgb, var(--rh-night) 90%%, transparent) 62%%,
    color-mix(in srgb, var(--rh-night) 96%%, transparent) 100%%);
}
.rh-free-card .rh-kicker { color: var(--rh-ink-accent); margin: 0; }
.rh-free-card h3 { font-family: 'Playfair Display', serif; font-weight: 900; font-size: clamp(1.3rem, 2.2vw, 1.6rem); line-height: 1.06; margin: 0; }
.rh-free-card p { margin: 0; font-size: .92rem; line-height: 1.45; color: var(--rh-ink-text); max-width: 40ch; }
.rh-free-card .rh-meta { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 4px; }
.rh-free-card .rh-pill { background: color-mix(in srgb, var(--rh-ink-text) 18%%, transparent); color: var(--rh-ink-text); }
.rh-free-card .rh-pill-free { background: var(--rh-accent); }

/* ── every game, by level ── */
.rh-games { padding: clamp(56px, 8vw, 104px) 0 clamp(40px, 6vw, 72px); background: var(--rh-card); border-top: 1px solid var(--rh-line); border-bottom: 1px solid var(--rh-line); }
.rh-group { margin-top: clamp(36px, 5vw, 56px); }
.rh-group-h {
  display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap;
  padding-bottom: 10px; margin: 0 0 6px; border-bottom: 2px solid var(--rh-text);
}
.rh-group-h h3 { font-family: 'Playfair Display', serif; font-weight: 700; font-size: clamp(1.4rem, 2.6vw, 1.8rem); margin: 0; }
.rh-group-h h3 small { font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; font-size: .8rem; color: var(--rh-text-dim); margin-left: 10px; }
.rh-group-h span { font-size: .95rem; color: var(--rh-text-dim); }
.rh-group-note { font-size: .98rem; line-height: 1.5; color: var(--rh-text-dim); margin: 0 0 18px; max-width: 70ch; }
.rh-cards { list-style: none; margin: 0; padding: 0; display: grid; gap: 16px; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); }
.rh-card {
  --c: var(--rh-contrast);
  position: relative; display: flex; flex-direction: column; height: 100%%;
  background: var(--rh-paper); border: 1px solid var(--rh-line); border-radius: 14px; overflow: hidden;
  text-decoration: none; color: inherit; box-shadow: 0 2px 10px var(--rh-shadow);
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.rh-card-bc { --c: var(--rh-secondary); }
.rh-card::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 5px; background: var(--c); z-index: 2; }
.rh-card:hover { transform: translateY(-4px); box-shadow: 0 18px 36px var(--rh-shadow); border-color: color-mix(in srgb, var(--c) 60%%, transparent); }
.rh-thumb { aspect-ratio: 16 / 9; overflow: hidden; background: var(--rh-navy); }
.rh-thumb img { width: 100%%; height: 100%%; object-fit: cover; display: block; transition: transform .6s ease; }
.rh-card:hover .rh-thumb img { transform: scale(1.05); }
.rh-card-body { display: flex; flex-direction: column; gap: 6px; padding: 14px 16px 16px; flex: 1; }
.rh-card-body .rh-world { align-self: flex-start; }
.rh-card-body h4 { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.14rem; line-height: 1.25; margin: 0; }
.rh-card-body p { font-size: .92rem; line-height: 1.5; color: var(--rh-text-dim); margin: 0; }
.rh-card-body p em { font-style: italic; color: var(--rh-text); }
.rh-card-meta { display: flex; flex-wrap: wrap; gap: 6px; margin-top: auto; padding-top: 8px; }

/* ── the two neighbours: picture plates ── */
.rh-plates { padding: clamp(56px, 8vw, 104px) 0 clamp(24px, 4vw, 40px); }
.rh-plate-list { list-style: none; margin: clamp(26px, 4vw, 40px) 0 0; padding: 0; display: grid; gap: 16px; grid-template-columns: 1fr 1fr; }
.rh-plate {
  position: relative; isolation: isolate; overflow: hidden;
  display: flex; flex-direction: column; justify-content: flex-end; gap: 8px;
  min-height: clamp(320px, 30vw, 380px); padding: clamp(18px, 2.6vw, 28px);
  border-radius: 16px; text-decoration: none; color: var(--rh-ink-text);
  box-shadow: 0 18px 40px var(--rh-shadow);
  transition: transform .18s ease, box-shadow .18s ease;
}
.rh-plate:hover { transform: translateY(-3px); box-shadow: 0 26px 52px var(--rh-shadow); }
.rh-plate img { position: absolute; inset: 0; z-index: -2; width: 100%%; height: 100%%; object-fit: cover; transition: transform 1.4s cubic-bezier(.2,.7,.2,1); }
.rh-plate:hover img { transform: scale(1.04); }
.rh-plate::before {
  content: ''; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(180deg, transparent 0%%,
    color-mix(in srgb, var(--rh-navy) 30%%, transparent) 16%%,
    color-mix(in srgb, var(--rh-navy) 90%%, transparent) 40%%,
    color-mix(in srgb, var(--rh-navy) 96%%, transparent) 100%%);
}
.rh-plate .rh-kicker { color: var(--rh-ink-accent); margin: 0; }
.rh-plate h3 { font-family: 'Playfair Display', serif; font-weight: 900; font-size: clamp(1.6rem, 3vw, 2.2rem); line-height: 1.02; margin: 0; }
.rh-plate p { margin: 0; font-size: .98rem; line-height: 1.5; color: var(--rh-ink-text); max-width: 46ch; }
.rh-plate p b { font-weight: 700; }
.rh-plate-go { font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; font-size: .84rem; color: var(--rh-ink-accent); margin-top: 4px; }
@media (max-width: 760px) { .rh-plate-list { grid-template-columns: 1fr; } }

/* ── notes ── */
.rh-notes { padding: clamp(24px, 4vw, 40px) 0 clamp(64px, 9vw, 112px); }
.rh-notes-grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(16px, 2.4vw, 28px); }
.rh-note { background: var(--rh-card); border: 1px solid var(--rh-line); border-radius: 16px; padding: clamp(22px, 3vw, 34px); }
.rh-note h3 { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.36rem; margin: 0 0 10px; color: var(--rh-text); }
.rh-note p { margin: 0; line-height: 1.64; color: var(--rh-text-dim); }
.rh-note p + p { margin-top: 10px; }
.rh-note strong { color: var(--rh-text); font-weight: 700; }
.rh-note a { color: var(--rh-accent); font-weight: 700; }
@media (max-width: 760px) { .rh-notes-grid { grid-template-columns: 1fr; } }

/* ── closing band over the covers ── */
.rh-close { position: relative; isolation: isolate; overflow: hidden; background: var(--rh-ink); color: var(--rh-ink-text); }
.rh-close-art { position: absolute; inset: 0; z-index: -2; width: 100%%; height: 100%%; object-fit: cover; object-position: 50%% 50%%; }
.rh-close::after {
  content: ''; position: absolute; inset: 0; z-index: -1;
  background: radial-gradient(ellipse 70%% 90%% at 50%% 50%%, color-mix(in srgb, var(--rh-ink) 92%%, transparent) 30%%, color-mix(in srgb, var(--rh-ink) 70%%, transparent) 100%%);
}
.rh-close-in { padding: clamp(72px, 10vw, 140px) var(--rh-gut); max-width: 860px; margin: 0 auto; text-align: center; }
.rh-close .rh-kicker { color: var(--rh-ink-accent); }
.rh-close .rh-h2 { color: var(--rh-ink-text); }
.rh-close .rh-h2 em { color: var(--rh-ink-accent); }
.rh-close p { font-size: 1.1rem; line-height: 1.62; color: var(--rh-ink-text-dim); margin: 0 auto 30px; max-width: 54ch; }
.rh-close .rh-ctas { justify-content: center; }
.rh-close .rh-btn { background: var(--rh-ink-text); border-color: var(--rh-ink-text); color: var(--rh-ink); }
.rh-close .rh-btn:hover { background: var(--rh-ink-accent); border-color: var(--rh-ink-accent); }
.rh-close .rh-btn-quiet { background: transparent; color: var(--rh-ink-text); border-color: color-mix(in srgb, var(--rh-ink-text) 55%%, transparent); }
.rh-close .rh-btn-quiet:hover { background: var(--rh-ink-text); color: var(--rh-ink); }

@media (prefers-reduced-motion: reduce) {
  .rh *, .rh *::before, .rh *::after { animation: none !important; transition: none !important; }
}
</style>
<!-- RPG-HUB-CSS:end -->
"""


def css():
    tokens = '\n'.join('  --rh-%s: %s;' % (k, v) for k, v in PALETTE.items())
    return CSS % {'tokens': tokens}


def _pills(g, world=True):
    out = []
    if world:
        out.append('<span class="rh-pill rh-pill-%s">%s</span>'
                   % ('bc' if g['world'] == 'block-camp' else 'story',
                      'Block Camp' if g['world'] == 'block-camp' else 'Story'))
    out += ['<span class="rh-pill">%s</span>' % esc(x) for x in g['gram']]
    if g['level']:
        out.append('<span class="rh-pill">%s</span>' % esc(g['level'].replace('-', '–')))
    out.append('<span class="rh-pill rh-pill-free">Free</span>' if g['free']
               else '<span class="rh-pill">Pro</span>')
    return ''.join(out)


def _card(g):
    thumb = web_copy(g['cover'], os.path.splitext(os.path.basename(g['file']))[0].lower()
                     .replace(' ', '-')[:40])
    world = ('<span class="rh-pill rh-pill-%s rh-world">%s</span>'
             % (('bc', 'Block Camp') if g['world'] == 'block-camp' else ('story', 'Story')))
    blurb = seo.trim(g['blurb'], 190) if g['blurb'] else ''
    return ('<li><a class="rh-card%s" href="%s">'
            '<span class="rh-thumb"><img src="%s" alt="" loading="lazy" width="640" height="360"></span>'
            '<span class="rh-card-body">%s<h4>%s</h4><p>%s</p>'
            '<span class="rh-card-meta">%s</span></span></a></li>'
            % (' rh-card-bc' if g['world'] == 'block-camp' else '', esc(seo.quote(g['file'])),
               esc(thumb), world, g['title'], blurb, _pills(g, world=False)))


def _free_card(g):
    thumb = web_copy(g['cover'], 'free-' + os.path.splitext(os.path.basename(g['file']))[0]
                     .lower().replace(' ', '-')[:40], width=960, quality=80)
    where = 'Block Camp' if g['world'] == 'block-camp' else 'Story game'
    return ('<li><a class="rh-free-card" href="%s">'
            '<img src="%s" alt="" loading="lazy" width="960" height="540">'
            '<p class="rh-kicker">%s &middot; %s</p><h3>%s</h3><p>%s</p>'
            '<span class="rh-meta">%s</span></a></li>'
            % (esc(seo.quote(g['file'])), esc(thumb), where, esc(g['level'].replace('-', '–')),
               g['title'], seo.trim(g['blurb'], 120) if g['blurb'] else '',
               _pills(g, world=False)))


def render(rows, images):
    """(css, body, json-ld) for rpg.html. `rows` are the finished lessons."""
    games = load(rows, images)
    n = len(games)
    free = [g for g in games if g['free']]
    bc = [g for g in games if g['world'] == 'block-camp']
    levels = topics.level_span([{'level': g['level']} for g in games]).replace(' to ', ' to ')
    b = []

    # ── hero ──
    b.append('''<main>
<header class="rh-hero" aria-labelledby="rh-h1">
  <img class="rh-hero-img" src="%s" width="2048" height="873" alt="%s" fetchpriority="high">
  <div class="rh-hero-in">
    <div class="rh-hero-copy">
      <p class="rh-kicker">Role-playing games &middot; %s &middot; %s</p>
      <h1 class="rh-h1" id="rh-h1">Choose your words, <em>choose your ending</em></h1>
      <p class="rh-lede">%s branching adventures, from a voxel Oz to a Paris boardroom. Every choice is a question about English &mdash; a tense, a modal, a conditional &mdash; and the answer decides where the story goes. All of them keep score; most have more than one ending.</p>
      <ul class="rh-stats">
        <li><b>%d</b><span>games</span></li>
        <li class="rh-stat-free"><b>%d</b><span>free &mdash; no sign-in</span></li>
        <li><b>%d</b><span>in Block Camp</span></li>
      </ul>
      <div class="rh-ctas">
        <a class="rh-btn" href="#free">Start with a free one <span aria-hidden="true">&darr;</span></a>
        <a class="rh-btn rh-btn-quiet" href="#games">Every game, by level</a>
      </div>
    </div>
  </div>
</header>''' % (esc(seo.quote(HERO)), esc(HERO_ALT), esc(levels), plural(n, 'game'),
                words(n).capitalize(), n, len(free), len(bc)))

    # ── how a game works ──
    b.append('''<section class="rh-how" id="how" aria-labelledby="rh-how-h">
  <div class="rh-wrap">
    <div class="rh-sechead">
      <p class="rh-kicker">How a game works</p>
      <h2 class="rh-h2" id="rh-how-h">A story that <em>asks questions</em></h2>
      <p>Not a quiz with a picture on it. The grammar is inside the plot: the tense you pick is what happened, the modal you pick is how sure you are, and the story takes you at your word.</p>
    </div>
    <ol class="rh-steps">
      <li class="rh-step"><h3>Read the scene</h3><p>One picture, one moment in the story, a paragraph of text. In the Block Camp games the text waits behind a <em>glowing object</em>: click it and the panel pops out.</p></li>
      <li class="rh-step"><h3>Choose</h3><p>Two or three ways forward, and each one is a form of English &mdash; the tense that fits the time, the modal that fits the evidence, the conditional the plan needs.</p></li>
      <li class="rh-step"><h3>Live with it</h3><p>The right form moves the story on. A wrong one costs you &mdash; a point, a life, a clue &mdash; and in most games the story branches on it. At the end: a score, and an ending you earned.</p></li>
    </ol>
  </div>
</section>''')

    # ── the free ones ──
    b.append('''<section class="rh-free" id="free" aria-labelledby="rh-free-h">
  <div class="rh-wrap">
    <div class="rh-sechead">
      <p class="rh-kicker">No sign-in</p>
      <h2 class="rh-h2" id="rh-free-h">%s you can play <em>right now</em></h2>
      <p>Free, in full, on any device. Put one on the projector and see whether the room takes to it before you pay for anything.</p>
    </div>
    <ul class="rh-free-list">''' % words(len(free)).capitalize())
    for g in free:
        b.append('      ' + _free_card(g))
    b.append('    </ul>\n  </div>\n</section>')

    # ── every game, by level ──
    b.append('''<section class="rh-games" id="games" aria-labelledby="rh-games-h">
  <div class="rh-wrap">
    <div class="rh-sechead">
      <p class="rh-kicker">Every game</p>
      <h2 class="rh-h2" id="rh-games-h">%s games, <em>by level</em></h2>
      <p>Beginners first. The chips say what each game drills. <em>Block Camp</em> marks the voxel-built ones, which also carry a language switcher for the story text; <em>Story</em> is everything else, from a gaslit London to a Grand Prix pit wall.</p>
    </div>''' % words(n).capitalize())
    for i, (span, name, note) in enumerate(BANDS):
        group = [g for g in games if g['band'] == i]
        if not group:
            continue
        gfree = sum(1 for g in group if g['free'])
        meta = plural(len(group), 'game') + (' &middot; %d free' % gfree if gfree else '')
        b.append('    <div class="rh-group">\n      <div class="rh-group-h"><h3>%s<small>%s</small></h3><span>%s</span></div>\n      <p class="rh-group-note">%s</p>\n      <ul class="rh-cards">'
                 % (span, name, meta, note))
        for g in group:
            b.append('        ' + _card(g))
        b.append('      </ul>\n    </div>')
    b.append('  </div>\n</section>')

    # ── the two neighbours ──
    bc_all = [r for r in rows if r['file'].startswith(('blockcamp-', 'block-camp/'))]
    bc_free = sum(1 for r in bc_all if r.get('access') != 'pro')
    b.append('''<section class="rh-plates" id="more" aria-labelledby="rh-more-h">
  <div class="rh-wrap">
    <div class="rh-sechead">
      <p class="rh-kicker">Next door</p>
      <h2 class="rh-h2" id="rh-more-h">Where the games <em>come from</em></h2>
      <p>%s of the %s are Block Camp adventures, and the camp is more than its adventures. And if what you want is a conversation to have out loud rather than a story to play, the roleplays are on the shelf next to these.</p>
    </div>
    <ul class="rh-plate-list">
      <li><a class="rh-plate" href="block-camp.html">
        <img src="%s" alt="" loading="lazy" width="1600" height="900">
        <p class="rh-kicker">Block Camp &middot; %s in the camp</p>
        <h3>The voxel world, with a grammar climb beside the games</h3>
        <p>One grammar point per adventure, a glowing object on every picture, and the tenses two parts each on the trail &mdash; active on the way up, passive on the way down. <b>%s, %d free.</b></p>
        <span class="rh-plate-go">Walk into camp &rarr;</span>
      </a></li>
      <li><a class="rh-plate" href="library.html#cat=Speaking+activity">
        <img src="%s" alt="" loading="lazy" width="1400" height="1050">
        <p class="rh-kicker">Speaking activities</p>
        <h3>Not a game &mdash; a roleplay</h3>
        <p>Scripted speaking practice for the classroom: a football press conference, a case file, a COO briefing, an escape room. Roles, cards and a conversation to have out loud.</p>
        <span class="rh-plate-go">Open the roleplays &rarr;</span>
      </a></li>
    </ul>
  </div>
</section>''' % (words(len(bc)).capitalize(), plural(n, 'game'),
                esc(web_copy('BlockCamp/hub-hero.jpg', 'plate-block-camp', width=1200, quality=80)),
                plural(len(bc_all), 'lesson'), plural(len(bc_all), 'lesson'), bc_free,
                esc(web_copy('CaseFileSilverPines/silver-pines-cover.jpg', 'plate-roleplays', width=1200, quality=80))))

    # ── notes ──
    b.append('''<section class="rh-notes" aria-label="Notes">
  <div class="rh-wrap">
    <div class="rh-notes-grid">
      <div class="rh-note">
        <h3>Teaching this?</h3>
        <p>Put it on the projector and let the room vote on every choice: one learner reads, one clicks, everyone argues the grammar before the click. Some games are a single lesson; Wild Frame is a two-hour quest and says so on its cover.</p>
        <p>Every game explains a wrong answer before it moves on, so the argument is worth having. <a href="pricing.html">Plans &amp; what&rsquo;s free &rarr;</a></p>
      </div>
      <div class="rh-note">
        <h3>Playing alone?</h3>
        <p>Every game keeps a score and the endings are worth a second run &mdash; a different tense at the fork is a different story. The Block Camp games translate their story text into other languages from the panel; the questions stay in English.</p>
        <p>The free ones need nothing. The rest open with a Pro sign-in, which also opens <a href="library.html">every other lesson on the site</a>.</p>
      </div>
    </div>
  </div>
</section>''')

    # ── closing band ──
    art, art_h = mosaic([g['cover'] for g in games])
    b.append('''<section class="rh-close" aria-labelledby="rh-close-h">
  <img class="rh-close-art" src="%s" alt="" loading="lazy" width="1536" height="%d">
  <div class="rh-close-in">
    <p class="rh-kicker">Free and Pro</p>
    <h2 class="rh-h2" id="rh-close-h">%s are free. <em>The rest come with Pro</em></h2>
    <p>One subscription opens every game here and every lesson on the site. The free ones stay free, sign-in or not.</p>
    <div class="rh-ctas">
      <a class="rh-btn" href="pricing.html">Plans &amp; prices</a>
      <a class="rh-btn rh-btn-quiet" href="#free">Back to the free games</a>
    </div>
  </div>
</section>
</main>''' % (esc(art), art_h, words(len(free)).capitalize()))

    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': '%s/index.html' % SITE},
            {'@type': 'ListItem', 'position': 2, 'name': 'Role-playing games',
             'item': '%s/%s' % (SITE, PAGE)}]},
        {'@type': 'ItemList', 'name': 'English role-playing games',
         'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1,
              'url': '%s/%s' % (SITE, seo.quote(g['file'])),
              'name': html.unescape(re.sub('<[^>]+>', '', g['title']))}
             for i, g in enumerate(games)]}]}
    gone = prune()
    print('  rpg.html: %d games (%d free, %d Block Camp), levels %s%s'
          % (n, len(free), len(bc), levels, '; pruned %s' % ', '.join(gone) if gone else ''))
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
    m = Image.open(src).convert('RGB').resize((600, 256))
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
        print('  %-14s on %-9s %5.2f:1 (min %.1f) %s  %s'
              % (fg, bg, r, need, 'PASS' if ok else 'FAIL', what))
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
