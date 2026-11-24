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