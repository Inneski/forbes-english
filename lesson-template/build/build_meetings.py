# -*- coding: utf-8 -*-
"""Open Answer Practice (B2) — rebuilt as a production deck.

This one was different from the others and the rebuild had to respect that.
The page had no multiple choice, no word banks and no answer key by design:
eight scenarios, a free-text box, and feedback from a model. Its own hero line
said so.

The problem is that the grading never worked. The page posted each answer to
api.anthropic.com straight from the browser with no key, no version header and
no proxy, so every submission failed CORS and fell into the catch branch. A
learner only ever saw "Your answer was submitted, but feedback could not be
loaded right now" and a dash where the score should be. Eight scenarios, no
feedback, no score.

So the deck keeps the eight scenarios and the open-answer format, drops the
scoring theatre, and replaces the missing tutor with something that works
without a server: each scenario carries a model answer and a note on what
makes it work. Write first, then compare — which is what the AI feedback was
approximating anyway.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-meetings.html'
F = 'Meetings'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090e0c;
  --surface       : #121c18;
  --surface2      : #1a2923;
  --border        : #b55e53;
  --text          : #f5f2f2;
  --text-dim      : #bfa6a3;
  --accent        : #e99085;
  --accent-bright : #f7aea5;
  --accent-dim    : #d54e3d;
  --secondary     : #040c09;
  --contrast      : #1deda0;''' % F

# (kind, title, scenario, task, model answer, what makes it work)
SCENARIOS = [
    ('Client meeting', 'Opening a meeting',
     'You are meeting Sarah Chen, procurement director of a mid-sized logistics company, for the first time. You sell software that automates invoicing.',
     'Open the meeting: greet her, introduce yourself and your company briefly, and say why you are here.',
     '&ldquo;Good morning, Ms Chen &mdash; thank you for making the time. I&rsquo;m Daniel Reyes from Arcline; we build invoicing automation for logistics operators. I&rsquo;d like to spend twenty minutes understanding how your invoicing runs today, and then show you where we&rsquo;ve saved similar teams about a week a month. Does that work for you?&rdquo;',
     'Three moves in four sentences: who you are, why you are here, and a check that the agenda suits her. The time estimate is what makes it easy to say yes to.'),
    ('Handling objections', 'Responding to price pushback',
     'You have presented your proposal. The client says: &ldquo;The price is higher than we expected. Our current provider charges significantly less.&rdquo;',
     'Respond. Acknowledge the concern, then make the case for your value &mdash; without being defensive and without dropping the price.',
     '&ldquo;That&rsquo;s a fair comparison to draw, and I&rsquo;d want to make it too. Can I ask what&rsquo;s included in their figure? Ours covers implementation and support, which is usually where the difference sits &mdash; and it&rsquo;s the part that decides whether the system is actually used six months in.&rdquo;',
     'It concedes the reasonableness of the objection, asks a question instead of arguing, and moves the comparison onto ground where the price makes sense.'),
    ('Email writing', 'Following up after no reply',
     'You sent a detailed proposal ten days ago. You have heard nothing. You want to follow up without seeming pushy.',
     'Write a subject line and the opening two or three sentences of your follow-up.',
     '<strong>Subject: Following up &mdash; Arcline proposal</strong><br>&ldquo;I hope this finds you well. I wanted to check whether you&rsquo;ve had a chance to look at the proposal I sent on the 3rd. If it would help to talk any of it through, I&rsquo;m happy to find twenty minutes this week.&rdquo;',
     '<em>Had a chance to</em> offers them a reason for the silence. The offer of a short call gives them something easier to say yes to than a full reply.'),
    ('Difficult situations', 'Delivering bad news',
     'A project will be delayed by two weeks because of technical issues at your end. The client has a strict deadline.',
     'Deliver the news. Take responsibility and propose a way forward.',
     '&ldquo;I need to tell you about a delay before it affects your planning. We&rsquo;ve hit a problem in the data migration, and it will push delivery back by two weeks, to the 28th. That&rsquo;s on us. Two things I can offer: we can release the reporting module on the original date so your finance team isn&rsquo;t held up, and I&rsquo;ll send you a written recovery plan by Thursday.&rdquo;',
     'The delay is named with a date, the responsibility is taken in three words, and two concrete offers follow. No hedging, no <em>unforeseen circumstances</em>.'),
    ('Telephone skills', 'Opening a cold call',
     'You are calling Marcus Hoffman, head of operations at a manufacturing company, who has never heard of you. You have about twenty seconds.',
     'Write your opening three or four sentences.',
     '&ldquo;Mr Hoffman, good morning &mdash; Daniel Reyes from Arcline. I&rsquo;ll be brief. We work with manufacturers who are running invoicing through three or four disconnected systems, and we typically cut the month-end close from nine days to three. Is that a problem you recognise, or am I describing someone else&rsquo;s company?&rdquo;',
     'It leads with the problem rather than the product, gives a number, and ends with a question that is genuinely easy to answer either way &mdash; which is what makes it hard to hang up on.'),
    ('Negotiation', 'Asking for a concession',
     'You want a supplier to extend payment terms from 30 days to 60. You do not want to seem demanding, but the cash flow matters.',
     'Raise the request. Write what you would say.',
     '&ldquo;There&rsquo;s one thing I&rsquo;d like to ask about before we finalise. Our cash cycle runs on 60 days with our own customers, so 30-day terms leave us carrying the gap. Would you consider 60? In return I&rsquo;m happy to commit to the full annual volume up front rather than quarterly.&rdquo;',
     'A reason, a specific ask, and something offered back. Asking for a concession without naming what you will trade is how a request becomes a demand.'),
    ('Client relationships', 'Responding to a complaint',
     'A long-standing client writes: &ldquo;We&rsquo;ve been very disappointed with the level of service recently. Response times have been slow and we&rsquo;re starting to question whether this partnership is still working for us.&rdquo;',
     'Write your reply. Acknowledge, apologise where it is warranted, and say what you will do.',
     '&ldquo;Thank you for telling me directly &mdash; I&rsquo;d much rather hear it than not. You&rsquo;re right about the response times; our average has slipped since August and that isn&rsquo;t the service you signed up for. I&rsquo;ve moved your account to a named contact from today, and I&rsquo;ll send you the response figures each Friday for the next month so you can see whether it&rsquo;s actually improving.&rdquo;',
     'Thanking someone for criticism is a strong opening because it costs you nothing and signals you are not about to argue. The check is measurable, and it is offered rather than promised.'),
    ('Closing a deal', 'Asking for the business',
     'Three productive meetings. The client seems interested but has not committed. Today has gone well and you sense the moment.',
     'Ask for the business. Write what you would say.',
     '&ldquo;It sounds as though the fit is there. Shall we make it real? If you&rsquo;re happy in principle, I can have the paperwork with you tomorrow for a start on the first of next month &mdash; and if something is still open, tell me what it is and let&rsquo;s deal with it now rather than in another meeting.&rdquo;',
     'Two doors, both easy to walk through: yes, or tell me what is in the way. The second is what stops a soft close from ending in another round of silence.'),
]

CHIPS = ['I wanted to check whether&hellip;', 'That&rsquo;s a fair point', 'That&rsquo;s on us',
         'Would you consider&hellip;?', 'In return, I&rsquo;m happy to&hellip;',
         'Shall we make it real?', 'Just to confirm']


def scenario_slide(i, s, bg=None):
    kind, title, scene, task, model, note = s
    return '''
    <section class="slide" data-type="discuss"%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="sEyebrow">%s</span> &middot; %d / 8</div>
        <h2 class="slide-title">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px" data-i18n="sCtx">The situation</p>
            <p class="prose" style="font-size:18px">%s</p>
            <p class="prose dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin:14px 0 6px" data-i18n="sTask">Your task</p>
            <p class="prose" style="font-size:18px">%s</p>
          </div>
          <div class="card">
            <p class="prose dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px" data-i18n="sModel">One way to say it &mdash; read after you have written</p>
            <p class="prose" style="font-size:17px">%s</p>
            <p class="prose dim" style="font-size:15px;margin-top:12px">%s</p>
          </div>
        </div>
      </div>
    </section>
''' % (D._bg(F, bg), kind, i, title, scene, task, model, note)


def build():
    logo = D.logo_from(TPL)
    slides = (
        D.cover(logo, 'Say it in <em>your own words</em>',
                'Eight situations, no options to choose from &mdash; write the answer, then read one that works',
                [('Level', 'B2 &middot; Open practice'), ('Focus', 'Meetings, calls &amp; email'),
                 ('Count', '13 slides')])
        + D.teach('howEyebrow', 'How to use this',
                  'howTitle', 'Write first. The model answer is not the point.',
                  [('h1h', '1 &middot; Write it',
                    'Three to five sentences, out loud or on paper, before you look right.',
                    'h1b', 'Reading a good answer teaches you almost nothing. Producing a bad one and then reading a good one teaches you a great deal.'),
                   ('h2h', '2 &middot; Compare the moves',
                    'Not the words &mdash; the moves. What does it do first, and why?',
                    'h2b', 'The model answers are one version, not the version. Yours may be better; check that it does the same jobs.'),
                   ('h3h', '3 &middot; Say it again',
                    'Rewrite your version using one phrase you took from the model.',
                    'h3b', 'One phrase per scenario is a realistic rate. Eight new phrases from one lesson is not.')],
                  folder=F)
        + D.teach('movesEyebrow', 'What nearly every answer needs',
                  'movesTitle', 'Acknowledge, be specific, offer something',
                  [('m1h', 'Acknowledge',
                    '<em>That&rsquo;s a fair point&hellip;</em> &middot; <em>You&rsquo;re right about the response times&hellip;</em>',
                    'm1b', 'Conceding what is true costs nothing and buys you the right to say the rest.'),
                   ('m2h', 'Be specific',
                    '<em>&hellip;back by two weeks, to the 28th.</em> &middot; <em>&hellip;from nine days to three.</em>',
                    'm2b', 'A date or a number turns a soft statement into something the other person can act on.'),
                   ('m3h', 'Offer something',
                    '<em>In return, I&rsquo;m happy to&hellip;</em> &middot; <em>I&rsquo;ll send you the figures each Friday.</em>',
                    'm3b', 'Bad news, a refusal and a request all need a second half. Without one you have only made a statement.')],
                  folder=F)
        + "".join(scenario_slide(i + 1, s, 'hero.jpg' if i % 2 else None)
                  for i, s in enumerate(SCENARIOS))
        + D.activate('Run three of them live', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'Pick three scenarios. Your partner plays the other side and does not make it easy.',
                     ['Cold call: your partner tries to end the call inside fifteen seconds.',
                      'Bad news: your partner asks twice who is at fault. Answer once, then move on.',
                      'Complaint: your partner is not satisfied by your first reply. Do not repeat yourself.',
                      'Close: your partner says &ldquo;let me think about it.&rdquo; Find out what is actually in the way.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Pick the scenario you found hardest and write it properly. Then rewrite it in half the words.',
                     'Dear Ms Chen,')
    )

    import i18n_meetings as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Say it in your own words — B2 open practice', I)
    print('wrote %s — %d slides, %d scenarios, %d bytes'
          % (OUT, s.count('<section class="slide'), len(SCENARIOS), len(s)))


if __name__ == '__main__':
    build()
