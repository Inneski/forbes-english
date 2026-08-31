#!/usr/bin/env python3
"""Build a Block Camp II deck - the passive-voice descent, stations 9 to 16.

THE MODEL. The descent is not a new subject. It is the SAME EIGHT CAMPS met
again on the way down, each one now in the passive, so a learner who climbed
past camp 3 in brown meets brown again coming down. House style, Appendix A:
"Passive-voice descent markers are separate camps."

    station  9  Present Perfect Passive      <- camp 7
    station 10  Future Simple Passive        <- camp 6
    station 11  Going To Passive             <- camp 5
    station 12  Past Continuous Passive      <- camp 4
    station 13  Past Simple Passive          <- camp 3
    station 14  Present Continuous Passive   <- camp 2
    station 15  Present Simple Passive       <- camp 1
    station 16  The Trial - mixed active and passive, every tense

Camp 8, Present Perfect Continuous, has no usable passive: nobody teaches
"has been being built". That is why the line has seven tense passives and a
trial rather than eight passives.

TWO THINGS FOLLOW FROM THE MODEL, and both are why this builder takes its
chassis from the matching Part I deck rather than from one fixed file:

  1. THE COLOUR IS THE CAMP'S. Lifting the chassis brings that camp's whole
     palette with it, already contrast-checked, instead of a second hex that
     only approximately matches.
  2. THE PLATES ARE THE CAMP'S. Coming down past camp 3 you are in the same
     place you climbed through. Re-using that camp's own artwork folder is the
     point, not a shortage - and it is what makes eight more decks possible
     without eight more folders of commissioned art.

WHY THIS FILE IS IN THE REPO. The Part I generator lived only in a sandbox and
a reset took it; the sixteen decks survived only because they had been
published. The deck this emits is a plain self-contained page that can be
hand-edited if the builder is lost again. Neither depends on the other.

    python3 lesson-template/descent/build_descent.py 9
"""
import importlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

# ── one new role, in the same discipline as --mark-aux ───────────────────
# Every passive is BE + PAST PARTICIPLE. The auxiliary already owns green;
# the participle is the other half and needs a colour that never changes.
# Hue 265, a cool violet: far from aux green (148), from the modal, and from
# every one of the thirteen tense accents, so the two halves of a passive can
# never be read as the same job whichever camp's colour the deck is wearing.
MARK_PP = "  --mark-pp: #b39bf5;"
PP_CSS = """
/* THE PARTICIPLE IS A JOB, NOT AN EMPHASIS. See --mark-pp above. */
.pp { color: var(--mark-pp) !important; font-weight: 700; }
"""


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


def cover(cov, st):
    """The cover, with every line the station rewrites made literal.

    data-i18n is stripped from those lines on purpose: the dictionary in the
    chassis still holds the Part I deck's German, and a key left in place would
    put 'Present Perfect' on a passive cover the moment somebody chose Deutsch.
    Whatever carries no key falls back to what is written on the slide.
    """
    cov = re.sub(r'\s*data-i18n="(coverTitle|coverSub|chipLevel|chipFocus|chipCount|coverFine|btnStart)"', '', cov)
    cov = re.sub(r'(<h1 class="cover-title">)[^<]*(</h1>)', r'\g<1>%s\g<2>' % st['title'], cov)
    cov = re.sub(r'(<p class="cover-sub">)[^<]*(</p>)', r'\g<1>%s\g<2>' % st['sub'], cov)
    chips = ['%s &middot; Grammar' % st['level'], 'Block Camp II',
             '%d slides' % (len(st['slides']) + 1)]
    n = [0]
    def swap(m):
        out = m.group(1) + chips[n[0]] + m.group(2); n[0] += 1
        return out
    return re.sub(r'(<span class="chip">)[^<]*(</span>)', swap, cov, count=3)


def build(st):
    head, cov, tail = split(os.path.join(ROOT, st['chassis']))
    head = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % st['doctitle'], head)
    head = re.sub(r"--hero: url\('[^']*'\)", "--hero: url('%s')" % st['hero'], head)
    head = head.replace('  --mark-aux: #46d98a;', '  --mark-aux: #46d98a;\n' + MARK_PP, 1)
    head = head.replace('.aux { color: var(--mark-aux) !important; font-weight: 700; }',
                        '.aux { color: var(--mark-aux) !important; font-weight: 700; }' + PP_CSS, 1)
    out = head + '\n\n    '.join([cover(cov, st)] + st['slides']) + tail
    path = os.path.join(ROOT, st['file'])
    open(path, 'w', encoding='utf-8').write(out)
    return path


if __name__ == '__main__':
    mod = importlib.import_module('station%02d' % int(sys.argv[1]))
    print('built', build(mod.STATION))
