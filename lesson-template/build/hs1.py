# -*- coding: utf-8 -*-
"""House style 1 (HOUSE-STYLE.md §000), as a library.

The reference is build_comeback_ride.py. Its per-deck machinery (frame(),
POP, GHOST, the texture field, the pop-out cover) lived in that one builder;
this module is the same code, lifted so any builder can use it. Comeback Ride
itself is untouched and stays the reference for how it looks.

    import hs1
    K = hs1.Deck('Venezuela', pop={'used': (None, 'blob')})
    s = [K.cover(E)]
    s.append(K.frame(K.talk('eT', 'tk1T', prompts, E), 'talk'))
    s.append(K.frame(D.mc(...), 'q-angel-falls', text=(stem, options)))
    out = K.assemble('deck.html', ''.join(s), 'Title', i18n_module, langs)

Rules it carries, from §000:
  * every picture is framed beside the text, never behind it, and the sides
    alternate (side='auto');
  * a plate is <folder>/<slot>.jpg, a whole 16:9 render with its subject
    centred; a slot whose plate has not landed yet gets NO picture, and the
    slide shows the texture field instead (rule 7), so a deck builds while
    its art is still being made, and K.missing lists what is owed;
  * no plate twice in a stage: frame() refuses a repeat inside one stage
    (K.stage() starts the next one);
  * pops (rule 4): POP = {slot: (span, mode[, box[, 'wide']])}, drawn by
    tools/pop_plate.py, mode square / blob / free;
  * the cover is a pop-out (rule 5), cut from <folder>/hero.jpg;
  * text width decides the frame: long options take the narrow frame,
    longer ones the full width with no picture.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
import deck as D  # noqa: E402
import pop_plate  # noqa: E402

TPL = 'lesson-template/lesson-template.html'

# Visible characters beyond which a question cannot sit beside the default
# frame (37%), beside the narrow one (30%), or beside any picture. From The
# Comeback Ride, where the reading options (60-75 characters) went narrow.
OPT_DEFAULT, OPT_NARROW = 44, 76
STEM_DEFAULT, STEM_NARROW = 92, 130

TEXTURE_CSS = '''
/* House style 1, rule 7: a slide with no picture of its own gets a faint
   grayscale close-up of the cover, multiplied in at 6%. Off on the cover. */
html[data-style="editorial"] .stage:not(.on-cover):not(:has(.slide.is-active[data-bg])) .bg-layer::before {
  content: ''; position: absolute; inset: 0;
  background: var(--hero) var(--art-pos, center) 45% / 260% auto no-repeat;
  filter: grayscale(1) contrast(1.15); opacity: .06; mix-blend-mode: multiply;
}
html[data-style="editorial"] .opts { gap: 8px; }
html[data-style="editorial"] .opt { padding-top: 10px; padding-bottom: 10px; }
'''

COVER_CSS = '''
/* House style 1, rule 5: the hero is cut out and bursts out of a rounded
   square of its own scene at the right, in a 640x600 zone at x 600-1240;
   the title stands on clean cream at the left. */
html[data-style="editorial"]:not(.is-flow) .cover-inner { max-width: %(cover_w)d%%; }   /* 44%% ends at 563px, clear of the zone */
html[data-style="editorial"]:not(.is-flow) .cover-title { font-size: %(title_px)dpx; }
html[data-style="editorial"]:not(.is-flow) .stage.on-cover .bg-layer::before {
  background: url('%(pop)s') 600px 64px / 640px 600px no-repeat;
  filter: drop-shadow(0 14px 26px color-mix(in srgb, var(--text) 18%%, transparent));
}
html[data-style="editorial"]:not(.is-flow) .stage.on-cover .bg-layer::after { content: none; }
/* On a phone the cover is a page: the type on the cream, the hero a band
   along the bottom, above the deck bar. */
html.is-flow[data-style="editorial"] .stage.on-cover .bg-layer::before {
  background: var(--hero) %(band_pos)s bottom 56px / auto 34svh no-repeat;
}
html.is-flow[data-style="editorial"] .stage.on-cover .bg-layer::after { content: none; }
html.is-flow[data-style="editorial"] .slide[data-type="cover"] .cover-inner {
  padding-bottom: calc(34svh + 16px);
}
'''


def _vis(s):
    return len(re.sub(r'<[^>]+>', '', s).replace('&nbsp;', ' '))


class Deck:
    def __init__(self, folder, pop=None, ghost=(), hero='hero', cover_mode='square',
                 cover_span=None, cover_box=None, title_px=72, band_pos='center', cover_slot=None, cover_w=40,
                 cover_name='pop-cover'):
        """cover_slot: the plate the cover pops out, when the hero is a scene
        with no one object in it (rembg then cuts a fragment). The hero still
        gives the texture field and the phone band."""
        self.F = folder
        self.cover_slot = cover_slot or hero
        # two decks sharing a folder each need their own cut (Swiss Mistakes 1 and 2)
        self.cover_name = cover_name
        self.pop = dict(pop or {})
        self.ghosts = set(ghost)
        self.hero = hero
        self.cover_mode, self.cover_span, self.cover_box = cover_mode, cover_span, cover_box
        self.title_px, self.band_pos, self.cover_w = title_px, band_pos, cover_w
        self.missing = []
        self.css = []
        self._side = 0
        self._stage = set()

    # ── plates ─────────────────────────────────────────────────────────
    def has(self, slot):
        return bool(slot) and os.path.exists(os.path.join(self.F, slot + '.jpg'))

    def stage(self):
        """Start the next stage: plates may repeat across stages, not inside one."""
        self._stage = set()

    def frame(self, html, slot, side='auto', pos=None, shape=None, size='auto', text=None):
        """Give a slide its framed picture, or the texture field.

        text: (stem, options) for a question, so the frame fits the words:
        long options take the narrow frame, longer ones no picture at all."""
        html = re.sub(r' data-bg="[^"]*"', '', html, count=1)
        if slot and not self.has(slot):
            if slot not in self.missing:
                self.missing.append(slot)
            slot = None
        if text and slot:
            stem, opts = text
            lo, ls = max(_vis(o) for o in opts), _vis(stem)
            if lo > OPT_NARROW or ls > STEM_NARROW:
                slot = None
            elif size == 'auto' and (lo > OPT_DEFAULT or ls > STEM_DEFAULT):
                size = 'narrow'
        if size == 'auto':
            size = None
        if not slot:
            return html
        assert slot not in self._stage, 'plate %r twice in one stage' % slot
        self._stage.add(slot)
        if side == 'auto':
            side = 'left' if self._side % 2 else None
            self._side += 1
        attrs = ' data-bg="%s/%s.jpg"' % (self.F, slot)
        if slot in self.pop:
            p = self.pop[slot]
            if len(p) > 3 and p[3] == 'wide':
                size = None
            narrow = size == 'narrow'
            out = os.path.join(self.F, 'pop-%s%s.webp' % (slot, '-n' if narrow else ''))
            if not os.path.exists(out):
                print('  pop', out, pop_plate.build(os.path.join(self.F, slot + '.jpg'), out, narrow, *p[:3]))
            attrs = ' data-bg="%s"' % out.replace(os.sep, '/')
            side, pos, shape = None, None, 'pop'
        if slot in self.ghosts and shape != 'pop':
            attrs += self._ghost(slot, side, pos, size)
        if side == 'left':
            attrs += ' data-art-side="left"'
        if pos:
            attrs += ' data-art-pos="%s"' % pos
        if shape:
            attrs += ' data-art="%s"' % shape
        if size:
            attrs += ' data-art-size="%s"' % size
        return re.sub(r'<section class="slide( is-active)?"', lambda m: m.group(0) + attrs, html, count=1)

    def _ghost(self, pl, side, pos, size):
        """The plate's scene carrying on past the frame as a faint grayscale
        ghost, at the frame's own scale (§000 rule 6)."""
        fw = (0.30 if size == 'narrow' else 0.37) * 1280
        fh = 0.57 * 720
        fl = 58 if side == 'left' else 1280 - 58 - fw
        w = max(fh * 16 / 9, fw)
        p = 0.5 if not pos or pos == 'center' else float(pos.rstrip('%')) / 100
        x = fl + (fw - w) * p
        gid = '%s-%s-%s' % (pl, size or 'std', side or 'right')
        grad = ('linear-gradient(90deg, transparent %.0fpx, #000 %.0fpx, #000 %.0fpx, transparent %.0fpx)'
                % (x + 20, fl - 30, fl + fw + 30, x + w - 20))
        self.css.append(
            'html[data-style="editorial"] .stage:has(.slide.is-active[data-ghost="%s"]) .bg-layer::before {\n'
            "  content: ''; position: absolute; inset: 0; opacity: .2; filter: grayscale(1);\n"
            "  background: url('%s/%s.jpg') %.1fpx 172px / %.1fpx %.1fpx no-repeat;\n"
            '  -webkit-mask-image: %s;\n  mask-image: %s;\n}' % (gid, self.F, pl, x, w, fh, grad, grad))
        return ' data-ghost="%s"' % gid

    # ── slides ─────────────────────────────────────────────────────────
    def cover(self, E, chips=None):
        assert os.path.exists(os.path.join(self.F, self.hero + '.jpg')), 'house style 1 needs %s/%s.jpg' % (self.F, self.hero)
        hero = os.path.join(self.F, self.cover_slot + '.jpg')
        out = os.path.join(self.F, self.cover_name + '.webp')
        if not os.path.exists(out):
            print('  pop', out, pop_plate.build(hero, out, span=self.cover_span, mode=self.cover_mode,
                                                box=self.cover_box, zone=(640, 600)))
        self.css.insert(0, COVER_CSS % dict(pop=out.replace(os.sep, '/'), title_px=self.title_px, cover_w=self.cover_w,
                                            band_pos=self.band_pos))
        chips = chips or [('Level', E['chipLevel']), ('Count', E['chipCount']), ('Focus', E['chipFocus'])]
        return D.cover(D.logo_from(TPL), E['coverTitle'], E['coverSub'], chips)

    @staticmethod
    def talk(ek, tk, prompts, E, cols=2):
        """Speaking prompts as cards (the reference deck's talk slide): two
        columns beside a picture, three on a slide with none."""
        cells = '\n          '.join(
            '<div class="card" style="padding:16px 20px;display:flex;align-items:center">'
            '<p class="prose" style="font-size:19px;line-height:1.42">%s</p></div>' % p for p in prompts)
        return '''
    <section class="slide" data-type="discuss">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:%s;gap:14px">
          %s
        </div>
      </div>
    </section>
''' % (ek, E[ek], tk, E[tk], ' '.join(['1fr'] * cols), cells)

    # ── the page ───────────────────────────────────────────────────────
    def _wash(self, body):
        """Innes, 2026-11-09, of the tennis net and the money seedling behind
        text-only slides: "we can have some full color full page backgrounds
        from time to time ... but compositionally should be flipped". A match or
        activation slide (no picture of its own) gets the hero
        in FULL colour, mirrored and pushed right so its subject sits on the
        side away from the text, fading out to the cream under the text
        column. The rest keep the faint texture field (rule 7)."""
        from PIL import Image, ImageOps
        src = os.path.join(self.F, self.hero + '.jpg')
        flip = os.path.join(self.F, self.hero + '-flip.jpg')
        if not os.path.exists(flip) or os.path.getmtime(flip) < os.path.getmtime(src):
            ImageOps.mirror(Image.open(src).convert('RGB')).save(flip, quality=86)
        def tag(m):
            t = m.group(0)
            # only where the content keeps to the left column: under full-width
            # cards (gap rows, three rule cards, the sort) it was clutter
            if 'data-bg=' in t or not re.search(r'data-type="(match|activate)"', t):
                return t
            return t[:-1] + ' data-wash>'
        body = re.sub(r'<section class="slide[^>]*>', tag, body)
        # fades out to the left (text) and above the deck bar
        grad = ('linear-gradient(90deg, transparent 34%, rgba(0,0,0,.55) 52%, #000 70%), '
                'linear-gradient(180deg, #000 78%, transparent 90%)')
        self.css.append(
            'html[data-style="editorial"]:not(.is-flow) .stage:not(.on-cover):not(:has(.slide.is-active[data-bg]))'
            ':has(.slide.is-active[data-wash]) .bg-layer::before {\n'
            "  content: ''; position: absolute; inset: 0; opacity: 1; filter: none; mix-blend-mode: normal;\n"
            "  background: url('%s') 330px center / auto 112%% no-repeat;\n"
            '  -webkit-mask-image: %s;\n  mask-image: %s;\n'
            '  -webkit-mask-composite: source-in; mask-composite: intersect;\n}'
            % (flip.replace(os.sep, '/'), grad, grad))
        return body

    def assemble(self, out_path, body, title, i18n, langs, extra_css=''):
        body = self._wash(body)
        out = D.assemble(TPL, out_path, body, D.editorial_palette('%s/%s.jpg' % (self.F, self.hero)),
                         title, i18n, langs=langs, style='editorial')
        assert '\n</style>' in out
        css = TEXTURE_CSS + '\n'.join(dict.fromkeys(self.css)) + extra_css
        out = out.replace('\n</style>', css + '\n</style>', 1)
        open(out_path, 'w', encoding='utf-8', newline='').write(out)
        n = body.count('<section class="slide')
        print('wrote %s — %d slides (house style 1)' % (out_path, n))
        if self.missing:
            print('  plates owed (texture field until they land): %s' % ', '.join(self.missing))
        return out
