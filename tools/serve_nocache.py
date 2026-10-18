"""Serve the repo locally with caching switched off.

    py tools/serve_nocache.py [port]        # default 8099

`py -m http.server` sends Last-Modified and no Cache-Control, so Chrome
caches pages heuristically and keeps showing a build that has since been
rewritten. On 2026-10-18 Innes reviewed the homepage draft in Chrome and
saw a yacht and gulls that had already been put back to size; the file on
disk was right, the browser was not. Every response from this server says
no-store, so a plain reload always shows what is on disk.
"""
import http.server
import os
import sys


class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8099
    http.server.ThreadingHTTPServer(('', port), NoCache).serve_forever()
