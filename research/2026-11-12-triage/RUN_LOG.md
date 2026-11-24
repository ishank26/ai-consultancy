# Run log: local triage (tiers 0-3), 2026-11-12 to 2026-11-13

## Outcome
- Mapping (research/2026-11-12-local-triage): 63 zone tasks, 8,439 listings, 8,169 after de-duplication.
  Zone checks: round 1 8 pass / 55 fail; round 2 22 pass / 33 fail, typically 75-90% of sampled entries
  confirmed. Leftovers labelled, not re-run (two-round rule); triage re-confirms each business anyway.
- Triage: paused by the owner at 157 of 819 batches (1,546 businesses, 1,351 operating), after all strong-evidence
  inner-ring businesses. Backlog and resume steps: BACKLOG.md.
- Checks (checks.sh): top 150 plus a 10% sample, 263 records: 129 confirmed, 129 corrected, 5 wrong business
  or closed. Applied to ranking.json / ranking.csv.
- Claude spot-checks (2026-11-13), all held: efoleyfirm.com self-signed certificate; adwaytech.com 502;
  ms3corp.com and trygar.com invalid certificate chains; rosedeb.com does not resolve; biondoroofing.com
  serves a Thai-language page; girgismd.com serves a gambling page; bussel.com hidden spam links (present only
  after scripts run, seen in a real browser); yuhasplumbing.com 6 tel: links and no form. Earlier: buschlaw.com
  certificate expired July 2024.
- Results written to the living doc ("Local triage: 1,546 businesses ranked") with a change-log row.

## Problems and fixes
- Leaked browser-harness daemons (they detach from the agent): run_agent.py now closes daemons with the slot's
  BU_NAME when the agent ends.
- Provider stream errors ("OpenAI Responses stream ended before a terminal response event") failed 5 zone
  revisions: reran them on slot 4; batch.py now retries a task once when it ends without an output file.
- Triage had no watcher at first: started watch.py on the triage directory.
- `pkill -f` matched the calling shell again (exit 144). Run pkill in its own command or match a narrower pattern.
- Ranking order within a score is batch order, not merit; 47 businesses score 17-18.

## 2026-11-13 16:50 health checks: round 1 checks done
- Round 1: 8 PASS, 18 FAIL; revisions 17 of 18 done at check-in time.
- Fix: verify-r1 folders got only rescue.json, not the screenshots, so checkers marked screenshot claims "unsupported". tools/avenues.py verify now copies *.png/*.jpg from the task folder and the latest revise folder into the verify folder (tested on a scratch copy). Applies from round 2; round 1 verdicts unchanged.
- Molnar Roofing: the checker found a public Chapter 7 petition by "Molnar Roofing, Inc." (D.N.J. case 26-18658, filed 2026-07-31). The revision adds a "check before any outreach" warning in the founder notes; the debtor's identity is not confirmed.

## 2026-11-13 17:30 health checks finished
- 26 checks; 16 PASS after 2 rounds, 10 UNVERIFIED (open issues listed in each pack file). pack/SUMMARY.md has notes added.
- Bussel's "hacked" finding rests on the 🐴 tab-title prefix, which is browser_harness's own tab marker (daemon.py), and an off-screen spam block the round-2 checker could not reproduce. The pack file is annotated "do not use as written".
- Spot-check: Morano Electric robots.txt verified live (195 lines, 192 sitemap, 128 .php, a sampled .php returns 404).
- Prompt change (owner told): added a BROWSER NOTE about the 🐴 marker to business_researcher, verifier, rescue_auditor and rescue_checker. Top-25 business_researcher tasks started after this pick it up; the 3 already running do not.
- 08 and 09 are the same practice (Crystal Smiles). Molnar (Chapter 7 petition) and Ajulia (NJDOL stop-work order): check before outreach.
- Top-25 deep audits started 17:30 (business_researcher, 3 parallel).

## 2026-11-13 18:45 top-25 check-in
- Profiles 25/25 (gate: 0 failing), analyses 25/25, no retries; audit writers running (4 parallel).
- Bussel's analysis carried the unconfirmed spam claim from triage. Added a CORRECTION to 05-audits/20-bussel-realty-corp/brief.md (task brief only, no role prompt change) before its writer ran.

## 2026-11-13 22:50 top-25 main loop done, two tasks short
- 05-audits-r1/24-njp-associates: the writer timed out (900 s, no output); revise.py reverify then crashed on the missing file, so 25-menlo never got its round-2 check. Pack showed both as UNVERIFIED, and Menlo's label referred to its pre-revision audit.
- Fix: revise.py reverify skips a missing revised audit. finish.sh reruns the NJP writer (1800 s), reverify, the verifier for NJP and Menlo, then the pack and LOOP_DONE. Still 2 rounds max.

## 2026-11-13 23:10 top-25 audits finished
- 25 audits in research/2026-11-13-top25-audits/deliverables; 15 PASS, 10 UNVERIFIED (NJP and Menlo still failed round 2 after finish.sh).
- Spot-check: Artheon (CME) contact page verified live: 7 phone numbers, only a search form, no enquiry form; "lorem ipsum" posts present (search returns 34 matches); 720 professionals on /about/.
- Living doc rev 28: new section "Website health checks and top-25 audits" plus a change-log row. Check-in cron deleted.

## 2026-11-14 zero-to-one action plan
- Owner asked for an action plan from the audits. Written to ZERO_TO_ONE.md and added to the living doc (section before "Top 10 opportunities", plus a change-log row). Four decisions left with the owner: employment contract, front-door fix price, Artheon size cap, healthcare agents off.
- 2026-11-14 later: owner said "plan both". ZERO_TO_ONE.md and the living doc now run two openers side by side (front-door-led walk-ins; agent-led emails with the demo line), with per-opener steps, numbers and an end-of-January keep rule. Decision 2 closed; 1, 3 and 4 still open.

## 2026-11-14 Step 1 materials
- PRICE_CARD.md/.pdf (one page; "Owner notes" section is cut from the print) and brand.json (placeholders for name, phone, email, site).
- tools/leave_behind.py renders printable leave-behinds: health checks from pack/ (founder notes, verdict and checker issues cut) and audits from deliverables/ ("For the founder", verdict, issues and every impact line cut). 26 + 25 PDFs, all one page, in each run's leave-behinds/. Eight audits keep a dollar figure that is a fact about the business (rents, a job ad, a mediator rate); the tool lists them on each run.
- Not done: business name, contact details, hosting location and the lawyer's read of the pilot terms; the data sheet and the pilot agreement.

## 2026-11-14 Jersey Soft Play (owner's request)
- Not in the 8,169-business map (a mobile party-rental service, East Brunswick, no storefront; one public directory listing found). research/2026-11-14-jersey-soft-play/loop.sh runs it end to end with one DeepSeek agent per stage: triage, triage_checker, then the top-25 deep-audit stages, pack and leave-behind. Stops with "STOP" in LOOP_DONE if triage finds it not operating. Claude reviews the outputs at the end.
- Jersey Soft Play done 13:16: triage operating, checker confirmed (no wrong claims); profile 12 facts, owner not named publicly; audit lead score 71; round 1 FAIL (7 issues: an overstated opener, a wrong navigation claim, "per trip" unsourced, an unlabelled assumption, 474-word body, a 64-vs-60 field count); round 2 PASS, high confidence, 29 claims checked, 2 wording notes. Claude re-verified live: packages $550/$650/$750, add-ons +$100/+$200, $100/hour; home page has a tel: link, a viewport tag and no form; /booking/ has no form and links to HoneyBook; XL bounce house 7.5x7x6 ft on /packages/. HoneyBook form content (XXL, reCAPTCHA) rests on the checker's browser read. Edited the deliverable's opener ("get a price" -> "check a date or get an all-in quote with delivery") per the round-2 note. leave_behind.py now also strips an italicised "Prepared from" line.
