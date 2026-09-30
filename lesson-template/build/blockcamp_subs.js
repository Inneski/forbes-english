<script>
/* CLIP SUBTITLES. window.CLIP_SUBS maps a clip's path to its cues,
   [start, end, {en, de, es, ...}] in seconds. The CC menu picks the language
   (or off) and is remembered per viewer; it starts in English, the language
   being spoken. Captions follow whichever clip element is on screen. */
(function () {
  var SUBS = window.CLIP_SUBS || {};
  var stage = document.getElementById('stage');
  /* REPLAY. Once a clip has played on a slide, a button brings it back from
     the start, with sound: the click is the gesture that allows it. It stays
     on that slide after leaving and coming back (Innes, 2026-09-30: "some of
     them dont have replay buttons" - leaving a slide rewinds its clip, and
     the button used to follow the running clip, not the slide). */
  var replay = document.createElement('button');
  replay.type = 'button'; replay.className = 'clip-replay';
  replay.innerHTML = '&#8635; Replay';
  replay.setAttribute('aria-label', 'Replay the animation');
  stage.appendChild(replay);
  var played = new WeakSet();
  function onSlide() { try { return slides[idx]; } catch (_) { return null; } }
  [].forEach.call(document.querySelectorAll('.bg-clip'), function (v) {
    v.addEventListener('playing', function () { var s = onSlide(); if (s) played.add(s); });
  });
  replay.addEventListener('click', function () {
    var v = document.querySelector('.bg-clip.run');
    if (!v) { var s = onSlide(); if (s && typeof clipPlay === 'function') clipPlay(s); return; }
    v.currentTime = 0; v.muted = false;
    var p = v.play();
    if (p && p.catch) p.catch(function () { v.muted = true; v.play().catch(function () {}); });
  });
  (function watch() {
    var s = onSlide();
    replay.classList.toggle('show', !!document.querySelector('.bg-clip.run') ||
      !!(s && s.dataset && s.dataset.clip && played.has(s)));
    requestAnimationFrame(watch);
  })();
  if (!Object.keys(SUBS).length) return;
  var cap = document.createElement('div');
  cap.className = 'clip-cap'; cap.setAttribute('aria-hidden', 'true');
  stage.appendChild(cap);
  // Short codes: the deck bar is full. The full name is each option's title.
  var NAMES = { off: 'CC off', en: 'CC EN', de: 'CC DE', es: 'CC ES', fr: 'CC FR', it: 'CC IT',
    pt: 'CC PT', ru: 'CC RU', ar: 'CC AR', zh: 'CC ZH', ja: 'CC JA' };
  var FULL = { off: 'Subtitles off', en: 'English', de: 'Deutsch', es: 'Español', fr: 'Français',
    it: 'Italiano', pt: 'Português', ru: 'Русский', ar: 'العربية', zh: '中文', ja: '日本語' };
  var sel = document.createElement('select');
  sel.className = 'cc-select'; sel.id = 'ccSelect';
  sel.setAttribute('aria-label', 'Subtitles');
  Object.keys(NAMES).forEach(function (k) { var o = new Option(NAMES[k], k); o.title = FULL[k]; sel.add(o); });
  sel.title = 'Subtitles';
  var lang = 'en';
  try { lang = localStorage.getItem('bc-cc') || 'en'; } catch (_) {}
  if (!NAMES[lang]) lang = 'en';
  sel.value = lang;
  var anchor = document.getElementById('langSelect');
  anchor.parentNode.insertBefore(sel, anchor.nextSibling);
  sel.addEventListener('change', function () {
    lang = sel.value;
    try { localStorage.setItem('bc-cc', lang); } catch (_) {}
    shown = null; render();
  });
  var shown = null;
  function current() {
    var vs = document.querySelectorAll('.bg-clip');
    for (var i = 0; i < vs.length; i++) {
      var v = vs[i];
      if (v.classList.contains('run') && (!v.paused || v.ended)) return v;
    }
    return null;
  }
  function tick() { render(); requestAnimationFrame(tick); }
  function render() {
    var v = lang === 'off' ? null : current(), line = '';
    if (v) {
      var cues = SUBS[v.getAttribute('src')] || [], t = v.currentTime;
      for (var i = 0; i < cues.length; i++) {
        if (t >= cues[i][0] && t < cues[i][1]) { line = cues[i][2][lang] || cues[i][2].en || ''; break; }
      }
    }
    if (line !== shown) {
      shown = line;
      cap.textContent = line;
      cap.dir = lang === 'ar' ? 'rtl' : 'ltr';
      cap.lang = lang;
      cap.classList.toggle('show', !!line);
    }
  }
  requestAnimationFrame(tick);
})();
</script>
