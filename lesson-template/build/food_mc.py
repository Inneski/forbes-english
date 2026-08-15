# -*- coding: utf-8 -*-
"""The six multiple-choice items for Food Ordering A1 Part 2, rebalanced.

Four of the six keys were the longest option on their slide (Q2 32 vs 31,
Q3 35 vs 31, Q5 34 vs 31, Q6 39 vs 35). At A1 that matters more than at B2,
because a beginner who has not yet learned the phrase will fall back on
surface cues, and "pick the longest" is the easiest surface cue there is.

The fix is the house rule: lengthen the distractors, never shorten the key.
Every rewritten wrong option is still wrong for a reason this lesson teaches
— literal translation, wrong register, wrong word order, or a phrase that is
grammatical but not what anyone says in a restaurant.
"""

MC = [
    dict(
        stem='The waiter asks: &ldquo;How would you like your steak?&rdquo; You want it cooked until there is no pink inside. You say:',
        options=[
            'I would like it very cooked, please.',
            'I&rsquo;d like it well done, please.',
            'I would like it completely hot.',
            'Please give me a cooked steak.',
        ],
        correct=1,
        why='<strong>Well done</strong> is the fixed term for a steak with no pink. The three cooking words are <em>rare</em>, <em>medium</em> and <em>well done</em> — nothing else is used, however logical it sounds.',
    ),
    dict(
        stem='You are vegetarian. The waiter describes a dish and you want to check whether there is meat in it. You ask:',
        options=[
            'Is this dish made without any animals?',
            'Did you put any meat inside this food?',
            'Does this dish contain any meat?',
            'I don&rsquo;t really like meat in my dishes.',
        ],
        correct=2,
        why='<strong>Contain</strong> is the verb we use for ingredients. Option D is a statement about your taste, not a question — the waiter cannot answer it, and you still do not know what is in the dish.',
    ),
    dict(
        stem='Your soup arrives cold. You want to tell the waiter politely. You say:',
        options=[
            'This soup is completely cold and terrible!',
            'I do not want to eat this soup any more.',
            'My soup is at a very cold temperature.',
            'Excuse me, I think my soup is cold.',
        ],
        correct=3,
        why='<strong>Excuse me</strong> opens the complaint and <strong>I think</strong> softens it. Both are doing real work: without them the same fact sounds like an accusation.',
    ),
    dict(
        stem='The waiter asks: &ldquo;Would you like still or sparkling water?&rdquo; You want water with bubbles. You say:',
        options=[
            'Sparkling, please.',
            'Bubbly one for me.',
            'Not the still one.',
            'The second, I think.',
        ],
        correct=0,
        why='When someone offers you two things, you answer with the one you want plus <em>please</em>. <em>Bubbly</em> is informal, and answering by pointing at what you do <em>not</em> want makes the waiter do the work.',
    ),
    dict(
        stem='Your friend has just ordered the pasta and you want the same dish. You say:',
        options=[
            'I will also order the pasta, please.',
            'I&rsquo;ll have the same as him, please.',
            'The same pasta that he did order.',
            'Give me the pasta of my friend.',
        ],
        correct=1,
        why='<strong>I&rsquo;ll have&hellip;</strong> is how you order in English — present simple <em>I order</em> sounds like a report rather than a request, and <em>give me</em> is an instruction.',
    ),
    dict(
        stem='You do not know what &ldquo;cr&egrave;me br&ucirc;l&eacute;e&rdquo; is. You ask the waiter:',
        options=[
            'Please translate cr&egrave;me br&ucirc;l&eacute;e for me now.',
            'This word is really very difficult to say.',
            'Could you tell me what cr&egrave;me br&ucirc;l&eacute;e is?',
            'What is the cr&egrave;me br&ucirc;l&eacute;e exactly made of?',
        ],
        correct=2,
        why='<strong>Could you tell me&hellip;</strong> is the polite way in. Note the word order after it: <em>what cr&egrave;me br&ucirc;l&eacute;e is</em>, not <em>what is cr&egrave;me br&ucirc;l&eacute;e</em> — indirect questions use statement order.',
    ),
]

if __name__ == '__main__':
    bad = 0
    for n, q in enumerate(MC, 1):
        L = [len(o) for o in q['options']]
        k = L[q['correct']]
        worst = max(L)
        flag = 'KEY LONGEST' if k == worst and L.count(worst) == 1 else 'ok'
        if flag != 'ok' or k > min(L) * 1.10:
            bad += 1
            flag += ' / ratio %.2f' % (k / min(L))
        print('Q%d key=%d max=%d %s  %s' % (n, k, worst, L, flag))
    print('flagged:', bad)
