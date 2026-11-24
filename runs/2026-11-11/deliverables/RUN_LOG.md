# Run log — 2026-11-11

Orchestrator: Claude (Opus 5.5). Every subagent ran on DeepSeek v4.1 Flash (Command Code) through `pi` with
pi-web-access (web_search, fetch_content, get_search_content, source_check). The subagents were
read-only: no logins, form posts, outreach or bash. Plan: `PLAN.md`.

## Volume
- 13 market mappers gave 78 candidates; 1 duplicate was dropped, leaving 77; 50 were selected and 27
  kept as buffer.
- 13 industry evidence briefs: 8–9 task hotspots, 6–8 NJ wage benchmarks (BLS OEWS, May 2025) and 5–9
  automation evidence items each, with strength ratings.
- 50 business profiles, all past the gate (at least 3 sourced facts). None needed a rerun.
- 50 opportunity analyses (3 opportunities and a Lead Score each).
- 11 audits written (the top 10 plus Gaines, which replaced PDR). Verifier runs: 11 first checks, then
  28 re-checks across revision rounds.

## Candidates dropped and why
- **Duplicate:** "MX Logistics Group (MX Logistics)", the same firm as MX Logistics Group.
- **Outside the 15-mile radius:** Lyons & Associates (Somerville) and David M Sweeney Realty (Bridgewater).
- **Likely over 200 staff:** US Beverage Packers (650,000 sq ft plant) and Atlas Systems.
- **Poor fit:** Sunbird Software and InetSoft are software product vendors, adjacent to competitors.
- **No website found:** Winter and Company, PC.
- **Lower priority within their industry, kept as buffer (20):** Sai CPA, Pinnacle Accounting, NisonCo,
  Presidential Cleaning, Black Rock, Tomar Construction, Kim's Bike Shop, Aum Groceries, Hands On NJ PT,
  Monroe Parke Vet, Amore Roofing, RA Nichols, Frank G. Milo Agency, ABNET, Arndt & Sutak, MX Logistics,
  Palisades Logistics, Accelerated CNC, Barrood Real Estate, Molloy Bros.
- **Found over TARGET_SIZE after research:** Packaging & Distribution Resources (PDR). It had the top
  score (82), but its own site says 250–300+ full-time staff. I removed it from the ranking and promoted
  #11 Gaines & Associates. PDR's verified audit is kept in `deliverables/audits/out-of-scope/`.

## Verification failures fixed
All 11 first drafts failed. The recurring causes, with examples:
- **Arithmetic:** impact ranges that didn't follow from their own assumptions (every audit, in at least
  one round).
- **Facts contradicted by the business's own pages:**
  - Sayrebrook's Friday hours (they close at 5, not 7).
  - Rich's Plumbing does offer online scheduling.
  - Soden's office list (Manasquan is the John B. Wright partner, not a Soden office) and its review
    count (182, not 177).
  - Fraser Brothers' brand names (they are Fraser Brothers, DeLaurier and Kennedy & Ward; Edison,
    Belford and Tinton Falls are the towns).
  - RAM Law's hours (only the Manalapan office publishes them).
- **Misquoted studies:** NBER w31161 (the audit said "8–34%" and "no gain for experienced staff") and the
  Stanford legal-AI hallucination study (two figures merged).
- **Inferences stated as fact:** "every inquiry lands in one inbox", "each one keyed by hand", and
  "businesses like yours often…" lines.
- **The outreach notes:** "I work with agencies in Middlesex County", "I left a note at your front desk"
  and "I've watched Soden grow" described things that never happened. All removed.
- **Length:** every first draft ran 520–680 words. Final bodies are 440–467 by raw count, including title,
  bold labels and footer; the verifiers judged all of them within about 450.

Passed in round 2: RAM Law, RCP, Sayrebrook, Fraser Brothers, Wiley Lavender, Gaines. Passed in round 3:
Rich's, Albany County Fasteners, Benaka. Round 4 (verify only, after my edits): Soden.

**Edits I made myself after a PASS (each narrows a claim to its source wording; logged for review):**
- RCP: "over 15,000 doors across 125 associations, rental communities and commercial properties".
- Wiley Lavender email: "whose site reports 200+ successful cases a year".
- Benaka: QCS/RMS is listed as "a plus", not required.
- Albany: the error target is "per quarter".
- PDR: "Microsoft Dynamics is used to manage each client's business".
- Rich's: one review calls pricing "a little high".
- Soden: wording fixes before its round-4 verification, then "2021 partnership" in place of "division"
  after it passed.

These seven were not re-verified, apart from Soden's pre-round-4 fixes.

**Non-blocking notes the verifiers left on passed audits:**
- The ×1.25 benefits load is our assumption. It is labeled as such and is conservative: BLS ECEC puts
  benefits at about 30% of compensation.
- Several BLS API links return a daily-limit error when re-opened. The O*NET local-wage pages carry the
  same figures.
- LinkedIn and Indeed block automated checks, so figures that rest only on them (for example, LinkedIn's
  12-employee count for Sayrebrook) can't be re-verified.

## Process incidents
- **First smoke test hung for 10 minutes:** `pi` waited on stdin. The launcher now closes stdin.
- **Duplicate analyst batch:** I launched a third analyst batch over tasks a second batch still had
  queued (35–43). I stopped it within seconds, using its exact PIDs, cleared its partial files and
  relaunched it on 44–50 only. No outputs were affected.
- **Invalid JSON:** one analyst output (Trans American) had a raw newline inside a JSON string. I
  repaired it by re-parsing with `strict=False`.
- **Industry labels:** analysts wrote free-text labels, so ranking now uses the selection's labels.
- **Provenance:** a reverify helper re-copied the edited round-3 audits into `06-verify-r3/*/audit.md`,
  so those copies show the post-edit text rather than exactly what the round-3 verifier read.

## Open questions for the founder
1. **EXCLUDE was blank.** Are there conflicts to skip, such as your employer's clients, competitors or
   vendors?
2. **TARGET_SIZE.** The strongest 3PL prospects may sit just over 200 staff (PDR has 300+). Raise the cap
   for logistics?
3. **Barrood.** Barrood Agency (insurance) and Barrood Real Estate share a name and may be related. Only
   the agency was researched.
4. **Software/IT and B2B services** scored lowest, and MSPs partly compete with us. Keep them in the
   next batch?
5. **Accuracy check.** Gaines & Associates and Benaka were placed on public data alone. Benaka's headcount
   sources disagree (11–50 on LinkedIn, about 98 on ZoomInfo). Confirm before walking in.

## Status table (all 50)
| # | Business | Industry | Phase reached | Status | Issues |
|---|---|---|---|---|---|
| 01 | Matthews & Nulty, CPA | accounting | analyzed + ranked | rank 28 | thin evidence |
| 02 | Rizick & Rizick, CPAs | accounting | analyzed + ranked | rank 37 | thin evidence |
| 03 | Gaines & Associates, PC | accounting | verified audit (PASS) | rank 10 | failed first check; passed in verify round 2 |
| 04 | Premier Personnel Group, Inc. | b2b-services | analyzed + ranked | rank 34 |  |
| 05 | Rang Digitech LLC | b2b-services | analyzed + ranked | rank 49 | thin evidence |
| 06 | R3M Engineering, Inc. | b2b-services | analyzed + ranked | rank 18 |  |
| 07 | Affiliated Engineering Laboratories, Inc. (AEL) | b2b-services | analyzed + ranked | rank 39 |  |
| 08 | Epic Management, Inc. (Epic Incorporated) | construction | analyzed + ranked | rank 29 | thin evidence |
| 09 | Crisdel Group, Inc. | construction | analyzed + ranked | rank 14 |  |
| 10 | Benaka, Inc. | construction | verified audit (PASS) | rank 9 | failed first check; passed in verify round 3 |
| 11 | G William Group LLC (GWG) | construction | analyzed + ranked | rank 42 | thin evidence |
| 12 | Aroma Paradise | ecommerce-retail | analyzed + ranked | rank 13 | thin evidence |
| 13 | Albany County Fasteners | ecommerce-retail | verified audit (PASS) | rank 5 | failed first check; passed in verify round 3 |
| 14 | Emporium International Foods | ecommerce-retail | analyzed + ranked | rank 19 |  |
| 15 | Katie's Pet Depot | ecommerce-retail | analyzed + ranked | rank 46 | thin evidence |
| 16 | Central Jersey Pediatric Dentistry & Orthodontics | healthcare | analyzed + ranked | rank 16 |  |
| 17 | Gentle Dental Care, LLC | healthcare | analyzed + ranked | rank 27 | thin evidence |
| 18 | Central Jersey Physical Therapy Associates | healthcare | analyzed + ranked | rank 26 |  |
| 19 | Sayrebrook Veterinary Hospital | healthcare | verified audit (PASS) | rank 6 | failed first check; passed in verify round 2 |
| 20 | Arctic Air Conditioning | home-services | analyzed + ranked | rank 20 |  |
| 21 | AMEC Electric, LLC | home-services | analyzed + ranked | rank 36 | thin evidence |
| 22 | Rich's Plumbing Heating & Air Conditioning, Inc. | home-services | verified audit (PASS) | rank 3 | failed first check; passed in verify round 3 |
| 23 | Temp Control Heating & Air Conditioning | home-services | analyzed + ranked | rank 31 |  |
| 24 | Oliver L.E. Soden Agency | insurance | verified audit (PASS) | rank 4 | failed first check; passed in verify round 4 |
| 25 | Barrood Agency | insurance | analyzed + ranked | rank 35 | thin evidence |
| 26 | AGS Insurance Group, LLC | insurance | analyzed + ranked | rank 41 | thin evidence |
| 27 | Fraser Brothers Group, LLC | insurance | verified audit (PASS) | rank 7 | failed first check; passed in verify round 2 |
| 28 | RAM Law | legal | verified audit (PASS) | rank 1 | failed first check; passed in verify round 2 |
| 29 | Kemeny, Ramp & Renaud, LLC | legal | analyzed + ranked | rank 24 |  |
| 30 | Spevack Law Firm | legal | analyzed + ranked | rank 12 | thin evidence |
| 31 | Wiley Lavender Maknoor | legal | verified audit (PASS) | rank 8 | failed first check; passed in verify round 2 |
| 32 | Berk's Warehouse (Berks Warehouse) | logistics-3pl | analyzed + ranked | rank 45 | thin evidence |
| 33 | LOKI 3PL | logistics-3pl | analyzed + ranked | rank 43 | thin evidence |
| 34 | Packaging & Distribution Resources (PDR) | logistics-3pl | verified audit | excluded | over TARGET_SIZE (own site: 250–300+ staff); audit passed in verify round 3, kept as extra |
| 35 | Flex Logistics | logistics-3pl | analyzed + ranked | rank 17 |  |
| 36 | Hydracore Inc | manufacturing | analyzed + ranked | rank 32 |  |
| 37 | Supreme Manufacturing Co., Inc. | manufacturing | analyzed + ranked | rank 48 | thin evidence |
| 38 | Integrity Ironworks, Inc. | manufacturing | analyzed + ranked | rank 22 | thin evidence |
| 39 | Scientific Machine & Supply Company (SciMac) | manufacturing | analyzed + ranked | rank 15 |  |
| 40 | CMS Property Management | property-realestate | analyzed + ranked | rank 40 | thin evidence |
| 41 | Towne & Country Management | property-realestate | analyzed + ranked | rank 25 |  |
| 42 | RCP Management Company | property-realestate | verified audit (PASS) | rank 2 | failed first check; passed in verify round 2 |
| 43 | Ross Management Group | property-realestate | analyzed + ranked | rank 30 | thin evidence |
| 44 | Cloud Guardian LLC | software-it | analyzed + ranked | rank 44 | thin evidence |
| 45 | Technology Visionaries LLC | software-it | analyzed + ranked | rank 38 |  |
| 46 | DINI Communications, Inc. | software-it | analyzed + ranked | rank 47 | thin evidence |
| 47 | Trans American Trucking & Warehouse | trucking-freight | analyzed + ranked | rank 21 |  |
| 48 | All Brunswick Van Lines / All Brunswick Moving & Storage | trucking-freight | analyzed + ranked | rank 33 |  |
| 49 | Expressway USA Freightlines, Inc. | trucking-freight | analyzed + ranked | rank 11 |  |
| 50 | Total Source Logistics, Inc. | trucking-freight | analyzed + ranked | rank 23 |  |
