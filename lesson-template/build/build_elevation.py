# -*- coding: utf-8 -*-
"""Reading the Elevation (C1) — new lesson, built to the deck house style.

Source is a vocabulary list Innes supplied — a long mixed export, of which
about thirty-six items are the language of describing buildings. Everything
architectural in the list is taught here: the fabric words (galvanized,
perforated, corroded, inert, dead weight, conduit), the decay words
(dilapidated, run-down, vestige, vestigial, conserve), the openings
(fenestration, defenestration, articulation, threshold, liminal, promenade),
the words for what a building does to the eye (conspicuous, obtrusive,
unobtrusive, eye-catching, suspended, overarching, trapezoid), and the words
for how a building treats its neighbours (pastiche, homage, revere, venerate,
juxtaposition, reductive, artisanal, meticulous, rigorous, a stone's throw,
continuum, all-encompassing).

Five Black Isler architectural illustrations came with the brief. The Noma
Bar-style cantilevered house is the cover and drives the palette — it measures
0.51 mean luminance, so house-style 4a puts it in the LIGHT theme; the accent
comes back as the building's own navy and the secondary as its coral. The
other four rotate as per-section backgrounds: the red cantilever on the fabric
slides, the dusk skyline on the decay slides, the pen-and-ink skyline on the
history slides, and the bare line drawing wherever the slide is dense.

Two things worth carrying forward:

  * The MC key is rotated to n % 4 at build time. Authoring every item with the
    key first is the readable way to write fourteen of them, but the source
    order survives into the PDF export and check-lesson.js fails the deck for
    it. Rotation, not shuffling, so the spread is exactly even.
  * The word bank is alphabetical and shared across all three gap slides, so
    the third slide's two answers had to be ordered meticulous-then-liminal.
    In the natural order they sat at bank positions 2 and 3 — ascending, which
    is the BANK gate's definition of an answer key.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'reading-the-elevation-c1.html'
F = 'ReadingTheElevation'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #babaca;
  --surface       : #ceced7;
  --surface2      : #c4c4d0;
  --border        : #4a7696;
  --text          : #111f2a;
  --text-dim      : #2e4a5e;
  --accent        : #095a95;
  --accent-bright : #013e6a;
  --accent-dim    : #379ae2;
  --secondary     : #f27463;
  --contrast      : #9c0d15;''' % F


def rotate(qs):
    """Move each key to position n % 4 so it is never parked on one letter."""
    out = []
    for n, q in enumerate(qs):
        opts = list(q['options'])
        key = opts.pop(q['correct'])
        tgt = n % 4
        opts.insert(tgt, key)
        out.append(dict(q, options=opts, correct=tgt))
    return out


# ── teaching slides: five, two cards each ──────────────────────────────
FABRIC = [
    (None, 'galvanized &middot; perforated &middot; corroded',
     'Steel dipped in zinc is <em>galvanized</em>, and does not rust. Metal pierced with a field of holes is <em>perforated</em>. Stone or metal eaten away by rain and chemistry has <em>corroded</em>.',
     None, 'Rust is one kind of corrosion &mdash; the kind that happens to iron.'),
    (None, 'inert &middot; dead weight &middot; conduit',
     '<em>Inert</em> means it cannot move itself. Its <em>dead weight</em> is what the structure carries before anybody walks in. A <em>conduit</em> is the tube that keeps cables out of sight.',
     None, 'Engineers say <em>dead load</em> for the building itself and <em>live load</em> for people, furniture and snow.'),
]

TIME = [
    (None, 'dilapidated &middot; run-down &middot; vestige',
     '<em>Dilapidated</em> is the strong word: gutters gone, roof open. <em>Run-down</em> is milder and stretches to a whole street. A <em>vestige</em> is what survives of something larger.',
     None, '<em>Vestigial</em> is the adjective &mdash; a vestigial chimney vents nothing and is kept anyway.'),
    (None, 'conserve &middot; revere &middot; venerate',
     'To <em>conserve</em> is to stop further harm and keep what is there, not to make it new. To <em>revere</em> is to hold in deep respect; to <em>venerate</em> is to do so almost devotionally.',
     None, 'Restoring returns a building to an earlier state. Conserving accepts the state it is in.'),
]

OPENINGS = [
    (None, 'fenestration &middot; articulation',
     '<em>Fenestration</em> is the arrangement of the windows and doors across one face of a building. <em>Articulation</em> is how its parts are jointed and visually separated.',
     None, '<em>Defenestration</em> looks like the opposite and is not: it means throwing a person out of a window.'),
    (None, 'threshold &middot; liminal &middot; promenade',
     'A <em>threshold</em> is the strip you cross at a door &mdash; and the level at which something starts to happen. A <em>liminal</em> space is neither one room nor the next: a lobby, a corridor, a stair.',
     None, 'A <em>promenade</em> is an unhurried public walk, and also the paved route built for it.'),
]

EYE = [
    (None, 'conspicuous &middot; eye-catching &middot; obtrusive &middot; unobtrusive',
     '<em>Conspicuous</em> is neutral: you cannot miss it. <em>Eye-catching</em> is praise. <em>Obtrusive</em> is a complaint &mdash; prominent and unwelcome. <em>Unobtrusive</em> is the compliment architects want most.',
     None, 'Only obtrusive carries its judgement inside the word.'),
    (None, 'suspended &middot; overarching &middot; trapezoid',
     '<em>Suspended</em> means hung from above. <em>Overarching</em> is literally arching over something, and figuratively the one idea the rest sit under. A <em>trapezoid</em> is a four-sided shape.',
     None, 'In American English a trapezoid has one pair of parallel sides; in British English that shape is a trapezium.'),
]

PAST = [
    (None, 'pastiche &middot; homage',
     'A <em>pastiche</em> imitates the style of another period or another architect. An <em>homage</em> acknowledges a source while still doing something of its own.',
     None, 'Pastiche is not automatically an insult. It becomes one when the imitation is all there is.'),
    (None, 'juxtaposition &middot; reductive &middot; artisanal',
     'A <em>juxtaposition</em> sets two things side by side so the contrast does the work. Calling a reading <em>reductive</em> says it has flattened something complicated. <em>Artisanal</em> means made by hand, by a trade.',
     None, '<em>Meticulous</em> and <em>rigorous</em> both mean careful &mdash; meticulous about detail, rigorous about method.'),
]

# ── section 1: the word the sentence wants ─────────────────────────────
PLACE = [
    dict(stem='The panels are <strong>______</strong> steel, which is why forty winters have left them unmarked.',
         options=['galvanized', 'corroded', 'perforated', 'suspended'], correct=0,
         why='Galvanized steel is coated in zinc, so it does not rust. Corroded is the opposite outcome, perforated is about holes, and suspended is about how a thing is held up.'),
    dict(stem='A critic praised &ldquo;the most confident <strong>______</strong> on the street&rdquo; &mdash; meaning the pattern of the windows.',
         options=['fenestration', 'defenestration', 'articulation', 'promenade'], correct=0,
         why='Fenestration is the arrangement of windows and doors on an elevation. Defenestration means throwing a person out of one &mdash; the two are unrelated, despite the spelling.'),
    dict(stem='The brick matches, the roofline continues, and the entrance is where you expect it. The annexe is <strong>______</strong>.',
         options=['unobtrusive', 'eye-catching', 'conspicuous', 'obtrusive'], correct=0,
         why='Unobtrusive means it does not push itself forward, and here that is praise. Conspicuous would mean you cannot miss it; obtrusive would add that you wish you could.'),
    dict(stem='The walkway is <strong>______</strong> from cables anchored in the roof, so nothing touches the ground between the towers.',
         options=['suspended', 'overarching', 'articulated', 'perforated'], correct=0,
         why='Suspended means hung from above. Compare cantilevered &mdash; held out from one end with nothing beneath it, which is what the house on the cover of this lesson is doing.'),
    dict(stem='Only a worn strip of stone marks the <strong>______</strong> between the street and the courtyard.',
         options=['threshold', 'continuum', 'vestige', 'conduit'], correct=0,
         why='A threshold is the strip you cross at a doorway. The same word names the level at which something begins &mdash; a pain threshold.'),
    dict(stem='Every joint was cut by hand in a workshop of eleven people. The work is <strong>______</strong> in the true sense, not the marketing one.',
         options=['artisanal', 'meticulous', 'reductive', 'inert'], correct=0,
         why='Artisanal means made by a skilled trade, by hand. Meticulous would describe the care taken, not the way the work was made.'),
    dict(stem='Reading the whole of post-war concrete as &ldquo;councils being mean&rdquo; is <strong>______</strong>.',
         options=['reductive', 'rigorous', 'liminal', 'overarching'], correct=0,
         why='Reductive means an account has flattened something complicated into something crude. Rigorous is close to the opposite charge.'),
    dict(stem='&ldquo;The station is <strong>a stone&rsquo;s throw</strong> from the office.&rdquo; How far is it?',
         options=['Close enough to walk in a couple of minutes.',
                  'About an hour on foot, at a steady pace.',
                  'Far enough that most people drive instead.',
                  'Somewhere between the two &mdash; nobody is certain.'], correct=0,
         why='A stone&rsquo;s throw is a very short distance. It is vague about the exact number of metres, never about whether the distance is short.'),
]

# ── section 2: the near miss ───────────────────────────────────────────
MISS = [
    dict(stem='A house built last year in a Georgian village: sash windows, a fanlight, a slate roof, copying the terraces on either side. A critic who dislikes it will call it a <strong>______</strong>.',
         options=['pastiche', 'homage', 'juxtaposition', 'vestige'], correct=0,
         why='A pastiche imitates the style of another period. An homage would acknowledge its source while doing something of its own &mdash; and the complaint here is that the imitation is all there is.'),
    dict(stem='Both words mean deep respect. Which one carries a devotional flavour, and is used of relics and saints as readily as of buildings?',
         options=['venerate', 'revere', 'conserve', 'concede'], correct=0,
         why='Venerate is the stronger, more religious word. Revere is broad and secular; conserve is about protecting fabric rather than about feeling.'),
    dict(stem='<strong>Defenestration</strong> is not the opposite of fenestration. What does it actually mean?',
         options=['Throwing a person out of a window.',
                  'Blocking up the windows of a building.',
                  'Fitting an elevation with too few windows.',
                  'Removing a window and bricking up the hole.'], correct=0,
         why='Defenestration is throwing someone out of a window, and by extension an abrupt removal from office. Fenestration is simply where the windows are.'),
    dict(stem='The conservation officer has refused permission to replace the eroded stone. She wants the wall <strong>______</strong>, not rebuilt.',
         options=['conserved', 'revered', 'perforated', 'suspended'], correct=0,
         why='To conserve is to halt further harm and keep what is there. Restoring or rebuilding would return the wall to an earlier state, which is exactly what she is refusing.'),
    dict(stem='A glass tower goes up beside a soot-black Victorian bank, and the whole point of the photograph is the collision between them. That collision is a <strong>______</strong>.',
         options=['juxtaposition', 'articulation', 'continuum', 'promenade'], correct=0,
         why='A juxtaposition is two things placed together so that the contrast does the work. A continuum would be the opposite &mdash; a range with no visible joins in it.'),
    dict(stem='<strong>Threshold</strong> has two everyday senses: the strip at a door, and one other. Which sentence uses the other one?',
         options=['Her threshold for noise is lower than mine.',
                  'He tripped on the threshold on his way in.',
                  'The threshold had been worn into a shallow dip.',
                  'They laid a brass threshold at the front door.'], correct=0,
         why='The second sense is the level something has to reach before it happens &mdash; a pain threshold, a threshold for noise. <em>Liminal</em> comes from the same Latin word, <em>limen</em>, a threshold.'),
]

# ── section 3: sorting ─────────────────────────────────────────────────
SORT_BINS = ['Praise', 'Neutral description', 'Complaint']
SORT_ITEMS = [
    ('eye-catching', 0), ('meticulous', 0), ('artisanal', 0), ('unobtrusive', 0),
    ('perforated', 1), ('galvanized', 1), ('suspended', 1), ('trapezoid', 1),
    ('obtrusive', 2), ('dilapidated', 2), ('run-down', 2), ('reductive', 2),
]
SORT_WHY = ('Eight of these carry a verdict inside the word. Perforated, galvanized, suspended and '
            'trapezoid describe a building without taking any view of it &mdash; which is exactly why a '
            'critic reaches for them when they want to sound fair. Note that <em>conspicuous</em> would '
            'not fit any of the three: it is the rare one that genuinely sits on the fence.')

# ── section 4: gap fill ────────────────────────────────────────────────
BANK = ['conduit', 'corroded', 'liminal', 'meticulous', 'obtrusive', 'vestige']
GAPS = [
    [('The chimney vents nothing now. It survives as a ______ of the brewery that stood here.',
      ['vestige'],
      'A vestige is a trace of something larger that has gone. The adjective is vestigial.'),
     ('Every cable is hidden inside a steel ______, so that nothing crosses the ceiling.',
      ['conduit'],
      'A conduit is a tube or channel that carries something through &mdash; wiring here, but the word works figuratively too.')],
    [('The extension is ______: you see it before you see the church it was added to.',
      ['obtrusive'],
      'Obtrusive is prominent <em>and</em> unwelcome. Conspicuous would report the prominence without the complaint.'),
     ('The stone has ______ where rain has run off the roof for a hundred and forty years.',
      ['corroded'],
      'Corrode is chemical wear over time. Rust is the specific case that happens to iron.')],
    [('Their survey of the roof was ______: all four thousand tiles were numbered.',
      ['meticulous'],
      'Meticulous is care about detail. Rigorous would be care about method &mdash; a rigorous survey has a defensible procedure, a meticulous one misses nothing.'),
     ('The lobby is a ______ space &mdash; you are no longer outside, and not yet at work.',
      ['liminal'],
      'Liminal means in between, on the threshold. Lobbies, stairwells and underpasses are the everyday examples.')],
]

# ── section 5: matching ────────────────────────────────────────────────
PAIRS = [
    ('a stone&rsquo;s throw', 'a very short distance away'),
    ('overarching', 'the one idea that all the others sit under'),
    ('all-encompassing', 'wide enough to take in every case'),
    ('continuum', 'an unbroken range with no clear steps in it'),
    ('vestigial', 'surviving only as a trace of something larger'),
    ('inert', 'unable to move by itself'),
]
MATCH_WHY = ('Overarching and all-encompassing both mean broad, but overarching implies a hierarchy '
             '&mdash; one idea above the rest &mdash; while all-encompassing is only about coverage. '
             'A continuum has no steps in it at all, which is why it is the wrong word for a contrast.')

# ── section 6: sentence building ───────────────────────────────────────
ORDER1 = ['The new wing', 'is clad in perforated brass', 'that has already begun to corrode',
          'into exactly the colour', 'the architects say they wanted']
ORDER1_WHY = ('The relative clause has to sit next to the brass it describes, and <em>corrode into</em> '
              'takes the colour as its destination. Move either one and the sentence says the wing '
              'corroded, not the brass.')
ORDER2 = ['A stone&rsquo;s throw from the cathedral', 'stands a trapezoid block',
          'whose unobtrusive brickwork', 'pays quiet homage', 'to the terraces behind it']
ORDER2_WHY = ('The sentence is inverted: the place comes first, and the verb <em>stands</em> comes '
              'before its subject, which is common in written description. Note <em>pay homage '
              '<strong>to</strong></em> &mdash; never <em>for</em>.')

CHIPS = ['fenestration', 'threshold', 'unobtrusive', 'obtrusive', 'pastiche', 'homage',
         'juxtaposition', 'conserve', 'vestige', 'liminal']


def build():
    D.assert_no_key_is_longest(PLACE, 'PLACE')
    D.assert_no_key_is_longest(MISS, 'MISS')
    for n, rows in enumerate(GAPS, 1):
        D.assert_bank_is_not_a_key(BANK, [a for _, ans, _ in rows for a in ans])

    place = rotate(PLACE)
    miss = rotate(MISS)
    D.assert_no_key_is_longest(place, 'PLACE(rotated)')
    D.assert_no_key_is_longest(miss, 'MISS(rotated)')

    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Reading the <em>Elevation</em>',
                'Thirty-six words for saying what a building is made of, what time has done to it, '
                'and how it treats the buildings next door',
                [('Level', 'C1 &middot; Vocabulary'),
                 ('Focus', 'Architecture &amp; description'),
                 ('Count', 'COUNT slides')])

        + D.teach('fabEyebrow', 'The fabric', 'fabTitle', 'What it is made of',
                  FABRIC, folder=F, bg='bg02.jpg')
        + D.teach('timeEyebrow', 'What time does', 'timeTitle',
                  'Decay, and the decision to stop it', TIME, folder=F, bg='bg04.jpg')
        + D.teach('openEyebrow', 'Openings', 'openTitle',
                  'The way in, and the way light gets in', OPENINGS, folder=F)
        + D.teach('eyeEyebrow', 'In the eye', 'eyeTitle',
                  'What the building does to you', EYE, folder=F, bg='bg05.jpg')

        + "".join(D.mc(i + 1, len(place), q, 'placeEyebrow', 'One word, in place',
                       'placeTitle', 'Which word does the sentence want?', folder=F,
                       bg=['bg02.jpg', None, 'bg03.jpg', None][i % 4])
                  for i, q in enumerate(place))

        + D.teach('pastEyebrow', 'Talking to the past', 'pastTitle',
                  'Copy, tribute, or collision', PAST, folder=F, bg='bg03.jpg')

        + "".join(D.mc(i + 1, len(miss), q, 'missEyebrow', 'The near miss',
                       'missTitle', 'Two words, one of them wrong', folder=F,
                       bg=['bg04.jpg', None, 'bg05.jpg'][i % 3])
                  for i, q in enumerate(miss))

        + D.sort_slide(SORT_BINS, SORT_ITEMS, 'sortEyebrow', 'Taking a view',
                       'sortTitle', 'Praise, description, complaint',
                       'sortHint',
                       'Some of these words judge the building. Some only describe it. Sort all twelve.',
                       SORT_WHY, folder=F, bg='bg05.jpg')

        + "".join(D.gap(i + 1, len(GAPS), rows, BANK, 'gapEyebrow', 'Fill the gap',
                        'gapTitle', 'One word from the bank per space', folder=F,
                        bg=['bg02.jpg', 'bg04.jpg', 'bg03.jpg'][i],
                        hint_key='gapHint',
                        hint='Case does not matter. Every word is used exactly once across the three slides.')
                  for i, rows in enumerate(GAPS))

        + D.match(PAIRS, 'matchEyebrow', 'Six more', 'matchTitle',
                  'Match the word to what it actually means', 'matchHint',
                  'Click a word, then click its meaning.', MATCH_WHY, folder=F, bg='bg03.jpg')

        + D.order(ORDER1, 'ordEyebrow', 'Build the sentence', 'ord1Title',
                  'A sentence about a material', 'ordHint',
                  'Click the parts in order &middot; click one again to take it back',
                  ORDER1_WHY, folder=F, bg='bg04.jpg')
        + D.order(ORDER2, 'ordEyebrow', 'Build the sentence', 'ord2Title',
                  'A sentence about a neighbour', 'ordHint',
                  'Click the parts in order &middot; click one again to take it back',
                  ORDER2_WHY, folder=F, bg='bg02.jpg')

        + D.results('resNext',
                    'You can name what you are looking at. Now describe a real building &rarr;',
                    folder=F, bg='bg05.jpg')

        + D.activate('Describe a building out loud', 'Use at least five:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs. One prompt each, two minutes, then swap. If you can finish a prompt without using the words above, you have answered a different question.',
                     ['Describe the nearest building you can see: its fenestration, its threshold, one material. Thirty seconds.',
                      'A developer wants to demolish a run-down warehouse. Argue for conserving it, not restoring it.',
                      'Defend a building your partner calls obtrusive. Use eye-catching, conspicuous and unobtrusive, and mean the difference.',
                      'A new terrace goes up in Georgian style. You say pastiche; your partner says homage.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write the walking-guide entry for one building you know well: what it is made of, what has happened to it, what it does to the eye, and how it treats its neighbours. No adjective twice.',
                     'From the bridge it reads as a single slab, until you notice &hellip;',
                     folder=F, bg='bg03.jpg')
    )

    import i18n_elevation as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Reading the Elevation — C1', I, langs=('en', 'de'))
    n = s.count('<section class="slide')
    s = s.replace('COUNT slides', '%d slides' % (n - 1))
    s = s.replace('chipCount: "28 slides"', 'chipCount: "%d slides"' % (n - 1))
    s = s.replace('chipCount: "28 Folien"', 'chipCount: "%d Folien"' % (n - 1))
    open(OUT, 'w', encoding='utf-8').write(s)
    # The engine scores a sort per ITEM and a match per PAIR, not one point per
    # slide, so the deck bar reads 40 rather than the 24 a per-slide count gives.
    scored = (len(place) + len(miss) + len(SORT_ITEMS)
              + sum(len(r) for r in GAPS) + len(PAIRS) + 2)
    print('wrote %s — %d sections, %d points (%d place, %d miss, %d sort items, '
          '%d gaps, %d match pairs, 2 order), %d bytes'
          % (OUT, n, scored, len(place), len(miss), len(SORT_ITEMS),
             sum(len(r) for r in GAPS), len(PAIRS), len(s)))


if __name__ == '__main__':
    build()
