#!/usr/bin/python3
"""Rank triaged businesses, cut checker tasks, and apply checker results.

Usage:
  triage_tools.py rank TRIAGE_DIR                    write ranking.json and ranking.csv from every b*/output.json
  triage_tools.py checks TRIAGE_DIR CHECK_DIR [--top N] [--sample F] [--per K]
      cut CHECK_DIR/cNNN/items.json tasks: the top N operating businesses plus a random fraction F of the rest
  triage_tools.py apply TRIAGE_DIR CHECK_DIR         fold checker verdicts and corrected scores into the ranking

Score = gap_size + ability_to_pay + ease + evidence (each 1-5, so 4-20), using a checker's corrected scores
when present. Businesses that are closed, not found or excluded are ranked last.
"""
import csv
import json
import random
import sys
from pathlib import Path

PARTS = ('gap_size', 'ability_to_pay', 'ease', 'evidence')


def load(path):
    try:
        return json.loads(Path(path).read_text(), strict=False)
    except (OSError, ValueError):
        return None


def records(root):
    for out in sorted(root.glob('b*/output.json')):
        for b in (load(out) or {}).get('businesses', []):
            yield dict(b, batch=out.parent.name)


def score(b):
    s = b.get('checked_scores') or b.get('scores') or {}
    try:
        return sum(int(s.get(k) or 0) for k in PARTS)
    except (TypeError, ValueError):
        return 0


def operating(b):
    return str(b.get('status', '')).lower().startswith('operating')


def write_ranking(root, ranked):
    for i, b in enumerate(ranked, 1):
        b['rank'] = i
    (root / 'ranking.json').write_text(json.dumps(ranked, indent=1))
    with (root / 'ranking.csv').open('w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['rank', 'score', 'ref', 'name', 'town', 'status', 'website', 'check', *PARTS, 'top opportunity',
                    'findable', 'answerable', 'bookable'])
        for b in ranked:
            s = b.get('checked_scores') or b.get('scores') or {}
            opp = (b.get('top_opportunities') or [{}])[0].get('opportunity', '')
            ar = b.get('agent_readiness') or {}
            w.writerow([b['rank'], score(b), b.get('ref'), b.get('name'), b.get('town'), b.get('status'), b.get('website'),
                        b.get('check', 'unchecked'), *[s.get(k) for k in PARTS], opp,
                        ar.get('findable'), ar.get('answerable'), ar.get('bookable')])


def rank(root):
    old = {b.get('ref'): b for b in load(root / 'ranking.json') or []}
    ranked = []
    for b in records(root):
        prev = old.get(b.get('ref'), {})
        for k in ('check', 'checked_scores', 'wrong_claims'):
            if k in prev:
                b[k] = prev[k]
        ranked.append(b)
    ranked.sort(key=lambda b: (operating(b), score(b)), reverse=True)
    write_ranking(root, ranked)
    print(len(ranked), 'ranked;', sum(map(operating, ranked)), 'operating')


def checks(root, out, top=100, sample=0.1, per=8):
    ranked = [b for b in load(root / 'ranking.json') or [] if operating(b)]
    done = {i.get('ref') for p in out.glob('c*/items.json') for i in load(p) or []}
    pick = ranked[:top] + [b for b in ranked[top:] if random.Random(b.get('ref')).random() < sample]
    pick = [b for b in pick if b.get('ref') not in done]
    out.mkdir(parents=True, exist_ok=True)
    start = len(list(out.glob('c*/')))
    for i in range(0, len(pick), per):
        d = out / f'c{start + i // per + 1:03d}'
        d.mkdir()
        (d / 'items.json').write_text(json.dumps(pick[i:i + per], indent=1))
        (d / 'brief.md').write_text('Check every record in items.json per your role. Today is 2026-11-12. '
                                    'Write the JSON to output.json.\n')
    print(len(pick), 'records in', -(-len(pick) // per), 'new check tasks')


def apply(root, out):
    ranked = load(root / 'ranking.json') or []
    by_ref = {b.get('ref'): b for b in ranked}
    n = 0
    for p in sorted(out.glob('c*/output.json')):
        for r in (load(p) or {}).get('results', []):
            b = by_ref.get(r.get('ref'))
            if not b:
                continue
            b['check'] = r.get('verdict', 'checked')
            b['wrong_claims'] = r.get('wrong_claims', [])
            if r.get('corrected_scores') and any(r['corrected_scores'].get(k) for k in PARTS):
                b['checked_scores'] = {k: r['corrected_scores'].get(k) or (b.get('scores') or {}).get(k) for k in PARTS}
            if str(r.get('verdict', '')).startswith('wrong'):
                b['status'] = 'excluded: checker found wrong business or closed'
            n += 1
    ranked.sort(key=lambda b: (operating(b), score(b)), reverse=True)
    write_ranking(root, ranked)
    print(n, 'checker results applied')


def main():
    cmd, root = sys.argv[1], Path(sys.argv[2])
    args = sys.argv[3:]
    opt = lambda k, d: type(d)(args[args.index(k) + 1]) if k in args else d
    if cmd == 'rank':
        rank(root)
    elif cmd == 'checks':
        checks(root, Path(args[0]), top=opt('--top', 100), sample=opt('--sample', 0.1), per=opt('--per', 8))
    elif cmd == 'apply':
        apply(root, Path(args[0]))


if __name__ == '__main__':
    main()
