# Website Health Check: Morano Electric

## What we saw on 13 November 2026

- moranoelectric.com loads normally (HTTP 200, valid certificate): the full business site with services, four regional phone numbers and a callback form.
- Its robots.txt has been overwritten with 192 sitemap lines; 128 point at .php files (groupon.php, recollection.php) that do not exist on this HTML site. Each one we tested returns 404.
- That robots.txt was clean in a 26 January 2022 archive capture and already injected by 25 July 2025.
- The domain is still registered through GoDaddy, paid to 25 October 2027 and transfer-locked. The Google listing (23 Serviss Ave, Electrician, 4.7 from 103 reviews) links to it and shows reviews from the past month.

## What it means for customers

A customer who taps the site today gets the real Morano Electric pages, so nothing looks wrong from outside. The change was made on the server that also receives the callback form, so it is worth closing out rather than leaving.

## How to fix it

1. Have the host scan the account and list recently changed files (2-4 hours).
2. Replace robots.txt and publish a real sitemap.xml (1-2 hours).
3. Change hosting, mail and form-script passwords, add two-factor, check mailbox forwarding (1-2 hours).
4. Keep the domain locked, funded and auto-renewing at the registrar (0.5-1 hour).
5. Clear the injected URLs in Search Console, submit the new sitemap, fix the contact-page street name and page titles (1-3 hours).

## After the fix

Put an estimate-request form on the contact page. The home page's main "LEARN MORE" button points there and the page has no form at all, while at phone width the header phone is hidden.

Prepared from publicly available information on 13 November 2026. We did not log in to or change anything.
