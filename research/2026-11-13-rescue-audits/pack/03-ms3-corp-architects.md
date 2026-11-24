# Website Health Check: MS3 Corp. Architects

**What we saw on 13 November 2026**

- ms3corp.com, the site on the firm's Google profile, does not open: ms3corp.com and www.ms3corp.com both stop at Chrome's "Your connection is not private" warning (NET::ERR_CERT_COMMON_NAME_INVALID), with a certificate issued to *.inmotionhosting.com.
- Over plain http the address shows an empty InMotion Hosting placeholder page headed "HOSTNAME", and ms3corp.com/services.html returns 404.
- The domain is not lost: the registration record shows it registered in 2010, paid to April 2029, last changed April 2024, registrar Tucows, nameservers at InMotion, and DNS still resolving.
- Customers are still sent there: the Google profile lists ms3corp.com, and nybizdb.com lists the same domain. Archived copies show a live site on 11 September 2025.

**What it means for customers**

Anyone who clicks the website link meets a security warning, and most will leave. The service and public-project pages that existed until recently are not readable by a customer or a search engine today.

**How to fix it**

1. Check the InMotion hosting account: is the plan active and ms3corp.com still attached? Renew or re-add it. (0.5-2 hours, owner plus host support)
2. Re-issue an SSL certificate for ms3corp.com in the hosting panel. (0.5-2 hours, host support or web person)
3. Restore the site from hosting backup, or republish a short site from the September 2025 archive. (4-12 hours, web designer)
4. Confirm domain auto-renew, then keep the Google profile link on the working https address. (under 1 hour, owner)
5. Add uptime and certificate-expiry monitoring so this is caught in days, not months. (0.5-1 hour, web person)

**After the fix**

The Google profile is still unclaimed: it shows "Claim this business" and "Add hours". Claiming it and adding hours, services and project photos would complete the listing itself, not just the website.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** checked: PASS (High confidence)

# Founder notes - MS3 Corp. Architects (B05565)

**Email draft (3 sentences)**

Hello - I'm writing from a small web consultancy in Milltown. I noticed that ms3corp.com, the site linked from your Google listing, currently opens to a browser security warning ("Your connection is not private") while the domain itself is still registered through 2029, and the old service page now returns a 404. I've saved screenshots of exactly what a visitor sees on a desktop and on a phone, and I'd be glad to send them over or show you the short list of hosting-side settings that usually explains this - would a 15-minute call this week be useful?

**Walk-in / phone opener (1 sentence)**

Hi - I'm calling because the website linked on your Google listing currently shows a security warning instead of your site; I have screenshots of what customers see and can show you in about two minutes.

**Sources**

- Domain record (registration 2010-04-23, expiry 2029-04-23, last changed 2024-04-09, registrar Tucows, InMotion nameservers): https://rdap.org/domain/ms3corp.com
- Live HTTPS failure, certificate error NET::ERR_CERT_COMMON_NAME_INVALID: https://ms3corp.com/ (screenshots: screenshot-https-ms3corp-desktop.png, screenshot-https-ms3corp-desktop-advanced.png, screenshot-ms3corp-mobile-390.png)
- http://ms3corp.com/ placeholder page (title "InMotion Hosting", body "HOSTNAME") and http://ms3corp.com/services.html HTTP 404: read by direct HTTP request on 13 Nov 2026
- DNS resolution of ms3corp.com and www.ms3corp.com to 173.205.126.156: https://dns.google/resolve?name=ms3corp.com&type=A
- Google Business Profile (36 Monticello Way, South River, NJ 08882; (848) 218-1744; Architect; 5.0; website ms3corp.com; "Claim this business"; "Add hours"): https://www.google.com/maps/search/MS3+Corp+Architects+South+River+NJ (screenshot-google-profile.png)
- Directory listing the domain as website http://www.ms3corp.com: https://www.nybizdb.com/company/ms3-corp-3796289/
- Archived live site 11 Sep 2025 (services, public projects, "Contact us online via our Online form"): https://web.archive.org/web/20250911153103/http://ms3corp.com/
- Archive history showing 200 responses from 2021 through 11 Sep 2025: https://web.archive.org/cdx/search/cdx?url=ms3corp.com&output=json&collapse=timestamp:6&from=2019&to=2026
- Directory profile describing the practice (South River, NJ): https://cisleads.com/company/details/49535
- 2005 NJDOT DBE directory entry (36 Monticello Way, (848) 218-1744, NAICS 541310 architectural services): https://www.nj.gov/transportation/business/procurement/ProfServ/documents/directory.pdf

**Open questions**

- Who holds the InMotion Hosting account and the registrar login today?
- Was the hosting plan cancelled, or was the site moved and the domain left pointing at the old server?
- Does any backup of the site files exist (host backup, a designer's copy, an old laptop)?
- Does the firm want the old site restored, or a smaller rebuilt one?
- Is the New York office (132 W. 31st St., shown on cached copies of the site) still active? We did not verify it.
- Is Mita Amin, listed as the contact in a 2005 NJDOT directory and on the firm's own site, still the principal and the right person to speak to?
- Was the site taken down on purpose, for example ahead of a relaunch?

