# -*- coding: utf-8 -*-
"""Forbes English — SEO metadata generator.

    python3 tools/seo.py            # write everything
    python3 tools/seo.py --check    # report, change nothing

Run it after any lesson build. It is idempotent: every page gets one
block fenced by `<!-- SEO:start -->` / `<!-- SEO:end -->`, and a re-run
replaces that block rather than adding a second one.

What it does, and why each part earns its place.

**The site had no meta descriptions, no Open Graph, no structured data,
two canonicals across 246 pages, and no sitemap.** Titles existed but
carried no brand and, on 77 lessons, no level — and level is exactly what
people type ("A2 English lesson", "B2 grammar exercises").

**Nothing here can be discovered by a crawler.** `library.html` builds
its list from Supabase in the browser, so the HTML that Google fetches
contains five links and 77 words. 236 lessons sit behind that, reachable
only by a URL you already know. This writes a static list into the page
(the JS still replaces it for people) and a sitemap listing every one.

**A paywalled page still has to say what it is.** 195 lessons are Pro,
and the Worker serves them all the same `locked.html`. Search engines
therefore see 195 identical, keyword-free pages. The fix is not to show
Google something a visitor cannot see — that is cloaking — but to make
the gate page itself carry the lesson's own title, description and
`isAccessibleForFree: false`, which is Google's documented way of saying
"gated on purpose, index the description". The Worker does the injection
at the edge; this script produces the per-lesson metadata it reads.

Data comes from the `lessons` table (title, level, access are
authoritative there — see HOUSE-STYLE §11.2) with `tools/lessons.json` as
an offline fallback so a build never depends on the network.
"""
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://forbesenglish.com'
BRAND = 'Forbes English'
CACHE = os.path.join(ROOT, 'tools', 'lessons.json')
DEFAULT_IMAGE = '/logo-forbes-english_1.png'

SUPABASE_URL = 'https://tusioporxpjtegjlqkkb.supabase.co'
# The same anon key the site ships in sb-client.js. Public by design.
SUPABASE_ANON = (
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6'
    'InR1c2lvcG9yeHBqdGVnamxxa2tiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODYxMjk2'
    'NjksImV4cCI6MjEwMTcwNTY2OX0.9jPi4_Y6IfcUdzqfPzPJ8XsBCSXPuLvtCN8wWFMiLe4')

START, END = '<!-- SEO:start -->', '<!-- SEO:end -->'
LIST_START, LIST_END = '<!-- SEO:lessons:start -->', '<!-- SEO:lessons:end -->'

# Pages that are not lessons but must still be indexable and described.
# A fourth element is optional: the page's own share image. Without one a
# page falls back to the site logo, which is right for index and pricing and
# wrong for any page that has real artwork of its own.
# The question bank's own size is data, not prose. Reading it from the
# builder's source is the only way this description cannot go stale — it
# already did once: the bank grew from 48 prompts to 136 and this file
# quietly rewrote the page's meta description back to "48".
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from ielts_bank_data import TOPICS as _BANK_TOPICS
    _BANK_N = sum(len(t['prompts']) for t in _BANK_TOPICS)
    _BANK_T = len(_BANK_TOPICS)
except Exception:                      # the tool must still run without it
    _BANK_N, _BANK_T = 136, 17

PAGES = {
    'index.html': ('English lessons that are actually lessons',
                   'Interactive English lessons at A1 to C2 — grammar, '
                   'vocabulary and speaking, built as 16:9 decks you can '
                   'teach from or work through alone.', 1.0),
    'library.html': ('Lesson library',
                     'Every Forbes English lesson, by level and topic: '
                     'A1 to C2 grammar, vocabulary, exam prep and '
                     'business English.', 0.9),
    'pricing.html': ('Plans and pricing',
                     'What a Forbes English subscription costs, and which '
                     'lessons are free forever.', 0.7),
    'ielts.html': ('IELTS Academic',
                   'The IELTS Academic route — Writing, Speaking, Listening, '
                   'Reading and the vocabulary that feeds them, in the order '
                   'they should be taught.', 0.9, '/ielts-model-answers/hero.jpg'),
    'ielts-writing.html': ('IELTS Academic Writing',
                   'A twelve-lesson route through IELTS Academic Writing — '
                   'Task 1 reports and Task 2 essays, in the order they '
                   'should be taught.', 0.9, '/ielts-model-answers/hero.jpg'),
    'ielts-speaking.html': ('IELTS Speaking',
                   'The IELTS Speaking route — how long an answer should be, '
                   'how to extend one without waffling, and how to fill the '
                   'two minutes of the long turn.', 0.9, '/ielts-speaking/hero.jpg'),
    'ielts-listening.html': ('IELTS Listening',
                   'The IELTS Listening route — thirty minutes, four sections, '
                   'forty questions, and every recording played once. How the '
                   'test is built, and what to do in the seconds before each '
                   'section starts.', 0.9, '/ielts-listening/hero.jpg'),
    'level-checker.html': ('Level Checker',
                           'A free adaptive placement test for English '
                           'tenses. Six questions a level, A1 to C1, and it '
                           'tells you which lesson to start on.', 0.8),
    'ielts-question-bank.html': ('IELTS Academic Writing Task 2: Question Bank & Ideas',
                                 f'{_BANK_N} IELTS Academic Writing Task 2 questions '
                                 f'across {_BANK_T} topics, sorted by essay '
                                 'type, each topic with arguments for both '
                                 'sides. Free.', 0.9,
                                 '/ielts-question-bank/hero.jpg'),
}
SKIP = {'locked.html', 'account.html', 'index_1.html', 'front-page.html'}


# ── data ───────────────────────────────────────────────────────────────
def lessons():
    """The lessons table, live if reachable and from cache if not."""
    try:
        req = urllib.request.Request(
            SUPABASE_URL + '/rest/v1/lessons'
            # Must match sbGetLessons() in sb-client.js. The static list this
            # writes into <div id="grid"> is what a crawler sees and what a
            # visitor gets when Supabase is unreachable, so if the two orders
            # disagree the fallback silently shows a different library.
            '?select=file,title,level,access,deck,video,created_at,sort_order'
            '&order=sort_order.asc.nullslast,id.asc',
            headers={'apikey': SUPABASE_ANON,
                     'Authorization': 'Bearer ' + SUPABASE_ANON})
        rows = json.loads(urllib.request.urlopen(req, timeout=20).read())
        with open(CACHE, 'w', encoding='utf-8') as fh:
            json.dump(rows, fh, ensure_ascii=False, indent=1)
        return rows, 'supabase'
    except Exception as e:                                  # noqa: BLE001
        print('  ! supabase unreachable (%s) — using %s' % (e, CACHE))
        return json.load(open(CACHE, encoding='utf-8')), 'cache'


def lesson_images():
    """The thumbnail map that library.html already maintains."""
    s = open(os.path.join(ROOT, 'library.html'), encoding='utf-8').read()
    m = re.search(r'const LESSON_IMAGES = \{(.*?)\n\};', s, re.S)
    if not m:
        return {}
    return dict(re.findall(r'"([^"]+\.html)"\s*:\s*"([^"]+)"', m.group(1)))


# ── per-page text ──────────────────────────────────────────────────────
def clean(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    t = t.replace('—', '—').replace('’', '’')
    return re.sub(r'\s+', ' ', t).strip()


def describe(src, row):
    """The best one-line description the page can supply about itself.

    A deck states its own promise on the cover, which is exactly what a
    description should be, so that is the first choice. Legacy pages get
    their first real paragraph. Only when a page says nothing about
    itself do we fall back to a built sentence — a generic description on
    every page is worth little more than none.

    The block this script wrote last time is stripped before any of that
    runs. It used to be left in place, so the third pattern below matched
    seo.py's OWN previous output and handed it straight back: whatever
    description a page was given on its first pass was frozen there for
    good, and no amount of rewriting the page could improve it. The
    grammar test carried "Forbes EnglishGrammar · Full Test 0 / 45 0 / 45
    ENGLISH Cheat Sheet Test..." — scraped chrome and flag emoji — as its
    Google snippet for exactly that reason."""
    src = re.sub(re.escape(START) + '.*?' + re.escape(END), ' ', src, flags=re.S)
    for pat in (r'coverSub\s*:\s*[\'"](.*?)[\'"]\s*,',
                r'class="cover-sub"[^>]*>(.*?)</p>',
                r'<meta name="description" content="([^"]+)"'):
        m = re.search(pat, src, re.S)
        if m and len(clean(m.group(1))) > 30:
            return trim(clean(m.group(1)), 155)

    # A legacy page's standfirst. Deliberately shorter than a paragraph, so it
    # gets a lower floor than the 60 below -- without this, a page whose only
    # self-description is a 54-character subtitle falls all the way through to
    # the built sentence.
    m = re.search(r'<p[^>]*class="(?:sub|subtitle|lede|standfirst)[^"]*"[^>]*>(.*?)</p>',
                  src, re.S)
    if m and len(clean(m.group(1))) > 24:
        return trim(clean(m.group(1)), 155)

    body = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', src, flags=re.S)
    # `<p[^>]*>` also matches <path>, <picture>, <pre> and <progress>. Every
    # page whose logo is an inline SVG opens with a <path>, so the "first
    # paragraph" ran from that path to the first real </p> further down and
    # swallowed the whole header on the way. The grammar test's Google snippet
    # was "Forbes EnglishGrammar · Full Test 0 / 45 0 / 45 ENGLISH ...
    # 🇬🇧English 🇩🇪Deutsch 🇮🇹Italiano" for precisely this reason.
    for m in re.finditer(r'<p(?:\s[^>]*)?>(.*?)</p>', body, re.S):
        t = clean(m.group(1))
        if len(t) > 60 and not t.lower().startswith(('cookie', 'loading')):
            return trim(t, 155)

    lvl = ('%s ' % row['level']) if row.get('level') else ''
    return trim('An interactive %sEnglish lesson from %s: %s.'
                % (lvl, BRAND, clean(row['title'])), 155)


GRAMMAR = re.compile(
    r'\b(verb|noun|adjective|adverb|tense|plural|singular|preposition|'
    r'article|pronoun|comparative|superlative|modal|passive|active|clause|'
    r'infinitive|gerund|participle|conditional|subject|object|question|'
    r'negative|countable|uncountable|past|present|future|perfect|continuous|'
    r'simple|syllable|contraction|register|collocation|phrasal)\b', re.I)


def rules(src, limit=8):
    """The statements a deck makes about the language it teaches.

    GEO, not SEO. An answer engine quotes a self-contained sentence that
    resolves a question, and a deck's rule cards already are exactly
    that — "Short adjectives take -er and then than" is quotable as it
    stands. They sit in `<p class="prose"><strong>` on teaching slides,
    which is a place no machine would look, so they get lifted into
    `teaches` where one will."""
    out = []
    for m in re.finditer(r'<p class="prose"><strong[^>]*>(.*?)</strong></p>', src, re.S):
        raw, t = m.group(1), clean(m.group(1))
        # A rule, not a scene-setting sentence: short enough to quote, long
        # enough to say something, and about the language rather than the
        # story. A deck's narrative cards ("You are a prisoner in B Block")
        # sit in the same markup and would otherwise be published as things
        # the lesson teaches, which is worse than publishing nothing.
        if not (40 < len(t) < 180) or t.endswith('?'):
            continue
        marked = re.search(r'<(em|strong|code)\b', raw)
        if marked or GRAMMAR.search(t):
            out.append(t)
    seen, uniq = set(), []
    for t in out:
        if t.lower() not in seen:
            seen.add(t.lower())
            uniq.append(t)
    return uniq[:limit]


def trim(t, n):
    if len(t) <= n:
        return t
    cut = t[:n].rsplit(' ', 1)[0]
    return cut.rstrip(' ,.;:—-') + '…'


def page_title(row):
    """Title, level, brand — in that order, because the first two are what
    someone actually searched for. Kept near 60 characters so Google shows
    the whole thing."""
    base = clean(row['title'])
    lvl = row.get('level')
    if lvl and lvl.lower() not in base.lower():
        base = '%s (%s)' % (base, lvl)
    full = '%s | %s' % (base, BRAND)
    return full if len(full) <= 65 else base


def esc(t):
    return html.escape(t, quote=True)


# ── the block ──────────────────────────────────────────────────────────
def seo_block(url, title, desc, image, row=None, noindex=False):
    out = [START]
    if noindex:
        # A lesson with no hero has not been rebuilt to house style yet.
        # The library shows it as "Coming soon" and will not link to it, so
        # the page must not be an entry point either — an indexed result
        # that lands on an unfinished lesson is worse than no result.
        # follow, not none: the internal links on it are still worth
        # crawling, and this reverses the moment artwork lands.
        out.append('<meta name="robots" content="noindex,follow">')
    out += ['<meta name="description" content="%s">' % esc(desc),
           '<link rel="canonical" href="%s">' % url,
           '<meta property="og:type" content="%s">'
           % ('article' if row else 'website'),
           '<meta property="og:site_name" content="%s">' % BRAND,
           '<meta property="og:title" content="%s">' % esc(title),
           '<meta property="og:description" content="%s">' % esc(desc),
           '<meta property="og:url" content="%s">' % url,
           '<meta property="og:image" content="%s%s">' % (SITE, image),
           '<meta property="og:locale" content="en_GB">',
           '<meta name="twitter:card" content="summary_large_image">',
           '<meta name="twitter:title" content="%s">' % esc(title),
           '<meta name="twitter:description" content="%s">' % esc(desc),
           '<meta name="twitter:image" content="%s%s">' % (SITE, image)]

    if row:
        free = row['access'] != 'pro'
        ld = {
            '@context': 'https://schema.org',
            '@type': 'LearningResource',
            'name': clean(row['title']),
            'description': desc,
            'url': url,
            'inLanguage': 'en',
            'learningResourceType': 'lesson',
            'interactivityType': 'active',
            'isAccessibleForFree': free,
            'image': SITE + image,
            'provider': {'@type': 'Organization', 'name': BRAND,
                         'url': SITE + '/'},
            'isPartOf': {'@type': 'Course', 'name': '%s lesson library' % BRAND,
                         'url': '%s/library.html' % SITE},
        }
        if row.get('level'):
            ld['educationalLevel'] = row['level']
        taught = row.get('_rules') or []
        if taught:
            ld['teaches'] = taught
        elif row.get('level'):
            ld['teaches'] = '%s English' % row['level']
        if row.get('created_at'):
            ld['datePublished'] = row['created_at'][:10]
        if not free:
            # Google's documented signal for subscription content: the
            # page is gated deliberately, and this is the part that is
            # gated. Without it, a gate page looks like cloaking or thin
            # content; with it, the description is indexed on its merits.
            ld['hasPart'] = {'@type': 'WebPageElement',
                             'isAccessibleForFree': False,
                             'cssSelector': '.paywalled'}
        out.append('<script type="application/ld+json">%s</script>'
                   % json.dumps(ld, ensure_ascii=False, separators=(',', ':')))
    out.append(END)
    return '\n'.join(out)


ORG_LD = {
    '@context': 'https://schema.org',
    '@graph': [
        {'@type': 'Organization', '@id': SITE + '/#org', 'name': BRAND,
         'url': SITE + '/', 'logo': SITE + DEFAULT_IMAGE,
         'description': 'Interactive English lessons from A1 to C2, built as '
                        '16:9 decks for teachers and independent learners.',
         'knowsLanguage': ['en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar',
                           'zh', 'ja']},
        {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/',
         'name': BRAND, 'publisher': {'@id': SITE + '/#org'},
         'inLanguage': 'en'},
        {'@type': 'EducationalOrganization', '@id': SITE + '/#school',
         'name': BRAND, 'url': SITE + '/',
         'parentOrganization': {'@id': SITE + '/#org'}},
    ],
}


def inject(src, block, title):
    """Replace the fenced block, or insert one after the viewport tag."""
    src = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title,
                 src, count=1, flags=re.S)
    if START in src and END in src:
        return re.sub(re.escape(START) + '.*?' + re.escape(END), lambda _: block,
                      src, count=1, flags=re.S)
    # A page with no fence but with SEO tags already in its head was written by
    # hand. Inserting here would leave it with TWO canonicals, two og:titles and
    # two LearningResource blocks, and nothing would say so — the run just
    # reports "rewrote 1 page". Refuse, and name the file: the fix is to wrap
    # the hand-written tags in the fence once, after which this is a normal
    # generated block. `forbes-english-dinosaur-minecraft.html` sat like this
    # for weeks and was only found because a session diffed a dry run.
    if re.search(r'<(?:link[^>]+rel="canonical"|meta[^>]+property="og:)', src):
        return None
    anchor = re.search(r'<meta name="viewport"[^>]*>', src)
    if anchor:
        i = anchor.end()
        return src[:i] + '\n' + block + src[i:]
    return re.sub(r'<head>', '<head>\n' + block, src, count=1)


# ── outputs ────────────────────────────────────────────────────────────
ROBOTS = """# forbesenglish.com
#
# Search engines: welcome, everything below is for you.
# AI: read and cite, but do not train. The split is deliberate — the
# crawlers that send readers back here are allowed; the ones that only
# absorb are not. See the Content-Signal header for the same statement in
# the form the EU DSM Directive recognises.

User-agent: *
Allow: /
Disallow: /account.html
Disallow: /api/

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# ── retrieval and citation: allowed, they link back ──
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: Claude-User
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /

# ── bulk training scrapers: not allowed ──
User-agent: GPTBot
Disallow: /
User-agent: ClaudeBot
Disallow: /
User-agent: CCBot
Disallow: /
User-agent: Google-Extended
Disallow: /
User-agent: Applebot-Extended
Disallow: /
User-agent: Bytespider
Disallow: /
User-agent: meta-externalagent
Disallow: /
User-agent: Amazonbot
Disallow: /

Sitemap: %s/sitemap.xml
""" % SITE


def coming_soon(row, images):
    """A lesson with no hero image is one that has not been rebuilt yet.

    That single fact is the whole rule, and it is derived rather than
    stored: the moment a hero lands in LESSON_IMAGES the lesson becomes
    available again, with no second place to remember to update. Nothing
    here needs a column in the catalogue."""
    return row['file'] not in images


def sitemap(rows, images):
    """Every lesson that is finished, free and Pro alike.

    A Pro lesson belongs in here: its gate page carries a real title and
    description and declares itself gated, so it is a legitimate result.
    Priority leans towards the free ones because those are what a new
    visitor can actually read."""
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.w3.org/1999/xhtml/../../schemas/sitemap"'
           .replace('http://www.w3.org/1999/xhtml/../../schemas/sitemap',
                    'http://www.sitemaps.org/schemas/sitemap/0.9') +
           ' xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']

    def url(loc, lastmod, prio, img=None):
        e = ['  <url>', '    <loc>%s</loc>' % loc]
        if lastmod:
            e.append('    <lastmod>%s</lastmod>' % lastmod)
        e.append('    <changefreq>monthly</changefreq>')
        e.append('    <priority>%.1f</priority>' % prio)
        if img:
            e.append('    <image:image><image:loc>%s%s</image:loc>'
                     '</image:image>' % (SITE, img))
        e.append('  </url>')
        return e

    for f, meta in PAGES.items():
        prio = meta[2]; img = meta[3] if len(meta) > 3 else None
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            out += url('%s/%s' % (SITE, f),
                       time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(p))),
                       prio, img)
    for r in rows:
        p = os.path.join(ROOT, r['file'])
        if not os.path.exists(p) or coming_soon(r, images):
            continue
        img = images.get(r['file'])
        out += url('%s/%s' % (SITE, quote(r['file'])),
                   (r.get('created_at') or '')[:10] or
                   time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(p))),
                   0.8 if r['access'] != 'pro' else 0.6,
                   '/' + quote(img) if img else None)
    out.append('</urlset>')
    return '\n'.join(out)


def quote(p):
    return urllib.parse.quote(p)


def llms_txt(rows, index, images):
    """`/llms.txt` — the map an answer engine reads instead of crawling.

    Not a search-engine file. The convention is markdown: what the site
    is, then every page worth citing with one line saying what it covers,
    so a model that has fetched one URL can see the shape of the rest
    without guessing. Free lessons are listed first and marked, because
    an engine recommending a page a reader cannot open is worse for us
    than not being recommended at all."""
    rows = [r for r in rows if not coming_soon(r, images)]
    free = [r for r in rows if r['access'] != 'pro']
    pro = [r for r in rows if r['access'] == 'pro']
    out = ['# %s' % BRAND, '',
           '> Interactive English lessons from A1 to C2 — grammar, vocabulary, '
           'business English and exam preparation. Each lesson is a 16:9 deck '
           'that a teacher can present from or a learner can work through '
           'alone: the rule is stated on the slide, then practised, then '
           'produced in a speaking and writing task. Many carry a language '
           'switcher covering German, Spanish, French, Italian, Portuguese, '
           'Russian, Arabic, Chinese and Japanese; the English being taught '
           'stays in English.', '',
           'Levels follow the CEFR (A1, A2, B1, B2, C1, C2). Lessons marked '
           '*subscribers* are behind a subscription — the page describes the '
           'lesson and is free to read; the exercises are not.', '']

    def section(name, items):
        out.append('## %s' % name)
        out.append('')
        for r in sorted(items, key=lambda x: clean(x['title'])):
            meta = index.get(r['file'], {})
            desc = meta.get('description', '')
            lvl = r.get('level')
            out.append('- [%s](%s/%s)%s: %s' % (
                clean(r['title']), SITE, quote(r['file']),
                ' — %s' % lvl if lvl else '', trim(desc, 140)))
        out.append('')

    section('Free lessons', free)
    section('Subscriber lessons', pro)
    out += ['## Site', '',
            '- [Lesson library](%s/library.html): every lesson, filterable by '
            'level and topic.' % SITE,
            '- [Plans](%s/pricing.html): what a subscription costs and what '
            'stays free.' % SITE,
            '- [Level Checker](%s/level-checker.html): a free adaptive '
            'placement test for the tenses, A1 to C1, that names the lesson '
            'to start on.' % SITE, '']
    return '\n'.join(out)


def crawlable_list(rows, images):
    """A plain list of every lesson, in the HTML, for crawlers and for
    anyone without JavaScript. The library's own script replaces it with
    the interactive grid the moment it runs, so nobody sees this — but it
    is the only thing standing between a crawler and 236 dead ends."""
    by_level = {}
    for r in rows:
        if coming_soon(r, images):
            continue
        by_level.setdefault(r.get('level') or 'All levels', []).append(r)
    order = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'A2-C1', 'All levels']
    # It is styled because it is not only a crawler's view: when Supabase is
    # unreachable the grid never renders, and this list is what the visitor
    # gets instead. It used to be a blank page.
    out = [LIST_START,
           '<style>#seo-lesson-index{grid-column:1/-1;font-family:Lato,sans-serif}'
           '#seo-lesson-index h2{font-family:"Playfair Display",serif;font-size:1.5rem;'
           'margin:8px 0 4px}#seo-lesson-index h3{font-family:"Barlow Condensed",sans-serif;'
           'letter-spacing:.08em;text-transform:uppercase;font-size:.95rem;color:#5d6f64;'
           'margin:18px 0 6px}#seo-lesson-index ul{columns:3;column-gap:32px;list-style:none;'
           'padding:0}#seo-lesson-index li{break-inside:avoid;margin:0 0 6px;font-size:.95rem}'
           '#seo-lesson-index a{color:#14301f;text-decoration:none;border-bottom:1px solid #c8d4c8}'
           '#seo-lesson-index a:hover{border-color:#b8962e}'
           '@media(max-width:900px){#seo-lesson-index ul{columns:1}}</style>',
           '<div id="seo-lesson-index">',
           '<h2>Every English lesson, by level</h2>']
    for lvl in sorted(by_level, key=lambda x: (order.index(x) if x in order
                                               else 99, x)):
        out.append('<h3>%s</h3>\n<ul>' % esc(lvl))
        for r in sorted(by_level[lvl], key=lambda x: clean(x['title'])):
            out.append('<li><a href="/%s">%s</a>%s</li>'
                       % (quote(r['file']), esc(clean(r['title'])),
                          '' if r['access'] != 'pro' else ' — subscribers'))
        out.append('</ul>')
    out += ['</div>', LIST_END]
    return '\n'.join(out)


# ── run ────────────────────────────────────────────────────────────────
def main(check=False):
    rows, source = lessons()
    images = lesson_images()
    print('  lessons: %d (from %s) · thumbnails: %d' % (len(rows), source,
                                                        len(images)))
    changed = skipped = 0
    unfenced = []
    index = {}

    for r in rows:
        f = os.path.join(ROOT, r['file'])
        if not os.path.exists(f) or r['file'] in SKIP:
            skipped += 1
            continue
        src = open(f, encoding='utf-8', errors='ignore').read()
        title = page_title(r)
        desc = describe(src, r)
        r = dict(r, _rules=rules(src))
        img = images.get(r['file'])
        soon = coming_soon(r, images)
        img = '/' + quote(img) if img else DEFAULT_IMAGE
        url = '%s/%s' % (SITE, quote(r['file']))
        new = inject(src, seo_block(url, title, desc, img, r, noindex=soon),
                     esc(title))
        if new is None:
            unfenced.append(r['file'])
            new = src            # still indexed below; only the write is skipped
        # The plain title, not `title`. The Worker builds the gate page from
        # this row and adds the brand itself, so handing it the already
        # brand-suffixed <title> put "| Forbes English" inside the gate's own
        # <h1> and made its <title> say it twice. It read that way on 194 of
        # the 260 entries — the other 66 only escaped because page_title()
        # drops the brand when the line would run past 65 characters, which is
        # why it looked like a handful of odd pages rather than the default.
        index[r['file']] = {'title': clean(r['title']), 'description': desc,
                            'level': r.get('level'), 'image': img,
                            'access': r['access']}
        # The Worker reads lesson-meta.json to build each gate page. The
        # flag is what lets it serve a "coming soon" page rather than an
        # unfinished lesson; the library derives the same state itself.
        if soon:
            index[r['file']]['coming_soon'] = True
        if new != src:
            changed += 1
            if not check:
                open(f, 'w', encoding='utf-8').write(new)

    for f, meta in PAGES.items():
        t, d = meta[0], meta[1]
        page_img = meta[3] if len(meta) > 3 else DEFAULT_IMAGE
        p = os.path.join(ROOT, f)
        if not os.path.exists(p):
            continue
        src = open(p, encoding='utf-8').read()
        title = '%s | %s' % (t, BRAND)
        new = inject(src, seo_block('%s/%s' % (SITE, f), title, d,
                                    page_img), esc(title))
        if new is None:
            unfenced.append(f)
            skipped += 1
            continue
        if f == 'index.html':
            # One place where the site says what it is and who runs it.
            # Both Google and an answer engine resolve the brand from here.
            org = ('<script type="application/ld+json">%s</script>'
                   % json.dumps(ORG_LD, ensure_ascii=False,
                                separators=(',', ':')))
            new = new.replace(END, org + '\n' + END, 1)
        if f == 'library.html':
            # Inside the grid the script empties on start-up, not appended to
            # the end of the page. A crawler reads it; a visitor never sees it,
            # because `grid.innerHTML = ''` clears it the moment the real cards
            # are ready. Putting it after </body> content would leave a raw
            # list of 236 links sitting under the library for everyone.
            new = re.sub(re.escape(LIST_START) + '.*?' + re.escape(LIST_END) + r'\n?',
                         '', new, flags=re.S)
            lst = crawlable_list(rows, images)
            new = re.sub(r'(<div class="grid" id="grid">)(.*?)(</div>)',
                         lambda m: m.group(1) + '\n' + lst + '\n' + m.group(3),
                         new, count=1, flags=re.S)
        if new != src:
            changed += 1
            if not check:
                open(p, 'w', encoding='utf-8').write(new)

    if not check:
        open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8').write(ROBOTS)
        open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write(
            sitemap(rows, images))
        # The Worker reads this to build a real gate page per lesson.
        open(os.path.join(ROOT, 'lesson-meta.json'), 'w',
             encoding='utf-8').write(json.dumps(index, ensure_ascii=False,
                                                indent=0, sort_keys=True))
        open(os.path.join(ROOT, 'llms.txt'), 'w',
             encoding='utf-8').write(llms_txt(rows, index, images))
    print('  %s %d page(s); skipped %d' %
          ('would rewrite' if check else 'rewrote', changed, skipped))
    if unfenced:
        print('  ! %d page(s) carry hand-written SEO tags with no '
              '<!-- SEO:start --> fence — NOT touched, or this run would have '
              'given each of them a second canonical and a second og:title:'
              % len(unfenced))
        for f in unfenced:
            print('      %s' % f)
        print('    Wrap the existing tags in the fence once, then re-run.')
    soon = [r for r in rows if coming_soon(r, images)]
    print('  coming soon (no hero): %d — noindexed, and out of the sitemap, '
          'the crawlable index and llms.txt' % len(soon))
    print('  sitemap: %d urls · robots.txt · llms.txt · lesson-meta.json (%d)'
          % (len(rows) - len(soon) + len(PAGES), len(index)))
    return changed


if __name__ == '__main__':
    sys.exit(0 if main('--check' in sys.argv) >= 0 else 1)
