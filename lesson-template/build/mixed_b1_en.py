# -*- coding: utf-8 -*-
"""B1 Mixed Grammar Tests — English interface and explanations.

The master copy. Every other `mixed_b1_<lang>.py` must define exactly these
keys; `i18n_mixed_b1.py` refuses to build if one is short or has extras.

Convention (house rule, not in HOUSE-STYLE.md): grammar forms in CAPS, cited
words in double quotes. English examples stay English in every language.
"""

# The grammar areas. Printed in bold at the head of each explanation, which is
# where the old page's after-answer badge was.
AREA = dict(
    presSimple='Present Simple', presCont='Present Continuous',
    pastSimple='Past Simple', pastCont='Past Continuous',
    presPerf='Present Perfect', futSimple='Future with WILL',
    compar='Comparatives &amp; superlatives', modals='Modal verbs',
    cond='Conditionals', passive='The passive', relative='Relative clauses',
    questions='Questions', quant='Quantifiers', prep='Prepositions',
    stative='State verbs',
)

# ── shared by both parts ────────────────────────────────────────────────────
COMMON = dict(
    chipLevel='B1 &middot; Intermediate',
    chipFocus='35 points &middot; five sections',
    chipCount='{N} slides',

    eIntro='Before you start',
    tIntro='One test, ten grammar areas',
    introA='Five sections',
    introAb='10 multiple choice &middot; a story with 8 gaps &middot; 6 true or '
            'false &middot; 5 sentences to build &middot; 6 mistakes to fix.',
    introAn='Every answer is explained as soon as you give it.',
    introB='What it tests',
    introBb='Present, past and perfect tenses, WILL, comparatives, modal verbs, '
            'conditionals, the passive, relative clauses and questions.',
    introBn='Work alone and don&rsquo;t look anything up. Your score is only '
            'useful if it is honest.',

    eMC='Section 1 &middot; Multiple choice',
    tMC='Choose the right form',
    eStory='Section 2 &middot; Reading',
    eTF='Section 3 &middot; True or false',
    tTF='Is this rule true?',
    eOrder='Section 4 &middot; Sentence building',
    tOrder='Put the parts in order',
    hOrder='Click a block to place it, click a placed block to take it back. '
           'One point for the whole sentence.',
    eFix='Section 5 &middot; Error correction',
    tFix='Find the mistake and fix it',
    hFix='One mistake in each sentence. Type the whole sentence again, '
         'corrected.',

    resPerfect='Flawless. B1 grammar is second nature to you &mdash; time to '
               'start on B2.',
    resStrong='Solid. A few gaps to close; the review below shows exactly '
              'which.',
    resMid='Good progress. Read the explanations for the ones you missed, then '
           'try again.',
    resLow='Keep building. Go through the review below slowly and take the '
           'test again tomorrow.',

    actUse='Use at least three',
    actSpeakBrief='In pairs. Use the grammar in brackets.',
    actWriteKind='Writing',
)

# ── Part 1 ──────────────────────────────────────────────────────────────────
P1 = dict(
    coverTitle='Mixed grammar <em>test</em>',
    coverSub='Ten grammar areas, one test: tenses, modals, conditionals, the '
             'passive and more.',
    tStory='Elena&rsquo;s day',
    hSt1='Write the verb in brackets in the correct form. '
         '&ldquo;Oversleep&rdquo; = wake up too late.',
    hSt2='Write the verb in brackets in the correct form. '
         '&ldquo;Borrow&rdquo; = take something and give it back later.',
    hSt3='The last gap needs a quantifier, not a verb: choose one of the two '
         'in brackets.',
    gTournament='&ldquo;Tournament&rdquo; = a sports competition with many '
                'teams.',
    gSeatbelt='&ldquo;Seatbelt&rdquo; = the belt that holds you in a car seat.',

    x_mc1='&ldquo;Listen!&rdquo; means now, so the action is in progress: IS + '
          'knocking. &ldquo;Knocks&rdquo; is a habit; &ldquo;knocked&rdquo; and '
          '&ldquo;was knocking&rdquo; are past.',
    x_mc2='WHILE + WAS / WERE + -ING gives the longer background action; the '
          'Past Simple (&ldquo;rang&rdquo;) interrupts it. The other three are '
          'present forms.',
    x_mc3='SINCE + a point in time (2019) needs HAS / HAVE + past participle. '
          '&ldquo;Lived&rdquo; cannot go with &ldquo;since&rdquo;, and the '
          'present forms cannot either.',
    x_mc4='&ldquo;I think&rdquo; introduces an opinion about the future: WILL '
          '+ verb. &ldquo;Is winning&rdquo; would mean the match is happening '
          'now.',
    x_mc5='Compared with every film this year, so the superlative: THE BEST. '
          '&ldquo;Goodest&rdquo; and &ldquo;more good&rdquo; do not exist; '
          '&ldquo;better&rdquo; compares only two.',
    x_mc6='A law is a strong obligation: MUST + verb. &ldquo;Might&rdquo; and '
          '&ldquo;could&rdquo; are possibility; &ldquo;would&rdquo; is '
          'imaginary.',
    x_mc7='First conditional: IF + Present Simple, then WILL in the other '
          'clause. WILL never goes after IF here.',
    x_mc8='&ldquo;Would learn&rdquo; shows an imaginary situation, so the '
          'second conditional: IF + Past Simple (&ldquo;had&rdquo;).',
    x_mc9='A bridge does not build itself, so the passive: WAS + past '
          'participle. &ldquo;Built&rdquo; alone is active and has no subject '
          'doing it.',
    x_mc10='WHO for people. WHICH is for things, WHOSE for possession, WHERE '
           'for places.',

    x_st1='&ldquo;Usually&rdquo; is a habit: Present Simple, and '
          '&ldquo;she&rdquo; takes -S (&ldquo;gets up&rdquo;). &ldquo;This '
          'morning&rdquo; is finished: Past Simple &ldquo;overslept&rdquo; '
          '(irregular).',
    x_st2='&ldquo;For almost three years now&rdquo; runs up to today: HAS + '
          'lived. HAS BEEN living is also correct.',
    x_st3='WHILE + WAS + -ING for the longer action; the knock '
          '(&ldquo;knocked&rdquo;) interrupts it.',
    x_st4='A table is booked, so it is an arrangement: IS + meeting. IS GOING '
          'TO meet is also correct.',
    x_st5='First conditional. After IF, Present Simple (&ldquo;is&rdquo;), '
          'not WILL; the result takes WILL + go.',
    x_st6='In a positive sentence we say A LOT OF. MUCH is for negatives and '
          'questions: &ldquo;They don&rsquo;t serve much seafood.&rdquo;',

    tf1='We use the Present Perfect with a finished time, like '
        '&ldquo;yesterday&rdquo; or &ldquo;in 2010&rdquo;.',
    tf2='&ldquo;Must&rdquo; and &ldquo;have to&rdquo; both express obligation, '
        'but only &ldquo;have to&rdquo; has a past form: &ldquo;had to&rdquo;.',
    tf3='In the first conditional, we use &ldquo;will&rdquo; after '
        '&ldquo;if&rdquo;.',
    tf4='A superlative usually has &ldquo;the&rdquo; in front of it.',
    tf5='The passive is BE + past participle.',
    tf6='In relative clauses we use &ldquo;who&rdquo; for people and '
        '&ldquo;which&rdquo; for things.',
    x_tf1='False. A finished time takes the Past Simple: &ldquo;I visited '
          'Paris in 2010&rdquo;, not &ldquo;I have visited&rdquo;.',
    x_tf2='True. MUST has no past form of its own, so for the past we use '
          'HAD TO.',
    x_tf3='False. After IF, the Present Simple (&ldquo;If it rains&rdquo;); '
          'WILL goes in the other clause (&ldquo;we&rsquo;ll stay in&rdquo;).',
    x_tf4='True. THE marks one thing as the only one in its group: THE best, '
          'THE tallest, THE most expensive.',
    x_tf5='True. &ldquo;Is built&rdquo;, &ldquo;was written&rdquo;, '
          '&ldquo;has been finished&rdquo;: always a form of BE + past '
          'participle.',
    x_tf6='True. THAT can replace either in everyday English, but WHO is only '
          'for people and WHICH only for things.',

    x_or1='The passive: subject + WAS + past participle, then the time.',
    x_or2='&ldquo;Who lives next door&rdquo; comes straight after &ldquo;the '
          'man&rdquo; and tells us which man. Then the main verb, IS.',
    x_or3='Question word + DID + subject + base verb. After DID the verb has '
          'no -ED: &ldquo;go&rdquo;, not &ldquo;went&rdquo;.',
    x_or4='Second conditional: IF + Past Simple (&ldquo;were&rdquo;), then '
          'WOULD (&rsquo;D) + verb.',
    x_or5='MUCH goes in front of a comparative to make it stronger; THAN '
          'introduces the second thing.',

    x_fx1='FOR + a length of time (five years). SINCE + a starting point '
          '(2019, March).',
    x_fx2='After IF in a first conditional, the Present Simple: &ldquo;If I '
          'have time&rdquo;. WILL stays in the other clause.',
    x_fx3='&ldquo;Better&rdquo; is already a comparative. MORE + BETTER is '
          'never correct.',
    x_fx4='The passive needs the past participle: write &rarr; wrote &rarr; '
          'WRITTEN.',
    x_fx5='&ldquo;Money&rdquo; is uncountable: MUCH, not MANY. MANY is for '
          'plural nouns: &ldquo;many coins&rdquo;.',
    x_fx6='WHICH is for things. For a person, WHO (or THAT).',

    actTitle='Now use it',
    actSpeak1='Your usual morning, then what went differently this morning. '
              '(Present Simple, Past Simple)',
    actSpeak2='What would you do with a whole year free? Ask your partner too. '
              '(second conditional)',
    actSpeak3='A famous building in your city: when was it built, and who by? '
              '(the passive)',
    actWriteBrief='An email, 120&ndash;150 words, to a friend visiting next '
                  'week: your plans, what they must bring, and what you&rsquo;ll '
                  'do if it rains.',
    actPlaceholder='Hi! I can&rsquo;t wait to see you next week&hellip;',
)

# ── Part 2 ──────────────────────────────────────────────────────────────────
P2 = dict(
    coverTitle='Mixed grammar test <em>part 2</em>',
    coverSub='Ten more grammar points, all new sentences: tenses, modals, '
             'conditionals, the passive and more.',
    tStory='Diego&rsquo;s trip',
    hSt1='Write the verb in brackets in the correct form.',
    hSt2='Write the verb in brackets in the correct form. '
         '&ldquo;Suitcase&rdquo; = the bag you pack for a trip.',
    hSt3='Write the verb in brackets in the correct form. '
         '&ldquo;Delayed&rdquo; = later than planned.',
    gForbidden='&ldquo;Forbidden&rdquo; = not allowed by a rule.',

    x_mc1='&ldquo;Be quiet!&rdquo; means now, so the action is in progress: '
          'IS + sleeping. &ldquo;Sleeps&rdquo; is a habit; the other two are '
          'past.',
    x_mc2='WHILE + WERE + -ING gives the background action that the lights '
          '(&ldquo;went out&rdquo;) interrupted. The others are present forms.',
    x_mc3='&ldquo;For ten years now&rdquo; runs up to today: HAVE + known. '
          '&ldquo;Are knowing&rdquo; is wrong because KNOW is not an action in '
          'progress; &ldquo;knew&rdquo; says it has ended.',
    x_mc4='A promise is a decision made as you speak: WILL + verb. '
          '&ldquo;Am helping&rdquo; would need an arrangement already made.',
    x_mc5='Compared with every city, so the superlative: THE + busiEST. '
          '&ldquo;Busier&rdquo; compares two; &ldquo;most busiest&rdquo; says it '
          'twice.',
    x_mc6='&ldquo;Forbidden&rdquo; is a rule against it: MUSTN&rsquo;T. '
          '&ldquo;Don&rsquo;t have to&rdquo; means it is not necessary, which '
          'is almost the opposite.',
    x_mc7='First conditional: IF + Present Simple, then WON&rsquo;T / WILL in '
          'the other clause.',
    x_mc8='&ldquo;Could join&rdquo; shows an imaginary situation: IF + Past '
          'Simple, and with BE we use WERE for every person.',
    x_mc9='The painting did not paint itself, so the passive: WAS + past '
          'participle, and BY names the painter.',
    x_mc10='WHICH (or THAT) for things. WHO is for people, WHOSE for '
           'possession, WHERE for places.',

    x_st1='&ldquo;Every summer&rdquo; is a habit: Present Simple, and '
          '&ldquo;he&rdquo; takes -S.',
    x_st2='&ldquo;Last month&rdquo; is finished: Past Simple &ldquo;booked&rdquo;. '
          'The friend recommended it first; &ldquo;recommended&rdquo; and '
          '&ldquo;had recommended&rdquo; are both correct.',
    x_st3='&ldquo;Never &hellip; before&rdquo; is his life up to now: HAS + '
          'NEVER + visited.',
    x_st4='WHILE + WAS + -ING for the longer action; the moment he realised '
          'interrupts it.',
    x_st5='A seat is chosen, so it is an arrangement: IS + flying. IS GOING '
          'TO fly is also correct.',
    x_st6='First conditional. After IF, Present Simple (&ldquo;is&rdquo;); '
          'the result takes WILL + miss. MIGHT miss is also correct.',

    tf1='The Present Continuous can describe a future arrangement, like '
        '&ldquo;I&rsquo;m flying to Rome on Monday.&rdquo;',
    tf2='&ldquo;Mustn&rsquo;t&rdquo; and &ldquo;don&rsquo;t have to&rdquo; mean '
        'the same thing.',
    tf3='In the second conditional we often use &ldquo;were&rdquo; instead of '
        '&ldquo;was&rdquo; after I, he, she and it.',
    tf4='Two-syllable adjectives always take &ldquo;more&rdquo;, never '
        '&ldquo;-er&rdquo;.',
    tf5='The passive of &ldquo;People speak English here&rdquo; is '
        '&ldquo;English is spoken here.&rdquo;',
    tf6='&ldquo;Whose&rdquo; is used to talk about possession.',
    x_tf1='True. When the plan is fixed (a ticket, a time), the Present '
          'Continuous is the natural choice.',
    x_tf2='False. MUSTN&rsquo;T means it is not allowed. DON&rsquo;T HAVE TO '
          'means it is not necessary. They are nearly opposites.',
    x_tf3='True. &ldquo;If I were you&rdquo;, &ldquo;If he were taller&rdquo;. '
          '&ldquo;Was&rdquo; is common in speech, but WERE is the standard '
          'form.',
    x_tf4='False. Many take -ER: happy &rarr; happier, easy &rarr; easier, '
          'narrow &rarr; narrower.',
    x_tf5='True. The object (&ldquo;English&rdquo;) becomes the subject, and '
          'the verb becomes IS + past participle.',
    x_tf6='True. &ldquo;Whose car is this?&rdquo; &middot; &ldquo;the man '
          'whose car was stolen&rdquo;.',

    x_or1='A passive question: WAS + subject + past participle, then BY + '
          'who did it.',
    x_or2='WHERE introduces a clause about a place: &ldquo;where we had '
          'dinner&rdquo; tells us which restaurant.',
    x_or3='HOW LONG + HAVE + subject + past participle: the Present Perfect '
          'question.',
    x_or4='Second conditional: IF + Past Simple (&ldquo;had&rdquo;), then '
          'WOULD + verb.',
    x_or5='THE + comparative, THE + comparative: two things that change '
          'together.',

    x_fx1='AGREE is an opinion, not an action in progress, so the Present '
          'Simple: &ldquo;I agree&rdquo;.',
    x_fx2='MARRIED TO someone, not &ldquo;married with&rdquo;.',
    x_fx3='After IF in a second conditional, the Past Simple: &ldquo;If I '
          'had&rdquo;. WOULD stays in the other clause.',
    x_fx4='&ldquo;Easy&rdquo; ends in -Y, so it takes -IER: EASIER, not '
          '&ldquo;more easy&rdquo;.',
    x_fx5='In the passive, BY names who did it: &ldquo;sent by the '
          'manager&rdquo;. FOR means the person receiving it.',
    x_fx6='WHOSE already means &ldquo;his&rdquo;, so &ldquo;his&rdquo; is '
          'said twice. Delete it.',

    actTitle='Now use it',
    actSpeak1='Your plans for Saturday, and what you&rsquo;ll do if it rains. '
              '(Present Continuous, first conditional)',
    actSpeak2='At work or school: three things you mustn&rsquo;t do, three you '
              'don&rsquo;t have to. (modal verbs)',
    actSpeak3='A trip that went wrong: what were you doing when it happened? '
              '(Past Continuous)',
    actWriteBrief='A review, 120&ndash;150 words, of a place you have visited. '
                  'Say how long you have known it, what it is famous for, and '
                  'why it is the best (or worst) of its kind.',
    actPlaceholder='I have been to &hellip; three times, and &hellip;',
)
