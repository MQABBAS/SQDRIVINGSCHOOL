# Premium local pages for inner Manchester, Wythenshawe and Altrincham.
# Replaces the templated postcode/neighbourhood pages for the districts in local_districts.py
# with hand-written content + SQ's own learner data (distance, instructor ratings, best times).
from layout import *
from pages_main import postcode_form
from pages_seo import faq_schema, crumbs_schema, prices_block
from local_districts import DISTRICTS
from local_facts import FACTS, miles_to_centre, score
from local_hoods_a import HOODS_A
from local_hoods_b import HOODS_B
from local_hoods_c import HOODS_C
from local_hoods_more import MORE

HOODS = {**HOODS_A, **HOODS_B, **HOODS_C}
OFFER = ("M16", "M18", "M19")
NAMES = {}  # slug -> display name
for _c, _d in DISTRICTS.items():
    for _s in _d["hoods"]:
        NAMES.setdefault(_s, None)

HOOD_NAME = {
    "city-centre": "Manchester City Centre", "piccadilly": "Piccadilly", "northern-quarter": "the Northern Quarter", "ancoats": "Ancoats",
    "new-islington": "New Islington", "deansgate": "Deansgate", "castlefield": "Castlefield", "spinningfields": "Spinningfields",
    "cheetham-hill": "Cheetham Hill", "crumpsall": "Crumpsall", "blackley": "Blackley", "higher-blackley": "Higher Blackley",
    "harpurhey": "Harpurhey", "charlestown": "Charlestown", "moston": "Moston", "newton-heath": "Newton Heath",
    "miles-platting": "Miles Platting", "collyhurst": "Collyhurst", "openshaw": "Openshaw", "clayton": "Clayton", "beswick": "Beswick",
    "prestwich": "Prestwich", "longsight": "Longsight", "ardwick": "Ardwick", "west-gorton": "West Gorton", "belle-vue": "Belle Vue",
    "gorton": "Gorton", "abbey-hey": "Abbey Hey", "chorlton-on-medlock": "Chorlton-on-Medlock", "victoria-park": "Victoria Park",
    "rusholme": "Rusholme", "fallowfield": "Fallowfield", "moss-side": "Moss Side", "ladybarn": "Ladybarn", "hulme": "Hulme",
    "levenshulme": "Levenshulme", "burnage": "Burnage", "didsbury": "Didsbury", "west-didsbury": "West Didsbury",
    "east-didsbury": "East Didsbury", "withington": "Withington", "parrs-wood": "Parrs Wood", "chorlton-cum-hardy": "Chorlton-cum-Hardy",
    "old-trafford": "Old Trafford", "whalley-range": "Whalley Range", "firswood": "Firswood", "trafford-park": "Trafford Park",
    "wythenshawe": "Wythenshawe", "northenden": "Northenden", "sharston": "Sharston", "benchill": "Benchill", "baguley": "Baguley",
    "brooklands": "Brooklands", "northern-moor": "Northern Moor", "altrincham": "Altrincham", "bowdon": "Bowdon",
    "broadheath": "Broadheath", "hale": "Hale", "hale-barns": "Hale Barns", "timperley": "Timperley",
}
def hname(s, cap=True):
    n = HOOD_NAME[s]
    return n[0].upper() + n[1:] if cap else n

HOOD_DISTRICT = {}
for _c, _d in DISTRICTS.items():
    for _s in _d["hoods"]:
        HOOD_DISTRICT.setdefault(_s, _c)
HOOD_DISTRICT["ardwick"] = "M12"
HOOD_DISTRICT["belle-vue"] = "M18"

NEAR = {  # neighbouring districts in this set, for internal links
    "M1": ["M2", "M3", "M4", "M12", "M13", "M15"], "M2": ["M1", "M3", "M4", "M15"], "M3": ["M1", "M2", "M15", "M16"],
    "M4": ["M1", "M8", "M11", "M40"], "M8": ["M4", "M9", "M25", "M40"], "M9": ["M8", "M25", "M40"],
    "M11": ["M4", "M12", "M18", "M40"], "M12": ["M1", "M11", "M13", "M18", "M19"], "M13": ["M1", "M12", "M14", "M15", "M19"],
    "M14": ["M13", "M15", "M16", "M19", "M20", "M21"], "M15": ["M1", "M3", "M13", "M14", "M16"], "M16": ["M15", "M14", "M17", "M21"],
    "M17": ["M16", "M21"], "M18": ["M11", "M12", "M19"], "M19": ["M12", "M13", "M14", "M18", "M20"],
    "M20": ["M14", "M19", "M21", "M22"], "M21": ["M14", "M16", "M20", "M23"], "M22": ["M20", "M23", "WA15"],
    "M23": ["M21", "M22", "WA15"], "M25": ["M8", "M9"], "M40": ["M4", "M8", "M9", "M11"], "WA14": ["WA15", "M23"], "WA15": ["WA14", "M22", "M23"],
}


def _bar(n):
    return f'<span class="lbar" aria-hidden="true"><span style="width:{n * 20}%"></span></span>'


def facts_card(code, root, title=None):
    f, d = FACTS[code], DISTRICTS[code]
    rows = "".join(f'<tr><td>{k}</td><td>{_bar(v)} <b>{v}/5</b></td></tr>' for k, v in f["ratings"].items())
    yn = lambda b: "Yes" if b else "No"
    return f'''<div class="card localdata"><div class="card__icon">{icon('chart')}</div><h3>{title or code + ' learner data'}</h3>
<p class="note mb-1">Our own figures from teaching in {code} — you won't find these on other driving school sites.</p>
<div class="localdata__score"><span class="localdata__num">{score(code)}</span><span>/10<br><small>SQ Learner Challenge score</small></span></div>
<table class="summary">{rows}
<tr><td>Distance to city centre</td><td><b>{miles_to_centre(code):.1f} miles</b> (straight line)</td></tr>
<tr><td>Trams in the area</td><td>{yn(f['trams'])}</td></tr><tr><td>Hills to practise on</td><td>{yn(f['hills'])}</td></tr>
<tr><td>Best time to practise</td><td>{f['best']}</td></tr><tr><td>Watch out for</td><td>{f['events']}</td></tr>
<tr><td>Usual test centre{'s' if len(d['centres']) > 1 else ''}</td><td>{' or '.join(d['centres'])}</td></tr></table>
<p class="note mt-1 mb-0">Ratings are our instructors' scores out of 5 (5 = most demanding). Score is weighted towards traffic and junctions.</p></div>'''


def offers_block(code, root, place):
    offer = code in OFFER
    first = (f'<article class="card neon-border" data-reveal="up"><span class="discount__who">{code} offer</span><span class="discount__badge">£320</span><p class="mb-0">Everyone picked up in {code} gets 10 hours for £320 — no ID needed.</p></article>' if offer else
             f'<article class="card" data-reveal="up"><span class="discount__who">10-hour block</span><span class="discount__badge">£350</span><p class="mb-0">Five 2-hour lessons, manual or automatic.</p></article>')
    return f'''<section class="section--tight"><div class="container"><div class="section__head"><div class="eyebrow">Offers in {place}</div><h2 data-split>Ways to save in {place}.</h2></div><div class="grid grid--3" data-stagger=".06">
{first}
<article class="card" data-reveal="up"><span class="discount__who">Students &amp; NHS staff</span><span class="discount__badge">£320</span><p class="mb-0">10 hours for £320. We'll check your uni/college student ID or NHS ID to confirm.</p></article>
<article class="card" data-reveal="up"><span class="discount__who">Free monthly draw</span><span class="discount__badge">£35</span><p class="mb-0">Tick the box when you book in 60 seconds for a chance to win a £35 lesson voucher. <a href="{root}free-prize-draw.html">How it works</a></p></article>
</div></div></section>'''


def _faqs_html(faqs):
    return "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)


def _std_faqs(place, code):
    offer = code in OFFER
    return [(f"How much are driving lessons in {place}?", "£70 for a 2-hour lesson (£35/hr) or £40 for a single hour. 10 hours is " + ("£320 for everyone picked up in " + code + "." if offer else "£350, or £320 for students and NHS staff once we've checked your ID.")),
            (f"Do you teach automatic in {place}?", "Yes — manual and automatic lessons are the same price, in dual-control cars.")]


def district_page(code):
    d, f = DISTRICTS[code], FACTS[code]
    root = "../"
    offer = code in OFFER
    place = code
    hood_cards = "".join(f'<a class="card" href="{root}driving-lessons/{s}.html" data-reveal="up"><div class="card__icon">{icon("pin")}</div><h3>{hname(s)}</h3><p class="mb-0">{HOODS[s]["line"]}</p></a>' for s in d["hoods"] if s in HOODS)
    ladder = "".join(f'<div class="step" data-reveal="left"><div class="step__dot">{i + 1}</div><div class="step__body"><h3>{t}</h3><p class="mb-0">{x}</p></div></div>' for i, (t, x) in enumerate(d["ladder"]))
    spots = "".join(f'<article class="card" data-reveal="up"><div class="card__icon">{icon("target")}</div><h3>{t}</h3><p class="mb-0">{x}</p></article>' for t, x in d["spots"])
    pick = "".join(f"<li><span>{p}</span></li>" for p in d["pickups"])
    near = "".join(f'<a class="chip{" chip--red" if c in OFFER else ""}" href="{c.lower()}.html">{c} · {DISTRICTS[c]["short"]}</a>' for c in NEAR.get(code, []))
    faqs = d["faqs"] + _std_faqs(code, code)
    offer_html = ""
    if offer:
        offer_html = f'<section class="section--tight"><div class="container"><div class="offer zone-dark" data-reveal="zoom"><div class="eyebrow">{code} special offer</div><h2>10 hours for <span class="glow-text">£320</span></h2><div class="offer__codes"><span class="offer__code">{code}</span></div><p>Every learner picked up in {code} saves £30 on a 10-hour block — no student or NHS ID needed.</p><a class="btn btn--red" href="{root}book.html">Book the offer</a></div></div></section>'
    body = page_hero(f"{code} · {d['short']} · {d['borough']}", f"Driving lessons in {code}.", f"Manual and automatic lessons across {d['name']}. Door-to-door pick-up, a real person on WhatsApp, and lessons planned around {code}'s roads.",
                     [f'<a href="{root}postcodes.html">Postcodes</a>', code], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="{root}book.html">{icon("calendar")} Book in 60 seconds</a><a class="btn btn--ghost" data-wa="Hi! I\'d like driving lessons in {code}." href="https://wa.me/{WA}">{icon("wa")} WhatsApp</a></div>')
    body += reassure() + offer_html
    body += f"""<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" class="prose"><h2 class="mt-0">What learning to drive in {code} is like</h2><p>{d['feel']}</p><p>{d['why']}</p>
  <p>Every lesson is logged in the free <a href="{root}student-portal.html">DriveSQ Student Portal</a>, so you can see your progress between lessons.</p></div>
  <div data-reveal="right">{facts_card(code, root)}</div>
</div></section>
{('<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Neighbourhoods</div><h2 data-split>Every part of ' + code + '.</h2><p class="lead">Each area has its own page with local pick-up points, roads and tips.</p></div><div class="grid grid--3" data-stagger=".05">' + hood_cards + '</div></div></section>') if hood_cards else ''}
<section class="section"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">Your road ladder</div><h2 data-split>From first lesson to test-ready in {code}.</h2><p class="lead">The order we usually build up your driving here. You move up when you're ready, not when the clock says so.</p></div>
<div class="timeline"><div class="timeline__fill"></div>{ladder}</div></div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Local hotspots</div><h2 data-split>Places {code} learners ask about.</h2></div><div class="grid grid--2" data-stagger=".06">{spots}</div></div></section>
<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" class="prose"><h2 class="mt-0">Your driving test from {code}</h2><p>{d['test']}</p><p>You book your test on <a href="https://www.gov.uk/book-driving-test" target="_blank" rel="noopener">GOV.UK</a>. We'll tell you when you're ready and practise the roads around your chosen centre. Read our <a href="{root}knowledge/greater-manchester-driving-test-centres.html">test centre guides</a>.</p></div>
  <div data-reveal="right" class="card"><div class="card__icon">{icon('car')}</div><h3>Popular pick-up points in {code}</h3><ul class="ticks">{pick}</ul><p class="note mb-0">Or anywhere else in {code} — home, school, college or work.</p></div>
</div></section>
{offers_block(code, root, code)}
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Prices</div><h2 data-split>Clear prices in {code}.</h2></div>{prices_block()}</div></section>
<section class="section"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">{code} FAQ</div><h2 data-split>Questions from {code} learners.</h2></div><div class="faq">{_faqs_html(faqs)}</div></div></section>
<section class="section section--alt"><div class="container"><div class="tool neon-border" data-reveal="up" style="max-width:820px;margin:0 auto">{postcode_form(True, "Check your full postcode")}</div>
<div class="mt-3"><h3>Nearby postcodes</h3><div class="hero__badges">{near}<a class="chip" href="{root}postcodes.html">All Greater Manchester postcodes</a></div></div></div></section>
{cta(root, f"Start driving in {code}.")}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "serviceType": "Driving lessons", "name": f"Driving lessons in {code}",
               "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE, "telephone": "+44 7352 932003"},
               "areaServed": {"@type": "PostalAddress", "postalCode": code, "addressLocality": d["short"], "addressRegion": "Greater Manchester", "addressCountry": "GB"},
               "offers": [{"@type": "Offer", "name": "2-hour lesson", "price": "70", "priceCurrency": "GBP"}, {"@type": "Offer", "name": "10-hour block", "price": "320" if offer else "350", "priceCurrency": "GBP"}]},
              faq_schema(faqs), crumbs_schema([("Home", ""), ("Postcodes", "postcodes.html"), (code, f"postcodes/{code.lower()}.html")])]
    title = f"Driving Lessons {code} · {d['short']}"
    desc = f"Driving lessons in {code} — {d['name']}. Local road ladder, hotspots, test centre advice and SQ learner data. £70 per 2-hour lesson, 10 hours {'£320' if offer else '£350'}."
    return page(f"postcodes/{code.lower()}.html", f"{title} | SQ Driving School", desc[:300], body, root, active="areas.html", schema=schema)


def glance_card(slug, code, root):
    f, d = FACTS[code], DISTRICTS[code]
    nm = hname(slug)
    return f'''<div class="card localdata"><div class="card__icon">{icon('pin')}</div><h3>{nm} at a glance</h3>
<div class="localdata__score"><span class="localdata__num">{score(code)}</span><span>/10<br><small>SQ Learner Challenge score for {code}</small></span></div>
<table class="summary"><tr><td>Postcode district</td><td><a href="{root}postcodes/{code.lower()}.html">{code}</a></td></tr>
<tr><td>Local hotspot</td><td>{HOODS[slug]['spot'][0]}</td></tr>
<tr><td>Main road to practise</td><td>{HOODS[slug]['roads'][0][0]}</td></tr>
<tr><td>Distance to city centre</td><td>{miles_to_centre(code):.1f} miles</td></tr>
<tr><td>Best time to practise</td><td>{f['best']}</td></tr>
<tr><td>Usual test centre{'s' if len(d['centres']) > 1 else ''}</td><td>{' or '.join(d['centres'])}</td></tr></table>
<p class="note mt-1 mb-0">The score is our instructors' own rating of how demanding the roads are (10 = most demanding). <a href="{root}postcodes/{code.lower()}.html">Full {code} data</a>.</p></div>'''


def plan_html(slug, code):
    hd, d = HOODS[slug], DISTRICTS[code]
    nm = hname(slug)
    r = hd["roads"]
    steps = [("Hours 1–2", hd["first"]),
             ("Hours 3–4", f"Junctions, roundabouts and meeting traffic on local roads, then your first drives on {r[0][0]} ({r[0][1]})."),
             ("Hours 5–6", f"{r[1][0]} ({r[1][1]}), and tackling the local hotspot: {hd['spot'][0]}."),
             ("Hours 7–8", f"{r[2][0]} ({r[2][1]}), plus manoeuvres and your first independent driving with sat-nav."),
             ("Hours 9–10", f"A mock test on roads like those around {' or '.join(d['centres'])} test centre, then we agree what to work on next.")]
    return "<ul class=\"ticks\">" + "".join(f"<li><span><b>{a}:</b> {b}</span></li>" for a, b in steps) + "</ul>"


def hood_page(slug):
    hd = HOODS[slug]
    code = HOOD_DISTRICT[slug]
    d = DISTRICTS[code]
    root = "../"
    offer = code in OFFER
    nm = hname(slug)
    roads = "".join(f'<article class="card" data-reveal="up"><div class="card__icon">{icon("road")}</div><h3>{r}</h3><p class="mb-0"><b>What you&#39;ll practise:</b> {w}.</p></article>' for r, w in hd["roads"])
    pick = "".join(f"<li><span>{p}</span></li>" for p in hd["pickups"])
    sibs = [s for s in d["hoods"] if s != slug and s in HOODS]
    sib_cards = "".join(f'<a class="card" href="{s}.html" data-reveal="up"><h3>{hname(s)}</h3><p class="mb-0">{HOODS[s]["line"]}</p></a>' for s in sibs)
    faqs = hd["faqs"] + _std_faqs(nm, code)
    offer_html = ""
    if offer:
        offer_html = f'<section class="section--tight"><div class="container"><div class="offer zone-dark" data-reveal="zoom"><div class="eyebrow">Special offer in {nm}</div><h2>10 hours for <span class="glow-text">£320</span></h2><div class="offer__codes"><span class="offer__code">{code}</span></div><p>Learners picked up in {code} save £30 on a 10-hour block — no student or NHS ID needed.</p><a class="btn btn--red" href="{root}book.html">Book the offer</a></div></div></section>'
    sp_t, sp_x = hd["spot"]
    body = page_hero(f"{nm} · {code} · {d['borough']}", f"Driving lessons in {nm}.", hd["intro"],
                     [f'<a href="{root}postcodes.html">Postcodes</a>', f'<a href="{root}postcodes/{code.lower()}.html">{code}</a>', nm], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="{root}book.html">{icon("calendar")} Book in 60 seconds</a><a class="btn btn--ghost" data-wa="Hi! I\'d like driving lessons in {nm} ({code})." href="https://wa.me/{WA}">{icon("wa")} WhatsApp</a></div>')
    body += reassure() + offer_html
    body += f"""<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" class="prose"><h2 class="mt-0">Your first lessons in {nm}</h2><p>{hd['first']}</p>
  <h3>How lessons usually go</h3><p>{MORE[slug]}</p>
  <h3>Where we'll pick you up</h3><ul class="ticks">{pick}</ul>
  <div class="callout callout--ok mt-2"><b>Local fact:</b> {hd['fact']}</div></div>
  <div data-reveal="right">{glance_card(slug, code, root)}</div>
</div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Roads you'll master</div><h2 data-split>Roads around {nm}.</h2><p class="lead">Once the basics click, these are the roads we'll use to build your skills.</p></div><div class="grid grid--3" data-stagger=".06">{roads}</div></div></section>
<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" class="card"><div class="card__icon">{icon('target')}</div><h3>Local hotspot: {sp_t}</h3><p class="mb-0">{sp_x}</p></div>
  <div data-reveal="right" class="prose"><h2 class="mt-0">Your 10-hour plan in {nm}</h2>{plan_html(slug, code)}<p>See the full <a href="{root}postcodes/{code.lower()}.html">{code} guide</a> for the step-by-step road ladder we use in this part of {d['borough']}.</p></div>
</div></section>
<section class="section--tight"><div class="container"><div class="callout callout--ok" data-reveal="up"><b>Ways to save in {nm}:</b> {('everyone picked up in ' + code + ' gets 10 hours for £320; ') if offer else ''}students and NHS staff get 10 hours for £320 after an ID check; and you can <a href="{root}free-prize-draw.html">enter our free £35 voucher draw</a> when you book.</div></div></section>
<section class="section section--alt"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">Prices</div><h2 data-split>Prices in {nm}.</h2></div><table class="summary"><tr><td>2-hour lesson</td><td><b>£70</b> (£35/hr)</td></tr><tr><td>Single 1-hour session</td><td><b>£40</b></td></tr><tr><td>10-hour block</td><td><b>{'£320 (' + code + ' offer)' if offer else '£350'}</b></td></tr><tr><td>Students &amp; NHS staff</td><td><b>£320</b> for 10 hours after an ID check</td></tr></table><p class="note mt-1 mb-0">Same price for manual and automatic. <a href="{root}prices.html">See every price and build a package</a>.</p></div></section>
<section class="section"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">{nm} FAQ</div><h2 data-split>Questions from {nm} learners.</h2></div><div class="faq">{_faqs_html(faqs)}</div></div></section>
{('<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Also in ' + code + '</div><h2 data-split>Nearby neighbourhoods.</h2></div><div class="grid grid--3" data-stagger=".05">' + sib_cards + '</div></div></section>') if sib_cards else ''}
<section class="section"><div class="container"><div class="tool neon-border" data-reveal="up" style="max-width:820px;margin:0 auto">{postcode_form(True, "Check your exact postcode")}</div>
<div class="mt-3"><h3>Manual &amp; automatic in {nm}</h3><div class="hero__badges"><a class="chip chip--red" href="{root}automatic-driving-lessons/{slug}.html">Automatic lessons in {nm}</a><a class="chip chip--red" href="{root}manual-driving-lessons/{slug}.html">Manual lessons in {nm}</a><a class="chip" href="{root}postcodes/{code.lower()}.html">All of {code}</a></div></div></div></section>
{cta(root, f"Start driving in {nm}.")}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "serviceType": "Driving lessons", "name": f"Driving lessons in {nm}",
               "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE, "telephone": "+44 7352 932003"},
               "areaServed": {"@type": "Place", "name": f"{nm}, {code}, {d['borough']}"},
               "offers": [{"@type": "Offer", "name": "2-hour lesson", "price": "70", "priceCurrency": "GBP"}, {"@type": "Offer", "name": "10-hour block", "price": "320" if offer else "350", "priceCurrency": "GBP"}]},
              faq_schema(faqs), crumbs_schema([("Home", ""), ("Postcodes", "postcodes.html"), (code, f"postcodes/{code.lower()}.html"), (nm, f"driving-lessons/{slug}.html")])]
    title = f"Driving Lessons {nm} ({code})"
    desc = f"Driving lessons in {nm}, {code}. {hd['line']} Local pick-up points, roads and test advice. £70 per 2-hour lesson, 10 hours {'£320' if offer else '£350'}."
    return page(f"driving-lessons/{slug}.html", f"{title} | Manual & Automatic | SQ Driving School", desc[:300], body, root, active="areas.html", schema=schema)


def all_pages():
    out = {}
    for c in DISTRICTS:
        out[f"postcodes/{c.lower()}.html"] = district_page(c)
    for s in HOODS:
        out[f"driving-lessons/{s}.html"] = hood_page(s)
    return out
