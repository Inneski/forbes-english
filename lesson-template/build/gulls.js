/* Gulls seen from above, flying across a picture.
 *
 * The idea is English Heritage's Myths Map (mythsmap.english-heritage.org.uk):
 * cut-out birds (a body and two wings), wings that beat and then glide, and
 * small flocks that cross the whole picture, leave, and come round again.
 * They drew theirs as PNGs and animated them in After Effects (Lottie); these
 * are drawn in SVG and moved with CSS and the Web Animations API, so there is
 * no library and nothing to download. Seen from directly above, a beating wing
 * does not swing, it foreshortens: raised or lowered, it looks shorter. So the
 * beat is a scaleY about the shoulder, with a little sweep back on the upstroke.
 * A soft shadow a little way below each bird is what reads as height.
 *
 * Shared: the Sailing the Seas hero (build_sailing.py inlines this file) and
 * the illustrated map on folkloreexplorer.com. Keep it dependency-free.
 *
 *   flyGulls(container, {
 *     aspect: 1.5,              // container width / height (the picture's)
 *     size: 4.6,                // bird wingspan, % of container width
 *     seed: 7,                  // for the small per-bird variations
 *     flocks: [{
 *       from: [70, 115], to: [62.5, -15],   // % of the container
 *       flight: 13, cycle: 40,  // seconds crossing; seconds per round
 *       at: 1,                  // where in its cycle the flock is on load (s)
 *       birds: [[0, 0, 1.05], [-1.6, 1.3, .95]]  // [ahead, across, scale],
 *     }],                       //   offsets in wingspans
 *   })
 *
 * from/to are where the LEADER crosses in and out; the route is lengthened
 * so the whole flock, shadows included, is out of the picture at both ends
 * (at the same speed), and a flock waiting for its turn is never seen.
 *
 * The container must be positioned and exactly cover the picture; the birds
 * go in a new child layer, made of spans (a picture inside a <button> may
 * hold only phrasing content), and are clipped to it. Colours come from
 * --gl-paper / --gl-ink if the page sets them, else --paper / --ink.
 * Nothing is drawn for prefers-reduced-motion, or without color-mix().
 */
(function (root) {
  'use strict';

  // One bird, heading +x (right), in a 40 x 40 box centred on 0,0. A gull
  // from above is mostly wing: span about two and a half times its length,
  // an arm that reaches slightly forward to the wrist, then a long narrow hand
  // swept back to a black tip (the M a child draws). A short body, a round
  // head, a small square tail.
  var BODY = 'M6.2,0C6.2,-.9 5.5,-1.3 4.6,-1.3C3.8,-1.3 3.2,-1.1 2.6,-1.5C1.4,-2.2 -1.2,-2.2 -3,-1.6' +
             'L-4.6,-1.2C-5.6,-1.5 -6.8,-1.9 -7.6,-1.7C-7.9,-.6 -7.9,.6 -7.6,1.7C-6.8,1.9 -5.6,1.5 -4.6,1.2' +
             'L-3,1.6C-1.2,2.2 1.4,2.2 2.6,1.5C3.2,1.1 3.8,1.3 4.6,1.3C5.5,1.3 6.2,.9 6.2,0Z';
  var BILL = 'M6.1,-.35L7.9,0L6.1,.35Z';
  // the right wing (+y); the left is the same group mirrored, so one set of
  // keyframes beats both symmetrically. The tip is the outer half of the hand.
  var WING = 'M2.3,1C3.3,3.6 3.9,6.2 3.6,8.4C2.9,12.6 -1,16.6 -4.8,19.8' +
             'C-3.7,16.8 -2.3,13.6 -1.4,11C-1.9,7.8 -2.8,4.4 -2.6,1Z';
  var TIP = 'M.56,14.48C-.98,16.4 -2.9,18.2 -4.8,19.8C-4.25,18.3 -3.63,16.75 -3.03,15.25Z';

  function birdSVG(cls) {
    var wing = '<g class="gw"><path class="w" d="' + WING + '"/><path class="t" d="' + TIP + '"/></g>';
    return '<svg class="' + cls + '" viewBox="-20 -20 40 40" focusable="false">' +
      wing + '<g transform="scale(1,-1)">' + wing + '</g>' +
      '<path class="b" d="' + BODY + '"/><path class="t" d="' + BILL + '"/></svg>';
  }

  var CSS = [
    '.gulls{position:absolute;inset:0;overflow:hidden;pointer-events:none;border-radius:inherit;',
    '  --gl-p:var(--gl-paper,var(--paper));--gl-i:var(--gl-ink,var(--ink));}',
    '.gl-flock{position:absolute;inset:0;will-change:transform;}',
    '.gl-bird{position:absolute;aspect-ratio:1;',
    '  animation:gl-wander var(--wd,8s) ease-in-out var(--wdl,0s) infinite alternate;}',
    '.gl-bird svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible;}',
    '.gl-bird .bd{transform:rotate(var(--hd));}',
    /* the sun is up and to the left, as on the chart: the shadow falls down-right */
    '.gl-bird .sh{transform:translate(30%,38%) rotate(var(--hd));opacity:.22;filter:blur(.7px);}',
    '.gl-bird .b{fill:var(--gl-p);}',
    '.gl-bird .w{fill:color-mix(in srgb,var(--gl-i) 24%,var(--gl-p));}',
    '.gl-bird .t{fill:var(--gl-i);}',
    '.gl-bird .b,.gl-bird .w{stroke:color-mix(in srgb,var(--gl-i) 62%,transparent);stroke-width:.8;stroke-linejoin:round;}',
    '.gl-bird .sh path{fill:var(--gl-i);stroke:none;}',
    '.gl-bird .gw{transform-box:fill-box;transform-origin:50% 0;',
    '  animation:gl-beat var(--fd,3.2s) ease-in-out var(--fdl,0s) infinite;}',
    /* four beats, then a glide: raised (short, swept back), level, lowered, level */
    '@keyframes gl-beat{0%,15%,30%,45%,60%,100%{transform:none}',
    '  5%,20%,35%,50%{transform:rotate(7deg) scaleY(.46)}',
    '  10%,25%,40%,55%{transform:rotate(-3deg) scaleY(.8)}}',
    '@keyframes gl-wander{to{transform:translate(var(--wx,0),var(--wy,0))}}',
    '@media (prefers-reduced-motion:reduce){.gulls{display:none}}',
    '@media print{.gulls{display:none}}',
    '@supports not (color:color-mix(in srgb,red 50%,blue)){.gulls{display:none}}'
  ].join('\n');

  function rng(seed) {                  // small deterministic generator
    var s = (seed >>> 0) || 1;
    return function () { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; };
  }
  function pct(v) { return (Math.round(v * 1000) / 1000) + '%'; }

  function flyGulls(container, opts) {
    opts = opts || {};
    if (!container || !opts.flocks) return null;
    if (root.matchMedia && root.matchMedia('(prefers-reduced-motion: reduce)').matches) return null;
    var doc = container.ownerDocument;
    if (!doc.getElementById('gulls-css')) {
      var st = doc.createElement('style');
      st.id = 'gulls-css';
      st.textContent = CSS;
      doc.head.appendChild(st);
    }
    var aspect = opts.aspect || (container.clientWidth / Math.max(1, container.clientHeight)) || 1.5;
    var size = opts.size || 4.6;
    var rand = rng(opts.seed || 7);
    var bw = size / 100 * aspect;       // wingspan in units where the height is 1

    var layer = doc.createElement('span');
    layer.className = 'gulls';
    layer.setAttribute('aria-hidden', 'true');

    opts.flocks.forEach(function (f) {
      var birds = f.birds || [[0, 0, 1]];
      var dx = (f.to[0] - f.from[0]) / 100 * aspect, dy = (f.to[1] - f.from[1]) / 100;
      var hd = Math.atan2(dy, dx);
      var ux = Math.cos(hd), uy = Math.sin(hd), nx = -uy, ny = ux;
      // A flock is longer than one bird: while it waits for its next crossing
      // no straggler may be left inside the picture. So the route starts far
      // enough back that the leader is out, and ends far enough on that the
      // last bird is out, with a wingspan to spare for size, shadow and
      // wander. The flight time stretches with it, so the speed is as given.
      var ahead = 0, behind = 0;
      birds.forEach(function (b) { ahead = Math.max(ahead, b[0]); behind = Math.max(behind, -b[0]); });
      var len = Math.sqrt(dx * dx + dy * dy);
      var pre = (ahead + 1) * bw, post = (behind + 1) * bw;
      var from = [f.from[0] - pre * ux / aspect * 100, f.from[1] - pre * uy * 100];
      var to = [f.to[0] + post * ux / aspect * 100, f.to[1] + post * uy * 100];
      var flight = f.flight * (len + pre + post) / len;
      var flock = doc.createElement('span');
      flock.className = 'gl-flock';
      flock.style.setProperty('--hd', (hd * 180 / Math.PI).toFixed(2) + 'deg');
      birds.forEach(function (b) {
        var sc = b[2] || 1;
        var ox = (b[0] * ux + b[1] * nx) * bw, oy = (b[0] * uy + b[1] * ny) * bw;
        var w = size * sc;                               // % of the width
        var el = doc.createElement('span');
        el.className = 'gl-bird';
        el.style.width = pct(w);
        el.style.left = pct(ox / aspect * 100 - w / 2);
        el.style.top = pct(oy * 100 - w * aspect / 2);  // square: its height is w% of the width
        el.style.setProperty('--fd', (2.7 + rand() * 0.9).toFixed(2) + 's');
        el.style.setProperty('--fdl', (-rand() * 3).toFixed(2) + 's');
        el.style.setProperty('--wd', (6 + rand() * 4).toFixed(2) + 's');
        el.style.setProperty('--wdl', (-rand() * 8).toFixed(2) + 's');
        el.style.setProperty('--wx', ((rand() - 0.5) * 70).toFixed(0) + '%');
        el.style.setProperty('--wy', ((rand() - 0.5) * 70).toFixed(0) + '%');
        el.innerHTML = birdSVG('sh') + birdSVG('bd');
        flock.appendChild(el);
      });
      layer.appendChild(flock);
      var a = 'translate(' + pct(from[0]) + ',' + pct(from[1]) + ')';
      var z = 'translate(' + pct(to[0]) + ',' + pct(to[1]) + ')';
      var cycle = Math.max(f.cycle || 0, flight * 1.25) * 1000;
      if (flock.animate) {
        flock.animate([{ transform: a, offset: 0 }, { transform: z, offset: flight * 1000 / cycle },
                       { transform: z, offset: 1 }],
                      { duration: cycle, delay: -(f.at || 0) * 1000, iterations: Infinity, easing: 'linear' });
      } else {
        flock.style.display = 'none';
      }
    });
    container.appendChild(layer);
    return { layer: layer, stop: function () { layer.remove(); } };
  }

  root.flyGulls = flyGulls;
  if (typeof module !== 'undefined' && module.exports) module.exports = flyGulls;
})(typeof window !== 'undefined' ? window : this);
