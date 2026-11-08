# -*- coding: utf-8 -*-
"""The Comeback Ride (B2–C1): phrases for changing your mind about a design,
and how to make a careful claim from sales figures. Classic Forbes deck, 30 slides.

Built 2026-11-06 from `the-comeback-ride.html`, a 60-minute scrolling page
Innes supplied (not yet on the site): two dashboards to compare, a short
original reading inspired by Charlie Thomas's 2023 feature for British GQ,
four phrases (HARK BACK TO, GROW ON, COME AT A PRICE, WIN OVER), a sales claim
to test with MAY PARTLY EXPLAIN / IS CONSISTENT WITH, a prototype role-play
and an exit ticket. All of it is kept.

Fixed:
  * The first phrase item had a plural subject and a singular key: "The cream
    paint and curved lettering ___ the scooters" keyed HARKS back to. The
    sentence now has one subject ("With its cream paint and curved
    lettering, the scooter ___ …").
  * The page said the Meteor was "the UK's best-selling motorbike in the
    over-125cc category" in 2022. The figures behind that (Bennetts
    BikeSocial, August 2022) cover January to July only, with the Meteor six
    bikes ahead of BMW's R 1250 GS Adventure; the full-year table does not
    put it top overall. The claim slide now says exactly that, and the narrow
    lead became one of the questions, since it is the best reason in the
    lesson for a careful claim.
  * The phrase quiz was four drop-downs over four phrases, so the last one
    was always free. It is now typed, from a bank of base forms the learner
    has to put in the right form, with WIN … OVER split around its pronoun.
  * The reading questions and the claim task were open, with a model answer
    behind a "show" link. They are now scored (five reading, three claim),
    and the open parts (the dealer's question, the two other explanations)
    moved to the speaking fields.
Added: rule cards for the four phrases and for careful claims, form items
(IT GREW ON ME, not "I grew on it"; WON ME OVER, not "won over me"), a
second gap, three speaking fields and the activation.

Look and art (2026-11-08): first shipped 2026-11-06 in house style 2 on six
flat ChatGPT plates, which Innes rejected ("looks like uter dogshit"; the
layout "terrible"). Cutting the plates out and rotating the accent to green
were tried and rejected too ("your ideas for upgrading were worse"). Rebuilt
as a classic Forbes deck on six Midjourney renders (prompts in the session,
`--sref` the old cover): hero = the café racer at sunset; bg-dash = the
handlebars at a red light; bg-read = the scooter outside the café; bg-show =
an older and a younger rider at the same classic bike (the reading's showroom);
bg-claim = the clipboard with two near-level bars; bg-act = the workshop.
Palette: extract-palette.py --light on the hero, every row PASS, unedited.

Run from the repo root:  py lesson-template/build/build_comeback_ride.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='the-comeback-ride.html',
    title='The Comeback Ride (B2–C1)',
    folder='ComebackRide',
)

# Editorial style, HOUSE-STYLE §15 (Innes, 2026-11-08: the classic washed
# deck is "the old house style"; Beyond the Handlebars "was closest to" the
# one he wants). Every picture is framed in its own column, never behind a
# sentence, and its crop is set so the frame holds the plate's subject.
#
# ART: one entry per flow step: (plate, side, pos, shape, size) or None for
# a full-width slide with no picture. pos is background-position x for the
# default frame (37% x 57% of the stage, so it shows 65% of a 16:9 plate's
# width: pos = left edge of the window / 0.35) or, with size 'narrow' (30%,
# 52% of the width shown), left edge / 0.475. Subject spans, as fractions of
# each plate's width, measured on a 10% grid:
#   hero      the café racer .41-.94          -> 100%
#   narrow:   bg-read 63% (scooter), bg-claim 63% (clipboard and bikes),
#             bg-dash 74% (the speedometer)
#   bg-dash   the speedometer .52-.70         -> 71%  (window .25-.90)
#   bg-read   table .17, scooter .31-.80      -> 46%  (window .16-.81)
#   bg-show   the two riders .17-.43, bike .60-1.0; narrow: riders + the row
#             of bikes behind them            -> 32% narrow (window .15-.67)
#   bg-claim  clipboard .34-.55, bikes .61-.87 -> 77% (window .27-.92)
#   bg-act    stools .31-.50, bike .52-.96    -> 91%  (window .32-.97)
ART = [
    ('hero', None, '100%', None, None),          # talk: warm-up
    ('bg-dash', 'left', '71%', None, None),      # dial or screen
    ('bg-read', None, '46%', 'arch', None),      # reading 1: the scooter
    ('bg-show', 'left', '32%', None, 'narrow'),  # reading 2: the showroom
    ('bg-read', None, '63%', None, 'narrow'),    # reading questions (long options)
    ('bg-show', 'left', '49%', None, None),      # phrases 1
    ('hero', None, '100%', None, None),          # phrases 2
    ('bg-show', 'left', '49%', None, None),      # form questions
    None,                                        # gap 1: full width
    None,                                        # gap 2: full width
    ('bg-act', None, '91%', None, None),         # talk with the phrases
    ('bg-claim', 'left', '77%', 'arch', None),   # the claim
    ('bg-claim', None, '63%', None, 'narrow'),   # claim questions (long options)
    None,                                        # three hedging cards
    ('bg-dash', None, '74%', None, 'narrow'),    # hedging questions (long options)
    None,                                        # gap 3: full width
    ('bg-act', 'left', '91%', None, None),       # final talk
]
ART_RESULTS = ('hero', None, '100%', 'arch', None)

# The second set of plates (Innes, 2026-11-08: "a bit sparse on illustrations
# and big on repetition"): one picture per slide wherever the slide has room,
# so no plate repeats inside a stage. Keyed by flow step; a question step takes
# a list, one per item. Each is drawn with its subject centred (the prompts ask
# for it), so it takes the centre crop. A plate not on disk yet falls back to
# the ART entry above, so the deck builds either way.
NEW = {
    0: 'talk-attic',
    # (slot, pos) where the subject is off-centre: the open-road rider sits
    # at .55-.75 of the plate, the dealer's group at .30-.80, the glare screen at
    # .55-.85 (narrow window .525 wide; default .65).
    4: ['q-1946', 'q-engine', ('q-open-road', '80%'), ('q-dealer', '60%'), 'q-first-ride'],
    5: 'grew-on',
    6: 'old-photo',
    7: ['f-seat', 'f-test-ride', 'f-headlamp', ('f-glare', '85%')],
    10: 'talk-cafe',
    12: ['c-lot', ('c-neck-and-neck', '95%'), 'c-price'],   # podium bike .55-.92
    14: ['h-magnifier', 'h-scales'],
}
NEW_RESULTS = 'ride-away'


def pick(a, slot, i=0):
    """The ART entry with its plate swapped for a new one, if it has landed.
    Question items alternate the frame's side, as Beyond the Handlebars does,
    except in the narrow frame (its body has no room on the left)."""
    pos = 'center'
    if isinstance(slot, tuple):
        slot, pos = slot
    if not a or not slot or not os.path.exists(os.path.join(F, slot + '.jpg')):
        return a
    pl, side, pos, shape, size = a
    if size != 'narrow' and i:
        side = 'left' if i % 2 else None
    return (slot, side, pos, shape, size)
ART_ACT = None    # the activation's two panels need the full width


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


DIAL = '''<svg viewBox="0 0 320 158" role="img" aria-label="A round speedometer with one needle, tick marks and a mileage window" style="width:100%;height:168px;display:block;background:var(--void);border-radius:14px;margin-bottom:12px">
            <circle cx="160" cy="79" r="62" fill="none" style="stroke:var(--text)" stroke-width="4"/>
            <path d="M113 110l6-5m-12-28h9m5-35 6 7m33-25v10m35 7-6 8m23 27h-10m-3 33-7-5" fill="none" style="stroke:var(--text)" stroke-width="4"/>
            <path d="M160 79l-28-30" style="stroke:var(--accent-bright)" stroke-width="5" stroke-linecap="round"/>
            <circle cx="160" cy="79" r="6" style="fill:var(--text)"/>
            <text x="160" y="104" text-anchor="middle" style="fill:var(--text)" font-family="DM Mono, monospace" font-size="10">MPH</text>
            <text x="160" y="123" text-anchor="middle" style="fill:var(--text)" font-family="DM Mono, monospace" font-size="13">003148</text>
          </svg>'''
SCREEN = '''<svg viewBox="0 0 320 158" role="img" aria-label="A digital display showing speed, a turn arrow, the distance to the turn and the riding mode" style="width:100%;height:168px;display:block;background:var(--void);border-radius:14px;margin-bottom:12px">
            <rect x="24" y="22" width="272" height="114" rx="12" style="fill:var(--text)"/>
            <g style="fill:var(--void)" font-family="DM Mono, monospace">
              <text x="43" y="87" font-size="52">24</text><text x="46" y="111" font-size="13">MPH</text>
              <text x="204" y="70" font-size="40">↱</text><text x="188" y="99" font-size="13">200 YD</text>
              <text x="188" y="119" font-size="11">RAIN MODE</text>
            </g>
          </svg>'''
DASH_SLIDE = '''
    <section class="slide" data-type="discuss">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="eL">Look closer</div>
        <h2 class="slide-title" data-i18n="lT">Which dashboard?</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1fr 1fr;gap:22px">
          <div class="card" style="padding:18px 22px">
          %s
            <p class="prose"><strong data-i18n="lA">A · The dial</strong></p>
            <p class="prose" style="font-size:17.5px;margin-top:4px" data-i18n="lAd">A needle, a ring of numbers, a little window for the mileage.</p>
          </div>
          <div class="card" style="padding:18px 22px">
          %s
            <p class="prose"><strong data-i18n="lB">B · The screen</strong></p>
            <p class="prose" style="font-size:17.5px;margin-top:4px" data-i18n="lBd">Your speed, the next turn and the riding mode on one display.</p>
          </div>
        </div>
        <p class="prose" style="margin-top:16px;font-size:18px" data-i18n="lTask">x</p>
      </div>
    </section>
''' % (DIAL, SCREEN)

P1 = ('In 1946, a scooter offered Italians a practical way to get moving again. Today a Vespa parked outside a café '
      'can look like a carefully chosen accessory. The curious thing is that the shape hardly needs to change for the '
      'meaning to change completely.')
P2 = ('Writing in British GQ in 2023, Charlie Thomas saw a similar appeal in smaller motorcycles. Take Royal Enfield’s '
      'Meteor. A modest engine and straightforward controls sound like an odd recipe for excitement. Yet a rider might '
      'remember the beat of that engine long after forgetting what the speedometer said. For Thomas, part of the '
      'attraction lies in how the bike feels.')
P3 = ('Imagine two people looking at the same round dial in a showroom. One remembers her father’s bike. The other has '
      'never ridden and is relieved to see just one thing to read. Both ask for a test ride. The dealer calls that a '
      'victory for nostalgia. He might want to ask the second customer first.')


def reading(ek, paras, note_key):
    body = '\n          '.join('<p class="prose" style="font-size:19.5px;line-height:1.58%s">%s</p>'
                               % (';margin-top:12px' if i else '', p) for i, p in enumerate(paras))
    return '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">x</div>
        <h2 class="slide-title" data-i18n="rT">Who gets to call it cool?</h2>
      </div></div>
      <div class="slide-body">
        <div class="card" style="padding:24px 30px">
          %s
          <p class="prose dim" style="margin-top:14px;font-size:15.5px" data-i18n="%s">x</p>
        </div>
      </div>
    </section>
''' % (ek, body, note_key)


CLAIM_SLIDE = '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="eC">Test a claim</div>
        <h2 class="slide-title" data-i18n="cT">Can sales tell us why?</h2>
      </div></div>
      <div class="slide-body">
        <div class="card" style="padding:18px 24px">
          <p class="prose"><strong data-i18n="cF">The figures</strong></p>
          <p class="prose" style="margin-top:6px;font-size:19px">From January to July 2022, the Royal Enfield Meteor 350 was the UK’s best-selling motorbike over 125cc — six bikes ahead of BMW’s big adventure bike.</p>
        </div>
        <div class="card" style="padding:18px 24px;margin-top:14px">
          <p class="prose"><strong data-i18n="cM">The showroom manager</strong></p>
          <p class="prose ex" style="margin-top:6px;font-size:21px">“That <strong>proves</strong> riders are tired of complicated bikes.”</p>
        </div>
        <p class="prose" style="margin-top:14px;font-size:18px" data-i18n="cTask">x</p>
        <p class="prose dim" style="margin-top:8px;font-size:14.5px" data-i18n="cSrc">x</p>
      </div>
    </section>
'''

READ = [
    q('Paragraph one: what changed about the Vespa between 1946 and today?',
      ['What it says about its owner: a style choice, not just transport',
       'Its shape: the designers made it rounder and more stylish',
       'Its price: it became a luxury that few people could afford',
       'Its use: people stopped riding it and just park it outside cafés'], 1),
    q('Which detail in paragraph two is something you could hear or feel?',
      ['the beat of the engine', 'a modest engine', 'straightforward controls', 'the speed on the dial'], 2),
    q('Why might a list of specifications have less effect on a reader than that detail?',
      ['Figures describe the bike; a sensation lets you imagine riding it',
       'Readers of a men’s magazine do not understand technical words',
       'Specifications change every year, so they are soon out of date',
       'A list takes up much more space on a page than a description'], 3),
    q('What does the dealer assume about the two customers?',
      ['That they both want the dial for the same reason: nostalgia',
       'That neither of them is really going to buy a motorbike',
       'That the second customer has more experience than the first',
       'That they both prefer the screen but are too polite to say'], 4),
    q('Why should the dealer ask the second customer first?',
      ['She has no memories of old bikes: she likes the dial because it is simple',
       'She is clearly the customer with more money to spend in the showroom today',
       'She has ridden far more bikes than the first customer and knows dials well',
       'She has already decided to buy the other bike, the one with the big screen'], 5),
]
FORM = [
    q('Which sentence is correct?',
      ['The leather seat grew on me.', 'I grew on the leather seat.', 'The leather seat grew me on.',
       'The leather seat was growing me.'], 6),
    q('I was sure I wanted the screen, but the test ride ____.',
      ['won me over', 'won over me', 'won me', 'won on me'], 7),
    q('The round headlamp harks back ____ the bikes of the 1950s.', ['to', 'on', 'at', 'from'], 8),
    q('Built-in navigation is useful, but it comes at a price: ____',
      ['the screen is hard to read in bright sunshine.', 'it is the feature that most new riders ask for.',
       'it helps riders find their way in a new city.', 'it is included free on every model this year.'], 9),
]
CLAIM = [
    q('What can the sales figures on their own actually show?',
      ['Which bike sold the most in those seven months', 'Why buyers chose the Meteor and not the BMW',
       'That riders are tired of complicated bikes', 'Which bike its owners enjoy riding the most'], 10),
    q('The Meteor was six bikes ahead after seven months. Why is that a reason to be careful?',
      ['A lead that small could vanish with a few sales', 'It proves that the BMW is really the better bike',
       'It means the figures must have been added up wrongly', 'It shows that most riders bought both of the bikes'], 11),
    q('Which fact, if true, would weaken the manager’s explanation most?',
      ['Most Meteor buyers say they chose it for its low price', 'The Meteor has a round dial and very simple controls',
       'Sales of motorbikes over 125cc rose during 2022', 'The BMW is a large and complicated adventure bike'], 12),
]
HEDGE = [
    q('Which sentence says what the figures support — no more, no less?',
      ['The ranking is consistent with a preference for simpler bikes.',
       'The ranking proves that riders now prefer simpler, less complicated bikes.',
       'The ranking shows exactly why so many riders are buying simpler bikes.',
       'The ranking tells us nothing at all about whether simpler bikes appeal.'], 13),
    q('A lower price ____ the ranking too.',
      ['may partly explain', 'may partly explains', 'may be partly explain', 'partly may explaining'], 14),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'What old-fashioned thing has become cool again?',
        'Do you own anything that is older than you are?',
        'Would you rather ride a classic bike or a brand-new one?',
        'Why do people pay more for things that look old?',
        'Which design from your parents’ time do you like?',
        'Is there anything new that you just can’t get used to?',
    ], 'talk', 3),
    ('raw', DASH_SLIDE),
    ('raw', reading('eR1', [P1], 'rPredict'), 'a'),
    ('raw', reading('eR2', [P2, P3], 'rNote')),
    ('mc', 'e1', 'mcT1', READ, 'a', 'left'),
    ('rules', 'eP', 'pT1', [
        ('grow on someone', ['pg1', 'pg2'], 'The square headlight <strong>grew on me</strong> after a couple of weeks.'),
        ('win someone over', ['pw1', 'pw2'], 'Then I heard the engine. That sound <strong>won me over</strong>.'),
    ], None),
    ('rules', 'eP', 'pT2', [
        ('hark back to something', ['ph1', 'ph2'], 'The cream paint <strong>harks back to</strong> the scooters of the sixties.'),
        ('come at a price', ['pc1', 'pc2'], 'That clean display <strong>comes at a price</strong>: the mileage is hidden in a menu.'),
    ], None),
    ('mc', 'e2', 'mcT2', FORM, 'b', None),
    ('gap', 'e2', 'gT', 'gHint', [
        ('With its cream paint and curved lettering, the scooter ______ the ones in my grandfather’s photos.',
         ['harks back to'], 'gw1'),
        ('I disliked the square headlight at first, but it ______ me after a couple of weeks.',
         ['grew on|had grown on'], 'gw2'),
    ], ['come at a price', 'win … over', 'hark back to', 'grow on']),
    # Split in two: four rows each grow an explanation once answered, and
    # together they ran 148px off the canvas in en/de/es.
    ('gap', 'e2', 'gT', 'gHint', [
        ('That beautifully clean display ______: to see the mileage, you have to open a menu.',
         ['comes at a price'], 'gw3'),
        ('I was ready to walk away. Then I heard the engine, and the sound instantly ______ me ______.',
         ['won', 'over'], 'gw4'),
    ], ['come at a price', 'win … over', 'hark back to', 'grow on']),
    ('talk', 'eM', 'tk2T', [
        'Tell your partner about something that <strong>grew on</strong> you.',
        'What finally <strong>won</strong> you <strong>over</strong>?',
        'Describe a design that <strong>harks back to</strong> another era.',
        'Does its appeal <strong>come at a price</strong>?',
        'You are the dealer: what would you ask the second customer? Partner: answer as her.',
        'Dial or screen: which would <strong>win</strong> your parents <strong>over</strong>?',
    ], None, 3),
    ('raw', CLAIM_SLIDE, 'c'),
    ('mc', 'eC', 'mcT3', CLAIM, 'c', 'left'),
    ('rules', 'eH', 'hT', [
        ('is consistent with', ['hc1', 'hc2'], 'The ranking <strong>is consistent with</strong> a preference for simpler bikes.'),
        ('may partly explain', ['hp1', 'hp2'], 'A low price <strong>may partly explain</strong> the ranking too.'),
        ('proves', ['hx1', 'hx2'], 'That <strong>proves</strong> riders are tired of complicated bikes. ✗'),
    ], None),
    ('mc', 'eH', 'mcT4', HEDGE, None, None),
    ('gap', 'eH', 'g2T', 'g2Hint', [
        ('The figures are consistent ______ a preference for simpler bikes.', ['with'], 'hw1'),
        ('A lower price ______ partly explain the ranking.', ['may|might|could'], 'hw2'),
        ('Six bikes is a narrow lead, so the figures do not ______ that riders are tired of complicated bikes.',
         ['prove|show'], 'hw3'),
    ]),
    ('talk', 'eT', 'tk3T', [
        'Which object from your childhood deserves a comeback?',
        'What design <strong>harks back to</strong> another era — and works?',
        'Which modern feature <strong>comes at a price</strong>?',
        'What would <strong>win</strong> you <strong>over</strong> to an old-fashioned phone?',
        'Has a new technology <strong>grown on</strong> you? Which one?',
        'A product sells well. What else <strong>may partly explain</strong> it, apart from quality?',
    ], None, 3),
]
# The activation strip shares .bank-chip with the gap bank, so the BANK gate
# reads it too: COMES AT A PRICE before HARKS BACK TO, against gap order.
SPEC['chips'] = ['comes at a price', 'may partly explain', 'won me over', 'harks back to', 'is consistent with',
                 'grew on me']

W = {
    'en': [
        'The shape hardly changed; the MEANING did: from a practical way to get moving to a carefully chosen accessory.',
        'THE BEAT of the engine is something you hear and feel. The other three are facts about the bike.',
        'Figures describe a machine. A sensation puts the reader on the seat, which is why the writer chose it.',
        'He calls it “a victory for nostalgia”: he assumes both of them are remembering old bikes.',
        'She has never ridden and is relieved to see one thing to read. She wants SIMPLICITY, not memories.',
        'The thing you come to like is the subject: IT GREW ON ME.',
        'WIN OVER separates, and a pronoun goes in the middle: WON ME OVER.',
        'HARK BACK TO + a noun: the 1950s, the scooters of the sixties.',
        'COMES AT A PRICE needs the disadvantage after it: the screen is hard to read in sunshine.',
        'A sales table counts bikes. It cannot tell you WHY anyone bought one.',
        'Six bikes in seven months is a tiny margin: a few sales either way would change the ranking.',
        'If buyers chose it for the PRICE, the ranking says little about complicated bikes.',
        'IS CONSISTENT WITH: the figures fit the idea without proving it. PROVES and SHOWS EXACTLY WHY claim too much; NOTHING AT ALL claims too little.',
        'MAY + the bare verb: MAY PARTLY EXPLAIN. No -s after a modal.',
    ],
    'de': [
        'Die Form hat sich kaum geändert, die BEDEUTUNG schon: vom praktischen Fortbewegungsmittel zum sorgfältig gewählten Accessoire.',
        'THE BEAT, der Takt des Motors, ist etwas, das man hört und spürt. Die anderen drei sind Fakten über das Motorrad.',
        'Zahlen beschreiben eine Maschine. Eine Sinneswahrnehmung setzt den Leser in den Sattel; deshalb hat der Autor sie gewählt.',
        'Er nennt es „einen Sieg der Nostalgie“: Er nimmt an, dass beide an alte Motorräder denken.',
        'Sie ist noch nie gefahren und ist erleichtert, nur eine Anzeige lesen zu müssen. Sie will EINFACHHEIT, keine Erinnerungen.',
        'Das, was man allmählich mag, ist das Subjekt: IT GREW ON ME.',
        'WIN OVER ist trennbar, und ein Pronomen steht in der Mitte: WON ME OVER.',
        'HARK BACK TO + Nomen: the 1950s, the scooters of the sixties.',
        'Nach COMES AT A PRICE folgt der Nachteil: Der Bildschirm ist in der Sonne schwer zu lesen.',
        'Eine Verkaufstabelle zählt Motorräder. Sie kann nicht sagen, WARUM jemand eines gekauft hat.',
        'Sechs Motorräder in sieben Monaten sind ein winziger Vorsprung: Ein paar Verkäufe mehr oder weniger, und die Rangliste ist anders.',
        'Wenn die Käufer es wegen des PREISES gewählt haben, sagt die Rangliste wenig über komplizierte Motorräder.',
        'IS CONSISTENT WITH: Die Zahlen passen zur Idee, ohne sie zu beweisen. PROVES und SHOWS EXACTLY WHY behaupten zu viel, NOTHING AT ALL zu wenig.',
        'MAY + Grundform: MAY PARTLY EXPLAIN. Nach einem Modalverb kein -s.',
    ],
    'es': [
        'La forma apenas cambió; el SIGNIFICADO sí: de un medio práctico para moverse a un accesorio elegido con cuidado.',
        'THE BEAT, el ritmo del motor, es algo que se oye y se siente. Los otros tres son datos sobre la moto.',
        'Las cifras describen una máquina. Una sensación pone al lector en el asiento; por eso la eligió el autor.',
        'Lo llama «una victoria de la nostalgia»: da por hecho que los dos recuerdan motos antiguas.',
        'Nunca ha conducido una moto y le alivia ver una sola cosa que leer. Quiere SENCILLEZ, no recuerdos.',
        'Lo que acaba gustándote es el sujeto: IT GREW ON ME.',
        'WIN OVER es separable, y el pronombre va en medio: WON ME OVER.',
        'HARK BACK TO + sustantivo: the 1950s, the scooters of the sixties.',
        'Después de COMES AT A PRICE va la desventaja: la pantalla se lee mal al sol.',
        'Una tabla de ventas cuenta motos. No puede decir POR QUÉ alguien compró una.',
        'Seis motos en siete meses es un margen mínimo: unas pocas ventas más o menos cambiarían la clasificación.',
        'Si los compradores la eligieron por el PRECIO, la clasificación dice poco sobre las motos complicadas.',
        'IS CONSISTENT WITH: las cifras encajan con la idea sin demostrarla. PROVES y SHOWS EXACTLY WHY afirman demasiado; NOTHING AT ALL, demasiado poco.',
        'MAY + infinitivo sin TO: MAY PARTLY EXPLAIN. Sin -s después de un modal.',
    ],
}

GW = {
    'en': dict(
        gw1='HARKS BACK TO: one scooter, so the -s.',
        gw2='IT GREW ON ME: the headlight is the subject; past simple.',
        gw3='COMES AT A PRICE: the clean look costs you the mileage.',
        gw4='WON ME OVER: the pronoun goes in the middle.',
        hw1='CONSISTENT WITH.',
        hw2='A modal: MAY (or MIGHT, COULD) PARTLY EXPLAIN.',
        hw3='Sales figures cannot PROVE a reason.',
    ),
    'de': dict(
        gw1='HARKS BACK TO: ein Roller, also das -s.',
        gw2='IT GREW ON ME: Der Scheinwerfer ist das Subjekt; Past Simple.',
        gw3='COMES AT A PRICE: Das klare Design kostet dich die Kilometeranzeige.',
        gw4='WON ME OVER: Das Pronomen steht in der Mitte.',
        hw1='CONSISTENT WITH.',
        hw2='Ein Modalverb: MAY (oder MIGHT, COULD) PARTLY EXPLAIN.',
        hw3='Verkaufszahlen können keinen Grund BEWEISEN (PROVE).',
    ),
    'es': dict(
        gw1='HARKS BACK TO: una sola moto, así que lleva -s.',
        gw2='IT GREW ON ME: el faro es el sujeto; past simple.',
        gw3='COMES AT A PRICE: el diseño limpio te cuesta el cuentakilómetros.',
        gw4='WON ME OVER: el pronombre va en medio.',
        hw1='CONSISTENT WITH.',
        hw2='Un modal: MAY (o MIGHT, COULD) PARTLY EXPLAIN.',
        hw3='Las cifras de ventas no pueden DEMOSTRAR (PROVE) un motivo.',
    ),
}

GQ = ('<a href="https://www.gq-magazine.co.uk/cars/article/how-motorbikes-found-their-cool-again-2023" '
      'target="_blank" rel="noopener" style="color:var(--accent-bright);text-decoration:underline;text-underline-offset:2px">%s ↗</a>')
BB = ('<a href="https://www.bennetts.co.uk/bikesocial/news-and-views/news/2022/august/best-selling-bikes-2022" '
      'target="_blank" rel="noopener" style="color:var(--accent-bright);text-decoration:underline;text-underline-offset:2px">Bennetts BikeSocial</a>')

T = {
    'en': dict(
        coverTitle='The <br><em>comeback ride</em>',
        coverSub='Old shapes, new riders, and the words for changing your mind.',
        chipLevel='B2–C1', chipFocus='phrases for taste · careful claims', chipCount='30 slides',
        eW='Warm-up', tk1T='Let’s talk!',
        eL='Look closer', lT='Which dashboard?',
        lA='A · The dial', lAd='A needle, a ring of numbers, a little window for the mileage.',
        lB='B · The screen', lBd='Your speed, the next turn and the riding mode on one display.',
        lTask='<strong>In pairs.</strong> You have one second to glance down at a red light. Choose one dashboard for a visitor in an unfamiliar city and one for yourself. Point to the detail that decides it. What would you miss if it disappeared?',
        eR1='Read for attitude', eR2='Read on', rT='Who gets to call it cool?',
        rPredict='Before you read on: what do you think the writer will praise about bikes like these? Tell your partner, then check on the next slide.',
        rNote='An original text written for this lesson, inspired by Charlie Thomas’s 2023 feature for British GQ. ' + GQ % 'Read the original',
        e1='Reading', mcT1='Read between the lines', mcT2='Say it right', mcT3='What do the figures show?', mcT4='How sure can we be?',
        eP='Language in use', pT1='Changing your mind', pT2='Looking back, paying for it',
        pg1='You did not like it at first; slowly, you start to like it.',
        pg2='The THING is the subject: IT GREW ON ME. Never “I grew on it”.',
        pw1='Something persuades you to like it or agree with it, often after doubts.',
        pw2='A pronoun goes in the middle: IT WON ME OVER, not “won over me”.',
        ph1='It reminds you of, or copies the style of, an earlier time.',
        ph2='A little formal; + a noun: it HARKS BACK TO the 1960s.',
        pc1='Something good brings a disadvantage with it.',
        pc2='The good thing is the subject: SIMPLICITY COMES AT A PRICE.',
        e2='Using the phrases', gT='Complete the reviews',
        gHint='Type the phrase in the right form. Use each one once.',
        eM='Make it yours', tk2T='Your turn: use the phrases',
        eC='Test a claim', cT='Can sales tell us why?', cF='The figures', cM='The showroom manager',
        cTask='What can the figures really tell us? Think of two other explanations for the ranking, then make the manager’s claim more careful.',
        cSrc='Figures: UK registrations, as reported by ' + BB + ', August 2022.',
        eH='Careful claims', hT='Say what the data shows',
        hc1='The data fits the idea, but other ideas could fit it too.',
        hc2='It does not say the idea is true.',
        hp1='One possible cause among several, and you are not sure.',
        hp2='Two ways of being careful in one phrase: MAY and PARTLY.',
        hx1='Only for something the data settles completely.',
        hx2='Sales figures almost never prove a reason.',
        g2T='Make it careful', g2Hint='One word in each gap.',
        eT='What deserves a comeback?', tk3T='Bring something back',
        actTitle='You get one prototype', actUse='Use at least four:',
        actSpeakBrief='In pairs: a small manufacturer can build one city bike for first-time riders. Choose a dashboard and agree on one extra feature.',
        actSpeak1='Design lead: bring one detail from an older machine into the design, and say what it does for the rider.',
        actSpeak2='First-time rider: describe one awkward moment on your new commute and ask how the design helps. Halfway through, swap roles.',
        actSpeak3='Give a 45-second pitch: rider, dashboard, feature, trade-off. Then answer: how would you find out if riders actually want it?',
        actWriteKind='Writing',
        actWriteBrief='Exit ticket (80–100 words): choose an object from your own life that deserves a comeback. Say what it HARKS BACK TO, who it might WIN OVER, whether its charm COMES AT A PRICE, and one reason your prediction could be wrong.',
        actPlaceholder='The object I would bring back is …',
    ),
    'de': dict(
        coverTitle='The <br><em>comeback ride</em>',
        coverSub='Alte Formen, neue Fahrer – und wie man seine Meinung ändert.',
        chipLevel='B2–C1', chipFocus='Geschmack · vorsichtige Aussagen', chipCount='30 Folien',
        eW='Zum Einstieg', tk1T='Sprechen wir!',
        eL='Genau hinsehen', lT='Welches Cockpit?',
        lA='A · Der Rundtacho', lAd='Eine Nadel, ein Zahlenkranz, ein kleines Fenster für den Kilometerstand.',
        lB='B · Das Display', lBd='Geschwindigkeit, nächste Abbiegung und Fahrmodus auf einem Bildschirm.',
        lTask='<strong>Zu zweit.</strong> An der roten Ampel hast du eine Sekunde für einen Blick nach unten. Wählt ein Cockpit für jemanden, der eine fremde Stadt besucht, und eines für euch selbst. Zeigt auf das Detail, das entscheidet. Was würdet ihr vermissen, wenn es fehlte?',
        eR1='Lesen: die Haltung', eR2='Weiterlesen', rT='Wer darf sagen, was cool ist?',
        rPredict='Bevor du weiterliest: Was wird der Autor an solchen Motorrädern loben? Sag es deinem Partner und prüfe es auf der nächsten Folie.',
        rNote='Ein eigener Text für diese Lektion, angeregt durch Charlie Thomas’ Artikel von 2023 in der britischen GQ. ' + GQ % 'Zum Original',
        e1='Lesen', mcT1='Zwischen den Zeilen lesen', mcT2='Richtig gesagt', mcT3='Was zeigen die Zahlen?', mcT4='Wie sicher können wir sein?',
        eP='Sprache im Einsatz', pT1='Seine Meinung ändern', pT2='Zurückblicken, dafür bezahlen',
        pg1='Zuerst mochtest du es nicht; nach und nach gefällt es dir.',
        pg2='Die SACHE ist das Subjekt: IT GREW ON ME. Nie „I grew on it“.',
        pw1='Etwas überzeugt dich, oft nach anfänglichen Zweifeln.',
        pw2='Ein Pronomen steht in der Mitte: IT WON ME OVER, nicht „won over me“.',
        ph1='Es erinnert an eine frühere Zeit oder greift ihren Stil auf.',
        ph2='Etwas gehoben; + Nomen: it HARKS BACK TO the 1960s.',
        pc1='Etwas Gutes bringt einen Nachteil mit sich.',
        pc2='Das Gute ist das Subjekt: SIMPLICITY COMES AT A PRICE.',
        e2='Die Wendungen anwenden', gT='Vervollständige die Bewertungen',
        gHint='Schreib die Wendung in der richtigen Form. Jede nur einmal.',
        eM='Mach es zu deinem', tk2T='Jetzt du: nutze die Wendungen',
        eC='Eine Behauptung prüfen', cT='Verraten Verkaufszahlen das Warum?', cF='Die Zahlen', cM='Der Filialleiter',
        cTask='Was sagen die Zahlen wirklich? Findet zwei andere Erklärungen für die Rangliste und formuliert die Aussage des Filialleiters vorsichtiger.',
        cSrc='Zahlen: Neuzulassungen in Großbritannien, laut ' + BB + ', August 2022.',
        eH='Vorsichtige Aussagen', hT='Sag, was die Daten zeigen',
        hc1='Die Daten passen zur Idee, aber auch andere Ideen könnten passen.',
        hc2='Es sagt nicht, dass die Idee stimmt.',
        hp1='Eine mögliche Ursache unter mehreren, und du bist nicht sicher.',
        hp2='Zwei Arten, vorsichtig zu sein, in einer Wendung: MAY und PARTLY.',
        hx1='Nur für etwas, das die Daten vollständig klären.',
        hx2='Verkaufszahlen beweisen fast nie einen Grund.',
        g2T='Mach es vorsichtig', g2Hint='Ein Wort pro Lücke.',
        eT='Was verdient ein Comeback?', tk3T='Hol etwas zurück',
        actTitle='Ihr bekommt einen Prototyp', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit: Ein kleiner Hersteller kann ein Stadtmotorrad für Fahranfänger bauen. Wählt ein Cockpit und einigt euch auf ein zusätzliches Extra.',
        actSpeak1='Designchef: Übernimm ein Detail von einer älteren Maschine und sag, was es für den Fahrer leistet.',
        actSpeak2='Fahranfänger: Beschreib einen schwierigen Moment auf deinem neuen Arbeitsweg und frag, wie das Design hilft. Nach der Hälfte tauscht ihr die Rollen.',
        actSpeak3='Haltet einen 45-Sekunden-Pitch: Fahrer, Cockpit, Extra, Kompromiss. Dann beantwortet: Wie würdet ihr herausfinden, ob Fahrer es wirklich wollen?',
        actWriteKind='Schreiben',
        actWriteBrief='Exit Ticket (80–100 Wörter): Welcher Gegenstand aus deinem Leben verdient ein Comeback? Woran erinnert er, wen überzeugt er, was kostet sein Charme? Und warum könntest du dich irren?',
        actPlaceholder='The object I would bring back is …',
    ),
    'es': dict(
        coverTitle='The <br><em>comeback ride</em>',
        coverSub='Formas clásicas, moteros nuevos y cambios de opinión.',
        chipLevel='B2–C1', chipFocus='gustos · afirmaciones prudentes', chipCount='30 diapositivas',
        eW='Para empezar', tk1T='¡A conversar!',
        eL='Mira con atención', lT='¿Qué tablero?',
        lA='A · La esfera', lAd='Una aguja, un anillo de números, una ventanita para los kilómetros.',
        lB='B · La pantalla', lBd='Tu velocidad, el próximo giro y el modo de conducción en una sola pantalla.',
        lTask='<strong>En parejas.</strong> En un semáforo en rojo tienes un segundo para mirar hacia abajo. Elijan un tablero para alguien que visita una ciudad desconocida y otro para ustedes. Señalen el detalle que lo decide. ¿Qué echarían de menos si desapareciera?',
        eR1='Leer la actitud', eR2='Sigue leyendo', rT='¿Quién decide qué es cool?',
        rPredict='Antes de seguir: ¿qué crees que va a elogiar el autor de motos como estas? Díselo a tu compañero y compruébalo en la siguiente diapositiva.',
        rNote='Un texto original escrito para esta lección, inspirado en el artículo de Charlie Thomas de 2023 para la GQ británica. ' + GQ % 'Leer el original',
        e1='Lectura', mcT1='Leer entre líneas', mcT2='Dilo bien', mcT3='¿Qué muestran las cifras?', mcT4='¿Qué tan seguros podemos estar?',
        eP='La lengua en uso', pT1='Cambiar de opinión', pT2='Mirar atrás, pagar el precio',
        pg1='Al principio no te gustaba; poco a poco empieza a gustarte.',
        pg2='La COSA es el sujeto: IT GREW ON ME. Nunca «I grew on it».',
        pw1='Algo te convence, a menudo después de tener dudas.',
        pw2='El pronombre va en medio: IT WON ME OVER, no «won over me».',
        ph1='Recuerda a una época anterior o copia su estilo.',
        ph2='Algo formal; + sustantivo: it HARKS BACK TO the 1960s.',
        pc1='Algo bueno trae consigo una desventaja.',
        pc2='Lo bueno es el sujeto: SIMPLICITY COMES AT A PRICE.',
        e2='Usar las expresiones', gT='Completa las reseñas',
        gHint='Escribe la expresión en la forma correcta. Usa cada una una vez.',
        eM='Hazlo tuyo', tk2T='Te toca: usa las expresiones',
        eC='Poner a prueba una afirmación', cT='¿Nos dicen las ventas por qué?', cF='Las cifras', cM='El gerente del concesionario',
        cTask='¿Qué nos dicen de verdad las cifras? Piensen en otras dos explicaciones para la clasificación y luego hagan más prudente la afirmación del gerente.',
        cSrc='Cifras: matriculaciones en el Reino Unido, según ' + BB + ', agosto de 2022.',
        eH='Afirmaciones prudentes', hT='Di lo que muestran los datos',
        hc1='Los datos encajan con la idea, pero otras ideas también podrían encajar.',
        hc2='No dice que la idea sea cierta.',
        hp1='Una causa posible entre varias, y no estás seguro.',
        hp2='Dos formas de ser prudente en una expresión: MAY y PARTLY.',
        hx1='Solo para algo que los datos resuelven por completo.',
        hx2='Las cifras de ventas casi nunca demuestran un motivo.',
        g2T='Hazlo prudente', g2Hint='Una palabra en cada hueco.',
        eT='¿Qué merece volver?', tk3T='Recupera algo',
        actTitle='Tienen un solo prototipo', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas: un pequeño fabricante puede construir una moto urbana para principiantes. Elijan un tablero y acuerden un extra.',
        actSpeak1='Jefe de diseño: trae un detalle de una máquina antigua al diseño y explica qué aporta al conductor.',
        actSpeak2='Principiante: describe un momento incómodo en tu nuevo trayecto al trabajo y pregunta cómo ayuda el diseño. A mitad, cambien de papel.',
        actSpeak3='Hagan una presentación de 45 segundos: conductor, tablero, extra, compromiso. Luego respondan: ¿cómo averiguarían si los conductores lo quieren de verdad?',
        actWriteKind='Escritura',
        actWriteBrief='Ticket de salida (80–100 palabras): ¿qué objeto de tu vida merece volver? ¿A qué recuerda, a quién convencería, qué precio tiene su encanto? ¿Y por qué podrías equivocarte?',
        actPlaceholder='The object I would bring back is …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w
    T[c].update(GW[c])

H.check_keys(T)

# The hand-built slides carry their English from T, one copy of each string.
_fill = lambda h: re.sub(r'data-i18n="(\w+)">[^<]*<', lambda m: 'data-i18n="%s">%s<' % (m.group(1), T['en'][m.group(1)]), h)
SPEC['flow'] = [(st[0], _fill(st[1])) + tuple(st[2:]) if st[0] == 'raw' else st for st in SPEC['flow']]

import importlib.util  # noqa: E402

import deck as D  # noqa: E402

TPL = 'lesson-template/lesson-template.html'
F = SPEC['folder']
LANGS = ('en', 'de', 'es')
os.makedirs(os.path.join('incoming', 'comeback-ride-mj'), exist_ok=True)


def frame(html, a):
    """Give a slide its framed picture (§15), or none. a = (plate, side, pos,
    shape, size) from ART. Any data-bg the slide builder wrote is replaced."""
    html = re.sub(r' data-bg="[^"]*"', '', html, count=1)
    if not a:
        return html
    pl, side, pos, shape, size = a
    assert os.path.exists(os.path.join(F, pl + '.jpg')), pl
    attrs = ' data-bg="%s/%s.jpg"' % (F, pl)
    if side == 'left':
        attrs += ' data-art-side="left"'
    if pos:
        attrs += ' data-art-pos="%s"' % pos
    if shape:
        attrs += ' data-art="%s"' % shape
    if size:
        attrs += ' data-art-size="%s"' % size
    return re.sub(r'<section class="slide( is-active)?"', lambda m: m.group(0) + attrs, html, count=1)


def talk(ek, tk, prompts, cols):
    """Speaking prompts as cards: two columns beside a picture, three without."""
    E = T['en']
    cells = '\n          '.join('<div class="card" style="padding:16px 20px;display:flex;align-items:center">'
                               '<p class="prose" style="font-size:19px;line-height:1.42">%s</p></div>' % p
                               for p in prompts)
    return '''
    <section class="slide" data-type="discuss">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:%s;gap:14px">
          %s
        </div>
      </div>
    </section>
''' % (ek, E[ek], tk, E[tk], ' '.join(['1fr'] * cols), cells)


# The cover. The café racer stands across .41-.94 of the hero's width, so the
# editorial default (a text column capped at 58% under a scrim that is opaque
# to 38% and clears at 68%) put the subtitle on the back wheel and fogged the
# rear half of the bike. Here the column stops at 30.5% (right edge 454px; the
# café chair starts at 470px, the bike at 525px) and the scrim clears by 41%:
# the type sits on the empty sky and sea only. The subtitle is one short line,
# as on Beyond the Handlebars, which is what lets the column be this narrow.
EXTRA_CSS = '''
/* The Comeback Ride: keep the cover type off the café racer (see builder). */
html[data-style="editorial"]:not(.is-flow) .cover-inner { max-width: 30.5%; }
html[data-style="editorial"]:not(.is-flow) .cover-title { font-size: 72px; }
html[data-style="editorial"]:not(.is-flow) .cover-sub { font-size: 21px; line-height: 1.35; }
/* Level and count share a row; the long focus chip takes the second. */
/* Answered, a four-option question grows its explanation: the editorial
   bars at 16px padding ran 16-72px off the canvas beside a picture. */
html[data-style="editorial"] .opts { gap: 8px; }
html[data-style="editorial"] .opt { padding-top: 10px; padding-bottom: 10px; }
html[data-style="editorial"]:not(.is-flow) .stage.on-cover .bg-layer::after {
  background: linear-gradient(90deg,
    color-mix(in srgb, var(--void) 94%, transparent) 0%,
    color-mix(in srgb, var(--void) 90%, transparent) 37%,
    transparent 41%);
}
/* Upright (a phone) the cover is a page: the type on the cream at the top,
   the café racer as a band along the bottom, above the deck bar, cropped to
   the bike (.27-.95 of the plate's width on a 390px phone). No scrim. */
html.is-flow[data-style="editorial"] .stage.on-cover .bg-layer::before {
  background: var(--hero) right 15% bottom 56px / auto 34svh no-repeat;
}
html.is-flow[data-style="editorial"] .stage.on-cover .bg-layer::after { content: none; }
/* the band's height is kept clear under the type, so on a short phone the
   cover scrolls rather than putting words on the bike */
html.is-flow[data-style="editorial"] .slide[data-type="cover"] .cover-inner {
  padding-bottom: calc(34svh + 16px);
}
'''


def build():
    E = T['en']
    assert len(ART) == len(SPEC['flow'])
    s = [D.cover(D.logo_from(TPL), E['coverTitle'], E['coverSub'],
                 [('Level', E['chipLevel']), ('Count', E['chipCount']), ('Focus', E['chipFocus'])])]
    dealt = 0
    for n_step, (step, a) in enumerate(zip(SPEC['flow'], ART)):
        kind = step[0]
        new = NEW.get(n_step)
        if kind != 'mc':
            a = pick(a, new)
        if kind == 'talk':
            s.append(frame(talk(step[1], step[2], step[3], 2 if a else 3), a))
        elif kind == 'raw':
            s.append(frame(step[1], a))
        elif kind == 'rules':
            _, ek, tk, cards, _slot = step
            built = [((pill, E[pill]) if pill in E else pill, [(b, E[b]) for b in bl], ex)
                     for pill, bl, ex in cards]
            s.append(frame(D.rules(ek, E[ek], tk, E[tk], built), a))
        elif kind == 'mc':
            _, ek, tk, items, _slot, _side = step
            items = [H._deal(it, dealt + i) for i, it in enumerate(items)]
            dealt += len(items)
            D.assert_no_key_is_longest(items, SPEC['out'])
            for i, it in enumerate(items, 1):
                ai = pick(a, new[i - 1], i) if new else a
                s.append(frame(D.mc(i, len(items), it, ek, E[ek], tk, E[tk]), ai))
        elif kind == 'gap':
            _, ek, tk, hk, rows = step[:5]
            bank = step[5] if len(step) > 5 else None
            if bank:
                D.assert_bank_is_not_a_key(bank, [a for _, ans, _ in rows for a in ans])
            s.append(frame(D.gap(1, 1, rows, bank, ek, E[ek], tk, E[tk],
                                 hint=E[hk], hint_key=hk, size=21), a))
        else:
            raise AssertionError(kind)
    s.append(frame(D.results(), pick(ART_RESULTS, NEW_RESULTS)))
    s.append(frame(D.activate(E['actTitle'], E['actUse'], SPEC['chips'], 'Speaking', E['actSpeakBrief'],
                              [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                              E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder']), ART_ACT))
    body = ''.join(s)
    n = body.count('<section class="slide')
    for c in LANGS:
        assert str(n) in T[c]['chipCount'], '%s chipCount %r, deck has %d' % (c, T[c]['chipCount'], n)
    out = D.assemble(TPL, SPEC['out'], body, D.editorial_palette('%s/hero.jpg' % F), SPEC['title'],
                     H._I18n(T, LANGS, False), langs=LANGS, style='editorial')
    assert out.count('\n</style>') >= 1
    out = out.replace('\n</style>', EXTRA_CSS + '</style>', 1)
    open(SPEC['out'], 'w', encoding='utf-8', newline='').write(out)
    print('wrote %s — %d slides, %d bytes' % (SPEC['out'], n, len(out)))


if __name__ == '__main__':
    build()
