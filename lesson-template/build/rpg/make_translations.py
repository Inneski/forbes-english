#!/usr/bin/env python3
"""Turn a ChatGPT-kind export's own `local` blocks into translations/<lang>.json.

    python3 lesson-template/build/rpg/make_translations.py <slug>

A ChatGPT-kind export (docs/CHATGPT-RPG-BRIEF.md) already carries all nine of
HOUSE-STYLE §8's languages on every learner-facing string, nested beside the
English it glosses. `rpg.apply_translations()` wants the opposite shape — one
flat `{English: translation}` map per language — so this flattens the nesting
once, rather than the builder reading `local` inline the way
build_lost_yellow_road.py does for its two languages.

Reads `rpg/<slug>/data.json`, writes `rpg/<slug>/translations/*.json`. Written
for A Fistful of Lies and generalised the moment a second export needed exactly
the same pass; four lessons use it now.

Rerunnable and lossless: it only ever reads data.json. Strings the builder
invents (the HUD label overrides, the briefing kicker) are not in the export
and are written out in the builder itself, in all nine.

It also reports collisions — one English string glossed two different ways in
the same language — because a flat map keyed by English silently keeps the
last one. There are none today; if a future re-export introduces one, that
string has to be disambiguated in the builder before this file can be trusted.
"""
import json, os, sys

if len(sys.argv) != 2:
    raise SystemExit(__doc__.strip().splitlines()[2].strip())
SLUG = os.path.basename(os.path.normpath(sys.argv[1]))
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), SLUG)
if not os.path.isdir(HERE):
    raise SystemExit('no such lesson directory: %s' % HERE)
LANGS = ('es', 'de', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja')
DATA = json.load(open(os.path.join(HERE, 'data.json'), encoding='utf-8'))

out = {l: {} for l in LANGS}
clash = []


def keep(l, en, tr, where):
    if out[l].get(en, tr) != tr:
        clash.append('%s [%s] %r -> %r / %r' % (where, l, en[:50], out[l][en][:40], tr[:40]))
    out[l][en] = tr


def pair(en, loc, key, where):
    """One English string against its gloss in every language."""
    for l in LANGS:
        tr = loc.get(l, {}).get(key)
        if isinstance(tr, str) and tr:
            keep(l, en, tr, where)


def pair_list(ens, loc, key, where):
    """A list of plain strings, glossed position by position (the cover chips)."""
    for i, en in enumerate(ens):
        for l in LANGS:
            seq = loc.get(l, {}).get(key)
            if seq and i < len(seq) and isinstance(seq[i], str):
                keep(l, en, seq[i], '%s[%d]' % (where, i))


def pair_dicts(items, loc, key, fields, where):
    """A list of objects (briefing cards, route choices), glossed field by field."""
    for i, it in enumerate(items):
        for l in LANGS:
            seq = loc.get(l, {}).get(key)
            if not seq or i >= len(seq):
                continue
            for f in fields:
                tr = seq[i].get(f)
                if isinstance(tr, str) and tr:
                    keep(l, it[f], tr, '%s[%d].%s' % (where, i, f))


c = DATA['cover']
for k in ('eyebrow', 'title', 'lead', 'start', 'small'):
    pair(c[k], c['local'], k, 'cover.' + k)
pair_list(c['rules'], c['local'], 'rules', 'cover.rules')

b = DATA['briefing']
for k in ('title', 'note', 'button'):
    pair(b[k], b['local'], k, 'briefing.' + k)
pair_dicts(b['cards'], b['local'], 'cards', ('head', 'text'), 'briefing.cards')

for sid, s in DATA['scenes'].items():
    for k in ('act', 'title', 'story', 'clue', 'prompt', 'explanation'):
        if k in s:
            pair(s[k], s['local'], k, '%s.%s' % (sid, k))
    if 'choices' in s:
        pair_dicts(s['choices'], s['local'], 'choices', ('label', 'note'), sid + '.choices')

for key, e in DATA['endings'].items():
    for k in ('label', 'title', 'text'):
        pair(e[k], e['local'], k, 'end_%s.%s' % (key, k))
    # the route-conditional closing paragraph, keyed by route rather than by field
    for route, en in (e.get('routeTexts') or {}).items():
        for l in LANGS:
            tr = (e['local'].get(l, {}).get('routeTexts') or {}).get(route)
            if isinstance(tr, str) and tr:
                keep(l, en, tr, 'end_%s.routeTexts.%s' % (key, route))

if clash:
    print('%d collisions — one English, two glosses:' % len(clash), file=sys.stderr)
    for c_ in clash:
        print('  ' + c_, file=sys.stderr)
    raise SystemExit(1)

d = os.path.join(HERE, 'translations')
os.makedirs(d, exist_ok=True)
for l in LANGS:
    with open(os.path.join(d, '%s.json' % l), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(out[l], f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')
    print('%s/%s.json  %d strings' % (SLUG, l, len(out[l])))
