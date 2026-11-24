# Startup advice research: run log, 2026-11-12

Asked by the owner before finalising the first-customer plan: "check any resources or advice or
suggestions for our business ... then show me the plan."

## Run

- Prompts: `prompts/advice_researcher.md`, `prompts/advice_verifier.md`; loop via
  `tools/avenues.py ... --kind advice`.
- Model: `commandcode/deepseek/deepseek-v4.1-flash` (pi), thinking high, 4 parallel.
- Seven questions: 01 first clients, 02 how SMBs buy AI, 03 packaging and retention, 04 NJ founder
  resources, 05 risk/legal/insurance, 06 vertical channels, 07 partner distribution.
- Two verification rounds (owner's cap), then stop.
  - Round 1: 1 PASS (05), 6 FAIL (4-10 notes each).
  - Round 2, on `revise-r1/`: 6 PASS, 1 FAIL (05, 4 wording notes: Insureon $1,300 floor not on
    page; "NJ does not require E&O" overstated; Aon 90% is share of potential coverage; Berkley
    exclusion attribution). Left labelled, per the owner's rule.
- Final briefs are `revise-r1/*/output.json`; round-2 notes in `verify-r2/*/output.json`.

## Claude spot-checks (re-opened 2026-11-12, all matched)

- NJ LLC: certificate of formation $100.00, annual report $75.00 (nj.gov/treasury/revenue/fees.shtml).
- NJSBDC Rutgers-New Brunswick serves Middlesex; virtual only for now.
- NJSBA Solo and Small-Firm Conference: Bronze $500 with opt-in attendee list; Silver $1,000;
  Gold $2,000. The form is for Feb 20-21, 2026 (already past); Feb 2027 is an assumption.
- Big I NJ associate: $400/calendar year; tech service providers named; Nov-Dec joiners renew
  the following year (page example: Nov 2026 join renews Jan 2028).
- Retell affiliate: 15% for 12 months, 90-day cookie, monthly payouts, referrals don't count to
  Solution Partner tiers.
- Insureon tech E&O: $110/month average for IT businesses; claims-made.
- MyCase consultant program: 10% of ACV annual, 5% monthly; certified after 3 accounts.
- NJAA: "Non-member suppliers / vendors cannot attend this event."
- N.J.S.A. 34:1B-265 own-time exception and its two carve-outs (employer business; work for employer).

## Output

The plan revision and resource table are in the owner's living doc
(https://claude.ai/artifact/EMuddoisDyw3YPYGAq4Wkx), section "First-customer plan: three tracks".
