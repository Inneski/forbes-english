/* Block Camp: a soundtrack under the deck, with a switch to turn it off.

   Innes, 2026-09-30: "give the whole of past simple a sound track that can be
   toggled off". Loaded with
       <script src="block-camp/camp-music.js" data-track="block-camp/music/<name>.m4a"
               data-loop="0.5 30.5" defer></script>
   data-loop is the loop's start and end in the file, in seconds. The file
   carries real music either side of them, so an encoder's few ms of priming
   never lands the seam on silence. Web Audio loops sample-accurately, which
   <audio loop> does not (it gaps on every lap in most browsers).

   On by default, remembered per viewer ('bc-music'). Browsers only allow sound
   after a gesture, so it starts on the first click or key. It fades out while
   a correct-answer clip plays with sound and comes back after, pauses in a
   hidden tab, and stays off under Save-Data. */
(function () {
  'use strict';
  var me = document.currentScript;
  var track = me && me.getAttribute('data-track');
  var bar = document.querySelector('.deck-bar');
  var AC = window.AudioContext || window.webkitAudioContext;
  if (!track || !bar || !AC || document.querySelector('.camp-music')) return;
  if (navigator.connection && navigator.connection.saveData) return;
  var loop = (me.getAttribute('data-loop') || '').split(/\s+/).map(Number);

  // Silent, not just lower, under a clip: several clips carry their own music
  // (the fishing one, 2026-09-30) and two tunes at once is a clash.
  var LEVEL = 0.2, DUCK = 0;
  var T = {
    en: ['Music', 'Music on', 'Music off'], de: ['Musik', 'Musik an', 'Musik aus'],
    es: ['Música', 'Música activada', 'Música desactivada'], fr: ['Musique', 'Musique activée', 'Musique coupée'],
    it: ['Musica', 'Musica attiva', 'Musica spenta'], pt: ['Música', 'Música ligada', 'Música desligada'],
    ru: ['Музыка', 'Музыка включена', 'Музыка выключена'], ar: ['الموسيقى', 'الموسيقى تعمل', 'الموسيقى متوقفة'],
    zh: ['音乐', '音乐已开', '音乐已关'], ja: ['音楽', '音楽オン', '音楽オフ']
  };

  var css = document.createElement('style');
  css.textContent =
    '.camp-music{display:inline-flex;align-items:center;gap:7px;flex:none;box-sizing:border-box;height:34px;' +
    'padding:0 11px;border-radius:6px;cursor:pointer;white-space:nowrap;font-family:var(--font-mono);font-size:12px;' +
    'letter-spacing:.06em;text-transform:uppercase;background:var(--scrim);color:var(--text);' +
    'border:1px solid color-mix(in srgb,var(--border) 70%,transparent);transition:border-color .15s,color .15s}' +
    '.camp-music:hover,.camp-music:focus-visible{border-color:var(--accent);color:var(--accent-bright)}' +
    '.camp-music svg{width:15px;height:15px;flex:none}' +
    '.camp-music[aria-pressed="false"]{color:var(--text-dim)}' +
    '.camp-music[aria-pressed="false"] .cm-note{opacity:.45}' +
    '.camp-music .cm-x{display:none}.camp-music[aria-pressed="false"] .cm-x{display:inline}' +
    '@media print{.camp-music{display:none!important}}';
  document.head.appendChild(css);

  var btn = document.createElement('button');
  btn.type = 'button'; btn.className = 'camp-music';
  btn.innerHTML = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" ' +
    'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><g class="cm-note"><path d="M6 12.5V3.2l7-1.4v9.1"/>' +
    '<circle cx="4.2" cy="12.5" r="1.9"/><circle cx="11.2" cy="10.9" r="1.9"/></g>' +
    '<path class="cm-x" d="M1.5 1.5l13 13"/></svg><span class="cm-l"></span>';
  var home = bar.querySelector('.camp-home');
  bar.insertBefore(btn, home ? home.nextSibling : bar.firstChild);

  var on = true;
  try { on = localStorage.getItem('bc-music') !== 'off'; } catch (_) {}

  function label() {
    var lang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase().slice(0, 2);
    var L = T[lang] || T.en;
    btn.querySelector('.cm-l').textContent = L[0];
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.title = on ? L[1] : L[2];
  }
  label();
  if (window.MutationObserver) new MutationObserver(label).observe(document.documentElement,
    { attributes: true, attributeFilter: ['lang'] });

  var ctx = null, gain = null, loading = null;
  function start() {
    if (ctx) return loading;
    ctx = new AC();
    gain = ctx.createGain(); gain.gain.value = 0; gain.connect(ctx.destination);
    loading = fetch(track).then(function (r) { return r.arrayBuffer(); })
      .then(function (b) { return new Promise(function (ok, no) { ctx.decodeAudioData(b, ok, no); }); })
      .then(function (buf) {
        var src = ctx.createBufferSource();
        src.buffer = buf; src.loop = true;
        if (loop.length === 2 && loop[1] > loop[0]) { src.loopStart = loop[0]; src.loopEnd = loop[1]; }
        src.connect(gain);
        src.start(0, loop.length === 2 ? loop[0] : 0);
        apply();
      })
      .catch(function () { btn.hidden = true; });
    return loading;
  }
  function target() {
    if (!on) return 0;
    var vs = document.querySelectorAll('.bg-clip');
    for (var i = 0; i < vs.length; i++) {
      var v = vs[i];
      if (v.classList.contains('run') && !v.paused && !v.ended && !v.muted) return DUCK;
    }
    return LEVEL;
  }
  var last = -1;
  function apply() {
    if (!ctx || !gain) return;
    var g = target();
    if (g !== last) { gain.gain.setTargetAtTime(g, ctx.currentTime, g < last ? 0.08 : 0.6); last = g; }
    if (on && !document.hidden && ctx.state === 'suspended') ctx.resume();
  }
  setInterval(apply, 150);

  function gesture() {
    if (!on) return;
    start();
    if (ctx && ctx.state === 'suspended') ctx.resume();
  }
  document.addEventListener('pointerdown', gesture, true);
  document.addEventListener('keydown', gesture, true);

  btn.addEventListener('click', function () {
    on = !on;
    try { localStorage.setItem('bc-music', on ? 'on' : 'off'); } catch (_) {}
    label();
    if (on) start();
    apply();
    if (!on && ctx) setTimeout(function () { if (!on && ctx) ctx.suspend(); }, 600);
  });
  document.addEventListener('visibilitychange', function () {
    if (!ctx) return;
    if (document.hidden) ctx.suspend(); else if (on) ctx.resume();
  });
})();
