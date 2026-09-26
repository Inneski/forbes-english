# -*- coding: utf-8 -*-
"""Build the topic hub pages: `grammar.html` and one page per topic.

    python3 tools/build_hubs.py          # then python3 tools/seo.py, always

Why these pages exist: a lesson page is written for the student who is
already in the room. A hub page is written for the person who typed
"present perfect exercises B1" into a search box and has never heard of
us. It explains the grammar point in plain sentences, then lists every
lesson on it by level, free ones first. The explanation is what ranks; the
list is what converts.

Every hub is generated from `tools/topics.py` (the copy and the
classifier) and the catalogue (`seo.lessons()`), so adding a lesson to
Supabase and re-running this puts it on the right hub with no hand edit.
The pages share the IELTS route page's stylesheet and top band, lifted
from `ielts.html` at build time so the chrome cannot drift.

The SEO fence is left empty for `tools/seo.py` to fill — it treats each
hub as one of its PAGES and writes the title, description, canonical and
Open Graph block. Run it after this, every time.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo                                   # noqa: E402
import topics                                # noqa: E402

ROOT = seo.ROOT
SITE = seo.SITE

STYLE_EXTRA = """
/* ── hub-only ── */
.prose { max-width: 62ch; }
.prose p { font-size: 1.04rem; line-height: 1.66; color: var(--ink); margin: 0 0 14px; }
.prose p em { font-style: italic; color: var(--green-lift); }
.prose p strong { font-weight: 700; }
.prose a { color: var(--gold-deep); }
.hero-side { display: grid; gap: 16px; align-content: start; }
.facts { list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; }
.facts li { background: #fff; border: 1px solid rgba(20,48,31,0.10); border-radius: 10px; padding: 10px 14px; font-size: .95rem; line-height: 1.45; }
.facts li b { font-family: 'Barlow Condensed', sans-serif; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; font-size: .74rem; color: var(--gold-deep); display: block; margin-bottom: 2px; }
.levelhead { display: flex; align-items: baseline; gap: 12px; margin: 26px 0 12px; }
.levelhead h3 { font-family: 'Barlow Condensed', sans-serif; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; font-size: 1rem; color: var(--green-lift); margin: 0; }
.levelhead span { font-size: .9rem; color: var(--muted); }
.step-n.lvl { font-size: 1.25rem; }
.tag-free { background: var(--gold-bright); color: var(--green-deep); }
.chips { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
.chip { font-family: 'Barlow Condensed', sans-serif; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; font-size: .78rem; color: var(--green-deep); background: #fff; border: 1px solid rgba(20,48,31,0.14); border-radius: 20px; padding: 6px 13px; text-decoration: none; }
.chip:hover { border-color: var(--gold); background: var(--gold-pale); }
.chip small { font-weight: 600; color: var(--muted); margin-left: 4px; }
/* the tense colour, as on grammar.html's cards: a swatch, never a text colour */
.tswatch { display: inline-block; width: .85em; height: .85em; border-radius: 3px; background: var(--tc); vertical-align: -.08em; margin-right: .5em; }
.chip .tswatch { width: .7em; height: .7em; margin-right: .4em; }
.topic-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
.topic-card { display: block; background: #fff; border: 1px solid rgba(20,48,31,0.10); border-radius: var(--radius); padding: 18px 20px; text-decoration: none; color: inherit; box-shadow: 0 2px 10px rgba(20,48,31,0.05); transition: transform .15s ease, box-shadow .15s ease; }
.topic-card:hover { transform: translateY(-2px); box-shadow: 0 12px 28px rgba(20,48,31,0.13); }
.topic-card h3 { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.15rem; margin: 0 0 6px; }
.topic-card p { font-size: .93rem; line-height: 1.5; color: var(--muted); margin: 0 0 10px; }
"""


def chrome():
    """The stylesheet and top band from ielts.html, so the hubs look like
    the rest of the site and keep looking like it when it changes."""
    src = open(os.path.join(ROOT, 'ielts.html'), encoding='utf-8').read()
    style = re.search(r'<style>.*?</style>', src, re.S).group(0)
    style = style.replace('</style>', STYLE_EXTRA + '</style>')
    fonts = '\n'.join(re.findall(r'<link[^>]+(?:preconnect|fonts\.googleapis)[^>]*>', src))
    nav = re.search(r'<nav class="topband">.*?</nav>', src, re.S).group(0)
    nav = nav.replace(' aria-current="page"', '')
    if GRAMMAR_LINK not in nav:
        print('  ! the top band has no %s; no hub will mark Grammar as current' % GRAMMAR_LINK)
    return style, fonts, nav


GRAMMAR_LINK = '<a href="grammar.html">Grammar</a>'


def nav_for(nav, current):
    """The top band with Grammar marked: 'page' on grammar.html itself,
    'true' (the current section) on a grammar topic, nothing elsewhere."""
    if not current:
        return nav
    return nav.replace(GRAMMAR_LINK, '<a href="grammar.html" aria-current="%s">Grammar</a>' % current)


def esc(t):
    return seo.esc(t)


def page(title, style, fonts, nav, body, ld, body_class='', wrap=True):
    """The shell every hub shares. `wrap` puts the body in the topic
    pages' column; the landing page manages its own full-bleed bands."""
    if wrap:
        body = '<div class="wrap">\n%s\n</div>' % body
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s | Forbes English</title>
%s
%s
%s
%s
<script type="application/ld+json">%s</script>
</head>
<body%s>
%s
%s
</body>
</html>
''' % (esc(title), seo.START, seo.END, fonts, style,
       json.dumps(ld, ensure_ascii=False, separators=(',', ':')),
       ' class="%s"' % body_class if body_class else '', nav, body)


def crumb(*parts):
    """parts: (label, href|None) — the last one is the current page."""
    out = []
    for label, href in parts:
        out.append('<a href="%s">%s</a>' % (href, label) if href else label)
    return '<p class="crumb">%s</p>' % ' &rsaquo; '.join(out)


def breadcrumb_ld(*parts):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': [
                {'@type': 'ListItem', 'position': i + 1, 'name': re.sub('<[^>]+>', '', n),
                 **({'item': '%s/%s' % (SITE, h)} if h else {})}
                for i, (n, h) in enumerate(parts)]}


def lesson_step(r, desc):
    lvl = r.get('level') or ''
    free = r.get('access') != 'pro'
    tags = ['<span class="tag tag-free">Free</span>' if free
            else '<span class="tag">Subscribers</span>']
    if lvl:
        tags.append('<span class="tag">%s</span>' % esc(lvl))
    return '''      <a class="step" href="%s">
        <div class="step-n lvl">%s</div>
        <div>
          <h3 class="step-title">%s</h3>
          <p class="step-desc">%s</p>
          <div class="tags">%s</div>
        </div>
        <div class="step-go">Open &rarr;</div>
      </a>''' % (seo.quote(r['file']), esc(lvl) or '&#8226;',
                 esc(seo.clean(r['title'])), esc(desc), ''.join(tags))


def describe(r):
    p = os.path.join(ROOT, r['file'])
    src = open(p, encoding='utf-8', errors='ignore').read()
    return seo.describe(src, r)


def swatch(slug, tc):
    """The tense colour a topic wears on grammar.html, as a swatch before
    its name, or nothing for a topic that has none."""
    import build_grammar_hub
    col = tc.get(build_grammar_hub.TOPIC_COLOUR.get(slug, ''))
    return '<span class="tswatch" style="--tc:%s" aria-hidden="true"></span>' % col[0] if col else ''


def topic_page(t, rows, images, allm, style, fonts, nav, tc):
    free = [r for r in rows if r.get('access') != 'pro']
    span = topics.level_span(rows)
    heroimg = topics.hero(rows, images)
    by_level = {}
    for r in rows:
        by_level.setdefault(r.get('level') or 'All levels', []).append(r)

    body = [crumb(('Home', 'index.html'), ('Grammar', 'grammar.html'), (t['name'], None))]
    body.append('  <div class="hero">\n    <div>')
    body.append('      <div class="eyebrow">%s%s &middot; %s &middot; %d lesson%s%s</div>'
                % (swatch(t['slug'], tc), esc(t['group']), esc(span) or 'All levels', len(rows),
                   '' if len(rows) == 1 else 's',
                   ' &middot; %d free' % len(free) if free else ''))
    body.append('      <h1>%s</h1>' % t['h1'])
    body.append('      <div class="prose">')
    for para in t['intro']:
        body.append('        <p>%s</p>' % para)
    body.append('      </div>')
    body.append('    </div>')
    body.append('    <div class="hero-side">')
    if heroimg:
        body.append('      <figure class="hero-art" style="margin:0"><img src="%s" alt="%s" loading="lazy"></figure>'
                    % (esc(heroimg.lstrip('/')), esc('Cover artwork from a Forbes English %s lesson' % t['name'])))
    body.append('      <ul class="facts">')
    body.append('        <li><b>Levels</b>%s</li>' % (esc(span) or 'All levels'))
    body.append('        <li><b>Free to open</b>%s</li>'
                % ('%d of %d lessons, no sign-in' % (len(free), len(rows)) if free
                   else 'Every lesson here is part of Forbes English Pro'))
    body.append('        <li><b>Not sure of your level?</b><a href="level-checker.html">Take the free Level Checker</a> &mdash; six questions a level, and it names the lesson to start on.</li>')
    body.append('      </ul>')
    body.append('    </div>\n  </div>')

    body.append('  <section class="track">')
    body.append('    <div class="track-head"><h2>The lessons</h2><span class="track-note">by level, free ones first &middot; every deck opens in the browser, 16:9, with a language switcher</span></div>')
    for lvl in sorted(by_level, key=topics.level_key):
        grp = by_level[lvl]
        body.append('    <div class="levelhead"><h3>%s</h3><span>%d lesson%s</span></div>'
                    % (esc(lvl), len(grp), '' if len(grp) == 1 else 's'))
        body.append('    <div class="steps">')
        for r in grp:
            body.append(lesson_step(r, describe(r)))
        body.append('    </div>')
    body.append('  </section>')

    related = [(o, allm[o['slug']]) for o in topics.TOPICS
               if o['slug'] != t['slug'] and allm[o['slug']]]
    body.append('  <section class="track">')
    body.append('    <div class="track-head"><h2>Other topics</h2></div>')
    body.append('    <div class="chips">')
    for o, orows in related:
        body.append('      <a class="chip" href="%s">%s%s<small>%d</small></a>'
                    % (topics.hub_url(o['slug']), swatch(o['slug'], tc), o['name'], len(orows)))
    body.append('    </div>\n  </section>')

    body.append('''  <div class="note">
    <div>
      <h3>Teaching this?</h3>
      <p>Every deck is built to be presented from: big type, one idea a slide, the rule stated before it is practised, and a speaking task at the end. Open a free one on the projector and see whether it suits your room before you pay for anything.</p>
    </div>
    <a href="pricing.html">Plans &amp; what&rsquo;s free &rarr;</a>
  </div>''')

    ld = {'@context': 'https://schema.org', '@graph': [
        breadcrumb_ld(('Home', 'index.html'), ('Grammar', 'grammar.html'),
                      (t['name'], topics.hub_url(t['slug']))),
        {'@type': 'ItemList', 'name': '%s lessons' % t['name'],
         'numberOfItems': len(rows),
         'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1,
              'url': '%s/%s' % (SITE, seo.quote(r['file'])),
              'name': seo.clean(r['title'])} for i, r in enumerate(rows)]}]}
    return page('%s: English lessons and exercises' % t['name'],
                style, fonts, nav, '\n'.join(body), ld)


def index_page(rows, images, allm, style, fonts, nav):
    """grammar.html — the landing page, from tools/build_grammar_hub.py:
    a full-bleed hero, the tense grid in colour, every topic as a card
    with its picture, the two routes, and a closing band."""
    import build_grammar_hub
    css, body, ld = build_grammar_hub.render(rows, images, allm)
    return page('English Grammar by Topic: Tenses, Modals, Passive, Prepositions',
                style + css, fonts, nav, body, ld, body_class='gh', wrap=False)


def main():
    rows, source = seo.lessons()
    images = seo.lesson_images()
    rows = [r for r in rows if os.path.exists(os.path.join(ROOT, r['file']))
            and r['file'] not in seo.SKIP]
    allm = topics.members(rows, images, seo.coming_soon)
    style, fonts, nav = chrome()
    import build_grammar_hub
    tc = build_grammar_hub.tense_colours(quiet=True)
    written = []
    for t in topics.generated():
        trows = allm[t['slug']]
        if not trows:
            print('  ! %s has no lessons; page not written' % t['slug'])
            continue
        out = os.path.join(ROOT, topics.hub_url(t['slug']))
        open(out, 'w', encoding='utf-8', newline='\n').write(
            topic_page(t, trows, images, allm, style, fonts,
                       nav_for(nav, 'true' if t.get('group') in ('Tenses', 'Grammar') else None), tc))
        written.append((topics.hub_url(t['slug']), len(trows),
                        sum(1 for r in trows if r.get('access') != 'pro')))
    open(os.path.join(ROOT, 'grammar.html'), 'w', encoding='utf-8', newline='\n').write(
        index_page(rows, images, allm, style, fonts, nav_for(nav, 'page')))
    print('  lessons: %d (from %s)' % (len(rows), source))
    for f, n, free in written:
        print('  %-32s %3d lessons, %2d free' % (f, n, free))
    # The five IELTS route pages and the landing page are generated from
    # tools/ielts_routes.py and the catalogue, so they go stale the same way
    # these do. All six at once: they share their pictures.
    import build_ielts_routes
    _, refused = build_ielts_routes.build_all(rows, images)
    # The Sherpa route map is hand-kept but states Free, levels and counts
    # that come from the catalogue; say so if they have drifted apart.
    import check_route_map
    check_route_map.report(rows, source)
    if refused:
        sys.exit('! IELTS: %s edited by hand (or unmarked), so none of the six IELTS pages '
                 'was rebuilt. Move the edit into tools/ielts_routes.py, or run '
                 'tools/build_ielts_routes.py --force. Do not run seo.py until then.'
                 % ', '.join(refused))
    print('  now run: python tools/seo.py')


if __name__ == '__main__':
    main()
