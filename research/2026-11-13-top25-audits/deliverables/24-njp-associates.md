# Opportunity Audit — NJP Associates

NJP Associates has advised retirees, families and business owners from one Highland Park office for over 40 years, and advertises a free first meeting. On a phone, that offer is hard to act on.

## 1. A front door a customer can act on

**As a customer sees it** (pages checked for this audit): phone and email are plain text with no tap-to-call link, the online route is a four-field form with no scheduling, and Google says "Claim this business".

**The agent would do:** replace the form with a short qualified intake offering real first-meeting slots, send each enquiry a prep checklist, and claim that listing.

**Impact:** about 36–108 staff hours a year (our assumption: 5–15 hrs/mo × 12 × 60% automated) at $28.69/hour (customer-service-representative median, NJ, 2025; ×1.25 for benefits, our assumption) = about $1,032–$3,098 a year.

**Pilot:** 2–3 weeks — tap-to-call, qualified intake, booking calendar, claimed listing.

## 2. One record for each call, email and form

**As it stands:** no chat, CRM or booking tool is present; pages carry Google Tag Manager and GA4. Bing lists 8 AM–9 PM weekdays and Sunday. Worth checking together: where an evening enquiry lands?

**The agent would do:** log each enquiry in a light system it owns, sort it (prospect, client servicing, CPA request, vendor), draft a reply with two meeting times, and set follow-ups at 2, 7 and 21 days.

**Impact:** about 18–48 staff hours a year (our assumption: 3–8 hrs/mo × 12 × 50% automated) at $28.69/hour (same median, NJ, 2025; ×1.25 benefits, our assumption) = about $516–$1,377 a year.

**Pilot:** 3–4 weeks, draft-only at first.

## 3. Keep the published story matching the record

**As it stands:** the footer calls Norman Politziner an Investment Adviser Representative of Koehler Asset Management; the SEC/FINRA record updated 18 May 2026 says he is not currently registered as one.

**The agent would do:** index the site, disclosure text, listings and regulatory record so answers come with the source cited, then check published claims weekly and hand you a ranked correction list.

**Impact:** about 12–24 staff hours a year (our assumption: 2–4 hrs/mo × 12 × 50% automated) at $28.69/hour (same median, NJ, 2025; ×1.25 benefits, our assumption) = about $344–$688 a year.

**Pilot:** 3–4 weeks, starting with a 25-question citation test.

## Why this works

- Nothing is sent, published or booked without your approval.
- It works with the form, mailbox, calendar and listing you use.
- Public pages only; no client account data held.

## Suggested first step

A 20-minute walkthrough, then a small paid pilot on the front door.

Prepared from publicly available information. Estimates are illustrative and would be confirmed in a discovery session.

## For the founder (not part of the audit)

**Email draft:** Norman — your contact page shows the phone and email as plain text with no tap-to-call link, the online route is a four-field form with no scheduling, and the Google listing still shows "Claim this business". Your home page invites people to a free first meeting, so the gap between that offer and what a phone visitor can do with it seemed worth two minutes. We build small agents that sit on the tools a practice already uses, with a person approving what goes out, and a front-door pilot takes two to three weeks.

**Walk-in opener:** "I stopped by because your site offers a free first meeting but a visitor on a phone can't tap your number — can I show you in two minutes?"

**Note for the discovery session:** if analysis.json travels with this audit, quote the audit's figures rather than the analysis ranges — the audit applies an automation share plus a 1.25 benefits load, so its numbers are the conservative pair.

**Sources**

- https://www.politziner.com/ — "more than 40 years", free no-obligation first meeting, footer calling Norman Politziner an Investment Adviser Representative of Koehler Asset Management, Google Tag Manager and GA4 tags, no chat/CRM/booking tool
- https://www.politziner.com/contact — phone and info@ address as plain text (no tel:/mailto: links), four-field form (name, email, subject, message), no scheduling
- https://reports.adviserinfo.sec.gov/reports/individual/individual_711308.pdf — record updated 18 May 2026: not currently registered as an Investment Adviser Representative
- https://www.google.com/maps/place/NJP+Associates/@40.4981312,-74.4370936,17z — "Claim this business" on the listing
- https://www.bing.com/maps?q=NJP+Associates+47+Raritan+Ave+Highland+Park+NJ — 8 AM–9 PM Monday–Friday and Sunday, Saturday closed
- https://www.onetonline.org/link/localwages/43-4051.00?st=NJ — NJ customer-service-representative median, $47,740 (BLS 2025 wage data), used in all three estimates


---

**Check:** UNVERIFIED: check failed (High confidence)

## Open issues from the checker

- Section 2: "no chat, CRM or booking tool is present": Overstated. What was verified is that no chat widget, CRM embed or booking script is loaded on the website. An adviser can run a CRM, phone system or scheduling tool off-site that would never appear in the page source, so the flat statement could be read (and rebutted by the owner) as a claim about his internal operations. analysis.json is correctly careful ("no chat widget, CRM embed or booking tool is loaded").
- Section 3: footer says he is an IAR of Koehler Asset Management, while the SEC/FINRA record updated 18 May 2026 "says he is not currently registered as one": Each half is literally accurate on the sources I re-opened, but the juxtaposition implies a stronger finding than the record establishes. The IAPD report itself states that not all jurisdictions require IAR registration or may grant an exemption, and it lists no Koehler Asset Management relationship at all, so absence of a current IAR registration there does not by itself prove the footer is wrong. For a compliance-sensitive claim about a named adviser this needs the caveat, or it reads as an accusation.
- "For the founder" note: the audit's figures are "the conservative pair": True for opportunities 1 and 2 (audit ranges sit entirely below analysis.json's $1,400-$4,100 and $830-$2,200). Not true for opportunity 3: the audit gives $344-$688 while analysis.json gives $275-$1,100, so the audit's floor is higher than the analysis floor. analysis.json's own opportunity-3 range is also internally inconsistent (the $275 floor implies a 50% reduction at $22.95/hr, the $1,100 ceiling implies no reduction and no benefits load), so it should not be relied on for a comparison.
- Section 1 heading claim "advised retirees, families and business owners": Not wrong, but assembled from two pages: the home page says "more than 40 years" and mentions retirement, selling a business and trusts/estates; the client categories come from the site's own sections (Retirees & Pre-Retirees, Individuals & Families, Strategic Business Planning). The Sources list only cites the home page for this line.
