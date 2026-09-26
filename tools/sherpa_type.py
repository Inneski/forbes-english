#!/usr/bin/env python3
"""Faktum on every Sherpa page, and the type a size up.

    python tools/sherpa_type.py --install <Faktum-Font.zip>   # copy the web fonts in (once)
    python tools/sherpa_type.py                                # add or refresh the block on every page
    python tools/sherpa_type.py --check                        # exit 1 if a page is missing it or it is stale
    node   tools/sherpa_type_check.js                          # measure: Faktum everywhere, nothing overflows

Innes, 2026-09-26: "change text to Faktum font and make some bigger
including the main Title Sherpa Tensing" ... "faktum in all those pages".
All 26: the route map and every camp, descent and cloud page.

HOW. A page's own CSS is never edited. The tool reads it (every <style>
block but the generated ones), and for each rule that sets font-family or a
px font-size it writes the same rule into a fenced block, one class
stronger (`:root ` in front), inside the same @media. Every override beats
its original, and the overrides keep the originals' order among
themselves, so whatever rule won before wins again, now in Faktum and a
size up. Re-running rebuilds the same block from the same CSS; cutting the
block out restores the page.

SIZES. The "Sherpa Tensing" wordmark goes from 20px to clamp(30px, 5vw,
42px), and the line beside it ("Forbes English · a route up the tenses")
from 13px to clamp(14px, 1.6vw, 17px). Headings (20 to 40px) grow 15%; display sizes of 40px and up stay.
Everything under 20px grows 1px, with nothing under 12px. A clamp() keeps
its floor (it is already tuned for a phone) and grows its top. em sizes
are left alone: they follow their parent. SVG text keeps its sizes: the
diagrams are drawn to them. Form controls, which inherit no font, are set
to Faktum outright.

FONTS. Faktum (Rene Bieder) is self-hosted, like the Sailing lesson's.
It covers every Latin letter on these pages; symbols (check marks, arrows)
and Cyrillic, Arabic and CJK fall back glyph by glyph to Inter, which stays
loaded for that. Fraunces is dropped from the Google Fonts link.
"""
import io
import glob
import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = 'Sherpa Tensing/fonts'
FACES = [  # (file, weight, style)
    ('Faktum-Regular', 400, 'normal'), ('Faktum-RegularItalic', 400, 'italic'),
    ('Faktum-Medium', 500, 'normal'), ('Faktum-SemiBold', 600, 'normal'),
    ('Faktum-SemiBoldItalic', 600, 'italic'), ('Faktum-Bold', 700, 'normal'),
    ('Faktum-BoldItalic', 700, 'italic'), ('Faktum-ExtraBold', 800, 'normal')]
PRELOAD = ['Faktum-Regular', 'Faktum-SemiBold']
STACK = "'Faktum','Inter',system-ui,sans-serif"
WORDMARK = 'clamp(30px,5vw,42px)'          # Innes: "SHERPA TENSING should be bigger"
WORDMARK_SUB = 'clamp(14px,1.6vw,17px)'    # ... "and 'route up the tenses' too"
START, END = '<!-- SHERPA-TYPE:start -->', '<!-- SHERPA-TYPE:end -->'
FENCE = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)
GENERATED = ('sherpa-topo', 'sherpa-type')


def scale(px):
    if px < 12:
        return 12.0
    if px < 20:
        return px + 1
    if px >= 40:
        return px       # display sizes (the hub's title, camp two's big numerals) are big enough
    return round(px * 1.15 * 2) / 2


def fmt(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')


# components drawn to their own measure, which take Faktum but keep their sizes:
# camp two's frequency timeline overflowed a 390px screen by 11px when it grew
KEEP_SIZE = ('#frequency-timeline-deluxe',)


def new_size(v, sel):
    if any(k in sel for k in KEEP_SIZE):
        return None
    v = v.strip()
    imp = ' !important' if '!important' in v else ''
    v = v.replace('!important', '').strip()
    if re.search(r'(^|,)\s*\.wordmark \.brand\s*$', sel):
        return WORDMARK + imp
    if re.search(r'(^|,)\s*\.wordmark \.sub\s*$', sel):
        return WORDMARK_SUB + imp
    m = re.fullmatch(r'([\d.]+)px', v)
    if m:
        return fmt(scale(float(m.group(1)))) + 'px' + imp
    m = re.fullmatch(r'clamp\(\s*([\d.]+)px\s*,\s*([\d.]+)vw\s*,\s*([\d.]+)px\s*\)', v)
    if m:
        # a clamp is already tuned for the phone at its floor: grow only the top
        # (camp two's timeline overflowed a 390px screen when the floor grew too)
        a, b, c = map(float, m.groups())
        return 'clamp(%spx,%svw,%spx)%s' % (fmt(a), fmt(b * 1.15), fmt(scale(c)), imp)
    return None          # em, %, keywords: relative, left alone


def strip_comments(css):
    return re.sub(r'/\*.*?\*/', '', css, flags=re.S)


def blocks(css):
    """Top-level statements: (prelude, body) for rules and at-rules with a block."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find('{', i)
        if j < 0:
            break
        prelude = css[i:j].strip()
        depth, k, q = 1, j + 1, None
        while k < n and depth:
            ch = css[k]
            if q:
                if ch == '\\':
                    k += 1
                elif ch == q:
                    q = None
            elif ch in '"\'':
                q = ch
            elif ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            k += 1
        out.append((prelude.split(';')[-1].strip(), css[j + 1:k - 1]))
        i = k
    return out


def split_selectors(sel):
    parts, depth, cur = [], 0, ''
    for ch in sel:
        if ch in '([':
            depth += 1
        elif ch in ')]':
            depth -= 1
        if ch == ',' and depth == 0:
            parts.append(cur.strip())
            cur = ''
        else:
            cur += ch
    parts.append(cur.strip())
    return [p for p in parts if p]


def bump(sel):
    out = []
    for s in split_selectors(sel):
        m = re.match(r'(html|:root)(\S*)(.*)$', s)
        if m:
            out.append('%s%s:not(.st-x)%s' % m.groups())
        else:
            out.append(':root ' + s)
    return ','.join(out)


def overrides(css):
    rules = []
    for prelude, body in blocks(strip_comments(css)):
        if prelude.startswith('@media') or prelude.startswith('@supports'):
            inner = overrides(body)
            if inner:
                rules.append('%s{\n%s\n}' % (re.sub(r'\s+', ' ', prelude), inner))
        elif prelude.startswith('@'):
            continue                       # @font-face, @keyframes, @page
        else:
            decls = []
            for prop, val in re.findall(r'(?:^|;)\s*(font-family|font-size|font)\s*:\s*([^;]+)', body):
                if prop == 'font-family':
                    decls.append('font-family:var(--sherpa-font)%s' % (' !important' if '!important' in val else ''))
                elif prop == 'font-size':
                    v = new_size(val, prelude)
                    if v:
                        decls.append('font-size:' + v)
                else:
                    # the shorthand: [style] [weight] SIZE[/line-height] FAMILY -> scaled size, Faktum
                    if val.strip() in ('inherit', 'initial', 'unset', 'revert'):
                        continue                   # takes its parent's, which is already Faktum
                    m = re.match(r'(.*?)([\d.]+)px(/\S+)?\s+.+$', val.strip())
                    if not m:
                        sys.exit('! a font: shorthand sherpa_type.py cannot read: %s { font: %s }' % (prelude, val))
                    decls.append('font:%s%spx%s var(--sherpa-font)' % (m.group(1), fmt(scale(float(m.group(2)))), m.group(3) or ''))
            if decls:
                rules.append('%s{%s;}' % (bump(re.sub(r'\s+', ' ', prelude)), ';'.join(decls)))
    return '\n'.join(rules)


def page_css(src):
    return ''.join(m.group(2) for m in re.finditer(r'<style([^>]*)>(.*?)</style>', src, re.S)
                   if not any('id="%s"' % g in m.group(1) for g in GENERATED))


def block(src):
    url = lambda f: '%s/%s.woff2' % (FONT_DIR.replace(' ', '%20'), f)
    faces = '\n'.join("@font-face{font-family:'Faktum';src:url('%s') format('woff2');font-weight:%d;font-style:%s;font-display:swap;}"
                      % (url(f), w, s) for f, w, s in FACES)
    pre = '\n'.join('<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' % url(f) for f in PRELOAD)
    return (START + '\n' + pre + '\n<style id="sherpa-type">\n'
            '/* Faktum and the type a size up (tools/sherpa_type.py): each rule below repeats one of\n'
            '   the page\'s own, one class stronger, in the same order and @media */\n'
            + faces + '\n:root{--sherpa-font:%s;}\n' % STACK
            + ':root svg text,:root svg tspan{font-family:var(--sherpa-font);}\n'
            + '/* form controls do not inherit a font: without this, 30 buttons drew in Arial */\n'
            + ':root button,:root input,:root select,:root textarea{font-family:var(--sherpa-font);}\n'
            + overrides(page_css(src)) + '\n'
            + '/* the wordmark is a name: one line, and on a narrow screen it takes the row to\n'
            + '   itself, with the line beside it (or the hub\'s language menu) underneath */\n'
            + ':root .wordmark .brand{white-space:nowrap;}\n'
            + '@media (max-width:700px){:root .wordmark{flex-wrap:wrap;row-gap:6px;}'
            + ':root .wordmark .brand{flex:1 0 100%;}}\n'
            + '</style>\n' + END + '\n')


def drop_fraunces(src):
    return re.sub(r'family=Fraunces:[^&"]*&', '', src)


def pages():
    return sorted(glob.glob(os.path.join(ROOT, 'sherpa-tensing-*.html')))


def install(zpath):
    os.makedirs(os.path.join(ROOT, FONT_DIR), exist_ok=True)
    z = zipfile.ZipFile(zpath)
    for f, _, _ in FACES:
        data = z.read('Faktum-Font/%s.woff2' % f)
        open(os.path.join(ROOT, FONT_DIR, f + '.woff2'), 'wb').write(data)
        print('  %s/%s.woff2  %d bytes' % (FONT_DIR, f, len(data)))


def main():
    if '--install' in sys.argv:
        return install(sys.argv[sys.argv.index('--install') + 1])
    check = '--check' in sys.argv
    bad = [('font missing: %s/%s.woff2' % (FONT_DIR, f)) for f, _, _ in FACES
           if not os.path.exists(os.path.join(ROOT, FONT_DIR, f + '.woff2'))]
    for p in pages():
        src = io.open(p, encoding='utf-8').read()
        name = os.path.basename(p)
        base = FENCE.sub('', src)
        # rewrite the block where it stands (tools/sherpa_topo.py keeps one beside it,
        # and moving either would make the other look stale); insert only when absent
        b = block(base)
        new = drop_fraunces(FENCE.sub(lambda m: b, src, count=1) if FENCE.search(src)
                            else src.replace('</head>', b + '</head>', 1))
        if check:
            if new != src:
                bad.append('%s: type block missing or stale' % name)
        elif new != src:
            io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
            print('  ' + name)
    for b in bad:
        print('FAIL ' + b)
    if check:
        print('PASS: %d pages' % len(pages()) if not bad else 'FAIL: %d problem(s)' % len(bad))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
