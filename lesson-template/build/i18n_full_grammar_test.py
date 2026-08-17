# -*- coding: utf-8 -*-
"""Interface strings for Escape from Grammar Jail (B1), all ten languages.

This is the most multilingual lesson on the site — en, de, it, es, fr, ja,
zh, ar, ru, pt — and almost none of it is retranslated here. Three tables
were committed beside this file when the page was still a scrolling test,
and they stay the source of truth:

  * `ui_i18n.json`        — the page chrome, ten languages
  * `sections_i18n.json`  — the fifteen grammar sections, ten languages
  * `all_questions_i18n.json` — per-question L1 prompt + L1 grammar note,
                            nine non-English languages, forty-five items

`ui_i18n.json` and `sections_i18n.json` are consumed here and mapped onto
the deck's key names. `all_questions_i18n.json` is *not*: `UI_I18N` is a
flat key/value table and the per-question layer is a 45x2 array per
language whose English column is deliberately empty, which the checker's
"every data-i18n resolves against a non-empty English key" rule cannot
express. It therefore stays in its own structure inside the lesson and is
wired to the same language selector — see `build_full_grammar_test.py`.

What the mapping buys, key by key:

  coverSub   <- ui.sub        ("15 grammar topics · 3 questions per topic")
  chipFocus  <- ui.introEye   ("Cheat Sheet Test · All Topics")
  chipCount  <- ui.h1         ("45 Questions")
  orTitle    <- ui.h1         (the orientation slide is the same claim)
  orTagA/B/C <- ui.typeTags   (MCQ / GAP / ERR, already translated)
  bankLabel  <- ui.hintLabel  ("Hint:" — the bank is a hint set)
  res*       <- ui.verdicts   (the four score bands, title + detail joined)
  sec{n}E    <- sections_i18n (the section's meaning, in the learner's L1)

`sec{n}T` is the English name of the structure — *might*, *have to*,
*So / Neither* — and is identical in all ten languages on purpose. It is
target language, not chrome, and the house rule is that the English being
taught stays English. The lesson's own name is handled the same way: the
cover title reads *Escape from Grammar Jail* in every language, the way a
film title does, and only the "· All Topics" half of the eyebrow moves.

Generic chrome comes from `chrome_i18n.py`; `actTitle`, `actUse` and
`actWriteKind` are lifted verbatim from `forbes-c1-negotiation.html`,
which is the ten-language reference. That leaves six strings genuinely
written for this lesson — the two activation briefs, the three speaking
prompts and the writing placeholder — and those are below.

Two traps, both live here. `actPlaceholder` reaches the DOM as a property
(`el.placeholder = v`), and the four `res*` strings reach it through
`textContent`, so an HTML entity in any of them renders as literal source.
Real characters only in those five.
"""
import json
import os
import sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

HERE = os.path.dirname(os.path.abspath(__file__))

UI = json.load(open(os.path.join(HERE, 'ui_i18n.json'), encoding='utf-8'))
SECTIONS = json.load(open(os.path.join(HERE, 'sections_i18n.json'), encoding='utf-8'))

LANGS = ('en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja')

# Raw JS literals, taken from chrome_i18n rather than retranslated.
LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel',
        'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext',
        'actEyebrow', 'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

# Lifted verbatim from forbes-c1-negotiation.html, the ten-language deck.
ACT_CHROME = {
    'actTitle': {
        'en': 'Put it to work', 'de': 'In die Praxis bringen',
        'es': 'Ponlo en práctica', 'fr': 'Passez à la pratique',
        'it': 'Mettilo in pratica', 'pt': 'Ponha em prática',
        'ru': 'Применить на деле', 'ar': 'ضعها موضع التنفيذ',
        'zh': '实际用起来', 'ja': '実際に使う'},
    'actUse': {
        'en': 'Use at least three:', 'de': 'Verwende mindestens drei:',
        'es': 'Usa al menos tres:', 'fr': 'Employez-en au moins trois :',
        'it': 'Usane almeno tre:', 'pt': 'Use pelo menos três:',
        'ru': 'Используйте не менее трёх:', 'ar': 'استخدم ثلاثاً على الأقل:',
        'zh': '至少使用其中三个：', 'ja': '次のうち3つ以上を使うこと：'},
    'actWriteKind': {
        'en': 'Writing &middot; 180&ndash;220 words',
        'de': 'Schreiben &middot; 180&ndash;220 Wörter',
        'es': 'Redacción &middot; 180&ndash;220 palabras',
        'fr': 'Rédaction &middot; 180&ndash;220 mots',
        'it': 'Scrittura &middot; 180&ndash;220 parole',
        'pt': 'Escrita &middot; 180&ndash;220 palavras',
        'ru': 'Письмо &middot; 180&ndash;220 слов',
        'ar': 'كتابة &middot; ١٨٠&ndash;٢٢٠ كلمة',
        'zh': '写作 &middot; 180&ndash;220 词',
        'ja': 'ライティング &middot; 180〜220語'},
}

# Target language, so identical in every layer. See the docstring.
SHARED = {
    'coverTitle': 'Escape from <em>Grammar Jail</em>',
    'chipLevel': 'B1',
}

# ── the six strings actually written for this lesson ───────────────────
# The speaking prompts are situations, and each one is built so that the
# structures the deck tests are the only comfortable way through it:
# obligation for the flatmate, plans and predictions for Saturday,
# present perfect plus So/Neither for the comparison.
ACT = {
    'en': dict(
        actSpeakBrief='Take a prompt each and keep going until your partner '
                      'has used the same structures back at you.',
        actSpeak1='Your flatmate has left the kitchen in a state again. Tell '
                  'them what they must do, what they mustn&rsquo;t do, and '
                  'what they don&rsquo;t have to bother with.',
        actSpeak2='Plan next Saturday together, disagreeing at first. Say '
                  'what you are going to do, what you think will happen, and '
                  'what you might do instead if it rains.',
        actSpeak3='Compare your lives. Three things you have already done, '
                  'three you have never done &mdash; and agree each time with '
                  '<em>So have I</em> or <em>Neither have I</em>.',
        actWriteBrief='Write to a friend who is coming to stay for a week. '
                      'Say what they have to bring, what they mustn&rsquo;t '
                      'forget, what you are going to do together, and one '
                      'thing neither of you has ever done that you would both '
                      'like to try.',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
    'de': dict(
        actSpeakBrief='Nehmt euch je eine Aufgabe und macht weiter, bis euer '
                      'Gegenüber dieselben Strukturen zurückgegeben hat.',
        actSpeak1='Dein Mitbewohner hat die Küche wieder verwüstet. Sag ihm, '
                  'was er tun muss, was er nicht tun darf und worum er sich '
                  'nicht zu kümmern braucht.',
        actSpeak2='Plant gemeinsam den nächsten Samstag &mdash; zuerst uneinig. '
                  'Sagt, was ihr vorhabt, was eurer Meinung nach passieren '
                  'wird und was ihr stattdessen machen könntet, wenn es regnet.',
        actSpeak3='Vergleicht euer Leben. Drei Dinge, die ihr schon gemacht '
                  'habt, drei, die ihr nie gemacht habt &mdash; und stimmt '
                  'jedes Mal mit <em>So have I</em> oder <em>Neither have '
                  'I</em> zu.',
        actWriteBrief='Schreibe einer Freundin oder einem Freund, die oder der '
                      'eine Woche bei dir wohnen wird. Sag, was sie oder er '
                      'mitbringen muss, was auf keinen Fall vergessen werden '
                      'darf, was ihr zusammen vorhabt und eine Sache, die ihr '
                      'beide noch nie gemacht habt und ausprobieren möchtet.',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
    'es': dict(
        actSpeakBrief='Tomad una consigna cada uno y seguid hasta que la otra '
                      'persona os haya devuelto las mismas estructuras.',
        actSpeak1='Tu compañero de piso ha vuelto a dejar la cocina hecha un '
                  'desastre. Dile qué tiene que hacer, qué no puede hacer y de '
                  'qué no hace falta que se ocupe.',
        actSpeak2='Planificad juntos el sábado que viene, sin poneros de '
                  'acuerdo al principio. Decid qué vais a hacer, qué creéis '
                  'que pasará y qué podríais hacer si llueve.',
        actSpeak3='Comparad vuestras vidas. Tres cosas que ya habéis hecho y '
                  'tres que no habéis hecho nunca &mdash; y mostrad acuerdo '
                  'cada vez con <em>So have I</em> o <em>Neither have I</em>.',
        actWriteBrief='Escribe a una amiga o un amigo que va a quedarse una '
                      'semana en tu casa. Di qué tiene que traer, qué no debe '
                      'olvidar, qué vais a hacer juntos y una cosa que ninguno '
                      'de los dos ha hecho nunca y que os gustaría probar.',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
    'fr': dict(
        actSpeakBrief='Prenez une consigne chacun et continuez jusqu’à ce que '
                      'votre partenaire vous ait renvoyé les mêmes structures.',
        actSpeak1='Ton colocataire a encore laissé la cuisine dans un état '
                  'épouvantable. Dis-lui ce qu’il doit faire, ce qu’il ne doit '
                  'surtout pas faire et ce dont il n’a pas besoin de s’occuper.',
        actSpeak2='Organisez samedi prochain ensemble, sans être d’accord au '
                  'départ. Dites ce que vous allez faire, ce qui va se passer '
                  'selon vous et ce que vous pourriez faire s’il pleut.',
        actSpeak3='Comparez vos vies. Trois choses que vous avez déjà faites, '
                  'trois que vous n’avez jamais faites &mdash; et approuvez à '
                  'chaque fois avec <em>So have I</em> ou <em>Neither have '
                  'I</em>.',
        actWriteBrief='Écris à un ami qui vient passer une semaine chez toi. '
                      'Dis ce qu’il doit apporter, ce qu’il ne doit pas '
                      'oublier, ce que vous allez faire ensemble et une chose '
                      'que ni l’un ni l’autre n’a jamais faite et que vous '
                      'aimeriez essayer.',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
    'it': dict(
        actSpeakBrief='Prendete una consegna a testa e andate avanti finché '
                      'l’altro non vi ha restituito le stesse strutture.',
        actSpeak1='Il tuo coinquilino ha lasciato di nuovo la cucina in '
                  'disordine. Digli che cosa deve fare, che cosa non deve fare '
                  'e di che cosa non ha bisogno di occuparsi.',
        actSpeak2='Organizzate insieme il prossimo sabato, all’inizio senza '
                  'essere d’accordo. Dite che cosa avete intenzione di fare, '
                  'che cosa pensate che succederà e che cosa potreste fare se '
                  'piove.',
        actSpeak3='Confrontate le vostre vite. Tre cose che avete già fatto, '
                  'tre che non avete mai fatto &mdash; e ogni volta trovatevi '
                  'd’accordo con <em>So have I</em> o <em>Neither have I</em>.',
        actWriteBrief='Scrivi a un amico che verrà a stare da te per una '
                      'settimana. Di’ che cosa deve portare, che cosa non deve '
                      'dimenticare, che cosa farete insieme e una cosa che '
                      'nessuno dei due ha mai fatto e che vorreste provare.',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
    'pt': dict(
        actSpeakBrief='Peguem numa consigna cada um e continuem até o outro '
                      'vos ter devolvido as mesmas estruturas.',
        actSpeak1='O teu colega de casa deixou outra vez a cozinha num estado '
                  'lastimável. Diz-lhe o que tem de fazer, o que não pode '
                  'fazer e aquilo de que não precisa de tratar.',
        actSpeak2='Planeiem juntos o próximo sábado, sem concordarem no '
                  'início. Digam o que vão fazer, o que acham que vai '
                  'acontecer e o que poderiam fazer se chover.',
        actSpeak3='Comparem as vossas vidas. Três coisas que já fizeram, três '
                  'que nunca fizeram &mdash; e concordem de cada vez com '
                  '<em>So have I</em> ou <em>Neither have I</em>.',
        actWriteBrief='Escreve a um amigo que vai ficar uma semana em tua '
                      'casa. Diz o que tem de trazer, o que não pode esquecer, '
                      'o que vão fazer juntos e uma coisa que nenhum dos dois '
                      'fez até hoje e que gostariam de experimentar.',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
    'ru': dict(
        actSpeakBrief='Возьмите по заданию и говорите, пока партнёр не вернёт '
                      'вам те же конструкции.',
        actSpeak1='Сосед снова оставил кухню в беспорядке. Скажите ему, что он '
                  'должен сделать, чего делать нельзя и о чём можно не '
                  'заботиться.',
        actSpeak2='Спланируйте субботу вместе, сначала не соглашаясь: что вы '
                  'собираетесь делать, что произойдёт и что могли бы сделать, '
                  'если дождь.',
        actSpeak3='Три дела, которые вы уже сделали, и три, которых не делали '
                  'никогда. Соглашайтесь каждый раз: <em>So have I</em>, '
                  '<em>Neither have I</em>.',
        actWriteBrief='Напишите другу, который приедет к вам на неделю: что '
                      'ему нужно взять, чего нельзя забыть, что вы будете '
                      'делать вместе и одну вещь, которую вы оба ещё не '
                      'пробовали.',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
    'ar': dict(
        actSpeakBrief='ليأخذ كل منكما مهمة، واستمرا حتى يستخدم الطرف الآخر '
                      'التراكيب نفسها في ردّه.',
        actSpeak1='ترك شريكك في السكن المطبخ في فوضى مرة أخرى. قل له ما الذي '
                  'يجب أن يفعله، وما الذي يُمنع عليه فعله، وما الذي لا داعي '
                  'لأن يشغل نفسه به.',
        actSpeak2='خطّطا معًا ليوم السبت المقبل، مع الاختلاف في البداية. قولا '
                  'ما تنويان فعله، وما تتوقعان حدوثه، وما يمكن أن تفعلاه بدلاً '
                  'من ذلك إذا أمطرت.',
        actSpeak3='قارنا حياتيكما: ثلاثة أشياء فعلتماها بالفعل، وثلاثة لم '
                  'تفعلاها قط &mdash; ووافقا في كل مرة بـ <em>So have I</em> '
                  'أو <em>Neither have I</em>.',
        actWriteBrief='اكتب إلى صديق سيقيم عندك أسبوعًا. قل له ما يجب أن '
                      'يُحضره، وما لا يجوز أن ينساه، وما ستفعلانه معًا، وشيئًا '
                      'واحدًا لم يجرّبه أي منكما من قبل وتودّان تجربته.',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
    'zh': dict(
        actSpeakBrief='每人认领一个话题，一直说到对方也用同样的结构回应你为止。',
        actSpeak1='室友又把厨房弄得一团糟。告诉他哪些事必须做、哪些事绝对不许做，'
                  '以及哪些事其实不必操心。',
        actSpeak2='一起安排下周六，先别急着达成一致。说说你们打算做什么、你觉得会'
                  '发生什么，以及如果下雨可能改做什么。',
        actSpeak3='比较你们的经历：三件已经做过的事，三件从来没做过的事——每次都用'
                  '<em>So have I</em> 或 <em>Neither have I</em> 来附和。',
        actWriteBrief='给一位要来你家住一周的朋友写信。写清楚他必须带什么、'
                      '千万不能忘记什么、你们打算一起做什么，以及一件你们两个都'
                      '从没做过、却都想试试的事。',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
    'ja': dict(
        actSpeakBrief='一つずつ担当し、相手が同じ構文を使って返してくるまで続けて'
                      'ください。',
        actSpeak1='ルームメイトがまたキッチンを散らかしました。何をしなければなら'
                  'ないか、何をしてはいけないか、何は気にしなくてよいかを伝えて'
                  'ください。',
        actSpeak2='次の土曜日の計画を一緒に立てます。最初は意見を合わせないこと。'
                  '何をするつもりか、何が起こると思うか、雨なら代わりに何をするか'
                  'を話してください。',
        actSpeak3='お互いの人生を比べます。もうやったこと3つ、一度もやったことが'
                  'ないこと3つ &mdash; そのたびに <em>So have I</em> か '
                  '<em>Neither have I</em> で応じてください。',
        actWriteBrief='一週間泊まりに来る友人に手紙を書いてください。何を持って'
                      'こなければならないか、何を絶対に忘れてはいけないか、一緒に'
                      '何をするつもりか、そして二人ともまだやったことがなく試して'
                      'みたいことを一つ書きます。',
        actPlaceholder='Hi Sam, I can’t wait for next week —'),
}

# The English name of each structure. Target language: identical in all ten.
SEC_LABELS = [
    'might', 'must / mustn&rsquo;t', 'have to', 'like + -ing',
    'be going to', 'will / won&rsquo;t', 'Past Simple', 'Present Perfect',
    'already / yet / just', 'ever / never', 'some / any', 'one / ones',
    'whose / possessive &rsquo;s', 'Adverbs of manner', 'So / Neither',
]

T = {}
for code in LANGS:
    u = UI[code]
    d = dict(SHARED)
    d['coverSub'] = u['sub']
    d['chipFocus'] = u['introEye']
    d['chipCount'] = u['h1']
    d['orTitle'] = u['h1']
    d['bankLabel'] = u['hintLabel']
    for n, tag in enumerate(u['typeTags']):
        d['orTag%s' % 'ABC'[n]] = tag
    # scoreMsg writes these with textContent — plain text only, and the
    # committed verdicts are already plain.
    for key, pair in zip(('resPerfect', 'resStrong', 'resMid', 'resLow'),
                         u['verdicts']):
        d[key] = '%s %s' % (pair[0], pair[1])
    for n, gloss in enumerate(SECTIONS[code]):
        d['sec%dE' % n] = gloss
        d['sec%dT' % n] = SEC_LABELS[n]
    for key, table in ACT_CHROME.items():
        d[key] = table[code]
    d.update(ACT[code])
    T[code] = d


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    return '{\n' + ',\n'.join(
        '    %s: %s' % (k, d[k] if k in LIFT
                        else json.dumps(d[k], ensure_ascii=False))
        for k in sorted(d)) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c in LANGS:
        m, x = base - set(T[c]), set(T[c]) - base
        print('%-3s %2d' % (c, len(T[c]) + len(LIFT)),
              ('MISSING %s' % sorted(m)) if m else 'complete',
              ('EXTRA %s' % sorted(x)) if x else '')
