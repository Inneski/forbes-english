"""Subtitles for the Block Camp correct-answer clips, all ten deck languages.

Cues are [start, end, text] in seconds; an end of 99 holds the line on the
clip's last frame. Timings come from a local Whisper medium.en pass
(word timestamps), set by where the words cluster, because Whisper stretches
a first word back over any silence before it. Clips with no speech, or only
noise that Whisper turned into words (the skeleton fight's "You", the bell's
"I'll see you next time", "Hmmm", "Ugh", the villagers' babble), have none.

Run this to write window.CLIP_SUBS into the four decks:
    py lesson-template/build/blockcamp_subs.py
"""
import json, os, re

L = ('en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja')

def c(start, end, *texts):
    assert len(texts) == len(L), texts[0]
    return [start, end, dict(zip(L, texts))]

PS = 'present-simple-time-signals/'
PC = 'present-continuous-time-signals/'
PA = 'past-simple-time-signals/'
PP = 'past-continuous-time-signals/'

SUBS = {
  # ── Present Simple, Part 1 ──────────────────────────────────────────
  PS + 'bg12.mp4': [
    c(5.7, 7.7, 'Yay, we found it!', 'Juhu, wir haben es gefunden!', '¡Bien, lo encontramos!',
      'Youpi, on l’a trouvé !', 'Evviva, l’abbiamo trovato!', 'Oba, encontramos!',
      'Ура, мы нашли!', 'رائع، وجدناه!', '耶，我们找到了！', 'やった、見つけた！'),
    c(7.8, 99, 'This is easy!', 'Das ist leicht!', '¡Esto es fácil!', 'C’est facile !',
      'È facile!', 'Isso é fácil!', 'Это легко!', 'هذا سهل!', '这很简单！', '簡単だね！'),
  ],
  PS + 'bg16.mp4': [
    c(4.0, 6.8, 'I feed the sheep every morning.', 'Ich füttere jeden Morgen die Schafe.',
      'Doy de comer a las ovejas cada mañana.', 'Je nourris les moutons tous les matins.',
      'Do da mangiare alle pecore ogni mattina.', 'Eu alimento as ovelhas todas as manhãs.',
      'Я кормлю овец каждое утро.', 'أُطعم الخراف كل صباح.', '我每天早上喂羊。',
      '毎朝、羊にえさをあげます。'),
  ],
  PS + 'bg24.mp4': [
    c(7.2, 99, 'Hey!', 'Hey!', '¡Eh!', 'Hé !', 'Ehi!', 'Ei!', 'Эй!', 'مرحبًا!', '嘿！', 'おーい！'),
  ],
  PS + 'bg38.mp4': [
    c(3.4, 8.3, 'I eat breakfast at seven o’clock every day.',
      'Ich frühstücke jeden Tag um sieben Uhr.', 'Desayuno a las siete todos los días.',
      'Je prends mon petit-déjeuner à sept heures tous les jours.',
      'Faccio colazione alle sette ogni giorno.', 'Eu tomo café da manhã às sete horas todos os dias.',
      'Я завтракаю в семь часов каждый день.', 'أتناول الفطور في الساعة السابعة كل يوم.',
      '我每天七点吃早饭。', '毎日七時に朝ごはんを食べます。'),
  ],
  PS + 'bg41.mp4': [
    c(0.9, 6.0, 'And remember: with he, she and it, an S must fit.',
      'Und denk dran: bei he, she und it muss ein S dazu.',
      'Y recuerda: con he, she e it, hay que poner una S.',
      'Et n’oublie pas : avec he, she et it, il faut un S.',
      'E ricorda: con he, she e it ci vuole una S.',
      'E lembre-se: com he, she e it, tem de ter um S.',
      'И запомни: с he, she и it нужна буква S.',
      'وتذكّر: مع he وshe وit يجب إضافة حرف S.',
      '记住：用 he、she 和 it 的时候，一定要加 S。',
      '覚えておいて：he、she、it のときは S をつけるよ。'),
    c(6.1, 99, 'Alrighty.', 'Alles klar.', 'Muy bien.', 'D’accord.', 'Va bene.', 'Beleza.',
      'Ладушки.', 'حسنًا.', '好嘞。', 'よーし。'),
  ],

  # ── Present Continuous, Part 1 ──────────────────────────────────────
  PC + 'bg09.mp4': [
    c(1.4, 3.8, 'Alex is baking bread.', 'Alex backt gerade Brot.', 'Alex está horneando pan.',
      'Alex est en train de faire du pain.', 'Alex sta cuocendo il pane.', 'Alex está assando pão.',
      'Алекс печёт хлеб.', 'أليكس يخبز الخبز.', 'Alex 正在烤面包。', 'アレックスはパンを焼いています。'),
  ],
  PC + 'bg11.mp4': [
    c(0.0, 2.3, 'Is the witch brewing a potion?', 'Braut die Hexe gerade einen Trank?',
      '¿La bruja está preparando una poción?', 'La sorcière est-elle en train de préparer une potion ?',
      'La strega sta preparando una pozione?', 'A bruxa está preparando uma poção?',
      'Ведьма варит зелье?', 'هل الساحرة تُحضّر جرعة سحرية؟', '女巫在熬药水吗？',
      '魔女は薬を作っているの？'),
    c(5.3, 7.3, 'Yes, I am.', 'Ja, das tue ich.', 'Sí, lo estoy.', 'Oui, c’est ça.', 'Sì, proprio così.',
      'Sim, estou.', 'Да, варю.', 'نعم، أفعل.', '是的，我在熬。', 'ええ、そうよ。'),
  ],
  PC + 'bg14.mp4': [
    c(3.5, 4.6, 'Hey!', 'Hey!', '¡Eh!', 'Hé !', 'Ehi!', 'Ei!', 'Эй!', 'مرحبًا!', '嘿！', 'ねえ！'),
    c(4.8, 7.0, 'Is all that clucking for me?', 'Ist das ganze Gegacker für mich?',
      '¿Todo ese cacareo es para mí?', 'Tout ce caquètement, c’est pour moi ?',
      'Tutto questo coccodè è per me?', 'Todo esse cacarejo é para mim?',
      'Это всё кудахтанье — для меня?', 'هل كل هذه القوقأة من أجلي؟', '这么多咯咯叫，是冲我来的吗？',
      'そのコッコッって、ぼくのため？'),
  ],
  PC + 'bg18.mp4': [
    c(3.5, 6.9, 'Steve mines every day, but today he’s resting.',
      'Steve baut jeden Tag Erz ab, aber heute ruht er sich aus.',
      'Steve pica en la mina todos los días, pero hoy está descansando.',
      'Steve mine tous les jours, mais aujourd’hui il se repose.',
      'Steve scava in miniera ogni giorno, ma oggi si sta riposando.',
      'Steve minera todos os dias, mas hoje está descansando.',
      'Стив каждый день работает в шахте, но сегодня он отдыхает.',
      'ستيف يعمل في المنجم كل يوم، لكنه اليوم يستريح.',
      'Steve 每天都挖矿，但今天他在休息。',
      'スティーブは毎日採掘するけど、今日は休んでいます。'),
  ],
  PC + 'bg33.mp4': [
    c(2.0, 4.4, 'We aren’t building the bridge right now.', 'Wir bauen gerade nicht an der Brücke.',
      'Ahora mismo no estamos construyendo el puente.', 'Nous ne construisons pas le pont en ce moment.',
      'In questo momento non stiamo costruendo il ponte.', 'Não estamos construindo a ponte agora.',
      'Сейчас мы не строим мост.', 'نحن لا نبني الجسر الآن.', '我们现在没在建桥。',
      '今は橋を作っていないよ。'),
    c(4.8, 7.0, 'We stopped an hour ago, aye?', 'Wir haben vor einer Stunde aufgehört, oder?',
      'Paramos hace una hora, ¿eh?', 'On s’est arrêtés il y a une heure, hein ?',
      'Ci siamo fermati un’ora fa, eh?', 'Paramos há uma hora, né?',
      'Мы закончили час назад, да?', 'توقفنا قبل ساعة، أليس كذلك؟', '我们一个小时前就停了，对吧？',
      '一時間前にやめたんだよね？'),
  ],
  PC + 'bg37.mp4': [
    c(0.0, 1.25, 'What do you reckon about this, mate?', 'Was meinst du dazu, Kumpel?',
      '¿Qué te parece esto, amigo?', 'T’en penses quoi, mon pote ?', 'Che ne pensi, amico?',
      'O que você acha disso, parceiro?', 'Что скажешь, приятель?', 'ما رأيك في هذا يا صاحبي؟',
      '伙计，你觉得这个怎么样？', 'これ、どう思う？'),
    c(1.25, 2.4, 'Needs more pink.', 'Braucht mehr Rosa.', 'Le falta más rosa.', 'Il faut plus de rose.',
      'Ci vuole più rosa.', 'Precisa de mais rosa.', 'Нужно больше розового.', 'يحتاج إلى مزيد من الوردي.',
      '需要更多粉色。', 'もっとピンクが必要だね。'),
    c(2.5, 4.3, 'Too right. You can never have enough.', 'Genau. Davon kann man nie genug haben.',
      'Totalmente. Nunca es suficiente.', 'Carrément. On n’en a jamais assez.',
      'Verissimo. Non è mai abbastanza.', 'Com certeza. Nunca é demais.',
      'Точно. Его много не бывает.', 'بالضبط. لا يكفي أبدًا.', '说得对。粉色永远不嫌多。',
      'そのとおり。多すぎることはないよ。'),
    c(4.4, 7.0, 'No worries. Let’s crack on and finish it, then.', 'Kein Problem. Dann machen wir es mal fertig.',
      'Tranquilo. Pues vamos a terminarlo.', 'Pas de souci. Allez, on le termine.',
      'Tranquillo. Allora diamoci da fare e finiamolo.', 'Sem problemas. Então vamos terminar.',
      'Без проблем. Тогда давай доделаем.', 'لا مشكلة. هيا لننهِه إذن.', '没问题。那我们加把劲把它完成吧。',
      '大丈夫。じゃあ、さっさと仕上げよう。'),
    c(8.0, 99, 'She’s looking pretty good now, isn’t she?', 'Sieht jetzt ziemlich gut aus, oder?',
      'Ahora se ve bastante bien, ¿verdad?', 'Elle a plutôt fière allure maintenant, non ?',
      'Adesso è davvero bella, vero?', 'Agora está ficando bem bonita, não está?',
      'Теперь выглядит неплохо, правда?', 'تبدو رائعة الآن، أليس كذلك؟', '现在看起来挺不错的，对吧？',
      'なかなかいい感じになったね。'),
  ],

  # ── Past Simple, Part 1 ─────────────────────────────────────────────
  PA + 'bg02.mp4': [
    c(0.4, 2.2, 'Yeah, I closed it.', 'Ja, ich hab sie zugemacht.', 'Sí, la cerré.', 'Ouais, je l’ai fermée.',
      'Sì, l’ho chiusa.', 'É, eu fechei.', 'Ага, я её закрыл.', 'نعم، أغلقتُه.', '对，我关上了。',
      'うん、閉めたよ。'),
    c(2.2, 99, 'That’s how I roll.', 'So mach ich das eben.', 'Así soy yo.', 'C’est comme ça que je fais.',
      'Io faccio così.', 'É assim que eu faço.', 'Вот так я и живу.', 'هكذا أنا.', '我就是这么酷。',
      'これがぼくのやり方さ。'),
  ],
  PA + 'bg24.mp4': [
    c(3.3, 4.4, 'Hey!', 'Hey!', '¡Eh!', 'Hé !', 'Ehi!', 'Ei!', 'Эй!', 'مرحبًا!', '嘿！', 'やあ！'),
    c(4.6, 99, 'When did you plant these trees?', 'Wann hast du diese Bäume gepflanzt?',
      '¿Cuándo plantaste estos árboles?', 'Quand est-ce que tu as planté ces arbres ?',
      'Quando hai piantato questi alberi?', 'Quando você plantou estas árvores?',
      'Когда ты посадила эти деревья?', 'متى زرعتِ هذه الأشجار؟', '这些树你是什么时候种的？',
      'この木はいつ植えたの？'),
  ],
  PA + 'bg05.mp4': [
    c(3.4, 4.3, 'Well…', 'Na…', 'Vaya…', 'Tiens…', 'Bene…', 'Ora…', 'Так…', 'حسنًا…', '哎呀……', 'おやおや…'),
    c(7.9, 99, 'Well, well, what do we have here?', 'Na, na, was haben wir denn hier?',
      'Vaya, vaya, ¿qué tenemos aquí?', 'Tiens, tiens, qu’est-ce qu’on a là ?',
      'Bene, bene, cosa abbiamo qui?', 'Ora, ora, o que temos aqui?',
      'Так-так, что тут у нас?', 'حسنًا، حسنًا، ماذا لدينا هنا؟', '哎呀呀，这是什么？',
      'おやおや、これは何かな？'),
  ],
  PA + 'bg07.mp4': [
    c(4.0, 6.4, 'What did you do before breakfast?', 'Was hast du vor dem Frühstück gemacht?',
      '¿Qué hiciste antes del desayuno?', 'Qu’est-ce que tu as fait avant le petit-déjeuner ?',
      'Cosa hai fatto prima di colazione?', 'O que você fez antes do café da manhã?',
      'Что ты делал до завтрака?', 'ماذا فعلت قبل الفطور؟', '早饭前你做了什么？',
      '朝ごはんの前に何をしたの？'),
    c(8.9, 99, 'I went down the mine.', 'Ich bin in die Mine gegangen.', 'Bajé a la mina.',
      'Je suis descendue à la mine.', 'Sono scesa in miniera.', 'Eu desci à mina.',
      'Я спустилась в шахту.', 'نزلتُ إلى المنجم.', '我下矿井去了。', '鉱山に行ったよ。'),
  ],
  PA + 'bg18.mp4': [
    c(0.3, 3.4, 'My neighbours were away, so I fed the chickens.',
      'Meine Nachbarn waren weg, also habe ich die Hühner gefüttert.',
      'Mis vecinos no estaban, así que di de comer a las gallinas.',
      'Mes voisins étaient absents, alors j’ai nourri les poules.',
      'I miei vicini erano via, così ho dato da mangiare alle galline.',
      'Meus vizinhos estavam fora, então eu alimentei as galinhas.',
      'Соседей не было, поэтому я покормила кур.',
      'كان جيراني مسافرين، فأطعمتُ الدجاج.', '邻居不在家，所以我喂了鸡。',
      '隣の人たちが留守だったから、ニワトリにえさをあげたよ。'),
    c(6.4, 8.2, 'Looking for me?', 'Suchst du mich?', '¿Me buscabas?', 'Tu me cherches ?',
      'Cercavi me?', 'Procurando por mim?', 'Меня ищешь?', 'هل تبحث عني؟', '在找我吗？', 'ぼくを探してる？'),
  ],
  PA + 'bg25.mp4': [
    c(3.9, 8.5, 'Let’s go feel that beat!', 'Los, spüren wir den Beat!', '¡Vamos a sentir ese ritmo!',
      'Allez, on va sentir ce rythme !', 'Andiamo a sentire quel ritmo!', 'Vamos sentir essa batida!',
      'Давайте почувствуем ритм!', 'هيا لنشعر بهذا الإيقاع!', '来，一起感受节奏吧！',
      'さあ、リズムを感じよう！'),
  ],
  PA + 'bg28.mp4': [
    c(0.4, 2.4, 'Watch your step with that box.', 'Pass auf, wo du hintrittst, mit der Kiste.',
      'Cuidado dónde pisas con esa caja.', 'Attention où tu marches avec cette caisse.',
      'Attento a dove metti i piedi con quella scatola.', 'Cuidado onde pisa com essa caixa.',
      'Смотри под ноги с этой коробкой.', 'انتبه لخطواتك وأنت تحمل هذا الصندوق.',
      '拿着箱子，小心脚下。', '箱を持ってるから、足元に気をつけて。'),
    c(2.5, 4.4, 'We are finally here, kids!', 'Wir sind endlich da, Kinder!', '¡Por fin hemos llegado, niños!',
      'On est enfin arrivés, les enfants !', 'Finalmente siamo arrivati, ragazzi!',
      'Finalmente chegamos, crianças!', 'Наконец-то мы на месте, дети!', 'وصلنا أخيرًا يا أطفال!',
      '孩子们，我们终于到了！', 'みんな、やっと着いたよ！'),
    c(4.4, 5.9, 'This is gonna be great!', 'Das wird toll!', '¡Esto va a ser genial!', 'Ça va être génial !',
      'Sarà fantastico!', 'Isso vai ser ótimo!', 'Будет здорово!', 'سيكون هذا رائعًا!', '这下可太棒了！',
      'きっと最高だよ！'),
    c(5.9, 7.6, 'I’ll race you to the room!', 'Wer zuerst im Zimmer ist!', '¡Te echo una carrera hasta la habitación!',
      'Le premier arrivé dans la chambre !', 'Facciamo a gara fino alla stanza!', 'Aposto corrida até o quarto!',
      'Наперегонки до комнаты!', 'لنتسابق إلى الغرفة!', '比赛看谁先到房间！', '部屋まで競争だ！'),
    c(8.1, 99, 'It’s good to be home.', 'Schön, zu Hause zu sein.', 'Qué bien estar en casa.',
      'Ça fait du bien d’être chez soi.', 'È bello essere a casa.', 'É bom estar em casa.',
      'Как хорошо быть дома.', 'ما أجمل أن نكون في البيت.', '到家真好。', 'やっぱり家はいいな。'),
  ],
  PA + 'bg16.mp4': [
    c(1.1, 2.9, 'We hit the mother lode!', 'Wir sind auf die Hauptader gestoßen!', '¡Dimos con la veta madre!',
      'On est tombés sur le filon !', 'Abbiamo trovato il filone!', 'Achamos o veio principal!',
      'Мы наткнулись на богатую жилу!', 'عثرنا على عِرق الذهب الغني!', '我们挖到大矿脉了！', '大鉱脈を掘り当てたぞ！'),
    c(3.2, 4.25, 'Keep digging!', 'Grab weiter!', '¡Sigue cavando!', 'Continue à creuser !', 'Continua a scavare!',
      'Continue cavando!', 'Копай дальше!', 'استمر في الحفر!', '继续挖！', '掘り続けて！'),
    c(4.25, 5.0, 'Look there!', 'Sieh mal da!', '¡Mira allí!', 'Regarde là !', 'Guarda lì!', 'Olha ali!',
      'Смотри туда!', 'انظر هناك!', '看那儿！', 'あそこを見て！'),
    c(5.3, 7.7, 'Wait, that’s no ordinary rock.', 'Moment, das ist kein gewöhnlicher Stein.',
      'Espera, eso no es una roca normal.', 'Attends, ce n’est pas un rocher ordinaire.',
      'Aspetta, quella non è una roccia qualunque.', 'Espera, isso não é uma pedra comum.',
      'Стой, это не простой камень.', 'انتظر، هذه ليست صخرة عادية.', '等等，那可不是普通的石头。',
      '待って、あれはただの岩じゃない。'),
    c(7.9, 9.5, 'It is an ancient statue!', 'Das ist eine uralte Statue!', '¡Es una estatua antigua!',
      'C’est une statue ancienne !', 'È una statua antica!', 'É uma estátua antiga!',
      'Это древняя статуя!', 'إنه تمثال قديم!', '是一座古老的雕像！', '古代の像だ！'),
    c(9.5, 11.0, 'Get back!', 'Zurück!', '¡Atrás!', 'Recule !', 'Indietro!', 'Para trás!', 'Назад!',
      'ارجع!', '快退后！', '下がって！'),
  ],
  PA + 'bg37.mp4': [
    c(1.0, 3.9, 'Where are you going with my succulent meal?',
      'Wohin willst du mit meinem saftigen Essen?', '¿Adónde vas con mi suculenta comida?',
      'Où tu vas avec mon succulent repas ?', 'Dove vai con il mio succulento pranzo?',
      'Aonde você vai com a minha refeição suculenta?', 'Куда это ты с моим сочным обедом?',
      'إلى أين تذهب بوجبتي الشهية؟', '你要把我美味的饭菜拿到哪里去？',
      'ぼくのおいしいごはんを持ってどこへ行くんだ？'),
    c(4.0, 99, 'Come back here!', 'Komm sofort zurück!', '¡Vuelve aquí!', 'Reviens ici !', 'Torna qui!',
      'Volte aqui!', 'А ну вернись!', 'عُد إلى هنا!', '给我回来！', '戻ってこい！'),
  ],
  PA + 'bg32.mp4': [
    c(1.0, 7.8, 'I left the village and set off for the big wide world.',
      'Ich verließ das Dorf und machte mich auf in die große weite Welt.',
      'Dejé el pueblo y partí hacia el ancho mundo.',
      'J’ai quitté le village et je suis parti découvrir le vaste monde.',
      'Ho lasciato il villaggio e sono partito per il grande mondo.',
      'Deixei a aldeia e parti para o vasto mundo.',
      'Я покинул деревню и отправился в большой мир.',
      'غادرتُ القرية وانطلقتُ إلى العالم الواسع.', '我离开了村子，出发去看广阔的世界。',
      '村を出て、広い世界へ旅立ったんだ。'),
  ],
  # ── Past Continuous, Part 1 ─────────────────────────────────────────
  PP + 'bg15.mp4': [
    c(0.0, 2.3, 'While I was riding through the fields,', 'Während ich durch die Felder ritt,',
      'Mientras cabalgaba por los campos,', 'Pendant que je traversais les champs à cheval,',
      'Mentre cavalcavo per i campi,', 'Enquanto eu cavalgava pelos campos,',
      'Пока я скакала по полям,', 'بينما كنتُ أركب الحصان عبر الحقول،', '我骑马穿过田野的时候，',
      '畑を馬で走っていたら、'),
    c(2.7, 99, 'I saw a buffalo on the horizon.', 'sah ich am Horizont einen Büffel.',
      'vi un búfalo en el horizonte.', 'j’ai vu un bison à l’horizon.',
      'ho visto un bufalo all’orizzonte.', 'vi um búfalo no horizonte.',
      'я увидела на горизонте бизона.', 'رأيتُ جاموسًا في الأفق.', '看见地平线上有一头野牛。',
      '地平線にバッファローが見えたの。'),
  ],
  PP + 'bg38.mp4': [
    c(2.7, 4.7, 'I was digging a tunnel all morning.', 'Ich habe den ganzen Morgen einen Tunnel gegraben.',
      'Estuve cavando un túnel toda la mañana.', 'J’ai creusé un tunnel toute la matinée.',
      'Ho scavato un tunnel tutta la mattina.', 'Passei a manhã toda cavando um túnel.',
      'Я всё утро копал туннель.', 'كنتُ أحفر نفقًا طوال الصباح.', '我一上午都在挖隧道。',
      '午前中ずっとトンネルを掘ってたんだ。'),
    c(4.9, 99, 'It was pretty hard work, my friend.', 'Das war ganz schön harte Arbeit, mein Freund.',
      'Fue un trabajo bastante duro, amigo.', 'C’était plutôt dur, mon ami.',
      'È stato un lavoro piuttosto duro, amico mio.', 'Foi um trabalho bem pesado, meu amigo.',
      'Тяжёлая была работа, друг мой.', 'كان عملًا شاقًا يا صديقي.', '这活儿可真累啊，朋友。',
      'かなりきつい仕事だったよ、友よ。'),
  ],
  PP + 'bg09.mp4': [
    c(0.9, 4.2, 'So, what were they doing during the eclipse yesterday?',
      'Und, was haben sie gestern während der Sonnenfinsternis gemacht?',
      'Entonces, ¿qué estaban haciendo durante el eclipse de ayer?',
      'Alors, qu’est-ce qu’ils faisaient pendant l’éclipse hier ?',
      'Allora, cosa stavano facendo ieri durante l’eclissi?',
      'E aí, o que eles estavam fazendo durante o eclipse ontem?',
      'Ну и что они делали вчера во время затмения?',
      'إذن، ماذا كانوا يفعلون أثناء الكسوف أمس؟', '那么，昨天日食的时候他们在干什么？',
      'それで、きのうの日食のとき、みんな何をしてたの？'),
    c(5.3, 99, 'I was just staring at the square sun.', 'Ich habe nur die eckige Sonne angestarrt.',
      'Yo solo estaba mirando el sol cuadrado.', 'Moi, je regardais juste le soleil carré.',
      'Io stavo solo fissando il sole quadrato.', 'Eu só estava olhando para o sol quadrado.',
      'Я просто смотрел на квадратное солнце.', 'كنتُ أحدّق فقط في الشمس المربعة.',
      '我只是一直盯着那个方形的太阳。', '僕は四角い太陽をじっと見てただけだよ。'),
  ],
  PP + 'bg36.mp4': [
    c(3.1, 5.4, 'What were you doing when I called last night?',
      'Was hast du gemacht, als ich gestern Abend angerufen habe?',
      '¿Qué estabas haciendo cuando te llamé anoche?',
      'Qu’est-ce que tu faisais quand j’ai appelé hier soir ?',
      'Cosa stavi facendo quando ti ho chiamato ieri sera?',
      'O que você estava fazendo quando eu liguei ontem à noite?',
      'Что ты делал, когда я звонил вчера вечером?',
      'ماذا كنتَ تفعل عندما اتصلتُ بك الليلة الماضية؟', '昨晚我打电话的时候你在干什么？',
      'ゆうべ電話したとき、何してたの？'),
    c(5.6, 99, 'I was busy fighting off a zombie horde outside.',
      'Ich war draußen damit beschäftigt, eine Zombiehorde abzuwehren.',
      'Estaba ocupado luchando contra una horda de zombis afuera.',
      'J’étais occupé à repousser une horde de zombies dehors.',
      'Ero impegnato a respingere un’orda di zombie qui fuori.',
      'Eu estava ocupado lutando contra uma horda de zumbis lá fora.',
      'Я был занят — отбивался от толпы зомби на улице.',
      'كنتُ مشغولًا بصدّ جيش من الزومبي في الخارج.', '我在外面忙着打退一大群僵尸。',
      '外でゾンビの群れと戦うのにいそがしかったんだ。'),
  ],
  PP + 'bg11.mp4': [
    c(1.7, 4.6, 'Where did they say the nearest store was?',
      'Wo, haben sie gesagt, ist der nächste Laden?',
      '¿Dónde dijeron que estaba la tienda más cercana?',
      'Ils ont dit que le magasin le plus proche était où ?',
      'Dove hanno detto che era il negozio più vicino?',
      'Onde disseram que ficava a loja mais próxima?',
      'Где, они сказали, ближайший магазин?',
      'أين قالوا إن أقرب متجر يقع؟', '他们说最近的商店在哪儿来着？',
      'いちばん近いお店はどこだって言ってた？'),
    c(5.0, 99, 'I wasn’t listening. I’m sorry.', 'Ich habe nicht zugehört. Tut mir leid.',
      'No estaba escuchando. Lo siento.', 'Je n’écoutais pas. Désolé.',
      'Non stavo ascoltando. Scusa.', 'Eu não estava prestando atenção. Desculpa.',
      'Я не слушал. Извини.', 'لم أكن أستمع. آسف.', '我刚才没在听。对不起。',
      '聞いてなかった。ごめんね。'),
  ],
  PP + 'bg05.mp4': [
    c(2.7, 5.5, 'No, we were climbing at eight o’clock, so we were.',
      'Nein, wir sind um acht Uhr geklettert, wirklich.',
      'No, a las ocho estábamos escalando, de verdad.',
      'Non, à huit heures on grimpait, je te dis.',
      'No, alle otto stavamo arrampicando, davvero.',
      'Não, às oito horas a gente estava escalando, sim.',
      'Нет, в восемь часов мы лазали по скалам, вот так.',
      'لا، كنا نتسلّق في الساعة الثامنة، حقًا.', '不，八点钟的时候我们在攀岩，真的。',
      'ちがうよ、八時にはぼくたち山登りしてたんだ、ほんとに。'),
    c(5.6, 99, 'We weren’t fishing at all!', 'Wir haben überhaupt nicht geangelt!',
      '¡No estábamos pescando para nada!', 'On ne pêchait pas du tout !',
      'Non stavamo affatto pescando!', 'A gente não estava pescando nada!',
      'Мы вовсе не рыбачили!', 'لم نكن نصطاد السمك أبدًا!', '我们根本没在钓鱼！',
      '釣りなんて全然してなかったよ！'),
  ],
  PP + 'bg08.mp4': [
    c(0.0, 1.6, 'We need to find shelter soon.', 'Wir müssen bald einen Unterschlupf finden.',
      'Tenemos que encontrar refugio pronto.', 'Il faut vite trouver un abri.',
      'Dobbiamo trovare un riparo presto.', 'Precisamos achar um abrigo logo.',
      'Нам надо скорее найти укрытие.', 'يجب أن نجد مأوى قريبًا.', '我们得赶快找个地方躲一躲。',
      '早くかくれる場所を見つけなきゃ。'),
    c(1.7, 3.9, 'Wait, look over there in the tall grass.', 'Warte, schau mal da drüben im hohen Gras.',
      'Espera, mira allí, en la hierba alta.', 'Attends, regarde là-bas, dans les hautes herbes.',
      'Aspetta, guarda laggiù nell’erba alta.', 'Espera, olha ali no capim alto.',
      'Стой, смотри — вон там, в высокой траве.', 'انتظر، انظر هناك في العشب الطويل.',
      '等等，看那边的高草丛里。', '待って、あそこの高い草の中を見て。'),
    c(4.4, 99, 'I think they might be hunting us.', 'Ich glaube, die jagen uns vielleicht.',
      'Creo que nos están cazando.', 'Je crois qu’ils nous chassent.',
      'Credo che ci stiano dando la caccia.', 'Acho que eles estão caçando a gente.',
      'Кажется, они на нас охотятся.', 'أظن أنهم ربما يطاردوننا.', '我觉得它们可能在追捕我们。',
      'あいつら、ぼくたちをねらってるのかも。'),
  ],
  PP + 'bg18.mp4': [
    c(5.0, 99, 'Hey, you dropped this on the ground!', 'Hey, das hast du auf den Boden fallen lassen!',
      '¡Eh, se te cayó esto al suelo!', 'Hé, tu as fait tomber ça par terre !',
      'Ehi, ti è caduto questo per terra!', 'Ei, você deixou cair isto no chão!',
      'Эй, ты уронил это на землю!', 'مرحبًا، لقد أسقطتَ هذا على الأرض!', '嘿，你的东西掉地上了！',
      'ねえ、これ地面に落としたよ！'),
  ],
  PP + 'bg27.mp4': [
    c(1.8, 99, 'What was I doing?', 'Was habe ich gerade gemacht?', '¿Qué estaba haciendo yo?',
      'Qu’est-ce que je faisais, déjà ?', 'Cosa stavo facendo?', 'O que eu estava fazendo mesmo?',
      'Что я делал?', 'ماذا كنتُ أفعل؟', '我刚才在干什么来着？', 'あれ、ぼく何してたんだっけ？'),
  ],
  PP + 'bg24.mp4': [
    c(4.9, 99, 'We sure did bake a lot of bread, didn’t we, honey?',
      'Wir haben echt viel Brot gebacken, was, Schatz?',
      'Sí que horneamos mucho pan, ¿verdad, cariño?',
      'On a vraiment fait cuire beaucoup de pain, hein, chéri ?',
      'Abbiamo proprio sfornato un sacco di pane, vero, tesoro?',
      'A gente assou muito pão mesmo, não foi, querido?',
      'Ну мы и напекли хлеба, правда, дорогой?',
      'لقد خبزنا الكثير من الخبز، أليس كذلك يا عزيزي؟', '我们真是烤了好多面包啊，对吧，亲爱的？',
      'ほんとにたくさんパンを焼いたね、ねえ、あなた？'),
  ],
  PP + 'bg25.mp4': [
    c(1.0, 2.1, 'What do you have there?', 'Was hast du da?', '¿Qué tienes ahí?', 'Qu’est-ce que tu as là ?',
      'Cos’hai lì?', 'O que você tem aí?', 'Что это у тебя?', 'ماذا لديك هناك؟', '你拿着什么？',
      'それ、なに持ってるの？'),
    c(2.2, 4.1, 'Something special for tonight?', 'Etwas Besonderes für heute Abend?',
      '¿Algo especial para esta noche?', 'Quelque chose de spécial pour ce soir ?',
      'Qualcosa di speciale per stasera?', 'Algo especial para hoje à noite?',
      'Что-то особенное на этот вечер?', 'شيء مميز لهذه الليلة؟', '今晚的特别礼物吗？',
      '今夜のための特別なもの？'),
    c(4.2, 7.0, 'To the best view in the world!', 'Auf die schönste Aussicht der Welt!',
      '¡Por la mejor vista del mundo!', 'À la plus belle vue du monde !',
      'Alla vista più bella del mondo!', 'À melhor vista do mundo!',
      'За самый лучший вид на свете!', 'نخب أجمل منظر في العالم!', '敬世界上最美的风景！',
      '世界一のながめに乾杯！'),
    c(8.2, 99, 'Quick, make a wish!', 'Schnell, wünsch dir was!', '¡Rápido, pide un deseo!',
      'Vite, fais un vœu !', 'Presto, esprimi un desiderio!', 'Rápido, faz um pedido!',
      'Скорее, загадай желание!', 'بسرعة، تمنَّ أمنية!', '快，许个愿！', '早く、願いごとをして！'),
  ],
}

DECKS = {
  'blockcamp-present-simple.html': PS,
  'blockcamp-present-continuous.html': PC,
  'blockcamp-past-simple.html': PA,
  'blockcamp-past-continuous.html': PP,
}

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
CSS = open(os.path.join(HERE, 'blockcamp_subs.css'), encoding='utf-8').read()
JS = open(os.path.join(HERE, 'blockcamp_subs.js'), encoding='utf-8').read()
CSS_START, CSS_END = '/* ── CLIP SUBTITLES ── */', '/* ── /CLIP SUBTITLES ── */'
JS_START, JS_END = '<!-- CLIP SUBTITLES -->', '<!-- /CLIP SUBTITLES -->'


def put(s, start, end, body, anchor, before):
    block = start + '\n' + body.strip() + '\n' + end
    if start in s:
        i = s.index(start); j = s.index(end, i) + len(end)
        return s[:i] + block + s[j:]
    assert s.count(anchor) == 1, anchor
    return s.replace(anchor, block + '\n' + anchor if before else anchor + '\n' + block)


for deck, prefix in DECKS.items():
    path = os.path.join(ROOT, deck)
    s = open(path, encoding='utf-8', newline='').read()
    mine = {k: v for k, v in SUBS.items() if k.startswith(prefix)}
    for k in mine:
        assert os.path.exists(os.path.join(ROOT, k)), k
        assert f'"{k}"' in s, (deck, k, 'clip not used by this deck')
    data = 'window.CLIP_SUBS=' + json.dumps(mine, ensure_ascii=False, separators=(',', ':')) + ';'
    s = put(s, CSS_START, CSS_END, CSS, '/* ── RESULTS ── */', True)
    s = put(s, JS_START, JS_END, '<script>' + data + '</script>\n' + JS, '</body>', True)
    open(path, 'w', encoding='utf-8', newline='').write(s)
    print(deck, len(mine), 'clips with subtitles,', sum(len(v) for v in mine.values()), 'cues')
