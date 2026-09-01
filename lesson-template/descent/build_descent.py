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
  --mark-obj: #909294;
  --mark-agent: #ffffff;
  --t-present-simple: #7A93B5;
  --t-present-continuous: #E68EA6;
  --t-past-simple: #B08968;
  --t-past-continuous: #F1D779;
  --t-going-to: #70A43A;
  --t-future-simple: #F0723F;
  --t-present-perfect: #70E0E0;"""

# THREE ROLES, AND THE PASSIVE IS THE MOVE BETWEEN THEM.
#
#   --mark-pp     the past participle, hue 265. Every passive is BE +
#                 participle, and the participle is the half that never
#                 changes, so it is the one colour that holds across all seven
#                 chains. Innes: if a participle is purple then the WORDS
#                 "past participle" and "third form" are purple too, wherever
#                 they are written. A label for a role wears the role's colour
#                 or the reader has to learn the rule twice.
#
#   --mark-obj    the object of the active - which is the subject of the
#                 passive. ONE colour for BOTH, because they are the same
#                 thing in two places, and seeing it move is the lesson.
#
#   --mark-agent  the doer.
#
# THE SECOND RULING, 2026-09-01. Innes, on two shipped stations at once:
# "white = the agent / grey = the thing / is/are being = pink / past
# participle = purple / has/have been = turquoise / past simple= brown".
#
# The agent goes to pure white (#ffffff) from a greenish white, and the object
# from magenta to a neutral grey. That reads as a demotion of the magenta and
# it is: the magenta was searched for and won on deltaE, but it won a contest
# about telling roles apart, and the roles are no longer what carries the
# lesson. The chains are. A saturated magenta beside a pink auxiliary and a
# purple participle is three loud colours in one sentence; white and grey put
# the two nouns in the background where a passive sentence wants them and let
# the chain be the thing you see.
#
# The grey is #909294 - solved, not picked. It clears 4.5:1 on the darkest of
# the eight descent surfaces at 5.24:1 (every one of them was measured) and
# sits 189 in RGB distance from the agent white, which is the only colour it
# has to be told apart from at a glance.
#
# TURQUOISE FOR THE PRESENT PERFECT, AND IT OVERRULES THE PALETTE. Camp 7 is
# #2E7D65 in lesson-template/tense-palette.css and that is what the route map
# and the camp page wear. It fails on a dark deck (3.3:1) and Innes asked for
# turquoise by name. #70E0E0 was searched the same way the magenta was: the
# cyan band at every saturation and value, rejecting anything under 4.5:1 on
# any of the eight surfaces, scored on its smallest deltaE against all the
# fixed roles and every tense accent. It clears 10.5:1 at worst and sits 83
# from camp 8's teal, its nearest neighbour. The descent deviates from the
# palette here; Part I does not.
#
# THE INFINITIVE DID NOT MOVE, EITHER TIME. Gold is the bare verb on three
# Part I decks and 46 separate words.
ROLE_CSS = """
/* One colour per job. See the MARKS block above for why each is what it is. */
.pp    { color: var(--mark-pp) !important;    font-weight: 700; }
.obj   { color: var(--mark-obj) !important;   font-weight: 700; }
.agent { color: var(--mark-agent) !important; font-weight: 700; }
/* THE SECOND FORM, WHICH THE PASSIVE MUST NOT TAKE. Station 11 sets 'broke'
   beside 'broken' and the whole slide is the difference between them; with no
   rule behind .t-past the second form rendered plain white and half the
   contrast was missing. #B08968 is camp 3's own hex from
   lesson-template/tense-palette.css - the brown a learner climbed past. */
.t-past { color: var(--t-past-simple) !important; font-weight: 700; }

/* ── TENSE IN SITU, ON THE SLIDES THAT SET TENSES AGAINST EACH OTHER ──
   Innes: "Tenses in situ e.g. Past Continuous 'was being' or 'were walking'
   should be in yellow as present simple is blue and past simple brown. e.g.
   this page 'Is' blue 'is being' pink 'was' brown 'was being' yellow".

   He was looking at station 12's second slide, where four chains sit in one
   column - is / is being / was / was being - and every one of them was the
   same role green, which is the one thing the slide is not about. Role colour
   answers "what job is this word doing"; on that slide every learner already
   knows the answer, and the question is "which tense is this". So on a
   CONTRAST slide only, the auxiliary chain wears its own camp's colour from
   lesson-template/tense-palette.css - the colour that camp's page, its route
   marker and its descent station all already wear.

   The participle stays purple in every row. It is the constant the slide is
   built to show, and colouring it by tense would destroy the point.

   Everywhere else, role colour is unchanged. This is not a new default.

   TWO DEVIATIONS, BOTH DELIBERATE.

   Present perfect ships as #2E7D65 and fails on a dark deck: 3.30:1 on
   station 12's warm surface and 3.49:1 on the Trial's cool one. That is the
   caution tense-palette.css writes down for its dark tokens, and its own
   remedy - lighten toward white, keep the hue. Solved rather than guessed:
   80% is the strongest mix that clears 4.5:1 on BOTH surfaces (4.81 and
   5.09), and it also sits furthest from its two nearest neighbours in the
   band that clears. #589784.

   tense-palette.css says never more than three tense colours on one slide.
   Station 16's grid has seven, because seven chains side by side IS that
   slide. Overruled knowingly, once, on the one slide whose subject is the
   set. */
.t-ps    { color: var(--t-present-simple) !important;     font-weight: 700; }
.t-pc    { color: var(--t-present-continuous) !important; font-weight: 700; }
.t-pastc { color: var(--t-past-continuous) !important;    font-weight: 700; }
.t-gt    { color: var(--t-going-to) !important;           font-weight: 700; }
.t-fs    { color: var(--t-future-simple) !important;      font-weight: 700; }
.t-pperf { color: var(--t-present-perfect) !important;    font-weight: 700; }

/* ── THE EYEBROW TAKES THE COLOUR THE AUXILIARIES GAVE UP ────────────
   Innes: "headings like 'The form' can be green". Green was the auxiliary's
   for the whole line and is now nobody's - every chain wears its own tense -
   so it is free, and an eyebrow is exactly what it should go to: it labels
   the slide without competing with anything inside it, and one steady colour
   across all eight stations makes the deck's spine legible at a glance.
   #46d98a still ships as --mark-aux on all 24 decks, so Part I is unaffected
   and the token keeps its name and its meaning there. */
.slide .eyebrow { color: var(--mark-aux); }
/* And the sub-headings with it. Innes: "I didnt just want the eyebrow green
   here - other subheaders like Now, in general, Now, as you watch, etc should
   also be green to set them apart from past continuous yellow." Exactly the
   collision: every heading took the DECK's accent, and on station 12 that
   accent is the same gold the past continuous chain wears, so the label of a
   row and the grammar inside it were the same colour.
   One layer, one colour, on every station: green is the deck talking about the
   slide, and the chain colours are the grammar. Its closest chain neighbours
   are the turquoise at 96 and the going-to lime at 105 in RGB - both wider
   than the 50 the object magenta was chosen on, and the headings are 12px
   mono small-caps in their own position, so they read as a different layer
   before colour is considered.
   <strong> inside a .prose is only ever a card title - slidekit's cards() is
   the one place that emits it - so this cannot catch an inline bold. */
.slide .para-head { color: var(--mark-aux); }
.slide .card .prose strong { color: var(--mark-aux); }

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


# ── THE CHASSIS ALSO BRINGS THE CAMP'S PART 1 / PART 2 CHIP ─────────────
# Each Block Camp I camp is two decks and they now link to each other from the
# deck bar. A descent station is ONE deck, so that chip arrives meaning nothing
# and pointing into Part I: the first rebuild after the chip shipped put
# "Part 2 ->" on the Trial, aimed at Present Perfect Continuous Part 2.
#
# Deleting it would leave a station with no way out but the browser's back
# button, so it is retargeted instead, at the thing a station actually has a
# sibling relationship with: the descent route map. The data-i18n key is
# dropped with it - the chassis dictionary still holds the CAMP's word for
# "Part 2" in all three languages, and leaving the key would put that back on
# screen the moment somebody chose Deutsch. Same trap as the cover chips.
PART_LINK = re.compile(r'<a class="part-link"[^>]*>.*?</a>', re.S)


# ── THE CHAIN CARRIES ITS OWN TENSE'S COLOUR, EVERYWHERE ────────────────
# Innes, on two shipped stations at once: "we need a better color coding
# system / white = the agent / grey = the thing / is/are being = pink / past
# participle = purple / has/have been = turquoise / past simple= brown".
#
# The old system answered "what JOB is this word doing" - one green for every
# auxiliary in the line. On a descent where the whole point is which tense the
# chain is in, that is the one question the learner never needs answered: they
# can see it is an auxiliary. What they cannot see is which tense, and the
# trail already taught them a colour for each.
#
# So the tense colours stop being a contrast-slide special case and become the
# system. The mapping below is the whole auxiliary vocabulary of the eight
# stations, taken from the sources rather than imagined - grep the .aux spans
# and this is the complete list. Anything not in it keeps role green, so a new
# word cannot go unstyled; check-colour-roles.py's ORPHAN gate still watches.
#
# NOT the participle: it stays purple in every chain. It is the constant, and
# a learner who sees purple at the end of all seven has learned the rule the
# decks exist to teach.
#
# 'being' and 'been' on their own are the words the station-10 and station-15
# slides are ABOUT, and each belongs to exactly one chain, so they take that
# chain's colour: being pink, been turquoise. That is the answer to the slide's
# own question in the colour of the answer.
# THE RULE, AS INNES SETTLED IT ON 2026-09-01:
#
#   "is/are always blue - then is blue + being pink, was brown + being yellow"
#
# The be-auxiliary keeps its OWN tense's colour wherever it appears, and the
# word that changes the chain carries the tense the chain becomes. So 'is' is
# blue in every sentence in the line, and what follows it says which chain you
# are in: nothing (present simple), 'being' (present continuous, pink), 'going
# to' (lime). 'was' is brown everywhere, and 'was being' is brown then yellow.
#
# The first version coloured the whole span by the chain, which made 'is' lime
# inside 'is going to' and blue two slides later - "is/are not blue
# consistently in document". This is that fix, generalised to every chain
# rather than patched onto the one deck he was looking at.
#
# has / have are NOT split: unlike be they have no present-simple job in this
# line - a bare 'has' here is always the front of a perfect - so 'has been' is
# turquoise end to end.
#
# The vocabulary below is the complete set of auxiliary spans in the eight
# stations, taken by grepping the sources rather than imagined. Anything not
# in it keeps role green, so a new word cannot go unstyled, and
# check-colour-roles.py's ORPHAN gate watches for exactly that.
HEAD_TENSE = {
    'is': 't-ps', 'are': 't-ps', 'am': 't-ps',
    "isn't": 't-ps', "aren't": 't-ps',
    'was': 't-past', 'were': 't-past',
    "wasn't": 't-past', "weren't": 't-past',
}
# What the tail does to the chain, given the tense of the head it follows.
TAIL_TENSE = {
    'being':       {'t-ps': 't-pc', 't-past': 't-pastc'},
    'been':        {'t-ps': 't-pperf', 't-past': 't-pperf'},
    'going to':    {'t-ps': 't-gt'},
    'going to be': {'t-ps': 't-gt'},
}
# Spans that are one unit, with no be-auxiliary to hold out in front.
AUX_TENSE = {
    't-ps':    ['am', 'is', 'are', "isn't", "aren't"],
    't-past':  ['was', 'were', "wasn't", "weren't", 'did'],
    't-pperf': ['has', 'have', 'has been', 'have been',
                "hasn't been", "haven't been", 'been'],
    't-gt':    ['going to'],
}
AUX_LOOKUP = {w: cls for cls, words in AUX_TENSE.items() for w in words}
AUX_SPAN = re.compile(r'<em class="aux">([^<]*)</em>')

# A bare 'being' is the word a slide is ABOUT, with no auxiliary beside it to
# take its tense from, so it takes the station's. Only the two continuous
# stations differ; everywhere else 'being' means the present continuous, the
# chain it is introduced on.
STATION_TENSE = {
    'blockcamp-passive-present-continuous.html': 't-pc',
    'blockcamp-passive-past-continuous.html': 't-pastc',
}


def _norm(raw):
    """A named word wears inverted commas, and the closing one is the SAME
    entity as the apostrophe in isn't - so strip the wrapping pair before
    turning what is left into an apostrophe, or 'is' normalises to "is'"."""
    w = raw.replace('&nbsp;', ' ').strip()
    if w.startswith('&lsquo;') and w.endswith('&rsquo;'):
        w = w[len('&lsquo;'):-len('&rsquo;')]
    return w.replace('&rsquo;', "'").strip().lower()


def tense_in_situ(html, station_file=''):
    """Colour every auxiliary by the tense of the chain it belongs to."""
    bare_being = STATION_TENSE.get(station_file, 't-pc')

    def em(cls, text):
        return '<em class="%s">%s</em>' % (cls, text)

    def swap(m):
        raw = m.group(1).strip()
        words = _norm(raw).split()

        # head + tail: the be keeps its own tense, the tail carries the chain
        if len(words) > 1 and words[0] in HEAD_TENSE:
            head_cls = HEAD_TENSE[words[0]]
            tail = ' '.join(words[1:])
            tail_cls = TAIL_TENSE.get(tail, {}).get(head_cls)
            if tail_cls:
                # keep the ORIGINAL text, so entities and capitals survive
                head_txt = raw.split(' ')[0]
                tail_txt = raw[len(head_txt):].strip()
                if tail == 'going to be':
                    tail_txt, be = tail_txt[:-2].strip(), tail_txt[-2:]
                    return (em(head_cls, head_txt) + ' ' + em(tail_cls, tail_txt)
                            + ' ' + em('inf', be))
                return em(head_cls, head_txt) + ' ' + em(tail_cls, tail_txt)

        word = _norm(raw)
        if word == 'being':
            return m.group(0).replace('class="aux"', 'class="%s"' % bare_being, 1)
        cls = AUX_LOOKUP.get(word)
        return m.group(0) if not cls else m.group(0).replace(
            'class="aux"', 'class="%s"' % cls, 1)

    return AUX_SPAN.sub(swap, html)


def retarget_part_link(out, st):
    link = ('<a class="part-link" id="partLink" href="block-camp-descent-map.html">'
            'Descent map</a>')
    return PART_LINK.sub(link, out)


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
    body = tense_in_situ('\n\n    '.join([cover(cov, st)] + st['slides']), st['file'])
    out = head + body + tail
    out = retarget_part_link(out, st)
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
