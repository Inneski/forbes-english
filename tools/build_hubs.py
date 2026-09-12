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
    nav = nav.replace('<a href="library.html#cat=Grammar+activity">Grammar</a>',
                      '<a href="grammar.html" aria-current="page">Grammar</a>')
    return style, fonts, nav


def esc(t):
    return seo.esc(t)


def page(title, style, fonts, nav, body, ld):
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
<body>
%s
<div class="wrap">
%s
</div>
</body>
</html>
''' % (esc(title), seo.START, seo.END, fonts, style,
       json.dumps(ld, ensure_ascii=False, separators=(',', ':')), nav, body)


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


def topic_page(t, rows, images, allm, style, fonts, nav):
    free = [r for r in rows if r.get('access') != 'pro']
    span = topics.level_span(rows)
    heroimg = topics.hero(rows, images)
    by_level = {}
    for r in rows:
        by_level.setdefault(r.get('level') or 'All levels', []).append(r)

    body = [crumb(('Home', 'index.html'), ('Grammar', 'grammar.html'), (t['name'], None))]
    body.append('  <div class="hero">\n    <div>')
    body.append('      <div class="eyebrow">%s &middot; %s &middot; %d lesson%s%s</div>'
                % (esc(t['group']), esc(span) or 'All levels', len(rows),
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
        body.append('      <a class="chip" href="%s">%s<small>%d</small></a>'
                    % (topics.hub_url(o['slug']), o['name'], len(orows)))
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


def index_page(allm, images, style, fonts, nav):
    body = [crumb(('Home', 'index.html'), ('Grammar', None))]
    body.append('''  <div class="hero">
    <div>
      <div class="eyebrow">Grammar &middot; A1 to C2</div>
      <h1>English grammar, <em>by topic</em></h1>
      <div class="prose">
        <p>Every grammar lesson on the site, shelved by the point it teaches. Each topic page explains the rule in plain sentences &mdash; the form, what it is for, and the mistake that gives a level away &mdash; and then lists the lessons that drill it, by level, free ones first.</p>
        <p>The tenses are taught in the order a learner meets them: Present Simple and Continuous, then the Past Simple, then the Present Perfect and the line between it and the past, then the future forms, and the perfect tenses last. The passive, the modals, prepositions and conditionals sit alongside, and the review pages put everything side by side once the pieces are in place.</p>
        <p>Every lesson is a 16:9 deck that opens in the browser: the rule on the slide, then practice, then a speaking task, with a language switcher for the explanations. Teachers present from them; learners work through them alone.</p>
      </div>
    </div>
    <div class="hero-side">
      <ul class="facts">
        <li><b>Where to start</b><a href="level-checker.html">The free Level Checker</a> tests the tenses adaptively, six questions a level, and names the lesson to open first.</li>
        <li><b>Two routes through the tenses</b><a href="sherpa-tensing-route-map.html">Sherpa Tensing</a> climbs them in order, active then passive; <a href="block-camp.html">Block Camp</a> does the same in Minecraft.</li>
        <li><b>Exam English</b><a href="ielts.html">IELTS Academic</a> has its own route: Writing, Speaking and Listening in teaching order.</li>
      </ul>
    </div>
  </div>''')
    groups = {}
    for t in topics.TOPICS:
        if not allm[t['slug']]:
            continue
        groups.setdefault(t['group'], []).append(t)
    for g in ('Tenses', 'Grammar', 'Skills'):
        if g not in groups:
            continue
        body.append('  <section class="track">')
        body.append('    <div class="track-head"><h2>%s</h2></div>' % esc(g))
        body.append('    <div class="topic-grid">')
        for t in sorted(groups[g], key=lambda x: x['order']):
            rows = allm[t['slug']]
            free = sum(1 for r in rows if r.get('access') != 'pro')
            desc = t['desc'] or 'The IELTS Academic route: Writing, Speaking, Listening and the vocabulary that feeds them.'
            desc = desc.split(': ', 1)[-1] if ': ' in desc else desc
            body.append('''      <a class="topic-card" href="%s">
        <h3>%s</h3>
        <p>%s</p>
        <div class="tags"><span class="tag">%s</span><span class="tag">%d lesson%s</span>%s</div>
      </a>''' % (topics.hub_url(t['slug']), esc(t['name']), esc(seo.trim(desc, 150)),
                 esc(topics.level_span(rows) or 'All levels'), len(rows),
                 '' if len(rows) == 1 else 's',
                 '<span class="tag tag-free">%d free</span>' % free if free else ''))
        body.append('    </div>\n  </section>')
    body.append('''  <div class="note">
    <div>
      <h3>Looking for one lesson in particular?</h3>
      <p>The library lists every lesson on the site, filterable by level, topic and whether it is free, with a picture for each so a class can pick by eye.</p>
    </div>
    <a href="library.html">Open the library &rarr;</a>
  </div>''')
    ld = {'@context': 'https://schema.org', '@graph': [
        breadcrumb_ld(('Home', 'index.html'), ('Grammar', 'grammar.html')),
        {'@type': 'ItemList', 'name': 'English grammar topics',
         'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1,
              'url': '%s/%s' % (SITE, topics.hub_url(t['slug'])), 'name': t['name']}
             for i, t in enumerate(x for x in topics.TOPICS if allm[x['slug']])]}]}
    return page('English Grammar by Topic: Tenses, Modals, Passive, Prepositions',
                style, fonts, nav, '\n'.join(body), ld)


def main():
    rows, source = seo.lessons()
    images = seo.lesson_images()
    rows = [r for r in rows if os.path.exists(os.path.join(ROOT, r['file']))
            and r['file'] not in seo.SKIP]
    allm = topics.members(rows, images, seo.coming_soon)
    style, fonts, nav = chrome()
    written = []
    for t in topics.generated():
        trows = allm[t['slug']]
        if not trows:
            print('  ! %s has no lessons; page not written' % t['slug'])
            continue
        out = os.path.join(ROOT, topics.hub_url(t['slug']))
        open(out, 'w', encoding='utf-8', newline='\n').write(
            topic_page(t, trows, images, allm, style, fonts, nav))
        written.append((topics.hub_url(t['slug']), len(trows),
                        sum(1 for r in trows if r.get('access') != 'pro')))
    open(os.path.join(ROOT, 'grammar.html'), 'w', encoding='utf-8', newline='\n').write(
        index_page(allm, images, style, fonts, nav))
    print('  lessons: %d (from %s)' % (len(rows), source))
    for f, n, free in written:
        print('  %-32s %3d lessons, %2d free' % (f, n, free))
    print('  grammar.html: %d topics' % len(written))
    print('  now run: python tools/seo.py')


if __name__ == '__main__':
    main()
