#!/usr/bin/env python3
"""Builds block-camp.html - the Block Camp hub - from template.html plus the
card data below, and writes a self-contained preview (every image inlined,
downscaled) to $PREVIEW_DIR (default: the system temp dir) for sending into a chat.

    python3 lesson-template/build/block-camp-hub/build.py

seo.html, nav.html and monocraft.css are the pieces lifted verbatim from the
previous hub so the SEO block, the site's top band and the Monocraft subset
stay byte-identical across rebuilds. If seo.py rewrites the SEO block in
block-camp.html, copy the new block back into seo.html before the next build,
or the build will put the old one back.

The published HTML is the site's copy; this script is how it was made. Keep
both in the repo (see docs/HANDOFF.md, 2026-09-04, and the Block Camp deck
generator that was lost with a sandbox)."""
import base64, mimetypes, os, re, sys, tempfile

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))

# The eight camp colours are the route map's stop colours, verbatim. Camp 9
# (Past Perfect, built 2026-09-04 on branch past-perfect-camp) has no stop on
# the map yet; its colour is the deck's own ink, #d66d77, the readable step up
# from its --t-past-perfect maroon.
CAMP = {1:'#7A93B5',2:'#E66085',3:'#B08968',4:'#F1D779',5:'#70A43A',6:'#F0723F',7:'#2E7D65',8:'#46B0AB',9:'#d66d77'}
INK  = {1:'#0b1a12',2:'#0b1a12',3:'#0b1a12',4:'#0b1a12',5:'#0b1a12',6:'#0b1a12',7:'#f2f7f3',8:'#0b1a12',9:'#0b1a12'}

def present(path):
    """A card is emitted only if its page exists in the repo. This is what lets
    the same builder run before and after the past-perfect branch lands: camp
    9, station 17 and the ninth reference appear the moment their files do."""
    return os.path.exists(os.path.join(REPO, path))

CLIMB = [
 (1,'Present Simple','present-simple','A1','A2'),
 (2,'Present Continuous','present-continuous','A1','A2'),
 (3,'Past Simple','past-simple','A1','A2'),
 (4,'Past Continuous','past-continuous','A1','A2'),
 (5,'Going To','going-to','A1','A2'),
 (6,'Future Simple','future-simple','A2','B1'),
 (7,'Present Perfect','present-perfect','A2','B1'),
 (8,'Present Perfect Continuous','present-perfect-continuous','B1','B1'),
 (9,'Past Perfect','past-perfect','B1','B1'),
]
FREE_CLIMB = {(1,1),(2,1),(3,1)}

DESCENT = [
 (9,1,'Present Simple Passive','present-simple','A2','free'),
 (10,2,'Present Continuous Passive','present-continuous','A2','pro'),
 (11,3,'Past Simple Passive','past-simple','A2','pro'),
 (12,4,'Past Continuous Passive','past-continuous','B1','pro'),
 (13,5,'Going To Passive','going-to','B1','pro'),
 (14,6,'Future Simple Passive','future-simple','B1','pro'),
 (15,7,'Present Perfect Passive','present-perfect','B1','pro'),
 (16,0,'The Trial','trial','B1','pro'),
 (17,9,'Past Perfect Passive','past-perfect','B1','pro'),
]

REFS = [
 (1,'Present Simple','present-simple-time-signals.html','present-simple-time-signals/bg01.jpg','A1','pro'),
 (2,'Present Continuous','present-continuous-time-signals.html','present-continuous-time-signals/bg01.jpg','A1','pro'),
 (3,'Past Simple','past-simple-time-signals.html','past-simple-time-signals/bg01.jpg','A1','pro'),
 (4,'Past Continuous','past-continuous-time-signals.html','past-continuous-time-signals/bg01.jpg','A1','pro'),
 (5,'Going To','going-to-infinitive.html','going-to-infinitive/bg01.jpg','A1','pro'),
 (6,'Future Simple: Will','future-simple-will.html','future-simple-will/bg01.jpg','A1','pro'),
 (7,'Present Perfect','present-perfect-time-signals.html','present-perfect-time-signals/bg07.jpg','A1','free'),
 (8,'Present Perfect Continuous','present-perfect-continuous-time-signals.html','present-perfect-continuous-time-signals/bg01.jpg','A1','pro'),
 (9,'Past Perfect','past-perfect-time-signals.html','past-perfect-time-signals/bg01.jpg','B1','pro'),
]

MORE = [
 ('Must &amp; Have To','minecraft-lesson.html','minecraft/giant-golem-moonrise.jpg','A2'),
 ('Minecraft B1 Lesson','forbes-english-minecraft-b1.html','minecraft/pig-creeper-building-hero.jpg','B1'),
 ('Minecraft Trivia','forbes-english-minecraft-editorial.html','minecraft/enderman-desert-landscape.jpg','B1'),
 ('Past Modals','forbes-english-past-modals-minecraft.html','minecraft/minecraft-underwater-temple.png','B2'),
 ('Tense Review','tense-review-minecraft.html','minecraft/creeper-hillside-dusk.jpg','B2'),
 ('Dino-Craft Part I','forbes-english-dinosaur-minecraft.html','minecraft/dc1-hero.jpg','C1'),
 ('Dino-Craft Part II','forbes-english-dinosaur-minecraft-part2.html','minecraft/dc2-hero.jpg','C1'),
 ('Minecraft C1 Lesson','forbes-english-minecraft-c1.html','minecraft/minecraft-landscape-thumb.jpg','C1'),
]

def chips(level, access):
    a = '<span class="chip chip-free">Free</span>' if access=='free' else '<span class="chip chip-pro"><svg viewBox="0 0 10 12" aria-hidden="true"><path d="M2 5V3.5a3 3 0 0 1 6 0V5h1v7H1V5h1zm1.4 0h3.2V3.5a1.6 1.6 0 0 0-3.2 0V5z"/></svg>Pro</span>'
    return f'<span class="chips"><span class="chip">{level}</span>{a}</span>'

def card(href, img, num, badge_text, title, level, access, colour=None, ink=None, sub=None):
    style = f' style="--c:{colour};--ci:{ink}"' if colour else ''
    badge = f'<span class="num" aria-hidden="true">{badge_text}</span>' if badge_text else ''
    subh = f'<span class="card-sub">{sub}</span>' if sub else ''
    return (f'<li><a class="card"{style} href="{href}">'
            f'<span class="thumb"><img src="{img}" alt="" loading="lazy"></span>'
            f'<span class="body"><span class="row">{badge}<span class="card-title">{title}</span></span>{subh}{chips(level,access)}</span>'
            f'</a></li>')

def climb_cards():
    out=[]
    for n,name,slug,l1,l2 in CLIMB:
        if present(f'blockcamp-{slug}.html'):
            out.append(card(f'blockcamp-{slug}.html', f'BlockCamp/{slug}-1a.jpg', n, str(n), name, l1,
                            'free' if (n,1) in FREE_CLIMB else 'pro', CAMP[n], INK[n], 'Part 1'))
        if present(f'blockcamp-{slug}-2.html'):
            out.append(card(f'blockcamp-{slug}-2.html', f'BlockCamp/{slug}-1b.jpg', n, str(n), name, l2,
                            'pro', CAMP[n], INK[n], 'Part 2'))
    return '\n'.join(out)

def count_climb():
    return sum(present(f'blockcamp-{s}.html') + present(f'blockcamp-{s}-2.html') for _,_,s,_,_ in CLIMB)

def count_tenses():
    return sum(present(f'blockcamp-{s}.html') for _,_,s,_,_ in CLIMB)

def descent_cards():
    out=[]
    for st,camp,name,slug,lvl,acc in DESCENT:
        if not present(f'blockcamp-passive-{slug}.html'): continue
        if camp:
            col,ink = CAMP[camp],INK[camp]
        else:
            col,ink = '#e8c04a','#0b1a12'
        out.append(card(f'blockcamp-passive-{slug}.html', f'BlockCamp/passive-{st}-{slug}.jpg', st, str(st), name, lvl, acc, col, ink,
                        'Station %d' % st if camp else 'Station 16 &middot; every tense, no labels'))
    return '\n'.join(out)

def count_descent():
    return sum(present(f'blockcamp-passive-{s}.html') for _,_,_,s,_,_ in DESCENT)

def ref_cards():
    return '\n'.join(card(h,i,n,'',t,l,a,CAMP[n],INK[n]) for n,t,h,i,l,a in REFS if present(h))

def count_refs():
    return sum(present(h) for _,_,h,_,_,_ in REFS)


# The adventures — the Block Camp RPGs under block-camp/. Built by
# lesson-template/build/rpg/ (see its README); a card appears once its page
# exists, and the tally strip / lede counts follow. `chips` are the grammar
# chips in order; `tag` is the coloured lead chip (start / new) or None.
ADVENTURES = [
 ('block-camp/last-train-home-rpg.html','block-camp/last-train-home-rpg/01_cover.webp','The Last Train Home',
  'A cyberpunk megacity, a curfew closing in, and one train left before the checkpoints seal the district. Every route out is a prediction about what will happen next.',
  ('Future Simple',),'A1&ndash;A2','pro','start'),
 ('block-camp/dracula-castle-of-if.html','block-camp/dracula-castle-of-if/01_cover.webp','Dracula: The Castle of If',
  'Bram Stoker&rsquo;s castle, reimagined as a branching grammar nightmare &mdash; every escape route runs on a conditional, and every guard&rsquo;s report comes back in the passive voice.',
  ('Conditionals','Passive'),'B2','pro','new'),
 ('block-camp/long-way-home-rpg.html','block-camp/long-way-home-rpg/00_cover.webp','The Long Way Home',
  'Homer&rsquo;s Odyssey rebuilt block by block. Thirty-six scenes of storm and monster where the tense you choose decides what happened first &mdash; and losing the thread costs you the crew.',
  ('Narrative Tenses',),'B1','pro','new'),
 ('block-camp/lost-yellow-road-rpg.html','block-camp/lost-yellow-road-rpg/01_cover.webp','The Lost Yellow Road',
  'A voxel Oz. The Witch has scattered four tiles of the yellow road, and every one comes back as a question about what was happening at that moment &mdash; click the glowing object in each scene to read.',
  ('Past Continuous',),'A1&ndash;A2','pro','new'),
 ('block-camp/wonderland-stolen-now-rpg.html','block-camp/wonderland-stolen-now-rpg/00_cover.webp','Wonderland: The Stolen Now',
  'The last afternoon is looping and the palace clock is counting down. Two branching acts, a pink-or-blue cake trial that splits what is happening now from what always happens, and three endings.',
  ('Present Continuous',),'A1&ndash;A2','pro','new'),
]

def adventure_cards():
    out=[]
    for href,img,title,desc,gram,lvl,acc,tag in ADVENTURES:
        if not present(href): continue
        lead = {'start':'<span class="chip chip-start">Start here</span>','new':'<span class="chip chip-new">New</span>'}.get(tag,'')
        pro = ('<span class="chip chip-free">Free</span>' if acc=='free' else
               '<span class="chip chip-pro"><svg viewBox="0 0 10 12" aria-hidden="true"><path d="M2 5V3.5a3 3 0 0 1 6 0V5h1v7H1V5h1zm1.4 0h3.2V3.5a1.6 1.6 0 0 0-3.2 0V5z"/></svg>Pro</span>')
        chipset = lead + ''.join(f'<span class="chip">{g}</span>' for g in gram) + f'<span class="chip">{lvl}</span>' + pro
        out.append(f'      <li><a class="card" href="{href}">\n        <span class="thumb"><img src="{img}" alt="" loading="lazy"></span>\n        <span class="body">\n          <span class="card-title">{title}</span>\n          <span class="desc">{desc}</span>\n          <span class="chips">{chipset}</span>\n        </span>\n      </a></li>')
    return '\n'.join(out)

def count_adv():
    return sum(present(h) for h,*_ in ADVENTURES)

WORDS = {3:'three',4:'four',5:'five',8:'eight',9:'nine',16:'sixteen',17:'seventeen',18:'eighteen',24:'twenty-four',25:'twenty-five',26:'twenty-six',27:'twenty-seven'}

def more_cards():
    return '\n'.join(card(h,i,0,'',t,l,'pro') for t,h,i,l in MORE)

def build(inline):
    tpl = open(os.path.join(HERE,'template.html')).read()
    tpl = (tpl.replace('{{SEO}}', open(os.path.join(HERE,'seo.html')).read())
              .replace('{{MONOCRAFT}}', open(os.path.join(HERE,'monocraft.css')).read())
              .replace('{{NAV}}', open(os.path.join(HERE,'nav.html')).read())
              .replace('{{CLIMB}}', climb_cards())
              .replace('{{DESCENT}}', descent_cards())
              .replace('{{REFS}}', ref_cards())
              .replace('{{MORE}}', more_cards())
              .replace('{{ADV}}', adventure_cards())
              .replace('{{N_ADV}}', str(count_adv()))
              .replace('{{W_ADV}}', WORDS.get(count_adv(), str(count_adv())))
              .replace('{{N_CLIMB}}', str(count_climb()))
              .replace('{{N_DESCENT}}', str(count_descent()))
              .replace('{{N_REFS}}', str(count_refs()))
              .replace('{{W_CLIMB}}', WORDS.get(count_climb(), str(count_climb())))
              .replace('{{W_DESCENT}}', WORDS.get(count_descent(), str(count_descent())))
              .replace('{{W_REFS}}', WORDS.get(count_refs(), str(count_refs())))
              .replace('{{W_TENSES}}', WORDS.get(count_tenses(), str(count_tenses())))
              .replace('{{N_TOTAL}}', WORDS.get(count_climb()+count_descent(), str(count_climb()+count_descent()))))
    if inline:
        def sub(m):
            p = m.group(2)
            if p.startswith('data:') or p.startswith('http'): return m.group(0)
            fp = os.path.join(REPO,p)
            if not os.path.exists(fp):
                print('MISSING', p, file=sys.stderr); return m.group(0)
            from PIL import Image; import io
            im = Image.open(fp).convert('RGB')
            maxw = 1600 if 'hub-hero' in p or 'watchtower' in p else 720
            if im.width > maxw: im = im.resize((maxw, round(im.height*maxw/im.width)), Image.LANCZOS)
            buf = io.BytesIO(); im.save(buf, 'JPEG', quality=78, optimize=True)
            mt = 'image/jpeg'; d = base64.b64encode(buf.getvalue()).decode()
            return f'{m.group(1)}data:{mt};base64,{d}{m.group(3)}'
        tpl = re.sub(r'(src="|url\()([^")]+\.(?:jpg|jpeg|png|webp))("|\))', sub, tpl)
    return tpl

if __name__ == '__main__':
    site = build(False)
    open(os.path.join(REPO,'block-camp.html'),'w').write(site)
    prev = build(True)
    open(os.path.join(os.environ.get('PREVIEW_DIR') or tempfile.gettempdir(), 'block-camp-hub-preview.html'),'w').write(prev)
    print('site', len(site), 'preview', len(prev))
