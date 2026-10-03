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
  /* slot  - a page that marks an element data-camp-music-slot gets the
             round button inside it, in the page's own flow (2026-10-02: the
             float sat on station 9 of the descent and on the hub's buttons
             on a phone). */
  var slot = document.querySelector('[data-camp-music-slot]');
  var mode = bar ? 'deck' : rpgSound ? 'rpg' : slot ? 'slot' : 'float';
  var loop = (me.getAttribute('data-loop') || '').split(/\s+/).map(Number);

  // Innes, 2026-10-01: "lower backing track, dont stop when playing clips".
  // 0.12 (was 0.2, -4.4 dB). Under a clip it keeps playing at half, so the
  // clip's lines stay clear (it used to go silent, because some clips carry
  // their own music).
  var LEVEL = 0.12, DUCK = 0.06;
  var T = {
    en: ['Music', 'Music on', 'Music off', 'Music volume'], de: ['Musik', 'Musik an', 'Musik aus', 'Musiklautstärke'],
    es: ['Música', 'Música activada', 'Música desactivada', 'Volumen de la música'],
    fr: ['Musique', 'Musique activée', 'Musique coupée', 'Volume de la musique'],
    it: ['Musica', 'Musica attiva', 'Musica spenta', 'Volume della musica'],
    pt: ['Música', 'Música ligada', 'Música desligada', 'Volume da música'],
    ru: ['Музыка', 'Музыка включена', 'Музыка выключена', 'Громкость музыки'],
    ar: ['الموسيقى', 'الموسيقى تعمل', 'الموسيقى متوقفة', 'مستوى صوت الموسيقى'],
    zh: ['音乐', '音乐已开', '音乐已关', '音乐音量'], ja: ['音楽', '音楽オン', '音楽オフ', '音楽の音量']
  };
  /* VOLUME (Innes, 2026-10-03: "add volume sliders on all block camps").
     A slider 0-100 beside the switch, remembered per viewer ('bc-music-vol').
     50 is the level above, unchanged for anyone who never touches it; each
     step either side is 0.24 dB, so the ends are +-12 dB (100 = 0.48 gain,
     still under full scale on a -16.5 dBFS track), and 0 is silence. */
  var vol = 50;
  try { var sv = parseInt(localStorage.getItem('bc-music-vol'), 10); if (sv >= 0 && sv <= 100) vol = sv; } catch (_) {}
  function mul() { return vol <= 0 ? 0 : Math.pow(10, (vol - 50) / 50 * 12 / 20); }

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
    '.camp-music-float.camp-music-slot{position:static;flex:none}' +
    '.camp-music-float[aria-pressed="false"] .cm-note{opacity:.45}' +
    '.camp-music-float .cm-x{display:none}.camp-music-float[aria-pressed="false"] .cm-x{display:inline}' +
    // the volume slider: one input, dressed for wherever the switch went
    '.camp-vol{-webkit-appearance:none;appearance:none;display:block;width:84px;height:22px;margin:0;padding:0;' +
    'background:transparent;cursor:pointer;--cv-fill:var(--accent,#d9b25a);' +
    '--cv-track:color-mix(in srgb,currentColor 28%,transparent)}' +
    '.camp-vol:focus{outline:none}.camp-vol:focus-visible{outline:2px solid var(--cv-fill);outline-offset:3px;border-radius:3px}' +
    '.camp-vol::-webkit-slider-runnable-track{height:4px;border-radius:2px;' +
    'background:linear-gradient(to right,var(--cv-fill) var(--cv,50%),var(--cv-track) var(--cv,50%))}' +
    '.camp-vol::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;width:14px;height:14px;margin-top:-5px;' +
    'border-radius:50%;border:0;background:var(--cv-fill)}' +
    '.camp-vol::-moz-range-track{height:4px;border-radius:2px;background:var(--cv-track)}' +
    '.camp-vol::-moz-range-progress{height:4px;border-radius:2px;background:var(--cv-fill)}' +
    '.camp-vol::-moz-range-thumb{width:14px;height:14px;border-radius:50%;border:0;background:var(--cv-fill)}' +
    '.camp-vol.cv-off{opacity:.5}' +
    '.camp-music-grp{display:inline-flex;align-items:center;gap:10px;flex:none;color:var(--text)}' +
    // RPG HUD: a pill in the engine's .utility style (the class supplies the
    // border, panel and padding); wider steps for a finger on a phone
    '.camp-vol-rpg{display:inline-flex;align-items:center;color:var(--bone)}' +
    '.camp-vol-rpg .camp-vol{width:calc(6 * var(--u,10px));min-width:64px;height:calc(1.6 * var(--u,10px));min-height:18px}' +
    // hub, maps, climb: a solid pill beside the round button, as the button is solid
    '.camp-vol-pill{display:inline-flex;align-items:center;align-self:center;box-sizing:border-box;height:44px;' +
    'padding:0 14px;margin-left:8px;border-radius:22px;background:#14201a;box-shadow:0 2px 10px #0008;' +
    'color:var(--bone,var(--text,#f3ead3));' +
    'border:1px solid color-mix(in srgb,var(--accent,#d9b25a) 60%,transparent)}' +
    '.camp-vol-pill .camp-vol{width:78px}' +
    // the floating button (pages with no bar, HUD or slot): the slider opens
    // beside it on hover or keyboard focus, so it never sits over the page
    '.camp-vol-float{position:fixed;z-index:60;margin:0;left:calc(64px + env(safe-area-inset-left,0px));' +
    'bottom:calc(12px + env(safe-area-inset-bottom,0px));opacity:0;pointer-events:none;transition:opacity .15s}' +
    '.camp-vol-float.cv-show{opacity:1;pointer-events:auto}' +
    '@media (hover:none){.camp-vol-float{display:none}}' +
    '@media print{.camp-music,.camp-music-rpg,.camp-music-float,.camp-vol,.camp-vol-rpg,.camp-vol-pill{display:none!important}}';
  document.head.appendChild(css);

  var NOTE = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" ' +
    'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><g class="cm-note"><path d="M6 12.5V3.2l7-1.4v9.1"/>' +
    '<circle cx="4.2" cy="12.5" r="1.9"/><circle cx="11.2" cy="10.9" r="1.9"/></g>' +
    '<path class="cm-x" d="M1.5 1.5l13 13"/></svg>';
  var btn = document.createElement('button');
  btn.type = 'button';
  var range = document.createElement('input');
  range.type = 'range'; range.min = '0'; range.max = '100'; range.step = '1';
  range.className = 'camp-vol';
  range.value = String(vol);
  var volBox;                                   // what holds the slider, hidden with the button
  if (mode === 'deck') {
    btn.className = 'camp-music';
    btn.innerHTML = NOTE + '<span class="cm-l"></span>';
    volBox = document.createElement('span');
    volBox.className = 'camp-music-grp';
    volBox.appendChild(btn); volBox.appendChild(range);
    var home = bar.querySelector('.camp-home');
    bar.insertBefore(volBox, home ? home.nextSibling : bar.firstChild);
  } else if (mode === 'rpg') {
    // The engine's utility buttons are an emoji plus a .u-label; follow suit.
    btn.className = 'utility camp-music-rpg';
    btn.innerHTML = '🎵<span class="u-label cm-l"></span>';
    rpgSound.parentNode.insertBefore(btn, rpgSound.nextSibling);
    volBox = document.createElement('span');
    volBox.className = 'utility camp-vol-rpg';
    volBox.appendChild(range);
    btn.parentNode.insertBefore(volBox, btn.nextSibling);
    // the engine sized its panel under the HUD before these two were in it;
    // on a phone the HUD gains a row, so ask it to measure again
    if (typeof window.fitZone === 'function') try { window.fitZone(); } catch (_) {}
  } else if (mode === 'slot') {
    btn.className = 'camp-music-float camp-music-slot';
    btn.innerHTML = NOTE;
    slot.appendChild(btn);
    volBox = document.createElement('span');
    volBox.className = 'camp-vol-pill';
    volBox.appendChild(range);
    slot.appendChild(volBox);
    // as tall as the round button the page drew (44 px on the hub, 36 on
    // the maps), and the slot's own gap instead of ours when it has one
    var bh = btn.offsetHeight;
    if (bh) { volBox.style.height = bh + 'px'; volBox.style.borderRadius = bh / 2 + 'px'; }
    if (parseFloat(getComputedStyle(slot).columnGap) > 0) volBox.style.marginLeft = '0';
  } else {
    btn.className = 'camp-music-float';
    btn.innerHTML = NOTE;
    document.body.appendChild(btn);
    volBox = document.createElement('span');
    volBox.className = 'camp-vol-pill camp-vol-float';
    volBox.appendChild(range);
    document.body.appendChild(volBox);
    // open on hover or focus of either, close a moment after both are left
    var hideT = null;
    var show = function () { clearTimeout(hideT); volBox.classList.add('cv-show'); };
    var hide = function () {
      clearTimeout(hideT);
      hideT = setTimeout(function () {
        if (!btn.matches(':hover') && !volBox.matches(':hover') && !volBox.contains(document.activeElement) &&
            !btn.matches(':focus-visible')) volBox.classList.remove('cv-show');
      }, 700);
    };
    [btn, volBox].forEach(function (el) {
      el.addEventListener('mouseenter', show); el.addEventListener('mouseleave', hide);
      el.addEventListener('focusin', show); el.addEventListener('focusout', hide);
    });
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
    range.setAttribute('aria-label', L[3]);
    range.title = L[3];
    range.classList.toggle('cv-off', !on);
    range.style.setProperty('--cv', vol + '%');
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
      .catch(function () { btn.hidden = true; volBox.hidden = true; });
    return loading;
  }
  function playing() { return !!(ctx && started && ctx.state === 'running'); }
  function target() {
    if (!on) return 0;
    var vs = document.querySelectorAll('.bg-clip');
    for (var i = 0; i < vs.length; i++) {
      var v = vs[i];
      if (v.classList.contains('run') && !v.paused && !v.ended && !v.muted) return DUCK * mul();
    }
    return LEVEL * mul();
  }
  var last = -1;
  function apply(fast) {
    if (!ctx || !gain) return;
    var g = target();
    // a slider moves the level at once; the switch and the clips fade
    if (g !== last) { gain.gain.setTargetAtTime(g, ctx.currentTime, fast ? 0.03 : g < last ? 0.08 : 0.6); last = g; }
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
  /* The slider. Moving it while the music is off is a request to hear it, so
     it switches the music on. Its keys stay its own (a deck turns the slide
     on the arrow keys), and a mouse or finger lets go of it afterwards, so
     the next arrow key goes back to the deck. */
  function setVol(v) {
    vol = Math.max(0, Math.min(100, Math.round(v)));
    try { localStorage.setItem('bc-music-vol', String(vol)); } catch (_) {}
    if (!on && vol > 0) {
      on = true;
      try { localStorage.setItem('bc-music', 'on'); } catch (_) {}
    }
    label();
    if (on) { unlock(); start(); }
    apply(true);
  }
  range.addEventListener('input', function () { setVol(Number(range.value)); });
  range.addEventListener('keydown', function (e) { e.stopPropagation(); });
  range.addEventListener('pointerup', function () { setTimeout(function () { range.blur(); }, 0); });
  // The RPGs' help line offers S for sound and F for fullscreen; M is music.
  if (mode === 'rpg') document.addEventListener('keydown', function (e) {
    if ((e.key === 'm' || e.key === 'M') && !e.target.matches('input, textarea, select')) btn.click();
  });
  /* Start on arrival (Innes, 2026-10-01: "it just needs to come on
     automatically"). Browsers decide: Chrome and Edge let audio start
     without a gesture once this site has been interacted with (arriving by
     a click from the hub, a deck or a map), so it plays at once there. Where
     the browser refuses (a first visit, Safari), the context waits in
     'suspended' and the first gesture below resumes it, as before. */
  if (on && !document.hidden) {
    try {
      ensureContext();
      var r = ctx.resume(); if (r && r.catch) r.catch(function () {});
      start(); apply();
    } catch (_) {}
  }
  document.addEventListener('visibilitychange', function () {
    if (!ctx) return;
    var p = document.hidden ? ctx.suspend() : (on ? ctx.resume() : null);
    if (p && p.catch) p.catch(function () {});
  });
})();
