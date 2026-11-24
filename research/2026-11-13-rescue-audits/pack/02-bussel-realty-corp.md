> **Reviewer note (Claude, 13 Nov 2026): do not use this check as written.** The horse emoji in the tab title is added by our own browser tool (browser_harness marks every tab it controls with it), not by bussel.com. The second check could not find the off-screen spam block either, in a plain fetch or in a clean browser. The "hacked" conclusion is probably wrong. The confirmed facts: the domain is registered to 2028, and /contact-us/ returns 404.

# Website Health Check: Bussel Realty Corp

**What we saw on 13 November 2026**

- bussel.com is registered through GoDaddy, paid to 1 August 2028 and registrar-locked, so it has not lapsed; whose GoDaddy login holds it is not visible from outside.
- The site loads normally in Chrome (logo, 732-287-3777, property search, listings, news), but the home page also carries an off-screen block of Vietnamese, Hebrew and Russian spam with four outbound links, and the tab title starts with a horse emoji.
- A plain fetch of the same page returns clean HTML with no emoji, so the altered version is served selectively; the emoji also appears on IIS's own 404 page.
- Google's profile (4.5, 2 Ethel Rd #202a, Edison NJ 08817) lists bussel.com; /contact-us/ returns a 404.

**What it means for customers**

Visitors see a normal, working site and no browser warning appeared; the text sits out of view. Google documents that hacked content can be dropped from results or labelled, so the risk is to visibility and trust.

**How to fix it**

1. Change hosting, FTP, database and staff-login passwords and add two-factor; have the GoDaddy account holder confirm the domain sits where expected (1-2 hours).
2. Compare the home page with the clean 4 August 2026 Wayback copy, then remove the block and emoji: templates and includes first, then /js files, server components, third-party tags (3-8 hours).
3. Ask the host to trace the entry point in access and FTP logs, then patch it (2-4 hours).
4. Check Search Console's Security Issues and Manual Actions, request a review once clean, add a weekly title and link check (1-2 hours).
5. Repair /contact-us/ and add a public enquiry route (2-4 hours).

**After the fix**

Add click-to-call on 732-287-3777 and a short requirement form; the contact page has no tel: link and its only form is the staff login.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** UNVERIFIED: check failed (High confidence)

# Founder notes - Bussel Realty Corp (B01139)

**Outreach email draft (3 sentences)**

Subject: Something on bussel.com you might not be able to see

Hi [name], while looking at commercial brokerages in Middlesex County I opened bussel.com in an ordinary browser and found an off-screen block of Vietnamese, Hebrew and Russian spam text with four outbound links on the home page, plus a horse emoji added to the browser tab title on the pages I opened. The site looks completely normal to a visitor, so I saved screenshots of the desktop and phone view along with the page code, and I am happy to send them to you or your developer. If it is useful, I can walk you through what I saw and where a developer would start looking.

**Walk-in / phone opener (1 sentence)**

"I was on bussel.com this morning and spotted hidden spam links on the home page that a visitor would never see - can I show you the screenshots?"

**Sources**

- https://bussel.com/ - live home page, HTTP 200; in Chrome the DOM holds div.dc at left:-9999px with 1,618 characters of Vietnamese, Hebrew and Russian text linking to vietnam-millionaire.me, portuguese-passport.online, top10binary.ru and top10shops.ru, and the title carries a horse emoji (13 Nov 2026)
- Screenshots: bussel-home-desktop-1440.png (1440px), bussel-home-mobile-390.png (390px), google-maps-profile.png
- https://bussel.com/news.asp - title carries the horse emoji, no off-screen block in the DOM
- https://bussel.com/contact-us/ - HTTP 404; the IIS error page title also carries the emoji
- https://rdap.org/domain/bussel.com - registration 1996-04-23, expiry 2028-08-01, last changed 2026-07-29, GoDaddy.com LLC (IANA 146), client delete/renew/transfer/update prohibited, NS49/NS50.DOMAINCONTROL.COM; no registrant details published
- https://web.archive.org/cdx/search/cdx?url=bussel.com&output=json&from=2024&filter=statuscode:200&collapse=timestamp:6 - monthly HTTP 200 captures from Feb 2024 to 4 Aug 2026
- https://web.archive.org/web/20260804094057/https://bussel.com/ - 4 Aug 2026 capture; clean title without emoji and no spam block
- https://www.google.com/maps/place/Bussel+Realty+Corporation/@40.5412402,-74.3948696,17z - profile: 4.5, 2 Ethel Rd #202a, Edison NJ 08817, "Located in: Durham Center", closed at the time of check, lists bussel.com, (732) 287-3777; screenshot google-maps-profile.png
- https://bussel.com/contact-us/commercial-real-estate/central-new-jersey - employee directory page; 0 tel: links; only form action /login.asp
- https://support.google.com/webmasters/answer/6347750 - Google guidance on hacked content, labels and review requests

**Open questions**

- Who holds the GoDaddy login for bussel.com, and which email address is on that account?
- Who holds the hosting/IIS login, and when were those passwords last changed?
- Who builds and maintains the classic ASP site - in-house, a web firm, or the host?
- When did the home page last change, and has anyone seen a rankings or traffic drop in Search Console?
- Is there a Google Business Profile login for "Bussel Realty Corporation", or is the profile unclaimed (the panel still shows "Add missing information" and "Add a photo")?
- Is there a New Brunswick office at all, or are those pages only service-area landing pages (the only address published on the site is Edison)?

## Open issues from the checker

- audit_md: 'the tab title starts with a horse emoji'; severity_reason: 'the page title is altered across the pages we opened'; founder_md email and Sources: 'a horse emoji added to the browser tab title'.: Not a property of bussel.com. The served HTML of https://bussel.com/, https://bussel.com/news.asp and https://bussel.com/contact-us/ contains clean titles with no emoji. In the same Chrome session the emoji also appears on pages that cannot be serving it: https://example.com (served title 'Example Domain') and the Google Maps profile page. So the prefix comes from the browser used for the check, not from the business's site. Quoting it to the owner in the outreach email as something on their site is wrong.
- audit_md: 'A plain fetch of the same page returns clean HTML with no emoji, so the altered version is served selectively; the emoji also appears on IIS's own 404 page'; likely_cause: 'whatever adds it acts on responses rather than only inside one page file'.: Contradicted twice. (1) The IIS 404 page as actually served (raw HTTP response for https://bussel.com/contact-us/) has the plain title 'IIS 10.0 Detailed Error - 404.0 - Not Found' with no emoji and no scripts on it. (2) Nothing is served selectively: a real browser fetch of https://bussel.com/ (same origin, cache disabled) returned 31,291 characters of HTML identical in substance to the plain fetch, with no emoji and no spam block; a navigation with page JavaScript disabled showed the same clean document. There is no server-side response modification to find.
- audit_md: 'the home page also carries an off-screen block of Vietnamese, Hebrew and Russian spam with four outbound links'; founder_md: 'the DOM holds div.dc at left:-9999px with 1,618 characters ... linking to vietnam-millionaire.me, portuguese-passport.online, top10binary.ru and top10shops.ru'.: The site does not serve that block. The HTML returned for https://bussel.com/ contains no such element and none of those four URLs, whether fetched plainly or from inside the browser (HTML length 31,286 vs 31,291 characters, no match). It appears only in the DOM of this particular Chrome after page scripts run, and it is not traceable to anything the page loads: no extra network request appears in the page's resource list, and none of the eight /js files the page loads contains the text. With page JavaScript disabled the element is absent, while other pages on the same site (news.asp, the contact directory, contact-us.asp) never show it. It is therefore not established as content of the business's site. The character count is also not reproducible: the block measured 1,615 characters of text (1,621 as rendered text).
- likely_cause: 'hacked' - 'the home page serves an off-screen block of gambling, passport and Russian-retail links' (also severity_reason and the email draft, which states it as something found on the site).: The reasoning is labelled an inference, which is correct, but every piece of evidence offered for it (emoji on the 404 page, selective serving, content added to the site's own pages) is contradicted above, so the conclusion 'injected spam on the business's own domain' is not supported by the audit's own tests. Telling a firm it has been hacked on this evidence is a false-alarm risk.
- fix_steps 1-3: change hosting, FTP, database, staff-login and mailbox passwords, hunt templates, /js files, IIS modules and ISAPI filters, then trace the entry point in host logs (1-2, 3-8 and 2-4 hours).: The sequence presumes a confirmed server-side compromise and points the developer at server components that the evidence does not implicate; the hours are plausible but would be spent on a fault that may not exist on the site. Step 5 also states that '/contact-us/' is the contact path, while https://bussel.com/contact-us.asp loads a working contact page.
- Body length of audit_md.: The body runs to roughly 340 words, above the 300-word limit for what the owner reads.
