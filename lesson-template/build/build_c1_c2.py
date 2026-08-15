# -*- coding: utf-8 -*-
"""Give camps one and two their future use, and the same timeline everyone
else now stands on.

Both camps already teach a future use in a single rule card — present
continuous for arrangements, present simple for timetables — and both bury it
among five other cards where it reads as a footnote. It is the opposite: it is
the use learners get wrong, because nothing on the page shows them that a
present tense can occupy future ground. So each camp gets its own section and
its own diagram, drawn on the identical line as camps five and seven, so the
four can be compared at a glance.

Camp one's block is the ripple from its own hero, moved along the line: the
same event, further out. Camp two's is the bedrock slab, standing where the
timetable says it will stand.
"""
import re, sys
sys.path.insert(0, 'lesson-template')
import sherpa_timeline as T

# ── the diagram for each camp ────────────────────────────────────────
def camp_one_svg(gid_suffix=""):
    """Two ripples on the same line: the one you are standing in, and the one
    already agreed further along. Both are clipped to the upper half so the
    line stays a line and the captions below it stay readable."""
    pink = [("0%", "#7A0F3E"), ("18%", "#C2185B"), ("42%", "#E0568F"),
            ("70%", "#F3B8CF"), ("100%", "#FBEAF0")]

    def dome(gid, cx, r, dashed):
        out = ['<circle cx="%d" cy="299" r="%d" fill="url(#%s)"/>' % (cx, r, gid)]
        for k in range(1, 8):
            d = ' stroke-dasharray="4 5"' if dashed else ''
            out.append('<circle cx="%d" cy="299" r="%.1f" fill="none" stroke="#C2185B" '
                       'stroke-width="1"%s opacity="%.2f"/>' % (cx, r * k / 8, d, 0.40 - 0.03 * k))
        return "\n      ".join(out)

    return '''<svg viewBox="0 0 640 344" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A timeline from past to future. A pink ripple rises from now, and a second, dashed ripple stands further along the line in the future.">
      <defs>
%s
%s
        <marker id="ah-rip" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill="#1c130c"/>
        </marker>
        <clipPath id="aboveLine"><rect x="0" y="0" width="640" height="299"/></clipPath>
      </defs>
      <rect x="0" y="0" width="640" height="344" fill="var(--paper)"/>
      <g clip-path="url(#aboveLine)">
      %s
      %s
      </g>
      <line x1="24" y1="299" x2="616" y2="299" stroke="#1c130c" stroke-width="2"
            marker-start="url(#ah-rip)" marker-end="url(#ah-rip)"/>
      %s
      <text x="150" y="26" text-anchor="middle" class="diagram-caption" fill="#8A7E84" style="letter-spacing:.14em" pointer-events="none">PAST</text>
      <text x="320" y="26" text-anchor="middle" class="diagram-caption" fill="#3E6A85" pointer-events="none">NOW</text>
      <text x="500" y="26" text-anchor="middle" class="diagram-caption" fill="#8A7E84" style="letter-spacing:.14em" pointer-events="none">FUTURE</text>
      <text x="320" y="192" text-anchor="middle" class="diagram-caption" fill="#7A0F3E" style="letter-spacing:.06em" pointer-events="none" data-i18n="dgNowCap">HAPPENING</text>
      <text x="500" y="192" text-anchor="middle" class="diagram-caption" fill="#7A0F3E" style="letter-spacing:.06em" pointer-events="none" data-i18n="dgFutCap">ARRANGED</text>
      <text x="320" y="319" text-anchor="middle" class="dg-reveal-1" font-family="Inter, sans-serif" font-size="11.5" fill="#8A6070" pointer-events="none" data-i18n="dgNowSub">right now, still moving</text>
      <text x="500" y="319" text-anchor="middle" class="dg-reveal-1" font-family="Inter, sans-serif" font-size="11.5" fill="#8A6070" pointer-events="none" data-i18n="dgFutSub">fixed, with a time and a place</text>
    </svg>''' % (
        T.radial_defs("ripNow", pink), T.radial_defs("ripFut", pink),
        dome("ripFut", 500, 88, True), dome("ripNow", 320, 88, False), T.NOW_COL)


def camp_two_svg():
    gid = "bedrockFade"
    navy = T.ramp('#3E6EA6', '#1E4372', '#0C2340', '#050F1C')
    svg = T.diagram(gid, navy, None, 'TIMETABLE',
                    'a printed time, not a plan', 'timetable',
                    label_ink='#7C8899', classes='',
                    aria=('A timeline from past to future. Now is a narrow column at the '
                          'centre; a scheduled event stands as a block in the future.'))
    svg = svg.replace('<svg class=""', '<svg')
    # the captions in this camp are translatable like the rest of the page
    svg = svg.replace('>TIMETABLE<', ' data-i18n="dgCap">TIMETABLE<')
    svg = svg.replace('>a printed time, not a plan<', ' data-i18n="dgSub">a printed time, not a plan<')
    svg = svg.replace('class="dg-reveal" data-for="shape-timetable"', 'class="dg-reveal-1"')
    svg = svg.replace('class="dg-reveal" data-for="shape-now"', 'class="dg-reveal-1"')
    return svg


# ── section markup ───────────────────────────────────────────────────
GLOBE = ('<div class="lang-globe-wrap" data-globe-section="%s"><button type="button" '
         'class="lang-globe-btn" aria-label="Translate this section" aria-haspopup="true" '
         'aria-expanded="false">&#127760;</button><div class="lang-menu" hidden></div></div>')

MARKER_CAL = ('<div class="marker"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" '
              'stroke-width="2"><rect x="3" y="4" width="18" height="17" rx="2"/>'
              '<path d="M3 9h18M8 2v4M16 2v4"/></svg></div>')


def section(cid, label_key, label, title_key, title, intro_key, intro, cards, svg, extra_css_id):
    rows = "\n".join(
        '''        <div class="rule-card">
          <h3 data-i18n="%s">%s</h3>
          <p data-i18n="%s">%s</p>
          <div class="ex" data-i18n="%s">%s</div>
        </div>''' % c for c in cards)
    return '''<div class="camp" id="%s">
      %s
      <div class="camp-label" data-i18n="%s">%s</div>
      <h2 data-i18n="%s">%s</h2>
      %s
      <div class="diagram-card">
        <p class="diagram-intro" data-i18n="%s">%s</p>
        <div class="diagram-stage">
          %s
        </div>
      </div>
      <div class="rule-grid" style="margin-top:18px">
%s
      </div>
    </div>

    ''' % (cid, MARKER_CAL, label_key, label, title_key, title, GLOBE % cid,
           intro_key, intro, svg, rows)


DIAGRAM_CSS = '''
  /* ── the shared route timeline ── */
  .diagram-card{background:var(--card);border:1px solid var(--accent-light);border-radius:var(--radius);padding:22px 22px 18px;margin-top:18px;}
  .diagram-intro{font-size:14px;color:var(--ink-soft);margin:0 0 16px;max-width:62ch;}
  .diagram-stage{width:100%;background:var(--paper);border:1px solid var(--accent-light);border-radius:var(--radius);padding:12px;}
  .diagram-stage svg{width:100%;height:auto;display:block;}
  .diagram-caption{font-family:'Inter',sans-serif;font-weight:700;font-size:15px;letter-spacing:.04em;}
  .dg-reveal-1{opacity:1;}
'''

# ═════════════════════════════════════════════════════════════════════
# CAMP ONE
# ═════════════════════════════════════════════════════════════════════
p1 = 'sherpa-tensing-camp-one-present-continuous.html'
s1 = open(p1, encoding='utf-8').read()

C1_CARDS = [
    ('fut1h', 'It has to be arranged',
     'fut1p', 'Somebody has agreed it. There is a time, and usually a place.',
     'fut1ex', '"We\'re meeting the Berlin team at nine on Thursday."'),
    ('fut2h', 'Not for predictions',
     'fut2p', 'If nobody arranged it, the present continuous cannot carry it.',
     'fut2ex', '"It\'s raining tomorrow." &#10007; &nbsp;"It\'s going to rain." &#10003;'),
    ('fut3h', 'The diary test',
     'fut3p', 'If you could write it in a diary, this tense will take it.',
     'fut3ex', '"I\'m flying to Oslo on the 14th."'),
]

C1_SECTION = section(
    'future', 'labelFuture', 'A ripple further along',
    'futureTitle', 'The arrangement you\'ve already made',
    'futureIntro',
    ('Present continuous is not only about now. Move the same ripple along the line and it '
     'becomes an arrangement: something already fixed between people, sitting in future time '
     'and behaving exactly as if it were under way. The dashed rings are the difference &mdash; '
     'the event is settled, but it has not started.'),
    C1_CARDS, camp_one_svg(), 'future')

anchor = s1.index('<div class="camp" id="quiz">')
s1 = s1[:anchor] + C1_SECTION + s1[anchor:]
s1 = s1.replace('  .quiz-card{', DIAGRAM_CSS + '  .quiz-card{', 1)

C1_I18N = {
 'en': dict(labelFuture='A ripple further along', futureTitle="The arrangement you've already made",
   futureIntro=('Present continuous is not only about now. Move the same ripple along the line and it becomes an '
                'arrangement: something already fixed between people, sitting in future time and behaving exactly as '
                'if it were under way. The dashed rings are the difference — the event is settled, but it has not started.'),
   fut1h='It has to be arranged', fut1p='Somebody has agreed it. There is a time, and usually a place.',
   fut1ex='"We\'re meeting the Berlin team at nine on Thursday."',
   fut2h='Not for predictions', fut2p='If nobody arranged it, the present continuous cannot carry it.',
   fut2ex='"It\'s raining tomorrow." ✗  "It\'s going to rain." ✓',
   fut3h='The diary test', fut3p='If you could write it in a diary, this tense will take it.',
   fut3ex='"I\'m flying to Oslo on the 14th."',
   dgNowCap='HAPPENING', dgFutCap='ARRANGED',
   dgNowSub='right now, still moving', dgFutSub='fixed, with a time and a place'),
 'de': dict(labelFuture='Eine Welle weiter vorn', futureTitle='Die Verabredung, die schon steht',
   futureIntro=('Das Present Continuous betrifft nicht nur das Jetzt. Verschiebt man dieselbe Welle auf der Linie, wird '
                'daraus eine feste Verabredung: etwas, das zwischen Menschen bereits abgemacht ist, in der Zukunft liegt '
                'und sich verhält, als liefe es schon. Die gestrichelten Ringe zeigen den Unterschied — die Sache steht, '
                'begonnen hat sie noch nicht.'),
   fut1h='Es muss verabredet sein', fut1p='Jemand hat zugestimmt. Es gibt eine Uhrzeit und meist einen Ort.',
   fut1ex='"We\'re meeting the Berlin team at nine on Thursday."',
   fut2h='Nicht für Vorhersagen', fut2p='Hat niemand es verabredet, trägt das Present Continuous es nicht.',
   fut2ex='"It\'s raining tomorrow." ✗  "It\'s going to rain." ✓',
   fut3h='Der Kalendertest', fut3p='Was im Kalender stehen könnte, verträgt diese Zeitform.',
   fut3ex='"I\'m flying to Oslo on the 14th."',
   dgNowCap='LÄUFT', dgFutCap='VERABREDET',
   dgNowSub='jetzt gerade, noch in Bewegung', dgFutSub='fest, mit Zeit und Ort'),
 'fr': dict(labelFuture='Une onde plus loin', futureTitle="L'arrangement déjà pris",
   futureIntro=("Le présent continu ne parle pas que du maintenant. Déplacez la même onde sur la ligne et elle devient "
                "un arrangement : quelque chose de déjà convenu entre des personnes, situé dans le futur et se comportant "
                "comme si c'était en cours. Les cercles en pointillés font la différence — c'est fixé, mais cela n'a pas commencé."),
   fut1h='Ce doit être convenu', fut1p="Quelqu'un a donné son accord. Il y a une heure, et souvent un lieu.",
   fut1ex='"We\'re meeting the Berlin team at nine on Thursday."',
   fut2h='Pas pour les prévisions', fut2p="Si personne ne l'a organisé, le présent continu ne le porte pas.",
   fut2ex='"It\'s raining tomorrow." ✗  "It\'s going to rain." ✓',
   fut3h="Le test de l'agenda", fut3p="Si vous pouviez l'écrire dans un agenda, ce temps convient.",
   fut3ex='"I\'m flying to Oslo on the 14th."',
   dgNowCap='EN COURS', dgFutCap='CONVENU',
   dgNowSub="en ce moment, encore en mouvement", dgFutSub='fixé, avec heure et lieu'),
 'it': dict(labelFuture='Un’onda più avanti', futureTitle='L’impegno che hai già preso',
   futureIntro=('Il present continuous non riguarda solo l’adesso. Sposta la stessa onda lungo la linea e diventa un '
                'accordo: qualcosa di già fissato fra persone, collocato nel futuro e trattato come se fosse in corso. '
                'I cerchi tratteggiati sono la differenza — è deciso, ma non è ancora cominciato.'),
   fut1h='Deve essere concordato', fut1p='Qualcuno ha detto di sì. C’è un orario, e di solito un luogo.',
   fut1ex='"We\'re meeting the Berlin team at nine on Thursday."',
   fut2h='Non per le previsioni', fut2p='Se nessuno l’ha organizzato, il present continuous non lo regge.',
   fut2ex='"It\'s raining tomorrow." ✗  "It\'s going to rain." ✓',
   fut3h='La prova dell’agenda', fut3p='Se lo scriveresti in agenda, questo tempo lo accetta.',
   fut3ex='"I\'m flying to Oslo on the 14th."',
   dgNowCap='IN CORSO', dgFutCap='FISSATO',
   dgNowSub='proprio ora, ancora in movimento', dgFutSub='fisso, con orario e luogo'),
 'es': dict(labelFuture='Una onda más adelante', futureTitle='La cita que ya has hecho',
   futureIntro=('El presente continuo no habla solo del ahora. Mueve la misma onda por la línea y se convierte en un '
                'compromiso: algo ya acordado entre personas, situado en el futuro y tratado como si estuviera en marcha. '
                'Los círculos discontinuos marcan la diferencia: está cerrado, pero aún no ha empezado.'),
   fut1h='Tiene que estar acordado', fut1p='Alguien ha dicho que sí. Hay una hora y, normalmente, un lugar.',
   fut1ex='"We\'re meeting the Berlin team at nine on Thursday."',
   fut2h='No para predicciones', fut2p='Si nadie lo ha organizado, el presente continuo no lo sostiene.',
   fut2ex='"It\'s raining tomorrow." ✗  "It\'s going to rain." ✓',
   fut3h='La prueba de la agenda', fut3p='Si lo escribirías en una agenda, este tiempo lo admite.',
   fut3ex='"I\'m flying to Oslo on the 14th."',
   dgNowCap='EN MARCHA', dgFutCap='ACORDADO',
   dgNowSub='ahora mismo, todavía en movimiento', dgFutSub='fijo, con hora y lugar'),
 'pl': dict(labelFuture='Fala dalej na osi', futureTitle='Umówiona już rzecz',
   futureIntro=('Present continuous nie dotyczy wyłącznie teraz. Przesuń tę samą falę wzdłuż linii, a stanie się '
                'ustaleniem: czymś już uzgodnionym między ludźmi, leżącym w przyszłości i traktowanym tak, jakby '
                'już trwało. Przerywane okręgi to właśnie różnica — sprawa jest ustalona, ale się nie zaczęła.'),
   fut1h='Musi być umówione', fut1p='Ktoś się zgodził. Jest godzina, a zwykle i miejsce.',
   fut1ex='"We\'re meeting the Berlin team at nine on Thursday."',
   fut2h='Nie do przewidywań', fut2p='Jeśli nikt tego nie umówił, present continuous tego nie udźwignie.',
   fut2ex='"It\'s raining tomorrow." ✗  "It\'s going to rain." ✓',
   fut3h='Test kalendarza', fut3p='Jeśli dałoby się to wpisać do kalendarza, ten czas to przyjmie.',
   fut3ex='"I\'m flying to Oslo on the 14th."',
   dgNowCap='TRWA', dgFutCap='UMÓWIONE',
   dgNowSub='właśnie teraz, wciąż w ruchu', dgFutSub='ustalone, z godziną i miejscem'),
 'ru': dict(labelFuture='Волна дальше по линии', futureTitle='Договорённость, которая уже есть',
   futureIntro=('Present continuous — не только про сейчас. Сдвиньте ту же волну по линии, и она станет договорённостью: '
                'тем, о чём люди уже условились, что лежит в будущем и ведёт себя так, будто уже идёт. Пунктирные круги — '
                'в этом и разница: дело решено, но ещё не началось.'),
   fut1h='Должно быть договорено', fut1p='Кто-то согласился. Есть время и обычно место.',
   fut1ex='"We\'re meeting the Berlin team at nine on Thursday."',
   fut2h='Не для прогнозов', fut2p='Если никто не договаривался, present continuous этого не выдержит.',
   fut2ex='"It\'s raining tomorrow." ✗  "It\'s going to rain." ✓',
   fut3h='Проверка ежедневником', fut3p='Если это можно записать в ежедневник, время подходит.',
   fut3ex='"I\'m flying to Oslo on the 14th."',
   dgNowCap='ИДЁТ', dgFutCap='НАЗНАЧЕНО',
   dgNowSub='прямо сейчас, ещё в движении', dgFutSub='твёрдо, со временем и местом'),
 'zh': dict(labelFuture='更远处的一圈涟漪', futureTitle='你已经约好的事',
   futureIntro=('现在进行时不只讲此刻。把同一圈涟漪沿着时间线往前挪，它就成了约定：人与人之间已经敲定、'
                '落在未来、却像已经在进行的事。虚线圆圈就是区别——事情定了，但还没开始。'),
   fut1h='必须是约好的', fut1p='有人答应了。有时间，通常还有地点。',
   fut1ex='"We\'re meeting the Berlin team at nine on Thursday."',
   fut2h='不用来预测', fut2p='没有人安排过的事，现在进行时撑不住。',
   fut2ex='"It\'s raining tomorrow." ✗  "It\'s going to rain." ✓',
   fut3h='日程本测试', fut3p='能写进日程本的事，这个时态就接得住。',
   fut3ex='"I\'m flying to Oslo on the 14th."',
   dgNowCap='正在发生', dgFutCap='已约定',
   dgNowSub='此刻，仍在进行', dgFutSub='已定，有时间有地点'),
}

def inject_i18n(src, table, label):
    """Add the new keys to each language block of an existing I18N object."""
    for code, entries in table.items():
        m = re.search(r'\n  %s: \{' % code, src)
        if not m:
            print('   !! no %s block in %s' % (code, label)); continue
        # find the end of this language object
        i = m.end(); depth = 1; j = i
        while depth and j < len(src):
            if src[j] == '{': depth += 1
            elif src[j] == '}': depth -= 1
            j += 1
        body = ",\n" + ",\n".join(
            '    %s: %s' % (k, json_str(v)) for k, v in entries.items()) + "\n  "
        src = src[:j-1].rstrip().rstrip(',') + body + src[j-1:]
    return src

def json_str(v):
    return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'

s1 = inject_i18n(s1, C1_I18N, 'camp one')
open(p1, 'w', encoding='utf-8').write(s1)
print('camp one: section + %d language blocks' % len(C1_I18N))


# ═════════════════════════════════════════════════════════════════════
# CAMP TWO
# ═════════════════════════════════════════════════════════════════════
p2 = 'sherpa-tensing-camp-two-present-simple.html'
s2 = open(p2, encoding='utf-8').read()

C2_CARDS = [
    ('sch1h', 'Timetables and programmes',
     'sch1p', 'Trains, flights, films, lessons &mdash; anything with a published time.',
     'sch1ex', '"The train leaves at 6:40." &middot; "The film starts at eight."'),
    ('sch2h', 'Somebody else set the time',
     'sch2p', 'You did not decide it and you cannot move it. That is the test.',
     'sch2ex', '"Our flight lands at midnight."'),
    ('sch3h', 'Not your own plans',
     'sch3p', 'A personal arrangement takes the present continuous instead.',
     'sch3ex', '"I meet Ana tomorrow." &#10007; &nbsp;"I\'m meeting Ana tomorrow." &#10003;'),
]

C2_SECTION = section(
    'scheduled', 'labelSched', 'Printed on the wall',
    'schedTitle', 'The future that is already on a timetable',
    'schedIntro',
    ('The bedrock reaches further than it looks. When a time has been published by somebody else '
     '&mdash; a railway, a cinema, a school &mdash; English treats it as a fact rather than a plan, '
     'and a fact takes the present simple even when it happens next week. The block stands in '
     'future time, but it is the same solid ground.'),
    C2_CARDS, camp_two_svg(), 'scheduled')

anchor = s2.index('<div class="camp" id="quiz">')
s2 = s2[:anchor] + C2_SECTION + s2[anchor:]
s2 = s2.replace('  .quiz-card{', DIAGRAM_CSS + '  .quiz-card{', 1)

C2_I18N = {
 'en': dict(labelSched='Printed on the wall', schedTitle='The future that is already on a timetable',
   schedIntro=('The bedrock reaches further than it looks. When a time has been published by somebody else — a railway, '
               'a cinema, a school — English treats it as a fact rather than a plan, and a fact takes the present simple '
               'even when it happens next week. The block stands in future time, but it is the same solid ground.'),
   sch1h='Timetables and programmes', sch1p='Trains, flights, films, lessons — anything with a published time.',
   sch1ex='"The train leaves at 6:40." · "The film starts at eight."',
   sch2h='Somebody else set the time', sch2p='You did not decide it and you cannot move it. That is the test.',
   sch2ex='"Our flight lands at midnight."',
   sch3h='Not your own plans', sch3p='A personal arrangement takes the present continuous instead.',
   sch3ex='"I meet Ana tomorrow." ✗  "I\'m meeting Ana tomorrow." ✓',
   dgCap='TIMETABLE', dgSub='a printed time, not a plan'),
 'de': dict(labelSched='Aushang an der Wand', schedTitle='Die Zukunft, die schon im Fahrplan steht',
   schedIntro=('Der Grundfels reicht weiter, als er aussieht. Wenn eine Zeit von jemand anderem veröffentlicht wurde — '
               'von einer Bahn, einem Kino, einer Schule —, behandelt das Englische sie als Tatsache und nicht als Plan, '
               'und eine Tatsache steht im Present Simple, auch wenn sie nächste Woche eintritt. Der Block steht in der '
               'Zukunft, ist aber derselbe feste Boden.'),
   sch1h='Fahrpläne und Programme', sch1p='Züge, Flüge, Filme, Unterricht — alles mit veröffentlichter Uhrzeit.',
   sch1ex='"The train leaves at 6:40." · "The film starts at eight."',
   sch2h='Die Zeit hat jemand anderes gesetzt', sch2p='Du hast sie nicht bestimmt und kannst sie nicht verschieben. Das ist der Test.',
   sch2ex='"Our flight lands at midnight."',
   sch3h='Nicht für eigene Pläne', sch3p='Eine persönliche Verabredung steht im Present Continuous.',
   sch3ex='"I meet Ana tomorrow." ✗  "I\'m meeting Ana tomorrow." ✓',
   dgCap='FAHRPLAN', dgSub='eine gedruckte Zeit, kein Plan'),
 'fr': dict(labelSched='Affiché au mur', schedTitle="Le futur qui figure déjà à l'horaire",
   schedIntro=("Le socle va plus loin qu'il n'y paraît. Quand une heure a été publiée par quelqu'un d'autre — une "
               "compagnie ferroviaire, un cinéma, une école — l'anglais y voit un fait et non un projet, et un fait prend "
               "le présent simple, même s'il a lieu la semaine prochaine. Le bloc se tient dans le futur, mais c'est le "
               "même sol solide."),
   sch1h='Horaires et programmes', sch1p='Trains, vols, films, cours — tout ce qui a une heure publiée.',
   sch1ex='"The train leaves at 6:40." · "The film starts at eight."',
   sch2h="L'heure vient d'ailleurs", sch2p="Vous ne l'avez pas décidée et vous ne pouvez pas la déplacer. C'est le test.",
   sch2ex='"Our flight lands at midnight."',
   sch3h='Pas vos propres projets', sch3p='Un arrangement personnel prend le présent continu.',
   sch3ex='"I meet Ana tomorrow." ✗  "I\'m meeting Ana tomorrow." ✓',
   dgCap='HORAIRE', dgSub='une heure imprimée, pas un projet'),
 'it': dict(labelSched='Affisso al muro', schedTitle='Il futuro che è già sull’orario',
   schedIntro=('La roccia madre arriva più lontano di quanto sembri. Quando un orario è stato pubblicato da qualcun altro '
               '— una ferrovia, un cinema, una scuola — l’inglese lo tratta come un fatto e non come un piano, e un fatto '
               'vuole il present simple anche se accade la settimana prossima. Il blocco sta nel futuro, ma è lo stesso '
               'terreno solido.'),
   sch1h='Orari e programmi', sch1p='Treni, voli, film, lezioni — tutto ciò che ha un orario pubblicato.',
   sch1ex='"The train leaves at 6:40." · "The film starts at eight."',
   sch2h='L’orario l’ha deciso un altro', sch2p='Non l’hai scelto tu e non puoi spostarlo. È questa la prova.',
   sch2ex='"Our flight lands at midnight."',
   sch3h='Non i tuoi piani', sch3p='Un impegno personale vuole il present continuous.',
   sch3ex='"I meet Ana tomorrow." ✗  "I\'m meeting Ana tomorrow." ✓',
   dgCap='ORARIO', dgSub='un orario stampato, non un piano'),
 'es': dict(labelSched='Colgado en la pared', schedTitle='El futuro que ya está en el horario',
   schedIntro=('La roca madre llega más lejos de lo que parece. Cuando otra persona ha publicado una hora —una compañía '
               'de trenes, un cine, una escuela—, el inglés la trata como un hecho y no como un plan, y un hecho lleva '
               'presente simple aunque ocurra la semana que viene. El bloque está en el futuro, pero es el mismo suelo firme.'),
   sch1h='Horarios y programaciones', sch1p='Trenes, vuelos, películas, clases: todo lo que tiene hora publicada.',
   sch1ex='"The train leaves at 6:40." · "The film starts at eight."',
   sch2h='La hora la puso otro', sch2p='No la decidiste tú y no puedes moverla. Esa es la prueba.',
   sch2ex='"Our flight lands at midnight."',
   sch3h='No para tus planes', sch3p='Una cita personal lleva presente continuo.',
   sch3ex='"I meet Ana tomorrow." ✗  "I\'m meeting Ana tomorrow." ✓',
   dgCap='HORARIO', dgSub='una hora impresa, no un plan'),
 'pl': dict(labelSched='Wywieszone na ścianie', schedTitle='Przyszłość, która jest już w rozkładzie',
   schedIntro=('Skała macierzysta sięga dalej, niż się wydaje. Gdy godzinę ogłosił ktoś inny — kolej, kino, szkoła — '
               'angielski traktuje ją jak fakt, a nie plan, a fakt wymaga present simple, nawet jeśli wydarzy się w '
               'przyszłym tygodniu. Blok stoi w przyszłości, ale to ten sam twardy grunt.'),
   sch1h='Rozkłady i programy', sch1p='Pociągi, loty, filmy, lekcje — wszystko z ogłoszoną godziną.',
   sch1ex='"The train leaves at 6:40." · "The film starts at eight."',
   sch2h='Godzinę ustalił ktoś inny', sch2p='Nie ty o niej zdecydowałeś i nie możesz jej przesunąć. To jest test.',
   sch2ex='"Our flight lands at midnight."',
   sch3h='Nie twoje własne plany', sch3p='Osobiste ustalenie wymaga present continuous.',
   sch3ex='"I meet Ana tomorrow." ✗  "I\'m meeting Ana tomorrow." ✓',
   dgCap='ROZKŁAD', dgSub='wydrukowana godzina, nie plan'),
 'ru': dict(labelSched='Вывешено на стене', schedTitle='Будущее, которое уже в расписании',
   schedIntro=('Основание тянется дальше, чем кажется. Если время объявил кто-то другой — железная дорога, кинотеатр, '
               'школа — английский считает это фактом, а не планом, а факт требует present simple, даже если событие '
               'будет на следующей неделе. Блок стоит в будущем, но это та же твёрдая порода.'),
   sch1h='Расписания и программы', sch1p='Поезда, рейсы, фильмы, уроки — всё, у чего есть объявленное время.',
   sch1ex='"The train leaves at 6:40." · "The film starts at eight."',
   sch2h='Время назначил не ты', sch2p='Ты его не выбирал и не можешь сдвинуть. Это и есть проверка.',
   sch2ex='"Our flight lands at midnight."',
   sch3h='Не про твои планы', sch3p='Личная договорённость требует present continuous.',
   sch3ex='"I meet Ana tomorrow." ✗  "I\'m meeting Ana tomorrow." ✓',
   dgCap='РАСПИСАНИЕ', dgSub='напечатанное время, а не план'),
 'zh': dict(labelSched='贴在墙上的那张表', schedTitle='已经写进时刻表的未来',
   schedIntro=('基岩延伸得比看上去更远。当时间是别人公布的——铁路、影院、学校——英语把它当作事实而不是计划，'
               '而事实要用一般现在时，哪怕事情下周才发生。方块站在未来，但仍是同一块坚实的地面。'),
   sch1h='时刻表与节目单', sch1p='火车、航班、电影、课程——凡是有公布时间的。',
   sch1ex='"The train leaves at 6:40." · "The film starts at eight."',
   sch2h='时间是别人定的', sch2p='不是你决定的，你也挪不动。这就是判断标准。',
   sch2ex='"Our flight lands at midnight."',
   sch3h='不用于自己的安排', sch3p='个人约定要用现在进行时。',
   sch3ex='"I meet Ana tomorrow." ✗  "I\'m meeting Ana tomorrow." ✓',
   dgCap='时刻表', dgSub='印好的时间，不是计划'),
}

s2 = inject_i18n(s2, C2_I18N, 'camp two')
open(p2, 'w', encoding='utf-8').write(s2)
print('camp two: section + %d language blocks' % len(C2_I18N))
