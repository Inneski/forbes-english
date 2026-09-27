# -*- coding: utf-8 -*-
"""B1 Mixed Grammar Test, parts 1 and 2 — rebuilt as editorial decks (§15).

**SUPERSEDED 2026-09-25. This builder never writes a live page any more.**
Both parts shipped as panel decks from `build_mixedgrammar1.py` and
`build_mixedgrammar2.py`: "house style 2", as Innes clarified it on 09-25, is
the panel layout, not §15, and he had the 16:9 art made for that plan
(`docs/PLAN-mixed-grammar-b1.md`), not the 7:6 plates this one waits for.
Its audit, its answer-key fixes and its EN/DE/ES explanations were ported
into those two builders. It stays for one reason: `mixed_b1_fr.py`, `_it.py`
and `_pt.py` hold French, Italian and Portuguese for all 35 items of both
parts — most of a second language pass for the panel decks. It writes the
gitignored `_…` preview only, whatever is on disk; left as it was, the day
its seven plates per part landed it would have overwritten the live decks.
Do not commission the 14 plates in docs/ARTWORK-b1-mixed-grammar.md.

    py lesson-template/build/build_mixed_b1.py        # both parts
    py lesson-template/build/build_mixed_b1.py 2      # one part
    py lesson-template/build/build_mixed_b1.py --stand-in   # hero in every
                                     # plate slot, preview only: measures layout

Both were scrolling pages with their own chrome: a TEST_DATA object rendered
into five stacked sections, a Spanish-only hover glossary, no language
switcher, no activation stage. Every scored item survives — 10 multiple
choice, 8 story gaps, 6 true/false, 5 sentences to build, 6 to correct: 35
points each, as before. Content is in `mixed_b1_data.py`, text in
`mixed_b1_<lang>.py`.

**Editorial style, Innes's request ("house style 2").** The two heroes are
already flat vector art — slate blue and coral desert scenes — which is the
case §15 was written for, so the fixed editorial palette is used and
`extract-palette.py` is not run.

**Artwork is commissioned, not yet delivered.** `docs/ARTWORK-b1-mixed-grammar.md`
is the shopping list: seven plates per part, named by slot. Until every plate
for a part is on disk, this builder writes the part to an underscore preview
(`_forbes-english-b1-mixed-grammar-test.html`), gitignored, and leaves the
live page alone — HOUSE-STYLE §5c, no converting on a thin set. The moment
the plates land it writes the real filename.

Defects in the source, fixed:

  * **Part 1, story gap 8 accepted "much" in "serves much fresh seafood".**
    Nobody says that; MUCH belongs to negatives and questions. The gap now
    takes A LOT OF only, and says why.
  * **Part 1, error correction 5 taught the same mistake the other way round.**
    "I have many money" → "I have much money" — the fix was itself unnatural
    English. It is a negative now ("I don't have many money"), where MUCH is
    the natural correction, and A LOT OF is accepted too.
  * **Accepted answers were too narrow.** "Has been living", "is going to
    meet", "'ll go", "the girl that is sitting there", "If I had money, I'd
    buy a house" — all correct, all marked wrong. Every correct alternative
    that fits the sentence is accepted now.
  * **Part 2, story: "he'd forgotten his passport at his parents' house".**
    FORGET does not take a place; LEAVE does. And "he's already checked in
    online" a week before the flight is impossible; he has chosen his seat.
  * **Part 2, error correction 6 was an error nobody makes** ("whose car was
    stolen it"). Replaced with a doubled possessive, "whose his car", which
    learners really do produce.
  * **Section 2 had no explanations at all.** Every gap row has one now.
  * **Error correction was word-for-word string matching** that failed a
    learner who left off the full stop. Every answer is accepted with or
    without its final punctuation and its commas.

New, with no source in the old pages: a one-slide briefing, per-part results
messages (the old score bands, re-cut to the engine's four), and the
activation stage (§10b).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_mixed_b1 as I
import mixed_b1_data as DATA

TPL = 'lesson-template/lesson-template.html'

PART = {
    1: dict(out='forbes-english-b1-mixed-grammar-test.html',
            folder='MixedGrammarPart1',
            hero='desert-building-sunset-clouds.jpg',
            title='B1 Mixed Grammar Test — Forbes English',
            gloss={4: 'gTournament', 6: 'gSeatbelt'},
            chips=['is knocking', 'I overslept', 'has lived', 'I think &hellip; will',
                   'must', 'if I had &hellip;, I would', 'was built', 'who / which']),
    2: dict(out='forbes-english-b1-mixed-grammar-test-part2.html',
            folder='MixedGrammarPart2',
            hero='hero.jpg',            # was desert-gas-station-sunset.jpg
            title='B1 Mixed Grammar Test, Part 2 — Forbes English',
            gloss={6: 'gForbidden'},
            chips=['I&rsquo;m flying', 'if it rains', 'mustn&rsquo;t',
                   'don&rsquo;t have to', 'was &hellip;-ing', 'have known',
                   'the best', 'whose']),
}

# The plate slots, one per section plus the activation (§5c). Filenames are
# the slot names; docs/ARTWORK-b1-mixed-grammar.md says what each one shows.
PLATES = ('plate-mc-a', 'plate-mc-b', 'plate-story', 'plate-tf', 'plate-order',
          'plate-fix', 'plate-act')

EXTRA_CSS = '''
/* ── B1 mixed grammar ───────────────────────────────────────────── */
.q-hint { color: var(--text-dim); font-size: .8em; white-space: nowrap; }
/* The route-map colour of a tense area (§5a), as a dot before its name. The
   ring is there for past continuous, whose yellow vanishes on the cream. */
.tdot {
  display: inline-block; width: .62em; height: .62em; border-radius: 50%;
  background: var(--tdot); margin-right: .45em; vertical-align: .02em;
  box-shadow: inset 0 0 0 1.5px color-mix(in srgb, var(--text) 30%, transparent);
}
/* Measured with every item answered wrongly: the explanation, its grammar
   area and "Answer: …" push an MC slide 2–16px past the canvas in EN and DE.
   The bars give back the space, not the type (§6): 12→9px between them and
   16→13px inside, 30px in all. */
html[data-style="editorial"] .opts { gap: 9px; }
html[data-style="editorial"] .opt { padding-top: 13px; padding-bottom: 13px; }
/* The gloss line is a footnote to the stem here, not the scene it usually is. */
.q-ctx { margin-bottom: 14px; }
.fix-wrong {
  display: block; margin-bottom: 6px; color: var(--text-dim);
  text-decoration: line-through; text-decoration-color: var(--contrast);
  text-decoration-thickness: 2px;
}
'''


def art(slide, n, size='narrow'):
    """Alternate the picture's side, and take the arch (still lifes have air)."""
    extra = (' data-art-side="left"' if n % 2 else '') + ' data-art="arch"'
    if size:
        extra += ' data-art-size="%s"' % size
    return slide.replace('<section class="slide"',
                         '<section class="slide"' + extra, 1)


def variants(answers):
    """Every accepted answer, with and without final punctuation and commas.

    The engine compares case- and space-insensitively but not punctuation, and
    a learner who types the right sentence without its full stop is right."""
    out = []
    for a in answers:
        base = a.rstrip('.?!')
        # base first: the engine shows the first alternative as "Answer: …"
        # and ends the line with its own full stop, so "wallet.." otherwise.
        for v in (base, a, base.replace(',', ''), a.replace(',', '')):
            if v not in out:
                out.append(v)
    return '|'.join(out)


def build(part, stand_in=False):
    """stand_in: put the hero in every plate slot and write the preview.

    For measuring. A plate takes 30% of the width, so a slide that fits with
    no picture can overflow with one; the checker has to see the real column
    before the real art exists."""
    cfg = PART[part]
    F = cfg['folder']
    P = DATA.PARTS[part]
    L = I.module(part)
    EN = L.EN

    have = {p: os.path.exists('%s/%s.jpg' % (F, p)) for p in PLATES}
    ready = all(have.values()) and not stand_in
    pic = lambda p: (cfg['hero'] if stand_in
                     else '%s.jpg' % p if have[p] else None)

    for q in P['MC']:
        q['why'] = 'x_mc%d' % (P['MC'].index(q) + 1)
    D.assert_no_key_is_longest(P['MC'], 'P%d MC' % part)

    logo = D.logo_from(TPL)
    slides = [D.cover(logo, EN['coverTitle'], EN['coverSub'],
                      [('Level', EN['chipLevel']), ('Focus', EN['chipFocus']),
                       ('Count', EN['chipCount'])])]

    slides.append(D.teach(
        'eIntro', EN['eIntro'], 'tIntro', EN['tIntro'],
        [('introA', EN['introA'], 'introAb', EN['introAb'], 'introAn', EN['introAn']),
         ('introB', EN['introB'], 'introBb', EN['introBb'], 'introBn', EN['introBn'])],
        cols='1fr 1fr', folder=F, bg=cfg['hero']))

    # ── Section 1 ─────────────────────────────────────────────────────
    for n, q in enumerate(P['MC'], 1):
        stem = q['stem'] + (' <span class="q-hint">(%s)</span>' % q['hint']
                            if q['hint'] else '')
        g = cfg['gloss'].get(n)
        slides.append(art(D.mc(
            n, len(P['MC']), dict(q, stem=stem), 'eMC', EN['eMC'], 'tMC', EN['tMC'],
            folder=F, bg=pic('plate-mc-a' if n <= 5 else 'plate-mc-b'),
            ctx=EN[g] if g else None, ctx_key=g), n))

    # ── Section 2 ─────────────────────────────────────────────────────
    k = 0
    for n, rows in enumerate(P['STORY'], 1):
        built = []
        for sentence, answers in rows:
            k += 1
            built.append((sentence, answers, 'x_st%d' % k))
        slides.append(art(D.gap(
            n, len(P['STORY']), built, None, 'eStory', EN['eStory'],
            'tStory', EN['tStory'], folder=F, bg=pic('plate-story'),
            hint=EN['hSt%d' % n], hint_key='hSt%d' % n, width=170), n))

    # ── Section 3 ─────────────────────────────────────────────────────
    for n, q in enumerate(P['TF'], 1):
        item = dict(stem=EN['tf%d' % n], options=['True', 'False'],
                    correct=q['correct'], why='x_tf%d' % n)
        slides.append(art(D.mc(
            n, len(P['TF']), item, 'eTF', EN['eTF'], 'tTF', EN['tTF'],
            folder=F, bg=pic('plate-tf'), stem_key='tf%d' % n), n))

    # ── Section 4 ─────────────────────────────────────────────────────
    for n, (chunks, _) in enumerate(P['ORDER'], 1):
        slides.append(art(D.order(
            chunks, 'eOrder', EN['eOrder'], 'tOrder', EN['tOrder'],
            'hOrder', EN['hOrder'], 'x_or%d' % n,
            folder=F, bg=pic('plate-order')), n))

    # ── Section 5 ─────────────────────────────────────────────────────
    fixes = P['FIX']
    for n in range(0, len(fixes), 2):
        rows = [('<span class="fix-wrong">%s</span>______' % f['wrong'],
                 [variants(f['answers'])], 'x_fx%d' % (n + j + 1))
                for j, f in enumerate(fixes[n:n + 2])]
        slides.append(art(D.gap(
            n // 2 + 1, (len(fixes) + 1) // 2, rows, None, 'eFix', EN['eFix'],
            'tFix', EN['tFix'], folder=F, bg=pic('plate-fix'),
            hint=EN['hFix'], hint_key='hFix', width=560), n // 2))

    slides.append(D.results(folder=F, bg=pic('plate-tf')))
    slides.append(art(D.activate(
        EN['actTitle'], EN['actUse'], cfg['chips'],
        'Speaking', EN['actSpeakBrief'],
        [EN['actSpeak1'], EN['actSpeak2'], EN['actSpeak3']],
        EN['actWriteKind'], EN['actWriteBrief'], EN['actPlaceholder'],
        folder=F, bg=pic('plate-act')), 0, size=None))

    # Superseded (see the docstring): a preview, never the live page, even
    # when every plate is on disk. `ready` still drives the missing-plate note.
    out = '_' + cfg['out']
    s = D.assemble(TPL, out, ''.join(slides),
                   D.editorial_palette('%s/%s' % (F, cfg['hero'])),
                   cfg['title'], L, langs=I.available(), style='editorial')
    s = s.replace('\n</style>', EXTRA_CSS + '</style>', 1)
    n = len(re.findall(r'<section class="slide[^>]*\bdata-type=', s))
    s = s.replace('{N}', str(n))
    open(out, 'w', encoding='utf-8', newline='').write(s)
    missing = [p for p in PLATES if not have[p]]
    print('%s — %d slides (editorial), %s%s' % (
        out, n, ', '.join(I.available()),
        ('\n  PREVIEW ONLY — plates not on disk: %s' % ', '.join(missing))
        if missing else ''))
    return out


if __name__ == '__main__':
    probs = I.check()
    if probs:
        sys.exit('\n'.join(probs))
    stand_in = '--stand-in' in sys.argv
    for p in ([int(a) for a in sys.argv[1:] if a.isdigit()] or [1, 2]):
        build(p, stand_in)
