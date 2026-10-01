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
  var AC = window.AudioContext || window.webkitAudioContext;
  if (!track || !AC || document.querySelector('.camp-music, .camp-music-rpg, .camp-music-float')) return;
  if (navigator.connection && navigator.connection.saveData) return;
  /* Where the switch goes (2026-09-30, the RPGs got music too):
       deck  - the grammar decks' .deck-bar, after the route-map chip;
       rpg   - the RPG engine's HUD (lesson-template/build/rpg/rpg.py), after
               its SOUND button, as one more .utility button in its style;
       float - anything else (the three hand-built RPGs redraw their HUD
               on every scene, which would wipe an inserted button): a small
               round button fixed in the bottom-left corner. */
  var bar = document.querySelector('.deck-bar');
  var rpgSound = document.querySelector('#sound.utility');
  var mode = bar ? 'deck' : rpgSound ? 'rpg' : 'float';
  var loop = (me.getAttribute('data-loop') || '').split(/\s+/).map(Number);

  // Innes, 2026-10-01: "lower backing track, dont stop when playing clips".
  // 0.12 (was 0.2, -4.4 dB). Under a clip it keeps playing at half, so the
  // clip's lines stay clear (it used to go silent, because some clips carry
  // their own music).
  var LEVEL = 0.12, DUCK = 0.06;
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
    '.camp-music-rpg[aria-pressed="false"]{opacity:.7}' +
    '.camp-music-float{position:fixed;z-index:60;left:calc(12px + env(safe-area-inset-left,0px));' +
    'bottom:calc(12px + env(safe-area-inset-bottom,0px));width:44px;height:44px;border-radius:50%;padding:0;' +
    'display:grid;place-items:center;cursor:pointer;color:var(--bone,var(--text,#f3ead3));' +
    // Solid, not a tint of the page's panel: on the hub that panel is
    // see-through and the text behind showed through the button.
    'background:#14201a;box-shadow:0 2px 10px #0008;' +
    'border:1px solid color-mix(in srgb,var(--accent,#d9b25a) 60%,transparent)}' +
    '.camp-music-float svg{width:20px;height:20px}' +
    '.camp-music-float[aria-pressed="false"] .cm-note{opacity:.45}' +
    '.camp-music-float .cm-x{display:none}.camp-music-float[aria-pressed="false"] .cm-x{display:inline}' +
    '@media print{.camp-music,.camp-music-rpg,.camp-music-float{display:none!important}}';
  document.head.appendChild(css);

  var NOTE = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" ' +
    'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><g class="cm-note"><path d="M6 12.5V3.2l7-1.4v9.1"/>' +
    '<circle cx="4.2" cy="12.5" r="1.9"/><circle cx="11.2" cy="10.9" r="1.9"/></g>' +
    '<path class="cm-x" d="M1.5 1.5l13 13"/></svg>';
  var btn = document.createElement('button');
  btn.type = 'button';
  if (mode === 'deck') {
    btn.className = 'camp-music';
    btn.innerHTML = NOTE + '<span class="cm-l"></span>';
    var home = bar.querySelector('.camp-home');
    bar.insertBefore(btn, home ? home.nextSibling : bar.firstChild);
  } else if (mode === 'rpg') {
    // The engine's utility buttons are an emoji plus a .u-label; follow suit.
    btn.className = 'utility camp-music-rpg';
    btn.innerHTML = '🎵<span class="u-label cm-l"></span>';
    rpgSound.parentNode.insertBefore(btn, rpgSound.nextSibling);
  } else {
    btn.className = 'camp-music-float';
    btn.innerHTML = NOTE;
    document.body.appendChild(btn);
  }

  var on = true;
  try { on = localStorage.getItem('bc-music') !== 'off'; } catch (_) {}

  function label() {
    var lang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase().slice(0, 2);
    var L = T[lang] || T.en;
    var l = btn.querySelector('.cm-l');
    if (l) l.textContent = mode === 'rpg' ? (on ? L[1] : L[2]).toUpperCase() : L[0];
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.setAttribute('aria-label', on ? L[1] : L[2]);
    btn.title = on ? L[1] : L[2];
  }
  label();
  if (window.MutationObserver) new MutationObserver(label).observe(document.documentElement,
    { attributes: true, attributeFilter: ['lang'] });

  /* PHONES. Safari on iPhone only lets audio start inside a real gesture -
     the finger LIFTING (touchend, click), not landing: a touch pointerdown is
     not a user activation in the HTML spec, and the first version listened
     only to pointerdown, so on an iPhone the music never started (Innes,
     2026-09-30: "music or maybe audio doesnt work on phone"). Chrome let it
     through because it resumes on any later call once the page has been
     touched at all. So: create and resume the context synchronously inside
     every gesture event until it runs, and play a one-sample silent buffer
     there, which is what opens iOS's audio path.
     An iPhone's silent switch also mutes Web Audio (not <video>) unless the
     page declares itself playback; navigator.audioSession does that on iOS 17+. */
  var ctx = null, gain = null, loading = null, started = false, blipped = false;
  function ensureContext() {
    if (ctx) return;
    try { if (navigator.audioSession) navigator.audioSession.type = 'playback'; } catch (_) {}
    ctx = new AC();
    gain = ctx.createGain(); gain.gain.value = 0; gain.connect(ctx.destination);
  }
  function unlock() {
    ensureContext();
    if (ctx.state !== 'running') { var p = ctx.resume(); if (p && p.catch) p.catch(function () {}); }
    if (!blipped) {
      try {
        var s = ctx.createBufferSource();
        s.buffer = ctx.createBuffer(1, 1, 22050); s.connect(ctx.destination); s.start(0);
        blipped = true;
      } catch (_) {}
    }
  }
  function start() {
    ensureContext();
    if (loading) return loading;
    loading = fetch(track).then(function (r) { if (!r.ok) throw new Error(r.status); return r.arrayBuffer(); })
      .then(function (b) { return new Promise(function (ok, no) { ctx.decodeAudioData(b, ok, no); }); })
      .then(function (buf) {
        var src = ctx.createBufferSource();
        src.buffer = buf; src.loop = true;
        if (loop.length === 2 && loop[1] > loop[0]) { src.loopStart = loop[0]; src.loopEnd = loop[1]; }
        src.connect(gain);
        src.start(0, loop.length === 2 ? loop[0] : 0);
        started = true;
        apply();
      })
      .catch(function () { btn.hidden = true; });
    return loading;
  }
  function playing() { return !!(ctx && started && ctx.state === 'running'); }
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
    // Chrome resumes here once the page has had any gesture; iOS ignores it
    // and waits for the next gesture below.
    if (on && !document.hidden && ctx.state !== 'running') {
      var p = ctx.resume(); if (p && p.catch) p.catch(function () {});
    }
  }
  setInterval(apply, 150);

  function gesture() {
    if (!on || document.hidden) return;
    unlock();
    start();
  }
  ['pointerdown', 'pointerup', 'touchend', 'click', 'keydown'].forEach(function (ev) {
    document.addEventListener(ev, gesture, { capture: true, passive: true });
  });

  btn.addEventListener('click', function () {
    // A tap on Music while it is meant to be on but is not sounding yet (the
    // first tap of the visit, or after the phone suspended it) is a request
    // to hear it, not to switch it off.
    if (on && !playing()) { unlock(); start(); apply(); return; }
    on = !on;
    try { localStorage.setItem('bc-music', on ? 'on' : 'off'); } catch (_) {}
    label();
    if (on) { unlock(); start(); }
    apply();
    if (!on && ctx) setTimeout(function () { if (!on && ctx) ctx.suspend(); }, 600);
  });
  // The RPGs' help line offers S for sound and F for fullscreen; M is music.
  if (mode === 'rpg') document.addEventListener('keydown', function (e) {
    if ((e.key === 'm' || e.key === 'M') && !e.target.matches('input, textarea, select')) btn.click();
  });
  document.addEventListener('visibilitychange', function () {
    if (!ctx) return;
    var p = document.hidden ? ctx.suspend() : (on ? ctx.resume() : null);
    if (p && p.catch) p.catch(function () {});
  });
})();
