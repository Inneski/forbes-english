#!/usr/bin/env python3
"""Build a Block Camp II deck - the passive-voice descent, stations 9 to 16.

THE MODEL. The descent is not a new subject. It is the SAME EIGHT CAMPS met
again on the way down, each one now in the passive, so a learner who climbed
past camp 3 in brown meets brown again coming down. House style, Appendix A:
"Passive-voice descent markers are separate camps."

THE DESCENT RUNS IN THE SAME ORDER AS THE CLIMB. Innes: "present simple should
start the descent (same as the ascent order)". Station N mirrors camp N-8, so
you meet the tenses in the order you learned them, not in reverse.

    station  9  Present Simple Passive       <- camp 1
    station 10  Present Continuous Passive   <- camp 2
    station 11  Past Simple Passive          <- camp 3
    station 12  Past Continuous Passive      <- camp 4
    station 13  Going To Passive             <- camp 5
    station 14  Future Simple Passive        <- camp 6
    station 15  Present Perfect Passive      <- camp 7
    station 16  The Trial - mixed active and passive, every tense

This table listed the REVERSED order until 2026-08-31 - an abandoned model from
before the order was settled. The station 15 deck has been right since it was
published; the table and the source filename were what lagged, because the push
that would have fixed them was blocked three times.

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

# ── three new roles, in the same discipline as --mark-aux ────────────────
# Why each is what it is, in the block below the declaration.
MARKS = """  --mark-pp: #b39bf5;
  --mark-obj: #f65af6;
  --mark-agent: #cfe8d8;"""

# THREE ROLES, AND THE PASSIVE IS THE MOVE BETWEEN THEM.
#
#   --mark-pp     the past participle. Every passive is BE + participle; the
#                 auxiliary already owns green, so the other half takes hue
#                 265, far from aux green (148), from the modal, and from all
#                 thirteen tense accents. Innes: if a participle is purple
#                 then the WORDS "past participle" and "third form" are purple
#                 too, wherever they are written. A label for a role wears the
#                 role's colour or the reader has to learn the rule twice.
#
#   --mark-obj    the object of the active - which is the subject of the
#                 passive. ONE colour for BOTH, because they are the same
#                 thing in two places, and seeing it move is the lesson.
#
#   --mark-agent  the doer. Greenish white: present when it matters, quiet
#                 enough to look droppable, which is what it usually is.
#
# THE RULING, AND IT WAS OVERDUE. The object used to be #ffd633, a yellow,
# against --mark-inf's #eec32f: 1.4 degrees apart in hue, CIE76 deltaE 8.5.
# They never shared a slide while the descent had two decks, but Going To
# Passive and Future Simple Passive put a bare verb and an object on the same
# page, and a learner would have had to tell them apart at deltaE 8.5.
#
# THE INFINITIVE DID NOT MOVE. Gold is the bare verb on three Part I decks and
# 46 separate words; the object exists only in the eight descent decks, two of
# them built. Moving the newer role costs less and breaks nothing published.
#
# The magenta was searched for, not picked: every hue at three lightnesses and
# three saturations, scored on its smallest deltaE against all nine fixed
# roles AND every deck accent in the line, rejecting anything under 4.5:1 on
# any surface. #f65af6 won at min deltaE 50.5 - which is its distance from the
# participle purple, the one it shares a line with on every passive sentence.
# Six times the collision it replaces. Gold 144.9, green 155.0, agent 106.8.
ROLE_CSS = """
/* One colour per job. See the MARKS block above for why each is what it is. */
.pp    { color: var(--mark-pp) !important;    font-weight: 700; }
.obj   { color: var(--mark-obj) !important;   font-weight: 700; }
.agent { color: var(--mark-agent) !important; font-weight: 700; }

/* THE RESULTS SLIDE STACKED THREE PANELS WITH 18px BETWEEN THEM, so the score
   plate and the message plate read as one overlapping box - Innes: "Now use
   it (overlapping boxes)". The panels are separated and the message is capped
   at a readable measure instead of running the width of the column. */
.slide[data-type="results"] .score-big { margin-bottom: 10px; }
.slide[data-type="results"] #scoreMsg  { margin-top: 26px !important; max-width: 34ch; }
.slide[data-type="results"] .slide-body > .prose.dim { margin-top: 22px !important; }
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


# The chassis fills en, de and es; the other seven blocks are empty and fall
# back to English at runtime. Anything filled that a station does not rewrite
# still carries the CAMP's active-voice advice.
CHASSIS_LANGS = ('en', 'de', 'es')


def rescore(tail, messages):
    """Replace the results messages, SCOPED TO EACH LANGUAGE BLOCK.

    THE SUBSTITUTION USED TO BE GLOBAL WITH count=1, WHICH ONLY EVER HIT en.
    The key names repeat once per language, and the first match in the file is
    always English, so de and es kept the chassis camp's ACTIVE wording: a
    learner on Deutsch was told "Geh zurueck zum Merksatz" - go back to the
    dictum, about the second and third form - on a deck about the passive.

    `messages` is either {key: text} (English only, as the first stations were
    written) or {lang: {key: text}}. A language the station does not supply is
    left alone and named in the return value, so the caller can say out loud
    which blocks are still wearing the camp's words.
    """
    if messages and all(isinstance(v, str) for v in messages.values()):
        messages = {'en': messages}
    for lang, msgs in messages.items():
        m = re.search(r'^  %s: \{$' % lang, tail, re.M)
        if not m:
            raise SystemExit('no %s block in the chassis dictionary' % lang)
        end = tail.find('\n  },', m.end())
        block = tail[m.end():end]
        for key, val in msgs.items():
            pat = re.compile(r'(\n\s*%s: )(".*?"|\'.*?\')(,)' % key)
            if not pat.search(block):
                raise SystemExit('message key %s.%s not found in the chassis' % (lang, key))
            block = pat.sub(lambda mm: mm.group(1) + '"%s"' % val + mm.group(3), block, count=1)
        tail = tail[:m.end()] + block + tail[end:]
    return tail


def build(st):
    head, cov, tail = split(os.path.join(ROOT, st['chassis']))
    # THE CHASSIS BRINGS THE CAMP'S SEO BLOCK WITH IT, AND IT IS POISON.
    # Once tools/seo.py had written blocks into the Part I decks, every descent
    # deck built afterwards inherited one wholesale: station 9 shipped carrying
    # camp 1's canonical - <link rel="canonical" href=".../blockcamp-present-
    # simple.html"> - which tells Google this page is a DUPLICATE of the active
    # lesson and to index that one instead. Also its og:title, its description
    # and its JSON-LD name, all naming the wrong lesson.
    # check-lesson.js's HEAD gate passed it, because the gate asks whether a
    # block is PRESENT, not whether it belongs to this page.
    # Strip it. seo.py writes the right one once the deck has a catalogue row.
    head = re.sub(r'\n?<!-- SEO:start -->.*?<!-- SEO:end -->\n?', '\n', head, flags=re.S)
    head = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % st['doctitle'], head)
    head = re.sub(r"--hero: url\('[^']*'\)", "--hero: url('%s')" % st['hero'], head)
    head = head.replace('  --mark-aux: #46d98a;', '  --mark-aux: #46d98a;\n' + MARKS, 1)
    head = head.replace('.aux { color: var(--mark-aux) !important; font-weight: 700; }',
                        '.aux { color: var(--mark-aux) !important; font-weight: 700; }' + ROLE_CSS, 1)
    tail = rescore(tail, st.get('messages', {}))
    out = head + '\n\n    '.join([cover(cov, st)] + st['slides']) + tail
    path = os.path.join(ROOT, st['file'])
    open(path, 'w', encoding='utf-8').write(out)
    return path


if __name__ == '__main__':
    mod = importlib.import_module('station%02d' % int(sys.argv[1]))
    st = mod.STATION
    print('built', build(st))
    msgs = st.get('messages', {})
    done = set(msgs) if not all(isinstance(v, str) for v in msgs.values()) else {'en'}
    stale = [l for l in CHASSIS_LANGS if l not in done]
    if stale:
        print('  WARNING: results messages still the chassis camp\'s ACTIVE wording in: %s'
              % ', '.join(stale))
