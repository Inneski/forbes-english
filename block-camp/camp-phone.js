/* Block Camp: the phone layout's switch and its touch fixes (camp-phone.css
   has the layout and the reasons).

   Loaded WITHOUT defer from <head>, straight after camp-phone.css, so the
   mode is on <html> before the first paint and a phone never flashes the
   tiny scaled canvas. The DOM work waits for DOMContentLoaded, which fires
   after the deferred camp-nav.js and camp-music.js, so their controls exist.

   Phone mode = the canvas would be drawn below 0.62 of its size. It is not
   re-decided while a text field has focus: a phone keyboard shrinks the
   window, and flipping layout mid-word loses the learner's place. */
(function () {
  'use strict';
  var html = document.documentElement;
  var THRESHOLD = 0.62;
  var typing = false;

  function wantPhone() { return Math.min(innerWidth / 1280, innerHeight / 720) < THRESHOLD; }
  function landscape() { return innerWidth > innerHeight * 1.15; }
  function setClasses() {
    var on = wantPhone();
    html.classList.toggle('bc-phone', on);
    html.classList.toggle('bc-land', on && landscape());
    html.classList.toggle('bc-port', on && !landscape());
    return on;
  }
  setClasses();

  function ready(fn) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn);
    else fn();
  }

  ready(function () {
    var stage = document.getElementById('stage');
    var bar = stage && stage.querySelector('.deck-bar');
    if (!stage || !bar) return;
    var slides = [].slice.call(stage.querySelectorAll('.slide'));

    // ── the menu: the bar's secondary controls, moved not cloned ──
    var MENU_SEL = '.camp-home, .camp-music, #langSelect, #ccSelect, #bwTrBtn, .part-link';
    var menuBtn = document.createElement('button');
    menuBtn.type = 'button'; menuBtn.className = 'bcp-menu';
    menuBtn.setAttribute('aria-expanded', 'false');
    menuBtn.setAttribute('aria-label', 'Menu');
    menuBtn.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" ' +
      'stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
    var sheet = document.createElement('div');
    sheet.className = 'bcp-sheet';
    sheet.setAttribute('role', 'menu');
    stage.appendChild(sheet);
    var home = [];                     // [node, placeholder] so a move can be undone exactly
    function toSheet() {
      if (menuBtn.parentNode !== bar) bar.insertBefore(menuBtn, bar.firstChild);
      [].slice.call(bar.querySelectorAll(MENU_SEL)).forEach(function (n) {
        var mark = document.createComment('bcp');
        n.parentNode.insertBefore(mark, n);
        home.push([n, mark]);
        sheet.appendChild(n);
      });
    }
    function toBar() {
      home.forEach(function (p) { if (p[1].parentNode) { p[1].parentNode.insertBefore(p[0], p[1]); p[1].remove(); } });
      home = [];
      if (menuBtn.parentNode) menuBtn.remove();
      closeMenu();
    }
    function closeMenu() { sheet.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); }
    menuBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = !sheet.classList.contains('open');
      sheet.classList.toggle('open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', function (e) {
      if (sheet.classList.contains('open') && !sheet.contains(e.target) && e.target !== menuBtn) closeMenu();
    });
    // Picking a language or subtitles, or following a link, closes the sheet.
    sheet.addEventListener('change', function () { setTimeout(closeMenu, 150); });
    sheet.addEventListener('click', function (e) { if (e.target.closest('a')) closeMenu(); });

    // ── the pop-out: Begin on a phone also goes full screen ──
    // camp-full.js (Innes, 2026-10-02: "full screen pop out ideally") can only
    // enter full screen from inside a tap, so it rides on the cover's own
    // forward tap. Where the phone has no full-screen API (an iPhone) this
    // does nothing; the bar's button explains the Home Screen instead.
    stage.addEventListener('click', function (e) {
      if (!html.classList.contains('bc-phone') || !window.CampFull) return;
      var go = e.target.closest && e.target.closest('[data-action="next"]');
      var cover = stage.querySelector('.slide.is-active[data-type="cover"]');
      if (go && cover) window.CampFull.popOut();
    }, true);

    // ── the score, short: "★ 3/12" (camp-phone.css shows it on a phone) ──
    var scoreEl = document.getElementById('deckScore');
    function shortScore() {
      var m = scoreEl.textContent.match(/(\d+\s*\/\s*\d+)\s*$/);
      if (m) scoreEl.setAttribute('data-short', m[1].replace(/\s+/g, ''));
      else scoreEl.removeAttribute('data-short');
    }
    if (scoreEl) { shortScore(); new MutationObserver(shortScore).observe(scoreEl, { childList: true, characterData: true, subtree: true }); }

    // ── the picture's focal point: the subject is opposite the text ──
    function focus() {
      var s = stage.querySelector('.slide.is-active');
      var side = s && s.getAttribute('data-side');
      var cover = s && s.getAttribute('data-type') === 'cover';
      stage.style.setProperty('--focus-x', cover ? '68%' : side === 'left' ? '72%' : side === 'right' ? '28%' : '50%');
    }

    // ── touch fixes ──
    var lastTouch = 0;
    document.addEventListener('touchstart', function () { lastTouch = Date.now(); }, { capture: true, passive: true });
    [].slice.call(stage.querySelectorAll('input.gap')).forEach(function (g) {
      g.setAttribute('autocapitalize', 'off'); g.setAttribute('autocorrect', 'off');
      g.setAttribute('autocomplete', 'off'); g.setAttribute('spellcheck', 'false');
    });
    slides.forEach(function (s) {
      var gaps = [].slice.call(s.querySelectorAll('input.gap'));
      gaps.forEach(function (g, i) { g.setAttribute('enterkeyhint', i < gaps.length - 1 ? 'next' : 'done'); });
    });
    // Return in a gap marked the WHOLE slide, empty gaps wrong, with no
    // second try. On a phone, Return moves to the next empty gap instead;
    // only the last one (or none left empty) checks.
    window.addEventListener('keydown', function (e) {
      if (!html.classList.contains('bc-phone') || e.key !== 'Enter') return;
      var t = e.target;
      if (!t.matches || !t.matches('input.gap')) return;
      var gaps = [].slice.call(t.closest('.slide').querySelectorAll('input.gap:not(:disabled)'));
      var after = gaps.slice(gaps.indexOf(t) + 1).concat(gaps.slice(0, gaps.indexOf(t)));
      var next = after.filter(function (g) { return !g.value.trim(); })[0];
      if (next) { e.preventDefault(); e.stopImmediatePropagation(); next.focus(); }
    }, true);
    document.addEventListener('focusin', function (e) {
      if (e.target.matches && e.target.matches('input, textarea')) { typing = true; html.classList.add('bc-typing'); }
    });
    document.addEventListener('focusout', function (e) {
      if (e.target.matches && e.target.matches('input, textarea')) {
        setTimeout(function () {
          var a = document.activeElement;
          if (!(a && a.matches && a.matches('input, textarea'))) { typing = false; html.classList.remove('bc-typing'); }
        }, 80);
      }
    });

    function arrived(s) {
      s.scrollTop = 0;
      focus();
      if (!html.classList.contains('bc-phone')) return;
      // The deck focuses the first gap 60ms after arrival, which opens a
      // phone keyboard over a sentence nobody has read yet.
      setTimeout(function () {
        var a = document.activeElement;
        if (a && a.matches && a.matches('input.gap') && Date.now() - lastTouch > 400) {
          a.blur();
          s.scrollTop = 0;       // the focus had already scrolled the slide down
        }
      }, 140);
    }
    slides.forEach(function (s) {
      new MutationObserver(function () {
        if (s.classList.contains('is-active') && !s._bcpActive) { s._bcpActive = true; arrived(s); }
        else if (!s.classList.contains('is-active')) s._bcpActive = false;
      }).observe(s, { attributes: true, attributeFilter: ['class'] });
      s._bcpActive = s.classList.contains('is-active');
    });
    // After an answer, bring the explanation into view.
    new MutationObserver(function (muts) {
      if (!html.classList.contains('bc-phone')) return;
      muts.forEach(function (m) {
        var el = m.target;
        if (el.classList && el.classList.contains('feedback') && el.classList.contains('show') && !el._bcpSeen) {
          el._bcpSeen = true;
          setTimeout(function () { el.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); }, 60);
        }
      });
    }).observe(stage, { subtree: true, attributes: true, attributeFilter: ['class'] });

    // A narrow line breaks after the hyphen in "-ing", leaving "take -" /
    // "ing?". Keep a suffix (-ing, -ed, -s) with itself in titles and labels.
    function keepSuffixes(root) {
      [].slice.call(root.querySelectorAll('.slide-title, .sort-bin-label, .eyebrow, .q-stem')).forEach(function (el) {
        var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), nodes = [], n;
        while ((n = walker.nextNode())) if (/(^|\s)[-‑][a-z]+/i.test(n.nodeValue)) nodes.push(n);
        nodes.forEach(function (t) {
          var frag = document.createDocumentFragment();
          t.nodeValue.split(/((?:^|\s)[-‑][a-z]+)/i).forEach(function (part, i) {
            if (i % 2) {
              var lead = part.match(/^\s*/)[0];
              if (lead) frag.appendChild(document.createTextNode(lead));
              var sp = document.createElement('span'); sp.style.whiteSpace = 'nowrap';
              sp.textContent = part.slice(lead.length); frag.appendChild(sp);
            } else if (part) frag.appendChild(document.createTextNode(part));
          });
          t.parentNode.replaceChild(frag, t);
        });
      });
    }

    // ── entering and leaving phone mode ──
    function apply() {
      var on = html.classList.contains('bc-phone');
      if (on && !home.length) {
        toSheet();
        [].slice.call(stage.querySelectorAll('.sort-bins')).forEach(function (b) {
          b.style.setProperty('--bins', b.children.length);
        });
        [].slice.call(stage.querySelectorAll('.sort-item')).forEach(function (i) { i.draggable = false; });
        if (!stage._bcpSuffixes) { stage._bcpSuffixes = true; keepSuffixes(stage); }
      } else if (!on && home.length) {
        toBar();
        [].slice.call(stage.querySelectorAll('.sort-item:not(.placed)')).forEach(function (i) { i.draggable = true; });
        if (typeof window.fitStage === 'function') window.fitStage();
      }
      focus();
    }
    apply();
    var t = null;
    addEventListener('resize', function () {
      if (typing) return;
      clearTimeout(t);
      t = setTimeout(function () { setClasses(); apply(); }, 120);
    });
  });
})();
