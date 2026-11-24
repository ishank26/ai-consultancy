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