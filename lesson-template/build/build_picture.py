# -*- coding: utf-8 -*-
"""Describing a Picture — the three duplicate lessons merged into one deck.

There were three files: an eight-word original and two nine-word revisions
that differ from each other only in masthead furniture. The merge keeps the
fuller nine-word set, both extra fill sentences, the better model answer and
the fuller tips, so nothing pedagogical is lost — then rebuilds the whole
thing as a 16:9 deck per the house style, with the Ireland artwork as the
cover, the palette derived mechanically from it, and an activation stage that
makes the learner actually produce a description instead of recognising one.

The vocabulary, the definitions and the seven sentences stay in English on
every language setting: they are the thing being taught. Only the chrome and
the instructions translate.
"""
import re, json

TPL = 'lesson-template/lesson-template.html'
OUT = 'english_class_picture_description.html'
FOLDER = 'english_class_picture_description'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #d4cbb1;
  --surface       : #ded8c8;
  --surface2      : #d8d1bc;
  --border        : #96714a;
  --text          : #2a1e11;
  --text-dim      : #5e472e;
  --accent        : #834300;
  --accent-bright : #693600;
  --accent-dim    : #eb8112;
  --secondary     : #99a4a0;
  --contrast      : #075255;''' % FOLDER

# ─────────────────────────────────────────────────────────────────────
# the merged content
# ─────────────────────────────────────────────────────────────────────
VOCAB = [
    ('scenic',       'adjective',    'providing or relating to views of impressive or beautiful natural scenery'),
    ('picturesque',  'adjective',    'visually attractive, especially in a charming or quaint way'),
    ('rugged',       'adjective',    '(of ground or terrain) having a broken, rocky, and uneven surface'),
    ('foreground',   'noun',         'the front area in a picture — the part nearest the viewer'),
    ('outdoors',     'noun / adv',   'any area outside buildings or shelter, typically far from human habitation'),
    ('fenestration', 'noun',         'the arrangement of windows and doors on the elevations of a building'),
    ('foreboding',   'noun',         'fearful apprehension; a feeling that something bad will happen'),
    ('aperture',     'noun',         'an opening, hole, or gap'),
    ('ruined',       'adjective',    '(of a building or place) reduced to a state of decay and disrepair'),
]

# (stem before the gap, answer, stem after, three wrong options, why)
QUESTIONS = [
    ('The', 'rugged', 'path wound through loose boulders and broken rock.',
     ['outdoors', 'scenic', 'ruined'],
     'Rugged describes ground that is broken and uneven. Ruined would need a building; scenic would be praising the view, not the surface underfoot.'),
    ('Light fell through the', 'aperture', 'in the crumbling wall, casting a pale oval on the floor.',
     ['fenestration', 'foreground', 'foreboding'],
     'An aperture is any opening or gap. Fenestration is the arrangement of windows in a building that still has them — a hole in a ruin is not fenestration.'),
    ('In the', 'foreground', ', fragments of old pottery lay scattered across the mud.',
     ['outdoors', 'aperture', 'background'],
     'The foreground is the part of a picture nearest the viewer. It is the standard word for starting a description and moving backwards.'),
    ('The building&rsquo;s ornate', 'fenestration', '&mdash; twelve tall windows in three rows &mdash; was remarkable.',
     ['ornamentation', 'foreboding', 'aperture'],
     'Fenestration is the arrangement of the windows, not a single window and not the decoration on them. It is the precise word an architect would use here.'),
    ('They preferred to dine', 'outdoors', ', surrounded by the pine-scented air of the mountains.',
     ['scenic', 'foreground', 'picturesque'],
     'Outdoors works as an adverb here — dine where? Scenic and picturesque are adjectives and would need a noun to describe.'),
    ('A heavy sense of', 'foreboding', 'settled over them as the sky darkened above the valley.',
     ['fenestration', 'aperture', 'confidence'],
     'Foreboding is the feeling that something bad is coming. It is the word to reach for when a picture&rsquo;s mood is uneasy rather than calm.'),
    ('The village was so', 'picturesque', 'that visitors often stopped to photograph its cobbled lanes.',
     ['foreboding', 'rugged', 'ruined'],
     'Picturesque means charmingly attractive, the sort of thing people photograph. Scenic would also work; rugged and ruined would not.'),
]

TIPS_A = [
    ('tipA1', 'Open with the whole thing',
     'Begin with a general overview before any detail: <strong>&ldquo;The picture shows&hellip;&rdquo;</strong> or <strong>&ldquo;In this image we can see&hellip;&rdquo;</strong>'),
    ('tipA2', 'Then work backwards',
     'Move from the <strong>foreground</strong>, what is nearest, through the middle distance, to the <strong>background</strong>, what is furthest away.'),
]
TIPS_B = [
    ('tipB1', 'Name the mood',
     'A description that only lists objects is a inventory. Say what the picture <em>feels</em> like &mdash; is there <strong>foreboding</strong>, peace, energy?'),
    ('tipB2', 'Be exact about position',
     '<strong>in the foreground</strong> &middot; <strong>to the left</strong> &middot; <strong>in the distance</strong> &middot; <strong>along the horizon</strong> &middot; <strong>set back from</strong>'),
]

MODEL_A = ('The <strong>foreground</strong> is dominated by <strong>rugged</strong>, broken ground &mdash; shards of old '
           'masonry half-swallowed by damp earth and coarse grass. Through a wide <strong>aperture</strong> in the '
           '<strong>ruined</strong> wall to the left, the eye is drawn straight <strong>outdoors</strong>, where a '
           '<strong>scenic</strong> and almost <strong>picturesque</strong> valley stretches toward a line of distant hills.')
MODEL_B = ('To the right, a tall inhabited building rises above the plain; its elaborate <strong>fenestration</strong> '
           '&mdash; four neat rows of tall, narrow windows &mdash; catches what little light the sky offers. The clouds '
           'press low and the whole composition carries a quiet quality of <strong>foreboding</strong>, as though the '
           'landscape is holding its breath before something changes.')


def vocab_card(word, pos, definition):
    return ('''<div class="card">
            <p class="prose"><strong>%s</strong> &nbsp;<span class="dim" style="font-size:15px;font-family:var(--font-mono)">%s</span></p>
            <p class="prose dim" style="font-size:17px;margin-top:6px">%s</p>
          </div>''' % (word, pos, definition))


def vocab_slide(n, words):
    return '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="vocabEyebrow">Vocabulary</span> &middot; %d / 3</div>
        <h2 class="slide-title" data-i18n="vocabTitle">Nine words for a landscape</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1fr 1fr 1fr">
          %s
        </div>
      </div>
    </section>
''' % (n, "\n          ".join(vocab_card(*w) for w in words))


def mc_slide(i, q):
    pre, ans, post, wrong, why = q
    opts = [('<button class="opt" data-correct>%s</button>' % ans)] + \
           [('<button class="opt">%s</button>' % w) for w in wrong]
    return '''
    <section class="slide" data-type="mc">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="qEyebrow">Question</span> &middot; %d / 7</div>
        <h2 class="slide-title" data-i18n="qTitle">Choose the right word</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">%s&nbsp;<em>_______</em>%s%s</p>
        <div class="opts two-up">
          %s
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (i, pre, '' if post[:1] in ',.;:' else '&nbsp;', post, "\n          ".join(opts), why.replace('"', '&quot;'))


SLIDES = '''
    <!-- ── COVER ────────────────────────────────────────────── -->
    <section class="slide is-active" data-type="cover">
      <div class="cover-inner">
        {LOGO}
        <h1 class="cover-title" data-i18n="coverTitle">Describing a <em>Picture</em></h1>
        <p class="cover-sub" data-i18n="coverSub">Nine precise words for a landscape, and the order to put them in</p>
        <div class="cover-meta">
          <span class="chip" data-i18n="chipLevel">B1–B2</span>
          <span class="chip" data-i18n="chipFocus">Vocabulary &amp; writing</span>
          <span class="chip" data-i18n="chipCount">18 slides</span>
        </div>
        <div style="margin-top:34px">
          <button class="btn btn-solid btn-lg" data-action="next" data-i18n="btnStart">Begin →</button>
        </div>
      </div>
    </section>

    <!-- ── THE SCENE ────────────────────────────────────────── -->
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="sceneEyebrow">The scene</div>
        <h2 class="slide-title" data-i18n="sceneTitle">This is the picture you will describe</h2>
      </div></div>
      <div class="slide-body">
        <!-- No inset plate here. The lesson background IS this picture, so a
             framed copy of it sitting on top of itself just cancels out. The
             slide shows the artwork full-bleed and puts only the caption on a
             card, which is also the strongest argument for keeping it up on
             every slide behind the vocabulary. -->
        <div class="scene-spacer"></div>
        <div class="card scene-plate">
          <p class="prose" data-i18n="sceneCaption">
            A <strong>ruined</strong> structure on the left; an inhabited building with elaborate <strong>fenestration</strong> on the right. Keep it in view — every word in this lesson is somewhere in it.
          </p>
        </div>
      </div>
    </section>

    <!-- ── HOW TO DESCRIBE ──────────────────────────────────── -->
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="tipsEyebrow">How to describe a picture</div>
        <h2 class="slide-title" data-i18n="tipsTitleA">Start wide, then go in</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols">
{TIPS_A}
        </div>
      </div>
    </section>

    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="tipsEyebrow">How to describe a picture</div>
        <h2 class="slide-title" data-i18n="tipsTitleB">Say how it feels, and exactly where</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols">
{TIPS_B}
        </div>
      </div>
    </section>
{VOCAB}{QUESTIONS}
    <!-- ── RESULTS ──────────────────────────────────────────── -->
    <section class="slide" data-type="results">
      <div class="slide-body" style="align-items:center;text-align:center">
        <div class="score-big"><span id="scoreVal">0</span><span class="dim" style="font-size:34px">/<span id="scoreMax">0</span></span></div>
        <p class="prose" style="margin-top:18px" id="scoreMsg"></p>
        <p class="prose dim" style="margin-top:14px" data-i18n="resNext">Recognising the language is half of it. Now produce it →</p>
      </div>
    </section>

    <!-- ── MODEL ANSWER ─────────────────────────────────────── -->
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="modelEyebrow">Model answer</span> &middot; 1 / 2</div>
        <h2 class="slide-title" data-i18n="modelTitleA">How a strong description opens</h2>
      </div></div>
      <div class="slide-body">
        <div class="card">
          <p class="prose">{MODEL_A}</p>
        </div>
        <p class="prose dim" style="margin-top:12px;font-size:17px" data-i18n="modelNoteA">
          Notice the order: nearest first, then through the gap in the wall, then out to the hills.
        </p>
      </div>
    </section>

    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="modelEyebrow">Model answer</span> &middot; 2 / 2</div>
        <h2 class="slide-title" data-i18n="modelTitleB">&hellip; and how it closes</h2>
      </div></div>
      <div class="slide-body">
        <div class="card">
          <p class="prose">{MODEL_B}</p>
        </div>
        <p class="prose dim" style="margin-top:12px;font-size:17px" data-i18n="modelNoteB">
          It ends on mood rather than on an object. That is what stops a description reading like a list.
        </p>
      </div>
    </section>

    <!-- ── ACTIVATION ───────────────────────────────────────── -->
    <section class="slide" data-type="activate">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="actEyebrow">Activation</div>
        <h2 class="slide-title" data-i18n="actTitle">Now describe it yourself</h2>
      </div></div>
      <div class="slide-body">
        <div class="act-target">
          <span class="act-target-label" data-i18n="actUse">Use at least five:</span>
          {CHIPS}
        </div>
        <div class="cols act-cols">
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">🗣</span><span data-i18n="actSpeakKind">Discussion · in pairs</span></div>
            <p class="act-brief" data-i18n="actSpeakBrief">One of you can see the picture; the other cannot. Sit back to back.</p>
            <ul class="act-list">
              <li data-i18n="actSpeak1">Describe it so well your partner can sketch it. No pointing, no naming the country.</li>
              <li data-i18n="actSpeak2">Swap. Now argue: should the modern building be allowed to stand there at all?</li>
              <li data-i18n="actSpeak3">Both of you: describe the same picture as an estate agent, then as a horror writer.</li>
            </ul>
          </div>
          <div class="card act-card">
            <div class="act-kind"><span class="act-icon">✍️</span><span data-i18n="actWriteKind">Writing · 150–200 words</span></div>
            <p class="act-brief" data-i18n="actWriteBrief">Write the caption for this photograph in a travel magazine. Move foreground to background, and end on the mood.</p>
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


def tip_cards(tips):
    return "\n".join(
        '          <div class="card">'
        '<p class="prose"><strong data-i18n="%sh">%s</strong></p>'
        '<p class="prose" style="margin-top:8px" data-i18n="%sb">%s</p></div>'
        % (k, h, k, b) for k, h, b in tips)


def build():
    s = open(TPL, encoding='utf-8').read()

    logo = re.search(r'(<svg class="fe-logo".*?</svg>)', s, re.S).group(1)

    vocab_html = (vocab_slide(1, VOCAB[0:3]) +
                  vocab_slide(2, VOCAB[3:6]) +
                  vocab_slide(3, VOCAB[6:9]))
    q_html = "".join(mc_slide(i + 1, q) for i, q in enumerate(QUESTIONS))
    chips = "\n          ".join('<span class="bank-chip">%s</span>' % w[0] for w in VOCAB)

    slides = (SLIDES.replace('{LOGO}', logo).replace('{FOLDER}', FOLDER)
              .replace('{TIPS_A}', tip_cards(TIPS_A))
              .replace('{TIPS_B}', tip_cards(TIPS_B))
              .replace('{VOCAB}', vocab_html).replace('{QUESTIONS}', q_html)
              .replace('{MODEL_A}', MODEL_A).replace('{MODEL_B}', MODEL_B)
              .replace('{CHIPS}', chips))

    # ── swap the slide region ──
    a = s.index('    <!-- ── COVER ')
    b = s.index('    <!-- ── DECK CHROME ')
    s = s[:a] + slides + '\n' + s[b:]

    # ── palette ──
    s = re.sub(r"  --hero: url\('sample-hero\.jpg'\);.*?--contrast      : #1ded49;",
               PALETTE, s, count=1, flags=re.S)

    # ── a bright, airy hero wants the paper theme ──
    s = s.replace('\n/* ── Fixed tokens',
                  '\n/* the scene slide: artwork full-bleed, caption on an opaque card. The\n   theme rule for .card is more specific, so this has to be too. */\n'
                  'html[data-theme="light"] .card.scene-plate,\n'
                  '.card.scene-plate { background: var(--surface); backdrop-filter: none; }\n'
                  '.scene-plate .prose { text-shadow: none; font-size: 18px; }\n'
                  '.scene-spacer { flex: 1 1 auto; min-height: 0; }\n'
                  '\n/* ── Fixed tokens', 1)

    s = s.replace('<html lang="en">', '<html lang="en" data-theme="light">', 1)
    if '<html lang="en" data-theme="light">' not in s:
        s = re.sub(r'<html([^>]*)>', r'<html\1 data-theme="light">', s, count=1)

    s = s.replace('<title>' + re.search(r'<title>(.*?)</title>', s, re.S).group(1) + '</title>',
                  '<title>Describing a Picture — Forbes English</title>', 1)

    # ── i18n ──
    import i18n_picture as I
    block = 'const UI_I18N = {\n' + ",\n".join(
        '  %s: %s' % (code, I.render(code)) for code in
        ['en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']) + '\n};'
    s = re.sub(r'const UI_I18N = \{.*?\n\};', block, s, count=1, flags=re.S)

    open(OUT, 'w', encoding='utf-8').write(s)
    n = s.count('<section class="slide')
    print('wrote %s — %d slides, %d questions, %d words, %d bytes'
          % (OUT, n, len(QUESTIONS), len(VOCAB), len(s)))


if __name__ == '__main__':
    import sys
    sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
    build()
