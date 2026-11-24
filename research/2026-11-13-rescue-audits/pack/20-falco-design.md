# Website Health Check: Falco Design

## What we saw on 13 November 2026
- The Google Business Profile lists falcodesign.com as the website, phone (732) 390-0099, category "Website designer", rating 3.7.
- In Chrome, falcodesign.com left the studio's site and landed on tr.l-bahiscasino-l.cam, an unrelated gambling domain that itself shows a Cloudflare 522 timeout (screenshots at desktop and 390 px).
- A direct request to the same domain returned HTTP 500 with a WordPress "critical error" page, so the redirect is added for browser visits rather than every request (inference).
- The domain is paid up (registered 1997, expires 16 Feb 2028, Network Solutions, HostGator nameservers); the last archived copy of the real homepage is 26 Sep 2025.

## What it means for customers
Anyone clicking the website link on Google, Instagram or about.me gets an error page for a gambling site instead of examples of the studio's work. Until it is fixed, the phone number on the Google profile is the dependable way to reach Falco Design.

## How to fix it
1. Check the Network Solutions registrar and HostGator hosting accounts, enable two-factor authentication and confirm renewals. Owner, 1-2 hours.
2. Take the WordPress install offline or restore a backup from before October 2025, then change all hosting, WordPress, database and mailbox passwords. Developer or host, 3-8 hours.
3. Re-test for redirects in a browser and by direct request, ask the host for a malware scan and request a Search Console review. Developer, 1-2 hours.
4. Meanwhile, remove or repoint the website link on Google, Instagram and about.me. Owner, 0.5-1 hour.
5. Rebuild a short clean site with services, portfolio, tap-to-call and a quote form, then re-link it. Designer or developer, 8-20 hours.

## After the fix
Maps still offers "Add missing information" and "Add a photo", shows no street address, and the rating is 3.7. Completing the profile and asking recent clients for reviews is a small follow-up that helps in local search.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** checked: PASS (High confidence)

## Outreach email draft

Subject: falcodesign.com is sending visitors to a casino site

Hi,

I'm with a small consultancy in Milltown, and while looking at design studios in East Brunswick I noticed that falcodesign.com currently sends visitors to an unrelated gambling domain, while the website link on your Google profile and Instagram still points there.

I have screenshots from 13 November at desktop and phone width, and I'm happy to send them over so you can see what a customer sees.

If it's useful I can also walk through what the public domain record and the web archive show about when it changed; whether you'd like help fixing it or just the screenshots is entirely up to you.

Best regards,
[Name], [Consultancy]

## Walk-in / phone opener

"Hi - do you look after falcodesign.com? When I opened it today it sent me to a casino site, and I have screenshots if you'd like to see them."

## Sources
- Google Maps place page (name, category, 3.7 rating, hours, phone, website field): https://www.google.com/maps/place/Falco+Design/@40.4070959,-74.5390155,11z
- Live site test (HTTP 500 WordPress error page, redirect to tr.l-bahiscasino-l.cam): https://falcodesign.com/ - screenshots falcodesign_desktop.png, falcodesign_mobile390.png, gmaps_place.png
- RDAP record (registration 1997-02-15, expiry 2028-02-16, last changed 2025-12-18, Network Solutions, HostGator nameservers): https://rdap.org/domain/falcodesign.com
- Wayback Machine snapshot, 2025-09-26 homepage: https://web.archive.org/web/20250926094258/https://falcodesign.com/
- Wayback snapshot index for falcodesign.com: http://web.archive.org/cdx/search/cdx?url=falcodesign.com&output=json&from=20240101
- Instagram profile with falcodesign.com bio link: https://www.instagram.com/falco_design/ - screenshot instagram_profile.png
- about.me profile linking to falcodesign.com/web-design/: https://about.me/falcodesign

## Open questions
- Who holds the Network Solutions registrar login, and who holds the HostGator hosting or cPanel login?
- Is there a clean backup of the WordPress site from before October 2025, and who looks after updates?
- When did the studio last see the site working, and is the falcodesign.com email address still in use?
- Did anyone receive a notice from the host or from Google about the site in the past year?
- Which social and directory profiles does the studio still control? Instagram is public; the LinkedIn page could not be opened.
