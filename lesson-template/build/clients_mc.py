# -*- coding: utf-8 -*-
"""The five multiple-choice items for Talking with Clients, rebalanced.

All five keys were the longest option on their slide. On a lesson about
professional register that is the worst possible failure mode, because the
professional answer genuinely is the more elaborate one — so a learner could
score five out of five on length alone and finish knowing nothing about tone.
Every distractor has been lengthened to sit within a few characters of its
key, and each stays wrong for a reason the lesson teaches: blaming, deflecting,
hedging, over-promising, or ending a meeting without an action point.
"""

MC = [
    dict(
        stem='Your client seems confused about the project timeline. Which response is most professionally appropriate?',
        options=[
            'Allow me to walk you through the key milestones so we&rsquo;re both on the same page.',
            'Perhaps have another look at the brief we sent over &mdash; the timeline is all in there.',
            'The schedule itself is fine; you just need to read the document more carefully.',
            'I think we may have explained this before, but I am very happy to try again.',
        ],
        correct=0,
        why='<strong>Walk you through</strong> offers to do the work, and <strong>on the same page</strong> makes the goal shared rather than corrective. The others send the client back to a document, which is the one thing a confused person does not want.',
    ),
    dict(
        stem='A client has just complained about a delayed delivery. What is the most effective way to open your response?',
        options=[
            'That is not really our fault &mdash; there were supply chain issues well beyond our control.',
            'Delays do happen from time to time, so this was unfortunately quite unavoidable for us.',
            'We completely understand your frustration and sincerely apologise for the inconvenience.',
            'I am sorry, but there is honestly not very much we can do about it at this stage.',
        ],
        correct=2,
        why='Acknowledge the feeling <em>before</em> the apology. Blaming a supply chain, calling the delay inevitable, or opening on your own helplessness all move the problem away from you before you have taken it on.',
    ),
    dict(
        stem='You are in a meeting and want to politely disagree with a client&rsquo;s suggestion. Which phrase is most appropriate?',
        options=[
            'I have to say that is quite the wrong approach for a project of this kind.',
            'I see where you&rsquo;re coming from &mdash; could we perhaps explore an alternative?',
            'No, I am afraid that will not work. We have already tried it once before.',
            'I disagree with that fairly strongly, but I will do it if you really insist.',
        ],
        correct=1,
        why='<strong>I see where you&rsquo;re coming from</strong> validates before it diverges, and <strong>could we perhaps explore</strong> keeps the decision open. The last option is the trap: agreeing under protest is worse than disagreeing well.',
    ),
    dict(
        stem='A client asks for a discount. You cannot offer one, but you want to keep the relationship positive. What should you say?',
        options=[
            'Our prices are fixed and we do not negotiate them with any of our clients, I am afraid.',
            'I&rsquo;m afraid we can&rsquo;t reduce the price, but I&rsquo;d be happy to discuss what value we can add.',
            'A discount is not really possible &mdash; you may want to look at a cheaper provider instead.',
            'Discounts are not part of our policy here, so there is genuinely nothing I can do for you.',
        ],
        correct=1,
        why='<strong>I&rsquo;m afraid</strong> softens the refusal, and offering added value keeps the conversation alive. The others close it: a policy, a competitor, or a shrug.',
    ),
    dict(
        stem='At the end of a client meeting, which is the best way to confirm the next steps?',
        options=[
            'So I suppose we will talk again at some point &mdash; just let me know what you decide.',
            'We will be in touch with you again fairly soon, once things are a little clearer at our end.',
            'Just to confirm: you send the brief by Friday, we follow up with a proposal by Wednesday.',
            'I think we have covered everything today, so we can probably finish up here for now.',
        ],
        correct=2,
        why='<strong>Just to confirm</strong> plus who does what by when. <em>At some point</em>, <em>fairly soon</em> and <em>covered everything</em> are the three vaguenesses that end meetings with nobody holding anything.',
    ),
]

if __name__ == '__main__':
    import html, re
    for n, q in enumerate(MC, 1):
        L = [len(html.unescape(re.sub(r'<[^>]+>', '', o))) for o in q['options']]
        k = L[q['correct']]
        flag = 'KEY LONGEST' if k == max(L) and L.count(max(L)) == 1 and k - sorted(L)[-2] >= 4 else 'ok'
        print('Q%d key=%d %s %s' % (n, k, L, flag))
