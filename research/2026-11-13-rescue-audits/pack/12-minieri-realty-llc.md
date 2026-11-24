# Website Health Check: Minieri Realty LLC

**What we saw on 13 November 2026**

- The Google Business Profile for Minieri Realty, 735 Georges Rd, North Brunswick, NJ 08902, lists (732) 354-1957, shows the office open, and links its Website field to roysellsnj.com.
- roysellsnj.com does not load: Chrome reports "This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN) on desktop and at phone width; www.roysellsnj.com fails too. Public DNS shows the domain's nameservers refusing queries for the zone.
- The domain is still registered through GoDaddy until 31 Dec 2026, so the name has not lapsed - the DNS/hosting connection is what broke.
- A second address the old site promoted, newjersey2floridahomeswithroy.com, now shows a GoDaddy parking page with a "Get This Domain" button and keyword links. The archive shows the real brokerage site live on 9 April 2025.

**What it means for customers**

Someone who clicks the website link on the Google listing, or follows an old search result, gets an error page, so listings and the enquiry route are unreachable. The phone still works, which means calls are currently the only way in.

**How to fix it**

1. Confirm who holds the GoDaddy account and the Cloudflare DNS, and that auto-renew is on. (1-2 h)
2. Reconnect DNS - rebuild the zone or move nameservers back to GoDaddy - and check apex and www over HTTPS. (2-4 h)
3. Rebuild a small site: home, buy/sell, about, contact, with a valuation request form and tap-to-call. (8-20 h)
4. Update the website field on the Google profile and the portal profiles; retire the parked domain. (1-2 h)
5. Add an uptime check and a reminder before the domain renews. (0.5-1 h)

**After the fix**

Pull the reviews now split between realtor.com and Zillow onto the Google profile and request one after each closing; the profile is the page most customers see first.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** checked: PASS (High confidence)

**Email draft**

Subject: Minieri Realty's website link is showing an error page

Hello Roy,

I looked at Minieri Realty's listing on Google this week and the website link there (roysellsnj.com) does not load - visitors get Chrome's "This site can't be reached" page, at desktop and phone width alike. The public domain record still shows roysellsnj.com registered and paid through December 2026, so this looks like a DNS or hosting disconnection rather than a lost name, but the Google listing still points customers to it. I have desktop and phone screenshots of what a customer sees today and of a second domain, newjersey2floridahomeswithroy.com, which now shows a GoDaddy parking page, and I can show you both if that is useful.

**Walk-in / phone opener**

"Hi Roy - I was checking how Minieri Realty shows up on Google and the website link there is landing on an error page; the domain still looks paid up, so it is probably a DNS fix, and I have screenshots of exactly what customers see."

**Sources**

- Google Business Profile / Maps place page (name, address, phone, hours, website field): https://www.google.com/maps/place/Minieri+Realty/@40.4668944,-74.454509,17z
- roysellsnj.com live test: https://roysellsnj.com/ (screenshots shot-roysellsnj-desktop.png, shot-roysellsnj-mobile390.png)
- DNS query for roysellsnj.com nameservers (REFUSED / lame delegation): https://dns.google/resolve?name=roysellsnj.com&type=NS
- RDAP, roysellsnj.com: https://rdap.org/domain/roysellsnj.com
- RDAP, newjersey2floridahomeswithroy.com: https://rdap.org/domain/newjersey2floridahomeswithroy.com
- Parked second domain: https://newjersey2floridahomeswithroy.com/ (screenshots shot-nj2fl-parked-desktop.png, shot-nj2fl-parked-mobile390.png)
- Wayback snapshot of the live site, 9 April 2025 (MLS search, broker bio, mention of the Florida domain): https://web.archive.org/web/20250409102948/https://roysellsnj.com/
- Wayback snapshot of the parked second domain, 13 July 2025: https://web.archive.org/web/20250713064103/https://newjersey2floridahomeswithroy.com/
- Wayback index of roysellsnj.com captures: https://web.archive.org/cdx/search/cdx?url=roysellsnj.com&output=json
- realtor.com agent profile and Zillow profile (review counts, mobile number) - seen only as search results, pages blocked to direct checks on the day: https://www.realtor.com/realestateagents/56b8e609bb954c01006b238a ; https://www.zillow.com/profile/Roy%20Minieri

**Open questions**

- Who actually holds the GoDaddy login for roysellsnj.com and the Cloudflare account its nameservers point to, and is that person or agency still reachable?
- Was the site deliberately taken down (ended hosting/web contract) or did it break unexpectedly?
- Does he want to keep roysellsnj.com as the public address, and is newjersey2floridahomeswithroy.com still needed for the Florida referral angle?
- Does he have IDX/MLS feed access to reuse on a new site, and who provides it?
- Are the Google profile and the realtor.com/Zillow/LoopNet profiles under his own login, or a portal's?
