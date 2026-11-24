#!/usr/bin/python3
"""Orchestrator gates between phases.

  gate.py profiles RUN   check 02b profiles: valid JSON, >=3 facts with http source URLs
  gate.py prep-analysis RUN [AVENUES]   create 03-analysis/<id>/ with profile.json, industry.json, brief.md,
      plus avenues.json (the verified physical/edge playbook, cut to the avenues for that industry) when AVENUES is given
"""
import json
import shutil
import sys
from pathlib import Path


# Industry keyword -> playbook avenues an analyst should see (first match wins; "*" is the fallback).
AVENUE_MAP = [
    (('restaurant', 'food service', 'caterer', 'cafe', 'bakery'),
     ('cold-chain-food-safety-sensors', 'restaurant-table-state', 'restaurant-kitchen-line', 'equipment-monitoring-sensors')),
    (('grocer', 'deli', 'food', 'retail', 'pharmacy', 'liquor'),
     ('cold-chain-food-safety-sensors', 'retail-shelf-inventory', 'retail-loss-prevention-nonbiometric')),
    (('3pl', 'logistics', 'warehous', 'distribut', 'ecommerce'),
     ('warehouse-dock-safety', 'warehouse-receiving-damage-count')),
    (('trucking', 'freight', 'fleet'), ('trucking-fleet-vision', 'warehouse-dock-safety')),
    (('manufactur', 'machine', 'fabricat', 'plastics', 'packaging'),
     ('manufacturing-visual-qc', 'equipment-monitoring-sensors')),
    (('construction', 'contractor'), ('construction-site-vision',)),
    (('property', 'real estate', 'multifamily', 'landlord'), ('property-sensors-multifamily',)),
    (('auto', 'collision', 'tire', 'car wash'), ('auto-service-intake',)),
    (('home-services', 'hvac', 'plumbing', 'electric'), ('equipment-monitoring-sensors', 'property-sensors-multifamily')),
    (('*',), ('other-local-physical-services',)),
]


def avenues_for(industry, playbook):
    industry = industry.lower()
    for keys, names in AVENUE_MAP:
        if '*' in keys or any(k in industry for k in keys):
            picked = [a for a in playbook['avenues'] if a['avenue'] in names]
            return {'note': playbook['note'], 'avenues': picked}
    return {'note': playbook['note'], 'avenues': []}


def load(path):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError):
        return None


def profiles(run):
    bad = []
    for task in sorted((run / '02b-business').glob('*/')):
        data = load(task / 'output.json')
        if not isinstance(data, dict):
            bad.append((task.name, 'missing or invalid output.json'))
            continue
        facts = [f for f in data.get('facts', []) if str(f.get('source_url', '')).startswith('http')]
        if 'insufficient data' in str(data.get('summary', '')).lower():
            bad.append((task.name, 'insufficient data'))
        elif len(facts) < 3:
            bad.append((task.name, f'only {len(facts)} sourced facts'))
    for name, reason in bad:
        print(f'{name}\t{reason}')
    print(f'# {len(bad)} failing')


def prep_analysis(run, avenues=None):
    playbook = load(avenues) if avenues else None
    selection = {c['id']: c for c in load(run / '01-map/selection.json')}
    for task in sorted((run / '02b-business').glob('*/')):
        profile, cand = load(task / 'output.json'), selection.get(task.name)
        if not isinstance(profile, dict) or not cand:
            continue
        brief_src = run / '02a-industry' / cand['industry'] / 'output.json'
        if not load(brief_src):
            print(f'{task.name}\tno industry brief for {cand["industry"]}')
            continue
        out = run / '03-analysis' / task.name
        out.mkdir(parents=True, exist_ok=True)
        shutil.copy(task / 'output.json', out / 'profile.json')
        shutil.copy(brief_src, out / 'industry.json')
        if playbook:
            (out / 'avenues.json').write_text(json.dumps(avenues_for(cand['industry'], playbook), indent=1))
        (out / 'brief.md').write_text(
            f'Analyze {cand["name"]} ({cand["town"]}, industry "{cand["industry"]}").\n'
            'Read profile.json and industry.json in your folder. Produce the top 3 opportunities and the Lead Score '
            'per your role. Note: treat "peer-reviewed" labels in industry.json with care; a working paper or '
            'preprint is not peer-reviewed, so say "working paper" when citing one. Write the JSON to output.json.\n')
    print('prepared', len(list((run / '03-analysis').glob('*/'))))


if __name__ == '__main__':
    {'profiles': profiles, 'prep-analysis': prep_analysis}[sys.argv[1]](Path(sys.argv[2]), *sys.argv[3:])
