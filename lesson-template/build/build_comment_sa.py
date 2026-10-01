"""Have Your Say — writing a comment on South Africa. B1–B2, two decks.

  writing-a-comment-south-africa.html          Part 1: the shape of a comment
  writing-a-comment-south-africa-part-2.html   Part 2: useful phrases

Part 1 arrived finished from outside the pipeline (Downloads, 2026-10-01).
Its markup is kept as comment-south-africa/part1.src.html with the pictures
as @HERO@ / @PICn@ / @BG@ placeholders; this builder fills them, applies the
palette derived from the hero, and corrects instruction text. Part 2 reuses
Part 1's engine and chrome and replaces the slides and lesson strings.

Part 1 instruction fixes: the writing task said "choose ONE statement from
the worksheet" and no worksheet exists, so it now names the statement; the
speaking task said "statement 6" without quoting it; the low-score message
said "three panels" where Stage 1 has five.

Part 2 source: Innes's "Comment: More useful phrases" sheet, 2026-10-01.
"Another signifact point" is corrected; "Following the line of arguments,
it can be concluded" and "It can only be true that…" are dropped as not
idiomatic.

Run from the repo root:  py lesson-template/build/build_comment_sa.py
"""
import re, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'lesson-template', 'build', 'comment-south-africa', 'part1.src.html')
OUT1 = os.path.join(ROOT, 'writing-a-comment-south-africa.html')
OUT2 = os.path.join(ROOT, 'writing-a-comment-south-africa-part-2.html')
ART = 'CommentSouthAfrica/'

def uri(name): return ART + name + '.jpg'

# extract-palette.py CommentSouthAfrica/<hero>.jpg --light — every row PASS
PALETTE1 = """  --void          : #d8c7ac;
  --surface       : #e1d6c4;
  --surface2      : #dcceb8;
  --border        : #96594a;
  --text          : #2a1611;
  --text-dim      : #5e382e;
  --accent        : #a62100;
  --accent-bright : #731700;
  --accent-dim    : #ef5631;
  --secondary     : #91b8c8;
  --contrast      : #07553f;"""
PALETTE2 = """  --void          : #d8c7ac;
  --surface       : #e1d6c4;
  --surface2      : #dcceb8;
  --border        : #96574a;
  --text          : #2a1511;
  --text-dim      : #5e362e;
  --accent        : #a72208;
  --accent-bright : #7c1400;
  --accent-dim    : #e75d42;
  --secondary     : #9cb9c8;
  --contrast      : #09533b;"""

def palette(h, pal):
    return re.sub(r"(:root \{\n  --hero: url\('[^']*'\);\n\n)(.*?)(\n\})", lambda m: m.group(1) + pal + m.group(3), h, count=1, flags=re.S)

def strings(h, langs, drop=None):
    """Rewrite lesson keys in the en/de/es blocks of UI_I18N."""
    for lg in ('en', 'de', 'es'):
        m = re.search(rf'\n  {lg}: \{{\n(.*?)\n  \}}', h, re.S)
        lines = [ln.rstrip(',') for ln in m.group(1).split('\n')]
        keys = set(langs[lg])
        lines = [ln for ln in lines if not (drop and re.match(drop, ln))
                 and not any(re.match(rf'\s+{k}:', ln) for k in keys)]
        add = [f'    {k}: {json.dumps(v, ensure_ascii=False)}' for k, v in sorted(langs[lg].items())]
        h = h[:m.start(1)] + ',\n'.join(add + lines) + h[m.end(1):]
    return h

def english_defaults(h, en):
    """Keep the hard-coded English in the markup in step with UI_I18N.en."""
    for k, v in en.items():
        h = re.sub(rf'(data-i18n="{k}">)(.*?)(</)', lambda m: m.group(1) + v + m.group(3), h, flags=re.S)
    return h

# ── Part 1 ─────────────────────────────────────────────────────────
HERO1 = 'ridge'
PICS1 = ['acacia', 'elephant', 'bokaap', 'township', 'truck', 'peak', 'walker']
BGS1 = ['ridge', 'bokaap', 'elephant', 'township', 'acacia', 'truck', 'peak', 'walker']
FIX1 = {
 'en': dict(
  actSpeak1="Statement 6 said: \"Beauty alone cannot build a fair country.\" Agree or disagree in one clear sentence, then give two reasons. Your partner argues the other side.",
  actWriteBrief="Write a comment for the class blog on this statement: \"South Africa should put its landscapes first, not its past.\" Write an introduction, two or three main-part paragraphs and a conclusion. 150–250 words.",
  resLow="Go back to Stage 1 and read the panels again, then try once more."),
 'de': dict(
  actSpeak1="In Aussage 6 stand: \"Beauty alone cannot build a fair country.\" Stimm zu oder widersprich in einem klaren Satz, dann nenne zwei Gründe. Dein Partner vertritt die Gegenseite.",
  actWriteBrief="Schreib einen Comment für den Klassenblog zu dieser Aussage: \"South Africa should put its landscapes first, not its past.\" Schreib eine Einleitung, zwei oder drei Absätze im Hauptteil und einen Schluss. 150–250 Wörter.",
  resLow="Geh zurück zu Teil 1, lies die Karten noch einmal und versuch es erneut."),
 'es': dict(
  actSpeak1="La afirmación 6 decía: \"Beauty alone cannot build a fair country.\" Di si estás de acuerdo o no en una frase clara y luego da dos razones. Tu pareja defiende la postura contraria.",
  actWriteBrief="Escribe un comentario para el blog de la clase sobre esta afirmación: \"South Africa should put its landscapes first, not its past.\" Escribe una introducción, dos o tres párrafos de desarrollo y una conclusión. 150–250 palabras.",
  resLow="Vuelve a la Etapa 1, lee de nuevo los paneles e inténtalo otra vez."),
}

def build1():
    h = open(SRC, encoding='utf8').read()
    h = h.replace('@HERO@', uri(HERO1))
    for i, n in enumerate(PICS1, 1):
        h = h.replace(f'@PIC{i}@', uri(n))
    for n in BGS1:
        h = h.replace('@BG@', uri(n), 1)
    assert '@' + 'BG@' not in h
    h = palette(h, PALETTE1)
    h = strings(h, FIX1)
    h = english_defaults(h, FIX1['en'])
    open(OUT1, 'w', encoding='utf8', newline='').write(h)
    print(OUT1)

# ── Part 2 ─────────────────────────────────────────────────────────
HERO = 'coast'
PICS = ['lighthouse', 'village', 'valley', 'farmhouse', 'washing', 'road', 'whitehouse']   # d1, t1..t5, d2
BGS = ['village', 'coast', 'washing', 'valley', 'farmhouse', 'whitehouse', 'lighthouse', 'road']  # q1..q6, results, activate

# ── teach cards: key, title, phrases (English, not translated) ──
TEACH = [
    ('t1', ["Leading in"], ["This comment will discuss …", "The problem discussed in this comment is …",
            "It is generally considered that …", "Therefore, it is interesting to have a closer look at …"]),
    ('t2', ["Adding and ordering points"], ["Firstly, / Secondly, / Thirdly, …", "In addition, …", "Moreover, …",
            "Not only … but I also think …", "Another important point is …", "One could argue that …"]),
    ('t3', ["Examples and comparisons"], ["For example, …", "For instance, …", "Take, for example, the case of …",
            "Similarly, …", "Likewise, …", "Compared to …"]),
    ('t4', ["Reasons and facts"], ["Because (of that) …", "Since …", "As …", "The fact is that …",
            "There is no doubt that …", "This proves that …"]),
    ('t5', ["Concluding"], ["As a result, …", "Therefore, …", "As mentioned above, …", "To put it in a nutshell, …",
            "I would like to conclude by saying …", "So all in all, I believe …"]),
]

# ── quiz: stem with gap, options (first is correct; shuffled by position below) ──
QUIZ = [
    ("______ the case of Kruger National Park: it gives thousands of people a job.",
     ["Take, for example,", "As a consequence,", "Not only that, but"], 0),
    ("Tourism brings money to Cape Town. ______, it creates jobs in the townships nearby.",
     ["For instance", "In addition", "To put it in a nutshell"], 1),
    ("______ Cape Town, small towns in the Karoo get very few tourists.",
     ["Moreover,", "Because of that,", "Compared to"], 2),
    ("Many young people leave the countryside ______ there is more work in the cities.",
     ["since", "likewise", "therefore"], 0),
    ("______ apartheid ended in 1994, but its effects can still be seen today.",
     ["Take, for example,", "It is a fact that", "In comparison with"], 1),
    ("______, I believe South Africa should protect both its landscapes and its memory.",
     ["Firstly", "For instance", "So all in all"], 2),
]

L = {
 'en': dict(
  coverTitle="Have <em>Your Say</em> · 2", coverSub="Useful phrases for a comment on South Africa",
  chipLevel="B1–B2 · Writing", chipFocus="Comment phrases", chipCount="16 slides",
  d1t="Phrases for every job", d1n="Stage 1 · five toolboxes", d2t="Which phrase?", d2n="Stage 2 · six gaps",
  e1="Comment phrases", e2="Which phrase?", qCtx="Choose the phrase that fits the gap. Ask what the gap does: add a point, give an example, compare, give a reason, state a fact or conclude?",
  t1a="Open with the topic. These phrases tell the reader what the comment is about before you give your opinion.",
  t2a="Add a new point and show the order of your arguments. Each one usually starts a new paragraph.",
  t3a="Back up a point with a real case, or set two things side by side.",
  t4a="Say <strong>why</strong> — or state something you are sure is true. A reason after <em>because / since / as</em> is a full clause.",
  t5a="Land the comment: sum up and give your final opinion. No new arguments after these.",
  q1w="<em>Take, for example, the case of …</em> brings in an example — here, Kruger National Park.",
  q2w="<em>In addition</em> adds a second point to the first one: money, and also jobs.",
  q3w="<em>Compared to</em> sets two things side by side: Cape Town and the Karoo towns.",
  q4w="<em>since</em> gives a reason (= because). <em>Therefore</em> would turn the sentence back to front.",
  q5w="<em>It is a fact that</em> states something sure: 1994 is a date, not an opinion.",
  q6w="<em>So all in all, I believe …</em> sums up and gives the final opinion. It belongs in the conclusion.",
  resPerfect="Perfect. You know which phrase does which job.",
  resStrong="Very good. Check the one you missed: ask what the gap is doing — adding, giving an example, a reason, or concluding?",
  resMid="Good start. Go back to the toolbox for the one you missed and say its phrases aloud.",
  resLow="Go back to Stage 1 and read the five toolboxes again, then try once more.",
  resNext="Recognising the phrases is half of it. Now use them →",
  actTitle="Now have your say", actUse="Use at least one phrase from each toolbox, for example:",
  actSpeakBrief="Work with a partner. Speak first, then write.", actSpeakKind="Discussion · in pairs",
  actSpeak1="\"South Africa should spend more on its townships than on its national parks.\" Agree or disagree, using <em>Firstly</em>, <em>In addition</em> and <em>For example</em>.",
  actSpeak2="Compare two places in South Africa from the pictures. Use <em>Compared to</em> and <em>Similarly</em>.",
  actSpeak3="Your partner gives an opinion. Sum it up for them in one sentence that starts <em>To put it in a nutshell, …</em>",
  actWriteBrief="Write a comment for the class blog on this statement: \"South Africa should spend more on its townships than on its national parks.\" Use at least one phrase from each of the five toolboxes. 150–250 words. (If you wrote a comment in Part 1, you can rewrite that one instead.)",
 ),
 'de': dict(
  coverTitle="Sag <em>deine Meinung</em> · 2", coverSub="Nützliche Wendungen für einen Comment über Südafrika",
  chipLevel="B1–B2 · Schreiben", chipFocus="Comment-Wendungen", chipCount="16 Folien",
  d1t="Wendungen für jede Aufgabe", d1n="Teil 1 · fünf Werkzeugkästen", d2t="Welche Wendung?", d2n="Teil 2 · sechs Lücken",
  e1="Comment-Wendungen", e2="Welche Wendung?", qCtx="Wähle die Wendung, die in die Lücke passt. Frag dich, was die Lücke tut: einen Punkt ergänzen, ein Beispiel geben, vergleichen, einen Grund nennen, eine Tatsache feststellen oder abschließen?",
  t1a="Beginne mit dem Thema. Diese Wendungen sagen, worum es im Comment geht, bevor du deine Meinung sagst.",
  t2a="Füge einen neuen Punkt hinzu und zeig die Reihenfolge deiner Argumente. Jedes beginnt meist einen neuen Absatz.",
  t3a="Stütze einen Punkt mit einem echten Fall oder stelle zwei Dinge nebeneinander.",
  t4a="Sag <strong>warum</strong> — oder nenne etwas, das sicher stimmt. Nach <em>because / since / as</em> folgt ein ganzer Satz.",
  t5a="Bring den Comment zum Ende: zusammenfassen und die abschließende Meinung sagen. Danach keine neuen Argumente.",
  q1w="<em>Take, for example, the case of …</em> leitet ein Beispiel ein — hier den Kruger-Nationalpark.",
  q2w="<em>In addition</em> fügt dem ersten Punkt einen zweiten hinzu: Geld und auch Arbeitsplätze.",
  q3w="<em>Compared to</em> stellt zwei Dinge nebeneinander: Kapstadt und die Orte in der Karoo.",
  q4w="<em>since</em> nennt einen Grund (= because). <em>Therefore</em> würde den Satz umdrehen.",
  q5w="<em>It is a fact that</em> nennt etwas Sicheres: 1994 ist ein Datum, keine Meinung.",
  q6w="<em>So all in all, I believe …</em> fasst zusammen und gibt die abschließende Meinung. Das gehört in den Schluss.",
  resPerfect="Perfekt. Du weißt, welche Wendung welche Aufgabe hat.",
  resStrong="Sehr gut. Schau dir den Fehler an: Was macht die Lücke — ergänzen, ein Beispiel, ein Grund oder ein Schluss?",
  resMid="Guter Anfang. Geh zum Werkzeugkasten für den Fehler zurück und sprich die Wendungen laut.",
  resLow="Geh zurück zu Teil 1, lies die fünf Werkzeugkästen noch einmal und versuch es erneut.",
  resNext="Die Wendungen zu erkennen ist die halbe Miete. Jetzt anwenden →",
  actTitle="Jetzt sag deine Meinung", actUse="Benutze mindestens eine Wendung aus jedem Werkzeugkasten, zum Beispiel:",
  actSpeakBrief="Arbeitet zu zweit. Erst sprechen, dann schreiben.", actSpeakKind="Diskussion · zu zweit",
  actSpeak1="\"South Africa should spend more on its townships than on its national parks.\" Stimm zu oder widersprich, mit <em>Firstly</em>, <em>In addition</em> und <em>For example</em>.",
  actSpeak2="Vergleiche zwei Orte in Südafrika aus den Bildern. Benutze <em>Compared to</em> und <em>Similarly</em>.",
  actSpeak3="Dein Partner sagt seine Meinung. Fasse sie in einem Satz zusammen, der mit <em>To put it in a nutshell, …</em> beginnt.",
  actWriteBrief="Schreib einen Comment für den Klassenblog zu dieser Aussage: \"South Africa should spend more on its townships than on its national parks.\" Benutze mindestens eine Wendung aus jedem der fünf Werkzeugkästen. 150–250 Wörter. (Wenn du in Teil 1 einen Comment geschrieben hast, kannst du stattdessen diesen überarbeiten.)",
 ),
 'es': dict(
  coverTitle="Da <em>tu opinión</em> · 2", coverSub="Expresiones útiles para un comentario sobre Sudáfrica",
  chipLevel="B1–B2 · Escritura", chipFocus="Expresiones del comentario", chipCount="16 diapositivas",
  d1t="Expresiones para cada función", d1n="Etapa 1 · cinco cajas de herramientas", d2t="¿Qué expresión?", d2n="Etapa 2 · seis huecos",
  e1="Expresiones del comentario", e2="¿Qué expresión?", qCtx="Elige la expresión que encaja en el hueco. Pregúntate qué hace el hueco: añadir un punto, dar un ejemplo, comparar, dar una razón, afirmar un hecho o concluir.",
  t1a="Empieza con el tema. Estas expresiones dicen de qué trata el comentario antes de dar tu opinión.",
  t2a="Añade un punto nuevo y muestra el orden de tus argumentos. Cada uno suele empezar un párrafo nuevo.",
  t3a="Apoya un punto con un caso real o pon dos cosas una al lado de la otra.",
  t4a="Di <strong>por qué</strong> — o afirma algo que es seguro. Después de <em>because / since / as</em> va una oración completa.",
  t5a="Cierra el comentario: resume y da tu opinión final. Después de estas, nada de argumentos nuevos.",
  q1w="<em>Take, for example, the case of …</em> introduce un ejemplo: aquí, el Parque Nacional Kruger.",
  q2w="<em>In addition</em> añade un segundo punto al primero: dinero, y también empleo.",
  q3w="<em>Compared to</em> pone dos cosas una al lado de la otra: Ciudad del Cabo y los pueblos del Karoo.",
  q4w="<em>since</em> da una razón (= because). <em>Therefore</em> pondría la frase al revés.",
  q5w="<em>It is a fact that</em> afirma algo seguro: 1994 es una fecha, no una opinión.",
  q6w="<em>So all in all, I believe …</em> resume y da la opinión final. Va en la conclusión.",
  resPerfect="Perfecto. Sabes qué función cumple cada expresión.",
  resStrong="Muy bien. Revisa la que fallaste: ¿qué hace el hueco — añadir, dar un ejemplo, una razón o concluir?",
  resMid="Buen comienzo. Vuelve a la caja de la que fallaste y di sus expresiones en voz alta.",
  resLow="Vuelve a la Etapa 1, lee de nuevo las cinco cajas e inténtalo otra vez.",
  resNext="Reconocer las expresiones es solo la mitad. Ahora úsalas →",
  actTitle="Ahora da tu opinión", actUse="Usa al menos una expresión de cada caja, por ejemplo:",
  actSpeakBrief="Trabaja en pareja. Primero habla, luego escribe.", actSpeakKind="Debate · en parejas",
  actSpeak1="\"South Africa should spend more on its townships than on its national parks.\" Muestra acuerdo o desacuerdo usando <em>Firstly</em>, <em>In addition</em> y <em>For example</em>.",
  actSpeak2="Compara dos lugares de Sudáfrica de las imágenes. Usa <em>Compared to</em> y <em>Similarly</em>.",
  actSpeak3="Tu pareja da su opinión. Resúmela en una frase que empiece por <em>To put it in a nutshell, …</em>",
  actWriteBrief="Escribe un comentario para el blog de la clase sobre esta afirmación: \"South Africa should spend more on its townships than on its national parks.\" Usa al menos una expresión de cada una de las cinco cajas. 150–250 palabras. (Si escribiste un comentario en la Parte 1, puedes reescribir ese.)",
 ),
}
TITLES = {
 'en': ["Leading in", "Adding and ordering points", "Examples and comparisons", "Reasons and facts", "Concluding"],
 'de': ["Einleiten", "Punkte ergänzen und ordnen", "Beispiele und Vergleiche", "Gründe und Fakten", "Abschließen"],
 'es': ["Introducir el tema", "Añadir y ordenar puntos", "Ejemplos y comparaciones", "Razones y hechos", "Concluir"],
}
for lg in L:
    for i, tt in enumerate(TITLES[lg], 1):
        L[lg][f't{i}t'] = f"{i} · {tt}"

BANK = ["This comment will discuss …", "Firstly, …", "For instance, …", "Since …", "To put it in a nutshell, …"]

def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def build2():
    h = open(SRC, encoding='utf8').read()
    h = h.replace('@HERO@', uri(HERO))
    h = re.sub(r'@PIC\d@', 'x', h).replace('@BG@', 'x')
    h = palette(h, PALETTE2)
    start = h.index('    <section class="slide is-active" data-type="cover">')
    end = h.index('    <!-- ── DECK CHROME')
    old = h[start:end]
    cover = old[:old.index('</section>') + len('</section>')]
    act = old[old.index('    <section class="slide" data-type="activate"'):]
    pics, bgs = iter(PICS), iter(BGS)
    en = L['en']

    def divider(k):
        u = uri(next(pics))
        return f'''    <section class="slide" data-type="divider" data-pic="{u}" style="--pic:url('{u}')">
      <div class="divider-pic"></div>
      <div class="divider-cap">
        <h2 data-i18n="{k}t">{en[k+'t']}</h2>
        <div class="divider-n" data-i18n="{k}n">{en[k+'n']}</div>
      </div>
    </section>
'''
    parts = [cover.replace(
        '<span class="chip" data-i18n="chipCount">16 slides</span>',
        '<span class="chip" data-i18n="chipCount">16 slides</span>') + '\n\n', divider('d1'), '\n']
    for i, (k, _, phrases) in enumerate(TEACH, 1):
        u = uri(next(pics)); side = ' data-side="right"' if i % 2 == 0 else ''
        ph = '<br>'.join(f'<em>{esc(p)}</em>' for p in phrases)
        parts.append(f'''    <section class="slide" data-type="teach" data-layout="panel" data-pic="{u}" style="--pic:url('{u}')"{side}>
      <div class="panel-pic"></div>
      <div class="panel-body">
        <div class="slide-head"><div>
          <div class="eyebrow" data-i18n="e1">{en['e1']}</div>
          <h2 class="slide-title" data-i18n="t{i}t">{en[f't{i}t']}</h2>
        </div></div>
        <div class="slide-body">
          <p class="prose" data-i18n="t{i}a">{en[f't{i}a']}</p>
          <p class="prose dim" style="line-height:1.55">{ph}</p>
        </div>
      </div>
    </section>

''')
    parts.append(divider('d2')); parts.append('\n')
    for i, (stem, opts, ok) in enumerate(QUIZ, 1):
        u = uri(next(bgs))
        ob = '\n'.join(f'          <button class="opt"{" data-correct" if j == ok else ""}>{esc(o)}</button>'
                       for j, o in enumerate(opts))
        parts.append(f'''    <section class="slide" data-type="mc" data-bg="{u}">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="e2">{en['e2']}</span> &middot; {i} / 6</div>
        <h2 class="slide-title" data-i18n="d2t">{en['d2t']}</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-ctx" data-i18n="qCtx">{en['qCtx']}</p>
        <p class="q-stem">{esc(stem)}</p>
        <div class="opts">
{ob}
        </div>
        <p class="feedback" data-explain="q{i}w"></p>
      </div>
    </section>

''')
    res = old[old.index('    <section class="slide" data-type="results"'):old.index('    <section class="slide" data-type="activate"')]
    parts.append(re.sub(r'data-bg="[^"]*"', f'data-bg="{uri(next(bgs))}"', res, count=1))
    # activation: new bank, new picture, English defaults refreshed from L['en']
    act = re.sub(r'data-bg="[^"]*"', f'data-bg="{uri(next(bgs))}"', act, count=1)
    act = re.sub(r'(<span class="act-target-label"[^>]*>)[^<]*(</span>)\s*(?:<span class="bank-chip">[^<]*</span>\s*)+',
                 lambda m: m.group(1) + en['actUse'] + m.group(2) + '\n' +
                 ''.join(f'          <span class="bank-chip">{esc(b)}</span>\n' for b in BANK), act)
    for k in ('actTitle', 'actSpeakBrief', 'actSpeak1', 'actSpeak2', 'actSpeak3', 'actWriteBrief', 'actSpeakKind'):
        act = re.sub(rf'(data-i18n="{k}">)(.*?)(</)', lambda m: m.group(1) + en[k] + m.group(3), act, count=1, flags=re.S)
    parts.append(act)
    h = h[:start] + ''.join(parts) + h[end:]


    # UI_I18N: drop Part 1 lesson keys (s*, q*w, …), add Part 2's
    for lg in ('en', 'de', 'es'):
        m = re.search(rf'\n  {lg}: \{{\n(.*?)\n  \}}', h, re.S)
        body = m.group(1)
        lines = [ln for ln in body.split('\n')
                 if not re.match(r'\s+(s\d[abt]|q\dw|d\d[nt]|e\d|qCtx|res(Low|Mid|Perfect|Strong|Next)|cover\w+|chip\w+|act(Title|Use|Speak\d|SpeakBrief|SpeakKind|WriteBrief)):', ln)]
        lines = [ln.rstrip(',') for ln in lines]
        add = [f'    {k}: {json.dumps(v, ensure_ascii=False)}' for k, v in sorted(L[lg].items())]
        h = h[:m.start(1)] + ',\n'.join(add + lines) + h[m.end(1):]

    h = re.sub(r'<title>[^<]*</title>', '<title>Have Your Say 2 — Useful Phrases for a Comment: South Africa (B1–B2)</title>', h, count=1)
    open(OUT2, 'w', encoding='utf8', newline='').write(h)
    print(OUT2)

if __name__ == '__main__':
    build1()
    build2()
