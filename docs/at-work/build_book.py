"""Lay out one book of Forbes English at Work as A4 pages, editorial style.

    py docs/at-work/build_book.py 1        -> docs/at-work/book-1.html
    node docs/at-work/print_book.js 1      -> docs/at-work/book-1.pdf

Reads the unit specs in level-<n>-*.md and the exercise content in
content_book<n>.py, and emits one HTML file of fixed 210 x 297 mm pages,
eight per unit, plus front and back matter.

The compositions follow HOUSE-STYLE §15, the editorial style: a flat cream
field, no plates under text, the heading across the full width and the
picture in a framed column under it — right or left, rounded or arched, a
39% plate beside 56% of text or a 30% plate beside 65%. Sides alternate by
unit so facing pages do not mirror each other. The one exception is the
unit opener, which carries its hero right across the top of the page.

Every picture is a dashed slot named after its artwork slot (u03-opener,
u03-scene) or its job (picture to label, spot). Every exercise on the page
is real text: the vocabulary set, the dialogue, the phrase box, the case
and the homework come from the spec; the matching task, the message
thread, the rule cards, the practice, the gist questions, the role cards,
the listening and the pronunciation note come from content_book<n>.py.
All of it is an AI draft until Innes replaces it; the dialogue says so on
the page.

The palette is the editorial set from HOUSE-STYLE §15 with the book's
accent (README §7) as the one accent. Not derived from a hero — there is
none yet.
"""
import html
import importlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
BOOKS = {
    1: ("level-1-day-one.md", "Day", "One", "A1/A2", "#e8735a", "coral"),
    2: ("level-2-joining-in.md", "Joining", "In", "A2/B1", "#2f8f7a", "sea green"),
    3: ("level-3-taking-charge.md", "Taking", "Charge", "B1+/B2", "#e0a020", "amber"),
    4: ("level-4-setting-the-course.md", "Setting the", "Course", "B2/C1", "#2451b3", "cobalt"),
    5: ("level-5-the-long-game.md", "The Long", "Game", "C1/C2", "#6b2d5c", "plum"),
}
LOGO = (HERE.parent.parent / "lesson-template" / "forbes-logo.svgfrag").read_text(encoding="utf-8")


# ---------------------------------------------------------------- parsing

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = s.replace("___", '<span class="gap">&nbsp;</span>')
    return s


def section(block, head, nxt):
    m = re.search(re.escape(head) + r"(.*?)(?=" + "|".join(re.escape(n) for n in nxt) + r"|\Z)", block, re.S)
    return m.group(1).strip() if m else ""


def bullets(text):
    return [ln[2:].strip() for ln in text.splitlines() if ln.startswith("- ")]


def parse_units(md):
    parts = re.split(r"^## Unit (\d+) · (.+)$", md, flags=re.M)
    units = []
    for i in range(1, len(parts), 3):
        n, title, body = int(parts[i]), parts[i + 1].strip(), parts[i + 2]
        u = {"n": n, "title": title}
        u["strap"] = re.search(r"^\*(.+?)\*\s*$", body, re.M).group(1)
        u["cando"] = section(body, "**Can do:**", ["**Scenario.**"])
        u["scenario"] = section(body, "**Scenario.**", ["| strand |"])
        u["rows"] = dict(re.findall(r"^\| (Vocabulary|Grammar|Communication|In the Room) \| (.+?) \|\s*$", body, re.M))
        u["leadin"] = section(body, "**Lead-in.**", ["**Grammar in the dialogue.**"])
        u["gramlines"] = bullets(section(body, "**Grammar in the dialogue.**", ["**In the Room — phrase box.**"]))
        u["phrases"] = bullets(section(body, "**In the Room — phrase box.**", ["**Model dialogue.**"]))
        dlg = section(body, "**Model dialogue.**", ["**The case.**"])
        u["dialogue"] = [ln.strip() for ln in dlg.splitlines() if ln.strip()]
        case = section(body, "**The case.**", ["**Homework.**", "**Artwork.**"])
        u["speak"] = re.search(r"\*Speak:\*\s*(.+)", case).group(1)
        u["write"] = re.search(r"\*Write:\*\s*(.+)", case).group(1)
        hw = section(body, "**Homework.**", ["**Artwork.**"])
        u["do"] = re.search(r"\*Do:\*\s*(.+)", hw).group(1)
        u["items"] = re.findall(r"^\s+\d\.\s+(.+)$", hw, re.M)
        u["key"] = re.search(r"\*Key:\*\s*(.+)", hw).group(1)
        art = section(body, "**Artwork.**", ["\n---", "\n## "])
        u["art"] = dict(re.findall(r"`(u\d\d-(?:opener|scene))` — (.+)", art))
        units.append(u)
    return units


def vocab_groups(row):
    out = []
    for grp in row.split("·"):
        grp = grp.strip()
        m = re.match(r"\*([^*]+):\*\s*(.*)", grp)
        label, rest = (m.group(1), m.group(2)) if m else ("", grp)
        words = [w.strip() for w in re.split(r",(?![^()]*\))", rest) if w.strip()]
        out.append((label, words))
    return out


def you_question(leadin):
    sents = re.findall(r"[^.?!]+[.?!]", leadin)
    mine = [s.strip() for s in sents if re.search(r"\byou\b", s) and "picture" not in s]
    return " ".join(mine) if mine else sents[0].strip()


# ---------------------------------------------------------------- pieces

def plate(name, subject, h, shape="round"):
    sub = f'<div class="slot-sub">{inline(subject)}</div>' if subject else ""
    return (f'<div class="plate {shape}" style="height:{h}">'
            f'<div class="slot-tag">illustration · {html.escape(name)}</div>{sub}</div>')


def split(text, art, side="right", size="wide"):
    """Heading already placed; the body yields a column to the picture."""
    return f'<div class="split {side} {size}"><div class="col-text">{text}</div><div class="col-art">{art}</div></div>'


def lines(n, gap="7.5mm"):
    return "".join(f'<div class="rule-line" style="height:{gap}"></div>' for _ in range(n))


def numbered(items, cls="ex", answer_line=True):
    li = "".join(f'<li>{inline(it)}{"<div class=ans></div>" if answer_line else ""}</li>' for it in items)
    return f'<ol class="{cls}">{li}</ol>'


def page(inner, head="", num=None, cls=""):
    foot = (f'<div class="foot"><span>{html.escape(head)}</span><span>{num if num else ""}</span></div>'
            if (head or num) else "")
    return f'<section class="page {cls}">{inner}{foot}</section>\n'


def h(eyebrow, title, big=False):
    tag = "h1" if big else "h2"
    return f'<div class="eyebrow">{eyebrow}</div><{tag}>{title}</{tag}>'


def strand_menu(u):
    return ('<table class="menu">' + "".join(
        f'<tr><th>{k}</th><td>{inline(u["rows"][k])}</td></tr>'
        for k in ("Vocabulary", "Grammar", "Communication", "In the Room")) + "</table>")


def match_ex(pairs, n):
    words = [w for w, _ in pairs]
    means = [m for _, m in pairs]
    rot = (n * 3) % len(means) or 2
    shuffled = means[rot:] + means[:rot]
    left = "".join(f'<li><span class="letter">{"abcdef"[i]}</span> {inline(w)}</li>' for i, w in enumerate(words))
    right = "".join(f"<li>{inline(m)}</li>" for m in shuffled)
    key = " · ".join(f"{'abcdef'[i]}{shuffled.index(m) + 1}" for i, m in enumerate(means))
    return f'<div class="match"><ul class="words">{left}</ul><ol class="means">{right}</ol></div>', key


def thread_ex(thread):
    intro, lns, bank, _key = thread
    chips = "".join(f'<span class="chip">{inline(b)}</span>' for b in sorted(bank, key=str.lower))
    body = "".join(f"<p>{inline(l)}</p>" for l in lns)
    return f'<div class="bank">{chips}</div><div class="thread"><div class="thread-head">{inline(intro)}</div>{body}</div>'


def dialogue_html(u):
    out = []
    for ln in u["dialogue"]:
        m = re.match(r"^([A-ZÀ-Þ][A-ZÀ-Þ .'\-]+):\s+(.*)$", ln)
        if m:
            out.append(f'<div class="turn"><span class="who">{html.escape(m.group(1).title())}</span><span class="say">{inline(m.group(2))}</span></div>')
        else:
            out.append(f'<p class="stage">{inline(ln)}</p>')
    return "".join(out)


# ---------------------------------------------------------------- unit pages

def unit_pages(u, c, start):
    """Six pages: opener · vocabulary · grammar · listen and read · in the room · case and homework."""
    n, T = u["n"], u["title"]
    head = f"Unit {n} · {T}"
    A = "right" if n % 2 else "left"          # the unit's main side
    B = "left" if A == "right" else "right"
    so, ss = f"u{n:02d}-opener", f"u{n:02d}-scene"
    P = []

    # 1 · opener: the hero right across the top
    cando = [x.strip() for x in re.split(r";\s*", u["cando"]) if x.strip()]
    P.append(page(
        plate(so, u["art"].get(so, ""), "126mm", "hero")
        + '<div class="body tight-top">'
        + h(f"Unit {n}", inline(T), big=True)
        + f'<p class="strap">{inline(u["strap"])}</p>'
        + split('<h3>In this unit you can</h3><ul class="cando">' + "".join(f"<li>{inline(x)}</li>" for x in cando) + "</ul>"
                f'<h3>Lead-in</h3><p class="lead">{inline(u["leadin"])}</p>',
                f'<h3>The unit</h3>{strand_menu(u)}', "right", "half")
        + f'<h3>The story</h3><p class="story">{inline(u["scenario"])}</p></div>',
        head, start, "opener"))

    # 2 · vocabulary: arch plate, word bank + matching beside it, thread below
    chips = "".join(
        f'<div class="group">{("<span class=glabel>" + html.escape(g) + "</span>") if g else ""}'
        + "".join(f'<span class="chip">{inline(w)}</span>' for w in ws) + "</div>" for g, ws in vocab_groups(u["rows"]["Vocabulary"]))
    m_html, m_key = match_ex(c["match"], n)
    P.append(page(
        '<div class="body">' + h("Vocabulary", inline(T))
        + split(f'<div class="wordbank">{chips}</div><h3>1 · Match the word to its meaning</h3>{m_html}',
                plate("picture to label", "the vocabulary set in one scene from the unit's story, numbered", "104mm", "arch"), A)
        + f'<h3>2 · Complete the text with words from the box</h3>{thread_ex(c["thread"])}'
        + f'<h3>3 · You</h3><p class="q">{inline(you_question(u["leadin"]))}</p>{lines(2)}</div>',
        head, start + 1))

    # 3 · grammar: rule beside a narrow plate; practice and the word-choice items below
    cards = "".join(f'<div class="card"><h4>{t}</h4><p>{inline(c[k])}</p></div>' for t, k in (("Form", "form"), ("Use", "use"), ("Watch out", "watch")))
    P.append(page(
        '<div class="body">' + h("Grammar", inline(u["rows"]["Grammar"].split(":")[0].split(" — ")[0]))
        + split('<h3>In the dialogue</h3><ol class="gram">' + "".join(f"<li>{inline(g)}</li>" for g in u["gramlines"]) + "</ol>"
                f'<h3>The rule</h3><div class="cards">{cards}</div>',
                plate("spot", f"the grammar in action: {u['gramlines'][0]}", "104mm", "round"), B, "narrow")
        + f'<h3>1 · Practice</h3>{numbered([p for p, _ in c["practice"]], "ex two-col")}'
        + f'<h3>2 · Choose the right word</h3>{numbered([p for p, _ in c["controlled"]], "ex two-col", answer_line=False)}'
        + '<p class="ref">Grammar reference: at the back of the book.</p></div>',
        head, start + 2))

    # 4 · listen and read: the dialogue beside the scene plate
    P.append(page(
        '<div class="body">' + h(f"Communication · {inline(u['rows']['Communication'])}", "Listen and read")
        + '<div class="draft">AI draft dialogue — to be replaced</div>'
        + split(f'<div class="dialogue">{dialogue_html(u)}</div>',
                plate(ss, u["art"].get(ss, ""), "140mm", "arch"), A)
        + '<h3>1 · Listen and answer</h3>' + numbered([q for q, _ in c["gist"]], "ex two-col")
        + '<h3>2 · Now you</h3><p>Read the dialogue in pairs. Then read it again and change three things: a name, a place and one number or time. Your partner listens for the changes.</p>'
        + f'<h3>3 · Role-play</h3><p class="q"><strong>Task.</strong> {inline(u["speak"])}</p>'
        f'<div class="role"><span class="rolelabel">A</span><p>{inline(c["roleA"])}</p></div>'
        f'<div class="role"><span class="rolelabel">B</span><p>{inline(c["roleB"])}</p></div></div>',
        head, start + 3))

    # 5 · in the room: phrase box beside an arch plate; listen; one-minute role-play; say it right
    P.append(page(
        '<div class="body">' + h("In the Room", inline(u["rows"]["In the Room"]))
        + split('<div class="phrases"><h3>Phrase box</h3><ul>' + "".join(f"<li>{inline(p)}</li>" for p in u["phrases"]) + "</ul></div>",
                plate("spot", "the phrase box in use: a small scene from the listening", "78mm", "arch"), B)
        + '<h3>1 · Listen and answer</h3>' + numbered([q for q, _ in c["listen"]], "ex two-col")
        + f'<h3>2 · One-minute role-play</h3><p>{inline(c["mini"])}</p>'
        + f'<div class="sayit"><h3>Say it right</h3><p>{inline(c["pron"])}</p></div>'
        + f'<h3>3 · Write it down</h3><p>Write the four phrases from the box you will use most, and one situation at work where each one helps.</p>{lines(4)}</div>',
        head, start + 4))

    # 6 · the case and the homework
    P.append(page(
        '<div class="body">' + h("The Case", inline(T))
        + split(f'<h3>Speak</h3><p>{inline(u["speak"])}</p><h3>Write</h3><p>{inline(u["write"])}</p>{lines(5)}',
                plate("spot", "the case's situation, from the unit's story", "92mm", "round"), A)
        + '<div class="hw">' + h("Homework", "")
        + split(f'<h3>Do</h3><p>{inline(u["do"])}</p>{lines(3)}',
                '<h3>Self-check</h3>' + numbered(u["items"], "ex selfcheck compact"), "right", "half")
        + '<p class="ref">Answers: in the key at the back of the book.</p></div></div>',
        head, start + 5))
    return P, m_key


# ---------------------------------------------------------------- book

def chunks(seq, size):
    return [seq[i:i + size] for i in range(0, len(seq), size)]


def build(book):
    fname, t1, t2, cefr, accent, accent_word = BOOKS[book]
    md = (HERE / fname).read_text(encoding="utf-8")
    units = parse_units(md)
    sys.path.insert(0, str(HERE))
    C = importlib.import_module(f"content_book{book}").C
    company = re.search(r"^\*\*The company\.\*\*(.+?)(?=\n\n)", md, re.S | re.M).group(1).strip()
    year = re.search(r"^\*\*The year\.\*\*(.+?)(?=\n\n)", md, re.S | re.M).group(1).strip()
    readme = (HERE / "README.md").read_text(encoding="utf-8")
    cast_block = re.search(r"\*\*Book %d — (.+?)\*\*\n\n(\| name.+?)(?=\n\n)" % book, readme, re.S)
    cast = re.findall(r"^\| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$", cast_block.group(2), re.M)[1:]
    setting = cast_block.group(1)
    btitle = f"{t1} {t2}"

    pages = []
    pages.append(page(
        plate(f"book-{book}-cover", f"the Unit 1 opener cropped to the front board; quiet space bottom-left; accent {accent_word}", "297mm", "cover-art")
        + f'<div class="cover-lockup">{LOGO}<div class="cover-series">Forbes English at Work</div>'
        f'<div class="cover-title">{html.escape(t1)} <em>{html.escape(t2)}</em></div>'
        f'<div class="cover-level">Book {book} · {html.escape(cefr)}</div></div>', cls="cover"))
    def maprows(us):
        return "".join(
            f'<tr><td class="num">{u["n"]}</td><td class="t">{inline(u["title"])}</td>'
            + "".join(f"<td>{inline(u['rows'][k])}</td>" for k in ("Vocabulary", "Grammar", "Communication", "In the Room")) + "</tr>" for u in us)
    mhead = '<tr><th></th><th>Unit</th><th>Vocabulary</th><th>Grammar</th><th>Communication</th><th>In the Room</th></tr>'
    pages.append(page('<div class="body">' + h("Map of the book", html.escape(btitle), big=True)
                      + f'<table class="map">{mhead}{maprows(units[:8])}</table></div>', "Map of the book", 2))
    pages.append(page('<div class="body">' + h("Map of the book", "Units 9 to 15")
                      + f'<table class="map">{mhead}{maprows(units[8:])}</table></div>', "Map of the book", 3))
    people = "".join(f'<div class="person">{plate("silhouette", f"{name}: {known}", "44mm", "arch")}<h4>{html.escape(name)}</h4><p>{inline(role)}</p></div>'
                     for name, role, _p, known in cast)
    pages.append(page('<div class="body">' + h("Meet the team", html.escape(setting), big=True)
                      + split(f'<p class="story">{inline(company)}</p><p class="story">{inline(year)}</p>',
                              plate("the office", "the whole team in one wide scene of the workplace, the props visible", "80mm", "round"), "right")
                      + f'<div class="people">{people}</div></div>', "Meet the team", 4))

    num = 5
    match_keys = {}
    for u in units:
        P, mk = unit_pages(u, C[u["n"]], num)
        pages.extend(P)
        match_keys[u["n"]] = mk
        num += 6

    # grammar reference
    for chunk in chunks(units, 4):
        pages.append(page('<div class="body">' + h("Grammar reference", "The rules in full") + "".join(
            f'<div class="refunit"><h4>Unit {u["n"]} · {inline(u["title"])}</h4><p>{inline(C[u["n"]]["ref"])}</p></div>' for u in chunk)
            + "</div>", "Grammar reference", num)); num += 1
    # audio scripts
    for chunk in chunks(units, 3):
        pages.append(page('<div class="body">' + h("Audio scripts", "In the Room listenings") + "".join(
            f'<div class="scriptunit"><h4>Unit {u["n"]} · {inline(u["rows"]["In the Room"])}</h4>'
            + "".join(f'<div class="turn"><span class="who">{html.escape(w)}</span><span class="say">{inline(l)}</span></div>' for w, l in C[u["n"]]["script"])
            + "</div>" for u in chunk) + "</div>", "Audio scripts", num)); num += 1
    # phrase bank
    for chunk in chunks(units, 8):
        pages.append(page('<div class="body">' + h("In the Room", "Phrase bank") + '<div class="bankgrid">' + "".join(
            f'<div><h4>Unit {u["n"]} · {inline(u["rows"]["In the Room"])}</h4><ul class="tight">' + "".join(f"<li>{inline(p)}</li>" for p in u["phrases"]) + "</ul></div>"
            for u in chunk) + "</div></div>", "Phrase bank", num)); num += 1
    # word list
    words = {}
    for u in units:
        for _g, ws in vocab_groups(u["rows"]["Vocabulary"]):
            for w in ws:
                w = re.sub(r"\*", "", w)
                words.setdefault(w.lower(), (w, set()))[1].add(u["n"])
    items = sorted(words.items())
    half = (len(items) + 1) // 2
    for part, title in ((items[:half], "A to " + items[half - 1][1][0][0].upper()), (items[half:], items[half][1][0][0].upper() + " to Z")):
        wl = "".join(f'<li>{inline(w)} <span class="unit">{", ".join(str(x) for x in sorted(ns))}</span></li>' for _k, (w, ns) in part)
        pages.append(page('<div class="body">' + h("Word list", title) + f'<ul class="wordlist">{wl}</ul></div>', "Word list", num)); num += 1
    # answer key
    def keyblock(u):
        c = C[u["n"]]
        rows = [("Vocabulary 1", match_keys[u["n"]]), ("Vocabulary 2", " · ".join(f"{i + 1} {k}" for i, k in enumerate(c["thread"][3]))),
                ("Grammar practice", " · ".join(f"{i + 1} {k}" for i, (_p, k) in enumerate(c["practice"]))),
                ("Listen and answer", " · ".join(f"{i + 1} {a}" for i, (_q, a) in enumerate(c["gist"]))),
                ("Practice 1", " · ".join(f"{i + 1} {k}" for i, (_p, k) in enumerate(c["controlled"]))),
                ("In the Room 1", " · ".join(f"{i + 1} {a}" for i, (_q, a) in enumerate(c["listen"]))),
                ("Self-check", u["key"])]
        return (f'<div class="keyunit"><h4>Unit {u["n"]} · {inline(u["title"])}</h4>'
                + "".join(f'<div class="keyrow"><span class="klabel">{lab}</span><span>{inline(val)}</span></div>' for lab, val in rows) + "</div>")
    for chunk in chunks(units, 3):
        pages.append(page('<div class="body">' + h("Answer key", "Every exercise") + "".join(keyblock(u) for u in chunk) + "</div>", "Answer key", num)); num += 1

    css = CSS.replace("ACCENT", accent)
    doc = ("<!doctype html><html lang='en'><head><meta charset='utf-8'>"
           f"<title>Forbes English at Work · Book {book} · {html.escape(btitle)}</title>"
           "<link rel='preconnect' href='https://fonts.googleapis.com'>"
           "<link href='https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700;1,900&family=DM+Sans:wght@400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap' rel='stylesheet'>"
           f"<style>{css}</style></head><body>{''.join(pages)}</body></html>")
    out = HERE / f"book-{book}.html"
    out.write_text(doc, encoding="utf-8")
    print(f"{out.name}: {len(pages)} pages, {len(units)} units")


CSS = """
:root{--accent:ACCENT;--paper:#fff9ed;--ground:#f3ede0;--ink:#123a3e;--slate:#1c5789;--blush:#f8dcd1;--mute:#5d6b6e;--line:#d9d0bf}
*{box-sizing:border-box}
html,body{margin:0;background:#bbb;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);font-size:10pt;line-height:1.36}
@page{size:A4;margin:0}
@media print{html,body{background:#fff}.page{margin:0;outline:0}}
.page{width:210mm;height:297mm;background:var(--paper);margin:8mm auto;position:relative;overflow:hidden;page-break-after:always;break-after:page;outline:1px solid #999}
.body{padding:13mm 15mm 16mm}
.body.tight-top{padding-top:7mm}
.foot{position:absolute;left:15mm;right:15mm;bottom:7mm;display:flex;justify-content:space-between;font-family:'DM Mono',monospace;font-size:7.5pt;color:var(--mute)}
.eyebrow{font-weight:700;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);margin:0 0 1.5mm}
h1{font-weight:800;font-size:34pt;line-height:.98;letter-spacing:-.02em;margin:0 0 2mm}
h2{font-weight:700;font-size:23pt;line-height:1.02;letter-spacing:-.015em;margin:0 0 4mm}
h3{font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:3.8mm 0 1.6mm;font-weight:700}
h4{margin:0 0 1.2mm;font-size:10pt;font-weight:700}
p{margin:0 0 2.2mm}
.strap{font-family:'Playfair Display',serif;font-style:italic;font-size:14pt;color:var(--slate);margin:0 0 3mm}
.story{font-family:'Playfair Display',serif;font-size:11pt;line-height:1.42}
.lead{font-size:10.5pt}
.split{display:grid;gap:7mm;align-items:start;margin:1mm 0 2mm}
.split.wide{grid-template-columns:56fr 39fr}.split.narrow{grid-template-columns:65fr 30fr}.split.half{grid-template-columns:1fr 1fr}
.split.left .col-text{order:2}.split.left .col-art{order:1}
.col-text > h3:first-child{margin-top:0}
.plate{background:var(--ground);border:.5pt solid var(--line);border-radius:3mm;position:relative;display:flex;flex-direction:column;justify-content:flex-end;padding:3mm 4mm;margin:0}
.plate.arch{border-radius:50% 50% 3mm 3mm / 34% 34% 3mm 3mm}
.plate.hero,.plate.cover-art{border-radius:0;border:0;border-bottom:.6pt dashed var(--accent);width:100%}
.plate.cover-art{position:absolute;inset:0;height:297mm!important}
.slot-tag{font-family:'DM Mono',monospace;font-size:7pt;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.slot-sub{font-size:8pt;color:var(--mute);font-style:italic;line-height:1.3}
.cando{margin:0;padding-left:4.5mm}.cando li{margin-bottom:1.2mm}
.menu{border-collapse:collapse;width:100%;font-size:8.6pt;line-height:1.3}.menu th{text-align:left;color:var(--accent);padding:1.2mm 2mm 1.2mm 0;vertical-align:top;white-space:nowrap;width:24mm;font-size:8pt;text-transform:uppercase;letter-spacing:.05em}.menu td{padding:1.2mm 0;border-bottom:.4pt solid var(--line)}
.wordbank{margin:0 0 1mm}.group{margin:0 0 1.6mm}
.glabel{font-family:'DM Mono',monospace;font-size:7pt;color:var(--mute);margin-right:1.5mm;text-transform:uppercase;letter-spacing:.08em}
.chip{display:inline-block;border:.5pt solid var(--line);background:#fff;border-radius:3mm;padding:.4mm 2.2mm;margin:0 1.2mm 1.2mm 0;font-size:9pt}
.match{display:grid;grid-template-columns:1fr 1.5fr;gap:4mm;font-size:9.4pt}.match ul,.match ol{margin:0;padding-left:0;list-style:none}.match li{padding:1mm 0;border-bottom:.4pt solid var(--line)}
.match .means{counter-reset:m}.match .means li::before{counter-increment:m;content:counter(m) " ";color:var(--accent);font-weight:700;margin-right:1mm}
.letter{color:var(--accent);font-weight:700;margin-right:1mm}
.bank{margin:0 0 2mm}
.thread{background:#fff;border:.5pt solid var(--line);border-radius:2mm;padding:3mm 4mm;font-size:9.6pt}.thread p{margin:0 0 1.2mm}.thread-head{font-family:'DM Mono',monospace;font-size:7.5pt;color:var(--mute);text-transform:uppercase;letter-spacing:.08em;margin-bottom:1.5mm}
.gap{display:inline-block;min-width:14mm;border-bottom:.6pt solid var(--ink);margin:0 .5mm}
.q{font-size:10pt}
.gram{padding-left:4.5mm;margin:0}.gram li{margin-bottom:1.4mm}.gram strong{color:var(--accent)}
.cards{display:grid;grid-template-columns:1fr;gap:2mm}.card{background:#fff;border:.5pt solid var(--line);border-radius:2mm;padding:2mm 3mm;font-size:9pt;line-height:1.32}.card h4{color:var(--accent);font-size:8.5pt;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.8mm}.card p{margin:0}
.ex{padding-left:5mm;margin:0;font-size:9.4pt}.ex li{margin-bottom:1.2mm}.ex.two-col{columns:2;column-gap:8mm}.ex.two-col li{break-inside:avoid}
.ans{border-bottom:.4pt solid var(--line);height:4.5mm}
.selfcheck li{padding-bottom:4mm;border-bottom:.4pt solid var(--line);margin-bottom:2mm}
.selfcheck.compact li{padding-bottom:2.6mm;margin-bottom:1.2mm;font-size:9.4pt}
.hw{border-top:.6pt solid var(--accent);margin-top:4mm;padding-top:3mm}.hw h2{display:none}
.rule-line{border-bottom:.4pt solid var(--line)}
.ref{font-size:8.2pt;color:var(--mute);margin-top:2mm}
.draft{display:inline-block;background:var(--accent);color:#fff;font-family:'DM Mono',monospace;font-size:7.2pt;letter-spacing:.1em;text-transform:uppercase;padding:.8mm 2.4mm;border-radius:1mm;margin:0 0 3mm}
.dialogue{font-size:9.4pt;line-height:1.32}
.turn{display:grid;grid-template-columns:16mm 1fr;gap:2.2mm;margin-bottom:1mm}
.who{font-family:'DM Mono',monospace;font-size:7.6pt;color:var(--accent);padding-top:.7mm}
.stage{font-style:italic;color:var(--mute);margin:1.5mm 0}.stage em{background:none;padding:0}
.dialogue strong{color:var(--accent)}.dialogue em{background:var(--blush);padding:0 .6mm;font-style:italic;border-radius:.6mm}
.role{display:grid;grid-template-columns:8mm 1fr;gap:2.5mm;align-items:start;background:#fff;border:.5pt solid var(--line);border-radius:2mm;padding:2mm 3mm;margin:0 0 1.8mm;font-size:9.2pt}.role p{margin:0}
.rolelabel{font-weight:800;font-size:16pt;color:var(--accent);line-height:1}
.phrases ul{margin:0;padding-left:4.5mm;font-style:italic;font-size:10.2pt}.phrases li{margin-bottom:1.6mm}
.sayit{background:var(--blush);border-radius:2mm;padding:3mm 4mm;margin-top:3mm}.sayit h3{margin-top:0;color:var(--ink)}.sayit p{margin:0;font-size:9.6pt}
.tight{margin:0;padding-left:4.5mm}.tight li{margin-bottom:.8mm}
.cover{background:var(--ground)}
.cover-lockup{position:absolute;left:15mm;bottom:20mm;width:130mm}
.cover-lockup svg{width:50mm;height:auto;display:block;margin-bottom:9mm;color:var(--ink)}
.cover-lockup .fe-logo-mark{color:var(--accent)}
.cover-series{font-weight:700;font-size:10pt;letter-spacing:.14em;text-transform:uppercase;color:var(--slate);margin-bottom:3mm}
.cover-title{font-family:'Playfair Display',serif;font-weight:900;font-size:44pt;line-height:1;letter-spacing:-.01em}.cover-title em{color:var(--accent)}
.cover-level{font-family:'DM Mono',monospace;font-size:9pt;letter-spacing:.14em;text-transform:uppercase;margin-top:5mm;color:var(--mute)}
.map{border-collapse:collapse;width:100%;font-size:7.6pt;line-height:1.25}.map th{text-align:left;color:var(--accent);border-bottom:.6pt solid var(--accent);padding:1.5mm 1.5mm 1.5mm 0;font-size:7.5pt;text-transform:uppercase;letter-spacing:.06em}.map td{vertical-align:top;padding:1.5mm 1.5mm 1.5mm 0;border-bottom:.4pt solid var(--line)}.map .num{font-family:'DM Mono',monospace;color:var(--accent)}.map .t{font-weight:700}
.people{display:grid;grid-template-columns:repeat(5,1fr);gap:4mm;margin-top:5mm}.person p{font-size:8.4pt;color:var(--mute)}.person .slot-sub{display:none}
.refunit{margin-bottom:4mm}.refunit p{font-size:9.4pt}
.scriptunit{margin-bottom:5mm;font-size:9.4pt}.scriptunit h4{color:var(--accent)}
.bankgrid{display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;font-size:8.8pt}.bankgrid h4{color:var(--accent);font-size:9pt}
.wordlist{columns:4;column-gap:6mm;margin:0;padding:0;list-style:none;font-size:8pt}.wordlist li{break-inside:avoid;border-bottom:.3pt solid var(--line);padding:.5mm 0}.wordlist .unit{float:right;color:var(--accent);font-family:'DM Mono',monospace;font-size:7.5pt}
.keyunit{margin-bottom:4mm;font-size:8.8pt}.keyunit h4{color:var(--accent)}.keyrow{display:grid;grid-template-columns:30mm 1fr;gap:3mm;padding:1mm 0;border-bottom:.3pt solid var(--line)}.klabel{font-family:'DM Mono',monospace;font-size:7.5pt;color:var(--mute);text-transform:uppercase;letter-spacing:.05em}
code{font-family:'DM Mono',monospace;font-size:.9em}
"""

if __name__ == "__main__":
    build(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
