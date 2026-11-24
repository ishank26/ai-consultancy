#!/usr/bin/python3
"""Merge area-mapper zone lists into one de-duplicated master list, and cut triage batches from it.

Usage:
  merge_zones.py MAP_DIR                      write MAP_DIR/master.json and master.csv from each zone's latest list
  merge_zones.py MAP_DIR batches OUT N [--towns T1,T2] [--evidence website,reviews] [--limit K]
      write OUT/bNNN/batch.json + brief.md, N businesses per batch, for businesses not already batched in OUT

A zone's latest list is revise-rN/<zone>/output.json if present, else <zone>/output.json. Duplicates
(same normalised name in the same town, or the same website domain) are merged, keeping every source.
"""
import csv
import json
import re
import sys
from pathlib import Path


def load(path):
    try:
        return json.loads(Path(path).read_text(), strict=False)
    except (OSError, ValueError):
        return None


def latest(root, zone):
    for p in sorted(root.glob(f'revise-r*/{zone}/output.json'), reverse=True):
        if load(p):
            return p
    return root / zone / 'output.json'


def norm(name):
    name = re.sub(r'\b(llc|inc|pc|pa|co|corp|corporation|company|the|of|and|&|ltd|l\.l\.c|p\.c)\b', ' ', name.lower())
    return re.sub(r'[^a-z0-9]+', '', name)


def domain(url):
    m = re.match(r'https?://(?:www\.)?([^/]+)', (url or '').strip().lower())
    return m.group(1) if m else ''


def merge(root):
    seen, out = {}, []
    for zone in sorted(p.name for p in root.glob('[0-9][0-9]-*/')):
        data = load(latest(root, zone)) or {}
        for b in data.get('businesses', []):
            keys = [f'{norm(b.get("name", ""))}|{b.get("town", "").lower().strip()}']
            if domain(b.get('website')):
                keys.append(domain(b['website']))
            hit = next((seen[k] for k in keys if k in seen), None)
            if hit is None:
                hit = dict(b, id=f'B{len(out) + 1:05d}', zones=[zone])
                out.append(hit)
            else:
                hit['source_urls'] = sorted(set(hit.get('source_urls', []) + b.get('source_urls', [])))
                hit['zones'] = sorted(set(hit['zones'] + [zone]))
                if not domain(hit.get('website')) and domain(b.get('website')):
                    hit['website'] = b['website']
            for k in keys:
                seen[k] = hit
    (root / 'master.json').write_text(json.dumps(out, indent=1))
    cols = ['id', 'name', 'category', 'group', 'town', 'address', 'website', 'phone', 'active_evidence', 'notes']
    with (root / 'master.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(out)
    print(len(out), 'businesses after de-duplication')


def batches(root, out_dir, size, towns=None, evidence=None, limit=None):
    master = load(root / 'master.json') or []
    out_dir.mkdir(parents=True, exist_ok=True)
    done = {b['id'] for p in out_dir.glob('b*/batch.json') for b in load(p) or []}
    todo = [b for b in master if b['id'] not in done
            and (not towns or any(t.lower() in b.get('town', '').lower() for t in towns))
            and (not evidence or any(e in (b.get('active_evidence', '') + ' ' + b.get('website', '')).lower()
                                     for e in evidence))]
    todo = todo[:limit] if limit else todo
    start = len(list(out_dir.glob('b*/')))
    for i in range(0, len(todo), size):
        d = out_dir / f'b{start + i // size + 1:03d}'
        d.mkdir()
        part = [{k: b.get(k) for k in ('id', 'name', 'category', 'town', 'address', 'website', 'phone', 'source_urls')}
                for b in todo[i:i + size]]
        (d / 'batch.json').write_text(json.dumps(part, indent=1))
        (d / 'brief.md').write_text(f'Triage every business in batch.json per your role. Today is 2026-11-12. '
                                    f'Use "batch": "{d.name}". Write the JSON to output.json.\n')
    print(len(todo), 'businesses in', -(-len(todo) // size), 'new batches')


def main():
    root = Path(sys.argv[1])
    if len(sys.argv) == 2:
        return merge(root)
    args = sys.argv[2:]
    opt = lambda k: args[args.index(k) + 1] if k in args else None
    batches(root, Path(args[1]), int(args[2]), towns=(opt('--towns') or '').split(',') if opt('--towns') else None,
            evidence=opt('--evidence').split(',') if opt('--evidence') else None,
            limit=int(opt('--limit')) if opt('--limit') else None)


if __name__ == '__main__':
    main()
