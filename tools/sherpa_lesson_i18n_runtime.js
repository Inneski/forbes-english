/* Sherpa lesson translations (tools/sherpa_lesson_i18n.py injects this with the page's data).
   The camp one pattern, on every lesson page: a globe on each section translates that
   section into one of nine languages, each English line keeping its translation beneath it;
   the quiz's own words swap; example sentences stay English and show their translation
   under them from the "Examples in" bar. The English being taught is never touched. */
(function () {
  var holder = document.getElementById('sherpa-i18n-data');
  if (!holder) return;
  var D = JSON.parse(holder.textContent);
  var IDX = {};
  D.langs.forEach(function (l, i) { IDX[l] = i; });
  var NAMES = { en: 'EN &middot; English', de: 'DE &middot; Deutsch', es: 'ES &middot; Espa&ntilde;ol',
    fr: 'FR &middot; Fran&ccedil;ais', it: 'IT &middot; Italiano', pt: 'PT &middot; Portugu&ecirc;s',
    ru: 'RU &middot; &#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;', ar: 'AR &middot; &#1575;&#1604;&#1593;&#1585;&#1576;&#1610;&#1577;',
    zh: 'ZH &middot; &#20013;&#25991;', ja: 'JA &middot; &#26085;&#26412;&#35486;' };
  var INLINE = /^(EM|STRONG|B|I|SPAN|A|BR|CODE|SUP|SUB|SMALL|MARK|ABBR|U|S|Q)$/;
  var SKIP = 'script,style,noscript,svg,.sr-only,.ex-tr,.i18n-inline,.i18n-en,#tr-bar,.voice-bar,.up-link,' +
    '#q-prompt,#options,.lang-globe-wrap,.topo-sheen,.sherpa-sky';
  var EXAMPLE = '.ex, p.example, .use-ex, .ft-example, .example';
  function norm(s) { return s.replace(/\s+/g, ' ').trim(); }
  function tr(map, en, lang) { var row = map[norm(en)]; return row && row[IDX[lang]] || ''; }
  function ui(key, lang, vars) {
    var s = tr(D.ui, key, lang) || key;
    for (var k in vars) s = s.split('{' + k + '}').join(vars[k]);
    return s;
  }

  /* a "block": an element holding text of its own, whose children are all inline */
  function blocks(root) {
    var out = [];
    root.querySelectorAll('*').forEach(function (el) {
      if (el.closest(SKIP) || INLINE.test(el.tagName)) return;
      var kids = el.childNodes, text = false, block = false;
      for (var i = 0; i < kids.length; i++) {
        if (kids[i].nodeType === 3 && kids[i].textContent.trim()) text = true;
        if (kids[i].nodeType === 1 && !INLINE.test(kids[i].tagName)) block = true;
      }
      if (block) return;
      if (!text && !norm(el.textContent)) return;
      out.push(el);
    });
    return out;
  }

  /* the English line and the translation line beneath it */
  function english(el) {
    var en = el.querySelector(':scope > .i18n-en');
    return en ? en.innerHTML : el.innerHTML;
  }
  function inline(el, text, lang) {
    var en = el.querySelector(':scope > .i18n-en');
    var old = el.querySelector(':scope > .i18n-inline');
    if (old) old.remove();
    if (!text) {
      if (en) { el.innerHTML = en.innerHTML; }
      return;
    }
    if (!en) {
      en = document.createElement('span');
      en.className = 'i18n-en';
      en.innerHTML = el.innerHTML;
      el.innerHTML = '';
      el.appendChild(en);
    }
    var sub = document.createElement('span');
    sub.className = 'i18n-inline';
    sub.setAttribute('lang', lang);
    if (lang === 'ar') sub.setAttribute('dir', 'rtl');
    sub.innerHTML = text;
    el.appendChild(sub);
  }

  /* a translated diagram label that would run out of its diagram is set smaller, from its
     anchor, until it fits (down to 60%): German's "eine Gewohnheit oder ein Zustand,
     vorbei und erledigt" ran off the used-to diagram. One proportional step is not enough:
     a diagram scaled to a phone is drawn at 6px on screen, where Chrome snaps each glyph to
     whole pixels, so the width barely moves between 11.5 and 10.75. Measure after every
     step; whatever still overflows at 60% is held to its room with textLength. */
  function fit(t) {
    if (t._fs0 === undefined) t._fs0 = t.style.fontSize;
    t.style.fontSize = t._fs0;
    if (t._fitLen) { t.removeAttribute('textLength'); t.removeAttribute('lengthAdjust'); t._fitLen = false; }
    var svg = t.ownerSVGElement, vb = svg && svg.viewBox && svg.viewBox.baseVal;
    if (!vb || !vb.width) return;
    var b = t.getBBox(), anchor = t.getAttribute('text-anchor') || 'start';
    var x = parseFloat(t.getAttribute('x')) || b.x, left = vb.x + 2, right = vb.x + vb.width - 2;
    var room = anchor === 'middle' ? 2 * Math.min(x - left, right - x) : anchor === 'end' ? x - left : right - x;
    if (b.width <= room || room <= 0) return;
    var fs = parseFloat(getComputedStyle(t).fontSize), floor = fs * 0.6, s = fs, w = b.width;
    for (var i = 0; i < 12 && w > room && s > floor; i++) {
      s = Math.max(floor, Math.min(s * room / w, s * 0.97));
      t.style.fontSize = s + 'px';
      w = t.getBBox().width;
    }
    if (w > room) { t.setAttribute('textLength', room); t.setAttribute('lengthAdjust', 'spacingAndGlyphs'); t._fitLen = true; }
  }

  /* sections: every camp, and the hero */
  var sections = [];
  var hero = document.querySelector('section.hero, .hero');
  if (hero) sections.push({ id: 'hero', el: hero });
  document.querySelectorAll('.camp').forEach(function (c, i) { sections.push({ id: c.id || 'camp-' + i, el: c }); });
  var lang = {};
  sections.forEach(function (s) { lang[s.id] = 'en'; });
  var OBSERVE = { childList: true, subtree: true, characterData: true };

  function refresh(s) {
    /* our own edits must not wake the watcher that calls us: disconnect while writing */
    if (s.obs) s.obs.disconnect();
    var l = lang[s.id], on = l !== 'en';
    blocks(s.el).forEach(function (el) {
      if (el.id === 'progress-text' || el.id === 'score-text' || el.id === 'next-btn' || el.id === 'retry-btn' || el.id === 'final-score') return;
      if (el.closest(EXAMPLE)) return;              /* examples are the "Examples in" bar's */
      inline(el, on ? tr(D.t, english(el), l) : '', l);
    });
    s.el.querySelectorAll('svg text').forEach(function (t) {
      if (!t.hasAttribute('data-en')) t.setAttribute('data-en', t.textContent);
      var en = t.getAttribute('data-en');
      var x = on ? tr(D.s, en, l) : '';
      if (t.querySelector('tspan')) return;                 /* multi-line labels keep their English */
      t.textContent = x || en;
      fit(t);
    });
    /* fit measures in whatever font is there now: refit once the web fonts are in, or a
       label measured in the narrower fallback runs out of its diagram in Faktum */
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () {
      s.el.querySelectorAll('svg text[data-en]').forEach(fit);
    });
    /* the quiz's own words */
    var p = s.el.querySelector('#progress-text'), sc = s.el.querySelector('#score-text');
    var nb = s.el.querySelector('#next-btn'), rb = s.el.querySelector('#retry-btn');
    if (p) {                                     /* "Checkpoint 3 of 14", in either language */
      var m = p.textContent.match(/(\d+)\D+(\d+)/);
      if (m) p.textContent = on ? ui('Checkpoint {n} of {m}', l, { n: m[1], m: m[2] }) : 'Checkpoint ' + m[1] + ' of ' + m[2];
    }
    if (sc) {
      var n = sc.textContent.match(/(\d+)/);
      if (n) sc.textContent = on ? ui('Score: {n}', l, { n: n[1] }) : 'Score: ' + n[1];
    }
    [nb, rb].forEach(function (b) {              /* the page writes these in English; remember what it wrote */
      if (!b) return;
      var cur = b.textContent;
      if (D.ui[norm(cur)] || !b.hasAttribute('data-en')) b.setAttribute('data-en', cur);
      var e = b.getAttribute('data-en');
      b.textContent = on ? ui(e, l, {}) : e;
    });
    if (s.obs) s.obs.observe(s.el, OBSERVE);
  }

  /* the quiz and the results rewrite their text as the learner goes: translate again */
  sections.forEach(function (s) {
    if (!s.el.querySelector('#quiz, #results, #q-hint, #feedback, #final-message')) return;
    s.obs = new MutationObserver(function () {
      if (lang[s.id] !== 'en') refresh(s);
    });
    s.obs.observe(s.el, OBSERVE);
  });

  /* a globe under each section's heading, as on camp one */
  function closeAll(except) {
    document.querySelectorAll('.lang-menu').forEach(function (m) { if (m !== except) m.hidden = true; });
    document.querySelectorAll('.lang-globe-btn').forEach(function (b) {
      if (!except || b.nextElementSibling !== except) b.setAttribute('aria-expanded', 'false');
    });
  }
  sections.forEach(function (s) {
    if (s.el.querySelector(':scope > .lang-globe-wrap, :scope .lang-globe-wrap[data-globe-section="' + s.id + '"]')) return;
    var wrap = document.createElement('div');
    wrap.className = 'lang-globe-wrap';
    wrap.setAttribute('data-globe-section', s.id);
    wrap.innerHTML = '<button type="button" class="lang-globe-btn" aria-haspopup="true" aria-expanded="false" ' +
      'aria-label="Translate this section">&#127760;</button><div class="lang-menu" hidden></div>';
    var anchor = s.id === 'hero' ? s.el.querySelector('h1 ~ p, p') : s.el.querySelector(':scope > h2');
    if (anchor) anchor.insertAdjacentElement('afterend', wrap); else s.el.insertBefore(wrap, s.el.firstChild);
    var btn = wrap.querySelector('button'), menu = wrap.querySelector('.lang-menu');
    ['en'].concat(D.langs).forEach(function (code) {
      var o = document.createElement('button');
      o.type = 'button';
      o.className = 'lang-opt' + (code === 'en' ? ' selected' : '');
      o.innerHTML = NAMES[code];
      o.addEventListener('click', function (e) {
        e.stopPropagation();
        lang[s.id] = code;
        menu.querySelectorAll('.lang-opt').forEach(function (x) { x.classList.remove('selected'); });
        o.classList.add('selected');
        btn.classList.toggle('active', code !== 'en');
        btn.setAttribute('aria-label', code === 'en' ? 'Translate this section' : ui('Translate this section', code, {}));
        refresh(s);
        menu.hidden = true;
        btn.setAttribute('aria-expanded', 'false');
      });
      menu.appendChild(o);
    });
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = menu.hidden;
      closeAll();
      menu.hidden = !open;
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function () { closeAll(); });

  /* examples: every model sentence without a translation of its own gets one from the bar */
  var bar = document.getElementById('tr-bar');
  if (!bar) {
    bar = document.createElement('div');
    bar.className = 'tr-bar';
    bar.id = 'tr-bar';
    bar.innerHTML = '<span class="tr-label">Examples in</span><button type="button" data-lang="" class="on">Off</button>' +
      D.langs.map(function (l) { return '<button type="button" data-lang="' + l + '">' + l.toUpperCase() + '</button>'; }).join('');
    var trail = document.querySelector('.trail-wrap') || document.querySelector('.camp');
    if (trail) trail.parentNode.insertBefore(bar, trail);
    bar.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      bar.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
    });
  }
  function examples(l) {
    blocks(document.body).forEach(function (el) {
      if (el.closest('.ex[data-tr]')) return;                 /* the page's own translations */
      var row = D.x[norm(english(el))];
      if (!row) return;
      var old = el.querySelector(':scope > .ex-tr');
      if (old) old.remove();
      if (!l) return;
      var line = document.createElement('span');
      line.className = 'ex-tr';
      line.setAttribute('lang', l);
      if (l === 'ar') line.setAttribute('dir', 'rtl');
      line.textContent = row[IDX[l]] || '';
      if (line.textContent) el.appendChild(line);
    });
  }
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-lang]');
    if (b) setTimeout(function () { examples(b.getAttribute('data-lang')); }, 0);
  });

  window.sherpaLessonI18n = {
    sections: sections.map(function (s) { return s.id; }),
    set: function (id, code) {
      var s = sections.filter(function (x) { return x.id === id; })[0];
      if (s) { lang[id] = code; refresh(s); }
    },
    examples: examples
  };
})();
