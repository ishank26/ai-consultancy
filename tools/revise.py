#!/usr/bin/python3
"""Phase 6 fix loop: build revision tasks from verifier issues, then re-verification tasks.

  revise.py prep RUN ROUND      05-audits-rN/<id>/ with audit.md, profile.json, analysis.json, issues.json, brief.md
  revise.py reverify RUN ROUND  06-verify-rN/<id>/ with the revised audit and the same evidence files
Only audits whose latest verdict is FAIL or that have issues are revised.
"""
import json
import shutil
import sys
from pathlib import Path


def latest_verify(run, task_id, round_no):
    for r in range(round_no - 1, 0, -1):
        p = run / f'06-verify-r{r}' / task_id / 'output.json'
        if p.exists():
            return p
    return run / '06-verify' / task_id / 'output.json'


def latest_audit(run, task_id, round_no):
    for r in range(round_no, 0, -1):
        p = run / f'05-audits-r{r}' / task_id / 'output.md'
        if p.exists():
            return p
    return run / '05-audits' / task_id / 'output.md'


def prep(run, round_no):
    for task in sorted((run / '05-audits').glob('*/')):
        src = latest_verify(run, task.name, round_no)
        if not src.exists():
            print('no verdict', task.name)
            continue
        verdict = json.loads(src.read_text(), strict=False)
        if verdict.get('verdict', '').upper().startswith('PASS') and not verdict.get('issues'):
            continue
        out = run / f'05-audits-r{round_no}' / task.name
        out.mkdir(parents=True, exist_ok=True)
        shutil.copy(latest_audit(run, task.name, round_no - 1), out / 'audit.md')
        for name in ('profile.json', 'analysis.json'):
            shutil.copy(task / name, out / name)
        (out / 'issues.json').write_text(json.dumps(verdict.get('issues', []), indent=1))
        (out / 'brief.md').write_text(
            'REVISION. audit.md in your folder is the current audit (including the "For the founder" section). '
            'issues.json lists problems an independent verifier found. Apply every fix: remove or correct any '
            'unsupported or wrong claim (never replace it with a new unsourced claim), reframe inferences as '
            '"businesses like yours often...", and keep the audit body (title through footer) at or under 450 '
            'words. Keep the same format, the founder section and the Sources list (drop sources for removed '
            'claims). Write the full revised Markdown to output.md.\n'
            '\nRULES THAT EARLIER ROUNDS BROKE (follow exactly):\n'
            '1. Impact lines: write each as "about H1–H2 staff hours a year (ASSUMPTIONS) at $R/hour '
            '(SOURCE ROLE median, NJ, YEAR, x1.25 for benefits) = about $A–$B a year". Compute H1, H2, A and B '
            'yourself by multiplying, and check the arithmetic twice. Use the wage and volume assumptions in '
            'analysis.json; if its own range does not follow from them, use your recomputed range. Round down.\n'
            '2. Do not write "businesses like yours often..." or any claim about how this business or its peers work '
            'internally. Where the point matters, ask it as a question for the walkthrough ("Worth checking '
            'together: ...?").\n'
            '3. Drop any claim the verifier could not open or confirm, and anything from a site that blocked it.\n'
            '4. In the founder section, make no claims about the consultancy\'s clients, experience or past actions '
            '(no "I work with...", "I left a note..."). Stick to what we observed publicly and what we offer.\n'
            '5. Absolute words ("every", "never", "only", "all") only where a source says so.\n'
            '6. Target 420 words for the audit body (title through footer) so it stays under 450.\n'
            '7. Hours must be a plain product you show inline: "VOLUME x TIME EACH x SHARE AUTOMATED". The low end is '
            'the product of every low input and the high end the product of every high input; dollars are hours x '
            'rate. Label staffing counts and the x1.25 benefits load as "our assumption". If a range cannot be '
            'reproduced this way, simplify the inputs until it can.\n')
        print('revise', task.name, len(verdict.get('issues', [])), 'issues')


def reverify(run, round_no):
    for task in sorted((run / f'05-audits-r{round_no}').glob('*/')):
        if not (task / 'output.md').exists():
            print('no revised audit', task.name)
            continue
        out = run / f'06-verify-r{round_no}' / task.name
        out.mkdir(parents=True, exist_ok=True)
        shutil.copy(task / 'output.md', out / 'audit.md')
        for name in ('profile.json', 'analysis.json', 'industry.json', 'brief.md'):
            shutil.copy(run / '06-verify' / task.name / name, out / name)
        print('reverify', task.name)


if __name__ == '__main__':
    {'prep': prep, 'reverify': reverify}[sys.argv[1]](Path(sys.argv[2]), int(sys.argv[3]))
