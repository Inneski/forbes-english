#!/usr/bin/env python3
"""Build a Block Camp II deck - the passive-voice descent, stations 9 to 16.

WHY THIS FILE EXISTS. The Part I generator lived only in a sandbox and a reset
took it with it; the sixteen decks survived only because they had been
published. So this builder ships in the repo from its first run, and the deck
it emits is a plain self-contained file that can be edited directly if the
builder is ever lost again. Neither one depends on the other.

The chassis - shell, CSS, engine, chrome - is lifted verbatim from a published
Part I deck, so the descent inherits every fix already argued for: the opt-in
equal-box rule, answer groups sized by their longest answer, drop targets that
are targets, example lists that stack, the nudge and the centre.

    python3 lesson-template/descent/build_descent.py 9
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

# ── the passive line's own colour ────────────────────────────────────────
# Derived from BlockCampDescent/watchtower-far-side.jpg by extract-palette.py,
# not chosen by eye: the descent is not a tense, so the thirteen tense colours
# do not apply and the house rule is a hero-derived palette. Every contrast
# pair in that report passed.
PALETTE = """  --void          : #13150d;
  --surface       : #202316;
  --surface2      : #2b301e;
  --border        : #5f5043;
  --text          : #f5f3f2;
  --text-dim      : #bfb0a3;
  --accent        : #be7f4a;
  --accent-bright : #d6a479;
  --accent-dim    : #7a5332;
  --secondary     : #334c4c;
  --contrast      : #25e4e1;"""

# ── one new role, in the same discipline as --mark-aux ───────────────────
# Every passive is BE + PAST PARTICIPLE. The auxiliary already owns green;
# the participle is the other half and needs a colour of its own that never
# changes. Hue 265, a cool violet: far from aux green (148), from the modal,
# and from this line's own copper accent (hue 28), so the two halves of a
# passive can never be read as the same job. 7.9:1 on --surface.
MARK_PP = "  --mark-pp: #b39bf5;"

PP_CSS = """
/* THE PARTICIPLE IS A JOB, NOT AN EMPHASIS. See --mark-pp above. */
.pp { color: var(--mark-pp) !important; font-weight: 700; }
"""


def chassis():
    head = open(os.path.join(HERE, 'chassis-head.html'), encoding='utf-8').read()
    tail = open(os.path.join(HERE, 'chassis-tail.html'), encoding='utf-8').read()
    return head, tail


def cover_template():
    """The cover, verbatim from a published deck, with its text made swappable.

    data-i18n is stripped from every line the station rewrites: the dictionary
    in the tail still holds the Part I deck's German, and a key left in place
    would put 'Present Perfect' on a passive cover the moment somebody chose
    Deutsch. Whatever carries no key falls back to what is written on the
    slide, which is the text this file put there.
    """
    src = open(os.path.join(ROOT, 'blockcamp-present-perfect.html'), encoding='utf-8').read()
    i = src.find('<section class="slide is-active" data-type="cover">')
    j = src.find('</section>', i) + len('</section>')
    cov = src[i:j]
    cov = re.sub(r'\s*data-i18n="(coverTitle|coverSub|chipLevel|chipFocus|chipCount|coverFine|btnStart)"', '', cov)
    cov = re.sub(r'(<h1 class="cover-title">)[^<]*(</h1>)', r'\1{TITLE}\2', cov)
    cov = re.sub(r'(<p class="cover-sub">)[^<]*(</p>)', r'\1{SUB}\2', cov)
    cov = re.sub(r'(<span class="chip">)[^<]*(</span>\s*<span class="chip">)[^<]*(</span>\s*<span class="chip">)[^<]*(</span>)',
                 r'\1{LEVEL}\2Block Camp II\3{COUNT} slides\4', cov)
    return cov


def head_for(head, station):
    h = head
    h = re.sub(r'<title>[^<]*</title>',
               '<title>%s</title>' % station['doctitle'], h)
    h = re.sub(r"--hero: url\('[^']*'\)", "--hero: url('%s')" % station['hero'], h)
    # the palette block: replace the eleven derived tokens in one go
    h = re.sub(r'  --void          : #[0-9a-f]{6};.*?  --contrast      : #[0-9a-f]{6};',
               PALETTE, h, count=1, flags=re.S)
    h = h.replace('  --mark-aux: #46d98a;', '  --mark-aux: #46d98a;\n' + MARK_PP, 1)
    h = h.replace('.aux { color: var(--mark-aux) !important; font-weight: 700; }',
                  '.aux { color: var(--mark-aux) !important; font-weight: 700; }' + PP_CSS, 1)
    return h


def build(station):
    head, tail = chassis()
    cov = cover_template().replace('{TITLE}', station['title']) \
                          .replace('{SUB}', station['sub']) \
                          .replace('{LEVEL}', station['level'] + ' &middot; Grammar') \
                          .replace('{COUNT}', str(len(station['slides']) + 1))
    body = [cov] + station['slides']
    out = head_for(head, station) + '\n\n    '.join(body) + tail
    path = os.path.join(ROOT, station['file'])
    open(path, 'w', encoding='utf-8').write(out)
    return path
