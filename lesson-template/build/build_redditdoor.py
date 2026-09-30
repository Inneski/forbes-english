# -*- coding: utf-8 -*-
"""Reddit × French Market: Getting in the Door (C1) — a new 16:9 panel deck
("house style 2"), the fourth lesson in the Reddit / French-market set.

The set so far: `forbes-reddit-french-market-c1.html` (vocabulary, register,
situational judgement), `forbes-roleplay-reddit-french-TEST-p3.html` (the
test) and the two Parisian Conquest RPGs (`forbes-dnd-rpg.html`,
`forbes-dnd-rpg-part2.html`), which start once the learner is already in
the room. None of them covers how he gets there. This one does: the cold
email, the gatekeeper call, the first meeting read the French way, and the
follow-up. The cast is the RPG's — Galeries Morel, Groupe Éclat, Maison
Éclore, Maison Lumière — so the four lessons read as one campaign.

Four parts, each opened by a divider and a panel, then teach cards of the
six phrases the part is built on, then practice:
  1 The cold approach   — cards ×2, MC ×3, gap ×2 (the email, four gaps)
  2 Past the gatekeeper — cards, order ×2, MC ×2
  3 Reading the room    — cards ×2, match, MC ×3
  4 The follow-up       — cards, gap ×2, sort (pushy / pitched / apologetic), MC ×2
then results and the activation stage. 37 slides, EN/DE/ES.

**Style 2.** Art: six slot plates briefed in docs/ARTWORK-reddit-door.md.
Until all six exist in `RedditFrench/` this writes a gitignored preview on
the two site pictures already in that folder (the café and the desk
silhouette); the live page is not written at all — the Contingency
precedent.

MC keys are checked against the longest-option rule at build time; the two
word banks are checked against gap order. Order slide 2 carries a decoy
("Might it be") that is wrong in every position.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_redditdoor as I

TPL = 'lesson-template/lesson-template.html'
LIVE = 'forbes-reddit-french-door-c1.html'
PREVIEW = '_forbes-reddit-french-door-c1.html'   # gitignored (leading underscore)
F = 'RedditFrench'

SLOTS = ('plate-cover', 'plate-door', 'plate-gate', 'plate-room',
         'plate-follow', 'plate-act')
PLACEHOLDER = {'plate-cover': 'cafe-hero.jpg', 'plate-door': 'office-silhouette-desk.jpg',
               'plate-gate': 'cafe-hero.jpg', 'plate-room': 'office-silhouette-desk.jpg',
               'plate-follow': 'cafe-hero.jpg', 'plate-act': 'cafe-hero.jpg'}
READY = all(os.path.exists(os.path.join(F, s + '.jpg')) for s in SLOTS)
PIC = {s: (s + '.jpg') if READY else PLACEHOLDER[s] for s in SLOTS}
OUT = LIVE if READY else PREVIEW
HERO, DOOR, GATE, ROOM, FOLLOW, ACT = (PIC[s] for s in SLOTS)

E = I.T['en']

# py lesson-template/extract-palette.py RedditFrench/plate-cover.jpg
# (derived from the placeholder cafe-hero.jpg until the plate lands; every
# row PASS)
PALETTE = """  --hero: url('%s/%s');

  --void          : #0c0e0a;
  --surface       : #171b14;
  --surface2      : #21271c;
  --border        : #7f4a3d;
  --text          : #f5f2f2;
  --text-dim      : #bfa9a3;
  --accent        : #d8654a;
  --accent-bright : #e99480;
  --accent-dim    : #9e3e28;
  --secondary     : #3a4d4d;
  --contrast      : #1dedb0;""" % (F, HERO)

# (phrase, body key, example) — the phrase and the example stay in English
CARDS = {
    1: [('What prompted me to write', 'c1',
         '“What prompted me to write was your interview in Les Echos on the Asian launch.”'),
        ('I’ll keep this brief', 'c2',
         '“I’ll keep this brief: one observation and one question.”'),
        ('We’ve been working with', 'c3',
         '“We’ve been working with two of the LVMH maisons on exactly this.”')],
    2: [('I’d welcome the chance to', 'c4',
         '“I’d welcome the chance to show you what French buyers are actually saying.”'),
        ('Would it be worth', 'c5',
         '“Would it be worth twenty minutes before your Q1 planning?”'),
        ('No need to reply if', 'c6',
         '“No need to reply if the timing is wrong; I’ll try again in the spring.”')],
    3: [('I was hoping to', 'c7',
         '“I was hoping to find fifteen minutes with Madame Morel before the end of the month.”'),
        ('Might there be', 'c8',
         '“Might there be a window after the Milan show?”'),
        ('I’ll be guided by you', 'c9',
         '“I’ll be guided by you on whether that goes to her directly or through you.”')],
    4: [('Could I leave it with you?', 'c10',
         '“Could I leave it with you, and check back in a fortnight?”'),
        ('I appreciate she’s', 'c11',
         '“I appreciate she’s in the middle of the budget round.”'),
        ('Would it help if I', 'c12',
         '“Would it help if I sent a one-page summary in French first?”')],
    5: [('Let me set out the premise', 'c13',
         '“Let me set out the premise before I show you anything.”'),
        ('I take it that', 'c14',
         '“I take it that the French launch is being run out of Paris, not London?”'),
        ('With respect', 'c15',
         '“With respect, the data on that point tells a different story.”')],
    6: [('Is that a no, or a not yet?', 'c16',
         '“Is that a no, or a not yet?”'),
        ('Shall we pick that up over lunch?', 'c17',
         '“Shall we pick that up over lunch?”'),
        ('I’ll let that sit', 'c18',
         '“I’ll let that sit for a moment; it is a lot to take in.”')],
    7: [('I’m conscious you’ll have a full inbox', 'c19',
         '“I’m conscious you’ll have a full inbox after the show.”'),
        ('Bumping this to the top', 'c20',
         '“Bumping this to the top of your inbox: any thoughts?”'),
        ('Since I last wrote', 'c21',
         '“Since I last wrote, two more French subreddits have passed 100k members.”')],
    8: [('I’ll take silence as', 'c22',
         '“I’ll take silence as ‘not this quarter’ and come back in March.”'),
        ('Close the loop', 'c23',
         '“I’d rather close the loop than keep writing into the void.”'),
        ('Park this until', 'c24',
         '“Shall we park this until the budget round is over?”')],
}
CARD_TITLE = {1: 'vt1', 2: 'vt2', 3: 'vt3', 4: 'vt3', 5: 'vt4', 6: 'vt5', 7: 'vt6', 8: 'vt6'}

# (ctx key, stem key, options, correct, why key)
MC = [
    ('x1', 's1',
     ['I hope this email finds you well and that the Milan show went as planned.',
      'What prompted me to write was your comment in Les Echos about launching in Asia.',
      'My name is Ciarán and I lead client partnerships at Reddit for the luxury sector.',
      'I’m reaching out because I’d love to connect and explore synergies with Galeries Morel.'],
     1, 'q1w'),
    ('x2', 's2',
     ['“I’d love to jump on a quick call whenever suits to walk you through our deck.”',
      '“Would it be worth twenty minutes before your Q1 planning? No need to reply if not.”',
      '“Please let me know your availability next week so we can schedule a meeting.”',
      '“I very much look forward to hearing from you at your earliest convenience about this.”'],
     1, 'q2w'),
    ('x3', 's3',
     ['Partnership opportunity: Reddit × Galeries Morel',
      'What French buyers said about your Asian launch',
      'Quick question about the Galeries Morel launch',
      'Introduction from Reddit’s client partnerships team'],
     1, 'q3w'),
    ('x4', 's4',
     ['“I completely understand. Might there be a window after the budget round, and would it help if I sent a one-pager first?”',
      '“That’s a shame, because this is genuinely important for her. Could you at least ask her whether she’d make an exception?”',
      '“No problem at all. I’ll try her directly on LinkedIn then, and perhaps we can find a time that works for both of us.”',
      '“I see. In that case, could you tell me who else in the business handles digital partnerships at director level?”'],
     0, 'q4w'),
    ('x5', 's5',
     ['“Could I leave it with you, and check back in a fortnight if I haven’t heard?”',
      '“Great, so you’ll speak to her this week and then come back to me by Friday, yes?”',
      '“Thanks anyway. I’ll send the deck to the general enquiries address instead.”',
      '“Perfect, I’ll call again tomorrow morning in case she has a moment for me then.”'],
     0, 'q5w'),
    ('x6', 's6',
     ['“Understood. Is that a no, or a not yet? The premise I set out was that this is research spend, not media spend.”',
      '“I hear you, but with respect, Reddit is not a forum any more, and your competitors have already understood that.”',
      '“That’s completely fair, and I don’t want to push. Perhaps we could revisit it next year once the platform has matured.”',
      '“Of course. Then let me show you the case studies from our UK clients, which I think will change your mind on that.”'],
     0, 'q6w'),
    ('x7', 's7',
     ['Wait. If it stretches, say “I’ll let that sit; it’s a lot to take in”, and wait again.',
      'Fill it: summarise the three benefits again more briefly, then ask whether he has any questions.',
      'Offer a discount: “If budget is the concern, there is some flexibility on the pilot pricing.”',
      'Move on: “Let me show you the timeline while you think about it,” and open the next slide.'],
     0, 'q7w'),
    ('x8', 's8',
     ['“With pleasure. Shall we pick up the question of the pilot over lunch?”',
      '“Thank you, but I have a train at two, so perhaps we could conclude now?”',
      '“Great idea! I’ll grab my laptop so we can run through the numbers there.”',
      '“Lovely. Let’s leave business at the door and just get to know each other.”'],
     0, 'q8w'),
    ('x9', 's9',
     ['“Just checking in to see whether you had a chance to look at my previous email yet. Would love to hear your thoughts on it!”',
      '“I’m conscious you’ll have a full inbox after Milan. Since I last wrote, r/beaute passed 100k members; chart attached.”',
      '“Following up on my email of the 12th. I would be grateful for a response at your earliest convenience.”',
      '“I haven’t heard back, so I assume this isn’t a priority. No worries at all, I’ll take you off my list.”'],
     1, 'q9w'),
    ('x10', 's10',
     ['“I’ll take silence as ‘not this quarter’ and come back in March, unless you tell me otherwise.”',
      '“I’ve now written four times without any reply, which I can only take to mean you are not interested.”',
      '“This is my last attempt to contact you, as I do not want to keep clogging up your inbox.”',
      '“Could you please just let me know either way, so I can stop chasing and update my records?”'],
     0, 'q10w'),
]
assert len(MC) == 10
MC_PART = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4]

# rows: (sentence, [answer], why key); bank must not be in gap order
GAP1 = [
    ('I’ll keep this ______: one observation and one question.', ['brief'], 'gw1'),
    ('What ______ me to write was your interview in Les Echos on the Asian launch.',
     ['prompted'], 'gw2'),
    ('I’d ______ the chance to show you what French buyers are actually saying about it.',
     ['welcome'], 'gw3'),
    ('No ______ to reply if the timing is wrong; I’ll try again in the spring.',
     ['need'], 'gw4'),
]
BANK1 = ['welcome', 'need', 'brief', 'prompted']
GAP2 = [
    ('I’m ______ you’ll have a full inbox after Milan.', ['conscious'], 'gw5'),
    ('______ I last wrote, two more French subreddits have passed 100k members.',
     ['since'], 'gw6'),
    ('I’d rather ______ the loop than keep writing into the void.', ['close'], 'gw7'),
    ('Shall we ______ this until the budget round is over?', ['park'], 'gw8'),
]
BANK2 = ['park', 'close', 'conscious', 'since']

ORDER1 = ['I was hoping', 'to find fifteen minutes', 'with Madame Morel',
          'before the end of the month']
ORDER2 = ['Might there be', 'a window', 'after the Milan show', 'for a short call?']
ORDER2_DECOY = ['Might it be']

MATCH = [
    ('set out the premise', 'state the reasoning before the proposal'),
    ('an opening position', 'a first “no” that can still move'),
    ('pre-socialise', 'share a proposal informally before the formal meeting'),
    ('the long lunch', 'the part of the meeting that happens at the table'),
    ('let it sit', 'leave a silence rather than fill it'),
]

SORT_BINS = ['Too pushy', 'Well pitched', 'Too apologetic']
SORT_ITEMS = [
    ('“I’ve chased three times now.”', 0),
    ('“I’m conscious you’ll have a full inbox.”', 1),
    ('“So sorry to bother you again.”', 2),
    ('“Please respond by Friday.”', 0),
    ('“Shall we park this until March?”', 1),
    ('“Apologies for the repeated emails.”', 2),
    ('“Can you just give me a yes or no?”', 0),
    ('“Since I last wrote, one thing has changed.”', 1),
    ('“I know you’re busy and I’m really sorry to add to it.”', 2),
]


def divider(n, pic, pos=None):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=pic, pos=pos)


def intro(n, pic, side, pos):
    return D.panel('e%d' % n, E['e%d' % n], 'p%dt' % n, E['p%dt' % n],
                   [('p%da' % n, E['p%da' % n]), ('p%db' % n, E['p%db' % n], 'dim')],
                   folder=F, pic=pic, side=side, pos=pos)


def cards(part, n):
    tk = CARD_TITLE[n]
    return D.teach('e%d' % part, E['e%d' % part], tk, E[tk],
                   [(None, w, k, E[k], None, ex) for w, k, ex in CARDS[n]],
                   cols='1fr 1fr 1fr')


def mc(i):
    xk, sk, opts, c, why = MC[i]
    part = MC_PART[i]
    return D.mc(i + 1, len(MC), dict(stem=E[sk], options=opts, correct=c, why=why),
                'e%d' % part, E['e%d' % part], 'mt%d' % part, E['mt%d' % part],
                ctx=E[xk], ctx_key=xk, stem_key=sk)


def gap(i, rows, bank, part, tk):
    # Two rows a slide: four rows plus the bank ran 84px off the canvas.
    return D.gap(i, 4, rows, bank, 'e%d' % part, E['e%d' % part],
                 tk, E[tk], hint=E['gh'], hint_key='gh', width=150, size=20)


def build():
    logo = D.logo_from(TPL)
    D.assert_no_key_is_longest([dict(options=o, correct=c) for _, _, o, c, _ in MC])
    D.assert_bank_is_not_a_key(BANK1, [r[1][0] for r in GAP1])
    D.assert_bank_is_not_a_key(BANK2, [r[1][0] for r in GAP2])

    slides = "".join([
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])]),

        divider(1, DOOR),
        intro(1, DOOR, 'left', '20% 50%'),
        cards(1, 1), cards(1, 2),
        mc(0), mc(1), mc(2),
        gap(1, GAP1[:2], BANK1, 1, 'gt1'), gap(2, GAP1[2:], BANK1, 1, 'gt1'),

        divider(2, GATE),
        intro(2, GATE, 'right', '80% 50%'),
        cards(2, 3), cards(2, 4),
        D.order(ORDER1, 'e2', E['e2'], 'ot1', E['ot1'], 'oh1', E['oh1'], 'ow1'),
        D.order(ORDER2, 'e2', E['e2'], 'ot2', E['ot2'], 'oh2', E['oh2'], 'ow2',
                decoys=ORDER2_DECOY),
        mc(3), mc(4),

        divider(3, ROOM),
        intro(3, ROOM, 'left', '50% 50%'),
        cards(3, 5), cards(3, 6),
        D.match(MATCH, 'e3', E['e3'], 'mtt', E['mtt'], 'matchHint', E['matchHint'],
                'matchWhy'),
        mc(5), mc(6), mc(7),

        divider(4, FOLLOW),
        intro(4, FOLLOW, 'right', '30% 50%'),
        cards(4, 7), cards(4, 8),
        gap(3, GAP2[:2], BANK2, 4, 'gt2'), gap(4, GAP2[2:], BANK2, 4, 'gt2'),
        D.sort_slide(SORT_BINS, SORT_ITEMS, 'e4', E['e4'], 'st', E['st'], 'sh', E['sh'],
                     'sw', bin_keys=['sb1', 'sb2', 'sb3']),
        mc(8), mc(9),

        D.results(),
        D.activate(E['actTitle'], E['actUse'],
                   ['What prompted me to write', 'Would it be worth', 'Might there be',
                    'I’ll be guided by you', 'Is that a no, or a not yet?',
                    'I’m conscious you’ll have', 'I’ll take silence as'],
                   'Speaking', E['actSpeakBrief'],
                   [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                   E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                   folder=F, bg=ACT),
    ])

    n = slides.count('<section class="slide')
    assert ('%d slides' % n) == E['chipCount'], (n, E['chipCount'])
    langs = tuple(c for c in I.LANGS if c in I.T)
    D.assemble(TPL, OUT, slides, PALETTE,
               'Reddit &times; French Market: Getting in the Door (C1) | Forbes English',
               I, langs=langs)
    print('wrote %s — %d slides, %s%s' % (OUT, n, ','.join(langs),
          '' if READY else ' (PREVIEW: plates missing, see docs/ARTWORK-reddit-door.md)'))


if __name__ == '__main__':
    build()
