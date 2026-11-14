# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: The Backshift Current, reported speech as a
current. The eighteenth chart.

    py lesson-template/build/build_backshift.py
    py tools/build_hubs.py && py tools/seo.py

THE TEACHING IDEA. Direct Harbour holds the words as they were said. Report
them later and the current carries each one to Reported Harbour, one tense
further back: present to past, past and present perfect to past perfect,
WILL to WOULD, CAN to COULD. The Drifting Buoys are the time and place words
that move with it (today, tomorrow, here); the Still Rocks are the forms
that cannot go further back (had done, would, could, should, might).

TENSE COLOURS. Innes, 2026-11-13: anything involving a tense uses its Sherpa
colour. Each harbour's disc on the chart is its tense, and the page's panel
rows carry the same colour, read from sea_tense.T. WOULD and COULD are not
tenses and have none.

THE ART. Layout by sea_layouts_5.py, painted by Codex on 2026-11-14.
sea_measure.py found all 14 dots (backshift_chart.json).
"""
import sys
sys.path.insert(0, 'lesson-template/build')
import sea_lesson as L
import sea_overlay as O
from sea_lesson import ex, exi, chart, fork, signals, rule_grid, MARK_FLAG, MARK_TABLE
from sea_tense import T as TENSE

OUT = 'sailing-the-seas-backshift.html'
ART = 'sailing-the-seas-backshift'
UID = 'back'

# py lesson-template/extract-palette.py sailing-the-seas-backshift/hero.jpg --light
EXTRACTED = {'text': '#2a2311', 'text-dim': '#5e522e', 'secondary': '#add0e0', 'contrast': '#0a526c'}

D = O.load('backshift_chart.json')
WEST = sorted((tuple(p) for p in D['dots'] if p[0] < 768), key=lambda p: p[1])
EAST = sorted((tuple(p) for p in D['dots'] if p[0] > 768), key=lambda p: p[1])
assert (len(WEST), len(EAST)) == (7, 7), D['dots']

# (key, direct, reported, tense of the direct words, tense of the report, the names of the two)
SHIFTS = [('am', '&#8220;I am tired.&#8221;', 'she was tired', 'present-simple', 'past-simple',
           'present simple', 'past simple'),
          ('work', '&#8220;I work here.&#8221;', 'he worked there', 'present-simple', 'past-simple',
           'present simple', 'past simple'),
          ('leaving', '&#8220;I&#8217;m leaving.&#8221;', 'she was leaving', 'present-continuous', 'past-continuous',
           'present continuous', 'past continuous'),
          ('finished', '&#8220;I&#8217;ve finished.&#8221;', 'he had finished', 'present-perfect', 'past-perfect',
           'present perfect', 'past perfect'),
          ('saw', '&#8220;I saw it.&#8221;', 'she had seen it', 'past-simple', 'past-perfect',
           'past simple', 'past perfect'),
          ('will', '&#8220;I&#8217;ll help.&#8221;', 'he would help', 'future-simple', None, 'will', 'would'),
          ('can', '&#8220;I can swim.&#8221;', 'she could swim', None, None, 'can', 'could')]
INK, WEST_LAND, EAST_LAND = '#20180A', '#B9B572', '#EBBF80'


def disc(tense):
    """The tense's Sherpa colour as a disc in a panel row. No double quotes:
    sea_lesson puts panel lines in a JS string, so the attribute is unquoted."""
    if not tense:
        return ''
    return '<i style=color:#%02X%02X%02X;font-style:normal;margin-right:.35em>&#9679;</i>' % TENSE[tense]


def overlay():
    spots, names = [], []
    for (key, direct, rep, _, _, n1, n2), (wx, wy), (ex_, ey) in zip(SHIFTS, WEST, EAST):
        names.append(O.name(wx, wy, (direct, n1, 'She said: ' + direct), INK, WEST_LAND, size=18, dy=-19, fit=False,
                            halo=.25))
        names.append(O.name(ex_, ey, (rep, n2, 'said (that) ' + rep), INK, EAST_LAND, size=18, dy=-19, fit=False,
                            halo=.25))
        spots.append(O.hotspot(UID, 'd-' + key, O.circle_path(wx, wy, 32), 'Direct: %s' % n1))
        spots.append(O.hotspot(UID, 'r-' + key, O.circle_path(ex_, ey, 32), 'Reported: %s' % n2))
    spots.append(O.hotspot(UID, 'buoys', O.rect_path(380, 845, 1160, 880), 'The drifting buoys: time and place words'))
    spots.append(O.hotspot(UID, 'rocks', O.rect_path(500, 882, 1040, 985), 'The still rocks: forms that never move'))
    sea_ink = '#0F2F3D'
    caps = [O.cap(768, 60, 'THE BACKSHIFT CURRENT', sea_ink, 39, face=O.SERIF, spacing='.05em'),
            O.cap(768, 96, 'report it later and the tense drifts one step back', sea_ink, 19, face=O.SERIF, weight=600,
                  spacing='0', style='italic'),
            O.cap(268, 176, 'DIRECT HARBOUR', INK, 25, face=O.SERIF, spacing='.02em', halo=WEST_LAND),
            O.cap(268, 202, 'the words as they were said', INK, 15, weight=600, spacing='0', style='italic',
                  halo=WEST_LAND),
            O.cap(1268, 176, 'REPORTED HARBOUR', INK, 25, face=O.SERIF, spacing='.02em', halo=EAST_LAND),
            O.cap(1268, 202, 'she said (that) &#8230;', INK, 15, weight=600, spacing='0', style='italic', halo=EAST_LAND),
            O.cap(768, 238, 'THE BACKSHIFT CURRENT', sea_ink, 18, face=O.SERIF, spacing='.05em'),
            O.cap(768, 868, 'DRIFTING BUOYS: today becomes that day &#183; tomorrow, the next day &#183; here, there',
                  sea_ink, 14, weight=600, spacing='0', style='italic'),
            O.cap(768, 972, 'THE STILL ROCKS: had done &#183; would &#183; could &#183; should &#183; might never move',
                  sea_ink, 14, weight=700, spacing='0')]
    return O.svg(1536, 1024, spots, caps, names)


HERO_ALT = ('An illustrated chart with two shores and seven dashed currents running west to east. On the green west '
            'shore, Direct Harbour, the words as they were said: I am tired, I work here, I&#39;m leaving, I&#39;ve '
            'finished, I saw it, I&#39;ll help, I can swim. On the sandy east shore, Reported Harbour: she was tired, '
            'he worked there, she was leaving, he had finished, she had seen it, he would help, she could swim. Each '
            'harbour has a disc in the colour of its tense. At the foot, drifting buoys and five still rocks.')

HERO = L.hero_block(
    ART, 'Sailing the Seas of Grammar &middot; Reported speech', 'The Backshift Current',
    'Ana says: <em>&#8220;I am tired.&#8221;</em> An hour later you tell a friend: <em>she said she was tired</em>. '
    'Between saying and reporting, a current runs, and it carries every tense one step back into the past. '
    'Read each line across, from the words as they were said to the words as you report them.',
    HERO_ALT)

RULES = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Reading the current</div>
      <h2>One step back, every time</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The reporting verb is in the past (<em>said</em>, <em>told me</em>), so what was said moves back with it. Each tense has exactly one place to go.</p>
      ''' + rule_grid([
    ('Present simple drifts to past simple',
     '<em>am / is</em> to <em>was</em>, <em>work</em> to <em>worked</em>.',
     ex('&#8220;I work here.&#8221; He said he <em>worked</em> there.')),
    ('Present continuous drifts to past continuous',
     '<em>am leaving</em> to <em>was leaving</em>.',
     ex('&#8220;I&#39;m leaving.&#8221; She said she <em>was leaving</em>.')),
    ('Present perfect drifts to past perfect',
     '<em>have finished</em> to <em>had finished</em>.',
     ex('&#8220;I&#39;ve finished.&#8221; He said he <em>had finished</em>.')),
    ('Past simple drifts to past perfect too',
     '<em>saw</em> to <em>had seen</em>. Two harbours feed one.',
     ex('&#8220;I saw it.&#8221; She said she <em>had seen</em> it.')),
    ('Will drifts to would, can to could',
     'The modals have a past form of their own.',
     ex('&#8220;I&#39;ll help.&#8221; He said he <em>would help</em>.')),
    ('Say or tell',
     '<em>Say</em> takes no person; <em>tell</em> must have one.',
     ex('She <em>said</em> she was tired. She <em>told me</em> she was tired.')),
]) + chart(
    'The seven currents',
    'Read each row west to east.',
    ['Direct', 'Its tense', 'Reported', 'Its tense'],
    [[d, n1, ('She said ' if r.startswith('she') else 'He said ') + r + '.', n2]
     for _, d, r, _, _, n1, n2 in SHIFTS]) + '''
    </div>

    '''

EXTRAS = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The drifting buoys and the still rocks</div>
      <h2>What moves with the tense, and what cannot move</h2>
      <p class="chart-note" style="margin:-6px 0 18px">A report is made later and somewhere else, so the words for time and place drift too. And some forms are already as far back as English goes.</p>
      ''' + chart(
    'The drifting buoys',
    'These change when the time or the place of the report is different.',
    ['Said', 'Reported', 'Also'],
    [['today', 'that day', 'tonight / that night'], ['tomorrow', 'the next day', 'next week / the following week'],
     ['yesterday', 'the day before', 'last week / the week before'], ['here', 'there', 'this / that'],
     ['now', 'then', 'ago / before'], ['I, my', 'he / she, his / her', 'we / they']]) + '''
      ''' + exi('&#8220;I&#39;ll call you tomorrow.&#8221; She said she <em>would call</em> me <em>the next day</em>.') + chart(
    'The still rocks',
    'These have nowhere further back to go, so they stay as they are.',
    ['Said', 'Reported', 'Why'],
    [['&#8220;I had already eaten.&#8221;', 'He said he had already eaten.', 'the past perfect is the last harbour'],
     ['&#8220;I would like tea.&#8221;', 'She said she would like tea.', '<em>would</em> stays'],
     ['&#8220;I could swim at five.&#8221;', 'He said he could swim at five.', '<em>could</em> stays'],
     ['&#8220;You should rest.&#8221;', 'She said I should rest.', '<em>should</em> stays'],
     ['&#8220;It might rain.&#8221;', 'He said it might rain.', '<em>might</em> stays']]) + '''
      ''' + exi('&#8220;You should rest.&#8221; The doctor said I <em>should rest</em>.') + '''
    </div>

    '''

DIAGRAM = L.diagram(
    ART, UID, overlay(),
    'Click a harbour and its line lights up below: the words as they were said on the left, the report in the '
    'middle. The disc beside each line is its tense colour. Switch the chart to see the tense at each end.',
    ('The words', 'The tense', 'With said'),
    [('Direct Harbour', 'is-west'), ('Reported Harbour', 'is-isle'), ('The buoys and the rocks', 'is-east')],
    'Drag the chart sideways to reach Reported Harbour.', min_zoom=1000)

TRAPS = fork(
    'Against the current',
    'Each of these stays in Direct Harbour when it should have drifted.',
    ['Not this', 'This', 'Why'],
    [['She said she is tired. (reporting it later)', 'She said she was tired.', 'present to past'],
     ['He said he has finished.', 'He said he had finished.', 'present perfect to past perfect'],
     ['She said she will help.', 'She said she would help.', 'will to would'],
     ['He said me he was tired.', 'He told me he was tired. / He said he was tired.', 'say has no person'],
     ['She told she was leaving.', 'She told me she was leaving. / She said she was leaving.', 'tell needs a person'],
     ['He said he would come tomorrow. (reported a week later)', 'He said he would come the next day.', 'a drifting buoy']],
    'If what was said is still true as you speak, English often lets the tense stay: <em>She said she lives in Rome.</em> The current is the safe choice in an exam.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-passive.html', 'The Passive Ferry')])

SIGNALS = signals(
    'You are in Direct Harbour',
    ['quotation marks', 'the speaker&#39;s own <em>I</em> and <em>my</em>', '<em>today</em>, <em>tomorrow</em>, <em>here</em>',
     'the original tense', '<em>&#8220;I&#39;ll help,&#8221; he said.</em>', 'a comma before the quotation'],
    'You are in Reported Harbour',
    ['<em>said (that)</em>, <em>told me (that)</em>', '<em>he</em>, <em>she</em>, <em>his</em>, <em>her</em>',
     '<em>that day</em>, <em>the next day</em>, <em>there</em>', 'one tense further back', '<em>He said he would help.</em>',
     'no quotation marks'],
    'One test: are there quotation marks? If not, check the tense, the pronoun and the time word, in that order.')

QUIZ = [
    ('&#8220;I am tired.&#8221; She said she ___ tired.', 'Present simple, one step back.', 'was',
     ['was', 'is', 'has been', 'will be'], 'Present simple drifts to past simple: was.'),
    ('&#8220;I work here.&#8221; He said he ___ there.', 'Present simple, one step back.', 'worked',
     ['worked', 'works', 'is working', 'has worked'], 'Work drifts to worked, and here to there.'),
    ('&#8220;I&#39;m leaving.&#8221; She said she ___.', 'Present continuous, one step back.', 'was leaving',
     ['was leaving', 'is leaving', 'left', 'has left'], 'Present continuous drifts to past continuous.'),
    ('&#8220;I&#39;ve finished.&#8221; He said he ___.', 'Present perfect, one step back.', 'had finished',
     ['had finished', 'has finished', 'finished it now', 'was finish'], 'Present perfect drifts to past perfect.'),
    ('&#8220;I saw it.&#8221; She said she ___ it.', 'Past simple, one step back.', 'had seen',
     ['had seen', 'has seen', 'sees', 'was seen'], 'Past simple drifts to past perfect: had seen.'),
    ('&#8220;I&#39;ll help.&#8221; He said he ___ help.', 'Will, one step back.', 'would',
     ['would', 'will', 'can', 'did'], 'Will drifts to would.'),
    ('&#8220;I can swim.&#8221; She said she ___ swim.', 'Can, one step back.', 'could',
     ['could', 'can', 'would', 'was'], 'Can drifts to could.'),
    ('He ___ me he was tired.', 'A person follows.', 'told',
     ['told', 'said', 'spoke', 'talked'], 'Tell takes a person: he told me.'),
    ('&#8220;I&#39;ll call tomorrow.&#8221; She said she would call ___.', 'A drifting buoy.', 'the next day',
     ['the next day', 'tomorrow day', 'the day before', 'yesterday'], 'Tomorrow drifts to the next day.'),
    ('&#8220;You should rest.&#8221; She said I ___ rest.', 'A still rock.', 'should',
     ['should', 'should have', 'would should', 'had should'], 'Should does not move.'),
    ('Which report is right? &#8220;I had already eaten.&#8221;', 'A still rock.', 'He said he had already eaten.',
     ['He said he had already eaten.', 'He said he had had already eaten.', 'He said he has already eaten.',
      'He said he already eats.'], 'The past perfect cannot go further back.'),
    ('Which sentence is right?', 'Say or tell.', 'She said she was leaving.',
     ['She said she was leaving.', 'She said me she was leaving.', 'She told she was leaving.',
      'She told to me she was leaving.'], 'Say without a person; tell with one.'),
]

PANELS = [
    [('d-' + key, '%s<b>%s</b> %s' % (disc(t1), n1, d)) for key, d, _, t1, _, n1, _ in SHIFTS],
    [('r-' + key, '%s<b>%s</b> %s' % (disc(t2), n2, r)) for key, _, r, _, t2, _, n2 in SHIFTS],
    [('buoys', '<b>The drifting buoys</b> <em>today</em> becomes <em>that day</em>'),
     ('buoys', '<em>tomorrow</em>, <em>the next day</em> &middot; <em>here</em>, <em>there</em>'),
     ('rocks', '<b>The still rocks</b> <em>had done</em>, <em>would</em>, <em>could</em>, <em>should</em>, <em>might</em> never move')],
]
TARGETS = {}
for key, _, _, _, _, _, _ in SHIFTS:
    TARGETS['d-' + key] = (0, 'd-' + key, '#0a526c')
    TARGETS['r-' + key] = (1, 'r-' + key, '#0a526c')
TARGETS['buoys'] = (2, 'buoys', '#0a526c')
TARGETS['rocks'] = (2, 'rocks', '#B4441F')

import ex_tr_backshift as T
L.build(OUT, ART, 'The Backshift Current &mdash; Reported Speech', 'Reported speech', EXTRACTED,
        HERO, 'to the words as you report them.', ('order', 'Read the chart'),
        RULES + EXTRAS + DIAGRAM + TRAPS + SIGNALS, QUIZ, UID, PANELS, TARGETS,
        [WEST_LAND, EAST_LAND, '#B4D6E1'], T.T,
        ['Clean run. Every tense drifted exactly one step back.',
         'Solid progress. Check the two that land on the past perfect: I’ve finished and I saw it.',
         'Good first attempt. Start with the first current: am becomes was.'],
        ('sailing-the-seas-bridges.html', 'Next chart: the Bridges'), gull_seed=73, long_name=24)
