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