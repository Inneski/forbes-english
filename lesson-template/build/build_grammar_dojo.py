# -*- coding: utf-8 -*-
"""文法道場 Grammar Dojo — Must, Have To, Mustn't, Don't Have To (A2, coding
edition, Japanese support). House style 1, 17 slides, EN / DE / ES / JA.

Rebuilt 2026-11-06 from `grammar-dojo.html`, a reference chart and ten
one-at-a-time items for software developers, each with a Japanese line
describing the situation. Japanese therefore ships with the house minimum
of German and Spanish; the situation line translates into every language.

All ten items are kept. Fixed:
  * Q1 (company policy) and Q6 (by law) offered both MUST and HAVE TO, and
    the old explanations themselves said MUST was also fine. MUST is now
    replaced by a wrong form (HAS TO with a plural subject), so the item
    tests what it says it tests.
  * Q9 "she must handle all the API work herself" is correct English;
    MUST is replaced by HAVE TO (wrong person).
  * Q8, typed, accepted only "will have to", though HAVE TO, MUST and NEED
    TO are all right before "tomorrow". It accepts them now and explains
    why WILL HAVE TO is the most explicit.
Added: a gap for DON'T HAVE TO, two sentence builds, speaking, activation.

Run from the repo root:  py lesson-template/build/build_grammar_dojo.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='grammar-dojo.html',
    title='Grammar Dojo — Must, Have To, Mustn’t, Don’t Have To (A2)',
    folder='GrammarDojo',
    scheme='slate',
    langs=('en', 'de', 'es', 'ja'),
    style='hs1',
    # Four items (A1, A3, B2, B3) are too long to sit beside any frame,
    # so they take the full width and the texture field (hs1.frame).
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): Midjourney plates, his style
    # images at --stylize 200, one per slide, briefs here.
    plates={
        'hero': 'a young developer with a laptop sitting cross-legged in a calm martial-arts dojo',
        'talk': 'a software team standing around a whiteboard covered in boxes and arrows',
        'a2': 'a developer hiding a golden key behind her back, a laptop open on the desk',
        'a4': 'a senior developer drawing branching lines on a whiteboard for a junior colleague',
        'b1': 'a server room, one data cabinet locked with a big padlock',
        'b4': 'a developer about to press a big red button, a colleague grabbing her arm',
        'o1': 'a developer reaching for a giant lever marked with a warning stripe',
        'o2': 'a circle of colleagues at a morning stand-up meeting, one chair empty',
        'talk2': 'two developers chatting in an office kitchen with mugs of tea',
        'results': 'a laptop on a tidy desk with a black belt folded beside it',
    },
    pop={'hero': (None, 'square'), 'talk2': (None, 'blob')},
    results='results',
    # the hint line under each stem (ctx) costs a row: tighter options keep
    # the answered state inside the slide (answered-overflow, en/de/es)
    css='html[data-style="editorial"] .slide:has(.q-ctx) .opt { padding-top: 7px; padding-bottom: 7px; }',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n, ctx='c%d' % n)


A = [
    q('According to company policy, all pull requests ____ be reviewed by at least two developers.',
      ['have to', 'has to', 'mustn’t', 'don’t have to'], 1),
    q('You ____ commit your .env file to the repository. It contains secret keys!',
      ['mustn’t', 'must', 'have to', 'don’t have to'], 2),
    q('Our stack supports JS and TS — you ____ use TypeScript if you prefer plain JavaScript.',
      ['don’t have to', 'doesn’t have to', 'mustn’t', 'don’t must'], 3),
    q('I really think every developer ____ understand how Git rebasing works — it’s fundamental!',
      ['must', 'have to', 'mustn’t', 'doesn’t have to'], 4),
]
B = [
    q('By law, all applications that store user data ____ comply with the GDPR.',
      ['have to', 'has to', 'don’t have to', 'mustn’t'], 6),
    q('— Do I need to join the daily stand-up? — No, it’s async. You ____ join if you’ve posted an update in Slack.',
      ['don’t have to', 'doesn’t have to', 'mustn’t', 'don’t must'], 7),
    q('She’s the only back-end developer this sprint, so she ____ handle all the API work herself.',
      ['has to', 'have to', 'mustn’t', 'doesn’t have to'], 9),
    q('You ____ run DROP TABLE in production without a backup — it’s irreversible!',
      ['mustn’t', 'must', 'have to', 'don’t have to'], 10),
]
APOS = lambda *xs: '|'.join(sorted({v for x in xs for v in (x, x.replace('’', "'"), x.replace("'", '’'))}))

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'What rules are there in your team’s code?',
        'What do you have to do before you push?',
        'What must every developer know?',
        'What is forbidden in production?',
        'Which meetings don’t you have to join?',
        'What did you have to fix last week?',
    ], 'talk', 3),
    ('stage',),
    ('rules', 'eR', 'rT', [
        ('must', ['rM1', 'rM2'], '// You <strong>must</strong> read the docs carefully.'),
        ('have to', ['rH1', 'rH2'], '// You <strong>have to</strong> push to a feature branch.'),
        ('mustn’t', ['rN1'], '// You <strong>mustn’t</strong> push to main directly.'),
        ('don’t have to', ['rD1'], '// You <strong>don’t have to</strong> use TypeScript.'),
    ], None),
    ('mc', 'e1', 'mcT', A, [None, 'a2', None, 'a4'], None),
    ('gap', 'e2', 'gapT', 'gHint', [
        ('The server was down, so we ______ deploy the hotfix by hand last night.', ['had to'], 'w5'),
        ('We ______ migrate the database before we can deploy v2.0 tomorrow.',
         [APOS('will have to', '’ll have to', 'have to', 'must', 'will need to', 'need to')], 'w8'),
        ('You ______ (not / have to) reply — this email is just for your information.',
         [APOS('don’t have to', 'do not have to')], 'gw1'),
    ]),
    ('stage',),
    ('mc', 'e3', 'mcT', B, ['b1', None, None, 'b4'], None),
    ('order', 'e3', 'orderT', 'orderHint', [
        (['You', 'mustn’t', 'push', 'to main', 'directly.'], ['don’t'], 'o1w'),
        (['She', 'didn’t', 'have to', 'attend', 'the stand-up.'], ['hasn’t'], 'o2w'),
    ], ['o1', 'o2'], None),
    ('talk', 'eT', 'tk2T', [
        'What <strong>mustn’t</strong> a new developer do on day one?',
        'What <strong>don’t</strong> you <strong>have to</strong> do on a Friday?',
        'What <strong>did</strong> you <strong>have to</strong> learn for your first job?',
        'What <strong>will</strong> your team <strong>have to</strong> change next year?',
        'Which rule <strong>must</strong> every team have, in your opinion?',
        'What <strong>has</strong> your manager <strong>got to</strong> decide this week?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['mustn’t', 'had to', 'don’t have to', 'has to', 'will have to', 'must']

W = {
    'en': [
        'A company rule comes from outside: HAVE TO. PULL REQUESTS is plural, so not HAS TO.',
        'MUSTN’T = it is forbidden. DON’T HAVE TO would mean it is optional — not the same!',
        'DON’T HAVE TO = no obligation; you can choose. MUSTN’T would forbid it.',
        'The speaker’s own strong opinion: MUST. EVERY DEVELOPER is singular, so not HAVE TO.',
        'MUST has no past form: the past of both is HAD TO.',
        'A law is an outside rule: HAVE TO (MUST is also used for laws). APPLICATIONS is plural, so not HAS TO.',
        'Not required, just optional: DON’T HAVE TO.',
        'Several things are right here: WILL HAVE TO is the most explicit about the future; HAVE TO, MUST and NEED TO also work.',
        'SHE → HAS TO: the situation forces her. HAVE TO is the wrong person.',
        'Strongly forbidden: MUSTN’T.',
    ],
    'de': [
        'Eine Firmenregel kommt von außen: HAVE TO. PULL REQUESTS ist Plural, also nicht HAS TO.',
        'MUSTN’T = es ist verboten („darf nicht“). DON’T HAVE TO hieße, es ist freiwillig — nicht dasselbe!',
        'DON’T HAVE TO = keine Pflicht („muss nicht“); du kannst wählen. MUSTN’T würde es verbieten.',
        'Die eigene feste Meinung des Sprechers: MUST. EVERY DEVELOPER ist Singular, also nicht HAVE TO.',
        'MUST hat keine Vergangenheitsform: Die Vergangenheit von beiden ist HAD TO.',
        'Ein Gesetz ist eine Regel von außen: HAVE TO (für Gesetze wird auch MUST benutzt). APPLICATIONS ist Plural, also nicht HAS TO.',
        'Nicht nötig, nur freiwillig: DON’T HAVE TO.',
        'Hier ist mehreres richtig: WILL HAVE TO zeigt die Zukunft am deutlichsten; HAVE TO, MUST und NEED TO gehen auch.',
        'SHE → HAS TO: Die Situation zwingt sie. HAVE TO ist die falsche Person.',
        'Streng verboten: MUSTN’T.',
    ],
    'es': [
        'Una norma de la empresa viene de fuera: HAVE TO. PULL REQUESTS es plural: no HAS TO.',
        'MUSTN’T = está prohibido. DON’T HAVE TO significaría que es opcional: ¡no es lo mismo!',
        'DON’T HAVE TO = no es obligatorio; puedes elegir. MUSTN’T lo prohibiría.',
        'La opinión firme de quien habla: MUST. EVERY DEVELOPER es singular, así que no HAVE TO.',
        'MUST no tiene pasado: el pasado de los dos es HAD TO.',
        'Una ley es una norma de fuera: HAVE TO (MUST también se usa para leyes). APPLICATIONS es plural, así que no HAS TO.',
        'No es necesario, es opcional: DON’T HAVE TO.',
        'Aquí hay varias respuestas correctas: WILL HAVE TO es la más clara sobre el futuro; HAVE TO, MUST y NEED TO también valen.',
        'SHE → HAS TO: la situación la obliga. HAVE TO es la persona equivocada.',
        'Totalmente prohibido: MUSTN’T.',
    ],
    'ja': [
        '会社のルールは外部からの義務なので HAVE TO。PULL REQUESTS は複数形なので HAS TO にはなりません。',
        'MUSTN’T は「禁止」です。DON’T HAVE TO だと「しなくてもいい」になり、意味がまったく違います！',
        'DON’T HAVE TO は「義務がない・選んでいい」。MUSTN’T だと禁止になってしまいます。',
        '話し手自身の強い意見なので MUST。EVERY DEVELOPER は単数なので HAVE TO にはなりません。',
        'MUST には過去形がありません。過去の義務はどちらも HAD TO です。',
        '法律は外部からのルールなので HAVE TO（法律には MUST も使われます）。APPLICATIONS は複数形なので HAS TO にはなりません。',
        '必要ない・任意なので DON’T HAVE TO。',
        'ここは複数の答えが正解です。未来をいちばん明確に示すのは WILL HAVE TO ですが、HAVE TO・MUST・NEED TO も使えます。',
        'SHE なので HAS TO。状況が彼女にそうさせています。HAVE TO は人称が違います。',
        '強い禁止なので MUSTN’T。',
    ],
}
CTX = {
    'en': ['Talking about the company’s code-review policy: a company rule.', 'A security warning: something absolutely forbidden.',
           'TypeScript is your choice here: you can use it or not.', 'Giving your own strong personal opinion.',
           '', 'Talking about laws and regulations.', 'Asking whether the stand-up is required.', '',
           'Talking about one colleague’s situation this sprint.', 'A danger warning: something you must never do.'],
    'de': ['Es geht um die Code-Review-Regel der Firma: eine Firmenregel.', 'Eine Sicherheitswarnung: etwas streng Verbotenes.',
           'TypeScript ist hier deine Wahl: Du kannst es benutzen oder nicht.', 'Du sagst deine eigene feste Meinung.',
           '', 'Es geht um Gesetze und Vorschriften.', 'Du fragst, ob das Stand-up Pflicht ist.', '',
           'Es geht um die Situation einer Kollegin in diesem Sprint.', 'Eine Gefahrenwarnung: etwas, das man nie tun darf.'],
    'es': ['La política de revisión de código: una norma de la empresa.', 'Un aviso de seguridad: algo totalmente prohibido.',
           'Aquí TypeScript es opcional: puedes usarlo o no.', 'Das tu propia opinión firme.',
           '', 'Hablas de leyes y normativas.', 'Preguntas si el stand-up es obligatorio.', '',
           'Hablas de la situación de una compañera en este sprint.', 'Un aviso de peligro: algo que nunca se debe hacer.'],
    'ja': ['コードレビューのポリシー（会社のルール）について話しています。', 'セキュリティの警告。絶対禁止のことを伝えています。',
           'TypeScript は使っても使わなくてもいい状況です（選択自由）。', '自分の強い個人的な意見として言っています。',
           '', '法律・規制について話しています。', 'スタンドアップミーティングが必須かどうか聞いています。', '',
           '今回のスプリントでの同僚の状況について話しています。', '危険な警告。絶対にしてはいけないことです。'],
}

T = {
    'en': dict(
        coverTitle='Grammar <br><em>Dojo</em>',
        coverSub='Coding edition: MUST, HAVE TO, MUSTN’T and DON’T HAVE TO in code reviews, deployments and stand-ups.',
        chipLevel='A2', chipFocus='must · have to · mustn’t · don’t have to', chipCount='17 slides',
        eW='Warm-up', eT='Let’s talk', eR='Reference chart', e1='Obligation', e2='Past and future', e3='Forbidden or optional?',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the right form',
        rT='Must vs have to: the quick reference',
        rM1='Your own authority, or a strong personal feeling.', rM2='No past form: use HAD TO.',
        rH1='Outside rules: laws, company policy.', rH2='All persons and tenses: HAS TO, HAD TO, WILL HAVE TO.',
        rN1='Forbidden. A strong warning.', rD1='No obligation: it’s optional. The opposite of MUSTN’T!',
        gapT='Write the missing words', gHint='Past, future or negative: write the form.',
        gw1='No obligation: DON’T HAVE TO.',
        orderT='Build the sentence', orderHint='Click the pieces in order. One piece is left over.',
        o1w='MUSTN’T + verb: forbidden. DON’T is left over: MUST never takes DO.',
        o2w='The past of DON’T HAVE TO is DIDN’T HAVE TO. HASN’T is left over.',
        actTitle='Team rules', actUse='Use at least four:',
        actSpeakBrief='In pairs: one of you is a team lead, the other is a new developer.',
        actSpeak1='Team lead: explain three things the new developer HAS TO do and two they MUSTN’T do.',
        actSpeak2='New developer: ask what you DON’T HAVE TO do in your first week.',
        actSpeak3='Swap roles. Talk about something you HAD TO fix in a hurry once.',
        actWriteKind='Writing',
        actWriteBrief='Write a short README section, “Rules for this repo” (80–100 words): what everyone HAS TO do, what you MUSTN’T do and what you DON’T HAVE TO do.',
        actPlaceholder='Everyone has to …',
    ),
    'de': dict(
        coverTitle='Grammar <br><em>Dojo</em>',
        coverSub='Coding-Ausgabe: MUST, HAVE TO, MUSTN’T und DON’T HAVE TO in Code-Reviews, Deployments und Stand-ups.',
        chipLevel='A2', chipFocus='must · have to · mustn’t · don’t have to', chipCount='17 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Übersicht', e1='Pflicht', e2='Vergangenheit und Zukunft', e3='Verboten oder freiwillig?',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die richtige Form',
        rT='Must und have to: die Kurzübersicht',
        rM1='Deine eigene Autorität oder ein starkes persönliches Gefühl.', rM2='Keine Vergangenheitsform: Nimm HAD TO.',
        rH1='Regeln von außen: Gesetze, Firmenregeln.', rH2='Alle Personen und Zeiten: HAS TO, HAD TO, WILL HAVE TO.',
        rN1='Verboten („darf nicht“). Eine starke Warnung.', rD1='Keine Pflicht („muss nicht“): freiwillig. Das Gegenteil von MUSTN’T!',
        gapT='Ergänze die fehlenden Wörter', gHint='Vergangenheit, Zukunft oder Verneinung: Schreib die Form.',
        gw1='Keine Pflicht: DON’T HAVE TO („musst nicht“).',
        orderT='Bilde den Satz', orderHint='Klicke die Teile der Reihe nach an. Ein Teil bleibt übrig.',
        o1w='MUSTN’T + Verb: verboten. DON’T bleibt übrig: MUST nimmt nie DO.',
        o2w='Die Vergangenheit von DON’T HAVE TO ist DIDN’T HAVE TO. HASN’T bleibt übrig.',
        actTitle='Teamregeln', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit: Eine Person ist Teamleitung, die andere ein neuer Entwickler.',
        actSpeak1='Teamleitung: Erklär drei Dinge, die der neue Entwickler tun muss (HAS TO), und zwei, die er nicht darf (MUSTN’T).',
        actSpeak2='Neuer Entwickler: Frag, was du in der ersten Woche nicht tun musst (DON’T HAVE TO).',
        actSpeak3='Tauscht die Rollen. Sprecht über etwas, das ihr einmal schnell reparieren musstet (HAD TO).',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib einen kurzen README-Abschnitt „Rules for this repo“ (80–100 Wörter): was alle tun müssen (HAS TO), was man nicht darf (MUSTN’T) und was man nicht tun muss (DON’T HAVE TO).',
        actPlaceholder='Everyone has to …',
    ),
    'es': dict(
        coverTitle='Grammar <br><em>Dojo</em>',
        coverSub='Edición programación: MUST, HAVE TO, MUSTN’T y DON’T HAVE TO en revisiones de código, despliegues y stand-ups.',
        chipLevel='A2', chipFocus='must · have to · mustn’t · don’t have to', chipCount='17 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='Tabla de referencia', e1='Obligación', e2='Pasado y futuro', e3='¿Prohibido u opcional?',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la forma correcta',
        rT='Must y have to: referencia rápida',
        rM1='Tu propia autoridad, o un sentimiento personal fuerte.', rM2='No tiene pasado: usa HAD TO.',
        rH1='Normas de fuera: leyes, políticas de empresa.', rH2='Todas las personas y tiempos: HAS TO, HAD TO, WILL HAVE TO.',
        rN1='Prohibido. Un aviso fuerte.', rD1='No es obligatorio: es opcional. ¡Lo contrario de MUSTN’T!',
        gapT='Escribe las palabras que faltan', gHint='Pasado, futuro o negativo: escribe la forma.',
        gw1='No es obligatorio: DON’T HAVE TO.',
        orderT='Construye la oración', orderHint='Haz clic en las piezas en orden. Sobra una pieza.',
        o1w='MUSTN’T + verbo: prohibido. Sobra DON’T: MUST nunca lleva DO.',
        o2w='El pasado de DON’T HAVE TO es DIDN’T HAVE TO. Sobra HASN’T.',
        actTitle='Normas del equipo', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas: uno lidera el equipo y el otro es un desarrollador nuevo.',
        actSpeak1='Líder: explica tres cosas que el nuevo desarrollador tiene que hacer (HAS TO) y dos que no puede hacer (MUSTN’T).',
        actSpeak2='Desarrollador nuevo: pregunta qué no tienes que hacer en tu primera semana (DON’T HAVE TO).',
        actSpeak3='Cambien los papeles. Hablen de algo que una vez tuvieron que arreglar deprisa (HAD TO).',
        actWriteKind='Escritura',
        actWriteBrief='Escribe una sección corta del README, «Rules for this repo» (80–100 palabras): lo que todos tienen que hacer (HAS TO), lo que no se puede hacer (MUSTN’T) y lo que no hace falta hacer (DON’T HAVE TO).',
        actPlaceholder='Everyone has to …',
    ),
    'ja': dict(
        coverTitle='Grammar <br><em>Dojo</em>',
        coverSub='コーディング編：コードレビュー、デプロイ、スタンドアップで使う MUST・HAVE TO・MUSTN’T・DON’T HAVE TO。',
        chipLevel='A2', chipFocus='must · have to · mustn’t · don’t have to', chipCount='17 スライド',
        eW='ウォームアップ', eT='話してみよう', eR='早見表', e1='義務', e2='過去と未来', e3='禁止？それとも任意？',
        tk1T='話してみよう！', tk2T='話してみよう！', mcT='正しい形を選ぼう',
        rT='must と have to の早見表',
        rM1='話し手自身の判断、または強い個人的な気持ち。', rM2='過去形はありません。HAD TO を使います。',
        rH1='外部のルール：法律、会社の規則。', rH2='すべての人称・時制で使えます：HAS TO、HAD TO、WILL HAVE TO。',
        rN1='禁止。強い警告。', rD1='義務がない：任意です。MUSTN’T の反対！',
        gapT='足りない語を書こう', gHint='過去・未来・否定：形を書きましょう。',
        gw1='義務がない：DON’T HAVE TO（しなくてもいい）。',
        orderT='文を組み立てよう', orderHint='ピースを順番にクリック。ひとつ余ります。',
        o1w='MUSTN’T + 動詞：禁止。DON’T が余ります。MUST は DO と一緒に使いません。',
        o2w='DON’T HAVE TO の過去は DIDN’T HAVE TO。HASN’T が余ります。',
        actTitle='チームのルール', actUse='少なくとも4つ使おう：',
        actSpeakBrief='ペアで：ひとりはチームリーダー、もうひとりは新しい開発者です。',
        actSpeak1='リーダー：新人がしなければならないこと（HAS TO）を3つ、してはいけないこと（MUSTN’T）を2つ説明しましょう。',
        actSpeak2='新人：最初の週にしなくてもいいこと（DON’T HAVE TO）を聞きましょう。',
        actSpeak3='役割を交代。以前急いで直さなければならなかったこと（HAD TO）について話しましょう。',
        actWriteKind='ライティング',
        actWriteBrief='README に「Rules for this repo」を書こう（80〜100語）：すること（HAS TO）、禁止（MUSTN’T）、しなくていいこと（DON’T HAVE TO）。',
        actPlaceholder='Everyone has to …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w
    for i, x in enumerate(CTX[c], 1):
        if x:
            T[c]['c%d' % i] = x

H.check_keys(T, SPEC['langs'])

if __name__ == '__main__':
    H.build(SPEC, T)
