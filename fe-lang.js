/* The language menu in the top row, on every page (Innes, 2026-10-19:
   "standard on every page same"). Generated from the front page's own
   dictionary by the scratch tool that wrote it; edit here and keep the
   front page (index.html, I18N) in step.

   What it does:
   - puts the front page's ENGLISH menu in the row, just before Go Pro, in
     the ink of the row's own links (dark, cream or white, page by page);
   - translates the row's links, as the front page does;
   - translates the page's own words wherever a page carries them: any
     element with data-fe="key", from <script type="application/json"
     id="fe-page-i18n">{"de": {"key": "…"}, …}</script>. An element's
     English is what it holds on first sight. A child with an id (a live
     count, say) is kept across the swap, and {n} / {m} are filled from
     data-n / data-m;
   - remembers the choice in localStorage 'fe-lang', the front page's key,
     and takes ?lang=xx;
   - keeps the row on one line: the least-used links step out, in the
     front page's order, until the row fits.
   A page with its own menu in the row (Block Camp, #hubLang) keeps it;
   this script leaves that page alone.
   window.FE_LANG = { lang(), t(key, english), apply(el?) }, and a
   'fe-lang' event on document after every change. */
(function () {
  'use strict';
  var LANGS = [['en', 'English'], ['de', 'Deutsch'], ['es', 'Español'], ['fr', 'Français'], ['it', 'Italiano'],
               ['pt', 'Português'], ['ru', 'Русский'], ['ar', 'العربية'], ['zh', '中文'], ['ja', '日本語']];
  var NAV = {"de": {"level-checker.html": "Einstufung", "library.html": "Bibliothek", "ielts.html": "IELTS", "grammar.html": "Grammatik", "rpg.html": "Rollenspiele", "block-camp.html": "Block Camp", "library.html#cat=Slide+Decks": "Foliensätze", "mailto:info@forbesenglish.com": "Mit mir arbeiten", "account.html": "Anmelden", "pricing.html": "Pro werden"}, "es": {"level-checker.html": "Prueba de nivel", "library.html": "Biblioteca", "ielts.html": "IELTS", "grammar.html": "Gramática", "rpg.html": "Juegos de rol", "block-camp.html": "Block Camp", "library.html#cat=Slide+Decks": "Presentaciones", "mailto:info@forbesenglish.com": "Trabaja conmigo", "account.html": "Iniciar sesión", "pricing.html": "Hazte Pro"}, "fr": {"level-checker.html": "Test de niveau", "library.html": "Bibliothèque", "ielts.html": "IELTS", "grammar.html": "Grammaire", "rpg.html": "Jeux de rôle", "block-camp.html": "Block Camp", "library.html#cat=Slide+Decks": "Diaporamas", "mailto:info@forbesenglish.com": "Travailler avec moi", "account.html": "Connexion", "pricing.html": "Passer Pro"}, "it": {"level-checker.html": "Test di livello", "library.html": "Biblioteca", "ielts.html": "IELTS", "grammar.html": "Grammatica", "rpg.html": "Giochi di ruolo", "block-camp.html": "Block Camp", "library.html#cat=Slide+Decks": "Presentazioni", "mailto:info@forbesenglish.com": "Lavora con me", "account.html": "Accedi", "pricing.html": "Passa a Pro"}, "pt": {"level-checker.html": "Teste de nível", "library.html": "Biblioteca", "ielts.html": "IELTS", "grammar.html": "Gramática", "rpg.html": "RPGs", "block-camp.html": "Block Camp", "library.html#cat=Slide+Decks": "Apresentações", "mailto:info@forbesenglish.com": "Trabalhe comigo", "account.html": "Entrar", "pricing.html": "Seja Pro"}, "ru": {"level-checker.html": "Тест уровня", "library.html": "Библиотека", "ielts.html": "IELTS", "grammar.html": "Грамматика", "rpg.html": "Ролевые игры", "block-camp.html": "Block Camp", "library.html#cat=Slide+Decks": "Презентации", "mailto:info@forbesenglish.com": "Работать со мной", "account.html": "Войти", "pricing.html": "Стать Pro"}, "ar": {"level-checker.html": "اختبار المستوى", "library.html": "المكتبة", "ielts.html": "IELTS", "grammar.html": "القواعد", "rpg.html": "ألعاب الأدوار", "block-camp.html": "Block Camp", "library.html#cat=Slide+Decks": "العروض التقديمية", "mailto:info@forbesenglish.com": "اعمل معي", "account.html": "تسجيل الدخول", "pricing.html": "اشترك في Pro"}, "zh": {"level-checker.html": "水平测试", "library.html": "课程库", "ielts.html": "IELTS", "grammar.html": "语法", "rpg.html": "角色扮演", "block-camp.html": "Block Camp", "library.html#cat=Slide+Decks": "幻灯片课件", "mailto:info@forbesenglish.com": "与我合作", "account.html": "登录", "pricing.html": "升级 Pro"}, "ja": {"level-checker.html": "レベルチェック", "library.html": "ライブラリー", "ielts.html": "IELTS", "grammar.html": "文法", "rpg.html": "RPG", "block-camp.html": "Block Camp", "library.html#cat=Slide+Decks": "スライド教材", "mailto:info@forbesenglish.com": "個別レッスン", "account.html": "ログイン", "pricing.html": "Proに登録"}};
  var KEY = 'fe-lang';
  var SQUEEZE = ['library.html#cat=Slide+Decks', 'mailto:info@forbesenglish.com', 'rpg.html', 'account.html',
                 'level-checker.html', 'block-camp.html', 'grammar.html'];
  var row = document.querySelector('.topband .tb-links, header .nav-links, .fe-row');
  if (!row || document.getElementById('hubLang') || document.getElementById('lang')) return;

  var PAGE = {};
  try { var j = document.getElementById('fe-page-i18n'); if (j) PAGE = JSON.parse(j.textContent); } catch (e) {}
  var cur = 'en';
  function ok(l) { return l === 'en' || !!NAV[l]; }
  function href(a) { return (a.getAttribute('href') || '').replace(/^(\.\.\/)+/, '').replace(/^\//, ''); }
  var links = [].slice.call(row.querySelectorAll('a'));
  var pro = row.querySelector('.tb-cta-gold, .nav-pill.gold, .fe-go') || links[links.length - 1];
  var plain = links.filter(function (a) { return a !== pro && a.offsetParent; })[0] || links[0];

  // the menu: the front page's, in this row's ink
  var css = document.createElement('style');
  css.textContent =
    '.fe-lang { position: relative; display: inline-flex; align-items: center; gap: 4px; flex: none; margin: 0;' +
    ' font: 600 12px/1 "Barlow Condensed", sans-serif; letter-spacing: 0.06em; text-transform: uppercase; white-space: nowrap;' +
    ' border: 1px solid currentColor; border-radius: 999px; padding: 5px 8px 5px 10px; cursor: pointer; opacity: 0.9; }' +
    '.fe-lang:hover, .fe-lang:focus-within { opacity: 1; }' +
    '.fe-lang:has(select:focus-visible) { outline: 2px solid currentColor; outline-offset: 2px; }' +
    '.fe-lang svg { width: 1em; height: 1em; fill: none; stroke: currentColor; stroke-width: 2.4; }' +
    '.fe-lang select { position: absolute; inset: 0; width: 100%; height: 100%; margin: 0; padding: 0; border: 0;' +
    ' opacity: 0; cursor: pointer; font-size: 16px; -webkit-appearance: none; appearance: none; }' +   /* 16px: iOS zooms to smaller */
    '.fe-lang option { color: #111; background: #fff; }' +
    '@media (min-width: 1101px) { .fe-lang { font-size: clamp(13px, 1vw, 15px); padding: 7px 10px 7px 12px; } }';
  document.head.appendChild(css);
  // the menu shows the language's own name, or its code where the row is
  // tight; the list itself always gives the names
  var box = document.createElement('label');
  box.className = 'fe-lang';
  box.title = 'Language';
  var cap = document.createElement('span');
  box.appendChild(cap);
  box.insertAdjacentHTML('beforeend', '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>');
  var sel = document.createElement('select');
  sel.setAttribute('aria-label', 'Language');
  box.appendChild(sel);
  var NAMES = {}, short = false;
  LANGS.forEach(function (p) { NAMES[p[0]] = p[1]; });
  function caption() { cap.textContent = short ? cur.toUpperCase() : NAMES[cur]; }
  LANGS.forEach(function (p) {
    var o = document.createElement('option');
    o.value = p[0]; o.lang = p[0]; o.textContent = p[1];
    if (p[0] === 'ar') o.dir = 'rtl';
    sel.appendChild(o);
  });
  row.insertBefore(box, pro);
  function ink() {
    var s = getComputedStyle(plain);
    box.style.color = s.color;
    box.style.textShadow = s.textShadow;
  }

  var english = links.map(function (a) { return a.innerHTML; });
  function t(key, en) { var T = PAGE[cur]; return (T && T[key] != null) ? T[key] : en; }
  function fill(el, html) {
    return html.split('{n}').join(el.getAttribute('data-n') || '').split('{m}').join(el.getAttribute('data-m') || '');
  }
  function one(el) {
    if (el._feEn == null) el._feEn = el.innerHTML;
    var key = el.getAttribute('data-fe'), T = PAGE[cur];
    var html = fill(el, (T && T[key] != null) ? T[key] : el._feEn);
    if (el.innerHTML !== html) {
      var keep = [].slice.call(el.querySelectorAll('[id]'));
      el.innerHTML = html;
      keep.forEach(function (n) { var m = el.querySelector('#' + n.id); if (m) m.replaceWith(n); });
    }
    if (T && T[key] != null) el.lang = cur; else el.removeAttribute('lang');
    // Arabic reads right to left, piece by piece; the page around it stays as it is
    var rtl = cur === 'ar' && T && T[key] != null;
    if (rtl) { el.dir = 'rtl'; el._feRtl = true; } else if (el._feRtl) { el.removeAttribute('dir'); el._feRtl = false; }
    // a buy button remembers its label to put back after a checkout attempt
    if (el.dataset && 'label' in el.dataset && !el.disabled) el.dataset.label = el.textContent;
  }
  function apply(el) {
    if (el) { one(el); return; }
    links.forEach(function (a, i) {
      var w = cur !== 'en' && NAV[cur][href(a)];
      a.innerHTML = w || english[i];
      if (w) a.lang = cur; else a.removeAttribute('lang');
    });
    [].forEach.call(document.querySelectorAll('[data-fe]'), one);
    sel.value = cur;
    caption();
    fit();
    try { document.dispatchEvent(new CustomEvent('fe-lang', { detail: cur })); } catch (e) {}
  }
  function set(l, remember) {
    cur = ok(l) ? l : 'en';
    if (remember) { try { localStorage.setItem(KEY, cur); } catch (e) {} }
    apply();
  }

  // the row stays on one line, in every language
  var logo = row.parentNode.querySelector('svg, img');
  var STEPS = SQUEEZE.concat(['short', 'library.html']);
  function fit() {
    links.forEach(function (a) { if (a.hasAttribute('data-fe-out')) { a.style.removeProperty('display'); a.removeAttribute('data-fe-out'); } });
    short = false; caption();
    ink();
    var limit = document.documentElement.clientWidth - 8;
    for (var i = 0; i < STEPS.length; i++) {
      var shown = [].slice.call(row.children).filter(function (x) { return x.offsetParent; });
      if (!shown.length) break;
      var right = Math.max.apply(null, shown.map(function (x) { return x.getBoundingClientRect().right; }));
      var left = Math.min.apply(null, shown.map(function (x) { return x.getBoundingClientRect().left; }));
      // the logo only counts when the row shares its line (some pages drop the row below it on a phone)
      var lr = logo && logo.getBoundingClientRect(), r0 = shown[0].getBoundingClientRect();
      var lim = lr && r0.top < lr.bottom && r0.bottom > lr.top ? lr.right + 12 : 0;
      var crowded = false;
      for (var k = 1; k < shown.length; k++) if (shown[k].getBoundingClientRect().left < shown[k - 1].getBoundingClientRect().right - 0.5) crowded = true;
      if (right <= limit && left >= lim && !crowded) break;
      if (STEPS[i] === 'short') { short = true; caption(); continue; }
      var a = links.filter(function (x) { return href(x) === STEPS[i] && x.offsetParent; })[0];
      if (a) { a.style.display = 'none'; a.setAttribute('data-fe-out', ''); }
    }
  }

  window.FE_LANG = { lang: function () { return cur; }, t: t, apply: apply };
  sel.addEventListener('change', function () { set(sel.value, true); });
  addEventListener('resize', fit);
  addEventListener('storage', function (e) { if (e.key === KEY && ok(e.newValue) && e.newValue !== cur) set(e.newValue, false); });
  addEventListener('pageshow', function (e) {
    if (!e.persisted) return;
    var s; try { s = localStorage.getItem(KEY); } catch (x) {}
    if (ok(s) && s !== cur) set(s, false);
  });
  var want = (location.search.match(/[?&]lang=([a-z]{2})\b/) || [])[1];
  if (ok(want)) { set(want, true); return; }
  try { want = localStorage.getItem(KEY); } catch (e) {}
  set(ok(want) ? want : 'en', false);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
})();
