#!/usr/bin/python3
"""Research loop: research, verify, revise, re-verify, until PASS.

  avenues.py verify DIR ROUND   DIR/verify-rN/<slug>/ with the latest brief (avenue.json or market.json) and a verifier brief
  avenues.py revise DIR ROUND [fail-only]   DIR/revise-rN/<slug>/ for avenues whose latest verdict is not a clean
      PASS (with fail-only, only FAIL verdicts, so later rounds stop reworking passed briefs)
  avenues.py table DIR          print the latest verdict, fit score and claim counts per avenue
  avenues.py repair DIR         fix output.json files an agent wrote with unescaped quotes (keeps output.raw.json)
  avenues.py playbook DIR OUT   write the analysts' playbook (avenues.json) from avenues whose latest verdict is PASS
Round 1 verifies the researcher's output.json in DIR/<slug>/.
Add --kind pricing for pricing briefs (prompts/pricing_researcher.md, pricing_verifier.md) --kind plan for
opportunity plans (opportunity_planner.md, opportunity_plan_verifier.md) --kind advice for startup advice
(advice_researcher.md, advice_verifier.md) or --kind zone for area business lists (area_mapper.md, zone_checker.md) or --kind rescue for website health
checks (rescue_auditor.md, rescue_checker.md);
the default is avenue.
"""
import json
import shutil
import sys
from pathlib import Path

KINDS = {
    'avenue': {'file': 'avenue.json',
               'revise': 'Rate vendor outcome claims Low. Recompute fit_score so the sub-scores stay in range, add up to '
                         'the total and match the evidence.'},
    'pricing': {'file': 'market.json',
                'revise': 'Copy every price exactly as its source shows it, with its unit, billing term and tier; label '
                          'third-party figures. Recompute price_ranges from the prices that remain and keep them labeled '
                          'as inference.'},
    'plan': {'file': 'plan.json',
             'revise': 'Copy every competitor price exactly as its source shows it, with its unit and billing term. '
                       'Keep only integrations the official docs show. Recompute running costs and totals, and keep '
                       'suggested_pricing, effort and feasibility labeled as inference and consistent with the evidence.'},
    'zone': {'file': 'businesses.json', 'revise': 'Correct or remove each entry the checker flagged, drop every excluded type, add each missing business the checker listed after confirming it on a page, and search again in any category the checker or your categories_thin note says is thin.'},
    'rescue': {'file': 'rescue.json',
               'revise': 'Re-open each domain before changing what audit_md says about it. Keep the cause labelled as '
                         'inference unless a source states it, and keep audit_md and founder_md consistent with the '
                         'fields that remain.'},
    'advice': {'file': 'advice.json',
               'revise': 'Keep program details and costs exactly as the program page states them, rate founder '
                         'anecdotes and marketing articles Low, and keep recommendations labeled as inference and '
                         'consistent with the findings that remain.'},
}


def load(path):
    try:
        return json.loads(Path(path).read_text(), strict=False)
    except (OSError, ValueError):
        return None


def slugs(root):
    return sorted(p.name for p in root.glob('[0-9][0-9]-*/'))


def latest_avenue(root, slug, round_no):
    for r in range(round_no, 0, -1):
        p = root / f'revise-r{r}' / slug / 'output.json'
        if load(p):
            return p
    return root / slug / 'output.json'


def latest_verdict(root, slug, round_no):
    for r in range(round_no, 0, -1):
        p = root / f'verify-r{r}' / slug / 'output.json'
        if load(p):
            return load(p)
    return None


def clean_pass(verdict):
    return bool(verdict) and str(verdict.get('verdict', '')).upper().startswith('PASS') and not verdict.get('issues')


def verify(root, round_no, kind):
    for slug in slugs(root):
        if round_no > 1 and not (root / f'revise-r{round_no - 1}' / slug).exists():
            continue
        src = latest_avenue(root, slug, round_no - 1)
        data = load(src)
        if not data:
            print('skip', slug, 'no valid output')
            continue
        out = root / f'verify-r{round_no}' / slug
        out.mkdir(parents=True, exist_ok=True)
        (out / kind['file']).write_text(json.dumps(data, indent=1))
        for folder in dict.fromkeys([root / slug, src.parent]):  # screenshots the brief cites; later ones win
            for shot in [*folder.glob('*.png'), *folder.glob('*.jpg')]:
                shutil.copy(shot, out / shot.name)
        (out / 'brief.md').write_text(f'Verify {kind["file"]} in your folder per your role. Re-open the cited sources '
                                      'yourself. Write the JSON verdict to output.json.\n')
        print('verify', slug)


def revise(root, round_no, kind, fail_only=False):
    for slug in slugs(root):
        verdict = latest_verdict(root, slug, round_no)
        if verdict is None or clean_pass(verdict):
            continue
        if fail_only and str(verdict.get('verdict', '')).upper().startswith('PASS'):
            continue
        out = root / f'revise-r{round_no}' / slug
        out.mkdir(parents=True, exist_ok=True)
        (out / kind['file']).write_text(json.dumps(load(latest_avenue(root, slug, round_no - 1)), indent=1))
        (out / 'issues.json').write_text(json.dumps(verdict.get('issues', []), indent=1))
        (out / 'brief.md').write_text(
            f'REVISION. {kind["file"]} in your folder is your earlier research brief; issues.json lists problems an '
            'independent verifier found. Apply every fix: correct or remove each unsupported, misstated or '
            'contradicted claim. Never replace a removed claim with a new unsourced one; if you add a claim, open '
            f'its source first. {kind["revise"]} Keep the same schema. Write the full revised JSON to output.json.\n')
        print('revise', slug, len(verdict.get('issues', [])), 'issues')


def table(root):
    rounds = sorted(int(p.name.split('-r')[1]) for p in root.glob('verify-r*/'))
    last = rounds[-1] if rounds else 0
    for slug in slugs(root):
        data = load(latest_avenue(root, slug, last)) or {}
        verdict = latest_verdict(root, slug, last) or {}
        fit = (data.get('fit_score') or {}).get('total', '?')
        checked = verdict.get('claims_checked', [])
        ok = sum(1 for c in checked if c.get('result') == 'confirmed')
        print(f"{slug:42} fit {fit!s:>4}  {verdict.get('verdict', '-'):5} issues {len(verdict.get('issues', [])):>2}  "
              f"confirmed {ok}/{len(checked)}")


def repair_text(text):
    # Agents sometimes write a quoted phrase inside a JSON string without escaping it; turn each stray
    # quote pair at the parse error into single quotes until the file parses.
    for _ in range(50):
        try:
            return json.loads(text, strict=False)
        except json.JSONDecodeError as e:
            i = text.rfind('"', 0, e.pos)
            if i < 0:
                raise
            text = text[:i] + "'" + text[i + 1:]
            j, end = text.find('"', i), text.find('\n', i)
            if 0 <= j < end and text[j + 1] not in ',}]:\n':
                text = text[:j] + "'" + text[j + 1:]
    raise ValueError('could not repair')


def repair(root):
    for p in sorted(root.rglob('output.json')):
        text = p.read_text()
        try:
            json.loads(text, strict=False)
            continue
        except ValueError:
            pass
        try:
            data = repair_text(text)
        except ValueError as e:
            print('could not repair', p, e)
            continue
        p.with_name('output.raw.json').write_text(text)
        p.write_text(json.dumps(data, indent=1))
        print('repaired', p)


def clip(text, n):
    text = str(text)
    return text if len(text) <= n else text[:n].rsplit(' ', 1)[0] + ' ...'


def playbook(root, out):
    rounds = sorted(int(p.name.split('-r')[1]) for p in root.glob('verify-r*/'))
    last = rounds[-1] if rounds else 0
    keep, skipped = [], []
    for slug in slugs(root):
        verdict = latest_verdict(root, slug, last) or {}
        if not str(verdict.get('verdict', '')).upper().startswith('PASS'):
            skipped.append(slug)
            continue
        a = load(latest_avenue(root, slug, last))
        tech = a.get('technical_approach', {})
        keep.append({'avenue': a.get('avenue') or slug[3:], 'one_line': a.get('one_line', ''),
                     'fit_score': (a.get('fit_score') or {}).get('total'),
                     'buyers': [{k: b.get(k) for k in ('business_type', 'naics', 'size_where_it_matters')}
                                for b in a.get('buyers', [])[:4]],
                     'problem_evidence': a.get('problem', {}).get('evidence', [])[:4],
                     'established_pattern': clip(tech.get('established_pattern', ''), 900),
                     'fine_tuning_needed': clip(tech.get('fine_tuning_needed', ''), 500),
                     'existing_solutions': [{k: e.get(k) for k in ('vendor', 'product', 'pricing', 'source_url')}
                                            for e in a.get('existing_solutions', [])[:5]],
                     'measured_outcomes': [o for o in a.get('measured_outcomes', [])
                                           if o.get('strength') in ('High', 'Medium')][:4],
                     'legal_privacy': [{'issue': clip(l.get('issue', ''), 200), 'rule': clip(l.get('rule_or_precedent', ''), 400),
                                        'source_url': l.get('source_url')}
                                       for l in a.get('legal_privacy', []) if l.get('confirmed') is True][:5],
                     'prospecting_signals': {k: [clip(x, 250) for x in v[:8]]
                                             for k, v in (a.get('prospecting_signals') or {}).items()},
                     'pilot': {k: clip(v, 500) for k, v in (a.get('pilot') or {}).items()},
                     'risks': [clip(r, 250) for r in a.get('risks', [])[:4]],
                     'full_brief': str(latest_avenue(root, slug, last))})
    Path(out).write_text(json.dumps({'note': 'Verified physical/edge AI avenues: an independent verifier re-opened the '
                                             'sources for the key numbers, prices, legal rules and outcomes. Hard limits: no face recognition or biometric ID, '
                                             'no audio, no automated accusations; a person reviews every alert. NJ: CCTV and AI used for '
                                             'security count as an alarm business (N.J.S.A. 45:5A-2, P.L.2021 c.2), so security '
                                             'installs need a licensed alarm or electrical contractor.',
                                     'avenues': keep}, indent=1))
    print('playbook', len(keep), 'avenues; not passed:', ' '.join(skipped) or 'none')


if __name__ == '__main__':
    args = sys.argv[1:]
    kind = KINDS['avenue']
    if '--kind' in args:
        i = args.index('--kind')
        kind = KINDS[args[i + 1]]
        del args[i:i + 2]
    sys.argv[1:] = args
    cmd, root = sys.argv[1], Path(sys.argv[2])
    {'verify': lambda: verify(root, int(sys.argv[3]), kind),
     'revise': lambda: revise(root, int(sys.argv[3]), kind, 'fail-only' in sys.argv[4:]),
     'table': lambda: table(root), 'repair': lambda: repair(root), 'playbook': lambda: playbook(root, sys.argv[3])}[cmd]()
