# -*- coding: utf-8 -*-
"""Alan Watts: The Art of Being Present (B1) — reading, vocabulary, sentence building.

Rebuilt from a standalone scrolling page Innes supplied (forbes-alan-watts-b1.html
in his Downloads): its own Cormorant/DM Sans chrome, a sticky score badge, three
stacked activity blocks, no language switcher, no activation stage, no SEO block.
Everything teachable in it is carried over. What changed, and why:

  * **Comprehension Q5 had the key as the longest option** — "We should focus on
    the present moment rather than worrying about past or future." ran 80
    characters against distractors of 74, 72 and 76, so a learner who had never
    read the passage could take the point on length alone. The three distractors
    are lengthened here (HOUSE-STYLE §7: never shorten the key) and
    `assert_no_key_is_longest` runs over the bank at build time. The other four
    items already passed and are untouched.

  * **The sentence-reorder activity shuffled individual WORDS** — eleven of them
    on the first item. That tests nothing but patience: an eleven-token shuffle
    is a jigsaw, not a grammar exercise, and a learner who knows the pattern
    still spends a minute clicking. Each sentence is re-chunked at the joint the
    item is actually teaching (HOUSE-STYLE §7, "chunk at the joints you are
    teaching, never mid-phrase"), so item 2 is now
    `The harder | you try to sleep, | the more difficult | it becomes` — four
    blocks, and the comparative pattern is visible in the blocks themselves.

  * **Nothing taught the three patterns the reorder was testing.** The activity
    arrived cold after the vocabulary gap-fill and explained itself only in the
    after-the-fact feedback. A teach slide now sits in front of it with the
    that-clause, the `the more… the more…` correlative and `rather than`, one
    card each, in the six-item form so the rule travels into German and Spanish.

  * **The lesson ended on a score.** HOUSE-STYLE §10b: an activation stage is
    required, and this had none. Three speaking prompts and a writing brief with
    a real audience are new here — they are the one part of this deck with no
    source in the original file.

  * The reading passage is unchanged in substance and split across six slides at
    the §6 budget. The pull quote gets a slide of its own because it is the line
    the lesson is built around.

**Editorial style (HOUSE-STYLE §15), at Innes's request — "do a type 2 house
style".** It is the right call for this artwork rather than a preference: all
nine plates are flat vector illustration with large near-white fields, which is
exactly the case §15 was written for. Under the default style the text plate has
to be pushed to near-opaque before `--text-dim` clears AA, at which point the
picture it was supposed to be showing is gone. Here the plates are framed objects
on a flat field instead, and `extract-palette.py` is not run at all — the fixed
brand set is used, verified with `tools/check-editorial-palette.py` (all rows
PASS).

Artwork, replaced 2026-09-22: `plate-a` … `plate-i` are nine still lifes —
the coat on the hook, the chair facing the sun, two chairs nobody sits in —
commissioned to `docs/ARTWORK-alan-watts.md`. They replace an interim set of
nine generated Watts portraits, on Innes's call: the house editorial stem says
*no people, no faces*, and repeated generated likenesses of a real named man
get worse the more of them there are.

Seven arrived native 7:6, which is the frame's own ratio and the first time
`--ar 7:6` has taken in this repo. The microphone and the river stone came back
16:9 and are cut to 7:6 here — the stone by its own subject centroid, the
microphone right-aligned by hand, because the dark wall panel on its left
captured the centroid and sliced the microphone off the right edge.

`hero.jpg` is still the ZEN/TAO/NOW/BEING diagram. It is the one slot the new
set does not cover, and it is centred, so the cover title sits on the word ZEN.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_watts as I

EN = I.T['en']

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-alan-watts-b1.html'
F = 'alan-watts'

# `.read-col` and `.read-ask` are builder-local in the reference deck too — the
# template ships only the editorial `.read-para` type rule, so the column that
# holds the passage has to come from here. Kept to the two rules that matter:
# a measure the eye can track, and the space between paragraphs.
EXTRA_CSS = '''
/* ── reading column ─────────────────────────────────────────────── */
.read-col { max-width: 41em; }
.read-para + .read-para { margin-top: 13px; }
.read-para mark { background: none; color: var(--accent-bright); font-weight: 600; }
/* The pull quote is the one place this deck raises its voice. It is a
   cover-style moment on an interior slide, so it takes the display face like
   the cover title does and nothing else on the slide competes with it. */
.pull-quote {
  font-family: var(--font-display); font-size: 31px; line-height: 1.34;
  font-weight: 500; font-style: italic; color: var(--accent-bright);
}
.pull-quote + .read-para { margin-top: 18px; }
'''


# ══════════════════════════════════════════════════════════════════════
# READING — the passage, unchanged in substance, split at the §6 budget
# ══════════════════════════════════════════════════════════════════════
def arched(bg):
    """True if this picture can take the 190px arch.

    The arch eats the top corners, so it needs a subject with air above it.
    The nine still lifes have that; the nine Watts portraits are
    head-and-shoulders that fill the frame and come back with the hair cut
    off. So the arch follows the PICTURE, not the deck — which is why this is
    a function and not one flag for the whole build."""
    return bg.startswith('plate-')


def reading(eyebrow_key, title_key, paras, bg, side=None, arch=None):
    """A passage slide: prose straight on the field, picture framed beside it.

    paras: list of (key, 'class') pairs — the text itself lives in i18n_watts,
    because at B1 the passage is the scaffolding the questions stand on and a
    learner who cannot read it cannot start (HOUSE-STYLE §8 keeps the *target*
    language in English; this is the lesson's own prose, not the target).
    """
    body = "\n          ".join(
        '<p class="prose %s" data-i18n="%s">%s</p>' % (cls, k, EN[k])
        for k, cls in paras)
    if arch is None:
        arch = arched(bg)
    extra = ''
    if side == 'left':
        extra += ' data-art-side="left"'
    if arch:
        extra += ' data-art="arch"'
    # A passage carries prose, so it takes the narrow picture and the wide
    # column — §15's data-art-size="narrow".
    extra += ' data-art-size="narrow"'
    return '''
    <section class="slide" data-type="teach"%s%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="read-col">
          %s
        </div>
      </div>
    </section>
''' % (D._bg(F, bg), extra, eyebrow_key, EN[eyebrow_key], title_key,
       EN[title_key], body)


def art(slide, side=None, shape=None, size=None):
    """Tag a slide with how the editorial style places its picture."""
    extra = ''
    if side == 'left':
        extra += ' data-art-side="left"'
    if shape == 'arch':
        extra += ' data-art="arch"'
    if size:
        extra += ' data-art-size="%s"' % size
    return slide.replace('<section class="slide"',
                         '<section class="slide"' + extra, 1)


# ══════════════════════════════════════════════════════════════════════
# COMPREHENSION — five items, each option carrying its own explanation
# ══════════════════════════════════════════════════════════════════════
COMP = [
    dict(stem='What was the main goal of Alan Watts&rsquo; work?',
         options=['He wanted to criticise Western science and its technology.',
                  'He wanted Westerners to understand Eastern philosophy.',
                  'He wanted people to move to Asia and study religion there.',
                  'He wanted to prove Buddhism better than the other faiths.'],
         correct=1,
         why='He spent most of his life explaining Zen, Taoism and Hinduism to '
             'people in the West.',
         ex=['He offered an alternative; he never attacked science.',
             None,
             'He brought the ideas west rather than sending anyone east.',
             'He was not ranking religions against each other.']),

    dict(stem='What was &ldquo;the illusion of the separate self&rdquo;?',
         options=['He believed identity comes only from memory and experience.',
                  'He thought the self vanishes in deep meditation or in sleep.',
                  'He argued people wrongly feel separate from the world.',
                  'He suggested our character comes from other people&rsquo;s hopes.'],
         correct=2,
         why='The illusion is feeling like a stranger looking out at nature, '
             'rather than being part of it.',
         ex=['The passage is about separation, not where identity comes from.',
             'Nothing has the self vanishing &mdash; it was never separate.',
             None,
             'Other people&rsquo;s expectations are not what the illusion is.']),

    dict(stem='Which example explains <em>wu wei</em>?',
         options=['Watching a flower grow slowly without any effort at all.',
                  'Walking in nature and clearing your mind of every thought.',
                  'Reading a hard book by relaxing and not concentrating much.',
                  'Trying to fall asleep, which is harder the more you force it.'],
         correct=3,
         why='Sleep is the example: effort is exactly what stops it working.',
         ex=['The flower is in the passage, but under impermanence.',
             'This is closer to meditation, which is not used here.',
             'Reading is not one of the passage&rsquo;s examples.',
             None]),

    dict(stem='How did Watts view the idea of impermanence?',
         options=['He found it frightening and told people not to think of it.',
                  'He accepted it and celebrated it: it makes life precious.',
                  'He thought it applied only to flowers and plants in nature.',
                  'He argued it is an illusion and that things last forever.'],
         correct=1,
         why='The value comes from the limit: a life that did not end would not '
             'be precious.',
         ex=['The passage says the opposite &mdash; he urged people not to.',
             None,
             'The flower illustrates the idea; it is not the limit of it.',
             'The illusion in this lesson is the separate self.']),

    # The distractors here are lengthened, not the key shortened (HOUSE-STYLE
    # §7). In the source file the key ran 80 characters against 74, 72 and 76 —
    # the longest option on the slide, and a free point.
    dict(stem='What was Watts&rsquo; central message?',
         options=['We should plan the future and learn from our past mistakes.',
                  'Eastern religions are the only true path to inner peace.',
                  'We should focus on the present, not the past or future.',
                  'The mind must be empty of thought before peace is possible.'],
         correct=2,
         why='Stop worrying about the future, stop regretting the past, be alive '
             'in this moment.',
         ex=['This is close to what he argued against.',
             'He explained Eastern ideas without claiming they were the only way.',
             None,
             'An empty mind is a meditation instruction; his point was '
             'attention.']),
]

# ══════════════════════════════════════════════════════════════════════
# VOCABULARY — seven words, seven spaces, split 3/2/2 at the §6 budget
# ══════════════════════════════════════════════════════════════════════
# The bank is alphabetised so its order is not the gap order — otherwise the
# exercise is answerable straight down the list (deck.assert_bank_is_not_a_key).
BANK = ['effortless', 'engaged', 'illusion', 'impermanence', 'precious',
        'separate', 'universe']

ROWS_1 = [
    ('Watts believed that the idea of a ______ self is a mistake &mdash; we are '
     'all connected.', ['separate'],
     '<em>Separate</em> is the adjective: a separate self, separate from the world.'),
    ('He said that you are not outside the ______ &mdash; you are part of it.',
     ['universe'],
     'Not a synonym for <em>world</em> here: he means everything there is.'),
]

ROWS_2 = [
    ('The concept of <em>wu wei</em> refers to ______ action &mdash; doing things '
     'naturally without forcing them.', ['effortless'],
     '<em>Effortless</em> describes the action, so it goes straight in front of it.'),
    ('The ______ of all things means nothing lasts forever &mdash; and Watts '
     'thought this was beautiful.', ['impermanence'],
     'The noun: <em>impermanent</em> is the adjective, <em>impermanence</em> the '
     'quality itself.'),
]

ROWS_3 = [
    ('Our lives are ______ because they are short &mdash; their value comes from '
     'their limits.', ['precious'],
     '<em>Precious</em> means valuable in a way that money does not measure.'),
    ('Watts said the secret of life is to be fully ______ with what you are doing '
     'right now.', ['engaged'],
     '<em>Engaged with</em> something means absorbed in it &mdash; not the '
     'engagement before a marriage.'),
]

ROWS_4 = [
    ('Believing we are separate from nature is, according to Watts, an ______ '
     '&mdash; a false idea that causes unhappiness.', ['illusion'],
     'An <em>illusion</em> is a false idea you believe, not a magic trick.'),
]


# ══════════════════════════════════════════════════════════════════════
# SENTENCE BUILDING — chunked at the joint each item is teaching
# ══════════════════════════════════════════════════════════════════════
ORDERS = [
    (['Watts believed', 'that the present moment', 'is the only real thing'],
     'After <em>believed</em>, the whole second idea arrives as one block, '
     'introduced by <em>that</em>.'),
    (['The harder', 'you try to sleep,', 'the more difficult', 'it becomes'],
     'A correlative comparative: <em>the</em> + comparative in both halves, and '
     'the second half is the result of the first.'),
    (['He encouraged people', 'to accept change', 'rather than fear it'],
     '<em>Encourage someone to do</em> something takes the infinitive; '
     '<em>rather than</em> then rejects the alternative.'),
    (['Nothing lasts forever,', 'and that is', 'what makes life beautiful'],
     '<em>What makes life beautiful</em> is a noun clause &mdash; it is the '
     'thing <em>that is</em> points at.'),
    (['You are not a stranger', 'in the world;', 'you are part of it'],
     'Two clauses balanced across a semicolon: the negative first, the '
     'correction second. This is Watts&rsquo; whole argument in one sentence.'),
]


# Six-item cards: (head_key, head, body_key, body, note_key, note). The VALUE
# has to be the English string, not None. deck.py interpolates it straight into
# the HTML, so a None prints the literal word "None" — invisible at runtime,
# because data-i18n overwrites it, but it is what a crawler and `seo.py`'s
# rules() read, and a None note renders no note element at all, which silently
# dropped all three example sentences.
TEACH_PATTERNS = [
    ('patA', EN['patA'], 'patAb', EN['patAb'], 'patAn', EN['patAn']),
    ('patB', EN['patB'], 'patBb', EN['patBb'], 'patBn', EN['patBn']),
    ('patC', EN['patC'], 'patCb', EN['patCb'], 'patCn', EN['patCn']),
]


# Eight, and short. The strip sits above both tracks, so every line it wraps
# to pushes the open panel down by that much — at ten chips, two of them full
# phrases, the writing panel ran 27px past the canvas.
CHIPS = ['the present moment', 'impermanence', 'wu wei', 'effortless action',
         'the separate self', 'fully engaged with', 'to force it',
         'to accept change']


def build():
    D.assert_no_key_is_longest(COMP, 'COMP')
    D.assert_bank_is_not_a_key(
        BANK, [a for rows in (ROWS_1, ROWS_2, ROWS_3, ROWS_4) for _, ans, _ in rows
               for a in ans])

    logo = D.logo_from(TPL)

    # Eighteen pictures now: nine Watts portraits (watts-*) and nine still
    # lifes (plate-*). They are not interchangeable and the split is the
    # lesson's own — **a portrait where the slide is about the man, an object
    # where it is about the idea.** The separate self is a coat that shares an
    # edge with its own shadow; wu wei is water parting round a stone. Putting
    # his face on those would say "here is Watts again" where the slide is
    # trying to say something specific.
    #
    # Innes, 2026-09-23: the portraits stay. An earlier pass read "no bearded
    # man in the shopping list" as "replace the portraits" and cut all nine.
    # They were restored from 614a7b0.
    READ = [
        # the man
        ('eWho', 'tWho', [('pWho1', 'read-para'), ('pWho2', 'read-para')],
         'watts-c.jpg', None),
        # him speaking — the line is his, so he is on the slide
        ('eQuote', 'tQuote', [('pQuote1', 'pull-quote'),
                              ('pQuote2', 'read-para dim')], 'watts-d.jpg', 'left'),
        # the three ideas, as objects
        ('eSelf', 'tSelf', [('pSelf1', 'read-para'), ('pSelf2', 'read-para')],
         'plate-a.jpg', None),
        ('eWu', 'tWu', [('pWu1', 'read-para'), ('pWu2', 'read-para')],
         'plate-d.jpg', 'left'),
        ('eImp', 'tImp', [('pImp1', 'read-para'), ('pImp2', 'read-para')],
         'plate-b.jpg', None),
        # why we still hear him: the recordings, so the microphone
        ('eLeg', 'tLeg', [('pLeg1', 'read-para'), ('pLeg2', 'read-para')],
         'plate-e.jpg', 'left'),
    ]

    # Comprehension is about what HE said, so it runs on his face — and it is
    # the one run long enough to show five different portraits.
    MC_BG = ['watts-a.jpg', 'watts-b.jpg', 'watts-f.jpg', 'watts-h.jpg',
             'watts-i.jpg']
    # Vocabulary is about the words, so it runs on the objects.
    GAP_BG = ['plate-f.jpg', 'plate-h.jpg', 'plate-c.jpg', 'plate-i.jpg']
    # Sentence building returns to him. Two unused portraits first, then the
    # three earliest MC faces again — far enough back not to read as a repeat.
    ORDER_BG = ['watts-e.jpg', 'watts-g.jpg', 'watts-a.jpg', 'watts-b.jpg',
                'watts-f.jpg']

    slides = (
        D.cover(logo, EN['coverTitle'], EN['coverSub'],
                [('Level', EN['chipLevel']),
                 ('Focus', EN['chipFocus']),
                 ('Count', 'COUNT slides')])

        + "".join(reading(ek, tk, paras, bg, side) for ek, tk, paras, bg, side in READ)

        + "".join(art(D.mc(i + 1, len(COMP), q, 'eComp', EN['eComp'],
                           'tComp', EN['tComp'], folder=F, explains=q['ex'],
                           bg=MC_BG[i]),
                      side='left' if i % 2 else None, size='narrow',
                      shape='arch' if arched(MC_BG[i]) else None)
                  for i, q in enumerate(COMP))

        + "".join(
            art(D.gap(i + 1, 4, rows, BANK, 'eVocab', EN['eVocab'], 'tVocab',
                      EN['tVocab'], folder=F, bg=bg, hint_key='hVocab',
                      hint=EN['hVocab'], width=200),
                side='left' if i % 2 else None, size='narrow',
                shape='arch' if arched(bg) else None)
            for i, (rows, bg) in enumerate(
                zip((ROWS_1, ROWS_2, ROWS_3, ROWS_4), GAP_BG)))

        # Three cards and a picture will not fit (§15), so this slide has none.
        + D.teach('ePat', EN['ePat'], 'tPat', EN['tPat'], TEACH_PATTERNS,
                  cols='1fr 1fr 1fr', folder=F)

        + "".join(art(D.order(items, 'eOrder', EN['eOrder'], 'tOrder',
                              EN['tOrder'], 'hOrder', EN['hOrder'], why,
                              folder=F, bg=ORDER_BG[i]),
                      side='left' if i % 2 else None, size='narrow',
                      shape='arch' if arched(ORDER_BG[i]) else None)
                  for i, (items, why) in enumerate(ORDERS))

        + D.results(folder=F, bg='plate-i.jpg')

        + D.activate(
            EN['actTitle'], EN['actUse'], CHIPS,
            'Speaking', EN['actSpeakBrief'],
            [EN['actSpeak1'], EN['actSpeak2'], EN['actSpeak3']],
            EN['actWriteKind'], EN['actWriteBrief'], EN['actPlaceholder'],
            folder=F, bg='plate-g.jpg')
    )

    s = D.assemble(TPL, OUT, slides, D.editorial_palette('%s/hero.jpg' % F),
                   'Alan Watts: The Art of Being Present — Forbes English',
                   I, langs=('en', 'de', 'es'), style='editorial')

    s = s.replace('\n</style>', EXTRA_CSS + '</style>', 1)

    # The count chip is written once the deck knows how long it is. Counting
    # `<section class="slide` returns N+1 — the template keeps one of its own
    # that never ships — so count the ones carrying a data-type.
    n = len(re.findall(r'<section class="slide[^>]*\bdata-type=', s))
    s = s.replace('COUNT slides', '%d slides' % n)
    s = s.replace('COUNT Folien', '%d Folien' % n)
    s = s.replace('COUNT diapositivas', '%d diapositivas' % n)

    open(OUT, 'w', encoding='utf-8', newline='').write(s)
    print('%s — %d slides (editorial)' % (OUT, n))


if __name__ == '__main__':
    build()
