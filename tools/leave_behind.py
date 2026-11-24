#!/usr/bin/python3
"""Printable leave-behinds and the price card: Markdown -> HTML -> PDF (headless Chrome).

  leave_behind.py health DIR [slug ...]     from DIR/pack/<slug>.md: the health check only (founder notes, verdict and
                                            checker issues cut), with the brand header and the dated footer
  leave_behind.py audit RUN [id ...]        from RUN/deliverables/<id>.md: the audit only ("For the founder", verdict and
                                            issues cut), every impact line with hour or dollar figures removed
  leave_behind.py card [PRICE_CARD.md]      the price card, with the "Owner notes" section cut

Output: <source dir>/leave-behinds/<name>.md, .html and .pdf (card: next to the source). Brand details come from
brand.json in the consultancy root; placeholders in square brackets are left for the owner to fill in. Any dollar
sign left in a body is reported so the owner can check it is a fact about the business, not an estimate.
"""
import html
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAND = json.loads((ROOT / 'brand.json').read_text())
CHROME = ROOT / 'tools/mcp/chrome-headless'
FOOTER = 'Prepared from publicly available information on {date}. We did not log in to or change anything.'
CSS = """
@page { size: Letter; margin: 0.6in 0.7in; }
body { font: 10pt/1.38 -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; color: #1a1a1a; max-width: 7.1in; margin: 0 auto; }
.brand { display: flex; justify-content: space-between; border-bottom: 1.5px solid #1a1a1a; padding-bottom: 6px; margin-bottom: 14px; font-size: 9.5pt; }
.brand b { font-size: 11pt; }
.meta { color: #555; font-size: 9pt; margin-bottom: 10px; }
h1 { font-size: 18pt; margin: 0 0 8px; line-height: 1.2; }
h2 { font-size: 12.5pt; margin: 16px 0 4px; border-bottom: 1px solid #ccc; padding-bottom: 2px; }
h3 { font-size: 11pt; margin: 12px 0 3px; }
p { margin: 5px 0; } ul, ol { margin: 4px 0 6px 1.2em; padding: 0; } li { margin: 2px 0; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 10px; font-size: 9.5pt; }
th, td { border: 1px solid #bbb; padding: 4px 6px; vertical-align: top; text-align: left; }
th { background: #f2f2f2; }
hr { border: 0; border-top: 1px solid #ccc; margin: 12px 0; }
.footer { margin-top: 18px; padding-top: 6px; border-top: 1px solid #ccc; color: #555; font-size: 9pt; }
a { color: inherit; text-decoration: none; }
"""
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']


def long_date(iso):
    y, m, d = (int(x) for x in iso.split('-'))
    return f'{d} {MONTHS[m - 1]} {y}'


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'(?<![="])(https?://[^\s<)]+)', r'<a href="\1">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


def md_to_html(md):
    out, para, lst, table = [], [], None, []

    def flush_para():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para.clear()

    def flush_list():
        nonlocal lst
        if lst:
            out.append(f'</{lst}>')
            lst = None

    def flush_table():
        if table:
            rows = [r for r in table if not re.match(r'^\|?\s*:?-{2,}', r)]
            cells = [[inline(c.strip()) for c in r.strip().strip('|').split('|')] for r in rows]
            out.append('<table><tr>' + ''.join(f'<th>{c}</th>' for c in cells[0]) + '</tr>' +
                       ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in cells[1:]) + '</table>')
            table.clear()

    for line in md.splitlines():
        s = line.strip()
        if s.startswith('|'):
            flush_para(); flush_list(); table.append(s); continue
        flush_table()
        if not s:
            flush_para(); flush_list(); continue
        m = re.match(r'^(#{1,3})\s+(.*)', s)
        if m:
            flush_para(); flush_list()
            out.append(f'<h{len(m.group(1))}>{inline(m.group(2))}</h{len(m.group(1))}>'); continue
        if s == '---':
            flush_para(); flush_list(); out.append('<hr>'); continue
        m = re.match(r'^([-*])\s+(.*)', s) or re.match(r'^(\d+[.)])\s+(.*)', s)
        if m:
            flush_para()
            kind = 'ul' if m.group(1) in '-*' else 'ol'
            if lst != kind:
                flush_list(); out.append(f'<{kind}>'); lst = kind
            out.append(f'<li>{inline(m.group(2))}</li>'); continue
        if lst and line.startswith('  '):
            out[-1] = out[-1][:-5] + ' ' + inline(s) + '</li>'; continue
        flush_list()
        m = re.fullmatch(r'\*\*([^*]+)\*\*', s)
        if m:  # a line that is only bold is a run-in heading (the audit writers use these for the numbered sections)
            flush_para(); out.append(f'<h3>{inline(m.group(1))}</h3>'); continue
        flush_para()  # the sources are generated line by line, so every line stands as its own paragraph
        para.append(s)
    flush_para(); flush_list(); flush_table()
    return '\n'.join(out)


def page(title, body_html, prepared_for=None, footer=None, extra_css=''):
    head = (f'<div class="brand"><div><b>{html.escape(BRAND["name"])}</b><br>{html.escape(BRAND["tagline"])}</div>'
            f'<div style="text-align:right">{html.escape(BRAND["phone"])}<br>{html.escape(BRAND["email"])}<br>'
            f'{html.escape(BRAND["site"])}</div></div>')
    meta = f'<div class="meta">Prepared for {html.escape(prepared_for)}</div>' if prepared_for else ''
    foot = f'<div class="footer">{html.escape(footer)}</div>' if footer else ''
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<style>{CSS}{extra_css}</style></head><body>{head}{meta}{body_html}{foot}</body></html>')


def to_pdf(html_path, pdf_path):
    profile = Path('/tmp') / 'leave-behind-chrome'
    subprocess.run([str(CHROME), '--no-sandbox', f'--user-data-dir={profile}', '--no-pdf-header-footer',
                    f'--print-to-pdf={pdf_path}', f'file://{html_path.resolve()}'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90, check=False)
    return pdf_path.exists()


def dollar_check(name, body):
    hits = [ln.strip()[:110] for ln in body.splitlines() if '$' in ln and not ln.strip().startswith('http')]
    for h in hits:
        print(f'  {name}: dollar sign left, check it is a fact about the business: {h}')


def render(out_dir, name, title, body_md, prepared_for, footer):
    out_dir.mkdir(exist_ok=True)
    (out_dir / f'{name}.md').write_text(f'{body_md.rstrip()}\n\n{footer}\n' if footer else body_md)
    html_path = out_dir / f'{name}.html'
    html_path.write_text(page(title, md_to_html(body_md), prepared_for, footer))
    ok = to_pdf(html_path, out_dir / f'{name}.pdf')
    print(name, 'pdf' if ok else 'NO PDF')


def health(root, slugs):
    src = root / 'pack'
    for path in sorted(src.glob('*.md')):
        if path.name == 'SUMMARY.md' or (slugs and path.stem not in slugs):
            continue
        text = path.read_text()
        text = re.sub(r'^> \*\*Reviewer note.*?\n\n', '', text, flags=re.S)  # internal note, not for the business
        body = text.split('\n---\n', 1)[0].rstrip()
        m = re.search(r'on (\d{1,2} \w+ \d{4})', body)
        footer = None  # the health check already ends with the dated footer
        if 'Prepared from publicly available information' not in body:
            footer = FOOTER.format(date=m.group(1) if m else long_date(date.today().isoformat()))
        title = re.match(r'#\s*(.*)', body).group(1)
        name = title.split(':', 1)[1].strip() if ':' in title else title
        dollar_check(path.stem, body)
        render(root / 'leave-behinds', path.stem, title, body, name, footer)


# Impact lines carry modelled hour and dollar ranges, which stay out of what the business reads. Writers vary the
# marker (**Impact:**, *Expected impact:*, bare "Impact:") and sometimes omit it, leaving "about 48–307 staff hours...".
IMPACT = re.compile(r'^\s*(?:[-*]\s+)?[*_]{0,2}\s*(?:expected\s+)?impact\b.*$'
                    r'|^\s*about\s+\d[\d,.]*\s*[–-]\s*\d[\d,.]*\s*(?:\w+\s+){0,3}hours\b.*$', re.I | re.M)


def audit(run, ids):
    src = run / 'deliverables'
    for path in sorted(src.glob('*.md')):
        if path.name == 'SUMMARY.md' or (ids and path.stem not in ids):
            continue
        text = path.read_text()
        body = re.split(r'\n## For the founder|\n---\n', text, maxsplit=1)[0]
        body = IMPACT.sub('', body)
        body = re.sub(r'^[*_]*Prepared from publicly available information.*$', '', body, flags=re.M)
        body = re.sub(r'\n{3,}', '\n\n', body).rstrip()
        m = re.search(r'(\d{4}-\d{2}-\d{2})', body)
        checked = long_date(m.group(1)) if m else long_date(date.fromtimestamp(path.stat().st_mtime).isoformat())
        body = re.sub(r'\b(20\d\d)-(\d\d)-(\d\d)\b', lambda x: long_date(x.group(0)), body)
        title = re.match(r'#\s*(.*)', body).group(1)
        name = re.split(r'\s[—–-]\s', title, maxsplit=1)[1] if re.search(r'\s[—–-]\s', title) else title
        dollar_check(path.stem, body)
        render(run / 'leave-behinds', path.stem, title, body, name, FOOTER.format(date=checked))


def card(path):
    text = path.read_text()
    body = re.split(r'\n---\n\n\*\*Owner notes', text, maxsplit=1)[0].rstrip()
    out = path.parent
    html_path = out / 'PRICE_CARD.html'
    compact = 'body{font-size:9.5pt} table{font-size:9pt} th,td{padding:3px 5px} h2{margin-top:10px} h1{font-size:16pt}'
    html_path.write_text(page('Price card', md_to_html(body), None, f'Prices as of {long_date(date.today().isoformat())}. '
                              'Each job is quoted in writing before it starts.', compact))
    print('PRICE_CARD', 'pdf' if to_pdf(html_path, out / 'PRICE_CARD.pdf') else 'NO PDF')


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'health':
        health(Path(sys.argv[2]), set(sys.argv[3:]))
    elif cmd == 'audit':
        audit(Path(sys.argv[2]), set(sys.argv[3:]))
    elif cmd == 'card':
        card(Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / 'PRICE_CARD.md')
