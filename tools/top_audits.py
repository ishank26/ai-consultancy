#!/usr/bin/python3
"""Deep audits (tier 4) for the top of a triage ranking, in the runs/2026-11-11 layout so gate.py and
revise.py work unchanged.

  top_audits.py setup RUN TRIAGE_DIR N    01-map/selection.json, 02a-industry briefs, 02b-business tasks for the
      top N operating businesses in TRIAGE_DIR/ranking.json (each task also gets the triage record as triage.json)
  top_audits.py writers RUN               05-audits/<id>/ with profile.json, analysis.json, triage.json and the writer brief
  top_audits.py verify RUN                06-verify/<id>/ with the audit and its evidence files, for the verifier
  top_audits.py pack RUN                  deliverables/<id>.md (latest audit plus its check verdict) and SUMMARY.md
Industry briefs are reused from runs/2026-11-11/02a-industry; an industry without one gets a stub that tells the
analyst to find and cite a wage benchmark itself.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRIEFS = ROOT / 'runs/2026-11-11/02a-industry'
# Category keyword -> industry brief (first match wins).
INDUSTRY = [
    (('law', 'attorney', 'legal'), 'legal'),
    (('engineer', 'architect', 'survey'), 'b2b-services'),
    (('account', 'cpa', 'tax', 'bookkeep', 'payroll'), 'accounting'),
    (('therapy', 'rehab', 'dent', 'orthodont', 'medic', 'physician', 'chiropract', 'clinic'), 'healthcare'),
    (('plumb', 'electric', 'hvac', 'roof', 'landscap', 'locksmith', 'pest'), 'home-services'),
    (('construct', 'contract', 'remodel', 'renovat', 'paving', 'driveway'), 'construction'),
    (('it services', 'software', 'technology', 'computer', 'web'), 'software-it'),
    (('warehous', 'logistic', 'distribut', '3pl'), 'logistics-3pl'),
    (('property', 'real estate', 'realty', 'brokerage'), 'property-realestate'),
    (('insurance',), 'insurance'),
    (('engineer', 'architect', 'survey', 'consult', 'financial', 'planning', 'marketing', 'staffing', 'printing'),
     'b2b-services'),
]
STUB = {'industry': '', 'note': 'No verified industry brief exists for this industry. For any impact estimate, find '
                                'the closest BLS OES wage (New Jersey, most recent year) with a quick search and cite '
                                'its URL; otherwise state the impact without dollar figures.'}
WRITER_RULES = (ROOT / 'runs/2026-11-11/05-audits/03-gaines-associates-pc/brief.md').read_text().split('\nRULES', 1)[1]


def load(path):
    try:
        return json.loads(Path(path).read_text(), strict=False)
    except (OSError, ValueError):
        return None


def industry_for(category):
    c = category.lower()
    for keys, name in INDUSTRY:
        if any(k in c for k in keys):
            return name
    return re.sub(r'[^a-z0-9]+', '-', c).strip('-') or 'other'


def setup(run, triage, n):
    master = {b['id']: b for b in load(ROOT / 'research/2026-11-12-local-triage/master.json')}
    ranked = [b for b in load(triage / 'ranking.json') if str(b.get('status', '')).lower().startswith('operating')]
    selection = []
    for i, b in enumerate(ranked[:n], 1):
        category = (master.get(b.get('ref')) or {}).get('category', '')
        sid = f'{i:02d}-' + re.sub(r'[^a-z0-9]+', '-', b['name'].split(' (')[0].lower()).strip('-')[:40]
        opp = (b.get('top_opportunities') or [{}])[0].get('opportunity', '')
        selection.append({'id': sid, 'name': b['name'], 'industry': industry_for(category), 'category': category,
                          'town': b.get('town', ''), 'website': b.get('website', ''),
                          'why_selected': f'Triage rank {b.get("rank")}. {b.get("what_they_do", "")} Top gap: {opp}',
                          'source_urls': [s for s in (b.get('sources') or []) if str(s).startswith('http')][:5],
                          'ref': b.get('ref')})
        task = run / '02b-business' / sid
        task.mkdir(parents=True, exist_ok=True)
        (task / 'triage.json').write_text(json.dumps(b, indent=1))
        (task / 'brief.md').write_text(
            f'INPUT\n- name: {b["name"]}\n- website: {b.get("website", "")}\n- town: {b.get("town", "")}\n'
            f'- industry: {selection[-1]["industry"]} ({category})\n- triage record: triage.json in your folder (an earlier '
            'browser review of the website, listing and agent readiness; a checker may have corrected parts of it, '
            'see wrong_claims). Use it as leads and re-check what you use.\n\n'
            'Build the profile per your role. Open the business\'s own site in the browser (home, services, about, '
            'careers, contact) at desktop and 390 px phone width, search job boards and review sources. Record the '
            'front-door facts too: how a customer calls, books or asks for a quote, what fails, and the Google '
            'profile. Aim for 6-12 sourced facts. Fill "website", "town" and "industry" exactly as given above. '
            'Today is 2026-11-13. Write the JSON to output.json (save it after each step).\n')
    (run / '01-map').mkdir(parents=True, exist_ok=True)
    (run / '01-map/selection.json').write_text(json.dumps(selection, indent=1))
    for name in {s['industry'] for s in selection}:
        out = run / '02a-industry' / name
        out.mkdir(parents=True, exist_ok=True)
        src = BRIEFS / name / 'output.json'
        if load(src):
            shutil.copy(src, out / 'output.json')
        else:
            (out / 'output.json').write_text(json.dumps(dict(STUB, industry=name), indent=1))
    print(len(selection), 'businesses;', ', '.join(sorted({s['industry'] for s in selection})))


def writers(run):
    selection = {c['id']: c for c in load(run / '01-map/selection.json')}
    for task in sorted((run / '03-analysis').glob('*/')):
        if not load(task / 'output.json'):
            print(task.name, 'no analysis')
            continue
        out = run / '05-audits' / task.name
        out.mkdir(parents=True, exist_ok=True)
        shutil.copy(task / 'profile.json', out / 'profile.json')
        shutil.copy(task / 'output.json', out / 'analysis.json')
        shutil.copy(run / '02b-business' / task.name / 'triage.json', out / 'triage.json')
        c = selection[task.name]
        (out / 'brief.md').write_text(
            f'Write the Opportunity Audit for {c["name"]} ({c["town"]}). Read profile.json and analysis.json in your '
            'folder. Use only facts present in those files, and keep every source URL you rely on in the Sources '
            'list. Write Markdown to output.md.\n\nRULES' + WRITER_RULES)
    print('writers', len(list((run / '05-audits').glob('*/'))))


def verify(run):
    for task in sorted((run / '05-audits').glob('*/')):
        if not (task / 'output.md').exists():
            print(task.name, 'no audit')
            continue
        out = run / '06-verify' / task.name
        out.mkdir(parents=True, exist_ok=True)
        shutil.copy(task / 'output.md', out / 'audit.md')
        for name in ('profile.json', 'analysis.json'):
            shutil.copy(task / name, out / name)
        shutil.copy(run / '03-analysis' / task.name / 'industry.json', out / 'industry.json')
        (out / 'brief.md').write_text(
            'Verify the audit in your folder. Files: audit.md, profile.json, analysis.json, industry.json. Check every '
            'factual claim in the audit section AND the "For the founder" email/opener. Re-open the business pages '
            'and each cited URL yourself (use the browser for pages that need scripts); for any benchmark behind an '
            'impact range, open the original source. Check the audit body is at most ~450 words. Record each check '
            'in claims_checked. Write the JSON to output.json.\n')
    print('verify', len(list((run / '06-verify').glob('*/'))))


def latest(run, task_id, kind):
    rounds = sorted((int(p.name.rsplit('-r', 1)[1]) for p in run.glob(f'{kind}-r*/')), reverse=True)
    name = 'output.md' if kind == '05-audits' else 'output.json'
    for r in rounds:
        p = run / f'{kind}-r{r}' / task_id / name
        if p.exists():
            return p
    return run / kind / task_id / name


def pack(run):
    out = run / 'deliverables'
    out.mkdir(exist_ok=True)
    selection = load(run / '01-map/selection.json')
    rows = ['# Top-25 opportunity audits', '', '| # | Business | Town | Lead score | Check | File |', '|---|---|---|---|---|---|']
    for c in selection:
        audit = latest(run, c['id'], '05-audits')
        verdict = load(latest(run, c['id'], '06-verify')) or {}
        analysis = load(run / '03-analysis' / c['id'] / 'output.json') or {}
        passed = str(verdict.get('verdict', '')).upper().startswith('PASS')
        label = 'checked: PASS' if passed else ('UNVERIFIED: check failed' if verdict else 'UNVERIFIED: not checked')
        text = audit.read_text() if audit.exists() else '(no audit written)'
        text += f'\n\n---\n\n**Check:** {label} ({verdict.get("confidence", "-")} confidence)\n'
        if verdict.get('issues') and not passed:
            text += '\n## Open issues from the checker\n\n' + '\n'.join(
                f'- {i.get("claim", "")}: {i.get("problem", "")}' for i in verdict['issues']) + '\n'
        (out / f'{c["id"]}.md').write_text(text)
        score = (analysis.get('lead_score') or {}).get('total', '?')
        rows.append(f'| {c["id"][:2]} | {c["name"]} | {c["town"]} | {score} | {label} | [{c["id"]}.md]({c["id"]}.md) |')
    (out / 'SUMMARY.md').write_text('\n'.join(rows) + '\n')
    print(len(selection), 'audits in', out)


if __name__ == '__main__':
    cmd, run = sys.argv[1], Path(sys.argv[2])
    if cmd == 'setup':
        setup(run, Path(sys.argv[3]), int(sys.argv[4]))
    else:
        {'writers': writers, 'verify': verify, 'pack': pack}[cmd](run)
