# Website Health Check: SALON G AND SPA

**What we saw on 13 November 2026**
- The Google profile (1727 US-130, North Brunswick Township, NJ 08902; hair salon; 4.5 stars) lists two websites: hairbarnyc.com and http://mysalongandspa.com.
- mysalongandspa.com no longer serves the salon: in Chrome it redirects to an ad page on cf.triorook.site that renders blank on desktop and at 390 px phone width, and the page served for the domain is a ParkLogic parking script. A non-browser HTTPS request to it fails certificate verification.
- hairbarnyc.com leads to Hair Bar NYC's booking site, which lists New York and Florida salons only.
- Google's "Book online" button works: it opens the salon's Square page, which lists services with prices (Women Haircut & Blowout $50, Deep Conditioner $25).

**What it means for customers**
Someone following the profile's website links reaches a blank ad page or another chain's booking screen, not this salon. Services and prices are reachable only through "Book online".

**How to fix it** (effort is an estimate)
1. Check the Square account and the registrar account that held mysalongandspa.com; the archived site was Square Online. (0.5-1 hr)
2. If the domain is out of reach, remove it from the profile. (0.2-0.5 hr)
3. Remove hairbarnyc.com too unless the salon is still part of that chain. (0.2-0.5 hr)
4. Point the profile at the Square booking page meanwhile. (0.2-0.5 hr)
5. Publish a one-page site on a new domain (services, prices, hours, tap-to-call, Book button); update directories; add renewal and certificate checks. (4-10 hrs)

**After the fix**
The Square page already lists services with prices, so a working site can send visitors straight into booking.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** UNVERIFIED: check failed (High confidence)

# Founder notes - SALON G AND SPA (B00792)

**Outreach email draft**
Hi - I looked at how Salon G and Spa appears on Google and noticed that both website links on the profile lead somewhere other than the salon: mysalongandspa.com now opens a blank ad page, and hairbarnyc.com opens a different chain's booking screen that offers no New Jersey location. I put together a short page showing what a customer sees on a phone and on a desktop, plus the order I would fix the links in. If it is useful I can show you the screenshots and walk through it; nothing on your accounts was touched.

**Walk-in / phone opener**
"I stopped in because the website links on your Google listing currently send customers to an ad page instead of your salon - I have screenshots on my phone if you want to see it."

**Sources**
- Google Business Profile place page (name, address, category, 4.5 rating, hours, both website fields and their destinations, Book online destination, phone): https://www.google.com/maps/place/SALON+G+AND+SPA/@40.443065,-74.4732439,17z/data=!4m6!3m5!1s0x89c3c571fbacea13:0xdb35f99b01a46995!8m2!3d40.443065!4d-74.4732439!16s%2Fg%2F11j0czt3ys
- mysalongandspa.com as served today (ParkLogic script naming the domain and tenant): http://mysalongandspa.com/
- Screenshots: mysalongandspa-desktop.png, mysalongandspa-phone390.png (both the blank ad page)
- RDAP record, mysalongandspa.com: https://rdap.org/domain/mysalongandspa.com
- RDAP record, hairbarnyc.com: https://rdap.org/domain/hairbarnyc.com
- Wayback captures 2025-02-06 to 2026-01-18 for mysalongandspa.com: https://web.archive.org/cdx/search/cdx?url=mysalongandspa.com&output=text&fl=timestamp,original,statuscode,digest&collapse=digest&limit=60
- Last archived page (Square Online generator, site title, custom domain www.mysalongandspa.com): https://web.archive.org/web/20260118094405id_/https://www.mysalongandspa.com/
- Hair Bar NYC locations, New York and Florida only (screenshot hairbarnyc-locations.png): https://hairbarnyc.com/locations/
- Hair Bar NYC booking flow location list (screenshot hairbarnyc-booking.png): https://book.hairbarnyc.com/
- Salon Square booking page (services and prices; screenshot square-booking-page.png): https://book.squareup.com/appointments/vrvtrhybp21hn9/location/LPVEQBTCPBEVB/services
- Birdeye review mirror (4.7 stars, 117 reviews, hours, unclaimed profile, no phone shown on the page): https://reviews.birdeye.com/salon-g-and-spa-169813247044904
- Giftly listing (address, hours, unclaimed profile): https://www.giftly.com/gift-card/salon-g-and-spa-north-brunswick-2

**Open questions**
- Who holds the Square account and the registrar account for mysalongandspa.com, and was the domain renewal paid in early 2026?
- Is the North Brunswick salon still part of the Hair Bar NYC chain, or independent with an old chain link left on the profile?
- The profile shows (732) 410-7951 and the Birdeye listing shows no phone at all - is that the number they want customers to see, and where should it appear?
- Are the services and prices on the Square booking page up to date, and do they want to keep Square for booking?
- Do they still have the old site's photos and text to reuse on a replacement page?

## Open issues from the checker

- audit_md, 'What it means for customers': '...reaches a blank ad page or another chain's booking screen, not this salon.' Also severity_reason: 'the other into a different chain's booking flow' and the outreach email: 'hairbarnyc.com opens a different chain's booking screen'.: Stated as fact, but it is not supported and is probably wrong. The auditor's own founder_md lists the same point as an open question ('Is the North Brunswick salon still part of the Hair Bar NYC chain, or independent with an old chain link left on the profile?'), so the two documents contradict each other. Evidence points the other way: this is the salon's own first website field on its Google profile, Google returns this profile first for a search of 'Hair Bar NYC North Brunswick NJ' and shows no separate Hair Bar listing in New Jersey, the Giftly listing for the same address carries a review tip mentioning '24 K Hairbar keratin treatment', and directory listings name the business 'Hair Bar NYC @ Salon G' at 1727 US-130 (callupcontact.com, localstylist.com). None of that proves a franchise relationship, but it means 'a different chain, not this salon' cannot be printed or said to the owner.
- The lead is treated throughout as an independent salon (role requires 'not a chain or franchise'), and fix step 3 is 'Remove hairbarnyc.com too unless the salon is still part of that chain.': The business may be a Hair Bar NYC franchise location ('Hair Bar NYC @ Salon G'). I could not confirm or rule this out from a primary source: hairbarnyc.com/locations/ is a corporate page showing nine NY/FL salons, the booking site shows the same nine, and third-party pages that use the 'Hair Bar NYC @ Salon G' name are aggregator/directory sites I could not open for verification (Cloudflare check on localstylist.com, timeout on salonlookup.com). If it is a franchise, the website links on the profile may be controlled by the franchisor, so telling the owner to remove them would be bad advice.
- rescue.json, domains[2]: 'Manicure and Pedicure (listed as free, 30 min)': The booking page lists them as two separate services: 'Manicure - Free - 30 min' and 'Pedicure - Free - 30 min' (confirmed in Chrome today and in square-booking-page.png). Minor, and it does not affect audit_md, which only cites Women Haircut & Blowout and Deep Conditioner.
