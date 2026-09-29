<script>
/* CLIP SUBTITLES. window.CLIP_SUBS maps a clip's path to its cues,
   [start, end, {en, de, es, ...}] in seconds. The CC menu picks the language
   (or off) and is remembered per viewer; it starts in English, the language
   being spoken. Captions follow whichever clip element is on screen. */
(function () {
  var SUBS = window.CLIP_SUBS || {};
  var stage = document.getElementById('stage');
  /* REPLAY. Once a clip has played on a slide, a button brings it back from
     the start, with sound: the click is the gesture that allows it. */
  var replay = document.createElement('button');
  replay.type = 'button'; replay.className = 'clip-replay';
  replay.innerHTML = '&#8635; Replay';
  replay.setAttribute('aria-label', 'Replay the animation');
  stage.appendChild(replay);
  replay.addEventListener('click', function () {
    var v = document.querySelector('.bg-clip.run');
    if (!v) return;
    v.currentTime = 0; v.muted = false;
    var p = v.play();
    if (p && p.catch) p.catch(function () { v.muted = true; v.play().catch(function () {}); });
  });
  (function watch() {
    replay.classList.toggle('show', !!document.querySelector('.bg-clip.run'));
    requestAnimationFrame(watch);
  })();
  if (!Object.keys(SUBS).length) return;
  var cap = document.createElement('div');
  cap.className = 'clip-cap'; cap.setAttribute('aria-hidden', 'true');
  stage.appendChild(cap);
  var NAMES = { off: 'CC off', en: 'CC English', de: 'CC Deutsch', es: 'CC Español',
    fr: 'CC Français', it: 'CC Italiano', pt: 'CC Português', ru: 'CC Русский',
    ar: 'CC العربية', zh: 'CC 中文', ja: 'CC 日本語' };
  var sel = document.createElement('select');
  sel.className = 'cc-select'; sel.id = 'ccSelect';
  sel.setAttribute('aria-label', 'Subtitles');
  Object.keys(NAMES).forEach(function (k) { sel.add(new Option(NAMES[k], k)); });
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
