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
generator that was lost with a sandbox).

LANGUAGES (2026-10-03). The hub speaks the ten languages the decks offer.
The words are hub_i18n.py, beside this file; the English stays in the
template and the tables below, and every translated element carries a
data-i18n key. build() checks the page against the table before it writes
anything - a key with no string in some language, a tag lost in a
translation, a count left unfilled, or a Lookout goal camp-flags.js can say
that the tile cannot - and stops with the list. The choice is remembered as
localStorage 'bc-lang'."""
import base64, importlib.util, json, mimetypes, os, re, sys, tempfile
from html.parser import HTMLParser

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

# ── FREE OR PRO IS THE CATALOGUE'S ANSWER, NOT THIS FILE'S ──────────────
# The access written into the tables below - FREE_CLIMB, and the 'free' /
# 'pro' in DESCENT, REFS and ADVENTURES - is only a fallback now, for a page
# the catalogue does not list yet. It used to be the answer, and it went stale
# twice: 9c0381a (Past Simple 1a freed, the hub still said Pro), then e709bfc
# on 2026-09-15, which freed five more camp 1a decks and eight Time Signals
# references so every topic hub had an open lesson. The hub printed Pro on all
# thirteen until 2026-09-27. lesson-meta.json is the file the Worker builds
# its gate pages from, so it is what a Free or Pro chip has to agree with.
# The quest and the deck buttons (block-camp-nav) read it through access()
# too, and checker/check-access.py holds all of them, and the hand-kept route
# map, to it.
def _catalogue():
    try:
        meta = json.load(open(os.path.join(REPO, 'lesson-meta.json'), encoding='utf-8'))
    except (OSError, ValueError):
        return {}
    return {f: row['access'] for f, row in meta.items() if row.get('access')}
CATALOGUE = _catalogue()

def access(page, fallback):
    return CATALOGUE.get(page.split('#')[0], fallback)

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
FREE_CLIMB = {(1,1),(2,1),(3,1),(4,1)}

DESCENT = [
 (9,1,'Present Simple Passive','present-simple','A2','pro'),
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

FREE_CHIP = '<span class="chip chip-free" data-i18n="free">Free</span>'
PRO_CHIP = '<span class="chip chip-pro"><svg viewBox="0 0 10 12" aria-hidden="true"><path d="M2 5V3.5a3 3 0 0 1 6 0V5h1v7H1V5h1zm1.4 0h3.2V3.5a1.6 1.6 0 0 0-3.2 0V5z"/></svg>Pro</span>'

def chips(level, access):
    a = FREE_CHIP if access=='free' else PRO_CHIP
    return f'<span class="chips"><span class="chip">{level}</span>{a}</span>'

def card(href, img, num, badge_text, title, level, access, colour=None, ink=None, sub=None, sub_key=None, sub_n=None):
    """sub_key / sub_n: the card-sub's data-i18n key and the number its {n}
    takes ("Part 1" is part / 1). The title is a camp, tense or lesson name,
    which stays English in every language, as on the decks' covers."""
    style = f' style="--c:{colour};--ci:{ink}"' if colour else ''
    badge = f'<span class="num" aria-hidden="true">{badge_text}</span>' if badge_text else ''
    key = (f' data-i18n="{sub_key}"' + (f' data-n="{sub_n}"' if sub_n is not None else '')) if sub_key else ''
    subh = f'<span class="card-sub"{key}>{sub}</span>' if sub else ''
    return (f'<li><a class="card"{style} href="{href}">'
            f'<span class="thumb"><img src="{img}" alt="" loading="lazy"></span>'
            f'<span class="body"><span class="row">{badge}<span class="card-title" lang="en">{title}</span></span>{subh}{chips(level,access)}</span>'
            f'</a></li>')

def climb_cards():
    out=[]
    for n,name,slug,l1,l2 in CLIMB:
        if present(f'blockcamp-{slug}.html'):
            out.append(card(f'blockcamp-{slug}.html', f'BlockCamp/{slug}-1a.jpg', n, str(n), name, l1,
                            access(f'blockcamp-{slug}.html', 'free' if (n,1) in FREE_CLIMB else 'pro'),
                            CAMP[n], INK[n], 'Part 1', 'part', 1))
        if present(f'blockcamp-{slug}-2.html'):
            out.append(card(f'blockcamp-{slug}-2.html', f'BlockCamp/{slug}-1b.jpg', n, str(n), name, l2,
                            access(f'blockcamp-{slug}-2.html', 'pro'), CAMP[n], INK[n], 'Part 2', 'part', 2))
    return '\n'.join(out)

def _runs(nums, sep=', ', conj=' and ', wrap=str):
    """[1,2,3,5,6,8] -> '1&ndash;3, 5, 6 and 8': a run of three or more is a range.
    sep / conj / wrap say it in another language (wrap isolates a range
    inside right-to-left text, where '1–4' would otherwise read '4–1')."""
    groups, out = [], []
    for n in nums:
        if groups and n == groups[-1][-1] + 1: groups[-1].append(n)
        else: groups.append([n])
    for g in groups:
        out += [wrap(f'{g[0]}&ndash;{g[-1]}')] if len(g) > 2 else [str(x) for x in g]
    return out[0] if len(out) == 1 else sep.join(out[:-1]) + conj + out[-1]

def climb_free_note(F=None, wrap=str):
    """The track note's free clause, from the same access() the chips use:
    it said 'Part 1 free on camps 1-3' for twelve days after camps 4, 5, 6,
    8 and 9 went free. F is a language's FREE table (hub_i18n.py); without
    one, the English."""
    camps = [n for n,_,s,_,_ in CLIMB if present(f'blockcamp-{s}.html')]
    free = [n for n,_,s,_,_ in CLIMB if present(f'blockcamp-{s}.html')
            and access(f'blockcamp-{s}.html', 'free' if (n,1) in FREE_CLIMB else 'pro') == 'free']
    if not free: return ''
    if F:
        if free == camps: return F['every']
        if len(camps) - len(free) == 1:
            return F['but'].replace('{n}', str(next(n for n in camps if n not in free)))
        return F['one' if len(free) == 1 else 'many'].replace('{list}', _runs(free, F['sep'], F['conj'], wrap))
    if free == camps: return ' &middot; Part 1 free on every camp'
    if len(camps) - len(free) == 1:
        return ' &middot; Part 1 free on every camp but %d' % next(n for n in camps if n not in free)
    return ' &middot; Part 1 free on camp%s %s' % ('s' if len(free) > 1 else '', _runs(free))

def descent_free_note(F=None, wrap=str):
    stations = [st for st,_,_,s,_,_ in DESCENT if present(f'blockcamp-passive-{s}.html')]
    free = [st for st,_,_,s,_,acc in DESCENT if present(f'blockcamp-passive-{s}.html')
            and access(f'blockcamp-passive-{s}.html', acc) == 'free']
    if not free: return ''
    if F:
        if free == stations: return F['dEvery']
        return F['dOne' if len(free) == 1 else 'dMany'].replace('{list}', _runs(free, F['sep'], F['conj'], wrap))
    if free == stations: return ' &middot; every station free'
    return ' &middot; station%s %s free' % ('s' if len(free) > 1 else '', _runs(free))

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
        out.append(card(f'blockcamp-passive-{slug}.html', f'BlockCamp/passive-{st}-{slug}.jpg', st, str(st), name, lvl,
                        access(f'blockcamp-passive-{slug}.html', acc), col, ink,
                        'Station %d' % st if camp else 'Station %d &middot; every tense, no labels' % st,
                        'station' if camp else 'trialSub', st))
    return '\n'.join(out)

def count_descent():
    return sum(present(f'blockcamp-passive-{s}.html') for _,_,_,s,_,_ in DESCENT)

def ref_cards():
    return '\n'.join(card(h,i,n,'',t,l,access(h,a),CAMP[n],INK[n]) for n,t,h,i,l,a in REFS if present(h))

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
 ('block-camp/dracula-castle-of-if.html','LibraryCards/dracula-castle-of-if.jpg','Grammar Stoker&rsquo;s Blocula',
  'Bram Stoker&rsquo;s castle as a branching grammar nightmare. The west door is locked, the iron key hangs on the Count&rsquo;s coat, and the last act asks whether you go down to the crypt or out through the courtyard &mdash; every route runs on a conditional, every report comes back in the passive.',
  ('Conditionals','Passive'),'B2','pro','new'),
 ('block-camp/long-way-home-rpg.html','block-camp/long-way-home-rpg/00_cover.webp','The Long Way Home',
  'Homer&rsquo;s Odyssey rebuilt block by block. Thirty-six scenes of storm and monster where the tense you choose decides what happened first &mdash; and losing the thread costs you the crew.',
  ('Narrative Tenses',),'B1','pro','new'),
 ('block-camp/lost-yellow-road-rpg.html','block-camp/lost-yellow-road-rpg/01_cover.webp','The Lost Yellow Road',
  'A voxel Oz. The Witch has scattered four tiles of the yellow road, and every one comes back as a question about what was happening at that moment &mdash; click the glowing object in each scene to read.',
  ('Past Continuous',),'A1&ndash;A2','pro','new'),
 ('block-camp/frankenstein-green-prometheus-rpg.html','block-camp/frankenstein-green-prometheus-rpg/01_cover.webp','Frankenstein Part I: Ambitions',
  'Mary Shelley&rsquo;s laboratory rebuilt block by block. Victor has the parts, the storm and the nerve, and every question asks what he is going to do with them &mdash; up to the moment the eyes open and the plan stops being his.',
  ('Going To',),'A2','pro','new'),
 ('block-camp/frankenstein-consequences-rpg.html','block-camp/frankenstein-green-prometheus-rpg/01_cover_part2.webp','Frankenstein Part II: Consequences',
  'The eyes are open and Victor has to live with it. Five branching choices decide what the Creature becomes &mdash; whether Victor speaks or runs, keeps his promise or breaks it &mdash; and the last asks Walton to choose between his crew and the glory that killed Victor.',
  ('Going To',),'A2','pro','new'),
 ('block-camp/sherlock-blue-hour-rpg.html','block-camp/sherlock-blue-hour-rpg/01_cover.webp','Sherlock Holmes: The Blue Hour',
  'The Blue Star is gone from its case and a guard faces prison for it. Two branching routes through a painted, gaslit London &mdash; the shops or the stables, the rooftops or the river &mdash; where every question asks what somebody does, every day, and four evidence tiles decide whether Holmes can prove it before the nine o&rsquo;clock bell.',
  ('Present Simple',),'A2','pro','new'),
 ('block-camp/last-bounty-rpg.html','block-camp/last-bounty-rpg/duel.webp','The Last Bounty',
  'You rode in for a five-hundred-dollar outlaw and found the man who killed your brother. Two story choices decide who has to find the courage &mdash; and a wrong answer never ends the run here: it explains the rule and lets you put it right, with the points going to whoever gets it first time.',
  ('Past Simple',),'A2','free','new'),
 ('block-camp/fistful-of-lies-rpg.html','block-camp/fistful-of-lies-rpg/22_dawn.webp','A Fistful of Lies',
  'Fifty dollars for one hour at a saloon piano, and nobody minds that you cannot play. Two branching trails through a robbery that runs on finished past actions &mdash; question the dealer or search the office, save your friend or stop the wagon &mdash; and four clue tiles that decide whether the case closes.',
  ('Past Simple',),'A1&ndash;A2','pro','new'),
 ('block-camp/wonderland-stolen-now-rpg.html','block-camp/wonderland-stolen-now-rpg/00_cover.webp','Wonderland: The Stolen Now',
  'The last afternoon is looping and the palace clock is counting down. Two branching acts, a pink-or-blue cake trial that splits what is happening now from what always happens, and three endings.',
  ('Present Continuous',),'A1&ndash;A2','pro','new'),
 ('block-camp/nautilus-black-archive-rpg.html','block-camp/nautilus-black-archive-rpg/01_intro.webp','Nautilus: The Black Archive',
  'A signal under the Atlantic, a city built from forgotten blocks, and something vast waking beneath it. Two branching descents &mdash; the crystal trench or the ruined temple, the engine room or the open water &mdash; and every question asks the same thing: a finished result, or an activity still running.',
  ('Present Perfect','Present Perfect Continuous'),'B1','pro','new'),
 ('block-camp/twenty-thousand-leagues-rpg.html','block-camp/twenty-thousand-leagues-rpg/01_intro.webp','Twenty Thousand Leagues: The Sealed Log',
  'The same voyage, painted, and told from the ship&rsquo;s log after the Nautilus came home. Every entry looks back from a later moment &mdash; what had already happened, what had still been going on &mdash; through the crystal trench, the coral city and the squid that was waiting beyond both.',
  ('Past Perfect','Past Perfect Continuous'),'B1&ndash;B2','pro','new'),
 ('block-camp/nautilus-black-archive-deep-rpg.html','block-camp/nautilus-black-archive-deep-rpg/39_archive.webp','Nautilus: The Black Archive (Deep-Sea)',
  'The Black Archive again, painted: the same signal under the Atlantic and the same drowned city, lit by lamps rather than built from blocks. Two branching descents &mdash; the crystal trench or the ruined temple, the engine room or the open water &mdash; and every question asks the one thing: a finished result, or an activity still running.',
  ('Present Perfect','Present Perfect Continuous'),'B1','pro','new'),
 ('block-camp/frostbound-river-rpg.html','block-camp/frostbound-river-rpg/01_intro.webp','Frostbound: The River Remembers',
  'A voice under the ice, two sisters who follow it north, and a dam their kingdom is proud of for the wrong reasons. Four branching choices through a frozen forest &mdash; the ridge or the trail, the fire spirit or the stone giants &mdash; where every question asks what somebody does every time, and your score alone decides which of three endings the flood leaves behind.',
  ('Present Simple',),'A1&ndash;A2','pro','new'),
 ('block-camp/grand-hotel-rpg.html','block-camp/grand-hotel-rpg/01_arrival.webp','The Last Night at the Grand Hotel',
  'A mountain hotel on its last night, an owner who vanishes in eleven seconds of darkness, and a deadline at midnight. Twenty-eight time checks across every tense &mdash; five of them clues that break an alibi &mdash; and three decisions about who to trust, what to save first and who gets to hear the truth.',
  ('Mixed Tenses',),'B1&ndash;B2','pro','new'),
]

def adv_slug(href):
    """block-camp/last-train-home-rpg.html -> last-train-home-rpg: the
    adventure's key in hub_i18n.ADV and in the page's data-i18n."""
    return os.path.splitext(os.path.basename(href))[0]

def adventure_cards():
    out=[]
    for href,img,title,desc,gram,lvl,acc,tag in ADVENTURES:
        if not present(href): continue
        lead = {'start':'<span class="chip chip-start" data-i18n="startHere">Start here</span>',
                'new':'<span class="chip chip-new" data-i18n="new">New</span>'}.get(tag,'')
        pro = FREE_CHIP if access(href, acc)=='free' else PRO_CHIP
        # the grammar chips are what is being taught: English, as in the decks
        chipset = lead + ''.join(f'<span class="chip" lang="en">{g}</span>' for g in gram) + f'<span class="chip">{lvl}</span>' + pro
        k = adv_slug(href)
        out.append(f'      <li><a class="card" href="{href}">\n        <span class="thumb"><img src="{img}" alt="" loading="lazy"></span>\n        <span class="body">\n          <span class="card-title" data-i18n="adv.{k}.t">{title}</span>\n          <span class="desc" data-i18n="adv.{k}.d">{desc}</span>\n          <span class="chips">{chipset}</span>\n        </span>\n      </a></li>')
    return '\n'.join(out)

def count_adv():
    return sum(present(h) for h,*_ in ADVENTURES)

WORDS = {3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
         11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
         16:'sixteen',17:'seventeen',18:'eighteen',
         24:'twenty-four',25:'twenty-five',26:'twenty-six',27:'twenty-seven',28:'twenty-eight'}
# every count here is spelled out in the lede, so a gap in this table shows up
# as "the 10 adventures" beside "twenty-six units". The tenth adventure found
# the first gap; the neighbours are filled in so the next one does not.

def more_cards():
    return '\n'.join(card(h,i,0,'',t,l,access(h,'pro')) for t,h,i,l in MORE)


# ── LANGUAGES ──────────────────────────────────────────────────────────
def load_i18n():
    """hub_i18n.py, by path: the quest, nav, flags and village builders load
    this file by path too, and none of them needs the words."""
    spec = importlib.util.spec_from_file_location('hub_i18n', os.path.join(HERE, 'hub_i18n.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def plural(lang, n):
    """Which of a {k|...} noun's forms a count takes."""
    if lang == 'ru':
        return 0 if n % 10 == 1 and n % 100 != 11 else 1 if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else 2
    if lang == 'ar':   # one | two | 3-10 | 11-99 | 100+
        return 0 if n == 1 else 1 if n == 2 else 2 if 3 <= n % 100 <= 10 else 3 if 11 <= n % 100 <= 99 else 4
    return 0 if n == 1 else 1

def fill(s, lang, vals):
    """{tenses} -> 9; {tenses|время|времени|времён} -> '9 времён'; {free} ->
    the clause. Anything not in vals ({n}, the Lookout's {t}) is left."""
    def sub(m):
        k, forms = m.group(1), m.group(2)
        if k not in vals: return m.group(0)
        v = vals[k]
        if forms is None or isinstance(v, str): return str(v)
        fs = forms[1:].split('|')
        return f'{v} {fs[min(plural(lang, v), len(fs) - 1)]}'
    return re.sub(r'\{(\w+)((?:\|[^|{}]+)+)?\}', sub, s)

NAV_KEYS = (('<a href="library.html">', 'navLessons'),
            ('<a href="pricing.html" class="tb-cta-gold">', 'navGoPro'),
            ('<a href="mailto:forbes@goodtimebook.com" class="tb-cta">', 'navWork'))

def nav_i18n(nav):
    """The hub's copy of the band gets its three keys (nav.html stays the
    shared original). A link that has moved is said, and stays English."""
    for tag, key in NAV_KEYS:
        if tag in nav: nav = nav.replace(tag, tag[:-1] + f' data-i18n="{key}">', 1)
        else: print(f'WARNING: nav.html has no {tag} - "{key}" stays English', file=sys.stderr)
    return nav

def i18n_table(I):
    """Everything the page's script needs, every count and free clause
    already filled in."""
    nums = dict(tenses=count_tenses(), adv=count_adv(), climb=count_climb(), descent=count_descent(),
                refs=count_refs(), total=count_climb() + count_descent())
    T = {}
    for lang, _ in I.LANGS[1:]:
        F = I.FREE[lang]
        wrap = (lambda s: f'<bdi dir="ltr">{s}</bdi>') if lang in I.RTL else str
        free = {'climbNote': climb_free_note(F, wrap), 'descNote': descent_free_note(F, wrap)}
        t = {k: fill(v, lang, dict(nums, free=free.get(k, ''))) for k, v in I.UI[lang].items()}
        for slug, (title, desc) in I.ADV[lang].items():
            t[f'adv.{slug}.t'], t[f'adv.{slug}.d'] = title, desc
        T[lang] = t
    return {'key': I.KEY, 'langs': I.LANGS, 'rtl': list(I.RTL), 'goals': I.GOALS,
            't': T, 'lk': {l: I.LK[l] for l, _ in I.LANGS[1:]}}

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}

class _Keys(HTMLParser):
    """Every translated element in the built page: key -> (English inner
    HTML or attribute, has data-n)."""
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src, self.depth, self.open, self.found = src, 0, [], {}
        self.starts = [0] + [m.end() for m in re.finditer('\n', src)]
    def _at(self):
        line, col = self.getpos()
        return self.starts[line - 1] + col
    def _attrs(self, a):
        for at, prop in (('data-i18n-aria', 'aria-label'), ('data-i18n-title', 'title')):
            if at in a: self.found.setdefault(a[at], (a.get(prop) or '', False))
    def handle_startendtag(self, tag, attrs):
        self._attrs(dict(attrs))
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self._attrs(a)
        if tag in VOID: return
        self.depth += 1
        if 'data-i18n' in a:
            self.open.append((self.depth, a['data-i18n'], self._at() + len(self.get_starttag_text()), 'data-n' in a))
    def handle_endtag(self, tag):
        if tag in VOID: return
        if self.open and self.open[-1][0] == self.depth:
            _, key, start, has_n = self.open.pop()
            self.found.setdefault(key, (self.src[start:self._at()], has_n))
        self.depth -= 1

def _tags(s):
    # <bdi> is a translation's own business: it isolates "1–4" in Arabic.
    return sorted(t for t in re.findall(r'<(\w+)(?:[^>]*?\sclass="([^"]*)")?[^>]*>', s) if t[0] != 'bdi')

def check_i18n(page, I, table):
    """The page against the table: what a learner would otherwise find as an
    English line in a German page, or a half-filled count. Returns the
    problems; build() refuses to write while there are any."""
    p = _Keys(page); p.feed(page); p.close()
    found, bad = p.found, []
    if p.open: bad.append('unclosed data-i18n element(s): %s' % [k for _, k, _, _ in p.open])
    for lang, t in table['t'].items():
        for key, (en, has_n) in found.items():
            if key not in t:
                bad.append(f'{lang}: no "{key}" (English: {en[:60]!r})'); continue
            if _tags(en) != _tags(t[key]):
                bad.append(f'{lang}: "{key}" tags {_tags(t[key])} != English {_tags(en)}')
            left = set(re.findall(r'\{\w+\}', t[key])) - ({'{n}'} if has_n else set())
            if left: bad.append(f'{lang}: "{key}" has {sorted(left)} left unfilled')
            if has_n != (key in I.N_KEYS): bad.append(f'{lang}: "{key}" data-n and N_KEYS disagree')
        stale = sorted(set(t) - set(found))
        if stale: print(f'WARNING: {lang}: in hub_i18n.py, not on the page: {stale}', file=sys.stderr)
    want = set(I.LK['de'])
    for lang, s in table['lk'].items():
        if set(s) != want: bad.append(f'{lang}: Lookout keys differ: {sorted(set(s) ^ want)}')
        need = {k for _, k in I.GOALS}
        if need - set(s): bad.append(f'{lang}: no Lookout goal for {sorted(need - set(s))}')
    for lang, _ in I.LANGS[1:]:
        if set(I.FREE[lang]) != set(I.FREE['de']): bad.append(f'{lang}: free-note keys differ')
    # Every goal the tile can be handed must be one the tile can say.
    try:
        flags = open(os.path.join(REPO, 'block-camp', 'camp-flags.js'), encoding='utf-8').read()
        goals = re.findall(r'"goal":"([^"]*)"', flags)
        if not goals: bad.append('camp-flags.js: no "goal" strings found to check the Lookout against')
        said = ['50% ' + g for g in goals] + ['50% adds a star to flag 1', 'clear it to fly its pennant']
        for g in ('adds a star to flag ', 'clear it to fly its pennant'):
            if g not in flags: bad.append(f'camp-flags.js no longer says "{g}": update hub_i18n.GOALS')
        for g in said:
            if not any(re.match(rx, g) for rx, _ in I.GOALS):
                bad.append(f'camp-flags.js goal "{g}" matches nothing in hub_i18n.GOALS')
    except OSError:
        print('WARNING: block-camp/camp-flags.js not found; Lookout goals not checked', file=sys.stderr)
    return bad

def i18n_json(table):
    # inside <script type="application/json">: nothing may close the element
    return json.dumps(table, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

def lang_options(I):
    return ''.join(f'<option value="{c}" lang="{c}"' + (' dir="rtl"' if c in I.RTL else '') + f'>{name}</option>'
                   for c, name in I.LANGS)

def build(inline):
    # Every read is explicitly utf-8: on Windows the default is cp1252, which
    # turns every em-dash and box-drawing rule in the template into mojibake.
    # It used to survive only because the write was cp1252 too and undid it.
    rd = lambda n: open(os.path.join(HERE,n), encoding='utf-8').read()
    I = load_i18n()
    table = i18n_table(I)
    tpl = rd('template.html')
    tpl = (tpl.replace('{{SEO}}', rd('seo.html'))
              .replace('{{MONOCRAFT}}', rd('monocraft.css'))
              .replace('{{NAV}}', nav_i18n(rd('nav.html')))
              .replace('{{I18N_KEY}}', I.KEY)
              .replace('{{I18N_CODES}}', '|'.join(c for c, _ in I.LANGS[1:]))
              .replace('{{I18N_RTL}}', '|'.join(I.RTL))
              .replace('{{LANG_OPTIONS}}', lang_options(I))
              .replace('{{CLIMB}}', climb_cards())
              .replace('{{DESCENT}}', descent_cards())
              .replace('{{CLIMB_FREE}}', climb_free_note())
              .replace('{{DESCENT_FREE}}', descent_free_note())
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
    bad = check_i18n(tpl, I, table)
    if bad:
        sys.exit('block-camp hub: the translations do not match the page (nothing written):\n  ' + '\n  '.join(bad))
    tpl = tpl.replace('{{I18N_JSON}}', i18n_json(table))
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
    # newline='\n' matters: this repo is LF throughout, and on Windows the
    # default translates every \n to \r\n, so a one-line blurb edit comes back
    # as all 569 lines changed (CLAUDE.md, "Working from Windows").
    site = build(False)
    # The hub's theme tune (block-camp/music/block-camp-theme.m4a): the tag
    # comes from deck_music.py like every camp's, so it follows loops.json.
    sys.path.insert(0, os.path.join(REPO, 'lesson-template', 'build', 'block-camp-music'))
    import deck_music
    site = deck_music.set_music(site, 'block-camp.html')
    open(os.path.join(REPO,'block-camp.html'),'w',encoding='utf-8',newline='\n').write(site)
    prev = build(True)
    open(os.path.join(os.environ.get('PREVIEW_DIR') or tempfile.gettempdir(), 'block-camp-hub-preview.html'),
         'w',encoding='utf-8',newline='\n').write(prev)
    print('site', len(site), 'preview', len(prev))
