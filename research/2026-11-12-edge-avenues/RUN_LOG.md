# Run log: edge/physical AI avenue research, 2026-11-12

- **Agents:** 16 avenue researchers, then verify/revise rounds. All on DeepSeek v4.1 Flash via `pi`, 4–6 at
  a time, thinking "high".
- **Rounds:**
  - Round 1: all 16 FAIL.
  - Revised all 16, then round 2: 5 PASS with notes.
  - Revised all 16 again, then round 3: 11 PASS.
  - Revised the 5 FAILs only (`fail-only`), then round 4: 12 PASS.
  - Revised the last 4, then round 5: all 16 PASS.
  - Every task exited 0. No timeouts.
- **Common verifier catches:**
  - prices and figures not on the cited page;
  - benchmark numbers attributed to the wrong model;
  - arXiv preprints labeled peer-reviewed;
  - vendor claims rated above Low;
  - FTC allegations stated as findings;
  - "confirmed" set on legal points that were really unresolved;
  - fit sub-scores inconsistent with the legal evidence.
- **Checked by the orchestrator:** NJ alarm licensing, which neither research pass could open. I read
  P.L.2021, c.2 (C.45:5A-2, approved January 21, 2021) and P.L.1997, c.305 from pub.njleg.gov. Copies of
  the text are in the session scratchpad, not in this folder. The memo's Licensing column is my reading of
  those, not legal advice.
- **Not fixed:** minor notes that verifiers left on PASS verdicts (2–9 per brief, in `verify-rN/*/output.json`).
  The memo cites only items whose final brief passed.
- **Pipeline changes:**
  - `prompts/avenue_researcher.md` and `avenue_verifier.md`; `tools/avenues.py`.
  - Mapper: `PREFER: physical`.
  - Researcher: `physical_signals`.
  - Analyst: an E opportunity, `walk_in_checks`, hard limits and the NJ licensing rule.
  - Writer: camera and sensor wording, and "What to check on the visit".
  - `gate.py prep-analysis RUN AVENUES` passes each analyst only its industry's avenues.
- **Smoke test:** I ran the changed analyst once (`smoke-analyst/`) on Emporium International Foods (from
  2026-11-11), with the grocer/deli slice of the playbook. It made opportunity #1 a cold-chain sensor package
  with 9 walk-in checks, and it rejected loss-prevention cameras, citing missing evidence and the
  alarm-licensing rule. Lead Score 75; it was 76 before.
- **Not yet tested:** the changed mapper, researcher and writer prompts. The next batch is their first run.
