# -*- coding: utf-8 -*-
"""Sailing the Seas of Grammar: Regularia & Irregularia, regular and
irregular past forms as a sea chart. The second chart in the series.

    py lesson-template/build/build_regularia.py
    py tools/build_hubs.py && py tools/seo.py

Built on the same machinery as build_sailing.py, which is the model (the
Sherpa camp shell: rule cards, the clickable chart, the fourteen-question
crossing, the nine-language example reveal). Read that file's docstring for
why the shell is borrowed and the mountain's progression stripped.

THE TEACHING IDEA. Almost every verb in English is regular, so Regularia is
the biggest land on the chart, and its three provinces are the three sounds
of -ed (/t/, /d/, /ɪd/), not three rules. The irregular verbs are not chaos:
they come in families that share a sound, and each family is an island named
after that sound (I·A·U, Ought, -EW, -T, -EN). Forked Isle holds the verbs
whose two meanings kept two pasts; the Shallows holds the verbs with two
correct pasts (learnt / learned). The currents say which way English is
moving: every new verb arrives regular.

*Didn't went* is a rule about sentences, not a place, so it is a section of
the page, not a feature of the map (docs/ARTWORK-sea-charts.md).

THE ART. hero.jpg is the labelled repaint and chart-clean.jpg the same
chart with every word removed, both made by Codex on 2026-10-04 from
sea_charts.py's coded layout. The clean one is labelled live by
regularia_map.py, from coordinates measured by regularia_measure.py.

PALETTE. Derived from hero.jpg by extract-palette.py --light (every row
PASS; block below). The page accent is that block's `contrast`, the sea
teal, so the series reads as one; the tints are mixed from it in code and
measured on every build.
"""
import re, sys, glob, json
sys.path.insert(0, 'lesson-template')
sys.path.insert(0, 'lesson-template/build')
sys.path.insert(0, 'lesson-template/build/sherpa/legacy')
import regularia_map as M

_SNAP = {f: open(f, 'rb').read() for f in glob.glob('sherpa-tensing-camp-*.html')}
from build_c10 import assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE, MARK_FORK, MARK_CLOCK, MARK_PANES
from build_c11_12_13 import chart, fork, signals, questions, palette
for _f, _b in _SNAP.items():
    if open(_f, 'rb').read() != _b:
        open(_f, 'wb').write(_b)
        print('restored', _f)

OUT = 'sailing-the-seas-regularia.html'
ART = 'sailing-the-seas-regularia'

# ── palette ───────────────────────────────────────────────────────────
# py lesson-template/extract-palette.py sailing-the-seas-regularia/hero.jpg --light
EXTRACTED = {
    'void': '#bacac2', 'surface': '#ced7d3', 'surface2': '#c4d0ca', 'border': '#96794a',
    'text': '#2a2011', 'text-dim': '#5e4b2e', 'accent': '#7e520d', 'accent-bright': '#604212',
    'accent-dim': '#d69630', 'secondary': '#a7cad3', 'contrast': '#0e5b67',
}
ACCENT = EXTRACTED['contrast']
PAPER = M.mix(EXTRACTED['secondary'], '#FFFFFF', .82)
DARK = M.mix(ACCENT, '#000000', .3)
LIGHT = M.mix(ACCENT, '#FFFFFF', .7)
LIGHTER = M.mix(ACCENT, '#FFFFFF', .9)
for fg, bg, need, what in [(EXTRACTED['text'], PAPER, 7, 'ink on paper'),
                           (EXTRACTED['text-dim'], PAPER, 4.5, 'soft ink on paper'),
                           (ACCENT, PAPER, 4.5, 'accent on paper'),
                           ('#FFFFFF', ACCENT, 4.5, 'white on accent'),
                           (DARK, LIGHTER, 4.5, 'dark on lighter')]:
    r = M.ratio(fg, bg)
    assert r >= need, 'palette: %s is %.2f:1, needs %s' % (what, r, need)
PALETTE = palette(EXTRACTED['text'], EXTRACTED['text-dim'], PAPER, ACCENT, DARK, LIGHT, LIGHTER)


def panel_css(cls, paint):
    bg = M.mix(paint, '#FFFFFF', .84)
    return ('  .diagram-panel.%s{background:%s;border-color:%s;}\n'
            '  .diagram-panel.%s h4{color:%s;}\n'
            % (cls, bg, M.mix(paint, '#FFFFFF', .45), cls, M.ink_for(bg, 7)))


# ── the examples that carry a translation, in page order ──────────────
EX = []


def ex(html):
    EX.append(html)
    return '\x01%d\x01%s' % (len(EX) - 1, html)


def exi(html):
    EX.append(html)
    return ('<p class="ex" data-tr="%d" style="margin:14px 0 0">%s</p>' % (len(EX) - 1, html))


HERO_MAP_ALT = (
    'An illustrated sea chart. On the west, a large green continent, Regularia, divided into three '
    'provinces by the sound the -ed ending makes: -ed says /t/ (Stop Harbour, Walk Ridge, Laugh Rock), '
    '-ed says /d/ (Play Bay, Study Sands, Open Sound) and -ed says /id/ (Start Point, Wait Moor, Land\'s End). '
    'To the east, an archipelago called Irregularia: I A U Island (ring, rang, rung), Ought Island (buy, bought), '
    '-EW Island (blow, blew, blown), -T Island (keep, kept) and -EN Island (speak, spoke, spoken). In the strait '
    'lies Forked Isle (one verb, two meanings, two pasts) and, to the south, a sandbank called the Shallows, '
    'where learnt and learned are both correct. Two currents flow west: new verbs sail west, and some old ones '
    'are drifting west. In the south-east are the Still Rocks (cut, put, hit) and the Lone Stacks (go, be, do, see).')

HERO = hero(
    'Sailing the Seas of Grammar &middot; past forms',
    'Regularia &amp; Irregularia',
    'One big tidy continent, and almost every verb in English lives on it: add <em>-ed</em> and you are done. '
    'Across the strait lies an archipelago of the verbs that are not regular. They do not break the rule at random. '
    'They come in families, and each family has its own island, named after the sound its verbs share. Learn the '
    'continent&#39;s three sounds, then sail the islands one at a time.',
    '<button type="button" class="hero-diagram-btn" id="hero-map-btn" aria-label="Expand the map">'
    '<img class="hero-diagram" src="%s/hero.jpg" alt="%s" loading="eager">'
    '</button>'
    '<div class="img-lightbox" id="hero-lightbox">'
    '<button type="button" class="lightbox-close" aria-label="Close">&times;</button>'
    '<img src="%s/hero.jpg" alt="%s">'
    '</div>' % (ART, HERO_MAP_ALT, ART, HERO_MAP_ALT))

# ═════════════════════════════════════════════════════════════════════
WEST = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">The continent</div>
      <h2>Regularia: add <em>-ed</em></h2>
      <p class="chart-note" style="margin:-6px 0 18px">Regularia is the biggest land on the chart because almost every verb lives there, including every verb invented this century. The rule is one rule. The six cards below are its spelling, and none of them changes the sound.</p>
      ''' + rule_grid([
    ('Add <em>-ed</em>',
     'The rule for almost every verb in English, and for every new one: <em>walk, play, call, open, visit</em>.',
     ex('We <em>walked</em> to the harbour and <em>played</em> cards on the quay.')),
    ('Ends in <em>-e</em>? Just add <em>-d</em>',
     '<em>like &rarr; liked, live &rarr; lived, decide &rarr; decided</em>. The <em>e</em> is already there.',
     ex('She <em>decided</em> to stay, and she <em>lived</em> there for years.')),
    ('Consonant + <em>y</em> becomes <em>-ied</em>',
     '<em>study &rarr; studied, carry &rarr; carried, try &rarr; tried</em>. After a vowel the <em>y</em> stays: <em>play &rarr; played, enjoy &rarr; enjoyed</em>.',
     ex('He <em>studied</em> the chart and <em>carried</em> it on deck.')),
    ('Short, stressed, one consonant: double it',
     '<em>stop &rarr; stopped, plan &rarr; planned, prefer &rarr; preferred</em>. No double when the stress falls earlier: <em>open &rarr; opened, visit &rarr; visited</em>. Never double <em>w, x</em> or <em>y</em>: <em>showed, fixed</em>.',
     ex('The engine <em>stopped</em>, so we <em>opened</em> the sails.')),
    ('British English doubles the <em>l</em>',
     '<em>travel &rarr; travelled, cancel &rarr; cancelled</em>. American English writes <em>traveled, canceled</em>. Both are correct; choose one and keep to it.',
     ex('They <em>travelled</em> north and <em>cancelled</em> the last crossing.')),
    ('One form for everybody',
     'The past does not change with the person: <em>I, you, she, we, they walked</em>. No <em>-s</em>, no exceptions. (<em>Be</em> is the only verb with two: <em>was, were</em>.)',
     ex('I <em>waited</em>, she <em>waited</em>, they all <em>waited</em>.')),
]) + chart(
    'The three provinces: what <em>-ed</em> sounds like',
    'The spelling never changes, but the sound does, and the chart&#39;s three provinces are these three sounds. Only one of them adds a syllable.',
    ['Sound', 'After', 'Say it'],
    [['/t/', 'a voiceless sound: <em>p, k, s, sh, ch, f</em>',
      'stopped &middot; walked &middot; watched &middot; cooked &middot; liked &middot; laughed'],
     ['/d/', 'a voiced sound (<em>b, g, v, l, m, n, r</em>) or any vowel',
      'played &middot; studied &middot; travelled &middot; called &middot; lived &middot; opened'],
     ['/&#618;d/', '<em>t</em> or <em>d</em>, and nothing else',
      'started &middot; waited &middot; visited &middot; needed &middot; decided &middot; landed']],
    'The test: put a hand on your throat and say the last <em>sound</em> of the verb (not the last letter: '
    '<em>like</em> ends in /k/). If it buzzes, <em>-ed</em> says /d/; if it does not, /t/. Only after <em>t</em> or '
    '<em>d</em> does it make an extra syllable: <em>walked</em> is one syllable, never <em>walk-ed</em>.') + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
EAST = '''<div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">The archipelago</div>
      <h2>Irregularia: no one rule, but families</h2>
      <p class="chart-note" style="margin:-6px 0 18px">About two hundred verbs never moved to the continent, and they are the ones you use every day: old, short and common. But they did not scatter. They live in families that share a sound, and each family has an island. Learn one verb on an island and you have a model for the rest of it.</p>
      ''' + rule_grid([
    ('I &middot; A &middot; U Island',
     'The vowel walks from <em>i</em> to <em>a</em> to <em>u</em>: <em>sing sang sung, drink drank drunk, swim swam swum, begin began begun</em>.',
     ex('We <em>sang</em> all the way home; I had never <em>sung</em> so loudly.')),
    ('Ought Island',
     'Past and participle both end in the sound <em>-ought</em>, sometimes spelled <em>-aught</em>: <em>bring brought, think thought, catch caught, teach taught, buy bought</em>.',
     ex('She <em>brought</em> the map and <em>taught</em> us to read it.')),
    ('-EW Island',
     'The past ends in <em>-ew</em> and the participle in <em>-own</em>: <em>blow blew blown, grow grew grown, know knew known, throw threw thrown, fly flew flown</em>.',
     ex('The wind <em>blew</em> all night, and by morning it had <em>blown</em> the tent away.')),
    ('-T Island',
     'A <em>-t</em> appears, often with a shorter vowel, and both forms are the same: <em>keep kept, sleep slept, feel felt, leave left, build built</em>.',
     ex('We <em>slept</em> on deck and <em>left</em> before dawn.')),
    ('-EN Island',
     'The third form ends in <em>-en</em>: <em>speak spoke spoken, break broke broken, take took taken, give gave given, write wrote written</em>.',
     ex('She <em>broke</em> the record, and it has never been <em>broken</em> since.')),
    ('The Still Rocks',
     'Verbs that never change, in any form: <em>cut, put, hit, let, cost, set, shut, hurt</em>. Nearly all of them end in <em>-t</em>.',
     ex('Yesterday it <em>cost</em> ten euros; today it costs twelve.')),
]) + chart(
    'Three forms, island by island',
    'The third column is the past participle, the form that follows <em>have</em> and makes the passive (<em>I have sung</em>, <em>it was broken</em>). On some islands it is a different word from the past; on others it is the same.',
    ['Island', 'Base &middot; past &middot; participle', 'More verbs that live there'],
    [['I&middot;A&middot;U', 'sing &middot; sang &middot; sung', 'ring, drink, swim, begin, sink, shrink'],
     ['Ought', 'buy &middot; bought &middot; bought', 'bring, think, fight, catch, teach, seek'],
     ['-EW', 'blow &middot; blew &middot; blown', 'grow, know, throw, fly, and <em>draw</em> (drew, drawn)'],
     ['-T', 'keep &middot; kept &middot; kept', 'sleep, feel, leave, build, send, spend, lend, mean'],
     ['-EN', 'speak &middot; spoke &middot; spoken', 'break, take, give, write, choose, steal, forget, eat'],
     ['Still Rocks', 'cut &middot; cut &middot; cut', 'put, hit, let, cost, set, shut, hurt, quit']]) + chart(
    'The Lone Stacks, and others to learn alone',
    'These belong to no family. They are also the commonest verbs in the language, which is why they kept their odd shapes: words used every day resist being smoothed out.',
    ['Verb', 'Past', 'Participle'],
    [['go', 'went', 'gone'], ['be', 'was &middot; were', 'been'], ['do', 'did', 'done'],
     ['see', 'saw', 'seen'], ['have', 'had', 'had'], ['make', 'made', 'made'], ['say', 'said', 'said'],
     ['get', 'got', 'got (British) &middot; gotten (American)'], ['come', 'came', 'come']]) + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
DIAGRAM = '''<div class="camp" id="order">
      ''' + MARK_PANES + '''
      <div class="camp-label">Interactive</div>
      <h2>Read the chart</h2>
      <div class="diagram-card" data-map-zoom data-mz-target=".chart-toggle-wrap" data-mz-btn=".name-bar" data-mz-ratio="1.5" data-mz-min="1100">
        <p class="diagram-intro">Click a landmass and its list lights up below. Every harbour is named after a verb. Switch the chart to <em>just the verbs</em> to see them bare, then to <em>the past forms</em> to see what each one becomes. Notice that on Regularia the past forms all look alike, while each island has its own pattern.</p>
        <div class="name-bar" id="name-bar">
          <span class="name-label">Read the chart as</span>
          <button type="button" data-mode="place" class="on" aria-pressed="true">Place names</button>
          <button type="button" data-mode="verb" aria-pressed="false">Just the verbs</button>
          <button type="button" data-mode="past" aria-pressed="false">The past forms</button>
        </div>
        <div class="diagram-stage" data-mz-scroll>
          <div class="chart-toggle-wrap">
            <img class="chart-photo" src="''' + ART + '''/chart-clean.jpg" alt="" width="1536" height="1024" loading="lazy">
            ''' + M.chart_overlay('reg') + '''
          </div>
        </div>
        <p class="chart-scroll-hint">Drag the chart sideways to reach the islands.</p>
        <div class="diagram-panels three">
          <div class="diagram-panel is-west" id="panel-reg">
            <h4>Regularia &middot; verb + <em>-ed</em></h4>
            <ul id="panel-reg-list"></ul>
          </div>
          <div class="diagram-panel is-isle" id="panel-strait">
            <h4>The strait &middot; two pasts</h4>
            <ul id="panel-strait-list"></ul>
          </div>
          <div class="diagram-panel is-east" id="panel-irr">
            <h4>Irregularia &middot; families</h4>
            <ul id="panel-irr-list"></ul>
          </div>
        </div>
      </div>
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
DID = '''<div class="camp" id="did">
      ''' + MARK_CLOCK + '''
      <div class="camp-label">Below deck</div>
      <h2>When <em>did</em> carries the past</h2>
      <p class="chart-note" style="margin:-6px 0 18px">Every verb on the chart, regular or irregular, behaves the same way in a question or a negative: <em>did</em> takes the past, and the main verb goes back to its base form, as if nothing had happened to it. The past is marked once, never twice.</p>
      ''' + chart(
    'The past is marked once',
    'If you can see <em>did</em>, the verb after it is bare.',
    ['', 'Not this', 'This'],
    [['Negative', 'We didn&#39;t went home.', 'We didn&#39;t <em>go</em> home.'],
     ['Question', 'Did you saw the lighthouse?', 'Did you <em>see</em> the lighthouse?'],
     ['Question', 'Did the engine stopped?', 'Did the engine <em>stop</em>?'],
     ['Short answer', 'Yes, I did went.', 'Yes, I <em>did</em>.'],
     ['Wh- question', 'Where did they found it?', 'Where did they <em>find</em> it?']]) + '''
      <p class="chart-note" style="margin-top:16px"><strong><em>Be</em> is the exception.</strong> It never uses <em>did</em>. You ask <em>Were you there?</em> and answer <em>I wasn&#39;t</em>; <em>Did you be there?</em> is not English.</p>
      ''' + exi('<em>Did</em> you <em>go</em>? &nbsp;&middot;&nbsp; <em>Were</em> you there?') + chart(
    'After <em>have</em>: the third form',
    'On Regularia, Ought Island, -T Island and the Still Rocks, the past and the participle are the same word, so nothing can go wrong. On I&middot;A&middot;U, -EW and -EN and on the Lone Stacks they are different, and <em>have</em> takes the third one.',
    ['Where', 'Past simple', 'After <em>have</em>'],
    [['I&middot;A&middot;U', 'We <em>sang</em>.', 'We have <em>sung</em>. Never <em>have sang</em>.'],
     ['-EW', 'It <em>grew</em>.', 'It has <em>grown</em>.'],
     ['-EN', 'She <em>took</em> it.', 'She has <em>taken</em> it.'],
     ['Lone Stacks', 'They <em>went</em>.', 'They have <em>gone</em>. Never <em>have went</em>.'],
     ['Regularia', 'I <em>waited</em>.', 'I have <em>waited</em>. The same word.']]) + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
ISLE = fork(
    'Forked Isle: one verb, two meanings, two pasts',
    'Three verbs on the chart have two meanings, and each meaning has kept its own past. Choosing the wrong one does '
    'not just sound odd: it says something else.',
    ['Verb', 'One meaning', 'The other'],
    [['lie', 'say something untrue &rarr; <em>lied</em><br><em>He lied about the weather.</em>',
      'be flat, rest &rarr; <em>lay</em>, <em>lain</em><br><em>She lay on the deck in the sun.</em>'],
     ['hang', 'kill with a rope &rarr; <em>hanged</em><br><em>Pirates were hanged at the port.</em>',
      'everything else &rarr; <em>hung</em><br><em>We hung the lanterns on the mast.</em>'],
     ['shine', 'polish (mostly American) &rarr; <em>shined</em><br><em>He shined his boots.</em>',
      'give out light &rarr; <em>shone</em><br><em>The moon shone on the water.</em>']],
    'And the rock beside the island: <em>lay</em> is also a separate verb, <em>lay &rarr; laid</em>, meaning '
    '<em>put something down</em>. <em>I lay down</em> is the past of <em>lie</em>; <em>I laid the map down</em> is the '
    'past of <em>lay</em>.',
    [('%s#quiz' % OUT, 'Straight to the test &rarr;'),
     ('sailing-the-seas-of-grammar.html', 'The first chart: gerunds and infinitives')])

SHALLOWS = '''<div class="camp" id="shallows">
      ''' + MARK_FORK + '''
      <div class="camp-label">The Shallows</div>
      <h2>Where both forms are right</h2>
      <p class="chart-note" style="margin:-6px 0 18px">South of the strait the water shoals. Here a handful of verbs have two past forms, an old one in <em>-t</em> and a newer one in <em>-ed</em>, and <strong>both are correct and mean the same thing</strong>. They are drifting west: the <em>-ed</em> form is slowly winning, and in American English it has already won.</p>
      ''' + chart(
    'The verbs in the Shallows',
    'Both columns are right. British English uses both; American English uses the <em>-ed</em> form almost always.',
    ['Verb', 'The old form', 'The newer form'],
    [['learn', 'learnt', 'learned'], ['dream', 'dreamt', 'dreamed'], ['burn', 'burnt', 'burned'],
     ['spell', 'spelt', 'spelled'], ['lean', 'leant', 'leaned'], ['smell', 'smelt', 'smelled'],
     ['spill', 'spilt', 'spilled'], ['spoil', 'spoilt', 'spoiled']]) + '''
      <p class="chart-note" style="margin-top:16px"><strong>One place the old form holds on:</strong> before a noun, as an adjective. <em>Burnt toast, a spoilt child, spilt milk</em> sound natural even to speakers who would say <em>burned</em> and <em>spoiled</em> as verbs.</p>
      ''' + exi('The toast <em>burned</em>. &nbsp;&middot;&nbsp; I hate <em>burnt</em> toast.') + chart(
    'Not every current runs west',
    'A few verbs are drifting the other way, from regular to irregular, mostly in American English. Worth recognising; there is no need to use them.',
    ['Verb', 'Regular', 'The newer irregular'],
    [['dive', 'dived', 'dove (American)'], ['sneak', 'sneaked', 'snuck (informal)'],
     ['fit', 'fitted', 'fit (American)']]) + '''
    </div>

    '''

# ═════════════════════════════════════════════════════════════════════
SIGNALS = signals(
    'Sail west &mdash; add <em>-ed</em>',
    ['almost every verb in the language',
     'every new verb: <em>texted, emailed, googled, zoomed</em>',
     'verbs made from nouns: <em>parked, phoned, emailed</em>',
     'long verbs: <em>discovered, remembered, organised</em>',
     'verbs borrowed from other languages',
     'any rare verb whose past you have never heard'],
    'Make for the islands &mdash; learn by family',
    ['the verbs you hear every day: <em>go, get, make, take, come</em>',
     '<em>-ing</em> and <em>-ink</em> verbs: often I&middot;A&middot;U (but <em>bring</em> and <em>think</em> sail to Ought)',
     '<em>-eep, -eel, -end</em> verbs: often -T',
     'short <em>-ow</em> verbs: often -EW (<em>show</em> is half: showed, shown)',
     'short <em>-t</em> verbs: often the Still Rocks',
     'and the four Lone Stacks: <em>go, be, do, see</em>'],
    'One line to keep: a verb you have never met before is almost certainly regular. The irregular ones are old, '
    'short and common, so you meet them early and often. The islands are where the everyday verbs live.')

# ═════════════════════════════════════════════════════════════════════
QUIZ = [
    ('The engine ___ halfway across the bay.',
     'Short, stressed, one consonant at the end.', 'stopped',
     ['stopped', 'stoped', 'stopt', 'stopping'],
     'Stop ends in one vowel and one consonant, and the syllable is stressed, so the consonant doubles: stopped. The same goes for plan, planned.'),
    ('She ___ the old charts every evening before bed.',
     'Consonant + <em>y</em>.', 'studied',
     ['studied', 'studyed', 'studed', 'studies'],
     'After a consonant, y becomes i before -ed: study, studied. After a vowel it stays: play, played.'),
    ('In which of these does <em>-ed</em> add an extra syllable?',
     'It happens after only two sounds.', 'waited',
     ['waited', 'walked', 'played', 'laughed'],
     'The extra syllable comes only after t or d: wait-ed. Walked and laughed end in /t/, played in /d/, and all three are one syllable.'),
    ('The whole crew ___ sea shanties until midnight.',
     'I&middot;A&middot;U Island: the vowel walks i, a, u.', 'sang',
     ['sang', 'sung', 'singed', 'sing'],
     'Sing, sang, sung: the past simple is the middle one. Sung is the third form, for have: we have sung. (Singed is the past of singe, to burn slightly.)'),
    ('He ___ a bottle of water for everyone.',
     'Ought Island.', 'brought',
     ['brought', 'bringed', 'brang', 'bought'],
     'Bring lives on Ought Island: bring, brought, brought. Brang is a common mistake made by analogy with sing, sang; bought is the past of buy.'),
    ('The wind ___ from the west all night.',
     '-EW Island.', 'blew',
     ['blew', 'blowed', 'blown', 'blewed'],
     'Blow, blew, blown. The past simple ends in -ew; blown is the third form, for have: it has blown.'),
    ('We ___ in the cabin while the storm passed.',
     '-T Island.', 'slept',
     ['slept', 'sleeped', 'sleept', 'slepted'],
     'Sleep is a -T Island verb: a t appears and the vowel shortens, slept. Keep, feel and leave do the same: kept, felt, left.'),
    ('Last summer the ferry ___ three euros.',
     'The Still Rocks never move.', 'cost',
     ['cost', 'costed', 'costs', 'coasted'],
     'Cost is a Still Rock: cost, cost, cost. Costed exists only in business English, meaning worked out the cost of.'),
    ('Did you ___ the lighthouse from the beach?',
     '<em>Did</em> has already taken the past.', 'see',
     ['see', 'saw', 'seen', 'seeing'],
     'After did the verb goes back to its base form: did you see? The past is marked once, by did. Did you saw marks it twice.'),
    ('We ___ to the island in the end. The sea was too rough.',
     'A negative with <em>did</em>.', 'didn&#39;t go',
     ['didn&#39;t go', 'didn&#39;t went', 'not went', 'don&#39;t went'],
     'Did not + base form: we didn&#39;t go. Didn&#39;t went is the commonest past-tense error in English, and every listener hears it.'),
    ('By the time we reached the quay, the ferry had already ___.',
     'After <em>had</em>: the third form. <em>Go</em> is a Lone Stack.', 'gone',
     ['gone', 'went', 'goed', 'go'],
     'Go, went, gone: had takes the third form. Had went is a common mistake, because on this stack the past and the third form are different words.'),
    ('She ___ on the deck all afternoon, reading.',
     'Forked Isle: which <em>lie</em> is this?', 'lay',
     ['lay', 'lied', 'laid', 'lain'],
     'Lie meaning rest or be flat has the past lay. Lied is the past of lie meaning say something untrue; laid is the past of lay, put something down.'),
    ('They ___ lanterns along the harbour wall for the festival.',
     'Forked Isle: a person, or a thing?', 'hung',
     ['hung', 'hanged', 'hang', 'hunged'],
     'Things are hung: we hung the lanterns. Hanged is only for executing a person with a rope.'),
    ('Which of these past forms is NOT correct?',
     'Two forms are fine in the Shallows. One of these is not a word at all.', 'teached',
     ['teached', 'learnt', 'dreamed', 'spelt'],
     'Learnt, dreamed and spelt are all correct: the Shallows has two forms for each. Teach lives on Ought Island and has only one past, taught.'),
]

# ═════════════════════════════════════════════════════════════════════
PANEL_REG = [
    '<b>/t/</b> stopped &middot; walked &middot; watched &middot; cooked &middot; liked &middot; laughed',
    '<b>/d/</b> played &middot; studied &middot; travelled &middot; called &middot; lived &middot; opened',
    '<b>/&#618;d/</b> started &middot; waited &middot; visited &middot; needed &middot; decided &middot; landed',
    'New verbs land here: <em>texted, emailed, googled</em>.',
]
PANEL_STRAIT = [
    ('forked', '<b>Forked Isle</b> lie: <em>lied</em> (untrue) &middot; <em>lay</em> (rest)'),
    ('forked', 'hang: <em>hanged</em> (a person) &middot; <em>hung</em> (a thing)'),
    ('forked', 'shine: <em>shined</em> (polish) &middot; <em>shone</em> (light)'),
    ('shallows', '<b>The Shallows</b> learnt / learned &middot; dreamt / dreamed &middot; burnt / burned &middot; spelt / spelled'),
]
PANEL_IRR = [
    ('iau', '<b>I&middot;A&middot;U</b> sing sang sung &middot; drink &middot; swim &middot; begin'),
    ('ought', '<b>Ought</b> buy bought &middot; bring &middot; think &middot; catch &middot; teach'),
    ('ew', '<b>-EW</b> blow blew blown &middot; grow &middot; know &middot; throw &middot; fly'),
    ('t', '<b>-T</b> keep kept &middot; sleep &middot; feel &middot; leave &middot; build'),
    ('en', '<b>-EN</b> speak spoke spoken &middot; break &middot; take &middot; give &middot; write'),
    ('still', '<b>Still Rocks</b> cut &middot; put &middot; hit &middot; let &middot; cost'),
    ('lone', '<b>Lone Stacks</b> go went gone &middot; be was been &middot; do did done &middot; see saw seen'),
]
for _rows in (PANEL_REG, [t for _, t in PANEL_STRAIT], [t for _, t in PANEL_IRR]):
    for _t in _rows:
        assert '"' not in _t, 'a panel line would break its JS string: ' + _t

# landmass -> (panel, row key, outline colour)
TARGETS = {
    'regularia': ('panel-reg', '', M.INK['regularia']),
    'forked': ('panel-strait', 'forked', M.INK['forked']),
    'shallows': ('panel-strait', 'shallows', M.INK['shallows']),
    'iau': ('panel-irr', 'iau', M.INK['iau']), 'ought': ('panel-irr', 'ought', M.INK['ought']),
    'ew': ('panel-irr', 'ew', M.INK['ew']), 't': ('panel-irr', 't', M.INK['t']),
    'en': ('panel-irr', 'en', M.INK['en']), 'still': ('panel-irr', 'still', M.SEA_INK),
    'lone': ('panel-irr', 'lone', M.SEA_INK),
}

DIAGRAM_JS = '''var panelReg = [
  %s
];
var panelStrait = [
  %s
];
var panelIrr = [
  %s
];

function renderList(id, items){
  var ul = document.getElementById(id);
  if (!ul) return;
  ul.innerHTML = "";
  items.forEach(function(it){
    var li = document.createElement("li");
    if (typeof it === "string"){ li.innerHTML = it; }
    else { li.innerHTML = it[1]; li.setAttribute("data-key", it[0]); }
    ul.appendChild(li);
  });
}
renderList("panel-reg-list", panelReg);
renderList("panel-strait-list", panelStrait);
renderList("panel-irr-list", panelIrr);

function pulseShape(el){
  el.animate([{ opacity: 1 }, { opacity: 0.55 }, { opacity: 1 }], { duration: 380, easing: "ease-out" });
}

// the chart reads three ways: place names, the bare verb, or its past
// form(s). All three live on the same text node and swap content.
// A two-form past ("sang · sung") is set a size smaller so it fits
// between its neighbours; a value with "|" (the Lone Stacks) goes on two
// lines, past above participle.
var NAME_ATTR = { place: "data-place", verb: "data-verb", past: "data-past" };
var SVGNS = "http://www.w3.org/2000/svg";
function regNames(mode){
  document.querySelectorAll(".sail-chart text.place-name").forEach(function(t){
    var v = t.getAttribute(NAME_ATTR[mode]);
    while (t.firstChild) t.removeChild(t.firstChild);
    if (v.indexOf("|") >= 0){
      v.split("|").forEach(function(part, i){
        var ts = document.createElementNS(SVGNS, "tspan");
        ts.setAttribute("x", t.getAttribute("x"));
        if (i) ts.setAttribute("dy", "1.15em");
        ts.textContent = part;
        t.appendChild(ts);
      });
    } else {
      t.textContent = v;
    }
    t.setAttribute("font-size", v.indexOf("·") >= 0 ? 15 : t.getAttribute("data-size"));
    t.style.fontStyle = mode === "place" ? "normal" : "italic";
  });
  document.querySelectorAll("#name-bar button").forEach(function(b){
    var on = b.getAttribute("data-mode") === mode;
    b.classList.toggle("on", on);
    b.setAttribute("aria-pressed", on ? "true" : "false");
  });
}
document.querySelectorAll("#name-bar button").forEach(function(b){
  b.addEventListener("click", function(){ regNames(b.getAttribute("data-mode")); });
});

// clicking a landmass lights its panel, and the island's own line in it
var TARGETS = %s;
Object.keys(TARGETS).forEach(function(key){
  var el = document.getElementById("reg-" + key);
  if (!el) return;
  var t = TARGETS[key];
  var activate = function(){
    pulseShape(el);
    document.querySelectorAll(".diagram-panel").forEach(function(p){ p.style.outline = "none"; });
    document.querySelectorAll(".diagram-panel li.is-lit").forEach(function(li){ li.classList.remove("is-lit"); });
    var panel = document.getElementById(t[0]);
    if (!panel) return;
    panel.style.outline = "2px solid " + t[2];
    if (t[1]){
      panel.querySelectorAll('li[data-key="' + t[1] + '"]').forEach(function(li){ li.classList.add("is-lit"); });
    }
    panel.scrollIntoView({ block: "nearest", behavior: "smooth" });
  };
  el.addEventListener("click", activate);
  el.addEventListener("keydown", function(e){
    if (e.key === "Enter" || e.key === " "){ e.preventDefault(); activate(); }
  });
});

''' % (",\n  ".join('"%s"' % e for e in PANEL_REG),
       ",\n  ".join('["%s", "%s"]' % kt for kt in PANEL_STRAIT),
       ",\n  ".join('["%s", "%s"]' % kt for kt in PANEL_IRR),
       json.dumps(TARGETS))

LIGHTBOX_JS = '''(function(){
  var btn = document.getElementById("hero-map-btn");
  var box = document.getElementById("hero-lightbox");
  if (!btn || !box) return;
  var closeBtn = box.querySelector(".lightbox-close");
  function openBox(){ box.classList.add("is-open"); document.body.style.overflow = "hidden"; closeBtn.focus(); }
  function closeBox(){ box.classList.remove("is-open"); document.body.style.overflow = ""; btn.focus(); }
  btn.addEventListener("click", openBox);
  closeBtn.addEventListener("click", closeBox);
  box.addEventListener("click", function(e){ if (e.target === box) closeBox(); });
  document.addEventListener("keydown", function(e){
    if (e.key === "Escape" && box.classList.contains("is-open")) closeBox();
  });
})();
'''

# The gulls cross the whole page in the sky layer, as on the first chart.
# No flock over the hero: this chart has words in every channel, and a gull
# must not cross a teaching label.
GULLS_JS = open('lesson-template/build/gulls.js', encoding='utf-8').read() + '''
skyGulls(document.getElementById("gull-sky"), {
  px: function (w) { return w < 560 ? 26 : 34; }, seed: 9,
  flocks: [
    {from: [-8, 70], to: [108, 26], flight: 17, cycle: 46, at: 3,
     birds: [[0, 0, 1], [-1.5, 1.1, .95], [-1.1, -1.3, 1.05]]},
    {from: [108, 16], to: [-8, 52], flight: 15, cycle: 46, at: 26,
     birds: [[0, 0, 1], [-1.4, -1, .92]]}
  ]
});
'''

sys.path.insert(0, 'tools')
import sherpa_sky, sherpa_topo
_music = json.load(open('sailing-the-seas-of-grammar/music.json', encoding='utf-8'))
MUSIC_TAG = ('<script src="block-camp/camp-music.js" data-track="sailing-the-seas-of-grammar/music.m4a" '
             'data-loop="%g %g" defer></script>\n' % tuple(_music['loop']))
SKY_CSS = ('  /* ── the sky: clouds and gulls (see build_sailing.py) ── */\n'
           '  .gull-sky{position:fixed;inset:0;z-index:-1;pointer-events:none;overflow:hidden;}\n'
           '  @media print{.gull-sky{display:none;}}\n'
           '  ' + ','.join(sherpa_topo.HALO_ON) + '{text-shadow:' + sherpa_topo.HALO + ';}\n')
SKY_EL = '<div class="gull-sky" id="gull-sky" aria-hidden="true"></div>\n' + sherpa_sky.ELEMENT

# The waterlined background is the first chart's, shared verbatim so the
# series looks like one series (sailing_waterline_gen.py makes it).
_sail = open('lesson-template/build/build_sailing.py', encoding='utf-8').read()
_a = _sail.index('/* Waterlining:')
_b = _sail.index('  /* ── the sea chart ── */')
WATERLINES = _sail[_a:_b]
assert WATERLINES.count('@supports') == 1 and WATERLINES.rstrip().endswith('}'), 'waterline block moved in build_sailing.py'

EXTRA_CSS = '''
  /* ── the hero map, click to expand ── */
  .hero-diagram-btn{all:unset;display:block;width:100%;cursor:zoom-in;position:relative;
                     border-radius:14px;overflow:hidden;}
  .hero-diagram-btn:hover .hero-diagram{filter:brightness(1.03);}
  .hero-diagram-btn:focus-visible{outline:3px solid var(--accent);outline-offset:3px;}
  .hero-diagram-btn::after{content:"Click to expand";position:absolute;right:12px;bottom:12px;
                            background:var(--accent);color:var(--on-accent);font-family:'Inter',sans-serif;
                            font-size:11.5px;font-weight:600;padding:5px 11px;border-radius:999px;
                            opacity:0;transition:opacity .15s ease;pointer-events:none;}
  .hero-diagram-btn:hover::after,.hero-diagram-btn:focus-visible::after{opacity:.92;}
  .img-lightbox{--scrim:color-mix(in srgb,var(--ink) 90%,transparent);
                display:none;position:fixed;inset:0;background:var(--scrim);
                align-items:center;justify-content:center;padding:28px;z-index:80;}
  .img-lightbox.is-open{display:flex;}
  .img-lightbox img{max-width:96vw;max-height:92vh;border-radius:10px;}
  .lightbox-close{position:absolute;top:18px;right:22px;background:transparent;
                   color:var(--card);border:1px solid var(--card);width:40px;height:40px;
                   border-radius:50%;font-size:24px;line-height:1;cursor:pointer;
                   display:flex;align-items:center;justify-content:center;}
  .lightbox-close:hover{background:var(--accent);}
  /* ── the header, in the sea-chart's own display face (the first chart's font file) ── */
  @font-face{font-family:'Faktum';src:url('sailing-the-seas-of-grammar/fonts/Faktum-Bold.woff2') format('woff2');
             font-weight:700;font-style:normal;font-display:swap;}
  .wordmark .brand,.hero h1{font-family:'Faktum','Fraunces',serif;font-weight:700;}
  .q-hint em,.rule-card .ex em{font-style:normal;font-weight:600;}
''' + WATERLINES + '''
  /* ── the sea chart ── */
  .diagram-panels.three{grid-template-columns:repeat(3,1fr);}
  @media (max-width:820px){.diagram-panels.three{grid-template-columns:1fr;}}
''' + panel_css('is-west', M.PAINT['regularia']) + panel_css('is-isle', M.PAINT['forked']) \
    + panel_css('is-east', M.PAINT['iau']) + '''
  .diagram-panel li{padding:3px 6px;margin:0 -6px;border-radius:6px;transition:background .15s ease;}
  .diagram-panel li.is-lit{background:var(--accent-lighter);}
  .diagram-panel li b{font-weight:700;margin-right:.3em;}
  .sail-chart-overlay{--hotspot-wash:color-mix(in srgb,var(--card) 24%,transparent);}
  .sail-chart-overlay .land{transition:fill .15s ease;}
  .sail-chart-overlay .land:hover{fill:var(--hotspot-wash);}
  .sail-chart-overlay .land:focus-visible{fill:var(--hotspot-wash);outline:3px solid var(--accent);outline-offset:2px;}
  .sail-chart-overlay text{pointer-events:none;}
  .chart-scroll-hint{display:none;font-size:12.5px;color:var(--ink-soft);margin:9px 2px 0;font-style:italic;}
  .name-bar{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:0 0 14px;
            font-family:'Inter',sans-serif;font-size:12.5px;color:var(--ink-soft);}
  .name-bar .name-label{letter-spacing:.06em;text-transform:uppercase;font-weight:700;font-size:11px;}
  .name-bar button{font:inherit;font-weight:600;border:1px solid var(--accent-light);
                   background:var(--card);color:var(--ink-soft);padding:5px 12px;border-radius:999px;
                   cursor:pointer;transition:background .12s ease,color .12s ease;}
  .name-bar button:hover{color:var(--ink);}
  .name-bar button.on{background:var(--accent);color:var(--on-accent);border-color:var(--accent);}
  .chart-toggle-wrap{position:relative;}
  .chart-toggle-wrap .chart-photo{display:block;width:100%;height:auto;border-radius:14px;}
  .chart-toggle-wrap .sail-chart{position:absolute;top:0;left:0;width:100%;height:100%;}
  .hero-cta{display:inline-flex;align-items:center;gap:6px;margin-top:18px;background:var(--accent);
            color:var(--on-accent);font-family:'Inter',sans-serif;font-weight:600;font-size:14px;
            padding:11px 20px;border-radius:999px;text-decoration:none;transition:opacity .12s ease;}
  .hero-cta:hover{opacity:.88;}
  /* a chart this dense is unreadable shrunk to a phone: it scrolls at a
     width where the harbour names are still about 12px */
  @media (max-width:760px){
    .diagram-stage{overflow-x:auto;-webkit-overflow-scrolling:touch;}
    .diagram-stage .chart-toggle-wrap{width:980px;max-width:none;}
    .chart-scroll-hint{display:block;}
  }
  /* on a phone the trail's 66px gutter and the card's padding left the chart
     a 205px window; the chart card reaches into the gutter instead */
  @media (max-width:600px){
    #order .diagram-card{margin-left:-56px;padding:16px 12px;}
  }
'''

# the result messages are set as text, not HTML: a real apostrophe, never &#39;
REPLACEMENTS = [
    ('then sail the islands one at a time.</p>\n    </div>',
     'then sail the islands one at a time.</p>\n      '
     '<a class="hero-cta" href="#order">Read the chart <span aria-hidden="true">&rarr;</span></a>\n    </div>'),
    ('<div class="brand">Sherpa <span>Tensing</span></div>',
     '<div class="brand">Sailing the <span>Seas of Grammar</span></div>'),
    ('<div class="sub">Forbes English &middot; a route up the tenses</div>',
     '<div class="sub">Forbes English &middot; regular and irregular verbs</div>'),
    ('<a class="up-link" href="sherpa-tensing-route-map.html"><span class="arw" aria-hidden="true">&larr;</span>Route map</a>',
     '<a class="up-link" href="grammar.html#maps"><span class="arw" aria-hidden="true">&larr;</span>Grammar maps</a>'),
    ('<div class="camp-label">Summit log</div>', '<div class="camp-label">Ship&#39;s log</div>'),
    ('<button class="retry-btn" id="retry-btn">Climb again</button>',
     '<button class="retry-btn" id="retry-btn">Sail it again</button>'),
    ('<a class="base-camp" href="sherpa-tensing-route-map.html">&larr; Return to base camp</a>',
     '<a class="base-camp" href="grammar.html#maps">&larr; Back to the grammar maps</a>'),
    ('<a class="next-camp" href="sherpa-tensing-route-map.html">Choose your next camp &rarr;</a>',
     '<a class="next-camp" href="sailing-the-seas-of-grammar.html">The first chart: gerunds and infinitives &rarr;</a>'),
    ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
     '"Clean run. You can sail the continent and name every island’s family."'),
    ('"Solid progress. Worth a look back at camp five before camp eight."',
     '"Solid progress. Say each island’s three forms aloud, then sail it again."'),
    ('"Good first attempt. The will/going to fork is the part to read again."',
     '"Good first attempt. Start with the continent: -ed, and its three sounds."'),
    ('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── THE SEA CHART ── */'),
    ('// ── NOW vs WILL diagram interactivity ──', '// ── the chart, made clickable ──'),
    ('\n</style>', EXTRA_CSS + SKY_CSS + '</style>'),
    ('<div class="camp-label">The fork in the path</div>', '<div class="camp-label">The strait</div>'),
    ('<div class="camp-label">Trail markers</div>', '<div class="camp-label">Tide tables</div>'),
    ('<div class="camp-label">The climb</div>', '<div class="camp-label">The crossing</div>'),
    ('"Reach the summit"', '"Make landfall"'),
]

TITLE = '<title>Regularia &amp; Irregularia &mdash; Regular and Irregular Verbs</title>'

s = assemble(
    HERO,
    WEST + EAST + DIAGRAM + DID + ISLE + SHALLOWS + SIGNALS,
    DIAGRAM_JS + LIGHTBOX_JS + GULLS_JS,
    questions(QUIZ),
    PALETTE,
    TITLE,
    REPLACEMENTS,
    OUT,
    own_tail=False)

for a, b in REPLACEMENTS:
    if a != '\n</style>':            # that one is meant to recur: the insert ends with it
        assert a not in s, 'replacement did not land: %r' % a[:70]
assert 'regular and irregular verbs</div>' in s and 'Make landfall' in s, 'the shell text was not replaced'

# ── strip the mountain's machinery: there is no camp here to earn ──
s = open(OUT, encoding='utf-8').read()
a = s.index('\n// ── progression:')
b = a + re.search(r'\nsherpaBar\(\);\n', s[a:]).end()
s = s[:a] + '\n' + s[b:]
s = re.sub(r'\n  /\* ── progression: the voice toggle and its lock ── \*/.*?\n(?=  /\*|\})',
           '\n', s, count=1, flags=re.S)

# ── lift the data-tr onto the wrapper rule_grid already drew ──
s = re.sub(r'<div class="ex">\x01(\d+)\x01', r'<div class="ex" data-tr="\1">', s)
assert '\x01' not in s, 'an example marker escaped'

# ── our own examples, our own translations ──
import ex_tr_regularia as T
rows = []
for i in range(len(EX)):
    r = T.T.get(i)
    assert r and len(r) == 9, 'missing or short translation for example %d: %s' % (i, EX[i])
    rows.append('"%d": %s' % (i, json.dumps(r, ensure_ascii=False)))
assert len(T.T) == len(EX), 'ex_tr_regularia has %d rows for %d examples' % (len(T.T), len(EX))
s = re.sub(r'var EX_TR = \{.*?\};\n', lambda m: 'var EX_TR = {%s};\n' % ", ".join(rows), s, count=1, flags=re.S)

# ── the sky and the music ──
from PIL import Image
_sizes = {k: Image.open('Sherpa Tensing/cloud-%d.webp' % k).size for k in range(1, sherpa_sky.IMAGES + 1)}
assert s.count('</head>') == 1
s = s.replace('</head>', sherpa_sky.block(_sizes) + '</head>', 1)
s, n = re.subn(r'(<body\b[^>]*>\n?)', lambda m: m.group(1) + SKY_EL, s, count=1)
assert n == 1, 'no <body> to hang the sky on'
assert s.count('</body>') == 1
# every map can be enlarged (Innes, 2026-11-08: "maps need to be expandable always")
s = s.replace('</body>', MUSIC_TAG + '<script src="map-zoom.js" defer></script>\n</body>', 1)

# the shell's SEO block describes the camp it was cloned from; tools/seo.py
# writes this page's own from the catalogue row, so leave the block empty
s, n = re.subn(r'(<!-- SEO:start -->).*?(<!-- SEO:end -->)', r'\1\n\2', s, count=1, flags=re.S)
assert n == 1, 'no SEO block in the shell'
# assemble() swaps an older form of the camp's title; seo.py rewrote the camp
# since, so set ours here (seo.py then adds the level and the site name)
s, n = re.subn(r'<title>.*?</title>', TITLE, s, count=1, flags=re.S)
assert n == 1, 'no <title> in the shell'

# nothing of the camp this shell was cloned from may leak through
for leak in ('Camp Seven', 'camp seven', 'will/going to', 'willExamples'):
    assert leak not in s, 'the Sherpa shell leaked: %s' % leak

import sea_chrome
s = sea_chrome.add(s)  # the logo and see-through panels (sea_chrome.py)

open(OUT, 'w', encoding='utf-8', newline='').write(s)
print('wrote %s: %d examples, %d questions, %d bytes' % (OUT, len(EX), len(QUIZ), len(s)))
