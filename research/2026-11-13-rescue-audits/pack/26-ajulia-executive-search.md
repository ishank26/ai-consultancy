# Website Health Check: Ajulia Executive Search

**What we saw on 13 November 2026**
- The website link on the Google listing, ajuliaexecutivesearch.com, redirects to https://www.airbase1.com/, an aviation web-design agency, at desktop and phone width; old Ajulia paths land there too.
- The domain over plain HTTP shows a hosting "Default Web Site Page". The job board at jobs.ajuliaexecutivesearch.com stops with a Chrome warning: its certificate is issued to airbase1.com and fails the name check.
- The domain record is current: registered 2012, paid to 14 June 2029, last changed 16 June 2026, GoDaddy, DNS at Cloudflare.
- Four public pages still link to it: Google, ClearlyRated, Birdeye and LeadIQ. The Google profile says "Claim this business" and has no hours or photos.

**What it means for customers**
A customer who clicks the website link reaches another company's sales page instead of Ajulia, and the old job board is blocked by a browser warning. We found no working page explaining what Ajulia does or how to reach a recruiter.

**How to fix it**
1. Sign in to GoDaddy and Cloudflare; confirm who controls the domain and where www, @ and jobs point (1-4 h).
2. If the domain is not yours, take the link down and move to a new one; if it is, repoint www and re-issue the jobs certificate (2-6 h).
3. Update the website link on Google, ClearlyRated, Birdeye and LeadIQ, claim the profile, and settle which address is current (1-2 h).
4. Publish a small site with services, open roles and tap-to-call, reusing the archived 2025 pages (8-20 h).

**After the fix**
A claimed profile with hours, photos and a working link; today the listing has neither and shows 2.5 stars.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.

---

**Check:** UNVERIFIED: check failed (High confidence)

**Outreach email (draft)**

Subject: Your Google listing's website link goes to an aviation design company

Hi [name] - I looked up Ajulia Executive Search today and the website on your Google listing opens an unrelated aviation web-design agency, while the old job board address stops with a browser certificate warning. I saved screenshots of both, plus the Google listing and the directory profiles that link to the same domain, and I can send them over or show you on a screen. If it helps, I can also take you through the fixes in the order I would do them - registrar and DNS first, then the listings.

**Walk-in / phone opener**

Hi - I was checking your Google listing and the website link takes people to an aviation design company instead of Ajulia; I have screenshots of it, can I show you?

**Sources**
- Google Business Profile: https://www.google.com/maps/search/Ajulia+Executive+Search+East+Brunswick+NJ
- Domain registration record (RDAP): https://rdap.org/domain/ajuliaexecutivesearch.com
- Public DNS for the apex: https://dns.google/resolve?name=ajuliaexecutivesearch.com&type=A
- Public DNS for www: https://dns.google/resolve?name=www.ajuliaexecutivesearch.com&type=A
- Public DNS for the jobs subdomain (69.167.165.235): https://dns.google/resolve?name=jobs.ajuliaexecutivesearch.com&type=A
- Public DNS for the retainedsearch subdomain: https://dns.google/resolve?name=retainedsearch.ajuliaexecutivesearch.com&type=A
- Wayback capture of the old homepage (19 Apr 2025): http://web.archive.org/web/20250419191500/https://www.ajuliaexecutivesearch.com/
- Wayback index of older pages: http://web.archive.org/cdx/search/cdx?url=ajuliaexecutivesearch.com&matchType=domain&output=json&from=20250420&to=20261113&limit=20&fl=timestamp,original,statuscode&collapse=urlkey
- Wayback index of the old job board (last captures 17 June 2025): http://web.archive.org/cdx/search/cdx?url=ajuliaexecutivesearch.com&matchType=domain&output=json&from=20250515&to=20261113&limit=20&fl=timestamp,original,statuscode
- Live break: https://www.ajuliaexecutivesearch.com/ and https://ajuliaexecutivesearch.com/ (both land on https://www.airbase1.com/); http://ajuliaexecutivesearch.com/cgi-sys/defaultwebpage.cgi (hosting default page); https://jobs.ajuliaexecutivesearch.com/ (certificate issued to airbase1.com); https://retainedsearch.ajuliaexecutivesearch.com/ (sign-in screen)
- Profiles that link to the domain: https://www.clearlyrated.com/staffing/nj-usa/new-brunswick-nj/ajulia-executive-search-new-brunswick-nj ; https://reviews.birdeye.com/ajulia-executive-search-154981789494430 ; https://leadiq.com/c/ajulia-executive-search/5a1da10f2300005e0092469a
- NJDOL stop-work order issued 21 April 2025 (announced 13 May 2025): https://www.nj.gov/labor/lwdhome/press/2025/20250513_Stop_Work.shtml
- Career.com posting (page title readable only, human check): https://www.career.com/job/ajulia-executive-search/division-manager/j202608060553049580162
- Screenshots in this folder: screenshot_ajulia_desktop_1440.png, screenshot_ajulia_mobile_390.png, screenshot_apex_http_default_page_1280.png, screenshot_jobs_subdomain_cert_error_1440.png, screenshot_jobs_subdomain_cert_error_390.png, screenshot_retainedsearch_login_1440.png, screenshot_retainedsearch_login_390.png, screenshot_google_maps_listing_1280.png, screenshot_clearlyrated_profile_1280.png, screenshot_birdeye_profile_1280.png

**Open questions**
- Who holds the GoDaddy login for ajuliaexecutivesearch.com, and who paid the renewal that runs to 14 June 2029?
- Who holds the Cloudflare DNS account, and what changed on 16 June 2026?
- Was the domain ever allowed to lapse, or was it handed to a web vendor at some point?
- Was the www record pointed at Airbase1's site on purpose, and by whom?
- Is web hosting still being paid for, and by whom?
- Which of the three published addresses (2 King Arthur Ct #10 North Brunswick; 1440 How Lane Suite 2E New Brunswick; 51 West Prospect Street Suite 204 East Brunswick) is the one customers should use?
- Is the firm trading now, and what is the status of the April 2025 stop-work order?
- Does the retainedsearch sign-in portal still matter, and does the jobs board need to exist?

## Open issues from the checker

- retainedsearch.ajuliaexecutivesearch.com: "No business content visible; not signed in and no credentials entered.": Contradicted. The page shows the Ajulia Executive Search logo with the tagline "Bridging the gap between possibility and reality" above the Email Address / Password / LOGIN fields - the auditor's own screenshot_retainedsearch_login_1440.png shows it, and my live view at 1280 px shows it too. It is a branded sign-in screen, not an unbranded one. Nothing else in the sentence is wrong (Email Address, Password, LOGIN, Forgotten your password?, English US all confirmed).
- likely_cause: "Apex and www resolve to Cloudflare addresses (172.64.80.1 for the apex, 172.67.213.38 / 104.21.45.105 for www)": Not reproducible. dns.google today returns 172.67.213.38 and 104.21.45.105 for BOTH the apex and www; 172.64.80.1 does not appear for the apex. The value is not in audit_md or founder_md, but as written it is a specific, checkable number that no longer holds (resolver/anycast variation or a later DNS change - either way it cannot be stated as fact).
- retainedsearch: "Loads a JavaScript-driven sign-in screen (browser title 'Loading')": The browser title today reads "Login", not "Loading" (the title changes as the app boots). As recorded it is a moment-in-time artefact presented as a property of the page.
- audit_md length: The body is 302 words by a straight whitespace count (markdown markers excluded), i.e. marginally over the 300-word limit.
- audit_md never mentions the NJDOL stop-work order while the record says status "operating" and severity_reason says "the business is not represented online today": Not false, and not hidden - the order, its date and the unconfirmed entity link are set out in caveats, fix_steps and the founder_md source list. But the owner-facing page reads as if the firm is simply trading with a broken website. If the April 2025 order is still in force (the NJDOL release says it stays until the liability is paid in full, and no later notice was found), that is the most important fact about this business today.
