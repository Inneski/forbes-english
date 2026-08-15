# -*- coding: utf-8 -*-
"""Mine, Yours, Hers (A1) — rebuilt as a deck.

Lena and Sophie survive, and so do all fifteen practice items. Almost
everything else needed work, because this lesson had more wrong with it than
any other in the batch.

**Two items were unanswerable.** Multiple choice 2 and 4 each carried *two*
blanks in a two-turn exchange &mdash; "Is this pencil ___?" / "Yes, it is
___!" &mdash; but only one key. The first blank needs <em>yours</em> and the
second needs <em>mine</em>. On item 2 <em>yours</em> was not even among the
options; on item 4 it was, so a learner who reasoned correctly from the first
blank was marked wrong. Both are now single-blank.

**One explanation taught the opposite of the truth.** "The speaker always uses
mine, not hers or yours" &mdash; and then two activities later the lesson has
Sophie ask Lena "Is this pencil case <em>yours</em>?" A speaker uses whichever
pronoun the owner requires. The rule is now stated properly.

**One sentence contradicted its own explanation.** "It is not hers &mdash; it
belongs to Sophie", glossed as "hers = belonging to Sophie". That reads as: it
is not Sophie's, it belongs to Sophie.

**And two identical structures had opposite keys.** "Lena and Sophie share a
locker. The locker is ___" was keyed <em>ours</em>; "The two girls share a
desk. The desk is ___" was keyed <em>theirs</em>. Both are narration, so both
are <em>theirs</em> unless the girls are speaking. Every item that needs a
speaker now says who is speaking.

Two more things. <em>His</em> was promised in the aim, put in the word bank,
and never once tested &mdash; there is now an item for it. And the explanations
were written in metalanguage an A1 learner cannot read: "independent
possessives", "the independent form", "no noun directly after". At this level
the rule is: <strong>the noun disappears</strong>.
"""
import sys
sys.path.insert(0, '/tmp')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-possessive-pronouns-a1.html'
F = 'Possessives'

PALETTE = '''  --hero: url('%s/hero.jpg');

  /* The locker corridor is the busiest hero on the site: hard-edged vertical
     louvres at high contrast, right behind the reading area. A light theme on
     top of it left the question stems fighting the artwork, so this lesson
     runs dark and drops the background well below the usual strength. Both
     departures are deliberate and both were made because text suffered. */
  --bg-opacity    : 0.30;

  --void          : #0a0d0a;
  --surface       : #141914;
  --surface2      : #1e251e;
  --border        : #853f47;
  --text          : #f5f2f2;
  --text-dim      : #bfa3a6;
  --accent        : #e0616f;
  --accent-bright : #eb8692;
  --accent-dim    : #a62837;
  --secondary     : #315582;
  --contrast      : #b8e62a;''' % F

MC = [
    dict(stem='Lena has a red bag. Sophie has a blue bag. The blue bag is ______.',
         options=['hers', 'mine', 'ours', 'yours'], correct=0,
         why='The bag belongs to <strong>Sophie</strong>, so it is <strong>hers</strong>. We do not say <em>her</em> here, because there is no word after it.'),
    dict(stem='Sophie asks Lena: &ldquo;Is this pencil ______?&rdquo;',
         options=['yours', 'mine', 'hers', 'theirs'], correct=0,
         why='Sophie is talking <strong>to Lena</strong>, so she says <strong>yours</strong>. If Lena answers, she says <em>Yes, it is mine.</em>'),
    dict(stem='Lena and Sophie say: &ldquo;This locker is ______. We use it together.&rdquo;',
         options=['ours', 'yours', 'theirs', 'hers'], correct=0,
         why='The two girls are speaking, and it belongs to <strong>both of them</strong>. <em>We</em> &rarr; <strong>ours</strong>.'),
    dict(stem='The teacher says: &ldquo;That red pen is ______. Please give it back.&rdquo;',
         options=['mine', 'hers', 'yours', 'theirs'], correct=0,
         why='The teacher is speaking about <strong>her own</strong> pen. When <em>I</em> speak about my own thing, I say <strong>mine</strong>.'),
    dict(stem='Lena points at two bags. &ldquo;Those bags belong to the boys. They are ______.&rdquo;',
         options=['theirs', 'ours', 'yours', 'hers'], correct=0,
         why='The bags belong to <strong>the boys</strong> &mdash; <em>they</em> &rarr; <strong>theirs</strong>. Lena is not one of the boys, so it is not <em>ours</em>.'),
    dict(stem='Tom has a black jacket. The black jacket is ______.',
         options=['his', 'hers', 'ours', 'mine'], correct=0,
         why='<strong>His</strong> is the easy one: it does not change. <em>his</em> jacket &rarr; the jacket is <strong>his</strong>.'),
]

TYPED = [
    ('Sophie has a pink ruler. The pink ruler is ______.', ['hers'],
     'It belongs to <strong>Sophie</strong> &rarr; <strong>hers</strong>.'),
    ('Lena says: &ldquo;That sandwich is ______! Please don&rsquo;t eat it!&rdquo;', ['mine'],
     'Lena is speaking about her own sandwich &rarr; <strong>mine</strong>.'),
    ('Lena and Sophie say: &ldquo;That classroom is ______ &mdash; we study there every day.&rdquo;', ['ours'],
     'Both girls are speaking, and they share it &rarr; <strong>ours</strong>.'),
    ('The boys left their coats. Are those coats ______?', ['theirs'],
     'They belong to <strong>the boys</strong> &rarr; <strong>theirs</strong>.'),
    ('Sophie asks Lena: &ldquo;Is this pencil case ______?&rdquo;', ['yours'],
     'Sophie is talking <strong>to Lena</strong> &rarr; <strong>yours</strong>.'),
]

BANKED = [
    ('Lena finds a book bag. It is not hers and it is not mine. She gives it to Tom: &ldquo;I think it is ______.&rdquo;', ['his'],
     'The bag belongs to <strong>Tom</strong> &rarr; <strong>his</strong>. Remember that <em>his</em> is the one word that does not change.'),
    ('Sophie says: &ldquo;This red coat is ______!&rdquo;', ['mine'],
     'Sophie is speaking about her own coat &rarr; <strong>mine</strong>.'),
    ('The teacher looks at Lena and asks: &ldquo;Are these pencils ______?&rdquo;', ['yours'],
     'The teacher is talking <strong>to Lena</strong> &rarr; <strong>yours</strong>.'),
    ('The two girls share a desk. The desk is ______.', ['theirs'],
     'Nobody is speaking here &mdash; the sentence is <em>about</em> the girls &rarr; <strong>theirs</strong>. If the girls said it themselves, it would be <em>ours</em>.'),
    ('Lena and Sophie say: &ldquo;That dog is ______ &mdash; we love him!&rdquo;', ['ours'],
     'Both girls are speaking &rarr; <strong>ours</strong>. The word <em>we</em> tells you.'),
]
BANK = sorted(['hers', 'mine', 'yours', 'theirs', 'ours', 'his'])

MATCH = [
    ('my book &rarr; the book is&hellip;', 'mine'),
    ('your book &rarr; the book is&hellip;', 'yours'),
    ('his book &rarr; the book is&hellip;', 'his'),
    ('her book &rarr; the book is&hellip;', 'hers'),
    ('our book &rarr; the book is&hellip;', 'ours'),
    ('their book &rarr; the book is&hellip;', 'theirs'),
]

CHIPS = ['mine', 'yours', 'his', 'hers', 'ours', 'theirs']


def build():
    D.assert_no_key_is_longest(MC, 'Possessives')
    pos = D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in BANKED for a in aa])
    logo = D.logo_from(TPL)

    table = '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="tabEyebrow">The whole rule, on one slide</div>
        <h2 class="slide-title" data-i18n="tabTitle">Two words for the same thing</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px" data-i18n="tabL">With a noun</p>
            <p class="prose" style="font-size:22px;line-height:2">
              <strong>my</strong> bag<br><strong>your</strong> bag<br><strong>his</strong> bag<br>
              <strong>her</strong> bag<br><strong>our</strong> bag<br><strong>their</strong> bag
            </p>
          </div>
          <div class="card">
            <p class="prose dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px" data-i18n="tabR">Without a noun</p>
            <p class="prose" style="font-size:22px;line-height:2">
              the bag is <strong>mine</strong><br>the bag is <strong>yours</strong><br>the bag is <strong>his</strong><br>
              the bag is <strong>hers</strong><br>the bag is <strong>ours</strong><br>the bag is <strong>theirs</strong>
            </p>
          </div>
        </div>
        <div class="card" style="margin-top:12px">
          <p class="prose" style="font-size:19px" data-i18n="tabNote">
            The word on the right is used when the noun <strong>disappears</strong>. Most of them add <strong>-s</strong>. Only <em>his</em> stays the same.
          </p>
        </div>
      </div>
    </section>
'''

    slides = (
        D.cover(logo, 'Mine. Yours. <em>Hers. Ours.</em>',
                'Lena and Sophie are at school in Hamburg, and everything in the corridor belongs to somebody',
                [('Level', 'A1 &middot; Grammar'), ('Focus', 'Possessive pronouns'),
                 ('Count', '16 slides')])
        + table
        + D.teach('whoEyebrow', 'One more thing',
                  'whoTitle', 'The word depends on who is speaking',
                  [('w1h', 'I am speaking',
                    'about <em>my</em> thing &rarr; <strong>mine</strong>',
                    'w1b', 'Lena: &ldquo;That sandwich is <strong>mine</strong>.&rdquo;'),
                   ('w2h', 'I am speaking to you',
                    'about <em>your</em> thing &rarr; <strong>yours</strong>',
                    'w2b', 'Sophie to Lena: &ldquo;Is this pencil <strong>yours</strong>?&rdquo;'),
                   ('w3h', 'Nobody is speaking',
                    'The sentence is <em>about</em> them &rarr; <strong>hers</strong>, <strong>his</strong>, <strong>theirs</strong>',
                    'w3b', '&ldquo;The two girls share a desk. The desk is <strong>theirs</strong>.&rdquo;')],
                  folder=F)
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'In the corridor',
                       'qTitle', 'Choose the right word', folder=F)
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 2, part, None, 'typEyebrow', 'Type the word',
                        'typTitle', 'Complete the sentence', folder=F,
                        hint_key='typHint',
                        hint='No list this time &mdash; type the word yourself.',
                        width=170, size=20)
                  for n, part in enumerate([TYPED[:3], TYPED[3:]]))
        + "".join(D.gap(n + 1, 2, part, BANK, 'bnkEyebrow', 'Choose from the list',
                        'bnkTitle', 'Complete the sentence', folder=F,
                        hint_key='bnkHint',
                        hint='Six words, five gaps. One word is not needed.',
                        width=170, size=19)
                  for n, part in enumerate([BANKED[:3], BANKED[3:]]))
        + D.match(MATCH, 'matchEyebrow', 'The pairs',
                  'matchTitle', 'Match the two forms',
                  'matchHint', 'Click a phrase on the left, then its partner.',
                  'Notice that five of the six add an -s, and his does not change at all. That is the whole pattern, and it is why his is the easiest one and hers is the one people get wrong.',
                  folder=F)
        + D.results('resNext', 'Now say who things belong to, out loud →')
        + D.activate('Whose is it?', 'Use at least four:', CHIPS,
                     'Speaking &middot; in pairs',
                     'Put four or five things on the table between you &mdash; pens, phones, keys, a bag.',
                     ['Point at something and ask: &ldquo;Is this <em>yours</em>?&rdquo; Answer with <em>mine</em> or a name.',
                      'Now describe the table to a third person. Everything becomes <em>hers</em>, <em>his</em> or <em>theirs</em>.',
                      'Find two things you share with your partner. &ldquo;That one is <em>ours</em>.&rdquo;',
                      'Say the same sentence twice: once with the noun, once without. <em>my pen</em> &rarr; <em>mine</em>.'],
                     'Writing &middot; 40&ndash;60 words',
                     'Write five sentences about your classroom. Use a different word each time.',
                     'The blue bag is hers. The pens are…')
    )

    import i18n_poss as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Mine, Yours, Hers — A1', I)

    # Lime for everything that announces a slide. On the dark corridor it reads
    # from the back of a classroom; the palette accent did not.
    css = (
        '\n/* ── per-lesson overrides ──────────────────────────────────────\n'
        '   The locker corridor is the busiest hero on the site, and at A1 the\n'
        '   learner is decoding the English as well as reading it. Two changes:\n'
        '   every heading runs in the lime counterpoint so it separates from the\n'
        '   blue and cream behind it, and the feedback line gets an opaque plate\n'
        '   with black text instead of coloured type on bare artwork — it was\n'
        '   landing across the floor/locker boundary and disappearing into it. */\n'
        '.cover-title, .slide-title, .eyebrow, .q-stem, .q-ctx,\n'
        '.order-hint, .cover-sub { color: var(--contrast); }\n'
        '.cover-title em { color: var(--accent-bright); }\n'
        '.fe-logo-mark { color: var(--contrast); }\n'
        '.feedback.show {\n'
        '  margin-top: 18px; padding: 14px 18px; border-radius: 10px;\n'
        '  background: #f4f1e4; color: #14100c;\n'
        '  border-left: 6px solid var(--contrast);\n'
        '  text-shadow: none; font-size: 18px; line-height: 1.5;\n'
        '}\n'
        '.feedback.show.no { border-left-color: var(--accent-dim); }\n'
        '.feedback.show strong, .feedback.show em { color: inherit; }\n'
        '/* the instruction line sits outside a card, so it needs full-strength\n'
        '   text rather than the dim tone, and the input needs to look typeable */\n'
        '.slide-body > .prose.dim { color: var(--text); }\n'
        'input.gap { background: rgba(245,242,242,0.92); color: #14100c; }\n'
        'input.gap::placeholder { color: #6b6258; }\n'
        '/* the engine focuses the first gap on arrival, and .gap:focus outranks\n'
        '   input.gap, so the focused field went dark while its neighbours went\n'
        '   light. Match the specificity and keep every field readable. */\n'
        'input.gap:focus { background: #ffffff; color: #14100c; }\n'
        'input.gap.correct, input.gap.wrong { background: rgba(245,242,242,0.92); }\n')
    s = s.replace('</style>\n</head>', css + '</style>\n</head>', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d slides, %d MC, %d typed, %d banked, %d pairs, bank %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(TYPED), len(BANKED),
             len(MATCH), pos, len(s)))


if __name__ == '__main__':
    build()
