# Triage backlog (paused 2026-11-13 10:15 on the owner's request)

The owner paused triage to work with what was done. Nothing here is lost: every remaining batch is already
cut and waiting with its brief.

## Done at pause
- Batches b001-b157 of 819 triaged (about 1,560 businesses; rerun `triage_tools.py rank` for the exact count).
- b001-b102: every inner-ring business with a website, reviews or other strong evidence (1,017 businesses).
- b103-b157: the first part of the inner-ring businesses with weaker evidence.
- Inner ring: Milltown, East Brunswick, North Brunswick, New Brunswick, Highland Park, South River, Spotswood,
  Helmetta.

## Waiting (b158-b819, about 6,600 businesses)
- b158-b231: the rest of the inner ring with weaker evidence (mostly directory-only listings).
- b232-b498: the outer towns with strong evidence (2,663 businesses). Best value of the backlog.
- b499-b819: the outer towns with weaker evidence (3,203 businesses).

## How to resume
1. Check memory (`free -m`) and close idle agents; each browser agent needs about 1.5 GB.
2. To continue the whole run: `setsid nohup bash research/2026-11-12-triage/loop.sh >> research/2026-11-12-triage/loop.out 2>&1 &`
   and a watcher: `setsid nohup python3 tools/watch.py research/2026-11-12-triage --every 60 --stall-mins 15 &`.
   The loop skips finished batches (`--skip-done`) and existing checker tasks, so it picks up at b158.
3. To run only part of it (for example the outer towns with strong evidence), call batch.py directly:
   `python3 tools/batch.py triage_analyst 4 research/2026-11-12-triage/b2[3-9][0-9]/ ... --browser --skip-done --thinking high --timeout 4200`,
   then `avenues.py repair` and `triage_tools.py rank`.
4. Speed seen: about 22 batches (220 businesses) an hour with 4 agents.

## Deferred deep audits (owner's choice, 2026-11-13)
The owner ran only the website health checks for the 26 hijacked, hacked, parked or lapsed domains
(research/2026-11-13-rescue-audits). Deferred:
- Full deep audits (tier 4) for the top 25 of ranking.csv: reuse business_researcher, opportunity_analyst,
  audit_writer and verifier as in runs/2026-11-11, adding front-door fixes (website, Google profile, intake,
  agent readiness) as an opportunity type before AI agents.
- Health checks for the other 68 operating businesses whose site is down (certificate errors, server errors,
  domains that no longer resolve): select with website_review.loads == false and a site listed, then run the
  same rescue_auditor / rescue_checker loop.

## Caveat
A batch that was stopped part-way has a partial output.json, and `--skip-done` treats it as done. Before
resuming, delete output.json in any batch whose status.json is missing or has no outputs.
