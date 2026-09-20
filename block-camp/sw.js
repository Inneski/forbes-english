/* Block Camp: The Quest — service worker.
   Scope is block-camp/ (it is registered from quest.html, which lives there),
   so the worker can only ever answer for the game and the adventures. It is
   network-first: the live page always wins, and the cache is what answers
   when the phone has no signal. A rebuilt adventure therefore reaches the
   learner on the next online visit, and nothing outside block-camp/ is
   touched. Bump VERSION to drop every cached copy. */
const VERSION = 'block-camp-quest-v1';
const CORE = ['quest.html', 'camp-save.js', 'manifest.webmanifest', 'quest-icons/icon-192.png', 'quest-icons/icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return;
  e.respondWith(
    fetch(e.request).then(res => {
      if (res && res.ok && (res.type === 'basic')) {
        const copy = res.clone();
        caches.open(VERSION).then(c => c.put(e.request, copy));
      }
      return res;
    }).catch(() => caches.match(e.request).then(hit => hit || (e.request.mode === 'navigate' ? caches.match('quest.html') : undefined)))
  );
});
