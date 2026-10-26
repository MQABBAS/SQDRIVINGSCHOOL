import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import SITE
import pages_main as M, pages_more as R, pages_extra as X, pages_comfort as C, pages_book as K, pages_seo as SEO, pages_knowledge as KN, pages_postcodes as PCD, pages_gearbox as GB, pages_niche as NI, pages_research as RS, pages_toolkit as TK, pages_routes as RT, pages_faults as TF, pages_solihull as SOL, pages_sol_more as SOLM, pages_sol_roads as SOLR

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
pages = {
    "index.html": M.index(), "lessons.html": M.lessons(), "prices.html": M.prices(), "discounts.html": M.discounts(),
    "offer-m16-m18-m19.html": M.offer(), "intensive.html": M.intensive(),
    "tools.html": R.tools(), "postcode-checker.html": R.postcode_page(), "theory-quiz.html": R.quiz_page(),
    "hazard-game.html": R.hazard_page(), "test-centres.html": R.centres_page(), "student-portal.html": R.portal_page(),
    "areas.html": R.areas_page(), "faq.html": R.faq_page(), "contact.html": R.contact_page(), "about.html": R.about_page(),
    "privacy.html": R.privacy_page(), "review-policy.html": R.review_page(), "404.html": R.notfound_page(),
    "guides.html": X.guides_hub(), "comfort.html": C.comfort_page(), "book.html": K.book_page(), "passes.html": __import__("pages_media").passes_page(), "free-prize-draw.html": K.draw_page(), "gift-vouchers.html": K.voucher_page(), "first-lesson.html": C.first_lesson_page(), "road-signs.html": X.signs_page(), "dashboard-lights.html": X.dash_page(),
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
pages.update(RS.all_pages())
pages.update(TK.all_pages())
pages.update(RT.all_pages())
pages.update(TF.all_pages())
pages.update(SOL.all_pages())
pages.update(SOLM.all_pages())
pages.update(SOLR.all_pages())
import pages_sol_gaps as SOLG
_g = SOLG.gap_pages()
assert not (set(_g) & set(pages)), set(_g) & set(pages)
pages.update(_g)
import pages_sol_local as SOLL
_l = SOLL.all_pages()
assert not (set(_l) & set(pages)), set(_l) & set(pages)
pages.update(_l)
import pages_niche2 as NICHE2
_n2 = NICHE2.all_pages()
assert not (set(_n2) & set(pages)), set(_n2) & set(pages)
pages.update(_n2)
import pages_sitemap as SM
# hand-written inner-Manchester, Wythenshawe & Altrincham pages replace the templated versions
import pages_local as LOCAL
pages.update(LOCAL.all_pages())
for _d in ("driving-lessons", "automatic-driving-lessons", "manual-driving-lessons"):
    pages.pop(f"{_d}/chorlton.html", None)  # duplicate of chorlton-cum-hardy; a redirect file is kept in the repo
import pages_manchester as MAN
pages.update(MAN.all_pages())
# areas/manchester.html is the borough hub (postcodes, neighbourhoods) — the pillar owns "driving lessons Manchester"
_am = pages["areas/manchester.html"]
_old_t = "Driving Lessons Manchester | SQ Driving School"
assert _old_t in _am
_am = _am.replace("<title>" + _old_t + "</title>", "<title>Manchester Areas &amp; Postcodes We Cover | SQ Driving School</title>").replace('content="' + _old_t + '"', 'content="Manchester Areas &amp; Postcodes We Cover | SQ Driving School"')
_mk = '<div class="mt-3"><h3>Postcodes in Manchester</h3>'
assert _mk in _am
_am = _am.replace(_mk, '<div class="mt-3"><a class="btn btn--red" href="../driving-lessons-manchester.html">Driving lessons in Manchester — prices, test centres &amp; lesson planner →</a></div>' + _mk, 1)
pages["areas/manchester.html"] = _am
import pages_roads as ROADS, pages_places as PLACES
_new_places = PLACES.all_pages()
assert not (set(_new_places) & set(pages)), set(_new_places) & set(pages)
pages.update(ROADS.all_pages())
pages.update(_new_places)
# link the new pages from their hubs
def _inject(path, marker, html):
    assert marker in pages[path], (path, marker)
    pages[path] = pages[path].replace(marker, html + marker, 1)
_cards = lambda items: '<div class="grid grid--3" data-stagger=".05">' + "".join(f'<a class="rx-study" href="{h}" data-reveal="up"><span class="k-cat">{c}</span><h3>{t}</h3><p>{d}</p></a>' for h, c, t, d in items) + "</div>"
_CTA = '<section class="section--tight">\n  <div class="container">\n    <div class="cta zone-dark" data-reveal="zoom">'
_sec = lambda eyebrow, title, items: f'<section class="section"><div class="container"><div class="section__head"><div class="eyebrow">{eyebrow}</div><h2 data-split>{title}</h2></div>{_cards(items)}</div></section>\n'
_inject("guides.html", _CTA, _sec("Greater Manchester", "Local driving guides.", [(f"guides/{g[0]}.html", "Guide", g[1], g[2]) for g in PLACES.GUIDES] + [("roads.html", "Roads", "Road & junction guides", f"{len(ROADS.R)} roads learners worry about.")]))
_inject("student-driving-lessons-manchester.html", _CTA, _sec("Sixth forms &amp; schools", "More schools and sixth forms.", [(f"students/{x[0]}.html", "Students", x[1], x[2]) for x in PLACES.SCHOOLS]))
_inject("driving-lessons-manchester.html", _CTA, _sec("Know your roads", "Guides for Manchester learners.", [("roads.html", "Roads", "Road &amp; junction guides", f"{len(ROADS.R)} roads and junctions, how we teach them."), ("work.html", "Work", "Lessons around your job", f"{len(PLACES.WORK)} big workplaces, around shifts."), ("guides.html", "Guides", "Local driving guides", "Matchdays, 20 mph zones, box junctions and more.")]))
_inject("guides.html", _CTA, _sec("Questions people search", "Niche questions, straight answers.", [(f"guides/{g[0]}.html", "Guide", g[1], g[2][:90] + "…") for g in NICHE2.GUIDES]))
# chorlton.html is a redirect to chorlton-cum-hardy.html — point every link straight at the real page
for _p in list(pages):
    if "/chorlton.html\"" in pages[_p]:
        pages[_p] = pages[_p].replace("/chorlton.html\"", "/chorlton-cum-hardy.html\"")
pages["sitemap.html"] = SM.html_sitemap(pages)
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
    NEW = ("solihull", "driving-lessons-solihull", "research", "driving/", "test-routes", "test-faults", "learner-toolkit", "sitemap.html", "knowledge", "test-centres.html")
    lm = lambda p: "2026-10-24" if p in MAN.all_pages() or p == "areas/manchester.html" else "2026-10-16" if p.startswith(NEW) or p in ("book.html", "contact.html", "privacy.html") else LASTMOD
    _prev = {}
    try:
        import re as _re
        _prev = dict(_re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", open(os.path.join(OUT, f"sitemap-{sec}.xml")).read()))
    except OSError:
        pass
    _lm = lm
    lm = lambda p, _lm=_lm, _prev=_prev: max(_lm(p), _prev.get(f"{SITE}/{'' if p == 'index.html' else p}", ""))
    urls = "".join(f"  <url><loc>{SITE}/{'' if p == 'index.html' else p}</loc><lastmod>{lm(p)}</lastmod></url>\n" for p in sorted(plist))
    open(os.path.join(OUT, f"sitemap-{sec}.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    index += f"  <sitemap><loc>{SITE}/sitemap-{sec}.xml</loc><lastmod>{max(lm(p) for p in plist)}</lastmod></sitemap>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{index}</sitemapindex>\n')
print(len(pages), "pages")
