#!/usr/bin/env python3
"""Pull the text and pictures out of a *static-markup* standalone RPG export.

    py lesson-template/build/rpg/extract_static.py <export.html> <slug>

README.md §2 names three export kinds and says "a fourth kind means: read its
script first, then decide which of the three it is closest to". This is the
fourth, and Nautilus: The Black Archive ("Minecraft Edition") is the first of
it. It carries no game object at all — no `window.*_GAME_DATA`, no
`EMBEDDED_SCENES`, no patch stack. Every scene is already rendered markup:

    <section class="scene" data-hull=".." data-oxygen=".." data-score=".." id="q0">
      <img src="data:image/webp;base64,...">
      <div class="panel">
        <div class="kicker">01 · THE SIGNAL</div>
        <p class="story">...</p>
        <div class="question">Captain Nemo <em>___</em> for ...</div>
        <div class="answers">
          <a class="choice answerLink" data-correct="1" data-why="..." href="#route">2. has been searching</a>
          ...

so the text needs no execution, only parsing — the easiest of the four. The
script tag holds nothing but the engine (scoring, hash routing, the feedback
box); every learner-facing string is in the DOM.

Two things the export does NOT carry, which the builder must supply: any
language but English (there is no `local` block and no `de`/`es` attribute
anywhere), and a picture per ending — it has one `#end` scene whose title and
paragraph are chosen in JavaScript from the score.

Output matches extract_standalone.py so the rest of the pipeline is unchanged:

  * `block-camp/<slug>/NN_<id>.webp` — the pictures, numbered in scene order;
  * `lesson-template/build/rpg/<slug>/data.json` — the text;
  * a printed scene list to fill the hotspot table from (README §3).
"""
import base64, json, os, re, struct, sys
from html import unescape

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))

TAG = re.compile(r'<[^>]+>')


def text(html, br='\n'):
    """Visible text of a fragment, with the blank kept as ___.

    `<br>` becomes `br`. The rule cards separate the meaning line from the
    form line with one, and stripping tags without it welds 'achievement'
    to 'have/has'.
    """
    html = re.sub(r'<em>(.*?)</em>', r'\1', html, flags=re.S)
    html = re.sub(r'<br\s*/?>', '\x00', html)
    out = re.sub(r'[ \t\r\n]+', ' ', unescape(TAG.sub('', html)))
    return re.sub(r'(\s*\x00\s*)+', br, out).strip().strip(br)


def webp_size(b):
    if b[12:16] == b'VP8X':
        return int.from_bytes(b[24:27], 'little') + 1, int.from_bytes(b[27:30], 'little') + 1
    if b[12:16] == b'VP8 ':
        return struct.unpack('<H', b[26:28])[0] & 0x3fff, struct.unpack('<H', b[28:30])[0] & 0x3fff
    if b[12:16] == b'VP8L':
        n = int.from_bytes(b[21:25], 'little')
        return (n & 0x3fff) + 1, ((n >> 14) & 0x3fff) + 1
    return None


def main(src, slug):
    s = open(src, encoding='utf-8').read()
    if 'GAME_DATA' in s or 'EMBEDDED_SCENES' in s:
        raise SystemExit('%s carries a game object — use extract_standalone.py' % src)

    img_dir = os.path.join(REPO, 'block-camp', slug)
    os.makedirs(img_dir, exist_ok=True)
    scenes, sizes, n = {}, set(), 0

    for m in re.finditer(r'<section class="scene"([^>]*)>(.*?)</section>', s, re.S):
        attrs, body = m.group(1), m.group(2)
        sid = re.search(r'id="([^"]+)"', attrs).group(1)
        sc = {'id': sid}
        for k in ('hull', 'oxygen', 'score'):
            v = re.search(r'data-%s="(-?\d+)"' % k, attrs)
            if v and int(v.group(1)):
                sc[k] = int(v.group(1))

        img = re.search(r'<img ([^>]*)src="data:image/(\w+);base64,([^"]+)"', body)
        if img:
            n += 1
            ext = img.group(2)
            name = '%02d_%s.%s' % (n, sid, ext)
            b = base64.b64decode(img.group(3))
            open(os.path.join(img_dir, name), 'wb').write(b)
            sizes.add(webp_size(b))
            sc['img'] = name
            alt = re.search(r'alt="([^"]*)"', img.group(1))
            if alt:
                sc['alt'] = unescape(alt.group(1))

        for key, pat in (('kicker', r'<div class="kicker">(.*?)</div>'),
                         ('title', r'<h1[^>]*>(.*?)</h1>'),
                         ('big', r'<div class="big"[^>]*>(.*?)</div>'),
                         ('badge', r'<div class="campaignBadge">(.*?)</div>')):
            v = re.search(pat, body, re.S)
            if v:
                sc[key] = text(v.group(1), br=' ')

        story = [text(x, br=' ') for x in re.findall(r'<p class="story">(.*?)</p>', body, re.S)]
        if story:
            sc['story'] = story

        q = re.search(r'<div class="question">(.*?)</div>', body, re.S)
        if q:
            sc['prompt'] = text(q.group(1), br=' ')

        opts = []
        for a in re.finditer(r'<a class="choice answerLink"([^>]*)>(.*?)</a>', body, re.S):
            at, label = a.group(1), text(a.group(2), br=' ')
            opts.append({
                'text': re.sub(r'^\d+\.\s*', '', label),
                'correct': re.search(r'data-correct="(\d)"', at).group(1) == '1',
                'why': unescape(re.search(r'data-why="([^"]*)"', at).group(1)),
                'next': re.search(r'href="#([^"]+)"', at).group(1),
            })
        if opts:
            sc['opts'] = opts

        routes = []
        for a in re.finditer(r'<a class="choice decisionLink"([^>]*)>(.*?)</a>', body, re.S):
            at = a.group(1)
            r = {'text': re.sub(r'^\d+\.\s*', '', text(a.group(2), br=' ')),
                 'next': re.search(r'href="#([^"]+)"', at).group(1)}
            for k in ('points', 'route'):
                v = re.search(r'data-%s="([^"]*)"' % k, at)
                if v:
                    r[k] = v.group(1)
            routes.append(r)
        if routes:
            sc['routes'] = routes

        rules = [(text(a), text(b)) for a, b in
                 re.findall(r'<div class="rule">\s*<b>(.*?)</b>(.*?)</div>', body, re.S)]
        if rules:
            sc['rules'] = [{'head': h, 'body': t} for h, t in rules]

        nxt = re.findall(r'<a class="next"[^>]*href="#([^"]+)"', body)
        if nxt:
            sc['next'] = nxt[0]

        scenes[sid] = sc

    out_dir = os.path.join(HERE, slug)
    os.makedirs(out_dir, exist_ok=True)
    data = {'source': os.path.basename(src),
            'title': text(re.search(r'<title>(.*?)</title>', s).group(1)),
            'scenes': scenes}
    out = os.path.join(out_dir, 'data.json')
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    print('%d pictures -> block-camp/%s/  sizes %s' % (n, slug, sorted(sizes, key=str)))
    if sizes - {(1536, 1024)}:
        print('  ! not 3:2 at 1536x1024 — pass img_w/img_h in the spec so the hotspots land')
    print('text -> %s' % os.path.relpath(out, REPO))
    print('langs in export: en only — every gloss must be written (README §1)')
    print('\nscenes (fill HOT from a gridded contact sheet):')
    for sid, sc in scenes.items():
        kind = ('question' if 'opts' in sc else 'choice' if 'routes' in sc
                else 'rules' if 'rules' in sc and sid != 'end' else 'story')
        print('  %-10s %-9s %-22s %s' % (sid, kind, sc.get('img', '-'),
                                         (sc.get('kicker') or sc.get('big') or '')[:40]))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: extract_static.py <export.html> <slug>')
    main(sys.argv[1], sys.argv[2])
