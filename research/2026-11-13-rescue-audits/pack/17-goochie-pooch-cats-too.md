# Website Health Check: Goochie Pooch & Cats Too

**What we saw on 13 November 2026**

- goochie-pooch.com, the domain the salon used until 2020, loads a GoDaddy page reading "parked free, courtesy of GoDaddy.com", with a "Get This Domain" button and ad links naming the salon.
- The public domain record (RDAP) shows it registered in May 2011 and paid up to May 2031, with the owner's name and email hidden.
- The Google profile's website field points to tpaw.net, which redirects to pet.ecomify.net and stopped on a Cloudflare security-verification page ("Performing security verification") that did not clear.
- Nextdoor still shows "Claim page" and lists goochie-pooch.com as the website. Hours differ: Nextdoor Mon-Fri 9-5, Google Friday 9-4, GroomerJob/dogdog.org Tue-Sat 9-4.

**What it means for customers**

A name search lands on a GoDaddy parking page with a "Get This Domain" button, so it can look as if the domain is up for grabs rather than a route to services, hours or booking. Phone and Google are the reliable paths.

**How to fix it**

1. Confirm who controls the GoDaddy account holding the domain, then check renewal and hosting setup (owner, 0.5-1 h).
2. If it is the salon's, point it at a host and publish a one-page site; if not, register a new domain and drop the old one (owner 1-2 h, build 4-8 h).
3. Replace the Google profile's website link and settle on one set of hours (owner, 0.5-1 h).
4. Claim the Nextdoor page and fix hours on the other directories (owner/helper, 1-2 h).
5. Add a renewal reminder (paid to 14 May 2031) plus uptime and certificate alerts (helper, 1-2 h).

**After the fix**

Nextdoor is unclaimed and hours disagree across Google, Nextdoor, GroomerJob and dogdog.org; claiming them and publishing one set of hours is the cheapest next win.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** UNVERIFIED: check failed (High confidence)

**Outreach email draft (3 sentences)**

Hi - I run a small web research outfit in Milltown and I was checking how Goochie Pooch & Cats Too shows up online: the domain that used to be your website, goochie-pooch.com, now displays a GoDaddy "parked free" page with a "Get This Domain" button, and the website link on your Google profile points to a third-party directory that stopped on a Cloudflare security-verification page reading "Performing security verification". I've saved screenshots of what a customer sees on a desktop and on a phone, and I'm happy to show them to you with no obligation. If it's useful, I can also point out where your hours differ between Google, Nextdoor and the grooming directories - reply and I'll send the short write-up.

**Walk-in or phone opener (1 sentence)**

Hi, I was looking up Goochie Pooch online and the domain that used to be your website now shows a GoDaddy parking page, while the website link on Google stops on a Cloudflare security-verification page that says "Performing security verification" - can I show you a couple of screenshots I took of it?

**Sources**

- https://goochie-pooch.com/lander - live GoDaddy parking page (final URL after redirect from https://goochie-pooch.com/); screenshots goochie-pooch-desktop.png and goochie-pooch-mobile390.png saved in this folder
- https://rdap.org/domain/goochie-pooch.com - registry record: registration 2011-05-14T00:55:19Z, expiration 2031-05-14T00:55:19Z, last changed 2026-06-12T20:35:05Z, registrar GoDaddy.com, LLC, nameservers NS59/NS60.DOMAINCONTROL.COM, delete/renew/transfer/update client locks
- https://rdap.godaddy.com/v1/domain/GOOCHIE-POOCH.COM - registrar view: registrant is an individual; name, organisation, street, city, postal code and email redacted, country US. This view renders the same moments as 2011-05-13T19:55:19Z and 2031-05-13T19:55:19Z, about five hours off the UTC values in the registry record.
- https://web.archive.org/cdx/search/cdx?url=goochie-pooch.com&output=json - captures from 2013-03-28 to 2020-11-30, none from 2021 onward
- https://web.archive.org/web/20201130012033id_/http://www.goochie-pooch.com/ - last archived version of the salon's own site (title "goochie-pooch", meta description "Goochie Pooch & Cats Too -=* Grooming Salon *=-")
- https://www.google.com/maps/place/Goochie+Pooch+%26+Cats+Too/@40.4272818,-74.3826089,17z - 4.5 stars, Pet groomer, 737 NJ-18, East Brunswick, NJ 08816, (732) 432-9191, website field "tpaw.net" (link target https://tpaw.net/explore/goochie-pooch-cats-too/), Friday 9 AM-4 PM, shown as closed when checked; screenshot google-profile.png
- https://tpaw.net/explore/goochie-pooch-cats-too/ - redirects to pet.ecomify.net and stops on a Cloudflare security-verification page (tab title "Just a moment...", visible text "Performing security verification"); screenshot tpaw-gmb-website-destination.png
- https://nextdoor.com/pages/goochie-pooch-cats-too-east-brunswick-nj/ - "Claim page" shown; contact block lists goochie-pooch.com; Mon-Fri 9:00 AM-5:00 PM, Sat/Sun closed; recommendations dated 21 Apr 25 and 9 Nov 21; Fave Awards 2023 and 2024; founder story says the salon was founded in East Brunswick in 1994
- https://groomerjob.com/goochie-pooch-cats-too - 4.5 from 92 reviews, Tue-Sat 9:00 AM-4:00 PM, Monday closed; no website link seen on the page
- https://www.dogdog.org/pet-groomer/goochie-pooch-cats-too-east-brunswick - Tue-Sat 9 AM-4 PM, Monday closed; no website link seen on the page

**Open questions**

- Who holds the GoDaddy account and the contact email for goochie-pooch.com today, and is auto-renew on?
- Was the website deliberately taken down (for example, a site builder or hosting plan expiring)?
- Did anyone else take over the registration? RDAP's "last changed" date of 2026-06-12 is unexplained publicly.
- What are the real current hours, service list and prices?
- Is the salon taking appointments this month? The newest public activity we found is an April 2025 neighbour recommendation.
- Who set the Google profile's website field to tpaw.net, and is the profile claimed?

## Open issues from the checker

- "A name search lands on a GoDaddy parking page with a 'Get This Domain' button, so it can look as if the domain is up for grabs..." (audit_md, What it means for customers): Unsupported assertion about search results. No SERP screenshot or citation is given, and nothing in the record shows the domain appearing for a name search. When I tried brand searches myself, the results I could reach returned directories and the Google listing (yellowpages, nextdoor, groomerjob, dogdog, bbb), not goochie-pooch.com; Google, DuckDuckGo and Bing SERPs were blocked or unusable from this network, so the claim can be neither confirmed nor refuted, only flagged as unsourced. The verified paths to the parking page are the Nextdoor site link and typing the old address, not a name search.
- "Hours differ: Nextdoor Mon-Fri 9-5, Google Friday 9-4, GroomerJob/dogdog.org Tue-Sat 9-4" and "hours disagree across Google, Nextdoor, GroomerJob and dogdog.org": Each per-source figure is correct, but the framing overstates the disagreement. GroomerJob and dogdog.org list identical hours (Tue-Sat 9-4, Monday closed), so hours do not "disagree across" those two, and Google's Friday 9-4 matches them. The only hours conflict I could confirm is Nextdoor's Mon-Fri 9-5 against the 9-4 listings; Google's other six days were not visible in the limited Maps view, so a Google-vs-directory conflict on other days is unproven.
- "goochie-pooch.com, the domain the salon used until 2020": Stated as fact, but the archive only shows the salon's own site captured on that domain from 2013-03-28 to 2020-11-30; nothing proves it was abandoned on that date (the record's own caveats say the parking start date cannot be established). Minor, but it is an inference presented flatly.
- Body length of audit_md (limit 300 words): Counting the body text (headings excluded) comes to roughly 305-315 words, just over the brief's limit.
