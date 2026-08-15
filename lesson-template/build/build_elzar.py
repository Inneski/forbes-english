# -*- coding: utf-8 -*-
"""El Zar — rebuilt as a 16:9 deck.

The old file was a long scrolling page with four exercise blocks stacked down
it. Every question, answer and explanation survives verbatim; what changes is
that they now sit one to a screen, the palette comes out of the studio artwork
rather than being hand-picked, and the lesson ends by making the learner use
the words rather than stopping at a score.

The teaching idea I added on top of the existing content: these eighteen words
are not synonyms with different registers, they are vectors. Each one carries a
direction — down, up, clearer, murkier, propped up — and at C2 the exam is
almost always testing the direction rather than the definition.
"""
import re, sys, json

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-el-zar-c2.html'
FOLDER = 'ElZar'

PALETTE = '''  --hero: url('%s/studio-hero.jpg');

  --void          : #d8c5ac;
  --surface       : #e1d5c4;
  --surface2      : #dcccb8;
  --border        : #96634a;
  --text          : #2a1911;
  --text-dim      : #5e3e2e;
  --accent        : #9f3906;
  --accent-bright : #722600;
  --accent-dim    : #e87237;
  --secondary     : #121713;
  --contrast      : #085449;''' % FOLDER

# ── carried over verbatim from the old lesson ────────────────────────
MC = [
    ("The producer used wide, rolling reverb to ______ the sharpness of the lead guitar, keeping the mix warm at high volumes.",
     ["exacerbate", "attenuate", "precipitate", "underscore"], 1,
     "<strong>Attenuate</strong> means to bring down the strength or sharpness of something. The producer wanted less harshness — not more (exacerbate), not a sudden shift (precipitate), and not further stress on it (underscore)."),
    ("The tour was meant to ______ the growing ill-feeling between the two founding members — yet within three nights it had ______ a lasting rift.",
     ["assuage … precipitated", "bolster … engendered", "circumscribe … attenuated", "mollify … corroborated"], 0,
     "<strong>Assuage</strong> means to make a painful feeling less sharp; <strong>precipitated</strong> means brought something about very fast and suddenly. The gap between what was hoped and what happened is the whole weight of the line."),
    ("The band&rsquo;s handler spoke in a rolling fog of vague, shifting words at every press gathering — plainly meant to ______ the truth rather than shed light on it.",
     ["elucidate", "substantiate", "corroborate", "obfuscate"], 3,
     "<strong>Obfuscate</strong> means to cloud or muddy something on purpose. The other three words all move toward clarity or backing up a claim — the other way round from what the handler was doing."),
    ("Three write-ups, each glowing and each written without knowledge of the others, went a long way to ______ the claim that El Zar&rsquo;s live shows had reached a new height.",
     ["diminish", "curtail", "corroborate", "circumscribe"], 2,
     "<strong>Corroborate</strong> means to back up a claim with fresh, independent support. Three separate writers agreeing is exactly that — the other three all narrow or weaken a claim rather than strengthening it."),
]

GAPS = [
    ("Years of thin funding had begun to ______ the band&rsquo;s standing, which had once been thought the strongest in the field.",
     "diminish",
     "<strong>Diminish</strong> means to make smaller or weaker by degrees. Standing that was once strong wore away through neglect."),
    ("Rather than deal with the row head-on, the label put out a statement so hedged and murky it seemed likely to ______ things rather than settle them.",
     "exacerbate",
     "<strong>Exacerbate</strong> means to make something bad even worse. Hedging and murkiness inflame rather than calm a row."),
    ("The tour manager hoped that handing out free backstage passes might ______ the anger of fans who had been turned away at the gate.",
     "mollify",
     "<strong>Mollify</strong> means to calm someone&rsquo;s anger or soften their mood. A goodwill offering is a classic way of trying to mollify."),
    ("The venue&rsquo;s deal ______ the band&rsquo;s freedom to play their own songs, setting a rule that at least forty in every hundred tracks had to be licensed covers.",
     "circumscribed",
     "<strong>Circumscribed</strong> means to draw a tight boundary around something — to hold it within set walls. The deal put a hard limit on their creative freedom."),
    ("The teacher played a track from El Zar&rsquo;s third record to ______ the idea of &lsquo;timbral layering&rsquo; — a term that had meant nothing to the students when it was set out in the abstract.",
     "elucidate",
     "<strong>Elucidate</strong> means to make something clear, to shed light on it. A real, heard example brought a dry idea to life."),
]
# Alphabetical, deliberately — see the note in the emails builder. The bank
# had been listing the five answers first, in gap order, which is an answer key.
BANK = sorted(["diminish", "exacerbate", "mollify", "circumscribed", "elucidate",
               "assuage", "curtail", "bolster"])

MATCH = [
    ("mitigate", "To make something harmful less sharp or strong in its reach"),
    ("engender", "To bring a feeling, mood, or state of things into being"),
    ("underscore", "To draw out the weight or meaning of something already there"),
    ("substantiate", "To back up a claim by bringing forward hard, real backing"),
    ("alleviate", "To lift some — though not all — of a weight, ache, or hardship"),
]

ORDER = [
    (["The write-up", "went a long way to bolster", "the long-held view", "that the band had lost none of their edge"],
     "<strong>Bolster</strong>: to prop up or strengthen. The write-up added weight to something people already believed."),
    (["The chairman&rsquo;s reach", "had been so thoroughly circumscribed", "by the board", "that his word carried almost no weight in the room"],
     "<strong>Circumscribed</strong>: held within tight walls. The board had drawn such a narrow ring around his power that he could do very little."),
    (["A long stretch of cold silence", "between the two lead players", "did nothing to abate", "the talk of a lasting split"],
     "<strong>Abate</strong>: to grow less strong. The silence did not quiet the talk — if anything it fed it."),
    (["Their failure to substantiate", "any of the claims", "with hard, written backing", "left their whole case hollow"],
     "<strong>Substantiate</strong>: to back up with solid proof. Without written backing, their words stood on nothing."),
    (["The rework, rather than attenuating", "the raw, unguarded feel of the first take,", "only seemed to precipitate", "a fresh wave of feeling for the old recording"],
     "<strong>Attenuate</strong>: to bring down in strength. <strong>Precipitate</strong>: to bring something about sharply and fast. The rework did not dull the old track — it sparked a new rush of love for it."),
]


def esc(t):
    return t.replace('"', '&quot;')


def mc_slide(i, item):
    text, choices, right, why = item
    opts = "\n          ".join(
        '<button class="opt"%s>%s</button>' % (' data-correct' if n == right else '', c)
        for n, c in enumerate(choices))
    return '''
    <section class="slide" data-type="mc">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="qEyebrow">Choose the word</span> &middot; %d / 4</div>
        <h2 class="slide-title" data-i18n="qTitle">Which direction does the sentence need?</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">%s</p>
        <div class="opts%s">
          %s
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (i, text, '' if len(choices[0]) > 22 else ' two-up', opts, esc(why))


def gap_slide(i, items):
    rows = "\n        ".join(
        '''<div class="card gap-row">
          <p class="q-stem" style="margin-bottom:12px">%s</p>
          <p class="feedback" data-explain="%s"></p>
        </div>''' % (line.replace('______',
                     '<input class="gap" data-answer="%s" aria-label="gap">' % ans), esc(why))
        for line, ans, why in items)
    chips = " ".join('<span class="bank-chip">%s</span>' % w for w in BANK)
    return '''
    <section class="slide" data-type="gap">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="gapEyebrow">Fill the gap</span> &middot; %d / 3</div>
        <h2 class="slide-title" data-i18n="gapTitle">One word, and only one, will do</h2>
      </div></div>
      <div class="slide-body">
        <div class="act-target" style="margin-bottom:14px">
          <span class="act-target-label" data-i18n="bankLabel">Word bank:</span>
          %s
        </div>
        %s
        <div style="margin-top:14px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
      </div>
    </section>
''' % (i, chips, rows)


MATCH_SLIDE = '''
    <section class="slide" data-type="match">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="matchEyebrow">Match the meanings</div>
        <h2 class="slide-title" data-i18n="matchTitle">Five more, defined by what they do</h2>
      </div></div>
      <div class="slide-body">
        <p class="prose dim" style="margin-bottom:14px;font-size:17px" data-i18n="matchHint">
          Click a word, then click its meaning. Each definition describes the <em>movement</em> the word makes, not just its sense.
        </p>
%s
        <div class="match-grid"></div>
        <p class="feedback" data-explain="Every one of these is a verb of force: something is lessened, brought into being, drawn out, propped up, or lifted."></p>
      </div>
    </section>
'''


def order_slide(i, item):
    chunks, why = item
    return '''
    <section class="slide" data-type="order">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="orderEyebrow">Build the sentence</span> &middot; %d / 5</div>
        <h2 class="slide-title" data-i18n="orderTitle">Put it in order</h2>
      </div></div>
      <div class="slide-body">
        <p class="order-hint" data-i18n="orderHint">Click the parts in order · click one again to take it back</p>
        <div class="order" data-answer="%s"></div>
        <div style="margin-top:16px">
          <button class="btn" data-action="check-order" data-i18n="btnCheck">Check</button>
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (i, esc(" | ".join(chunks)), esc(why))


HEAD = '''
    <!-- ── COVER ────────────────────────────────────────────── -->
    <section class="slide is-active" data-type="cover">
      <div class="cover-inner">
        {LOGO}
        <h1 class="cover-title" data-i18n="coverTitle">El Zar — the <em>pull</em> of these words</h1>
        <p class="cover-sub" data-i18n="coverSub">Eighteen C2 verbs of force and effect, sorted by the direction they push</p>
        <div class="cover-meta">
          <span class="chip" data-i18n="chipLevel">C2 Proficiency</span>
          <span class="chip" data-i18n="chipFocus">Vocabulary in use</span>
          <span class="chip" data-i18n="chipCount">18 slides</span>
        </div>
        <div style="margin-top:34px">
          <button class="btn btn-solid btn-lg" data-action="next" data-i18n="btnStart">Begin →</button>
        </div>
      </div>
    </section>

    <!-- ── THE IDEA ─────────────────────────────────────────── -->
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="famEyebrow">The idea</div>
        <h2 class="slide-title" data-i18n="famTitleA">These are not synonyms. They are vectors.</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols">
          <div class="card">
            <p class="prose" data-i18n="famIntroA">At C2 the test is almost never <em>what does this word mean</em>. It is <strong>which way does it push</strong> — and the four wrong options will usually push the other way.</p>
          </div>
          <div class="card">
            <p class="prose" data-i18n="famIntroB">Learn them in the four groups on the next slide and most questions answer themselves before you have read the options.</p>
          </div>
        </div>
        <div class="card" style="margin-top:16px">
          <p class="prose dim" data-i18n="famNote">Every sentence in this lesson comes from the world of a fictional band called El Zar — their tours, their rows, their reviews.</p>
        </div>
      </div>
    </section>

    <!-- ── THE FOUR FAMILIES ────────────────────────────────── -->
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="famEyebrow">The idea</div>
        <h2 class="slide-title" data-i18n="famTitleB">Four directions, eighteen words</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose"><strong data-i18n="fam1h">↓ Turn it down</strong></p>
            <p class="prose" style="margin-top:6px;font-size:18px">attenuate · diminish · abate · curtail · mitigate · alleviate · assuage · mollify · circumscribe</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="fam2h">↑ Turn it up, or set it off</strong></p>
            <p class="prose" style="margin-top:6px;font-size:18px">exacerbate · precipitate · engender · bolster</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="fam3h">◑ Clear it, or cloud it</strong></p>
            <p class="prose" style="margin-top:6px;font-size:18px">elucidate · obfuscate</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="fam4h">⌈ Back it up</strong></p>
            <p class="prose" style="margin-top:6px;font-size:18px">corroborate · substantiate · underscore</p>
          </div>
        </div>
      </div>
    </section>
'''

TAIL = '''
    <!-- ── RESULTS ──────────────────────────────────────────── -->
    <section class="slide" data-type="results">
      <div class="slide-body" style="align-items:center;text-align:center">
        <div class="score-big"><span id="scoreVal">0</span><span class="dim" style="font-size:34px">/<span id="scoreMax">0</span></span></div>
        <p class="prose" style="margin-top:18px" id="scoreMsg"></p>
        <p class="prose dim" style="margin-top:14px" data-i18n="resNext">Recognising the language is half of it. Now produce it →</p>
      </div>
    </section>

    <!-- ── ACTIVATION ───────────────────────────────────────── -->
    <section class="slide" data-type="activate">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="actEyebrow">Activation</div>
        <h2 class="slide-title" data-i18n="actTitle">Write the band into trouble</h2>
      </div></div>
      <div class="slide-body">
        <div class="act-target">
          <span class="act-target-label" data-i18n="actUse">Use at least four:</span>
          {CHIPS}
        </div>
        <div class="cols act-cols">
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">🗣</span><span data-i18n="actSpeakKind">Discussion · in pairs</span></div>
            <p class="act-brief" data-i18n="actSpeakBrief">One of you manages El Zar. The other runs the label. The tour is losing money.</p>
            <ul class="act-list">
              <li data-i18n="actSpeak1">Manager: press for a bigger marketing spend without conceding the tour was mismanaged.</li>
              <li data-i18n="actSpeak2">Label: curtail the tour by four dates, and mollify the manager while you do it.</li>
              <li data-i18n="actSpeak3">Both: agree a public statement that does not obfuscate, yet admits nothing actionable.</li>
            </ul>
          </div>
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">✍️</span><span data-i18n="actWriteKind">Writing · 180–220 words</span></div>
            <p class="act-brief" data-i18n="actWriteBrief">Write the review that ends the band — or saves them. Broadsheet register, no hedging.</p>
            <textarea class="act-input" id="actInput" data-i18n-ph="actPlaceholder" placeholder="Write your response here…" aria-label="Written response"></textarea>
            <div class="act-foot">
              <span class="act-count" id="actCount">0 words</span>
              <button class="btn act-copy" data-action="copy-writing" data-i18n="btnCopy">Copy</button>
            </div>
            <div class="act-print" id="actPrint" aria-hidden="true"></div>
          </div>
        </div>
        <div style="margin-top:14px;text-align:center">
          <button class="btn" data-action="restart" data-i18n="btnRestart">Start again</button>
        </div>
      </div>
    </section>
'''


def _assert_bank_is_not_a_key():
    pos = [BANK.index(a) for _, a, _ in GAPS if a in BANK]
    assert not all(x < y for x, y in zip(pos, pos[1:])), \
        'the word bank lists the gap answers in gap order: %s' % pos


def build():
    _assert_bank_is_not_a_key()
    s = open(TPL, encoding='utf-8').read()
    logo = re.search(r'(<svg class="fe-logo".*?</svg>)', s, re.S).group(1)

    pairs = "\n".join('        <div class="match-pair" data-term="%s" data-def="%s"></div>' % (w, d)
                      for w, d in MATCH)
    chips = "\n          ".join('<span class="bank-chip">%s</span>' % w for w in
                               ['attenuate', 'assuage', 'precipitate', 'obfuscate',
                                'corroborate', 'circumscribe', 'bolster', 'engender'])

    slides = (HEAD.replace('{LOGO}', logo)
              + "".join(mc_slide(i + 1, m) for i, m in enumerate(MC))
              + gap_slide(1, GAPS[0:2]) + gap_slide(2, GAPS[2:4]) + gap_slide(3, GAPS[4:5])
              + (MATCH_SLIDE % pairs)
              + "".join(order_slide(i + 1, o) for i, o in enumerate(ORDER))
              + TAIL.replace('{CHIPS}', chips))

    a = s.index('    <!-- ── COVER ')
    b = s.index('    <!-- ── DECK CHROME ')
    s = s[:a] + slides + '\n' + s[b:]

    s = re.sub(r"  --hero: url\('sample-hero\.jpg'\);.*?--contrast      : #1ded49;",
               PALETTE, s, count=1, flags=re.S)
    s = s.replace('<html lang="en">', '<html lang="en" data-theme="light">', 1)
    s = s.replace('<title>' + re.search(r'<title>(.*?)</title>', s, re.S).group(1) + '</title>',
                  '<title>El Zar — Words of Force and Effect (C2)</title>', 1)

    import i18n_elzar as I
    block = 'const UI_I18N = {\n' + ",\n".join(
        '  %s: %s' % (c, I.render(c)) for c in
        ['en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']) + '\n};'
    s = re.sub(r'const UI_I18N = \{.*?\n\};', block, s, count=1, flags=re.S)

    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, %d order, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH), len(ORDER), len(s)))


if __name__ == '__main__':
    sys.path.insert(0, '/tmp')
    build()
