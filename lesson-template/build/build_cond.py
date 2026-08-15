# -*- coding: utf-8 -*-
"""Business Conditionals (B2) — rebuilt as a deck.

The brief was explicit: state the rules at the start. The old page went
straight into fifteen questions and taught the grammar only in the feedback
after each one, so a learner met the three conditionals in pieces, out of
order, and never side by side. Two teaching slides now open the deck: the
three conditionals in one table, then the formal business variants —
<em>unless</em>, <em>provided that</em>, and the two inversions that carry
most formal correspondence.

The old page also ran two scales at once: ten points per item on the badge,
one per item in the final total. The deck engine counts scored elements once.

Every option in the five multiple-choice items keeps its own explanation,
which the deck engine supports — telling a learner why THEIR answer was wrong
is worth more than restating why the key was right.
"""
import sys
sys.path.insert(0, '/tmp')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-lesson (2).html'
F = 'Business2'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090e0d;
  --surface       : #121c1a;
  --surface2      : #1a2925;
  --border        : #b57b68;
  --text          : #f5f3f2;
  --text-dim      : #bfaaa3;
  --accent        : #e9ad9a;
  --accent-bright : #f8b59f;
  --accent-dim    : #d37354;
  --secondary     : #0b1311;
  --contrast      : #1dedbb;''' % F

MC = [
    dict(stem='If the board <strong>approves</strong> the merger, the company ______ its market share significantly.',
         options=['will expand noticeably', 'would be expanding steadily',
                  'expanded very significantly', 'would expand substantially'],
         correct=0,
         ex=['First conditional: <em>if</em> + present simple &rarr; <em>will</em> + bare infinitive. The approval is realistic, so <strong>will expand</strong>.',
             'Close, but the simple form is what a real future outcome takes. <em>Will be expanding</em> describes a process, not a result.',
             'Past simple. It cannot follow a present-tense <em>if</em>-clause about a future possibility.',
             'Second-conditional structure, which would mean the approval is unlikely &mdash; contradicting <em>approves</em>.'],
         why='First conditional: <em>if</em> + present simple &rarr; <em>will</em> + bare infinitive.'),
    dict(stem='______ we had invested in that technology earlier, we would not be facing these supply chain issues today.',
         options=['Had', 'Although', 'If', 'Provided'],
         correct=0,
         ex=['<strong>Had we invested</strong> is an inverted third conditional &mdash; the formal written form of <em>If we had invested&hellip;</em>.',
             '<em>Although</em> introduces a contrast, not a condition. It cannot carry regret about a past action.',
             'Grammatical as <em>If we had invested</em>, but the sentence is already inverted: the verb comes first, so <em>If</em> would make it ungrammatical.',
             '<em>Provided</em> needs <em>that</em> and a present tense. It cannot take the past perfect.'],
         why='The inversion <em>Had we invested&hellip;</em> is the formal third conditional, common in business writing.'),
    dict(stem='If our competitors <strong>were to reduce</strong> their prices by 20%, our sales division ______ a significant response strategy.',
         options=['would certainly need', 'will certainly need',
                  'certainly needed then', 'would have needed'],
         correct=0,
         ex=['<em>Were to</em> + infinitive is a formal hypothetical, and it pairs with <strong>would</strong> + bare infinitive.',
             '<em>Will need</em> implies the event is likely, but <em>were to reduce</em> marks it as hypothetical.',
             'Past simple does not pair with <em>were to reduce</em>.',
             '<em>Would have needed</em> is a third-conditional result &mdash; past unreal. The <em>if</em>-clause here is present hypothetical.'],
         why='<em>Were to</em> + infinitive is the formal second conditional. The result clause takes <em>would</em>.'),
    dict(stem='Unless the client ______ by Friday, we will cancel the contract automatically.',
         options=['confirms payment promptly', 'would confirm the payment',
                  'had confirmed the payment', 'will confirm their payment'],
         correct=0,
         ex=['<em>Unless</em> = <em>if&hellip;not</em>, and it introduces a real future condition: present simple in the clause, <em>will</em> in the result.',
             '<em>Would confirm</em> is second-conditional mood. The result clause here is <em>will cancel</em>, so the condition is real.',
             'Past perfect belongs to the third conditional. This sentence looks forward.',
             'This is the classic error: never <em>will</em> after <em>if</em> or <em>unless</em>.'],
         why='<em>Unless</em> takes the present simple, exactly like <em>if</em>. Never <em>will</em> in the condition clause.'),
    dict(stem='If the CEO <strong>had announced</strong> the restructuring last quarter, the board ______ more time to prepare a response.',
         options=['would have had enough', 'would have enough time',
                  'will have had sufficient', 'had had sufficient time'],
         correct=0,
         ex=['Third conditional: <em>if</em> + past perfect &rarr; <strong>would have</strong> + past participle. It did not happen, so the board did not get the time.',
             '<em>Would have</em> alone is incomplete &mdash; the result clause needs the past participle too.',
             'Future perfect. It has no place in a third conditional.',
             'Past perfect belongs in the <em>if</em>-clause, not in the result.'],
         why='Third conditional: <em>if</em> + past perfect &rarr; <em>would have</em> + past participle.'),
]

VERBS = [
    ('Provided that all stakeholders ______ <em>(agree)</em> to the revised terms, the contract will be signed by the end of the month.',
     ['agree|agrees'],
     '<em>Provided that</em> introduces a real condition, so present simple. Both forms are accepted here.'),
    ('If the development team ______ <em>(start)</em> testing earlier, we would not have missed the launch deadline.',
     ['had started'],
     'Third conditional: <em>if</em> + past perfect. The testing did not start early &mdash; this is an imagined past.'),
    ('If I ______ <em>(be)</em> in your position, I would renegotiate the terms before signing anything.',
     ['were|was'],
     'Second conditional. <strong>Were</strong> is the subjunctive form preferred in business writing; <em>was</em> is also heard.'),
    ('Should the auditors ______ <em>(identify)</em> any discrepancies, the finance director will be notified immediately.',
     ['identify'],
     '<em>Should</em> + subject + base verb is an inverted first conditional &mdash; the formal equivalent of <em>If the auditors identify&hellip;</em>.'),
    ('The project ______ <em>(be)</em> completed on time if the supplier had delivered the components as scheduled.',
     ['would have been'],
     'Third-conditional result clause: <em>would have</em> + past participle. The supplier did not deliver, so the project was not completed.'),
]

EMAIL = [
    ('Dear Mr Harrington, we are writing to confirm that ______ the new warehouse capacity, your delivery lead times will decrease by roughly 30%.',
     ['once we expand'],
     'A real future condition. <em>Unless we expand</em> would reverse the meaning; <em>if we had expanded</em> puts it in an unreal past.'),
    ('Please note that if ______ the invoice by the 15th, a late payment fee of 2% will be applied automatically.',
     ['you do not settle'],
     'Present simple in the condition clause. <em>Will not settle</em> is the error to avoid after <em>if</em>.'),
    ('We would strongly recommend reconsidering the timeline &mdash; ______ at this pace, we risk alienating key stakeholders.',
     ['if we continue'],
     'A first conditional used as a warning about a real, current trend: present simple in both halves.'),
    ('______ required, our technical team is available to provide a full system demonstration at your offices.',
     ['Should this be'],
     'Inverted first conditional &mdash; highly formal, and the standard way to offer something in correspondence.'),
    ('In retrospect, ______ the partnership agreement more carefully at the outset, we would not have encountered these disputes.',
     ['had we reviewed'],
     'Inverted third conditional. <em>In retrospect</em> confirms it: this is regret about the past.'),
]
BANK = sorted(['once we expand', 'you do not settle', 'if we continue',
               'Should this be', 'had we reviewed',
               'unless we expand', 'if we continued', 'have we reviewed'])

CHIPS = ['if + present &rarr; will', 'if + past &rarr; would', 'if + past perfect &rarr; would have',
         'unless', 'provided that', 'Should this be&hellip;', 'Had we&hellip;']


def build():
    D.assert_no_key_is_longest(MC, 'Conditionals')
    pos = D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in EMAIL for a in aa])
    logo = D.logo_from(TPL)

    def mcslide(i, q):
        opts = "\n          ".join(
            '<button class="opt"%s data-explain="%s">%s</button>'
            % (' data-correct' if n == q['correct'] else '', D.esc(e), o)
            for n, (o, e) in enumerate(zip(q['options'], q['ex'])))
        return '''
    <section class="slide" data-type="mc">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="qEyebrow">Choose the conditional</span> &middot; %d / 5</div>
        <h2 class="slide-title" data-i18n="qTitle">Complete the sentence</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">%s</p>
        <div class="opts">
          %s
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (i, q['stem'], opts, D.esc(q['why']))

    slides = (
        D.cover(logo, 'Business <em>Conditionals</em>',
                'The three conditionals, plus the formal inversions that carry professional correspondence',
                [('Level', 'B2 &middot; Grammar'), ('Focus', 'Conditionals at work'),
                 ('Count', '15 slides')])
        + D.teach('rulesEyebrow', 'The rules, stated once',
                  'rulesTitle', 'Three conditionals, three time frames',
                  [('c1h', 'First &mdash; real',
                    '<em>if</em> + present simple &rarr; <strong>will</strong> + verb',
                    'c1b', '&ldquo;If the board approves the merger, the company <em>will expand</em>.&rdquo; Something that may well happen.'),
                   ('c2h', 'Second &mdash; hypothetical',
                    '<em>if</em> + past simple &rarr; <strong>would</strong> + verb',
                    'c2b', '&ldquo;If I <em>were</em> in your position, I <em>would</em> renegotiate.&rdquo; Unlikely, or simply imagined.'),
                   ('c3h', 'Third &mdash; unreal past',
                    '<em>if</em> + past perfect &rarr; <strong>would have</strong> + participle',
                    'c3b', '&ldquo;If the CEO <em>had announced</em> it, the board <em>would have had</em> time.&rdquo; It did not happen. This is regret.')],
                  folder=F)
        + D.teach('formEyebrow', 'What business writing does instead',
                  'formTitle', 'Four formal variants worth recognising on sight',
                  [('v1h', 'unless',
                    '= <em>if&hellip;not</em>. Real condition, present simple.',
                    'v1b', '&ldquo;<em>Unless</em> the client confirms by Friday&hellip;&rdquo; Never <em>will</em> after it.'),
                   ('v2h', 'provided that / once',
                    'A condition with a hint of a guarantee attached.',
                    'v2b', '&ldquo;<em>Provided that</em> all stakeholders agree&hellip;&rdquo; Present tense, always.'),
                   ('v3h', 'Should + subject + verb',
                    'Inverted first conditional. Formal, and very common.',
                    'v3b', '&ldquo;<em>Should this be</em> required&hellip;&rdquo; = <em>If this should be required&hellip;</em>'),
                   ('v4h', 'Had + subject + participle',
                    'Inverted third conditional. The written form of regret.',
                    'v4b', '&ldquo;<em>Had we reviewed</em> the agreement&hellip;&rdquo; = <em>If we had reviewed&hellip;</em>')],
                  cols='1fr 1fr 1fr 1fr', folder=F)
        + "".join(mcslide(i + 1, q) for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 2, part, None, 'vEyebrow', 'The form in brackets',
                        'vTitle', 'Put the verb in the right tense', folder=F,
                        hint_key='vHint',
                        hint='Type the form of the bracketed verb that the conditional needs.',
                        width=210)
                  for n, part in enumerate([VERBS[:3], VERBS[3:]]))
        + "".join(D.gap(n + 1, 3, part, BANK, 'eEyebrow', 'Straight from the inbox',
                        'eTitle', 'Complete the email extract', folder=F,
                        hint_key='eHint',
                        hint='Three of the eight phrases in the bank are wrong for these gaps.',
                        width=230)
                  for n, part in enumerate([EMAIL[:2], EMAIL[2:4], EMAIL[4:]]))
        + D.results('resNext', 'You can pick the form. Now write one →')
        + D.activate('Write the difficult email', 'Use at least four:', CHIPS,
                     'Discussion &middot; in pairs',
                     'Argue both sides. One of you is the supplier, one the client.',
                     ['A delivery is late. State the consequence with <em>unless</em>, without threatening.',
                      'Offer something conditionally: <em>provided that&hellip;</em> Make the condition specific.',
                      'Look back at a decision that went wrong. Use the inversion: <em>Had we&hellip;</em>',
                      'Offer help formally with <em>Should this be required&hellip;</em> Then say the same thing casually.'],
                     'Writing &middot; 120&ndash;160 words',
                     'A supplier has missed two deadlines. Write the email that sets a condition without ending the relationship.',
                     'Dear Mr Harrington,')
    )

    import i18n_cond as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Business Conditionals — B2', I)
    print('wrote %s — %d slides, %d MC, %d verb gaps, %d email gaps, bank %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(VERBS), len(EMAIL),
             pos, len(s)))


if __name__ == '__main__':
    build()
