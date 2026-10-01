/* Block Camp: the end slide as a choice, not a wall.

   Innes, 2026-10-01: "make end screen with choice buttons to expand discuss
   and write". The activation slide's two cards (speaking in pairs, the
   writing task) used to stand side by side over the end clip. Now the word
   bank stays, and two big buttons, Discuss and Write, open one card at a
   time; a second tap closes it. Nothing is removed: the cards are the deck's
   own nodes, only shown and hidden, so the deck's translation, word count
   and Copy button keep working. Print shows both.

   Load with  <script src="block-camp/camp-end.js" defer></script>  */
(function () {
  'use strict';
  var slide = document.querySelector('.slide[data-type="activate"]');
  if (!slide || slide.querySelector('.act-choose')) return;
  var cols = slide.querySelector('.act-cols');
  var cards = cols ? [].slice.call(cols.querySelectorAll('.act-card')) : [];
  if (cards.length < 2) return;
  // Which card is which: the writing card is the one with the text box.
  var write = cards.filter(function (c) { return c.querySelector('textarea'); })[0] || cards[1];
  var speak = cards.filter(function (c) { return c !== write; })[0];

  var T = {
    en: ['Discuss', 'Write'], de: ['Sprechen', 'Schreiben'], es: ['Conversar', 'Escribir'],
    fr: ['Discuter', 'Écrire'], it: ['Discutere', 'Scrivere'], pt: ['Conversar', 'Escrever'],
    ru: ['Обсудить', 'Написать'],
    ar: ['ناقش', 'اكتب'],
    zh: ['讨论', '写作'], ja: ['話し合う', '書く']
  };

  var css = document.createElement('style');
  css.textContent =
    '.act-choose{display:flex;flex-wrap:wrap;gap:14px;margin:16px 0 4px}' +
    '.act-choice{display:inline-flex;align-items:center;gap:12px;min-height:58px;padding:0 26px;' +
    'border-radius:14px;cursor:pointer;font-family:var(--font-display);font-size:22px;letter-spacing:.02em;' +
    'color:var(--text);background:var(--surface2);background:color-mix(in srgb,var(--surface2) 86%,transparent);' +
    'border:2px solid color-mix(in srgb,var(--accent) 65%,transparent);transition:background .15s,color .15s,border-color .15s}' +
    '.act-choice .act-choice-i{font-size:24px;line-height:1}' +
    '.act-choice:hover,.act-choice:focus-visible{border-color:var(--accent);outline:none}' +
    '.act-choice[aria-expanded="true"]{background:var(--accent);color:var(--void);border-color:var(--accent)}' +
    '.act-choosing .act-cols{display:block!important}' +
    '.act-choosing .act-card{display:none!important}' +
    '.act-choosing .act-card.act-open{display:block!important;width:100%;max-width:none}' +
    // The card is full width now, so the box is too (it was sized for half).
    '.act-choosing .act-card.act-open .act-input{width:100%!important;max-width:none;min-height:120px;box-sizing:border-box}' +
    '@media print{.act-choose{display:none!important}.act-choosing .act-card{display:block!important}}';
  document.head.appendChild(css);

  var row = document.createElement('div');
  row.className = 'act-choose';
  row.setAttribute('role', 'group');
  function make(card, icon, key) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'act-choice';
    b.setAttribute('aria-expanded', 'false');
    b.innerHTML = '<span class="act-choice-i" aria-hidden="true">' + icon + '</span><span class="act-choice-l"></span>';
    b._card = card; b._key = key;
    if (!card.id) card.id = 'act-card-' + key;
    b.setAttribute('aria-controls', card.id);
    b.addEventListener('click', function () { toggle(b); });
    row.appendChild(b);
    return b;
  }
  var bSpeak = make(speak, '🗣️', 0);
  var bWrite = make(write, '✍️', 1);
  cols.parentNode.insertBefore(row, cols);
  slide.classList.add('act-choosing');

  function toggle(b) {
    var opening = b.getAttribute('aria-expanded') !== 'true';
    [bSpeak, bWrite].forEach(function (x) {
      var on = opening && x === b;
      x.setAttribute('aria-expanded', on ? 'true' : 'false');
      x._card.classList.toggle('act-open', on);
    });
    if (opening) {
      // Bring the opened task into view on a scrolling (phone) slide.
      try { b._card.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); } catch (_) {}
      var ta = b._card.querySelector('textarea');
      if (ta && !(window.matchMedia && matchMedia('(pointer: coarse)').matches)) ta.focus({ preventScroll: true });
    }
  }

  function label() {
    var lang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase().slice(0, 2);
    var L = T[lang] || T.en;
    bSpeak.querySelector('.act-choice-l').textContent = L[0];
    bWrite.querySelector('.act-choice-l').textContent = L[1];
  }
  label();
  if (window.MutationObserver) new MutationObserver(label).observe(document.documentElement,
    { attributes: true, attributeFilter: ['lang'] });
})();
