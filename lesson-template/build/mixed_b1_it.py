# -*- coding: utf-8 -*-
"""B1 Mixed Grammar Tests — Italian. Same keys as mixed_b1_en.py.

Tense names stay in English; the other area names translate. English
examples stay English, in «» quotes.
"""

AREA = dict(
    presSimple='Present Simple', presCont='Present Continuous',
    pastSimple='Past Simple', pastCont='Past Continuous',
    presPerf='Present Perfect', futSimple='Futuro con WILL',
    compar='Comparativi e superlativi', modals='Verbi modali',
    cond='Periodi ipotetici', passive='Il passivo', relative='Frasi relative',
    questions='Domande', quant='Quantificatori', prep='Preposizioni',
    stative='Verbi di stato',
)

COMMON = dict(
    chipLevel='B1 &middot; Intermedio',
    chipFocus='35 punti &middot; cinque parti',
    chipCount='{N} slide',

    eIntro='Prima di iniziare',
    tIntro='Un test, dieci aree di grammatica',
    introA='Cinque parti',
    introAb='10 a scelta multipla &middot; una storia con 8 spazi &middot; 6 '
            'vero o falso &middot; 5 frasi da costruire &middot; 6 errori da '
            'correggere.',
    introAn='Ogni risposta viene spiegata appena la dai.',
    introB='Cosa verifica',
    introBb='Tempi presenti, passati e perfect, WILL, comparativi, verbi '
            'modali, periodi ipotetici, passivo, frasi relative e domande.',
    introBn='Lavora da solo e non cercare niente. Il punteggio serve solo se è '
            'onesto.',

    eMC='Parte 1 &middot; Scelta multipla',
    tMC='Scegli la forma giusta',
    eStory='Parte 2 &middot; Lettura',
    eTF='Parte 3 &middot; Vero o falso',
    tTF='Questa regola è vera?',
    eOrder='Parte 4 &middot; Costruire frasi',
    tOrder='Metti le parti in ordine',
    hOrder='Clicca su un blocco per metterlo, su un blocco messo per toglierlo. '
           'Un punto per la frase intera.',
    eFix='Parte 5 &middot; Correzione degli errori',
    tFix='Trova l&rsquo;errore e correggilo',
    hFix='Un errore per frase. Riscrivi tutta la frase, corretta.',

    resPerfect='Perfetto. La grammatica B1 ti viene naturale &mdash; è ora del '
               'B2.',
    resStrong='Solido. Restano poche lacune; l&rsquo;elenco qui sotto ti dice '
              'esattamente quali.',
    resMid='Buoni progressi. Rileggi le spiegazioni degli errori e riprova.',
    resLow='Continua così. Ripassa con calma l&rsquo;elenco qui sotto e rifai '
           'il test domani.',

    actUse='Usane almeno tre',
    actSpeakBrief='In coppia. Usa la grammatica tra parentesi.',
    actWriteKind='Scrittura',
)

P1 = dict(
    coverTitle='Test di grammatica <em>mista</em>',
    coverSub='Dieci aree di grammatica, un test: tempi verbali, modali, periodi '
             'ipotetici, passivo e altro.',
    tStory='La giornata di Elena',
    hSt1='Scrivi il verbo tra parentesi nella forma giusta. '
         '&laquo;Oversleep&raquo; = non svegliarsi in tempo.',
    hSt2='Scrivi il verbo tra parentesi nella forma giusta. '
         '&laquo;Borrow&raquo; = prendere in prestito.',
    hSt3='L&rsquo;ultimo spazio vuole un quantificatore, non un verbo: scegli '
         'uno dei due tra parentesi.',
    gTournament='&laquo;Tournament&raquo; = torneo.',
    gSeatbelt='&laquo;Seatbelt&raquo; = cintura di sicurezza.',

    x_mc1='&laquo;Listen!&raquo; vuol dire adesso: l&rsquo;azione è in corso, '
          'IS + knocking. &laquo;Knocks&raquo; è un&rsquo;abitudine; '
          '&laquo;knocked&raquo; e &laquo;was knocking&raquo; sono passato.',
    x_mc2='WHILE + WAS / WERE + -ING dà l&rsquo;azione di sfondo, più lunga; '
          'il Past Simple (&laquo;rang&raquo;) la interrompe. Le altre tre sono '
          'forme del presente.',
    x_mc3='SINCE + un momento (2019) vuole HAS / HAVE + participio passato. '
          '&laquo;Lived&raquo; non va con &laquo;since&raquo;, e nemmeno le '
          'forme del presente.',
    x_mc4='&laquo;I think&raquo; introduce un&rsquo;opinione sul futuro: WILL + '
          'verbo. &laquo;Is winning&raquo; vorrebbe dire che la partita si sta '
          'giocando ora.',
    x_mc5='Confrontato con tutti i film dell&rsquo;anno, quindi il '
          'superlativo: THE BEST. &laquo;Goodest&raquo; e &laquo;more '
          'good&raquo; non esistono; &laquo;better&raquo; confronta solo due '
          'cose.',
    x_mc6='Una legge è un obbligo forte: MUST + verbo. &laquo;Might&raquo; e '
          '&laquo;could&raquo; esprimono possibilità; &laquo;would&raquo; è '
          'ipotetico.',
    x_mc7='Periodo ipotetico di primo tipo: IF + Present Simple, poi WILL '
          'nell&rsquo;altra parte. Qui WILL non va mai dopo IF.',
    x_mc8='&laquo;Would learn&raquo; indica una situazione immaginaria, quindi '
          'secondo tipo: IF + Past Simple (&laquo;had&raquo;).',
    x_mc9='Un ponte non si costruisce da solo, quindi il passivo: WAS + '
          'participio passato. &laquo;Built&raquo; da solo è attivo e nessuno '
          'compie l&rsquo;azione.',
    x_mc10='WHO per le persone. WHICH per le cose, WHOSE per il possesso, '
           'WHERE per i luoghi.',

    x_st1='&laquo;Usually&raquo; è un&rsquo;abitudine: Present Simple, e '
          '&laquo;she&raquo; prende la -S (&laquo;gets up&raquo;). &laquo;This '
          'morning&raquo; è finito: Past Simple &laquo;overslept&raquo; '
          '(irregolare).',
    x_st2='&laquo;For almost three years now&raquo; arriva fino a oggi: HAS + '
          'lived. Anche HAS BEEN living è corretto.',
    x_st3='WHILE + WAS + -ING per l&rsquo;azione più lunga; il colpo alla porta '
          '(&laquo;knocked&raquo;) la interrompe.',
    x_st4='Il tavolo è prenotato, quindi è un impegno fissato: IS + meeting. '
          'Anche IS GOING TO meet è corretto.',
    x_st5='Primo tipo. Dopo IF, Present Simple (&laquo;is&raquo;), non WILL; '
          'la conseguenza prende WILL + go.',
    x_st6='In una frase affermativa si dice A LOT OF. MUCH si usa nelle '
          'negative e nelle domande: &laquo;They don&rsquo;t serve much '
          'seafood.&raquo;',

    tf1='Usiamo il Present Perfect con un tempo concluso, come '
        '&laquo;yesterday&raquo; o &laquo;in 2010&raquo;.',
    tf2='&laquo;Must&raquo; e &laquo;have to&raquo; esprimono entrambi un '
        'obbligo, ma solo &laquo;have to&raquo; ha una forma passata: '
        '&laquo;had to&raquo;.',
    tf3='Nel periodo ipotetico di primo tipo usiamo &laquo;will&raquo; dopo '
        '&laquo;if&raquo;.',
    tf4='Davanti a un superlativo di solito c&rsquo;è &laquo;the&raquo;.',
    tf5='Il passivo è BE + participio passato.',
    tf6='Nelle frasi relative usiamo &laquo;who&raquo; per le persone e '
        '&laquo;which&raquo; per le cose.',
    x_tf1='Falso. Un tempo concluso vuole il Past Simple: &laquo;I visited '
          'Paris in 2010&raquo;, non &laquo;I have visited&raquo;.',
    x_tf2='Vero. MUST non ha un passato suo, quindi per il passato usiamo HAD '
          'TO.',
    x_tf3='Falso. Dopo IF, il Present Simple (&laquo;If it rains&raquo;); WILL '
          'va nell&rsquo;altra parte (&laquo;we&rsquo;ll stay in&raquo;).',
    x_tf4='Vero. THE indica una cosa come l&rsquo;unica del suo gruppo: THE '
          'best, THE tallest, THE most expensive.',
    x_tf5='Vero. &laquo;Is built&raquo;, &laquo;was written&raquo;, &laquo;has '
          'been finished&raquo;: sempre una forma di BE + participio passato.',
    x_tf6='Vero. Nell&rsquo;inglese di tutti i giorni THAT può sostituire '
          'entrambi, ma WHO è solo per le persone e WHICH solo per le cose.',

    x_or1='Il passivo: soggetto + WAS + participio passato, poi il tempo.',
    x_or2='&laquo;Who lives next door&raquo; viene subito dopo &laquo;the '
          'man&raquo; e dice di quale uomo si parla. Poi il verbo principale, '
          'IS.',
    x_or3='Parola interrogativa + DID + soggetto + forma base. Dopo DID il '
          'verbo non prende -ED: &laquo;go&raquo;, non &laquo;went&raquo;.',
    x_or4='Secondo tipo: IF + Past Simple (&laquo;were&raquo;), poi WOULD '
          '(&rsquo;D) + verbo.',
    x_or5='MUCH davanti a un comparativo lo rafforza; THAN introduce il '
          'secondo termine.',

    x_fx1='FOR + una durata (five years). SINCE + un punto di partenza (2019, '
          'March).',
    x_fx2='Dopo IF nel primo tipo, il Present Simple: &laquo;If I have '
          'time&raquo;. WILL resta nell&rsquo;altra parte.',
    x_fx3='&laquo;Better&raquo; è già un comparativo. MORE + BETTER non è mai '
          'corretto.',
    x_fx4='Il passivo vuole il participio passato: write &rarr; wrote &rarr; '
          'WRITTEN.',
    x_fx5='&laquo;Money&raquo; è non numerabile: MUCH, non MANY. MANY va con i '
          'sostantivi plurali: &laquo;many coins&raquo;.',
    x_fx6='WHICH è per le cose. Per una persona, WHO (o THAT).',

    actTitle='Ora usalo',
    actSpeak1='La tua mattina normale, poi cosa è stato diverso stamattina. '
              '(Present Simple, Past Simple)',
    actSpeak2='Cosa faresti con un anno intero libero? Chiedilo anche al tuo '
              'compagno. (secondo tipo)',
    actSpeak3='Un edificio famoso della tua città: quando e da chi è stato '
              'costruito? (il passivo)',
    actWriteBrief='Un&rsquo;email di 120&ndash;150 parole a un amico che viene '
                  'la settimana prossima: i tuoi piani, cosa deve portare e '
                  'cosa farete se piove.',
    actPlaceholder='Hi! I can&rsquo;t wait to see you next week&hellip;',
)

P2 = dict(
    coverTitle='Test di grammatica mista <em>parte 2</em>',
    coverSub='Altri dieci punti di grammatica, tutte frasi nuove: tempi verbali, '
             'modali, periodi ipotetici, passivo e altro.',
    tStory='Il viaggio di Diego',
    hSt1='Scrivi il verbo tra parentesi nella forma giusta.',
    hSt2='Scrivi il verbo tra parentesi nella forma giusta. '
         '&laquo;Suitcase&raquo; = valigia.',
    hSt3='Scrivi il verbo tra parentesi nella forma giusta. '
         '&laquo;Delayed&raquo; = in ritardo.',
    gForbidden='&laquo;Forbidden&raquo; = vietato.',

    x_mc1='&laquo;Be quiet!&raquo; vuol dire adesso: l&rsquo;azione è in corso, '
          'IS + sleeping. &laquo;Sleeps&raquo; è un&rsquo;abitudine; le altre '
          'due sono passato.',
    x_mc2='WHILE + WERE + -ING dà l&rsquo;azione di sfondo che il blackout '
          '(&laquo;went out&raquo;) ha interrotto. Le altre sono forme del '
          'presente.',
    x_mc3='&laquo;For ten years now&raquo; arriva fino a oggi: HAVE + known. '
          '&laquo;Are knowing&raquo; è sbagliato perché KNOW non è '
          'un&rsquo;azione in corso; &laquo;knew&raquo; dice che è finita.',
    x_mc4='Una promessa è una decisione presa mentre parli: WILL + verbo. '
          '&laquo;Am helping&raquo; richiederebbe un impegno già preso.',
    x_mc5='Confrontato con tutte le città, quindi il superlativo: THE + '
          'busiEST. &laquo;Busier&raquo; confronta due cose; &laquo;most '
          'busiest&raquo; lo dice due volte.',
    x_mc6='&laquo;Forbidden&raquo; è un divieto: MUSTN&rsquo;T. &laquo;Don&rsquo;t '
          'have to&raquo; vuol dire che non è necessario, quasi il contrario.',
    x_mc7='Primo tipo: IF + Present Simple, poi WON&rsquo;T / WILL '
          'nell&rsquo;altra parte.',
    x_mc8='&laquo;Could join&raquo; indica una situazione immaginaria: IF + '
          'Past Simple, e con BE usiamo WERE per tutte le persone.',
    x_mc9='Il quadro non si è dipinto da solo, quindi il passivo: WAS + '
          'participio passato, e BY nomina il pittore.',
    x_mc10='WHICH (o THAT) per le cose. WHO per le persone, WHOSE per il '
           'possesso, WHERE per i luoghi.',

    x_st1='&laquo;Every summer&raquo; è un&rsquo;abitudine: Present Simple, e '
          '&laquo;he&raquo; prende la -S.',
    x_st2='&laquo;Last month&raquo; è finito: Past Simple &laquo;booked&raquo;. '
          'L&rsquo;amico l&rsquo;ha consigliato prima; &laquo;recommended&raquo; '
          'e &laquo;had recommended&raquo; sono entrambi corretti.',
    x_st3='&laquo;Never &hellip; before&raquo; è la sua vita fino a ora: HAS + '
          'NEVER + visited.',
    x_st4='WHILE + WAS + -ING per l&rsquo;azione più lunga; il momento in cui '
          'se ne accorge la interrompe.',
    x_st5='Il posto è scelto, quindi è un impegno fissato: IS + flying. Anche '
          'IS GOING TO fly è corretto.',
    x_st6='Primo tipo. Dopo IF, Present Simple (&laquo;is&raquo;); la '
          'conseguenza prende WILL + miss. Anche MIGHT miss è corretto.',

    tf1='Il Present Continuous può esprimere un impegno futuro già fissato, '
        'come &laquo;I&rsquo;m flying to Rome on Monday.&raquo;',
    tf2='&laquo;Mustn&rsquo;t&raquo; e &laquo;don&rsquo;t have to&raquo; '
        'significano la stessa cosa.',
    tf3='Nel periodo ipotetico di secondo tipo usiamo spesso '
        '&laquo;were&raquo; invece di &laquo;was&raquo; con I, he, she e it.',
    tf4='Gli aggettivi di due sillabe prendono sempre &laquo;more&raquo;, mai '
        '&laquo;-er&raquo;.',
    tf5='Il passivo di &laquo;People speak English here&raquo; è '
        '&laquo;English is spoken here.&raquo;',
    tf6='&laquo;Whose&raquo; si usa per parlare di possesso.',
    x_tf1='Vero. Quando il piano è fissato (un biglietto, un orario), il '
          'Present Continuous è la scelta naturale.',
    x_tf2='Falso. MUSTN&rsquo;T vuol dire che è vietato. DON&rsquo;T HAVE TO '
          'vuol dire che non è necessario. Sono quasi opposti.',
    x_tf3='Vero. &laquo;If I were you&raquo;, &laquo;If he were taller&raquo;. '
          '&laquo;Was&raquo; è comune nel parlato, ma WERE è la forma '
          'standard.',
    x_tf4='Falso. Molti prendono -ER: happy &rarr; happier, easy &rarr; '
          'easier, narrow &rarr; narrower.',
    x_tf5='Vero. Il complemento (&laquo;English&raquo;) diventa il soggetto, e '
          'il verbo diventa IS + participio passato.',
    x_tf6='Vero. &laquo;Whose car is this?&raquo; &middot; &laquo;the man whose '
          'car was stolen&raquo;.',

    x_or1='Una domanda al passivo: WAS + soggetto + participio passato, poi BY '
          '+ chi l&rsquo;ha fatto.',
    x_or2='WHERE introduce una frase su un luogo: &laquo;where we had '
          'dinner&raquo; dice quale ristorante.',
    x_or3='HOW LONG + HAVE + soggetto + participio passato: la domanda al '
          'Present Perfect.',
    x_or4='Secondo tipo: IF + Past Simple (&laquo;had&raquo;), poi WOULD + '
          'verbo.',
    x_or5='THE + comparativo, THE + comparativo: due cose che cambiano '
          'insieme.',

    x_fx1='AGREE è un&rsquo;opinione, non un&rsquo;azione in corso: Present '
          'Simple, &laquo;I agree&raquo;.',
    x_fx2='MARRIED TO someone, non &laquo;married with&raquo;.',
    x_fx3='Dopo IF nel secondo tipo, il Past Simple: &laquo;If I had&raquo;. '
          'WOULD resta nell&rsquo;altra parte.',
    x_fx4='&laquo;Easy&raquo; finisce in -Y, quindi prende -IER: EASIER, non '
          '&laquo;more easy&raquo;.',
    x_fx5='Nel passivo, BY nomina chi ha fatto l&rsquo;azione: &laquo;sent by '
          'the manager&raquo;. FOR sarebbe il destinatario.',
    x_fx6='WHOSE vuol già dire &laquo;his&raquo;, quindi &laquo;his&raquo; è '
          'di troppo. Cancellalo.',

    actTitle='Ora usalo',
    actSpeak1='I tuoi piani per sabato, e cosa farai se piove. (Present '
              'Continuous, primo tipo)',
    actSpeak2='Al lavoro o a scuola: tre cose vietate e tre non obbligatorie. '
              '(verbi modali)',
    actSpeak3='Un viaggio andato male: cosa stavi facendo quando è successo? '
              '(Past Continuous)',
    actWriteBrief='Una recensione di 120&ndash;150 parole su un posto che '
                  'conosci: da quanto tempo, per cosa è famoso e perché è il '
                  'migliore (o il peggiore).',
    actPlaceholder='I have been to &hellip; three times, and &hellip;',
)
