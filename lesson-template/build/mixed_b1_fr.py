# -*- coding: utf-8 -*-
"""B1 Mixed Grammar Tests — French. Same keys as mixed_b1_en.py.

Tense names stay in English; the other area names translate. English
examples stay English, in « » quotes with French spacing.
"""

AREA = dict(
    presSimple='Present Simple', presCont='Present Continuous',
    pastSimple='Past Simple', pastCont='Past Continuous',
    presPerf='Present Perfect', futSimple='Futur avec WILL',
    compar='Comparatifs et superlatifs', modals='Verbes modaux',
    cond='Conditionnelles', passive='Le passif', relative='Propositions relatives',
    questions='Questions', quant='Quantificateurs', prep='Prépositions',
    stative='Verbes d&rsquo;état',
)

COMMON = dict(
    chipLevel='B1 &middot; Intermédiaire',
    chipFocus='35 points &middot; cinq parties',
    chipCount='{N} diapositives',

    eIntro='Avant de commencer',
    tIntro='Un test, dix points de grammaire',
    introA='Cinq parties',
    introAb='10 QCM &middot; une histoire à 8 trous &middot; 6 vrai ou faux '
            '&middot; 5 phrases à construire &middot; 6 fautes à corriger.',
    introAn='Chaque réponse est expliquée dès que tu la donnes.',
    introB='Ce qui est testé',
    introBb='Les temps du présent, du passé et le perfect, WILL, les '
            'comparatifs, les modaux, les conditionnelles, le passif, les '
            'relatives et les questions.',
    introBn='Travaille seul et ne cherche rien. Ton score n&rsquo;est utile '
            'que s&rsquo;il est honnête.',

    eMC='Partie 1 &middot; QCM',
    tMC='Choisis la bonne forme',
    eStory='Partie 2 &middot; Lecture',
    eTF='Partie 3 &middot; Vrai ou faux',
    tTF='Cette règle est-elle vraie ?',
    eOrder='Partie 4 &middot; Construire des phrases',
    tOrder='Remets les morceaux dans l&rsquo;ordre',
    hOrder='Clique sur un bloc pour le placer, sur un bloc placé pour le '
           'retirer. Un point pour la phrase entière.',
    eFix='Partie 5 &middot; Correction d&rsquo;erreurs',
    tFix='Trouve l&rsquo;erreur et corrige-la',
    hFix='Une erreur par phrase. Réécris toute la phrase, corrigée.',

    resPerfect='Sans faute. La grammaire B1 est naturelle pour toi &mdash; '
               'place au B2.',
    resStrong='Solide. Quelques lacunes à combler ; la liste ci-dessous dit '
              'exactement lesquelles.',
    resMid='Bons progrès. Relis les explications de tes erreurs, puis '
           'recommence.',
    resLow='Continue. Reprends lentement la liste ci-dessous et refais le test '
           'demain.',

    actUse='Utilise-en au moins trois',
    actSpeakBrief='À deux. Utilise la grammaire entre parenthèses.',
    actWriteKind='Écriture',
)

P1 = dict(
    coverTitle='Test de grammaire <em>mixte</em>',
    coverSub='Dix points de grammaire, un test : les temps, les modaux, les '
             'conditionnelles, le passif et plus.',
    tStory='La journée d&rsquo;Elena',
    hSt1='Mets le verbe entre parenthèses à la bonne forme. '
         '&laquo;&nbsp;Oversleep&nbsp;&raquo; = se réveiller trop tard.',
    hSt2='Mets le verbe entre parenthèses à la bonne forme. '
         '&laquo;&nbsp;Borrow&nbsp;&raquo; = emprunter.',
    hSt3='Le dernier trou demande un quantificateur, pas un verbe : choisis '
         'l&rsquo;un des deux entre parenthèses.',
    gTournament='&laquo;&nbsp;Tournament&nbsp;&raquo; = tournoi.',
    gSeatbelt='&laquo;&nbsp;Seatbelt&nbsp;&raquo; = ceinture de sécurité.',

    x_mc1='&laquo;&nbsp;Listen!&nbsp;&raquo; veut dire maintenant : '
          'l&rsquo;action est en cours, IS + knocking. '
          '&laquo;&nbsp;Knocks&nbsp;&raquo; est une habitude ; '
          '&laquo;&nbsp;knocked&nbsp;&raquo; et &laquo;&nbsp;was '
          'knocking&nbsp;&raquo; sont au passé.',
    x_mc2='WHILE + WAS / WERE + -ING donne l&rsquo;action de fond, plus '
          'longue ; le Past Simple (&laquo;&nbsp;rang&nbsp;&raquo;) '
          'l&rsquo;interrompt. Les trois autres sont au présent.',
    x_mc3='SINCE + un moment (2019) demande HAS / HAVE + participe passé. '
          '&laquo;&nbsp;Lived&nbsp;&raquo; ne va pas avec '
          '&laquo;&nbsp;since&nbsp;&raquo;, les formes du présent non plus.',
    x_mc4='&laquo;&nbsp;I think&nbsp;&raquo; introduit une opinion sur '
          'l&rsquo;avenir : WILL + verbe. &laquo;&nbsp;Is winning&nbsp;&raquo; '
          'voudrait dire que le match se joue maintenant.',
    x_mc5='Comparé à tous les films de l&rsquo;année, donc le superlatif : THE '
          'BEST. &laquo;&nbsp;Goodest&nbsp;&raquo; et &laquo;&nbsp;more '
          'good&nbsp;&raquo; n&rsquo;existent pas ; '
          '&laquo;&nbsp;better&nbsp;&raquo; compare seulement deux choses.',
    x_mc6='Une loi est une obligation forte : MUST + verbe. '
          '&laquo;&nbsp;Might&nbsp;&raquo; et &laquo;&nbsp;could&nbsp;&raquo; '
          'expriment une possibilité ; &laquo;&nbsp;would&nbsp;&raquo; est '
          'hypothétique.',
    x_mc7='Conditionnelle de type 1 : IF + Present Simple, puis WILL dans '
          'l&rsquo;autre partie. Ici, WILL ne vient jamais après IF.',
    x_mc8='&laquo;&nbsp;Would learn&nbsp;&raquo; montre une situation '
          'imaginaire, donc type 2 : IF + Past Simple '
          '(&laquo;&nbsp;had&nbsp;&raquo;).',
    x_mc9='Un pont ne se construit pas tout seul, donc le passif : WAS + '
          'participe passé. &laquo;&nbsp;Built&nbsp;&raquo; seul est actif, '
          'sans personne pour faire l&rsquo;action.',
    x_mc10='WHO pour les personnes. WHICH pour les choses, WHOSE pour la '
           'possession, WHERE pour les lieux.',

    x_st1='&laquo;&nbsp;Usually&nbsp;&raquo; = habitude : Present Simple, '
          'avec -S après &laquo;&nbsp;she&nbsp;&raquo;. &laquo;&nbsp;This '
          'morning&nbsp;&raquo; est fini : Past Simple '
          '&laquo;&nbsp;overslept&nbsp;&raquo; (irrégulier).',
    x_st2='&laquo;&nbsp;For almost three years now&nbsp;&raquo; va '
          'jusqu&rsquo;à aujourd&rsquo;hui : HAS + lived. HAS BEEN living '
          'aussi.',
    x_st3='WHILE + WAS + -ING pour l&rsquo;action la plus longue ; le coup à '
          'la porte (&laquo;&nbsp;knocked&nbsp;&raquo;) l&rsquo;interrompt.',
    x_st4='La table est réservée, c&rsquo;est donc un rendez-vous fixé : IS + '
          'meeting. IS GOING TO meet est aussi correct.',
    x_st5='Conditionnelle de type 1. Après IF, Present Simple '
          '(&laquo;&nbsp;is&nbsp;&raquo;), pas WILL ; la conséquence prend '
          'WILL + go.',
    x_st6='Dans une phrase affirmative, on dit A LOT OF. MUCH sert dans les '
          'négations et les questions : &laquo;&nbsp;They don&rsquo;t serve '
          'much seafood.&nbsp;&raquo;',

    tf1='On utilise le Present Perfect avec un moment terminé, comme '
        '&laquo;&nbsp;yesterday&nbsp;&raquo; ou &laquo;&nbsp;in '
        '2010&nbsp;&raquo;.',
    tf2='&laquo;&nbsp;Must&nbsp;&raquo; et &laquo;&nbsp;have to&nbsp;&raquo; '
        'expriment tous deux l&rsquo;obligation, mais seul '
        '&laquo;&nbsp;have to&nbsp;&raquo; a une forme au passé : '
        '&laquo;&nbsp;had to&nbsp;&raquo;.',
    tf3='Dans la conditionnelle de type 1, on met &laquo;&nbsp;will&nbsp;&raquo; '
        'après &laquo;&nbsp;if&nbsp;&raquo;.',
    tf4='Un superlatif est en général précédé de &laquo;&nbsp;the&nbsp;&raquo;.',
    tf5='Le passif, c&rsquo;est BE + participe passé.',
    tf6='Dans les relatives, on utilise &laquo;&nbsp;who&nbsp;&raquo; pour les '
        'personnes et &laquo;&nbsp;which&nbsp;&raquo; pour les choses.',
    x_tf1='Faux. Un moment terminé demande le Past Simple : &laquo;&nbsp;I '
          'visited Paris in 2010&nbsp;&raquo;, pas &laquo;&nbsp;I have '
          'visited&nbsp;&raquo;.',
    x_tf2='Vrai. MUST n&rsquo;a pas de passé à lui, donc pour le passé on '
          'utilise HAD TO.',
    x_tf3='Faux. Après IF, le Present Simple (&laquo;&nbsp;If it '
          'rains&nbsp;&raquo;) ; WILL va dans l&rsquo;autre partie '
          '(&laquo;&nbsp;we&rsquo;ll stay in&nbsp;&raquo;).',
    x_tf4='Vrai. THE désigne une chose comme la seule de son groupe : THE '
          'best, THE tallest, THE most expensive.',
    x_tf5='Vrai. &laquo;&nbsp;Is built&nbsp;&raquo;, &laquo;&nbsp;was '
          'written&nbsp;&raquo;, &laquo;&nbsp;has been finished&nbsp;&raquo; : '
          'toujours une forme de BE + participe passé.',
    x_tf6='Vrai. À l&rsquo;oral, THAT peut remplacer les deux, mais WHO est '
          'réservé aux personnes et WHICH aux choses.',

    x_or1='Le passif : sujet + WAS + participe passé, puis le moment.',
    x_or2='&laquo;&nbsp;Who lives next door&nbsp;&raquo; vient juste après '
          '&laquo;&nbsp;the man&nbsp;&raquo; et dit de quel homme il '
          's&rsquo;agit. Puis le verbe principal, IS.',
    x_or3='Mot interrogatif + DID + sujet + base verbale. Après DID, le verbe '
          'ne prend pas -ED : &laquo;&nbsp;go&nbsp;&raquo;, pas '
          '&laquo;&nbsp;went&nbsp;&raquo;.',
    x_or4='Type 2 : IF + Past Simple (&laquo;&nbsp;were&nbsp;&raquo;), puis '
          'WOULD (&rsquo;D) + verbe.',
    x_or5='MUCH devant un comparatif le renforce ; THAN introduit le second '
          'élément.',

    x_fx1='FOR + une durée (five years). SINCE + un point de départ (2019, '
          'March).',
    x_fx2='Après IF dans une conditionnelle de type 1, le Present Simple : '
          '&laquo;&nbsp;If I have time&nbsp;&raquo;. WILL reste dans '
          'l&rsquo;autre partie.',
    x_fx3='&laquo;&nbsp;Better&nbsp;&raquo; est déjà un comparatif. MORE + '
          'BETTER n&rsquo;est jamais correct.',
    x_fx4='Le passif demande le participe passé : write &rarr; wrote &rarr; '
          'WRITTEN.',
    x_fx5='&laquo;&nbsp;Money&nbsp;&raquo; est indénombrable : MUCH, pas MANY. '
          'MANY va avec les noms au pluriel : &laquo;&nbsp;many '
          'coins&nbsp;&raquo;.',
    x_fx6='WHICH est pour les choses. Pour une personne, WHO (ou THAT).',

    actTitle='À toi maintenant',
    actSpeak1='Ton matin habituel, puis ce qui a été différent ce matin. '
              '(Present Simple, Past Simple)',
    actSpeak2='Que ferais-tu d&rsquo;une année entière de libre ? Demande '
              'aussi à ton partenaire. (type 2)',
    actSpeak3='Un bâtiment célèbre de ta ville : quand et par qui a-t-il été '
              'construit ? (le passif)',
    actWriteBrief='Un e-mail de 120 à 150 mots à un ami qui vient la semaine '
                  'prochaine : tes projets, ce qu&rsquo;il doit apporter et ce '
                  'que vous ferez s&rsquo;il pleut.',
    actPlaceholder='Hi! I can&rsquo;t wait to see you next week&hellip;',
)

P2 = dict(
    coverTitle='Test de grammaire mixte <em>partie 2</em>',
    coverSub='Dix autres points de grammaire, que des phrases nouvelles : les '
             'temps, les modaux, les conditionnelles, le passif et plus.',
    tStory='Le voyage de Diego',
    hSt1='Mets le verbe entre parenthèses à la bonne forme.',
    hSt2='Mets le verbe entre parenthèses à la bonne forme. '
         '&laquo;&nbsp;Suitcase&nbsp;&raquo; = valise.',
    hSt3='Mets le verbe entre parenthèses à la bonne forme. '
         '&laquo;&nbsp;Delayed&nbsp;&raquo; = retardé.',
    gForbidden='&laquo;&nbsp;Forbidden&nbsp;&raquo; = interdit.',

    x_mc1='&laquo;&nbsp;Be quiet!&nbsp;&raquo; veut dire maintenant : '
          'l&rsquo;action est en cours, IS + sleeping. '
          '&laquo;&nbsp;Sleeps&nbsp;&raquo; est une habitude ; les deux autres '
          'sont au passé.',
    x_mc2='WHILE + WERE + -ING donne l&rsquo;action de fond que la coupure '
          '(&laquo;&nbsp;went out&nbsp;&raquo;) a interrompue. Les autres sont '
          'au présent.',
    x_mc3='&laquo;&nbsp;For ten years now&nbsp;&raquo; va jusqu&rsquo;à '
          'aujourd&rsquo;hui : HAVE + known. &laquo;&nbsp;Are '
          'knowing&nbsp;&raquo; est faux, car KNOW n&rsquo;est pas une action '
          'en cours ; &laquo;&nbsp;knew&nbsp;&raquo; dit que c&rsquo;est fini.',
    x_mc4='Une promesse est une décision prise en parlant : WILL + verbe. '
          '&laquo;&nbsp;Am helping&nbsp;&raquo; supposerait un rendez-vous déjà '
          'fixé.',
    x_mc5='Comparé à toutes les villes, donc le superlatif : THE + busiEST. '
          '&laquo;&nbsp;Busier&nbsp;&raquo; compare deux choses ; '
          '&laquo;&nbsp;most busiest&nbsp;&raquo; le dit deux fois.',
    x_mc6='&laquo;&nbsp;Forbidden&nbsp;&raquo; est une interdiction : '
          'MUSTN&rsquo;T. &laquo;&nbsp;Don&rsquo;t have to&nbsp;&raquo; veut '
          'dire que ce n&rsquo;est pas nécessaire, presque le contraire.',
    x_mc7='Type 1 : IF + Present Simple, puis WON&rsquo;T / WILL dans '
          'l&rsquo;autre partie.',
    x_mc8='&laquo;&nbsp;Could join&nbsp;&raquo; montre une situation '
          'imaginaire : IF + Past Simple, et avec BE on utilise WERE à toutes '
          'les personnes.',
    x_mc9='Le tableau ne s&rsquo;est pas peint tout seul, donc le passif : WAS '
          '+ participe passé, et BY nomme le peintre.',
    x_mc10='WHICH (ou THAT) pour les choses. WHO pour les personnes, WHOSE '
           'pour la possession, WHERE pour les lieux.',

    x_st1='&laquo;&nbsp;Every summer&nbsp;&raquo; est une habitude : Present '
          'Simple, et &laquo;&nbsp;he&nbsp;&raquo; prend un -S.',
    x_st2='&laquo;&nbsp;Last month&nbsp;&raquo; est terminé : Past Simple '
          '&laquo;&nbsp;booked&nbsp;&raquo;. L&rsquo;ami l&rsquo;a recommandé '
          'avant ; &laquo;&nbsp;recommended&nbsp;&raquo; et &laquo;&nbsp;had '
          'recommended&nbsp;&raquo; sont tous deux corrects.',
    x_st3='&laquo;&nbsp;Never &hellip; before&nbsp;&raquo;, c&rsquo;est sa vie '
          'jusqu&rsquo;à maintenant : HAS + NEVER + visited.',
    x_st4='WHILE + WAS + -ING pour l&rsquo;action la plus longue ; le moment '
          'où il s&rsquo;en rend compte l&rsquo;interrompt.',
    x_st5='Le siège est choisi, c&rsquo;est donc prévu : IS + flying. IS GOING '
          'TO fly est aussi correct.',
    x_st6='Type 1. Après IF, Present Simple (&laquo;&nbsp;is&nbsp;&raquo;) ; '
          'la conséquence prend WILL + miss. MIGHT miss est aussi correct.',

    tf1='Le Present Continuous peut exprimer un projet déjà fixé, comme '
        '&laquo;&nbsp;I&rsquo;m flying to Rome on Monday.&nbsp;&raquo;',
    tf2='&laquo;&nbsp;Mustn&rsquo;t&nbsp;&raquo; et &laquo;&nbsp;don&rsquo;t '
        'have to&nbsp;&raquo; veulent dire la même chose.',
    tf3='Dans la conditionnelle de type 2, on utilise souvent '
        '&laquo;&nbsp;were&nbsp;&raquo; au lieu de &laquo;&nbsp;was&nbsp;&raquo; '
        'avec I, he, she et it.',
    tf4='Les adjectifs de deux syllabes prennent toujours '
        '&laquo;&nbsp;more&nbsp;&raquo;, jamais &laquo;&nbsp;-er&nbsp;&raquo;.',
    tf5='Le passif de &laquo;&nbsp;People speak English here&nbsp;&raquo; est '
        '&laquo;&nbsp;English is spoken here.&nbsp;&raquo;',
    tf6='&laquo;&nbsp;Whose&nbsp;&raquo; sert à parler de la possession.',
    x_tf1='Vrai. Quand le projet est fixé (un billet, une heure), le Present '
          'Continuous est le choix naturel.',
    x_tf2='Faux. MUSTN&rsquo;T veut dire que c&rsquo;est interdit. DON&rsquo;T '
          'HAVE TO veut dire que ce n&rsquo;est pas nécessaire. Ils sont presque '
          'contraires.',
    x_tf3='Vrai. &laquo;&nbsp;If I were you&nbsp;&raquo;, &laquo;&nbsp;If he '
          'were taller&nbsp;&raquo;. &laquo;&nbsp;Was&nbsp;&raquo; est courant '
          'à l&rsquo;oral, mais WERE est la forme standard.',
    x_tf4='Faux. Beaucoup prennent -ER : happy &rarr; happier, easy &rarr; '
          'easier, narrow &rarr; narrower.',
    x_tf5='Vrai. Le complément (&laquo;&nbsp;English&nbsp;&raquo;) devient le '
          'sujet, et le verbe devient IS + participe passé.',
    x_tf6='Vrai. &laquo;&nbsp;Whose car is this?&nbsp;&raquo; &middot; '
          '&laquo;&nbsp;the man whose car was stolen&nbsp;&raquo;.',

    x_or1='Une question au passif : WAS + sujet + participe passé, puis BY + '
          'qui l&rsquo;a fait.',
    x_or2='WHERE introduit une proposition sur un lieu : &laquo;&nbsp;where we '
          'had dinner&nbsp;&raquo; dit de quel restaurant il s&rsquo;agit.',
    x_or3='HOW LONG + HAVE + sujet + participe passé : la question au Present '
          'Perfect.',
    x_or4='Type 2 : IF + Past Simple (&laquo;&nbsp;had&nbsp;&raquo;), puis '
          'WOULD + verbe.',
    x_or5='THE + comparatif, THE + comparatif : deux choses qui changent '
          'ensemble.',

    x_fx1='AGREE est une opinion, pas une action en cours, donc le Present '
          'Simple : &laquo;&nbsp;I agree&nbsp;&raquo;.',
    x_fx2='MARRIED TO someone, pas &laquo;&nbsp;married with&nbsp;&raquo;.',
    x_fx3='Après IF dans une conditionnelle de type 2, le Past Simple : '
          '&laquo;&nbsp;If I had&nbsp;&raquo;. WOULD reste dans l&rsquo;autre '
          'partie.',
    x_fx4='&laquo;&nbsp;Easy&nbsp;&raquo; finit par -Y, donc -IER : EASIER, '
          'pas &laquo;&nbsp;more easy&nbsp;&raquo;.',
    x_fx5='Au passif, BY nomme celui qui fait l&rsquo;action : '
          '&laquo;&nbsp;sent by the manager&nbsp;&raquo;. FOR désignerait le '
          'destinataire.',
    x_fx6='WHOSE veut déjà dire &laquo;&nbsp;his&nbsp;&raquo;, donc '
          '&laquo;&nbsp;his&nbsp;&raquo; est en trop. Supprime-le.',

    actTitle='À toi maintenant',
    actSpeak1='Tes projets pour samedi, et ce que tu feras s&rsquo;il pleut. '
              '(Present Continuous, type 1)',
    actSpeak2='Au travail ou à l&rsquo;école : trois choses interdites, trois '
              'choses pas obligatoires. (modaux)',
    actSpeak3='Un voyage qui a mal tourné : que faisais-tu quand c&rsquo;est '
              'arrivé ? (Past Continuous)',
    actWriteBrief='Un avis de 120 à 150 mots sur un lieu que tu connais : '
                  'depuis quand, pourquoi il est célèbre et pourquoi c&rsquo;est '
                  'le meilleur (ou le pire).',
    actPlaceholder='I have been to &hellip; three times, and &hellip;',
)
