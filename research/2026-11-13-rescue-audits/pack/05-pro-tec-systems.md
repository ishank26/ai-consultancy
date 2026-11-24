# Website Health Check: Pro-Tec Systems Inc

**What we saw on 13 November 2026**

- Google lists Pro-Tec Systems Inc, 607 Georges Rd, North Brunswick NJ 08902, (732) 828-7756, category "General contractor", rated 5.0 (no review count shown), unclaimed, website field protecsystems.net.
- The domain still serves the 2008 FrontPage site. https://www.protecsystems.net/ loads without a warning; https://protecsystems.net/ (no www) stops at "Your connection is not private", NET::ERR_CERT_COMMON_NAME_INVALID.
- The home page carries 110 unrelated links (handbags, "instagram followers", chatgpt) in a block pushed off-screen by an injected script; the feedback page carries 87. Visitors see a normal page; crawlers read the links.
- The Feedback form posts to FrontPage's _derived/nortbots.htm, the footer email is @protecsystems.org (a Squarespace "Coming Soon" page), and there is no mobile layout.

**What it means for customers**

Someone who types the domain without "www" meets a certificate warning before any content appears. Those who reach the page find a 2008-era layout with no tap-to-call and a form that cannot send a message.

**How to fix it**

1. Confirm who holds the Network Solutions login (domain paid to 29 Jan 2027) and the hosting account; change passwords. Owner - 1-3 h.
2. Extend the certificate to the bare domain or redirect it to www; keep http redirected to https. Host - 2-6 h.
3. Strip the injected link block and its script from each page; ask the host to scan the account. Developer - 3-8 h.
4. Replace the dead form with a working service-request form, add tap-to-call, fix the footer email. Developer - 2-6 h.
5. Point the Google profile and MacRae's listing at the fixed address; recheck monthly. Office manager - 1-2 h.

**After the fix**

Claim the Google Business Profile - right category, hours, service area and photos of completed installs - so visitors can act on it.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** checked: PASS (High confidence)

**Outreach email draft**

Subject: What customers see at protecsystems.net

Hello - your Google listing shows protecsystems.net as the website, and typed without "www" Chrome stops at "Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID), while the www address does load. On the page itself, a block of 110 unrelated handbag and "instagram followers" links sits in the page code behind a script that moves it off-screen, and the Feedback form posts to a FrontPage file that cannot deliver a message. I have screenshots at desktop and phone width showing what a customer sees today, and would be glad to show them to you - nothing on the site has been changed.

**Walk-in / phone opener**

Quick one for whoever handles the website: protecsystems.net shows a certificate warning when typed without "www", and I have screenshots of what a customer sees if you would like to look at them.

**Sources**

- Live site, home page, loaded over https at www with no warning (110-anchor injected block, 119 anchors total, injected off-screen style script, no viewport meta, 2008 footer): https://www.protecsystems.net/
- Live site, feedback page (form action _derived/nortbots.htm; 87-anchor injected block, 91 anchors total): http://www.protecsystems.net/feedback.htm
- Bare domain over https, Chrome 'Your connection is not private', net::ERR_CERT_COMMON_NAME_INVALID: https://protecsystems.net/
- robots.txt returns a 404 'Page Not Found': http://www.protecsystems.net/robots.txt
- Google Business Profile panel (5.0 with no review count, 'General contractor', 'Claim this business', 'Add hours', website protecsystems.net, phone (732) 828-7756, 607 Georges Rd): https://www.google.com/maps/place/Pro-Tec+Systems+Inc/@40.4696268,-74.4516802,17z
- MacRae's Blue Book listing with website link to http://protecsystems.net: https://www.macraesbluebook.com/search/company.cfm?company=586220
- RDAP protecsystems.net (registered 2008-01-29, expires 2027-01-29, last changed 2025-11-30, Network Solutions): https://rdap.org/domain/protecsystems.net
- RDAP protecsystems.org (registered 2026-10-21, expires 2029-10-21, last changed 2026-10-26, Squarespace Domains): https://rdap.org/domain/protecsystems.org
- Squarespace holding page ('We're under construction', noindex): https://protecsystems.org/
- Wayback capture 2023-01-29, no link block and no hiding script: https://web.archive.org/web/20230129055239/http://protecsystems.net/
- Wayback capture 2024-11-05, same link block and same hiding script: https://web.archive.org/web/20241105032156/http://protecsystems.net/
- NJ DCA fire protection contractor report, October 2026 (Pro-Tec Systems Inc, permit P00814, C4 fire alarm system, expires 04/30/2028): https://www.nj.gov/dca/dfs/pdf/Cont%20Cert%20Lists/Report%20Fire%20Protection%20Contractors%20October%202026.pdf
- Screenshots in this folder (retaken on 2026-11-13): screenshot-protecsystems-desktop.png, screenshot-protecsystems-mobile-390.png, screenshot-protecsystems-apex-https-privacy-error.png, screenshot-protecsystems-org-coming-soon-desktop.png, screenshot-google-maps-listing.png

**Open questions**

- Who holds the Network Solutions registrar login, and who holds the hosting account that is serving the old pages?
- Who last edited the site, and does anyone still have the FrontPage files?
- Is protecsystems.org (registered 2026-10-21, Squarespace, 'under construction') theirs, i.e. is a new site already in progress?
- Which mailbox is current - the footer uses @protecsystems.org, the contact block uses @protecsystems.net, and the phone number is 732-828-7756?
- Are there other places (Facebook, industry directories, email signatures, proposal templates) that still link to protecsystems.net?
