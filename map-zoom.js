/* map-zoom.js: every map on the site can be enlarged.

   Innes, 2026-11-08: "maps need to be expandable always". A page loads this
   file and marks each map:

     <div data-map-zoom data-mz-target=".chart-toggle-wrap" data-mz-ratio="1.5" data-mz-min="1100">

   data-map-zoom   the block that goes full screen (the map plus whatever
                   must stay with it: its toggles, the lists it lights up)
   data-mz-target  selector, inside it, of the element to resize (the map)
   data-mz-ratio   the map's width / height
   data-mz-min     the narrowest the map may be when enlarged, in px; on a
                   phone the enlarged map is wider than the screen and scrolls
   data-mz-btn     optional selector, inside the block, of a toolbar to put
                   the button in (inline, at its end) instead of the block's
                   top-right corner. Use it when the block is taller than a
                   screen, so the button sits right above the map.

   An "Enlarge" button is added to the block's top right. Enlarged, the same
   elements are pinned over the page, so a clickable map stays clickable.
   The map fills the screen height (or width), never smaller than
   data-mz-min. Escape or the close button puts it back.

   Colours come from the page's own tokens (--card, --ink, --accent,
   --on-accent), with system colours as the fallback. */
(function () {
  var CSS =
    '.mz-btn{position:absolute;top:10px;right:10px;z-index:3;display:inline-flex;align-items:center;gap:6px;' +
    'font:600 12.5px/1 Inter,system-ui,sans-serif;letter-spacing:.04em;padding:8px 12px 8px 10px;border-radius:999px;cursor:pointer;' +
    'border:1px solid color-mix(in srgb,var(--ink,CanvasText) 18%,transparent);background:var(--card,Canvas);color:var(--ink,CanvasText);' +
    'box-shadow:0 4px 14px color-mix(in srgb,var(--ink,CanvasText) 18%,transparent);}' +
    '.mz-btn:hover,.mz-btn:focus-visible{background:var(--accent,Highlight);color:var(--on-accent,HighlightText);border-color:transparent;}' +
    '.mz-btn svg{width:16px;height:16px;}' +
    '.mz-btn.mz-inline{position:static;margin-left:auto;}' +
    '[data-map-zoom]{position:relative;}' +
    '.mz-max{position:fixed!important;inset:0!important;z-index:2147483000!important;margin:0!important;max-width:none!important;' +
    'width:auto!important;border-radius:0!important;overflow:auto!important;overscroll-behavior:contain;' +
    'padding:56px 16px 24px!important;background:var(--card,Canvas)!important;}' +
    '.mz-max .mz-btn,.mz-max .mz-btn.mz-inline{position:fixed;top:10px;right:14px;margin:0;}' +
    '.mz-max [data-mz-scroll]{overflow:visible!important;}' +
    '.mz-max .mz-target{margin-left:auto;margin-right:auto;max-width:none!important;flex:none!important;}' +
    'html.mz-lock,html.mz-lock body{overflow:hidden!important;}';
  var ICON_OPEN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  var ICON_SHUT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>';

  function init() {
    var blocks = document.querySelectorAll('[data-map-zoom]');
    if (!blocks.length) return;
    var st = document.createElement('style');
    st.textContent = CSS;
    document.head.appendChild(st);
    var open = null;

    function size(b) {
      var t = b.querySelector(b.dataset.mzTarget);
      if (!t) return;
      var ratio = parseFloat(b.dataset.mzRatio) || 1.5;
      var min = parseFloat(b.dataset.mzMin) || 0;
      var fit = Math.min(window.innerWidth - 32, (window.innerHeight - 80) * ratio);
      t.style.width = Math.round(Math.max(fit, min)) + 'px';
    }
    function shut() {
      if (!open) return;
      var b = open, t = b.querySelector(b.dataset.mzTarget);
      open = null;
      b.classList.remove('mz-max');
      document.documentElement.classList.remove('mz-lock');
      if (t) { t.style.width = ''; t.classList.remove('mz-target'); }
      var btn = b.querySelector('.mz-btn');
      btn.innerHTML = ICON_OPEN + 'Enlarge';
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-label', 'Enlarge the map');
      btn.focus();
    }
    blocks.forEach(function (b) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'mz-btn';
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-label', 'Enlarge the map');
      btn.innerHTML = ICON_OPEN + 'Enlarge';
      var bar = b.dataset.mzBtn && b.querySelector(b.dataset.mzBtn);
      if (bar) { btn.classList.add('mz-inline'); bar.appendChild(btn); } else b.appendChild(btn);
      btn.addEventListener('click', function () {
        if (open === b) return shut();
        shut();
        open = b;
        var t = b.querySelector(b.dataset.mzTarget);
        if (t) t.classList.add('mz-target');
        b.classList.add('mz-max');
        document.documentElement.classList.add('mz-lock');
        size(b);
        btn.innerHTML = ICON_SHUT + 'Close';
        btn.setAttribute('aria-expanded', 'true');
        btn.setAttribute('aria-label', 'Close the enlarged map');
        b.scrollTop = 0;
        b.scrollLeft = (b.scrollWidth - b.clientWidth) / 2;
      });
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && open) shut(); });
    window.addEventListener('resize', function () { if (open) size(open); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
