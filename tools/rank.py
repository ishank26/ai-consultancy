#!/usr/bin/python3
"""Phase 4: rank analyzed businesses, pick the top 10, write the lead list.

Usage: rank.py RUN
Sort: Lead Score desc; ties by evidence strength (not thin, then sourced fact count), then industry
diversity (at most 2 per industry in the top 10), then approximate road distance from Milltown.
Writes RUN/04-rank/ranked.json, RUN/04-rank/top10.json and RUN/deliverables/LEAD_LIST.csv.
"""
import csv
import json
import sys
from pathlib import Path

# Approximate miles from Milltown, NJ 08850 by town keyword (driving distance, rounded).
MILES = {'milltown': 0, 'east brunswick': 3, 'north brunswick': 4, 'new brunswick': 4, 'helmetta': 5, 'spotswood': 5,
         'south river': 5, 'highland park': 5, 'jamesburg': 7, 'monroe': 8, 'edison': 8, 'metuchen': 8, 'sayreville': 8,
         'old bridge': 9, 'piscataway': 9, 'dayton': 9, 'south brunswick': 9, 'fords': 10, 'iselin': 10,
         'woodbridge': 10, 'avenel': 11, 'cranbury': 11, 'franklin': 11, 'somerset': 10, 'south plainfield': 11,
         'carteret': 13, 'middlesex': 12}


# Found over TARGET_SIZE (5-200) only after research: kept off the ranking, listed at the end of the lead list.
EXCLUDED = {'34-packaging-distribution-resourc': 'over TARGET_SIZE: own site says 250-300+ full-time staff'}


def miles(town):
    town = town.lower()
    return min((v for k, v in MILES.items() if k in town), default=15)


def main():
    run = Path(sys.argv[1])
    sel = json.loads((run / '01-map/selection.json').read_text())
    sizes = {c['id']: c.get('est_employees', '') for c in sel}
    inds = {c['id']: c['industry'] for c in sel}
    rows = []
    for task in sorted((run / '03-analysis').glob('*/')):
        try:
            a = json.loads((task / 'output.json').read_text())
            p = json.loads((task / 'profile.json').read_text())
        except (OSError, ValueError):
            print('missing', task.name)
            continue
        ls = a['lead_score']
        facts = sum(1 for f in p.get('facts', []) if str(f.get('source_url', '')).startswith('http'))
        rows.append({'id': task.name, 'business': p.get('business') or a.get('business'), 'industry': inds[task.name],
                     'town': p.get('town'), 'website': p.get('website'), 'score': int(ls['total']), 'sub': ls,
                     'est_size': sizes.get(task.name, ''), 'thin': bool(a.get('evidence_thin')), 'facts': facts, 'miles': miles(p.get('town', '')),
                     'top_opportunity': a['opportunities'][0]['title'], 'signal': a.get('best_evidence_signal', ''),
                     'channel': a.get('suggested_channel', ''), 'summary': p.get('summary', '')})
    excluded = [r for r in rows if r['id'] in EXCLUDED]
    rows = [r for r in rows if r['id'] not in EXCLUDED]
    rows.sort(key=lambda r: (-r['score'], r['thin'], -r['facts'], r['miles']))
    top, per = [], {}
    for r in rows:
        if len(top) < 10 and per.get(r['industry'], 0) < 2:
            top.append(r)
            per[r['industry']] = per.get(r['industry'], 0) + 1
    ranked = top + [r for r in rows if r not in top]
    for i, r in enumerate(ranked, 1):
        r['rank'] = i
    out = run / '04-rank'
    out.mkdir(exist_ok=True)
    (out / 'ranked.json').write_text(json.dumps(ranked, indent=1))
    (out / 'top10.json').write_text(json.dumps(top, indent=1))
    (run / 'deliverables').mkdir(exist_ok=True)
    with (run / 'deliverables/LEAD_LIST.csv').open('w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['rank', 'business', 'industry', 'town', 'website', 'est_size', 'lead_score', 'score_breakdown',
                    'top_opportunity', 'best_evidence_signal', 'suggested_channel', 'notes'])
        for r in ranked:
            s = r['sub']
            w.writerow([r['rank'], r['business'], r['industry'], r['town'], r['website'], r.get('est_size', ''),
                        r['score'], f"pain {s['pain']}/fit {s['fit']}/pay {s['ability_to_pay']}/ease {s['ease']}/"
                        f"strategic {s['strategic']}", r['top_opportunity'], r['signal'], r['channel'],
                        ('thin evidence; ' if r['thin'] else '') + ('full audit' if r in top else '')])
        for r in excluded:
            s = r['sub']
            w.writerow(['excluded', r['business'], r['industry'], r['town'], r['website'], r.get('est_size', ''),
                        r['score'], f"pain {s['pain']}/fit {s['fit']}/pay {s['ability_to_pay']}/ease {s['ease']}/"
                        f"strategic {s['strategic']}", r['top_opportunity'], r['signal'], r['channel'],
                        EXCLUDED[r['id']] + '; verified audit kept as an out-of-scope extra'])
    for r in ranked[:15]:
        print(f"{r['rank']:>2} {r['score']:>3} {'thin' if r['thin'] else '    '} f{r['facts']:<2} {r['miles']:>2}mi "
              f"{r['industry'][:14]:14} {r['business'][:40]}")


if __name__ == '__main__':
    main()
