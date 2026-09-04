# -*- coding: utf-8 -*-
"""Nietzsche on Film — C1 Vocabulary, Part V — rebuilt as a 16:9 deck.

`nietzsche-film-vocab-c1-part5.html`, the strongest of the six Nietzsche pages
and the first of them off the scrolling format. All fifteen scored items
survive, in their five sections of three: critical terminology, collocation,
register and connotation, phrasal verbs and idiom, word formation.

What changed, beyond the format:

- **The key sequence was a cycle.** From question five onward the answers ran
  `c, b, d, a` repeated verbatim to the end — and Part IV of the same series
  uses the identical sequence, character for character, because the two pages
  are the same build re-skinned. A learner who spotted it took ten of the
  fifteen without reading. New positions in `nietzsche5_data.py`, and the
  runtime shuffle now moves them again on every load.
- **Question six was keyed against its own stem.** The sentence gave the
  definition of *unprecedented* — no studio had taken that risk before — and
  then marked *groundbreaking* correct, while the explanation conceded that
  unprecedented "means never done before". Re-keyed.
- **Question fifteen was not a word-formation item.** It sat in the derivation
  section, its key was a collocation with an added adjective, and its own
  feedback said several options were correct before marking them wrong.
  Replaced with a genuine derivation on the same root.
- **It now teaches properly.** The original opened each section with a rubric
  paragraph explaining what was being tested, which is better than most of this
  library manages, but it never taught the language. Three slides do: the terms
  that only look like ordinary words, the register scale that is the actual C1
  skill here, and the mechanics of collocation and suffix. Every one of the
  fifteen items sits inside one of the three.

Artwork is the existing `Nietzsche/` family — six flat-vector portraits in
coral, slate and cream, already on disk and already used by this series. The
camera portrait, `img3-hero.jpg`, was this page's own hero and stays the cover;
the other five become per-slide backgrounds. The `-pattern.jpg` variants are
pre-dimmed for a scrolling page and are not used here, because the deck dims
its own backgrounds and would dim them twice.

`--void` is lifted off the derived near-black to a grey, per Innes's standing
preference. Every other token is `extract-palette.py` output unedited; a
re-derivation would put the black back.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from nietzsche5_data import MC

TPL = 'lesson-template/lesson-template.html'
OUT = 'nietzsche-film-vocab-c1-part5.html'
F = 'Nietzsche'

# python3 lesson-template/extract-palette.py Nietzsche/img3-hero.jpg
PALETTE = '''  --hero: url('%s/img3-hero.jpg');

  --void          : #2d3134;
  --surface       : #12191c;
  --surface2      : #1a2429;
  --border        : #a14d41;
  --text          : #f5f2f2;
  --text-dim      : #bfa7a3;
  --accent        : #e67262;
  --accent-bright : #f3a79c;
  --accent-dim    : #c63a26;
  --secondary     : #0a1920;
  --contrast      : #1deda2;''' % F

CHIPS = ['mise-en-scène', 'non-diegetic', 'verisimilitude', 'the definitive',
         'ersatz', 'eschew', 'for all its', 'countenance', 'restrained']

# One section, one background. Five sections, five portraits.
SEC = [
    ('s1Eyebrow', 'Section 1 &middot; Critical terminology',
     's1Title', 'The term the field would use', 'img4-hero.jpg'),
    ('s2Eyebrow', 'Section 2 &middot; Precise collocation',
     's2Title', 'The word that goes with this word', 'img2-hero.jpg'),
    ('s3Eyebrow', 'Section 3 &middot; Register and connotation',
     's3Title', 'Right meaning, wrong temperature', 'img5-hero.jpg'),
    ('s4Eyebrow', 'Section 4 &middot; Phrasal verbs and idiom',
     's4Title', 'What a professional would actually say', 'img6-hero.jpg'),
    ('s5Eyebrow', 'Section 5 &middot; Word formation',
     's5Title', 'The right shape of the right word', 'img3-hero.jpg'),
]


def build():
    D.assert_no_key_is_longest(MC, 'Nietzsche5')
    logo = D.logo_from(TPL)

    questions = "".join(
        D.mc(n + 1, 3, MC[s * 3 + n], ek, e, tk, t, folder=F, bg=bg)
        for s, (ek, e, tk, t, bg) in enumerate(SEC)
        for n in range(3))

    slides = (
        D.cover(logo, 'Nietzsche <em>on Film</em>',
                'The vocabulary of film criticism, and the C1 skill of choosing a word '
                'by its register rather than its meaning',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Film criticism vocabulary'),
                 ('Count', '21 slides')])

        + D.teach('termEyebrow', 'Before the questions',
                  'termTitle', 'Terms that only look like ordinary words',
                  [('te1h', '<em>Mise-en-sc&egrave;ne</em> is not the camera', 'te1b',
                    'It is everything composed <em>inside</em> the frame &mdash; set, '
                    'light, costume, where the actors stand. '
                    '<strong>Cinematography</strong> is the camera and the lighting '
                    'technique; <strong>blocking</strong> is movement alone.',
                    'te1n', 'Three terms, three different jobs. Critics do not use '
                            'them loosely.'),
                   ('te2h', 'Diegetic means inside the story', 'te2b',
                    'A piano playing in the room is <strong>diegetic</strong>: the '
                    'characters could hear it. A score is '
                    '<strong>non-diegetic</strong>: only the audience can. The line is '
                    'drawn by who can hear it, not by what it sounds like.',
                    'te2n', 'A radio a character switches on is diegetic. The same '
                            'tune over the credits is not.'),
                   ('te3h', '<em>Verisimilitude</em> is not realism', 'te3b',
                    'Verisimilitude is seeming true <em>within the conventions of the '
                    'work</em>. Realism names an artistic movement. '
                    '<strong>Authenticity</strong> is a cultural claim; '
                    '<strong>continuity</strong> is only consistency between shots.',
                    'te3n', 'A fantasy film can have high verisimilitude. It cannot be '
                            'realist.')],
                  folder=F, bg='img3-hero.jpg')

        + D.teach('regEyebrow', 'The C1 move',
                  'regTitle', 'Four words, one meaning, four temperatures',
                  [('re1h', 'The distractors are not wrong', 're1b',
                    'At C1 the wrong answer is rarely false. <em>Derivative</em>, '
                    '<em>imitative</em>, <em>unoriginal</em> and <em>ersatz</em> all '
                    'say a work copies. Only <strong>ersatz</strong> accuses it of '
                    'pretending to be the real thing.',
                    're1n', 'Read what the sentence is doing, not only what it means.'),
                   ('re2h', 'Register follows the document', 're2b',
                    'In a press release a director does not <em>bail out</em> or '
                    '<em>quit</em>; she <strong>withdraws</strong>. The informal word '
                    'is not a smaller version of the formal one &mdash; it carries a '
                    'judgement the formal one refuses.',
                    're2n', 'The right word in the wrong register is still the wrong '
                            'word.'),
                   ('re3h', 'Praise has a scale too', 're3b',
                    '<em>Memorable</em> is unforgettable. <em>Outstanding</em> is very '
                    'good. <strong>Definitive</strong> claims something narrower and '
                    'larger: the version future performances will be measured against.',
                    're3n', 'Ask what the critic is committing to, not how enthusiastic '
                            'they sound.')],
                  folder=F, bg='img5-hero.jpg')

        + D.teach('formEyebrow', 'The mechanics',
                  'formTitle', 'Collocation, and the shape of a word',
                  [('fo1h', 'Fixed phrases have no logic to appeal to', 'fo1b',
                    'A studio <strong>greenlights</strong> a film; nothing else does. '
                    'Funding arrives <strong>at the eleventh hour</strong>, never '
                    '<em>in</em> or <em>on</em> it. These are learned whole or got '
                    'wrong.',
                    'fo1n', '<em>Authorised</em> and <em>permitted</em> are not wrong '
                            'English. They are the wrong industry.'),
                   ('fo2h', 'Suffixes carry word class', 'fo2b',
                    '<em>-al</em> and <em>-ment</em> tend to make nouns, <em>-ive</em> '
                    'and <em>-ic</em> adjectives, <em>-ly</em> adverbs. <em>Evoke</em> '
                    'becomes <strong>evocative</strong>, the way <em>demonstrate</em> '
                    'becomes <em>demonstrative</em>.',
                    'fo2n', 'If the suffix does not exist (<em>evocational</em>), the '
                            'word does not either.'),
                   ('fo3h', 'A nominalisation is not a gerund', 'fo3b',
                    '<strong>Portrayal</strong> is the noun that formal criticism '
                    'reaches for. <em>Portraying</em> is a verb doing a noun&rsquo;s '
                    'work &mdash; possible, weaker; <em>portrait</em> is a different '
                    'object altogether.',
                    'fo3n', 'Academic register prefers the derived noun. It is why this '
                            'prose feels dense.')],
                  folder=F, bg='img6-hero.jpg')

        + questions

        + D.results('resNext', 'You can name it. Now write the review &rarr;',
                    folder=F, bg='img3-hero.jpg')

        + D.activate('Review the film', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you has just seen the film and thinks it works; the other '
                     'reviews for a broadsheet and does not. Four minutes each, then '
                     'swap.',
                     ['Describe one scene by its mise-en-sc&egrave;ne, without saying '
                      '&ldquo;good&rdquo; or &ldquo;beautiful&rdquo;.',
                      'Criticise a performance you otherwise admired. Pick the word '
                      'that carries exactly as much blame as you mean.',
                      'Defend the non-diegetic score against the charge that it tells '
                      'the audience what to feel.',
                      'Say what the film gets right about Nietzsche and what it '
                      'flattens &mdash; and hedge the second.'],
                     'Writing &middot; 200&ndash;250 words',
                     'Write the review a quality newspaper would print. Praise one '
                     'thing precisely, object to one thing precisely, and let the '
                     'register do the work: no intensifiers, and no word chosen for '
                     'being stronger rather than right.',
                     'For all the assurance of its mise-en-scène, the film…',
                     folder=F, bg='img4-hero.jpg')
    )

    import i18n_nietzsche5 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Nietzsche on Film — C1 Vocabulary · Part V | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(s)))


if __name__ == '__main__':
    build()
