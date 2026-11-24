#!/usr/bin/python3
"""Phase 1: merge mapper outputs, drop duplicates and malformed entries, write candidates.json.

Usage: consolidate.py RUN_DIR
Writes RUN_DIR/01-map/candidates.json (all valid, deduped) and prints a per-industry summary.
Chain/franchise and size judgments stay with the orchestrator, who edits selection.json by hand.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


def domain(url):
    host = urlparse(url if '://' in url else 'https://' + url).netloc.lower()
    return host.removeprefix('www.')


def key(name):
    return re.sub(r'\b(inc|llc|llp|pc|pa|co|corp|company|the|of|and)\b|[^a-z0-9]', '', name.lower())


def main():
    run = Path(sys.argv[1])
    seen, kept, dropped = {}, [], []
    for out in sorted(run.glob('01-map/*/output.json')):
        try:
            items = json.loads(out.read_text())
        except ValueError as exc:
            dropped.append({'file': str(out), 'reason': f'invalid JSON: {exc}'})
            continue
        for item in items if isinstance(items, list) else []:
            name, site = item.get('name', '').strip(), item.get('website', '').strip()
            if not name or not item.get('source_urls'):
                dropped.append({'name': name, 'reason': 'missing name or source_urls'})
                continue
            ids = {key(name)} | ({domain(site)} if site and site != 'Unknown' else set())
            dup = next((seen[i] for i in ids if i in seen), None)
            if dup:
                dropped.append({'name': name, 'reason': f'duplicate of {dup}'})
                continue
            for i in ids:
                seen[i] = name
            item['industry'] = out.parent.name
            kept.append(item)
    (run / '01-map/candidates.json').write_text(json.dumps(kept, indent=1))
    (run / '01-map/dropped.json').write_text(json.dumps(dropped, indent=1))
    counts = {}
    for item in kept:
        counts[item['industry']] = counts.get(item['industry'], 0) + 1
    print(json.dumps({'kept': len(kept), 'dropped': len(dropped), 'by_industry': counts}, indent=1))


if __name__ == '__main__':
    main()
