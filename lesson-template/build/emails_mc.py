# -*- coding: utf-8 -*-
"""The five multiple-choice items, with the distractors rebalanced.

Every one of these keys was the longest option on its slide — all five — so a
learner could have scored full marks by always picking the longest and learning
nothing about register. That is the single defect the house style calls out by
name, and it is exactly the trap a lesson about professional email walks into,
because the professional version genuinely is the more elaborate one.

The fix is the one the house style prescribes: lengthen the distractors, never
shorten the key. Each wrong option is now the same length as the right one and
wrong for a reason this lesson teaches — too casual, too blunt, too apologetic,
too defensive, or missing the commitment that makes the closing useful.
"""

MC = [
    dict(
        stem='You want to open a professional email to a client you have not been in contact with for two months. Which opening is most appropriate?',
        options=[
            'Hi there — I wanted to get in touch because it has been a while now, and I thought I would see how you are getting on.',
            'I hope this email finds you well. I am writing to follow up on our previous conversation regarding the proposal.',
            'Just checking in to see what is happening on your side with the project, and whether anything has moved along since we spoke.',
            'Sorry for the long silence — things have been extremely busy at our end, but I did want to reach out and pick this back up.',
        ],
        correct=1,
        why='<strong>I hope this email finds you well</strong> is the standard opener after a gap, and stating the purpose immediately — <em>I am writing to follow up</em> — is the B2 structure. The others are too casual, too vague, or open by apologising for something the client has probably not noticed.',
    ),
    dict(
        stem='You are on a call and you cannot hear the client clearly. What is the most professional way to handle this?',
        options=[
            'Sorry, can you say that again? The line is really bad at my end and I keep losing you.',
            'I apologise — I am having some difficulty hearing you. Could you repeat that, please?',
            'I missed what you said — there seems to be a problem with the connection somewhere.',
            'Wait a moment — the sound is cutting out on my end and I cannot follow what you are saying.',
        ],
        correct=1,
        why='A brief apology before the explanation is the professional order, and <em>Could you repeat that, please?</em> is the polite request form. The others either open with a bald <em>sorry</em>, or describe the problem without ever asking for anything.',
    ),
    dict(
        stem='You sent a proposal three days ago and have not heard back. Which follow-up email opening is most appropriate?',
        options=[
            'I wanted to check whether you have had a chance to review the proposal I sent on Monday.',
            'I sent the proposal three days ago and am still waiting to hear back from you about it.',
            'Just a quick note to say I have not heard anything back and am wondering where things stand.',
            'Did you receive the proposal? Please let me know what you think as soon as you possibly can.',
        ],
        correct=0,
        why='<strong>Whether you have had a chance to</strong> is the polite formula: it offers the other person a reason for the silence. The others count the days, admit you are waiting, or issue an instruction — all of which put the client on the back foot.',
    ),
    dict(
        stem='You need to end a call professionally and confirm the action points. Which closing is best?',
        options=[
            'Right, I think that covers everything for today. I will send you a summary at some point and we can take it from there.',
            'OK so we are agreed — I will send a recap of today&rsquo;s actions by end of day and look forward to your confirmation.',
            'I think we are done here for now. I will be in touch again as soon as something comes up at our end that you should know.',
            'Let me know if there is anything else you need, and otherwise I will talk to you again in the next week or so.',
        ],
        correct=1,
        why='The right closing does three things: it summarises the agreement, it commits to a next action <em>with a deadline</em>, and it invites confirmation. The others end the call politely but leave nobody holding anything — <em>at some point</em> and <em>in the next week or so</em> are not commitments.',
    ),
    dict(
        stem='A client emails to say they are not satisfied with a report you submitted. What is the most effective opening to your reply?',
        options=[
            'Thank you for your feedback. I am sorry to hear the report did not fully meet your expectations.',
            'I understand that you are not happy with the report, which is genuinely disappointing to hear.',
            'I am rather surprised by your feedback, as we followed the brief we agreed on very closely.',
            'We worked extremely hard on this report and I would like to understand more about your concerns.',
        ],
        correct=0,
        why='Thanking someone for criticism signals professionalism before you have conceded anything, and <em>did not fully meet your expectations</em> is measured rather than self-flagellating. The others open on the client&rsquo;s unhappiness, or defend the work — both of which set the wrong tone in the first line.',
    ),
]

if __name__ == '__main__':
    for n, q in enumerate(MC, 1):
        L = [len(o) for o in q['options']]
        k = L[q['correct']]
        worst = max(L)
        flag = 'KEY LONGEST' if k == worst and L.count(worst) == 1 else 'ok'
        print('Q%d key=%d max=%d ratio=%.2f  %s  %s' % (n, k, worst, k / min(L), L, flag))
