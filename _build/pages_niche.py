"""Niche audience pages: NHS hospitals and universities/colleges across Greater Manchester.

SQ Driving School is not affiliated with any of these organisations — every page says so.
"""
import re
from layout import *
from pages_main import postcode_form
from pages_more import BOROUGHS

BMAP = {b[1]: b for b in BOROUGHS}

# (name, short name, borough, area, postcode district)
HOSPITALS = [
    ("Manchester Royal Infirmary", "MRI", "Manchester", "Oxford Road", "M13"),
    ("Wythenshawe Hospital", "Wythenshawe Hospital", "Manchester", "Wythenshawe", "M23"),
    ("North Manchester General Hospital", "North Manchester General", "Manchester", "Crumpsall", "M8"),
    ("The Christie", "The Christie", "Manchester", "Withington", "M20"),
    ("Salford Royal", "Salford Royal", "Salford", "Pendleton", "M6"),
    ("Trafford General Hospital", "Trafford General", "Trafford", "Davyhulme", "M41"),
    ("Stepping Hill Hospital", "Stepping Hill", "Stockport", "Hazel Grove", "SK2"),
    ("Tameside General Hospital", "Tameside General", "Tameside", "Ashton-under-Lyne", "OL6"),
    ("Royal Oldham Hospital", "Royal Oldham", "Oldham", "Oldham", "OL1"),
    ("Rochdale Infirmary", "Rochdale Infirmary", "Rochdale", "Rochdale", "OL12"),
    ("Fairfield General Hospital", "Fairfield General", "Bury", "Bury", "BL9"),
    ("Royal Bolton Hospital", "Royal Bolton", "Bolton", "Farnworth", "BL4"),
    ("Royal Albert Edward Infirmary", "Wigan Infirmary", "Wigan", "Wigan", "WN1"),
    ("Leigh Infirmary", "Leigh Infirmary", "Wigan", "Leigh", "WN7"),
]

# (name, borough, area, kind)
COLLEGES = [
    ("University of Manchester", "Manchester", "Oxford Road", "university"),
    ("Manchester Metropolitan University", "Manchester", "All Saints & Oxford Road", "university"),
    ("University of Salford", "Salford", "Salford Crescent & MediaCityUK", "university"),
    ("University of Bolton", "Bolton", "Bolton town centre", "university"),
    ("The Manchester College", "Manchester", "across Manchester", "college"),
    ("Xaverian College", "Manchester", "Rusholme", "sixth form college"),
    ("Loreto College", "Manchester", "Hulme", "sixth form college"),
    ("Salford City College", "Salford", "across Salford", "college"),
    ("Trafford College", "Trafford", "Trafford", "college"),
    ("Stockport College", "Stockport", "Stockport town centre", "college"),
    ("Aquinas College", "Stockport", "Stockport", "sixth form college"),
    ("Tameside College", "Tameside", "Ashton-under-Lyne", "college"),
    ("Oldham College", "Oldham", "Oldham", "college"),
    ("Hopwood Hall College", "Rochdale", "Rochdale & Middleton", "college"),
    ("Bury College", "Bury", "Bury town centre", "college"),
    ("Holy Cross College", "Bury", "Bury", "sixth form college"),
    ("Bolton College", "Bolton", "Bolton town centre", "college"),
    ("Wigan & Leigh College", "Wigan", "Wigan & Leigh", "college"),
    ("Winstanley College", "Wigan", "Billinge", "sixth form college"),
    ("St John Rigby College", "Wigan", "Orrell", "sixth form college"),
]


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("&", "and")).strip("-")


def _faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]}


def _crumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + u} for i, (n, u) in enumerate(items)]}


def _nearby(borough, hoods, k=10):
    return [h for h in hoods if h["borough"] == borough][:k]


def hospital_page(hosp, hoods):
    name, short, borough, area, pc = hosp
    root = "../"
    b = BMAP[borough]
    bslug, bname, bcodes, districts, roads, centres = b
    slug = slugify(name)
    near = "".join(f'<a class="chip" href="{root}driving-lessons/{h["slug"]}.html">{h["name"]}</a>' for h in _nearby(borough, hoods))
    others = "".join(f'<a class="chip" href="{slugify(x[0])}.html">{x[1]}</a>' for x in HOSPITALS if x[0] != name)
    faqs = [(f"Do you offer an NHS discount for {short} staff?", "Yes — NHS staff get 10 hours of driving lessons for £320 instead of £350. Show your NHS ID badge, NHS email or a recent payslip."),
            ("Can lessons fit around my shifts?", "Yes. Message us your shift pattern on WhatsApp and we'll plan lessons around early, late and night shifts where we can."),
            (f"Can you pick me up from {short}?", f"Yes — we can pick up from near the hospital in {area}, or from your home anywhere in Greater Manchester."),
            (f"Where would I take my test?", f"Learners in {bname} usually test at {' or '.join(centres)}.")]
    fh = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    body = page_hero(f"NHS staff · {name} · {pc}", f"Driving lessons for {short} staff.",
                     f"10 hours of driving lessons for £320 for NHS staff at {name} and across Greater Manchester. Lessons around your shifts, with pick-up from the hospital or home.",
                     [f'<a href="{root}nhs-driving-lessons.html">NHS staff</a>', short], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" data-wa="Hi! I work at {name} and I\'d like the NHS discount (10 hours £320)." href="https://wa.me/{WA}">{icon("wa")} Claim NHS discount</a><a class="btn btn--ghost" href="{root}book.html">Book in 60 seconds</a></div>')
    body += reassure()
    body += f"""<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" class="prose"><h2 class="mt-0">Lessons that fit around shifts</h2>
  <p>Hospital rotas don't fit neatly into weekly 9–5 slots. Tell us your shift pattern and we'll plan 2-hour lessons around it — before an early, after a late, or on your days off.</p>
  <p>We can pick you up from near {name} in {area}, or from home. Lessons build up to the roads {bname} drivers use every day: {roads[0].lower() + roads[1:]}</p>
  <h3>Why NHS staff choose SQ</h3><ul class="ticks"><li><span><b>10 hours for £320</b> instead of £350</span></li><li><span><b>Manual or automatic</b> — same price</span></li><li><span><b>Free DriveSQ Student Portal</b> — revise theory on breaks</span></li><li><span><b>Nervous?</b> Calm, judgement-free teaching</span></li></ul></div>
  <div data-reveal="right"><div class="card neon-border"><div class="card__icon">{icon('heart')}</div><h3>NHS offer</h3><div class="discount__badge">£320</div><p>10 hours · <s>£350</s> · save £30</p>
  <table class="summary"><tr><td>Hospital</td><td>{short}</td></tr><tr><td>Area</td><td>{area}, {pc}</td></tr><tr><td>Borough</td><td>{bname}</td></tr><tr><td>Proof</td><td>NHS ID / email / payslip</td></tr><tr><td>Test centres</td><td>{', '.join(centres)}</td></tr></table>
  <a class="btn btn--red btn--block" data-wa="Hi! I work at {name} and I'd like the NHS discount." href="https://wa.me/{WA}">{icon('wa')} Claim on WhatsApp</a></div></div>
</div></section>
<section class="section section--alt"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">NHS FAQ</div><h2 data-split>Questions from {short} staff.</h2></div><div class="faq">{fh}</div>
<p class="note mt-2">SQ Driving School is an independent driving school and is not affiliated with or endorsed by {name} or the NHS. The NHS discount is our own offer for NHS staff.</p></div></section>
<section class="section"><div class="container"><h3>Lessons near {short}</h3><div class="hero__badges">{near}<a class="chip" href="{root}areas/{bslug}.html">All of {bname}</a></div>
<h3 class="mt-3">Other hospitals</h3><div class="hero__badges">{others}</div></div></section>
{cta(root, "Thank you for everything you do.", "Message us your shift pattern and we'll get you booked in.")}"""
    sch = [{"@context": "https://schema.org", "@type": "Service", "serviceType": "Driving lessons for NHS staff", "name": f"Driving lessons for {name} staff",
            "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE, "telephone": "+44 7352 932003"},
            "areaServed": {"@type": "Place", "name": f"{area}, {bname}"}, "audience": {"@type": "Audience", "audienceType": "NHS staff"},
            "offers": {"@type": "Offer", "name": "NHS 10-hour block", "price": "320", "priceCurrency": "GBP"}},
           _faq_schema(faqs), _crumbs([("Home", ""), ("NHS staff", "nhs-driving-lessons.html"), (short, f"nhs/{slug}.html")])]
    return page(f"nhs/{slug}.html", f"Driving Lessons for {short} Staff | NHS £320",
                f"NHS staff at {name} ({area}) get 10 hours of driving lessons for £320. Lessons around shifts, pick-up from the hospital or home. Manual & automatic.", body, root, active="discounts.html", schema=sch)


def college_page(col, hoods):
    name, borough, area, kind = col
    root = "../"
    b = BMAP[borough]
    bslug, bname, bcodes, districts, roads, centres = b
    slug = slugify(name)
    near = "".join(f'<a class="chip" href="{root}driving-lessons/{h["slug"]}.html">{h["name"]}</a>' for h in _nearby(borough, hoods))
    others = "".join(f'<a class="chip" href="{slugify(x[0])}.html">{x[0]}</a>' for x in COLLEGES if x[0] != name)
    uni = kind == "university"
    who = "students" if uni else "students (17+)"
    faqs = [(f"Is there a student discount for {name} students?", "Yes — students get 10 hours for £320 instead of £350 with a valid student ID card or enrolment letter."),
            ("Can lessons fit around my timetable?", "Yes. Most students book two 2-hour lessons a week around lectures or classes."),
            (f"Can you pick me up from {name}?", f"Yes — from near campus in {area}, " + ("your halls, " if uni else "") + "or from home anywhere in Greater Manchester."),
            ("How do I prepare for the theory test?", "Every SQ learner gets the free DriveSQ Student Portal with a theory library and 50-question mock tests.")]
    fh = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    body = page_hero(f"Students · {name}", f"Driving lessons for {name} students.",
                     f"Student discount: 10 hours for £320. Lessons around your {'lectures' if uni else 'classes'}, with pick-up from near campus in {area}{', halls' if uni else ''} or home.",
                     [f'<a href="{root}student-driving-lessons-manchester.html">Students</a>', name], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" data-wa="Hi! I study at {name} and I\'d like the student discount (10 hours £320)." href="https://wa.me/{WA}">{icon("wa")} Claim student discount</a><a class="btn btn--ghost" href="{root}book.html">Book in 60 seconds</a></div>')
    body += reassure()
    body += f"""<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" class="prose"><h2 class="mt-0">Learn to drive while you study</h2>
  <p>Passing your test while you're at {name} gives you freedom for placements, part-time jobs and getting home. Two 2-hour lessons a week usually fit well around a {'university' if uni else 'college'} timetable.</p>
  <p>We pick up from near campus in {area}{', from halls' if uni else ''} or from home, and lessons build up to {bname}'s roads: {roads[0].lower() + roads[1:]}</p>
  <h3>Student tips</h3><ul class="ticks"><li><span><b>Avoid long gaps</b> — finish lessons before long holidays where you can</span></li><li><span><b>Revise theory for free</b> in the DriveSQ Student Portal</span></li><li><span><b>Book your test early</b> — see the <a href="{root}knowledge/driving-test-booking-rules-2026.html">2026 booking rules</a></span></li></ul></div>
  <div data-reveal="right"><div class="card neon-border"><div class="card__icon">{icon('grad')}</div><h3>Student offer</h3><div class="discount__badge">£320</div><p>10 hours · <s>£350</s> · save £30</p>
  <table class="summary"><tr><td>For</td><td>{name} {who}</td></tr><tr><td>Area</td><td>{area}</td></tr><tr><td>Borough</td><td>{bname}</td></tr><tr><td>Proof</td><td>Student ID / enrolment letter</td></tr><tr><td>Test centres</td><td>{', '.join(centres)}</td></tr></table>
  <a class="btn btn--red btn--block" data-wa="Hi! I study at {name} and I'd like the student discount." href="https://wa.me/{WA}">{icon('wa')} Claim on WhatsApp</a></div></div>
</div></section>
<section class="section section--alt"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">Student FAQ</div><h2 data-split>Questions from {name} students.</h2></div><div class="faq">{fh}</div>
<p class="note mt-2">SQ Driving School is an independent driving school and is not affiliated with or endorsed by {name}. The student discount is our own offer.</p></div></section>
<section class="section"><div class="container"><h3>Lessons near {name}</h3><div class="hero__badges">{near}<a class="chip" href="{root}areas/{bslug}.html">All of {bname}</a></div>
<h3 class="mt-3">Other universities &amp; colleges</h3><div class="hero__badges">{others}</div></div></section>
{cta(root, "Pass before you graduate.", "Message us with your timetable and we'll get you booked in.")}"""
    sch = [{"@context": "https://schema.org", "@type": "Service", "serviceType": "Driving lessons for students", "name": f"Driving lessons for {name} students",
            "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE, "telephone": "+44 7352 932003"},
            "areaServed": {"@type": "Place", "name": f"{area}, {bname}"}, "audience": {"@type": "EducationalAudience", "educationalRole": "student"},
            "offers": {"@type": "Offer", "name": "Student 10-hour block", "price": "320", "priceCurrency": "GBP"}},
           _faq_schema(faqs), _crumbs([("Home", ""), ("Students", "student-driving-lessons-manchester.html"), (name, f"students/{slug}.html")])]
    return page(f"students/{slug}.html", f"Driving Lessons for {name} Students | £320",
                f"{name} students get 10 hours of driving lessons for £320. Lessons around your timetable, pick-up from near campus or home. Manual & automatic.", body, root, active="discounts.html", schema=sch)


def nhs_hub():
    root = ""
    cards = "".join(f'<a class="card" href="nhs/{slugify(h[0])}.html" data-reveal="up" data-tilt="6"><div class="card__icon">{icon("heart")}</div><h3>{h[0]}</h3><p class="mb-0">{h[3]}, {h[2]} · {h[4]}</p></a>' for h in HOSPITALS)
    body = page_hero("NHS staff discount", "Driving lessons for NHS staff.", "Thank you for everything you do. NHS staff across Greater Manchester get 10 hours of driving lessons for £320, with lessons around your shifts.", ["NHS staff"], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" data-wa="Hi! I work for the NHS and I\'d like the NHS discount (10 hours £320)." href="https://wa.me/{WA}">{icon("wa")} Claim NHS discount</a><a class="btn btn--ghost" href="discounts.html">All discounts</a></div>')
    body += reassure()
    body += f"""<section class="section"><div class="container"><div class="section__head"><div class="eyebrow">Find your hospital</div><h2 data-split>NHS staff at every Greater Manchester hospital.</h2><p class="lead">The discount is for all NHS staff — clinical and non-clinical — wherever you work.</p></div><div class="grid grid--3" data-stagger=".04">{cards}</div>
<p class="note mt-3">SQ Driving School is independent and not affiliated with the NHS or any hospital. Proof of NHS employment is required.</p></div></section>
{cta(root, "10 hours for £320.", "Message us your shift pattern and we'll get you booked in.")}"""
    return page("nhs-driving-lessons.html", "NHS Staff Driving Lessons Greater Manchester | 10 Hours £320",
                "NHS staff driving lesson discount across Greater Manchester: 10 hours for £320. Lessons around shifts at every major hospital. Manual & automatic.", body, root, active="discounts.html")


def students_hub():
    root = ""
    unis = "".join(f'<a class="card" href="students/{slugify(c[0])}.html" data-reveal="up" data-tilt="6"><div class="card__icon">{icon("grad")}</div><h3>{c[0]}</h3><p class="mb-0">{c[2]}, {c[1]}</p></a>' for c in COLLEGES if c[3] == "university")
    cols = "".join(f'<a class="card" href="students/{slugify(c[0])}.html" data-reveal="up" data-tilt="6"><div class="card__icon">{icon("book")}</div><h3>{c[0]}</h3><p class="mb-0">{c[2]}, {c[1]}</p></a>' for c in COLLEGES if c[3] != "university")
    body = page_hero("Student discount", "Driving lessons for students in Manchester.", "University, college and sixth form students across Greater Manchester get 10 hours of driving lessons for £320. Lessons around your timetable.", ["Students"], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" data-wa="Hi! I\'m a student and I\'d like the student discount (10 hours £320)." href="https://wa.me/{WA}">{icon("wa")} Claim student discount</a><a class="btn btn--ghost" href="knowledge/learning-to-drive-as-a-student-in-manchester.html">Student guide</a></div>')
    body += reassure()
    body += f"""<section class="section"><div class="container"><div class="section__head"><div class="eyebrow">Universities</div><h2 data-split>University students.</h2></div><div class="grid grid--4" data-stagger=".04">{unis}</div></div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Colleges &amp; sixth forms</div><h2 data-split>College and sixth form students.</h2></div><div class="grid grid--3" data-stagger=".04">{cols}</div>
<p class="note mt-3">SQ Driving School is independent and not affiliated with any university or college. Valid student ID or an enrolment letter is required.</p></div></section>
{cta(root, "Pass before you graduate.")}"""
    return page("student-driving-lessons-manchester.html", "Student Driving Lessons Manchester | 10 Hours £320",
                "Student driving lessons in Manchester: 10 hours for £320 for university, college and sixth form students across Greater Manchester.", body, root, active="discounts.html")
