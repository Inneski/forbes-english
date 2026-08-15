# -*- coding: utf-8 -*-
"""The Language of Geoscience (C1, technical English) — rebuilt as a 16:9 deck.

Same filename, so the live URL does not change.

**Two factual errors went out to a professional audience.** The feedback
on the water-saturation item told the reader that high water saturation
alongside high resistivity "can indicate … the presence of conductive
minerals". Conductive minerals — clay, pyrite — do the opposite: they
depress resistivity, and they are the classic cause of *low-resistivity
pay*, a good zone that logs as wet. They cannot explain an interval that
is both wet and highly resistive. The textbook explanation for that
combination — fresh, low-salinity formation water — was absent
altogether. It now has a slide of its own, with very low porosity and
deep mud-filtrate invasion as the other two candidates and the
conductive-mineral case named as the *opposite* anomaly. And the first
gap-fill stem said the formation "contained residual oil shows,
suggesting **active** generation and migration" while its own explanation
said that residual means immobile; residual shows are evidence that
migration happened at some stage, not that it is happening now, and the
stem says that instead.

**Every key sat in the same place.** The correct multiple-choice option
was data-position 1 in all six items and the gap answer was the first
chip in all six banks. A runtime shuffle hid it, but a static rebuild
reading the data in order would have rendered the answer as option A six
times. The thirteen multiple-choice keys here are deranged across all
four positions and the distribution is asserted at build time; the six
gap answers sit at bank positions 8, 1, 3, 7, 2 and 9 of one shared
twelve-term bank, so no order-of-appearance rule helps.

**The key was also the longest option in six of six**, four of them
strictly by character count, so a test-wise reader scored without
reading the stems. Two items added a lexical echo: only the key for
"dual porosity" mentioned pore space, and only the key for
"stratigraphic trapping" described a sealed accumulation. The
distractors have been lengthened — never the key shortened — and each of
those two items now seeds the stem's keyword into a distractor, so the
echo tells the reader nothing. The ANSWERS gate passes.

**There was no teaching stage anywhere in the lesson.** Twelve
substantive explanations existed only as post-answer feedback, and the
seven-pair matching activity had none at all: a reader who mispaired
never learned which pairing was right. Nineteen language slides now come
before the questions that use them, and the whole of the old feedback is
in them. The seven report terms are glossed on two slides before the
activity and then explained again, with a worked example sentence,
inside it.

**The matching activity could not be lost, and one slip cost two
marks.** A wrong pairing locked both items, consuming the true partners
of two different terms, so finishing with exactly one matching error was
impossible; the shared match engine in `deck.py` also allows unlimited
free retries, which is thirty-odd shipped lessons' worth of behaviour and
not this rebuild's decision to change. The seven pairs are now seven
one-per-slide multiple-choice items — the term quoted in a real report
sentence, four definitions, one attempt, its own explanation on every
wrong option. One error costs one mark, and a run of wrong answers scores
zero, which is verified by script rather than asserted.

**The score was a running ratio.** The readout was `correct / answered`,
starting at "0 / 0", while the progress bar divided by a fixed 19, so
mid-lesson a reader saw "3 / 4" against a 21% bar and never met the real
denominator until the end. The engine here shows `score / 19` from the
first slide, and there are exactly nineteen scored points: six phrase
items, six gaps, seven term items.

**It was a domain-knowledge test wearing an English-lesson skin.** The
stated audience is practising geoscientists, and it stays that audience —
but twenty-three distractor terms were never defined anywhere, and the
stems used *four-way closure*, *net pay*, *mud weight*, *bubble point*,
*cuttings* and *depth conversion* without glossing any of them (four-way
closure was defined only in the feedback of the item whose stem used it).
Those six have a glossary slide before Activity 1, the word bank's other
six terms are all taught on language slides, and every phrase tested is
explained before it is met. The geology is still the context; the English
is still the target.

Also corrected: "fault throw" is now the vertical *component* of
displacement, with heave named as the horizontal one; the overmature
source rock no longer "converted most of its organic content to gas or
lost it to cracking" — cracking is the mechanism, not an alternative to
it; and the cross-bedding item keeps its "consistent with a high-energy
fluvial environment" hedge, with a note that currents build cross-beds in
aeolian, tidal and deltaic settings too.

Not ported: the dead first `card.innerHTML` in `buildMatch()`, the
unreachable reselection branch in `pickFITB`, the answer key held as a
literal in an onclick attribute and re-derived by string-parsing it, the
gap that scored on first click with no chance to change one's mind, and
the two decorative SVGs with non-linear scales drawn as linear (the
header depth scale at 0 m / 500 / 1 km / 2 km / 3 km / 4 km on equal
spacing, and the seismic panel's TWT labels at 32/58/72/96 px for equal
0.2 s steps). This audience would have noticed both.

Artwork, and the one decision in the brief that had to be overruled.
The audit's Part E describes `Geoscience/hero.jpg` as "banded
sedimentary strata above a red plain" and `buttes.jpg` as Monument
Valley. The files do not match those labels. `hero.jpg` is an erupting
stratovolcano over the sea: a steep central-vent cone, an incandescent
column and an ash plume, with no sedimentary content in it at all.
`stratovolcano.jpg` is a second cone with an ash column, `volcano.jpg`
is a linear curtain of fire along an escarpment, and `fissure.jpg` is a
banded escarpment above a plain of what its filename says is lava. The
only file in the folder with no volcanic content is `buttes.jpg` —
Monument Valley, flat-lying banded strata above a red plain, which is
also exactly the picture the audit meant when it approved "banded
sedimentary strata above a red plain" for the cover.

So `buttes.jpg` is the hero here: the cover, the background pattern on
every interior slide, the palette source and the library thumbnail. It
is never captioned, in particular never as cross-bedding — the deck only
says cross-bedding is *consistent with* fluvial settings, and those
faces read as flat-lying strata.

The four eruption images are not used and are not referenced, which the
build asserts. This lesson is petroleum and sedimentary subsurface
geoscience from end to end: no eruption styles, no plate boundaries, no
magma, no lava. Putting an erupting cone on the cover of it would assert
a subject the deck never teaches, and captioning any of these four would
be a factual claim the reader has no means to check — a central-vent
stratovolcano and a fissure eruption are different things, and nothing
in the deck lets a reader tell them apart.

Light theme. The palette is pasted verbatim from
`extract-palette.py Geoscience/buttes.jpg --light`; every row of the
contrast report PASSES (text on surface 11.37:1, the weakest row —
border on surface — 3.07:1 against a 1.25 floor). Daylight, open sky
and pale ground is the house definition of a hero that belongs in a
light lesson.
"""
import re
import sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
import i18n_geo as I

TPL = '/home/claude/forbes-english/lesson-template/lesson-template.html'
OUT = '/home/claude/forbes-english/forbes-geoscience-phrases.html'
F = 'Geoscience'
E = I.T['en']

# The hero. Monument Valley: flat-lying banded strata above a red plain,
# and the only picture in the folder with no volcanic content in it —
# see the docstring for why the file called hero.jpg is not the hero.
HERO = 'buttes.jpg'

# Derived mechanically from Geoscience/buttes.jpg:
#   python3 lesson-template/extract-palette.py Geoscience/buttes.jpg --light
# Pasted verbatim; every row of the contrast report PASSES (text on
# surface 11.37:1, the weakest row — border on surface — 3.07:1 against a
# 1.25 floor). Light theme, so <html> also carries data-theme="light":
# setting one without the other gives dark chrome on paper.
PALETTE = '''  --hero: url('%s/%s');

  --void          : #d8c7ac;
  --surface       : #e1d6c4;
  --surface2      : #dcceb8;
  --border        : #96714a;
  --text          : #2a1e11;
  --text-dim      : #5e472e;
  --accent        : #8c4e0d;
  --accent-bright : #633404;
  --accent-dim    : #db8b39;
  --secondary     : #90a8ad;
  --contrast      : #095153;''' % (F, HERO)

# .q-ctx carries the report sentence a term is quoted from, above the
# question. The template styles its halo but not its size, so the rule
# lives here, as it does on the Nature Agency decks.
CSS = ('.q-ctx { font-size: 16px; line-height: 1.5; font-style: italic; '
       'color: var(--text-dim); border-left: 2px solid var(--accent-dim); '
       'padding-left: 14px; margin-bottom: 12px; max-width: 84ch; }\n'
       '.bank-chip { font-size: 13px; }\n'
       # The word bank and the hint above each gap are reading content,
       # and on this light deck they were the two blocks sitting on the
       # bare illustration: the mesa runs straight through them and the
       # dim hint measured worse than the body copy anywhere else. They
       # get the card treatment — translucent surface, 3px blur, a real
       # hairline — rather than a heavier wash over the whole slide,
       # which is the failure HOUSE-STYLE §5 warns about.
       '[data-type="gap"] .act-target,\n'
       '[data-type="gap"] .slide-body > .prose.dim {\n'
       '  background: color-mix(in srgb, var(--surface) 84%, transparent);\n'
       '  backdrop-filter: blur(3px);\n'
       '  border: 1px solid color-mix(in srgb, var(--border) 90%, transparent);\n'
       '  border-radius: 14px; padding: 9px 14px; }\n'
       '[data-type="gap"] .slide-body > .prose.dim { color: var(--text); }\n')


# ── guards ─────────────────────────────────────────────────────────────
def assert_key_is_deranged(mc, label='MC'):
    """The key was at data-position 1 in every item of the old file.

    A per-item fact cannot express what is wrong with that, so it is
    measured as a distribution across every multiple-choice item in the
    deck: all four positions used, none starved."""
    n = len(mc)
    keys = [q['correct'] for q in mc]
    counts = [keys.count(i) for i in range(4)]
    assert 0 not in counts, (
        '%s: position(s) %s never carry the key (%s)'
        % (label, [i for i, c in enumerate(counts) if not c], counts))
    assert max(counts) - min(counts) <= max(1, n // 5), (
        '%s: the key distribution is lopsided (%s)' % (label, counts))
    return counts


def assert_bank_is_deranged(bank, answers_in_gap_order):
    """The gap answer was bank[0] in all six items of the old file.

    One shared bank is used across the six gap slides, so the reader
    cannot learn "the answer is the first chip" or "the answers come in
    order". Both failure modes are checked: the positions must not all be
    equal, and they must not ascend (which is the BANK gate in
    check-lesson.js, measured over the deduplicated document order)."""
    pos = [bank.index(a) for a in answers_in_gap_order]
    assert len(set(pos)) > 1, 'every gap answer sits at bank position %d' % pos[0]
    assert not all(x < y for x, y in zip(pos, pos[1:])), (
        'the bank lists the gap answers in gap order (%s)' % pos)
    return pos


def assert_no_answer_is_shown(html):
    """Nothing may reveal an answer before it is given.

    The rule this enforces has bitten the site once already, as a
    `placeholder` attribute holding the accepted answer verbatim, so the
    first half is deliberately blunt: no scored input carries a
    placeholder at all. The second half checks the stem and the hint of
    every gap row against every accepted spelling of its own answer. The
    word bank is excluded by design — a bank the answer is missing from
    is not a bank — and `data-explain` is excluded because it is an
    attribute, written into the page only after marking."""
    for m in re.finditer(r'<input[^>]*class="gap"[^>]*>', html):
        assert 'placeholder' not in m.group(0), \
            'a gap input carries a placeholder: %s' % m.group(0)[:120]

    def visible(chunk):
        chunk = re.sub(r'<div class="act-target".*?</div>', '', chunk,
                       flags=re.S)          # the shared word bank
        chunk = re.sub(r'data-explain="[^"]*"', '', chunk)
        return re.sub(r'<[^>]+>', ' ', chunk).lower()

    for slide in re.findall(r'<section class="slide"[^>]*data-type="gap".*?'
                            r'</section>', html, re.S):
        chunks = slide.split('<div class="card gap-row"')
        head = visible(chunks[0])
        for chunk in chunks[1:]:
            found = re.findall(r'data-answer="([^"]+)"', chunk)
            # One gap per row, always: checkGaps marks the FIRST .gap in
            # each row while maxScore counts every .gap on the slide, so a
            # second input inside one row creates a point nobody can score.
            assert len(found) == 1, 'one gap per row, or scoring loses one'
            text = head + ' ' + visible(chunk)
            for alt in found[0].split('|'):
                assert alt.lower() not in text, \
                    'the accepted answer %r is readable before it is given' % alt


def mc_slide(i, total, q, ek, tk, folder='', bg=None):
    """D.mc, plus a per-distractor explanation.

    The shared builder writes one explanation per slide, which is what
    made right and wrong identical on all twelve explained items of the
    file this replaces. Rather than change a builder thirty lessons
    share, the attribute is injected here — the third lesson to do it
    this way: each wrong option says why *it* is wrong and the key falls
    through to the slide's own `why`. The engine already prefers an
    option's own explanation."""
    html = D.mc(i, total, q, ek, E[ek], tk, E[tk], folder=folder, bg=bg,
                ctx=q.get('ctx'))
    ex = q['opt_why']
    assert len(ex) == len(q['options']), 'opt_why must line up with options'
    assert ex[q['correct']] is None, 'the key takes the slide explanation'
    assert all(x for n, x in enumerate(ex) if n != q['correct']), \
        'every distractor needs its own explanation'
    parts = html.split('<button class="opt"')
    out = [parts[0]]
    for n, chunk in enumerate(parts[1:]):
        attr = ' data-explain="%s"' % D.esc(ex[n]) if ex[n] else ''
        out.append('<button class="opt"%s%s' % (attr, chunk))
    return ''.join(out)


def teach(ek, tk, cards, cols=None, bg=None):
    """cards: list of (head_key_or_None, body_html, note_key_or_None)."""
    return D.teach(ek, E[ek], tk, E[tk],
                   [(hk, E[hk] if hk else '', body, nk, E[nk] if nk else None)
                    for hk, body, nk in cards],
                   cols=cols, folder=F, bg=bg)


# ══ ACTIVITY 1 — six phrases in context ════════════════════════════════
# Keys at 2, 0, 3, 1, 3, 0. Every distractor is the same length as the key
# or longer, and in the first two items one distractor carries the stem's
# own keyword so that the lexical echo cannot be used to answer.
MC = [
    dict(correct=2,
         stem='A well completion report notes that <em>the reservoir exhibits '
              'dual porosity behaviour</em>, with significant implications for '
              'the production forecast.',
         options=[
             'The pore space drains in two stages because the well has been '
             'completed across two separate intervals of the same reservoir',
             'The reservoir pressure moves between two measurable states as '
             'the aquifer recharges the pore space from season to season',
             'Pore space sits in two systems &mdash; the rock matrix and a '
             'fracture network &mdash; which give up their fluid at very '
             'different rates',
             'The hydrocarbon column has two parts, a gas cap above and an oil '
             'leg below, divided by a mappable fluid contact'],
         why='Matrix pores hold most of the fluid and release it slowly; the '
             'fractures hold little but carry it to the wellbore. Treating the '
             'two as one system is what gets the flow rates wrong.',
         opt_why=[
             'Dual porosity is a property of the rock, not of the completion '
             'programme. It would still be there if the well had been drilled '
             'and completed in a single pass.',
             'Seasonal recharge belongs to shallow groundwater, not to a '
             'reservoir at depth &mdash; and the phrase describes the pore '
             'space itself, not a pressure that changes.',
             None,
             'That is a gas cap over an oil leg, separated by a fluid contact. '
             'It is a division of the <em>fluids</em>; dual porosity is a '
             'division of the <em>pore space</em>.']),

    dict(correct=0,
         stem='At peer review, the panel objects that the authors have not '
              'ruled out <em>stratigraphic trapping</em> as an explanation for '
              'the accumulation.',
         options=[
             'Hydrocarbons held in place by a change of rock type or porosity '
             'rather than by any deformation of the beds',
             'Hydrocarbons held in place by a fold or a sealing fault, with '
             'the closure defined by the shape of the structure',
             'Sedimentary particles becoming progressively locked together as '
             'burial compaction squeezes the pore volume out',
             'A seismic artefact created by velocity changes inside a layered '
             'sequence, which can mimic a real accumulation'],
         why='A pinch-out, a facies change or an unconformity does the sealing. '
             'Nothing has to be folded or faulted &mdash; which is also why '
             'these traps are subtler on seismic than structural ones.',
         opt_why=[
             None,
             'That is a <em>structural</em> trap, and it is the alternative '
             'the panel is contrasting it with. A stratigraphic trap needs no '
             'deformation at all.',
             'That describes compaction and cementation &mdash; a diagenetic '
             'process acting on the rock. It destroys pore space; it does not '
             'trap anything in it.',
             'That is a processing or velocity problem in the seismic image. '
             'A stratigraphic trap is a real feature of the rock, however hard '
             'it is to see.']),

    dict(correct=3,
         stem='A field geologist records that the exposed section shows '
              '<em>well-developed cross-bedding</em>, consistent with a '
              'high-energy fluvial environment.',
         options=[
             'Flat lamination formed as fine particles settle out of '
             'suspension in still water, one quiet layer at a time',
             'A network of intersecting fractures cutting across several '
             'bedding planes at a range of different orientations',
             'Beds of alternating grain size stacked in cycles, each of them '
             'recording a rise and fall of relative sea level',
             'Layers inclined inside a bed, built as dunes or ripples migrate '
             'and sediment avalanches down their lee face'],
         why='The dip direction of the foresets gives the palaeocurrent; the '
             'scale and angle of the sets give the energy of the flow. Hence '
             '&ldquo;consistent with&rdquo; a high-energy river.',
         opt_why=[
             'Still water and suspension settling give flat, parallel '
             'lamination. Cross-bedding needs a current strong enough to move '
             'grains along the bed.',
             'Fractures cut <em>across</em> bedding after the rock is lithified. '
             'Cross-beds are depositional: they are laid down inclined, inside '
             'the bed.',
             'That is cyclicity, read at the scale of a whole section. '
             'Cross-bedding is a structure inside a single bed.',
             None]),

    dict(correct=1,
         stem='A risking assessment concludes that the prospect has a low '
              'chance of success, primarily because of uncertainty over '
              '<em>seal integrity</em>.',
         options=[
             'The strength of the casing and the cement bond in the upper part '
             'of the planned wellbore, tested before drilling ahead',
             'The capacity of the cap rock above the reservoir to hold the '
             'hydrocarbon column and stop it leaking upward',
             'The degree to which an interpreted seismic horizon corresponds '
             'to a genuine geological boundary in the subsurface',
             'The quality of the confidentiality terms governing the exchange '
             'of data between the partners in a joint venture'],
         why='Shale, evaporite or tight carbonate, with pore throats fine '
             'enough to hold a buoyant column. It fails by faulting, by '
             'fracturing, or by capillary leakage through those throats.',
         opt_why=[
             'That is <em>well</em> integrity &mdash; a drilling and '
             'completion question. Seal integrity is a property of the rock '
             'above the reservoir, and it matters before a well exists.',
             None,
             'That is the reliability of the seismic interpretation. It is a '
             'real risk on a prospect, but it is not what the seal is or does.',
             'That is commercial confidentiality between partners. The word '
             '<em>seal</em> here is geological: the rock that keeps the '
             'column in the trap.']),

    dict(correct=3,
         stem='At a basin-scale conference presentation, the speaker argues '
              'that prospectivity depends on finding <em>mature source '
              'rock</em> within reach of a migration pathway.',
         options=[
             'Rock that has been fully compacted and cemented, so that no '
             'further loss of porosity can take place with burial',
             'Strata exposed at surface for long enough to be described, '
             'logged and sampled in detail by a field party',
             'A formation whose petrophysical properties are well established '
             'from several wells drilled in the same basin',
             'Organic-rich rock buried deep and hot enough to have generated '
             'hydrocarbons and expelled them into a carrier bed'],
         why='Maturity follows burial depth and temperature history. Below the '
             'oil window the kerogen has not generated; above it, the kerogen '
             'is spent and earlier oil has been cracked to gas.',
         opt_why=[
             'That is compaction and diagenesis, which act on any buried rock. '
             'Maturity is about the <em>organic matter</em> in it and the '
             'temperature it has reached.',
             'That is an outcrop being well described. <em>Mature</em> is a '
             'thermal state at depth, and a source rock at surface has stopped '
             'generating.',
             'That is a well-characterised reservoir, not a source rock. The '
             'two are different rocks doing different jobs in the same play.',
             None]),

    dict(correct=0,
         stem='A petrophysicist highlights an interval with <em>anomalously '
              'high water saturation</em> despite elevated resistivity '
              'readings, and recommends further analysis.',
         options=[
             'A share of the pore space filled with water that is larger than '
             'the other measurements would lead you to expect',
             'An unusually high concentration of dissolved salt in the '
             'formation water, which depresses the resistivity reading',
             'A borehole condition in which mud filtrate has invaded the '
             'near-wellbore rock to an unusually great depth',
             'A surface geochemical trace of shallow gas, picked up by '
             'sampling while the upper hole section was being drilled'],
         why='Wet and highly resistive at once points to fresh, low-salinity '
             'formation water, to very low porosity, or to deep invasion by '
             'resistive mud filtrate &mdash; and is why it is called anomalous.',
         opt_why=[
             None,
             'Saline water is a good conductor, so more salt means '
             '<em>lower</em> resistivity. That is the opposite of the '
             'combination described here.',
             'Invasion is one of the explanations an interpreter would test '
             'for this reading, but it is not what the phrase means. The '
             'phrase names the saturation itself.',
             'That is a surface geochemical survey. Water saturation is a '
             'petrophysical measurement made downhole, over a specific '
             'interval.']),
]

# ══ ACTIVITY 2 — six field-note sentences, one shared bank ═════════════
# Twelve chips, alphabetical, and every one of them is defined on a
# language slide before this activity starts. The old banks were five
# chips per item with the answer always first, and eleven of their
# eighteen distractors were terms defined nowhere in the lesson.
BANK = ['anticlinal crest', 'check-shot survey', 'effective porosity',
        'gas cap drive', 'hydrostatic gradient', 'overburden stress',
        'pore pressure', 'residual oil shows', 'solution gas drive',
        'structural closure', 'total porosity', 'two-way time']

GAPS = [
    ('h1', 'Geochemical analysis of the cuttings confirmed that the formation '
           'contained ______, so hydrocarbons had migrated along the fault '
           'corridor at some stage.',
     'residual oil shows',
     'Shows are visible or measurable traces of hydrocarbon in cuttings, core '
     'or mud. <strong>Residual</strong> means immobile &mdash; a '
     'palaeo-accumulation, or the tail of a column that has since moved on. '
     'They record that migration happened, not that it is happening now.', 215),

    ('h2', 'The structure map showed a well-defined ______ at about 2,400 '
           'metres subsea, with four-way closure confirmed by the seismic '
           'interpretation.',
     'anticlinal crest',
     'The crest is the highest point of the fold, and buoyant hydrocarbons '
     'collect there first if a seal is present above. With four-way closure '
     'the beds dip away on every side, so nothing has to be sealed by a '
     'fault.', 200),

    ('h3', 'Wireline analysis gave net pay of 18 metres, with ______ averaging '
           '22% once clay-bound water and isolated pores had been excluded.',
     'effective porosity',
     'Total porosity counts every void in the rock; the effective figure '
     'counts only the interconnected pore space available to flow, and it is '
     'the one that goes into the volumetrics. The exclusions in the sentence '
     'are what makes it effective.', 205),

    ('h4', 'The team saw a sharp rise in ______ while drilling the '
           'overpressured shale, and raised the mud weight at once to keep the '
           'well under control.',
     'pore pressure',
     'Pore pressure is the pressure of the fluid in the pore spaces. Where it '
     'runs above the hydrostatic gradient the interval is overpressured, and '
     'the mud weight has to be raised to balance it or the formation flows '
     'into the well.', 190),

    ('h5', 'Integrating the results of a ______ with the 3D seismic volume let '
           'the team calibrate the velocity model and improve the depth '
           'conversion of the reservoir target.',
     'check-shot survey|check shot survey|checkshot survey',
     'A receiver is lowered to known depths in the well and the travel time '
     'from surface is measured directly. That calibrates the velocity model '
     'used to turn two-way time into true vertical depth.', 210),

    ('h6', 'The reservoir model predicted that ______ would dominate recovery '
           'in the early production phase, given limited aquifer support and '
           'the absence of a gas cap.',
     'solution gas drive',
     'Below the bubble point, gas dissolved in the oil comes out of solution '
     'and expands, pushing oil toward the wellbore. With no aquifer and no gas '
     'cap it is what remains, and it is generally the least efficient of the '
     'three drives.', 210),
]

# ══ ACTIVITY 3 — the seven report terms ════════════════════════════════
# These replace a seven-pair matching board that could not be lost and
# whose wrong pairings locked two terms at a time. Keys at 1, 3, 2, 0, 1,
# 2, 0. Each item quotes the term in a report sentence, which is the
# worked example the matching activity never gave it.
TERMS = [
    dict(correct=1,
         ctx='&ldquo;Vitrinite reflectance in the deepest well averages 0.85% '
             'Ro, placing the shale squarely in the oil window.&rdquo;',
         stem='What does <em>vitrinite reflectance</em> measure?',
         options=[
             'The proportion of organic carbon still present in the shale, '
             'measured by combustion of a crushed sample',
             'The thermal maturity of the source rock, read from the '
             'reflectivity of organic particles in it',
             'The temperature at which the deepest sample in the well was '
             'recovered from the borehole wall',
             'The volume of oil the source rock has already expelled, as a '
             'fraction of its original potential'],
         why='Vitrinite particles reflect more light the hotter and longer '
             'they have been buried, so %Ro is read as a maturity scale: '
             'roughly 0.6&ndash;1.0% for the oil window.',
         opt_why=[
             'That is total organic carbon (TOC) &mdash; how much organic '
             'matter is present. Reflectance says how far the organic matter '
             'has been <em>cooked</em>, which is a different question.',
             None,
             'Nothing is measured at the moment of recovery. The reflectivity '
             'records the whole burial and temperature history of the sample, '
             'not the conditions in the borehole.',
             'That is the transformation ratio. Reflectance is measured '
             'optically on the particles themselves and says nothing directly '
             'about how much has left the rock.']),

    dict(correct=3,
         ctx='&ldquo;The bounding fault has a throw of about 40 metres at '
             'reservoir level, so the sand is juxtaposed against shale.&rdquo;',
         stem='What does the <em>throw</em> of a fault describe?',
         options=[
             'The horizontal component of the displacement, measured across '
             'the fault plane at right angles to it',
             'The total length of the fault plane where it cuts the mapped '
             'reservoir horizon in the subsurface',
             'The angle at which the fault plane dips away from the vertical '
             'as it passes through the section',
             'The vertical component of the displacement of the strata on '
             'either side of the fault plane'],
         why='Throw and heave are the two components of one displacement: '
             'throw is the vertical part, heave the horizontal. At 40 metres '
             'of throw the sand is offset against shale, which may seal it.',
         opt_why=[
             'That is the <em>heave</em> &mdash; the other component of the '
             'same displacement. Quoting it as the throw understates or '
             'overstates the offset at reservoir level.',
             'That is the length or extent of the fault, which a map shows. '
             'Throw is measured across the fault, not along it.',
             'That is the dip of the fault plane. It controls how throw and '
             'heave divide up the displacement, but it is not the throw '
             'itself.',
             None]),

    dict(correct=2,
         ctx='&ldquo;Mercury injection gave a capillary entry pressure high '
             'enough to hold a hydrocarbon column of about 200 metres.&rdquo;',
         stem='What is <em>capillary entry pressure</em>?',
         options=[
             'The pressure at which pore fluid in the seal begins to escape '
             'upward along a fault plane',
             'The pressure needed to fracture the cap rock and open a path '
             'through it for the hydrocarbons',
             'The pressure a non-wetting fluid needs to enter a pore throat '
             'and displace the wetting fluid',
             'The pressure below which gas dissolved in the oil column begins '
             'to come out of solution'],
         why='The finer the pore throats, the higher the entry pressure and '
             'the taller the column the seal can hold. It is measured in the '
             'laboratory by forcing mercury into a sample.',
         opt_why=[
             'That is leakage along a fault, one of the ways a seal fails. '
             'Entry pressure is a property of the seal&rsquo;s pore throats, '
             'measured before any fault is involved.',
             'That is the fracture pressure, and fracturing is a different '
             'failure mode. Capillary leakage happens through intact pore '
             'throats, without breaking the rock.',
             None,
             'That is the bubble point, which belongs to the fluid in the '
             'reservoir rather than to the seal above it.']),

    dict(correct=0,
         ctx='&ldquo;The gas&ndash;water contact was picked at 2,310 metres '
             'from the resistivity and density logs.&rdquo;',
         stem='What does a <em>gas&ndash;water contact</em> mark?',
         options=[
             'The level below which the pore space holds water rather than gas',
             'The level at which drilling mud first entered the gas-bearing '
             'sand',
             'The boundary between the reservoir sand and the cap rock '
             'above it',
             'The depth at which the well was cased before drilling ahead '
             'into water'],
         why='A fluid contact, not a rock boundary: the same reservoir '
             'continues below it, but the pore space is water-filled. It is '
             'picked from the logs and used to close the volumetrics.',
         opt_why=[
             None,
             'That is invasion by mud filtrate, which happens all along the '
             'open hole. The contact is a property of the reservoir, not of '
             'the drilling.',
             'That is the top of the reservoir. The contact sits inside the '
             'reservoir, wherever the gas gives way to water.',
             'That is a casing point, chosen for well control reasons. It has '
             'no necessary relationship to where the fluids change.']),

    dict(correct=1,
         ctx='&ldquo;Net-to-gross falls from 0.8 in the channel axis to below '
             '0.3 towards the margin of the fan.&rdquo;',
         stem='What does the <em>net-to-gross ratio</em> express?',
         options=[
             'The share of the recoverable oil that the operator expects to '
             'produce in the first five years',
             'The share of an interval that meets the cut-offs for being '
             'counted as reservoir',
             'The share of the drilled section that was cored rather than '
             'logged with wireline tools',
             'The share of the pore space occupied by hydrocarbons rather than '
             'by formation water'],
         why='Net thickness over gross thickness, once porosity, saturation '
             'and shale cut-offs are applied. It is the same idea as net pay, '
             'expressed as a ratio rather than a thickness.',
         opt_why=[
             'That is a production profile or a recovery factor. '
             'Net-to-gross is measured in the rock and is fixed before a '
             'single barrel is produced.',
             None,
             'That is core coverage, a data question. Net-to-gross is a '
             'property of the interval itself, however it was measured.',
             'That is hydrocarbon saturation, which is one of the cut-offs '
             'applied &mdash; but the ratio counts thickness, not pore '
             'volume.']),

    dict(correct=2,
         ctx='&ldquo;The shale below 3,000 metres is overpressured, and the '
             'casing point was moved up accordingly.&rdquo;',
         stem='What does <em>overpressure</em> mean?',
         options=[
             'Pressure in the drilling mud column that exceeds the strength of '
             'the exposed formation',
             'Pressure applied at the wellhead to hold the fluids back while '
             'the well is being completed',
             'Pore fluid pressure above the hydrostatic pressure expected at '
             'that depth',
             'Pressure in the reservoir that has been maintained by injecting '
             'water into the aquifer'],
         why='Usually a compacting shale that could not expel its water fast '
             'enough. The mud weight has to be raised to balance it, which is '
             'why the casing programme changes.',
         opt_why=[
             'That is over-balance, or at its extreme lost circulation '
             '&mdash; too <em>heavy</em> a mud fracturing the rock. '
             'Overpressure is in the formation, before any mud arrives.',
             'That is wellhead or annular pressure, an engineering measure at '
             'surface. Overpressure is measured in the pores at depth.',
             None,
             'That is pressure maintenance by water injection, a production '
             'operation. Overpressure is natural and is present before the '
             'field is developed.']),

    dict(correct=0,
         ctx='&ldquo;The facies association &mdash; cross-bedded sands passing '
             'up into bioturbated mudstone &mdash; points to a tidally '
             'influenced delta front.&rdquo;',
         stem='What is a <em>facies association</em>?',
         options=[
             'A group of related facies that together characterise one '
             'depositional environment',
             'A correlation between two wells in which the same bed is '
             'identified in both of them',
             'A set of sedimentary structures that all formed after burial, '
             'during diagenesis',
             'A list of the fossil species recovered from a single measured '
             'section of the outcrop'],
         why='One facies on its own is ambiguous; the company it keeps is not. '
             'Cross-bedded sand passing up into bioturbated mud is a delta '
             'front in a way that either bed alone is not.',
         opt_why=[
             None,
             'That is a well correlation. An association is read within one '
             'section, from what lies with what.',
             'Diagenetic features form after deposition. A facies records the '
             'conditions the sediment was <em>laid down</em> in.',
             'That is a faunal list. Fossils contribute to a facies, but the '
             'association is about the sediment as a whole.']),
]


def build():
    key_spread = assert_key_is_deranged(MC + TERMS, 'all multiple choice')
    D.assert_no_key_is_longest(MC, 'Activity 1')
    D.assert_no_key_is_longest(TERMS, 'Activity 3')
    bank_spread = assert_bank_is_deranged(
        BANK, [a.split('|')[0] for _, _, a, _, _ in GAPS])

    logo = D.logo_from(TPL)
    S = [D.cover(logo, E['coverTitle'], E['coverSub'],
                 [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                  ('Time', E['chipTime']), ('Count', E['chipCount'])])]

    # ── 2. who the deck is for ──
    S += [teach('tOrient', 'oT', [
        ('oa', 'The phrases here are the ones that turn up in well completion '
               'reports, prospect risking notes, wireline analyses and '
               'conference talks. The geology is the context; the English is '
               'the target.', None),
        ('ob', 'Every phrase in the three activities, and every term in the '
               'word bank, is explained on a slide before you meet it in a '
               'question. Read the language slides first.', 'on')],
        cols='1fr 1fr')]

    # ── 3. porosity ──
    S += [teach('tRes', 'p1T', [
        ('p1a', 'The intergranular pore space of the rock itself. It usually '
                'holds most of the fluid in the reservoir, but it gives that '
                'fluid up slowly.', None),
        ('p1b', 'The void space of a fracture network. It holds very little, '
                'but it drains quickly, so the fractures are the main conduits '
                'to the wellbore.', 'p1n')], cols='1fr 1fr')]

    # ── 4. traps ──
    S += [teach('tRes', 'p2T', [
        ('p2a', 'Deformation makes the closure: a fold &mdash; an anticline '
                '&mdash; or a fault sealing across the reservoir. The shape of '
                'the structure holds the hydrocarbons in.', None),
        ('p2b', 'A change in the rock makes the closure: a sandstone pinching '
                'out, a facies change, an unconformity cutting across the bed. '
                'No deformation is needed.', 'p2n')], cols='1fr 1fr')]

    # ── 5. the seal ──
    S += [teach('tRes', 'p3T', [
        ('p3a', 'The cap rock above the reservoir &mdash; shale, evaporite or '
                'tight carbonate. Its pore throats are fine enough to hold '
                'back a buoyant hydrocarbon column.', None),
        ('p3b', 'A fault offsets it, fractures open a path through it, or the '
                'column grows tall enough to force fluid through the pore '
                'throats. That last one is capillary leakage.', 'p3n')],
        cols='1fr 1fr')]

    # ── 6. maturity ──
    S += [teach('tSrc', 's1T', [
        ('s1a', 'Buried too shallow, or too cool for too long. The kerogen has '
                'not yet generated hydrocarbons.', None),
        ('s1b', 'Typically about 60&ndash;120&nbsp;&deg;C. The rock generates '
                'liquid hydrocarbons and expels them into a carrier bed. A '
                '<strong>mature source rock</strong> has reached this stage.',
         None),
        ('s1c', 'The kerogen has exhausted its oil potential, and oil '
                'generated earlier has been cracked to gas.', 's1n')],
        cols='1fr 1fr 1fr')]

    # ── 7. saturation ──
    S += [teach('tSrc', 's2T', [
        ('s2a', 'The fraction of the pore space filled with water. What is '
                'left is filled with hydrocarbons, so a low Sw is what the '
                'interpreter hopes to see.', None),
        ('s2b', 'Saline formation water conducts electricity; oil, gas and '
                'tight clean rock do not. High resistivity is therefore '
                'usually read as hydrocarbons in the pores.', 's2n')],
        cols='1fr 1fr')]

    # ── 8. the anomaly, corrected ──
    S += [teach('tSrc', 's3T', [
        ('s3a', 'Fresh, low-salinity formation water is a poor conductor, so a '
                'fully wet interval can log as resistive. Very low porosity '
                'does the same, and so does deep invasion by resistive mud '
                'filtrate.', None),
        ('s3b', 'Conductive minerals &mdash; clay, pyrite &mdash; pull '
                'resistivity <em>down</em>. They produce low-resistivity pay: '
                'a good zone that logs as wet, with its Sw overestimated.',
         's3n')], cols='1fr 1fr')]

    # ── 9. cross-bedding ──
    S += [teach('tSrc', 's4T', [
        ('s4a', 'Layers inclined within a larger bed, formed as sediment '
                'avalanches down the lee face of a migrating dune or ripple. '
                '<strong>Well-developed</strong> means the sets are clear and '
                'measurable.', None),
        ('s4b', 'The dip direction of the foresets gives the palaeocurrent '
                'direction; the scale and angle of the sets give the energy of '
                'the flow.', 's4n')], cols='1fr 1fr')]

    # ── 10. the jargon the stems use ──
    S += [teach('tGlos', 'gT', [
        ('ga', 'the structure dips away from the crest on every side, so '
               'nothing escapes laterally', None),
        ('gb', 'the thickness of an interval that counts as reservoir once the '
               'cut-offs are applied', None),
        ('gc', 'the density of the drilling fluid, set to balance the pressure '
               'in the formation', None),
        ('gd', 'the pressure at which gas dissolved in the oil starts to come '
               'out of solution', None),
        ('ge', 'the rock chips carried up by the mud and examined for '
               'lithology and shows', None),
        ('gf', 'turning a seismic image measured in travel time into one '
               'measured in metres', 'gn')], cols='1fr 1fr 1fr')]

    # ── 11. Activity 1 divider ──
    S += [teach('a1E', 'd1T', [
        ('d1a', 'Each question quotes a phrase from a field report, a well '
                'completion report, a peer review or a conference '
                'presentation, and asks what it means where it stands. Every '
                'one of them has been explained on the slides you have just '
                'read.', 'd1n')], cols='1fr')]

    # ── Activity 1 ──
    S += [mc_slide(i + 1, len(MC), q, 'a1E', 'a1T', folder=F)
          for i, q in enumerate(MC)]

    # ── 18. structure ──
    S += [teach('tStr', 'b1T', [
        ('b1a', 'The highest point of an anticlinal fold. Hydrocarbons migrate '
                'upward by buoyancy and collect there first, provided there is '
                'a seal above.', None),
        ('b1b', 'The vertical distance from the crest down to the lowest '
                'closing contour. With <strong>four-way closure</strong> the '
                'beds dip away on every side, so no fault has to seal.',
         'b1n')], cols='1fr 1fr')]

    # ── 19. pressure ──
    S += [teach('tStr', 'b2T', [
        ('b2a', 'Normal pore pressure is the weight of the column of formation '
                'water above the point of measurement &mdash; roughly '
                '10&nbsp;kPa for every metre of depth.', None),
        ('b2b', 'Pore fluid pressure above that normal value, usually where '
                'compacting shale could not expel its water. The mud weight '
                'has to be raised to balance it.', 'b2n')], cols='1fr 1fr')]

    # ── 20. wellsite ──
    S += [teach('tWell', 'b3T', [
        ('b3a', 'Visible or measurable traces of hydrocarbon in cuttings, core '
                'or mud. <strong>Residual</strong> shows are immobile: they '
                'record that migration happened at some stage, not that it is '
                'happening now.', None),
        ('b3b', 'The interconnected pore space available to flow, once '
                'isolated pores and clay-bound water are excluded. Total '
                'porosity counts all of it and reads higher.', 'b3n')],
        cols='1fr 1fr')]

    # ── 21. time and depth ──
    S += [teach('tWell', 'b4T', [
        ('b4a', 'Seismic data is recorded in the time a wave takes to travel '
                'down to a reflector and back, not in metres. The section is '
                'an image in time.', None),
        ('b4b', 'A receiver is lowered to known depths in the well and the '
                'travel time from surface is measured directly. That '
                'calibrates the velocity model used for depth conversion.',
         'b4n')], cols='1fr 1fr')]

    # ── 22. drive mechanisms ──
    S += [teach('tWell', 'b5T', [
        ('b5a', 'Below the bubble point, gas dissolved in the oil comes out of '
                'solution and expands, pushing oil toward the wellbore. '
                'Recovery is usually modest.', None),
        ('b5b', 'A free gas cap above the oil expands as the reservoir is '
                'produced and drives the oil down toward the perforations.',
         None),
        ('b5c', 'An aquifer moves in as pressure falls, holding the pressure '
                'up and sweeping the oil ahead of it. Usually the most '
                'efficient of the three.', 'b5n')], cols='1fr 1fr 1fr')]

    # ── Activity 2 ──
    # One gap per row and one row per slide: checkGaps marks the first
    # .gap in each .gap-row while maxScore counts every .gap on the
    # slide, so a second input in one row would create an unscoreable
    # point. The bank is the same twelve chips on every slide.
    for n, (hk, sentence, answer, why, width) in enumerate(GAPS, 1):
        S += [D.gap(n, len(GAPS), [(sentence, [answer], why)], BANK,
                    'a2E', E['a2E'], 'a2T', E['a2T'], folder=F,
                    hint=E[hk], hint_key=hk, width=width, size=19)]

    # ── 29/30. the seven report terms, glossed before they are tested ──
    S += [teach('tGlos', 'm1T', [
        ('m1a', 'a measure of thermal maturity, read from the optical '
                'reflectivity of vitrinite particles in the source rock and '
                'quoted as %Ro', None),
        ('m1b', 'the vertical component of the displacement across a fault '
                'plane; the horizontal component is the heave', None),
        ('m1c', 'the pressure a non-wetting fluid needs before it can enter '
                'the pore throats of the seal and displace the wetting fluid',
         None),
        ('m1d', 'the level in the reservoir below which the pore space holds '
                'water rather than gas', 'm1n')], cols='1fr 1fr')]

    S += [teach('tGlos', 'm2T', [
        ('m2a', 'the proportion of an interval that meets the cut-offs for '
                'reservoir quality &mdash; net thickness over gross '
                'thickness', None),
        ('m2b', 'pore fluid pressure that exceeds the hydrostatic pressure '
                'expected at that depth', None),
        ('m2c', 'a group of related sedimentary facies that together '
                'characterise one depositional environment', 'm2n')],
        cols='1fr 1fr 1fr')]

    # ── Activity 3 ──
    S += [mc_slide(i + 1, len(TERMS), q, 'a3E', 'a3T', folder=F)
          for i, q in enumerate(TERMS)]

    # ── results and activation ──
    S += [D.results(),
          D.activate(E['actTitle'], E['actUse'],
                     ['exhibits dual porosity behaviour',
                      'stratigraphic trapping', 'seal integrity',
                      'mature source rock',
                      'anomalously high water saturation',
                      'four-way closure', 'net pay', 'residual oil shows',
                      'solution gas drive'],
                     'Discussion &middot; in pairs', E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'])]
    return S, key_spread, bank_spread


if __name__ == '__main__':
    slides, key_spread, bank_spread = build()
    body = "".join(slides)
    n = body.count('<section class="slide')
    body = body.replace('NN slides', '%d slides' % n)
    I.T['en']['chipCount'] = '%d slides' % n
    I.T['de']['chipCount'] = '%d Folien' % n

    s = D.assemble(TPL, OUT, body, PALETTE,
                   'The Language of Geoscience — C1 Technical English', I)
    s = s.replace('<html lang="en">', '<html lang="en" data-theme="light">', 1)
    s = s.replace('</style>\n</head>', CSS + '</style>\n</head>', 1)
    assert 'data:image' not in s, 'a base64 blob survived into the build'
    assert_no_answer_is_shown(s)
    # Nothing volcanic, including the file misleadingly called hero.jpg.
    for bad in ('hero.jpg', 'volcano.jpg', 'stratovolcano.jpg', 'fissure.jpg'):
        assert '%s/%s' % (F, bad) not in s, \
            'the deck references %s — this lesson has no volcanic content' % bad
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d bytes, %d slides' % (OUT, len(s), n))
    print('MC key positions A/B/C/D: %s' % key_spread)
    print('gap answer positions in the shared bank: %s' % bank_spread)
    print('scored points: %d phrases + %d gaps + %d terms = %d'
          % (len(MC), len(GAPS), len(TERMS), len(MC) + len(GAPS) + len(TERMS)))
