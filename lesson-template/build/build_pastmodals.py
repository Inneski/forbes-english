# -*- coding: utf-8 -*-
"""Past Modals in Minecraft (B2) — rebuilt as a 16:9 deck.

`forbes-english-past-modals-minecraft.html`, first of the six Minecraft
lessons still on the old scrolling format. All fifteen scored items survive:
five multiple choice, five gaps, five matched pairs.

What changed:

- **Option A was never the answer.** Keys sat at 1, 2, 3, 2, 2 across five
  questions. Spread in `pastmodals_data.py`. No key was the longest option,
  which is unusual here and worth recording rather than assuming.
- **The grammar guide was a five-row table** — correct, but a reference, not
  teaching. It is three slides now: the shared form, the certainty pair
  (must/might, and why the confident negative is `can't have`), and the
  regret pair (should/could/needn't). Every one of the fifteen items lands
  inside one of those three.
- **The gap-fill hint was the answer key.** The same line sat under all five
  gaps: "should / must / could / might / needn't + have" — the five answers
  and nothing else. Removed; the forms are taught on the slide before instead.
- `mustn't have` appeared only as a distractor with no comment. It is one of
  the commonest B2 errors and is not English, so the teaching slide says so
  and the explanation on that item names it.

Artwork: `PastModals/`, four flat-vector Minecraft scenes — Steve at noon for
the cover, then the creeper hillside at dusk, the golem at moonrise and the
enderman, which suit a lesson about working out what happened after the fact.
Three came from Innes's Downloads, one was already in `minecraft/`.

`--void` is lifted off the derived near-black to a grey, per Innes's standing
preference; every other token is `extract-palette.py` output unedited. A
re-derivation would put the black back.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from pastmodals_data import MC, FIB, MATCH

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-past-modals-minecraft.html'
F = 'PastModals'

# python3 lesson-template/extract-palette.py PastModals/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #2c2f28;
  --surface       : #161b13;
  --surface2      : #1f271b;
  --border        : #bd9027;
  --text          : #f5f4f2;
  --text-dim      : #bfb7a3;
  --accent        : #fbc84f;
  --accent-bright : #ffc12c;
  --accent-dim    : #e3a30b;
  --secondary     : #98bcca;
  --contrast      : #1dbeed;''' % F

CHIPS = ['should have', 'could have', 'must have', 'might have',
         "needn't have", "can't have", 'the evidence suggests', 'it was possible']

MC_BG = ['dusk.jpg', 'enderman.jpg', 'dusk.jpg', 'golem.jpg', 'enderman.jpg']
FIB_BG = ['golem.jpg', 'dusk.jpg', 'enderman.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'PastModals')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Past <em>Modals</em>',
                'What you should have done, what you could have done, and how you know',
                [('Level', 'B2 &middot; Upper-intermediate'),
                 ('Focus', 'Modals + have + past participle'),
                 ('Count', '16 slides')])

        + D.teach('formEyebrow', 'Before the questions',
                  'formTitle', 'One shape, five jobs',
                  [('fo1h', 'The shape never changes', 'fo1b',
                    'Every one of these is <strong>modal + have + past participle</strong>. '
                    'The modal carries the meaning; <em>have + p.p.</em> only says that we '
                    'are talking about the past.',
                    'fo1n', '<em>Have</em> never becomes <em>had</em> here, whoever the '
                            'subject is.'),
                   ('fo2h', 'Looking back at a mistake', 'fo2b',
                    '<strong>Should have</strong> is advice given too late: the right thing '
                    'did not happen. <strong>Could have</strong> is the chance that existed '
                    'and was not taken.',
                    'fo2n', 'Both point at a past that could have gone differently. Only '
                            '<em>should</em> blames.'),
                   ('fo3h', 'Working out what happened', 'fo3b',
                    '<strong>Must have</strong> is near-certainty from evidence. '
                    '<strong>Might have</strong> is a guess. <strong>Needn&rsquo;t '
                    'have</strong> says it was done and was not needed.',
                    'fo3n', '<em>Needn&rsquo;t have</em> is the one learners miss: the '
                            'action <em>did</em> happen.')],
                  folder=F, bg='dusk.jpg')

        + D.teach('sureEyebrow', 'The deduction pair',
                  'sureTitle', 'How certain are you?',
                  [('su1h', 'Almost certain', 'su1b',
                    '<strong>Must have.</strong> There are footprints round the chest, so '
                    'the thief <em>must have</em> been here. You did not see it; the '
                    'evidence leaves little room for anything else.',
                    'su1n', 'Roughly 90% or more. Not proof &mdash; a conclusion.'),
                   ('su2h', 'One possibility of several', 'su2b',
                    '<strong>Might have</strong> or <strong>could have.</strong> Nobody saw '
                    'who broke the bridge, so it <em>might have</em> been a griefer. It is '
                    'a guess, offered as a guess.',
                    'su2n', 'Under 50%. <em>May have</em> is the same idea in a more formal '
                            'register.'),
                   ('su3h', 'The negative flips', 'su3b',
                    'For a confident negative, English uses <strong>can&rsquo;t have</strong>, '
                    'not <em>mustn&rsquo;t have</em>: <em>she can&rsquo;t have finished '
                    'already</em>.',
                    'su3n', '<em>Mustn&rsquo;t have</em> is one of the commonest B2 errors, '
                            'and it is not English.')],
                  folder=F, bg='golem.jpg')

        + D.teach('regEyebrow', 'The regret pair',
                  'regTitle', 'The past that did not happen',
                  [('re1h', 'Should have', 're1b',
                    '<em>You <strong>should have</strong> built the walls higher.</em> The '
                    'right action, identified afterwards. It carries criticism, so it lands '
                    'hard.',
                    're1n', '<em>Shouldn&rsquo;t have</em> criticises something that '
                            '<em>was</em> done.'),
                   ('re2h', 'Could have', 're2b',
                    '<em>You <strong>could have</strong> used the Elytra.</em> The ability '
                    'or the opportunity was there and went unused. No blame attached.',
                    're2n', 'It also softens a suggestion: <em>you could have asked me</em> '
                            'is gentler than <em>should</em>.'),
                   ('re3h', 'Needn&rsquo;t have', 're3b',
                    '<em>He <strong>needn&rsquo;t have</strong> walked &mdash; there was a '
                    'horse.</em> He walked. It was wasted effort. The action happened.',
                    're3n', 'Compare <em>didn&rsquo;t need to walk</em>, which usually means '
                            'he did not walk at all.')],
                  folder=F, bg='enderman.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow', 'Activity 1 &middot; Multiple choice',
                       'mcTitle', 'Choose the modal that fits', folder=F, bg=MC_BG[i])
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 3, part, None,
                        'fibEyebrow', 'Activity 2 &middot; The exact form',
                        'fibTitle', 'Complete the sentence',
                        folder=F, bg=FIB_BG[n], hint_key='fibHint',
                        hint='Two words each time: a modal, then <em>have</em>.',
                        width=170, size=18)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:]]))

        + D.match(MATCH, 'matchEyebrow', 'Activity 3 &middot; Meaning',
                  'matchTitle', 'Match the sentence to what it does',
                  'matchHint', 'Click a sentence, then click what it means.',
                  'matchWhy', folder=F, bg='dusk.jpg')

        + D.results('resNext', 'You can read the certainty. Now write it &rarr;',
                    folder=F, bg='hero.jpg')

        + D.activate('Account for the disaster', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you runs the server and wants to know what happened. The '
                     'other was there. Four minutes each, then swap.',
                     ['The base was destroyed overnight. Say what happened and how sure '
                      'you are.',
                      'Your partner blames you. Say what you could have done, without '
                      'conceding a mistake.',
                      'Describe something you needn&rsquo;t have done last week.',
                      'Give three deductions, each more confident than the last.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write the incident report a server admin would post after the raid. '
                     'Say what must have happened, what might have happened, and what the '
                     'team should have done &mdash; and keep the three levels of certainty '
                     'distinct.',
                     'From the state of the east wall, the raiders must have&hellip;',
                     folder=F, bg='golem.jpg')
    )

    import i18n_pastmodals as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Past Modals in Minecraft (B2) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(MATCH), len(s)))


if __name__ == '__main__':
    build()
