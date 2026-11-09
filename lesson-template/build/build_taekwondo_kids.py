# -*- coding: utf-8 -*-
"""Grammar Dojo: Should Have, Must & Have To — Taekwondo English for Kids
(A2, German support). House style 2, 13 slides, on the Taekwondo/ plates.

Rebuilt 2026-11-06 from `taekwondo-english-kids.html`, a reference page:
three rules in German and English and fifteen example sentences with a
German line under each. Everything is kept: the rules are pill-tab cards in
EN/DE/ES, the examples are cards whose German line is the click-to-reveal
gloss (Spanish added). The practice lives on the sibling page,
taekwondo-exercises.html; this deck adds one scored task of its own — sort
nine situations by the form that fits them — so a learner checks the
rules before moving on, and three quick checks.

Changed: "must" was explained as "from inside" and "have to" as "from
outside" with no qualification. The cards keep that (it is the right first
rule for a child) and add that a written rule can say MUST.

Run from the repo root:  py lesson-template/build/build_taekwondo_kids.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H
import deck as D

SPEC = dict(
    out='taekwondo-english-kids.html',
    title='Grammar Dojo: Should Have, Must & Have To (A2)',
    folder='Taekwondo',
    scheme='rose',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09). The five live Taekwondo
    # plates plus Midjourney renders (his style images, --stylize 200, the
    # live plates' slate blue / coral / cream named in the prompt).
    plates={
        'hero': 'a black belt in a fighting stance, a red sun behind',
        'solo_kick': 'a student kicking high in an empty dojo',
        'pads_drill': 'a coach holding pads for a student’s kick',
        'handshake': 'two students shaking hands across a dojo',
        'talk': 'a folded white dobok with a black belt on a wooden bench in a dojo',
        'k-homework': 'a boy in a white dobok remembering his homework, an open schoolbag at the dojo door',
        'k-bow': 'children in white doboks bowing at the door of a dojo',
        'k-belt': 'a determined girl in a white dobok tying her belt, a black belt hanging on the wall behind',
        'talk2': 'two children in doboks sitting on the dojo floor talking after class',
        'results': 'a row of coloured belts hanging on hooks in a dojo',
    },
    pop={'hero': (None, 'square'), 'k-belt': (None, 'free'), 'talk2': (None, 'blob')},
    results='results',
)

SH = [('lDef', 'I <strong>should have kept</strong> my guard up!', 'k1'),
      ('lTim', 'I <strong>should have kicked</strong> earlier!', 'k2'),
      ('lMen', 'I <strong>should have stayed</strong> calmer.', 'k3'),
      ('lFoot', 'I <strong>should have moved</strong> my feet faster!', 'k4'),
      ('lAtt', 'I <strong>shouldn’t have jumped</strong> — too risky!', 'k5'),
      ('lMen', 'We <strong>should have practised</strong> more sparring.', 'k6')]
MU = [('lMust', 'I <strong>must train</strong> harder every day!', 'k7'),
      ('lMust', 'I <strong>must focus</strong> better in competitions.', 'k8'),
      ('lAtt', 'She <strong>must practise</strong> her roundhouse kick.', 'k9'),
      ('lMen', 'We <strong>mustn’t give up</strong> — keep fighting!', 'k10')]
HT = [('lRule', 'We <strong>have to bow</strong> when we enter the dojo.', 'k11'),
      ('lRule', 'He <strong>has to wear</strong> a white dobok.', 'k12'),
      ('lRule', 'She <strong>has to listen</strong> to the coach.', 'k13'),
      ('lPast', 'I <strong>had to do</strong> 50 push-ups after training!', 'k14'),
      ('lRule', 'We <strong>don’t have to fight</strong> today — just patterns!', 'k15')]


def cards(eyebrow_key, title_key, rows, E, cols=3):
    c = "\n          ".join(
        '<div class="card" style="padding:16px 20px">'
        '<span class="chip" style="background:var(--void);font-size:11px" data-i18n="%s">%s</span>'
        '<p class="prose gloss" data-tr="%s" style="margin-top:10px;font-size:19px;line-height:1.4">%s</p>'
        '</div>' % (lk, E[lk], tr, s) for lk, s, tr in rows)
    return '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:repeat(%d,1fr);gap:14px">
          %s
        </div>
      </div>
    </section>
''' % (eyebrow_key, E[eyebrow_key], title_key, E[title_key], cols, c)


T = {
    'en': dict(
        mcT='Choose the right move',
        kw1='A mistake in the past: SHOULD HAVE + participle → SHOULD HAVE DONE.',
        kw2='A rule from outside, with WE: HAVE TO.',
        kw3='You really want it: MUST + the base verb. No TO, no -S.',
        coverTitle='Grammar <br><em>Dojo!</em>',
        coverSub='Taekwondo English: three super moves for your English brain — SHOULD HAVE for oops moments, MUST from the heart, HAVE TO for dojo rules.',
        chipLevel='A2', chipFocus='should have · must · have to', chipCount='13 slides',
        eW='Warm-up', eR='The rule', eX='Examples', eS='Check', eT='Let’s talk',
        tk1T='Let’s talk!', tk2T='Let’s talk!',
        rT='Three super moves',
        rS1='When you wish you had done something differently. Oops!',
        rS2='SHOULD HAVE + the past participle (-ED or the 3rd form).',
        rM1='It comes from INSIDE: you feel it is necessary.',
        rM2='No past form: use HAD TO.',
        rH1='It comes from OUTSIDE: a rule, a teacher, a coach.',
        rH2='HE / SHE HAS TO. A written rule can also say MUST.',
        xSH='Should have: oops moments!', xMU='Must: from the heart!', xHT='Have to: dojo rules!',
        lDef='Defence', lTim='Timing', lMen='Mental', lFoot='Footwork', lAtt='Attack',
        lMust='Must', lRule='Have to', lPast='Had to',
        sortT='Which move fits?', sortHint='Click a situation, then the move that fits it.',
        sortWhy='A mistake in the past → SHOULD HAVE. Your own wish → MUST. A rule or a coach → HAVE TO.',
        binA='should have', binB='must', binC='have to',
        actTitle='My dojo', actUse='Use all three:',
        actSpeakBrief='In pairs. Talk about your training, your school or your sport.',
        actSpeak1='Say two things you SHOULD HAVE done better last week.',
        actSpeak2='Say one thing you MUST do, because YOU want to.',
        actSpeak3='Say two rules: what do you HAVE TO do at school or in training?',
        actWriteKind='Writing',
        actWriteBrief='Write five sentences (40–60 words) about your sport or your school: two with SHOULD HAVE, one with MUST and two with HAVE TO.',
        actPlaceholder='I should have …',
    ),
    'de': dict(
        mcT='Wähle den richtigen Move',
        kw1='Ein Fehler in der Vergangenheit: SHOULD HAVE + Partizip → SHOULD HAVE DONE.',
        kw2='Eine Regel von außen, mit WE: HAVE TO.',
        kw3='Du willst es wirklich: MUST + Grundform. Kein TO, kein -S.',
        coverTitle='Grammar <br><em>Dojo!</em>',
        coverSub='Taekwondo-Englisch: drei Super-Moves fürs Englisch-Gehirn — SHOULD HAVE für Oops-Momente, MUST von Herzen, HAVE TO für Dojo-Regeln.',
        chipLevel='A2', chipFocus='should have · must · have to', chipCount='13 Folien',
        eW='Zum Einstieg', eR='Die Regel', eX='Beispiele', eS='Prüfen', eT='Sprechen wir!',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!',
        rT='Drei Super-Moves',
        rS1='Wenn du wünschst, du hättest etwas anders gemacht. Oops! („hätte … sollen“)',
        rS2='SHOULD HAVE + Partizip (-ED oder 3. Form).',
        rM1='Kommt von INNEN: Du findest es selbst nötig.',
        rM2='Keine Vergangenheit: Nimm HAD TO.',
        rH1='Kommt von AUSSEN: eine Regel, eine Lehrerin, ein Coach.',
        rH2='HE / SHE HAS TO. Eine geschriebene Regel kann auch MUST sagen.',
        xSH='Should have: Oops-Momente!', xMU='Must: von Herzen!', xHT='Have to: Dojo-Regeln!',
        lDef='Verteidigung', lTim='Timing', lMen='Mental', lFoot='Beinarbeit', lAtt='Angriff',
        lMust='Must', lRule='Have to', lPast='Had to',
        sortT='Welcher Move passt?', sortHint='Klicke eine Situation an, dann den passenden Move.',
        sortWhy='Ein Fehler in der Vergangenheit → SHOULD HAVE. Dein eigener Wunsch → MUST. Eine Regel oder ein Coach → HAVE TO.',
        binA='should have', binB='must', binC='have to',
        actTitle='Mein Dojo', actUse='Verwende alle drei:',
        actSpeakBrief='Zu zweit. Sprecht über euer Training, eure Schule oder euren Sport.',
        actSpeak1='Sag zwei Dinge, die du letzte Woche besser hättest machen sollen (SHOULD HAVE).',
        actSpeak2='Sag eine Sache, die du tun musst, weil DU es willst (MUST).',
        actSpeak3='Sag zwei Regeln: Was musst du in der Schule oder im Training tun (HAVE TO)?',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib fünf Sätze (40–60 Wörter) über deinen Sport oder deine Schule: zwei mit SHOULD HAVE, einen mit MUST und zwei mit HAVE TO.',
        actPlaceholder='I should have …',
    ),
    'es': dict(
        mcT='Elige el movimiento correcto',
        kw1='Un error en el pasado: SHOULD HAVE + participio → SHOULD HAVE DONE.',
        kw2='Una regla de fuera, con WE: HAVE TO.',
        kw3='Lo quieres de verdad: MUST + verbo base. Sin TO, sin -S.',
        coverTitle='Grammar <br><em>Dojo!</em>',
        coverSub='Inglés de taekwondo: tres súper movimientos para tu cerebro en inglés — SHOULD HAVE para los momentos «¡uy!», MUST de corazón, HAVE TO para las reglas del dojo.',
        chipLevel='A2', chipFocus='should have · must · have to', chipCount='13 diapositivas',
        eW='Para empezar', eR='La regla', eX='Ejemplos', eS='Comprueba', eT='¡A conversar!',
        tk1T='¡A conversar!', tk2T='¡A conversar!',
        rT='Tres súper movimientos',
        rS1='Cuando te gustaría haber hecho algo de otra manera. ¡Uy! («debería haber …»)',
        rS2='SHOULD HAVE + participio (-ED o la 3.ª forma).',
        rM1='Viene de DENTRO: tú sientes que es necesario.',
        rM2='No tiene pasado: usa HAD TO.',
        rH1='Viene de FUERA: una regla, una profesora, un entrenador.',
        rH2='HE / SHE HAS TO. Una norma escrita también puede decir MUST.',
        xSH='Should have: ¡momentos «uy»!', xMU='Must: ¡de corazón!', xHT='Have to: ¡reglas del dojo!',
        lDef='Defensa', lTim='Tiempo', lMen='Mente', lFoot='Pies', lAtt='Ataque',
        lMust='Must', lRule='Have to', lPast='Had to',
        sortT='¿Qué movimiento encaja?', sortHint='Haz clic en una situación y después en el movimiento que encaja.',
        sortWhy='Un error en el pasado → SHOULD HAVE. Tu propio deseo → MUST. Una regla o un entrenador → HAVE TO.',
        binA='should have', binB='must', binC='have to',
        actTitle='Mi dojo', actUse='Usa los tres:',
        actSpeakBrief='En parejas. Hablen de su entrenamiento, su escuela o su deporte.',
        actSpeak1='Di dos cosas que deberías haber hecho mejor la semana pasada (SHOULD HAVE).',
        actSpeak2='Di una cosa que debes hacer porque TÚ quieres (MUST).',
        actSpeak3='Di dos reglas: ¿qué tienes que hacer en la escuela o en el entrenamiento (HAVE TO)?',
        actWriteKind='Escritura',
        actWriteBrief='Escribe cinco oraciones (40–60 palabras) sobre tu deporte o tu escuela: dos con SHOULD HAVE, una con MUST y dos con HAVE TO.',
        actPlaceholder='I should have …',
    ),
}
E = T['en']
SORT = D.sort_slide(
    [E['binA'], E['binB'], E['binC']],
    [('You lost — you were too slow.', 0), ('You forgot your belt yesterday.', 0), ('You didn’t warm up and hurt your leg.', 0),
     ('You want to win the next grading.', 1), ('You promise yourself to train every day.', 1), ('You really want a black belt.', 1),
     ('The coach says: bow!', 2), ('The dojo rule: white dobok.', 2), ('Your school starts at eight.', 2)],
    'eS', E['eS'], 'sortT', E['sortT'], 'sortHint', E['sortHint'], 'sortWhy', bin_keys=['binA', 'binB', 'binC'])

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Do you do taekwondo, karate or another sport?',
        'What are the rules where you train?',
        'What do you want to get better at?',
        'Do you sometimes make mistakes in a match or a game?',
        'Who is your coach or your favourite teacher?',
        'What do you have to wear for your sport?',
    ], 'talk', 3),
    ('stage',),
    ('rules', 'eR', 'rT', [
        ('should have + verb', ['rS1', 'rS2'], 'I <strong>should have kicked</strong> earlier!'),
        ('must + verb', ['rM1', 'rM2'], 'I <strong>must train</strong> harder!'),
        ('have to / has to + verb', ['rH1', 'rH2'], 'We <strong>have to bow</strong>.'),
    ], None),
    ('raw', None), ('raw', None), ('raw', None), ('raw', SORT),
    ('stage',),
    ('mc', 'eS', 'mcT', [
        dict(stem='Oops! I ____ my homework yesterday.', options=['should have done', 'should have do', 'should has done', 'should had done'], correct=0, why='kw1'),
        dict(stem='“We ____ bow when we enter the dojo.” — It’s a rule.', options=['have to', 'has to', 'should have', 'had'], correct=0, why='kw2'),
        dict(stem='“I ____ train harder — I really want my black belt!”', options=['must', 'must to', 'has to', 'musts'], correct=0, why='kw3'),
    ], ['k-homework', 'k-bow', 'k-belt'], None),
    ('talk', 'eT', 'tk2T', [
        'What <strong>should</strong> you <strong>have done</strong> better this week?',
        'What <strong>must</strong> you do this weekend?',
        'What do you <strong>have to</strong> do every morning?',
        'What did you <strong>have to</strong> do yesterday?',
        'What <strong>don’t</strong> you <strong>have to</strong> do in the holidays?',
        'What <strong>mustn’t</strong> you forget for training?',
    ], 'talk2', 3),
]
# the three example slides: two card columns beside their frame
SPEC['flow'][3] = ('raw', cards('eX', 'xSH', SH, E, cols=2), 'solo_kick')
SPEC['flow'][4] = ('raw', cards('eX', 'xMU', MU, E, cols=2), 'pads_drill')
SPEC['flow'][5] = ('raw', cards('eX', 'xHT', HT, E, cols=2), 'handshake')
SPEC['chips'] = ['should have', 'must', 'have to', 'had to', 'don’t have to', 'mustn’t']

GLOSS = {
    'de': dict(k1='Ich hätte meine Deckung oben halten sollen!', k2='Ich hätte früher kicken sollen!',
               k3='Ich hätte ruhiger bleiben sollen.', k4='Ich hätte meine Füße schneller bewegen sollen!',
               k5='Ich hätte nicht springen sollen — zu riskant!', k6='Wir hätten mehr Sparring üben sollen.',
               k7='Ich muss jeden Tag härter trainieren!', k8='Ich muss mich bei Wettkämpfen besser konzentrieren.',
               k9='Sie muss ihren Roundhouse-Kick üben.', k10='Wir dürfen nicht aufgeben — kämpft weiter!',
               k11='Wir müssen uns verbeugen, wenn wir das Dojo betreten.', k12='Er muss einen weißen Dobok tragen.',
               k13='Sie muss auf den Coach hören.', k14='Ich musste nach dem Training 50 Liegestütze machen!',
               k15='Wir müssen heute nicht kämpfen — nur Formen!'),
    'es': dict(k1='¡Debería haber mantenido la guardia alta!', k2='¡Debería haber pateado antes!',
               k3='Debería haber estado más tranquilo.', k4='¡Debería haber movido los pies más rápido!',
               k5='No debería haber saltado: ¡demasiado arriesgado!', k6='Deberíamos haber practicado más combate.',
               k7='¡Tengo que entrenar más cada día!', k8='Tengo que concentrarme mejor en las competiciones.',
               k9='Tiene que practicar su patada circular.', k10='¡No podemos rendirnos: sigan luchando!',
               k11='Tenemos que hacer una reverencia al entrar en el dojo.', k12='Tiene que llevar un dobok blanco.',
               k13='Tiene que escuchar al entrenador.', k14='¡Tuve que hacer 50 flexiones después del entrenamiento!',
               k15='Hoy no tenemos que pelear: ¡solo formas!'),
}

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T, GLOSS)
