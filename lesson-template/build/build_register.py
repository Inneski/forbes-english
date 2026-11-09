# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Heights of Register, formal and everyday
vocabulary as the height of a mountain island. The seventh chart.

    py lesson-template/build/build_register.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. One meaning, two heights: the everyday word lives on the
shore (get, buy, need), its formal twin near the summit (obtain, purchase,
require), and a footpath joins them. The higher you climb, the more formal
the writing: chat and texts on the shore, emails on the slopes, reports and
letters at the top. Phrasal verbs live in the valleys.

THE ART. Layout by sea_layouts_3.py (docs/sea-charts/heights-of-register.png),
painted by ChatGPT on 2026-11-09 with Gerundia as the style. Dots measured by
sea_measure.py into register_chart.json. The clean copy carried one dot the
layout never had, on the south-west cliffs at (346, 872); it was painted out
of chart-clean.jpg with cv2.inpaint and dropped from the JSON.
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE

OUT = 'sailing-the-seas-register.html'
ART = 'sailing-the-seas-register'
UID = 'reg'

# py lesson-template/extract-palette.py sailing-the-seas-register/hero.jpg --light
EXTRACTED = {'text': '#2a2211', 'text-dim': '#5e4e2e', 'secondary': '#adcbd5', 'contrast': '#0e5667'}

D = O.load('register_chart.json')
DOTS = [tuple(p) for p in D['dots']]
assert len(DOTS) == 16, DOTS


def near(x, y):
    p = min(DOTS, key=lambda q: abs(q[0] - x) + abs(q[1] - y))
    assert abs(p[0] - x) + abs(p[1] - y) < 12, (x, y, p)
    return p


# (everyday, formal, with a noun: everyday, formal, low dot, high dot, side of the high label)
TRAILS = [
    ('help', 'assist', 'help passengers', 'assist passengers', (648, 178), (720, 389), 'e'),
    ('need', 'require', 'need a passport', 'require a passport', (426, 226), (626, 410), 'w'),
    ('buy', 'purchase', 'buy tickets', 'purchase tickets', (252, 324), (552, 450), 'w'),
    ('get', 'obtain', 'get a visa', 'obtain a visa', (146, 454), (500, 496), 'w'),
    ('find out', 'discover', 'find out why', 'discover why', (1366, 624), (1008, 568), 'e'),
    ('enough', 'sufficient', 'enough time', 'sufficient time', (1210, 738), (956, 620), 'e'),
    ('ask', 'enquire', 'ask about prices', 'enquire about prices', (1078, 837), (890, 658), 'e'),
    ('start', 'commence', 'start at nine', 'commence at nine', (857, 898), (790, 676), 'w'),
]
TRAILS = [(a, b, c, d, near(*lo), near(*hi), side) for a, b, c, d, lo, hi, side in TRAILS]
assert len({t[4] for t in TRAILS} | {t[5] for t in TRAILS}) == 16
INK, LAND = '#2A2011', '#E9E2C4'
HIGH_INK, HIGH_LAND = '#2A1A2E', '#E7DCE6'


def key(w):
    return w.replace(' ', '-')


def overlay():
    spots, names = [], []
    for low, high, low2, high2, (lx, ly), (hx, hy), side in TRAILS:
        names.append(O.name(lx, ly, (low, low2, '%s &#183; everyday' % low), INK, LAND, size=20, dy=-15, fit=False, halo=.1))
        anchor, dx = ('end', -14) if side == 'w' else ('start', 14)
        names.append(O.name(hx, hy, (high, high2, '%s &#183; formal' % high), HIGH_INK, HIGH_LAND, size=20,
                            anchor=anchor, dx=dx, dy=6, fit=False, halo=.1))
        spots.append(O.hotspot(UID, key(low), O.circle_path(lx, ly, 26), '%s: the everyday word' % low))
        spots.append(O.hotspot(UID, key(high), O.circle_path(hx, hy, 26), '%s: the formal word' % high))
    spots.append(O.hotspot(UID, 'summit', O.circle_path(768, 540, 80), 'The summit: the most formal writing'))
    caps = [O.cap(768, 60, 'THE HEIGHTS OF REGISTER', '#1E2A30', 38, face=O.SERIF, spacing='.04em'),
            O.cap(768, 90, 'the higher you climb, the more formal the word', '#1E2A30', 19, face=O.SERIF, weight=600,
                  spacing='0', style='italic'),
            O.cap(768, 548, 'THE SUMMIT', '#1E2A30', 24, face=O.SERIF, spacing='.05em', halo='#F4F1EA'),
            O.cap(712, 722, 'FORMAL &#183; reports, letters', '#3A2440', 17, weight=600, spacing='0', style='italic', halo=HIGH_LAND),
            O.cap(712, 812, 'NEUTRAL &#183; emails', INK, 17, weight=600, spacing='0', style='italic', halo=LAND),
            O.cap(712, 910, 'EVERYDAY &#183; chat, texts', INK, 17, weight=600, spacing='0', style='italic', halo=LAND),
            O.cap(70, 980, 'phrasal verbs live in the valleys', '#1E2A30', 17, 'start', weight=600, spacing='0',
                  style='italic')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart of a round mountain island. Meadows and villages ring the shore, then farmland, '
            'then purple moorland, and a snowy summit in the middle. Eight footpaths climb from an everyday word on '
            'the shore to its formal twin near the top: get to obtain, buy to purchase, need to require, help to '
            'assist, start to commence, ask to enquire, enough to sufficient, find out to discover.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; formal and everyday words', 'The Heights of Register',
    'Most meanings have two words: one for a chat with a friend, one for a letter to a bank. On this island the '
    'everyday word lives on the shore and its formal twin near the summit, with a footpath between them. '
    'Before you write, ask how high you are standing, then choose the word that lives there.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the heights</div>
      <h2>One meaning, two heights</h2>
      <p class="chart-note" style="margin:-6px 0 18px"><em>Register</em> is how formal your English is. Neither height is wrong: the mistake is using a summit word on the shore, or a shore word at the summit.</p>
      ''' + rule_grid([
    ('The shore: everyday English',
     'Chat, texts, messages to friends. Short, common words, often phrasal verbs.',
     ex('Can you <em>find out</em> when the ferry leaves?')),
    ('The summit: formal English',
     'Reports, official letters, notices, applications. Longer words, often from Latin or French.',
     ex('Passengers must <em>obtain</em> a visa before travelling.')),
    ('The slopes: neutral English',
     'Most work emails sit halfway up: polite, clear, not stiff. <em>Need</em>, <em>help</em> and <em>start</em> are fine here.',
     ex('We <em>need</em> the figures by Friday.')),
    ('Same meaning, different height',
     '<em>Buy</em> and <em>purchase</em> mean the same. The height tells the reader what kind of text this is.',
     ex('Tickets may be <em>purchased</em> online.')),
    ('Formal words change the grammar around them',
     'Some take a different preposition or pattern: <em>ask about</em> but <em>enquire about</em>; <em>help someone</em> but <em>assist someone with</em>.',
     ex('Staff will <em>assist</em> you with your luggage.')),
    ('Do not mix heights in one text',
     'A formal letter with one shore word sounds careless; a chat with one summit word sounds like a joke.',
     ex('I&#39;m writing to <em>enquire</em> about the vacancy.')),
]) + chart(
    'The eight footpaths',
    'Each pair means roughly the same. The shore word works almost everywhere; the summit word only in formal writing.',
    ['On the shore', 'At the summit', 'In a formal sentence'],
    [['get', 'obtain', 'Visitors must obtain a permit.'], ['buy', 'purchase', 'Tickets may be purchased online.'],
     ['need', 'require', 'All passengers require a valid passport.'], ['help', 'assist', 'Staff will assist passengers.'],
     ['start', 'commence', 'Boarding will commence at nine.'], ['ask', 'enquire', 'Please enquire at the desk.'],
     ['enough', 'sufficient', 'There was not sufficient time.'], ['find out', 'discover', 'We discovered the cause.']]) + '''
    </div>

    '''

VALLEYS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The valleys</div>
      <h2>Phrasal verbs live low</h2>
      <p class="chart-note" style="margin:-6px 0 18px">A phrasal verb is a verb plus a small word: <em>find out</em>, <em>set up</em>, <em>put off</em>. They are everyday English, so in a formal text they are often swapped for one longer verb.</p>
      ''' + chart(
    'Down in the valley, up on the summit',
    'The phrasal verb is never wrong in speech. In a report or an official letter, the single verb usually reads better.',
    ['Phrasal verb', 'Formal verb', 'At the summit'],
    [['find out', 'discover', 'The inspectors discovered a leak.'], ['set up', 'establish', 'The company was established in 1902.'],
     ['put off', 'postpone', 'The meeting has been postponed.'], ['look into', 'investigate', 'We will investigate the complaint.'],
     ['go up', 'increase', 'Prices increased by 4%.'], ['carry on', 'continue', 'Please continue to the gate.'],
     ['turn down', 'reject', 'The offer was rejected.'], ['get in touch', 'contact', 'Please contact us for details.']]) + '''
      ''' + exi('The meeting has been <em>postponed</em> until Monday.') + chart(
    'Whole phrases climb too',
    'The same climb happens with whole phrases. Notices, emails to strangers and official letters live at the top.',
    ['On the shore', 'At the summit'],
    [['Thanks for your email.', 'Thank you for your email.'], ['Sorry about the delay.', 'We apologise for the delay.'],
     ['Can you send me the form?', 'Could you please send me the form?'], ['Let me know.', 'Please let me know.'],
     ['Talk soon.', 'I look forward to hearing from you.']]) + '''
      ''' + exi('We <em>apologise</em> for the delay.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a word and its line lights up below: shore words on the left, summit words in the middle. Switch the chart '
    'to see each word with a noun, then with its height: the meaning stays the same all the way up the path.',
    ('The words', 'With a noun', 'How high'),
    [('The shore &middot; everyday', 'is-west'), ('The summit &middot; formal', 'is-isle'),
     ('The valleys and the top', 'is-east')],
    'Drag the chart sideways to reach the east coast.', min_zoom=1000)

TRAPS = fork(
    'Wrong height, wrong ending',
    'The commonest mistakes are a summit word in a chat, and a summit word with a shore preposition.',
    ['Not this', 'This', 'Why'],
    [['Hey, did you purchase the milk?', 'Hey, did you buy the milk?', 'a chat lives on the shore'],
     ['I am writing to ask some questions about the job, and to find out the salary.',
      'I am writing to enquire about the position and its salary.', 'a formal letter lives at the summit'],
     ['Could you assist me to carry this?', 'Could you help me carry this? / assist me with this?', '<em>assist</em> takes <em>with</em>'],
     ['I need to enquire you something.', 'I need to ask you something.', '<em>enquire</em> takes no person'],
     ['We have sufficient of chairs.', 'We have enough chairs. / sufficient chairs.', 'no <em>of</em>']],
    'Words at the summit are not better English, only more formal English. Most writing at work sits on the slopes.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-soundings.html', 'Soundings of frequency')])

SIGNALS = signals(
    'You are on the shore',
    ['a chat or a text', 'a message to a friend', 'a phone call', '<em>Hi</em>, <em>Hey</em>, <em>Cheers</em>',
     'contractions: <em>I&#39;m</em>, <em>can&#39;t</em>', 'phrasal verbs: <em>find out</em>, <em>set up</em>'],
    'You are at the summit',
    ['a report or an official letter', 'a notice or a sign', 'an application or a complaint',
     '<em>Dear Sir or Madam</em>, <em>Yours faithfully</em>', 'no contractions: <em>I am</em>, <em>cannot</em>',
     'the passive: <em>tickets may be purchased</em>'],
    'One test: who will read it? A friend, the shore. A stranger at work, the slopes. An office or an official, the summit.')

QUIZ = [
    ('Formal notice: Passengers must ___ a valid ticket.', 'At the summit.', 'obtain',
     ['obtain', 'get', 'get hold of', 'grab'], 'A notice is formal: obtain is the summit word for get.'),
    ('Text to a friend: Can you ___ some bread on the way home?', 'On the shore.', 'buy',
     ['buy', 'purchase', 'acquire', 'procure'], 'A text lives on the shore: buy.'),
    ('Which is the formal twin of find out?', 'Read the footpath.', 'discover',
     ['discover', 'look out', 'find up', 'search'], 'Find out on the shore, discover at the summit.'),
    ('Formal letter: I am writing to ___ about the position.', 'Which word takes about?', 'enquire',
     ['enquire', 'ask you', 'question', 'ask for'], 'Enquire about something: the summit word for ask about.'),
    ('Staff will ___ you with your luggage.', 'Which word takes with?', 'assist',
     ['assist', 'help to', 'assistance', 'aid to'], 'Assist someone with something.'),
    ('Notice: Boarding will ___ at 9.00.', 'Start, at the summit.', 'commence',
     ['commence', 'kick off', 'get going', 'begin up'], 'Commence is the formal start.'),
    ('Which sentence is correct?', 'Watch the grammar around a summit word.', 'We have sufficient chairs.',
     ['We have sufficient chairs.', 'We have sufficient of chairs.', 'We have chairs sufficient.', 'We have sufficiently chairs.'],
     'Sufficient goes straight before the noun, like enough.'),
    ('Report: The meeting has been ___ until Monday.', 'The formal verb for put off.', 'postponed',
     ['postponed', 'put off', 'pushed back', 'moved off'], 'In a report, postponed: put off is the valley word.'),
    ('Which sentence is too formal for a chat?', 'One summit word on the shore.', 'Shall we commence lunch?',
     ['Shall we commence lunch?', 'Shall we start lunch?', 'Shall we have lunch?', 'Lunch now?'],
     'Commence in a chat sounds like a joke. Start, or have.'),
    ('All passengers ___ a valid passport.', 'Formal, present simple.', 'require',
     ['require', 'requires', 'are requiring', 'need of'], 'All passengers require: plural, so no -s.'),
    ('Which ending fits a formal email to a stranger?', 'The summit sign-off.', 'I look forward to hearing from you.',
     ['I look forward to hearing from you.', 'Talk soon!', 'Cheers!', 'Speak later.'],
     'I look forward to hearing from you: the formal close.'),
    ('Which pair is NOT a shore word and its summit twin?', 'One pair means different things.', 'ask / answer',
     ['ask / answer', 'get / obtain', 'need / require', 'buy / purchase'], 'Ask and answer are opposites, not two heights of one meaning.'),
]

PANELS = [
    [(key(t[0]), '<b>%s</b> &middot; %s' % (t[0], t[2])) for t in TRAILS],
    [(key(t[1]), '<b>%s</b> &middot; %s' % (t[1], t[3])) for t in TRAILS],
    [('summit', '<b>The summit</b> reports, official letters, notices'),
     ('summit', '<b>The slopes</b> work emails: <em>need</em>, <em>help</em>, <em>start</em> are fine'),
     ('summit', '<b>The valleys</b> phrasal verbs: <em>find out</em>, <em>set up</em>, <em>put off</em>')],
]
TARGETS = {}
for t in TRAILS:
    TARGETS[key(t[0])] = (0, key(t[0]), '#0e5667')
    TARGETS[key(t[1])] = (1, key(t[1]), '#6A3A6E')
TARGETS['summit'] = (2, 'summit', '#0e5667')

import ex_tr_register as T
L.build(OUT, ART, 'The Heights of Register &mdash; Formal and Everyday Words', 'formal and everyday words', EXTRACTED,
        HERO, 'then choose the word that lives there.', ('order', 'Read the chart'),
        RULES + VALLEYS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        ['#B9CC86', '#C9A9C4', '#D8C79A'], T.T,
        ['Clean run. You can tell how high you are standing, and choose the word that lives there.',
         'Solid progress. Before you write, ask who will read it.',
         'Good first attempt. Start with the eight footpaths: one meaning, two heights.'],
        ('sailing-the-seas-inversion.html', 'Next chart: the inversion maelstrom'), gull_seed=31)
