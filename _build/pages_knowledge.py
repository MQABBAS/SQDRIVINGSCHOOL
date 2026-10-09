"""Greater Manchester Driving Knowledge Hub pages."""
import re
from layout import *
from pages_more import BOROUGHS
from pages_extra import GUIDES
from knowledge_data import ARTICLES, CENTRES, GOV_BOOK, GOV_FIND_CENTRE, DVSA_STATS

UPDATED = "9 October 2026"
UPDATED_ISO = "2026-10-09"
ART = {a["slug"]: a for a in ARTICLES}


def _ids(body):
    toc = []

    def rep(m):
        text = re.sub("<[^>]+>", "", m.group(1))
        hid = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
        toc.append((hid, text))
        return f'<h2 id="{hid}">{m.group(1)}</h2>'
    return re.sub(r"<h2>(.*?)</h2>", rep, body), toc


def _minutes(html):
    return max(2, round(len(re.sub("<[^>]+>", " ", html).split()) / 200))


def _schema(title, desc, path, faqs, crumbs):
    return [
        {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "datePublished": UPDATED_ISO, "dateModified": UPDATED_ISO,
         "author": {"@type": "Organization", "name": "SQ Driving School", "url": SITE}, "publisher": {"@type": "Organization", "name": "SQ Driving School", "logo": {"@type": "ImageObject", "url": SITE + "/favicon.svg"}},
         "mainEntityOfPage": SITE + "/" + path},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + u} for i, (n, u) in enumerate(crumbs)]},
    ]


def _article_shell(path, cat, title, desc, takeaways, body, faqs, sources, related_html, crumbs_html, crumbs_schema):
    root = "../"
    body, toc = _ids(body)
    mins = _minutes(body)
    toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    tk = "".join(f"<li>{t}</li>" for t in takeaways)
    faq_html = "".join(f'<details><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    src = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in sources)
    meta = f'<div class="article-meta" data-reveal="up"><span>Updated {UPDATED}</span><span>{mins} min read</span><span>By SQ Driving School · Greater Manchester</span></div>'
    out = page_hero(cat, title, desc, crumbs_html, root, meta)
    out += f"""<section class="section--tight"><div class="container article-grid">
  <article>
    <div class="takeaways" data-reveal="up"><h3>Key takeaways</h3><ul>{tk}</ul></div>
    <div class="prose">{body}
      <div class="callout callout--ok"><b>Learning with SQ?</b> 2-hour lessons £70 · 10 hours £350 (£320 NHS, students, M16/M18/M19) · free DriveSQ Student Portal. <a href="{root}book.html">Book in 60 seconds →</a></div>
      <h2 id="faq">Frequently asked questions</h2><div class="faq">{faq_html}</div>
      <h2 id="sources">Sources</h2><ul class="sources">{src}</ul>
      <p class="note">This guide is general information, checked against the official sources above on {UPDATED}. Rules and figures can change — always check GOV.UK before booking or travelling.</p>
    </div>
  </article>
  <aside>
    <nav class="toc" aria-label="On this page"><h4>On this page</h4><ol>{toc_html}<li><a href="#faq">FAQ</a></li><li><a href="#sources">Sources</a></li></ol></nav>
    <div class="card mt-2"><h3 style="font-size:1.1rem">Ready to start?</h3><p>Lessons across all of Greater Manchester.</p><a class="btn btn--red btn--block" href="{root}book.html">{icon('calendar')} Book now</a></div>
  </aside>
</div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Keep learning</div><h2 data-split>Related guides.</h2></div><div class="grid grid--3" data-stagger=".06">{related_html}</div>
<div class="center mt-3"><a class="btn btn--ghost" href="{root}knowledge.html">All Greater Manchester guides {icon('arrow')}</a></div></div></section>
{cta(root)}"""
    return out


def _related_cards(slugs):
    out = ""
    for s in slugs:
        if s in ART:
            a = ART[s]
            out += f'<a class="card" href="{s}.html" data-reveal="up"><div class="card__icon">{icon(a["icon"])}</div><span class="k-cat">{a["cat"]}</span><h3 class="mt-1">{a["title"]}</h3><p class="mb-0">{a["desc"][:110]}…</p></a>'
        elif s == "greater-manchester-driving-test-centres":
            out += f'<a class="card" href="{s}.html" data-reveal="up"><div class="card__icon">{icon("flag")}</div><span class="k-cat">Test centres</span><h3 class="mt-1">Every Greater Manchester test centre</h3><p class="mb-0">Which centre serves your area and how to choose.</p></a>'
    return out


def article_page(a):
    path = f"knowledge/{a['slug']}.html"
    crumbs = [f'<a href="../knowledge.html">Learn</a>', a["title"]]
    body = _article_shell(path, a["cat"], a["title"], a["desc"], a["takeaways"], a["body"], a["faqs"], a["sources"], _related_cards(a["related"]), crumbs, None)
    sch = _schema(a["title"], a["desc"], path, a["faqs"], [("Home", ""), ("Learn", "knowledge.html"), (a["title"], path)])
    return page(path, f"{a['title']} | SQ Driving School", a["desc"], body, "../", active="knowledge.html", schema=sch)


def _centre_link(name):
    for c in CENTRES:
        if c[1] == name:
            return f'<a href="test-centre-{c[0]}.html">{name}</a>'
    return name


def centre_page(c):
    slug, name, area, boroughs, intro, roads, skills = c
    path = f"knowledge/test-centre-{slug}.html"
    bl = ", ".join(f'<a href="../areas/{b[0]}.html">{b[1]}</a>' for b in BOROUGHS if b[1] in boroughs)
    others = [x for x in CENTRES if x[0] != slug and set(x[3]) & set(boroughs)]
    alt = ", ".join(f'<a href="test-centre-{x[0]}.html">{x[1]}</a>' for x in others) or "other nearby centres"
    sk = "".join(f"<li><span>{s}</span></li>" for s in skills)
    body_html = f"""
<h2>Who tests at {name}?</h2>
<p>{intro} Learners from {bl} commonly book here, but there's no catchment area for new bookings — you can book any centre on GOV.UK.</p>
<h2>What the roads are like</h2>
<p>{roads}</p>
<p>Your exact route isn't published in advance, and examiners vary routes. The best preparation is to be comfortable with the <i>types</i> of road around the centre rather than memorising one route.</p>
<h2>Skills to practise for {name}</h2>
<ul class="ticks">{sk}</ul>
<p>Every one of these is tracked as a skill in the DriveSQ Student Portal, so you'll know when you're ready.</p>
<h2>Booking a test at {name}</h2>
<p>Book on GOV.UK. Under the <a href="driving-test-booking-rules-2026.html">2026 booking rules</a> you can normally change a booking twice, and a booked test can only move to one of the three nearest centres. If {name} has a long wait, compare {alt}.</p>
<p>Pass rates for every centre are published in the DVSA's official statistics. Figures quoted on other websites often come from different years and don't agree, so check the official data if you want to compare.</p>
<h2>On the day</h2>
<ul><li>Bring your photocard provisional licence.</li><li>Arrive early — late arrivals can lose their test.</li><li>We provide the SQ car and a warm-up lesson around the area beforehand.</li><li>Read our <a href="../guides/test-day-checklist.html">test day checklist</a> and <a href="why-learners-fail-the-driving-test.html">the most common faults</a>.</li></ul>
"""
    faqs = [(f"Who usually takes their test at {name}?", f"Learners from {', '.join(boroughs)} commonly book {name}, but you can book any centre."),
            (f"Can I practise the {name} test routes?", "Routes aren't published and examiners vary them. We practise the types of roads around the centre so you're ready for any route."),
            (f"Where can I find the {name} pass rate?", "In the DVSA's official driving test statistics, published on GOV.UK.")]
    takeaways = [f"{name} serves {area} — commonly learners from {', '.join(boroughs)}.", "Prepare for the types of road around the centre, not one memorised route.", "Since 2026 you can normally change a booking twice, and only to nearby centres.", "Check the official DVSA statistics for pass rates."]
    title = f"{name} driving test centre: a learner's guide"
    desc = f"Guide to {name} driving test centre ({area}): who tests there, what the roads are like, skills to practise and how to book under the 2026 rules."
    crumbs = [f'<a href="../knowledge.html">Learn</a>', '<a href="greater-manchester-driving-test-centres.html">Test centres</a>', name]
    related = _related_cards(["greater-manchester-driving-test-centres", "driving-test-booking-rules-2026", "why-learners-fail-the-driving-test"])
    body = _article_shell(path, f"Test centre · {area}", title, desc, takeaways, body_html, faqs, [GOV_FIND_CENTRE, GOV_BOOK, DVSA_STATS], related, crumbs, None)
    sch = _schema(title, desc, path, faqs, [("Home", ""), ("Learn", "knowledge.html"), ("Test centres", "knowledge/greater-manchester-driving-test-centres.html"), (name, path)])
    return page(path, f"{name} Driving Test Centre Guide | SQ Driving School", desc, body, "../", active="knowledge.html", schema=sch)


def centres_overview():
    path = "knowledge/greater-manchester-driving-test-centres.html"
    rows = "".join(f'<tr><td><a href="test-centre-{c[0]}.html">{c[1]}</a></td><td>{c[2]}</td><td>{", ".join(c[3])}</td></tr>' for c in CENTRES)
    finder = ""
    for b in BOROUGHS:
        near = [c for c in CENTRES if b[1] in c[3]]
        finder += f'<details><summary>I live in {b[1]}</summary><div>Most {b[1]} learners test at ' + " or ".join(f'<a href="test-centre-{c[0]}.html">{c[1]}</a>' for c in near) + f'. <a href="../areas/{b[0]}.html">Lessons in {b[1]} →</a></div></details>'
    body_html = f"""
<h2>All Greater Manchester practical test centres</h2>
<table><tr><th>Centre</th><th>Area</th><th>Commonly used by learners from</th></tr>{rows}</table>
<p>There's no catchment area for new bookings: you can book any centre on GOV.UK. Since June 2026, moving an existing booking is limited to nearby centres — see <a href="driving-test-booking-rules-2026.html">the 2026 rules</a>.</p>
<h2>Which centre is nearest to me?</h2>
<div class="faq">{finder}</div>
<h2>How to choose a test centre</h2>
<ul><li><b>Familiarity:</b> testing near where you learn means familiar road types.</li><li><b>Waiting time:</b> compare several centres on GOV.UK — see <a href="driving-test-waiting-times-greater-manchester.html">waiting times</a>.</li><li><b>Travel:</b> you'll usually have a warm-up lesson first, so choose somewhere practical for you and your instructor.</li><li><b>Pass rates:</b> official figures are in the DVSA statistics. Differences between centres are usually smaller than the difference good preparation makes.</li></ul>
<h2>Theory test centres</h2>
<p>For the theory test, Greater Manchester learners commonly use the Manchester (Ardwick) and Stockport centres. See <a href="theory-test-greater-manchester.html">the theory test guide</a>.</p>
"""
    faqs = [("How many driving test centres are in Greater Manchester?", "Around ten practical test centres serve Greater Manchester, including Cheetham Hill, West Didsbury, Sale, Bredbury, Chadderton, Rochdale, Bolton, Bury, Hyde and Atherton."),
            ("Can I take my test at any centre?", "Yes, new bookings can be made at any centre. Moving an existing booking is limited to nearby centres.")]
    takeaways = ["Around ten practical test centres serve Greater Manchester.", "You can book any centre — there's no catchment area for new bookings.", "Compare waiting times at several centres on GOV.UK.", "Official pass rates are in the DVSA's statistics."]
    title = "Every Greater Manchester driving test centre"
    desc = "All Greater Manchester driving test centres — Cheetham Hill, West Didsbury, Sale, Bredbury, Chadderton, Rochdale, Bolton, Bury, Hyde and Atherton — and which to choose."
    body = _article_shell(path, "Test centres", title, desc, takeaways, body_html, faqs, [GOV_FIND_CENTRE, GOV_BOOK, DVSA_STATS], _related_cards(["driving-test-booking-rules-2026", "driving-test-waiting-times-greater-manchester", "theory-test-greater-manchester"]),
                          [f'<a href="../knowledge.html">Learn</a>', "Test centres"], None)
    sch = _schema(title, desc, path, faqs, [("Home", ""), ("Learn", "knowledge.html"), ("Test centres", path)])
    return page(path, "Greater Manchester Driving Test Centres Guide | SQ Driving School", desc, body, "../", active="knowledge.html", schema=sch)


def hub():
    root = ""
    cards = ""
    for a in ARTICLES:
        cards += f'<a class="card k-card" data-cat="{a["cat"]}" href="knowledge/{a["slug"]}.html" data-reveal="up"><div class="card__icon">{icon(a["icon"])}</div><span class="k-cat">{a["cat"]}</span><h3 class="mt-1">{a["title"]}</h3><p class="mb-0">{a["desc"]}</p></a>'
    cards += f'<a class="card k-card" data-cat="Test centres" href="knowledge/greater-manchester-driving-test-centres.html" data-reveal="up"><div class="card__icon">{icon("flag")}</div><span class="k-cat">Test centres</span><h3 class="mt-1">Every Greater Manchester test centre</h3><p class="mb-0">All ten centres, who uses them and how to choose.</p></a>'
    for c in CENTRES:
        cards += f'<a class="card k-card" data-cat="Test centres" href="knowledge/test-centre-{c[0]}.html" data-reveal="up"><div class="card__icon">{icon("flag")}</div><span class="k-cat">Test centres</span><h3 class="mt-1">{c[1]} test centre</h3><p class="mb-0">{c[4]}</p></a>'
    for slug, title, ic, desc, _ in GUIDES:
        cards += f'<a class="card k-card" data-cat="Skills &amp; tests" href="guides/{slug}.html" data-reveal="up"><div class="card__icon">{icon(ic)}</div><span class="k-cat">Skills &amp; tests</span><h3 class="mt-1">{title}</h3><p class="mb-0">{desc}</p></a>'
    cats = ["Tests & booking", "Manchester roads", "Learner life", "Test centres", "Skills &amp; tests"]
    cb = "".join(f'<button type="button" class="btn btn--ghost btn--sm" data-kcat="{c}" aria-pressed="false">{c}</button>' for c in cats)
    n = len(ARTICLES) + 1 + len(CENTRES) + len(GUIDES)
    body = page_hero("Greater Manchester Driving Knowledge Hub", "Everything learners in Greater Manchester need to know.", f"{n} fact-checked guides on tests, booking rules, local roads, test centres and learner life — written for Manchester, Salford, Trafford, Stockport, Tameside, Oldham, Rochdale, Bury, Bolton and Wigan.", ["Learn"], root)
    body += f"""<section class="section--tight"><div class="container">
<div class="k-filter" data-tool="kfilter"><input class="input" type="search" placeholder="Search guides — e.g. bus lane, insurance, Bolton" aria-label="Search guides"><button type="button" class="btn btn--red btn--sm" data-kcat="all" aria-pressed="true">All</button>{cb}<span class="chip js-kcount">{n} guides</span></div>
<div class="grid grid--3">{cards}</div></div></section>
{cta(root)}"""
    sch = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Greater Manchester Driving Knowledge Hub", "url": SITE + "/knowledge.html", "publisher": {"@type": "Organization", "name": "SQ Driving School"}}]
    return page("knowledge.html", "Greater Manchester Driving Knowledge Hub | SQ Driving School", f"{n} fact-checked guides for Greater Manchester learner drivers: 2026 test booking rules, test centres, bus lanes, trams, smart motorways, insurance and more.", body, root, schema=sch)
