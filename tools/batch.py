#!/usr/bin/python3
"""Run many subagent tasks in parallel. Each task dir must already hold brief.md.

Usage: batch.py ROLE PARALLEL TASK_DIR... [--thinking LEVEL] [--timeout SECS] [--skip-done] [--browser]

--browser gives each running agent its own Chrome slot (1..PARALLEL, see tools/mcp/). A task that ends
without an output file (a provider stream error or a stop for silence) is retried once.
"""
import argparse
import json
import queue
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RUN = Path(__file__).resolve().parent / 'run_agent.py'


SLOTS = queue.Queue()


def one(args, task):
    out = next(Path(task).glob('output.*'), None)
    if args.skip_done and out and out.stat().st_size > 50:
        return {'task': Path(task).name, 'skipped': True}
    for old in Path(task).glob('output.*'):
        old.unlink()
    cmd = ['python3', str(RUN), args.role, task, str(Path(task) / 'brief.md'), '--thinking', args.thinking,
           '--timeout', str(args.timeout)]
    for attempt in range(2):
        slot = SLOTS.get() if args.browser else None
        try:
            res = subprocess.run(cmd + (['--slot', str(slot)] if slot else []), capture_output=True, text=True,
                                 stdin=subprocess.DEVNULL, check=False)
        finally:
            if slot:
                SLOTS.put(slot)
        try:
            status = json.loads(res.stdout.strip().splitlines()[-1])
        except (ValueError, IndexError):
            status = {'task': Path(task).name, 'launcher_error': res.stderr[-300:]}
        if status.get('outputs'):
            break
        status['attempt'] = attempt + 1  # no output (provider stream error, stall stop): one retry
    return status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('role')
    ap.add_argument('parallel', type=int)
    ap.add_argument('tasks', nargs='+')
    ap.add_argument('--thinking', default='medium')
    ap.add_argument('--timeout', type=int, default=1800)
    ap.add_argument('--skip-done', action='store_true')
    ap.add_argument('--browser', action='store_true')
    args = ap.parse_args()
    for slot in range(1, args.parallel + 1):
        SLOTS.put(slot)
    with ThreadPoolExecutor(args.parallel) as pool:
        for status in pool.map(lambda t: one(args, t), args.tasks):
            print(json.dumps(status), flush=True)


if __name__ == '__main__':
    main()
