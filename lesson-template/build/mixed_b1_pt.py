# -*- coding: utf-8 -*-
"""B1 Mixed Grammar Tests — Portuguese. Same keys as mixed_b1_en.py.

Tense names stay in English; the other area names translate. English
examples stay English, in “” quotes.
"""

AREA = dict(
    presSimple='Present Simple', presCont='Present Continuous',
    pastSimple='Past Simple', pastCont='Past Continuous',
    presPerf='Present Perfect', futSimple='Futuro com WILL',
    compar='Comparativos e superlativos', modals='Verbos modais',
    cond='Condicionais', passive='A voz passiva', relative='Orações relativas',
    questions='Perguntas', quant='Quantificadores', prep='Preposições',
    stative='Verbos de estado',
)

COMMON = dict(
    chipLevel='B1 &middot; Intermediário',
    chipFocus='35 pontos &middot; cinco partes',
    chipCount='{N} slides',

    eIntro='Antes de começar',
    tIntro='Um teste, dez áreas de gramática',
    introA='Cinco partes',
    introAb='10 de escolha múltipla &middot; uma história com 8 lacunas '
            '&middot; 6 de verdadeiro ou falso &middot; 5 frases para montar '
            '&middot; 6 erros para corrigir.',
    introAn='Cada resposta é explicada assim que você responde.',
    introB='O que o teste avalia',
    introBb='Tempos do presente, do passado e perfect, WILL, comparativos, '
            'verbos modais, condicionais, voz passiva, orações relativas e '
            'perguntas.',
    introBn='Faça sozinho e não consulte nada. A nota só serve se for honesta.',

    eMC='Parte 1 &middot; Escolha múltipla',
    tMC='Escolha a forma certa',
    eStory='Parte 2 &middot; Leitura',
    eTF='Parte 3 &middot; Verdadeiro ou falso',
    tTF='Esta regra é verdadeira?',
    eOrder='Parte 4 &middot; Montar frases',
    tOrder='Coloque as partes em ordem',
    hOrder='Clique num bloco para colocá-lo e num bloco colocado para '
           'retirá-lo. Um ponto pela frase inteira.',
    eFix='Parte 5 &middot; Correção de erros',
    tFix='Encontre o erro e corrija',
    hFix='Um erro em cada frase. Escreva a frase inteira de novo, corrigida.',

    resPerfect='Perfeito. A gramática B1 já é natural para você &mdash; hora '
               'de começar o B2.',
    resStrong='Sólido. Faltam poucas lacunas; a lista abaixo mostra exatamente '
              'quais.',
    resMid='Bom progresso. Leia as explicações das que errou e tente de novo.',
    resLow='Continue praticando. Revise a lista abaixo com calma e faça o '
           'teste de novo amanhã.',

    actUse='Use pelo menos três',
    actSpeakBrief='Em pares. Use a gramática entre parênteses.',
    actWriteKind='Escrita',
)

P1 = dict(
    coverTitle='Teste de gramática <em>mista</em>',
    coverSub='Dez áreas de gramática, um teste: tempos verbais, modais, '
             'condicionais, voz passiva e mais.',
    tStory='O dia de Elena',
    hSt1='Escreva o verbo entre parênteses na forma correta. '
         '&ldquo;Oversleep&rdquo; = perder a hora.',
    hSt2='Escreva o verbo entre parênteses na forma correta. '
         '&ldquo;Borrow&rdquo; = pedir emprestado.',
    hSt3='A última lacuna pede um quantificador, não um verbo: escolha um dos '
         'dois entre parênteses.',
    gTournament='&ldquo;Tournament&rdquo; = torneio.',
    gSeatbelt='&ldquo;Seatbelt&rdquo; = cinto de segurança.',

    x_mc1='&ldquo;Listen!&rdquo; quer dizer agora: a ação está em andamento, '
          'IS + knocking. &ldquo;Knocks&rdquo; é um hábito; '
          '&ldquo;knocked&rdquo; e &ldquo;was knocking&rdquo; são passado.',
    x_mc2='WHILE + WAS / WERE + -ING dá a ação de fundo, mais longa; o Past '
          'Simple (&ldquo;rang&rdquo;) a interrompe. As outras três são formas '
          'do presente.',
    x_mc3='SINCE + um ponto no tempo (2019) pede HAS / HAVE + particípio. '
          '&ldquo;Lived&rdquo; não combina com &ldquo;since&rdquo;, nem as '
          'formas do presente.',
    x_mc4='&ldquo;I think&rdquo; introduz uma opinião sobre o futuro: WILL + '
          'verbo. &ldquo;Is winning&rdquo; significaria que o jogo está '
          'acontecendo agora.',
    x_mc5='Comparado com todos os filmes do ano, então o superlativo: THE '
          'BEST. &ldquo;Goodest&rdquo; e &ldquo;more good&rdquo; não existem; '
          '&ldquo;better&rdquo; compara só duas coisas.',
    x_mc6='Uma lei é uma obrigação forte: MUST + verbo. &ldquo;Might&rdquo; e '
          '&ldquo;could&rdquo; são possibilidade; &ldquo;would&rdquo; é '
          'hipotético.',
    x_mc7='Primeira condicional: IF + Present Simple, depois WILL na outra '
          'parte. Aqui WILL nunca vem depois de IF.',
    x_mc8='&ldquo;Would learn&rdquo; mostra uma situação imaginária, então '
          'segunda condicional: IF + Past Simple (&ldquo;had&rdquo;).',
    x_mc9='Uma ponte não se constrói sozinha, então a passiva: WAS + '
          'particípio. &ldquo;Built&rdquo; sozinho é ativo, e ninguém faz a '
          'ação.',
    x_mc10='WHO para pessoas. WHICH para coisas, WHOSE para posse, WHERE para '
           'lugares.',

    x_st1='&ldquo;Usually&rdquo; é um hábito: Present Simple, e '
          '&ldquo;she&rdquo; leva -S (&ldquo;gets up&rdquo;). &ldquo;This '
          'morning&rdquo; já terminou: Past Simple &ldquo;overslept&rdquo; '
          '(irregular).',
    x_st2='&ldquo;For almost three years now&rdquo; vai até hoje: HAS + lived. '
          'HAS BEEN living também está certo.',
    x_st3='WHILE + WAS + -ING para a ação mais longa; a batida na porta '
          '(&ldquo;knocked&rdquo;) a interrompe.',
    x_st4='A mesa está reservada, então é um compromisso marcado: IS + '
          'meeting. IS GOING TO meet também está certo.',
    x_st5='Primeira condicional. Depois de IF, Present Simple '
          '(&ldquo;is&rdquo;), não WILL; o resultado leva WILL + go.',
    x_st6='Numa frase afirmativa dizemos A LOT OF. MUCH é para negativas e '
          'perguntas: &ldquo;They don&rsquo;t serve much seafood.&rdquo;',

    tf1='Usamos o Present Perfect com um tempo terminado, como '
        '&ldquo;yesterday&rdquo; ou &ldquo;in 2010&rdquo;.',
    tf2='&ldquo;Must&rdquo; e &ldquo;have to&rdquo; expressam obrigação, mas '
        'só &ldquo;have to&rdquo; tem forma no passado: &ldquo;had to&rdquo;.',
    tf3='Na primeira condicional usamos &ldquo;will&rdquo; depois de '
        '&ldquo;if&rdquo;.',
    tf4='Antes de um superlativo geralmente vem &ldquo;the&rdquo;.',
    tf5='A voz passiva é BE + particípio.',
    tf6='Nas orações relativas usamos &ldquo;who&rdquo; para pessoas e '
        '&ldquo;which&rdquo; para coisas.',
    x_tf1='Falso. Um tempo terminado pede o Past Simple: &ldquo;I visited '
          'Paris in 2010&rdquo;, não &ldquo;I have visited&rdquo;.',
    x_tf2='Verdadeiro. MUST não tem passado próprio, então para o passado '
          'usamos HAD TO.',
    x_tf3='Falso. Depois de IF, o Present Simple (&ldquo;If it rains&rdquo;); '
          'WILL vai na outra parte (&ldquo;we&rsquo;ll stay in&rdquo;).',
    x_tf4='Verdadeiro. THE marca uma coisa como a única do seu grupo: THE '
          'best, THE tallest, THE most expensive.',
    x_tf5='Verdadeiro. &ldquo;Is built&rdquo;, &ldquo;was written&rdquo;, '
          '&ldquo;has been finished&rdquo;: sempre uma forma de BE + '
          'particípio.',
    x_tf6='Verdadeiro. No inglês do dia a dia THAT pode substituir os dois, '
          'mas WHO é só para pessoas e WHICH só para coisas.',

    x_or1='A passiva: sujeito + WAS + particípio, depois o tempo.',
    x_or2='&ldquo;Who lives next door&rdquo; vem logo depois de &ldquo;the '
          'man&rdquo; e diz qual homem. Depois o verbo principal, IS.',
    x_or3='Palavra interrogativa + DID + sujeito + forma base. Depois de DID o '
          'verbo não leva -ED: &ldquo;go&rdquo;, não &ldquo;went&rdquo;.',
    x_or4='Segunda condicional: IF + Past Simple (&ldquo;were&rdquo;), depois '
          'WOULD (&rsquo;D) + verbo.',
    x_or5='MUCH antes de um comparativo o reforça; THAN introduz a segunda '
          'coisa.',

    x_fx1='FOR + uma duração (five years). SINCE + um ponto de partida (2019, '
          'March).',
    x_fx2='Depois de IF na primeira condicional, o Present Simple: &ldquo;If I '
          'have time&rdquo;. WILL fica na outra parte.',
    x_fx3='&ldquo;Better&rdquo; já é comparativo. MORE + BETTER nunca está '
          'certo.',
    x_fx4='A passiva precisa do particípio: write &rarr; wrote &rarr; WRITTEN.',
    x_fx5='&ldquo;Money&rdquo; é incontável: MUCH, não MANY. MANY é para '
          'substantivos no plural: &ldquo;many coins&rdquo;.',
    x_fx6='WHICH é para coisas. Para uma pessoa, WHO (ou THAT).',

    actTitle='Agora use',
    actSpeak1='A sua manhã normal, e depois o que foi diferente hoje de manhã. '
              '(Present Simple, Past Simple)',
    actSpeak2='O que você faria com um ano inteiro livre? Pergunte ao seu '
              'colega também. (segunda condicional)',
    actSpeak3='Um prédio famoso da sua cidade: quando e por quem foi '
              'construído? (voz passiva)',
    actWriteBrief='Um e-mail de 120&ndash;150 palavras para um amigo que vem '
                  'na semana que vem: os seus planos, o que ele precisa trazer '
                  'e o que vocês vão fazer se chover.',
    actPlaceholder='Hi! I can&rsquo;t wait to see you next week&hellip;',
)

P2 = dict(
    coverTitle='Teste de gramática mista <em>parte 2</em>',
    coverSub='Mais dez pontos de gramática, só frases novas: tempos verbais, '
             'modais, condicionais, voz passiva e mais.',
    tStory='A viagem de Diego',
    hSt1='Escreva o verbo entre parênteses na forma correta.',
    hSt2='Escreva o verbo entre parênteses na forma correta. '
         '&ldquo;Suitcase&rdquo; = mala.',
    hSt3='Escreva o verbo entre parênteses na forma correta. '
         '&ldquo;Delayed&rdquo; = atrasado.',
    gForbidden='&ldquo;Forbidden&rdquo; = proibido.',

    x_mc1='&ldquo;Be quiet!&rdquo; quer dizer agora: a ação está em andamento, '
          'IS + sleeping. &ldquo;Sleeps&rdquo; é um hábito; as outras duas são '
          'passado.',
    x_mc2='WHILE + WERE + -ING dá a ação de fundo que a luz (&ldquo;went '
          'out&rdquo;) interrompeu. As outras são formas do presente.',
    x_mc3='&ldquo;For ten years now&rdquo; vai até hoje: HAVE + known. '
          '&ldquo;Are knowing&rdquo; está errado porque KNOW não é uma ação em '
          'andamento; &ldquo;knew&rdquo; diz que já acabou.',
    x_mc4='Uma promessa é uma decisão tomada na hora: WILL + verbo. &ldquo;Am '
          'helping&rdquo; precisaria de um compromisso já marcado.',
    x_mc5='Comparado com todas as cidades, então o superlativo: THE + busiEST. '
          '&ldquo;Busier&rdquo; compara duas; &ldquo;most busiest&rdquo; diz '
          'duas vezes.',
    x_mc6='&ldquo;Forbidden&rdquo; é uma proibição: MUSTN&rsquo;T. '
          '&ldquo;Don&rsquo;t have to&rdquo; quer dizer que não é necessário, '
          'quase o contrário.',
    x_mc7='Primeira condicional: IF + Present Simple, depois WON&rsquo;T / '
          'WILL na outra parte.',
    x_mc8='&ldquo;Could join&rdquo; mostra uma situação imaginária: IF + Past '
          'Simple, e com BE usamos WERE para todas as pessoas.',
    x_mc9='O quadro não se pintou sozinho, então a passiva: WAS + particípio, '
          'e BY diz quem pintou.',
    x_mc10='WHICH (ou THAT) para coisas. WHO para pessoas, WHOSE para posse, '
           'WHERE para lugares.',

    x_st1='&ldquo;Every summer&rdquo; é um hábito: Present Simple, e '
          '&ldquo;he&rdquo; leva -S.',
    x_st2='&ldquo;Last month&rdquo; já terminou: Past Simple '
          '&ldquo;booked&rdquo;. O amigo recomendou antes; '
          '&ldquo;recommended&rdquo; e &ldquo;had recommended&rdquo; estão '
          'certos.',
    x_st3='&ldquo;Never &hellip; before&rdquo; é a vida dele até agora: HAS + '
          'NEVER + visited.',
    x_st4='WHILE + WAS + -ING para a ação mais longa; o momento em que ele '
          'percebe a interrompe.',
    x_st5='O assento está escolhido, então é um plano marcado: IS + flying. IS '
          'GOING TO fly também está certo.',
    x_st6='Primeira condicional. Depois de IF, Present Simple '
          '(&ldquo;is&rdquo;); o resultado leva WILL + miss. MIGHT miss também '
          'está certo.',

    tf1='O Present Continuous pode expressar um plano futuro já marcado, como '
        '&ldquo;I&rsquo;m flying to Rome on Monday.&rdquo;',
    tf2='&ldquo;Mustn&rsquo;t&rdquo; e &ldquo;don&rsquo;t have to&rdquo; '
        'significam a mesma coisa.',
    tf3='Na segunda condicional costumamos usar &ldquo;were&rdquo; em vez de '
        '&ldquo;was&rdquo; com I, he, she e it.',
    tf4='Adjetivos de duas sílabas sempre levam &ldquo;more&rdquo;, nunca '
        '&ldquo;-er&rdquo;.',
    tf5='A passiva de &ldquo;People speak English here&rdquo; é '
        '&ldquo;English is spoken here.&rdquo;',
    tf6='&ldquo;Whose&rdquo; é usado para falar de posse.',
    x_tf1='Verdadeiro. Quando o plano está marcado (uma passagem, um horário), '
          'o Present Continuous é a escolha natural.',
    x_tf2='Falso. MUSTN&rsquo;T quer dizer que é proibido. DON&rsquo;T HAVE TO '
          'quer dizer que não é necessário. São quase opostos.',
    x_tf3='Verdadeiro. &ldquo;If I were you&rdquo;, &ldquo;If he were '
          'taller&rdquo;. &ldquo;Was&rdquo; é comum na fala, mas WERE é a '
          'forma padrão.',
    x_tf4='Falso. Muitos levam -ER: happy &rarr; happier, easy &rarr; easier, '
          'narrow &rarr; narrower.',
    x_tf5='Verdadeiro. O objeto (&ldquo;English&rdquo;) vira o sujeito, e o '
          'verbo vira IS + particípio.',
    x_tf6='Verdadeiro. &ldquo;Whose car is this?&rdquo; &middot; &ldquo;the man '
          'whose car was stolen&rdquo;.',

    x_or1='Uma pergunta na passiva: WAS + sujeito + particípio, depois BY + '
          'quem fez.',
    x_or2='WHERE introduz uma oração sobre um lugar: &ldquo;where we had '
          'dinner&rdquo; diz qual restaurante.',
    x_or3='HOW LONG + HAVE + sujeito + particípio: a pergunta no Present '
          'Perfect.',
    x_or4='Segunda condicional: IF + Past Simple (&ldquo;had&rdquo;), depois '
          'WOULD + verbo.',
    x_or5='THE + comparativo, THE + comparativo: duas coisas que mudam juntas.',

    x_fx1='AGREE é uma opinião, não uma ação em andamento: Present Simple, '
          '&ldquo;I agree&rdquo;.',
    x_fx2='MARRIED TO someone, não &ldquo;married with&rdquo;.',
    x_fx3='Depois de IF na segunda condicional, o Past Simple: &ldquo;If I '
          'had&rdquo;. WOULD fica na outra parte.',
    x_fx4='&ldquo;Easy&rdquo; termina em -Y, então leva -IER: EASIER, não '
          '&ldquo;more easy&rdquo;.',
    x_fx5='Na passiva, BY diz quem fez: &ldquo;sent by the manager&rdquo;. FOR '
          'seria quem recebe.',
    x_fx6='WHOSE já quer dizer &ldquo;his&rdquo;, então &ldquo;his&rdquo; está '
          'sobrando. Apague.',

    actTitle='Agora use',
    actSpeak1='Os seus planos para sábado, e o que vai fazer se chover. '
              '(Present Continuous, primeira condicional)',
    actSpeak2='No trabalho ou na escola: três coisas proibidas e três que não '
              'são obrigatórias. (modais)',
    actSpeak3='Uma viagem que deu errado: o que você estava fazendo quando '
              'aconteceu? (Past Continuous)',
    actWriteBrief='Uma avaliação de 120&ndash;150 palavras de um lugar que '
                  'você conhece: desde quando, por que é famoso e por que é o '
                  'melhor (ou o pior).',
    actPlaceholder='I have been to &hellip; three times, and &hellip;',
)
