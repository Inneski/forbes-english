/* Block Camp: the way back to the map, and the way on to the next camp.

   GENERATED. The source is lesson-template/build/block-camp-nav/template.js,
   and the route below comes from build.py beside it. Edit those, then run

       py lesson-template/build/block-camp-nav/build.py

   Anything edited in block-camp/camp-nav.js itself is overwritten.

   Innes, 2026-09-27: "we need a navigational button on each level back to the
   main camp at all times and to the next camp once you finish each camp".
   Until then the only way out of a camp was the Part 1 / Part 2 chip or the
   browser's back button. A learner who finished Present Simple had to know
   where the map was to find Present Continuous.

   TWO BUTTONS, BOTH IN THE DECK BAR, because that is the one strip that is on
   every slide, never over the artwork, and already under the learner's hand:

     - the route map, first in the bar, on every slide from the cover on;
     - the next camp, beside the forward arrow, once this camp is finished -
       its last slide reached, now or on an earlier visit. The save file
       (camp-save.js) remembers, so a finished camp offers the next one from
       the cover. It wears the next camp's colour, the colour its stop wears
       on the map, and a padlock when the lesson it opens is Pro, because a
       link that lands on a paywall without saying so is the thing the map's
       padlocks exist to prevent.

   One file for all 26 decks, loaded with <script src> beside camp-save.js,
   so the order of the camps is written down once. The camp 9 and descent
   builders take their chassis from a Part I deck, script tag included, so a
   rebuilt deck keeps it. */
(function () {
  'use strict';

  var ROUTE = {
    "maps": {"climb": "block-camp-map.html", "descent": "block-camp-descent-map.html"},
    "end": {"href": "block-camp.html#adventures", "colour": "#e8c04a", "ink": "#0b1a12"},
    "decks": {
      "blockcamp-present-simple": {"href": "blockcamp-present-simple.html", "line": "climb", "n": 1, "name": "Present Simple", "colour": "#7A93B5", "ink": "#0b1a12", "access": "free", "next": "blockcamp-present-continuous", "part": 1},
      "blockcamp-present-simple-2": {"href": "blockcamp-present-simple-2.html", "line": "climb", "n": 1, "name": "Present Simple", "colour": "#7A93B5", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-present-continuous", "part": 2},
      "blockcamp-present-continuous": {"href": "blockcamp-present-continuous.html", "line": "climb", "n": 2, "name": "Present Continuous", "colour": "#E66085", "ink": "#0b1a12", "access": "free", "next": "blockcamp-past-simple", "part": 1},
      "blockcamp-present-continuous-2": {"href": "blockcamp-present-continuous-2.html", "line": "climb", "n": 2, "name": "Present Continuous", "colour": "#E66085", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-past-simple", "part": 2},
      "blockcamp-past-simple": {"href": "blockcamp-past-simple.html", "line": "climb", "n": 3, "name": "Past Simple", "colour": "#B08968", "ink": "#0b1a12", "access": "free", "next": "blockcamp-past-continuous", "part": 1},
      "blockcamp-past-simple-2": {"href": "blockcamp-past-simple-2.html", "line": "climb", "n": 3, "name": "Past Simple", "colour": "#B08968", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-past-continuous", "part": 2},
      "blockcamp-past-continuous": {"href": "blockcamp-past-continuous.html", "line": "climb", "n": 4, "name": "Past Continuous", "colour": "#F1D779", "ink": "#0b1a12", "access": "free", "next": "blockcamp-going-to", "part": 1},
      "blockcamp-past-continuous-2": {"href": "blockcamp-past-continuous-2.html", "line": "climb", "n": 4, "name": "Past Continuous", "colour": "#F1D779", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-going-to", "part": 2},
      "blockcamp-going-to": {"href": "blockcamp-going-to.html", "line": "climb", "n": 5, "name": "Going To", "colour": "#70A43A", "ink": "#0b1a12", "access": "free", "next": "blockcamp-future-simple", "part": 1},
      "blockcamp-going-to-2": {"href": "blockcamp-going-to-2.html", "line": "climb", "n": 5, "name": "Going To", "colour": "#70A43A", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-future-simple", "part": 2},
      "blockcamp-future-simple": {"href": "blockcamp-future-simple.html", "line": "climb", "n": 6, "name": "Future Simple", "colour": "#F0723F", "ink": "#0b1a12", "access": "free", "next": "blockcamp-present-perfect", "part": 1},
      "blockcamp-future-simple-2": {"href": "blockcamp-future-simple-2.html", "line": "climb", "n": 6, "name": "Future Simple", "colour": "#F0723F", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-present-perfect", "part": 2},
      "blockcamp-present-perfect": {"href": "blockcamp-present-perfect.html", "line": "climb", "n": 7, "name": "Present Perfect", "colour": "#2E7D65", "ink": "#f2f7f3", "access": "pro", "next": "blockcamp-present-perfect-continuous", "part": 1},
      "blockcamp-present-perfect-2": {"href": "blockcamp-present-perfect-2.html", "line": "climb", "n": 7, "name": "Present Perfect", "colour": "#2E7D65", "ink": "#f2f7f3", "access": "pro", "next": "blockcamp-present-perfect-continuous", "part": 2},
      "blockcamp-present-perfect-continuous": {"href": "blockcamp-present-perfect-continuous.html", "line": "climb", "n": 8, "name": "Present Perfect Continuous", "colour": "#46B0AB", "ink": "#0b1a12", "access": "free", "next": "blockcamp-past-perfect", "part": 1},
      "blockcamp-present-perfect-continuous-2": {"href": "blockcamp-present-perfect-continuous-2.html", "line": "climb", "n": 8, "name": "Present Perfect Continuous", "colour": "#46B0AB", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-past-perfect", "part": 2},
      "blockcamp-past-perfect": {"href": "blockcamp-past-perfect.html", "line": "climb", "n": 9, "name": "Past Perfect", "colour": "#d66d77", "ink": "#0b1a12", "access": "free", "next": "blockcamp-passive-present-simple", "part": 1},
      "blockcamp-passive-present-simple": {"href": "blockcamp-passive-present-simple.html", "line": "descent", "n": 9, "name": "Present Simple Passive", "colour": "#7A93B5", "ink": "#0b1a12", "access": "free", "next": "blockcamp-passive-present-continuous"},
      "blockcamp-passive-present-continuous": {"href": "blockcamp-passive-present-continuous.html", "line": "descent", "n": 10, "name": "Present Continuous Passive", "colour": "#E66085", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-passive-past-simple"},
      "blockcamp-passive-past-simple": {"href": "blockcamp-passive-past-simple.html", "line": "descent", "n": 11, "name": "Past Simple Passive", "colour": "#B08968", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-passive-past-continuous"},
      "blockcamp-passive-past-continuous": {"href": "blockcamp-passive-past-continuous.html", "line": "descent", "n": 12, "name": "Past Continuous Passive", "colour": "#F1D779", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-passive-going-to"},
      "blockcamp-passive-going-to": {"href": "blockcamp-passive-going-to.html", "line": "descent", "n": 13, "name": "Going To Passive", "colour": "#70A43A", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-passive-future-simple"},
      "blockcamp-passive-future-simple": {"href": "blockcamp-passive-future-simple.html", "line": "descent", "n": 14, "name": "Future Simple Passive", "colour": "#F0723F", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-passive-present-perfect"},
      "blockcamp-passive-present-perfect": {"href": "blockcamp-passive-present-perfect.html", "line": "descent", "n": 15, "name": "Present Perfect Passive", "colour": "#2E7D65", "ink": "#f2f7f3", "access": "pro", "next": "blockcamp-passive-trial"},
      "blockcamp-passive-trial": {"href": "blockcamp-passive-trial.html", "line": "descent", "n": 16, "name": "The Trial", "colour": "#e8c04a", "ink": "#0b1a12", "access": "pro", "next": "blockcamp-passive-past-perfect"},
      "blockcamp-passive-past-perfect": {"href": "blockcamp-passive-past-perfect.html", "line": "descent", "n": 17, "name": "Past Perfect Passive", "colour": "#d66d77", "ink": "#0b1a12", "access": "pro", "next": "end"}
    }
  };

  /* The words, in every language a Block Camp deck offers. Map, camp and
     descent are the Sherpa hub's (tools/sherpa_hub_i18n.py), which a
     native-level reader went over. Camp names stay English, as they do
     everywhere in the line. */
  var T = {
    en: { map: 'Route map', descentMap: 'Descent map', nextCamp: 'Next camp', nextStation: 'Next station',
          descent: 'The descent', next: 'Next', adventures: 'The adventures', pro: ', subscribers only' },
    de: { map: 'Routenkarte', descentMap: 'Abstiegskarte', nextCamp: 'Nächstes Lager', nextStation: 'Nächste Station',
          descent: 'Der Abstieg', next: 'Weiter', adventures: 'Die Abenteuer', pro: ', nur für Abonnenten' },
    es: { map: 'Mapa de la ruta', descentMap: 'Mapa de la bajada', nextCamp: 'Siguiente campamento', nextStation: 'Siguiente estación',
          descent: 'La bajada', next: 'Sigue', adventures: 'Las aventuras', pro: ', solo para suscriptores' },
    fr: { map: 'Carte de l’itinéraire', descentMap: 'Carte de la descente', nextCamp: 'Camp suivant', nextStation: 'Station suivante',
          descent: 'La descente', next: 'Ensuite', adventures: 'Les aventures', pro: ', réservé aux abonnés' },
    it: { map: 'Mappa del percorso', descentMap: 'Mappa della discesa', nextCamp: 'Prossimo campo', nextStation: 'Prossima tappa',
          descent: 'La discesa', next: 'Avanti', adventures: 'Le avventure', pro: ', solo per abbonati' },
    pt: { map: 'Mapa da trilha', descentMap: 'Mapa da descida', nextCamp: 'Próximo acampamento', nextStation: 'Próxima estação',
          descent: 'A descida', next: 'A seguir', adventures: 'As aventuras', pro: ', só para assinantes' },
    ru: { map: 'Карта маршрута', descentMap: 'Карта спуска',
          nextCamp: 'Следующий лагерь', nextStation: 'Следующая станция',
          descent: 'Спуск', next: 'Дальше', adventures: 'Приключения',
          pro: ', только для подписчиков' },
    ar: { map: 'خريطة الطريق', descentMap: 'خريطة النزول',
          nextCamp: 'المخيم التالي', nextStation: 'المحطة التالية',
          descent: 'النزول', next: 'التالي', adventures: 'المغامرات',
          pro: '، للمشتركين فقط' },
    zh: { map: '路线图', descentMap: '下山路线图', nextCamp: '下一个营地', nextStation: '下一站',
          descent: '下山', next: '接下来', adventures: '冒险故事', pro: '，仅限订阅用户' },
    ja: { map: 'ルートマップ', descentMap: '下りのマップ', nextCamp: '次のキャンプ', nextStation: '次のステーション',
          descent: '下り', next: '次へ', adventures: 'アドベンチャー', pro: '（購読者限定）' }
  };

  /* Built from the deck's own theme tokens, so each chip sits in the palette
     of the deck it is on. No black or white written in: the drop under the
     next-camp button is the button's own colour mixed toward --void. */
  var CSS = [
    '.camp-home{display:inline-flex;align-items:center;gap:8px;flex:none;box-sizing:border-box;',
    '  height:34px;padding:0 12px 0 10px;border-radius:6px;text-decoration:none;white-space:nowrap;',
    '  font-family:var(--font-mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;',
    '  background:var(--scrim);color:var(--text);',
    '  border:1px solid color-mix(in srgb,var(--border) 70%,transparent);',
    '  transition:border-color .15s ease,color .15s ease}',
    '.camp-home:hover,.camp-home:focus-visible{border-color:var(--accent);color:var(--accent-bright)}',
    '.camp-home svg{width:17px;height:17px;flex:none}',
    '.camp-next{display:inline-flex;align-items:center;gap:12px;flex:none;box-sizing:border-box;',
    '  height:54px;padding:0 16px 0 18px;border-radius:12px;text-decoration:none;',
    '  background:var(--nc);color:var(--nci);',
    '  box-shadow:0 3px 0 color-mix(in srgb,var(--nc) 55%,var(--void));',
    '  transition:transform .15s ease,box-shadow .15s ease}',
    '.camp-next[hidden]{display:none}',
    '.camp-next:hover,.camp-next:focus-visible{transform:translateY(-2px);',
    '  box-shadow:0 5px 0 color-mix(in srgb,var(--nc) 55%,var(--void))}',
    '.camp-next-t{display:flex;flex-direction:column;gap:3px;line-height:1.1;text-align:start}',
    '.camp-next-cap{font-family:var(--font-mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase}',
    '.camp-next-name{font-family:var(--font-display);font-size:16px;font-weight:700;white-space:nowrap}',
    '.camp-next-go{font-size:22px;line-height:1}',
    '[dir="rtl"] .camp-next-go{transform:scaleX(-1)}',
    '.camp-next-lock{display:inline-block;width:.72em;height:.84em;margin-inline-start:.45em;',
    '  vertical-align:-.06em;background:currentColor;',
    '  -webkit-mask:url("' + LOCK() + '") no-repeat center/contain;mask:url("' + LOCK() + '") no-repeat center/contain}',
    '.camp-sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;',
    '  clip:rect(0 0 0 0);white-space:nowrap;border:0}',
    /* It arrives, once, the moment the last slide is reached: in from the
       arrow's side, then three rings, so the eye that is on the forward arrow
       finds it. A camp finished on an earlier visit shows it still. */
    '.camp-next.is-new{animation:camp-next-in .45s cubic-bezier(.2,.8,.3,1.2) both,',
    '  camp-next-ring 1.6s ease-out .45s 3}',
    '@keyframes camp-next-in{from{opacity:0;transform:translateX(14px) scale(.92)}to{opacity:1;transform:none}}',
    '@keyframes camp-next-ring{',
    '  0%{box-shadow:0 3px 0 color-mix(in srgb,var(--nc) 55%,var(--void)),0 0 0 0 color-mix(in srgb,var(--nc) 70%,transparent)}',
    '  70%{box-shadow:0 3px 0 color-mix(in srgb,var(--nc) 55%,var(--void)),0 0 0 12px color-mix(in srgb,var(--nc) 0%,transparent)}',
    '  100%{box-shadow:0 3px 0 color-mix(in srgb,var(--nc) 55%,var(--void)),0 0 0 0 color-mix(in srgb,var(--nc) 0%,transparent)}}',
    '@media (prefers-reduced-motion:reduce){.camp-next.is-new{animation:none}}'
  ].join('\n');

  /* The map's padlock, verbatim (block-camp-map.html, .lock). */
  function LOCK() {
    return "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2012%2014'%3E%3Cpath%20d='M3.4%206.2V4.1a2.6%202.6%200%200%201%205.2%200v2.1'%20fill='none'%20stroke='black'%20stroke-width='1.5'%20stroke-linecap='round'/%3E%3Crect%20x='1.4'%20y='6.2'%20width='9.2'%20height='7.1'%20rx='1.5'%20fill='black'/%3E%3Ccircle%20cx='6'%20cy='9.3'%20r='1'%20fill='white'/%3E%3Crect%20x='5.5'%20y='9.3'%20width='1'%20height='2'%20rx='.5'%20fill='white'/%3E%3C/svg%3E";
  }

  /* A folded map. A tent was tried first and at 17px it read as a warning
     triangle. Drawn in currentColor so it takes the chip's ink and its hover
     colour. */
  var MAP = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" ' +
    'stroke-width="1.5" stroke-linejoin="round"><path d="M1.5 3.6 5.8 2l4.4 1.6L14.5 2v10.4L10.2 14l-4.4-1.6-4.3 1.6z"/>' +
    '<path d="M5.8 2v10.4M10.2 3.6V14"/></svg>';

  function pageId() {
    var p = (location.pathname || '').split('/').pop() || '';
    try { p = decodeURIComponent(p); } catch (_) {}
    return p.replace(/\.html?$/i, '');
  }

  var id = pageId();
  var me = ROUTE.decks[id];
  var bar = document.querySelector('.deck-bar');
  if (!me || !bar || document.querySelector('.camp-home')) return;

  var style = document.createElement('style');
  style.id = 'camp-nav-css';
  style.textContent = CSS;
  document.head.appendChild(style);

  // ── the way back ──
  var home = document.createElement('a');
  home.className = 'camp-home';
  home.href = ROUTE.maps[me.line];
  home.innerHTML = MAP + '<span class="camp-home-l"></span>';
  bar.insertBefore(home, bar.firstChild);

  // ── the way on ──
  var nx = me.next === 'end' ? null : ROUTE.decks[me.next];
  var to = nx || ROUTE.end;
  var next = document.createElement('a');
  next.className = 'camp-next';
  next.hidden = true;
  next.href = to.href;
  next.style.setProperty('--nc', to.colour);
  next.style.setProperty('--nci', to.ink);
  // The padlock rides on the caption line, after its words, where the map
  // puts it after a lesson's name.
  next.innerHTML = '<span class="camp-next-t"><span class="camp-next-cap"><span class="camp-next-w"></span>' +
    (nx && nx.access === 'pro'
      ? '<span class="camp-next-lock" aria-hidden="true"></span><span class="camp-sr"></span>' : '') +
    '</span><span class="camp-next-name"></span></span><span class="camp-next-go" aria-hidden="true">&rarr;</span>';
  var name = next.querySelector('.camp-next-name');
  var sr = next.querySelector('.camp-sr');
  bar.appendChild(next);

  function label() {
    var lang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase().slice(0, 2);
    var L = T[lang] || T.en;
    var w = function (k) { return L[k] != null ? L[k] : T.en[k]; };
    home.querySelector('.camp-home-l').textContent = w(me.line === 'descent' ? 'descentMap' : 'map');
    var cap = !nx ? w('next')
            : nx.line === 'climb' ? w('nextCamp')
            : me.line === 'climb' ? w('descent')
            : w('nextStation');
    next.querySelector('.camp-next-w').textContent = cap;
    // An English name inside an Arabic bar keeps its own order: number first.
    name.textContent = nx ? nx.n + ' · ' + nx.name : w('adventures');
    name.dir = nx ? 'ltr' : 'auto';
    if (sr) sr.textContent = w('pro');
    next.title = cap + ': ' + name.textContent;
  }
  label();
  // The deck sets <html lang> whenever the language picker changes.
  if (window.MutationObserver) {
    new MutationObserver(label).observe(document.documentElement,
      { attributes: true, attributeFilter: ['lang'] });
  }

  // ── finished? ──
  var slides = document.querySelectorAll('.slide');
  var last = slides[slides.length - 1];
  function saved() {
    try {
      var e = window.CampSave && window.CampSave.load().deck[id];
      return !!(e && e.done);
    } catch (_) { return false; }
  }
  function reveal(fresh) {
    if (!next.hidden) return;
    next.hidden = false;
    if (fresh) next.classList.add('is-new');
  }
  if (saved() || (last && last.classList.contains('is-active'))) reveal(false);
  if (last && window.MutationObserver) {
    new MutationObserver(function () {
      if (last.classList.contains('is-active')) reveal(true);
    }).observe(last, { attributes: true, attributeFilter: ['class'] });
  }
})();
