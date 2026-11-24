# Opportunity Audit — Stone Ridge Engineering, LLC

You have built a principal-led MEP/FP practice on referrals: 12+ years, a P.E. and an NJ electrical contractor licence. On 13 November 2026 the phone still works; the form and mobile menu do not, and the Google listing is unclaimed.

## 1. A contact form that cannot send

The page has five fields and a Submit button, but its action is `javascript:void(0)` and its jQuery is blocked, so submitting does nothing. At 390 px the menu opens nothing and the phone number is not tappable.

The agent would give the form a real endpoint, confirmation screen and alert to you, add tap-to-call and fix the menu.

Impact: a visitor who prefers web to phone gets nothing back; no analytics or call tracking exists to size traffic.

Pilot: 2–3 weeks. Worth checking together: how many enquiries arrive by web versus phone?

## 2. Enquiry-to-proposal drafting

Enquiries arrive as a call or a free-text comment, with no questions on building type, size, systems or deadline. The pages describe written reports; a scoping or priced proposal step is our inference — worth checking together?

The agent asks your qualifying questions, sorts by service line, drafts in your template and queues 3/7/14-day follow-ups. You set each fee; nothing sends without you.

about 48–307 staff hours a year (48–96 proposals × 4–8 hours each × 25–40% automated; volumes and hours are our assumptions; 25% from the ACEC 2025 estimate that AI could automate up to 29% of tasks, 40% from the Science 2023 writing study, both transfers) at $62.90/hour (O*NET NJ civil engineer median $50.32, 2025, ×1.25 benefits, our assumption) = about $3,019–$19,310 a year.

Pilot: one service line, due diligence first.

## 3. Past reports, searchable

Due diligence reports, feasibility studies and peer reviews are reusable documents; the site shows no portal or file-transfer tool.

The agent indexes your reports and standard details, answering with a citation or "not found" rather than a guess, and assembles draft skeletons marked unverified.

about 12–83 staff hours a year (48–52 weeks × 1–4 hours a week × 25–40% automated; weekly hours and automation shares are our assumptions) at $62.90/hour (same median, ×1.25 for benefits) = about $754–$5,220 a year.

Pilot: 12–24 months of one client's reports, 20 test questions you score.

## Why this works

- **You stay the engineer:** each fee, scope and conclusion is yours; software signs nothing.
- **Data stays yours:** one dedicated index, per-client separation, no client PDFs in chat tools.

**First step:** a 20-minute walkthrough, then a small paid pilot on the front door.

*Prepared from publicly available information. Estimates are illustrative and would be confirmed in a discovery session.*

## For the founder (not part of the audit)

**Email draft:** "Mr. Cioffi — I looked at stoneridgeeng.com the way a prospective client would: the Submit button on your contact form sends nothing, the phone-width menu doesn't open, and your Google listing still shows 'Claim this business'. There is a one-page audit of what a visitor runs into and what we would fix first. Would 20 minutes this week work for a walkthrough?"

**Walk-in opener:** "I'm local to the Route 1 corridor and noticed your website's contact form doesn't submit — I have a one-page audit of three fixes if you'd like to see it."

**Sources**

- https://stoneridgeeng.com/contact.html — five form fields, `javascript:void(0)` action, address, no published email
- https://stoneridgeeng.com/index.html — jQuery loaded over http on an https page, no `tel:` links, dead 390 px menu, no JSON-LD or meta description
- https://www.google.com/maps/search/Stone+Ridge+Engineering+North+Brunswick+NJ — 'Claim this business', 'Add hours', 'Add photos'
- https://stoneridgeeng.com/about.html — Robert Cioffi P.E., NJ electrical contractor licence, 12+ years
- https://stoneridgeeng.com/due-diligence.html — due diligence reports, feasibility studies and peer reviews as written deliverables; no proposal or scoping step described
- https://stoneridgeeng.com/mep-engineering.html — mechanical, electrical, plumbing and fire protection scope
- https://www.onetonline.org/link/localwages/17-2051.00?st=NJ — NJ civil engineer median wage $50.32/hour (BLS 2025 wage data)
- https://www.science.org/doi/10.1126/science.adh2586 — 40% faster completion on short professional writing tasks
- https://www.acec.org/resource/new-acec-research-institute-report-finds-ai-is-transforming-engineering-by-accelerating-human-talent/ — ACEC Research Institute 2025: 68% estimate AI could automate up to 29% of current tasks


---

**Check:** checked: PASS (High confidence)
