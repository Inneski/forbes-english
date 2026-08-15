# -*- coding: utf-8 -*-
"""Talking with Clients (B2) — rebuilt as a deck.

Everything scored survives: five register scenarios, five collocations and
five office idioms. What did not survive is the defect: all five
multiple-choice keys were the longest option on their slide, which on a lesson
about professional register is close to self-defeating, because the
professional answer genuinely is the wordier one. All fifteen distractors were
lengthened to match.

The lesson also had no teaching at all — the grammar and phrasing were only
ever explained after you had already answered. Two slides now open it: the
four moves that hold a client conversation together, and the same message at
three temperatures.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from clients_mc import MC

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-lesson (talking with clients).html'
F = 'Clients'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0e0e09;
  --surface       : #1c1c12;
  --surface2      : #29291a;
  --border        : #a05448;
  --text          : #f5f2f2;
  --text-dim      : #bfa7a3;
  --accent        : #e37b6b;
  --accent-bright : #f1aea4;
  --accent-dim    : #c6412d;
  --secondary     : #507791;
  --contrast      : #1deda5;''' % F

GAPS = [
    ('I&rsquo;m calling to ______ up on the proposal we sent you last Tuesday.', ['follow'],
     '<strong>Follow up on</strong> is the fixed phrasal verb for checking progress on something already sent. <em>Catch up</em> is social; <em>reflect on</em> is private; <em>take over</em> means to assume control.'),
    ('We&rsquo;d like to ______ a meeting to go over the contract details in person.', ['arrange'],
     '<strong>Arrange a meeting</strong> is the standard collocation. You <em>conduct</em> research, <em>undertake</em> a commitment, and <em>perform</em> a task &mdash; but you arrange a meeting.'),
    ('Please ______ free to contact me if you have any further questions.', ['feel'],
     '<strong>Feel free to</strong> is a fixed closing phrase. <em>Make free</em>, <em>stay free</em> and <em>keep free</em> are all possible English, and none of them means this.'),
    ('We need to ______ the client&rsquo;s expectations before we begin the project.', ['manage'],
     '<strong>Manage expectations</strong> is the phrase that names one of the actual jobs. <em>Control</em> sounds authoritarian, and <em>adjust</em> means changing expectations that already exist.'),
    ('I&rsquo;d like to ______ your attention to the budget section of the report.', ['draw'],
     '<strong>Draw attention to</strong> is the formal standard. <em>Bring to your attention</em> also exists, but takes a different structure and is slightly heavier.'),
]
BANK = sorted(['follow', 'arrange', 'feel', 'manage', 'draw',
               'reflect', 'conduct', 'handle', 'point', 'catch'])

MATCH = [
    ('Touch base', 'Make brief contact to check on progress'),
    ('Circle back', 'Return to a topic or a person later on'),
    ('On the same page', 'In agreement, with a shared understanding'),
    ('Moving forward', 'From now on, or as the next step'),
    ('Take it offline', 'Discuss privately, outside the meeting'),
]

CHIPS = ['follow up on', 'arrange a meeting', 'feel free to', 'manage expectations',
         'draw your attention to', 'just to confirm', 'I&rsquo;m afraid']


def build():
    D.assert_no_key_is_longest(MC, 'Clients')
    pos = D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in GAPS for a in aa])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Talking with <em>Clients</em>',
                'Meetings, calls and negotiations &mdash; and the register that holds them together',
                [('Level', 'B2 &middot; Professional English'), ('Focus', 'Client communication'),
                 ('Count', '14 slides')])
        + D.teach('movesEyebrow', 'Before the questions',
                  'movesTitle', 'Four moves that carry a client conversation',
                  [('mv1h', '1 &middot; Acknowledge first',
                    '<em>I see where you&rsquo;re coming from&hellip;</em> &middot; <em>We completely understand your frustration&hellip;</em>',
                    'mv1b', 'Say what you heard before you say what you think. Skipping this is what makes a correct answer land badly.'),
                   ('mv2h', '2 &middot; Soften the refusal',
                    '<em>I&rsquo;m afraid we can&rsquo;t&hellip;</em> &middot; <em>Could we perhaps explore&hellip;?</em>',
                    'mv2b', '<em>I&rsquo;m afraid</em> costs nothing and changes everything. A bare <em>no</em> reads as a door closing.'),
                   ('mv3h', '3 &middot; Offer something',
                    '<em>&hellip;but I&rsquo;d be happy to discuss what value we can add.</em>',
                    'mv3b', 'Every refusal needs a second half. Without one you have ended the conversation, not answered it.'),
                   ('mv4h', '4 &middot; Confirm the action',
                    '<em>Just to confirm: you send the brief by Friday&hellip;</em>',
                    'mv4b', 'Who does what, by when. <em>At some point</em> and <em>fairly soon</em> are not commitments.')],
                  cols='1fr 1fr 1fr 1fr', folder=F)
        + D.teach('tempEyebrow', 'Register',
                  'tempTitle', 'The same refusal at three temperatures',
                  [('t1h', 'Too cold',
                    '&ldquo;Our prices are fixed and we do not negotiate.&rdquo;',
                    't1b', 'True, and the relationship is now over. A policy is not an answer to a person.'),
                   ('t2h', 'About right',
                    '&ldquo;I&rsquo;m afraid we can&rsquo;t reduce the price, but I&rsquo;d be happy to discuss what value we can add.&rdquo;',
                    't2b', 'Refuses clearly, then opens a door. The client can still say yes to something.'),
                   ('t3h', 'Too warm',
                    '&ldquo;We can change absolutely anything you want &mdash; just tell us.&rdquo;',
                    't3b', 'Agreeing to everything is not service. It tells the client you had no view in the first place.')],
                  folder=F)
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'In front of the client',
                       'qTitle', 'What do you say?', folder=F)
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 2, part, BANK, 'gapEyebrow', 'The exact word',
                        'gapTitle', 'Business English runs on collocation', folder=F,
                        hint_key='gapHint',
                        hint='Five of the ten words in the bank belong to no gap here.')
                  for n, part in enumerate([GAPS[:3], GAPS[3:]]))
        + D.match(MATCH, 'matchEyebrow', 'Office idiom',
                  'matchTitle', 'Five phrases nobody ever explains to you',
                  'matchHint', 'Click a phrase, then click what it means.',
                  'Two of these carry a tone worth noticing: circle back often means not now, and take it offline can mean let us not do this in front of everyone.',
                  folder=F)
        + D.results('resNext', 'Recognising the register is half of it. Now produce it →')
        + D.activate('Handle the difficult client', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you is the client and is not in a good mood. Swap after each round.',
                     ['The client is confused about the timeline. Explain it without sending them back to the brief.',
                      'They ask for a 20% discount. Refuse, and keep them talking.',
                      'They propose something you think is wrong. Disagree without saying no.',
                      'Close the meeting so that both of you leave holding something specific.'],
                     'Writing &middot; 120&ndash;160 words',
                     'A long-standing client writes that your response times have slipped and they are questioning the partnership. Reply.',
                     'Dear Ms Okafor,')
    )

    import i18n_clients as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Talking with Clients — B2', I)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, bank %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH),
             pos, len(s)))


if __name__ == '__main__':
    build()
