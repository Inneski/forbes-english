# -*- coding: utf-8 -*-
"""Content for the two B1 Mixed Grammar Tests — every scored item, in English.

The English here is the thing under test (HOUSE-STYLE §8), so stems, options,
story sentences, chunks and the wrong sentences never translate. What does
translate is keyed: each item names an AREA (the grammar area, which the old
page printed as a badge after answering) and an explanation key, and the text
for both lives in `i18n_mixed_b1.py`.

Defects in the source pages are fixed here, not in the i18n; see the builder's
docstring for the list.
"""

# ── the grammar areas, and the tense colour each one wears (§5a) ─────────────
# A tense area takes its route-map colour; a non-tense area takes none.
TENSE_COLOUR = {
    'presSimple': '#16345C', 'presCont': '#C2185B', 'pastSimple': '#B08968',
    'pastCont': '#FFD400', 'presPerf': '#0F6E56', 'futSimple': '#E8632A',
}


def mc(stem, options, correct, area, hint=''):
    return dict(stem=stem, options=options, correct=options.index(correct),
                area=area, hint=hint)


def tf(correct, area):
    """True/false: the statement and explanation are keyed text."""
    return dict(correct=0 if correct else 1, area=area)


def fix(wrong, area, *answers):
    """Error correction. answers[0] is what the learner is shown if wrong."""
    return dict(wrong=wrong, area=area, answers=list(answers))


# ══════════════════════════════════════════════════════════════════════════
# PART 1
# ══════════════════════════════════════════════════════════════════════════
P1 = dict(
    MC=[
        mc('Listen! Someone ______ at the door.',
           ['knocks', 'is knocking', 'knocked', 'was knocking'],
           'is knocking', 'presCont', 'knock'),
        mc('While I ______ dinner, the phone rang.',
           ['cook', 'was cooking', 'cooks', 'am cooking'],
           'was cooking', 'pastCont', 'cook'),
        mc('She ______ in Madrid since 2019.',
           ['lives', 'lived', 'has lived', 'is living'],
           'has lived', 'presPerf', 'live'),
        mc('I think Brazil ______ the tournament.',
           ['is winning', 'won', 'wins', 'will win'],
           'will win', 'futSimple', 'win'),
        mc('This is ______ film I&rsquo;ve seen this year.',
           ['the goodest', 'the better', 'more good', 'the best'],
           'the best', 'compar', 'good'),
        mc('You ______ wear a seatbelt in this country &mdash; it&rsquo;s the law.',
           ['might', 'could', 'would', 'must'], 'must', 'modals'),
        mc('If it ______ tomorrow, we&rsquo;ll cancel the picnic.',
           ['will rain', 'rained', 'would rain', 'rains'],
           'rains', 'cond', 'rain'),
        mc('If I ______ more free time, I would learn to paint.',
           ['have', 'will have', 'has', 'had'], 'had', 'cond', 'have'),
        mc('This bridge ______ in 1889.',
           ['built', 'has built', 'builds', 'was built'],
           'was built', 'passive', 'build'),
        mc('The woman ______ lives next door is a doctor.',
           ['which', 'whose', 'where', 'who'], 'who', 'relative'),
    ],
    # Elena's day, three slides of two rows. (sentence, [answers], area list)
    STORY=[
        [('Elena usually ______ (get up) at seven o&rsquo;clock, but this morning '
          'she ______ (oversleep) because her alarm didn&rsquo;t ring.',
          ['gets up', 'overslept']),
         ('She ______ (live) in this apartment for almost three years now, and '
          'she loves the quiet street.',
          ['has lived|&rsquo;s lived|has been living|&rsquo;s been living'])],
        [('Last night, while she ______ (read) a book, her neighbour knocked on '
          'the door to borrow some sugar.', ['was reading']),
         ('Tomorrow, Elena ______ (meet) her sister for lunch &mdash; '
          'they&rsquo;ve already booked a table at a new restaurant.',
          ['is meeting|&rsquo;s meeting|is going to meet|&rsquo;s going to meet'])],
        [('If the weather ______ (be) nice this weekend, they ______ (go) to the '
          'coast afterwards.',
          ['is|&rsquo;s', 'will go|&rsquo;ll go|are going to go|&rsquo;re going to go']),
         ('The new restaurant serves ______ (a lot of / much) fresh seafood, so '
          'Elena can&rsquo;t wait to try it.', ['a lot of'])],
    ],
    TF=[tf(False, 'presPerf'), tf(True, 'modals'), tf(False, 'cond'),
        tf(True, 'compar'), tf(True, 'passive'), tf(True, 'relative')],
    ORDER=[
        (['This house', 'was', 'built', 'in 1990.'], 'passive'),
        (['The man', 'who', 'lives next door', 'is', 'friendly.'], 'relative'),
        (['Where', 'did', 'you', 'go', 'yesterday?'], 'questions'),
        (['If I', 'were', 'rich,', 'I&rsquo;d', 'travel the world.'], 'cond'),
        (['This one', 'is', 'much', 'bigger', 'than', 'that one.'], 'compar'),
    ],
    FIX=[
        fix('She has lived here since five years.', 'prep',
            'She has lived here for five years.', 'She has lived here for 5 years.',
            'She&rsquo;s lived here for five years.',
            'She&rsquo;s lived here for 5 years.'),
        fix('If I will have time, I will call you.', 'cond',
            'If I have time, I will call you.', 'If I have time, I&rsquo;ll call you.'),
        fix('This song is more better than the last one.', 'compar',
            'This song is better than the last one.'),
        fix('The letter was wrote by my grandmother.', 'passive',
            'The letter was written by my grandmother.'),
        # Was "I have many money in my wallet" → "much". Wrong the other way:
        # nobody says "I have much money" in a positive sentence, so the page
        # taught a form it then penalised in the story (gap 8, "a lot of").
        # A negative makes MUCH the natural fix.
        fix('I don&rsquo;t have many money in my wallet.', 'quant',
            'I don&rsquo;t have much money in my wallet.',
            'I do not have much money in my wallet.',
            'I don&rsquo;t have a lot of money in my wallet.'),
        fix('The girl which is sitting there is my cousin.', 'relative',
            'The girl who is sitting there is my cousin.',
            'The girl that is sitting there is my cousin.',
            'The girl who&rsquo;s sitting there is my cousin.',
            'The girl sitting there is my cousin.'),
    ],
)

# ══════════════════════════════════════════════════════════════════════════
# PART 2
# ══════════════════════════════════════════════════════════════════════════
P2 = dict(
    MC=[
        mc('Be quiet! The baby ______.',
           ['sleeps', 'slept', 'was sleeping', 'is sleeping'],
           'is sleeping', 'presCont', 'sleep'),
        mc('The lights went out while we ______ a film.',
           ['watch', 'watches', 'are watching', 'were watching'],
           'were watching', 'pastCont', 'watch'),
        mc('They ______ each other for ten years now.',
           ['know', 'knew', 'are knowing', 'have known'],
           'have known', 'presPerf', 'know'),
        mc('I promise I ______ you tomorrow.',
           ['am helping', 'helped', 'help', 'will help'],
           'will help', 'futSimple', 'help'),
        mc('Of all the cities I&rsquo;ve visited, Tokyo is ______.',
           ['busier', 'more busy', 'the most busiest', 'the busiest'],
           'the busiest', 'compar', 'busy'),
        mc('You ______ smoke in here &mdash; it&rsquo;s strictly forbidden.',
           ['might not', 'don&rsquo;t have to', 'wouldn&rsquo;t', 'mustn&rsquo;t'],
           'mustn&rsquo;t', 'modals'),
        mc('If you ______ the instructions, the machine won&rsquo;t break.',
           ['will follow', 'followed', 'would follow', 'follow'],
           'follow', 'cond', 'follow'),
        mc('If she ______ taller, she could join the team.',
           ['is', 'will be', 'has been', 'were'], 'were', 'cond', 'be'),
        mc('The Mona Lisa ______ by Leonardo da Vinci.',
           ['painted', 'paints', 'has painted', 'was painted'],
           'was painted', 'passive', 'paint'),
        mc('The book ______ I&rsquo;m reading is fascinating.',
           ['who', 'where', 'whose', 'which'], 'which', 'relative'),
    ],
    STORY=[
        [('Diego ______ (travel) to Italy every summer, but this year he&rsquo;s '
          'trying something different.', ['travels']),
         ('Last month, he ______ (book) a flight to Lisbon after a friend ______ '
          '(recommend) it.', ['booked', 'recommended|had recommended'])],
        [('He ______ (never / visit) Portugal before, so he&rsquo;s very excited.',
          ['has never visited|&rsquo;s never visited']),
         # Was "he'd forgotten his passport at his parents' house". FORGET does
         # not take a place in standard English; LEAVE does.
         ('Last week, while he ______ (pack) his suitcase, he realised he&rsquo;d '
          'left his passport at his parents&rsquo; house.', ['was packing'])],
        # Was "he's already checked in online" — a week ahead, which no airline
        # allows. Booking a seat is the arrangement that makes the Present
        # Continuous right, and it is true.
        [('Next Friday, Diego ______ (fly) from Madrid to Lisbon &mdash; he&rsquo;s '
          'already chosen his seat.',
          ['is flying|&rsquo;s flying|is going to fly|&rsquo;s going to fly']),
         ('If the flight ______ (be) delayed, he ______ (miss) his hotel check-in '
          'time.',
          ['is|&rsquo;s', 'will miss|&rsquo;ll miss|is going to miss|might miss|'
                          'could miss|may miss'])],
    ],
    TF=[tf(True, 'presCont'), tf(False, 'modals'), tf(True, 'cond'),
        tf(False, 'compar'), tf(True, 'passive'), tf(True, 'relative')],
    ORDER=[
        (['Was', 'this painting', 'painted', 'by', 'a famous artist?'], 'passive'),
        (['The restaurant', 'where', 'we had dinner', 'was', 'excellent.'],
         'relative'),
        (['How long', 'have', 'you', 'lived', 'here?'], 'questions'),
        (['If he', 'had', 'more time,', 'he would', 'exercise every day.'], 'cond'),
        (['The more', 'you practise,', 'the better', 'you become.'], 'compar'),
    ],
    FIX=[
        fix('I am agreeing with you completely.', 'stative',
            'I agree with you completely.', 'I completely agree with you.'),
        fix('She is married with a doctor.', 'prep',
            'She is married to a doctor.', 'She&rsquo;s married to a doctor.'),
        fix('If I would have money, I would buy a house.', 'cond',
            'If I had money, I would buy a house.',
            'If I had money, I&rsquo;d buy a house.',
            'If I had the money, I would buy a house.',
            'If I had the money, I&rsquo;d buy a house.'),
        fix('This exercise is more easy than the last one.', 'compar',
            'This exercise is easier than the last one.'),
        fix('The email was sent for the manager yesterday.', 'passive',
            'The email was sent by the manager yesterday.'),
        # Was "This is the man whose car was stolen it." — an error nobody
        # makes. A doubled possessive after WHOSE is one learners really do
        # make (Spanish "cuyo su", Arabic resumptive pronouns).
        fix('This is the man whose his car was stolen.', 'relative',
            'This is the man whose car was stolen.'),
    ],
)

PARTS = {1: P1, 2: P2}
