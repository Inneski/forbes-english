# -*- coding: utf-8 -*-
"""Talk Me Through the Last Job: Customer Interviews on Site (B2-C1).
House style 1, through hs1.py.

Written 2026-11-17 for a product manager at a Swiss maker of vapour
barriers and roofing and cladding membranes. His customers are carpenters,
roofers and retailers; he runs market research with them in England and
Ireland and talks to suppliers about product development. He asked for the
focus to be entirely on speaking.

Four lessons on the site already cover his ground, so this one is built in
the gap between them rather than over them:
  * Product Strategy & Market Research Speaking (C1): general discussion;
  * Talking About Your Product (B1): open vs closed questions, a pitch;
  * Within Spec, Below Standard (B2-C1): the supplier meeting;
  * Bringing a Membrane to Market (B2): launch language, word stress.
What none of them does is the moment on site with a British or Irish
tradesperson: the trade's own words for his products (VCL, breather
membrane, laps, the merchant, the trade), the understatement that makes
interview notes wrong ("it's grand" recorded as praise), and the three
interviewing moves that get past it (open on a real job, probe their word,
play it back). Then three role cards the teacher plays, and a 60-second
report back to head office.

Speaking-first, as he asked. The writing track that HOUSE-STYLE §10b
requires is his interview guide for the next visit: writing in service of
the conversation, not a writing task for its own sake.

Art: no hero was supplied. The plates are copies of existing domain art
(SupplierQuality's roofers, roof, rolls and office; ProductSpeaking's trade
fair; roofing's factory roof), byte-identical so git stores them once. The
owed slots below get the texture field until real plates land; their
briefs are the shopping list.

Run from the repo root:  python3 lesson-template/build/build_siteinterviews.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
import deck as D
import hs1
import i18n_siteinterviews as I

F = 'SiteInterviews'
OUT = 'customer-interviews-on-site-b2-c1.html'
TITLE = 'Talk Me Through the Last Job: Customer Interviews on Site (B2–C1)'
E = I.T['en']

POP = {}
K = hs1.Deck(F, pop=POP, cover_mode='square', title_px=60, cover_w=44)

# The deck's own plates. Each slide asks for its own slot and falls back to
# a borrowed plate until that slot's picture lands in SiteInterviews/, so
# the art can arrive one picture at a time with no code change. `--brief`
# writes docs/ARTWORK-site-interviews.md from this table; edit it here.
# (slot, borrowed fallback, what the picture shows). Subject centred, one
# clear subject: hs1 crops to it and the cover cuts it out.
PLATES = [
    ('hero', None, 'two roofers kneeling on a pitched roof rolling out a breather membrane, one of them looking up mid-sentence at a man in a fleece with a notebook standing on the scaffold beside them'),
    ('p-warm', 'crew', 'a man in a fleece with a notebook and a roofer in a hard hat chatting on scaffolding beside a half-finished roof'),
    ('p-specced', 'roll', 'an architect\'s roof drawing unrolled on a site table, weighted with a roll of membrane and a tape measure'),
    ('p-callback', 'roof', 'a roofer on a ladder looking up at a damp patch under the eaves of a house, his van parked below'),
    ('p-trade', 'fair', 'a builders\' merchant trade counter, rolls of membrane stacked behind it, a tradesman in hi-vis being served'),
    ('p-firstfix', 'crew', 'a carpenter stapling a vapour control layer across the timber studs of a house frame, no plasterboard yet'),
    ('p-grand', 'hero', 'a roofer on a cottage roof in light Irish drizzle giving a so-so shrug, green hills behind'),
    ('p-faff', 'crew', 'a carpenter wrestling with tangled tape around a window opening in a timber-frame wall'),
    ('p-tape', 'roll', 'a roofer kneeling and pressing tape along the overlap of two membrane sheets with a small approving nod'),
    ('p-shelf', 'fair', 'rolls of membrane gathering dust on a warehouse shelf, an empty gap beside them where another product sold out'),
    ('p-dear', 'roof', 'a roofer frowning at a long receipt beside a stack of membrane rolls on a van\'s tailgate'),
    ('p-switch', 'suits', 'a site manager in a hard hat on the phone beside a half-built house, weighing something up'),
    ('p-tea', 'horizon', 'a roofer and a man in a fleece sitting on a stack of pallets on site with mugs of tea, talking'),
    ('p-ask', 'roll', 'a roofer describing a roof with both hands while a man in a fleece listens, notebook closed'),
    ('p-probe', 'hero', 'a gloved hand holding up a corner of membrane, another hand pointing at a crease in it'),
    ('p-decide', 'factory', 'an architect, a builder and a roofer leaning over drawings spread on a car bonnet on site'),
    ('p-playback', 'crew', 'a man holding up a short length of membrane and explaining, a roofer listening with arms folded'),
    ('p-choose', 'roof', 'two rolls of membrane in different colours side by side on a roof, a gloved hand reaching between them'),
    ('p-galway', 'hero', 'a crew of four roofers on a cottage roof in the west of Ireland, stone walls and the sea behind'),
    ('p-kent', 'crew', 'a timber-frame house going up in the Kent countryside, an oast house in the distance, a site manager with a clipboard'),
    ('p-manchester', 'fair', 'a builders\' merchant yard among red-brick warehouses, a forklift carrying pallets of membrane rolls, a branch manager in a fleece'),
    ('p-report', 'suits', 'a man presenting from a laptop to a small team in a meeting room, mountains through the window'),
]
FALLBACK = {slot: fb for slot, fb, _ in PLATES}
STEM = ('flat mid-century screen-print illustration, {}, muted slate blue, cream and dusty pink palette, '
        'fine grain, hard silhouettes, one clear subject in the centre, calm open edges, no text '
        '--ar 16:9 --stylize 200 --sref https://forbesenglish.com/SupplierQuality/bg-meeting.jpg '
        '--no text, letters, numbers, logo, watermark')


def P(slot):
    """This slide's own plate once it has landed, else the borrowed one."""
    return slot if K.has(slot) or not FALLBACK.get(slot) else FALLBACK[slot]


# ── content ────────────────────────────────────────────────────────────
MC1 = [  # stage 1: the trade's words
    dict(stem='The architect ____ your breather membrane, but the contractor swapped it out for a cheaper one.',
         options=['specced', 'specialised', 'spaced', 'speculated'], correct=0, why='q1w'),
    dict(stem='“We had three ____ last winter. Water was coming in at the laps.”',
         options=['callbacks', 'recalls', 'comebacks', 'returns'], correct=0, why='q2w'),
    dict(stem='“The ____ ask for it by name, so we always keep it in stock.”',
         options=['trade', 'traders', 'tradesman', 'trading'], correct=0, why='q3w'),
    dict(stem='The carpenters fit the VCL at ____, before the plasterboard goes up.',
         options=['first fix', 'second fix', 'final fix', 'pre-fix'], correct=0, why='q4w'),
]
MC1_SLOTS = ['p-specced', 'p-callback', 'p-trade', 'p-firstfix']

MC2 = [  # stage 2: what they mean (ctx key, quote, options)
    ('c5', dict(stem='“Ah, it’s grand, yeah. Does the job.”',
                options=['It’s acceptable, but they aren’t excited by it.',
                         'They think it’s excellent, better than the rest.',
                         'They think it’s too heavy to carry up the ladder.',
                         'They want a bigger discount before they buy more.'], correct=0, why='q5w')),
    ('c6', dict(stem='“It’s a bit of a faff around the windows.”',
                options=['It takes extra time and effort around the windows.',
                         'It looks a bit untidy there, but nobody will see it.',
                         'It costs a bit more for the small pieces around them.',
                         'It works better around windows than on open walls.'], correct=0, why='q6w')),
    ('c7', dict(stem='“Not bad at all, to be fair.”',
                options=['They like it, and say so in a modest way.',
                         'It’s poor, and they’re trying to be polite.',
                         'They haven’t tried it yet, so they can’t say.',
                         'It’s fine, but only if the price comes down.'], correct=0, why='q7w')),
    ('c8', dict(stem='“To be honest, it doesn’t really move.”',
                options=['It sells slowly and sits on the shelf.',
                         'It’s too heavy for the lads to carry.',
                         'It slips on the roof in wet weather.',
                         'Deliveries to the branch are often late.'], correct=0, why='q8w')),
    ('c9', dict(stem='“It’s fierce dear for what it is.”',
                options=['It’s very expensive for what you get.',
                         'It’s good value, and the lads love it.',
                         'It’s a bit pricey, but worth every cent.',
                         'It’s hard to find in the merchants here.'], correct=0, why='q9w')),
    ('c10', dict(stem='“I wouldn’t say no, if the price was right.”',
                 options=['They would switch, on one condition: price.',
                          'They won’t switch, whatever the price is.',
                          'They want you to call back later in the year.',
                          'They have already decided to switch to you.'], correct=0, why='q10w')),
]
MC2_SLOTS = ['p-grand', 'p-faff', 'p-tape', 'p-shelf', 'p-dear', 'p-switch']

MC3 = [  # stage 3: the better question (ctx key, stem key, q)
    ('c11', 's11', dict(options=['How do you get on with the tape?',
                                 'Don’t you find our tape much easier?',
                                 'You like the new tape, don’t you?',
                                 'Is it the best tape you’ve ever used?'], correct=0, why='q11w')),
    ('c12', 's12', dict(options=['When you say fiddly, what do you mean?',
                                 'Fiddly? Is that because it’s too thin?',
                                 'OK, fiddly. And how is the price for you?',
                                 'Fiddly? Most roofers say it’s really easy.'], correct=0, why='q12w')),
    ('c13', 's13', dict(options=['On your last job, who decided what went on?',
                                 'Do you always choose the membrane yourself?',
                                 'Would you choose our membrane if you could?',
                                 'Is it usually the architect who decides it?'], correct=0, why='q13w')),
]
MC3_SLOTS = ['p-ask', 'p-probe', 'p-decide']

# Keys are written first above, for readability; deal them across the
# letters in the source (check-lesson KEYS), by a fixed rotation.
def _deal(q, at):
    o = q['options']
    k = len(o) - at % len(o)
    q['options'] = o[k:] + o[:k]
    q['correct'] = at % len(o)


for _n, _q in enumerate(MC1 + [q for _, q in MC2] + [q for _, _, q in MC3]):
    _deal(_q, (_n * 3 + 1) % 4)

D.assert_no_key_is_longest(MC1, 'MC1')
D.assert_no_key_is_longest([q for _, q in MC2], 'MC2')
D.assert_no_key_is_longest([q for _, _, q in MC3], 'MC3')

APOS = lambda a: '|'.join(sorted({a, a.replace('’', "'"), a.replace("'", '’')}))
GAP_A = [
    ('______ me through the last job where you used it.', ['Talk|Walk'], 'g1w'),
    ('When you ______ “fiddly”, what do you mean exactly?', ['say'], 'g2w'),
    ('That’s interesting. Can you give me an ______?', ['example'], 'g3w'),
]
GAP_B = [
    ('So if I’ve ______ you correctly, it’s the time on the roof, not the price?',
     ['understood|got'], 'g4w'),
    ('What would it ______ for you to switch to a different membrane?', ['take'], 'g5w'),
    ('On that job, who ______ the final decision on the membrane?', ['made|took'], 'g6w'),
]

ORDERS = [
    (['So', 'if I’ve got this right,', 'it’s not the price,', 'it’s the time', 'on the roof?'], 'o1w', 'p-playback'),
    (['What', 'would it take', 'for you', 'to switch', 'suppliers?'], 'o2w', 'p-choose'),
]

TALK_W = [
    'Who was the last customer you talked to: a roofer, a carpenter or a retailer? What did you learn?',
    'What do you most want to find out from customers in England and Ireland this year?',
    'Which is harder for you in English: asking the questions, or understanding the answers?',
    'How are roofers in the UK or Ireland different from roofers in Switzerland?',
    'What do your customers complain about most? How do they say it?',
    'When did something a customer said change a product decision?',
]
TALK_2 = [
    'Which of your customers praise things the least? How do you know when they are really happy?',
    'When a Swiss carpenter says “passt schon”, what does it mean? Is it the same as “it’s grand”?',
    'Think of the last complaint you heard. Was it softened? What was the real problem?',
    'A roofer tells you your product is “a bit dear”. What do you ask next?',
    'A survey or a conversation on site: which tells you more? Give a real example.',
    'Who in your company needs to hear what customers really say, in their words?',
]
DEBRIEF = [
    'The main thing we learned is that …',
    'What surprised me was …',
    'In their words: “…” What they meant was …',
    'What we still don’t know is …',
    'So my recommendation is to …',
    'The next step is to talk to …',
]


# ── slide helpers ──────────────────────────────────────────────────────
def b(keys):
    return [(k, E[k]) for k in keys]


def role(n):
    """A role card: who the customer is, and what to find out. Instructions,
    so every line translates; the teacher improvises the customer."""
    finds = ''.join('<li data-i18n="role%d%s" style="margin:6px 0">%s</li>' % (n, x, E['role%d%s' % (n, x)])
                    for x in 'abc')
    return '''
    <section class="slide" data-type="discuss">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="e4">%s</div>
        <h2 class="slide-title" data-i18n="role%dT">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="card tab-card"><span class="tab-pill" data-i18n="roleWho">%s</span>
          <p class="prose" style="font-size:18.5px;line-height:1.45" data-i18n="role%dd">%s</p></div>
        <div class="card tab-card" style="margin-top:14px"><span class="tab-pill" data-i18n="roleFind">%s</span>
          <ul style="font-size:18.5px;line-height:1.4">%s</ul></div>
        <p class="prose dim" style="margin-top:12px;font-size:16px" data-i18n="roleRule">%s</p>
      </div>
    </section>
''' % (E['e4'], n, E['role%dT' % n], E['roleWho'], n, E['role%dd' % n], E['roleFind'], finds, E['roleRule'])


def slides():
    s = [K.cover(E)]
    s.append(K.frame(K.talk('eW', 'tkWT', TALK_W, E), P('p-warm')))

    # ── stage 1 · the words on the roof ────────────────────────────────
    K.stage()
    s.append(D.rules('e1', E['e1'], 'r1T', E['r1T'], [
        (('pRoof', E['pRoof']), b(['r1a', 'r1b', 'r1c']),
         'We <strong>lap</strong> it and <strong>tape</strong> it, then the <strong>counter-battens</strong> go on.'),
        (('pTrade', E['pTrade']), b(['r1d', 'r1e', 'r1f']),
         'It was <strong>specced</strong>, but the builder <strong>swapped it out</strong>.'),
        (('pCounter', E['pCounter']), b(['r1g', 'r1h', 'r1i']),
         'The <strong>trade</strong> ask for it, so it <strong>moves</strong>.'),
    ]))
    s.append(D.match([
        ('breather membrane', 'lets water vapour out of the roof but keeps the rain out'),
        ('VCL', 'stops warm, moist air from inside reaching the insulation'),
        ('counter-batten', 'runs along the rafter, over the membrane, under the battens'),
        ('lap', 'the overlap where one sheet of membrane covers the next'),
        ('callback', 'going back to a finished job to put a problem right'),
        ('builders’ merchant', 'the shop where tradespeople buy their materials'),
    ], 'e1', E['e1'], 'mT', E['mT'], 'mHint', E['mHint'], 'mWhy'))
    for n, (q, slot) in enumerate(zip(MC1, map(P, MC1_SLOTS))):
        s.append(K.frame(D.mc(n + 1, len(MC1), q, 'e1', E['e1'], 'mc1T', E['mc1T']), slot,
                         text=(q['stem'], q['options'])))

    # ── stage 2 · what they really mean ────────────────────────────────
    K.stage()
    s.append(D.rules('e2', E['e2'], 'r2T', E['r2T'], [
        (('pPraise', E['pPraise']), b(['r2a', 'r2b']), 'It’s <strong>not bad at all</strong>, to be fair.'),
        (('pGrand', E['pGrand']), b(['r2c', 'r2d']), 'Ah, it’s <strong>grand</strong>. Does the job.'),
        (('pSoft', E['pSoft']), b(['r2e', 'r2f']), 'The lads <strong>aren’t mad about</strong> the tape.'),
    ]))
    for n, ((ck, q), slot) in enumerate(zip(MC2, map(P, MC2_SLOTS))):
        s.append(K.frame(D.mc(n + 1, len(MC2), q, 'e2', E['e2'], 'mc2T', E['mc2T'],
                              ctx=E[ck], ctx_key=ck), slot, text=(q['stem'], q['options'])))
    s.append(K.frame(K.talk('e2', 'tk2T', TALK_2, E), P('p-tea')))

    # ── stage 3 · questions that get the truth ─────────────────────────
    K.stage()
    s.append(D.rules('e3', E['e3'], 'r3T', E['r3T'], [
        (('pOpen', E['pOpen']), b(['r3a', 'r3b']), '<strong>Talk me through</strong> the last roof you did.'),
        (('pProbe', E['pProbe']), b(['r3c', 'r3d']), '<strong>When you say</strong> fiddly, <strong>what do you mean</strong>?'),
        (('pBack', E['pBack']), b(['r3e', 'r3f']), '<strong>So if I’ve got this right</strong>, it’s the time, not the price?'),
    ]))
    for n, ((ck, sk, q), slot) in enumerate(zip(MC3, map(P, MC3_SLOTS))):
        q = dict(q, stem=E[sk])
        s.append(K.frame(D.mc(n + 1, len(MC3), q, 'e3', E['e3'], 'mc3T', E['mc3T'],
                              ctx=E[ck], ctx_key=ck, stem_key=sk), slot, text=(q['stem'], q['options'])))
    for rows in (GAP_A, GAP_B):
        s.append(D.gap(1, 1, rows, None, 'e3', E['e3'], 'gapT', E['gapT'],
                       hint=E['gHint'], hint_key='gHint', size=21))
    for items, why, slot in ORDERS:
        s.append(K.frame(D.order(items, 'e3', E['e3'], 'orderT', E['orderT'], 'orderHint',
                                 E['orderHint'], why), P(slot)))

    # ── stage 4 · run the conversation ─────────────────────────────────
    K.stage()
    s.append(K.frame(role(1), P('p-galway')))
    s.append(K.frame(role(2), P('p-kent')))
    s.append(K.frame(role(3), P('p-manchester')))
    s.append(K.frame(K.talk('e4', 'debT', DEBRIEF, E), P('p-report')))
    s.append(K.frame(D.results(), 'horizon'))
    chips = ['Talk me through …', 'When you say …, what do you mean?', 'Can you give me an example?',
             'So if I’ve understood you …', 'What would it take for you to …?', 'Who made the decision?']
    s.append(K.activation(D.activate(E['actTitle'], E['actUse'], chips, 'Speaking', E['actSpeakBrief'],
                                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                                     E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'])))
    return ''.join(s)


def build():
    body = slides()
    n = body.count('<section class="slide')
    for c in ('en', 'de', 'es'):
        assert str(n) in I.T[c]['chipCount'], '%s chipCount %r, deck has %d' % (c, I.T[c]['chipCount'], n)
    K.assemble(OUT, body, TITLE, I, ('en', 'de', 'es'))


BRIEF = 'docs/ARTWORK-site-interviews.md'
DROP = 'incoming/site-interviews'
WIN = 'C:\\Users\\black\\Documents\\FORBES\\'


def brief():
    """The Midjourney brief, from PLATES. Makes the drop folder too
    (CLAUDE.md: a brief that names a drop folder creates it)."""
    os.makedirs(DROP, exist_ok=True)
    have = [x for x, _, _ in PLATES if x != 'hero' and K.has(x)]
    out = ['# Talk Me Through the Last Job: Midjourney brief', '',
           'Generated by `py lesson-template/build/build_siteinterviews.py --brief`; edit PLATES in the builder, not this file.', '',
           'The deck shipped on plates borrowed from Within Spec, Below Standard, Talking About Your Product and the '
           'roofing lesson. These %d are its own. Each slide switches to its own picture the moment that picture is '
           'in, one at a time, so there is no need to make them all at once.' % len(PLATES), '',
           '## How to use it', '',
           '1. Paste each prompt into Midjourney as it is. `--sref` points at the roofers plate already on the live '
           'site, so the new set matches the borrowed one; add your own style images as usual.',
           '2. Pick the best of the four, upscale it, and save it under the name shown (`hero.png`, `p-warm.png` …) in',
           '   [%s%s](../%s)' % (WIN, DROP.replace('/', '\\'), DROP),
           '3. Tell a local Claude session "site interviews art is in", or run `/publish`.', '',
           'Keep the subject in the middle with calm space round it: the deck crops to the subject, and the cover '
           'cuts the hero out and pops it out of a square.', '']
    if have:
        out += ['Already in: %s.' % ', '.join(have), '']
    out += ['## The pictures (%d)' % len(PLATES), '']
    for n, (slot, fb, idea) in enumerate(PLATES, 1):
        where = 'the cover and the library card' if slot == 'hero' else 'until it lands: `%s.jpg`' % fb
        out += ['### %d. `%s.png` (%s)' % (n, slot, where), '', '```', STEM.format(idea), '```', '']
    out += ['## For the Claude session that puts them in', '',
            '```bash',
            'python3 tools/prep-artwork.py incoming/site-interviews/ --into SiteInterviews --keep-names --dry-run',
            'python3 tools/prep-artwork.py incoming/site-interviews/ --into SiteInterviews --keep-names',
            '```', '',
            '- A new `hero`: it replaces the borrowed `SiteInterviews/hero.jpg` (`--force` past the duplicate check '
            'if needed). Delete `SiteInterviews/pop-cover.webp` so the cover is cut again, and recut '
            '`LibraryCards/customer-interviews-on-site-b2-c1.jpg` (1200x512) from it.',
            '- Then `python3 lesson-template/build/build_siteinterviews.py`, look at every new crop and pop, '
            '`node lesson-template/check-lesson.js customer-interviews-on-site-b2-c1.html`, '
            '`python3 tools/seo.py` last, and re-run `--brief` so this file lists what is in.',
            '- The borrowed plates stay in the folder while any slide still falls back to one.', '']
    open(BRIEF, 'w', encoding='utf-8', newline='').write('\n'.join(out))
    print('wrote %s (%d plates); drop folder %s exists' % (BRIEF, len(PLATES), DROP))


if __name__ == '__main__':
    if '--brief' in sys.argv:
        brief()
    else:
        build()
