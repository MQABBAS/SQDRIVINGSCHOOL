import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import SITE
import pages_main as M, pages_more as R, pages_extra as X, pages_comfort as C, pages_book as K, pages_seo as SEO, pages_knowledge as KN, pages_postcodes as PCD, pages_gearbox as GB, pages_niche as NI

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
pages = {
    "index.html": M.index(), "lessons.html": M.lessons(), "prices.html": M.prices(), "discounts.html": M.discounts(),
    "offer-m16-m18-m19.html": M.offer(), "intensive.html": M.intensive(),
    "tools.html": R.tools(), "postcode-checker.html": R.postcode_page(), "theory-quiz.html": R.quiz_page(),
    "hazard-game.html": R.hazard_page(), "test-centres.html": R.centres_page(), "student-portal.html": R.portal_page(),
    "areas.html": R.areas_page(), "faq.html": R.faq_page(), "contact.html": R.contact_page(), "about.html": R.about_page(),
    "privacy.html": R.privacy_page(), "review-policy.html": R.review_page(), "404.html": R.notfound_page(),
    "guides.html": X.guides_hub(), "comfort.html": C.comfort_page(), "book.html": K.book_page(), "gift-vouchers.html": K.voucher_page(), "first-lesson.html": C.first_lesson_page(), "road-signs.html": X.signs_page(), "dashboard-lights.html": X.dash_page(),
}
HOODS = SEO.neighbourhoods()
for b in R.BOROUGHS:
    html = R.borough_page(b)
    hoods = "".join(f'<a class="chip" href="../driving-lessons/{x["slug"]}.html">{x["name"]}</a>' for x in HOODS if x["borough"] == b[1])
    svcs = "".join(f'<a class="chip" href="../services/{x[0]}-{b[0]}.html">{x[1]}</a>' for x in SEO.SERVICES)
    marker = '<div class="mt-3"><h3>Other areas</h3>'
    assert marker in html
    pcs = "".join(f'<a class="chip" href="../postcodes/{c[0].lower()}.html">{c[0]}</a>' for c in PCD.postcode_list(SEO.load_postcodes) if c[1] == b[1])
    html = html.replace(marker, f'<div class="mt-3"><h3>Postcodes in {b[1]}</h3><div class="hero__badges">{pcs}</div></div><div class="mt-3"><h3>Neighbourhoods in {b[1]}</h3><div class="hero__badges">{hoods}</div></div><div class="mt-3"><h3>Lessons in {b[1]}</h3><div class="hero__badges">{svcs}</div></div>' + marker)
    pages[f"areas/{b[0]}.html"] = html
pages["areas.html"] = SEO.areas_index(HOODS)
pages["services.html"] = SEO.services_index()
for n in HOODS:
    pages[f"driving-lessons/{n['slug']}.html"] = SEO.neighbourhood_page(n, HOODS)
for sv in SEO.SERVICES:
    pages[f"services/{sv[0]}.html"] = SEO.service_hub(sv, HOODS)
    for b in R.BOROUGHS:
        pages[f"services/{sv[0]}-{b[0]}.html"] = SEO.service_borough(sv, b, HOODS)
for g in X.GUIDES:
    pages[f"guides/{g[0]}.html"] = X.guide_page(g)
CODES = PCD.postcode_list(SEO.load_postcodes)
for e in CODES:
    pages[f"postcodes/{e[0].lower()}.html"] = PCD.postcode_page(e, CODES, HOODS)
pages["postcodes.html"] = PCD.postcode_index(CODES, HOODS)
pages["driving-lessons-near-me.html"] = PCD.near_me_page(CODES, HOODS)
for kind in ("automatic", "manual"):
    pages[f"{kind}-driving-lessons-manchester.html"] = GB.pillar(kind, HOODS)
    for n in HOODS:
        pages[f"{kind}-driving-lessons/{n['slug']}.html"] = GB.gearbox_area_page(kind, n, HOODS)
pages["nhs-driving-lessons.html"] = NI.nhs_hub()
pages["student-driving-lessons-manchester.html"] = NI.students_hub()
for h in NI.HOSPITALS:
    pages[f"nhs/{NI.slugify(h[0])}.html"] = NI.hospital_page(h, HOODS)
for c in NI.COLLEGES:
    pages[f"students/{NI.slugify(c[0])}.html"] = NI.college_page(c, HOODS)
pages["knowledge.html"] = KN.hub()
pages["knowledge/greater-manchester-driving-test-centres.html"] = KN.centres_overview()
for a in KN.ARTICLES:
    pages[f"knowledge/{a['slug']}.html"] = KN.article_page(a)
for c in KN.CENTRES:
    pages[f"knowledge/test-centre-{c[0]}.html"] = KN.centre_page(c)
for path, html in pages.items():
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)
LASTMOD = "2026-10-09"
groups = {}
for p in pages:
    if p == "404.html":
        continue
    sec = p.split("/")[0] if "/" in p else "main"
    groups.setdefault(sec, []).append(p)
index = ""
for sec, plist in sorted(groups.items()):
    urls = "".join(f"  <url><loc>{SITE}/{'' if p == 'index.html' else p}</loc><lastmod>{LASTMOD}</lastmod></url>\n" for p in sorted(plist))
    open(os.path.join(OUT, f"sitemap-{sec}.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    index += f"  <sitemap><loc>{SITE}/sitemap-{sec}.xml</loc><lastmod>{LASTMOD}</lastmod></sitemap>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{index}</sitemapindex>\n')
print(len(pages), "pages")
