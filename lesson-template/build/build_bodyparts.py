# -*- coding: utf-8 -*-
"""Head to Toe (C1) — the body, part by part. Rebuild of a scrolling lesson.

Innes sent the coursebook page his student Andreas is working from (Body and
mind, unit 10, p.89: thirty-six body parts, ten idioms, seventeen verbs of
contact) and asked for a Forbes English lesson on all of it. The site already
held the same material as `forbes-english-body-parts-c1.html` — a five-tab
scrolling page, 61 items, built 2026-08 — so this is a §10 revamp rather than
a new lesson, and it keeps the filename so the URL a student may have
bookmarked still resolves.

**It is one lesson split in two, per HOUSE-STYLE §7.** The coursebook page
carries three exercises' worth of material and would not fit one deck under
twenty-four slides: this is the thirty-six words, and
`build_bodyidioms.py` is the ten idioms and the verbs. They ship together,
they share an art family, and either can be taught alone.

What the old page had, and what happened to it:

  * its 33 definitions were tightened from ~22 words to ~12 so that six fit a
    match grid without shrinking type (§6), and the register was kept;
  * its German glosses survive in the match feedback — see i18n_bodyparts's
    docstring for why they cannot sit under the term;
  * **cheek, earlobe and jaw were missing** from the old lesson entirely,
    though all three are on the coursebook page. They are taught here, and
    all three were added to the face plate, which did not carry them either;
  * temple is kept, though the coursebook does not have it. It is the word a
    C1 learner reaches for when a headache is being described and it costs
    nothing to leave in.

The three anatomical plates in BodyParts/ are the old lesson's own artwork
(§10: bespoke diagrams are the best thing in an old file). Each shows whole
on a divider and then, **stripped of its labels**, behind that stage's
questions — a labelled chart behind a matching round is an answer key.
`plates_bodyparts.py` does the stripping, the leader-line halos and the
JPEGs; run it before this if a plate changes.

Light theme: the artwork is cream and navy line work, and §4a is explicit
that bright art belongs in a light deck rather than being forced dark.

    py lesson-template/build/plates_bodyparts.py     # only if a plate changed
    py lesson-template/build/build_bodyparts.py
    node lesson-template/check-lesson.js forbes-english-body-parts-c1.html
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_bodyparts as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-body-parts-c1.html'

F = 'BodyParts'
E = I.T['en']

# The picture slots, in one place. Innes is supplying proper artwork (2026-09-19);
# when it lands, these seven values are the whole edit — every slide names its
# background through this map. The three CHART_* entries are the labelled
# anatomy plates and are NOT candidates for generated art: they carry the
# thirty-six words as leader-line labels, which an image generator cannot write.
# The BG_* entries are their wordless counterparts, and a supplied picture
# replaces those, never the charts.
CHART_FACE = 'face-neck.jpg'
CHART_TORSO = 'torso-organs.jpg'
CHART_LIMBS = 'limbs-extremities.jpg'

HERO = 'hero.jpg'
BG_FACE = 'face-plain.jpg'
BG_TORSO = 'torso-plain.jpg'
BG_LIMBS = 'limbs-plain.jpg'
BG_TALK = 'speaking.jpg'

# Mechanically derived — the verbatim output of
#     py lesson-template/extract-palette.py BodyParts/hero.jpg --light
# Contrast report: PASS on all eight rows, the tightest being accent on
# surface at 4.88:1 against a 4.5 floor. Never hand-pick a value in here.
PALETTE = '''  --hero: url('%s/%s');

  --void          : #d8c9ad;
  --surface       : #e1d8c5;
  --surface2      : #dcd0b8;
  --border        : #964a59;
  --text          : #2a1116;
  --text-dim      : #5e2e38;
  --accent        : #b60226;
  --accent-bright : #85001b;
  --accent-dim    : #ef4466;
  --secondary     : #f1ebdf;
  --contrast      : #075520;

  /* Raised from the 0.68 default, for the text plates ONLY.

     What this does and does not touch is worth stating, because the obvious
     reading is wrong: on a light deck `.card` and `.opt` do not follow
     --plate at all — lesson-template.html's light-theme rules fix them at
     92%% and 95%% of --surface — so this moves only --plate-bg, the plate
     behind an uncarded run: slide titles, eyebrows, task hints, question
     stems. Those are exactly the runs that sit straight on the artwork, and
     these plates have one very dark mass in them (a navy head, a navy arm)
     rather than an even field.

     Measured over all 70 uncarded text runs in the deck, sampling the
     darkest composited pixel under each and contrasting it against --text:
     worst 6.55:1 at 0.68, 8.98:1 at 0.94. Both clear AA; the raise buys
     comfort rather than rescuing a failure. Carded text measures 11.08:1 at
     either value, which is the same number twice because the card ignores
     the variable. */
  --plate         : 0.94;''' % (F, HERO)


# ── the thirty-six words ────────────────────────────────────────────────
# Definitions run 9-14 words. The old lesson's were 18-24, which is a fine
# length in a scrolling list and a slide overflow in a six-pair match grid.
# Nothing defining was dropped in the shortening; the padding was.
FACE_UPPER = [
    ('forehead', 'the smooth expanse between the eyebrows and the hairline'),
    ('temple', 'the flat area at the side of the head, just behind the eye'),
    ('eyebrow', 'the arch of hair above the eye socket, raised to signal surprise'),
    ('eyelash', 'one of the fine hairs fringing the lid, keeping grit out'),
    ('nostril', 'either of the two openings that draw air into the nose'),
    ('earlobe', 'the soft hanging tip of the ear, where a stud goes'),
]

FACE_LOWER = [
    ('cheek', 'the fleshy side of the face, between the eye and the jaw'),
    ('lip', 'one of the two soft edges framing the mouth'),
    ('chin', 'the point at the front of the lower jaw, below the mouth'),
    ('jaw', 'the hinged bone that opens and closes the mouth'),
    ('throat', 'the passage inside the neck, shared by air and food'),
    ('neck', 'the column of muscle and bone joining the head to the shoulders'),
]

TRUNK_FRAME = [
    ('chest', 'the front of the torso between the neck and the stomach'),
    ('waist', 'the narrowest part of the torso, where a belt sits'),
    ('hip', 'the joint at the side of the pelvis where the leg pivots'),
    ('pelvis', 'the basin of bone at the base of the spine'),
    ('spine', 'the column of stacked vertebrae running down the back'),
    ('rib', 'one of the curved bones arcing from the spine round the chest'),
]

TRUNK_INSIDE = [
    ('stomach', 'the sac where swallowed food is churned before the intestines'),
    ('lung', 'one of a pair of spongy organs that draw oxygen into the blood'),
    ('liver', 'the large organ under the right ribs that filters the blood'),
    ('kidney', 'one of a pair of bean-shaped organs that make urine'),
    ('intestines', 'the long coiled tube where digestion is finished'),
    ('veins', 'the vessels carrying blood back towards the heart'),
]

ARM_HAND = [
    ('armpit', 'the hollow beneath the shoulder where the arm meets the torso'),
    ('elbow', 'the hinge halfway along the arm, above the forearm'),
    ('wrist', 'the joint that lets the hand turn and bend on the arm'),
    ('palm', 'the flat inner surface of the hand, below the fingers'),
    ('knuckle', 'one of the joints along a finger, prominent in a clenched fist'),
    ('thumb', 'the short, opposed digit that gives the hand its grip'),
]

LEG_FOOT = [
    ('thigh', 'the thick upper leg, from the hip down to the knee'),
    ('shin', 'the sharp front edge of the lower leg, below the knee'),
    ('calf', 'the muscular back of the lower leg'),
    ('ankle', 'the joint connecting the foot to the leg'),
    ('heel', 'the rounded back of the foot, beneath the ankle'),
    ('sole', 'the underside of the foot, which meets the ground'),
]

MATCHES = [
    (FACE_UPPER, 'm1', 's1Eyebrow', 'face-plain.jpg'),
    (FACE_LOWER, 'm2', 's1Eyebrow', 'face-plain.jpg'),
    (TRUNK_FRAME, 'm3', 's2Eyebrow', 'torso-plain.jpg'),
    (TRUNK_INSIDE, 'm4', 's2Eyebrow', 'torso-plain.jpg'),
    (ARM_HAND, 'm5', 's3Eyebrow', 'limbs-plain.jpg'),
    (LEG_FOOT, 'm6', 's3Eyebrow', 'limbs-plain.jpg'),
]


# ── consolidation ───────────────────────────────────────────────────────
# Three kinds, no item that could honestly go in two bins: a sort whose
# items are arguable tests nerve rather than knowledge.
SORT_ITEMS = [
    ('rib', 0), ('spine', 0), ('pelvis', 0),
    ('liver', 1), ('lung', 1), ('kidney', 1), ('stomach', 1), ('intestines', 1),
    ('elbow', 2), ('wrist', 2), ('knuckle', 2), ('ankle', 2), ('hip', 2),
]

ORDER = ['forehead', 'jaw', 'throat', 'chest', 'waist', 'thigh', 'shin', 'heel']


# ── multiple choice ─────────────────────────────────────────────────────
# Every stem is a question ABOUT English with no blank in it, so both it and
# its context line carry keys and translate (deck.mc's docstring). The
# options never do: they are the words under test. No key is the longest
# option on its slide — D.assert_no_key_is_longest checks it at build time.
QUESTIONS = [
    dict(stem=E['q1Stem'], stem_key='q1Stem', ctx=E['q1Ctx'], ctx_key='q1Ctx',
         options=['shin', 'thigh', 'calf', 'heel'], correct=2,
         bg=BG_LIMBS,
         why='The <strong>calf</strong> is the muscle at the back of the lower leg. '
             'The <em>shin</em> is the bone in front of it, the <em>thigh</em> is above '
             'the knee, and the <em>heel</em> is part of the foot.'),
    dict(stem=E['q2Stem'], stem_key='q2Stem', ctx=E['q2Ctx'], ctx_key='q2Ctx',
         options=['neck', 'throat', 'jaw', 'chin'], correct=1,
         bg=BG_FACE,
         why='Swallowing happens in the <strong>throat</strong>, which is inside. The '
             '<em>neck</em> is the outside of the same region: you get a stiff neck from '
             'sleeping badly, not from a cold.'),
    dict(stem=E['q3Stem'], stem_key='q3Stem', ctx=E['q3Ctx'], ctx_key='q3Ctx',
         options=['knuckle', 'palm', 'thumb', 'wrist'], correct=3,
         bg=BG_LIMBS,
         why='The <strong>wrist</strong> joins the hand to the forearm. A '
             '<em>knuckle</em> is a joint in a finger, and the <em>palm</em> is a surface '
             'rather than a joint at all.'),
    dict(stem=E['q4Stem'], stem_key='q4Stem', ctx=E['q4Ctx'], ctx_key='q4Ctx',
         options=['shin', 'ankle', 'wrist', 'knuckle'], correct=0,
         bg=BG_LIMBS,
         why='The <strong>shin</strong> is a surface, not a meeting of two bones. That is '
             'why you bark or bruise a shin but sprain an ankle, a wrist or a knuckle.'),
    dict(stem=E['q5Stem'], stem_key='q5Stem', ctx=E['q5Ctx'], ctx_key='q5Ctx',
         options=['lung', 'kidney', 'liver', 'stomach'], correct=2,
         bg=BG_TORSO,
         why='The <strong>liver</strong> sits under the ribs on the right and filters the '
             'blood. The <em>kidneys</em> are lower, at the back, and make urine; both are '
             'paired, the liver is not.'),
]


# ── gap fill ────────────────────────────────────────────────────────────
GAPS = [
    dict(title_key='g1Title', hint_key='g1Hint', bg=BG_FACE,
         bank=['ankle', 'chest', 'rib', 'shin', 'throat', 'wrist'],
         rows=[
             ('I came off my bike and put a hand out to stop the fall &mdash; now I '
              'can&rsquo;t bend my ______ at all.', ['wrist'],
              'The joint between hand and forearm. A <strong>knuckle</strong> is further '
              'out, in the finger itself.'),
             ('It catches when I breathe in, just here on the left. I think I&rsquo;ve '
              'cracked a ______.', ['rib'],
              'One bone of the cage round the chest. <strong>Cracked a rib</strong> is the '
              'everyday phrase for it.'),
             ('Swallowing hurts and my voice has gone &mdash; my ______ has been raw '
              'since Sunday.', ['throat'],
              'Inside the neck. A sore <strong>throat</strong>; a stiff <em>neck</em> is '
              'the outside, and a different complaint.'),
         ]),
    dict(title_key='g2Title', hint_key='g2Hint', bg=BG_LIMBS,
         bank=['calf', 'heel', 'hip', 'palm', 'thumb', 'waist'],
         rows=[
             ('These new boots have rubbed a blister on my left ______.', ['heel'],
              'The rounded back of the foot. The <strong>sole</strong> is underneath it '
              '&mdash; and a shoe has one too.'),
             ('I pulled a muscle in my right ______ running for the bus.', ['calf'],
              'The muscle behind the lower leg. You <strong>pull</strong> a muscle; the '
              '<em>shin</em> in front is bone, and you bark that instead.'),
             ('She came off her bike at eighty-one and broke her ______, which at that '
              'age means an operation.', ['hip'],
              'The joint where the leg meets the pelvis. <strong>Breaking a hip</strong> '
              'is the injury that changes an older person&rsquo;s year.'),
         ]),
]


CHIPS = ['a stiff neck', 'a sore throat', 'a sprained ankle', 'a bruised shin',
         'a pulled calf muscle', 'a swollen knuckle',
         'it hurts when I breathe in']

SPEAK = [E['actSpeak1'], E['actSpeak2'], E['actSpeak3'], E['actSpeak4']]


def build():
    logo = D.logo_from(TPL)
    D.assert_no_key_is_longest(QUESTIONS)
    for g in GAPS:
        D.assert_bank_is_not_a_key(g['bank'], [r[1][0] for r in g['rows']])

    def match_slide(pairs, key, eyebrow_key, bg):
        return D.match(pairs, eyebrow_key, E[eyebrow_key],
                       key + 'Title', E[key + 'Title'],
                       key + 'Hint', E[key + 'Hint'],
                       key + 'Why', folder=F, bg=bg)

    slides = "".join(
        [D.cover(logo, E['coverTitle'], E['coverSub'],
                 [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                  ('Count', E['chipCount'])])]

        # ── stage 1: above the collarbone ──
        + [D.divider('d1Title', E['d1Title'], 'd1Note', E['d1Note'],
                     folder=F, pic=CHART_FACE)]
        + [match_slide(*MATCHES[0])]
        + [match_slide(*MATCHES[1])]
        + [D.teach('t1Eyebrow', E['t1Eyebrow'], 't1Title', E['t1Title'],
                   [(None, 'neck &middot; throat', 't1b1', E['t1b1'], 't1n1', E['t1n1']),
                    (None, 'jaw &middot; chin', 't1b2', E['t1b2'], 't1n2', E['t1n2']),
                    (None, 'forehead &middot; temple', 't1b3', E['t1b3'], 't1n3', E['t1n3'])],
                   folder=F, bg=BG_FACE)]

        # ── stage 2: the trunk ──
        + [D.divider('d2Title', E['d2Title'], 'd2Note', E['d2Note'],
                     folder=F, pic=CHART_TORSO)]
        + [match_slide(*MATCHES[2])]
        + [match_slide(*MATCHES[3])]

        # ── stage 3: the limbs ──
        + [D.divider('d3Title', E['d3Title'], 'd3Note', E['d3Note'],
                     folder=F, pic=CHART_LIMBS)]
        + [match_slide(*MATCHES[4])]
        + [match_slide(*MATCHES[5])]
        + [D.teach('t2Eyebrow', E['t2Eyebrow'], 't2Title', E['t2Title'],
                   [(None, 'sprain a joint', 't2b1', E['t2b1'], 't2n1', E['t2n1']),
                    (None, 'shin &middot; calf', 't2b2', E['t2b2'], 't2n2', E['t2n2']),
                    (None, 'palm &middot; sole', 't2b3', E['t2b3'], 't2n3', E['t2n3'])],
                   folder=F, bg=BG_LIMBS)]

        # ── consolidation ──
        + [D.sort_slide([E['sortBin1'], E['sortBin2'], E['sortBin3']], SORT_ITEMS,
                        'sortEyebrow', E['sortEyebrow'], 'sortTitle', E['sortTitle'],
                        'sortHint', E['sortHint'], 'sortWhy', folder=F,
                        bg=BG_TORSO,
                        bin_keys=['sortBin1', 'sortBin2', 'sortBin3'])]
        + [D.order(ORDER, 'ordEyebrow', E['ordEyebrow'], 'ordTitle', E['ordTitle'],
                   'ordHint', E['ordHint'], 'ordWhy', folder=F, bg=BG_FACE)]

        + [D.mc(i + 1, len(QUESTIONS), q, 'qEyebrow', E['qEyebrow'],
                'qTitle', E['qTitle'], folder=F, bg=q['bg'],
                ctx=q['ctx'], ctx_key=q['ctx_key'], stem_key=q['stem_key'])
           for i, q in enumerate(QUESTIONS)]

        + [D.gap(i + 1, len(GAPS), g['rows'], g['bank'],
                 'gapEyebrow', E['gapEyebrow'],
                 g['title_key'], E[g['title_key']],
                 hint=E[g['hint_key']], hint_key=g['hint_key'],
                 width=150, folder=F, bg=g['bg'])
           for i, g in enumerate(GAPS)]

        + [D.results('resNext', E['resNext'], folder=F, bg=BG_TALK)]

        + [D.activate(E['actTitle'], E['actUse'], CHIPS,
                      E['actSpeakKind'], E['actSpeakBrief'], SPEAK,
                      E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                      folder=F, bg=BG_TALK)]
    )

    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Head to Toe: The Body, Part by Part (C1)',
                   I, langs=('en', 'de', 'es'))

    # The chip says the number check-lesson.js reports, which is one less than
    # the raw count — the template's authoring comment contains the string
    # too. Patched in every language, or it changes when a learner switches.
    n = s.count('<section class="slide') - 1
    s = s.replace('NSLIDES', str(n))
    open(OUT, 'w', encoding='utf-8', newline='').write(s)

    pairs = sum(len(m) for m, _, _, _ in MATCHES)
    gap_pts = sum(len(g['rows']) for g in GAPS)
    print('wrote %s - %d slides, %d scored (%d match, %d sort, 1 order, %d mc, '
          '%d gap), %d bytes'
          % (OUT, n, pairs + len(SORT_ITEMS) + 1 + len(QUESTIONS) + gap_pts,
             pairs, len(SORT_ITEMS), len(QUESTIONS), gap_pts, len(s)))


if __name__ == '__main__':
    build()
