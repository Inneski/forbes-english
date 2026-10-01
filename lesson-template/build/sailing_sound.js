/* The sound of Sailing the Seas: the sea under everything, gulls now and
   then, a foghorn far off once in a while, and an accordion drifting faintly
   in and out from along the quay. Sounds: sailing_sound.py.

   Innes, 2026-10-01: "sea and birds sounds occasional foghorn, accordion
   fades faintly in and out occasionally". Built on Block Camp's
   camp-music.js, and keeps its hard-won rules: on by default and remembered
   per viewer ('sea-sound'); browsers only allow sound after a gesture, so it
   starts on the first click, tap or key, inside that gesture, with a silent
   one-sample blip to open iOS's audio path; a page that is meant to sound but
   is not yet sounding takes a tap on the button as "play", not "off"; quiet
   in a hidden tab; off under Save-Data. A round button bottom-left. */
(function () {
  'use strict';
  var AC = window.AudioContext || window.webkitAudioContext;
  var cfg = window.SEA_SOUND;
  if (!AC || !cfg || document.querySelector('.sea-sound')) return;
  if (navigator.connection && navigator.connection.saveData) return;

  var LEVEL = 0.6;
  var T = {
    en: ['Sea sounds on', 'Sea sounds off'], de: ['Meeresklänge an', 'Meeresklänge aus'],
    es: ['Sonido del mar activado', 'Sonido del mar desactivado'], fr: ['Bruits de la mer activés', 'Bruits de la mer coupés'],
    it: ['Suoni del mare attivi', 'Suoni del mare spenti'], pt: ['Sons do mar ligados', 'Sons do mar desligados'],
    ru: ['Звуки моря включены', 'Звуки моря выключены'], ar: ['أصوات البحر تعمل', 'أصوات البحر متوقفة'],
    zh: ['海浪声已开', '海浪声已关'], ja: ['波の音オン', '波の音オフ']
  };

  var css = document.createElement('style');
  css.textContent =
    '.sea-sound{position:fixed;z-index:60;left:calc(14px + env(safe-area-inset-left,0px));' +
    'bottom:calc(14px + env(safe-area-inset-bottom,0px));width:44px;height:44px;border-radius:50%;padding:0;' +
    'display:grid;place-items:center;cursor:pointer;color:var(--paper);background:var(--accent-dark,var(--accent));' +
    'border:1px solid color-mix(in srgb,var(--paper) 35%,transparent);' +
    'box-shadow:0 2px 10px color-mix(in srgb,var(--ink) 30%,transparent)}' +
    '.sea-sound:focus-visible{outline:3px solid var(--accent);outline-offset:3px}' +
    '.sea-sound svg{width:22px;height:22px}' +
    '.sea-sound[aria-pressed="false"] .ss-w{opacity:.4}' +
    '.sea-sound .ss-x{display:none}.sea-sound[aria-pressed="false"] .ss-x{display:inline}' +
    '@media print{.sea-sound{display:none!important}}';
  document.head.appendChild(css);

  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'sea-sound';
  btn.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" ' +
    'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><g class="ss-w">' +
    '<path d="M2.5 9.5c2.4-2.2 4.4-2.2 6.3 0s3.9 2.2 6.3 0 4.4-2.2 6.4 0"/>' +
    '<path d="M2.5 15c2.4-2.2 4.4-2.2 6.3 0s3.9 2.2 6.3 0 4.4-2.2 6.4 0"/></g>' +
    '<path class="ss-x" d="M3.5 3.5l17 17"/></svg>';
  document.body.appendChild(btn);

  var on = true;
  try { on = localStorage.getItem('sea-sound') !== 'off'; } catch (_) {}
  function label() {
    var lang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase().slice(0, 2);
    var L = T[lang] || T.en;
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.setAttribute('aria-label', on ? L[0] : L[1]);
    btn.title = on ? L[0] : L[1];
  }
  label();
  if (window.MutationObserver) new MutationObserver(label).observe(document.documentElement,
    { attributes: true, attributeFilter: ['lang'] });

  var ctx = null, master = null, bufs = {}, loading = null, started = false, blipped = false, timers = [];
  function ensureContext() {
    if (ctx) return;
    try { if (navigator.audioSession) navigator.audioSession.type = 'playback'; } catch (_) {}
    ctx = new AC();
    master = ctx.createGain(); master.gain.value = 0; master.connect(ctx.destination);
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
  function load(name) {
    return fetch(cfg.dir + name + '.m4a').then(function (r) { if (!r.ok) throw new Error(r.status); return r.arrayBuffer(); })
      .then(function (b) { return new Promise(function (ok, no) { ctx.decodeAudioData(b, ok, no); }); })
      .then(function (buf) { bufs[name] = buf; });
  }
  function rand(a, b) { return a + Math.random() * (b - a); }
  // one shot: through its own gain and pan, optionally faded in and out
  function play(name, opts) {
    var buf = bufs[name];
    if (!buf || !ctx) return;
    var src = ctx.createBufferSource(); src.buffer = buf;
    src.playbackRate.value = opts.rate || 1;
    var g = ctx.createGain(), t = ctx.currentTime;
    var node = g;
    if (ctx.createStereoPanner) { var p = ctx.createStereoPanner(); p.pan.value = opts.pan || 0; g.connect(p); node = p; }
    node.connect(master);
    src.connect(g);
    var dur = opts.dur || buf.duration / (opts.rate || 1);
    if (opts.fade) {
      g.gain.setValueAtTime(0, t);
      g.gain.linearRampToValueAtTime(opts.gain, t + opts.fade);
      g.gain.setValueAtTime(opts.gain, t + dur - opts.fade);
      g.gain.linearRampToValueAtTime(0, t + dur);
    } else g.gain.value = opts.gain;
    src.start(t, opts.offset || 0, opts.dur ? opts.dur : undefined);
  }
  // each occasional voice reschedules itself; nothing plays in a hidden tab
  function every(min, max, first, fn) {
    function tick() {
      if (on && !document.hidden && ctx && ctx.state === 'running') fn();
      timers.push(setTimeout(tick, rand(min, max) * 1000));
    }
    timers.push(setTimeout(tick, first * 1000));
  }
  function start() {
    ensureContext();
    if (loading) return loading;
    var names = ['sea', 'foghorn', 'accordion'];
    for (var i = 1; i <= cfg.gulls; i++) names.push('gull-' + i);
    // the sea first: it is what you hear at once
    loading = load('sea').then(function () {
      var src = ctx.createBufferSource();
      src.buffer = bufs.sea; src.loop = true;
      src.loopStart = cfg.loop[0]; src.loopEnd = cfg.loop[1];
      var g = ctx.createGain(); g.gain.value = 0.85;
      src.connect(g); g.connect(master);
      src.start(0, cfg.loop[0]);
      started = true;
      apply();
      return Promise.all(names.slice(1).map(load));
    }).then(function () {
      every(7, 22, rand(3, 8), function () {
        play('gull-' + (1 + Math.floor(Math.random() * cfg.gulls)),
             { gain: rand(0.25, 0.6), pan: rand(-0.85, 0.85), rate: rand(0.9, 1.1) });
      });
      every(80, 160, rand(30, 55), function () { play('foghorn', { gain: rand(0.35, 0.5), pan: rand(-0.5, 0.5) }); });
      every(70, 140, rand(45, 75), function () {
        var len = rand(16, 26), b = bufs.accordion;
        play('accordion', { gain: rand(0.1, 0.15), pan: rand(-0.6, 0.6), fade: 6, dur: len,
                            offset: rand(0, Math.max(0, b.duration - len - 1)) });
      });
    }).catch(function () { btn.hidden = true; });
    return loading;
  }
  function playing() { return !!(ctx && started && ctx.state === 'running'); }
  var last = -1;
  function apply() {
    if (!ctx || !master) return;
    var g = on ? LEVEL : 0;
    if (g !== last) { master.gain.setTargetAtTime(g, ctx.currentTime, g < last ? 0.1 : 0.8); last = g; }
    if (on && !document.hidden && ctx.state !== 'running') { var p = ctx.resume(); if (p && p.catch) p.catch(function () {}); }
  }
  setInterval(apply, 200);

  function gesture(e) {
    if (!on || document.hidden || (e && e.target && e.target.closest && e.target.closest('.sea-sound'))) return;
    unlock();
    start();
  }
  ['pointerdown', 'pointerup', 'touchend', 'click', 'keydown'].forEach(function (ev) {
    document.addEventListener(ev, gesture, { capture: true, passive: true });
  });

  btn.addEventListener('click', function () {
    if (on && !playing()) { unlock(); start(); apply(); return; }
    on = !on;
    try { localStorage.setItem('sea-sound', on ? 'on' : 'off'); } catch (_) {}
    label();
    if (on) { unlock(); start(); }
    apply();
    if (!on && ctx) setTimeout(function () { if (!on && ctx) ctx.suspend(); }, 700);
  });
  document.addEventListener('visibilitychange', function () {
    if (!ctx) return;
    var p = document.hidden ? ctx.suspend() : (on ? ctx.resume() : null);
    if (p && p.catch) p.catch(function () {});
  });
})();
