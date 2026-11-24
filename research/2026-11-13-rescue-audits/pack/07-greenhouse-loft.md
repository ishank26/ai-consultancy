# Website Health Check: Greenhouse Loft

## What we saw on 13 November 2026

- greenhouselofthp.com, the address the venue's own site still declares as home, opens an Indonesian/Malay-language MEGA888 casino page at cavaliercorneronline.com (screenshots saved).
- The working Squarespace site (arnold-weinberg-zgc3.squarespace.com) loads photos, day rates, FAQ and an enquiry form, but its canonical tag still names greenhouselofthp.com.
- Nextdoor (phone (732) 339-8044 shown publicly) and the Green Bowtie directory both link there.
- The Google Maps profile (4.6, Event venue, 431 Raritan Ave Second Floor) shows "Add website", "Add place's phone number" and "Add hours".

## What it means for customers

Typing the old address, or clicking from Nextdoor or Green Bowtie, reaches a gambling page with no route back to the venue. Visitors from Google see a rating and an address but no link, so the enquiry stops there.

## How to fix it

1. Confirm who controls the domain - the GoDaddy registration account and the Cloudflare DNS account (owner; 1-2 h).
2. If still yours, reset passwords, enable two-factor, remove unknown DNS records and point it at the Squarespace site; if not, use the registrar's abuse contact and ICANN's dispute process (owner + web person; 2-4 h).
3. Drop the greenhouselofthp.com canonical from Squarespace and fix the website field on Nextdoor, Green Bowtie and Facebook (web person; 1-2 h).
4. If it cannot be recovered, register a new one and connect it to the site (web person; 2-6 h).
5. Fill in the Google profile: website, phone, hours, photos (owner; 1 h).

## After the fix

Complete the Google Business Profile; adding website, phone and hours gives the rating page something a customer can act on.

---

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** UNVERIFIED: check failed (High confidence)

# Greenhouse Loft (B05499) - founder notes

## Outreach email draft

Hi - I'm [name] from [consultancy]. While checking listings for event venues in Highland Park I noticed that greenhouselofthp.com, the address your own website still names as its home, now opens an online-casino page, and the website links on your Nextdoor page and Green Bowtie listing point there too. I have desktop and phone screenshots from 13 November 2026 showing exactly what a customer sees, and I'd be glad to send them or walk you through them for ten minutes.

## Walk-in / phone opener

Hi, is this the team that runs Greenhouse Loft on Raritan Ave? I noticed the website address linked from your Nextdoor page now opens a casino page - I've got screenshots of what customers see and can show you.

## Sources

- https://www.greenhouselofthp.com/ (redirects to https://cavaliercorneronline.com/; the served page's canonical and og:url both name https://cavaliercorneronline.com/; screenshots `greenhouselofthp-domain-desktop.png`, `greenhouselofthp-domain-mobile390.png`)
- https://culturenightmarket.com/ (a separate domain name that opened today onto the same https://cavaliercorneronline.com/ casino page, same template)
- https://arnold-weinberg-zgc3.squarespace.com/ (live site; canonical tag and JSON-LD url = https://www.greenhouselofthp.com/, empty telephone/openingHours)
- https://arnold-weinberg-zgc3.squarespace.com/pricing (day rates for Friday, Saturday, Sunday and Monday-Thursday, plus hourly photoshoot rates)
- https://arnold-weinberg-zgc3.squarespace.com/contact-us (enquiry form; page says replies take up to 48 hours)
- https://www.google.com/maps/search/Greenhouse+Loft+431+Raritan+Ave+Highland+Park+NJ (4.6, Event venue, 431 Raritan Ave Second Floor, identifies as women-owned; 'Add place's phone number', 'Add hours', 'Add website' prompts)
- https://nextdoor.com/pages/greenhouse-loft-highland-park-nj/ (public page, no login: website field https://www.greenhouselofthp.com/, phone (732) 339-8044 as a tel: link, email greenhouseloft@gmail.com, short 'Our story' block)
- https://www.greenbowtie.com/venues/new-jersey/greenhouse-loft-highland-park ('Visit website' leads to greenhouselofthp.com with utm parameters; listing shows 4.7 from 52 reviews and 'On Green Bowtie since Mar 2026')
- https://www.facebook.com/people/Greenhouse-Loft/100076522939012/ (page title and 382 follower count visible without login; About/contact block requires login, so the website field was not re-read today)
- https://rdap.org/domain/greenhouselofthp.com (registered 2017-01-30, expires 2027-01-30, last changed 2026-03-15, GoDaddy, Cloudflare nameservers, client delete/renew/transfer/update prohibited, registrant redacted)
- https://web.archive.org/cdx/search/cdx?url=greenhouselofthp.com (venue site captured 2026-03-16 and 2026-04-02; casino content 2026-05-12; 301 responses from 2026-07-06)
- https://web.archive.org/web/20260402193335id_/https://www.greenhouselofthp.com/ and https://web.archive.org/web/20260512010315id_/http://www.greenhouselofthp.com/ (2 April 2026 capture is the venue site; 12 May 2026 capture is a MEGA888 page)
- https://www.instagram.com/greenhouse_loft/ ("Profile isn't available")
- https://greenhouseloft.com/ (a different venue of the same name at 2545 W Diversey Ave, Chicago, IL 60647)
- https://gregoryburrusproductions.com/event/lynette-sheard-and-glenn-merritt-trio-in-2025-icmad-evening-of-soul-fundraiser/ (public event at the venue, 24 May 2025)

## Open questions

- Who holds the GoDaddy account and the Cloudflare DNS account for greenhouselofthp.com today, and did anyone from the venue log in around April 2026?
- Was the site previously hosted on a plan that has since expired, or was the domain repointed without the venue's knowledge?
- Which address does the venue want going forward - the recovered old domain, or a new one?
- Is (732) 339-8044, the number Nextdoor displays publicly, the line they want customers to call (Google has none)?
- Does the Facebook page still carry the old address in its website field? Its About block is behind a login wall for us.
- Is the Instagram account still active under a different handle? @greenhouse_loft returned "profile isn't available".


## Open issues from the checker

- links_to_broken_domain[2], caveats[2] and data_gaps say the Facebook page's About/contact block 'now sits behind a login wall', so the website field 'could not be re-read today' and is 'carried over from the earlier pass'; founder_md repeats this as an open question.: Contradicted on 13 November 2026. Opened https://www.facebook.com/people/Greenhouse-Loft/100076522939012/ in a clean, logged-out browser: the Intro/About block rendered directly with 'A unique venue perfect for private events.', 'Page · Event', '431 Raritan ave 2nd Floor, Highland Park, NJ', email greenhouselofthp@gmail.com and the website field 'greenhouselofthp.com', plus 'Not yet rated (4 reviews)' and a September 2022 post. Only the scroll-triggered 'See more from Greenhouse Loft' gate requires login (the auditor's screenshot shows that gate). So the website field is verifiable without login and does still point at the old domain.
- audit_md bullet 2 ('its canonical tag still names greenhouselofthp.com') and fix step 3 ('Drop the greenhouselofthp.com canonical from Squarespace').: Accurate but not plain English for a venue owner: 'canonical tag' and 'canonical' are unexplained technical terms in the document the business reads.
