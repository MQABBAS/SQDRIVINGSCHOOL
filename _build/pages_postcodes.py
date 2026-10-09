"""Postcode district pages, extra neighbourhoods, postcode directory and 'near me'."""
from layout import *
from pages_main import postcode_form
from pages_more import BOROUGHS
from pages_seo import TIPS

OFFER = ("M16", "M18", "M19")
BMAP = {b[1]: b for b in BOROUGHS}

# Well-known Greater Manchester places not already listed in the postcode checker.
# (name, main postcode district, borough)
EXTRA_HOODS = [
    # Manchester
    ("Piccadilly", "M1", "Manchester"), ("Castlefield", "M3", "Manchester"), ("Spinningfields", "M3", "Manchester"),
    ("New Islington", "M4", "Manchester"), ("Higher Blackley", "M9", "Manchester"), ("Charlestown", "M9", "Manchester"),
    ("Beswick", "M11", "Manchester"), ("West Gorton", "M12", "Manchester"), ("Chorlton-on-Medlock", "M13", "Manchester"),
    ("Ladybarn", "M14", "Manchester"), ("Belle Vue", "M18", "Manchester"), ("East Didsbury", "M20", "Manchester"),
    ("West Didsbury", "M20", "Manchester"), ("Parrs Wood", "M20", "Manchester"), ("Chorlton", "M21", "Manchester"),
    ("Benchill", "M22", "Manchester"), ("Sharston", "M22", "Manchester"), ("Northern Moor", "M23", "Manchester"),
    ("Miles Platting", "M40", "Manchester"), ("Collyhurst", "M40", "Manchester"),
    # Salford
    ("Clifton", "M27", "Salford"), ("Boothstown", "M28", "Salford"), ("Ellenbrook", "M28", "Salford"),
    ("Monton", "M30", "Salford"), ("Winton", "M30", "Salford"), ("Patricroft", "M30", "Salford"),
    # Trafford
    ("Gorse Hill", "M32", "Trafford"), ("Ashton upon Mersey", "M33", "Trafford"), ("Davyhulme", "M41", "Trafford"),
    ("Bowdon", "WA14", "Trafford"), ("Broadheath", "WA14", "Trafford"), ("Hale Barns", "WA15", "Trafford"),
    # Stockport
    ("Heaton Mersey", "SK4", "Stockport"), ("Heaton Norris", "SK4", "Stockport"), ("Woodley", "SK6", "Stockport"),
    ("High Lane", "SK6", "Stockport"), ("Marple Bridge", "SK6", "Stockport"), ("Compstall", "SK6", "Stockport"),
    ("Cheadle Hulme", "SK8", "Stockport"), ("Heald Green", "SK8", "Stockport"),
    # Tameside
    ("Gee Cross", "SK14", "Tameside"), ("Hattersley", "SK14", "Tameside"), ("Mottram", "SK14", "Tameside"),
    # Oldham
    ("Derker", "OL1", "Oldham"), ("Uppermill", "OL3", "Oldham"), ("Delph", "OL3", "Oldham"), ("Diggle", "OL3", "Oldham"),
    ("Greenfield", "OL3", "Oldham"), ("Moorside", "OL4", "Oldham"),
    # Rochdale
    ("Castleton", "OL11", "Rochdale"), ("Norden", "OL12", "Rochdale"), ("Wardle", "OL12", "Rochdale"),
    ("Smallbridge", "OL16", "Rochdale"), ("Newhey", "OL16", "Rochdale"),
    # Bury
    ("Walshaw", "BL8", "Bury"), ("Unsworth", "BL9", "Bury"), ("Summerseat", "BL9", "Bury"),
    # Bolton
    ("Astley Bridge", "BL1", "Bolton"), ("Halliwell", "BL1", "Bolton"), ("Heaton", "BL1", "Bolton"), ("Smithills", "BL1", "Bolton"),
    ("Breightmet", "BL2", "Bolton"), ("Harwood", "BL2", "Bolton"), ("Tonge Moor", "BL2", "Bolton"),
    ("Deane", "BL3", "Bolton"), ("Great Lever", "BL3", "Bolton"), ("Little Lever", "BL3", "Bolton"), ("Lostock", "BL6", "Bolton"),
    # Wigan
    ("Aspull", "WN2", "Wigan"), ("Abram", "WN2", "Wigan"), ("Platt Bridge", "WN2", "Wigan"), ("Hindley Green", "WN2", "Wigan"),
    ("Appley Bridge", "WN6", "Wigan"), ("Golborne", "WA3", "Wigan"), ("Lowton", "WA3", "Wigan"),
]

AREA_NAMES = {"M": "Manchester", "BL": "Bolton", "OL": "Oldham", "SK": "Stockport", "WA": "Warrington", "WN": "Wigan"}


def _area(code):
    return "".join(ch for ch in code if ch.isalpha())


def _num(code):
    return int("".join(ch for ch in code if ch.isdigit()))


def postcode_list(load_postcodes):
    """[(code, borough, area_label)] including WA3 (Wigan side)."""
    out = [(c, b, a) for c, b, a in load_postcodes() if c != "M90"]
    out.append(("WA3", "Wigan", "Golborne / Lowton"))
    return sorted(out, key=lambda x: (_area(x[0]), _num(x[0])))


def postcode_page(entry, all_codes, hoods):
    code, borough, area_label = entry
    root = "../"
    b = BMAP[borough]
    bslug, bname, bcodes, districts, roads, centres = b
    offer = code in OFFER
    in_code = [h for h in hoods if code in h["codes"]]
    names = [h["name"] for h in in_code] or [x.strip() for x in area_label.split("/")]
    nice = " & ".join(names[:2]) if len(names) <= 2 else ", ".join(names[:2]) + " & more"
    same_area = [c for c in all_codes if _area(c[0]) == _area(code) and c[0] != code]
    nearby = sorted(same_area, key=lambda c: abs(_num(c[0]) - _num(code)))[:6]
    same_b = [c for c in all_codes if c[1] == borough and c[0] != code and c not in nearby][:6]
    near_html = "".join(f'<a class="chip{" chip--red" if c[0] in OFFER else ""}" href="{c[0].lower()}.html">{c[0]} · {c[2].split(" / ")[0]}</a>' for c in nearby + same_b)
    hood_cards = "".join(f'<a class="card" href="{root}driving-lessons/{h["slug"]}.html" data-reveal="up"><div class="card__icon">{icon("pin")}</div><h3>{h["name"]}</h3><p class="mb-0">Driving lessons in {h["name"]}, {code}.</p></a>' for h in in_code)
    svc_html = "".join(f'<a class="chip" href="{root}services/{s}-{bslug}.html">{t}</a>' for s, t in [("automatic-driving-lessons", "Automatic"), ("manual-driving-lessons", "Manual"), ("intensive-driving-courses", "Intensive"), ("nervous-driver-lessons", "Nervous drivers"), ("beginner-driving-lessons", "Beginners"), ("refresher-driving-lessons", "Refresher"), ("mock-driving-tests", "Mock tests"), ("student-driving-lessons", "Students")])
    area_word = AREA_NAMES.get(_area(code), "")
    offer_html = ""
    if offer:
        offer_html = f'<section class="section--tight"><div class="container"><div class="offer zone-dark" data-reveal="zoom"><div class="eyebrow">{code} special offer</div><h2>10 hours for <span class="glow-text">£320</span></h2><div class="offer__codes"><span class="offer__code">{code}</span></div><p>Every learner picked up in {code} saves £30 on a 10-hour block — no ID needed.</p><a class="btn btn--red" href="{root}book.html">Book the offer</a></div></div></section>'
    faqs = [(f"Do you give driving lessons in {code}?", f"Yes. SQ Driving School covers all of {code} ({', '.join(names)}) in {bname}, with door-to-door pick-up."),
            (f"How much are driving lessons in {code}?", "£70 per 2-hour lesson (£35/hr), £40 for a single hour, or 10 hours for " + ("£320 with the " + code + " offer." if offer else "£350 — £320 for NHS staff and students.")),
            (f"Which test centre is closest to {code}?", f"Learners in {code} usually test at {' or '.join(centres)}."),
            (f"Do you teach automatic in {code}?", "Yes — manual and automatic, same price.")]
    faq_html = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    faq_sec = f'<section class="section"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">{code} FAQ</div><h2 data-split>Questions about lessons in {code}.</h2></div><div class="faq">{faq_html}</div></div></section>'
    h = sum(map(ord, code)) * 7 + _num(code) * 13
    INTROS = [f"The {code} district covers {', '.join(names)} in {bname}. We pick up from homes, schools, colleges and workplaces right across the district.",
              f"Live, work or study in {code}? Your SQ instructor can collect you anywhere in {', '.join(names)} — and drop you back afterwards.",
              f"{code} is one of {len([c for c in all_codes if c[1] == borough])} postcode districts we cover in {bname}, taking in {', '.join(names)}.",
              f"From {names[0]} to the edges of the district, SQ Driving School teaches manual and automatic learners all over {code}."]
    LEARN = [f"Lessons start on quieter local streets and build up to the roads {bname} learners meet every day — {roads[0].lower() + roads[1:]}",
             f"We'll begin away from the busiest roads in {code}, then step up to {bname}'s main routes: {roads[0].lower() + roads[1:]}",
             f"Expect a gradual build-up: calm streets near home first, then the roads that matter for {bname} drivers — {roads[0].lower() + roads[1:]}",
             f"Every route is planned around your level. Later lessons cover {roads[0].lower() + roads[1:]}"]
    intro_p, learn_p = INTROS[h % 4], LEARN[(h // 4) % 4]
    tips = list(dict.fromkeys(TIPS[(h + k * 7) % len(TIPS)] for k in range(4)))
    tips_sec = '<section class="section"><div class="container"><div class="section__head"><div class="eyebrow">Local tips</div><h2 data-split>Driving tips for ' + code + ' learners.</h2></div><div class="grid grid--4" data-stagger=".05">' + "".join(f'<article class="card" data-reveal="up"><div style="font-size:1.8rem">{e}</div><h3 class="mt-1" style="font-size:1.1rem">{t}</h3><p class="mb-0">{d}</p></article>' for e, t, d in tips) + '</div></div></section>'
    title = f"Driving Lessons {code} · {nice}"
    body = page_hero(f"{code} postcode district · {bname}", f"Driving lessons in {code}.", f"Manual and automatic lessons across the {code} postcode district — {', '.join(names)}. Door-to-door pick-up anywhere in {code}.",
                     [f'<a href="{root}postcodes.html">Postcodes</a>', code], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="{root}book.html">{icon("calendar")} Book in 60 seconds</a><a class="btn btn--ghost" data-wa="Hi! I\'d like driving lessons in {code}." href="https://wa.me/{WA}">{icon("wa")} WhatsApp</a></div>')
    body += reassure() + offer_html
    body += f"""<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left"><div class="card"><div class="card__icon">{icon('pin')}</div><h3>{code} at a glance</h3>
  <table class="summary"><tr><td>Postcode district</td><td>{code}</td></tr><tr><td>Postcode area</td><td>{_area(code)} ({area_word})</td></tr><tr><td>Local authority</td><td>{bname}</td></tr>
  <tr><td>Areas covered</td><td>{', '.join(names)}</td></tr><tr><td>Nearby test centres</td><td>{', '.join(centres)}</td></tr><tr><td>2-hour lesson</td><td>£70</td></tr><tr><td>10 hours</td><td>{'£320 (' + code + ' offer)' if offer else '£350 · £320 NHS/students'}</td></tr></table></div></div>
  <div data-reveal="right" class="prose"><h2 class="mt-0">Learning to drive in {code}</h2>
  <p>{intro_p}</p>
  <p>{learn_p}</p>
  <p>Most learners from {code} take their practical test at {' or '.join(centres)}. Read our <a href="{root}knowledge/greater-manchester-driving-test-centres.html">test centre guides</a>.</p></div>
</div></section>
{('<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Neighbourhoods in ' + code + '</div><h2 data-split>Lessons in every part of ' + code + '.</h2></div><div class="grid grid--3" data-stagger=".05">' + hood_cards + '</div></div></section>') if hood_cards else ''}
{(tips_sec + faq_sec) if h % 2 else (faq_sec + tips_sec)}
<section class="section section--alt"><div class="container"><div class="tool neon-border" data-reveal="up" style="max-width:820px;margin:0 auto">{postcode_form(True, "Check your full postcode")}</div>
<div class="mt-3"><h3>Lessons in {bname}</h3><div class="hero__badges">{svc_html}<a class="chip" href="{root}areas/{bslug}.html">All of {bname}</a></div></div>
<div class="mt-3"><h3>Nearby postcodes</h3><div class="hero__badges">{near_html}<a class="chip" href="{root}postcodes.html">All Greater Manchester postcodes</a></div></div></div></section>
{cta(root, f"Start driving in {code}.")}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "serviceType": "Driving lessons", "name": f"Driving lessons in {code}",
               "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE, "telephone": "+44 7352 932003"},
               "areaServed": {"@type": "PostalAddress", "postalCode": code, "addressRegion": "Greater Manchester", "addressCountry": "GB"},
               "offers": [{"@type": "Offer", "name": "2-hour lesson", "price": "70", "priceCurrency": "GBP"}, {"@type": "Offer", "name": "10-hour block", "price": "320" if offer else "350", "priceCurrency": "GBP"}]},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Postcodes", "item": SITE + "/postcodes.html"}, {"@type": "ListItem", "position": 3, "name": code, "item": f"{SITE}/postcodes/{code.lower()}.html"}]}]
    desc = f"Driving lessons in {code} ({', '.join(names[:4])}), {bname}. Manual & automatic, £70 per 2-hour lesson, 10 hours {'£320' if offer else '£350 (£320 NHS & students)'}. Door-to-door pick-up."
    return page(f"postcodes/{code.lower()}.html", f"{title} | SQ Driving School", desc, body, root, active="areas.html", schema=schema)


def postcode_index(all_codes, hoods):
    root = ""
    blocks = ""
    for letter in ["M", "BL", "OL", "SK", "WA", "WN"]:
        codes = [c for c in all_codes if _area(c[0]) == letter]
        if not codes:
            continue
        rows = "".join(f'<tr><td><a href="postcodes/{c[0].lower()}.html"><b>{c[0]}</b></a>{" <span class=" + chr(39) + "tag" + chr(39) + ">£320 offer</span>" if c[0] in OFFER else ""}</td><td>{c[2].replace(" / ", ", ")}</td><td><a href="areas/{BMAP[c[1]][0]}.html">{c[1]}</a></td></tr>' for c in codes)
        blocks += f'<h2 class="mt-3" data-reveal="up" style="font-size:1.6rem">{letter} — {AREA_NAMES[letter]} postcode area</h2><div class="table-wrap" data-reveal="up"><table class="table"><thead><tr><th>District</th><th>Areas</th><th>Borough</th></tr></thead><tbody>{rows}</tbody></table></div>'
    body = page_hero("Postcode directory", "Every Greater Manchester postcode.", f"SQ Driving School covers {len(all_codes)} postcode districts across Greater Manchester. Find yours for local prices, test centres and neighbourhoods.", ["Postcodes"], root)
    body += f"""<section class="section--tight"><div class="container" style="max-width:820px"><div class="tool neon-border" data-reveal="up">{postcode_form(True, "Search your postcode")}</div></div></section>
<section class="section--tight"><div class="container">{blocks}<p class="note mt-2">Some districts (such as WA3, WN8 and SK12) cross the Greater Manchester boundary — check your full postcode above.</p></div></section>
{cta(root)}"""
    return page("postcodes.html", "Greater Manchester Postcodes | Driving Lessons by Postcode | SQ Driving School",
                f"Driving lessons in every Greater Manchester postcode district: M, BL, OL, SK, WA and WN. {len(all_codes)} districts covered by SQ Driving School.", body, root, active="areas.html")


def near_me_page(all_codes, hoods):
    root = ""
    bor = "".join(f'<a class="card" href="areas/{b[0]}.html" data-reveal="up" data-tilt="6"><div class="card__icon">{icon("pin")}</div><h3>{b[1]}</h3><p class="mb-0">{", ".join(b[3].split(", ")[:5])}…</p></a>' for b in BOROUGHS)
    popular = ["levenshulme", "didsbury", "chorlton-cum-hardy", "fallowfield", "old-trafford", "gorton", "sale", "stretford", "eccles", "prestwich", "cheadle-hulme", "bramhall", "ashton-under-lyne", "hyde", "royton", "middleton", "heywood", "farnworth", "leigh", "altrincham"]
    by = {h["slug"]: h for h in hoods}
    pop = "".join(f'<a class="chip" href="driving-lessons/{s}.html">{by[s]["name"]}</a>' for s in popular if s in by)
    faqs = [("Do you offer driving lessons near me?", "If you're anywhere in Greater Manchester, yes. Enter your postcode above to check instantly."),
            ("How much are driving lessons near me?", "£70 per 2-hour lesson, £40 for a single hour, £350 for 10 hours — or £320 for NHS staff, students and M16, M18 & M19."),
            ("Do you pick up from home?", "Yes — door-to-door pick-up from home, school, college, university or work.")]
    fq = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    body = page_hero("Near me", "Driving lessons near you.", f"We cover all 10 Greater Manchester boroughs, {len(all_codes)} postcode districts and over {len(hoods)} neighbourhoods. Enter your postcode to see local prices and offers.", ["Near me"], root)
    body += f"""<section class="section--tight"><div class="container" style="max-width:820px"><div class="tool neon-border" data-reveal="zoom">{postcode_form(True, "Your postcode")}</div></div></section>
<section class="section"><div class="container"><div class="section__head"><div class="eyebrow">Popular areas</div><h2 data-split>Where our learners are.</h2></div><div class="hero__badges">{pop}<a class="chip" href="areas.html">All areas</a><a class="chip" href="postcodes.html">All postcodes</a></div></div></section>
<section class="section section--alt"><div class="container"><div class="grid grid--3" data-stagger=".04">{bor}</div></div></section>
<section class="section"><div class="container" style="max-width:900px"><div class="faq">{fq}</div></div></section>
{cta(root)}"""
    sch = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}]
    return page("driving-lessons-near-me.html", "Driving Lessons Near Me | Greater Manchester | SQ Driving School",
                "Find driving lessons near you anywhere in Greater Manchester. Check your postcode for local prices, offers and test centres. Manual & automatic from £35/hr.", body, root, active="areas.html", schema=sch)
