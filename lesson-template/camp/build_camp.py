#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a Block Camp I deck (the climb) from a published chassis and a spec.

WHY THIS EXISTS. The generator that built camps 1-8 lived only in a sandbox
and was lost when it was recycled; the sixteen decks survived because they had
been published, and blockcamp-status.md rightly says the published HTML is now
the source of truth for THOSE decks. A NEW camp still has to come from
somewhere, and the descent builder (lesson-template/descent/build_descent.py)
already shows the safe way: take a published deck as the chassis - its shell,
its fonts, its engine, its chrome dictionary - and replace only the slides,
the palette and the lesson strings. This file is that, for the climb.

Camp 9, Past Perfect, is the first deck built with it:

    python3 lesson-template/camp/build_camp.py 9

The spec (camp09.py) is plain data: a palette derived from its hero with
extract-palette.py, the slides as HTML strings keyed with data-i18n, the
dictionary for en/de/es, and the translate-on-request table BW_TR. What the
builder does to the chassis is listed at build(), step by step.

THE DICTIONARY IS THE ONE PLACE A CHASSIS CAN LIE. UI_I18N in a published deck
holds ten languages, and every one of them carries that deck's LESSON strings -
coverTitle: "Past Simple", useTitle, the results messages - next to the chrome
strings every deck shares. Leave a lesson key in place and a learner who picks
Français sees the past simple's cover on a past perfect deck. So every lesson
key is dropped from every language and only the chrome keys survive; the spec
then supplies en/de/es. The engine offers a language only when its key count
matches English (initLang), so fr..ja simply leave the menu instead of showing
half a lesson. That is the same trap build_descent.py's cover() names, solved
for the whole dictionary rather than for seven keys.
"""
import importlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)

# Strings every deck shares. Everything else in UI_I18N belongs to the lesson
# the chassis was, and is replaced.
CHROME_KEYS = {
    'partLink', 'actEyebrow', 'actUse', 'actSpeakBrief', 'actSpeakKind',
    'actWriteKind', 'bankLabel', 'btnCheck', 'btnCopied', 'btnCopy', 'btnHint',
    'btnNext', 'btnOpen', 'btnRestart', 'btnStart', 'chipFocus', 'coverFine',
    'fbAnswer', 'fbCorrect', 'fbWrong', 'gap1Eyebrow', 'gap2Eyebrow',
    'ledClues', 'ledDp', 'ledTime', 'matchEyebrow', 'ord1Eyebrow', 'qEyebrow',
    'resNext', 'scoreLabel', 'slideOf', 'sortEyebrow', 'wordCount',
}
PART_LINK = re.compile(r'<a class="part-link"[^>]*>.*?</a>', re.S)
KEY_LINE = re.compile(r'^    ([A-Za-z0-9_]+): (.*?),?$')


def split(path):
    """A published deck, cut into chassis-head, cover, chassis-tail."""
    src = open(path, encoding='utf-8').read()
    tags = [m for m in re.finditer(r'<section class="slide[^>]*>', src)
            if 'data-type=' in m.group(0)]
    head = src[:tags[0].start()]
    tail = src[src.rfind('</section>') + len('</section>'):]
    i = src.find('<section class="slide is-active" data-type="cover">')
    cov = src[i:src.find('</section>', i) + len('</section>')]
    return head, cov, tail


def js_str(v):
    """A dictionary value as the deck writes it: double-quoted JS."""
    return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'


def rewrite_dictionary(tail, spec):
    """Drop every lesson key from every language; add the spec's en/de/es."""
    m = re.search(r'^const UI_I18N = \{$', tail, re.M)
    end = tail.find('\n};', m.end())
    body = tail[m.end():end]
    out = []
    blocks = re.split(r'(?m)^  ([a-z]{2}): \{$', body)
    # blocks[0] is '' ; then lang, content, lang, content ...
    for i in range(1, len(blocks), 2):
        lang, content = blocks[i], blocks[i + 1]
        kept = []
        for line in content.split('\n'):
            km = KEY_LINE.match(line)
            if km and km.group(1) in CHROME_KEYS:
                kept.append((km.group(1), km.group(2)))
        extra = spec['i18n'].get(lang, {})
        if lang not in spec['i18n']:
            # A language the spec does not author is EMPTIED, not trimmed:
            # check-lesson.js's I18N gate rejects a partial dictionary, and
            # initLang() hides an empty one from the menu. Chrome-only would
            # be "partial" - 33 keys of 106 - and fail the gate.
            kept = []
        else:
            # a chrome key the spec overrides (partLink, actSpeakKind...)
            kept = [(k, v) for k, v in kept if k not in extra]
        lines = ['    %s: %s,' % (k, v) for k, v in kept]
        lines += ['    %s: %s,' % (k, js_str(v)) for k, v in sorted(extra.items())]
        if lines:
            lines[-1] = lines[-1].rstrip(',')
        out.append('  %s: {\n%s\n  },' % (lang, '\n'.join(lines)))
    new_body = '\n' + '\n'.join(out)
    new_body = new_body.rstrip(',')
    return tail[:m.end()] + new_body + tail[end:]


def replace_between(src, start_pat, end_pat, new):
    a = re.search(start_pat, src)
    b = re.search(end_pat, src[a.end():])
    return src[:a.start()] + new + src[a.end() + b.end():]


def build(spec):
    head, cov, tail = split(os.path.join(ROOT, spec['chassis']))

    # 1. The chassis brings the camp's SEO block, and it names the wrong
    #    lesson. seo.py writes the right one once the deck has a catalogue row.
    head = re.sub(r'\n?<!-- SEO:start -->.*?<!-- SEO:end -->\n?', '\n', head, flags=re.S)
    head = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % spec['doctitle'], head)
    head = head.replace('<meta name="viewport"',
                        '<meta name="description" content="%s">\n<meta name="viewport"'
                        % spec['description'], 1)

    # 2. Hero and palette - the block extract-palette.py writes, verbatim.
    head = re.sub(r"--hero: url\('[^']*'\)", "--hero: url('%s')" % spec['hero'], head)
    head = replace_between(head, r'  --void\s*:', r'  --contrast\s*:[^\n]*\n', spec['palette'])

    # 3. Tense tokens. The past simple's brown stays, because the LATER action
    #    in every past perfect sentence is a past simple and the deck sets the
    #    two side by side; the past perfect's own maroon joins it.
    head = head.replace('  --t-past-ink: #D5AB89;\n}',
                        '  --t-past-ink: #D5AB89;\n' + spec['tokens'] + '\n}', 1)
    head = head.replace(
        'em.t-past, b.t-past { color: var(--t-past-ink) !important; font-weight: 700; }',
        'em.t-past, b.t-past { color: var(--t-past-ink) !important; font-weight: 700; }\n'
        + spec['role_css'], 1)

    # 4. Cover. Keys stay - the dictionary below supplies every language.
    cov = re.sub(r'(<h1 class="cover-title" data-i18n="coverTitle">)[^<]*(</h1>)',
                 r'\g<1>%s\g<2>' % spec['i18n']['en']['coverTitle'], cov)
    cov = re.sub(r'(<p class="cover-sub" data-i18n="coverSub">)[^<]*(</p>)',
                 r'\g<1>%s\g<2>' % spec['i18n']['en']['coverSub'], cov)
    cov = re.sub(r'(data-i18n="chipLevel">)[^<]*(</span>)',
                 r'\g<1>%s\g<2>' % spec['i18n']['en']['chipLevel'], cov)
    cov = re.sub(r'(data-i18n="chipCount">)[^<]*(</span>)',
                 r'\g<1>%s\g<2>' % spec['i18n']['en']['chipCount'], cov)

    # 5. Slides.
    body = '\n\n    '.join([cov] + spec['slides'])

    # 6. Dictionary, translate-on-request table, part link.
    tail = rewrite_dictionary(tail, spec)
    tail = re.sub(r'<script>window\.BW_TR=.*?;</script>',
                  lambda m: '<script>window.BW_TR=%s;</script>'
                  % json.dumps(spec['tr'], ensure_ascii=False), tail, count=1, flags=re.S)
    out = head + body + tail
    out = PART_LINK.sub(spec['part_link'], out)

    out = seo(out, spec)
    path = os.path.join(ROOT, spec['file'])
    open(path, 'w', encoding='utf-8', newline='\n').write(out)
    return path


def seo(src, spec):
    """The SEO block, from tools/seo.py against a synthetic catalogue row.

    seo.py iterates the Supabase rows (or tools/lessons.json when the session
    cannot reach Supabase), so a brand-new deck with no row yet is skipped
    entirely and ships with no block - the HEAD gate fails. The block is
    written here from the same functions seo.py uses, against the row this
    deck WILL have; when the row exists, seo.py's own run overwrites it with an
    identical block. The hero path is the library card's, which does not exist
    until the cover is rendered to BlockCamp/<slug>.jpg - so the image is set
    by name here and the card is made alongside the deck.
    """
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import seo as S
    row = dict(spec['row'])
    title = S.page_title(row)
    desc = S.describe(src, row)
    row = dict(row, _rules=S.rules(src))
    img = '/' + S.quote(spec['card'])
    url = '%s/%s' % (S.SITE, S.quote(row['file']))
    new = S.inject(src, S.seo_block(url, title, desc, img, row), S.esc(title))
    return new if new is not None else src


if __name__ == '__main__':
    mod = importlib.import_module('camp%02d' % int(sys.argv[1]))
    print('built', build(mod.CAMP))
