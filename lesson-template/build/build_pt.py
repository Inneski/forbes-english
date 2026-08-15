# -*- coding: utf-8 -*-
"""Present Simple vs Present Continuous — speed sorting.

This one stays a game. It was already a falling-word sorter and that is
the right shape for a closed two-way contrast; the reference the user
sent (a Wordwall speed-sorting activity) is the same idea. What it needed
was the teaching, the honesty and the house style.

**Four of the twenty words were keyed wrong.** `today`, `this week`,
`this month` and `these days` were all marked present continuous only.
Every one of them takes the present simple just as readily — *I have
three lessons today*, *the shop closes at six this week*, *these days
people work from home*. A learner who knew that was marked wrong for
knowing it. They are now a third box, *either — the meaning decides*,
which turns the lesson's worst items into its most interesting ones, and
six more of that kind have been added so the box is worth having.

**The game taught nothing.** No rule anywhere, and the only feedback was
a coloured flash: right and wrong looked different and said nothing. A
learner who did not already know the answer could not learn it by
playing. There is now a rule card before play, reachable again from the
game, and every card carries its own explanation, shown on a miss.

**You had to wait for the card to land.** `guess()` returned early while
`dropping` was true, so every single item had dead time before an answer
was accepted — in a game whose name is *speed sorting*. You can now
answer the moment you can read the card.

**The card said you could drag it.** `cursor: grab`, and
`:active { cursor: grabbing }`, with no drag implemented anywhere. Drag
works now; so does clicking a box, and so do the number keys, which the
old version supported and never mentioned.

**Also:** no logo, no hero, its own font stack, palette invented rather
than derived, and no German — in a lesson whose sibling files all carry
it.
"""
import json, sys
sys.path.insert(0, '/tmp')
import deck as D

OUT = '/home/claude/forbes-english/present-simple-vs-continuous.html'
TPL = '/home/claude/forbes-english/lesson-template/lesson-template.html'
DATA = json.load(open('/tmp/pt_data.json', encoding='utf-8'))
LOGO = D.logo_from(TPL)

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Present Simple vs Present Continuous — Forbes English</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
/* Palette derived from PresentTenses/hero.jpg with extract-palette.py, like
   every other lesson on the site. The old version of this page invented
   #1a1a2e and two bin gradients from nothing. */
:root {
  --hero: url('PresentTenses/hero.jpg');
  --void          : #0c0f0e;
  --surface       : #161c1a;
  --surface2      : #1f2725;
  --border        : #ac6162;
  --text          : #f5f2f2;
  --text-dim      : #bfa3a4;
  --accent        : #e48f90;
  --accent-bright : #f3adae;
  --accent-dim    : #cc4b4c;
  --secondary     : #586e84;
  --contrast      : #1ded86;
  --ok: #35c98b; --no: #e4626f;
  --font-display: 'Playfair Display', Georgia, serif;
  --font-ui: 'DM Sans', system-ui, sans-serif;
  --font-mono: 'DM Mono', ui-monospace, monospace;
  --r: 14px;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font-ui); color: var(--text); background: var(--void);
  height: 100vh; width: 100vw; overflow: hidden;
}
#bg { position: fixed; inset: 0; z-index: 0; overflow: hidden; }
#bg::before {
  content: ''; position: absolute; inset: 0;
  background: var(--hero) center / cover no-repeat;
  opacity: .30; filter: saturate(.8);
}
#bg::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(180deg,
    color-mix(in srgb, var(--void) 55%, transparent) 0%,
    color-mix(in srgb, var(--void) 25%, transparent) 40%,
    color-mix(in srgb, var(--void) 80%, transparent) 100%);
}
#wrap {
  position: fixed; inset: 0; z-index: 10;
  display: flex; flex-direction: column;
  max-width: 1100px; margin: 0 auto;
}

/* ── top bar ── */
#top {
  display: flex; align-items: center; justify-content: space-between;
  gap: 16px; padding: 12px 20px;
  border-bottom: 1px solid color-mix(in srgb, var(--border) 40%, transparent);
  background: color-mix(in srgb, var(--void) 70%, transparent);
  backdrop-filter: blur(6px);
}
.fe-logo { width: 96px; height: auto; display: block; }
.fe-logo-mark { color: var(--accent); }
.fe-logo-word { fill: var(--text); opacity: 0; transition: opacity .25s ease; }
.fonts-ready .fe-logo-word { opacity: 1; }
#top-right { display: flex; align-items: center; gap: 10px; }
.badge {
  font-family: var(--font-mono); font-size: 12px; color: var(--text);
  background: color-mix(in srgb, var(--surface2) 80%, transparent);
  border: 1px solid color-mix(in srgb, var(--border) 45%, transparent);
  border-radius: 999px; padding: 5px 13px; white-space: nowrap;
}
.tbtn {
  font-family: var(--font-mono); font-size: 12px; color: var(--text);
  background: transparent;
  border: 1px solid color-mix(in srgb, var(--border) 45%, transparent);
  border-radius: 999px; padding: 5px 13px; cursor: pointer;
}
.tbtn:hover { border-color: var(--accent); }
select.tbtn { padding-right: 8px; }

/* ── arena ── */
#arena { flex: 1; position: relative; overflow: hidden; }
#rail {
  position: absolute; left: 50%; top: 0; bottom: 200px;
  transform: translateX(-50%); width: 2px;
  background: linear-gradient(180deg,
    transparent, color-mix(in srgb, var(--accent) 45%, transparent), transparent);
}
#card {
  position: absolute; left: 50%; transform: translateX(-50%);
  font-family: var(--font-display); font-size: 30px; font-weight: 700;
  color: var(--void); background: var(--accent-bright);
  border-radius: var(--r); padding: 14px 30px; white-space: nowrap;
  box-shadow: 0 10px 40px rgba(0,0,0,.45); cursor: grab; user-select: none;
  z-index: 20;
}
#card:active { cursor: grabbing; }
#card.dragging { opacity: .5; }
#card.good { background: var(--ok); }
#card.bad  { background: var(--no); color: var(--text); animation: shake .3s; }
@keyframes shake { 25%{transform:translateX(calc(-50% - 5px))} 75%{transform:translateX(calc(-50% + 5px))} }

/* ── bins ── */
#bins {
  position: absolute; left: 0; right: 0; bottom: 0; height: 200px;
  display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; padding: 12px 16px 18px;
  z-index: 15;
}
.bin {
  border-radius: var(--r); cursor: pointer; position: relative;
  border: 2px dashed color-mix(in srgb, var(--border) 55%, transparent);
  background: color-mix(in srgb, var(--surface) 80%, transparent);
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  gap: 8px; padding: 14px; text-align: center;
  transition: border-color .12s, background .12s, transform .1s;
}
.bin:hover, .bin.over { border-style: solid; border-color: var(--accent); transform: translateY(-2px); }
.bin.pop { animation: pop .22s ease-out; }
@keyframes pop { 50% { transform: scale(1.04); } }
.bin-key {
  font-family: var(--font-mono); font-size: 11px; color: var(--void);
  background: var(--accent); border-radius: 999px; width: 22px; height: 22px;
  display: grid; place-items: center;
}
.bin-label { font-family: var(--font-ui); font-weight: 600; font-size: 17px; }
.bin-sub {
  font-family: var(--font-mono); font-size: 10.5px; letter-spacing: .06em;
  text-transform: uppercase; color: var(--text-dim);
}
.bin-count {
  position: absolute; top: 10px; right: 12px;
  font-family: var(--font-mono); font-size: 12px; color: var(--text-dim);
}
#bar-wrap { position: absolute; left: 0; right: 0; bottom: 200px; height: 3px;
  background: rgba(0,0,0,.35); z-index: 15; }
#bar { height: 100%; width: 0; background: var(--accent); transition: width .3s; }

/* ── why line ── */
#why {
  position: absolute; left: 50%; bottom: 214px; transform: translateX(-50%);
  width: min(760px, 92%); z-index: 18;
  background: color-mix(in srgb, var(--surface) 94%, transparent);
  border: 1px solid color-mix(in srgb, var(--border) 50%, transparent);
  border-left: 5px solid var(--ok);
  border-radius: 10px; padding: 12px 16px;
  font-size: 16px; line-height: 1.45; color: var(--text);
  opacity: 0; pointer-events: none; transition: opacity .18s;
}
#why.show { opacity: 1; }
#why.no { border-left-color: var(--no); }

/* ── overlays ── */
.overlay {
  position: fixed; inset: 0; z-index: 100; display: none;
  align-items: center; justify-content: center; padding: 24px;
  background: color-mix(in srgb, var(--void) 78%, transparent);
  backdrop-filter: blur(5px);
}
.overlay.show { display: flex; }
.sheet {
  background: color-mix(in srgb, var(--surface) 96%, transparent);
  border: 1px solid color-mix(in srgb, var(--border) 50%, transparent);
  border-radius: 20px; padding: 30px 34px; max-width: 880px; width: 100%;
  box-shadow: 0 20px 70px rgba(0,0,0,.6);
}
.eyebrow {
  font-family: var(--font-mono); font-size: 11.5px; letter-spacing: .14em;
  text-transform: uppercase; color: var(--accent-bright); margin-bottom: 8px;
}
.sheet h2 {
  font-family: var(--font-display); font-size: 32px; font-weight: 700;
  line-height: 1.15; margin-bottom: 18px;
}
.sheet h2 em { color: var(--accent-bright); font-style: italic; }
.rules { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; margin-bottom: 20px; }
.rule {
  background: color-mix(in srgb, var(--surface2) 85%, transparent);
  border: 1px solid color-mix(in srgb, var(--border) 40%, transparent);
  border-radius: 12px; padding: 16px;
}
.rule h3 { font-size: 17px; font-weight: 700; color: var(--accent-bright); margin-bottom: 6px; }
.rule p { font-size: 15.5px; line-height: 1.45; }
.rule .n { font-size: 13.5px; color: var(--text-dim); margin-top: 8px; line-height: 1.5; }
.howto { font-size: 14.5px; color: var(--text-dim); margin-bottom: 18px; }
.btn {
  font-family: var(--font-ui); font-size: 16px; font-weight: 600;
  background: var(--accent); color: var(--void); border: none;
  border-radius: 999px; padding: 13px 32px; cursor: pointer;
}
.btn:hover { background: var(--accent-bright); }
.big { font-family: var(--font-display); font-size: 58px; font-weight: 900; line-height: 1; }
.big span { color: var(--text-dim); font-size: 32px; }
.pills { display: flex; gap: 12px; justify-content: center; margin: 14px 0 18px; }
.pill { font-family: var(--font-mono); font-size: 13px; border-radius: 999px; padding: 7px 16px; }
.pill.g { background: color-mix(in srgb, var(--ok) 22%, transparent); color: var(--ok); }
.pill.b { background: color-mix(in srgb, var(--no) 22%, transparent); color: var(--no); }
.centre { text-align: center; }
@media (max-width: 820px) {
  .rules, #bins { grid-template-columns: 1fr; }
  #bins { height: auto; position: static; }
}
</style>
</head>
<body>

<div id="bg"></div>

<div id="wrap">
  <div id="top">
    LOGO_HERE
    <div id="top-right">
      <select class="tbtn" id="lang" aria-label="Language">
        <option value="en">English</option>
        <option value="de">Deutsch</option>
      </select>
      <button class="tbtn" id="btn-rule"></button>
      <span class="badge"><span id="left">0</span> <span id="left-l"></span></span>
      <span class="badge"><span id="score-l"></span> <span id="score">0</span></span>
    </div>
  </div>

  <div id="arena">
    <div id="rail"></div>
    <div id="card" style="display:none"></div>
    <div id="why"></div>
    <div id="bar-wrap"><div id="bar"></div></div>
    <div id="bins"></div>
  </div>
</div>

<div class="overlay show" id="intro">
  <div class="sheet">
    <div class="eyebrow" id="i-eyebrow"></div>
    <h2 id="i-title"></h2>
    <div class="rules">
      <div class="rule"><h3 id="r1h"></h3><p id="r1b"></p><p class="n" id="r1n"></p></div>
      <div class="rule"><h3 id="r2h"></h3><p id="r2b"></p><p class="n" id="r2n"></p></div>
      <div class="rule"><h3 id="r3h"></h3><p id="r3b"></p><p class="n" id="r3n"></p></div>
    </div>
    <p class="howto" id="i-howto"></p>
    <div class="centre"><button class="btn" id="i-play"></button></div>
  </div>
</div>

<div class="overlay" id="done">
  <div class="sheet centre">
    <div class="eyebrow" id="d-eyebrow"></div>
    <div class="big"><span id="d-score">0</span><span> / TOTAL</span></div>
    <div class="pills">
      <span class="pill g" id="d-good"></span>
      <span class="pill b" id="d-bad"></span>
    </div>
    <p id="d-msg" style="font-size:16px;line-height:1.5;margin-bottom:20px"></p>
    <button class="btn" id="d-again"></button>
  </div>
</div>

<script>
const DATA = DATA_HERE;
const WORDS = DATA.words, BINS = DATA.bins, I18N = DATA.i18n;
let lang = 'en';
const t = k => (I18N[lang] && I18N[lang][k] != null) ? I18N[lang][k] : I18N.en[k];

document.fonts.ready.then(() => document.documentElement.classList.add('fonts-ready'));
setTimeout(() => document.documentElement.classList.add('fonts-ready'), 1500);

const $ = id => document.getElementById(id);
const cardEl = $('card'), whyEl = $('why'), binsEl = $('bins');

function buildBins() {
  binsEl.innerHTML = '';
  BINS[lang].forEach((label, i) => {
    const b = document.createElement('div');
    b.className = 'bin'; b.dataset.bin = i;
    b.innerHTML = '<div class="bin-key">' + (i + 1) + '</div>' +
      '<div class="bin-label">' + label + '</div>' +
      '<div class="bin-count" data-count="' + i + '">0</div>';
    binsEl.appendChild(b);
  });
}

function paint() {
  document.documentElement.lang = lang;
  $('i-eyebrow').innerHTML = t('ruleEyebrow');
  $('i-title').innerHTML = t('ruleTitle');
  ['r1h','r1b','r1n','r2h','r2b','r2n','r3h','r3b','r3n']
    .forEach(k => $(k).innerHTML = t(k));
  $('i-howto').innerHTML = t('howto');
  $('i-play').innerHTML = t('play');
  $('btn-rule').innerHTML = t('backRule');
  $('left-l').innerHTML = t('left');
  $('score-l').innerHTML = t('scoreLabel');
  $('d-eyebrow').innerHTML = t('doneTitle');
  $('d-again').innerHTML = t('again');
  buildBins();
  renderCounts();
}

/* ── game state ── */
let queue = [], i = 0, right = 0, wrong = 0, counts = [0,0,0];
let live = false, locked = false, dragging = false;
let y = 0, raf = null;

const shuffle = a => a.map(v => [Math.random(), v]).sort((p, q) => p[0] - q[0]).map(p => p[1]);

function start() {
  $('intro').classList.remove('show');
  $('done').classList.remove('show');
  queue = shuffle(WORDS.map((w, n) => n));
  i = 0; right = 0; wrong = 0; counts = [0,0,0];
  live = true;
  renderCounts(); next();
}

function renderCounts() {
  counts.forEach((c, n) => {
    const el = binsEl.querySelector('[data-count="' + n + '"]');
    if (el) el.textContent = c;
  });
  $('left').textContent = Math.max(0, queue.length - i);
  $('score').textContent = right;
  $('bar').style.width = (queue.length ? (i / queue.length) * 100 : 0) + '%';
}

function next() {
  if (i >= queue.length) return finish();
  const w = WORDS[queue[i]];
  cardEl.innerHTML = w.t;
  cardEl.className = '';
  cardEl.style.display = 'block';
  cardEl.setAttribute('draggable', 'true');
  y = 8; cardEl.style.top = y + 'px';
  locked = false;
  hideWhy();
  cancelAnimationFrame(raf);
  fall();
}

/* The card falls, but an answer is accepted from the first frame — the old
   version refused input until it landed, which put dead time in front of
   every single item in a game called speed sorting. */
function fall() {
  const stop = binsEl.getBoundingClientRect().top
             - $('arena').getBoundingClientRect().top - cardEl.offsetHeight - 74;
  if (y < stop) { y += 1.9; cardEl.style.top = y + 'px'; raf = requestAnimationFrame(fall); }
  else { y = Math.max(8, stop); cardEl.style.top = y + 'px'; }
}

function showWhy(text, ok) {
  whyEl.innerHTML = text;
  whyEl.classList.toggle('no', !ok);
  whyEl.classList.add('show');
}
function hideWhy() { whyEl.classList.remove('show'); }

function answer(bin) {
  if (!live || locked) return;
  locked = true;
  cancelAnimationFrame(raf);
  const w = WORDS[queue[i]];
  const ok = bin === w.b;
  if (ok) { right++; counts[bin]++; } else { wrong++; }
  cardEl.classList.add(ok ? 'good' : 'bad');
  const b = binsEl.querySelector('.bin[data-bin="' + bin + '"]');
  if (b) { b.classList.add('pop'); setTimeout(() => b.classList.remove('pop'), 230); }
  // Every card explains itself. The old version's entire feedback was a
  // colour, so a learner who did not already know could not find out.
  showWhy(w.why, ok);
  renderCounts();
  setTimeout(() => {
    cardEl.style.display = 'none';
    i++; renderCounts();
    setTimeout(() => (i < queue.length ? next() : finish()), 150);
  }, ok ? 1100 : 2600);
}

function finish() {
  live = false;
  cardEl.style.display = 'none';
  hideWhy();
  const total = queue.length;
  $('d-score').textContent = right;
  $('d-score').nextElementSibling.textContent = ' / ' + total;
  $('d-good').textContent = '\\u2713 ' + right + ' ' + t('correct');
  $('d-bad').textContent  = '\\u2717 ' + wrong + ' ' + t('wrong');
  const p = total ? right / total : 0;
  $('d-msg').innerHTML = p === 1 ? t('band4') : p >= .75 ? t('band3')
                        : p >= .5 ? t('band2') : t('band1');
  $('done').classList.add('show');
}

/* ── input: click a bin, drag onto it, or press 1/2/3 ── */
binsEl.addEventListener('click', e => {
  const b = e.target.closest('.bin');
  if (b) answer(+b.dataset.bin);
});
cardEl.addEventListener('dragstart', e => {
  if (!live || locked) return e.preventDefault();
  dragging = true; cardEl.classList.add('dragging');
  e.dataTransfer.effectAllowed = 'move';
  e.dataTransfer.setData('text/plain', '');
});
cardEl.addEventListener('dragend', () => {
  dragging = false; cardEl.classList.remove('dragging');
  binsEl.querySelectorAll('.bin').forEach(b => b.classList.remove('over'));
});
binsEl.addEventListener('dragover', e => {
  const b = e.target.closest('.bin');
  if (!b) return;
  e.preventDefault(); b.classList.add('over');
});
binsEl.addEventListener('dragleave', e => {
  const b = e.target.closest('.bin');
  if (b) b.classList.remove('over');
});
binsEl.addEventListener('drop', e => {
  const b = e.target.closest('.bin');
  if (!b) return;
  e.preventDefault(); b.classList.remove('over');
  answer(+b.dataset.bin);
});
addEventListener('keydown', e => {
  if (!live) return;
  if (e.key === '1' || e.key === 'ArrowLeft')  answer(0);
  if (e.key === '2' || e.key === 'ArrowDown')  answer(1);
  if (e.key === '3' || e.key === 'ArrowRight') answer(2);
});

$('i-play').addEventListener('click', start);
$('d-again').addEventListener('click', start);
$('btn-rule').addEventListener('click', () => {
  live = false; cancelAnimationFrame(raf); cardEl.style.display = 'none';
  $('intro').classList.add('show');
});
$('lang').addEventListener('change', e => { lang = e.target.value; paint(); });

paint();
</script>
</body>
</html>
'''

html = HTML.replace('LOGO_HERE', LOGO)
html = html.replace('DATA_HERE', json.dumps(DATA, ensure_ascii=False))
html = html.replace('<span> / TOTAL</span>', '<span> / %d</span>' % len(DATA['words']))
open(OUT, 'w', encoding='utf-8').write(html)
print('wrote %s — %d bytes, %d words' % (OUT, len(html), len(DATA['words'])))
