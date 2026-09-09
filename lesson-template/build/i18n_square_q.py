# -*- coding: utf-8 -*-
"""The Square — the question side, in all ten languages.

Split from the other two string modules because it is a different decision,
not just more of the same. Innes, 2026-09-09, looking at the first multiple
choice: *"They are not translated e.g. She put her arm out to take the coin
from the table. She ____ for it. Nothing has been translated."*

**Where the line now falls.** The sentence carrying the blank stays English;
everything around it translates. So this item ships as:

    ctx   (translated)  Sie streckte den Arm aus, um die Münze vom Tisch
                        zu nehmen.
    stem  (English)     She ____ for it.
    opts  (English)     reached / scratched / whistled / deserted
    why   (translated)  Richtig. *Reach* heißt, den Arm nach etwas …

The learner reads the situation in their own language and completes an
English sentence out of English options, which is the exercise. Translating
the stem too would make it a translation drill and would leave the options
answering a German sentence.

That is a narrowing of HOUSE-STYLE §8, not a break with it: §8's list of what
stays English was written for grammar decks, where the stem *is* the item.
At A2 the situation is scaffolding, and a learner who cannot parse it cannot
reach the item at all.

**What is still English on purpose, in all ten:** the options, the gap
answers and their word bank, the sort chips, the sentence-build chunks, the
search object names, and the headwords and example sentences on the teach
cards. Each of those is the vocabulary itself. `searchStem` translates its
instruction and keeps its noun — *Finde die magnifying glass.*

`M_DEFS` is the match slide. Its English definition is the button text; the
nine translations ride along as `data-def-<lang>` and the engine shows only
the one matching the current language. The *term* side is never glossed —
printing "whistle / pfeifen" next to "scratch / kratzen" turns matching into
reading off.
"""

Q = {}

# ══════════════════════════════════════════════════════════════════════
#  ENGLISH
# ══════════════════════════════════════════════════════════════════════
Q['en'] = dict(
    sortBinA='A thing', sortBinB='An action',
    q1c='She put her arm out to take the coin from the table.',
    q1x='<em>Reach</em> is putting your arm out towards something. '
        '<em>Scratch</em> marks a surface, <em>whistle</em> makes a sound, and '
        '<em>desert</em> means to leave someone behind.',
    q2c='His friends still needed him, but he walked away and never came back.',
    q2x='To <em>desert</em> people is to leave them when they still need you. '
        'Watch the stress: de-<em>SERT</em> is this verb; <em>DE</em>-sert is '
        'the dry, sandy place.',
    q3s='Which sentence is correct English?',
    q3x='<em>Homework</em> has no plural, so <em>homeworks</em> does not exist '
        'and <em>many</em> and <em>two</em> cannot go in front of it. Use '
        '<em>a lot of</em> or <em>much</em>.',
    q4c="It comes out every day, on big sheets of paper, and it is full of "
        "today's news.",
    q4x='A <em>newspaper</em> is daily news on big sheets. A <em>magazine</em> '
        'is thinner, has far more pictures, and comes out every week or every '
        'month.',

    g1h='One word in each space. The sentences stay in English — the words you '
        'need are in the bank above.',
    g1x1='<em>Push</em> is away from you; <em>pull</em> is towards you. The '
         'sign tells you which one.',
    g1x2='A <em>pocket</em> is sewn into your clothes. A <em>bag</em> is a '
         'separate container you carry.',
    g1x3='A <em>magnifying glass</em> is a lens with a handle that makes small '
         'things look big.',
    g2h='One word in each space. Two of these are among the smallest words in '
        'the lesson.',
    g2x1='<em>Sometimes</em> means occasionally — some days yes, some days no.',
    g2x2='<em>They</em> stands for two or more people you have already named.',
    g2x3='<em>True</em> agrees with the facts; <em>false</em> does not.',
)

# ══════════════════════════════════════════════════════════════════════
#  GERMAN
# ══════════════════════════════════════════════════════════════════════
Q['de'] = dict(
    sortBinA='Ein Ding', sortBinB='Eine Handlung',
    q1c='Sie streckte den Arm aus, um die Münze vom Tisch zu nehmen.',
    q1x='<em>Reach</em> heißt, den Arm nach etwas ausstrecken. '
        '<em>Scratch</em> hinterlässt eine Spur, <em>whistle</em> macht ein '
        'Geräusch, und <em>desert</em> heißt, jemanden im Stich zu lassen.',
    q2c='Seine Freunde brauchten ihn noch, aber er ging weg und kam nie zurück.',
    q2x='<em>Desert</em> heißt, Menschen zu verlassen, die dich noch brauchen. '
        'Achte auf die Betonung: de-<em>SERT</em> ist dieses Verb, '
        '<em>DE</em>-sert ist die trockene Sandwüste.',
    q3s='Welcher Satz ist korrektes Englisch?',
    q3x='<em>Homework</em> hat keinen Plural: <em>homeworks</em> gibt es nicht, '
        'und <em>many</em> oder <em>two</em> können nicht davorstehen. Nimm '
        '<em>a lot of</em> oder <em>much</em>.',
    q4c='Es erscheint jeden Tag, auf großen Papierbögen, und ist voll mit den '
        'Nachrichten von heute.',
    q4x='Ein <em>newspaper</em> bringt täglich Nachrichten auf großen Bögen. '
        'Ein <em>magazine</em> ist dünner, hat viel mehr Bilder und erscheint '
        'wöchentlich oder monatlich.',

    g1h='Ein Wort pro Lücke. Die Sätze bleiben auf Englisch — die passenden '
        'Wörter stehen oben im Wortspeicher.',
    g1x1='<em>Push</em> ist von dir weg, <em>pull</em> ist zu dir hin. Das '
         'Schild sagt dir, welches gilt.',
    g1x2='Ein <em>pocket</em> ist in die Kleidung eingenäht. Eine <em>bag</em> '
         'ist ein eigener Behälter, den du trägst.',
    g1x3='Eine <em>magnifying glass</em> ist eine Linse mit Griff, die kleine '
         'Dinge groß erscheinen lässt.',
    g2h='Ein Wort pro Lücke. Zwei davon gehören zu den kleinsten Wörtern der '
        'Lektion.',
    g2x1='<em>Sometimes</em> heißt gelegentlich — an manchen Tagen ja, an '
         'anderen nicht.',
    g2x2='<em>They</em> steht für zwei oder mehr Personen, die du schon genannt '
         'hast.',
    g2x3='<em>True</em> stimmt mit den Tatsachen überein, <em>false</em> nicht.',
)

# ══════════════════════════════════════════════════════════════════════
#  SPANISH
# ══════════════════════════════════════════════════════════════════════
Q['es'] = dict(
    sortBinA='Una cosa', sortBinB='Una acción',
    q1c='Estiró el brazo para coger la moneda de la mesa.',
    q1x='<em>Reach</em> es estirar el brazo hacia algo. <em>Scratch</em> deja '
        'una marca, <em>whistle</em> hace un sonido, y <em>desert</em> '
        'significa abandonar a alguien.',
    q2c='Sus amigos todavía lo necesitaban, pero se marchó y no volvió nunca.',
    q2x='<em>Desert</em> es dejar a gente que todavía te necesita. Fíjate en el '
        'acento: de-<em>SERT</em> es este verbo; <em>DE</em>-sert es el lugar '
        'seco y arenoso.',
    q3s='¿Qué frase es inglés correcto?',
    q3x='<em>Homework</em> no tiene plural: <em>homeworks</em> no existe, y '
        '<em>many</em> o <em>two</em> no pueden ir delante. Usa <em>a lot '
        'of</em> o <em>much</em>.',
    q4c='Sale todos los días, en hojas grandes de papel, y está lleno de las '
        'noticias de hoy.',
    q4x='Un <em>newspaper</em> trae noticias diarias en hojas grandes. Una '
        '<em>magazine</em> es más fina, tiene muchas más fotos y sale cada '
        'semana o cada mes.',

    g1h='Una palabra por hueco. Las frases siguen en inglés — las palabras que '
        'necesitas están arriba, en el banco.',
    g1x1='<em>Push</em> es lejos de ti; <em>pull</em> es hacia ti. El cartel te '
         'dice cuál.',
    g1x2='Un <em>pocket</em> va cosido a la ropa. Una <em>bag</em> es un '
         'recipiente aparte que llevas contigo.',
    g1x3='Una <em>magnifying glass</em> es una lente con mango que hace que las '
         'cosas pequeñas se vean grandes.',
    g2h='Una palabra por hueco. Dos de ellas están entre las palabras más '
        'pequeñas de la lección.',
    g2x1='<em>Sometimes</em> significa de vez en cuando — unos días sí y otros '
         'no.',
    g2x2='<em>They</em> sustituye a dos o más personas que ya has nombrado.',
    g2x3='<em>True</em> concuerda con los hechos; <em>false</em> no.',
)

# ══════════════════════════════════════════════════════════════════════
#  FRENCH
# ══════════════════════════════════════════════════════════════════════
Q['fr'] = dict(
    sortBinA='Une chose', sortBinB='Une action',
    q1c='Elle a tendu le bras pour prendre la pièce sur la table.',
    q1x='<em>Reach</em>, c’est tendre le bras vers quelque chose. '
        '<em>Scratch</em> laisse une marque, <em>whistle</em> fait un son, et '
        '<em>desert</em> veut dire abandonner quelqu’un.',
    q2c='Ses amis avaient encore besoin de lui, mais il est parti et n’est '
        'jamais revenu.',
    q2x='<em>Desert</em>, c’est quitter des gens qui ont encore besoin de toi. '
        'Attention à l’accent : de-<em>SERT</em> est ce verbe ; '
        '<em>DE</em>-sert est le lieu sec et sablonneux.',
    q3s='Quelle phrase est de l’anglais correct ?',
    q3x='<em>Homework</em> n’a pas de pluriel : <em>homeworks</em> n’existe '
        'pas, et <em>many</em> ou <em>two</em> ne peuvent pas le précéder. '
        'Utilise <em>a lot of</em> ou <em>much</em>.',
    q4c='Il paraît chaque jour, sur de grandes feuilles de papier, et il est '
        'plein des nouvelles du jour.',
    q4x='Un <em>newspaper</em> donne les nouvelles du jour sur de grandes '
        'feuilles. Un <em>magazine</em> est plus fin, a beaucoup plus '
        'd’images, et paraît chaque semaine ou chaque mois.',

    g1h='Un mot par espace. Les phrases restent en anglais — les mots dont tu '
        'as besoin sont dans la banque ci-dessus.',
    g1x1='<em>Push</em>, c’est loin de toi ; <em>pull</em>, c’est vers toi. Le '
         'panneau te dit lequel.',
    g1x2='Un <em>pocket</em> est cousu dans les vêtements. Un <em>bag</em> est '
         'un contenant séparé que tu portes.',
    g1x3='Une <em>magnifying glass</em> est une lentille avec un manche qui '
         'fait paraître grandes les petites choses.',
    g2h='Un mot par espace. Deux d’entre eux comptent parmi les plus petits '
        'mots de la leçon.',
    g2x1='<em>Sometimes</em> veut dire de temps en temps — certains jours oui, '
         'd’autres non.',
    g2x2='<em>They</em> remplace deux personnes ou plus que tu as déjà nommées.',
    g2x3='<em>True</em> est conforme aux faits ; <em>false</em> ne l’est pas.',
)

# ══════════════════════════════════════════════════════════════════════
#  ITALIAN
# ══════════════════════════════════════════════════════════════════════
Q['it'] = dict(
    sortBinA='Una cosa', sortBinB="Un'azione",
    q1c='Ha allungato il braccio per prendere la moneta dal tavolo.',
    q1x='<em>Reach</em> vuol dire allungare il braccio verso qualcosa. '
        '<em>Scratch</em> lascia un segno, <em>whistle</em> fa un suono, e '
        '<em>desert</em> vuol dire abbandonare qualcuno.',
    q2c='I suoi amici avevano ancora bisogno di lui, ma se n’è andato e non è '
        'più tornato.',
    q2x='<em>Desert</em> vuol dire lasciare persone che hanno ancora bisogno '
        'di te. Attenzione all’accento: de-<em>SERT</em> è questo verbo; '
        '<em>DE</em>-sert è il luogo secco e sabbioso.',
    q3s='Quale frase è inglese corretto?',
    q3x='<em>Homework</em> non ha plurale: <em>homeworks</em> non esiste, e '
        '<em>many</em> o <em>two</em> non possono precederlo. Usa <em>a lot '
        'of</em> o <em>much</em>.',
    q4c='Esce ogni giorno, su grandi fogli di carta, ed è pieno delle notizie '
        'di oggi.',
    q4x='Un <em>newspaper</em> porta le notizie del giorno su grandi fogli. Una '
        '<em>magazine</em> è più sottile, ha molte più immagini ed esce ogni '
        'settimana o ogni mese.',

    g1h='Una parola per spazio. Le frasi restano in inglese — le parole che ti '
        'servono sono nella banca qui sopra.',
    g1x1='<em>Push</em> è lontano da te; <em>pull</em> è verso di te. Il '
         'cartello ti dice quale.',
    g1x2='Un <em>pocket</em> è cucito nei vestiti. Una <em>bag</em> è un '
         'contenitore a parte che porti con te.',
    g1x3='Una <em>magnifying glass</em> è una lente con un manico che fa '
         'sembrare grandi le cose piccole.',
    g2h='Una parola per spazio. Due di queste sono fra le parole più piccole '
        'della lezione.',
    g2x1='<em>Sometimes</em> vuol dire ogni tanto — certi giorni sì, certi no.',
    g2x2='<em>They</em> sta per due o più persone che hai già nominato.',
    g2x3='<em>True</em> è in accordo con i fatti; <em>false</em> no.',
)

# ══════════════════════════════════════════════════════════════════════
#  PORTUGUESE
# ══════════════════════════════════════════════════════════════════════
Q['pt'] = dict(
    sortBinA='Uma coisa', sortBinB='Uma ação',
    q1c='Ela esticou o braço para apanhar a moeda em cima da mesa.',
    q1x='<em>Reach</em> é esticar o braço na direção de algo. <em>Scratch</em> '
        'deixa uma marca, <em>whistle</em> faz um som, e <em>desert</em> quer '
        'dizer abandonar alguém.',
    q2c='Os amigos ainda precisavam dele, mas ele foi-se embora e nunca mais '
        'voltou.',
    q2x='<em>Desert</em> é deixar pessoas que ainda precisam de ti. Repara na '
        'sílaba forte: de-<em>SERT</em> é este verbo; <em>DE</em>-sert é o '
        'lugar seco e arenoso.',
    q3s='Que frase está em inglês correto?',
    q3x='<em>Homework</em> não tem plural: <em>homeworks</em> não existe, e '
        '<em>many</em> ou <em>two</em> não podem vir à frente. Usa <em>a lot '
        'of</em> ou <em>much</em>.',
    q4c='Sai todos os dias, em folhas grandes de papel, e está cheio das '
        'notícias de hoje.',
    q4x='Um <em>newspaper</em> traz as notícias do dia em folhas grandes. Uma '
        '<em>magazine</em> é mais fina, tem muito mais imagens e sai todas as '
        'semanas ou todos os meses.',

    g1h='Uma palavra por espaço. As frases ficam em inglês — as palavras de que '
        'precisas estão no banco acima.',
    g1x1='<em>Push</em> é para longe de ti; <em>pull</em> é na tua direção. A '
         'placa diz-te qual é.',
    g1x2='Um <em>pocket</em> é cosido na roupa. Uma <em>bag</em> é um '
         'recipiente à parte que levas contigo.',
    g1x3='Uma <em>magnifying glass</em> é uma lente com cabo que faz as coisas '
         'pequenas parecerem grandes.',
    g2h='Uma palavra por espaço. Duas delas estão entre as palavras mais '
        'pequenas da lição.',
    g2x1='<em>Sometimes</em> quer dizer de vez em quando — uns dias sim, outros '
         'não.',
    g2x2='<em>They</em> substitui duas ou mais pessoas que já nomeaste.',
    g2x3='<em>True</em> está de acordo com os factos; <em>false</em> não está.',
)

# ══════════════════════════════════════════════════════════════════════
#  RUSSIAN
# ══════════════════════════════════════════════════════════════════════
Q['ru'] = dict(
    sortBinA='Предмет', sortBinB='Действие',
    q1c='Она вытянула руку, чтобы взять монету со стола.',
    q1x='<em>Reach</em> — это вытянуть руку к чему-то. <em>Scratch</em> '
        'оставляет след, <em>whistle</em> издаёт звук, а <em>desert</em> '
        'значит бросить кого-то.',
    q2c='Друзья всё ещё нуждались в нём, но он ушёл и больше не вернулся.',
    q2x='<em>Desert</em> — оставить людей, которым ты ещё нужен. Обрати '
        'внимание на ударение: de-<em>SERT</em> — это глагол, а '
        '<em>DE</em>-sert — сухая песчаная пустыня.',
    q3s='Какое предложение — правильный английский?',
    q3x='У <em>homework</em> нет множественного числа: <em>homeworks</em> не '
        'существует, и <em>many</em> или <em>two</em> перед ним не ставятся. '
        'Используй <em>a lot of</em> или <em>much</em>.',
    q4c='Выходит каждый день, на больших листах бумаги, и полон сегодняшних '
        'новостей.',
    q4x='<em>Newspaper</em> — ежедневные новости на больших листах. '
        '<em>Magazine</em> тоньше, картинок в нём гораздо больше, и выходит он '
        'раз в неделю или раз в месяц.',

    g1h='По одному слову в каждый пропуск. Предложения остаются на английском — '
        'нужные слова в банке выше.',
    g1x1='<em>Push</em> — от себя, <em>pull</em> — к себе. Табличка говорит, '
         'какое из двух.',
    g1x2='<em>Pocket</em> вшит в одежду. <em>Bag</em> — отдельная ёмкость, '
         'которую носят с собой.',
    g1x3='<em>Magnifying glass</em> — линза с ручкой, которая делает мелкое '
         'крупным на вид.',
    g2h='По одному слову в каждый пропуск. Два из них — среди самых маленьких '
        'слов урока.',
    g2x1='<em>Sometimes</em> значит иногда — в какие-то дни да, в какие-то нет.',
    g2x2='<em>They</em> заменяет двух или более людей, которых ты уже назвал.',
    g2x3='<em>True</em> совпадает с фактами, <em>false</em> — нет.',
)

# ══════════════════════════════════════════════════════════════════════
#  ARABIC
# ══════════════════════════════════════════════════════════════════════
Q['ar'] = dict(
    sortBinA='شيء', sortBinB='فعل',
    q1c='مدّت ذراعها لتأخذ العملة من على الطاولة.',
    q1x='<em>Reach</em> تعني مدّ الذراع نحو شيء. و<em>scratch</em> تترك أثراً، '
        'و<em>whistle</em> تُصدر صوتاً، و<em>desert</em> تعني التخلّي عن أحد.',
    q2c='كان أصدقاؤه ما زالوا بحاجة إليه، لكنه مضى ولم يعد أبداً.',
    q2x='<em>Desert</em> هي ترك أناس ما زالوا بحاجة إليك. انتبه إلى النبر: '
        'de-<em>SERT</em> هو هذا الفعل، أما <em>DE</em>-sert فهي الصحراء '
        'الجافة الرملية.',
    q3s='أي جملة إنجليزية صحيحة؟',
    q3x='<em>Homework</em> لا جمع لها: <em>homeworks</em> غير موجودة، ولا يصح '
        'وضع <em>many</em> أو <em>two</em> قبلها. استعمل <em>a lot of</em> أو '
        '<em>much</em>.',
    q4c='يصدر كل يوم على أوراق كبيرة، وهو مليء بأخبار اليوم.',
    q4x='الـ<em>newspaper</em> أخبار يومية على أوراق كبيرة. أما '
        'الـ<em>magazine</em> فأرقّ، وصورها أكثر بكثير، وتصدر كل أسبوع أو كل '
        'شهر.',

    g1h='كلمة واحدة في كل فراغ. الجمل تبقى بالإنجليزية — والكلمات التي تحتاجها '
        'في البنك أعلاه.',
    g1x1='<em>Push</em> بعيداً عنك، و<em>pull</em> نحوك. واللافتة تقول لك أيّهما.',
    g1x2='الـ<em>pocket</em> مخيط في الملابس، أما الـ<em>bag</em> فوعاء منفصل '
         'تحمله معك.',
    g1x3='الـ<em>magnifying glass</em> عدسة لها مقبض تجعل الأشياء الصغيرة تبدو '
         'كبيرة.',
    g2h='كلمة واحدة في كل فراغ. اثنتان منها من أصغر كلمات الدرس.',
    g2x1='<em>Sometimes</em> تعني أحياناً — في بعض الأيام نعم وفي بعضها لا.',
    g2x2='<em>They</em> تحلّ محلّ شخصين أو أكثر سبق أن ذكرتهم.',
    g2x3='<em>True</em> يطابق الوقائع، و<em>false</em> لا يطابقها.',
)

# ══════════════════════════════════════════════════════════════════════
#  CHINESE
# ══════════════════════════════════════════════════════════════════════
Q['zh'] = dict(
    sortBinA='东西', sortBinB='动作',
    q1c='她伸出手臂，要拿桌上的硬币。',
    q1x='<em>Reach</em> 是朝某物伸出手臂。<em>Scratch</em> 是留下划痕，'
        '<em>whistle</em> 是发出声音，<em>desert</em> 是抛下某人。',
    q2c='朋友们还需要他，他却走了，再也没有回来。',
    q2x='<em>Desert</em> 是在别人还需要你的时候离开他们。注意重音：'
        'de-<em>SERT</em> 是这个动词，<em>DE</em>-sert 是干燥多沙的沙漠。',
    q3s='哪一句是正确的英语？',
    q3x='<em>Homework</em> 没有复数，所以没有 <em>homeworks</em> 这个词，'
        '前面也不能加 <em>many</em> 或 <em>two</em>。要用 <em>a lot of</em> '
        '或 <em>much</em>。',
    q4c='它每天出一份，印在大张纸上，满是当天的新闻。',
    q4x='<em>Newspaper</em> 是印在大张纸上的每日新闻。<em>Magazine</em> 更薄，'
        '图片多得多，每周或每月出一期。',

    g1h='每个空填一个词。句子仍然是英语——需要的词在上面的词库里。',
    g1x1='<em>Push</em> 是朝外推，<em>pull</em> 是朝自己拉。牌子告诉你是哪一个。',
    g1x2='<em>Pocket</em> 是缝在衣服上的，<em>bag</em> 是你另外拿着的容器。',
    g1x3='<em>Magnifying glass</em> 是带柄的镜片，让小东西看起来变大。',
    g2h='每个空填一个词。其中两个是本课最小的词。',
    g2x1='<em>Sometimes</em> 是“偶尔”——有些天会，有些天不会。',
    g2x2='<em>They</em> 指你已经提过的两个或更多的人。',
    g2x3='<em>True</em> 与事实相符，<em>false</em> 不相符。',
)

# ══════════════════════════════════════════════════════════════════════
#  JAPANESE
# ══════════════════════════════════════════════════════════════════════
Q['ja'] = dict(
    sortBinA='もの', sortBinB='動作',
    q1c='彼女はテーブルの上のコインを取ろうと腕をのばした。',
    q1x='<em>Reach</em> は何かに向かって腕をのばすことです。<em>Scratch</em> '
        'は跡をつけること、<em>whistle</em> は音を出すこと、<em>desert</em> '
        'は人を見捨てることです。',
    q2c='友だちはまだ彼を必要としていたのに、彼は去って二度と戻らなかった。',
    q2x='<em>Desert</em> は、まだ自分を必要としている人を置き去りにすること。'
        'アクセントに注意：de-<em>SERT</em> がこの動詞で、<em>DE</em>-sert は'
        '乾いた砂の砂漠です。',
    q3s='正しい英語はどれですか。',
    q3x='<em>Homework</em> に複数形はありません。<em>homeworks</em> は存在せず、'
        '<em>many</em> や <em>two</em> を前に置くこともできません。'
        '<em>a lot of</em> か <em>much</em> を使います。',
    q4c='それは毎日、大きな紙に印刷されて出て、その日のニュースでいっぱいです。',
    q4x='<em>Newspaper</em> は大きな紙に載る毎日のニュース。<em>Magazine</em> '
        'はもっと薄く、写真がずっと多く、毎週または毎月出ます。',

    g1h='空欄ごとに語を一つ。文は英語のままです。必要な語は上の単語バンクに'
        'あります。',
    g1x1='<em>Push</em> は自分から遠ざける方向、<em>pull</em> は自分のほうへ。'
         '掲示がどちらかを教えてくれます。',
    g1x2='<em>Pocket</em> は服に縫いつけられたもの、<em>bag</em> は別に持ち歩く'
         '入れ物です。',
    g1x3='<em>Magnifying glass</em> は柄のついたレンズで、小さいものを大きく'
         '見せます。',
    g2h='空欄ごとに語を一つ。うち二つはこの課でいちばん小さい語です。',
    g2x1='<em>Sometimes</em> は「ときどき」。ある日はそうで、ある日はそうでは'
         'ありません。',
    g2x2='<em>They</em> はすでに挙げた二人以上の人を指します。',
    g2x3='<em>True</em> は事実と合い、<em>false</em> は合いません。',
)

# ══════════════════════════════════════════════════════════════════════
#  The match slide. Keyed by the English term; the English definition is the
#  button text, the rest ride as data-def-<lang>.
# ══════════════════════════════════════════════════════════════════════
M_DEFS = {
    'en': {'whistle': 'make a high sound with your lips',
           'scratch': 'mark a surface with something sharp',
           'build': 'put parts together to make a house',
           'rug': 'a small, thick cloth on the floor'},
    'de': {'whistle': 'mit den Lippen einen hohen Ton machen',
           'scratch': 'eine Oberfläche mit etwas Spitzem markieren',
           'build': 'Teile zusammensetzen und ein Haus bauen',
           'rug': 'ein kleines, dickes Tuch auf dem Boden'},
    'es': {'whistle': 'hacer un sonido agudo con los labios',
           'scratch': 'marcar una superficie con algo puntiagudo',
           'build': 'unir piezas para hacer una casa',
           'rug': 'una tela pequeña y gruesa sobre el suelo'},
    'fr': {'whistle': 'faire un son aigu avec les lèvres',
           'scratch': 'marquer une surface avec quelque chose de pointu',
           'build': 'assembler des pièces pour faire une maison',
           'rug': 'un petit tissu épais posé au sol'},
    'it': {'whistle': 'fare un suono acuto con le labbra',
           'scratch': 'segnare una superficie con qualcosa di appuntito',
           'build': 'mettere insieme dei pezzi per fare una casa',
           'rug': 'un panno piccolo e spesso sul pavimento'},
    'pt': {'whistle': 'fazer um som agudo com os lábios',
           'scratch': 'marcar uma superfície com algo pontiagudo',
           'build': 'juntar peças para fazer uma casa',
           'rug': 'um pano pequeno e grosso no chão'},
    'ru': {'whistle': 'издать губами высокий звук',
           'scratch': 'оставить след на поверхности чем-то острым',
           'build': 'соединить части и построить дом',
           'rug': 'небольшой плотный кусок ткани на полу'},
    'ar': {'whistle': 'إصدار صوت حادّ بالشفتين',
           'scratch': 'ترك أثر على سطح بشيء حادّ',
           'build': 'ضمّ الأجزاء لبناء بيت',
           'rug': 'قطعة قماش صغيرة سميكة على الأرض'},
    'zh': {'whistle': '用嘴唇发出又高又清的声音',
           'scratch': '用尖的东西在表面留下痕迹',
           'build': '把零件组合起来盖成房子',
           'rug': '铺在地上的一小块厚布'},
    'ja': {'whistle': 'くちびるで高く澄んだ音を出す',
           'scratch': 'とがったもので表面に跡をつける',
           'build': '部品を組み合わせて家を建てる',
           'rug': '床に置く小さくて厚い布'},
}
