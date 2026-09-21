"""Lay out one book of Forbes English at Work as A4 pages.

    py docs/at-work/build_book.py 1        -> docs/at-work/book-1.html
    node docs/at-work/print_book.js 1      -> docs/at-work/book-1.pdf

Reads the unit specs in level-<n>-*.md and emits one HTML file of fixed
210 x 297 mm pages, eight per unit, plus front and back matter. Every unit
opener carries a hero band right across the top of the page; the inner
pages carry dashed illustration slots named after the artwork slots in the
spec (u03-opener, u03-scene) or after their job (picture to label, spot).

What is real and what is a placeholder:
  - real: title, strapline, can-do, unit menu, lead-in, vocabulary set,
    grammar as it lands in the dialogue, the model dialogue, the In the
    Room phrase box, the case, the homework with its self-check, the key,
    the word list, the phrase bank
  - placeholder, marked "to write": the vocabulary exercises, the three
    rule cards, the grammar practice, the listening tasks, the role cards
  - the model dialogue is the AI draft from the spec and is tagged as such
    on the page until Innes replaces it with his own

The accent colours here are not derived from a hero (there is none yet);
they are the words in README §7 given a hex so the proof prints. The
designer fixes the print palette.
"""
import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
BOOKS = {
    1: ("level-1-day-one.md", "Day One", "A1/A2", "#e8735a", "coral"),
    2: ("level-2-joining-in.md", "Joining In", "A2/B1", "#2f8f7a", "sea green"),
    3: ("level-3-taking-charge.md", "Taking Charge", "B1+/B2", "#e0a020", "amber"),
    4: ("level-4-setting-the-course.md", "Setting the Course", "B2/C1", "#2451b3", "cobalt"),
    5: ("level-5-the-long-game.md", "The Long Game", "C1/C2", "#6b2d5c", "plum"),
}
LOGO = (HERE.parent.parent / "lesson-template" / "forbes-logo.svgfrag").read_text(encoding="utf-8")


# ---------------------------------------------------------------- parsing

def inline(s):
    """Markdown inline -> HTML: bold, italics, code, ellipsis-safe."""
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
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
        rows = dict(re.findall(r"^\| (Vocabulary|Grammar|Communication|In the Room) \| (.+?) \|\s*$", body, re.M))
        u["rows"] = rows
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
    """'*jobs:* a, b · *places:* c' -> [(label, [words])]"""
    out = []
    for grp in row.split("·"):
        grp = grp.strip()
        m = re.match(r"\*([^*]+):\*\s*(.*)", grp)
        label, rest = (m.group(1), m.group(2)) if m else ("", grp)
        words = [w.strip() for w in re.split(r",(?![^()]*\))", rest) if w.strip()]
        out.append((label, words))
    return out


# ---------------------------------------------------------------- html bits

def slot(name, subject="", h="60mm", cls=""):
    sub = f'<div class="slot-sub">{inline(subject)}</div>' if subject else ""
    return (f'<div class="slot {cls}" style="height:{h}">'
            f'<div class="slot-tag">illustration · {html.escape(name)}</div>{sub}</div>')


def todo(label, h="30mm"):
    return f'<div class="todo" style="height:{h}"><span>{html.escape(label)} — to write</span></div>'


def lines(n, gap="8mm"):
    return "".join(f'<div class="rule-line" style="height:{gap}"></div>' for _ in range(n))


def page(inner, head="", num=None, cls=""):
    foot = f'<div class="foot"><span>{html.escape(head)}</span><span>{num if num else ""}</span></div>' if (head or num) else ""
    return f'<section class="page {cls}">{inner}{foot}</section>\n'


def you_question(leadin):
    """The personal question from the lead-in: the sentences with 'you' in them."""
    sents = re.findall(r"[^.?!]+[.?!]", leadin)
    mine = [s.strip() for s in sents if re.search(r"\byou\b", s) and "picture" not in s]
    return " ".join(mine) if mine else sents[0].strip()


def strand_menu(u):
    return ('<table class="menu">' + "".join(
        f'<tr><th>{k}</th><td>{inline(u["rows"][k])}</td></tr>' for k in ("Vocabulary", "Grammar", "Communication", "In the Room")
    ) + "</table>")


def unit_pages(u, book, start):
    n, T = u["n"], u["title"]
    head = f"Unit {n} · {T}"
    slot_o = f"u{n:02d}-opener"
    slot_s = f"u{n:02d}-scene"
    P = []

    # 1 opener — hero right across the top
    cando = [c.strip() for c in re.split(r";\s*", u["cando"]) if c.strip()]
    P.append(page(
        slot(slot_o, u["art"].get(slot_o, ""), "96mm", "hero")
        + f'<div class="body"><div class="eyebrow">Unit {n}</div>'
        f'<h1>{inline(T)}</h1><p class="strap">{inline(u["strap"])}</p>'
        '<div class="two"><div><h3>In this unit you can</h3><ul class="cando">'
        + "".join(f"<li>{inline(c)}</li>" for c in cando)
        + f'</ul></div><div>{strand_menu(u)}</div></div>'
        f'<div class="box leadin"><h3>Lead-in</h3><p>{inline(u["leadin"])}</p></div></div>',
        head, start, "opener"))

    # 2 vocabulary
    groups = vocab_groups(u["rows"]["Vocabulary"])
    chips = "".join(
        f'<div class="group">{("<span class=glabel>" + html.escape(g) + "</span>") if g else ""}'
        + "".join(f'<span class="chip">{inline(w)}</span>' for w in ws) + "</div>" for g, ws in groups)
    P.append(page(
        f'<div class="body"><div class="eyebrow">Vocabulary</div><h2>{inline(T)}</h2>'
        f'<div class="wordbank">{chips}</div>'
        + slot("picture to label", "the vocabulary set in one scene from the unit's story, numbered", "62mm")
        + '<h3>1 · Label the picture</h3>' + todo("matching task, 8–10 items", "22mm")
        + '<h3>2 · Complete the message</h3>' + todo("a message thread or form using the set", "34mm")
        + f'<h3>3 · You</h3><p class="q">{inline(you_question(u["leadin"]))}</p>{lines(2)}</div>',
        head, start + 1))

    # 3 grammar
    P.append(page(
        f'<div class="body"><div class="eyebrow">Grammar</div><h2>{inline(u["rows"]["Grammar"].split(":")[0].split(" — ")[0])}</h2>'
        '<h3>In the dialogue</h3><ol class="gram">'
        + "".join(f"<li>{inline(g)}</li>" for g in u["gramlines"])
        + '</ol><h3>The rule</h3><div class="cards">'
        + "".join(f'<div class="card"><h4>{c}</h4>{todo("card", "26mm")}</div>' for c in ("Form", "Use", "Watch out"))
        + '</div><h3>Practice</h3><ol class="practice">' + "".join("<li></li>" for _ in range(6))
        + '</ol><p class="ref">Grammar reference: see the back of the book.</p></div>',
        head, start + 2))

    # 4 dialogue — scene band across the top, AI draft tagged
    dl = []
    for ln in u["dialogue"]:
        m = re.match(r"^([A-ZÀ-Þ][A-ZÀ-Þ .'\-]+):\s+(.*)$", ln)
        if m:
            dl.append(f'<div class="turn"><span class="who">{html.escape(m.group(1).title())}</span><span class="say">{inline(m.group(2))}</span></div>')
        else:
            dl.append(f'<p class="stage">{inline(ln)}</p>')
    P.append(page(
        slot(slot_s, u["art"].get(slot_s, ""), "66mm", "band")
        + f'<div class="body"><div class="eyebrow">Communication · {inline(u["rows"]["Communication"])}</div><h2>Listen and read</h2>'
        '<div class="draft">AI draft dialogue — to be replaced</div>'
        f'<div class="dialogue">{"".join(dl)}</div>'
        '<h3>Listen and answer</h3>' + todo("two gist questions", "16mm") + "</div>",
        head, start + 3))

    # 5 communication practice
    P.append(page(
        f'<div class="body"><div class="eyebrow">Communication</div><h2>Practice</h2>'
        '<h3>Useful language</h3><div class="box"><ul class="tight">'
        + "".join(f"<li>{inline(g)}</li>" for g in u["gramlines"]) + "</ul></div>"
        '<h3>1 · Controlled practice</h3>' + todo("staged practice, 6 items", "34mm")
        + '<h3>2 · Role-play</h3><div class="two roles">'
        f'<div class="card"><h4>Student A</h4>{todo("role card", "40mm")}</div>'
        f'<div class="card"><h4>Student B</h4>{todo("role card", "40mm")}</div></div>'
        f'<p class="q"><strong>Task.</strong> {inline(u["speak"])}</p></div>',
        head, start + 4))

    # 6 in the room
    P.append(page(
        f'<div class="body"><div class="eyebrow">In the Room</div><h2>{inline(u["rows"]["In the Room"])}</h2>'
        '<div class="two"><div class="box phrases"><h3>Phrase box</h3><ul>'
        + "".join(f"<li>{inline(p)}</li>" for p in u["phrases"]) + "</ul></div>"
        + slot("spot", "a small scene: the phrase box in use", "58mm") + "</div>"
        '<h3>1 · Listen</h3>' + todo("a short listening in which the phrases do their work; 4 questions", "36mm")
        + '<h3>2 · One-minute role-play</h3>' + todo("mini role-play", "28mm")
        + '<h3>Say it right</h3>' + todo("pronunciation note: where intonation carries the meaning", "20mm") + "</div>",
        head, start + 5))

    # 7 the case
    P.append(page(
        f'<div class="body"><div class="eyebrow">The Case</div><h2>{inline(T)}</h2>'
        f'<p class="scenario">{inline(u["scenario"])}</p>'
        + slot("spot", "the case's situation, from the unit's story", "50mm")
        + f'<div class="box"><h3>Speak</h3><p>{inline(u["speak"])}</p></div>'
        f'<div class="box"><h3>Write</h3><p>{inline(u["write"])}</p>{lines(9)}</div></div>',
        head, start + 6))

    # 8 homework
    P.append(page(
        f'<div class="body"><div class="eyebrow">Homework</div><h2>{inline(T)}</h2>'
        f'<div class="box"><h3>Do</h3><p>{inline(u["do"])}</p>{lines(8)}</div>'
        '<h3>Self-check</h3><ol class="selfcheck">'
        + "".join(f"<li>{inline(it)}</li>" for it in u["items"])
        + '</ol><p class="ref">Answers: see the key at the back of the book.</p></div>',
        head, start + 7))
    return P


def build(book):
    fname, btitle, cefr, accent, accent_word = BOOKS[book]
    md = (HERE / fname).read_text(encoding="utf-8")
    units = parse_units(md)
    company = re.search(r"^\*\*The company\.\*\*(.+?)(?=\n\n)", md, re.S | re.M).group(1).strip()
    year = re.search(r"^\*\*The year\.\*\*(.+?)(?=\n\n)", md, re.S | re.M).group(1).strip()
    readme = (HERE / "README.md").read_text(encoding="utf-8")
    cast_block = re.search(r"\*\*Book %d — (.+?)\*\*\n\n(\| name.+?)(?=\n\n)" % book, readme, re.S)
    cast = re.findall(r"^\| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$", cast_block.group(2), re.M)[1:]
    setting = cast_block.group(1)

    pages = []
    # cover
    pages.append(page(
        slot(f"book-{book}-cover", f"the Unit 1 opener, cropped to the front board; quiet space bottom-left; accent {accent_word}", "297mm", "cover-art")
        + f'<div class="cover-lockup">{LOGO}<div class="cover-title">Forbes English<br>at Work</div>'
        f'<div class="cover-sub">{html.escape(btitle)}</div><div class="cover-level">Book {book} · {html.escape(cefr)}</div></div>',
        cls="cover"))
    # map of the book
    rows = "".join(
        f'<tr><td class="num">{u["n"]}</td><td class="t">{inline(u["title"])}</td>'
        + "".join(f"<td>{inline(u['rows'][k])}</td>" for k in ("Vocabulary", "Grammar", "Communication", "In the Room")) + "</tr>"
        for u in units)
    pages.append(page(
        '<div class="body"><div class="eyebrow">Map of the book</div>'
        f'<h1>{html.escape(btitle)}</h1><table class="map"><tr><th></th><th>Unit</th><th>Vocabulary</th><th>Grammar</th><th>Communication</th><th>In the Room</th></tr>{rows}</table></div>',
        "Map of the book", 2))
    # meet the team
    cards = "".join(
        f'<div class="person">{slot("silhouette", f"{name}: {known}", "42mm")}<h4>{html.escape(name)}</h4><p>{inline(role)}</p></div>'
        for name, role, _pron, known in cast)
    pages.append(page(
        f'<div class="body"><div class="eyebrow">Meet the team</div><h1>{html.escape(setting)}</h1>'
        f'<p class="lede">{inline(company)}</p><p>{inline(year)}</p><div class="people">{cards}</div></div>',
        "Meet the team", 3))

    num = 4
    for u in units:
        pages.extend(unit_pages(u, book, num))
        num += 8

    # back matter: grammar reference stubs, phrase bank, word list, answer key
    ref = "".join(
        f'<div class="refunit"><h4>Unit {u["n"]} · {inline(u["rows"]["Grammar"].split(":")[0].split(" — ")[0])}</h4>'
        f'<p>{inline(u["rows"]["Grammar"])}</p>{todo("full rule and exceptions", "14mm")}</div>' for u in units)
    half = (len(units) + 1) // 2
    for i, chunk in enumerate((units[:half], units[half:])):
        pages.append(page('<div class="body"><div class="eyebrow">Grammar reference</div>' + "".join(
            f'<div class="refunit"><h4>Unit {u["n"]} · {inline(u["rows"]["Grammar"].split(":")[0].split(" — ")[0])}</h4>'
            f'<p>{inline(u["rows"]["Grammar"])}</p>{todo("full rule and exceptions", "12mm")}</div>' for u in chunk)
            + "</div>", "Grammar reference", num)); num += 1
    for i, chunk in enumerate((units[:half], units[half:])):
        pages.append(page('<div class="body"><div class="eyebrow">In the Room — phrase bank</div><div class="bank">' + "".join(
            f'<div><h4>Unit {u["n"]} · {inline(u["rows"]["In the Room"])}</h4><ul class="tight">'
            + "".join(f"<li>{inline(p)}</li>" for p in u["phrases"]) + "</ul></div>" for u in chunk)
            + "</div></div>", "Phrase bank", num)); num += 1
    words = {}
    for u in units:
        for _g, ws in vocab_groups(u["rows"]["Vocabulary"]):
            for w in ws:
                w = re.sub(r"\*", "", w)
                words.setdefault(w.lower(), (w, set()))[1].add(u["n"])
    wl = "".join(f'<li>{inline(w)} <span class="unit">{", ".join(str(n) for n in sorted(ns))}</span></li>'
                 for _k, (w, ns) in sorted(words.items()))
    pages.append(page(f'<div class="body"><div class="eyebrow">Word list</div><ul class="wordlist">{wl}</ul></div>', "Word list", num)); num += 1
    keys = "".join(f'<div class="keyrow"><span class="num">Unit {u["n"]}</span> {inline(u["key"])}</div>' for u in units)
    pages.append(page(f'<div class="body"><div class="eyebrow">Answer key — self-check</div>{keys}</div>', "Answer key", num)); num += 1

    css = CSS.replace("ACCENT", accent)
    doc = ("<!doctype html><html lang='en'><head><meta charset='utf-8'>"
           f"<title>Forbes English at Work · Book {book} · {html.escape(btitle)}</title>"
           "<link rel='preconnect' href='https://fonts.googleapis.com'>"
           "<link href='https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap' rel='stylesheet'>"
           f"<style>{css}</style></head><body>{''.join(pages)}</body></html>")
    out = HERE / f"book-{book}.html"
    out.write_text(doc, encoding="utf-8")
    print(f"{out.name}: {len(pages)} pages, {len(units)} units")


CSS = """
:root{--accent:ACCENT;--paper:#fff9ed;--ink:#1c1c1c;--mute:#6b6459;--line:#d9d0bf;--wash:#f3ede0}
*{box-sizing:border-box}
html,body{margin:0;background:#bbb;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);font-size:10.5pt;line-height:1.38}
@page{size:A4;margin:0}
@media print{html,body{background:#fff}.page{margin:0;outline:0}}
.page{width:210mm;height:297mm;background:var(--paper);margin:8mm auto;position:relative;overflow:hidden;page-break-after:always;break-after:page;outline:1px solid #999}
.body{padding:14mm 16mm 18mm}
.hero+.body,.band+.body{padding-top:8mm}
.foot{position:absolute;left:16mm;right:16mm;bottom:8mm;display:flex;justify-content:space-between;font-family:'DM Mono',monospace;font-size:7.5pt;color:var(--mute);border-top:.4pt solid var(--line);padding-top:2mm}
.eyebrow{font-family:'DM Mono',monospace;font-size:8pt;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:0 0 2mm}
h1{font-family:'Playfair Display',serif;font-weight:900;font-size:30pt;line-height:1.05;margin:0 0 2mm}
h2{font-family:'Playfair Display',serif;font-weight:700;font-size:17pt;line-height:1.15;margin:0 0 4mm}
h3{font-size:9pt;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:5mm 0 2mm;font-weight:700}
h4{margin:0 0 1.5mm;font-size:10pt}
p{margin:0 0 2.5mm}
.strap{font-family:'Playfair Display',serif;font-style:italic;font-size:13pt;color:var(--mute);margin-bottom:5mm}
.two{display:grid;grid-template-columns:1fr 1fr;gap:6mm;align-items:start}
.cando{margin:0;padding-left:5mm}.cando li{margin-bottom:1.5mm}
.menu{border-collapse:collapse;width:100%;font-size:9pt}.menu th{text-align:left;color:var(--accent);padding:1.2mm 2mm 1.2mm 0;vertical-align:top;white-space:nowrap;width:24mm}.menu td{padding:1.2mm 0;border-bottom:.4pt solid var(--line)}
.box{background:var(--wash);border-radius:2mm;padding:4mm 5mm;margin:4mm 0}
.box h3{margin-top:0}
.leadin p{margin:0}
.slot{border:.6pt dashed var(--accent);background:var(--wash);border-radius:2mm;position:relative;margin:3mm 0;display:flex;flex-direction:column;justify-content:flex-end;padding:3mm 4mm}
.slot.hero,.slot.band,.slot.cover-art{border-radius:0;margin:0;border:0;border-bottom:.6pt dashed var(--accent);width:100%}
.slot.cover-art{position:absolute;inset:0;height:297mm!important;border:0}
.slot-tag{font-family:'DM Mono',monospace;font-size:7.5pt;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.slot-sub{font-size:8.5pt;color:var(--mute);font-style:italic}
.todo{border:.5pt dashed var(--line);border-radius:1.5mm;margin:1.5mm 0 3mm;display:flex;align-items:center;justify-content:center;color:var(--mute);font-family:'DM Mono',monospace;font-size:7.5pt;letter-spacing:.06em}
.rule-line{border-bottom:.4pt solid var(--line)}
.wordbank{margin:0 0 2mm}.group{margin:0 0 2mm}
.glabel{font-family:'DM Mono',monospace;font-size:7.5pt;color:var(--mute);margin-right:2mm;text-transform:uppercase;letter-spacing:.08em}
.chip{display:inline-block;border:.5pt solid var(--line);background:#fff;border-radius:3mm;padding:.6mm 2.4mm;margin:0 1.4mm 1.4mm 0;font-size:9.5pt}
.q{font-size:10pt}
.gram{padding-left:5mm;margin:0 0 2mm}.gram li{margin-bottom:1.6mm}.gram strong{color:var(--accent)}
.cards{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm}.card{background:#fff;border:.5pt solid var(--line);border-radius:2mm;padding:3mm}.card h4{color:var(--accent)}
.practice{padding-left:5mm;margin:0}.practice li{border-bottom:.4pt solid var(--line);height:8mm}
.ref{font-size:8.5pt;color:var(--mute);margin-top:3mm}
.draft{display:inline-block;background:var(--accent);color:#fff;font-family:'DM Mono',monospace;font-size:7.5pt;letter-spacing:.1em;text-transform:uppercase;padding:1mm 2.5mm;border-radius:1mm;margin:0 0 3mm}
.dialogue{font-size:10pt}
.turn{display:grid;grid-template-columns:22mm 1fr;gap:3mm;margin-bottom:1.6mm}
.who{font-family:'DM Mono',monospace;font-size:8pt;color:var(--accent);padding-top:.6mm}
.stage{font-style:italic;color:var(--mute);margin:2mm 0}
.dialogue strong{color:var(--accent)}.dialogue em{background:#fff;padding:0 .6mm;font-style:italic}
.tight{margin:0;padding-left:4.5mm}.tight li{margin-bottom:1mm}
.phrases ul{margin:0;padding-left:4.5mm;font-style:italic}.phrases li{margin-bottom:1.5mm}
.roles .card{min-height:50mm}
.scenario{color:var(--mute);font-style:italic}
.selfcheck{padding-left:5mm}.selfcheck li{margin-bottom:2mm;padding-bottom:5mm;border-bottom:.4pt solid var(--line)}
.cover{background:var(--wash)}
.cover-lockup{position:absolute;left:16mm;bottom:22mm;width:120mm;color:var(--ink)}
.cover-lockup svg{width:52mm;height:auto;display:block;margin-bottom:8mm;color:var(--ink)}
.cover-lockup .fe-logo-mark{color:var(--accent)}
.cover-title{font-family:'Playfair Display',serif;font-weight:900;font-size:30pt;line-height:1.02}
.cover-sub{font-family:'Playfair Display',serif;font-style:italic;font-size:20pt;margin-top:4mm;color:var(--accent)}
.cover-level{font-family:'DM Mono',monospace;font-size:9pt;letter-spacing:.14em;text-transform:uppercase;margin-top:5mm;color:var(--mute)}
.map{border-collapse:collapse;width:100%;font-size:7.6pt;line-height:1.25}.map th{text-align:left;color:var(--accent);border-bottom:.6pt solid var(--accent);padding:1.5mm 1.5mm 1.5mm 0;font-size:7.5pt;text-transform:uppercase;letter-spacing:.06em}.map td{vertical-align:top;padding:1.5mm 1.5mm 1.5mm 0;border-bottom:.4pt solid var(--line)}.map .num{font-family:'DM Mono',monospace;color:var(--accent)}.map .t{font-weight:600}
.lede{font-size:11pt}
.people{display:grid;grid-template-columns:repeat(5,1fr);gap:4mm;margin-top:6mm}.person p{font-size:8.5pt;color:var(--mute)}
.refunit{margin-bottom:4mm}.refunit p{font-size:9pt}
.bank{display:grid;grid-template-columns:1fr 1fr;gap:4mm 8mm;font-size:8.8pt}.bank h4{color:var(--accent);font-size:9pt}
.wordlist{columns:3;column-gap:8mm;margin:0;padding:0;list-style:none;font-size:8.6pt}.wordlist li{break-inside:avoid;border-bottom:.3pt solid var(--line);padding:.6mm 0}.wordlist .unit{float:right;color:var(--accent);font-family:'DM Mono',monospace;font-size:7.5pt}
.keyrow{font-size:9pt;padding:1.8mm 0;border-bottom:.4pt solid var(--line)}.keyrow .num{font-family:'DM Mono',monospace;color:var(--accent);margin-right:3mm}
code{font-family:'DM Mono',monospace;font-size:.9em}
"""

if __name__ == "__main__":
    build(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
