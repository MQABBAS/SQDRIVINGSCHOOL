"""Sixth forms & colleges, big workplaces, and practical Greater Manchester driving guides.

Schools: only places with 16-18 students (you can start driving at 17), named as they are today
(e.g. Manchester Creative and Media Academy is now Co-op Academy North Manchester). We describe the area, not the
school's results or admissions, and never claim a partnership with any school or employer."""
from hub_shell import *
import re
import zlib
import pages_routes as RT
import pages_seo as SEO
import local_districts as LD

HOODS = {h["slug"]: h for h in SEO.neighbourhoods()}
CBY = {c["slug"]: c for c in RT.C}
SIDE = (f'<p>£35/hr manual or automatic · single hour £40 · 10 hours £350 (£320 for NHS staff, students and M16, M18 &amp; M19) · door-to-door pick-up.</p>'
        f'<a class="btn btn--red btn--block" href="#book">{icon("calendar")} Book in 60 seconds</a>')
GOV = {"prov": ("GOV.UK — Apply for your first provisional driving licence", "https://www.gov.uk/apply-first-provisional-driving-licence"),
       "theory": ("GOV.UK — Theory test: cars", "https://www.gov.uk/theory-test"),
       "lessons": ("GOV.UK — Driving lessons and learning to drive", "https://www.gov.uk/driving-lessons-learning-to-drive"),
       "supervise": ("GOV.UK — Supervising a learner driver", "https://www.gov.uk/supervise-learner-driver"),
       "hc": ("GOV.UK — The Highway Code", "https://www.gov.uk/guidance/the-highway-code"),
       "mway": ("GOV.UK — Learner drivers on motorways", "https://www.gov.uk/government/news/learner-drivers-will-be-allowed-on-motorways-from-2018")}


def area_link(key, root="../"):
    if key in HOODS:
        return f'<a href="{root}driving-lessons/{key}.html">{HOODS[key]["name"]}</a>'
    return f'<a href="{root}areas/{key}.html">{key.replace("-", " ").title()}</a>'


def centre_html(cs, root="../"):
    return ", ".join(f'<a href="{root}test-routes/{c}-driving-test-routes.html">{CBY[c]["name"]}</a> ({CBY[c]["rate"]}% in 2024-25)' for c in cs if c in CBY)


def _district(area):
    if area in HOODS:
        for c in HOODS[area]["codes"]:
            if c in LD.DISTRICTS:
                return LD.DISTRICTS[c]
    return None


def _parts(area, cs):
    """Real local detail for an area: the hand-written district notes (inner Manchester, Altrincham, Hale…) and the
    roads and common mistakes of the test centres learners there use."""
    out, d = [], _district(area)
    if d:
        out.append((f"Learning to drive around {d['short']}", f"<p>{d['feel']}</p>"))
        out.append((f"From quiet roads to test-ready in {d['short']}", "<ol>" + "".join(f"<li><b>{t}.</b> {x}</li>" for t, x in d["ladder"]) + "</ol>"))
        out.append(("Local hotspots we teach", "<ul>" + "".join(f"<li><b>{t}.</b> {x}</li>" for t, x in d["spots"]) + "</ul>"))
        out.append(("Where we pick up nearby", "<ul>" + "".join(f"<li>{x}</li>" for x in d["pickups"]) + f"</ul><p>{d['why']}</p>"))
    road = lambda rs: "<ul>" + "".join(f"<li><b>{(r[0] + ' ' + r[1]).strip()}</b> — {r[2]}</li>" for r in rs) + "</ul>"
    mis = lambda ms: "<ul>" + "".join(f"<li><b>{m[0]}.</b> {m[1]} <i>How we fix it:</i> {m[2]}</li>" for m in ms) + "</ul>"
    strip = lambda h: re.sub(r"<[^>]+>", "", h)
    for c in cs:
        if c in CBY:
            C = CBY[c]
            out.append((f"About {C['name']} test centre", f"<p>{strip(C['intro'])}</p>"))
            out.append((f"Roads on {C['name']} test routes", road(C["roads"][:3])))
            out.append((f"Where learners slip up at {C['name']}", mis(C["mistakes"][:2])))
            if C["roads"][3:]:
                out.append((f"More roads examiners use from {C['name']}", road(C["roads"][3:6])))
            if C["mistakes"][2:]:
                out.append((f"More {C['name']} faults to avoid", mis(C["mistakes"][2:4])))
            out.append((f"What {C['name']}'s routes are like", f"<p>{strip(C['area'])}</p>"))
    return out


_GROUPS = {}
def _pick(key, area, cs):
    """Pages that share an area get different slices of its local detail, so no two read the same."""
    d = _district(area)
    members = _GROUPS.setdefault(((d or {}).get("short"), tuple(cs)), [])
    if key not in members:
        members.append(key)
    parts, k, n = _parts(area, cs), members.index(key), len(members)
    if not parts:
        return ""
    if n == 1:  # on its own: start somewhere different from pages in other areas that use the same test centre
        st = zlib.crc32(key.encode()) % len(parts)
        chosen = (parts[st:] + parts[:st])[:4]
    else:
        chosen = parts[k::n] or [parts[k % len(parts)]]
    return "".join(f"<h2>{h}</h2>{b}" for h, b in chosen[:4])


# slug, name, where (short), area key, centres, kind, note
SCHOOLS = [
 ("whalley-range-11-18-high-school", "Whalley Range 11-18 High School", "Whalley Range, M16", "whalley-range", ["west-didsbury"], "school", "A large girls' school with its own sixth form. Students often have Princess Road and Wilbraham Road on their doorstep — both on West Didsbury test routes."),
 ("parrs-wood-high-school", "Parrs Wood High School & Sixth Form", "East Didsbury, M20", "east-didsbury", ["west-didsbury", "bredbury"], "school", "Next to the Parrs Wood leisure park at the end of Kingsway — a perfect place to learn dual-carriageway lane discipline before your test."),
 ("william-hulmes-grammar-school", "William Hulme's Grammar School", "Whalley Range, M16", "whalley-range", ["west-didsbury"], "school", "An all-through school with a sixth form in Whalley Range. Many sixth formers book weekend or holiday lessons around a busy timetable."),
 ("manchester-grammar-school", "The Manchester Grammar School", "Rusholme / Fallowfield, M13", "rusholme", ["west-didsbury"], "independent", "Students come from right across Greater Manchester, so we often pick up from home rather than school — tell us which suits you."),
 ("withington-girls-school", "Withington Girls' School", "Fallowfield, M14", "fallowfield", ["west-didsbury"], "independent", "Close to Wilmslow Road's busy bus corridor, which is great practice once your basics are solid."),
 ("manchester-high-school-for-girls", "Manchester High School for Girls", "Rusholme / Fallowfield, M14", "fallowfield", ["west-didsbury"], "independent", "Lessons can start from home or school; many students book a block in the Easter or summer holidays."),
 ("chethams-school-of-music", "Chetham's School of Music", "Manchester city centre, M3", "city-centre", ["cheetham-hill"], "independent", "A city-centre school next to Victoria station. We start students somewhere quieter, then build up to city streets and Cheetham Hill's test routes, ten minutes north."),
 ("king-david-high-school", "King David High School", "Crumpsall, M8", "crumpsall", ["cheetham-hill"], "school", "Right by Cheetham Hill test routes — Bury Old Road and Bury New Road are part of everyday driving here."),
 ("abbey-college-manchester", "Abbey College Manchester", "Manchester city centre", "city-centre", ["cheetham-hill"], "independent", "A sixth-form college in the city centre with many international students — see our page for overseas drivers if you've driven abroad."),
 ("trinity-cofe-high-school", "Trinity CofE High School & Sixth Form", "Hulme, M15", "hulme", ["west-didsbury", "cheetham-hill"], "school", "On the edge of the city centre in Hulme, between the Mancunian Way and Princess Road — both great roads to build up to."),
 ("connell-co-op-college", "Connell Co-op College", "Beswick, M11", "beswick", ["cheetham-hill", "chadderton"], "college", "A sixth-form college near the Etihad Campus. Alan Turing Way and Ashton New Road give quick access to dual-carriageway practice."),
 ("altrincham-grammar-school-for-boys", "Altrincham Grammar School for Boys", "Altrincham, WA14", "altrincham", ["sale"], "school", "Close to the A56 — Sale test centre is a short drive away along Washway Road."),
 ("altrincham-grammar-school-for-girls", "Altrincham Grammar School for Girls", "Altrincham, WA14", "altrincham", ["sale"], "school", "Students practise around Altrincham and Timperley before Sale's test routes."),
 ("sale-grammar-school", "Sale Grammar School", "Sale, M33", "sale", ["sale"], "school", "Very close to Sale test centre — you'll know its roads well before your test."),
 ("stretford-grammar-school", "Stretford Grammar School", "Stretford, M32", "stretford", ["sale", "west-didsbury"], "school", "Next to the A56 Chester Road and the M60 — plenty of variety for building up to test standard."),
 ("urmston-grammar", "Urmston Grammar", "Urmston, M41", "urmston", ["sale"], "school", "Quiet residential roads for early lessons, with the Trafford Centre's busy roundabouts nearby for later ones."),
 ("loreto-grammar-school", "Loreto Grammar School", "Altrincham, WA14", "altrincham", ["sale"], "school", "A girls' grammar with a sixth form — lessons can fit before school, after school or at weekends."),
 ("st-ambrose-college", "St Ambrose College", "Hale Barns, WA15", "hale-barns", ["sale"], "school", "Close to the M56 and Manchester Airport — ideal for a first motorway lesson once you're ready."),
 ("cheadle-and-marple-sixth-form-college", "Cheadle and Marple Sixth Form College", "Cheadle Hulme & Marple", "cheadle-hulme", ["bredbury"], "college", "Two campuses, Cheadle Hulme and Marple. Bredbury is the usual test centre, and we pick up from either campus."),
 ("cheadle-hulme-school", "Cheadle Hulme School", "Cheadle Hulme, SK8", "cheadle-hulme", ["bredbury", "west-didsbury"], "independent", "Near the A555 airport relief road — great for higher-speed practice and big roundabouts."),
 ("stockport-grammar-school", "Stockport Grammar School", "Stockport, SK2", "stockport", ["bredbury"], "independent", "On the A6 south of Stockport town centre; Bredbury test centre is a short drive away."),
 ("ashton-sixth-form-college", "Ashton Sixth Form College", "Ashton-under-Lyne, OL6", "ashton-under-lyne", ["bredbury", "chadderton"], "college", "One of Tameside's biggest sixth-form colleges. Learners usually test at Bredbury or Chadderton."),
 ("oldham-sixth-form-college", "Oldham Sixth Form College", "Oldham town centre", "oldham", ["chadderton"], "college", "Chadderton test centre is close by — Broadway and its business-park roundabouts are key practice."),
 ("hulme-grammar-school-oldham", "The Hulme Grammar School", "Oldham", "oldham", ["chadderton"], "independent", "An Oldham independent school; lessons can start from home or school and build up to Chadderton's test routes."),
 ("rochdale-sixth-form-college", "Rochdale Sixth Form College", "Rochdale town centre", "rochdale", ["rochdale"], "college", "Near Rochdale's one-way system and hilly terraced streets — practise them and Rochdale's test routes hold no surprises."),
 ("bolton-school", "Bolton School", "Bolton", "bolton", ["bolton"], "independent", "Bolton's test centre is close to the A666 St Peter's Way — we practise it with every Bolton learner."),
 ("bury-grammar-school", "Bury Grammar School", "Bury town centre", "bury", ["bury"], "independent", "A short drive from Bury test centre and the Peel Way ring road."),
 ("pendleton-sixth-form-college", "Pendleton Sixth Form College", "Pendleton, Salford", "pendleton", ["cheetham-hill"], "college", "Part of Salford City College, near the A6 and the M602 — ideal for a first motorway lesson."),
 ("royal-northern-college-of-music", "Royal Northern College of Music", "Oxford Road, M13", "chorlton-on-medlock", ["west-didsbury", "cheetham-hill"], "college", "On Oxford Road — learn the bus gates and restrictions there, and practise somewhere calmer first."),
]

# slug, name, where, area key, centres, note, shifts?
WORK = [
 ("mediacityuk", "MediaCityUK", "Salford Quays, M50", "salford-quays", ["cheetham-hill", "sale"], "Lessons before or after shifts, with pick-up from the Quays. Trafford Road and the M602 are nearby for later lessons.", True),
 ("manchester-airport", "Manchester Airport", "Ringway, M90", "wythenshawe", ["west-didsbury", "sale"], "Thousands of people work early and late shifts at the airport. We fit lessons around rotas and pick up from home or work.", True),
 ("airport-city", "Airport City", "next to Manchester Airport", "wythenshawe", ["west-didsbury", "sale"], "Offices, hotels and logistics beside the airport, with the M56 and the A555 relief road on the doorstep.", True),
 ("trafford-park", "Trafford Park", "Trafford, M17", "trafford-park", ["sale"], "One of Europe's biggest industrial estates — lorries, roundabouts and shift traffic make it serious practice.", True),
 ("trafford-centre", "The Trafford Centre", "Trafford, M17", "trafford-park", ["sale"], "Retail and hospitality staff often need evening or weekend lessons; the roads around the centre are great for big-roundabout practice.", True),
 ("etihad-campus", "Etihad Campus", "Beswick, M11", "beswick", ["cheetham-hill", "chadderton"], "Event days change the roads completely — we plan lessons around fixtures.", True),
 ("old-trafford", "Old Trafford (stadium and cricket ground)", "Old Trafford, M16", "old-trafford", ["sale", "west-didsbury"], "Matchday staff and stewards work odd hours; we work around them, and avoid the area on event days.", True),
 ("spinningfields", "Spinningfields", "Manchester city centre, M3", "spinningfields", ["cheetham-hill", "west-didsbury"], "Office workers book early-morning or lunchtime lessons — we collect you outside work and drive somewhere quieter.", False),
 ("manchester-arndale", "Manchester Arndale", "Manchester city centre", "city-centre", ["cheetham-hill"], "Retail staff often need lessons on days off; we pick up from home or near the centre.", True),
 ("manchester-science-park", "Manchester Science Park", "Oxford Road corridor, M15", "hulme", ["west-didsbury"], "Close to Oxford Road and the universities — learn the bus gates there safely.", False),
 ("salford-quays", "Salford Quays", "Salford, M50", "salford-quays", ["cheetham-hill", "sale"], "Offices, hotels and apartments; lessons before or after work.", False),
 ("manchester-fort", "Manchester Fort", "Cheetham Hill, M8", "cheetham-hill", ["cheetham-hill"], "Staff here work right on Cheetham Hill test routes — you'll know them before test day.", True),
 ("roundthorn-industrial-estate", "Roundthorn Industrial Estate", "Wythenshawe, M23", "wythenshawe", ["west-didsbury", "sale"], "Shift workers in Wythenshawe; Princess Parkway and the M56 are close for later lessons.", True),
 ("broadway-business-park", "Broadway Business Park", "Chadderton, OL9", "chadderton", ["chadderton"], "Right next to Chadderton test centre — its roundabouts are on the test routes.", True),
 ("hollinwood-business-district", "Hollinwood Business District", "Hollinwood, Oldham", "hollinwood", ["chadderton"], "Near the M60 and the Oldham Road; lessons around shifts.", True),
 ("kingsway-business-park", "Kingsway Business Park", "Rochdale", "rochdale", ["rochdale"], "Close to Rochdale's test centre and the A627(M).", True),
 ("heywood-distribution-park", "Heywood Distribution Park", "Heywood, OL10", "heywood", ["rochdale", "bury"], "Warehouse and logistics shifts; M62 nearby for motorway lessons when you're ready.", True),
 ("middlebrook", "Middlebrook", "Horwich, Bolton", "horwich", ["bolton"], "Retail, leisure and offices near the M61 — evening and weekend lessons are popular.", True),
 ("logistics-north", "Logistics North", "Bolton", "bolton", ["bolton", "atherton"], "Shift workers near the M61; lessons around rotas.", True),
 ("stockport-exchange", "Stockport Exchange", "Stockport town centre", "stockport", ["bredbury"], "Offices by Stockport station; lunchtime and after-work lessons.", False),
 ("crown-point-denton", "Crown Point", "Denton, M34", "denton", ["bredbury"], "Retail staff in Denton; lessons on days off. M60 and M67 junctions nearby.", True),
 ("port-salford", "Port Salford", "Barton / Irlam, Salford", "eccles", ["cheetham-hill", "sale"], "Logistics next to the Manchester Ship Canal and the M60.", True),
]


def _school_shell(path, name, where, cs, body, faqs):
    first = CBY[cs[0]]["name"] if cs and cs[0] in CBY else "your"
    return shell(path, f"Driving Lessons for {name} Students | SQ Driving", "Students", [("Students", "student-driving-lessons-manchester.html"), (name, path)],
                 f"Driving lessons for {name} students.", f"Lessons around your timetable for students at {name}, {where} — 10 hours £320 with student ID, pick-up from school, college or home.",
                 [("17", "age you can start"), ("£320", "10 hrs with student ID"), (first, "nearest test centre"), ("Free", "Student Portal")],
                 ["Start at 17 — apply for your provisional at 15 years 9 months.", "Lessons around your timetable and holidays.", "10 hours £320 with student ID.", f"Practise on {first} test routes."],
                 body, faqs, [GOV["prov"], GOV["theory"], GOV["supervise"]],
                 [("student-driving-lessons-manchester.html", "Students", "Student driving lessons", "£320 for 10 hours."), ("driving-lessons-manchester.html", "Manchester", "Driving lessons in Manchester", "Prices, areas and the planner."), ("intensive.html", "Intensive", "Holiday intensive courses", "Big progress in the holidays.")],
                 side_title="Student lessons", booking_heading="Book student driving lessons in 60 seconds", active="lessons.html", side_html=SIDE)


def work_page(w):
    slug, name, where, area, cs, note, shifts = w
    path = f"work/{slug}.html"
    body = f"""<p class="lead">Driving lessons for people who work at {name} ({where}). {note}</p>
<h2>Lessons that fit your work</h2>
<ul>{"<li><b>Shift-friendly:</b> early mornings, late afternoons and days off — tell us your rota.</li>" if shifts else "<li><b>Before or after work, or at lunchtime</b> — a single hour is £40, two hours £70.</li>"}
<li><b>Pick-up from work or home</b> — wherever it's safe and legal to stop.</li>
</ul>
{_pick("w:" + slug, area, cs)}
<p>Local area: {area_link(area)} · usual test centre{"s" if len(cs) > 1 else ""}: {centre_html(cs)}. Lessons £35/hr, £40 for a single hour, 10 hours £350. <a href="../prices.html">Prices →</a></p>
<p class="note">SQ Driving School isn't connected to {name}; we teach lots of people who work there.</p>"""
    faqs = [(f"Can you pick me up from {name}?", "Yes, from anywhere safe and legal to stop, or from home."),
            ("Can lessons fit around shifts?", "Yes — tell us your rota and we'll match an instructor whose hours fit."),
            ("How much are lessons?", "£35/hr for 2 hours or more, £40 for a single hour, £350 for 10 hours.")]
    first = CBY[cs[0]]["name"] if cs and cs[0] in CBY else "your local"
    return shell(path, f"Driving Lessons for {name} Workers | SQ Driving", "Workplaces", [("Workplaces", "work.html"), (name, path)],
                 f"Driving lessons for people who work at {name}.", f"Lessons around your {'shifts' if shifts else 'working day'} at {name}, {where} — pick-up from work or home, £35/hr.",
                 [("£35", "per hour"), ("£40", "single hour"), (first, "test centre"), ("Free", "Student Portal")],
                 ["Lessons around your working hours.", "Pick-up from work or home.", "Learn your own commute.", f"Practise on {first} test routes."],
                 body, faqs, [GOV["lessons"], GOV["mway"]],
                 [("driving-lessons-manchester.html", "Manchester", "Driving lessons in Manchester", "Prices, areas and the planner."), ("evening-weekend-driving-lessons-manchester.html", "Timing", "Evening & weekend lessons", "Around work and family."), ("nhs-driving-lessons.html", "NHS", "NHS staff discount", "10 hours £320.")],
                 side_title="Lessons around work", booking_heading="Book driving lessons in 60 seconds", active="lessons.html", side_html=SIDE)


# practical guides: slug, title, desc, body, faqs, sources
GUIDES = [
 ("matchday-driving-manchester", "Driving on matchdays in Manchester", "How Old Trafford and Etihad events change the roads — and how learners and new drivers should plan around them.",
  """<p class="lead">On matchdays and concert nights, the roads around Old Trafford (M16) and the Etihad Campus (M11) fill hours before and after events, some roads close, and thousands of pedestrians cross wherever they can.</p>
<h2>What changes</h2><ul><li><b>Road closures and diversions</b> near the grounds — follow official signs, not your sat-nav.</li><li><b>Crowds on foot</b>, often not looking at traffic.</li><li><b>Parking restrictions</b> on residential streets near the stadiums.</li><li><b>Slow queues</b> on Chester Road, Ashton New Road and Alan Turing Way.</li></ul>
<h2>For learners</h2><p>We plan lessons around fixtures so you don't lose an hour in a queue — and if you're testing at Sale or Cheetham Hill, we'll check the event calendar with you.</p>
<h2>For new drivers</h2><ul><li>Check the fixture list before you set off.</li><li>Leave much earlier or avoid the area.</li><li>Slow right down near crowds; expect people stepping out.</li></ul>""",
  [("Do driving tests run on matchdays?", "Yes, tests run as normal — but roads nearby may be busier. Plan to arrive early."), ("Can we avoid the area in lessons?", "Yes — tell us and we'll plan around events.")], ["hc"]),
 ("20mph-zones-manchester", "20 mph zones in Greater Manchester", "Why so many Manchester roads are 20 mph, how to spot them and how examiners judge your speed.",
  """<p class="lead">Many residential streets across Greater Manchester have 20 mph limits, often marked with signs at the entry and painted roundels on the road.</p>
<h2>How to spot them</h2><ul><li>Circular 20 signs where the zone starts, and an end sign where it finishes.</li><li>Painted "20" roundels on the road surface.</li><li>Traffic calming such as speed humps or narrowings in some zones.</li></ul>
<h2>On the driving test</h2><p>Going over the limit is a fault — but so is crawling far below it without reason. Drive at a safe speed for the conditions, up to the limit.</p>
<h2>Our tip</h2><p>Every time you turn into a new road, look for a limit sign. If there are street lights and no signs, the limit is usually 30 mph — unless it's marked otherwise.</p>""",
  [("Is 20 mph enforced?", "Yes, limits are enforceable. Treat every sign seriously."), ("What if I'm unsure of the limit?", "Look for signs and roundels; street lights without other signs usually mean 30 mph.")], ["hc"]),
 ("yellow-box-junctions-manchester", "Yellow box junctions: the Manchester learner's guide", "When you can and can't enter a yellow box, and the city-centre spots where learners get it wrong.",
  """<p class="lead">Yellow criss-cross boxes keep junctions clear. You must not enter the box unless your exit is clear — the one exception is turning right, when you may wait in the box if only oncoming traffic (or other right-turners) stops you.</p>
<h2>Where you'll meet them</h2><p>Busy city-centre and inner-ring-road junctions, and outside fire and ambulance stations.</p>
<h2>How to get it right</h2><ul><li>Look at your exit before you reach the box.</li><li>If the exit isn't clear, stop before the yellow lines.</li><li>Turning right? You can wait in the box for a gap in oncoming traffic.</li></ul>""",
  [("Can I be fined for stopping in a box junction?", "Yes, in many areas box junctions are camera-enforced."), ("Is it a test fault?", "Entering when your exit isn't clear can be marked as a fault.")], ["hc"]),
 ("advanced-stop-lines-cycle-boxes", "Cycle boxes and advanced stop lines", "The green boxes at Manchester traffic lights: where to stop and how to treat cyclists.",
  """<p class="lead">At many traffic lights you'll see a second stop line with a cycle box in front of it — often coloured green. It gives cyclists a safe space ahead of traffic.</p>
<h2>The rule</h2><p>Stop at the first white line when the lights are amber or red. If you've already crossed the first line when the lights change, stop at the second and don't block the box any more than you have to.</p>
<h2>Cyclists</h2><ul><li>Expect cyclists to move off first.</li><li>Check your left mirror and blind spot before turning left.</li><li>Give at least 1.5 metres when overtaking at up to 30 mph (Highway Code).</li></ul>""",
  [("Is stopping in the cycle box a test fault?", "It can be. Stop at the first line if you can."), ("How much room should I give cyclists?", "The Highway Code advises at least 1.5 metres at speeds up to 30 mph, more at higher speeds.")], ["hc"]),
 ("bus-stop-bypasses-manchester", "Bus-stop bypasses and floating bus stops", "Manchester's Oxford Road and Wilmslow Road layouts explained for learners.",
  """<p class="lead">On corridors like Oxford Road and Wilmslow Road, cycle lanes run behind bus stops, so passengers cross the cycle lane to reach a bus-stop island.</p>
<h2>What it means for drivers</h2><ul><li>Cyclists may be moving fast just to your left.</li><li>Pedestrians step off islands to cross — watch for them.</li><li>Buses stop in the main lane; don't take risks passing them.</li></ul>
<h2>How we teach it</h2><p>We drive these corridors only once your car control is automatic, and we talk through each layout before you meet it.</p>""",
  [("Can I overtake a stopped bus?", "Only when it's safe and legal — watch for pedestrians stepping out in front of it."), ("Do I need to give way to cyclists turning in?", "Check your mirrors and blind spots before turning across a cycle lane.")], ["hc"]),
 ("school-run-driving", "Driving at school-run times", "Parked cars, children and lollipop crossings — how to stay safe and calm.",
  """<p class="lead">Between about 8 and 9am and 3 and 4pm, residential roads near schools change completely: cars double-parked, children crossing between vehicles, and school crossing patrols.</p>
<h2>What to do</h2><ul><li>Slow right down near schools — expect a child to step out.</li><li>Stop for school crossing patrols (lollipop signs) — it's the law.</li><li>Never stop on zig-zag lines outside schools.</li></ul>
<h2>In lessons</h2><p>We deliberately drive near schools at these times once you're ready, because test routes run through residential areas all day.</p>""",
  [("Must I stop for a lollipop sign?", "Yes, you must stop when a school crossing patrol shows a stop sign."), ("Can I stop on school zig-zags?", "No — they're for keeping the area clear.")], ["hc"]),
 ("winter-driving-pennine-roads", "Winter driving on Greater Manchester's Pennine roads", "Snow, ice and fog on the high roads around Saddleworth, Littleborough and the edge of the moors.",
  """<p class="lead">The eastern and northern edges of Greater Manchester climb into the Pennines. Roads over the moors from Saddleworth and Littleborough can get snow, ice and fog when the city is just wet.</p>
<h2>Before you go</h2><ul><li>Check the weather and road conditions, especially for high routes.</li><li>Clear all snow and ice from windows, lights and the roof.</li><li>Pack warm clothes, water and a charged phone.</li></ul>
<h2>On the road</h2><ul><li>Stopping distances can be up to ten times longer on ice (Highway Code).</li><li>Use the highest gear you can for grip; brake and steer gently.</li><li>In fog, use dipped headlights and fog lights only when visibility is seriously reduced.</li></ul>""",
  [("Do you give winter lessons?", "Yes — in safe conditions we practise wet, dark and cold-weather driving. We won't take risks in ice or snow."), ("How much longer is stopping on ice?", "The Highway Code says up to ten times longer.")], ["hc"]),
 ("hill-starts-greater-manchester", "Hill starts in Greater Manchester", "Mastering hills — from Rochdale's terraced streets to the climbs out of the city.",
  """<p class="lead">Greater Manchester isn't flat: the towns towards the Pennines have steep terraced streets, and the north and east of the city have plenty of gradients.</p>
<h2>Manual cars</h2><ol><li>Handbrake on, clutch down, select first.</li><li>Set a little more gas than usual, bring the clutch to the bite.</li><li>Check mirrors and blind spot, release the handbrake as the car wants to move.</li></ol>
<h2>Automatic cars</h2><p>Many automatics hold the car briefly on a hill. Still use the handbrake or hold the brake until you're ready.</p>
<h2>On the test</h2><p>Examiners may ask you to pull up and move off on a hill. Rolling back is a fault — practise until it's automatic.</p>""",
  [("Is a hill start on the test?", "You may be asked to move off on a gradient as part of normal driving."), ("Do automatics roll back?", "Many have hill-hold, but always be ready with the brake.")], ["hc"]),
 ("multi-storey-car-park-practice", "Multi-storey car parks for learners", "Ramps, tight bends and bays — how to handle city car parks.",
  """<p class="lead">Multi-storey car parks combine tight ramps, sharp bends, pedestrians and bay parking — all at low speed.</p>
<h2>Tips</h2><ul><li>Go very slowly up and down ramps; use clutch control in a manual.</li><li>Keep left on two-way ramps.</li><li>Expect pedestrians walking between cars.</li><li>Choose an end bay with space while you learn.</li></ul>
<h2>On the test</h2><p>You may be asked to bay park in a car park. We practise forward and reverse bay parking until you can do both reliably.</p>""",
  [("Is bay parking on the test?", "You may be asked to do one of several manoeuvres, including forward or reverse bay parking."), ("Do we practise in real car parks?", "Yes, once you're ready, at quiet times.")], ["hc"]),
 ("emergency-vehicles-what-to-do", "Emergency vehicles: what to do", "How to let an ambulance or fire engine through safely — without breaking the law.",
  """<p class="lead">When you hear sirens or see blue lights, stay calm. Look for where the vehicle is and what it wants to do.</p>
<h2>Do</h2><ul><li>Pull over to the left when it's safe and legal.</li><li>Keep your speed steady until you can let it pass.</li><li>Watch for more than one emergency vehicle.</li></ul>
<h2>Don't</h2><ul><li>Don't go through a red light or into a bus lane in hours.</li><li>Don't stop on a bend, a crest or a junction.</li><li>Don't panic-brake.</li></ul>""",
  [("Can I go through a red light for an ambulance?", "No — you could be fined. Wait for a safe, legal way to move over."), ("What if it happens on my test?", "Deal with it safely; examiners want to see calm, legal decisions.")], ["hc"]),
 ("e-scooters-and-cyclists-manchester", "Sharing the road with cyclists and e-scooters", "Overtaking distances, the Dutch reach and junction checks.",
  """<p class="lead">You'll share Manchester's roads with cyclists, delivery riders and e-scooters. The Highway Code's hierarchy of road users means drivers have the greatest responsibility to look out for them.</p>
<h2>Key rules</h2><ul><li>At least 1.5 metres when overtaking at up to 30 mph.</li><li>Check mirrors and blind spots before turning or opening a door.</li><li>The "Dutch reach" — open your door with the hand furthest from it so you turn and look.</li></ul>""",
  [("How much space for a cyclist?", "At least 1.5 metres at up to 30 mph."), ("What is the Dutch reach?", "Opening your door with your far hand so you naturally look behind for cyclists.")], ["hc"]),
 ("one-way-streets-city-centre", "One-way streets and contraflows in Manchester city centre", "No-entry signs, contraflow bus lanes and planning your route.",
  """<p class="lead">Manchester city centre has many one-way streets, some with contraflow bus or cycle lanes running the other way.</p>
<h2>How to read them</h2><ul><li>Blue rectangular one-way signs and white no-entry signs.</li><li>Contraflow lanes are marked — buses or bikes may come towards you.</li><li>Plan your route before you set off; sat-navs can be out of date.</li></ul>
<h2>Our approach</h2><p>We start city-centre lessons only when your basics are solid, and we build up street by street. See our <a href="../knowledge/manchester-city-centre-driving-guide.html">city-centre driving guide</a>.</p>""",
  [("Can I use a contraflow lane?", "Only if the signs allow your vehicle — usually they're for buses or cycles."), ("Is the city centre on the test?", "Cheetham Hill routes include some city-style driving, so we practise it.")], ["hc"]),
]


# register every page's group before any page is built, so slices are shared out evenly
for _s in SCHOOLS:
    _pick("s:" + _s[0], _s[3], _s[4])
for _w in WORK:
    _pick("w:" + _w[0], _w[3], _w[4])


def guide_page(g):
    slug, title, desc, body, faqs, src = g
    path = f"guides/{slug}.html"
    return shell(path, f"{title} | SQ Driving School", "Guide", [("Guides", "guides.html"), (title, path)], title + ".", desc,
                 [("Free", "guide"), ("Manchester", "focused"), ("£35", "per hour lessons"), ("Free", "Student Portal")],
                 [desc], body, faqs, [GOV[k] for k in src], [("driving-lessons-manchester.html", "Manchester", "Driving lessons in Manchester", "Prices, areas and the planner."), ("roads.html", "Roads", "Road guides", "The roads learners worry about."), ("guides.html", "Guides", "All learner guides", "Everything in one place.")],
                 side_title="Lessons in Manchester", booking_heading="Book a lesson in 60 seconds", active="knowledge.html", side_html=SIDE)


def work_hub():
    cards = [(f"work/{w[0]}.html", "Workplace", w[1], w[2], "users") for w in WORK]
    return hub_page("work.html", "Driving Lessons Around Your Job | Greater Manchester | SQ Driving", "Workplaces", "Driving lessons around your job.",
                    f"Lessons for people who work at {len(WORK)} of Greater Manchester's biggest workplaces — around shifts, with pick-up from work or home.", cards)


def all_pages():
    out = {f"students/{s[0]}.html": _school_shell(f"students/{s[0]}.html", s[1], s[2], s[4], _school_body(s), _school_faqs(s)) for s in SCHOOLS}
    out.update({f"work/{w[0]}.html": work_page(w) for w in WORK})
    out["work.html"] = work_hub()
    out.update({f"guides/{g[0]}.html": guide_page(g) for g in GUIDES})
    return out


def _school_body(s):
    slug, name, where, area, cs, kind, note = s
    sixth = kind != "college"
    return f"""<p class="lead">Driving lessons for students at {name} ({where}). {note}</p>
<h2>Learning to drive while you study</h2>
<ul><li><b>You can start at 17.</b> Apply for your provisional licence from 15 years 9 months so it's ready on your birthday.</li>
<li><b>Lessons around your timetable</b> — {"free periods, after school, weekends" if sixth else "gaps between classes, after college, weekends"} and holidays.</li>
</ul>
{_pick("s:" + slug, area, cs)}
<p>Local area: {area_link(area)} · usual test centre{"s" if len(cs) > 1 else ""}: {centre_html(cs)}. <b>10 hours £320</b> with a valid student ID (normally £350); £35/hr otherwise. <a href="../student-driving-lessons-manchester.html">Student discount →</a> · <a href="../knowledge/parents-guide-to-learner-drivers.html">Parents' guide →</a></p>
<p class="note">SQ Driving School isn't connected to {name}; we simply teach lots of students in the area.</p>"""


def _school_faqs(s):
    slug, name, where, area, cs, kind, note = s
    return [(f"Do you pick up from {name}?", "Yes — from school or college, home, or anywhere convenient that's safe to stop. Tell us when you book."),
            ("Is there a student discount?", "Yes: 10 hours for £320 (normally £350) with a valid student ID."),
            ("When can I start?", "From your 17th birthday with a provisional licence. You can apply up to 3 months before."),
            ("Which test centre should I use?", f"Most learners here use {', '.join(CBY[c]['name'] for c in cs if c in CBY)}. Pick the one you can practise around and get a date at.")]
