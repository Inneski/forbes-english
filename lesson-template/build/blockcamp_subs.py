"""Subtitles for the Block Camp correct-answer clips, all ten deck languages.

Cues are [start, end, text] in seconds; an end of 99 holds the line on the
clip's last frame. Timings come from a local Whisper medium.en pass
(word timestamps), set by where the words cluster, because Whisper stretches
a first word back over any silence before it. Clips with no speech, or only
noise that Whisper turned into words (the skeleton fight's "You", the bell's
"I'll see you next time", "Hmmm", "Ugh", the villagers' babble), have none.

Run this to write window.CLIP_SUBS into the three decks:
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
}

DECKS = {
  'blockcamp-present-simple.html': PS,
  'blockcamp-present-continuous.html': PC,
  'blockcamp-past-simple.html': PA,
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
