# -*- coding: utf-8 -*-
"""Escape from Alcatraz (A2) — an escape-room deck.

New lesson, built to the house style, and the first one to use three
mechanics that did not exist in the engine before this build. They live
in `lesson-template/lesson-template.html` and `deck.py`, not in this
file, so every future lesson inherits them:

  * `search` — a timed identify-the-object hunt over unlabelled line
    drawings (`icons.py`). The names stay hidden while the clock runs,
    because a labelled picture turns a vocabulary task into a reading
    task: the learner scans for the word in the stem instead of
    recognising the thing.
  * `lock`   — a combination lock. The digits are earned one per room.
  * the rail — a strip of stops along the bottom that remembers which
    room you are in and which digit you picked up there. It exists so
    that the final lock tests *reading an instruction in English*
    ("the lock takes them backwards") rather than testing memory. A2
    learners have enough to carry.

Everything else is the standard set: cover, teaching slides, MC, gap,
sort, order, results, activation.

Three decisions worth recording.

**The rules translate; the examples do not.** `deck.teach` grew an
optional key for a card's body for this lesson. At B2 the house split —
heading translated, body left in English — is right, because the body is
the language being taught. At A2 it is not: a learner who cannot read
the rule cannot use it, and that is the level's whole problem. So the
rules are translated into all ten languages and only the worked examples
stay English.

**The escapees are real; the protagonist is not.** The June 1962 escape
is taught as fact on its own slide (Morris and the Anglin brothers, the
false heads, the fifty-odd raincoats, West left behind, the FBI closing
the case in 1979) and every figure in it is sourced. The learner plays
an invented prisoner on an invented route, so nothing is put in a real
person's mouth.

**Every distractor is wrong for a reason the lesson taught**, and no key
is the longest option — `assert_no_key_is_longest` runs over all of them
at build time.
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(os.path.dirname(HERE))

import deck as D
import icons
import i18n_alcatraz as I

E = I.T['en']
F = 'Alcatraz'
TPL = os.path.join(ROOT, 'lesson-template', 'lesson-template.html')
OUT = os.path.join(ROOT, 'escape-from-alcatraz-a2.html')

PALETTE = """  --hero: url('Alcatraz/hero.jpg');

  --void          : #0d1314;
  --surface       : #152122;
  --surface2      : #1d2e2f;
  --border        : #bb5046;
  --text          : #f5f2f2;
  --text-dim      : #bfa6a3;
  --accent        : #ed847a;
  --accent-bright : #f8bcb7;
  --accent-dim    : #dc3e2f;
  --secondary     : #2f4c5e;
  --contrast      : #1ded9b;"""

# HOUSE-STYLE §5: raise the wash only on the lesson that needs it, and
# say that you did. Four of these sixteen illustrations are cream-and-
# coral at full brightness — the pipe corridor, the roof opening, the
# office, the shore — and at the default 0.06 / 0.20 the sorting bins and
# the un-carded hints on those slides measured under 3.5:1. The dark
# slides can afford it: the deck still measures inside the 0.025-0.08
# band for a dark theme with this on.
CSS = """
<style>
:root { --wash-mid: rgba(0,0,0,0.17); --wash-edge: rgba(0,0,0,0.36); }
</style>
"""

# The digit earned in each room, in room order. The lock takes them
# backwards, which is the last thing the deck tests: an instruction in
# English, not a feat of memory — the rail is showing all five.
DIGITS = ['7', '3', '9', '4', '6']
CODE = ''.join(reversed(DIGITS))          # 64937


def T(key):
    return E[key]


def teach(ek, tk, cards, bg=None, cols=None):
    """cards: list of (head_key, body_key, note_key_or_None)."""
    return D.teach(ek, E[ek], tk, E[tk],
                   [(hk, E[hk], bk, E[bk], nk, E[nk] if nk else None)
                    for hk, bk, nk in cards],
                   cols=cols, folder=F, bg=bg)


# ══ ROOM 1 — prepositions of place ═════════════════════════════════════
MC1 = [
    dict(correct=0, ek='eCell', tk='t4',
         stem='The vent is small. It is <em>_______</em> the sink, at the '
              'back of the cell.',
         options=['behind', 'between', 'under', 'above'],
         why='<strong>Behind</strong> means at the back of something. The '
             'vent is at the back of the sink, so it is behind it.'),
    dict(correct=1, ek='eCell', tk='t5',
         stem='Your spoon is <em>_______</em> the bed and the wall, where '
              'nobody looks.',
         options=['behind', 'between', 'under', 'inside'],
         why='<strong>Between</strong> needs two things and the word '
             '<em>and</em>: between the bed <em>and</em> the wall.'),
]

GAP1 = [
    ('There is a photo <em>______</em> the wall, next to your bed.',
     ['on'],
     '<strong>On</strong> for a surface you touch: on the wall, on the '
     'table, on the floor.'),
    ('Your shoes are <em>______</em> the bed, in the dust.',
     ['under'],
     '<strong>Under</strong> means lower than something and covered by it.'),
]
BANK1 = ['under', 'above', 'on', 'behind']

SEARCH1 = dict(
    ek='eFind', tk='t7', bg='eye', take=DIGITS[0],
    stem='The wall behind the vent is soft. You need something to dig '
         'with. Which one?',
    items=[('a cup', 'cup', False), ('a spoon', 'spoon', True),
           ('a book', 'book', False), ('soap', 'soap', False),
           ('a towel', 'towel', False), ('a comb', 'comb', False)],
    why='A <strong>spoon</strong>. In 1962 three men opened the vents in '
        'their cells with spoons and a drill made from a vacuum-cleaner '
        'motor. Scratched inside the vent: the number %s.' % DIGITS[0])

# ══ ROOM 2 — there is / there are ══════════════════════════════════════
MC2 = [
    dict(correct=2, ek='eCorridor', tk='t9',
         stem='It is dark in here. <em>_______</em> three pipes on the left '
              'and one ladder on the right.',
         options=['There has', 'It has', 'There are', 'There is'],
         why='Three pipes is more than one, so <strong>there are</strong>. '
             'The ladder later in the sentence does not change it.'),
]

GAP2 = [
    ('There <em>______</em> any windows in this corridor.',
     ["aren't|are not"],
     'No windows &mdash; plural and negative, so <strong>there '
     'aren&rsquo;t</strong>.'),
    ('There <em>______</em> a small light above the door.',
     ["is|'s"],
     'One light, so <strong>there is</strong>.'),
]
BANK2 = ['is', "aren't", 'are', "isn't"]

SORT2 = dict(
    ek='eCorridor', tk='t11',
    bins=['There is', 'There are'],
    items=[('a ladder', 0), ('three doors', 1), ('some water', 0),
           ('two guards', 1), ('a red light', 0), ('some pipes', 1),
           ('a lot of noise', 0), ('four steps', 1)],
    hint='Click a phrase, then click the box it belongs in.',
    why='Water and noise have no plural form, so they take <strong>there '
        'is</strong> even with <em>some</em> or <em>a lot of</em>.')

SEARCH2 = dict(
    ek='eFind', tk='t12', bg='screen', take=DIGITS[1],
    stem='There is no light in the corridor and you cannot see the steps. '
         'Which one do you need?',
    items=[('a bucket', 'bucket', False), ('a key', 'key', False),
           ('a ladder', 'ladder', False), ('a torch', 'torch', True),
           ('a pipe', 'pipe', False), ('a hammer', 'hammer', False)],
    why='A <strong>torch</strong> &mdash; in American English, a '
        'flashlight. Painted on the handle: the number %s.' % DIGITS[1])

# ══ ROOM 3 — past simple ═══════════════════════════════════════════════
MC3 = [
    dict(correct=1, ek='eShop', tk='t15',
         stem='In 1962 the three men <em>_______</em> the false heads from '
              'paper, paint and real hair.',
         options=['make', 'made', 'making', 'were make'],
         why='<strong>Made</strong> is the past simple of <em>make</em>. It '
             'is irregular, so there is no <em>-ed</em> ending.'),
]

GAP3 = [
    ('The three men <em>______</em> more than fifty raincoats from the shop.',
     ['took'],
     '<strong>Took</strong> &mdash; the past simple of <em>take</em>.'),
    ('After that they <em>______</em> up to the roof.',
     ['went'],
     '<strong>Went</strong> &mdash; the past simple of <em>go</em>.'),
]
BANK3 = ['went', 'got', 'took', 'put']

ORDER3 = dict(
    ek='eShop', tk='t17',
    items=['The guards', 'did not find', 'the three men',
           'on the island', 'that night'],
    hint='Click the parts in order &middot; click one again to take it back',
    why='After <em>did not</em> comes the base form: <strong>did not '
        'find</strong>, never <em>did not found</em>.')

SEARCH3 = dict(
    ek='eFind', tk='t18', bg='watcher', take=DIGITS[2],
    stem='The false head needs real hair, and the hair is on the floor. '
         'Which one can you cut with?',
    items=[('a comb', 'comb', False), ('soap', 'soap', False),
           ('scissors', 'scissors', True), ('a cup', 'cup', False),
           ('a towel', 'towel', False), ('a spoon', 'spoon', False)],
    why='<strong>Scissors</strong>. The word is always plural: '
        '<em>a pair of scissors</em>, never <em>a scissor</em>. On the '
        'handle: the number %s.' % DIGITS[2])

# ══ ROOM 4 — can / can't / must / mustn't ══════════════════════════════
MC4 = [
    dict(correct=3, ek='eWork', tk='t20',
         stem='A guard walks past every thirty minutes. You '
              '<em>_______</em> make any noise.',
         options=['needn&rsquo;t', 'could', 'may', 'mustn&rsquo;t'],
         why='<strong>Mustn&rsquo;t</strong> means it is forbidden. '
             '<em>Needn&rsquo;t</em> means the opposite &mdash; that it is '
             'not necessary.'),
    dict(correct=0, ek='eWork', tk='t21',
         stem='The rule on the wall says: every prisoner <em>_______</em> '
              'be in his cell at nine o&rsquo;clock.',
         options=['must', 'can', 'mustn&rsquo;t', 'would'],
         why='<strong>Must</strong> means it is necessary. It is a rule, '
             'not a choice and not a possibility.'),
]

SORT4 = dict(
    ek='eWork', tk='t22',
    bins=['You must', "You mustn't"],
    items=[('be quiet at night', 0), ('make a noise', 1),
           ('work every day', 0), ('carry a knife', 1),
           ('keep your cell clean', 0), ('open the vent', 1),
           ('wear the prison clothes', 0), ('leave your cell after nine', 1)],
    hint='Click a rule, then click the box it belongs in.',
    why='<strong>Must</strong> = you have to do it. <strong>Mustn&rsquo;t'
        '</strong> = you are not allowed to do it.')

SEARCH4 = dict(
    ek='eFind', tk='t23', bg='screen', take=DIGITS[3],
    stem='Fifty of these, cut open and joined together, make a boat. '
         'Which one?',
    items=[('a hammer', 'hammer', False), ('a boot', 'boot', False),
           ('a ladder', 'ladder', False), ('a coat', 'coat', True),
           ('a saw', 'saw', False), ('a bucket', 'bucket', False)],
    why='A <strong>raincoat</strong>. The 1962 escapers took more than '
        'fifty of them and made a rubber boat. Inside the collar: the '
        'number %s.' % DIGITS[3])

# ══ ROOM 5 — comparatives + going to ═══════════════════════════════════
MC5 = [
    dict(correct=2, ek='eWater', tk='t26',
         stem='The water on the north side is <em>_______</em> the water in '
              'the bay, and the currents are stronger.',
         options=['more cold than', 'as colder than', 'colder than',
                  'colder that'],
         why='<em>Cold</em> is a short adjective, so add <strong>-er</strong> '
             'and then <strong>than</strong>. Never <em>more</em> with a '
             'short adjective.'),
    dict(correct=1, ek='eWater', tk='t28',
         stem='You are in the boat. Which sentence is a <em>plan</em>?',
         options=['We usually leave at ten.',
                  'We&rsquo;re going to leave at ten.',
                  'We left at ten last night.',
                  'We can leave at ten.'],
         why='<strong>Going to</strong> shows a plan you have already made. '
             'The others show a habit, the past, and a possibility.'),
]

GAP5 = [
    ('I <em>______</em> going to take the paddle and sit at the front.',
     ["am|'m"],
     'With <em>I</em>, the verb <em>be</em> is <strong>am</strong>.'),
    ('They <em>______</em> going to wait for us on the shore.',
     ["are|'re"],
     'With <em>they</em>, the verb <em>be</em> is <strong>are</strong>.'),
]
BANK5 = ['are', 'am', 'going', 'is']

SEARCH5 = dict(
    ek='eFind', tk='t29', bg='boat', take=DIGITS[4],
    stem='The boat is in the water and the current is against you. Which '
         'one can you row with?',
    items=[('a rope', 'rope', False), ('a candle', 'candle', False),
           ('a paddle', 'paddle', True), ('a boot', 'boot', False),
           ('a pipe', 'pipe', False), ('a key', 'key', False)],
    why='A <strong>paddle</strong>. The men in 1962 made theirs out of '
        'wood. Burnt into the handle: the number %s.' % DIGITS[4])

# ══ THE FINAL CHECK — a real test, no scaffolding ══════════════════════
# The five rooms teach and practise one point at a time, with the rule on
# the screen two slides earlier. This section mixes all five, gives no
# hint, and is where the learner finds out what actually stuck.
TEST_MC = [
    dict(correct=2, tk='x1',
         stem='The torch is <em>_______</em> the two pipes, where the guard '
              'cannot see it.',
         options=['under', 'behind', 'between', 'above'],
         why='Two pipes, one thing in the middle: <strong>between</strong>.'),
    dict(correct=3, tk='x2',
         stem='<em>_______</em> any guards on the roof tonight?',
         options=['Is there', 'There are', 'Have there', 'Are there'],
         why='A question with a plural noun: <strong>Are there</strong>. '
             'The verb comes first in a question.'),
    dict(correct=1, tk='x3',
         stem='They <em>_______</em> the raincoats in the workshop, not in '
              'the shop.',
         options=['didn&rsquo;t found', 'didn&rsquo;t find',
                  'not found', 'didn&rsquo;t founded'],
         why='After <em>didn&rsquo;t</em> comes the base form: '
             '<strong>didn&rsquo;t find</strong>.'),
    dict(correct=0, tk='x4',
         stem='The gate is locked at nine. After nine you <em>_______</em> '
              'walk in this corridor.',
         options=['can&rsquo;t', 'must', 'should', 'could'],
         why='The gate is locked, so it is not possible: '
             '<strong>can&rsquo;t</strong>.'),
    dict(correct=2, tk='x5',
         stem='The east shore is <em>_______</em> the north shore, so we '
              'are going that way.',
         options=['more safe than', 'safer that', 'safer than', 'safe than'],
         why='<em>Safe</em> is short, so <strong>safer</strong>, and the '
             'comparison word is <strong>than</strong>.'),
    dict(correct=3, tk='x6',
         stem='Look at the sky. It <em>_______</em> rain before we reach '
              'the shore.',
         options=['is go to', 'goes to', 'going to', 'is going to'],
         why='<strong>Is going to</strong> &mdash; the verb <em>be</em> is '
             'part of the structure and cannot be dropped.'),
]

TEST_GAP = [
    # `were` is accepted, and it is not a concession: the sentence carries
    # no time marker and the row under it is past simple, so a learner who
    # reads the two together and writes `were` has read them correctly.
    # What the item tests is the agreement, not the tense.
    [('There <em>______</em> two boats at the pier and one man on the wall.',
      ['are|were'],
      'Two boats is plural, so <strong>there are</strong> &mdash; or '
      '<strong>there were</strong>, if you are telling it as the past. '
      'Never <em>there is</em> with a plural.'),
     ('The guard <em>______</em> the door at ten and went back upstairs.',
      ['locked'],
      '<em>Lock</em> is regular, so the past simple is '
      '<strong>locked</strong>.')],
    # `can't` is accepted. For prohibition the two overlap in real use,
    # and marking a learner wrong for the commoner of the two teaches
    # them to distrust the exercise rather than to hear the difference.
    [('You <em>______</em> use a light on the roof &mdash; they will see you.',
      ["mustn't|must not|can't|cannot|can not"],
      'Both work. <strong>Mustn&rsquo;t</strong> is the rule &mdash; it is '
      'forbidden. <strong>Can&rsquo;t</strong> is the situation &mdash; it '
      'is not possible, or you are not allowed. For prohibition, English '
      'uses either.'),
     ('We <em>______</em> going to wait for the fog before we row.',
      ["are|'re"],
      'With <em>we</em>, the verb <em>be</em> is <strong>are</strong>.')],
]

TEST_ORDER = dict(
    tk='x9',
    items=['We', 'are going to', 'put the false heads', 'in the beds',
           'before ten'],
    hint='Click the parts in order &middot; click one again to take it back',
    why='<em>Be going to</em> comes straight after the subject, then the '
        'base verb, then the rest of the sentence.')


# ══ BUILD ══════════════════════════════════════════════════════════════
def mc(q, n, total, bg=None, stop=None, take=None):
    s = D.mc(n, total, q, q['ek'], E[q['ek']], q['tk'], E[q['tk']],
             folder=F, bg=bg)
    return D.at(s, stop, take) if stop else s


def build():
    D.assert_no_key_is_longest(MC1 + MC2 + MC3 + MC4 + MC5, 'rooms')
    D.assert_no_key_is_longest(TEST_MC, 'final check')
    for bank, gaps in ((BANK1, GAP1), (BANK2, GAP2), (BANK3, GAP3),
                       (BANK5, GAP5)):
        D.assert_bank_is_not_a_key(bank, [g[1][0] for g in gaps])

    logo = D.logo_from(TPL)
    S = []
    a = S.append

    # ── cover + orientation ──
    a(D.cover(logo, E['coverTitle'], E['coverSub'],
              [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
               ('Time', E['chipTime']), ('Count', E['chipCount'])]))
    a(teach('eIsland', 't1',
            [('h1a', 'b1a', None), ('h1b', 'b1b', 'n1')], bg='sunset.jpg'))
    a(teach('eIsland', 't2',
            [('h2a', 'b2a', None), ('h2b', 'b2b', 'n2')], bg='watcher.jpg'))

    # ── room 1 ──
    a(D.at(teach('eCell', 't3',
                 [('h3a', 'b3a', None), ('h3b', 'b3b', 'n3')],
                 bg='cell.jpg'), 1))
    a(mc(MC1[0], 1, 2, bg='cell.jpg', stop=1))
    a(mc(MC1[1], 2, 2, bg='cell.jpg', stop=1))
    a(D.at(D.gap(1, 1, GAP1, BANK1, 'eCell', E['eCell'], 't6', E['t6'],
                 folder=F, bg='cell-hole.jpg'), 1))
    a(search(SEARCH1, 1))

    # ── room 2 ──
    a(D.at(teach('eCorridor', 't8',
                 [('h8a', 'b8a', None), ('h8b', 'b8b', 'n8')],
                 bg='corridor.jpg'), 2))
    a(mc(MC2[0], 1, 1, bg='corridor.jpg', stop=2))
    a(D.at(D.gap(1, 1, GAP2, BANK2, 'eCorridor', E['eCorridor'], 't10',
                 E['t10'], folder=F, bg='corridor.jpg'), 2))
    a(D.at(D.sort_slide(SORT2['bins'], SORT2['items'], 'eCorridor',
                        E['eCorridor'], 't11', E['t11'], 'sortHint',
                        SORT2['hint'], SORT2['why'], folder=F,
                        bg='corridor.jpg'), 2))
    a(search(SEARCH2, 2))

    # ── room 3 ──
    a(D.at(teach('eShop', 't13',
                 [('h13a', 'b13a', None), ('h13b', 'b13b', 'n13')],
                 bg='shop.jpg'), 3))
    a(D.at(teach('eShop', 't14',
                 [('h14a', 'b14a', None), ('h14b', 'b14b', 'n14')],
                 bg='shop.jpg'), 3))
    a(mc(MC3[0], 1, 1, bg='shop.jpg', stop=3))
    a(D.at(D.gap(1, 1, GAP3, BANK3, 'eShop', E['eShop'], 't16', E['t16'],
                 folder=F, bg='shop.jpg'), 3))
    a(D.at(D.order(ORDER3['items'], 'eShop', E['eShop'], 't17', E['t17'],
                   'orderHint', ORDER3['hint'], ORDER3['why'], folder=F,
                   bg='shop.jpg'), 3))
    a(search(SEARCH3, 3))

    # ── room 4 ──
    a(D.at(teach('eWork', 't19',
                 [('h19a', 'b19a', None), ('h19b', 'b19b', 'n19')],
                 bg='workshop.jpg'), 4))
    a(mc(MC4[0], 1, 2, bg='workshop.jpg', stop=4))
    a(mc(MC4[1], 2, 2, bg='workshop.jpg', stop=4))
    a(D.at(D.sort_slide(SORT4['bins'], SORT4['items'], 'eWork', E['eWork'],
                        't22', E['t22'], 'sortHint', SORT4['hint'],
                        SORT4['why'], folder=F, bg='workshop.jpg'), 4))
    a(search(SEARCH4, 4))

    # ── room 5 ──
    a(D.at(teach('eWater', 't24',
                 [('h24a', 'b24a', None), ('h24b', 'b24b', 'n24')],
                 bg='roof.jpg'), 5))
    a(D.at(teach('eWater', 't25',
                 [('h25a', 'b25a', None), ('h25b', 'b25b', 'n25')],
                 bg='water.jpg'), 5))
    a(mc(MC5[0], 1, 2, bg='patrolboat.jpg', stop=5))
    a(D.at(D.gap(1, 1, GAP5, BANK5, 'eWater', E['eWater'], 't27', E['t27'],
                 folder=F, bg='water.jpg'), 5))
    a(mc(MC5[1], 2, 2, bg='pier.jpg', stop=5))
    a(search(SEARCH5, 5))

    # ── the final check ──
    a(teach('eCheck', 'tCheck',
            [('hC1', 'bC1', None), ('hC2', 'bC2', 'nC')], bg='check.jpg'))
    n = 0
    total = len(TEST_MC) + len(TEST_GAP) + 1
    CHECK_BG = ['cellsearch.jpg', 'cellsearch.jpg', 'office.jpg',
                'office.jpg', 'patrol.jpg', 'patrol.jpg', 'guard.jpg',
                'guard.jpg', 'gateguards.jpg']
    for q in TEST_MC[:3]:
        q = dict(q, ek='eCheck')
        a(D.mc(n + 1, total, q, 'eCheck', E['eCheck'], q['tk'], E[q['tk']],
               folder=F, bg=CHECK_BG[n]))
        n += 1
    a(D.gap(n + 1, total, TEST_GAP[0], None, 'eCheck', E['eCheck'], 'x7',
            E['x7'], folder=F, bg=CHECK_BG[n]))
    n += 1
    for q in TEST_MC[3:]:
        q = dict(q, ek='eCheck')
        a(D.mc(n + 1, total, q, 'eCheck', E['eCheck'], q['tk'], E[q['tk']],
               folder=F, bg=CHECK_BG[n]))
        n += 1
    a(D.gap(n + 1, total, TEST_GAP[1], None, 'eCheck', E['eCheck'], 'x8',
            E['x8'], folder=F, bg=CHECK_BG[n]))
    n += 1
    a(D.order(TEST_ORDER['items'], 'eCheck', E['eCheck'], 'x9', E['x9'],
              'orderHint', TEST_ORDER['hint'], TEST_ORDER['why'],
              folder=F, bg=CHECK_BG[n]))

    # ── the lock, results, activation ──
    a(D.lock(CODE, E['lockStem'], 'eLock', E['eLock'], 't30', E['t30'],
             E['lockWhy'], folder=F, bg='gate.jpg'))
    a(D.results(folder=F, bg='raft.jpg'))
    a(D.activate(E['actTitle'], E['actUse'],
                 ['There is / There are', 'under &middot; behind &middot; '
                  'between', 'must / mustn&rsquo;t', 'I&rsquo;m going to&hellip;',
                  'colder than'],
                 'Discussion &middot; in pairs', E['actSpeakBrief'],
                 [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                 E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder']))
    return S


def search(spec, stop):
    """The rooms are numbered 1-5 and so are their searches, so the stop
    number doubles as the item number in the eyebrow."""
    return D.search(stop, 5, spec['stem'],
                    [(name, icons.icon(ico), key)
                     for name, ico, key in spec['items']],
                    spec['ek'], E[spec['ek']], spec['tk'], E[spec['tk']],
                    spec['why'], limit=22, folder=F, bg=spec['bg'] + '.jpg',
                    stop=stop, take=spec['take'])


if __name__ == '__main__':
    slides = build()
    body = ''.join(slides)
    n = body.count('<section class="slide')
    body = body.replace('NN slides', '%d slides' % n)
    for code in I.T:
        I.T[code]['chipCount'] = I.T[code]['chipCount'].replace('NN', str(n))

    s = D.assemble(TPL, OUT, body, PALETTE, 'Escape from Alcatraz — A2', I,
                   langs=tuple(I.T))
    s = s.replace('</head>', CSS + '</head>', 1)
    assert 'data:image' not in s, 'a base64 blob survived into the build'
    open(OUT, 'w', encoding='utf-8').write(s)

    pts = (len(MC1 + MC2 + MC3 + MC4 + MC5) + len(TEST_MC)
           + len(GAP1 + GAP2 + GAP3 + GAP5)
           + sum(len(g) for g in TEST_GAP)
           + len(SORT2['items']) + len(SORT4['items'])
           + 2                       # the two order slides
           + 5                       # the five searches
           + 1)                      # the lock
    print('wrote %s — %d bytes, %d slides' % (OUT, len(s), n))
    print('scored points: %d   lock code: %s' % (pts, CODE))
    print('languages: %s' % ', '.join(sorted(I.T)))
