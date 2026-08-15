# -*- coding: utf-8 -*-
"""Conditionals in The Curious Incident (B2) — rebuilt as a deck.

Everything scored survives: six multiple-choice items, five gaps and five
matched conditionals. The multiple choice here was already well built — no key
was conspicuously the longest option, which is rarer than it should be.

Four things were fixed rather than carried over.

The lesson had no teaching. All four conditional types were explained only in
the feedback after each item, so a learner met them one at a time, out of
order, and never saw them side by side. Two slides now open the deck: the four
conditionals in one table, then the connectors and inversions.

Question 5's explanation called the answer "a mixed conditional" while
correctly describing a third conditional. It is a third conditional; the
explanation now says so, and a separate line explains what a mixed conditional
actually is, since the item sits next to one.

Two sentences were framed as excerpts from the novel with a gap cut into
them. They are not in Haddon's text. They are perfectly good B2 sentences, so
they stay — as sentences written in Christopher's voice, which is what they
are, rather than as quotations.

And the matching activity scored every *attempt*, so a learner who guessed
twice was marked out of a larger denominator than one who guessed once. The
deck engine scores pairs.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-lesson-curious incident.html'
F = 'CuriousIncident'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090d0e;
  --surface       : #12191c;
  --surface2      : #1a2429;
  --border        : #cc6e61;
  --text          : #f5f2f2;
  --text-dim      : #bfa7a3;
  --accent        : #f5a99e;
  --accent-bright : #ffb3a8;
  --accent-dim    : #e76350;
  --secondary     : #04171f;
  --contrast      : #1deda3;''' % F

MC = [
    dict(ctx='Christopher cannot tell lies. A sentence in his own voice, describing how he always behaves:',
         stem='&ldquo;I know that ______ someone asks me to describe something, I will always tell the exact truth.&rdquo;',
         options=['if', 'unless', 'although', 'provided that'],
         correct=0,
         why='<strong>If</strong> is the zero-conditional marker: this is a universal truth about how Christopher works. <em>Unless</em> would reverse the meaning, and <em>although</em> is concessive, not conditional.'),
    dict(ctx='Christopher imagines what would have happened if he had never found Wellington.',
         stem='Which sentence uses the third conditional correctly?',
         options=['If Christopher hadn&rsquo;t found Wellington, he wouldn&rsquo;t have started investigating.',
                  'If Christopher hasn&rsquo;t found Wellington, he wouldn&rsquo;t have started investigating.',
                  'If Christopher didn&rsquo;t find Wellington, he wouldn&rsquo;t have started investigating.',
                  'If Christopher wouldn&rsquo;t find Wellington, he hadn&rsquo;t started investigating then.'],
         correct=0,
         why='Third conditional: <em>if</em> + past perfect &rarr; <strong>would have</strong> + past participle. It describes a past that did not happen and a consequence that therefore did not either.'),
    dict(ctx='Siobhan is advising Christopher about social situations. She chooses a formal structure.',
         stem='&ldquo;______ you to trust people more, conversations would feel less overwhelming.&rdquo;',
         options=['Were', 'Had', 'Should', 'If you would'],
         correct=0,
         why='<strong>Were you to&hellip;</strong> is the formal inversion of <em>If you were to&hellip;</em> &mdash; a second conditional. <em>Had</em> inverts the third conditional; <em>Should</em> inverts the first.'),
    dict(ctx='Christopher likes statements that are true every time, without exception.',
         stem='Which sentence expresses a general scientific truth &mdash; a zero conditional?',
         options=['If you heat water to 100&deg;C, it boils.',
                  'If you would heat water to 100&deg;C, it boils.',
                  'If you had heated water to 100&deg;C, it boils.',
                  'If you heated the water to 100&deg;C, it would boil.'],
         correct=0,
         why='Zero conditional: present simple in <em>both</em> clauses. Not a prediction and not a hypothesis &mdash; a fact that holds every time.'),
    dict(ctx='Christopher reflects: &ldquo;I wish Father hadn&rsquo;t lied to me.&rdquo;',
         stem='Which conditional thought follows from that?',
         options=['If he hadn&rsquo;t lied, I would have trusted him more.',
                  'If he hadn&rsquo;t lied, I would be trusting him now.',
                  'If he didn&rsquo;t lie, I would trust him rather more now.',
                  'If he wouldn&rsquo;t lie, I will have trusted him by now.'],
         correct=0,
         why='Third conditional throughout: an unreal past condition and an unreal past result. Option B is a <em>mixed</em> conditional &mdash; past condition, present result &mdash; which is also correct English, but it says something different: that he does not trust his father <em>now</em>.'),
    dict(ctx='Christopher&rsquo;s routines are not optional for him.',
         stem='Which sentence uses <em>unless</em> correctly in a first conditional?',
         options=['Unless he follows his routine, he will become distressed.',
                  'Unless he will follow his routine, he becomes distressed.',
                  'Unless he would follow his routine, he will become distressed.',
                  'Unless he had followed his routine, he will become distressed.'],
         correct=0,
         why='<strong>Unless</strong> means <em>if not</em>, and it behaves exactly like <em>if</em>: present simple in the clause, <em>will</em> in the result. Never <em>will</em> after <em>unless</em>.'),
]

GAPS = [
    ('If Christopher ______ so methodical, he would never have solved the mystery of Wellington&rsquo;s death.',
     ["hadn't been"],
     'Third conditional, negative: <em>if</em> + past perfect. <strong>Hadn&rsquo;t been</strong> sets up a past that did not happen.'),
    ('If Christopher ______ better at reading facial expressions, social interactions would be far simpler for him.',
     ['were|was'],
     'Second conditional. <strong>Were</strong> is the subjunctive form used for every subject in careful writing; <em>was</em> is common in speech.'),
    ('Provided that his mother ______ to him sooner, he would not have believed she was dead for so long.',
     ['had written'],
     '<em>Provided that</em> works like <em>if</em>. The third conditional needs <strong>had</strong> + past participle in the condition clause.'),
    ('Christopher will attempt the A-level maths exam ______ his school supports him properly.',
     ['as long as'],
     '<strong>As long as</strong> means <em>on condition that</em> &mdash; a real future possibility, so a first conditional. <em>Despite</em> is not a conditional connector at all.'),
    ('If he ______ to London alone, he would never have discovered his own independence.',
     ['had not travelled|hadn’t travelled|had not traveled'],
     'Third conditional again. The journey did happen, so the sentence imagines the version where it did not.'),
]
BANK = sorted(["hadn't been", 'were', 'had written', 'as long as', 'had not travelled',
               "wouldn't have been", 'wrote', 'unless', 'even if', 'despite'])

MATCH = [
    ('If Christopher had known the truth from the start,', 'he would have felt far less betrayed by his father.'),
    ('Unless Siobhan explains the social rules clearly,', 'Christopher finds everyday conversation confusing.'),
    ('If he were to meet a stranger on the street,', 'he would most likely ignore them entirely.'),
    ('Had his father been honest earlier,', 'the family crisis might never have escalated.'),
    ('Christopher will keep solving problems logically', 'provided that nobody interferes with his methods.'),
]

CHIPS = ['if + present &rarr; present', 'if + present &rarr; will', 'if + past &rarr; would',
         'if + past perfect &rarr; would have', 'unless', 'as long as', 'Were you to&hellip;',
         'Had he&hellip;']


def build():
    D.assert_no_key_is_longest(MC, 'Curious Incident')
    pos = D.assert_bank_is_not_a_key(BANK, [a.split('|')[0] for _, aa, _ in GAPS for a in aa])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Conditionals in <em>The Curious Incident</em>',
                'Four conditional types, learned through the logic of Christopher Boone',
                [('Level', 'B2 &middot; Grammar in literature'),
                 ('Focus', 'Conditionals'), ('Count', '15 slides')])
        + D.teach('condEyebrow', 'The four types, side by side',
                  'condTitle', 'What each conditional is actually claiming',
                  [('c0h', 'Zero &mdash; always true',
                    '<em>if</em> + present &rarr; <strong>present</strong>',
                    'c0b', '&ldquo;If you heat water to 100&deg;C, it boils.&rdquo; No exceptions. Christopher&rsquo;s favourite kind of sentence.'),
                   ('c1h', 'First &mdash; likely',
                    '<em>if</em> + present &rarr; <strong>will</strong> + verb',
                    'c1b', '&ldquo;Unless he follows his routine, he <em>will</em> become distressed.&rdquo; A real future.'),
                   ('c2h', 'Second &mdash; imagined',
                    '<em>if</em> + past &rarr; <strong>would</strong> + verb',
                    'c2b', '&ldquo;If he <em>were</em> better at reading faces, it would be simpler.&rdquo; Not true now, and unlikely.'),
                   ('c3h', 'Third &mdash; unreal past',
                    '<em>if</em> + past perfect &rarr; <strong>would have</strong> + participle',
                    'c3b', '&ldquo;If he <em>hadn&rsquo;t</em> found Wellington&hellip;&rdquo; It did happen. This imagines the version where it did not.')],
                  cols='1fr 1fr 1fr 1fr', folder=F)
        + D.teach('connEyebrow', 'Everything else that starts a condition',
                  'connTitle', 'Four connectors and two inversions',
                  [('n1h', 'unless',
                    '= <em>if&hellip;not</em>. Takes the present simple.',
                    'n1b', '&ldquo;<em>Unless</em> he follows his routine&hellip;&rdquo; Never <em>will</em> or <em>would</em> after it.'),
                   ('n2h', 'provided that / as long as',
                    'A condition with a promise attached.',
                    'n2b', '&ldquo;&hellip;<em>provided that</em> nobody interferes with his methods.&rdquo; Present tense, always.'),
                   ('n3h', 'Were you to&hellip;',
                    'The formal second conditional, inverted.',
                    'n3b', '= <em>If you were to&hellip;</em> Slightly literary; Siobhan speaks like this, Christopher does not.'),
                   ('n4h', 'Had he&hellip;',
                    'The formal third conditional, inverted.',
                    'n4b', '&ldquo;<em>Had</em> his father been honest earlier&hellip;&rdquo; = <em>If his father had been honest&hellip;</em>')],
                  cols='1fr 1fr 1fr 1fr', folder=F, bg='steps.jpg')
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Christopher&rsquo;s logic',
                       'qTitle', 'Which conditional?', folder=F,
                       ctx=q['ctx'], bg='steps.jpg' if i % 2 else None)
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 2, part, BANK, 'gapEyebrow', 'The exact form',
                        'gapTitle', 'Complete the conditional', folder=F,
                        hint_key='gapHint',
                        hint='Five of the ten items in the bank belong to no gap here. The bracket after each sentence is a hint, not part of the answer.',
                        width=210, size=18)
                  for n, part in enumerate([GAPS[:3], GAPS[3:]]))
        + D.match(MATCH, 'matchEyebrow', 'Two halves of one thought',
                  'matchTitle', 'Match the opening to its ending',
                  'matchHint', 'Click an opening, then click the ending that fits it.',
                  'The tense of the opening clause decides the ending every time. Had his father been honest is past perfect, so the ending has to be would have or might have — nothing in the present will fit it.',
                  folder=F)
        + D.results('resNext', 'You can name them. Now use them to imagine something →')
        + D.activate('Imagine it otherwise', 'Use at least four:', CHIPS,
                     'Discussion &middot; in pairs',
                     'Christopher&rsquo;s story turns on things people did and did not say. Argue about them.',
                     ['If Christopher had never found Wellington, what would the novel have been? Two versions each.',
                      'Was the father right to lie? Answer with <em>if he hadn&rsquo;t</em>, not with <em>yes</em> or <em>no</em>.',
                      'Give Christopher three rules for a situation he finds hard, using <em>unless</em> and <em>as long as</em>.',
                      'Take one regret of your own and say it twice: third conditional, then mixed.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write the chapter Christopher would have written if his father had told him the truth on the first day.',
                     'If Father had told me the truth that evening,')
    )

    import i18n_curious as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Conditionals in The Curious Incident — B2', I)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, bank %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH),
             pos, len(s)))


if __name__ == '__main__':
    build()
