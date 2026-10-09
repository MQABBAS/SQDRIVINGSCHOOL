"""Local SEO pages: neighbourhoods, services, and service x borough."""
import os
import re
from layout import *
from pages_main import postcode_form
from pages_more import BOROUGHS

OFFER = ("M16", "M18", "M19")
BMAP = {b[1]: b for b in BOROUGHS}


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def load_postcodes():
    js = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "js", "sq.js"), encoding="utf-8").read()
    block = js[js.index("var PC = {"):js.index("};", js.index("var PC = {"))]
    names = dict(re.findall(r"(\w+): \"([^\"]+)\"", js[js.index("var B = {"):js.index("};", js.index("var B = {"))]))
    out = []
    for code, bkey, area in re.findall(r"(\w+): \[B\.(\w+), \"([^\"]+)\"\]", block):
        out.append((code, names[bkey], area))
    return out


def neighbourhoods():
    """One entry per neighbourhood name, with all postcodes it appears in."""
    seen = {}
    for code, borough, area in load_postcodes():
        for name in [a.strip() for a in area.split("/")]:
            if name in ("City Centre",) and code != "M1":
                continue
            if name in ("Salford", "Manchester Airport") or re.search(r"\b(North|South|East|West)$", name) or (name.endswith(" Centre") and name != "City Centre"):
                continue
            key = slugify(name)
            if key in seen:
                if code not in seen[key]["codes"]:
                    seen[key]["codes"].append(code)
                continue
            seen[key] = {"slug": key, "name": name, "codes": [code], "borough": borough}
    from pages_postcodes import EXTRA_HOODS
    for name, code, borough in EXTRA_HOODS:
        key = slugify(name)
        if key in seen:
            if code not in seen[key]["codes"]:
                seen[key]["codes"].append(code)
            continue
        seen[key] = {"slug": key, "name": name, "codes": [code], "borough": borough}
    return list(seen.values())


SERVICES = [
    ("automatic-driving-lessons", "Automatic Driving Lessons", "auto",
     "No clutch, no gears — just steering, braking and reading the road. Automatic lessons are easier to pick up, great in stop-start traffic, and the future with electric cars.",
     ["Same price as manual: £70 per 2-hour lesson", "Ideal for nervous learners and busy city roads", "Your licence will cover automatic cars", "Free DriveSQ Student Portal"],
     [("Do automatic lessons cost more?", "No — automatic and manual lessons are the same price with SQ."), ("Can I drive a manual after passing in an automatic?", "No. An automatic licence only covers automatic cars. You'd need to pass a manual test to drive manual cars.")]),
    ("manual-driving-lessons", "Manual Driving Lessons", "gear",
     "Learn clutch control, gear changes and hill starts properly, with patient step-by-step teaching. Pass in a manual and your licence covers both manual and automatic cars.",
     ["£70 per 2-hour lesson (£35/hr)", "Clutch control taught somewhere quiet first", "Licence covers manual and automatic", "Free DriveSQ Student Portal"],
     [("Is manual harder to learn?", "It takes a little longer to master the clutch, but it gives you a licence for both manual and automatic cars."), ("What if I keep stalling?", "Everyone stalls. We practise clutch control on quiet roads until it feels natural.")]),
    ("intensive-driving-courses", "Intensive Driving Courses", "bolt",
     "Need your licence fast? Concentrated lessons over 1 to 4 weeks, planned around your theory pass and your practical test date.",
     ["10, 20, 30 or 40-hour courses", "Lessons at £35/hr, discounted blocks £320", "Manual or automatic", "Course planner on our website"],
     [("How long is an intensive course?", "Usually 1–4 weeks depending on your experience and the hours you need."), ("Do I need my theory test first?", "You must pass your theory test before you can book your practical test, so it's best to have it done.")]),
    ("nervous-driver-lessons", "Lessons for Nervous Drivers", "heart",
     "Feeling anxious about driving is completely normal. We go at your pace, start on quiet roads, explain everything first and never judge.",
     ["Quiet roads first, busier roads only when you're ready", "Breaks whenever you need", "Personal comfort plan and breathing coach", "Progress you can see in the Student Portal"],
     [("What if I panic while driving?", "Your instructor has dual controls and will help you pull over safely to take a breather."), ("Can I tell you about my anxiety first?", "Please do — message us and we'll plan your first lessons around how you feel.")]),
    ("beginner-driving-lessons", "Beginner Driving Lessons", "star",
     "Never driven before? Perfect. Your first lesson starts with your instructor driving you somewhere quiet, then explaining the car before you take the wheel.",
     ["Calm first lesson on empty roads", "2-hour lessons give you time to settle", "Every skill tracked in your portal", "From £35 per hour"],
     [("What happens in my first lesson?", "Licence and eyesight check, a drive to a quiet area, the controls explained, then your first drive. See our first-lesson guide."), ("What do I need to start?", "Your provisional driving licence.")]),
    ("refresher-driving-lessons", "Refresher Driving Lessons", "users",
     "Passed years ago but lost your confidence? Moved to Manchester from somewhere quieter? Refresher lessons get you back on the road comfortably.",
     ["Tailored to the roads you're worried about", "Motorways, city centre or parking — your choice", "£70 per 2-hour lesson", "Single 1-hour session from £40"],
     [("How many refresher lessons will I need?", "Many drivers feel confident again after just a few lessons. We'll agree a plan after your first one."), ("Can you help with motorway driving?", "Yes — motorway refreshers are one of our most popular requests.")]),
    ("motorway-driving-lessons", "Motorway Driving Lessons", "road",
     "Learner drivers can drive on motorways with an approved instructor in a dual-controlled car. Learn joining, lane discipline and leaving safely around the M60, M62, M56 and M61.",
     ["Learners and newly qualified drivers welcome", "Joining, overtaking and lane discipline", "Smart motorway awareness", "£35 per hour"],
     [("Can learners drive on the motorway?", "Yes — with an approved driving instructor in a car fitted with dual controls."), ("Is motorway driving on the test?", "Not on the motorway itself, but fast roads and dual carriageways often are.")]),
    ("mock-driving-tests", "Mock Driving Tests", "target",
     "A full test-style drive marked like the real thing, so test day holds no surprises. Find out exactly where you're losing marks — before it counts.",
     ["Real test format: eyesight, show me / tell me, independent drive, manoeuvre", "Marked like the real test", "Faults logged in your Student Portal", "Charged at our normal lesson rate"],
     [("When should I take a mock test?", "A week or two before your real test, once your portal readiness checklist is nearly complete."), ("Will a mock test help me pass?", "It shows exactly which faults to fix and makes test day feel familiar.")]),
    ("student-driving-lessons", "Student Driving Lessons", "grad",
     "College and university students get 10 hours for £320 instead of £350. Flexible times around lectures, with pick-up from campus or home.",
     ["10-hour block £320 with student ID", "Evening and weekend lessons", "Pick-up from campus or halls", "Free theory mock tests in the portal"],
     [("What counts as proof of being a student?", "A valid student ID card or enrolment letter."), ("Can you pick me up from university?", "Yes, anywhere within Greater Manchester.")]),
    ("nhs-driving-lessons", "NHS Staff Driving Lessons", "heart",
     "Thank you for everything you do. NHS staff get 10 hours of driving lessons for £320 instead of £350, with lessons arranged around shifts.",
     ["10-hour block £320 for NHS staff", "Lessons around shift patterns", "Doctors, nurses, HCAs, porters, admin — all NHS staff", "Manual or automatic"],
     [("What proof do I need?", "An NHS ID badge, NHS email address or a recent payslip."), ("Can lessons fit around night shifts?", "Message us your shift pattern and we'll work around it.")]),
    ("affordable-driving-lessons", "Affordable Driving Lessons", "pound",
     "Clear, honest prices with no hidden fees: £35 an hour in 2-hour lessons, 10-hour blocks for £350, and £320 for NHS staff, students and M16, M18 & M19.",
     ["£70 per 2-hour lesson", "10 hours £350 — or £320 with a discount", "Single 1-hour session £40", "Free Student Portal included"],
     [("Are there any hidden costs?", "No. Lesson prices are on our website. DVSA test fees are paid separately to the DVSA."), ("How can I save money?", "Book 10-hour blocks with a discount, and use the free portal for theory revision.")]),
    ("pass-plus-courses", "Pass Plus Courses", "shield",
     "Just passed? Pass Plus is extra training after your test covering town, all-weather, rural, night, dual carriageway and motorway driving.",
     ["Six modules of post-test training", "Builds real-world confidence", "Ask us about course details and pricing", "Available across Greater Manchester"],
     [("Who is Pass Plus for?", "Newly qualified drivers who want extra training and confidence."), ("How do I book Pass Plus?", "Message us on WhatsApp and we'll explain the course and pricing.")]),
]


LEARN_VARIANTS = [
    "{name} is part of {borough}, so your lessons build up to the roads learners here meet every day: {roads}",
    "Learners in {name} get to know {borough}'s roads step by step. Expect {roads}",
    "Driving around {name} means getting comfortable with {borough} traffic. We'll cover {roads}",
    "From your first lesson in {name}, we plan routes that suit your level. Later lessons include {roads}",
]
START_VARIANTS = [
    "Your first lessons start on quiet residential streets near your pick-up point in {name}. As your confidence grows we'll move on to busier junctions, roundabouts and main roads.",
    "We begin somewhere calm near {name} and only head for busier roads when you're ready. Every new skill is introduced slowly and practised until it clicks.",
    "Early lessons stay on the quieter side of {name}. Once moving off, stopping and turning feel natural, we'll add roundabouts, crossings and faster roads.",
    "There's no rush. We'll pick a peaceful spot close to {name} for your first drives, then build up to the routes you'll use every day.",
]
TIPS = [
    ("🚲", "Cyclists", "Leave at least 1.5 metres when overtaking cyclists at up to 30mph."),
    ("🚌", "Bus lanes", "Check the times on the blue signs — many bus lanes are only active at peak hours."),
    ("🏫", "School streets", "Expect children, parked cars and lollipop crossings around school times."),
    ("🌧️", "Rain", "Double your gap in the wet — Manchester's roads get slippery fast."),
    ("🔄", "Big roundabouts", "Follow the lane markings; they override the general left/right rule."),
    ("🚶", "Turning into side roads", "Give way to pedestrians crossing or waiting to cross the road you're turning into."),
    ("🅿️", "Parked cars", "Look for feet under parked cars and doors opening as you pass."),
    ("🛑", "Box junctions", "Don't enter a yellow box unless your exit is clear."),
    ("🚋", "Trams", "Never stop on tram tracks, and watch for trams on shared roads."),
    ("🌙", "Dark evenings", "Dip your headlights for oncoming traffic and watch for pedestrians in dark clothing."),
    ("🚑", "Emergency vehicles", "Stay calm and only move over when it's safe and legal."),
    ("🧭", "Independent driving", "Practise following sat-nav and road signs — about 20 minutes of the test is independent."),
]
FAQ_Q = [
    ["Do you cover {name}?", "Is {name} in your area?", "Can you pick me up in {name}?"],
    ["How much are driving lessons in {name}?", "What do lessons cost in {name}?", "What are your prices in {name}?"],
    ["Which test centre is nearest to {name}?", "Where will I take my test if I live in {name}?", "What's the closest test centre to {name}?"],
    ["Do you offer automatic lessons in {name}?", "Can I learn in an automatic in {name}?", "Is automatic available in {name}?"],
]

INTRO_VARIANTS = [
    "Looking for driving lessons in {name}? SQ Driving School picks up from homes, colleges and workplaces across {name} ({codes}) in {borough}.",
    "Learn to drive in {name} with SQ Driving School. We cover the whole of {codes}, with door-to-door pick-up anywhere in {name}.",
    "SQ Driving School teaches manual and automatic learners in {name}, {borough}. Lessons start right outside your door in {codes}.",
    "Friendly, patient driving lessons in {name} ({codes}). Whether you're a complete beginner or nearly test-ready, we'll start from where you are.",
]


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]}


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + u} for i, (n, u) in enumerate(items)]}


def prices_block():
    return f"""<div class="grid grid--3" data-stagger=".08">
  <article class="card" data-reveal="up"><div class="card__icon">{icon('clock')}</div><h3>£70 · 2-hour lesson</h3><p class="mb-0">£35 per hour. Our standard lesson. Single 1-hour session £40.</p></article>
  <article class="card" data-reveal="up"><div class="card__icon">{icon('layers')}</div><h3>£350 · 10 hours</h3><p class="mb-0">Block booking for manual or automatic lessons.</p></article>
  <article class="card" data-reveal="up"><div class="card__icon">{icon('heart')}</div><h3>£320 · 10 hours</h3><p class="mb-0">For NHS staff, students, and learners in M16, M18 &amp; M19.</p></article>
</div>"""


def neighbourhood_page(n, all_n):
    root = "../"
    b = BMAP[n["borough"]]
    bslug, bname, bcodes, districts, roads, centres = b
    codes = ", ".join(n["codes"])
    offer = [c for c in n["codes"] if c in OFFER]
    h = sum(map(ord, n["slug"])) + len(n["slug"]) * 7
    v = INTRO_VARIANTS[h % len(INTRO_VARIANTS)].format(name=n["name"], codes=codes, borough=bname)
    learn = LEARN_VARIANTS[(h // 3) % 4].format(name=n["name"], borough=bname, roads=roads[0].lower() + roads[1:])
    start = START_VARIANTS[(h // 5) % 4].format(name=n["name"])
    tips = [TIPS[(h + k * 5) % len(TIPS)] for k in range(4)]
    tips = list(dict.fromkeys(tips))
    tips_html = "".join(f'<article class="card" data-reveal="up"><div style="font-size:1.8rem">{e}</div><h3 class="mt-1" style="font-size:1.1rem">{t}</h3><p class="mb-0">{d}</p></article>' for e, t, d in tips)
    same_pc = [x for x in all_n if x["slug"] != n["slug"] and set(x["codes"]) & set(n["codes"])]
    same_pc_html = (f'<p>{codes} also covers ' + ", ".join(f'<a href="{x["slug"]}.html">{x["name"]}</a>' for x in same_pc) + ' — we teach there too.</p>') if same_pc else ""
    fq = lambda i: FAQ_Q[i][(h + i) % 3].format(name=n["name"])
    sibs = [x for x in all_n if x["borough"] == n["borough"] and x["slug"] != n["slug"]][:12]
    sib_html = "".join(f'<a class="chip" href="{x["slug"]}.html">{x["name"]}</a>' for x in sibs)
    svc_html = "".join(f'<a class="chip" href="{root}services/{s[0]}-{bslug}.html">{s[1]} in {bname}</a>' for s in SERVICES[:8])
    offer_html = ""
    if offer:
        offer_html = f'<section class="section--tight"><div class="container"><div class="offer zone-dark" data-reveal="zoom"><div class="eyebrow">Special offer in {n["name"]}</div><h2>10 hours for <span class="glow-text">£320</span></h2><div class="offer__codes">{"".join(f"<span class={chr(39)}offer__code{chr(39)}>{c}</span>" for c in offer)}</div><p>Learners picked up in {", ".join(offer)} save £30 on a 10-hour block — no NHS or student ID needed.</p><a class="btn btn--red" href="{root}book.html">Book the offer</a></div></div></section>'
    faqs = [(fq(0), f"Yes. SQ Driving School covers all of {codes} in {bname}, with pick-up from your home, college or work."),
            (fq(1), "£70 for a 2-hour lesson (£35/hr), £40 for a single hour, or £350 for 10 hours. NHS staff and students pay £320 for 10 hours." + (f" Learners in {', '.join(offer)} also get 10 hours for £320." if offer else "")),
            (fq(2), f"Learners in {n['name']} usually test at {' or '.join(centres)}. Book your test on GOV.UK and we'll help you choose."),
            (fq(3), f"Yes — manual and automatic lessons in {n['name']} are the same price.")]
    faq_html = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    title = f"Driving Lessons {n['name']} ({n['codes'][0]})"
    prices_sec = f'''<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Prices in {n['name']}</div><h2 data-split>Clear prices for {n['name']} learners.</h2></div>{prices_block()}</div></section>'''
    tips_sec = f'''<section class="section"><div class="container"><div class="section__head"><div class="eyebrow">Local driving tips</div><h2 data-split>Tips for driving around {n['name']}.</h2></div><div class="grid grid--4" data-stagger=".05">{tips_html}</div></div></section>'''
    faq_sec = f'''<section class="section section--alt"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">{n['name']} FAQ</div><h2 data-split>Questions from {n['name']} learners.</h2></div><div class="faq">{faq_html}</div></div></section>'''
    body = page_hero(f"{n['name']} · {codes} · {bname}", f"Driving lessons in {n['name']}.", v, [f'<a href="{root}areas.html">Areas</a>', f'<a href="{root}areas/{bslug}.html">{bname}</a>', n["name"]], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="{root}book.html">{icon("calendar")} Book in 60 seconds</a><a class="btn btn--ghost" data-wa="Hi! I\'d like driving lessons in {n["name"]} ({n["codes"][0]})." href="https://wa.me/{WA}">{icon("wa")} WhatsApp</a></div>')
    body += reassure() + offer_html
    body += f"""<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" class="prose"><h2 class="mt-0">Learning to drive around {n['name']}</h2>
    <p>{learn}</p>
    <p>{start} Before your test we'll practise around {' and '.join(centres)} test centre{'s' if len(centres) > 1 else ''}.</p>
    {same_pc_html}
    <p>Every lesson is logged in the free <a href="{root}student-portal.html">DriveSQ Student Portal</a>, so you can see your progress between lessons.</p></div>
  <div data-reveal="right"><div class="card"><div class="card__icon">{icon('pin')}</div><h3>{n['name']} at a glance</h3>
    <table class="summary"><tr><td>Postcode{'s' if len(n['codes']) > 1 else ''}</td><td>{", ".join(f'<a href="{root}postcodes/{c.lower()}.html">{c}</a>' for c in n["codes"])}</td></tr><tr><td>Borough</td><td>{bname}</td></tr><tr><td>Nearby test centres</td><td>{', '.join(centres)}</td></tr><tr><td>Lessons</td><td>Manual &amp; automatic</td></tr><tr><td>10-hour block</td><td>{'£320 (offer area)' if offer else '£350 · £320 NHS/students'}</td></tr></table>
    <a class="btn btn--red btn--block mt-1" href="{root}book.html">Book in {n['name']}</a></div></div>
</div></section>
{(prices_sec + tips_sec + faq_sec) if h % 2 else (tips_sec + faq_sec + prices_sec)}
<section class="section section--alt"><div class="container"><div class="tool neon-border" data-reveal="up" style="max-width:820px;margin:0 auto">{postcode_form(True, "Check your exact postcode")}</div>
<div class="mt-3"><h3>Manual &amp; automatic in {n['name']}</h3><div class="hero__badges"><a class="chip chip--red" href="{root}automatic-driving-lessons/{n['slug']}.html">Automatic lessons in {n['name']}</a><a class="chip chip--red" href="{root}manual-driving-lessons/{n['slug']}.html">Manual lessons in {n['name']}</a></div></div><div class="mt-3"><h3>Lessons in {bname}</h3><div class="hero__badges">{svc_html}</div></div>
<div class="mt-3"><h3>Nearby areas</h3><div class="hero__badges">{sib_html}<a class="chip" href="{root}areas/{bslug}.html">All of {bname}</a></div></div></div></section>
{cta(root, f"Start driving in {n['name']}.")}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "serviceType": "Driving lessons", "name": f"Driving lessons in {n['name']}",
               "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE, "telephone": "+44 7352 932003"},
               "areaServed": {"@type": "Place", "name": f"{n['name']}, {bname}"},
               "offers": [{"@type": "Offer", "name": "2-hour lesson", "price": "70", "priceCurrency": "GBP"}, {"@type": "Offer", "name": "10-hour block", "price": "320" if offer else "350", "priceCurrency": "GBP"}]},
              faq_schema(faqs), crumbs_schema([("Home", ""), ("Areas", "areas.html"), (bname, f"areas/{bslug}.html"), (n["name"], f"driving-lessons/{n['slug']}.html")])]
    desc = f"Driving lessons in {n['name']} ({codes}), {bname}. Manual & automatic, £70 per 2-hour lesson, 10 hours {'£320' if offer else '£350 (£320 NHS & students)'}. Free DriveSQ Student Portal."
    return page(f"driving-lessons/{n['slug']}.html", f"{title} | Manual & Automatic | SQ Driving School", desc, body, root, active="areas.html", schema=schema)


def service_hub(s, all_n):
    slug, name, ic, intro, bullets, faqs = s
    root = "../"
    bl = "".join(f"<li><span>{x}</span></li>" for x in bullets)
    bor = "".join(f'<a class="card" href="{slug}-{b[0]}.html" data-reveal="up" data-tilt="6"><div class="card__icon">{icon("pin")}</div><h3>{name} in {b[1]}</h3><p class="mb-0">{", ".join(b[3].split(", ")[:4])} and more.</p></a>' for b in BOROUGHS)
    faq_html = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    body = page_hero("Greater Manchester", f"{name}.", intro, [f'<a href="{root}services.html">Services</a>', name], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="{root}book.html">{icon("calendar")} Book in 60 seconds</a><a class="btn btn--ghost" data-wa="Hi! I\'m interested in {name.lower()}." href="https://wa.me/{WA}">{icon("wa")} WhatsApp</a></div>')
    body += reassure()
    if slug in ("automatic-driving-lessons", "manual-driving-lessons"):
        k = slug.split("-")[0]
        body += f'<section class="section--tight"><div class="container"><div class="callout callout--ok" data-reveal="up"><b>Looking for {k} lessons near you?</b> See <a href="{root}{k}-driving-lessons-manchester.html">{k} driving lessons in Manchester</a> — with every area A–Z and a manual-or-automatic quiz.</div></div></section>'
    body += f"""<section class="section"><div class="container split"><div data-reveal="left"><div class="card__icon">{icon(ic)}</div><h2 data-split>What's included.</h2></div><ul class="ticks" data-reveal="right">{bl}</ul></div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Choose your borough</div><h2 data-split>{name} across Greater Manchester.</h2></div><div class="grid grid--3" data-stagger=".04">{bor}</div></div></section>
<section class="section"><div class="container" style="max-width:900px"><div class="faq">{faq_html}</div></div></section>
{cta(root)}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "serviceType": name, "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE}, "areaServed": "Greater Manchester"}, faq_schema(faqs)]
    return page(f"services/{slug}.html", f"{name} Greater Manchester | SQ Driving School", f"{name} across Greater Manchester with SQ Driving School. {intro[:110]}", body, root, active="lessons.html", schema=schema)


def service_borough(s, b, all_n):
    slug, name, ic, intro, bullets, faqs = s
    bslug, bname, bcodes, districts, roads, centres = b
    root = "../"
    hoods = [x for x in all_n if x["borough"] == bname]
    gear = slug if slug in ("automatic-driving-lessons", "manual-driving-lessons") else None
    hl = "".join(f'<a class="chip" href="{root}{gear}/{x["slug"]}.html">{name} {x["name"]}</a>' if gear else f'<a class="chip" href="{root}driving-lessons/{x["slug"]}.html">{x["name"]}</a>' for x in hoods)
    others = "".join(f'<a class="chip" href="{x[0]}-{bslug}.html">{x[1]}</a>' for x in SERVICES if x[0] != slug)
    bl = "".join(f"<li><span>{x}</span></li>" for x in bullets)
    offer = [c for c in bcodes if c in OFFER]
    lf = faqs + [(f"Do you offer {name.lower()} across {bname}?", f"Yes — we pick up across {bname}, including {', '.join(districts.split(', ')[:5])}."),
                 (f"Where do {bname} learners take their test?", f"Usually at {' or '.join(centres)}. See our test centre guide.")]
    faq_html = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in lf)
    body = page_hero(f"{bname} · {name}", f"{name} in {bname}.", intro, [f'<a href="{root}services.html">Services</a>', f'<a href="{slug}.html">{name}</a>', bname], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="{root}book.html">{icon("calendar")} Book in 60 seconds</a><a class="btn btn--ghost" data-wa="Hi! I\'m interested in {name.lower()} in {bname}." href="https://wa.me/{WA}">{icon("wa")} WhatsApp</a></div>')
    body += reassure()
    body += f"""<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" class="prose"><h2 class="mt-0">{name} across {bname}</h2>
  <p>We pick up from {districts}.</p>
  <p>Lessons build up to the roads {bname} learners meet every day: {roads[0].lower() + roads[1:]} Nearby test centres include {' and '.join(centres)}.</p>
  {f'<p><b>Special offer:</b> learners in {", ".join(offer)} get 10 hours for £320.</p>' if offer else ''}</div>
  <div data-reveal="right"><div class="card"><div class="card__icon">{icon(ic)}</div><h3>What's included</h3><ul class="ticks">{bl}</ul></div></div>
</div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Prices</div><h2 data-split>Clear prices in {bname}.</h2></div>{prices_block()}</div></section>
<section class="section"><div class="container" style="max-width:900px"><div class="faq">{faq_html}</div></div></section>
<section class="section section--alt"><div class="container"><h3>Areas in {bname}</h3><div class="hero__badges">{hl}</div><h3 class="mt-3">Other lessons in {bname}</h3><div class="hero__badges">{others}</div></div></section>
{cta(root)}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "serviceType": name, "name": f"{name} in {bname}", "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE, "telephone": "+44 7352 932003"},
               "areaServed": {"@type": "AdministrativeArea", "name": bname}}, faq_schema(lf),
              crumbs_schema([("Home", ""), ("Services", "services.html"), (name, f"services/{slug}.html"), (bname, f"services/{slug}-{bslug}.html")])]
    return page(f"services/{slug}-{bslug}.html", f"{name} {bname} | SQ Driving School", f"{name} in {bname}, Greater Manchester. £35/hr, 2-hour lessons £70, 10 hours £350 (£320 NHS & students). Pick-up across {bname}.", body, root, active="lessons.html", schema=schema)


def services_index():
    root = ""
    cards = "".join(f'<a class="card" href="services/{s[0]}.html" data-reveal="up" data-tilt="6"><div class="card__icon">{icon(s[2])}</div><h3>{s[1]}</h3><p class="mb-0">{s[3][:120]}…</p></a>' for s in SERVICES)
    body = page_hero("Services", "Every kind of lesson.", "Choose a lesson type, then your borough, to see everything we offer near you.", ["Services"], root)
    body += f'<section class="section--tight"><div class="container"><div class="grid grid--3" data-stagger=".04">{cards}</div></div></section>{cta(root)}'
    return page("services.html", "Driving Lesson Services Greater Manchester | SQ Driving School", "All SQ Driving School lesson types across Greater Manchester: automatic, manual, intensive, nervous drivers, refresher, motorway, mock tests and more.", body, root, active="lessons.html")


def areas_index(all_n):
    root = ""
    blocks = ""
    for b in BOROUGHS:
        hoods = [x for x in all_n if x["borough"] == b[1]]
        chips = "".join(f'<a class="chip{" chip--red" if any(c in OFFER for c in x["codes"]) else ""}" href="driving-lessons/{x["slug"]}.html">{x["name"]} <span class="mono" style="font-size:.75rem;opacity:.7">{x["codes"][0]}</span></a>' for x in hoods)
        blocks += f'<div class="card" data-reveal="up" style="margin-bottom:20px"><h3><a href="areas/{b[0]}.html">{b[1]}</a></h3><div class="hero__badges">{chips}</div></div>'
    bor = "".join(f'<a class="card" href="areas/{s}.html" data-reveal="up" data-tilt="8"><div class="card__icon">{icon("pin")}</div><h3>{n}</h3><p class="mb-0">{len([x for x in all_n if x["borough"] == n])} neighbourhoods</p></a>' for s, n, *_ in BOROUGHS)
    body = page_hero("Areas we cover", "All of Greater Manchester.", f"Ten boroughs and {len(all_n)} neighbourhoods. Door-to-door pick-up from home, college, university or work.", ["Areas"], root)
    body += f"""<section class="section--tight"><div class="container"><div class="grid grid--4" data-stagger=".04">{bor}</div></div></section>
<section class="section"><div class="container" style="max-width:820px"><div class="tool neon-border" data-reveal="up">{postcode_form(True, "Check your postcode")}</div></div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Every neighbourhood</div><h2 data-split>Find your area.</h2><p class="lead">Red areas get 10 hours for £320.</p></div>{blocks}</div></section>
{cta(root)}"""
    return page("areas.html", "Driving Lessons Across Greater Manchester | All Areas | SQ Driving School",
                f"SQ Driving School covers all 10 Greater Manchester boroughs and {len(all_n)} neighbourhoods. Find driving lessons near you.", body, root)
