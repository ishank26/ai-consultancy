#!/usr/bin/python3
"""Build the deep-audit run for the one hand-added business from its triage record (mirrors top_audits.setup)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, '/home/ishank/work/consultancy/tools')
from top_audits import STUB, load  # noqa: E402

RUN = Path(__file__).resolve().parent
SID, INDUSTRY = '01-jersey-soft-play', 'kids-party-rental'
b = load(RUN / 'triage/ranking.json')[0]
batch = load(RUN / 'triage/b001/batch.json')[0]
opp = (b.get('top_opportunities') or [{}])[0].get('opportunity', '')
selection = [{'id': SID, 'name': b['name'], 'industry': INDUSTRY, 'category': batch['category'], 'town': b.get('town', ''),
              'website': b.get('website', ''), 'why_selected': f'Added at the owner\'s request. {b.get("what_they_do", "")} '
              f'Top gap: {opp}', 'source_urls': [s for s in (b.get('sources') or []) if str(s).startswith('http')][:5],
              'ref': b.get('ref')}]
(RUN / '01-map').mkdir(exist_ok=True)
(RUN / '01-map/selection.json').write_text(json.dumps(selection, indent=1))
ind = RUN / '02a-industry' / INDUSTRY
ind.mkdir(parents=True, exist_ok=True)
(ind / 'output.json').write_text(json.dumps(dict(STUB, industry=INDUSTRY), indent=1))
task = RUN / '02b-business' / SID
task.mkdir(parents=True, exist_ok=True)
(task / 'triage.json').write_text(json.dumps(b, indent=1))
(task / 'brief.md').write_text(
    f'INPUT\n- name: {b["name"]}\n- website: {b.get("website", "")}\n- town: {b.get("town", "")}\n'
    f'- industry: {INDUSTRY} ({batch["category"]})\n- triage record: triage.json in your folder (a browser review of the '
    'web presence, listing and agent readiness done today; a checker may have corrected parts of it, see wrong_claims). '
    'Use it as leads and re-check what you use.\n\n'
    'Build the profile per your role. This is a mobile party-rental business, so there may be no storefront: its front '
    'door is its website or booking page, Google profile, Instagram or Facebook page and the enquiry route (form, DM, '
    'text, call). Open each in the browser at desktop and 390 px phone width. Record the front-door facts: how a parent '
    'asks for a date and a quote, what fails, and how fast public replies look. Search review sources and local parent '
    'directories. Aim for 6-12 sourced facts. The listed street address may be a home base: use only public business '
    'listings and the business\'s own pages, and do not look up the property or who lives there. Fill "website", '
    '"town" and "industry" exactly as given above. Today is 2026-11-14. Write the JSON to output.json (save it after '
    'each step).\n')
print('set up', SID, b.get('status'), b.get('website'))
