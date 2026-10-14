/* CAMP RULES — the info pages come out of the slide run.
   Innes, 2026-10-14: "the static info pages as a separate option to open and
   we will go straight into an animated opener". So the deck runs cover ->
   first question, and the teach slides wait behind a Rules button on the
   cover and in the deck bar, paged in an overlay that returns the learner to
   exactly where they were.

   Load it WITHOUT defer, after the stage markup and BEFORE the deck's inline
   script: the engine takes its slide list once, from
   document.querySelectorAll('.slide'), so the teach slides must already be
   parked (class 'rule-slide', in #campRules, outside the stage) by then.
   They stay in the document, so applyLang() and the gloss wiring still reach
   them. Showing one puts it back in the stage as a .slide for as long as it
   is open; the engine never learns it exists.

   The opener itself is the engine's own cover clip (data-clip +
   data-clip-auto on the cover). Until the file exists the request fails and
   the still stays, which is the page as it was. */
(function () {
  var stage = document.getElementById('stage');
  if (!stage) return;
  var rules = [].slice.call(stage.querySelectorAll('.slide[data-type="teach"]'));
  if (!rules.length) return;

  var park = document.createElement('div');
  park.id = 'campRules'; park.hidden = true;
  document.body.appendChild(park);
  rules.forEach(function (s) {
    s.classList.remove('slide', 'is-active');
    s.classList.add('rule-slide');
    park.appendChild(s);
  });

  var WORD = {
    en: ['Rules', 'Back to the questions'], es: ['Reglas', 'Volver a las preguntas'],
    de: ['Regeln', 'Zurück zu den Fragen'], fr: ['Règles', 'Retour aux questions'],
    it: ['Regole', 'Torna alle domande'], pt: ['Regras', 'Voltar às perguntas'],
    ru: ['Правила', 'Назад к вопросам'], ar: ['القواعد', 'العودة إلى الأسئلة'],
    zh: ['规则', '返回题目'], ja: ['ルール', '問題に戻る']
  };
  function w(i) {
    var l = (document.documentElement.lang || 'en').slice(0, 2);
    return (WORD[l] || WORD.en)[i];
  }

  var css = document.createElement('style');
  css.textContent =
    '.cr-open{margin-left:10px}' +
    '.cr-hud{font:600 11.5px/1 var(--font-mono,monospace);letter-spacing:.12em;' +
      'text-transform:uppercase;padding:9px 12px;border-radius:6px;cursor:pointer;' +
      'color:var(--accent-bright,var(--text));background:var(--scrim);border:1px solid var(--hairline)}' +
    '.stage.rules-open .cr-hud{background:var(--accent);color:var(--on-accent,#fff)}' +
    '.cr-bar{position:absolute;top:14px;left:50%;transform:translateX(-50%);z-index:60;' +
      'display:none;align-items:center;gap:10px;padding:6px 8px;border-radius:999px;' +
      'background:var(--scrim);border:1px solid var(--hairline);color:var(--text);' +
      'font:600 13px/1 var(--font-mono,monospace);letter-spacing:.06em}' +
    '.stage.rules-open .cr-bar{display:flex}' +
    '.cr-bar button{font:inherit;color:inherit;background:none;border:1px solid var(--hairline);' +
      'border-radius:999px;padding:7px 12px;cursor:pointer}' +
    '.cr-bar,.cr-bar *{white-space:nowrap}' +
    '@media (max-width:700px){.cr-bar{top:10px;gap:6px}.cr-bar .cr-word{display:none}}' +
    '.cr-bar button:disabled{opacity:.35;cursor:default}' +
    '.cr-bar .cr-close{background:var(--accent);border-color:var(--accent);color:var(--on-accent,#fff)}' +
    '.stage.on-cover .bg-clip.run{opacity:1}';
  document.head.appendChild(css);

  var bar = document.createElement('div');
  bar.className = 'cr-bar';
  bar.innerHTML = '<button type="button" class="cr-prev" aria-label="Previous">‹</button>' +
    '<span class="cr-count"></span>' +
    '<button type="button" class="cr-next" aria-label="Next">›</button>' +
    '<button type="button" class="cr-close"></button>';
  stage.appendChild(bar);

  var begin = stage.querySelector('.slide[data-type="cover"] [data-action="next"]');
  var coverBtn = null;
  if (begin) {
    coverBtn = document.createElement('button');
    coverBtn.type = 'button';
    coverBtn.className = 'btn btn-lg cr-open';
    begin.parentNode.insertBefore(coverBtn, begin.nextSibling);
  }
  var hudBtn = document.createElement('button');
  hudBtn.type = 'button';
  hudBtn.className = 'part-link cr-hud';   // .part-link: camp-phone.js moves it into the phone menu
  var prevNav = stage.querySelector('.deck-bar [data-action="prev"]');
  if (prevNav) prevNav.parentNode.insertBefore(hudBtn, prevNav);

  var at = -1, back = null, backHero = '', backCover = false;
  function label() {
    if (coverBtn) coverBtn.textContent = w(0);
    hudBtn.textContent = w(0);
    bar.querySelector('.cr-close').innerHTML = '✕<span class="cr-word"> ' + w(1) + '</span>';
    if (at >= 0) bar.querySelector('.cr-count').textContent =
      w(0) + ' ' + (at + 1) + ' / ' + rules.length;
  }
  label();
  if (window.MutationObserver) new MutationObserver(label)
    .observe(document.documentElement, { attributes: true, attributeFilter: ['lang'] });

  function put(i) {
    if (at >= 0) {
      var old = rules[at];
      old.classList.remove('slide', 'is-active');
      park.appendChild(old);
    }
    at = i;
    var s = rules[at];
    s.classList.add('slide', 'is-active');
    stage.insertBefore(s, bar);
    stage.style.setProperty('--hero', s.dataset.bg ? "url('" + s.dataset.bg + "')" : '');
    bar.querySelector('.cr-prev').disabled = at === 0;
    bar.querySelector('.cr-next').disabled = at === rules.length - 1;
    label();
  }
  function open() {
    if (at >= 0) return;
    back = stage.querySelector('.slide.is-active');
    backHero = stage.style.getPropertyValue('--hero');
    backCover = stage.classList.contains('on-cover');
    if (back) back.classList.remove('is-active');
    [].forEach.call(stage.querySelectorAll('.bg-clip'), function (v) { v.pause(); });
    var layer = stage.querySelector('.bg-layer');
    if (layer) layer.classList.remove('clip-on');
    stage.classList.remove('on-cover');
    stage.classList.add('rules-open');
    put(0);
  }
  function close() {
    if (at < 0) return;
    var s = rules[at];
    s.classList.remove('slide', 'is-active');
    park.appendChild(s);
    at = -1;
    stage.classList.remove('rules-open');
    stage.classList.toggle('on-cover', backCover);
    stage.style.setProperty('--hero', backHero);
    if (back) back.classList.add('is-active');
  }

  if (coverBtn) coverBtn.addEventListener('click', open);
  hudBtn.addEventListener('click', function () { at >= 0 ? close() : open(); });
  bar.querySelector('.cr-prev').addEventListener('click', function () { if (at > 0) put(at - 1); });
  bar.querySelector('.cr-next').addEventListener('click', function () { if (at < rules.length - 1) put(at + 1); });
  bar.querySelector('.cr-close').addEventListener('click', close);

  // While the rules are open the deck must not move under them: the arrow
  // keys and the deck bar's own ‹ › page the rules instead.
  document.addEventListener('click', function (e) {
    if (at < 0) return;
    var nav = e.target.closest('.deck-bar [data-action="prev"], .deck-bar [data-action="next"]');
    if (!nav) return;
    e.preventDefault(); e.stopImmediatePropagation();
    var d = nav.dataset.action === 'next' ? 1 : -1;
    var j = at + d;
    if (j >= 0 && j < rules.length) put(j);
  }, true);
  document.addEventListener('keydown', function (e) {
    if (at < 0) return;
    if (e.key === 'Escape') { close(); }
    else if (['ArrowRight', 'PageDown', ' '].indexOf(e.key) >= 0) { if (at < rules.length - 1) put(at + 1); }
    else if (['ArrowLeft', 'PageUp'].indexOf(e.key) >= 0) { if (at > 0) put(at - 1); }
    else return;
    e.preventDefault(); e.stopImmediatePropagation();
  }, true);
})();
