#!/usr/bin/python3
"""Build the website health check pack from the latest rescue outputs and verdicts.

Usage: rescue_pack.py DIR

Writes DIR/pack/<slug>.md (the health check, then the founder notes, the check verdict and any issues still
open) and DIR/pack/SUMMARY.md (one row per business: severity, likely cause, verdict). A check that did not
pass is labelled unverified, with the checker's open issues listed.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from avenues import latest_avenue, latest_verdict, load, slugs  # noqa: E402

ORDER = {'High': 0, 'Medium': 1, 'Low': 2}


def main():
    root = Path(sys.argv[1])
    last = max([int(p.name.split('-r')[1]) for p in root.glob('verify-r*/')] or [0])
    pack = root / 'pack'
    pack.mkdir(exist_ok=True)
    rows = []
    for slug in slugs(root):
        data = load(latest_avenue(root, slug, last)) or {}
        verdict = latest_verdict(root, slug, last) or {}
        passed = str(verdict.get('verdict', '')).upper().startswith('PASS')
        label = 'checked: PASS' if passed else ('UNVERIFIED: check failed' if verdict else 'UNVERIFIED: not checked')
        lines = [data.get('audit_md', '(no health check written)'), '', '---', '',
                 f'**Check:** {label} ({verdict.get("confidence", "-")} confidence)', '', data.get('founder_md', '')]
        if verdict.get('issues') and not passed:
            lines += ['', '## Open issues from the checker', '']
            lines += [f'- {i.get("claim", "")}: {i.get("problem", "")}' for i in verdict['issues']]
        (pack / f'{slug}.md').write_text('\n'.join(lines) + '\n')
        cause = (data.get('likely_cause') or {}).get('cause', '?')
        rows.append((ORDER.get(data.get('severity'), 3), slug, data.get('name', slug), data.get('town', ''),
                     data.get('status', ''), data.get('severity', '?'), cause, label))
    rows.sort()
    table = ['# Website health checks', '', '| Business | Town | Status | Severity | Likely cause | Check | File |',
             '|---|---|---|---|---|---|---|']
    table += [f'| {n} | {t} | {st} | {sv} | {c} | {lb} | [{s}.md]({s}.md) |' for _, s, n, t, st, sv, c, lb in rows]
    (pack / 'SUMMARY.md').write_text('\n'.join(table) + '\n')
    print(len(rows), 'health checks in', pack, ';', sum(1 for r in rows if r[7] == 'checked: PASS'), 'passed')


if __name__ == '__main__':
    main()
