/* Block Camp: The Quest — service worker.
   Scope is block-camp/ (it is registered from quest.html, which lives there),
   so the worker can only ever answer for the game, the village and the
   adventures. It is network-first: the live page always wins, and the cache
   is what answers when the phone has no signal. A rebuilt adventure therefore
   reaches the learner on the next online visit, and nothing outside
   block-camp/ is touched. Bump VERSION to drop every cached copy.

   v2 (2026-10-02): the live Worker 307s every *.html to its clean URL, so a
   precached 'quest.html' came back with redirected=true, and a redirected
   response may not answer a navigation: the installed app's offline launch
   (start_url quest.html) failed with ERR_FAILED. Every copy is now stored as
   a plain response, and an offline navigation tries the clean and the .html
   spelling of the URL before falling back to the Quest.

   v3 (2026-10-02): quest.html loads camp-flags.js?v=2 (the Lookout stat), so
   it is precached with the rest; without it an installed Quest opened
   offline before an online visit showed "Lookout ->" with no count. */
const VERSION = 'block-camp-quest-v3';
// Must all load, or the worker does not install.
const CORE = ['quest.html', 'camp-save.js', 'manifest.webmanifest', 'quest-icons/icon-192.png', 'quest-icons/icon-512.png'];
// Nice to have offline; one missing does not stop the rest.
const EXTRA = ['camp-flags.js?v=2', 'camp-full.js', 'village.html', '../BlockCamp/hub-hero.jpg'];

// A response that followed a redirect, rebuilt as a plain one with the same
// status, headers and bytes (a blob, which every engine accepts as a body).
function plain(res) {
  if (!res.redirected) return Promise.resolve(res);
  return res.blob().then(b => new Response(b, { status: res.status, statusText: res.statusText, headers: res.headers }));
}
function store(c, key, res) { return plain(res).then(p => c.put(key, p)); }

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c =>
    Promise.all(CORE.map(u => fetch(u, { cache: 'reload' }).then(r => { if (!r.ok) throw new Error(u + ' ' + r.status); return store(c, u, r); })))
      .then(() => Promise.all(EXTRA.map(u => fetch(u, { cache: 'reload' }).then(r => r.ok ? store(c, u, r) : null).catch(() => null))))
  ).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

// The other spelling of a page's URL: /x.html <-> /x (the Worker's clean URL).
function twin(url) {
  const u = new URL(url); u.search = ''; u.hash = '';
  if (/\.html$/.test(u.pathname)) u.pathname = u.pathname.replace(/\.html$/, '');
  else if (!u.pathname.endsWith('/')) u.pathname += '.html';
  else return null;
  return u.href;
}
function offline(req) {
  const nav = req.mode === 'navigate';
  return caches.match(req, { ignoreSearch: nav }).then(hit => {
    if (hit || !nav) return hit;
    const t = twin(req.url);
    return (t ? caches.match(t) : Promise.resolve(null)).then(h => h || caches.match('quest.html'));
  });
}

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return;
  e.respondWith(
    fetch(e.request).then(res => {
      if (res && res.ok && res.type === 'basic') {
        const copy = res.clone();
        e.waitUntil(caches.open(VERSION).then(c => store(c, e.request, copy)).catch(() => {}));
      }
      return res;
    }).catch(() => offline(e.request).then(hit => hit || Response.error()))
  );
});
