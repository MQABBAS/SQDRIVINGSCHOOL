"""Automatic and manual driving lesson pages: Manchester pillars + one per neighbourhood."""
from layout import *
from pages_main import postcode_form
from pages_more import BOROUGHS
from pages_seo import TIPS

OFFER = ("M16", "M18", "M19")
BMAP = {b[1]: b for b in BOROUGHS}
CITY = {"Manchester", "Salford", "Trafford"}
HILLY = {"Oldham", "Tameside", "Rochdale", "Bolton", "Stockport", "Bury"}

AUTO_COMMON = ["Fewer controls, so many learners progress faster early on.", "No stalling — ever.", "All electric cars are automatic, so you're ready for the future.", "Great for nervous learners: more brainpower for the road.", "Same price as manual with SQ.", "Smooth, relaxed driving in heavy traffic."]
AUTO_WHY = {
    "city": ["Stop-start traffic is far less tiring with no clutch to hold.", "More attention for trams, bus lanes, cyclists and pedestrians.", "Smooth, quiet progress through busy junctions and queues."],
    "hilly": ["No clutch hill starts — the car holds itself on slopes.", "Steep, stop-start town-centre roads feel much easier.", "Fewer controls to juggle while you learn to read the road."],
    "mixed": ["Comfortable on faster roads and in town alike.", "Ideal if you plan to drive a hybrid or electric car.", "Simple to pick up on quieter suburban streets."],
}
MANUAL_COMMON = ["One licence covers manual and automatic cars.", "Practise in most family cars, which are often manual.", "Hire cars and vans abroad are commonly manual.", "Clutch control gives precise slow-speed control.", "Same price as automatic with SQ.", "A wider choice of cheaper second-hand cars."]
MANUAL_WHY = {
    "city": ["Clutch control makes slow city queues and parking precise.", "Pass in a manual and you can drive manual and automatic cars.", "More choice of cars to buy, borrow or hire."],
    "hilly": ["Master hill starts on the slopes you'll drive every day.", "Gear control is useful on steep and rural roads.", "A manual licence covers both manual and automatic cars."],
    "mixed": ["Full control on country roads and faster routes.", "Often cheaper second-hand cars and family cars to practise in.", "One licence for manual and automatic cars."],
}
HEAD_WHY = ["Why learn {kind} in {name}?", "Is {kind} right for you in {name}?", "{K} lessons in {name}: the benefits", "Why {name} learners choose {kind}"]
HEAD_SKILLS = ["{K} skills, step by step.", "What your {kind} lessons cover.", "Your {kind} learning plan.", "From first drive to test-ready."]


def _trait(borough):
    return "city" if borough in CITY else "hilly" if borough in HILLY else "mixed"


def _variant(seed, items):
    return items[sum(map(ord, seed)) % len(items)]


def gearbox_area_page(kind, n, all_n):
    auto = kind == "automatic"
    K = "Automatic" if auto else "Manual"
    other = "manual" if auto else "automatic"
    root = "../"
    b = BMAP[n["borough"]]
    bslug, bname, bcodes, districts, roads, centres = b
    trait = _trait(bname)
    codes = ", ".join(n["codes"])
    offer = [c for c in n["codes"] if c in OFFER]
    seed = n["slug"] + kind
    hh = sum(map(ord, seed)) * 31 + len(seed)
    pool = (AUTO_COMMON if auto else MANUAL_COMMON)
    why = [(AUTO_WHY if auto else MANUAL_WHY)[trait][hh % 3]] + [pool[(hh // 3 + k * 2) % len(pool)] for k in range(3)]
    why = list(dict.fromkeys(why))
    h_why = HEAD_WHY[hh % 4].format(kind=kind, K=K, name=n["name"])
    h_sk = HEAD_SKILLS[(hh // 5) % 4].format(kind=kind, K=K)
    intro = _variant(seed, [
        f"{K} driving lessons in {n['name']} ({codes}) with door-to-door pick-up anywhere in {n['name']}. £70 for a 2-hour lesson — the same price for manual and automatic.",
        f"Learn to drive an {kind} car in {n['name']}, {bname}. Friendly, patient instructors, 2-hour lessons and a free DriveSQ Student Portal.",
        f"Looking for {kind} lessons in {n['name']}? SQ Driving School covers all of {codes}, from complete beginners to nearly test-ready learners.",
    ]) if auto else _variant(seed, [
        f"Manual driving lessons in {n['name']} ({codes}). Master the clutch with a patient instructor — £70 for a 2-hour lesson.",
        f"Learn to drive a manual car in {n['name']}, {bname}, and pass with a licence that covers both manual and automatic cars.",
        f"Looking for manual lessons in {n['name']}? We cover all of {codes} with door-to-door pick-up and 2-hour lessons.",
    ])
    if auto:
        skills = ["Using drive, reverse, neutral and park", "Creep control for slow manoeuvres", "Smooth braking and acceleration", "Hill hold and parking brake", "Manoeuvres using creep", "Independent driving with sat-nav"]
        local = {"city": f"Around {n['name']} you'll meet {roads[0].lower() + roads[1:]} An automatic lets you focus on all of that instead of the clutch.",
                 "hilly": f"{bname} is known for its hills. In {n['name']} an automatic takes the stress out of starting on slopes, so you can concentrate on {roads[0].lower() + roads[1:]}",
                 "mixed": f"{n['name']} learners drive a mix of town streets and faster roads — {roads[0].lower() + roads[1:]} An automatic keeps things simple while you learn to read them."}[trait]
    else:
        skills = ["Finding the biting point", "Moving off smoothly without stalling", "Choosing the right gear", "Hill starts", "Clutch control in queues and manoeuvres", "Independent driving with sat-nav"]
        local = {"city": f"In {n['name']}, slow city traffic is the perfect place to perfect clutch control. Later lessons cover {roads[0].lower() + roads[1:]}",
                 "hilly": f"{bname}'s hills make {n['name']} a great place to master hill starts properly — a skill that makes you a confident driver anywhere. Expect {roads[0].lower() + roads[1:]}",
                 "mixed": f"{n['name']} gives a good mix of quiet streets to learn the clutch and faster roads to practise gear changes — {roads[0].lower() + roads[1:]}"}[trait]
    tip = TIPS[hh % len(TIPS)]
    tip2 = TIPS[(hh // 7 + 3) % len(TIPS)]
    r = hh % len(skills)
    skills = skills[r:] + skills[:r] if hh % 2 else skills
    sk = "".join(f"<li><span>{s}</span></li>" for s in skills)
    wy = "".join(f"<li><span>{w}</span></li>" for w in why)
    sibs = [x for x in all_n if x["borough"] == bname and x["slug"] != n["slug"]][:14]
    sib_html = "".join(f'<a class="chip" href="{x["slug"]}.html">{K} lessons {x["name"]}</a>' for x in sibs)
    offer_line = f" Learners in {', '.join(offer)} pay just £320 for 10 hours." if offer else ""
    faqs = [(f"How much are {kind} driving lessons in {n['name']}?", f"£70 for a 2-hour lesson (£35/hr), £40 for a single hour, or £350 for 10 hours — £320 for NHS staff and students.{offer_line}"),
            (f"Do {kind} lessons cost more than {other}?", "No. SQ Driving School charges the same for manual and automatic lessons."),
            ((f"Can I drive a manual car if I pass in an automatic?", "No — an automatic licence only covers automatic cars. You'd need to pass a manual test to drive manual cars.") if auto else
             (f"Can I drive an automatic if I pass in a manual?", "Yes — a manual licence covers both manual and automatic cars.")),
            (f"Where will I take my {kind} test from {n['name']}?", f"Most {n['name']} learners test at {' or '.join(centres)}. We'll take you in an SQ {kind} car with a warm-up lesson first.")]
    faq_html = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    title = f"{K} Driving Lessons {n['name']} ({n['codes'][0]})"
    body = page_hero(f"{K} · {n['name']} · {codes}", f"{K} driving lessons in {n['name']}.", intro,
                     [f'<a href="{root}{kind}-driving-lessons-manchester.html">{K} lessons</a>', f'<a href="{root}services/{kind}-driving-lessons-{bslug}.html">{bname}</a>', n["name"]], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="{root}book.html">{icon("calendar")} Book {kind} lessons</a><a class="btn btn--ghost" data-wa="Hi! I\'d like {kind} driving lessons in {n["name"]} ({n["codes"][0]})." href="https://wa.me/{WA}">{icon("wa")} WhatsApp</a></div>')
    body += reassure()
    body += f"""<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" class="prose"><h2 class="mt-0">{h_why}</h2><ul class="ticks">{wy}</ul><p>{local}</p></div>
  <div data-reveal="right"><div class="card"><div class="card__icon">{icon('auto' if auto else 'gear')}</div><h3>{K} lessons in {n['name']}</h3>
  <table class="summary"><tr><td>Gearbox</td><td>{K}</td></tr><tr><td>Postcode</td><td>{", ".join(f'<a href="{root}postcodes/{c.lower()}.html">{c}</a>' for c in n["codes"])}</td></tr><tr><td>2-hour lesson</td><td>£70</td></tr><tr><td>10 hours</td><td>{'£320 (offer area)' if offer else '£350 · £320 NHS/students'}</td></tr><tr><td>Licence covers</td><td>{'Automatic only' if auto else 'Manual &amp; automatic'}</td></tr><tr><td>Test centres</td><td>{', '.join(centres)}</td></tr></table>
  <a class="btn btn--red btn--block mt-1" href="{root}book.html">Book in 60 seconds</a></div></div>
</div></section>
<section class="section section--alt"><div class="container split">
  <div data-reveal="left"><div class="eyebrow">What you'll learn</div><h2 data-split>{h_sk}</h2><p class="lead">Every skill is rated after each lesson in your free DriveSQ Student Portal.</p>
  <div class="callout mt-2"><b>{tip[0]} Local tip — {tip[1]}:</b> {tip[2]}</div>{f'<div class="callout callout--info"><b>{tip2[0]} {tip2[1]}:</b> {tip2[2]}</div>' if tip2 != tip else ''}</div>
  <ul class="ticks" data-reveal="right">{sk}</ul>
</div></section>
<section class="section"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">{K} lessons FAQ</div><h2 data-split>Questions from {n['name']} learners.</h2></div><div class="faq">{faq_html}</div>
<p class="mt-2">Not sure which to choose? Take our <a class="red" href="{root}automatic-driving-lessons-manchester.html#quiz">manual or automatic quiz</a>, or see <a class="red" href="{root}{other}-driving-lessons/{n['slug']}.html">{other} lessons in {n['name']}</a>.</p></div></section>
<section class="section section--alt"><div class="container">
<div class="tool neon-border" data-reveal="up" style="max-width:820px;margin:0 auto">{postcode_form(True, "Check your full postcode")}</div>
<div class="mt-3"><h3>{K} lessons near {n['name']}</h3><div class="hero__badges">{sib_html}<a class="chip" href="{root}services/{kind}-driving-lessons-{bslug}.html">{K} lessons across {bname}</a></div></div>
<div class="mt-3"><h3>More in {n['name']}</h3><div class="hero__badges"><a class="chip" href="{root}driving-lessons/{n['slug']}.html">All driving lessons in {n['name']}</a><a class="chip" href="{root}{other}-driving-lessons/{n['slug']}.html">{other.capitalize()} lessons in {n['name']}</a><a class="chip" href="{root}services/intensive-driving-courses-{bslug}.html">Intensive courses in {bname}</a></div></div>
</div></section>
{cta(root, f"Start {kind} lessons in {n['name']}.")}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "serviceType": f"{K} driving lessons", "name": f"{K} driving lessons in {n['name']}",
               "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE, "telephone": "+44 7352 932003"},
               "areaServed": {"@type": "Place", "name": f"{n['name']}, {bname}"},
               "offers": [{"@type": "Offer", "name": f"2-hour {kind} lesson", "price": "70", "priceCurrency": "GBP"}, {"@type": "Offer", "name": f"10-hour {kind} block", "price": "320" if offer else "350", "priceCurrency": "GBP"}]},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": f"{K} lessons", "item": f"{SITE}/{kind}-driving-lessons-manchester.html"}, {"@type": "ListItem", "position": 3, "name": n["name"], "item": f"{SITE}/{kind}-driving-lessons/{n['slug']}.html"}]}]
    desc = f"{K} driving lessons in {n['name']} ({codes}), {bname}. £70 per 2-hour lesson, same price as {other}. 10 hours {'£320' if offer else '£350 (£320 NHS & students)'}. Door-to-door pick-up."
    return page(f"{kind}-driving-lessons/{n['slug']}.html", f"{title} | SQ Driving School", desc, body, root, active="lessons.html", schema=schema)


QUIZ = [
    ("Will you mainly drive a family or friend's car that's manual?", [("Yes", 2), ("No / not sure", -1)]),
    ("Are you likely to drive an electric or hybrid car?", [("Yes", -2), ("Not sure", 0), ("No", 1)]),
    ("How do you feel about learning to drive?", [("Very nervous", -2), ("A bit nervous", -1), ("Confident", 1)]),
    ("Might you need to hire vans or cars abroad?", [("Yes", 2), ("No", 0)]),
    ("Do you want the simplest, quickest route to a licence?", [("Yes", -2), ("I want the full licence", 2)]),
]


def pillar(kind, hoods):
    auto = kind == "automatic"
    K = "Automatic" if auto else "Manual"
    other = "manual" if auto else "automatic"
    root = ""
    bor = "".join(f'<a class="card" href="services/{kind}-driving-lessons-{b[0]}.html" data-reveal="up" data-tilt="6"><div class="card__icon">{icon("pin")}</div><h3>{K} lessons in {b[1]}</h3><p class="mb-0">{", ".join(b[3].split(", ")[:4])} and more.</p></a>' for b in BOROUGHS)
    az = ""
    for b in BOROUGHS:
        hs = sorted([h for h in hoods if h["borough"] == b[1]], key=lambda h: h["name"])
        az += f'<div class="card" data-reveal="up" style="margin-bottom:18px"><h3>{K} lessons in {b[1]}</h3><div class="hero__badges">' + "".join(f'<a class="chip" href="{kind}-driving-lessons/{h["slug"]}.html">{h["name"]}</a>' for h in hs) + '</div></div>'
    qz = ""
    for i, (q, opts) in enumerate(QUIZ):
        o = "".join(f'<input type="radio" name="g{i}" id="g{i}{j}" value="{v}"><label for="g{i}{j}">{t}</label>' for j, (t, v) in enumerate(opts))
        qz += f'<div class="field"><span class="label">{i + 1}. {q}</span><div class="seg">{o}</div></div>'
    if auto:
        body_html = """<h2>Why automatic is booming in Greater Manchester</h2>
<p>More learners than ever are choosing automatic. With no clutch and no gear changes, you can put all your attention on the road — which matters in a region of busy junctions, trams, bus lanes and steep hills. Electric and hybrid cars are automatic too, and they're becoming more common every year.</p>
<h2>Automatic vs manual: the honest comparison</h2>
<table><tr><th></th><th>Automatic</th><th>Manual</th></tr>
<tr><td>Price with SQ</td><td>£70 / 2 hours</td><td>£70 / 2 hours</td></tr>
<tr><td>Licence covers</td><td>Automatic cars only</td><td>Manual and automatic</td></tr>
<tr><td>Learning curve</td><td>Fewer controls — many learners progress faster</td><td>Clutch and gears to master</td></tr>
<tr><td>Hills &amp; queues</td><td>Easy — no stalling</td><td>Needs clutch control</td></tr>
<tr><td>Electric cars</td><td>Yes — all EVs are automatic</td><td>—</td></tr></table>
<h2>What automatic lessons include</h2>
<p>You'll learn drive, reverse, neutral and park, creep control for slow manoeuvres, smooth braking, hill hold, all the test manoeuvres and independent driving. Every skill is tracked in your free DriveSQ Student Portal.</p>
<h2>Taking your test in an automatic</h2>
<p>You take your test in an SQ automatic car at a Greater Manchester centre, with a warm-up lesson first. Pass, and your licence covers automatic cars. You can upgrade later by passing a manual test.</p>"""
    else:
        body_html = """<h2>Why many learners still choose manual</h2>
<p>A manual licence is the most flexible licence you can get: pass in a manual and you can drive both manual and automatic cars. It's useful if your family car is manual, if you'll hire cars or vans, or if you simply want full control of the car.</p>
<h2>Manual vs automatic: the honest comparison</h2>
<table><tr><th></th><th>Manual</th><th>Automatic</th></tr>
<tr><td>Price with SQ</td><td>£70 / 2 hours</td><td>£70 / 2 hours</td></tr>
<tr><td>Licence covers</td><td>Manual and automatic</td><td>Automatic cars only</td></tr>
<tr><td>Learning curve</td><td>Clutch and gears to master</td><td>Fewer controls</td></tr>
<tr><td>Car choice</td><td>Any car</td><td>Automatic cars only</td></tr>
<tr><td>Hills</td><td>Hill starts to learn — great on Greater Manchester's hills</td><td>Hill hold does it for you</td></tr></table>
<h2>What manual lessons include</h2>
<p>Finding the biting point, moving off without stalling, choosing gears, hill starts, clutch control in queues and manoeuvres, and independent driving. Stalling is normal — we practise somewhere quiet until it clicks.</p>
<h2>Taking your test in a manual</h2>
<p>You take your test in an SQ manual car at a Greater Manchester centre, with a warm-up lesson first. Pass, and you're licensed for manual and automatic cars.</p>"""
    faqs = [(f"How much are {kind} driving lessons in Manchester?", "£70 for a 2-hour lesson (£35/hr), £40 for a single hour, or £350 for 10 hours — £320 for NHS staff, students and learners in M16, M18 and M19."),
            (f"Do you offer {kind} lessons across Greater Manchester?", f"Yes — all 10 boroughs and {len(hoods)} neighbourhoods. Find yours below."),
            ("Is automatic or manual cheaper?", "Neither with SQ — they're the same price."),
            ("Should I learn manual or automatic?", "It depends on the cars you'll drive and how you feel about learning. Take the quiz on this page for a personal recommendation.")]
    faq_html = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    body = page_hero(f"{K} driving lessons · Greater Manchester", f"{K} driving lessons in Manchester.",
                     (f"Learn in a modern automatic with patient, friendly instructors across Manchester and all of Greater Manchester. £70 for 2 hours — the same price as manual." if auto else
                      f"Learn to drive a manual car with patient, friendly instructors across Manchester and all of Greater Manchester. One licence for manual and automatic. £70 for 2 hours."),
                     [f"{K} lessons"], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="book.html">{icon("calendar")} Book {kind} lessons</a><a class="btn btn--ghost" href="#quiz">Manual or automatic? Take the quiz</a></div>')
    body += reassure()
    body += f"""<section class="section"><div class="container article-grid"><article class="prose">{body_html}</article>
<aside><div class="card"><div class="card__icon">{icon('auto' if auto else 'gear')}</div><h3>{K} lessons</h3><table class="summary"><tr><td>2-hour lesson</td><td>£70</td></tr><tr><td>Single hour</td><td>£40</td></tr><tr><td>10 hours</td><td>£350</td></tr><tr><td>NHS / students / M16·M18·M19</td><td>£320</td></tr></table><a class="btn btn--red btn--block" href="book.html">Book now</a><a class="btn btn--ghost btn--block mt-1" href="{other}-driving-lessons-manchester.html">{other.capitalize()} lessons instead</a></div></aside></div></section>
<section class="section section--alt" id="quiz"><div class="container" style="max-width:900px"><div class="tool neon-border" data-tool="gearbox" data-reveal="up">
<div class="tool__head"><div class="card__icon">{icon('gear')}</div><div><h3>Manual or automatic? 5-question quiz</h3><p class="mb-0 note">Get a personal recommendation in 30 seconds.</p></div></div>
<form>{qz}<button class="btn btn--red btn--block" type="submit">Show my recommendation</button><div class="result" role="status" aria-live="polite"></div></form></div></div></section>
<section class="section"><div class="container"><div class="section__head"><div class="eyebrow">By borough</div><h2 data-split>{K} lessons across Greater Manchester.</h2></div><div class="grid grid--3" data-stagger=".04">{bor}</div></div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">A–Z of areas</div><h2 data-split>Find {kind} lessons near you.</h2></div>{az}</div></section>
<section class="section"><div class="container" style="max-width:900px"><div class="faq">{faq_html}</div></div></section>
{cta(root, f"Start {kind} lessons this week.")}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "serviceType": f"{K} driving lessons", "name": f"{K} driving lessons in Manchester",
               "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE, "telephone": "+44 7352 932003"},
               "areaServed": [{"@type": "AdministrativeArea", "name": "Greater Manchester"}] + [{"@type": "AdministrativeArea", "name": b[1]} for b in BOROUGHS],
               "offers": {"@type": "Offer", "price": "70", "priceCurrency": "GBP", "description": f"2-hour {kind} lesson"}},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}]
    return page(f"{kind}-driving-lessons-manchester.html", f"{K} Driving Lessons Manchester | £35/hr | SQ Driving School",
                f"{K} driving lessons in Manchester and across Greater Manchester. £70 per 2-hour lesson, same price as {other}. {len(hoods)} areas covered. Take the manual or automatic quiz.", body, root, active="lessons.html", schema=schema)
