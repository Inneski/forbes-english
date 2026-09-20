/* Block Camp save file.
   One localStorage record shared by every camp page: the RPGs write a result
   at each ending, the tense decks write how far the learner paged, and the
   overworld (block-camp/quest.html) reads all of it back as a game.

   The engine (lesson-template/build/rpg/rpg.py) inlines this file into every
   RPG it builds, so a page stays one self-contained file; the hand-built
   adventures and the decks load it with <script src>. Either way the API is
   window.CampSave and every call is guarded — a browser with storage blocked
   just plays the lesson as before.

   Page ids are the file name without .html, so an RPG is 'lost-yellow-road-rpg'
   and a deck is 'blockcamp-past-simple'. The overworld maps those ids onto
   camps with the same tables the hub builder uses.

   Format (v1):
     { v:1, name:'', created, updated, last:{id,href,title,kind,at},
       rpg:  { id: { plays, last, parts: { chapter: {best,max,tiles,tilesMax,cleared,master,endings:{id:n}} } } },
       deck: { id: { plays, seen, total, done, last } } }
   'parts' is keyed by chapter index for a page that holds several games
   (the Kraken saga); every other RPG has one part, keyed '0'. */
(function () {
  var KEY = 'forbes-camp-save', V = 1, MAGIC = 'BLOCKCAMP1:';

  function pageId() {
    var p = (location.pathname || '').split('/').pop() || '';
    try { p = decodeURIComponent(p); } catch (_) {}
    return p.replace(/\.html?$/i, '') || 'index';
  }
  function blank() { return { v: V, name: '', created: Date.now(), updated: Date.now(), last: null, rpg: {}, deck: {} }; }
  function load() {
    try { var s = JSON.parse(localStorage.getItem(KEY) || 'null'); if (s && s.v === V && s.rpg && s.deck) return s; } catch (_) {}
    return blank();
  }
  function store(s) {
    s.updated = Date.now();
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (_) {}
    try { window.dispatchEvent(new CustomEvent('campsave', { detail: s })); } catch (_) {}
    return s;
  }
  function touch(s, kind) {
    s.last = { id: pageId(), href: location.pathname.split('/').pop() || location.href, dir: /\/block-camp\//.test(location.pathname) ? 'block-camp' : '',
               title: (document.title || '').replace(/\s*\|.*$/, ''), kind: kind, at: Date.now() };
  }

  var CampSave = {
    KEY: KEY, id: pageId, load: load,

    /* every camp page calls this once on load: it is what "Continue" points at */
    visit: function (kind) { var s = load(); touch(s, kind || 'page'); return store(s); },

    /* an RPG calls this from its ending scene */
    rpgEnd: function (r) {
      var s = load(), id = pageId(), e = s.rpg[id] || (s.rpg[id] = { plays: 0, parts: {} });
      var k = String(r.chapter == null ? 0 : r.chapter), p = e.parts[k] || (e.parts[k] = { best: 0, max: 0, tiles: 0, tilesMax: 0, cleared: false, master: false, endings: {} });
      e.plays += 1; e.last = Date.now();
      p.max = Math.max(p.max, r.max || 0); p.tilesMax = Math.max(p.tilesMax, r.tilesMax || 0);
      if ((r.score || 0) >= p.best) { p.best = r.score || 0; p.tiles = Math.max(p.tiles, r.tiles || 0); }
      p.tiles = Math.max(p.tiles, r.tiles || 0);
      if (r.cleared) p.cleared = true;
      if (r.master) p.master = true;
      if (r.ending) p.endings[r.ending] = (p.endings[r.ending] || 0) + 1;
      touch(s, 'rpg');
      return store(s);
    },

    /* a deck calls this from show(): how far the learner has paged */
    deck: function (idx, total) {
      var s = load(), id = pageId(), e = s.deck[id] || (s.deck[id] = { plays: 0, seen: 0, total: 0 });
      if (idx === 0 && e.seen === 0) e.plays += 1;
      e.seen = Math.max(e.seen, (idx | 0) + 1); e.total = total | 0; e.done = e.total > 0 && e.seen >= e.total; e.last = Date.now();
      touch(s, 'deck');
      return store(s);
    },

    setName: function (name) { var s = load(); s.name = String(name || '').slice(0, 24); return store(s); },
    reset: function () { try { localStorage.removeItem(KEY); } catch (_) {} return store(blank()); },

    /* a save moves between browsers as one line of text */
    exportText: function () { try { return MAGIC + btoa(unescape(encodeURIComponent(JSON.stringify(load())))); } catch (_) { return ''; } },
    importText: function (t) {
      t = String(t || '').trim(); if (t.indexOf(MAGIC) !== 0) return null;
      try { var s = JSON.parse(decodeURIComponent(escape(atob(t.slice(MAGIC.length))))); if (s && s.v === V && s.rpg && s.deck) return store(s); } catch (_) {}
      return null;
    },

    /* scores every RPG on a common scale, whatever its own point ladder:
       0–100 for the best run, 25 a tile, 50 for clearing it, 50 more for the
       master ending. A deck is 50 read to the end, pro rata before that. */
    rpgXp: function (e) {
      var xp = 0; if (!e) return 0;
      Object.keys(e.parts).forEach(function (k) { var p = e.parts[k];
        xp += p.max ? Math.round(100 * p.best / p.max) : 0; xp += 25 * (p.tiles || 0); if (p.cleared) xp += 50; if (p.master) xp += 50; });
      return xp;
    },
    deckXp: function (e) { if (!e || !e.total) return 0; return e.done ? 50 : Math.round(50 * e.seen / e.total); },
    xp: function (s) {
      s = s || load(); var t = 0, self = this;
      Object.keys(s.rpg).forEach(function (k) { t += self.rpgXp(s.rpg[k]); });
      Object.keys(s.deck).forEach(function (k) { t += self.deckXp(s.deck[k]); });
      return t;
    }
  };
  window.CampSave = CampSave;
})();
