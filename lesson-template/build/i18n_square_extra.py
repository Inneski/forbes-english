# -*- coding: utf-8 -*-
"""The Square — the seven languages beyond English, German and Spanish.

Split out of `i18n_square.py` only for length: ten complete languages at 97
keys each is a thousand strings, and one file of it is unreadable. The
contents are exactly the same shape — `EXTRA[code]` is merged into
`i18n_square.T` at import, and the completeness check in that module covers
these the same as the first three.

The scope boundary of HOUSE-STYLE §8 holds here as it does there: the
headwords, the example sentences, `searchStem` and `actPlaceholder` are the
English being taught and stay English in every one of the ten. What
translates is the definition, the instruction and the chrome.

Arabic is in the engine's RTL_LANGS, so the layout mirrors when it is
selected; nothing in this file has to allow for that.
"""

EXTRA = {}

# ══════════════════════════════════════════════════════════════════════
#  FRENCH
# ══════════════════════════════════════════════════════════════════════
EXTRA['fr'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='Quarante-quatre mots, un après-midi en cubes',
    chipLevel='A2 · Élémentaire', chipFocus='Vocabulaire',
    chipCount='24 diapositives',
    bankLabel='Banque de mots :',

    e1='Choses de la place',
    e2='Ce que font les gens',
    e3='Idées, sentiments, petits mots',
    e4='Exercices',

    s1t="À l'intérieur d'un bâtiment",
    s1ab='Une ouverture dans un mur, avec du verre. La lumière entre ; tu '
         'regardes dehors.',
    s1bb="Tu l'ouvres pour entrer dans une pièce, un bâtiment ou une voiture.",
    s1cb="La pièce où l'on se lave.",
    s1db='Un petit tissu épais posé au sol. La moquette couvre tout le sol ; '
         'un <em>rug</em> non.',

    s2t='Dans ton sac',
    s2ab='Un contenant souple, ouvert en haut, pour transporter des choses.',
    s2bb='Une petite poche cousue dans les vêtements.',
    s2cb="De l'argent plat et rond, en métal.",
    s2db='Une lentille avec un manche. Elle fait paraître grandes les petites '
         'choses.',

    s3t='Lire, jouer, faire',
    s3ab="Un fascicule fin avec beaucoup d'images. Il paraît chaque semaine ou "
         'chaque mois.',
    s3bb='De grandes feuilles de papier avec les nouvelles du jour. Il paraît '
         'chaque jour.',
    s3cb='Des jeux auxquels on joue sur un plateau, en déplaçant des pièces — '
         'les échecs, par exemple.',
    s3db='Le travail scolaire que tu fais à la maison. Pas de pluriel : jamais '
         '<em>homeworks</em>.',

    s4t='Sur toi, et sur la table',
    s4ab='Ce que tu portes : pantalons, robes, vestes. Toujours au pluriel.',
    s4bb="Un short qu'un homme porte pour nager. Au pluriel aussi.",
    s4cb='Du pain grillé, doré et chaud. On dit <em>a piece of toast</em>, pas '
         '<em>a toast</em>.',
    s4db='Une personne que tu connais et que tu apprécies.',

    s5t='Ce que font tes mains',
    s5ab='Déplacer quelque chose loin de toi.',
    s5bb='Déplacer quelque chose vers toi.',
    s5cb='Tendre le bras pour toucher ou prendre quelque chose.',
    s5db='Porter la main, ou une batte, avec force contre quelque chose.',

    s6t='Les mains, et où tu vas',
    s6ab='Marquer une surface avec quelque chose de pointu.',
    s6bb='Assembler des pièces : une maison, un mur, une machine.',
    s6cb='Assembler des choses pour créer quelque chose. Plus large que '
         '<em>build</em> — on fait un gâteau, on construit une maison.',
    s6db='Se déplacer sur ses pieds, un pied toujours au sol.',

    s7t='Son, direction, esprit',
    s7ab="Souffler de l'air entre les lèvres et produire un son aigu et clair.",
    s7bb='Passer à un nouveau point — un nouveau sujet, ou une nouvelle '
         'direction.',
    s7cb='Avoir une opinion ou une idée sur quelque chose.',
    s7db="Avoir déjà l'information en tête.",

    s8t='Commencer, abandonner, finir',
    s8ab='Quand quelque chose commence à se produire.',
    s8bb='Mener une tâche à son terme. La finir.',
    s8cb='Quitter des gens qui ont encore besoin de toi. Le verbe est '
         'de-<em>SERT</em> ; le <em>DE</em>-sert sec et sablonneux est le nom.',
    s8db='Quelque chose qui arrive, en général prévu et important.',

    s9t='Vrai, faux, mauvais',
    s9ab='Conforme aux faits.',
    s9bb='Pas vrai.',
    s9cb="De mauvaise qualité, ou d'un niveau faible.",
    s9db='Un homme qui ne suit pas les règles — souvent dit avec un sourire.',

    s10t='Sentiments, et à quel point',
    s10ab='Très contrarié. En colère.',
    s10bb='De grande valeur ou de grand effet. Cela compte.',
    s10cb='À un haut degré. Cela renforce un adjectif.',
    s10db='De temps en temps — pas tout le temps.',

    s11t='Les quatre plus petits mots',
    s11ab='À utiliser la première fois que tu nommes quelque chose.',
    s11bb="À l'intérieur de quelque chose, ou entouré par cela.",
    s11cb='Deux personnes ou choses ou plus, que tu as déjà nommées.',
    s11db="Un bonjour familier — et un au revoir familier. C'est de l'italien, "
          "et l'anglais l'a emprunté.",

    q1t="Son bras s'est tendu",
    q2t='Il est parti sans revenir',
    q3t='Un mot, pas de pluriel',
    q4t='Chaque jour, ou chaque mois ?',

    g1t='Sur la place',
    g2t='Pas tous les jours',
    gapHint='Écris un mot dans chaque espace.',

    matchT='Mot et sens',
    matchHint="Clique sur un mot, puis sur ce qu'il signifie.",
    matchWhy="Quatre verbes et un nom, tous des choses que l'on peut voir sur "
             'la place.',

    sortT='Une chose, ou une action ?',
    sortHint='Place chaque mot dans la bonne case.',
    sortWhy='Une chose est un nom — on peut mettre <em>a</em> ou <em>the</em> '
            'devant. Une action est un verbe — on peut mettre <em>I</em> devant.',

    orderT='Construis la phrase',
    orderHint='Clique sur les parties dans le bon ordre.',
    orderWhy='<em>Sometimes</em> peut ouvrir la phrase. Ensuite ce que tu fais, '
             'puis pourquoi, puis quand.',

    searchT='Trouve-le avant la fin du chrono',
    searchStem='Trouve la <em>magnifying glass</em>.',
    searchWhy='Une <em>magnifying glass</em> est une lentille ronde avec un '
              "manche. La pièce est ronde aussi, mais elle n'a pas de manche.",

    resPerfect="Score parfait. Quarante-quatre mots, et aucun n'est passé à "
               'travers.',
    resStrong='Solide. Retourne aux deux diapositives à trous — c’est là que le '
              'dernier point se perd le plus souvent.',
    resMid='Une bonne moitié. Relis les quatre diapositives de noms, puis '
           'réessaie.',
    resLow='Recommence depuis le début et lis chaque carte à voix haute avant '
           'de répondre. Ce sont des mots que tu croises tous les jours.',

    actTitle='Maintenant, utilise-les',
    actUse='Utilise au moins cinq :',
    actSpeakBrief='À deux. Ne lis pas les cartes — dis-le.',
    actSpeak1="Regardez l'image de couverture. Dis à ton binôme cinq choses que "
              'tu vois. Dis <em>a</em> la première fois et <em>the</em> ensuite.',
    actSpeak2="Ton binôme a un sac. Demande ce qu'il y a dedans. Réponds avec "
              "trois mots d'aujourd'hui et une chose qui n'est pas vraie.",
    actSpeak3='Raconte ton dimanche : ce que tu fais parfois, ce que tu finis '
              'avant lundi, et une chose qui te met en colère.',
    actWriteKind='Écriture · devoirs',
    actWriteBrief="Ton ami a manqué l'événement sur la place samedi. Écris-lui "
                  'un message : ce qui a commencé, ce que tu as vu, ce que tu as '
                  'fait, et pourquoi tu as dû finir tôt. 120–150 mots.',
    actPlaceholder='Ciao! You missed a good day…',
)

# ══════════════════════════════════════════════════════════════════════
#  ITALIAN
# ══════════════════════════════════════════════════════════════════════
EXTRA['it'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='Quarantaquattro parole, un pomeriggio a cubi',
    chipLevel='A2 · Elementare', chipFocus='Lessico', chipCount='24 diapositive',
    bankLabel='Banca di parole:',

    e1='Cose della piazza',
    e2='Quello che fa la gente',
    e3='Idee, sentimenti, parole piccole',
    e4='Esercizi',

    s1t='Dentro un edificio',
    s1ab="Un'apertura nel muro, con il vetro. La luce entra; tu guardi fuori.",
    s1bb="La apri per entrare in una stanza, in un edificio o in un'auto.",
    s1cb='La stanza dove ci si lava.',
    s1db='Un panno piccolo e spesso sul pavimento. La moquette copre tutto il '
         'pavimento; un <em>rug</em> no.',

    s2t='Nella tua borsa',
    s2ab='Un contenitore morbido, aperto in alto, per portare le cose.',
    s2bb='Una piccola tasca cucita nei vestiti.',
    s2cb='Denaro piatto e rotondo, fatto di metallo.',
    s2db='Una lente con un manico. Fa sembrare grandi le cose piccole.',

    s3t='Leggere, giocare, fare',
    s3ab='Un fascicolo sottile con molte immagini. Esce ogni settimana o ogni '
         'mese.',
    s3bb='Grandi fogli di carta con le notizie di oggi. Esce ogni giorno.',
    s3cb='Giochi che si fanno su un tabellone, muovendo pezzi — gli scacchi, '
         'per esempio.',
    s3db='Il lavoro di scuola che fai a casa. Senza plurale: mai '
         '<em>homeworks</em>.',

    s4t='Addosso a te, e sul tavolo',
    s4ab='Quello che indossi: pantaloni, vestiti, giacche. Sempre plurale.',
    s4bb='Pantaloncini che un uomo indossa per nuotare. Anche plurale.',
    s4cb='Pane reso caldo e dorato. Si dice <em>a piece of toast</em>, non '
         '<em>a toast</em>.',
    s4db='Una persona che conosci e che ti piace.',

    s5t='Quello che fanno le tue mani',
    s5ab='Spostare qualcosa lontano da te.',
    s5bb='Spostare qualcosa verso di te.',
    s5cb='Allungare il braccio per toccare o prendere qualcosa.',
    s5db='Portare la mano, o una mazza, con forza contro qualcosa.',

    s6t='Le mani, e dove vai',
    s6ab='Segnare una superficie con qualcosa di appuntito.',
    s6bb='Mettere insieme dei pezzi: una casa, un muro, una macchina.',
    s6cb='Mettere insieme delle cose per creare qualcosa. Più ampio di '
         '<em>build</em> — una torta si fa, una casa si costruisce.',
    s6db='Muoversi sui piedi, un piede sempre a terra.',

    s7t='Suono, direzione, mente',
    s7ab='Soffiare aria tra le labbra e fare un suono acuto e chiaro.',
    s7bb='Passare a un punto nuovo — un argomento nuovo, o una direzione nuova.',
    s7cb="Avere un'opinione o un'idea su qualcosa.",
    s7db="Avere già l'informazione in testa.",

    s8t='Iniziare, abbandonare, finire',
    s8ab='Quando qualcosa comincia ad accadere.',
    s8bb='Portare un lavoro alla fine. Completarlo.',
    s8cb='Lasciare persone che hanno ancora bisogno di te. Il verbo è '
         'de-<em>SERT</em>; il <em>DE</em>-sert secco e sabbioso è il sostantivo.',
    s8db='Qualcosa che accade, di solito previsto e importante.',

    s9t='Vero, falso, cattivo',
    s9ab='In accordo con i fatti.',
    s9bb='Non vero.',
    s9cb='Di scarsa qualità, o di livello basso.',
    s9db='Un uomo che non segue le regole — spesso detto con un sorriso.',

    s10t='Sentimenti, e quanto',
    s10ab='Molto seccato. Arrabbiato.',
    s10bb='Di grande valore o effetto. Conta.',
    s10cb='In alto grado. Rafforza un aggettivo.',
    s10db='Ogni tanto — non tutto il tempo.',

    s11t='Le quattro parole più piccole',
    s11ab='Usalo la prima volta che nomini qualcosa.',
    s11bb='Dentro qualcosa, o circondato da esso.',
    s11cb='Due o più persone o cose che hai già nominato.',
    s11db="Un ciao informale — e un arrivederci informale. È italiano, e "
          "l'inglese lo ha preso in prestito.",

    q1t='Il suo braccio si è allungato',
    q2t="Se n'è andato e basta",
    q3t='Una parola, senza plurale',
    q4t='Ogni giorno, o ogni mese?',

    g1t='In piazza',
    g2t='Non tutti i giorni',
    gapHint='Scrivi una parola in ogni spazio.',

    matchT='Parola e significato',
    matchHint='Clicca una parola, poi il suo significato.',
    matchWhy='Quattro verbi e un sostantivo, tutte cose che si possono vedere '
             'in piazza.',

    sortT="Una cosa, o un'azione?",
    sortHint='Metti ogni parola nella casella giusta.',
    sortWhy='Una cosa è un sostantivo — puoi metterci davanti <em>a</em> o '
            "<em>the</em>. Un'azione è un verbo — puoi metterci davanti "
            '<em>I</em>.',

    orderT='Costruisci la frase',
    orderHint="Clicca le parti nell'ordine giusto.",
    orderWhy='<em>Sometimes</em> può aprire la frase. Poi quello che fai, poi '
             'perché, poi quando.',

    searchT='Trovalo prima che scada il tempo',
    searchStem='Trova la <em>magnifying glass</em>.',
    searchWhy='Una <em>magnifying glass</em> è una lente rotonda con un manico. '
              'Anche la moneta è rotonda, ma non ha il manico.',

    resPerfect='Punteggio pieno. Quarantaquattro parole, e non ne è sfuggita '
               'nessuna.',
    resStrong='Bene. Torna alle due diapositive con gli spazi — è lì che di '
              "solito se ne va l'ultimo punto.",
    resMid='Una buona metà. Rileggi le quattro diapositive dei sostantivi e '
           'riprova.',
    resLow="Ricomincia dall'inizio e leggi ogni scheda ad alta voce prima di "
           'rispondere. Sono parole che incontri ogni giorno.',

    actTitle='Ora usale',
    actUse='Usane almeno cinque:',
    actSpeakBrief='In coppia. Non leggere le schede — dillo.',
    actSpeak1="Guardate l'immagine di copertina. Di' al tuo compagno cinque "
              "cose che vedi. Di' <em>a</em> la prima volta e <em>the</em> dopo.",
    actSpeak2="Il tuo compagno ha una borsa. Chiedi che cosa c'è dentro. "
              'Rispondi con tre parole di oggi e una cosa che non è vera.',
    actSpeak3='Racconta la tua domenica: che cosa fai a volte, che cosa finisci '
              'prima di lunedì, e una cosa che ti fa arrabbiare.',
    actWriteKind='Scrittura · compiti',
    actWriteBrief="Il tuo amico si è perso l'evento in piazza sabato. Scrivigli "
                  'un messaggio: che cosa è iniziato, che cosa hai visto, che '
                  'cosa hai fatto e perché hai dovuto finire presto. '
                  '120–150 parole.',
    actPlaceholder='Ciao! You missed a good day…',
)

# ══════════════════════════════════════════════════════════════════════
#  PORTUGUESE
# ══════════════════════════════════════════════════════════════════════
EXTRA['pt'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='Quarenta e quatro palavras, uma tarde em blocos',
    chipLevel='A2 · Elementar', chipFocus='Vocabulário',
    chipCount='24 diapositivos',
    bankLabel='Banco de palavras:',

    e1='Coisas da praça',
    e2='O que as pessoas fazem',
    e3='Ideias, sentimentos, palavras pequenas',
    e4='Prática',

    s1t='Dentro de um edifício',
    s1ab='Uma abertura na parede, com vidro. A luz entra; tu olhas para fora.',
    s1bb='Abre-la para entrar num quarto, num edifício ou num carro.',
    s1cb='A divisão onde te lavas.',
    s1db='Um pano pequeno e grosso no chão. A alcatifa cobre o chão todo; um '
         '<em>rug</em> não.',

    s2t='Na tua bolsa',
    s2ab='Um recipiente mole, aberto em cima, para transportar coisas.',
    s2bb='Um bolso pequeno cosido na roupa.',
    s2cb='Dinheiro plano e redondo, feito de metal.',
    s2db='Uma lente com cabo. Faz as coisas pequenas parecerem grandes.',

    s3t='Ler, jogar, fazer',
    s3ab='Um caderno fino com muitas imagens. Sai todas as semanas ou todos os '
         'meses.',
    s3bb='Folhas grandes de papel com as notícias de hoje. Sai todos os dias.',
    s3cb='Jogos que se jogam num tabuleiro, movendo peças — o xadrez, por '
         'exemplo.',
    s3db='Trabalho da escola que fazes em casa. Sem plural: nunca '
         '<em>homeworks</em>.',

    s4t='Em ti, e na mesa',
    s4ab='O que vestes: calças, vestidos, casacos. Sempre no plural.',
    s4bb='Calções que um homem veste para nadar. Também plural.',
    s4cb='Pão tornado quente e dourado. Diz-se <em>a piece of toast</em>, não '
         '<em>a toast</em>.',
    s4db='Uma pessoa que conheces e de quem gostas.',

    s5t='O que as tuas mãos fazem',
    s5ab='Mover algo para longe de ti.',
    s5bb='Mover algo na tua direção.',
    s5cb='Esticar o braço para tocar ou apanhar algo.',
    s5db='Levar a mão, ou um taco, com força contra algo.',

    s6t='As mãos, e para onde vais',
    s6ab='Marcar uma superfície com algo pontiagudo.',
    s6bb='Juntar peças: uma casa, um muro, uma máquina.',
    s6cb='Juntar coisas para criar algo. Mais amplo do que <em>build</em> — um '
         'bolo faz-se, uma casa constrói-se.',
    s6db='Mover-te sobre os pés, um pé sempre no chão.',

    s7t='Som, direção, cabeça',
    s7ab='Soprar ar entre os lábios e fazer um som agudo e claro.',
    s7bb='Passar a um ponto novo — um tema novo, ou uma direção nova.',
    s7cb='Ter uma opinião ou uma ideia sobre algo.',
    s7db='Já ter a informação na cabeça.',

    s8t='Começar, abandonar, terminar',
    s8ab='Quando algo começa a acontecer.',
    s8bb='Levar uma tarefa ao fim. Completá-la.',
    s8cb='Deixar pessoas que ainda precisam de ti. O verbo é de-<em>SERT</em>; '
         'o <em>DE</em>-sert seco e arenoso é o substantivo.',
    s8db='Algo que acontece, normalmente planeado e importante.',

    s9t='Verdadeiro, falso, mau',
    s9ab='De acordo com os factos.',
    s9bb='Não verdadeiro.',
    s9cb='De má qualidade, ou de nível baixo.',
    s9db='Um homem que não segue as regras — dito muitas vezes com um sorriso.',

    s10t='Sentimentos, e quanto',
    s10ab='Muito aborrecido. Zangado.',
    s10bb='De grande valor ou efeito. Importa.',
    s10cb='Em alto grau. Reforça um adjetivo.',
    s10db='De vez em quando — não sempre.',

    s11t='As quatro palavras mais pequenas',
    s11ab='Usa-o na primeira vez que nomeias algo.',
    s11bb='Dentro de algo, ou rodeado por isso.',
    s11cb='Duas ou mais pessoas ou coisas que já nomeaste.',
    s11db='Um olá informal — e um adeus informal. É italiano, e o inglês '
          'pediu-o emprestado.',

    q1t='O braço dela esticou-se',
    q2t='Foi-se embora sem mais',
    q3t='Uma palavra, sem plural',
    q4t='Todos os dias, ou todos os meses?',

    g1t='Na praça',
    g2t='Não todos os dias',
    gapHint='Escreve uma palavra em cada espaço.',

    matchT='Palavra e significado',
    matchHint='Clica numa palavra e depois no que ela significa.',
    matchWhy='Quatro verbos e um substantivo, todos coisas que se podem ver na '
             'praça.',

    sortT='Uma coisa, ou uma ação?',
    sortHint='Coloca cada palavra na caixa certa.',
    sortWhy='Uma coisa é um substantivo — podes pôr <em>a</em> ou <em>the</em> '
            'à frente. Uma ação é um verbo — podes pôr <em>I</em> à frente.',

    orderT='Constrói a frase',
    orderHint='Clica nas partes pela ordem certa.',
    orderWhy='<em>Sometimes</em> pode abrir a frase. Depois o que fazes, depois '
             'para quê, e por fim quando.',

    searchT='Encontra-o antes de o relógio parar',
    searchStem='Encontra a <em>magnifying glass</em>.',
    searchWhy='Uma <em>magnifying glass</em> é uma lente redonda com cabo. A '
              'moeda também é redonda, mas não tem cabo.',

    resPerfect='Pontuação máxima. Quarenta e quatro palavras, e não escapou '
               'nenhuma.',
    resStrong='Forte. Volta aos dois diapositivos de espaços — é aí que costuma '
              'ir o último ponto.',
    resMid='Boa metade. Lê outra vez os quatro diapositivos de substantivos e '
           'tenta de novo.',
    resLow='Começa do início e lê cada cartão em voz alta antes de responderes. '
           'São palavras que encontras todos os dias.',

    actTitle='Agora usa-as',
    actUse='Usa pelo menos cinco:',
    actSpeakBrief='A pares. Não leias os cartões — di-lo.',
    actSpeak1='Olhem para a imagem da capa. Diz ao teu par cinco coisas que '
              'vês. Diz <em>a</em> na primeira vez e <em>the</em> depois.',
    actSpeak2='O teu par tem uma bolsa. Pergunta o que está lá dentro. Responde '
              'com três palavras de hoje e uma coisa que não seja verdade.',
    actSpeak3='Conta o teu domingo: o que fazes às vezes, o que terminas antes '
              'de segunda-feira, e uma coisa que te deixa zangado.',
    actWriteKind='Escrita · trabalho de casa',
    actWriteBrief='O teu amigo perdeu o evento na praça no sábado. Escreve-lhe '
                  'uma mensagem: o que começou, o que viste, o que fizeste e '
                  'por que tiveste de terminar cedo. 120–150 palavras.',
    actPlaceholder='Ciao! You missed a good day…',
)

# ══════════════════════════════════════════════════════════════════════
#  RUSSIAN
# ══════════════════════════════════════════════════════════════════════
EXTRA['ru'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='Сорок четыре слова, один блочный день',
    chipLevel='A2 · Начальный', chipFocus='Лексика', chipCount='24 слайда',
    bankLabel='Банк слов:',

    e1='Вещи на площади',
    e2='Что делают люди',
    e3='Идеи, чувства, маленькие слова',
    e4='Практика',

    s1t='Внутри здания',
    s1ab='Отверстие в стене со стеклом. Свет входит, а ты смотришь наружу.',
    s1bb='Ты открываешь её, чтобы войти в комнату, здание или машину.',
    s1cb='Комната, где моются.',
    s1db='Небольшой плотный кусок ткани на полу. Ковровое покрытие занимает '
         'весь пол, а <em>rug</em> — нет.',

    s2t='В твоей сумке',
    s2ab='Мягкая ёмкость с отверстием сверху, чтобы носить вещи.',
    s2bb='Маленькая сумка, вшитая в одежду.',
    s2cb='Плоские круглые деньги из металла.',
    s2db='Линза с ручкой. Она делает маленькие вещи большими на вид.',

    s3t='Читать, играть, делать',
    s3ab='Тонкая книжка с множеством картинок. Выходит каждую неделю или каждый '
         'месяц.',
    s3bb='Большие листы бумаги с новостями дня. Выходит каждый день.',
    s3cb='Игры на доске, где двигают фигуры, — например, шахматы.',
    s3db='Школьная работа, которую делаешь дома. Множественного числа нет: '
         'никогда <em>homeworks</em>.',

    s4t='На тебе и на столе',
    s4ab='То, что ты носишь: брюки, платья, куртки. Всегда во множественном '
         'числе.',
    s4bb='Короткие штаны, в которых мужчина плавает. Тоже множественное число.',
    s4cb='Хлеб, подрумяненный и горячий. Говорят <em>a piece of toast</em>, а не '
         '<em>a toast</em>.',
    s4db='Человек, которого ты знаешь и который тебе нравится.',

    s5t='Что делают твои руки',
    s5ab='Двигать что-то от себя.',
    s5bb='Двигать что-то к себе.',
    s5cb='Вытянуть руку, чтобы дотронуться или взять.',
    s5db='С силой ударить рукой или битой по чему-то.',

    s6t='Руки, и куда ты идёшь',
    s6ab='Оставить след на поверхности чем-то острым.',
    s6bb='Соединять части: дом, стену, машину.',
    s6cb='Соединять вещи и создавать что-то. Шире, чем <em>build</em>: торт '
         'делают, а дом строят.',
    s6db='Двигаться на ногах, всегда одной ногой на земле.',

    s7t='Звук, направление, ум',
    s7ab='Продувать воздух через губы и издавать высокий чистый звук.',
    s7bb='Перейти к новому пункту — к новой теме или в новом направлении.',
    s7cb='Иметь мнение или мысль о чём-то.',
    s7db='Уже держать сведения в голове.',

    s8t='Начать, бросить, закончить',
    s8ab='Когда что-то начинает происходить.',
    s8bb='Довести дело до конца. Завершить его.',
    s8cb='Оставить людей, которым ты ещё нужен. Глагол — de-<em>SERT</em>; '
         'сухая песчаная <em>DE</em>-sert — существительное.',
    s8db='То, что происходит, обычно запланированное и важное.',

    s9t='Правда, ложь, плохое',
    s9ab='Соответствующий фактам.',
    s9bb='Не соответствующий правде.',
    s9cb='Плохого качества или низкого уровня.',
    s9db='Мужчина, который не соблюдает правила, — часто говорится с улыбкой.',

    s10t='Чувства, и насколько',
    s10ab='Очень раздражённый. Сердитый.',
    s10bb='Большой ценности или силы. Это имеет значение.',
    s10cb='В высокой степени. Усиливает прилагательное.',
    s10db='Иногда — не всё время.',

    s11t='Четыре самых маленьких слова',
    s11ab='Используй его, когда называешь что-то в первый раз.',
    s11bb='Внутри чего-то или окружённый этим.',
    s11cb='Двое или больше людей или вещей, которых ты уже назвал.',
    s11db='Неформальное «привет» — и неформальное «пока». Слово итальянское, '
          'английский его позаимствовал.',

    q1t='Её рука вытянулась',
    q2t='Он просто ушёл',
    q3t='Одно слово, без множественного числа',
    q4t='Каждый день или каждый месяц?',

    g1t='На площади',
    g2t='Не каждый день',
    gapHint='Впиши по одному слову в каждый пропуск.',

    matchT='Слово и значение',
    matchHint='Нажми на слово, затем на его значение.',
    matchWhy='Четыре глагола и одно существительное — всё это можно увидеть на '
             'площади.',

    sortT='Предмет или действие?',
    sortHint='Помести каждое слово в нужное поле.',
    sortWhy='Предмет — это существительное: перед ним можно поставить '
            '<em>a</em> или <em>the</em>. Действие — это глагол: перед ним '
            'можно поставить <em>I</em>.',

    orderT='Собери предложение',
    orderHint='Нажимай на части в правильном порядке.',
    orderWhy='<em>Sometimes</em> может стоять в начале предложения. Затем то, '
             'что ты делаешь, затем зачем, затем когда.',

    searchT='Найди это, пока идут часы',
    searchStem='Найди <em>magnifying glass</em>.',
    searchWhy='<em>Magnifying glass</em> — круглая линза с ручкой. Монета тоже '
              'круглая, но ручки у неё нет.',

    resPerfect='Полный балл. Сорок четыре слова, и ни одно не проскочило.',
    resStrong='Сильно. Вернись к двум слайдам с пропусками — именно там обычно '
              'теряется последний балл.',
    resMid='Хорошая половина. Перечитай четыре слайда с существительными и '
           'попробуй ещё раз.',
    resLow='Начни сначала и читай каждую карточку вслух перед ответом. Это '
           'слова, которые встречаются каждый день.',

    actTitle='Теперь используй их',
    actUse='Используй хотя бы пять:',
    actSpeakBrief='В парах. Не читай карточки — скажи это.',
    actSpeak1='Посмотрите на картинку на обложке. Назови партнёру пять вещей, '
              'которые видишь. Скажи <em>a</em> в первый раз и <em>the</em> '
              'потом.',
    actSpeak2='У партнёра есть сумка. Спроси, что в ней. Ответь тремя '
              'сегодняшними словами и одной неправдой.',
    actSpeak3='Расскажи про своё воскресенье: что ты иногда делаешь, что '
              'заканчиваешь до понедельника и что тебя злит.',
    actWriteKind='Письмо · домашнее задание',
    actWriteBrief='Твой друг пропустил событие на площади в субботу. Напиши ему '
                  'сообщение: что началось, что ты видел, что делал и почему '
                  'пришлось закончить рано. 120–150 слов.',
    actPlaceholder='Ciao! You missed a good day…',
)

# ══════════════════════════════════════════════════════════════════════
#  ARABIC  (RTL — the engine mirrors the layout)
# ══════════════════════════════════════════════════════════════════════
EXTRA['ar'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='أربع وأربعون كلمة، وعصرٌ من المكعّبات',
    chipLevel='A2 · مبتدئ', chipFocus='المفردات', chipCount='٢٤ شريحة',
    bankLabel='بنك الكلمات:',

    e1='أشياء في الساحة',
    e2='ما يفعله الناس',
    e3='أفكار ومشاعر وكلمات صغيرة',
    e4='تدريب',

    s1t='داخل المبنى',
    s1ab='فتحة في الجدار فيها زجاج. يدخل الضوء منها، وتنظر أنت إلى الخارج.',
    s1bb='تفتحه لتدخل إلى غرفة أو مبنى أو سيارة.',
    s1cb='الغرفة التي تغتسل فيها.',
    s1db='قطعة قماش صغيرة وسميكة على الأرض. الموكيت يغطي الأرض كلها، أما '
         '<em>rug</em> فلا.',

    s2t='في حقيبتك',
    s2ab='وعاء ليّن مفتوح من الأعلى، لحمل الأشياء.',
    s2bb='جيب صغير مخيط في الملابس.',
    s2cb='نقود مسطّحة ومستديرة مصنوعة من المعدن.',
    s2db='عدسة لها مقبض. تجعل الأشياء الصغيرة تبدو كبيرة.',

    s3t='للقراءة واللعب والعمل',
    s3ab='كتيّب رفيع فيه صور كثيرة. يصدر كل أسبوع أو كل شهر.',
    s3bb='أوراق كبيرة فيها أخبار اليوم. تصدر كل يوم.',
    s3cb='ألعاب تُلعب على لوحة بتحريك القطع — الشطرنج مثلاً.',
    s3db='عمل المدرسة الذي تؤدّيه في البيت. لا جمع له: لا تقل أبداً '
         '<em>homeworks</em>.',

    s4t='عليك، وعلى الطاولة',
    s4ab='ما ترتديه: البناطيل والفساتين والسترات. دائماً بصيغة الجمع.',
    s4bb='بنطال قصير يرتديه الرجل للسباحة. جمع أيضاً.',
    s4cb='خبز مُحمَّر وساخن. نقول <em>a piece of toast</em> ولا نقول '
         '<em>a toast</em>.',
    s4db='شخص تعرفه وتحبّه.',

    s5t='ما تفعله يداك',
    s5ab='تحريك شيء بعيداً عنك.',
    s5bb='تحريك شيء نحوك.',
    s5cb='مدّ ذراعك لتلمس شيئاً أو تأخذه.',
    s5db='ضرب شيء بقوة باليد أو بمضرب.',

    s6t='اليدان، وإلى أين تمضي',
    s6ab='ترك أثر على سطح بشيء حادّ.',
    s6bb='ضمّ الأجزاء معاً: بيت أو جدار أو آلة.',
    s6cb='ضمّ الأشياء لصنع شيء ما. أوسع من <em>build</em>: الكعكة تُصنع، '
         'والبيت يُبنى.',
    s6db='التحرّك على القدمين، وقدم واحدة على الأرض دائماً.',

    s7t='صوت واتجاه وذهن',
    s7ab='دفع الهواء بين الشفتين لإصدار صوت حادّ وصافٍ.',
    s7bb='الانتقال إلى نقطة جديدة — موضوع جديد أو اتجاه جديد.',
    s7cb='أن يكون لك رأي أو فكرة عن شيء.',
    s7db='أن تكون المعلومة في رأسك بالفعل.',

    s8t='البدء والترك والإنهاء',
    s8ab='حين يبدأ شيء في الحدوث.',
    s8bb='إيصال العمل إلى نهايته. إتمامه.',
    s8cb='ترك أناس ما زالوا بحاجة إليك. الفعل هو de-<em>SERT</em>، أما '
         '<em>DE</em>-sert الجافة الرملية فهي الاسم.',
    s8db='شيء يحدث، غالباً مُخطَّط له ومهم.',

    s9t='صحيح وخاطئ وسيّئ',
    s9ab='مطابق للوقائع.',
    s9bb='غير صحيح.',
    s9cb='رديء النوعية أو منخفض المستوى.',
    s9db='رجل لا يلتزم بالقواعد — وتُقال غالباً بابتسامة.',

    s10t='المشاعر، وإلى أي حدّ',
    s10ab='منزعج جداً. غاضب.',
    s10bb='ذو قيمة أو أثر كبير. له وزن.',
    s10cb='إلى درجة عالية. يقوّي الصفة.',
    s10db='أحياناً — لا طوال الوقت.',

    s11t='أصغر أربع كلمات',
    s11ab='استعملها أول مرة تسمّي فيها شيئاً.',
    s11bb='داخل شيء أو محاط به.',
    s11cb='شخصان أو شيئان فأكثر سبق أن ذكرتهما.',
    s11db='تحية غير رسمية — ووداع غير رسمي. أصلها إيطالي، والإنجليزية '
          'استعارتها.',

    q1t='امتدّت ذراعها',
    q2t='مضى ولم يعد',
    q3t='كلمة واحدة، بلا جمع',
    q4t='كل يوم أم كل شهر؟',

    g1t='في الساحة',
    g2t='ليس كل يوم',
    gapHint='اكتب كلمة واحدة في كل فراغ.',

    matchT='الكلمة والمعنى',
    matchHint='انقر على كلمة ثم على معناها.',
    matchWhy='أربعة أفعال واسم واحد، وكلها أشياء يمكن رؤيتها في الساحة.',

    sortT='شيء أم فعل؟',
    sortHint='ضع كل كلمة في الصندوق الصحيح.',
    sortWhy='الشيء اسم — يمكن وضع <em>a</em> أو <em>the</em> قبله. والفعل يمكن '
            'وضع <em>I</em> قبله.',

    orderT='ابنِ الجملة',
    orderHint='انقر على الأجزاء بالترتيب الصحيح.',
    orderWhy='يمكن أن تبدأ الجملة بـ<em>Sometimes</em>. ثم ما تفعله، ثم لماذا، '
             'ثم متى.',

    searchT='جِدْه قبل أن تتوقف الساعة',
    searchStem='جِد الـ<em>magnifying glass</em>.',
    searchWhy='الـ<em>magnifying glass</em> عدسة مستديرة لها مقبض. والعملة '
              'مستديرة أيضاً لكن بلا مقبض.',

    resPerfect='علامة كاملة. أربع وأربعون كلمة، ولم تفلت منك واحدة.',
    resStrong='قوي. ارجع إلى شريحتَي الفراغات — هناك تضيع النقطة الأخيرة عادةً.',
    resMid='نصف جيّد. أعد قراءة شرائح الأسماء الأربع ثم حاول مرة أخرى.',
    resLow='ابدأ من البداية واقرأ كل بطاقة بصوت عالٍ قبل أن تجيب. هذه كلمات '
           'تصادفها كل يوم.',

    actTitle='الآن استعملها',
    actUse='استعمل خمساً على الأقل:',
    actSpeakBrief='في ثنائيات. لا تقرأ البطاقات — قُلها.',
    actSpeak1='انظرا إلى صورة الغلاف. اذكر لزميلك خمسة أشياء تراها. قل '
              '<em>a</em> في المرة الأولى و<em>the</em> بعد ذلك.',
    actSpeak2='مع زميلك حقيبة. اسأله عمّا فيها. أجب بثلاث كلمات من درس اليوم '
              'وبشيء واحد غير صحيح.',
    actSpeak3='احكِ عن يوم أحدك: ما تفعله أحياناً، وما تنهيه قبل الاثنين، وشيء '
              'واحد يغضبك.',
    actWriteKind='كتابة · واجب منزلي',
    actWriteBrief='فاتَ صديقك الحدث في الساحة يوم السبت. اكتب له رسالة: ما الذي '
                  'بدأ، وما الذي رأيته، وما الذي فعلته، ولماذا اضطررت إلى '
                  'الإنهاء مبكراً. ١٢٠–١٥٠ كلمة.',
    actPlaceholder='Ciao! You missed a good day…',
)

# ══════════════════════════════════════════════════════════════════════
#  CHINESE
# ══════════════════════════════════════════════════════════════════════
EXTRA['zh'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='四十四个词，一个方块午后',
    chipLevel='A2 · 初级', chipFocus='词汇', chipCount='24 张幻灯片',
    bankLabel='词库：',

    e1='广场上的东西',
    e2='人们做的事',
    e3='想法、情绪和小词',
    e4='练习',

    s1t='在建筑物里',
    s1ab='墙上的开口，装着玻璃。光线进来，你往外看。',
    s1bb='你把它打开，进入房间、建筑物或汽车。',
    s1cb='洗澡洗漱的房间。',
    s1db='铺在地上的一小块厚布。地毯铺满整个地面，<em>rug</em> 不会。',

    s2t='在你的包里',
    s2ab='上面开口的软容器，用来装东西。',
    s2bb='缝在衣服上的小口袋。',
    s2cb='金属做的、扁平的圆形钱币。',
    s2db='带柄的镜片，让小东西看起来变大。',

    s3t='读的、玩的、做的',
    s3ab='图片很多的薄册子，每周或每月出一期。',
    s3bb='印着当天新闻的大张纸，每天出一份。',
    s3cb='在棋盘上移动棋子来玩的游戏，比如国际象棋。',
    s3db='在家里做的学校功课。没有复数：绝不能说 <em>homeworks</em>。',

    s4t='穿在身上，摆在桌上',
    s4ab='你穿的东西：裤子、裙子、外套。永远用复数。',
    s4bb='男人游泳时穿的短裤，也是复数。',
    s4cb='烤得又热又黄的面包。要说 <em>a piece of toast</em>，不能说 '
         '<em>a toast</em>。',
    s4db='你认识而且喜欢的人。',

    s5t='你的手做的事',
    s5ab='把东西朝离开自己的方向移动。',
    s5bb='把东西朝自己的方向移动。',
    s5cb='伸出手臂去碰或去拿东西。',
    s5db='用手或球棒用力打在某物上。',

    s6t='手，以及你去哪里',
    s6ab='用尖的东西在表面上留下痕迹。',
    s6bb='把零件组合起来：房子、墙、机器。',
    s6cb='把东西组合起来创造出某物。比 <em>build</em> 更宽：蛋糕是 make，'
         '房子是 build。',
    s6db='用脚移动，总有一只脚在地上。',

    s7t='声音、方向、头脑',
    s7ab='让气从嘴唇之间出来，发出又高又清的声音。',
    s7bb='转到新的一点——新的话题，或新的方向。',
    s7cb='对某事有看法或想法。',
    s7db='脑子里已经有这个信息。',

    s8t='开始、抛下、结束',
    s8ab='某件事开始发生的时候。',
    s8bb='把一件事做到底，把它完成。',
    s8cb='在别人还需要你的时候离开他们。动词读作 de-<em>SERT</em>；干燥多沙的 '
         '<em>DE</em>-sert 是名词。',
    s8db='发生的事，通常是计划好的、重要的。',

    s9t='真、假、坏',
    s9ab='与事实相符。',
    s9bb='不是真的。',
    s9cb='质量差，或水平低。',
    s9db='不守规矩的男人——常常是带着笑意说的。',

    s10t='情绪，以及程度',
    s10ab='非常恼火。生气。',
    s10bb='价值大或影响大。要紧。',
    s10cb='程度很高，用来加强形容词。',
    s10db='偶尔——不是一直。',

    s11t='最小的四个词',
    s11ab='第一次提到某样东西时用它。',
    s11bb='在某物里面，或被它围着。',
    s11cb='你已经提过的两个或更多的人或物。',
    s11db='随意的问候，也是随意的告别。它来自意大利语，英语借了过来。',

    q1t='她伸出了手臂',
    q2t='他走了，再没回来',
    q3t='一个词，没有复数',
    q4t='每天，还是每月？',

    g1t='在广场上',
    g2t='不是每天',
    gapHint='在每个空格里填一个词。',

    matchT='词与词义',
    matchHint='先点一个词，再点它的意思。',
    matchWhy='四个动词和一个名词，都是广场上看得见的东西。',

    sortT='是东西，还是动作？',
    sortHint='把每个词放进正确的框里。',
    sortWhy='东西是名词——前面可以放 <em>a</em> 或 <em>the</em>。动作是动词'
            '——前面可以放 <em>I</em>。',

    orderT='把句子拼起来',
    orderHint='按正确的顺序点击各部分。',
    orderWhy='<em>Sometimes</em> 可以放在句首。然后是你做什么，再是为什么，'
             '最后是什么时候。',

    searchT='在计时结束前找到它',
    searchStem='找出 <em>magnifying glass</em>。',
    searchWhy='<em>magnifying glass</em> 是带柄的圆形镜片。硬币也是圆的，'
              '但没有柄。',

    resPerfect='满分。四十四个词，一个也没漏。',
    resStrong='不错。回到那两张填空幻灯片——最后一分通常丢在那里。',
    resMid='对了一半。把四张名词幻灯片再读一遍，然后再试一次。',
    resLow='从头开始，回答之前把每张卡片大声读出来。这些都是每天都会遇到的词。',

    actTitle='现在用起来',
    actUse='至少用五个：',
    actSpeakBrief='两人一组。别照着卡片念——说出来。',
    actSpeak1='看封面的图。告诉同伴你看到的五样东西。第一次说 <em>a</em>，'
              '之后说 <em>the</em>。',
    actSpeak2='同伴有一个包。问问里面有什么。用今天的三个词回答，再加一件'
              '不是真的事。',
    actSpeak3='说说你的星期天：你有时候做什么，星期一之前要完成什么，'
              '还有一件让你生气的事。',
    actWriteKind='写作 · 作业',
    actWriteBrief='你的朋友错过了星期六广场上的活动。写条消息给他：什么开始了，'
                  '你看到了什么，你做了什么，以及为什么你得早点结束。120–150 词。',
    actPlaceholder='Ciao! You missed a good day…',
)

# ══════════════════════════════════════════════════════════════════════
#  JAPANESE
# ══════════════════════════════════════════════════════════════════════
EXTRA['ja'] = dict(
    coverTitle='The <em>Square</em>',
    coverSub='四十四の単語、ブロックの午後',
    chipLevel='A2 · 初級', chipFocus='語彙', chipCount='24 スライド',
    bankLabel='単語バンク：',

    e1='広場にあるもの',
    e2='人がすること',
    e3='考え、気持ち、小さな語',
    e4='練習',

    s1t='建物の中で',
    s1ab='壁にあるガラス入りの開口部。光が入り、外が見えます。',
    s1bb='部屋や建物や車に入るために開けるもの。',
    s1cb='体を洗う部屋。',
    s1db='床に置く小さくて厚い布。カーペットは床全体を覆いますが、'
         '<em>rug</em> は覆いません。',

    s2t='かばんの中に',
    s2ab='上が開いた柔らかい入れ物。ものを運ぶために使います。',
    s2bb='服に縫いつけられた小さな袋。',
    s2cb='金属でできた、平たくて丸いお金。',
    s2db='柄のついたレンズ。小さいものを大きく見せます。',

    s3t='読む、遊ぶ、やる',
    s3ab='写真の多い薄い冊子。毎週または毎月出ます。',
    s3bb='その日のニュースが載った大きな紙。毎日出ます。',
    s3cb='盤の上で駒を動かして遊ぶゲーム。たとえばチェス。',
    s3db='家でやる学校の課題。複数形はありません。<em>homeworks</em> とは'
         '言いません。',

    s4t='身につけるもの、机の上のもの',
    s4ab='着るもの。ズボン、ワンピース、上着など。いつも複数形です。',
    s4bb='男性が泳ぐときにはく短いズボン。これも複数形です。',
    s4cb='こんがり焼いた熱いパン。<em>a piece of toast</em> と言い、'
         '<em>a toast</em> とは言いません。',
    s4db='知っていて、好きだと思う人。',

    s5t='手ですること',
    s5ab='ものを自分から遠ざけるように動かす。',
    s5bb='ものを自分のほうへ動かす。',
    s5cb='腕をのばして、さわったり取ったりする。',
    s5db='手やバットを強く何かに当てる。',

    s6t='手と、行き先',
    s6ab='とがったもので表面に跡をつける。',
    s6bb='部品を組み合わせる。家、壁、機械など。',
    s6cb='ものを組み合わせて何かを作る。<em>build</em> より広く、ケーキは '
         'make、家は build です。',
    s6db='足で移動する。いつもどちらかの足が地面についています。',

    s7t='音、方向、頭の中',
    s7ab='くちびるの間から息を出して、高く澄んだ音を出す。',
    s7bb='新しい点へ移る。新しい話題、または新しい方向へ。',
    s7cb='何かについて意見や考えを持つ。',
    s7db='その情報をすでに頭に持っている。',

    s8t='始める、見捨てる、終える',
    s8ab='何かが起こり始めるとき。',
    s8bb='仕事を最後までやる。完成させる。',
    s8cb='まだ自分を必要としている人を置き去りにする。動詞は de-<em>SERT</em>、'
         '乾いた砂の <em>DE</em>-sert は名詞です。',
    s8db='起こること。ふつうは計画された、大事なこと。',

    s9t='本当、うそ、悪い',
    s9ab='事実と合っていること。',
    s9bb='本当ではないこと。',
    s9cb='質が悪い、水準が低い。',
    s9db='ルールを守らない男性。多くは笑いを含んで言います。',

    s10t='気持ちと、どのくらい',
    s10ab='とてもいらだっている。怒っている。',
    s10bb='価値や影響が大きい。大事である。',
    s10cb='程度が高い。形容詞を強めます。',
    s10db='ときどき。いつもではありません。',

    s11t='いちばん小さい四つの語',
    s11ab='何かを初めて言うときに使います。',
    s11bb='何かの中に、または何かに囲まれて。',
    s11cb='すでに名前を出した二人以上の人、二つ以上のもの。',
    s11db='くだけた「こんにちは」であり、くだけた「さようなら」。'
          'イタリア語で、英語が借りて使っています。',

    q1t='彼女の腕がのびた',
    q2t='彼は去ったきりだった',
    q3t='一つの語、複数形なし',
    q4t='毎日か、毎月か',

    g1t='広場で',
    g2t='毎日ではない',
    gapHint='それぞれの空欄に語を一つ書いてください。',

    matchT='語と意味',
    matchHint='語をクリックしてから、その意味をクリックします。',
    matchWhy='動詞が四つと名詞が一つ。どれも広場で見られるものです。',

    sortT='もの、それとも動作？',
    sortHint='それぞれの語を正しい箱に入れてください。',
    sortWhy='ものは名詞で、前に <em>a</em> や <em>the</em> を置けます。'
            '動作は動詞で、前に <em>I</em> を置けます。',

    orderT='文を組み立てる',
    orderHint='正しい順番で各部分をクリックしてください。',
    orderWhy='<em>Sometimes</em> は文頭に置けます。次に何をするか、次になぜ、'
             '最後にいつ、の順です。',

    searchT='時間切れになる前に見つけて',
    searchStem='<em>magnifying glass</em> を見つけてください。',
    searchWhy='<em>magnifying glass</em> は柄のついた丸いレンズです。'
              'コインも丸いですが、柄がありません。',

    resPerfect='満点。四十四語、ひとつも取りこぼしなし。',
    resStrong='good。空欄補充の二枚に戻ってみてください。最後の一点はたいてい'
              'そこで落ちます。',
    resMid='半分は取れています。名詞の四枚をもう一度読んで、再挑戦を。',
    resLow='最初からやり直し、答える前に各カードを声に出して読んでください。'
           '毎日出会う語ばかりです。',

    actTitle='さあ使ってみよう',
    actUse='少なくとも五つ使うこと：',
    actSpeakBrief='ペアで。カードを読まずに、口に出して。',
    actSpeak1='表紙の絵を見てください。見えるものを五つ相手に言います。'
              '最初は <em>a</em>、そのあとは <em>the</em> を使って。',
    actSpeak2='相手はかばんを持っています。中に何があるか聞いてください。'
              '今日の語を三つ使い、ひとつだけ本当ではないことを混ぜて答えます。',
    actSpeak3='日曜日のことを話してください。ときどきすること、月曜までに'
              '終えること、そして腹が立つことを一つ。',
    actWriteKind='ライティング · 宿題',
    actWriteBrief='友だちは土曜日の広場のイベントに来られませんでした。'
                  'メッセージを書いてください。何が始まり、何を見て、何をして、'
                  'なぜ早く切り上げたのか。120〜150語。',
    actPlaceholder='Ciao! You missed a good day…',
)

# The ledger chrome the template's markup always reads, per language.
TAIL_EXTRA = {
    'fr': {'ledClues': "'Indices'", 'ledDp': "'DP'", 'ledTime': "'Temps'"},
    'it': {'ledClues': "'Indizi'", 'ledDp': "'DP'", 'ledTime': "'Tempo'"},
    'pt': {'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tempo'"},
    'ru': {'ledClues': "'Улики'", 'ledDp': "'DP'", 'ledTime': "'Время'"},
    'ar': {'ledClues': "'أدلة'", 'ledDp': "'DP'", 'ledTime': "'الوقت'"},
    'zh': {'ledClues': "'线索'", 'ledDp': "'DP'", 'ledTime': "'时间'"},
    'ja': {'ledClues': "'手がかり'", 'ledDp': "'DP'", 'ledTime': "'時間'"},
}
