# -*- coding: utf-8 -*-
"""Modal Verbs (B1) — rebuilt as a deck.

Everything scored in the old page survives: six multiple-choice items, five
modal gaps, five sentences to repair and five sentences to rebuild from
chunks. The ski setting survives too — it is what makes the examples concrete.

Two fixes. The old page stated its rules only inside per-question hint boxes,
so a learner met the grammar one line at a time and never saw it whole; the
rules now open the deck on two slides. And error-correction item 2 was broken
at source — the wrong modal rendered after the sentence instead of inside it,
because the whole sentence sat in the `before` field with `after` empty — so
that item is now written the way the other four are.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-modal-verbs-B1.html'
F = 'ModalsB1'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090e0e;
  --surface       : #121c1c;
  --surface2      : #1a2929;
  --border        : #653d4b;
  --text          : #f5f2f3;
  --text-dim      : #bfa3ad;
  --accent        : #c84071;
  --accent-bright : #dd7299;
  --accent-dim    : #812b4a;
  --secondary     : #4677ae;
  --contrast      : #22e742;''' % F

MC = [
    dict(stem='Maria is an expert skier. She ______ ski on black runs without any difficulty.',
         options=['can', 'must', 'should', 'might'], correct=0,
         why='<strong>Can</strong> is present ability &mdash; something she is able to do. <em>Must</em> is obligation, <em>should</em> is advice, <em>might</em> is possibility.'),
    dict(stem='All skiers ______ wear a helmet on the slopes. It is a resort rule.',
         options=['might', 'could', 'must', 'would'], correct=2,
         why='<strong>Must</strong> is a strong obligation. If the resort makes helmets compulsory, this is the modal &mdash; nothing weaker will do.'),
    dict(stem='You ______ take a lesson before trying the black run. It is very steep.',
         options=['will', 'should', 'must', 'can'], correct=1,
         why='<strong>Should</strong> gives advice. The speaker thinks a lesson is a good idea, but it is not a rule &mdash; <em>must</em> would be too strong.'),
    dict(stem='The weather looks cloudy. It ______ snow this afternoon, but I am not sure.',
         options=['will', 'must', 'might', 'should'], correct=2,
         why='<strong>Might</strong> is uncertainty. <em>Will</em> would mean you are certain, and the second half of the sentence says you are not.'),
    dict(stem='Excuse me, ______ you show me how to put on my ski boots, please?',
         options=['must', 'will', 'should', 'could'], correct=3,
         why='<strong>Could you&hellip;?</strong> is the polite request. <em>Can you?</em> also works but is more direct; <em>must you?</em> asks whether somebody is obliged to do something.'),
    dict(stem='I ______ like to book a ski lesson for tomorrow morning, please.',
         options=['could', 'would', 'must', 'might'], correct=1,
         why='<strong>Would like</strong> is the polite way to state a wish. It is the form to use in any shop, hotel or ticket office.'),
]

GAPS = [
    ('You ______ ski off-piste without a guide. It is extremely dangerous.', ['must not'],
     '<strong>Must not</strong> is prohibition &mdash; forbidden, not merely unwise.'),
    ('When she was younger, Anna ______ ski perfectly, but she has not skied for ten years.', ['could'],
     '<strong>Could</strong> is the past of <em>can</em>: an ability she had and no longer uses.'),
    ('You ______ ski alone on the mountain &mdash; always go with a friend or a guide.', ['should not'],
     '<strong>Should not</strong> is negative advice. Weaker than <em>must not</em>: a recommendation, not a rule.'),
    ('If you practise every day this week, you ______ definitely improve before the race.', ['will'],
     '<strong>Will</strong> is a confident prediction. <em>Might</em> would introduce a doubt the speaker does not have.'),
    ('The forecast is bad, so the lift ______ open tomorrow. We should check the website.', ['might not'],
     '<strong>Might not</strong> is an uncertain negative. <em>Will not</em> would claim knowledge nobody has.'),
]
BANK = sorted(['can', 'could', 'might not', 'must not', 'should not', 'will', 'would', 'must'])

FIX = [
    ('Tom is only five years old, so he <s>must not</s> ski on the difficult runs yet.', 'cannot',
     'This is about ability, not permission. Tom is not <em>able</em> to ski difficult runs, so <strong>cannot</strong>. <em>Must not</em> would mean it is forbidden.'),
    ('<s>Must</s> you help me carry my skis to the chairlift, please?', 'Could',
     'A polite request takes <strong>Could</strong> (or <em>Can</em>). <em>Must you&hellip;?</em> asks whether somebody is obliged to do something &mdash; which is not what you meant.'),
    ('The mountain rescue team <s>should</s> arrive in about twenty minutes &mdash; they called ahead.', 'will',
     'They called ahead, so the arrival is confirmed. <strong>Will</strong> states a certain future; <em>should</em> would only express an expectation.'),
    ('We cannot find your ski poles. You <s>might leave</s> them at the rental shop this morning.', 'might have left',
     'Past possibility is <strong>might have</strong> + past participle. <em>Might leave</em> points forwards, not back.'),
    ('You <s>should book</s> the ski school earlier &mdash; now all the sessions are full.', 'should have booked',
     'Regret about the past is <strong>should have</strong> + past participle. <em>Should book</em> would still be advice about the future, which is too late.'),
]

REORDER = [
    (['You must', 'always check', 'the avalanche forecast', 'before skiing off-piste.'],
     'Subject + modal + bare infinitive. Never <em>to</em> after a modal, and the adverb <em>always</em> sits between the modal and the verb.'),
    (['Beginners', 'should not', 'attempt the black run', 'without an instructor.'],
     'Negative modals are <em>modal + not</em>, then the bare verb. <em>Should not to attempt</em> is wrong.'),
    (['Could you', 'show me', 'how to use the ski lift,', 'please?'],
     'In a modal question the modal comes first: <em>Could + you + bare verb</em>. There is no <em>do</em>.'),
    (['She might', 'have forgotten', 'her ski pass', 'at the hotel.'],
     'Past speculation is <em>might + have + past participle</em>. <em>Might forget</em> would point at the future.'),
    (['We should', 'have booked', 'the ski school sessions', 'in advance.'],
     '<em>Should have booked</em> is regret about something that did not happen &mdash; a core B1 structure.'),
]

CHIPS = ['must / must not', 'should / should not', 'can / could', 'might / might not',
         'will', 'would like', 'should have + past participle']


def build():
    D.assert_no_key_is_longest(MC, 'Modals')
    pos = D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in GAPS for a in aa])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Modal <em>Verbs</em>',
                'can &middot; could &middot; must &middot; should &middot; might &middot; will &middot; would &mdash; learned on a mountain',
                [('Level', 'B1 &middot; Grammar'), ('Focus', 'Modal verbs'), ('Count', '20 slides')])
        + D.teach('mEyebrow', 'What each one does',
                  'mTitle', 'Seven modals, four jobs',
                  [('m1h', 'Ability',
                    '<strong>can</strong> now &middot; <strong>could</strong> in the past',
                    'm1b', '&ldquo;She <em>can</em> ski black runs.&rdquo; &ldquo;When she was younger she <em>could</em> ski perfectly.&rdquo;'),
                   ('m2h', 'Obligation &amp; advice',
                    '<strong>must</strong> = a rule &middot; <strong>should</strong> = advice',
                    'm2b', '<em>Must not</em> is forbidden. <em>Should not</em> is only a bad idea. The gap between them is the whole point.'),
                   ('m3h', 'Certainty',
                    '<strong>will</strong> = sure &middot; <strong>might</strong> = maybe',
                    'm3b', '&ldquo;You <em>will</em> improve.&rdquo; &ldquo;The lift <em>might not</em> open.&rdquo;'),
                   ('m4h', 'Politeness',
                    '<strong>could you&hellip;?</strong> &middot; <strong>I would like&hellip;</strong>',
                    'm4b', 'These two carry almost every polite request you will ever need to make.')],
                  cols='1fr 1fr 1fr 1fr', folder=F)
        + D.teach('fEyebrow', 'The form &mdash; it never changes',
                  'fTitle', 'Modal, then the bare verb. Always.',
                  [('f1h', 'Statement',
                    '<strong>You must check</strong> the forecast.',
                    'f1b', 'Never <em>to check</em>, never <em>checking</em>. The modal takes the plain verb.'),
                   ('f2h', 'Negative &amp; question',
                    '<strong>Beginners should not attempt&hellip;</strong><br><strong>Could you show me&hellip;?</strong>',
                    'f2b', 'Negative: modal + <em>not</em> + verb. Question: the modal jumps to the front. No <em>do</em>, ever.'),
                   ('f3h', 'Talking about the past',
                    '<strong>might have left</strong> &middot; <strong>should have booked</strong>',
                    'f3b', 'Modal + <em>have</em> + past participle. <em>Might leave</em> and <em>should book</em> point at the future instead.')],
                  folder=F)
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'On the mountain',
                       'qTitle', 'Choose the modal', folder=F)
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 2, part, BANK, 'gapEyebrow', 'Which modal',
                        'gapTitle', 'Complete the sentence', folder=F,
                        hint_key='gapHint',
                        hint='Some answers are two words. Type them exactly as they appear in the bank.')
                  for n, part in enumerate([GAPS[:3], GAPS[3:]]))
        + "".join(D.gap(n + 1, 2, [(b, [a], w) for b, a, w in part], None,
                        'fixEyebrow', 'One modal is wrong',
                        'fixTitle', 'Repair the sentence', folder=F,
                        hint_key='fixHint',
                        hint='The crossed-out modal is wrong. Type the form that belongs there.',
                        width=230)
                  for n, part in enumerate([FIX[:3], FIX[3:]]))
        + "".join(D.order(chunks, 'ordEyebrow', 'Word order',
                          'ordTitle', 'Build the sentence',
                          'ordHint', 'Click the chunks in the right order.', why, folder=F)
                  for chunks, why in REORDER)
        + D.results('resNext', 'You can pick them. Now use them out loud →')
        + D.activate('Use all seven', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you works at the ski school. The other has never skied.',
                     ['Give three pieces of advice, and one absolute rule. Make the difference audible.',
                      'Ask politely for three things: a lesson, boots in your size, and the forecast.',
                      'Something went wrong yesterday. Say what you should have done differently.',
                      'Speculate about why your friend is late. Use <em>might have</em> twice.'],
                     'Writing &middot; 80&ndash;120 words',
                     'Write the safety notice for a ski resort. Rules with <em>must</em>, advice with <em>should</em>.',
                     'All skiers must…')
    )

    import i18n_modals as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Modal Verbs — B1', I)
    print('wrote %s — %d slides, %d MC, %d gaps, %d fixes, %d reorders, bank %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(FIX),
             len(REORDER), pos, len(s)))


if __name__ == '__main__':
    build()
