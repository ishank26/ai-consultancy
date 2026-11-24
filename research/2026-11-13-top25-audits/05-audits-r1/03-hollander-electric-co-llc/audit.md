# Opportunity Audit — Hollander Electric Co LLC

Thirty-eight years trading, four master licences on the page, commercial and industrial electrical as the stated focus, and 24/7 emergency response sold to facility clients. What caught our eye is the front door: 31 town pages with no page titles.

### 1. Titles and a booking path for 31 town pages
**Now (checked 13 November 2026):** all 32 pages have an empty title, no description and no structured data; the sitemap lists the homepage alone.
**Build:** per-town titles and descriptions from existing copy, structured data with the four licences and service towns, redirects for old addresses, and a five-field request form offering call windows.
**Impact:** searchers and assistants get the town, trade and licences; requests arrive bookable, not callback-first. About 1–2 days, plus a week for booking.
**Pilot:** two weeks, validated in Search Console.

### 2. An after-hours line that answers
**Now:** 24/7 emergency response is advertised to commercial clients, but the web form is same-business-day and published hours are Mon–Fri 8:00–4:30 (third-party profiles).
**Build:** a voice and text agent answering after hours and on overflow — what is down, panel size, generator status, access — flagging commercial emergencies to the on-call electrician, who accepts before overtime. Pricing stays with you.
**Impact:** about 120–320 staff hours a year (25–40 leads a week × 20 minutes × 30–50% handled without a callback × 48 weeks — our assumptions) at $28.69–$32.81/hour (BLS medians, customer-service rep to dispatcher, NJ, May 2025, ×1.25 benefits — our assumption) = about $3,442–$10,500.
**Pilot:** four weeks on one number, weekly transcript review.

### 3. Watch the panels you already service
**Now:** public pages show switchgear, motor controls, standby generators and an industrial maintenance programme; nothing public shows how equipment is checked between visits — worth checking together: is a visit the first look?
**Build:** clamp-on current and temperature sensors at two or three customer sites plus generator exercise signals; drift raises a draft ticket to a named person who picks next visit or sooner. No camera, no audio, no face recognition; a person checks each alert.
**Impact (our inference):** about 10–60 electrician hours a year (2–3 sites × 5–20 avoided emergency hours per site) at $46.42/hour (BLS median electrician $77,250, NJ, May 2025, ÷ 2,080 hours, ×1.25 benefits — our assumption) = about $464–$2,785.
**Pilot:** four weeks at one maintenance customer, 30–60 days of baseline.

## Why this works
- Nothing is dispatched, priced or promised without a person approving it.
- It sits beside the tools already in use — site, Google profile, review platform, calendar.

## Suggested first step
A 20-minute walkthrough, then a small paid two-week pilot, priced before we start.

Prepared from publicly available information. Estimates are illustrative and would be confirmed in a discovery session.

## For the founder (not part of the audit)

**Email draft (personalise before sending).**

*Subject: two fixes on hollanderelectric.com — 20 minutes*

Hi Toby — I read through hollanderelectric.com and the Milltown page: the town pages carry no page title or structured business data, and the quote form has no field for the service address, so search results and AI assistants have little to work with. We build that machine-readable layer and a request form that captures what your callback would ask, with every price and dispatch still approved by you. Would 20 minutes on a screen share be worth it?

**Walk-in opener.** I was looking at your Milltown page and noticed none of the town pages carry a page title — is that already someone's job?

### What to check on the visit
- How many customers are on a written maintenance contract, what it promises (visit frequency, response time, generator ownership), and whether any contract already covers remote diagnostics.
- Spare space in panels and MCCs for clamp-on CTs; whether panels are live-work restricted or need a shutdown window.
- Cellular signal inside electrical rooms and generator enclosures; whether a BMS/BAS exists with an open protocol.
- Generator controller make and age — readable exercise status and fault codes without a vendor licence?
- Who at a customer site approves third-party sensors, and whether leases or landlords block it.
- Whether a maintenance customer has been lost after an unplanned failure.
- What a delivered maintenance report looks like today and who writes it.

## Sources
- https://hollanderelectric.com/ — stated commercial/industrial focus, the four licence numbers, 24/7 emergency claim, form fields, no booking, empty title and no structured data.
- https://hollanderelectric.com/sitemap.xml — homepage-only sitemap (lastmod 2026-09-03).
- https://hollanderelectric.com/residential.php — legacy indexed URL serving the same empty shell.
- https://hollanderelectric.com/electrician/milltown — 31 town pages and service-area copy.
- https://reviews.birdeye.com/hollander-electric-llc-889694528 — published hours Mon–Fri 8:00–4:30.
- https://www.google.com/maps/place/Hollander+Electric/@40.4835935,-74.497676,10z/data=!4m8!3m7!1s0x89c3c4583c2a3431:0x5f303e8f28a7c110!8m2!3d40.4835935!4d-74.497676!9m1!1b1!16s%2Fg%2F1xg5tmkb — 4.8 from 207 reviews; reviewer account of the owner taking a Friday call.
- https://www.neifund.org/hollanderelectric-llc/ — preventive-maintenance programme for industrial facilities, NEIF/JCP&L financing.
- https://api.bls.gov/publicAPI/v1/timeseries/data/OEUS340000000000043405113 — BLS OEWS New Jersey medians used for the wage lines (customer-service rep $47,740; dispatcher $54,590; electrician median $77,250).
