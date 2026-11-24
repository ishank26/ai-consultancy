#!/usr/bin/python3
"""Watch running research agents, keep a live status board, and stop agents that go quiet.

Usage: watch.py DIR [--every SECS] [--stall-mins N]

Every SECS it rewrites DIR/STATUS.md: each task folder (including verify-rN/ and revise-rN/) as waiting,
running, done or failed, with minutes running, minutes since the agent last logged anything, tool calls
and how many items its output.json holds so far. An agent silent for more than --stall-mins is stopped
(its pi process gets SIGTERM) so the batch moves on; batch.py --skip-done reruns it later. Appends every
stop to DIR/watch.log. Exits when no agent is running and nothing has changed for an hour.
"""
import argparse
import json
import os
import signal
import time
from pathlib import Path


def pi_procs():
    procs = {}
    for p in Path('/proc').iterdir():
        if not p.name.isdigit():
            continue
        try:
            if (p / 'comm').read_text().strip() == 'pi':
                procs[os.path.realpath(p / 'cwd')] = int(p.name)
        except OSError:
            continue
    return procs


def count_items(task):
    try:
        data = json.loads((task / 'output.json').read_text(), strict=False)
    except (OSError, ValueError):
        return ''
    if isinstance(data, dict):
        for key in ('businesses', 'findings', 'claims_checked', 'items'):
            if isinstance(data.get(key), list):
                return f'{len(data[key])} {key}'
        return 'saved'
    return f'{len(data)} items' if isinstance(data, list) else 'saved'


def tools_used(log):
    calls = 0
    try:
        with log.open(errors='ignore') as f:
            for line in f:
                if '"tool_execution_start"' in line:
                    calls += 1
    except OSError:
        pass
    return calls


def tasks(root):
    for brief in sorted(root.glob('**/brief.md')):
        yield brief.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dir')
    ap.add_argument('--every', type=int, default=60)
    ap.add_argument('--stall-mins', type=float, default=15)
    args = ap.parse_args()
    root = Path(args.dir).resolve()
    last_change = time.time()
    while True:
        now = time.time()
        procs = pi_procs()
        rows, counts = [], {'running': 0, 'done': 0, 'failed': 0, 'waiting': 0}
        for task in tasks(root):
            log, status = task / 'log.jsonl', task / 'status.json'
            pid = procs.get(str(task))
            quiet = (now - log.stat().st_mtime) / 60 if log.exists() else None
            if pid:
                state = 'running'
                if quiet is not None and quiet > args.stall_mins:
                    os.kill(pid, signal.SIGTERM)
                    state = 'stopped (quiet)'
                    with (root / 'watch.log').open('a') as f:
                        f.write(f'{time.strftime("%F %T")} stopped {task.relative_to(root)} after {quiet:.0f} quiet minutes\n')
            elif status.exists():
                try:
                    st = json.loads(status.read_text())
                    ok = st.get('exit') == 0 and st.get('outputs')
                except ValueError:
                    ok = False
                state = 'done' if ok else 'failed'
            else:
                state = 'waiting'
            counts[state.split()[0] if state.split()[0] in counts else 'failed'] += 1
            if state != 'waiting':
                started = (task / 'session').stat().st_mtime if (task / 'session').exists() else now
                rows.append(f'| {task.relative_to(root)} | {state} | {(now - started) / 60:.0f} | '
                            f'{"" if quiet is None else f"{quiet:.0f}"} | {tools_used(log)} | {count_items(task)} |')
        board = (f'# Status: {root.name}\n\nUpdated {time.strftime("%F %T")}. '
                 f'Running {counts["running"]}, done {counts["done"]}, failed {counts["failed"]}, waiting {counts["waiting"]}. '
                 f'Agents quiet for over {args.stall_mins:g} minutes are stopped and rerun later.\n\n'
                 '| Task | State | Minutes since start | Minutes quiet | Tool calls | Saved so far |\n|---|---|---|---|---|---|\n'
                 + '\n'.join(rows) + '\n')
        old = (root / 'STATUS.md').read_text() if (root / 'STATUS.md').exists() else ''
        if old.split('\n', 3)[3:] != board.split('\n', 3)[3:]:
            last_change = now
        (root / 'STATUS.md').write_text(board)
        if not counts['running'] and now - last_change > 3600:
            return
        time.sleep(args.every)


if __name__ == '__main__':
    main()
