#!/usr/bin/python3
"""Run one DeepSeek v4.1 Flash research subagent headless and capture its output file.

Usage: run_agent.py ROLE TASK_DIR BRIEF_FILE [--thinking LEVEL] [--timeout SECS] [--slot N]

ROLE picks prompts/<role>.md as the system prompt addition. The brief is the task input. The agent
works inside TASK_DIR and must write its result to TASK_DIR/output.json (or output.md); this script
records a log, the final assistant text and a one-line JSON status. --slot N gives the agent its own real
Chrome (tools/mcp/slot-N.json: separate port and empty profile) through pi-mcp-adapter.
"""
import argparse
import json
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL = 'commandcode/deepseek/deepseek-v4.1-flash'
EXT = Path('~/.pi/agent/npm/node_modules').expanduser()
TOOLS = 'read,write,ls,web_search,fetch_content,get_search_content,source_check'


def close_daemons(name):
    """Stop browser-harness daemons left behind for this slot (they detach, so the agent's exit misses them)."""
    for proc in Path('/proc').glob('[0-9]*'):
        try:
            if b'browser_harness.daemon' in (proc / 'cmdline').read_bytes() and \
                    f'BU_NAME={name}'.encode() in (proc / 'environ').read_bytes().split(b'\0'):
                subprocess.run(['kill', proc.name], check=False)
        except OSError:
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('role')
    ap.add_argument('task_dir')
    ap.add_argument('brief')
    ap.add_argument('--thinking', default='medium')
    ap.add_argument('--timeout', type=int, default=1800)
    ap.add_argument('--slot', type=int)
    args = ap.parse_args()
    task = Path(args.task_dir).resolve()
    task.mkdir(parents=True, exist_ok=True)
    argv = ['pi', '--session-dir', str(task / 'session'), '--no-context-files', '--no-skills', '--no-prompt-templates',
            '--no-mcp', '--no-extensions', '-e', str(EXT / 'pi-commandcode-provider'), '-e', str(EXT / 'pi-web-access'),
            *(['-e', str(EXT / 'pi-mcp-adapter'), '--mcp-config', str(ROOT / f'tools/mcp/slot-{args.slot}.json')]
              if args.slot else []),
            '--tools', TOOLS + (',mcp' if args.slot else ''), '--model', MODEL, '--thinking', args.thinking,
            '--append-system-prompt', str(ROOT / 'prompts/rules.md'),
            '--append-system-prompt', str(ROOT / 'prompts' / f'{args.role}.md'),
            '--mode', 'json', '-p', Path(args.brief).read_text()]
    started = time.time()
    with (task / 'log.jsonl').open('w') as out, (task / 'stderr.txt').open('w') as err:
        try:
            code = subprocess.run(argv, cwd=task, stdin=subprocess.DEVNULL, stdout=out, stderr=err, timeout=args.timeout,
                                  check=False).returncode
        except subprocess.TimeoutExpired:
            code = 'timeout'
        finally:
            if args.slot:
                subprocess.run(['pkill', '-f', f'chrome.*--remote-debugging-port={9240 + args.slot}'], check=False)
                close_daemons(f'research-{args.slot}')
    text, tools, errors = '', {}, []
    for line in (task / 'log.jsonl').read_text(errors='ignore').splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get('type') == 'tool_execution_start':
            name = event.get('toolName') or event.get('name') or '?'
            tools[name] = tools.get(name, 0) + 1
        if event.get('type') == 'message_end' and (event.get('message') or {}).get('role') == 'assistant':
            message = event['message']
            if message.get('errorMessage'):
                errors.append(message['errorMessage'][:300])
            part = ''.join(i.get('text', '') for i in message.get('content') or [] if i.get('type') == 'text')
            if part.strip():
                text = part
    (task / 'final.txt').write_text(text)
    outputs = sorted(p.name for p in task.glob('output.*'))
    status = {'role': args.role, 'task': task.name, 'exit': code, 'secs': round(time.time() - started),
              'tools': tools, 'outputs': outputs, 'errors': errors[-3:]}
    (task / 'status.json').write_text(json.dumps(status, indent=1))
    print(json.dumps(status))


if __name__ == '__main__':
    main()
