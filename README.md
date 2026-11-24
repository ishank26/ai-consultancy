# AI Opportunity Audit pipeline

Claude acts as the orchestrator. Every subagent role runs on DeepSeek v4.1 Flash (Command Code) through `pi`, with
`pi-web-access` providing web_search, fetch_content, get_search_content and source_check.
No bash, no logins, no form posts.

- `prompts/` holds the role prompts from the prompt pack, plus `rules.md` (shared hard limits for every subagent).
- `tools/run_agent.py` runs one subagent in a task folder (`brief.md` in, `output.json` or `output.md` out,
  plus `log.jsonl` and `status.json`).
- `tools/batch.py ROLE N DIR...` runs many task folders N at a time.
- `tools/consolidate.py`, `gate.py`, `rank.py` and `revise.py` are the orchestrator's checks between phases.
- `research/<date>-<topic>/` holds avenue research (one brief per avenue, verified like the audits).
- `runs/<date>/` holds one run per date. `deliverables/` has the lead list, verified audits, patterns memo and run log.

Phase folders in a run: `01-map` (mapper per industry, `selection.json` and `buffer.json`), `02a-industry`,
`02b-business`, `03-analysis`, `04-rank`, `05-audits` (and `-rN` revisions), `06-verify` (and `-rN`).

Notes:
- `pi` needs stdin closed (`run_agent.py` does this) or it waits forever.
- `batch.py` prints results in input order, so a slow first task holds back the log. Check `status.json` per folder.
- Never launch a second batch over folders an earlier batch still has queued.
- Subagents sometimes write raw newlines inside JSON strings. Load with `json.loads(..., strict=False)` and re-save.

Physical/edge AI preference (added 2026-11-12):
- `prompts/avenue_researcher.md` and `avenue_verifier.md` research one camera/sensor/on-device avenue each.
  `tools/avenues.py verify|revise|table|playbook DIR ...` runs the verify-and-revise loop
  (`revise DIR N fail-only` once most have passed) and builds `avenues.json`, the analysts' playbook, from
  PASSed briefs only.
- To prefer these opportunities in a run: put `PREFER: physical` in the mapper CONFIG, add physical
  industries (restaurants, delis/grocers, 3PL, machine shops, property managers), and pass the playbook to
  `gate.py prep-analysis RUN research/<dir>/avenues.json`. The researcher now collects `physical_signals`;
  the analyst then makes one of three opportunities an E opportunity with `walk_in_checks`, and the writer
  adds "What to check on the visit".
- NJ: CCTV, access control and AI used for physical security are an "alarm business" under N.J.S.A. 45:5A-2
  (P.L.2021, c.2), including survey and design. Security installs need a licensed alarm or electrical
  contractor. Sensors (temperature, leak, vibration) are outside it; operations cameras are unresolved.
- Ultralytics YOLO is AGPL-3.0: buy the enterprise licence or ship Apache-licensed detectors (e.g. RF-DETR).

Pricing and opportunity plans (added 2026-11-12):
- `prompts/pricing_researcher.md` / `pricing_verifier.md` research what one market segment charges;
  `prompts/opportunity_planner.md` / `opportunity_plan_verifier.md` turn one audited opportunity into a
  build plan with competitors, prices, running costs, leverage, compliance and feasibility (inputs:
  audit.md, profile.json, analysis.json copied into the task folder, and into each revise folder).
- The same loop tool handles them: `tools/avenues.py verify|revise DIR N --kind pricing|plan`.
  `tools/avenues.py repair DIR` fixes output.json files with unescaped quotes (keeps output.raw.json).
- The owner's rule: at most 2 verification rounds, then use the briefs and label open verifier notes as
  unverified. Re-check by hand only the prices a decision or pitch depends on.
- To wait on a batch, match `pgrep -f "^python3 tools/batch.py"`; an unanchored pattern also matches the
  waiting shell's own command line and never returns.

## Startup advice research (added 2026-11-12)

`prompts/advice_researcher.md` and `prompts/advice_verifier.md` answer one question each about starting
the consultancy (first clients, buying behaviour, resources, risk, channels, partners). Run them like the
other kinds: `tools/avenues.py verify|revise DIR N --kind advice`, reading and writing `advice.json`.
See `research/2026-11-12-startup-advice/RUN_LOG.md`.
