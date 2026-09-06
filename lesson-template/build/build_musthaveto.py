# -*- coding: utf-8 -*-
"""Must & Have To — Minecraft Edition (A2), rebuilt as a 16:9 deck.

`minecraft-lesson.html` was a hand-built, tab-based page (custom pixel-art
CSS, not the shared template) whose only language support was Polish, glossed
inline inside the English sentences (`<span class="pl">Muszę...</span>`)
rather than through the site's `LANGS` / `UI_I18N` system. Polish is not one
of the site's nine languages and `docs/HANDOFF.md` held this page for a
decision on whether to add it. Innes decided: standard EN + DE + ES like
every other deck, Polish dropped, no changes to the shared template or
`chrome_i18n.py`.

Also fixed, found during the rebuild:

- **Gap-fills were compared with `===`.** `checkFill()` lower-cased and
  trimmed but accepted exactly one spelling per gap. `mustn't` typed as
  `must not` scored wrong. Every gap here accepts both.
- **The eight-question quiz reused the same four options** (must / have to /
  mustn't / don't have to) for almost every item, so a learner already knew
  the four candidate words from question one and pattern-matched on which
  answer *looked* different that time, rather than reasoning from context.
  Six MC items now vary the option pool per question. This also fixes the
  underlying length problem: `don't have to` (13 characters) was frequently
  the correct answer sitting in a set with `must` (4) and `have to` (7) —
  the longest option was correct three times, which `check-lesson.js`'s
  ANSWERS gate would fail outright. Every item now pairs its key against a
  same-length or longer plausible distractor.
- **The static comparison table taught nothing by itself** — a table is
  read, not answered. It is now a six-pair match activity: each form against
  what it actually means, which is the same information turned into a task.

**Artwork.** Four flat-vector Minecraft illustrations, none of them
claimed by another deck's dedicated folder: `hero.jpg` (a giant golem over a
moonlit ruined city — the page's original cover image, kept because it
already suits the "obligation looming over you" theme and nothing about
switching to the deck format required losing it), `hillside.jpg` (a
silhouetted mob at dusk), `desert.jpg` (an Enderman in warm desert tones),
`pig.jpg` (a close study of a Minecraft pig, for the lighter no-obligation
material). Sourced from the shared `minecraft/` folder, which HANDOFF notes
is otherwise exhausted for Past Modals / Tense Review / Minecraft B1 — these
four were never claimed by any of those builders.

The accent is rotated to creeper green (`--accent-hue=130`) because the
honest derivation returns the same gold/amber Past Modals and Minecraft
Editorial both already use, and three decks cannot share one palette family.
Green also happens to suit a lesson about permission and prohibition.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'minecraft-lesson.html'
F = 'MustHaveTo'

# python3 lesson-template/extract-palette.py MustHaveTo/hero.jpg \
#            --accent-hue=130 --accent-sat=0.55
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0a0d0d;
  --surface       : #131b1b;
  --surface2      : #1b2727;
  --border        : #83b58c;
  --text          : #f2f5f2;
  --text-dim      : #a3bfa8;
  --accent        : #b5e9bd;
  --accent-bright : #4fe468;
  --accent-dim    : #72d082;
  --secondary     : #fae0a4;
  --contrast      : #c468ee;''' % F

CHIPS = ['must', 'have to', "mustn't", "don't have to", 'had to', 'will have to']

MC = [
    dict(stem="It's nearly dark and Steve hasn't built a shelter. He thinks: "
              "‘I ______ get inside before the mobs spawn.’",
         options=['have to', 'can', 'must', 'should'], correct=2, why='mc1why'),
    dict(stem="The server's welcome sign says: ‘All new players ______ read "
              "the rules before joining a world.’",
         options=['must', 'have to', 'need to', 'ought to'], correct=1, why='mc2why'),
    dict(stem="A sign at the cave entrance: ‘Danger! You ______ enter without a torch.’",
         options=["mustn't", 'have to', 'can', "don't have to"], correct=0, why='mc3why'),
    dict(stem="It's creative mode, so building costs nothing. You ______ collect "
              "wood — you already have unlimited blocks.",
         options=["don't have to", 'are not allowed to', 'must', "mustn't"], correct=0, why='mc4why'),
    dict(stem="Yesterday's game was brutal — the Ender Dragon attacked twice! "
              "I ______ rebuild my base from scratch.",
         options=['must', 'have to', 'had to', 'has to'], correct=2, why='mc5why'),
    dict(stem="The quest board says Alex ______ collect 64 blocks of wood before "
              "she can start the next mission.",
         options=['must', 'has to', "mustn't", "doesn't have to"], correct=1, why='mc6why'),
]

GAPS = [
    ("You ______ touch another player's chest without asking. It's strictly "
     "against the rules.",
     ["mustn't|must not"], 'g1why'),
    ("In hardcore mode, Steve ______ be careful — he only has one life, "
     "and that's the game's own rule.",
     ['has to'], 'g2why'),
    ("Last night was a disaster! I ______ fight the Ender Dragon completely "
     "alone because my friend disconnected.",
     ['had to'], 'g3why'),
    ("In creative mode you ______ gather resources — everything is "
     "already unlocked for you.",
     ["don't have to|do not have to"], 'g4why'),
    ("I ______ log off now — I've been playing for six hours and I can feel it!",
     ['must'], 'g5why'),
    ("New players ______ read the server rules before they can join a world.",
     ['have to'], 'g6why'),
]

MATCH = [
    ('must', 'An obligation you feel yourself'),
    ('have to', 'An obligation that comes from outside you'),
    ("mustn't", 'Forbidden — do not do this'),
    ("don't have to", "No obligation — you can, but you don't need to"),
    ('had to', 'An obligation in the past'),
    ('will have to', 'An obligation that starts in the future'),
]


def build():
    D.assert_no_key_is_longest(MC, 'MustHaveTo')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Must &amp; <em>Have To</em>',
                'Two ways to say you have no choice — and why the game keeps '
                'testing the difference',
                [('Level', 'A2 &middot; Elementary'),
                 ('Focus', 'must vs have to &amp; the negative trap'),
                 ('Count', '16 slides')])

        + D.teach('rwEyebrow', 'Before you play',
                  'rwTitle', 'Whose rule is it?',
                  [('rw1h', "MUST — it's your own idea", 'rw1b',
                    'Use <strong>must</strong> when the obligation comes from you '
                    '— your own opinion, feeling or decision. <em>I must save '
                    'my progress before I log off.</em>',
                    'rw1n', '<em>Must you…?</em> sounds very formal in a '
                            'question. <em>Do you have to…?</em> is what '
                            'people actually say.'),
                   ('rw2h', "HAVE TO — someone else's rule", 'rw2b',
                    'Use <strong>have to</strong> when the obligation comes from '
                    'outside you — a rule, a law, another person. <em>In '
                    'survival mode you have to eat, or your health drops.</em>',
                    'rw2n', '<strong>Has to</strong> for he / she / it: '
                            '<em>Steve has to sleep before morning.</em>')],
                  folder=F, bg='hero.jpg')

        + D.teach('trEyebrow', 'The trap',
                  'trTitle', "Mustn't is not the opposite of must",
                  [('tr1h', "MUSTN'T — forbidden", 'tr1b',
                    "<strong>Mustn't</strong> means it is forbidden — do not "
                    "do this. <em>You mustn't dig straight down; lava might be "
                    "waiting.</em>",
                    'tr1n', 'A warning sign uses <em>mustn’t</em>, never '
                            '<em>don’t have to</em>.'),
                   ('tr2h', "DON'T HAVE TO — no obligation", 'tr2b',
                    "<strong>Don't have to</strong> means there's no obligation "
                    "— you can if you want, but nothing forces you. <em>In "
                    "creative mode you don't have to mine for resources.</em>",
                    'tr2n', 'Opposites in meaning, not just in form. Confusing '
                            'these two is the single most common mistake with '
                            'this grammar.')],
                  folder=F, bg='desert.jpg')

        + D.teach('pfEyebrow', 'Other times',
                  'pfTitle', 'Must has no past — and no future',
                  [('pf1h', 'HAD TO — the past', 'pf1b',
                    "<strong>Must</strong> doesn't change for the past. Use "
                    "<strong>had to</strong> instead. <em>I had to respawn three "
                    "times last night.</em>",
                    'pf1n', 'Same for questions and negatives: <em>Did you have '
                            'to fight it alone?</em>'),
                   ('pf2h', 'WILL HAVE TO — the future', 'pf2b',
                    'For an obligation that starts later, use <strong>will have '
                    'to</strong>. <em>After this update, you will have to find a '
                    'new seed.</em>',
                    'pf2n', 'Never <em>will must</em> — two modal-like forms '
                            'never stack.')],
                  folder=F, bg='hillside.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow', 'Activity 1 &middot; Which form?',
                       'mcTitle', 'Choose the correct word', folder=F, bg=bg)
                  for i, (q, bg) in enumerate(zip(MC,
                      ['hero.jpg', 'desert.jpg', 'hillside.jpg', 'pig.jpg', 'hero.jpg', 'desert.jpg'])))

        + "".join(D.gap(n + 1, 3, part, None,
                        'gapEyebrow', 'Activity 2 &middot; Type it in',
                        'gapTitle', 'Complete the sentence', folder=F, bg=bg,
                        hint_key='gapHint',
                        hint='Contractions and full forms are both fine — '
                             '<em>mustn’t</em> or <em>must not</em>, either works.',
                        width=180, size=18)
                  for n, (part, bg) in enumerate(zip(
                      [GAPS[:2], GAPS[2:4], GAPS[4:]],
                      ['hillside.jpg', 'pig.jpg', 'hero.jpg'])))

        + D.match(MATCH, 'matchEyebrow', 'Activity 3 &middot; The six forms',
                  'matchTitle', 'Match the form to what it means',
                  'matchHint', 'Click a form, then click what it means.',
                  'matchWhy', folder=F, bg='desert.jpg')

        + D.results('resNext', 'You can pick the right form. Now use it &rarr;',
                    folder=F, bg='pig.jpg')

        + D.activate('Explain the rules of your world', 'Use at least four:', CHIPS,
                     'Speaking &middot; in pairs',
                     'One of you is an experienced player explaining the rules '
                     'to someone brand new. Two minutes each, then swap.',
                     ['Tell your partner three things a new player must do in '
                      'their first ten minutes.',
                      "Warn your partner about two things they mustn't do, and "
                      'explain why.',
                      "Say one thing you don't have to do in easy mode, and one "
                      'thing you do have to do.',
                      'Describe something that happened to you in a game and '
                      'explain what you had to do about it.'],
                     'Writing &middot; 100&ndash;130 words',
                     'Write a short survival guide for a new player joining your '
                     'favourite game or world. Say what they must do, what they '
                     "mustn't do, and what they don't have to worry about. Use "
                     'at least one sentence with <em>had to</em>, about '
                     'something that has already happened to you.',
                     'The first thing you have to do is…',
                     folder=F, bg='hero.jpg')
    )

    import i18n_musthaveto as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Must &amp; Have To — Minecraft Edition (A2) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairings, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH), len(s)))


if __name__ == '__main__':
    build()
