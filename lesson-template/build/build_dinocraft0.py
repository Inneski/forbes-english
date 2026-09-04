# -*- coding: utf-8 -*-
"""Dino-Craft Part 0: The Briefing (C1) — rebuilt as a 16:9 deck.

Was `-dinosaurs C1.html`, a scrolling page, and before that one half of a
duplicate pair with `forbes-english-lesson (dinosoausrs c1).html`. All
twenty-five scored items survive: five multiple choice, five gap-fills, five
discourse-marker gaps, five matched terms and five sentences to rebuild.

Innes's call on the naming: rather than renaming the page down to match its
catalogue card, fold it into the existing Dino-Craft series as a prequel. It
fits the content — Parts I and II each teach a set of language points and then
practise them, while this file is five activity types over twenty-five items
with no teaching at all, which is a placement test, and a placement test
belongs before the expedition rather than beside it.

What the rebuild fixes, beyond the format:

- **It now teaches.** The original was twenty-five questions and a score, with
  every rule appearing only in the feedback after the answer. Three slides open
  the deck on the three structures the questions actually test: the consensus
  passive, the unreal past, and the participle clause with its dangling-subject
  trap. Nothing in the activities is untaught any more.
- **Key positions, the word bank and the per-item explanations** — see the
  docstring in `dinocraft0_data.py`.
- **Ten explanations that did not exist.** Three activities shared one
  paragraph between five items each.

Artwork: six illustrations from Innes's Downloads, all 2944×1648 and one
family — muted teal skies, coral sun, silhouetted sauropods and theropods.
They replace the four voxel-style images the first pass used, and the gain is
not only that they are better: **each background now matches the slide it sits
behind**. The amber lump sits behind the amber-block participle question and
the bone-grinding gap; the feathered dinosaur sits behind the China-fossils gap
and the hedging slide; the volcano sits behind the asteroid counterfactual; the
T. rex sits behind the apex-predator item. A background that illustrates its
own slide is worth more than a background that merely alternates.

Palette is `extract-palette.py` with `--accent-hue=40 --accent-sat=0.8`. The
honest derivation returns a pale coral accent that sits a hair off the
near-white body text (1.48:1 against a 1.45 floor), so headings barely
separate. Rotating to the gold that is already in the artwork — the sun, the
amber — fixes it without hand-picking anything.

`--void` is the one value here that is NOT the tool's output. Innes asked for
the interior slides to sit on grey rather than near-black, so the derived
canvas is lifted while every other token stays as derived. It is the canvas
only: the cover shows its hero at full opacity and is untouched, and the cards
still use the derived `--surface`, so the contrast between card and canvas is
what carries the layout. Body text still measures about 12:1 on it.
**A rebuild will not revert this — but re-deriving the palette would, so lift
it again if you re-run extract-palette.py.**
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from dinocraft0_data import MC, FIB, DND, BANK, MATCH, ORDER

TPL = 'lesson-template/lesson-template.html'
OUT = '-dinosaurs C1.html'
F = 'DinoCraft0'

# python3 lesson-template/extract-palette.py DinoCraft0/hero.jpg \
#            --accent-hue=40 --accent-sat=0.8
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #2e312e;
  --surface       : #151919;
  --surface2      : #1e2424;
  --border        : #bb913e;
  --text          : #f5f4f2;
  --text-dim      : #bfb6a3;
  --accent        : #efc570;
  --accent-bright : #fdbf43;
  --accent-dim    : #e0a124;
  --secondary     : #ed8972;
  --contrast      : #1dc6ed;''' % F

CHIPS = ['was considered', 'is thought to be', 'believed to have been',
         'gain traction', 'might have evolved', 'had the asteroid not struck',
         'having + past participle', 'contrary to popular belief',
         'by and large', 'it was not until… that']

# one background per slide, chosen for what the slide is about
MC_BG  = ['rex.jpg', 'volcano.jpg', 'plain.jpg', 'amber.jpg', 'plain.jpg']
FIB_BG = ['feather.jpg', 'amber.jpg', 'feather.jpg']
DND_BG = ['plain.jpg', 'volcano.jpg', 'plain.jpg']
ORD_BG = ['feather.jpg', 'rex.jpg', 'rex.jpg', 'amber.jpg', 'amber.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'DinoCraft0')
    D.assert_bank_is_not_a_key(BANK, [a[0] for _, a, _ in DND])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Dino-Craft <em>Part 0</em>',
                'The briefing &mdash; five activities to place your C1 English before '
                'the expedition sets out',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Placement briefing'),
                 ('Count', '23 slides')])

        + D.teach('conEyebrow', 'Before the questions',
                  'conTitle', 'Stating what the science accepts',
                  [('con1h', 'The consensus passive', 'con1b',
                    'English reports settled findings in the passive and the simple '
                    'past: <em>the T. rex was considered an apex predator</em>. The '
                    'agent is left out because the point is the finding, not who '
                    'found it.',
                    'con1n', 'Perfect and continuous forms sound like an unfinished '
                             'process, not a conclusion.'),
                   ('con2h', 'Hedging a claim', 'con2b',
                    'Science rarely asserts flatly. <em>Widely believed to have '
                    'been</em>, <em>is thought to be</em>, <em>appears to have</em> '
                    '&mdash; the hedge marks how firmly the field holds the claim.',
                    'con2n', '<em>Believed to have been</em> reports a present belief '
                             'about the past.'),
                   ('con3h', 'The register carries it', 'con3b',
                    'A theory <em>gains traction</em>; a discovery <em>transforms our '
                    'understanding</em>; a habitat is <em>disrupted</em>. At C1 the '
                    'fixed collocation is the difference between fluent and merely '
                    'correct.',
                    'con3n', 'Every one of these is a set phrase. Change one word and '
                             'it stops sounding native.')],
                  folder=F, bg='rex.jpg')

        + D.teach('cfEyebrow', 'The unreal past',
                  'cfTitle', 'A past that did not happen',
                  [('cf1h', 'Third conditional', 'cf1b',
                    'An unreal past condition takes an unreal past result: <em>if the '
                    'asteroid had not struck, the dinosaurs would have survived</em>. '
                    'Both halves have to be in the past.',
                    'cf1n', 'A present result (<em>would survive</em>) turns it into a '
                            'mixed conditional &mdash; a different sentence.'),
                   ('cf2h', 'How sure are you?', 'cf2b',
                    'Swap the modal to change the confidence: <em>would have</em> '
                    '(certain), <em>might</em> or <em>could have</em> (possible), '
                    '<em>may have</em> (possible, more formal).',
                    'cf2n', 'All of them keep <em>have + past participle</em>. That '
                            'part does not move.'),
                   ('cf3h', 'Inversion drops the <em>if</em>', 'cf3b',
                    '<em>Had the asteroid not struck Earth&hellip;</em> is the formal '
                    'equivalent of <em>if the asteroid had not struck Earth</em>. '
                    'Invert the auxiliary and the subject, and delete <em>if</em>.',
                    'cf3n', 'Written register only. It is common in academic prose and '
                            'rare in speech.')],
                  folder=F, bg='volcano.jpg')

        + D.teach('ppEyebrow', 'The trap',
                  'ppTitle', 'Participle clauses, and what goes wrong with them',
                  [('pp1h', 'What it does', 'pp1b',
                    '<em>Having mined the amber block, the player&hellip;</em> '
                    'compresses <em>after the player had mined</em> into three words. '
                    'It signals that one action finished before the next began.',
                    'pp1n', '<em>Having + past participle</em> for a completed action; '
                            '<em>-ing</em> alone for a simultaneous one.'),
                   ('pp2h', 'The subject rule', 'pp2b',
                    'The participle has no subject of its own, so it borrows the '
                    'subject of the main clause. Whoever did the first action must be '
                    'the one doing the second.',
                    'pp2n', 'This is the whole rule. Everything below follows from it.'),
                   ('pp3h', 'The dangling participle', 'pp3b',
                    '<em>Having mined the amber block, the velociraptor was '
                    'discovered.</em> The main clause subject is the velociraptor, so '
                    'the sentence says the velociraptor did the mining.',
                    'pp3n', 'It is the commonest C1 writing error, and the writer '
                            'almost never hears it.')],
                  folder=F, bg='amber.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow', 'Activity 1 &middot; Multiple choice',
                       'mcTitle', 'Choose the form that fits',
                       folder=F, bg=MC_BG[i])
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 3, part, None,
                        'fibEyebrow', 'Activity 2 &middot; The exact word',
                        'fibTitle', 'Collocation, register and precision',
                        folder=F, bg=FIB_BG[n],
                        hint_key='fibHint',
                        hint='Type the word. Several sentences accept more than one answer.',
                        width=170, size=18)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:]]))

        + "".join(D.gap(n + 1, 3, part, BANK,
                        'dndEyebrow', 'Activity 3 &middot; Discourse markers',
                        'dndTitle', 'Put the right phrase in the gap',
                        folder=F, bg=DND_BG[n],
                        hint_key='dndHint',
                        hint='Three of the eight phrases in the bank belong to no gap here.',
                        width=230, size=18)
                  for n, part in enumerate([DND[:2], DND[2:4], DND[4:]]))

        + D.match(MATCH, 'matchEyebrow', 'Activity 4 &middot; Terminology',
                  'matchTitle', 'The vocabulary the field actually uses',
                  'matchHint', 'Click a term, then click what it means.',
                  'These five terms carry the register of the whole lesson. '
                  '<em>Herbivorous</em> is not <em>omnivorous</em>, and the Cretaceous '
                  'is not the Jurassic &mdash; at C1 the precision is the point.',
                  folder=F, bg='feather.jpg')

        + "".join(D.order(chunks, 'ordEyebrow', 'Activity 5 &middot; Sentence building',
                          'ordTitle', 'Put the sentence back together',
                          'ordHint', 'Click a chunk to place it, click a placed chunk '
                                     'to take it back.',
                          why, folder=F, bg=ORD_BG[n])
                  for n, (chunks, why) in enumerate(ORDER))

        + D.results('resNext', 'The briefing is done. Now write it up &rarr;',
                    folder=F, bg='volcano.jpg')

        + D.activate('Brief the expedition', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'You are the expedition scientist; your partner is the sceptic who '
                     'wants the evidence. Three minutes each, then swap.',
                     ['Explain what the feathered fossils found in China changed, and '
                      'how confident the field is about it.',
                      'Argue what might have happened to the dinosaurs if the asteroid '
                      'had missed. Stay in the unreal past throughout.',
                      'Correct a popular misconception about dinosaurs &mdash; the size '
                      'of a velociraptor, or their colour &mdash; without saying '
                      '&ldquo;that is wrong&rdquo;.',
                      'Your partner claims the Pteranodon was a dinosaur. Put them '
                      'right, politely, in one turn.'],
                     'Writing &middot; 200&ndash;250 words',
                     'Write the briefing note the expedition team reads before it '
                     'deploys. Set out what is established, what is still contested, '
                     'and what the team should not assume. Hedge the claims that '
                     'deserve hedging.',
                     'It is now widely accepted that&hellip;',
                     folder=F, bg='rex.jpg')
    )

    import i18n_dinocraft0 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Dino-Craft Part 0: The Briefing (C1) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d fib, %d dnd, %d pairs, %d order, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(DND),
             len(MATCH), len(ORDER), len(s)))


if __name__ == '__main__':
    build()
