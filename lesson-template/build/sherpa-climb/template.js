/* The Climb (lesson-template/build/sherpa-climb/template.js). The data and the strings are
   inlined above this by build.py: window.CLIMB_DATA (content.py + the route map) and
   window.CLIMB_I18N (the chrome in English, and every complete language).

   Saves to localStorage 'sherpa.climb.v1' only. It never writes 'sherpa.progress.v1': the
   route map counts that as camps finished, and opens passives from it. */
(function () {
  'use strict';
  var D = window.CLIMB_DATA, I = window.CLIMB_I18N;
  var CAMPS = D.camps, SUMMIT = D.summit, TENSES = D.tenses;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var body = document.body;
  var ITEM = {};
  CAMPS.forEach(function (c) { c.items.forEach(function (it) { ITEM[it.id] = it; }); });
  if (SUMMIT) SUMMIT.items.forEach(function (it) { ITEM[it.id] = it; });
  var RM = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };
  var COARSE = window.matchMedia ? window.matchMedia('(pointer: coarse)') : { matches: false };

  /*CANON:start*/
  /* A typed answer and the accepted ones, made comparable: NFKC, lower case, curly and back
     quotes to ', dashes to -, "..." to a space, spaces collapsed, a final . ! ? dropped. Then
     each contraction is expanded, so "'m tying" = "am tying" and "dont" = "do not"; "'s" and
     "'d" could be two things, so every reading is kept (a SET of variants). Right = any variant
     of the answer meets any variant of any accepted entry. */
  function flat(s) {
    s = String(s == null ? '' : s);
    if (s.normalize) s = s.normalize('NFKC');
    s = s.toLowerCase()
      .replace(/[‘’‚‛′´`]/g, "'")
      .replace(/[“”„‟″]/g, '"')
      .replace(/[‐-―−]/g, '-')
      .replace(/\.\.\.|…/g, ' ')
      .replace(/\s+/g, ' ').trim()
      .replace(/\s*[.!?]+$/, '')
      .trim();
    return s;
  }
  var NEG_BARE = /\b(dont|doesnt|didnt|isnt|arent|wasnt|werent|havent|hasnt|hadnt|wont|cant)\b/g;
  function variants(s) {
    s = flat(s)
      .replace(NEG_BARE, function (m) { return m.slice(0, -1) + "'t"; })
      .replace(/\bwon't\b/g, 'will not').replace(/\bcan't\b/g, 'can not').replace(/\bcannot\b/g, 'can not')
      .replace(/\bshan't\b/g, 'will not').replace(/\bshall\b/g, 'will')  // BrE "I / we shall" = will
      .replace(/n't\b/g, ' not')
      .replace(/'m\b/g, ' am').replace(/'re\b/g, ' are').replace(/'ve\b/g, ' have').replace(/'ll\b/g, ' will');
    var out = [s];
    [[/'s\b/, [' is', ' has']], [/'d\b/, [' had', ' would']]].forEach(function (rule) {
      var next = [];
      out.forEach(function (v) {
        var todo = [v];
        while (todo.length) {
          var x = todo.shift();
          if (!rule[0].test(x) || next.length > 64) { if (next.indexOf(x) < 0) next.push(x); continue; }
          rule[1].forEach(function (alt) { todo.push(x.replace(rule[0], alt)); });
        }
      });
      out = next;
    });
    return out.map(function (v) { return v.replace(/\s+/g, ' ').trim(); });
  }
  function accepts(input, accept) {
    var mine = variants(input);
    if (!mine[0]) return false;
    return (accept || []).some(function (a) {
      return variants(a).some(function (v) { return mine.indexOf(v) >= 0; });
    });
  }
  /*CANON:end*/

  // ── strings ──────────────────────────────────────────────────────────────────
  var LKEY = 'sherpa.lang.v1';
  var lang = 'en';
  function t(key, vars) {
    var en = I.en[key] || key;
    var s = (lang !== 'en' && I.t[lang] && I.t[lang][en]) || en;
    for (var k in (vars || {})) s = s.split('{' + k + '}').join(vars[k]);
    return s;
  }
  function gloss(en) { return (lang !== 'en' && en && I.t[lang] && I.t[lang][en]) || ''; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  var CAPS = /\b[A-Z][A-Z]+(?:['’-][A-Z]+)*\b/g;
  function rich(s, caps) {
    s = esc(s);
    if (caps) s = s.replace(CAPS, '<span class="cap">$&</span>');
    return s.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
  }
  function glHtml(en, caps, tag) {
    var g = gloss(en);
    if (!g) return '';
    return '<' + (tag || 'span') + ' class="gl" lang="' + lang + '"' + (I.rtl.indexOf(lang) >= 0 ? ' dir="rtl"' : '') + '>' +
      rich(g, caps) + '</' + (tag || 'span') + '>';
  }
  /* A narrative line on a card: the English, and the learner's language in the same box,
     beneath it (.gl). When the card has no room for both, fit() hides the glosses and shows
     the card's "Translation" toggle, which puts each gloss in place of its English (.tx) in
     that same box, and back. With no gloss (English) it is just the English. */
  function pair(en, caps) {
    var g = glHtml(en, caps);
    return g ? '<span class="tx" lang="en">' + rich(en, caps) + '</span>' + g : rich(en, caps);
  }
  var GLOBE = '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="1.5">' +
    '<circle cx="10" cy="10" r="7.5"/><ellipse cx="10" cy="10" rx="3.2" ry="7.5"/><path d="M2.5 10h15M3.9 6.5h12.2M3.9 13.5h12.2"/></svg>';
  // the card's one toggle (shown only while fit() has the glosses hidden); none in English
  function togHtml() {
    if (lang === 'en') return '';
    return '<button class="gtog" id="gtog" type="button" aria-pressed="' + gsw.on + '" lang="' + lang + '"' +
      (I.rtl.indexOf(lang) >= 0 ? ' dir="rtl"' : '') + '>' + GLOBE + '<span>' + esc(t('translation')) + '</span></button>';
  }
  /* The toggle's position is remembered for the card on screen only: a new card starts with
     the English. A redraw of the same card (a language change, a resize) keeps it. */
  var gsw = { on: false };
  function newCard() { gsw = { on: false }; }
  function fmt(n) {
    try { return new Intl.NumberFormat(lang === 'en' ? 'en-GB' : lang, { numberingSystem: 'latn' }).format(n); }
    catch (e) { return String(n); }
  }
  function marks(el) {
    if (lang === 'en') { el.removeAttribute('lang'); el.removeAttribute('dir'); return; }
    el.setAttribute('lang', lang);
    if (I.rtl.indexOf(lang) >= 0) el.setAttribute('dir', 'rtl'); else el.removeAttribute('dir');
  }

  // ── the save ─────────────────────────────────────────────────────────────────
  var SKEY = /*@game:climb*/'sherpa.climb.v1'/*@game:descent*/'sherpa.descent.v1'/*@game:end*/;
  var mem = null;   // stands in for storage when the browser blocks it (private windows)
  function fresh() { return { v: 1, camps: {}, summit: null, last: null, misses: {} }; }
  function load() {
    if (mem) return mem;
    var s = null;
    try { s = JSON.parse(localStorage.getItem(SKEY)); } catch (e) { s = null; }
    if (!s || s.v !== 1 || typeof s !== 'object') s = fresh();
    if (!s.camps || typeof s.camps !== 'object') s.camps = {};
    if (!s.misses || typeof s.misses !== 'object') s.misses = {};
    if (!('summit' in s)) s.summit = null;
    if (!('last' in s)) s.last = null;
    return s;
  }
  function put(s) {
    try { localStorage.setItem(SKEY, JSON.stringify(s)); mem = null; } catch (e) { mem = s; }
  }

  // ── sound: two short tones, off until asked for (rpg.py's beep) ───────────────
  var sound = false;
  try { sound = localStorage.getItem('sherpa-climb-sound') === '1'; } catch (e) {}
  function beep(ok) {
    if (!sound) return;
    try {
      var c = new (window.AudioContext || window.webkitAudioContext)();
      var o = c.createOscillator(), g = c.createGain();
      o.type = ok ? 'square' : 'sawtooth'; o.frequency.value = ok ? 620 : 180; g.gain.value = .03;
      o.connect(g); g.connect(c.destination); o.start();
      g.gain.exponentialRampToValueAtTime(.001, c.currentTime + .16); o.stop(c.currentTime + .18);
      o.onended = function () { c.close(); };
    } catch (e) {}
  }
  function paintSound() {
    var b = $('#snd');
    b.setAttribute('aria-pressed', String(sound));
    b.setAttribute('aria-label', t(sound ? 'soundOn' : 'soundOff'));
    b.title = t(sound ? 'soundOn' : 'soundOff') + ' (S)';
  }
  function setSound(on) {
    sound = !!on;
    try { localStorage.setItem('sherpa-climb-sound', sound ? '1' : '0'); } catch (e) {}
    paintSound();
  }

  // ── pictures ─────────────────────────────────────────────────────────────────
  function sceneSrc(stage) {
    if (stage === 'top') return D.top.scene;
    return stage.scene + (window.innerWidth < 900 ? '-sm' : '') + '.jpg';
  }
  function setScene(src) {
    var img = $('#scene');
    if (img.getAttribute('src') === src) return;
    if (!RM.matches) img.classList.add('loading');
    img.onload = img.onerror = function () { img.classList.remove('loading'); };
    img.setAttribute('src', src);
  }
  function preload(stage) { if (stage) { var i = new Image(); i.src = sceneSrc(stage); } }
  function fig(who, cls) { return '<span class="' + (cls || 'fig-s') + '">' + (D.figs[who] || '') + '</span>'; }
  function flagSvg(gold, title) {
    return '<svg class="flag-ico' + (gold ? ' gold' : '') + '" viewBox="0 0 18 20" role="img" aria-label="' + esc(title) + '">' +
      '<title>' + esc(title) + '</title><path d="M3 19 V2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>' +
      '<path class="pennant" d="M3 2.5 L16 6.5 L3 10.5 Z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>';
  }

  // ── the start screen ─────────────────────────────────────────────────────────
  function after(n) {
    var i = -1;
    CAMPS.forEach(function (c, k) { if (c.n === n) i = k; });
    if (i >= 0 && CAMPS[i + 1]) return CAMPS[i + 1].n;
    if (n === D.lastRoute && SUMMIT) return 'summit';
    return null;
  }
  /* Where "Continue" goes: the camp left half-way, else the one after the last finished,
     else the first not yet played (a summit run with camps unplayed sends you back down to
     them), else nothing ("Start at camp one"). */
  function nextTarget(s) {
    var any = Object.keys(s.camps).length > 0 || !!s.summit;
    if (!any && s.last == null) return null;
    if (s.last === 'summit' && SUMMIT && !s.summit) return 'summit';
    if (s.last != null && s.last !== 'summit' && byN(s.last)) {
      if (!s.camps[s.last]) return s.last;
      var a = after(s.last);
      if (a === 'summit' ? !s.summit : (a != null && !s.camps[a])) return a;
    }
    for (var i = 0; i < CAMPS.length; i++) if (!s.camps[CAMPS[i].n]) return CAMPS[i].n;
    if (SUMMIT && !s.summit) return 'summit';
    return null;
  }
  function byN(n) { for (var i = 0; i < CAMPS.length; i++) if (String(CAMPS[i].n) === String(n)) return CAMPS[i]; return null; }
  function isGold(rec) { return !!rec && (rec.gold || rec.best / rec.total >= .75); }

  function paintStart() {
    var s = load();
    $$('.pick[data-camp]').forEach(function (b) {
      var n = b.getAttribute('data-camp');
      var rec = n === 'summit' ? s.summit : s.camps[n];
      var best = $('.pick-best', b), flag = $('.pick-flag', b);
      if (rec && rec.total) {
        best.innerHTML = rec.best + '/' + rec.total + '<span class="sr-only"> · ' + esc(t('srBest', { k: rec.best, m: rec.total })) + '</span>';
        flag.innerHTML = flagSvg(isGold(rec), t(isGold(rec) ? 'flagGold' : 'flagPlain'));
      } else { best.innerHTML = ''; flag.innerHTML = ''; }
    });
    var go = $('#go'), label = $('#go-label');
    var target = nextTarget(s);
    go.setAttribute('data-target', target == null ? (CAMPS[0] ? CAMPS[0].n : '') : target);
    if (target == null) { label.setAttribute('data-t', 'startOne'); label.textContent = t('startOne'); }
    else if (target === 'summit') { label.setAttribute('data-t', 'continueTop'); label.textContent = t('continueTop'); }
    else { label.removeAttribute('data-t'); label.textContent = t('continue', { n: target }); }
    marks(label);
    paintMaps(s);
  }
  function paintMaps(s) {
    $$('.mtn').forEach(function (m) {
      $$('.dot[data-camp]', m).forEach(function (g) {
        var rec = s.camps[g.getAttribute('data-camp')];
        var f = $('.dflag', g);
        if (f) f.setAttribute('class', 'dflag' + (rec ? (isGold(rec) ? ' gold' : ' plain') : ''));
        // the mini-map shows the climb so far: a camp takes its colour once reached, or while you are in it
        if (m.classList.contains('mtn-mini')) {
          var here = run && run.kind === 'camp' && String(run.stage.n) === g.getAttribute('data-camp');
          $('.dot-fill', g).setAttribute('fill', rec || here ? g.getAttribute('data-color') : D.grey);
        }
      });
      $$('.seg', m).forEach(function (p) {
        p.setAttribute('stroke', s.camps[p.getAttribute('data-seg')] ? p.getAttribute('data-color') : D.grey);
      });
    });
  }
  function light(n, on) {
    $$('.pick[data-camp="' + n + '"], .mtn .dot[data-camp="' + n + '"]').forEach(function (el) { el.classList.toggle('lit', on); });
  }

  // ── the climb ────────────────────────────────────────────────────────────────
  /* run: one camp (or the summit push) under way. run.cur is the line on screen, kept whole
     (its option order, whether it has come back, what was answered), so a language change
     or a resize draws the same line again instead of dealing a new one. */
  var run = null, view = 'start', shownAlt = 0, altTimer = 0, lastPick = null, sceneOf = null;
  var CLICK_GAP = 350;   // ms: a click this soon after a line appears is the tail of a double-click

  function stageOf(target) { return target === 'summit' ? SUMMIT : byN(target); }
  function tenseOf(it) { return TENSES[String(it.camp)]; }
  function campColours(n) {
    var tn = TENSES[String(n)];
    return tn ? '--c:' + tn.fill + ';--k:' + tn.ink + ';--d:' + tn.deep + ';--m:' + tn.mark : '';
  }
  function setView(v) {
    view = v;
    $('#play').setAttribute('data-view', v === 'q' && run && run.cur ? 'q-' + run.items[run.cur.idx].kind : v);
    paintKeys();
  }
  function paintKeys() {
    var k = $('#keys');
    if (!k) return;
    var key = view === 'q' ? (run && run.cur && run.items[run.cur.idx].kind === 'type' ? 'keysType' : 'keys') : 'keysMove';
    k.textContent = t(key); marks(k);
  }
  function setSide(side) { $('#play').setAttribute('data-side', side === 'left' ? 'left' : 'right'); }

  function enter() {
    if (!body.classList.contains('playing')) {
      body.classList.add('playing');
      $('#play').setAttribute('aria-hidden', 'false');
      ['#start', '#wordmark', '.up-link'].forEach(function (s) { var el = $(s); if (el) el.inert = true; });
      $('#utils-slot').appendChild($('#util'));
    }
  }
  function leave() {
    if (!body.classList.contains('playing')) return;
    var dlg = $('#rv'); if (dlg && dlg.open) dlg.close();
    run = null; view = 'start'; sceneOf = null;
    body.classList.remove('playing');
    $('#play').setAttribute('aria-hidden', 'true');
    $('#play').removeAttribute('data-view');
    /*@game:descent*/
    $('#play').removeAttribute('data-storm');
    /*@game:end*/
    ['#start', '#wordmark', '.up-link'].forEach(function (s) { var el = $(s); if (el) el.inert = false; });
    $('.wm-right').appendChild($('#util'));
    $('#view').innerHTML = ''; $('#fb').innerHTML = '';
    if (location.hash) try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
    paintStart();
    var back = lastPick && $('.pick[data-camp="' + lastPick + '"]');
    (back || $('#go')).focus({ preventScroll: false });
  }

  function play(target) {
    var stage = stageOf(target);
    if (!stage) return;
    lastPick = target;
    var s = load();
    s.last = target; put(s);
    run = { target: target, stage: stage, kind: target === 'summit' ? 'summit' : 'camp',
            items: stage.items, queue: stage.items.map(function (_, i) { return i; }),
            first: {}, right: {}, missed: {}, seen: {}, cur: null };
    enter();
    sceneOf = stage;
    /*@game:descent*/
    $('#play').setAttribute('data-storm', String(stage.storm || 0));   // the snow, 0-3 (descent.css)
    /*@game:end*/
    setScene(sceneSrc(stage));
    setSide(stage.side);
    var nx = run.kind === 'camp' ? after(stage.n) : null;
    preload(nx === 'summit' ? SUMMIT : nx != null ? byN(nx) : null);
    paintBar();
    setAlt(altNow(), true);
    paintMini(true);
    showArrive();
  }

  function chipText() {
    if (!run) return '';
    if (view === 'summit') return t('summitH');
    return run.kind === 'camp' ? t('campN', { n: run.stage.n }) + ' · ' + TENSES[String(run.stage.n)].name : t('summitPush');
  }
  function paintBar() {
    if (!run) return;
    var style = run.kind === 'camp' && view !== 'summit' ? campColours(run.stage.n) : '';
    $$('.pb-chip').forEach(function (chip) { chip.setAttribute('style', style); chip.textContent = chipText(); });
    var k = Object.keys(run.right).length;
    var html = run.items.map(function (it, i) {
      var on = view === 'summit' || run.right[it.id];
      var now = view === 'q' && run.cur && run.cur.idx === i;
      var miss = !on && run.missed[it.id];
      var tn = tenseOf(it);
      return '<li class="' + [on ? 'on' : '', now ? 'now' : '', miss ? 'miss' : ''].join(' ').trim() + '" style="--c:' + (tn ? tn.fill : 'var(--ink)') + '"></li>';
    }).join('');
    $$('.pips').forEach(function (pips) {
      pips.setAttribute('aria-label', t('progress', { k: view === 'summit' ? run.items.length : k, m: run.items.length }));
      pips.innerHTML = html;
    });
  }

  function altNow() {
    if (!run) return 0;
    if (view === 'summit') return SUMMIT ? SUMMIT.nextAlt : run.stage.nextAlt;
    var st = run.stage, f = Object.keys(run.right).length / run.items.length;
    return Math.round(st.alt + f * (st.nextAlt - st.alt));
  }
  function setAlt(v, now) {
    var el = $('#alt');
    cancelAnimationFrame(altTimer);
    if (now || RM.matches) { shownAlt = v; el.textContent = fmt(v); return; }
    var from = shownAlt, t0 = performance.now(), dur = 900;
    (function step(ts) {
      var p = Math.min(1, Math.max(0, (ts - t0) / dur)), e = 1 - Math.pow(1 - p, 3);
      shownAlt = Math.round(from + (v - from) * e);
      el.textContent = fmt(shownAlt);
      if (p < 1) altTimer = requestAnimationFrame(step);
    })(t0);
  }

  /*@game:descent*/
  /* The point a fraction f of the way along a polyline, by length: the descent's legs bend
     through the camps that have no passive, so the climber follows the route, not a chord. */
  function along(pts, f) {
    var len = 0, i, seg = [];
    for (i = 1; i < pts.length; i++) { seg.push(Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1])); len += seg[i - 1]; }
    var d = Math.max(0, Math.min(1, f)) * len;
    for (i = 0; i < seg.length; i++) {
      if (d <= seg[i] || i === seg.length - 1) {
        var k = seg[i] ? Math.min(1, d / seg[i]) : 0;
        return [pts[i][0] + (pts[i + 1][0] - pts[i][0]) * k, pts[i][1] + (pts[i + 1][1] - pts[i][1]) * k];
      }
      d -= seg[i];
    }
    return pts[0];
  }

  /*@game:end*/
  function paintMini(jump) {
    var m = $('.mtn-mini');
    if (!m || !run) return;
    paintMaps(load());
    var here = run.kind === 'camp' ? D.dots[String(run.stage.n)] : D.dots[String(D.lastRoute)];
    var n = run.kind === 'camp' ? run.stage.n : null;
    /*@game:climb*/
    var to = run.kind === 'summit' || n === D.lastRoute ? D.peak : D.dots[String(n + 1)] || here;
    var f = view === 'summit' ? 1 : Object.keys(run.right).length / run.items.length;
    var x = here[0] + (to[0] - here[0]) * f, y = here[1] + (to[1] - here[1]) * f;
    /*@game:descent*/
    var f = view === 'summit' ? 1 : Object.keys(run.right).length / run.items.length;
    var p = along(D.legs[run.kind === 'camp' ? String(n) : 'summit'], f), x = p[0], y = p[1];
    /*@game:end*/
    var c = $('#climber');
    if (jump) { c.style.transition = 'none'; c.getBoundingClientRect(); }
    c.style.transform = 'translate(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px)';
    if (jump) { c.getBoundingClientRect(); c.style.transition = ''; }
    var p = $('.pulse', m);
    var at = run.kind === 'summit' ? D.peak : here;
    p.setAttribute('cx', at[0]); p.setAttribute('cy', at[1]);
    p.setAttribute('class', 'pulse on');
  }

  function viaHtml(via) { return via ? ' <span class="via">· ' + pair(D.via[via]) + '</span>' : ''; }
  function lineHtml(ln) {
    return '<li class="line">' + fig(ln.who) + '<div><p class="who">' + esc(D.cast[ln.who].name) + viaHtml(ln.via) + '</p>' +
      '<p class="en">' + pair(ln.en) + '</p></div></li>';
  }

  function showArrive(keepFocus) {
    setView('arrive');
    if (!keepFocus) newCard();
    var st = run.stage, camp = run.kind === 'camp';
    var tn = camp ? TENSES[String(st.n)] : null;
    var html = '<div class="v-arrive" style="' + (camp ? campColours(st.n) : '') + '">' +
      '<div class="c-top"><p class="k">' + esc(camp ? t('campAlt', { n: st.n, alt: fmt(st.alt) }) : t('summitAlt', { alt: fmt(st.alt) })) + '</p>' +
      togHtml() + '</div>' +
      '<h2 class="tense">' + esc(camp ? tn.name : t('summitPush')) + '</h2>' +
      '<p class="tip">' + pair(st.tip, true) + '</p>' +
      '<ul class="lines">' + (st.arrive || []).map(lineHtml).join('') + '</ul>' +
      '<div class="acts"><button class="btn btn-main" id="begin" type="button">' + esc(t('start')) + ' <span aria-hidden="true">&rarr;</span></button>' +
      (camp ? '<a class="read" href="' + esc(tn.href) + '">' + esc(t('readFirst', { n: st.n })) + '</a>' : '') + '</div></div>';
    render(html);
    paintBar();
    $('#begin').addEventListener('click', begin);
    if (!keepFocus) focusCard($('#begin'));
  }
  function begin() { if (run && view === 'arrive') showItem(); }

  function shuffled(a) {   // Fisher-Yates: never sort(() => Math.random() - .5)
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var x = a[i]; a[i] = a[j]; a[j] = x; }
    return a;
  }

  /* The next line in the queue becomes run.cur, dealt once: its option order and whether it
     has come back are fixed here, and renderQ() only ever draws them. */
  function showItem() {
    var idx = run.queue[0], it = run.items[idx];
    run.cur = { idx: idx, back: !!run.seen[it.id], order: it.kind === 'type' ? null : shuffled(it.options),
                typed: '', answered: false, ok: null, val: null, at: 0, shownAt: Date.now() };
    run.seen[it.id] = true;
    newCard();
    renderQ(true);
  }

  function renderQ(focus) {
    var cur = run.cur, it = run.items[cur.idx];
    setView('q');
    var ask = it.kind === 'spot' ? t('askSpot') : it.kind === 'type' ? t('askType') : t(it.gaps === 2 ? 'askChoose2' : 'askChoose');
    // no tense name before the answer: at the summit push it would be the key
    var top = '<div class="q-top">' + fig(it.who) + '<span class="q-who">' + esc(D.cast[it.who].name) + viaHtml(it.via) + '</span>' +
      (cur.back ? '<span class="again">' + esc(t('again')) + '</span>' : '') + togHtml() + '</div>';
    var ctl = '';
    if (it.kind === 'type') {
      ctl = '<form class="typer" id="typer" autocomplete="off"><input id="typed" type="text" autocapitalize="off" autocorrect="off" ' +
        'autocomplete="off" spellcheck="false" enterkeyhint="done" aria-label="' + esc(t('typeAria')) + '" placeholder="' + esc(t('typeHint')) + '">' +
        '<button class="btn btn-main" type="submit">' + esc(t('check')) + '</button></form>';
    } else {
      ctl = '<div class="opts" lang="en">' + cur.order.map(function (o, i) {
        if (it.kind === 'spot') {
          var ot = TENSES[String(o)];
          return '<button class="opt tense-opt" type="button" data-v="' + o + '" style="--c:' + ot.fill + ';--k:' + ot.ink + '">' +
            '<kbd>' + (i + 1) + '</kbd><span>' + esc(ot.name) + '</span><span class="mk" aria-hidden="true"></span></button>';
        }
        return '<button class="opt" type="button" data-v="' + esc(o).replace(/"/g, '&quot;') + '"><kbd>' + (i + 1) + '</kbd><span>' + esc(o) +
          '</span><span class="mk" aria-hidden="true"></span></button>';
      }).join('') + '</div>';
    }
    var html = '<div class="v-q" data-id="' + esc(it.id) + '" data-kind="' + it.kind + '" style="' + campColours(it.camp) + '">' + top +
      '<p class="q-ask">' + esc(ask) + '</p><p class="q-line" lang="en">' + it.q + '</p>' + ctl + '</div>';
    render(html);
    $$('#view .gap').forEach(function (g) { g.innerHTML = '<span class="sr-only">' + esc(t('gap')) + '</span>'; });
    if (it.kind === 'type') {
      var inp = $('#typed');
      inp.value = cur.answered ? cur.val : cur.typed;
      inp.addEventListener('input', function () { if (!cur.answered) cur.typed = inp.value; });
      $('#typer').addEventListener('submit', function (e) {
        e.preventDefault();
        var v = inp.value;
        if (!v.trim()) { inp.focus(); return; }
        answer(v);
      });
    } else {
      $$('#view .opt').forEach(function (b) {
        b.addEventListener('click', function (e) {
          // the second click of a double-click on "Next" (or "Start") lands here: not an answer
          if (e.detail > 1 || Date.now() - cur.shownAt < CLICK_GAP) return;
          answer(b.getAttribute('data-v'), b);
        });
      });
    }
    if (cur.answered) paintAnswered(false);
    else if (focus) focusCard(it.kind === 'type' && !COARSE.matches ? $('#typed') : null);
    paintBar();
  }

  function svgMark(ok) {
    return ok ? '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="9" fill="currentColor"/><path d="M6 10.5l2.6 2.6L14.2 7.4" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
      : '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="9" fill="currentColor"/><path d="M7 7l6 6M13 7l-6 6" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/></svg>';
  }

  function answer(val, btn) {
    if (!run || view !== 'q' || !run.cur || run.cur.answered) return;
    var cur = run.cur, it = run.items[cur.idx];
    var ok = it.kind === 'type' ? accepts(val, it.accept) : String(val) === String(it.answer);
    cur.answered = true; cur.ok = ok; cur.val = String(val); cur.at = Date.now();
    if (!(it.id in run.first)) {
      run.first[it.id] = ok;
      var s = load();
      if (ok) delete s.misses[it.id]; else s.misses[it.id] = true;
      put(s);
    }
    if (ok) { run.right[it.id] = true; run.queue.shift(); }
    else { run.missed[it.id] = true; run.queue.push(run.queue.shift()); }
    beep(ok);
    paintAnswered(true);
    paintBar();
    if (ok) { setAlt(altNow()); paintMini(false); }
  }

  /* The answered line: the sentence put right in place (the answer in bold, the cue gone),
     the option you chose and the right one (the others go: they were only in the way), then
     the verdict, the reason and "Next". Nothing advances by itself. */
  function paintAnswered(fresh) {
    var cur = run.cur, it = run.items[cur.idx], ok = cur.ok;
    var v = $('#view .v-q');
    v.classList.add('answered');
    $('#view .q-line').innerHTML = it.fixed;
    if (it.kind === 'type') {
      var inp = $('#typed');
      inp.value = cur.val; inp.readOnly = true; inp.classList.add(ok ? 'right' : 'wrong');
      $('#typer').classList.add('done');
    } else {
      $$('#view .opt').forEach(function (b) {
        var bv = b.getAttribute('data-v'), isKey = bv === String(it.answer), mine = bv === cur.val;
        b.disabled = true;
        if (isKey) { b.classList.add('right'); $('.mk', b).textContent = '✓'; }
        else if (mine) { b.classList.add('wrong'); $('.mk', b).textContent = '✗'; }
        else b.classList.add('out');
      });
    }
    var tn = tenseOf(it);
    var chip = run.kind === 'summit' && tn ? '<span class="tchip" style="' + campColours(it.camp) + '">' + esc(tn.name) + '</span>' : '';
    $('#fb').innerHTML =
      '<p class="verdict ' + (ok ? 'good' : 'bad') + '">' + svgMark(ok) + '<span class="vt">' + esc(t(ok ? 'right' : 'wrong')) + '</span>' + chip + '</p>' +
      (ok ? '' : '<p class="more">' + esc(t('wrongMore')) + '</p>') +
      '<p class="sr-only" lang="en">' + it.fixed + '</p>' +
      '<p class="why">' + pair(it.fb, true) + '</p>' +
      '<div class="acts"><button class="btn btn-main next" id="next" type="button">' + esc(t('next')) + ' <span aria-hidden="true">&rarr;</span></button></div>';
    marks($('#fb .verdict .vt')); marks($('#fb .more') || document.createElement('i'));
    $('#next').addEventListener('click', function (e) { if (e.detail > 1) return; next(); });
    if (fresh) $('#next').focus({ preventScroll: true });
    fit();
    keepNextInView();
  }
  // the card does not scroll by design (test_climb.js measures it); if a screen is too small
  // for that, "Next" is still brought into view
  function keepNextInView() {
    var n = $('#next'), card = $('#card');
    if (!n || !card) return;
    var r = n.getBoundingClientRect(), cr = card.getBoundingClientRect();
    if (r.bottom > cr.bottom - 4) card.scrollTop += r.bottom - cr.bottom + 16;
  }

  function next() {
    if (!run || view !== 'q' || !run.cur || !run.cur.answered) return;
    if (Date.now() - run.cur.at < CLICK_GAP) return;   // the Enter or click that answered is not also a Next
    if (!run.queue.length) return complete();
    showItem();
  }

  function complete() {
    var total = run.items.length, k = firstRight();
    var s = load();
    if (run.kind === 'camp') {
      var n = String(run.stage.n), rec = s.camps[n] || { best: 0, total: total, gold: false, plays: 0 };
      rec.best = Math.max(rec.best || 0, k); rec.total = total;
      rec.gold = !!rec.gold || rec.best / total >= .75;
      rec.plays = (rec.plays || 0) + 1;
      s.camps[n] = rec;
    } else {
      var sr = s.summit || { best: 0, total: total, plays: 0 };
      s.summit = { best: Math.max(sr.best || 0, k), total: total, plays: (sr.plays || 0) + 1 };
    }
    put(s);
    run.cur = null;
    if (run.kind === 'summit') { run.top = 1; return showTop(); }
    showDone();
  }
  function firstRight() { return run.items.filter(function (it) { return run.first[it.id]; }).length; }

  function showDone(keepFocus) {
    setView('done');
    if (!keepFocus) newCard();
    var st = run.stage, total = run.items.length, k = firstRight(), gold = k / total >= .75;
    var nx = after(st.n);
    var html = '<div class="v-done" style="' + campColours(st.n) + '">' +
      '<div class="reached">' + flagSvg(gold, t(gold ? 'flagGold' : 'flagPlain')) + '<h2>' + esc(t('reached', { n: st.n })) + '</h2>' + togHtml() + '</div>' +
      '<p class="score">' + esc(t('firstTry', { k: k, m: total })) + '</p>' +
      '<p class="goldline">' + esc(t(gold ? 'goldYes' : 'goldNo')) + '</p>' +
      (st.done ? '<ul class="lines">' + lineHtml(st.done) + '</ul>' : '') +
      '<div class="acts">' +
      (nx != null ? '<button class="btn btn-main" id="onward" type="button">' + esc(nx === 'summit' ? t('onTop') : t('onTo', { n: nx })) + ' <span aria-hidden="true">&rarr;</span></button>' : '') +
      '<button class="btn ' + (nx != null ? 'btn-ghost' : 'btn-main') + '" id="tocamps" type="button">' + esc(t('camps')) + '</button></div></div>';
    render(html);
    if ($('#onward')) $('#onward').addEventListener('click', function (e) { if (e.detail > 1) return; play(nx); });
    $('#tocamps').addEventListener('click', leave);
    paintBar(); setAlt(altNow(), !!keepFocus); paintMini(false);
    if (!keepFocus) focusCard($('#onward') || $('#tocamps'));
  }

  /* The summit, in two steps, each a card that fits on its own. Step one is the end of the
     story: the push's last line and the ending, and "See your climb". Step two is the
     climb: the stats, the way on, and the lines missed first time counted per camp. Those
     lines themselves open in a dialog (the route map's own), which may scroll: it is a list
     to read, not a game panel. */
  function missedByCamp() {
    var s = load(), groups = {}, order = [];
    Object.keys(s.misses).forEach(function (id) {
      var it = ITEM[id];
      if (!it || !s.misses[id]) return;
      var key = String(it.camp);
      if (!groups[key]) { groups[key] = []; order.push(key); }
      groups[key].push(it);
    });
    order.sort(function (a, b) { return +a - +b; });
    return { groups: groups, order: order };
  }
  function showTop(keepFocus) {
    setView('summit');
    if (!keepFocus) newCard();
    var s = load();
    sceneOf = 'top';
    setScene(sceneSrc('top'));
    /*@game:descent*/
    $('#play').setAttribute('data-storm', String(D.top.storm || 0));
    /*@game:end*/
    setSide(D.top.side);
    setAlt(altNow());
    var lines = (SUMMIT && SUMMIT.done ? [SUMMIT.done] : []).concat(D.outro || []);
    if (run.top !== 2 && lines.length) {
      render('<div class="v-top s1">' +
        '<div class="c-top"><h2 class="tense">' + esc(t('summitH')) + '</h2>' + togHtml() + '</div>' +
        '<ul class="lines">' + lines.map(lineHtml).join('') + '</ul>' +
        '<div class="acts"><button class="btn btn-main" id="seeclimb" type="button">' + esc(t('seeClimb')) +
        ' <span aria-hidden="true">&rarr;</span></button></div></div>');
      paintBar(); paintMini(false);
      // the second click of a double-click on the last "Next" lands here: not a step on
      $('#seeclimb').addEventListener('click', function (e) {
        if (e.detail > 1 || !run || view !== 'summit') return;
        run.top = 2; run.topAt = Date.now();
        showTop();
      });
      if (!keepFocus) focusCard($('#seeclimb'));
      return;
    }
    run.top = 2;
    var golds = CAMPS.filter(function (c) { return isGold(s.camps[c.n]); }).length;
    var sum = 0, tot = 0;
    CAMPS.forEach(function (c) { var r = s.camps[c.n]; if (r) { sum += r.best; tot += r.total; } });
    var m = missedByCamp(), count = 0;
    m.order.forEach(function (key) { count += m.groups[key].length; });
    // the camps with the most to look at again, four at most; the rest are a count, and
    // every line is in the dialog
    var most = m.order.slice().sort(function (a, b) { return m.groups[b].length - m.groups[a].length || +a - +b; });
    var shown = most.slice(0, 4);
    var review = m.order.length
      ? '<div class="rv-row"><ul class="rv-chips">' + shown.map(function (key) {
          return '<li style="' + campColours(key) + '">' + esc(t('rvChip', { n: key, k: m.groups[key].length })) + '</li>';
        }).join('') + (most.length > shown.length ? '<li class="rv-more">+' + (most.length - shown.length) + '</li>' : '') +
        '</ul><button class="btn btn-ghost rv-open" id="rv-open" type="button">' + esc(t('rvOpen')) +
        ' <span class="rv-n">' + count + '</span></button></div>'
      : '<p class="rv-none">' + esc(t('reviewNone')) + '</p>';
    // two halves: the scores and the way on, then the review (side by side on a phone on
    // its side, one under the other elsewhere)
    var html = '<div class="v-top s2"><div class="t2-a">' +
      '<h2 class="tense">' + esc(t(lines.length ? 'yourClimb' : 'summitH')) + '</h2>' +
      '<p class="stats"><span>' + esc(t('goldCount', { x: golds, m: CAMPS.length })) + '</span>' +
      (tot ? '<span>' + esc(t('overall', { p: Math.round(100 * sum / tot) })) + '</span>' : '') + '</p>' +
      '<div class="acts"><button class="btn btn-main" id="again" type="button">' + esc(t('climbAgain')) + '</button>' +
      '<a class="btn btn-ghost" href="sherpa-tensing-route-map.html">' + esc(t('upLink')) + '</a>' +
      '<a class="read" href="/*@game:climb*/sherpa-tensing-the-descent.html/*@game:descent*/sherpa-tensing-the-climb.html/*@game:end*/">' + esc(t('wayDown')) + ' <span aria-hidden="true">&rarr;</span></a></div>' +
      '</div><div class="t2-b"><h3 class="rv-h">' + esc(t('review')) + '</h3>' + review + '</div></div>';
    render(html);
    paintBar(); paintMini(false);
    $('#again').addEventListener('click', function (e) {
      // the Enter or the second click that took you to this step is not also "Climb again":
      // it would clear the lines to look at again before you had seen them
      if (e.detail > 1 || Date.now() - (run.topAt || 0) < CLICK_GAP) return;
      var s2 = load(); s2.misses = {}; s2.last = null; put(s2);
      if (CAMPS[0]) play(CAMPS[0].n);
    });
    if ($('#rv-open')) $('#rv-open').addEventListener('click', openReview);
    var dlg = $('#rv');
    if (dlg && dlg.open) fillReview();
    if (!keepFocus) focusCard($('#again'));
  }
  function fillReview() {
    var m = missedByCamp();
    $('#rv-h').textContent = t('review'); marks($('#rv-h'));
    $('#rv-x').setAttribute('aria-label', t('close'));
    $('#rv-close').textContent = t('close'); marks($('#rv-close'));
    $('#rv-list').innerHTML = m.order.map(function (key) {
      var tn = TENSES[key];
      return '<li class="rv-g" style="' + campColours(key) + '"><p class="rv-t">' + esc(t('campN', { n: key }) + ' · ' + tn.name) + '</p>' +
        m.groups[key].map(function (it) { return '<p lang="en">' + it.fixed + '</p>'; }).join('') + '</li>';
    }).join('');
  }
  function openReview() {
    var dlg = $('#rv');
    if (!dlg) return;
    fillReview();
    if (typeof dlg.showModal === 'function') { if (!dlg.open) dlg.showModal(); }
    else dlg.setAttribute('open', '');
  }

  function render(html) {
    $('#fb').innerHTML = '';
    $('#view').innerHTML = html;
    $('#card').scrollTop = 0;
    fit();
  }
  /* Innes: "NO scrolling" in a game panel. The card is laid out to fit every screen down to
     a phone on its side; if a long line still makes it taller than the screen, it tightens
     a step at a time (fit1: spacing, no portraits; fit2: "Next" beside the verdict, the
     right option only in the sentence; fit3: a size smaller) until it fits.
     In a learner's language the glosses beneath the English come first: they give way only
     when the tightest step still does not fit (never one that fits). Then fitG hides them
     and shows the card's "Translation" toggle, and the ladder is climbed again from the
     bottom, for the first step at which the card fits with the English AND with the
     translations in its place (gsw), so pressing the toggle moves nothing. */
  var FITS = ['fit1', 'fit2', 'fit3', 'fit4'];   // fit4: the last resort, a German translation swapped in on a phone on its side
  function fit() {
    var card = $('#card');
    if (!card || !body.classList.contains('playing')) return;
    function step(k, g, sw) {
      FITS.forEach(function (c, i) { card.classList.toggle(c, i < k); });
      card.classList.toggle('fitG', g);
      card.classList.toggle('gsw', g && sw);
    }
    function over() { return card.scrollHeight > card.clientHeight + 1; }
    var k;
    for (k = 0; k <= FITS.length; k++) { step(k, false, false); if (!over()) return paintTog(); }
    var glossed = $$('.gl', card).some(function (g) { return g.textContent.trim(); });
    if (!glossed) return paintTog();     // nothing to give way: the tightest step (keepNextInView)
    for (k = 0; k <= FITS.length; k++) {
      step(k, true, true);
      if (over()) continue;
      step(k, true, false);
      if (!over()) break;
    }
    step(Math.min(k, FITS.length), true, gsw.on);
    paintTog();
  }
  function paintTog() {
    var b = $('#gtog');
    if (b) b.setAttribute('aria-pressed', String(gsw.on));
  }
  function toggleGloss() {
    gsw.on = !gsw.on;
    fit();
    if (run && view === 'q' && run.cur && run.cur.answered) keepNextInView();
  }
  function focusCard(el) {
    var target = el || $('#card');
    try { target.focus({ preventScroll: true }); } catch (e) { target.focus(); }
  }

  // ── language ─────────────────────────────────────────────────────────────────
  function stored() { try { return localStorage.getItem(LKEY); } catch (e) { return null; } }
  function initialLang() {
    var q = (location.search.match(/[?&]lang=([a-z]{2})\b/) || [])[1];
    if (q && I.langs.indexOf(q) >= 0) return q;
    var s = stored();
    return I.langs.indexOf(s) >= 0 ? s : 'en';
  }
  var tagline = null;
  function applyLang(l) {
    lang = I.langs.indexOf(l) >= 0 ? l : 'en';
    document.documentElement.lang = lang;
    $$('[data-t]').forEach(function (el) { el.textContent = t(el.getAttribute('data-t')); marks(el); });
    $$('[data-t-aria]').forEach(function (el) { el.setAttribute('aria-label', t(el.getAttribute('data-t-aria'))); });
    $$('[data-gl]').forEach(function (el) {
      var g = gloss(el.getAttribute('data-gl'));
      el.innerHTML = g ? rich(g) : '';
      if (g) marks(el);
    });
    // the tagline stays byte-exact in the source (tools/sherpa_links.py); swap its words here
    var sub = $('.wordmark .sub');
    if (sub) {
      if (!tagline) { var n = sub.lastChild; if (n && n.nodeType === 3) tagline = n; }
      if (tagline) tagline.nodeValue = ' · ' + t('tagline');
    }
    var sel = $('#lang'); if (sel) sel.value = lang;
    paintSound();
    paintStart();
    paintKeys();
    if (run) {
      // the same view again, in the new language: the same line, its options in the same
      // order, what was typed, the answer if one was given. The focus stays on the menu
      if (view === 'arrive') showArrive(true);
      else if (view === 'done') showDone(true);
      else if (view === 'summit') showTop(true);
      else if (view === 'q' && run.cur) renderQ(false);
      paintBar();
      setAlt(altNow(), true);
    }
  }

  // ── wiring ───────────────────────────────────────────────────────────────────
  $('#go').addEventListener('click', function () {
    var tgt = this.getAttribute('data-target');
    play(tgt === 'summit' ? 'summit' : +tgt);
  });
  $$('.pick[data-camp]').forEach(function (b) {
    var n = b.getAttribute('data-camp');
    b.addEventListener('click', function () { play(n === 'summit' ? 'summit' : +n); });
    b.addEventListener('mouseenter', function () { light(n, true); });
    b.addEventListener('mouseleave', function () { light(n, false); });
    b.addEventListener('focus', function () { light(n, true); });
    b.addEventListener('blur', function () { light(n, false); });
  });
  $$('.mtn:not(.mtn-mini) .dot[data-camp]:not(.soon)').forEach(function (g) {
    var n = g.getAttribute('data-camp');
    g.addEventListener('click', function () { if (byN(n)) play(+n); });
    g.addEventListener('mouseenter', function () { light(n, true); });
    g.addEventListener('mouseleave', function () { light(n, false); });
  });
  var more = $('.brief-more');
  if (more) more.addEventListener('click', function () {
    var open = $('#brief').classList.toggle('open');
    more.setAttribute('aria-expanded', String(open));
  });
  $('#back').addEventListener('click', leave);
  // the card's "Translation" toggle is drawn with each card, so it is caught here
  $('#card').addEventListener('click', function (e) {
    if (e.target && e.target.closest && e.target.closest('#gtog')) toggleGloss();
  });
  $('#snd').addEventListener('click', function () { setSound(!sound); beep(true); });
  $('#lang').addEventListener('change', function () {
    try { localStorage.setItem(LKEY, this.value); } catch (e) {}
    applyLang(this.value);
  });
  (function () {
    var dlg = $('#rv');
    if (!dlg) return;
    dlg.addEventListener('click', function (e) {
      if (e.target !== dlg) return;
      var r = dlg.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
    });
    dlg.addEventListener('close', function () { var o = $('#rv-open'); if (o) o.focus(); });
  })();
  function isControl(el) { return !!(el && el.closest && el.closest('button, a, select, input, textarea')); }
  document.addEventListener('keydown', function (e) {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
    var dlg = $('#rv');
    if (dlg && dlg.open) return;                      // the dialog has its own keys (Esc closes it)
    var tag = (e.target && e.target.tagName) || '';
    var playing = body.classList.contains('playing');
    // Enter held down repeats: in the game that would answer, go on and start again on its
    // own (a held Enter on "See your climb" reached "Climb again"). One press, one step
    if (playing && e.repeat && tag !== 'SELECT' && (e.key === 'Enter' || (e.key === ' ' && tag !== 'INPUT' && tag !== 'TEXTAREA'))) {
      e.preventDefault(); return;
    }
    if (e.key === 'Escape' && playing && tag !== 'SELECT') { e.preventDefault(); leave(); return; }
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
    if (e.key === 's' || e.key === 'S') { setSound(!sound); beep(true); return; }
    if (!playing || !run) return;
    if (view === 'arrive' && e.key === 'Enter' && !isControl(e.target)) { e.preventDefault(); begin(); return; }
    if (view === 'q' && run.cur && !run.cur.answered && /^[1-3]$/.test(e.key)) {
      var b = $$('#view .opt')[+e.key - 1];
      if (b) { e.preventDefault(); answer(b.getAttribute('data-v'), b); }
      return;
    }
    if (view === 'q' && run.cur && run.cur.answered && (e.key === 'Enter' || e.key === ' ') && !isControl(e.target)) { e.preventDefault(); next(); return; }
    if ((view === 'done' || view === 'summit') && e.key === 'Enter' && !isControl(e.target)) {
      var p = $('#view .btn-main'); if (p) { e.preventDefault(); p.click(); }
    }
  });
  // a turned phone or a resized window: the right scene for the width, and "Next" in view
  var resizeT = 0;
  window.addEventListener('resize', function () {
    clearTimeout(resizeT);
    resizeT = setTimeout(function () {
      if (!run) return;
      if (sceneOf) setScene(sceneSrc(sceneOf));
      fit();
      if (view === 'q' && run.cur && run.cur.answered) keepNextInView();
    }, 120);
  });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { if (run) fit(); });
  window.addEventListener('storage', function (e) { if (e.key === SKEY && !run) paintStart(); });
  window.addEventListener('pageshow', function (e) { if (e.persisted && !run) paintStart(); });

  applyLang(initialLang());
  var h = (location.hash.match(/^#(camp-(\d+)|summit)$/) || []);
  if (h[2] && byN(+h[2])) play(+h[2]);
  else if (h[1] === 'summit' && SUMMIT) play('summit');

  // for tests and for a teacher's console: read-only views of the game
  window.SherpaClimb = { canon: { flat: flat, variants: variants, accepts: accepts }, state: function () { return { view: view, run: run }; } };
})();
