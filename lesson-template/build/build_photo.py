# -*- coding: utf-8 -*-
"""Advanced Photography (B2) — rebuilt as a deck.

The old page called itself a lesson and was a test. There was no presentation
stage, no reading, no reference chart — nothing at all before the questions.
Every one of its seventeen items asked for specialist vocabulary the page had
never taught, and the explanations only appeared after the learner had been
scored on not knowing them. Three teaching slides now open the deck: the
exposure triangle, the lens and its characteristic faults, and composition.
Every scored item is answerable from them.

Then the defects.

**Four of the six multiple-choice keys were the longest option**, and the key
was above the mean option length in all six. Distractors lengthened; no key
shortened.

**The word bank was a rotation of the gap order**, not a shuffle: gaps 3, 4,
6, 5, 1, 2. Two placements and the rest fell out by pattern. It is alphabetical
now, and carries decoys.

**The scoring did not add up.** The page advertised 17 questions and scored 18
points, so the progress bar rendered at 106% and a perfect learner was shown
18/18 under a header promising 17. The reorder was also all-or-nothing while
the section reported partial credit, so 4/5 displayed as 4/5 and recorded 0.

**And two definitions were wrong.** EV was defined as "the total amount of
light reaching the sensor", which is exposure, not exposure value — and the
lesson's own feedback contradicted the option it made you choose. Focal length
was defined as the distance from optical centre to sensor, which is only true
at infinity focus.
"""
import sys
sys.path.insert(0, '/tmp')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-photography-b2.html'
F = 'Photography'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0d0c0a;
  --surface       : #191815;
  --surface2      : #25231e;
  --border        : #724d46;
  --text          : #f5f2f2;
  --text-dim      : #bfa7a3;
  --accent        : #cb6553;
  --accent-bright : #e09385;
  --accent-dim    : #904032;
  --secondary     : #95a5ac;
  --contrast      : #24e5a5;''' % F

MC = [
    dict(stem='Which term describes the zone in a scene that appears <strong>acceptably sharp</strong>?',
         options=['Depth of field &mdash; the sharp zone extending in front of and behind the focus point',
                  'Focal length &mdash; the optical property of a lens that determines its angle of view',
                  'Dynamic range &mdash; the ratio between the lightest and darkest values a sensor records',
                  'Exposure range &mdash; the span of tones a camera can capture in one single frame'],
         correct=0,
         why='<strong>Depth of field</strong> is the sharp zone. A wide aperture (low f-number) makes it shallow; a narrow one makes it deep. Distance to subject and focal length matter too.'),
    dict(stem='You want to freeze a sprinting athlete with no motion blur, and you have light to spare. Which setting matters most?',
         options=['Shutter speed &mdash; a fast setting limits how long the sensor is exposed',
                  'White balance &mdash; matching colour temperature to the ambient light source',
                  'Aperture priority &mdash; a wide aperture throws the background out of focus',
                  'Focal length &mdash; a longer lens fills the frame with the moving subject'],
         correct=0,
         why='<strong>Shutter speed</strong> is the one that decides whether motion is frozen. At 1/1000s the athlete is sharp; at 1/30s they are a streak. In poor light you would then raise ISO to pay for it &mdash; but the shutter is still the setting doing the work.'),
    dict(stem='In the exposure triangle, raising ISO from 400 to 3200 costs you what?',
         options=['More digital noise, as the sensor amplifies its signal',
                  'A shallower depth of field, so the background goes soft',
                  'More camera shake, as the sensor picks up vibration',
                  'A narrower aperture, so less light enters the lens'],
         correct=0,
         why='ISO amplifies the signal the sensor already has, and amplifies its errors with it. That is <strong>noise</strong> &mdash; grain in the shadows and mottled colour. Nothing optical changes.'),
    dict(stem='<em>Bokeh</em>, from the Japanese for blur, refers specifically to what?',
         options=['The quality of the out-of-focus areas, especially the highlights',
                  'A post-processing technique for selectively sharpening parts of an image',
                  'A filter placed in front of the lens to soften contrast across the frame',
                  'Deliberate camera movement during a long exposure, for artistic effect'],
         correct=0,
         why='Not <em>how much</em> blur &mdash; <em>what kind</em>. <strong>Bokeh</strong> is the character of the blur, and photographers pay a great deal for lenses that render it smoothly.'),
    dict(stem='What does the <em>sunny 16 rule</em> help you estimate, with no light meter?',
         options=['Exposure in sunlight: f/16, with shutter speed matched to ISO',
                  'The ideal focal length in millimetres for shooting in bright daylight',
                  'The white balance in Kelvin needed for neutral colour outdoors',
                  'The number of frames you can shoot before the memory card fills'],
         correct=0,
         why='In direct sun, set f/16 and the shutter to roughly 1 over the ISO &mdash; ISO 100 gives 1/100s. It is a starting point, not a law, but it is close enough to work.'),
    dict(stem='Which technique places the subject on one of four intersections of a 3&times;3 grid?',
         options=['The rule of thirds &mdash; off-centre placement, for visual balance',
                  'Leading lines &mdash; diagonals that pull the eye towards the subject',
                  'Negative space &mdash; empty area around a subject, to emphasise it',
                  'The golden ratio &mdash; a spiral proportion borrowed from nature'],
         correct=0,
         why='The <strong>rule of thirds</strong> is the one with the grid. Dead centre is static; the four intersections put the subject slightly off balance, which is what makes a frame feel alive.'),
]

GAPS = [
    ('A ______ has a fixed focal length and no zoom, but usually a wider maximum aperture than a zoom of the same price.',
     ['prime lens'],
     'A <strong>prime lens</strong> gives up zoom and gets aperture back &mdash; which buys you low light and shallow depth of field.'),
    ('The camera&rsquo;s ______ mode decides how it measures brightness: evaluative, centre-weighted or spot.',
     ['metering'],
     '<strong>Metering</strong> is how the camera reads the scene. Evaluative weighs the whole frame; spot reads a small circle and ignores everything else.'),
    ('______ means shooting the same scene several times at different exposures, usually a stop apart.',
     ['bracketing'],
     '<strong>Bracketing</strong> insures you against a scene you cannot meter reliably &mdash; and it is what HDR is built from.'),
    ('A ______ graphs the tones in an image, from black on the left to white on the right.',
     ['histogram'],
     'A <strong>histogram</strong> tells you what the screen cannot: data piled against either edge is <em>clipped</em>, and that detail is gone.'),
    ('______ is a lens fault where different wavelengths do not focus at one point, leaving coloured fringes.',
     ['chromatic aberration'],
     '<strong>Chromatic aberration</strong> shows up as purple or green edging on high-contrast boundaries &mdash; branches against a bright sky, most often.'),
    ('______ is the darkening towards the corners of a frame &mdash; a lens artefact, or added deliberately afterwards.',
     ['vignetting'],
     '<strong>Vignetting</strong> is a fault when the lens does it and a technique when you do: darkened corners hold the eye in the middle of the frame.'),
]
BANK = sorted(['prime lens', 'metering', 'bracketing', 'histogram',
               'chromatic aberration', 'vignetting', 'zone system', 'panning'])

MATCH = [
    ('White balance', 'Adjusts colour rendering for the light source'),
    ('RAW format', 'Unprocessed sensor data, for maximum editing latitude'),
    ('EV', 'A scale of equivalent aperture and shutter combinations'),
    ('Panning', 'Moving with the subject to keep it sharp against a blur'),
    ('Zone system', 'Eleven tonal steps from pure black to pure white'),
]

WORKFLOW = ['Brief &mdash; agree the client&rsquo;s requirements and visual references',
            'Recce &mdash; visit the location, note the light and the hazards',
            'Capture &mdash; shoot, adjusting as the conditions change',
            'Edit &mdash; select, grade and retouch',
            'Deliver &mdash; export in the agreed formats and hand over']

CHIPS = ['depth of field', 'shutter speed', 'stop down / open up', 'bokeh',
         'the rule of thirds', 'bracketing', 'clipped highlights', 'a recce']


def build():
    D.assert_no_key_is_longest(MC, 'Photography')
    pos = D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in GAPS for a in aa])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Advanced <em>Photography</em>',
                'The exposure triangle, the lens, and the words for what light is doing',
                [('Level', 'B2 &middot; Upper-intermediate'), ('Focus', 'Photography'),
                 ('Count', '16 slides')])
        + D.teach('expEyebrow', 'Before the questions &middot; 1 of 3',
                  'expTitle', 'The exposure triangle &mdash; three ways to the same brightness',
                  [('e1h', 'Aperture &mdash; f/1.8 to f/22',
                    'How wide the lens opens. Low number = wide.',
                    'e1b', 'Also sets <strong>depth of field</strong>: wide open, only the eyes are sharp; stopped down, the whole street is.'),
                   ('e2h', 'Shutter &mdash; 1/1000s to 30s',
                    'How long the sensor is exposed.',
                    'e2b', 'Also decides <strong>motion</strong>: fast freezes the athlete, slow turns them into a streak. This is the creative choice, not just the exposure one.'),
                   ('e3h', 'ISO &mdash; 100 to 25,600',
                    'How hard the signal is amplified afterwards.',
                    'e3b', 'Costs you <strong>noise</strong>. ISO is what you spend when aperture and shutter are already committed &mdash; a payment, not a free gain.')],
                  folder=F)
        + D.teach('lensEyebrow', 'Before the questions &middot; 2 of 3',
                  'lensTitle', 'The lens, and the four faults it is known by',
                  [('l1h', 'prime vs zoom',
                    'A <strong>prime</strong> has one focal length and no zoom.',
                    'l1b', 'In exchange it opens wider than a zoom at the same price &mdash; which is the whole reason people carry them.'),
                   ('l2h', 'bokeh',
                    'The <em>character</em> of the out-of-focus areas.',
                    'l2b', 'Not how much blur, but what kind. Smooth round highlights are prized; busy, edged ones are not.'),
                   ('l3h', 'chromatic aberration',
                    'Wavelengths that fail to focus at one point.',
                    'l3b', 'Coloured fringing &mdash; purple or green &mdash; on high-contrast edges. Branches against a bright sky show it first.'),
                   ('l4h', 'vignetting',
                    'The corners darker than the centre.',
                    'l4b', 'A fault when the lens does it, a technique when you do: it holds the eye in the middle of the frame.')],
                  cols='1fr 1fr 1fr 1fr', folder=F)
        + D.teach('compEyebrow', 'Before the questions &middot; 3 of 3',
                  'compTitle', 'Reading the light, and arranging the frame',
                  [('c1h', 'Metering &amp; the histogram',
                    '<strong>Metering</strong> reads the scene; the <strong>histogram</strong> reports it.',
                    'c1b', 'Black on the left, white on the right. Data piled against either edge is <em>clipped</em> &mdash; that detail no longer exists.'),
                   ('c2h', 'Bracketing',
                    'Several frames, a stop apart, of the same scene.',
                    'c2b', 'Insurance against light you cannot meter &mdash; and the raw material of HDR.'),
                   ('c3h', 'Composition',
                    '<strong>Rule of thirds</strong> &middot; leading lines &middot; negative space',
                    'c3b', 'The thirds grid gives four intersections. Dead centre is static; slightly off is what makes a frame move.')],
                  folder=F, bg='motel.jpg')
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Through the lens',
                       'qTitle', 'Choose the precise term', folder=F,
                       bg='motel.jpg' if i % 2 else None)
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 2, part, BANK, 'gapEyebrow', 'The exact word',
                        'gapTitle', 'Develop your vocabulary', folder=F,
                        hint_key='gapHint',
                        hint='Two of the eight words in the bank belong to no gap here.',
                        width=220, size=18)
                  for n, part in enumerate([GAPS[:3], GAPS[3:]]))
        + D.match(MATCH, 'matchEyebrow', 'Term and definition',
                  'matchTitle', 'Five you will meet in any camera menu',
                  'matchHint', 'Click a term, then click its definition.',
                  'One worth stating precisely: EV is a scale of equivalent aperture-and-shutter combinations, not a measure of how much light reached the sensor. Every setting on one EV step gives the same exposure by a different route.',
                  folder=F)
        + D.order(WORKFLOW, 'ordEyebrow', 'The commission',
                  'ordTitle', 'Put the professional workflow in order',
                  'ordHint', 'Click the stages in the order they happen.',
                  'The brief defines what the pictures are for; the recce is what stops the shoot day producing surprises. Both come before anyone takes a photograph, and both are the stages amateurs skip.',
                  folder=F, bg='motel.jpg')
        + D.results('resNext', 'You have the words. Now use them on a real picture →')
        + D.activate('Talk about a photograph', 'Use at least four:', CHIPS,
                     'Discussion &middot; in pairs',
                     'Bring one photograph each &mdash; yours, or one you admire. Describe it technically.',
                     ['Guess the settings from the picture: wide or narrow aperture? Fast or slow shutter? How can you tell?',
                      'Where is the subject in the frame, and what would change if it were dead centre?',
                      'Your partner has taken a picture that is too dark. Diagnose it in three questions.',
                      'Argue for one of these: a prime lens, or a zoom. Use <em>depth of field</em> at least once.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write the brief for a shoot you would like to do: what it is for, who sees it, and what the light needs to be doing.',
                     'The brief: a series of six portraits, shot in available light,')
    )

    import i18n_photo as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Advanced Photography — B2', I)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, bank %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH),
             pos, len(s)))


if __name__ == '__main__':
    build()
