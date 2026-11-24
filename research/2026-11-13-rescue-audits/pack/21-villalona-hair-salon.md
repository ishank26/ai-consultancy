## Website Health Check: Villalona Hair Salon

### What we saw on 13 November 2026
- villalonahairsalon.com now serves a parking page saying the domain may be for sale, with no salon name, phone or hours (desktop and phone screenshots).
- The Google profile (hair salon, 4.6, 631 Georges Rd) lists its website as vagaro.com; its Book online button also goes there.
- Domain records: one registration from 14 April 2010, paid to 14 April 2027 at GoDaddy, with nameservers at Above.com.
- Wayback Machine: the salon's own page ("VILLALONA HAIR SALON", (732) 640-2800) on 26 March 2022; a parking page by 27 May 2024.

### What it means for customers
Anyone who types the old address lands on a for-sale page with no salon information, and we found no public page that still links to it. The Google profile's website field and Book online button both go to Vagaro, so customers who find the salon through Google do not reach the parked domain.

### How to fix it
1. Confirm who can log in to the GoDaddy account holding the domain; it is paid to April 2027 (1-2 hrs, owner).
2. If it is still yours, replace the Above.com nameservers with your host's and turn off parking; if not, choose a new domain (1-2 hrs, web person).
3. Put a one-page site on it: name, address, hours, phone, services with prices, stylists, Vagaro booking link (8-20 hrs, web designer).
4. Point the Google profile's website field at that address (1-2 hrs, owner).
5. Add an uptime and renewal reminder (1 hr, web person).

### After the fix
Publish the menu and starting prices as text on the salon's own page, so search results and AI assistants can answer price questions without the booking platform.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** UNVERIFIED: check failed (High confidence)

## Outreach draft

Subject: Your old domain villalonahairsalon.com now shows a "for sale" page

Hi — I was looking up Villalona Hair Salon on Georges Road and noticed that villalonahairsalon.com, which by the Wayback Machine was your site in 2022, now shows a page that says the domain may be for sale, with no salon information on it. Your Google listing's website field and Book online button both go to your Vagaro page, so people who find you through Google still get to the booking page; the for-sale page is what someone sees if they type the old address. I have screenshots from a desktop and a phone if you would like to see exactly what that looks like, and I can walk you through who to ask about the domain account.

## Walk-in / phone opener

"Hi — I noticed villalonahairsalon.com now shows a 'domain may be for sale' page instead of your salon; I have screenshots of what it looks like on a phone if that's useful."

## Sources
- https://villalonahairsalon.com/ (live parking/for-sale page, checked 13 Nov 2026; screenshots shot-parked-desktop.png, shot-parked-mobile390.png)
- https://www.google.com/maps/search/villalona+hair+salon+631+Georges+Rd+North+Brunswick+NJ (name, hair salon, 4.6 rating, 631 Georges Rd, open at check time, (732) 640-2800; website field https://www.vagaro.com/villalonahairsalon; Book online button to vagaro.com/googlemap/.../services; shot-google-profile.png)
- https://rdap.org/domain/villalonahairsalon.com (registration 2010-04-14, expiry 2027-04-14, last changed 2026-04-15, GoDaddy.com LLC, Above.com nameservers)
- https://web.archive.org/web/20220326152229/https://villalonahairsalon.com/ (GoDaddy Website Builder page, title "VILLALONA HAIR SALON", phone (732) 640-2800)
- http://web.archive.org/web/20240527063352id_/https://villalonahairsalon.com/ (parking lander with window.park script, 27 May 2024)
- https://www.vagaro.com/villalonahairsalon (browser blocked by Imperva "Error 15" at 2026-11-13 21:34 UTC, shot-vagaro-blocked.png; plain fetch returned page title and description only)
- https://reviews.birdeye.com/villalona-hair-salon-170189478317752 (4.6, 84 reviews, address, hours; profile shows as unclaimed)

## Open questions
- Does the salon still have the login for the GoDaddy account that owns villalonahairsalon.com, and did anyone deliberately point it at a parking service?
- Was the 2010 site set up by the owner or by an outside person who kept the account?
- Does the salon still want this exact domain, or would it rather start fresh?
- Who currently updates the Google Business Profile and the Vagaro listing, and are the Vagaro services and prices up to date?

## Open issues from the checker

- audit_md: "we found no public page that still links to it" (and rescue.json "links_to_broken_domain": [] , severity_reason "damage is limited to anyone who types or follows the old brand domain"): Contradicted. The salon's own Vagaro profile - the page the Google profile's website field and Book online button both go to - has a contact block reading "Website: villalonahairsalon.com" linking to http://villalonahairsalon.com/ (same page also lists Phone (732) 640-2800, hours Thu-Fri 9-6, Sat 8-5:30). So a public page does still link to the parked domain, and a customer can reach it in two clicks from Google, not only by typing it. Verified in Chrome on 2026-11-13 (screenshot verify-vagaro-website-field.png in this folder).
- audit_md fix step 4: "Point the Google profile's website field at that address (1-2 hrs, owner)" / founder_md: "the for-sale page is what someone sees if they type the old address": The fix list never tells the owner to change the Website field on the Vagaro listing, which is the one place actually pointing at the dead domain, and the outreach note implies typing the address is the only route there.
- caveats: "A plain HTTP fetch of villalonahairsalon.com returns a small script page that reloads the URL with a tracking parameter; the for-sale wording and banner appear only once that script runs, so a reader without JavaScript sees neither the salon nor the parking text.": Not true of the page as served now. A plain HTTP GET with no JavaScript returned static HTML whose <title> is "villalonahairsalon.com" and whose body already contains "Find information, resources and relevant links... This domain may be for sale." plus the Terms/Privacy links; only the black top banner needs the script. A reader without JavaScript does see the for-sale text.
- severity_reason: "The damage is limited to anyone who types or follows the old brand domain": Built on the same wrong premise as issue 1 - the brand domain is one click from the Vagaro contact block that Google sends customers to.
