"""Human-readable HTML sitemap: every page on the site, grouped by section, built from the final pages dict."""
import re, html as H
from layout import *

SECTIONS = [
    ("main", "Main pages", "The essentials: lessons, prices, booking and contact."),
    ("learner-toolkit", "Learner toolkit", "Free interactive calculators and planners."),
    ("driving", "Toolkit pages", "Stopping distances, test-day planning, eyesight, hazard perception and more."),
    ("test-routes", "Driving test routes", "Road-by-road guides to every Greater Manchester test centre."),
    ("test-faults", "Driving test faults", "The most common reasons for failing, explained and fixed."),
    ("research", "Driving Data Lab", "Original research and statistics."),
    ("knowledge", "Knowledge hub", "Greater Manchester roads, rules and test centres."),
    ("guides", "Learner guides", "Practical guides for learner drivers."),
    ("services", "Lessons by type and borough", "Every lesson type in every borough."),
    ("areas", "Boroughs", "Driving lessons across the ten boroughs."),
    ("driving-lessons", "Neighbourhoods", "Driving lessons in every neighbourhood we cover."),
    ("automatic-driving-lessons", "Automatic lessons by area", "Automatic driving lessons, area by area."),
    ("manual-driving-lessons", "Manual lessons by area", "Manual driving lessons, area by area."),
    ("postcodes", "Postcodes", "Every postcode district we cover."),
    ("nhs", "NHS staff", "Lessons near Greater Manchester hospitals."),
    ("students", "Students", "Lessons near colleges and universities."),
]


def _title(html):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S) or re.search(r"<title>(.*?)</title>", html, re.S)
    t = re.sub("<[^>]+>", "", m.group(1)).strip() if m else ""
    return H.unescape(t).split(" | ")[0]


def html_sitemap(pages):
    groups = {}
    for p, html in pages.items():
        if p in ("404.html", "sitemap.html"):
            continue
        sec = p.split("/")[0] if "/" in p else ("learner-toolkit" if p == "learner-toolkit.html" else "test-routes" if p == "test-routes.html" else "test-faults" if p == "test-faults.html" else "research" if p == "research.html" else "knowledge" if p == "knowledge.html" else "main")
        groups.setdefault(sec, []).append((p, _title(html)))
    total = sum(len(v) for v in groups.values())
    nav = "".join(f'<a class="chip" href="#s-{k}">{n} ({len(groups.get(k, []))})</a>' for k, n, d in SECTIONS if groups.get(k))
    secs = ""
    for k, n, d in SECTIONS:
        items = groups.pop(k, [])
        if not items:
            continue
        lis = "".join(f'<li><a href="{p}">{H.escape(t or p)}</a></li>' for p, t in sorted(items, key=lambda x: x[1].lower()))
        secs += f'<section class="sm-sec" id="s-{k}" data-reveal="up"><h2>{n} <small>{len(items)}</small></h2><p class="note">{d}</p><ul class="sm-list">{lis}</ul></section>'
    for k, items in groups.items():
        lis = "".join(f'<li><a href="{p}">{H.escape(t or p)}</a></li>' for p, t in sorted(items))
        secs += f'<section class="sm-sec" id="s-{k}"><h2>{k.title()} <small>{len(items)}</small></h2><ul class="sm-list">{lis}</ul></section>'
    body = page_hero("Sitemap", "Every page on SQ Driving School.", f"All {total:,} pages, grouped by section — lessons, test routes, toolkit, research and every area we cover. Part of DriveSQ.", ["Sitemap"], "")
    body += f"""<style>.sm-nav{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:24px}}.sm-sec{{margin-bottom:34px}}.sm-sec h2 small{{font:600 .8rem var(--font-mono);color:var(--red);margin-left:6px}}
.sm-list{{columns:3 240px;column-gap:28px;padding-left:18px;font-size:.92rem}}.sm-list li{{break-inside:avoid;margin:0 0 6px}}</style>
<section class="section--tight"><div class="container"><nav class="sm-nav" aria-label="Sections">{nav}</nav>{secs}
<p class="note">Looking for the XML sitemap? It's at <a href="sitemap.xml">sitemap.xml</a>.</p></div></section>{cta("")}"""
    return page("sitemap.html", f"Sitemap — All {total:,} Pages | SQ Driving School", "Every page on SQ Driving School, grouped by section: lessons, test-route guides, learner toolkit, Data Lab research, and every borough, neighbourhood and postcode we cover.", body, "")
