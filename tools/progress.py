#!/usr/bin/python3
"""One progress report across the current study, refreshed on a timer.

Usage: progress.py OUT.md MAP_DIR TRIAGE_DIR [--every SECS]

Writes OUT.md with: mapping (zones done, failed, running; businesses found; check rounds), triage (batches
done of total, businesses triaged, operating, top 10 so far), stopped agents from each watch.log, running agents
and free memory. With --every it rewrites the file every SECS until TRIAGE_DIR/TRIAGE_DONE exists.
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path


def load(path):
    try:
        return json.loads(Path(path).read_text(), strict=False)
    except (OSError, ValueError):
        return None


def states(root, pattern):
    done = failed = 0
    for task in root.glob(pattern):
        st = load(task / 'status.json')
        if st is None:
            continue
        if st.get('exit') == 0 and st.get('outputs'):
            done += 1
        else:
            failed += 1
    return done, failed


def report(out, mdir, tdir):
    lines = [f'# Progress\n\nUpdated {time.strftime("%F %T")}.\n']
    zones = sorted(mdir.glob('[0-9][0-9]-*/'))
    done, failed = states(mdir, '[0-9][0-9]-*/')
    found = sum(len((load(z / 'output.json') or {}).get('businesses', [])) for z in zones)
    lines.append(f'## 1. Mapping\n\nZones done {done} of {len(zones)}, failed {failed}. Businesses listed so far '
                 f'(before de-duplication): {found}.')
    for r in (1, 2):
        v = mdir / f'verify-r{r}'
        if v.exists():
            verdicts = [str((load(p) or {}).get('verdict', '')).upper()[:4] for p in v.glob('*/output.json')]
            lines.append(f'Check round {r}: {len(verdicts)} of {len(list(v.glob("*/")))} checked, '
                         f'{verdicts.count("PASS")} pass, {verdicts.count("FAIL")} fail.')
    if (mdir / 'master.json').exists():
        merged = time.strftime('%F %H:%M', time.localtime((mdir / 'master.json').stat().st_mtime))
        lines.append(f'After de-duplication (last merged {merged}): {len(load(mdir / "master.json") or [])} businesses.')
    lines.append('Mapping finished.' if (mdir / 'LOOP_DONE').exists() else '')
    batches = sorted(tdir.glob('b*/'))
    tdone, tfailed = states(tdir, 'b*/')
    ranked = load(tdir / 'ranking.json') or []
    operating = [b for b in ranked if str(b.get('status', '')).lower().startswith('operating')]
    lines.append(f'\n## 2. Triage\n\nBatches done {tdone} of {len(batches)}, failed {tfailed}. Businesses triaged: '
                 f'{len(ranked)}, operating: {len(operating)}.' if batches else '\n## 2. Triage\n\nNot started (waits for mapping).')
    if operating:
        lines.append('\n| Rank | Score | Business | Town | Top opportunity |\n|---|---|---|---|---|')
        for b in operating[:10]:
            s = b.get('checked_scores') or b.get('scores') or {}
            total = sum(int(s.get(k) or 0) for k in ('gap_size', 'ability_to_pay', 'ease', 'evidence'))
            opp = (b.get('top_opportunities') or [{}])[0].get('opportunity', '')[:90]
            lines.append(f'| {b.get("rank")} | {total} | {b.get("name")} | {b.get("town")} | {opp} |')
    checks = tdir / 'checks'
    if checks.exists():
        cdone, _ = states(checks, 'c*/')
        lines.append(f'\nChecks done {cdone} of {len(list(checks.glob("c*/")))}.')
    lines.append('Triage finished.' if (tdir / 'TRIAGE_DONE').exists() else '')
    stops = []
    for d in (mdir, tdir):
        if (d / 'watch.log').exists():
            stops += (d / 'watch.log').read_text().splitlines()[-5:]
    running = subprocess.run(['pgrep', '-xc', 'pi'], capture_output=True, text=True).stdout.strip() or '0'
    mem = re.search(r'Mem:\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+(\d+)', subprocess.run(['free', '-m'], capture_output=True, text=True).stdout)
    lines.append(f'\n## 3. Health\n\nAgents running: {running}. Memory available: {mem.group(1) if mem else "?"} MB. '
                 f'Recent stops for silence: {len(stops)}.')
    lines += [f'- {s}' for s in stops]
    Path(out).write_text('\n'.join(l for l in lines if l is not None) + '\n')


def main():
    out, mdir, tdir = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    every = int(sys.argv[sys.argv.index('--every') + 1]) if '--every' in sys.argv else 0
    while True:
        report(out, mdir, tdir)
        if not every or (tdir / 'TRIAGE_DONE').exists():
            return
        time.sleep(every)


if __name__ == '__main__':
    main()
