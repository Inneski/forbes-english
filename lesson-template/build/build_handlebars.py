# -*- coding: utf-8 -*-
"""Beyond the Handlebars (B2/C1) — cycling vocabulary, collocation and inference.

Rebuilt from a standalone deck Innes supplied: a 14-slide saved-DOM page with
its own Arial/Georgia chrome, its 21 illustrations base64'd into the markup,
no language switcher, no activation stage and no SEO block. Everything
teachable in it is carried over. What changed, and why:

  * **Five multiple-choice items had the key as the conspicuously longest
    option** — reading Q1/Q2/Q3, vocabulary Q2 and idiom Q2. On reading Q1 the
    key ran 66 characters against distractors of 45 and 47, which is a free
    point for anyone who has never read the passage. The distractors are
    lengthened here (never the key shortened) and `assert_no_key_is_longest`
    runs over every bank at build time.

  * **The three idioms were a closed set asked three times as MCQ**, so on the
    item whose key was `an uphill struggle` the key was unavoidably five
    characters longer than the next option and no rewrite of the options could
    fix it — the options ARE the answer set. It is a gap-fill with a shared,
    alphabetised bank instead. Same three sentences, same three targets, and
    the bank order is not the gap order.

  * **The bicycle schematic carried a brand name** on the down tube and in its
    aria-label. This site does not ship another company's trademark on a
    teaching diagram; the `<text>` element is gone and the label describes what
    the drawing is. The drawing itself is unchanged and still editable.

  * **The teacher notes credited a competitor's lesson pages** and closed with
    "The lesson has not been published to forbesenglish.com." Both are gone.

  * The 12-type rider quiz was twelve rating questions that produced a
    personality label. The language value in it is the discussion question
    attached to each type, so it is an explore-grid: one click, one portrait,
    what that riding involves, and the question to answer aloud. All twelve
    types and all twelve questions survive; the scoring machinery does not.

Body and option weight is lifted to DM Sans 500 (EXTRA_CSS). The house type
SCALE is fixed by HOUSE-STYLE §6 and is untouched — the table pins sizes and
the display weights, and says nothing about the weight of 19–20px UI text.
Innes asked for bolder; this is the axis that was free.

Hero is the supplied coastal rider; palette is derived from it, dark theme,
every contrast row PASS.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'beyond-the-handlebars.html'
F = 'BeyondTheHandlebars'
BIKE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    'handlebars_bike.svgfrag')

# --plate is raised from the template's 0.68, and it is declared HERE because
# the palette block is injected above the template's derived properties in the
# same :root — a --plate set anywhere else loses on cascade order.
#
# Measured rather than chosen, per the template's own instruction. The busiest
# slide is the repair shop over `workshop-red-bike.jpg`; photographing the card
# surface with its text hidden and taking the brightest 2% of it gives:
#
#     plate   --text    --text-dim
#     0.68     8.00        4.13     <- the note line on every teach card, under AA
#     0.78    10.03        5.17
#     0.86    11.84        6.11     <- chosen
#     0.92    13.30        6.86
#
# These illustrations are flat vector art with large areas near white, which is
# exactly the case the template's comment says to raise the plate for. 0.86
# clears 4.5:1 on the dim note with margin and still lets the artwork read.
PALETTE = '''  --hero: url('%s/hero.jpg');

  --plate         : 0.86;
  --void          : #0b110c;
  --surface       : #141f16;
  --surface2      : #1b2c1f;
  --border        : #cd926f;
  --text          : #f5f3f2;
  --text-dim      : #bfaea3;
  --accent        : #f5c8ad;
  --accent-bright : #fdb387;
  --accent-dim    : #e69260;
  --secondary     : #b0cfda;
  --contrast      : #1dedd7;''' % F


# ── the twelve rider types ─────────────────────────────────────────────
# (name, family, portrait, what the riding involves, the question to answer)
RIDERS = [
    ('Commuter', 'Everyday / Urban', 'rider-commuter.jpg',
     'Daily travel to work or school, often with a backpack or panniers.',
     'What would persuade you to commute by bike more often?'),
    ('Fair-weather casual', 'Everyday / Urban', 'rider-fair-weather.jpg',
     'Relaxed rides on flat routes, sometimes on a cruiser or a shared bike.',
     'Does good weather make you more adventurous?'),
    ('Coffee cruiser', 'Everyday / Urban', 'rider-coffee-cruiser.jpg',
     'Social rides with time built in for coffee and conversation.',
     'Is the destination or the company more important?'),
    ('Errand runner', 'Everyday / Urban', 'rider-errand-runner.jpg',
     'Practical neighbourhood trips — shopping and everyday tasks.',
     'Which local car journey could you replace?'),
    ('Climber', 'Sport / Road', 'rider-climber.jpg',
     'Long ascents, a light bike and a high power-to-weight ratio.',
     'Would the view justify the effort?'),
    ('Sprinter', 'Sport / Road', 'rider-sprinter.jpg',
     'Powerful acceleration and short, fast finishes.',
     'Do you prefer brief intensity or sustained effort?'),
    ('Puncheur', 'Sport / Road', 'rider-puncheur.jpg',
     'Punchy climbs and repeated changes of pace on a rolling route.',
     'How would you pace yourself over several steep hills?'),
    ('Rouleur', 'Sport / Road', 'rider-rouleur.jpg',
     'Sustained speed and consistent effort over hours of flat road.',
     'What helps you stay focused during a long effort?'),
    ('Time trialist', 'Sport / Road', 'rider-time-trialist.jpg',
     'Aerodynamics, precise pacing and solo performance against the clock.',
     'Would measuring everything improve your enjoyment?'),
    ('Mountain biker', 'Off-road / Adventure', 'rider-mountain-biker.jpg',
     'Singletrack, technical descents, bike-handling skills and suspension.',
     'Which matters more on a technical trail: courage or control?'),
    ('Gravel rider', 'Off-road / Adventure', 'rider-gravel.jpg',
     'Mixed surfaces and quiet backroads on a drop-bar bike.',
     'Would you take an unfamiliar track without knowing where it leads?'),
    ('Bikepacker', 'Off-road / Adventure', 'rider-bikepacker.jpg',
     'Self-supported, multi-day travel with bags strapped to the bicycle.',
     'What would you sacrifice in order to travel lighter?'),
]

# ── the bicycle, as numbered hotspots ──────────────────────────────────
# (label, x%, y%, what it does, a sentence a learner can borrow)
PARTS = [
    ('Saddle', 31.8, 9.8, 'The seat that supports the rider.',
     'The saddle feels too far forward.'),
    ('Seatpost', 33.4, 20.0, 'The post connecting the saddle to the frame.',
     'The seatpost slides into the seat tube.'),
    ('Top tube', 50.5, 25.5,
     'The upper frame tube, running forward from the seat-tube area.',
     'The top tube slopes slightly.'),
    ('Down tube', 56.2, 46.0,
     'The main diagonal frame tube, running towards the bottom bracket.',
     'The brand name usually appears on the down tube.'),
    ('Seat tube', 38.6, 43.0,
     'The frame tube that receives the seatpost and reaches the crank area.',
     'The seat tube sets how upright you sit.'),
    ('Drop handlebars', 78.3, 27.7,
     'Curved handlebars offering several hand positions.',
     'She moved her hands onto the drops.'),
    ('Brake / shift lever', 83.1, 21.0,
     'A control that applies a brake and, on a road bike, changes gear.',
     'The brake lever feels different from usual.'),
    ('Stem', 69.9, 16.2,
     'The component connecting the handlebars to the fork steerer.',
     'The stem affects how far forward the bars sit.'),
    ('Fork', 74.3, 46.7,
     'The component holding the front wheel and linking it to the steering.',
     'The front wheel sits between the fork legs.'),
    ('Hub', 78.1, 60.5,
     'The central part of a wheel, around which the wheel rotates.',
     'The spokes connect the rim to the hub.'),
    ('Disc-brake rotor', 80.1, 56.3,
     'The metal disc attached to the hub that the brake pads act on.',
     'The rotor appears to rub against a brake pad.'),
    ('Tyre', 96.5, 65.0,
     'The rubber part around the wheel that contacts the ground.',
     'The rear tyre lost traction on the gravel.'),
    ('Rim', 92.7, 71.8,
     'The outer structural ring of the wheel, supporting the tyre.',
     'The mechanic inspected the rim for damage.'),
    ('Spokes', 12.5, 46.0,
     "The slender members connecting a wheel's hub to its rim.",
     'One of the spokes is loose.'),
    ('Cassette', 19.5, 57.0,
     'The cluster of sprockets fitted at the rear wheel.',
     'The mechanic checked the chain and cassette for wear.'),
    ('Rear derailleur', 18.5, 70.0,
     'The mechanism guiding the chain between rear sprockets and keeping it tense.',
     'The rear derailleur moves the chain across the cassette.'),
    ('Chain', 30.3, 77.1,
     'The linked metal loop transmitting power to the rear sprocket.',
     'The chain seems to slip under load.'),
    ('Chainrings', 44.3, 69.0,
     'The toothed rings at the front of the drivetrain, turned by the cranks.',
     'She shifted onto the smaller chainring.'),
    ('Front derailleur', 40.6, 56.2,
     'The mechanism guiding the chain between the front chainrings.',
     'The front derailleur shifts the chain across.'),
    ('Crank arm', 49.4, 70.0,
     'The arm connecting a pedal to the rotating crank assembly.',
     'The pedal is attached to the end of the crank arm.'),
    ('Clipless pedal', 55.9, 71.6,
     'A pedal that connects to a cleat on a cycling shoe.',
     'His shoes clip into the pedals.'),
    ('Brake caliper', 75.3, 56.5,
     'The part holding the brake pads, which act on the rotor.',
     'The mechanic checked whether the caliper was aligned.'),
]

# Which hotspots belong to which of the two diagram slides.
MAP_ONE = [0, 1, 2, 3, 4, 5, 6, 7, 8]                      # frame, fit, control
MAP_TWO = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]   # wheels, drive


# ── teaching cards ─────────────────────────────────────────────────────
FIT = [
    ('fitSaddle', 'Saddle &amp; seatpost',
     'The <strong>saddle</strong> is the seat. The <strong>seatpost</strong> holds it, '
     'and slides into the seat tube to set your height.',
     'fitSaddleN', 'Adjust the seatpost, not the saddle, for height.'),
    ('fitTubes', 'Top tube, down tube, seat tube',
     'The three main tubes of the frame. The <strong>down tube</strong> is the big '
     'diagonal one; the <strong>top tube</strong> runs along the top.',
     'fitTubesN', 'Together they are the frame — never "the body".'),
]

CONTROL = [
    ('ctlBars', 'Drop handlebars',
     'Curved bars giving several hand positions. The curved lower section is '
     '<strong>the drops</strong>.',
     'ctlBarsN', '&ldquo;She moved her hands onto the drops.&rdquo;'),
    ('ctlStem', 'Stem &amp; fork',
     'The <strong>stem</strong> clamps the bars to the <strong>fork</strong>, which '
     'holds the front wheel and turns with the bars.',
     'ctlStemN', 'The stem sets how far forward you reach.'),
]

DRIVE = [
    ('drvFront', 'At the front',
     '<strong>Crank arms</strong> turn the <strong>chainrings</strong>; the '
     '<strong>front derailleur</strong> moves the chain between them.',
     'drvFrontN', 'Pedals clip to the end of each crank arm.'),
    ('drvRear', 'At the back',
     'The <strong>chain</strong> drives the <strong>cassette</strong> — the cluster '
     'of sprockets — and the <strong>rear derailleur</strong> selects one.',
     'drvRearN', 'Chainrings at the front, cassette at the back.'),
]

PRECISE = [
    ('preCad', 'Cadence',
     'The rate at which you turn the pedals, in revolutions per minute. '
     '<strong>Not</strong> your speed along the road.',
     'preCadN', 'Maintain a steady cadence.'),
    ('preTrac', 'Traction',
     'Grip between the tyre and the surface you are riding on.',
     'preTracN', 'The rear tyre lost traction on the gravel.'),
    ('preRim', 'Rim vs hub',
     'The <strong>rim</strong> is the outer ring under the tyre. The '
     '<strong>hub</strong> is the centre. <strong>Spokes</strong> join the two.',
     'preRimN', 'The spokes connect the rim to the hub.'),
]

COLL_TEACH = [
    ('colMaintain', 'maintain a steady cadence',
     'English <em>maintains</em> a cadence. It does not achieve one or perform one.',
     'colMaintainN', 'Also: maintain a pace, maintain your line.'),
    ('colShift', 'shift <strong>into</strong> a lower gear',
     'You shift <em>into</em> a gear — not <em>on</em> it and not <em>at</em> it.',
     'colShiftN', 'Also: change into a lower gear.'),
    ('colLose', 'lose traction',
     'A tyre <em>loses</em> traction. It does not drop it or miss it.',
     'colLoseN', 'Also: lose grip, lose the back wheel.'),
    ('colInto', 'ride <strong>into</strong> a headwind',
     'A headwind blows towards you, so you ride <em>into</em> it.',
     'colIntoN', 'Also: ride into a crosswind, ride with a tailwind.'),
]

IDIOM_TEACH = [
    ('idBack', 'backpedal',
     'To retreat from a claim or a position you took earlier.',
     'idBackN', 'The spokesperson began to backpedal under questioning.'),
    ('idUphill', 'an uphill struggle',
     'A task that is hard going and stays hard going.',
     'idUphillN', 'Changing the policy was an uphill struggle.'),
    ('idGear', 'get into gear',
     'To start working actively and effectively, after a slow start.',
     'idGearN', 'We have talked for weeks — it is time to get into gear.'),
]


# ── question banks ─────────────────────────────────────────────────────
# Each option carries its own explanation, so a learner who picks a
# distractor is told why THAT was wrong (deck.py mc(explains=…)).
VOCAB = [
    dict(stem='The cluster of sprockets on the rear wheel is the&hellip;',
         options=['chainring', 'cassette', 'crank arm'], correct=1,
         why='A cassette is the cluster of sprockets at the rear wheel.',
         ex=['A chainring is at the front, turned by the cranks.', None,
             'A crank arm connects a pedal to the crank assembly.']),
    dict(stem='The mechanism guiding the chain between the rear sprockets is the rear&hellip;',
         options=['derailleur', 'brake caliper', 'hub assembly'], correct=0,
         why='The rear derailleur guides the chain across the cassette.',
         ex=[None, 'A caliper holds the brake pads — it does not touch the chain.',
             'The hub is what the wheel turns around, not a chain guide.']),
    dict(stem='Your rate of pedalling, measured in revolutions per minute, is your&hellip;',
         options=['traction', 'gradient', 'cadence'], correct=2,
         why='Cadence is how fast you turn the pedals — not how fast you travel.',
         ex=['Traction is grip between the tyre and the surface.',
             'Gradient is the steepness of the road.', None]),
    dict(stem='When the tyre stops gripping the surface, it loses&hellip;',
         options=['traction', 'cadence', 'clearance'], correct=0,
         why='Traction is grip between the tyre and the riding surface.',
         ex=[None, 'Cadence is your pedalling rate, not grip.',
             'Clearance is the space around a part.']),
    dict(stem='The outer structural ring of a wheel, beneath the tyre, is the&hellip;',
         options=['hub', 'rim', 'rotor'], correct=1,
         why='The rim supports the tyre; the hub is at the centre.',
         ex=['The hub is the centre the wheel turns around.', None,
             'The rotor is the brake disc attached to the hub.']),
    dict(stem='The toothed ring attached to the crank assembly is a&hellip;',
         options=['cassette', 'sprocket cluster', 'chainring'], correct=2,
         why='A chainring turns with the cranks at the front of the drivetrain.',
         ex=['A cassette is at the rear wheel.',
             'That describes the cassette, which is also at the rear.', None]),
]

COLL = [
    dict(stem='Complete the phrase: <em>______</em> a steady cadence.',
         options=['Maintain', 'Achieve', 'Perform'], correct=0,
         why='Maintain a steady cadence — keep your pedalling rhythm consistent.',
         ex=[None, 'You achieve a result, not an ongoing rhythm.',
             'You perform an action, not a cadence.']),
    dict(stem='Before the climb, she shifted <em>______</em> a lower gear.',
         options=['on', 'into', 'at'], correct=1,
         why='Shift into a lower gear is the natural combination.',
         ex=['Shift on is not used of gears.', None,
             'Shift at is not used of gears.']),
    dict(stem='On loose gravel, the rear tyre briefly <em>______</em> traction.',
         options=['missed', 'dropped', 'lost'], correct=2,
         why='Lose traction — lose grip on the riding surface.',
         ex=['Miss takes a target, not a quality you had.',
             'Drop suggests letting something fall.', None]),
    dict(stem='We spent the return journey riding <em>______</em> a headwind.',
         options=['into', 'onto', 'beneath'], correct=0,
         why='A headwind blows towards you, so you ride into it.',
         ex=[None, 'Onto marks arrival on a surface.',
             'Beneath puts you under something.']),
]

# Distractors lengthened so the key is no longer the giveaway. The source
# deck ran a 66-character key against 45 and 47.
INFER = [
    dict(stem='What does &ldquo;speed arriving in a box&rdquo; suggest?',
         options=[
             'Maya expected the purchase to improve her performance immediately.',
             'Maya was hoping the shop would deliver the bicycle to her door.',
             'Maya was already the quickest rider in her local cycling club.'],
         correct=0,
         why='The metaphor is about expectation: she thought buying the bike would deliver speed.',
         ex=[None, 'The box is a metaphor, not an actual delivery.',
             'The passage says a neighbour still passed her on the climb.']),
    dict(stem='What is the club rider really encouraging Maya to do?',
         options=[
             'Sell the new bicycle and buy an ordinary one.',
             'Identify what is actually limiting her riding.',
             'Stop paying attention to how her rides go.'],
         correct=1,
         why='The question asks whether she identified the problem before buying a solution.',
         ex=['Nobody suggests she get rid of the bike.', None,
             'The point is to measure the right thing, not to stop measuring.']),
    dict(stem='How does Maya&rsquo;s attitude change?',
         options=[
             'She becomes embarrassed about owning such expensive equipment.',
             'She decides that every upgrade is a waste of money.',
             'She still values the bike, but has more realistic expectations.'],
         correct=2,
         why='She still loves it; what changes is the claim she makes for it.',
         ex=['The passage says she still loved the bike.',
             '&ldquo;Dismissing every upgrade as vanity is too easy.&rdquo;', None]),
    dict(stem='Which statement best captures the writer&rsquo;s conclusion?',
         options=[
             'The value of an upgrade depends on the rider&rsquo;s needs.',
             'Better habits always make equipment irrelevant.',
             'Premium equipment is only worthwhile for professionals.'],
         correct=0,
         why='The closing question is explicitly about who benefits, and for what.',
         ex=[None, '&ldquo;Always&rdquo; is stronger than the passage allows.',
             'The passage never restricts good equipment to professionals.']),
]

# The three idioms are a closed set, so as MCQ the longest one is always the
# giveaway on its own item. A gap-fill with a shared alphabetical bank asks
# the same thing and cannot leak the answer by length.
IDIOM_BANK = ['an uphill struggle', 'backpedal', 'get into gear']
IDIOM_ROWS = [
    ('After promising that no jobs would be cut, the manager began to ______ when questioned.',
     ['backpedal'], 'Backpedal — retreat from a claim you made earlier.'),
    ('Persuading the committee to fund the project was ______.',
     ['an uphill struggle'], 'The article is part of the expression: <em>an</em> uphill struggle.'),
    ('We have talked about the plan for weeks. It is time to ______.',
     ['get into gear'], 'Get into gear — start working actively.'),
]

DILEMMAS = [
    ('An exceptional bike once a month, or an ordinary bike every day?',
     '&ldquo;The main trade-off would be&hellip;&rdquo;'),
    ('A flat route into a headwind, or a steep climb in calm weather?',
     '&ldquo;I&rsquo;d be inclined to choose&hellip;, provided that&hellip;&rdquo;'),
    ('An older premium bike, or a new basic bike with a warranty?',
     '&ldquo;I&rsquo;d want to establish whether&hellip;&rdquo;'),
    ('A quicker ride through traffic, or a longer protected route?',
     '&ldquo;Although&hellip; would save time, I&rsquo;d prioritise&hellip;&rdquo;'),
    ('Spend the money on equipment, or on a cycling holiday?',
     '&ldquo;The benefit I&rsquo;d value most would be&hellip;&rdquo;'),
]

SHOP_PHRASES = ['It seems to&hellip;', 'When you say&hellip;, do you mean&hellip;?',
                'One possibility is&hellip;, although&hellip;',
                'I&rsquo;d need to check before&hellip;']

SHOP_DIALOGUE = [
    ('Rider', 'The chain seems to slip when I press hard on the pedals, especially uphill.'),
    ('Mechanic', 'When you say &ldquo;slips&rdquo;, do you mean the pedals suddenly move '
                 'without the bike pulling forward?'),
    ('Rider', 'Yes. It started two rides ago. I assumed the cassette needed replacing.'),
    ('Mechanic', 'Wear could be a factor, although I&rsquo;d need to inspect it before '
                 'drawing a conclusion.'),
    ('Rider', 'Could you give me an estimate before replacing anything?'),
    ('Mechanic', 'Of course. We&rsquo;ll inspect it, then call you with our findings and a quote.'),
]


# ── bespoke slides ─────────────────────────────────────────────────────
def riders_slide():
    cells = "\n          ".join(
        '<button class="rider" type="button" data-rider="%d" aria-pressed="%s">'
        '<img src="%s/%s" alt="%s" loading="lazy"><span class="rider-name">%s</span></button>'
        % (n, 'true' if n == 0 else 'false', F, pic, D.esc(name), name)
        for n, (name, fam, pic, what, ask) in enumerate(RIDERS))
    data = "\n        ".join(
        '<template data-rider-info="%d"><span class="rider-fam">%s</span>'
        '<span class="rider-what">%s</span><span class="rider-ask">%s</span></template>'
        % (n, fam, what, ask)
        for n, (name, fam, pic, what, ask) in enumerate(RIDERS))
    return '''
    <section class="slide" data-type="teach" data-custom="riders">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="ridersEyebrow">Break the ice</div>
        <h2 class="slide-title" data-i18n="ridersTitle">What kind of cyclist are you?</h2>
      </div></div>
      <div class="slide-body">
        <p class="prose dim" style="font-size:16px;margin-bottom:12px" data-i18n="ridersHint">Click a rider. Read what the riding involves, then answer the question underneath.</p>
        <div class="rider-wrap">
          <div class="rider-grid">
          %s
          </div>
          <div class="rider-info">
            <h3 class="rider-title">%s</h3>
            <p class="rider-fam-out"></p>
            <p class="rider-what-out prose"></p>
            <p class="rider-ask-out"><span class="rider-ask-label" data-i18n="ridersAsk">Talk about it</span></p>
          </div>
        </div>
        %s
      </div>
    </section>
''' % (cells, RIDERS[0][0], data)


def map_slide(which, idx, eyebrow_key, eyebrow, title_key, title):
    spots = "\n            ".join(
        '<button class="spot" type="button" data-part="%d" aria-pressed="%s" '
        'style="left:%s%%;top:%s%%" aria-label="%d. %s">%d</button>'
        % (p, 'true' if n == 0 else 'false', PARTS[p][1], PARTS[p][2],
           n + 1, D.esc(PARTS[p][0]), n + 1)
        for n, p in enumerate(idx))
    opts = "\n              ".join(
        '<option value="%d">%d. %s</option>' % (p, n + 1, PARTS[p][0])
        for n, p in enumerate(idx))
    data = "\n        ".join(
        '<template data-part-info="%d"><span class="part-name">%s</span>'
        '<span class="part-what">%s</span><span class="part-say">%s</span></template>'
        % (p, PARTS[p][0], PARTS[p][3], PARTS[p][4]) for p in idx)
    return '''
    <section class="slide" data-type="teach" data-custom="map" data-map="%s">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="map-wrap">
          <div class="map-stage">
            <svg class="map-bike" viewBox="0 0 1536 1024" role="img"
                 aria-label="Schematic side view of a road bicycle from the drivetrain side"><use href="#bikeImage"></use></svg>
            %s
          </div>
          <div class="map-info">
            <label class="map-pick">
              <span data-i18n="mapPick">Choose a component</span>
              <select class="map-select">
              %s
              </select>
            </label>
            <h3 class="part-name-out"></h3>
            <p class="part-what-out prose"></p>
            <p class="part-say-out"></p>
            <p class="prose dim map-hint" data-i18n="mapHint">Click a number. Say what the part does, then use it in a sentence of your own.</p>
          </div>
        </div>
        <p class="map-note dim" data-i18n="mapNote">Teaching schematic &middot; not a specified production model.</p>
        %s
      </div>
    </section>
''' % (which, eyebrow_key, eyebrow, title_key, title, spots, opts, data)


def reading_slide(n, eyebrow_key, eyebrow, title_key, title, paras, ask_key, ask, bg):
    body = "\n          ".join('<p class="prose read-para">%s</p>' % p for p in paras)
    return '''
    <section class="slide" data-type="teach" data-custom="read"%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="read-col">
          %s
        </div>
        <p class="read-ask" data-i18n="%s">%s</p>
      </div>
    </section>
''' % (D._bg(F, bg), eyebrow_key, eyebrow, title_key, title, body, ask_key, ask)


def shop_slide():
    phrases = " ".join('<span class="bank-chip">%s</span>' % p for p in SHOP_PHRASES)
    lines = "\n            ".join(
        '<p class="dlg"><strong>%s:</strong> %s</p>' % (who, what)
        for who, what in SHOP_DIALOGUE)
    return '''
    <section class="slide" data-type="teach" data-custom="shop"%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="shopEyebrow">Role play</div>
        <h2 class="slide-title" data-i18n="shopTitle">&ldquo;It only happens on hills&rdquo;</h2>
      </div></div>
      <div class="slide-body">
        <p class="prose dim" style="font-size:16px;margin-bottom:12px" data-i18n="shopHint">Take a role each. Run it twice, then swap and try a rubbing brake instead.</p>
        <div class="cols">
          <div class="card">
            <p class="prose"><strong data-i18n="shopRiderRole">A &middot; The rider</strong></p>
            <p class="prose" data-i18n="shopRiderBrief" style="margin-top:8px;font-size:18px">Your chain slips when you press hard on the pedals. It started two rides ago.</p>
            <p class="prose dim" data-i18n="shopRiderTask" style="margin-top:8px;font-size:15px">Describe when it happens. Ask for an estimate. Agree a spending limit.</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="shopMechRole">B &middot; The mechanic</strong></p>
            <p class="prose" data-i18n="shopMechBrief" style="margin-top:8px;font-size:18px">You need to inspect the bike before you can identify the cause.</p>
            <p class="prose dim" data-i18n="shopMechTask" style="margin-top:8px;font-size:15px">Clarify the symptoms. Explain what you cannot yet know. Agree to call before extra work.</p>
          </div>
        </div>
        <div class="act-target" style="margin-top:14px">
          <span class="act-target-label" data-i18n="shopBorrow">Borrow a phrase</span>
          %s
        </div>
        <div style="margin-top:12px">
          <button class="btn dlg-toggle" type="button" data-i18n="shopModel"
                  data-label-hide="Hide the dialogue">Show a model dialogue</button>
        </div>
        <div class="dlg-box" hidden>
          %s
        </div>
      </div>
    </section>
''' % (D._bg(F, 'workshop-red-bike.jpg'), phrases, lines)


def trade_slide():
    data = "\n        ".join(
        '<template data-dilemma="%d"><span class="dil-q">%s</span>'
        '<span class="dil-s">%s</span></template>' % (n, q, s)
        for n, (q, s) in enumerate(DILEMMAS))
    return '''
    <section class="slide" data-type="teach" data-custom="trade"%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="tradeEyebrow">Would you rather&hellip;?</div>
        <h2 class="slide-title" data-i18n="tradeTitle">There is always a trade-off</h2>
      </div></div>
      <div class="slide-body">
        <p class="dil-count"><span data-i18n="tradeCount">Dilemma</span> <span class="dil-n">1</span> / %d</p>
        <p class="dil-q-out q-stem"></p>
        <p class="dil-s-out"></p>
        <p class="prose dim" style="font-size:16px;margin-top:18px" data-i18n="tradeHint">State a preference, concede a drawback, then say what would change your mind.</p>
        <div style="margin-top:16px">
          <button class="btn dil-next" type="button" data-i18n="tradeNext">Another dilemma &rarr;</button>
        </div>
        %s
      </div>
    </section>
''' % (D._bg(F, 'alpine-road.jpg'), len(DILEMMAS), data)


def debate_slide():
    return '''
    <section class="slide" data-type="teach" data-custom="debate"%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="debateEyebrow">Debate and negotiate</div>
        <h2 class="slide-title" data-i18n="debateTitle">Who is the city for?</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem" data-i18n="debateMotion">Replace town-centre parking with a protected cycle lane.</p>
        <div class="cols cols-3">
          <div class="card">
            <p class="prose"><strong data-i18n="debateRoleA">The commuter</strong></p>
            <p class="prose" data-i18n="debateBriefA" style="margin-top:8px;font-size:17px">You need a continuous route and junctions you can trust.</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="debateRoleB">The shop owner</strong></p>
            <p class="prose" data-i18n="debateBriefB" style="margin-top:8px;font-size:17px">You need deliveries to arrive and customers to reach the door.</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="debateRoleC">The access advocate</strong></p>
            <p class="prose" data-i18n="debateBriefC" style="margin-top:8px;font-size:17px">You speak for crossings, bus stops and disabled residents.</p>
          </div>
        </div>
        <p class="prose" style="margin-top:14px" data-i18n="debateTask">Agree one recommendation and two conditions.</p>
        <div class="timer-row">
          <span class="timer-face">01:30</span>
          <button class="btn timer-start" type="button" data-i18n="debateStart"
                  data-label-pause="Pause" data-label-resume="Resume" data-label-restart="Restart">Start</button>
          <button class="btn timer-reset" type="button" data-i18n="debateReset">Reset</button>
          <span class="prose dim timer-note" data-i18n="debateTimer">90-second final pitch</span>
        </div>
      </div>
    </section>
''' % D._bg(F, 'city-ride.jpg')


# ── weight, and the machinery the bespoke slides need ──────────────────
EXTRA_CSS = '''
/* ── BEYOND THE HANDLEBARS ──────────────────────────────────────────
   Innes asked for bolder text. HOUSE-STYLE §6 pins the type SCALE and the
   display weights and says nothing about the weight of 19-20px DM Sans, so
   weight is the axis that was free. DM Sans 500 is already loaded by the
   template's font link; nothing new is fetched. */
.prose, .q-stem, .opt, .sort-item, .match-item, .bank-chip, .gap { font-weight: 500; }
.prose strong, .card .prose strong { font-weight: 700; }
.read-para { font-weight: 400; }   /* except a passage, which reads worse bold */

/* ── the twelve rider types ── */
.rider-wrap { display: grid; grid-template-columns: 1fr 330px; gap: 20px; align-items: start; }
.rider-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 8px; }
.rider {
  border: 2px solid transparent; background: var(--surface); border-radius: 10px;
  padding: 0; overflow: hidden; cursor: pointer; display: block; text-align: center;
}
.rider img { width: 100%; aspect-ratio: 56/62; object-fit: cover; object-position: 50% 22%; display: block; }
.rider-name {
  display: block; padding: 5px 4px 6px; font-family: var(--font-ui);
  font-size: 11px; font-weight: 500; line-height: 1.2; color: var(--text-dim);
}
.rider[aria-pressed="true"] { border-color: var(--accent-bright); }
.rider[aria-pressed="true"] .rider-name { color: var(--accent-bright); }
.rider-info { background: var(--surface2); border-radius: 12px; padding: 18px 18px 20px; }
.rider-title { font-family: var(--font-display); font-size: 27px; font-weight: 700;
               line-height: 1.15; color: var(--text); margin: 0; }
.rider-fam-out { font-family: var(--font-mono); font-size: 11.5px; letter-spacing: .16em;
                 text-transform: uppercase; color: var(--accent-bright); margin: 6px 0 12px; }
.rider-what-out { font-size: 17px; }
.rider-ask-out { margin-top: 14px; font-size: 18px; font-weight: 500; color: var(--text); }
.rider-ask-label {
  display: block; font-family: var(--font-mono); font-size: 11.5px; letter-spacing: .16em;
  text-transform: uppercase; color: var(--text-dim); margin-bottom: 5px;
}

/* ── the numbered bicycle ──
   The stage is sized, not flexed. The schematic is 1536x1024, so a stage
   given the leftover 790px of an `1fr 340px` grid comes out 527px tall and
   the slide overflowed by 24px. Fixing the WIDTH fixes the height with it,
   and it has to be the stage rather than the <svg>: the hotspots are
   positioned in percentages of .map-stage, so anything that letterboxes the
   drawing inside a taller box walks every number off its part. */
.map-wrap { display: grid; grid-template-columns: 690px 1fr; gap: 20px; align-items: start; }
.map-stage { position: relative; border-radius: 12px; overflow: hidden; background: #fff; }
.map-bike { display: block; width: 100%; height: auto; }
.spot {
  position: absolute; width: 30px; height: 30px; border-radius: 50%;
  transform: translate(-50%, -50%); padding: 0; cursor: pointer;
  border: 2px solid #fff; background: #163b43; color: #fff;
  font-family: var(--font-mono); font-size: 13px; line-height: 1;
}
.spot[aria-pressed="true"] { background: var(--accent-dim); color: #16110d;
                             box-shadow: 0 0 0 5px rgba(230, 146, 96, .32); }
.map-info { background: var(--surface2); border-radius: 12px; padding: 16px 18px 18px; }
.map-pick { display: block; font-family: var(--font-mono); font-size: 11.5px;
            letter-spacing: .16em; text-transform: uppercase; color: var(--text-dim); }
.map-select {
  display: block; width: 100%; margin-top: 6px; padding: 9px 10px; border-radius: 8px;
  background: var(--surface); color: var(--text); border: 1px solid var(--border);
  font-family: var(--font-ui); font-size: 15px; font-weight: 500;
}
.part-name-out { font-family: var(--font-display); font-size: 25px; font-weight: 700;
                 line-height: 1.15; color: var(--text); margin: 14px 0 8px; }
.part-what-out { font-size: 17px; }
.part-say-out { margin-top: 10px; font-size: 17px; font-weight: 500; font-style: italic;
                color: var(--accent-bright); }
.map-hint { font-size: 14px; margin-top: 14px; }
.map-note { font-family: var(--font-mono); font-size: 11px; letter-spacing: .1em;
            text-transform: uppercase; margin-top: 10px; }

/* ── plates ──
   The template plates every piece of text that would otherwise paint straight
   onto the washed hero, and its own comment on that selector list says
   "anything that paints text straight onto the stage belongs in [it]". These
   are this deck's additions. Measured first: the reading passage was white
   DM Sans over a bright peloton illustration and came out unreadable.
   The passage takes one plate around the whole column rather than a plate per
   paragraph — six stacked shadows read as six bars, and a passage wants to
   look like a page. It takes solid --surface rather than --plate-bg: the
   plate is deliberately a little transparent, which is right behind a
   heading and wrong behind ten lines a learner has to read twice. */
.read-col { background: var(--surface); border-radius: 10px; padding: 17px 20px; }
.map-note, .dil-count, .dil-s-out, .timer-face, .timer-note {
  background: var(--plate-bg); border-radius: 8px;
  box-shadow: 0 0 0 0.34em var(--plate-bg); text-shadow: none;
  width: fit-content;
}

/* ── the reading passages ── */
.read-col { max-width: 41em; }
.read-para + .read-para { margin-top: 13px; }
.read-para mark { background: none; color: var(--accent-bright); font-weight: 600; }
.read-ask {
  margin-top: 22px; padding: 13px 16px; border-left: 3px solid var(--accent-dim);
  background: var(--surface2); border-radius: 0 10px 10px 0;
  font-size: 17px; font-weight: 500; color: var(--text); max-width: 41em;
}

/* ── the repair shop ── */
.dlg-box { margin-top: 14px; background: var(--surface2); border-radius: 12px; padding: 14px 18px; }
.dlg { font-family: var(--font-ui); font-size: 16px; line-height: 1.5; color: var(--text); }
.dlg + .dlg { margin-top: 7px; }
.dlg strong { color: var(--accent-bright); font-weight: 600; }

/* ── the dilemmas ── */
.dil-count { font-family: var(--font-mono); font-size: 11.5px; letter-spacing: .16em;
             text-transform: uppercase; color: var(--accent-bright); margin-bottom: 14px; }
.dil-q-out { max-width: 30em; margin-bottom: 14px; }
.dil-s-out { font-size: 20px; font-weight: 500; font-style: italic; color: var(--accent-bright); }

/* ── the debate timer ── */
.timer-row { display: flex; align-items: center; gap: 14px; margin-top: 18px; flex-wrap: wrap; }
.timer-face { font-family: var(--font-mono); font-size: 34px; color: var(--text);
              min-width: 3.3em; font-variant-numeric: tabular-nums; }
.timer-note { font-size: 15px; }

@media print {
  .dlg-box[hidden] { display: block !important; }
  .dlg-toggle, .dil-next, .timer-row { display: none !important; }
}
'''

EXTRA_JS = '''
<script>
/* Beyond the Handlebars — the four bespoke slides.
   Everything here is per-slide and idempotent: goTo() may re-run a slide any
   number of times, and the language switcher re-renders data-i18n nodes under
   it, so nothing caches a translated string. */
(function () {
  var $$ = function (r, s) { return Array.prototype.slice.call(r.querySelectorAll(s)); };
  function tpl(root, sel, cls) {
    var t = root.querySelector(sel);
    if (!t) return '';
    var n = t.content.querySelector('.' + cls);
    return n ? n.innerHTML : '';
  }

  /* ── rider types ── */
  $$(document, '[data-custom="riders"]').forEach(function (sl) {
    var info = sl.querySelector('.rider-info');
    function show(n) {
      $$(sl, '.rider').forEach(function (b) {
        b.setAttribute('aria-pressed', b.dataset.rider === String(n) ? 'true' : 'false');
      });
      var sel = '[data-rider-info="' + n + '"]';
      info.querySelector('.rider-title').textContent =
        sl.querySelector('.rider[data-rider="' + n + '"] .rider-name').textContent;
      info.querySelector('.rider-fam-out').innerHTML = tpl(sl, sel, 'rider-fam');
      info.querySelector('.rider-what-out').innerHTML = tpl(sl, sel, 'rider-what');
      var ask = info.querySelector('.rider-ask-out');
      var label = ask.querySelector('.rider-ask-label');
      ask.innerHTML = '';
      ask.appendChild(label);
      ask.insertAdjacentHTML('beforeend', tpl(sl, sel, 'rider-ask'));
    }
    $$(sl, '.rider').forEach(function (b) {
      b.addEventListener('click', function () { show(b.dataset.rider); });
    });
    show(0);
  });

  /* ── the numbered bicycle ── */
  $$(document, '[data-custom="map"]').forEach(function (sl) {
    var sel = sl.querySelector('.map-select');
    function show(p) {
      $$(sl, '.spot').forEach(function (b) {
        b.setAttribute('aria-pressed', b.dataset.part === String(p) ? 'true' : 'false');
      });
      sel.value = String(p);
      var q = '[data-part-info="' + p + '"]';
      sl.querySelector('.part-name-out').innerHTML = tpl(sl, q, 'part-name');
      sl.querySelector('.part-what-out').innerHTML = tpl(sl, q, 'part-what');
      sl.querySelector('.part-say-out').innerHTML = '&ldquo;' + tpl(sl, q, 'part-say') + '&rdquo;';
    }
    $$(sl, '.spot').forEach(function (b) {
      b.addEventListener('click', function () { show(b.dataset.part); });
    });
    sel.addEventListener('change', function () { show(sel.value); });
    show(sl.querySelector('.spot').dataset.part);
  });

  /* ── the repair-shop model dialogue ── */
  $$(document, '.dlg-toggle').forEach(function (btn) {
    var box = btn.closest('.slide').querySelector('.dlg-box');
    btn.addEventListener('click', function () {
      var open = box.hasAttribute('hidden');
      if (open) box.removeAttribute('hidden'); else box.setAttribute('hidden', '');
      /* Swap through data-i18n so the switcher keeps control of the wording:
         the open label lives in a second key the engine also translates. */
      btn.dataset.i18n = open ? 'shopModelHide' : 'shopModel';
      if (window.applyI18n) window.applyI18n();
    });
  });

  /* ── the dilemmas ── */
  $$(document, '[data-custom="trade"]').forEach(function (sl) {
    var n = 0, total = $$(sl, '[data-dilemma]').length;
    function show() {
      var q = '[data-dilemma="' + n + '"]';
      sl.querySelector('.dil-n').textContent = String(n + 1);
      sl.querySelector('.dil-q-out').innerHTML = tpl(sl, q, 'dil-q');
      sl.querySelector('.dil-s-out').innerHTML = tpl(sl, q, 'dil-s');
    }
    sl.querySelector('.dil-next').addEventListener('click', function () {
      n = (n + 1) % total; show();
    });
    show();
  });

  /* ── the 90-second pitch ── */
  $$(document, '[data-custom="debate"]').forEach(function (sl) {
    var face = sl.querySelector('.timer-face');
    var start = sl.querySelector('.timer-start');
    var left = 90, tick = null, until = 0;
    function paint() {
      face.textContent = String(Math.floor(left / 60)).padStart(2, '0') + ':' +
                         String(left % 60).padStart(2, '0');
    }
    function label(k) { start.textContent = start.dataset['label' + k] || start.textContent; }
    function stop() {
      clearInterval(tick); tick = null;
      if (!left) label('Restart'); else if (left === 90) { start.dataset.i18n = 'debateStart';
        if (window.applyI18n) window.applyI18n(); } else label('Resume');
    }
    start.addEventListener('click', function () {
      if (tick) { stop(); return; }
      if (!left) left = 90;
      until = Date.now() + left * 1000;
      label('Pause');
      tick = setInterval(function () {
        left = Math.max(0, Math.ceil((until - Date.now()) / 1000));
        paint();
        if (!left) stop();
      }, 150);
    });
    sl.querySelector('.timer-reset').addEventListener('click', function () {
      clearInterval(tick); tick = null; left = 90; paint();
      start.dataset.i18n = 'debateStart';
      if (window.applyI18n) window.applyI18n();
    });
    paint();
  });
})();
</script>
'''


def build():
    D.assert_no_key_is_longest(VOCAB, 'VOCAB')
    D.assert_no_key_is_longest(COLL, 'COLL')
    D.assert_no_key_is_longest(INFER, 'INFER')
    D.assert_bank_is_not_a_key(IDIOM_BANK,
                               [a for _, ans, _ in IDIOM_ROWS for a in ans])

    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Beyond the <em>handlebars</em>',
                'The parts of a bicycle, the words that ride with them, and the '
                'conversations they start',
                [('Level', 'B2 / C1 &middot; Vocabulary'),
                 ('Focus', 'Precision &amp; inference'),
                 ('Count', 'COUNT slides')])

        + riders_slide()

        + D.teach('fitEyebrow', 'The bike, decoded', 'fitTitle',
                  'Where you sit, and what holds you', FIT, folder=F,
                  bg='mountain-road.jpg')
        + D.teach('controlEyebrow', 'The bike, decoded', 'controlTitle',
                  'What you steer with', CONTROL, folder=F)
        + map_slide('one', MAP_ONE, 'mapOneEyebrow', 'The bike, decoded',
                    'mapOneTitle', 'Frame, fit and control')

        + D.teach('driveEyebrow', 'The bike, decoded', 'driveTitle',
                  'Where the power goes', DRIVE, folder=F, bg='workshop-inspect.jpg')
        + map_slide('two', MAP_TWO, 'mapTwoEyebrow', 'The bike, decoded',
                    'mapTwoTitle', 'Wheels, braking and drivetrain')

        + D.teach('preEyebrow', 'Make it precise', 'preTitle',
                  'Three that get confused', PRECISE, cols='1fr 1fr 1fr',
                  folder=F, bg='mountain-pedal.jpg')
        + "".join(D.mc(i + 1, len(VOCAB), q, 'vocabEyebrow', 'Make it precise',
                       'vocabTitle', 'Not just &ldquo;that bit&rdquo;', folder=F,
                       explains=q['ex'],
                       bg=[None, 'workshop-inspect.jpg', None,
                           'mountain-pedal.jpg', None, 'workshop-red-bike.jpg'][i % 6])
                  for i, q in enumerate(VOCAB))

        + D.teach('collTeachEyebrow', 'Sound like a rider', 'collTeachTitle',
                  'Words that ride together', COLL_TEACH, cols='1fr 1fr',
                  folder=F, bg='cycle-lane.jpg')
        + "".join(D.mc(i + 1, len(COLL), q, 'collEyebrow', 'Natural combinations',
                       'collTitle', 'Which word does English put here?', folder=F,
                       explains=q['ex'],
                       bg=[None, 'alpine-road.jpg', None, 'cycle-lane.jpg'][i % 4])
                  for i, q in enumerate(COLL))

        + reading_slide(
            1, 'readOneEyebrow', 'Read between the lines', 'readOneTitle',
            'Buying speed',
            ['When Maya bought her first high-end road bike, she imagined '
             '<mark>speed arriving in a box</mark>. The carbon frame was lighter, the '
             'gear changes quieter and the riding position more aggressive. On her '
             'usual climb, the same neighbour still passed her on an ordinary-looking '
             'bicycle.',
             'At first, she blamed the headwind. Then her tyre pressure. Eventually, a '
             'club rider asked: was she buying equipment to solve a problem she had '
             'never properly identified?'],
            'readAskOne',
            'Pause and predict: what might Maya change next? What does the highlighted '
            'phrase suggest?', 'mountain-road.jpg')

        + reading_slide(
            2, 'readTwoEyebrow', 'Read between the lines', 'readTwoTitle',
            'Finding perspective',
            ['Maya focused on her <mark>cadence</mark> and changed gear before the road '
             'became steep. She also asked a mechanic to investigate a rubbing brake. '
             'None of this produced a spectacular transformation. It did make riding '
             'more enjoyable.',
             'She still loved the bike. Beautiful engineering could be a pleasure '
             'without being a shortcut to fitness. What changed was the claim she made '
             'for it.',
             'Yet dismissing every upgrade as vanity is too easy. A bike that fits '
             'badly or shifts unreliably may be worth replacing. The question is: '
             '<mark>worth it for whom, and for what?</mark>'],
            'readAskTwo',
            'Find the sentence that balances the writer&rsquo;s argument. Why is it '
            'there?', 'cafe-conversation.jpg')

        + "".join(D.mc(i + 1, len(INFER), q, 'inferEyebrow', 'Meaning beneath the words',
                       'inferTitle', 'What is the writer really saying?', folder=F,
                       explains=q['ex'],
                       bg=[None, 'cafe-conversation.jpg', None, 'mountain-road.jpg'][i % 4])
                  for i, q in enumerate(INFER))

        + shop_slide()

        + D.teach('idiomTeachEyebrow', 'When cycling becomes a metaphor',
                  'idiomTeachTitle', 'Take the language further', IDIOM_TEACH,
                  cols='1fr 1fr 1fr', folder=F, bg='city-ride.jpg')
        + D.gap(1, 1, IDIOM_ROWS, IDIOM_BANK, 'idiomEyebrow', 'Off the bike',
                'idiomTitle', 'One idiom per space', folder=F,
                hint_key='idiomHint',
                hint='Three idioms, three sentences, each used once. Case does not matter.',
                width=210)

        + trade_slide()
        + debate_slide()

        + D.results(next_key='resNext',
                    next_text='You can name the parts and question the claims. Now use both &rarr;',
                    folder=F, bg='alpine-road.jpg')

        + D.activate(
            'Your next conversation starts here', 'Use these',
            ['cadence', 'traction', 'cassette', 'derailleur', 'rim', 'chainring',
             'maintain a steady cadence', 'shift into a lower gear', 'lose traction',
             'ride into a headwind', 'backpedal', 'an uphill struggle'],
            'Speaking',
            'Without looking back at the deck, work through all three in pairs.',
            ['Name three components and say what each one does.',
             'Describe a fault using two natural combinations.',
             'Qualify one claim about the cause &mdash; what makes you think that?'],
            'Writing',
            'Write 150&ndash;180 words: is premium equipment worth it? Use four target '
            'expressions, one concession and one conditional sentence.',
            'It depends on what the rider is actually trying to fix…',
            folder=F, bg='hero.jpg')
    )

    import i18n_handlebars as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Beyond the Handlebars — Forbes English',
                   I, langs=('en', 'de', 'es'))

    # The bicycle's <defs> and the bespoke slides' machinery. Both go in after
    # assemble(), because assemble() owns the region between the cover marker
    # and the deck chrome and will not carry anything else through.
    bike = open(BIKE, encoding='utf-8').read()
    s = s.replace('\n</style>', EXTRA_CSS + '</style>', 1)
    s = s.replace('</body>', bike + EXTRA_JS + '\n</body>', 1)

    # The count chip is written once the deck knows how long it is. Counting
    # `<section class="slide` returns N+1 — the template keeps one of its own
    # that never ships — so count the ones that carry a data-type, which is
    # the set check-lesson.js reports in its header line.
    n = len(re.findall(r'<section class="slide[^>]*\bdata-type=', s))
    s = s.replace('COUNT slides', '%d slides' % n)
    s = s.replace('COUNT Folien', '%d Folien' % n)
    s = s.replace('COUNT diapositivas', '%d diapositivas' % n)

    open(OUT, 'w', encoding='utf-8', newline='').write(s)
    print('%s — %d slides' % (OUT, n))


if __name__ == '__main__':
    build()
