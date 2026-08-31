#!/usr/bin/env python3
"""Make a deck that survives being sent on its own.

A Block Camp deck points at ~21 background plates by relative path. Sent into
a conversation by itself it arrives BLANK - Innes, on the first one:
"no images appear in this". This rewrites every local reference as a data URI
and then REFUSES to write the file if a local reference is still in it, so the
failure can never reach him silently again.

The template's own comments contain example paths (data-bg="folder/other.jpg"),
so comments are masked out before the check - otherwise the gate fails on
documentation.

    python3 lesson-template/descent/inline_preview.py deck.html out-PREVIEW.html
"""
import base64, mimetypes, os, re, sys


def inline(path, out):
    src = open(path, encoding='utf-8').read()
    root = os.path.dirname(os.path.abspath(path))
    seen = {}

    def uri(rel):
        if rel not in seen:
            p = os.path.join(root, rel)
            if not os.path.exists(p):
                seen[rel] = None
            else:
                mime = mimetypes.guess_type(p)[0] or 'application/octet-stream'
                seen[rel] = 'data:%s;base64,%s' % (
                    mime, base64.b64encode(open(p, 'rb').read()).decode())
        return seen[rel]

    def swap(m):
        pre, rel, post = m.group(1), m.group(2), m.group(3)
        u = uri(rel)
        return m.group(0) if u is None else pre + u + post

    # data-bg="folder/file.jpg"  and  url('folder/file.jpg')  and  src="..."
    pats = [r'(data-bg=")([^"]+\.(?:jpg|jpeg|png|webp))(")',
            r"(url\(')([^']+\.(?:jpg|jpeg|png|webp))('\))",
            r'(src=")([^"]+\.(?:jpg|jpeg|png|webp))(")']
    for p in pats:
        src = re.sub(p, swap, src)

    # the gate: nothing local may remain
    masked = re.sub(r'<!--.*?-->', '', src, flags=re.S)
    left = set()
    for p in pats:
        for m in re.finditer(p, masked):
            if not m.group(2).startswith(('data:', 'http')):
                left.add(m.group(2))
    if left:
        raise SystemExit('REFUSING TO WRITE %s - still points at local files:\n  %s'
                         % (out, '\n  '.join(sorted(left))))

    open(out, 'w', encoding='utf-8').write(src)
    print('%s  %.1f MB  (%d plates inlined)'
          % (out, os.path.getsize(out) / 1e6, len([v for v in seen.values() if v])))


if __name__ == '__main__':
    inline(sys.argv[1], sys.argv[2])
