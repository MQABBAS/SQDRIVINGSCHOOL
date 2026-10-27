"""Solihull — SQ Driving School's first area outside Greater Manchester (lessons running, same prices).

Pillar page (driving-lessons-solihull.html) plus solihull/: area pages, lesson-type pages, test-centre route guides
(Shirley and the Birmingham centres Solihull learners book), a test-centre comparison and a data-led local guide.
Facts come from Census 2021, Solihull Council, National Highways/TfWM and passrates.uk's analysis of DVSA data;
route roads come from public route sheets (DVSA no longer publishes routes). No invented reviews or claims.
Each page is written around the phrases people actually search for, and links to the DriveSQ Solihull pages."""
from hub_shell import *

DSQ = "https://www.drivesq.co.uk/"
DSQ_PAGES = [
    (DSQ + "driving-lessons-solihull.html", "DriveSQ", "Book driving lessons in Solihull with DriveSQ", "£35/hr manual or auto, plus the free Student Portal: progress tracking, 700+ theory questions and 14 mock tests."),
    (DSQ + "free-learner-driver-resources-solihull.html", "DriveSQ", "Free learner driver resources", "The Student Portal, 11 free tools and official guides in one place."),
    (DSQ + "solihull-driving-schools-compared.html", "DriveSQ", "Solihull driving schools compared", "What 12 Solihull schools publish — and which have a student portal."),
    (DSQ + "solihull-driving-school.html", "DriveSQ", "DriveSQ driving school in Solihull", "Meet the DriveSQ Solihull team, the Student Portal and how lessons work."),
    (DSQ + "solihull-driving-test-pass-rates.html", "DriveSQ data", "Solihull driving test pass rates 2026", "Every test centre near Solihull ranked, with what the numbers mean."),
    (DSQ + "driving-instructor-jobs-solihull.html", "Careers", "Driving instructor jobs in Solihull", "Teach with DriveSQ: pupils matched by postcode, Instructor Portal."),
    (DSQ + "solihull-driving-test-centre-finder.html", "DriveSQ tool", "Solihull test centre finder", "Your postcode → the best of the 7 centres by distance and pass rate."),
    (DSQ + "solihull-learner-driver-cost-calculator.html", "DriveSQ tool", "Full licence cost calculator", "Provisional, lessons, tests, retakes and insurance — added up."),
    (DSQ + "solihull-learner-driver-lesson-plan.html", "DriveSQ tool", "Week-by-week lesson plan", "From quiet estates to the M42, with a test-ready date."),
    (DSQ + "solihull-driving-test-readiness-check.html", "DriveSQ tool", "Am I ready for my test?", "A 15-question self-check built around Solihull's test routes."),
    (DSQ + "solihull-daylight-driving-planner.html", "DriveSQ tool", "Daylight & sun-glare planner", "Sunrise, sunset and dazzle times in Solihull for any date."),
    (DSQ + "solihull.html", "DriveSQ", "Every DriveSQ Solihull tool & guide", "Parents' guide, theory test, new drivers and instructor training."),
]
# every DriveSQ Solihull page — listed on the SQ Solihull directory so the two sites link page to page
DSQ_ALL = [(DSQ + f, "DriveSQ", t, "") for f, t in [
    ("driving-lessons-solihull.html", "Driving lessons in Solihull (DriveSQ)"), ("free-learner-driver-resources-solihull.html", "Free learner resources"),
    ("solihull-driving-schools-compared.html", "Solihull driving schools compared"), ("learner-driver-age-checker.html", "When can I start driving?"),
    ("driving-test-fault-counter.html", "Would I have passed?"), ("passing-distance-guide.html", "Passing distance guide"),
    ("which-lights-should-i-use.html", "Which lights should I use?"), ("cockpit-drill-checklist.html", "Cockpit drill checklist"),
    ("manual-or-automatic-decider.html", "Manual or automatic?"),
    ("solihull.html", "Every DriveSQ Solihull tool & guide"), ("solihull-driving-school.html", "DriveSQ driving school Solihull"),
    ("driving-instructors-solihull.html", "Driving instructors Solihull"), ("solihull-driving-test-pass-rates.html", "Solihull driving test pass rates"),
    ("solihull-driving-test-centre-finder.html", "Test centre finder"), ("solihull-learner-driver-cost-calculator.html", "Licence cost calculator"),
    ("solihull-daylight-driving-planner.html", "Daylight & sun-glare planner"), ("solihull-driving-test-readiness-check.html", "Test readiness check"),
    ("solihull-learner-driver-lesson-plan.html", "Week-by-week lesson plan"), ("solihull-parents-guide-learner-drivers.html", "Parents' guide"),
    ("solihull-new-drivers-first-year.html", "First year after passing"), ("solihull-theory-test-guide.html", "Theory test from Solihull"),
    ("solihull-learner-driver-insurance.html", "Learner driver insurance"), ("driving-instructor-training-solihull.html", "Become a driving instructor"),
    ("driving-instructor-jobs-solihull.html", "Driving instructor jobs Solihull")]]
SRC = {
    "pr_shirley": ("passrates.uk — Birmingham (Shirley) test centre, 2024-25", "https://passrates.uk/centres/birmingham-shirley"),
    "pr_bham": ("passrates.uk — Birmingham test centres pass rates", "https://passrates.uk/guide/birmingham-driving-test-centres-pass-rates"),
    "pr_gg": ("passrates.uk — Birmingham (Garretts Green), 2024-25", "https://passrates.uk/centres/birmingham-garretts-green"),
    "pr_sy": ("passrates.uk — Birmingham (South Yardley), 2024-25", "https://passrates.uk/centres/birmingham-south-yardley"),
    "pr_kh": ("passrates.uk — Birmingham (Kings Heath), 2024-25", "https://passrates.uk/centres/birmingham-kings-heath"),
    "pr_cov": ("passrates.uk — Coventry, 2024-25", "https://passrates.uk/centres/coventry"),
    "pr_war": ("passrates.uk — Warwick (Wedgenock House), 2024-25", "https://passrates.uk/centres/warwick-wedgenock-house"),
    "pr_red": ("passrates.uk — Redditch, 2024-25", "https://passrates.uk/centres/redditch"),
    "pr_nat": ("passrates.uk — UK driving test pass rate 2024-25", "https://passrates.uk/guide/driving-test-pass-rate-2024-2025"),
    "dvsa": ("DVSA — Car driving test data by test centre (DVSA1203)", "https://www.gov.uk/government/statistical-data-sets/car-driving-test-data-by-test-centre"),
    "find": ("GOV.UK — Find a driving test centre", "https://www.gov.uk/find-driving-test-centre"),
    "book": ("GOV.UK — Book your driving test", "https://www.gov.uk/book-driving-test"),
    "census": ("ONS — How Solihull has changed (Census 2021)", "https://www.ons.gov.uk/visualisations/censusareachanges/E08000029/"),
    "story": ("Solihull Council — The Story of Solihull 2023", "https://www.solihull.gov.uk/sites/default/files/2023-09/Story-of-Solihull-2023.pdf"),
    "ons_cars": ("ONS — Housing, England and Wales: Census 2021 (car availability)", "https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021"),
    "speed": ("Solihull Council — speed limit policy review", "https://www.solihull.gov.uk/news/solihull-speed-limit-policy-set-review"),
    "safety": ("Solihull Council — Road safety strategies", "https://www.solihull.gov.uk/about-council/road-safety-strategies"),
    "caz": ("Solihull Council — Birmingham Clean Air Zone", "https://www.solihull.gov.uk/news/birmingham-clean-air-zone"),
    "brum": ("Brum Breathes — Clean Air Zone charges", "https://www.brumbreathes.co.uk/info/32/charges-operation/35/clean-air-zone-charging-order"),
    "m42": ("National Highways — M42 junction 6 improvement", "https://nationalhighways.co.uk/m42j6/"),
    "tfwm": ("TfWM — Interchange and M42 J6 works", "https://www.tfwm.org.uk/plan-your-journey/major-roadworks-and-events/interchange-m42-j6/"),
    "theory_close": ("GOV.UK — Solihull theory test centre to close (2011)", "https://www.gov.uk/government/news/solihull-theory-test-centre-to-close"),
    "motorway": ("GOV.UK — Learner drivers on motorways", "https://www.gov.uk/government/news/learner-drivers-will-be-allowed-on-motorways-from-2018"),
    "college": ("Solihull College & University Centre — campuses", "https://www.solihull.ac.uk/about-us/our-campuses/"),
    "jlr": ("JLR — where we are (Solihull)", "https://careers.jaguarlandrover.com/where-we-are/united-kingdom"),
    "lessons": ("GOV.UK — Driving lessons and learning to drive", "https://www.gov.uk/driving-lessons-learning-to-drive"),
    "cost": ("GOV.UK — Driving test cost", "https://www.gov.uk/driving-test-cost"),
}
NAT = 48.7
SIDE = (f'<p>£35/hr manual or automatic · 2 hours £70 · 10 hours £350 (£320 for NHS staff and students) · free DriveSQ Student Portal · door-to-door pick-up across Solihull.</p>'
        f'<a class="btn btn--red btn--block" href="#book">{icon("calendar")} Book in 60 seconds</a>')
BOOK_H = "Book driving lessons in Solihull in 60 seconds"


def _x(pairs):
    return [(h, c, t, d) for h, c, t, d in pairs]


def _dsq_box():
    links = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a> — {d}</li>' for u, c, t, d in DSQ_PAGES)
    return f'<div class="rx-method" data-reveal="up"><h3>SQ Driving School is part of DriveSQ</h3><p>Lessons in Solihull are run by SQ Driving School and DriveSQ together — the same instructors, prices and Student Portal. More from DriveSQ:</p><ul>{links}</ul></div>'


PROMO = (f'<div class="callout" style="border-left:4px solid #D10A11"><b>Learning in Solihull?</b> Book with <a href="{DSQ}driving-lessons-solihull.html">DriveSQ</a> — £35/hr manual or automatic, '
         f'with the <a href="{DSQ}student.html">free DriveSQ Student Portal</a>: progress tracking, 700+ theory questions, 14 mock tests and instructor messaging. '
         f'Instructors get the free <a href="{DSQ}dashboard.html">Instructor Portal</a>.</div>')


def S(path, seo, cat, crumb, title, desc, stats, keys, body, faqs, src, related, root=ROOT, extra_schema=None, after=""):
    rel = list(related) + [(DSQ_PAGES[0][0], "DriveSQ", DSQ_PAGES[0][2], DSQ_PAGES[0][3])]
    crumbs = [("Solihull", "driving-lessons-solihull.html")] + ([crumb] if crumb else [])
    body = body.replace("</p>", "</p>" + PROMO, 1) if "</p>" in body else PROMO + body
    html = shell(path, seo, cat, crumbs, title, desc, stats, keys, body + _dsq_box(), faqs, [SRC[k] if isinstance(k, str) else k for k in src], rel,
                 side_title="Lessons in Solihull", portal_mode="wm", booking_heading=BOOK_H, active="areas.html", side_html=SIDE, root=root,
                 extra_schema=extra_schema, after_body=after)
    # external DriveSQ links in the related grid must not get ROOT prefixed
    return html.replace(f'href="{root}{DSQ}', f'href="{DSQ}').replace(f'href="../{DSQ}', f'href="{DSQ}')


def _biz(path, area, pcs):
    return [{"@context": "https://schema.org", "@type": "DrivingSchool", "name": f"SQ Driving School — {area}", "url": f"{SITE}/{path}", "telephone": "+44 7352 932003",
             "priceRange": "£35–£350", "parentOrganization": {"@type": "Organization", "name": "DriveSQ", "url": DSQ},
             "areaServed": [{"@type": "Place", "name": f"{area}, Solihull"}] + [{"@type": "Place", "name": p} for p in pcs],
             "makesOffer": [{"@type": "Offer", "name": "Single 1-hour driving lesson", "price": "40", "priceCurrency": "GBP"}, {"@type": "Offer", "name": "Driving lesson (2 hours or more), per hour", "price": "35", "priceCurrency": "GBP"}, {"@type": "Offer", "name": "10-hour block", "price": "350", "priceCurrency": "GBP"}]}]


# ============================================================ TEST CENTRES
CENTRES = [
    dict(slug="shirley", name="Shirley", full="Birmingham (Shirley)", pc="B90 4AA", address="401 Stratford Road (A34), Shirley, Solihull B90 4AA",
         rate=58.1, note="2024-25, about 9,600 tests", src="pr_shirley",
         who="Shirley, Monkspath, Dickens Heath, Cheswick Green, Hillfield, Solihull town centre, Olton, Knowle, Dorridge, Hockley Heath and Hall Green",
         intro="Shirley is the only DVSA car test centre inside the borough of Solihull — and in the 2024-25 test year it had the highest pass rate of any Birmingham-area centre, 58.1%, nearly ten points above the UK average. It sits on the A34 Stratford Road in Shirley, and almost every reported route spends time on that road.",
         area="Routes start with a service road onto the A34 and then mix the busy Stratford Road corridor with Monkspath's modern estates and roundabouts, residential Shirley, and the lanes towards Dickens Heath. Expect lots of roundabouts — large ones on the boulevards and mini-roundabouts in the estates.",
         roads=[("A34", "Stratford Road", "On 13 of 15 routes in one public route collection. Busy, with bus stops, frequent side roads, shops and roundabouts — mirrors and lane discipline all the way.", ("Bus stops", "Roundabouts", "Side roads")),
                ("", "Marshall Lake Road and Cranmore Road", "Reported early on routes — residential and industrial traffic near the A34.", ("Junctions",)),
                ("", "Cranmore Boulevard", "Consistently reported as a left at a roundabout. Wide boulevard where speed can creep up.", ("Roundabout", "Speed")),
                ("", "Monkspath Hall Road", "Usually an early left turn on reported routes, leading into Monkspath's estates.", ("Left turns", "Estates")),
                ("", "Dog Kennel Lane", "Appears as a roundabout exit or an end-of-road junction depending on the route.", ("Roundabout",)),
                ("", "Highlands Road", "A roundabout followed by a mini-roundabout — take each one separately.", ("Mini-roundabout",)),
                ("", "Dickens Heath Road and Tanworth Lane", "Lanes towards Dickens Heath and Hillfield: bends, changing speed limits and parked cars near the village.", ("Bends", "Speed changes")),
                ("", "Union Road and Shirley Park Road", "Reported as roundabout-heavy — signals and lane choice matter.", ("Roundabouts",)),
                ("", "Blackford Road, Bills Lane, Widney Lane and Haslucks Green Road", "Residential roads on reported routes — junction observations, parked cars and manoeuvres.", ("Parked cars", "Manoeuvres"))],
         spokes=[("Stratford Rd (A34)", "Hall Green / M42 J4"), ("Cranmore Blvd", "Monkspath"), ("Dog Kennel Ln", "Shirley"), ("Tanworth Ln", "Dickens Heath"), ("Haslucks Green Rd", "Shirley West"), ("Highlands Rd", "Shirley")],
         marks=[("Stratford Road shops", "Shirley's high street along the A34."), ("Blythe Valley Park", "At M42 junction 4, south of Shirley via the A34."), ("Monkspath", "Modern estates and boulevards east of the A34."), ("Dickens Heath", "Village reached by Dickens Heath Road."), ("Shirley station", "On the line from Birmingham towards Stratford.")],
         mistakes=[("Lane discipline on the A34", "Multi-lane approaches to roundabouts and lights along Stratford Road.", "Read lane arrows early and stay in your lane all the way through."),
                   ("Buses pulling out", "Bus stops line Stratford Road.", "Check mirrors, anticipate the bus indicating, and give way where it's safe."),
                   ("Speed on the boulevards", "Wide roads like Cranmore Boulevard tempt learners over the limit.", "Check every limit sign; wide road doesn't mean faster limit."),
                   ("Roundabout then mini-roundabout", "Treating Highlands Road's pair as one junction.", "Deal with each: look right, give way, signal if needed."),
                   ("Bends towards Dickens Heath", "Entering bends too fast on the lanes.", "Brake before the bend, steer through, gently accelerate out.")]),
    dict(slug="garretts-green", name="Garretts Green", full="Birmingham (Garretts Green)", pc="B33 0SD", address="Granby Avenue, Garretts Green, Birmingham B33 0SD",
         rate=42.0, note="2024-25, 21,871 tests", src="pr_gg",
         who="Chelmsley Wood, Kingshurst, Smith's Wood, Fordbridge, Castle Bromwich, Marston Green and nearby east Birmingham",
         intro="Garretts Green, on Granby Avenue in east Birmingham, is the busiest test centre in Birmingham — almost 22,000 car tests in 2024-25 — and the closest for many learners in north Solihull. Its pass rate, 42.0%, is well below the UK average. Learners from Chelmsley Wood, Kingshurst and Marston Green often book here, so this is where our north Solihull lessons focus.",
         area="Routes leave Granby Avenue for Garretts Green Lane and Meadway, then use Cooks Lane, Stechford Road and the fast A45 Coventry Road dual carriageway, with multi-lane roundabouts and some tight residential streets.",
         roads=[("", "Granby Avenue", "Start and finish of every test, through a business park — vans and lorries.", ("Moving off", "Large vehicles")),
                ("", "Garretts Green Lane", "Reached at a roundabout straight out of the centre.", ("Roundabout",)),
                ("", "Meadway", "Reported with a turn at traffic lights.", ("Traffic lights",)),
                ("", "Cooks Lane and Forth Drive", "Including a roundabout reported as 'left' and 'third right' on different routes — know where each exit goes.", ("Roundabout exits",)),
                ("", "Stechford Road / Stechford Lane", "Busy local road on reported routes.", ("Junctions",)),
                ("A45", "Coventry Road", "Fast dual carriageway towards the airport and Solihull — lane discipline, merging and speed.", ("Dual carriageway", "Merging"))],
         spokes=[("Granby Ave", "test centre"), ("Garretts Green Ln", "Sheldon"), ("Meadway", "Kitts Green"), ("Cooks Ln", "Kingshurst"), ("A45 Coventry Rd", "Airport / Solihull")],
         marks=[("Granby Business Park", "Where the centre is."), ("Lea Hall station", "Trains to Birmingham New Street."), ("Sheldon Country Park", "Next to Birmingham Airport."), ("A45 Coventry Road", "About 1.5 miles south.")],
         mistakes=[("Merging onto the A45", "Joining a fast dual carriageway too slowly.", "Use the whole slip road to match speed, check mirrors and blind spot, then merge."),
                   ("Roundabout exit counting on Cooks Lane", "Taking the wrong exit or the wrong lane.", "Count exits on the approach and choose your lane from the markings."),
                   ("Business-park traffic", "Vans and lorries on Granby Avenue at the start of the test.", "Give large vehicles extra time and space."),
                   ("Traffic lights on Meadway", "Late reaction to amber.", "Approach at a speed where stopping is easy.")]),
    dict(slug="south-yardley", name="South Yardley", full="Birmingham (South Yardley)", pc="B26 1EA", address="Clay Lane, South Yardley, Birmingham B26 1EA",
         rate=41.6, note="2024-25, 12,709 tests", src="pr_sy",
         who="Sheldon, Yardley, Acocks Green, Elmdon, Olton and west Solihull border areas",
         intro="South Yardley, on Clay Lane, is close to Solihull's western edge and had the lowest pass rate of the Birmingham centres in 2024-25 at 41.6%. Some Olton and Elmdon learners book it for an earlier date — this guide tells you what you'd be taking on.",
         area="Most routes start on Clay Lane and quickly reach the A45 Coventry Road, with fast dual-carriageway sections, then dense urban junctions around Yardley.",
         roads=[("", "Clay Lane", "Where most routes start.", ("Moving off",)),
                ("A45", "Coventry Road", "Fast dual-carriageway sections — lane changes and speed management.", ("Dual carriageway",)),
                ("", "Barrows Lane", "Reported on routes — residential junctions.", ("Junctions",)),
                ("", "Gilbertstone Avenue", "Reported on routes — residential with parked cars.", ("Parked cars",))],
         spokes=[("Clay Ln", "test centre"), ("A45 Coventry Rd", "Sheldon / Solihull"), ("Barrows Ln", "Yardley"), ("Gilbertstone Ave", "South Yardley")],
         marks=[("Swan Shopping Centre", "Yardley — a reported navigation point."), ("South Yardley Library", "Near the centre."), ("A45 Coventry Road", "Main road into Solihull and the airport.")],
         mistakes=[("Lane choice on the A45", "Ending in the wrong lane at junctions.", "Read gantry and lane signs early."),
                   ("Dense urban junctions", "Restricted views with parked cars.", "Creep and peep; look twice."),
                   ("Speed changes", "Missing a change of limit between dual carriageway and local roads.", "Watch for repeater signs and adjust before the change.")]),
    dict(slug="kings-heath", name="Kings Heath", full="Birmingham (Kings Heath)", pc="B14 5JA", address="955 Alcester Road South, Birmingham B14 5JA",
         rate=47.0, note="2024-25, 8,488 tests", src="pr_kh",
         who="Shirley West, Hall Green, Hollywood, Majors Green and Solihull's south-western edge",
         intro="Kings Heath test centre is on the A435 Alcester Road South near the Druids Lane roundabout. It's an alternative for learners on Solihull's south-western side. There's no on-site parking and no toilets — plan your warm-up lesson accordingly. Pass rate in 2024-25: 47.0%.",
         area="Expect fast multi-lane roundabouts such as Druids Lane and the Maypole, the Hollywood Bypass, Yardley Wood Road, and residential streets, with some country-road sections.",
         roads=[("A435", "Alcester Road South", "The centre's main road — busy, with shops and buses.", ("Buses", "Shops")),
                ("", "Druids Lane roundabout", "Fast and multi-lane, close to the centre.", ("Multi-lane roundabout",)),
                ("", "Maypole roundabout and Maypole Lane", "Another large roundabout on reported routes.", ("Roundabout",)),
                ("", "Hollywood Bypass", "Faster road towards Hollywood and Solihull's border.", ("Speed",)),
                ("", "Yardley Wood Road", "Long main road with side roads and parked cars.", ("Junctions",)),
                ("", "Walkers Heath Road, Packhorse Lane and May Lane", "Residential and semi-rural roads on reported routes.", ("Bends",))],
         spokes=[("Alcester Rd S (A435)", "Kings Heath"), ("Druids Ln", "Druids Heath"), ("Maypole Ln", "Maypole"), ("Hollywood Bypass", "Hollywood"), ("Yardley Wood Rd", "Yardley Wood")],
         marks=[("Druids Heath", "Next to the centre."), ("The Maypole", "Roundabout and local shops."), ("Cocks Moors Woods Leisure Centre", "Off Alcester Road.")],
         mistakes=[("Speed on approach to Druids Lane", "Arriving too fast to assess traffic.", "Slow early, look right early."),
                   ("Lane changes on multi-lane roundabouts", "Changing lanes mid-roundabout.", "Pick your lane on approach and keep it."),
                   ("Country-road bends", "Entering bends too fast.", "Slow before the bend.")]),
]
# Coventry, Warwick and Redditch — the centres south and east Solihull learners also book. Route roads are the ones
# reported on public route compilations (DVSA no longer publishes routes); kept to roads more than one source names.
CENTRES += [
    dict(slug="coventry", name="Coventry", full="Coventry", pc="CV7 9EJ", address="42 Bayton Road, Exhall, Coventry CV7 9EJ",
         rate=42.3, note="2024-25, about 9,100 tests", src="pr_cov",
         who="Balsall Common, Meriden, Berkswell, Hampton-in-Arden and the borough's eastern villages",
         intro="Coventry test centre is on Bayton Road in Exhall, on the northern edge of Coventry close to the M6 and the A444. For learners in Meriden, Berkswell and Balsall Common it can be nearer than the Birmingham centres — but its 42.3% pass rate in 2024-25 was well below the UK average, so it rewards proper preparation.",
         area="Reported routes leave Bayton Road's industrial estate and quickly reach busy roundabouts on the A444, then mix main roads like Foleshill Road with residential streets around Exhall and Longford.",
         roads=[("", "Bayton Road", "Start and finish of every test — an industrial estate with lorries and vans.", ("Moving off", "Large vehicles")),
                ("A444", "Phoenix Way / Holbrook bypass", "Fast dual carriageway with large roundabouts — the stretch most reported routes return to.", ("Dual carriageway", "Roundabouts")),
                ("", "Old Church Road", "Reported early on routes, with junctions and parked cars.", ("Junctions",)),
                ("", "Foleshill Road", "A busy main road with shops, buses and side roads.", ("Buses", "Side roads"))],
         spokes=[("Bayton Rd", "test centre"), ("A444", "Coventry / M6"), ("Old Church Rd", "Exhall"), ("Foleshill Rd", "Foleshill")],
         marks=[("M6 junction 3", "The motorway is very close to the centre."), ("Ricoh / Coventry Building Society Arena", "To the south, beside the A444."), ("Bayton Road industrial estate", "Where the centre is.")],
         mistakes=[("Roundabout exits on the A444", "Taking the wrong exit or lane at speed.", "Count exits on approach and choose your lane from the markings."),
                   ("Industrial-estate traffic", "Lorries reversing and pulling out on Bayton Road.", "Slow down, look well ahead and give large vehicles room."),
                   ("Busy main-road junctions", "Pulling out on Foleshill Road without a safe gap.", "Wait for a real gap; creep and peep where views are blocked.")]),
    dict(slug="warwick", name="Warwick", full="Warwick (Wedgenock House)", pc="CV34", address="Wedgenock House, Rothwell Road (off Wedgnock Lane), Warwick CV34",
         rate=48.4, note="2024-25, about 10,900 tests", src="pr_war",
         who="Knowle, Dorridge, Balsall Common and the southern villages",
         intro="Warwick's test centre, Wedgenock House, sits on Rothwell Road just off Wedgnock Lane on the north side of Warwick, close to the Warwick bypass. For learners in Knowle, Dorridge and Balsall Common it's a straight run down the A4141 — and in 2024-25 its pass rate was close to the UK average.",
         area="Reported routes use the residential estates around Woodloes and Hampton Magna, main roads like Birmingham Road into Warwick, and roundabouts near the bypass — plus narrow streets in the historic town centre.",
         roads=[("", "Wedgnock Lane & Rothwell Road", "Every test starts and ends here, on the edge of an industrial area.", ("Moving off",)),
                ("", "Birmingham Road", "Main road into Warwick, with junctions, crossings and changing limits.", ("Junctions", "Speed changes")),
                ("", "Budbrooke Road & Old Budbrooke Road", "Reported on routes towards Hampton Magna — bends and rural sections.", ("Bends", "Rural roads")),
                ("", "Blandford Way & Damson Road", "Residential roads on reported routes — parked cars and junctions.", ("Parked cars",)),
                ("", "Friars Street", "Town-centre street with pedestrians and tight junctions.", ("Pedestrians", "Town centre"))],
         spokes=[("Wedgnock Ln", "test centre"), ("Birmingham Rd", "Warwick"), ("Budbrooke Rd", "Hampton Magna"), ("Friars St", "town centre")],
         marks=[("Warwick Castle", "In the town centre — narrow historic streets nearby."), ("Warwick bypass (A46)", "Close to the centre."), ("Hampton Magna", "A village on reported routes.")],
         mistakes=[("Rural bends", "Entering bends towards Hampton Magna too fast.", "Brake before the bend, steer smoothly, accelerate gently out."),
                   ("Town-centre streets", "Pedestrians and tight junctions near Friars Street.", "Keep speed down and look well ahead."),
                   ("Changing limits", "Missing a change on Birmingham Road.", "Watch for every sign and repeater.")]),
    dict(slug="redditch", name="Redditch", full="Redditch", pc="B97 6HJ", address="Elm Road, Redditch B97 6HJ",
         rate=46.7, note="2024-25, about 4,700 tests", src="pr_red",
         who="Hockley Heath, Earlswood, Tidbury Green and Tanworth-in-Arden",
         intro="Redditch test centre is on Elm Road, just north of the town centre. It's a smaller centre — about 4,700 car tests in 2024-25 — and an option for learners on Solihull's southern edge around Hockley Heath and Tidbury Green. Redditch is known for its network of roundabouts and its ring road.",
         area="Reported routes go from Elm Road onto Hewell Road and the Ringway, then use the town's fast 'highway' roads such as the Alvechurch Highway, plenty of roundabouts, and residential roads like Throckmorton Road and Walkwood Road.",
         roads=[("", "Elm Road", "Where every test starts and ends.", ("Moving off",)),
                ("", "Hewell Road", "Main road from the centre towards the town — junctions and traffic lights.", ("Junctions",)),
                ("", "Ringway", "Redditch's ring road around the town centre — lane choice at every junction.", ("Ring road", "Lane choice")),
                ("", "Alvechurch Highway", "One of Redditch's fast highways — merging and higher speeds.", ("Higher speed", "Merging")),
                ("", "Throckmorton Road & Walkwood Road", "Residential distributor roads with roundabouts.", ("Roundabouts",))],
         spokes=[("Elm Rd", "test centre"), ("Hewell Rd", "town centre"), ("Ringway", "ring road"), ("Alvechurch Hwy", "north")],
         marks=[("Kingfisher Shopping Centre", "Inside the Ringway."), ("Redditch station", "Close to the town centre."), ("Arrow Valley Country Park", "To the east of the town.")],
         mistakes=[("Roundabout after roundabout", "Losing track of lane and signal on Redditch's roundabout network.", "Treat each roundabout separately; pick your lane on approach."),
                   ("Joining the highways", "Merging too slowly onto the fast highway roads.", "Use the slip road to build speed and check your blind spot."),
                   ("Ringway lane choice", "Ending in the wrong lane on the ring road.", "Read the signs early and move across in good time.")]),
]
OTHER = []


def centre_page(c):
    path = f"solihull/{c['slug']}-driving-test-centre-routes.html"
    diff = c["rate"] - NAT
    body = f"""
<p class="lead">{c['intro']}</p>
<div class="callout callout--info"><b>Address:</b> {c['address']}. Always check your booking confirmation and GOV.UK before you travel.</div>
<h2>{c['name']} driving test centre pass rate</h2>
<div class="rt-pass" data-reveal="up"><div class="rx-gauge-num" data-count="{c['rate']}" data-suffix="%">{c['rate']}%</div><div><p class="mb-0"><b>{c['full']} car pass rate</b> — {c['note']}.</p><p class="note mb-0">{abs(diff):.1f} points {'above' if diff > 0 else 'below'} the UK average of {NAT}% for the same year. Source: <a href="{SRC[c['src']][1]}" target="_blank" rel="noopener">{SRC[c['src']][0]}</a>. Official figures: DVSA1203.</p></div></div>
<h2>{c['name']} driving test routes: the roads</h2>
<p>{c['area']}</p>
{radial_map(c['name'], c['spokes'])}
<p class="note">The DVSA no longer publishes test routes and examiners vary them. These roads are the ones reported most often on public route sheets for {c['full']}, cross-checked between sources.</p>
{''.join(road(*r) for r in c['roads'])}
<h2>Landmarks near {c['name']} test centre</h2>
{landmarks(c['marks'])}
<h2>Common mistakes at {c['name']}</h2>
{mistakes(c['mistakes'])}
<h2>Who tests at {c['name']}?</h2>
<p>Solihull learners from {c['who']} commonly book here. You can book any centre, but since June 2026 a booked test can only move to one of the three centres nearest it. Compare every option in our <a href="solihull-driving-test-centres-compared.html">Solihull test centres comparison</a>.</p>
<h2>Other test centres near Solihull</h2>
<div class="hero__badges">{''.join(f'<a class="chip" href="{x["slug"]}-driving-test-centre-routes.html">{x["name"]} ({x["rate"]}%)</a>' for x in CENTRES if x["slug"] != c["slug"])}<a class="chip" href="solihull-driving-test-centres-compared.html">Compare all</a><a class="chip" href="https://www.drivesq.co.uk/solihull-driving-test-centre-finder.html">Find yours by postcode</a></div>
<h2>How we prepare you for {c['name']}</h2>
<ol class="rx-steps"><li data-n="1"><h4>Road types first</h4><p>Roundabouts, dual carriageways and busy high streets on quieter Solihull roads.</p></li>
<li data-n="2"><h4>The roads around {c['name']}</h4><p>In the final weeks we drive the roads above, at the time of day of your test.</p></li>
<li data-n="3"><h4>Mock test</h4><p>Marked like the DVSA sheet and logged in your DriveSQ Student Portal.</p></li>
<li data-n="4"><h4>Warm-up on the day</h4><p>A lesson that ends at the test centre.</p></li></ol>"""
    faqs = [(f"Where is {c['name']} driving test centre?", c["address"] + "."),
            (f"What is the pass rate at {c['name']} driving test centre?", f"{c['rate']}% in {c['note']}, against a UK average of {NAT}%."),
            (f"What roads are on {c['name']} driving test routes?", "Commonly reported roads include " + ", ".join(r[1] for r in c["roads"][:4]) + ". Routes aren't published and examiners vary them."),
            (f"Do you offer lessons for a test at {c['name']}?", "Yes. SQ Driving School (part of DriveSQ) teaches across Solihull and practises the roads around the centre before your test.")]
    sch = [{"@context": "https://schema.org", "@type": "Place", "name": f"{c['full']} driving test centre (DVSA)", "address": {"@type": "PostalAddress", "streetAddress": c["address"].rsplit(",", 1)[0], "postalCode": c["pc"], "addressCountry": "GB"}}]
    rel = [("solihull/solihull-driving-test-centres-compared.html", "Compare", "Solihull test centres compared", "Pass rates and which centre suits your postcode."),
           ("driving/driving-test-day-planner.html", "Planner", "Test day planner", "Light, traffic and a timetable for your test day.")]
    return S(path, f"{c['name']} Driving Test Centre Routes & Pass Rate ({c['rate']}%) | Solihull", "Test centre", (f"{c['name']} test centre", path),
             f"{c['name']} driving test centre: routes, roads and pass rate", f"{c['full']} driving test centre ({c['pc']}): reported test-route roads, roundabouts, landmarks, the {c['rate']}% pass rate and the mistakes to avoid — for Solihull learners.",
             [(f"{c['rate']}%", "pass rate"), (c["pc"], "postcode"), (str(len(c["roads"])), "roads profiled"), (str(len(c["mistakes"])), "mistakes to avoid")],
             [f"{c['full']}: {c['address']}.", f"Pass rate {c['rate']}% ({c['note']}).", f"Reported routes use {c['roads'][0][1]} and {c['roads'][1][1]}.", "Routes aren't published — prepare for the road types."],
             body, faqs, [c["src"], "pr_nat", "dvsa", "find", "book"], rel, extra_schema=sch, after=feedback_form(c["name"]))


def compare_page():
    path = "solihull/solihull-driving-test-centres-compared.html"
    rows = [(c["full"], c["address"].split(",")[-1].strip(), c["rate"], c["src"], c["who"], f'{c["slug"]}-driving-test-centre-routes.html') for c in CENTRES] + [(n, a, r, s, w, "") for n, a, r, s, w in OTHER]
    rows.sort(key=lambda x: -x[2])
    tr = "".join(f'<tr><td>{f"<a href={chr(34)}{h}{chr(34)}>{n}</a>" if h else n}</td><td class="mono">{a}</td><td class="mono"><b>{r}%</b></td><td>{w}</td></tr>' for n, a, r, s, w, h in rows)
    bars = RS._bars([(n.replace("Birmingham ", ""), "", r, "rx-bar__fill--green" if r >= NAT else "") for n, a, r, s, w, h in rows] + [("UK average", "2024-25", NAT, "rx-bar__fill--grey")], "%", 70)
    body = f"""
<p class="lead">Solihull has one driving test centre of its own — Shirley — but learners here regularly book six or seven others. Which one you choose changes the roads you're tested on, and the pass rates differ by more than 16 points. Here is every centre a Solihull learner realistically uses, ranked.</p>
{bars}
<div class="rx-table-wrap" data-reveal="up"><table class="rx-table"><thead><tr><th>Centre</th><th>Location</th><th>Pass rate 2024-25</th><th>Handy for</th></tr></thead><tbody>{tr}</tbody></table></div>
<p class="note">Pass rates: passrates.uk's analysis of DVSA data for 2024-25. UK average {NAT}%.</p>
<h2>Which test centre is closest to my Solihull postcode?</h2>
<ul><li><b>B90 (Shirley, Monkspath, Dickens Heath, Cheswick Green)</b> — <a href="shirley-driving-test-centre-routes.html">Shirley</a> is on your doorstep.</li>
<li><b>B91 (Solihull town centre)</b> — Shirley is closest; South Yardley is an alternative.</li>
<li><b>B92 (Olton, Elmdon)</b> — Shirley or <a href="south-yardley-driving-test-centre-routes.html">South Yardley</a>.</li>
<li><b>B93 (Knowle, Dorridge, Bentley Heath)</b> — Shirley, or Warwick for a date.</li>
<li><b>B94 (Hockley Heath)</b> — Shirley or Redditch.</li>
<li><b>B36 / B37 (Chelmsley Wood, Kingshurst, Smith's Wood, Castle Bromwich, Marston Green)</b> — <a href="garretts-green-driving-test-centre-routes.html">Garretts Green</a> is usually nearest.</li>
<li><b>CV7 (Balsall Common, Meriden)</b> — Coventry or Warwick, or Shirley.</li></ul>
<h2>Should you chase the highest pass rate?</h2>
<p>Shirley's 58.1% is the best in the area, and if you live in south Solihull it's also your nearest centre — ideal. But driving across the borough to a centre whose roads you've never practised usually cancels out a pass-rate advantage. Our <a href="{ROOT}research/driving-test-pass-rates-explained-manchester.html">pass-rate study</a> shows how to read these numbers properly.</p>
<h2>Theory test centres for Solihull</h2>
<p>Solihull's own theory test centre closed on 31 August 2011. Learners now usually take the theory test in Birmingham city centre or Coventry — check the address on your booking.</p>"""
    faqs = [("Which driving test centre is in Solihull?", "Birmingham (Shirley), at 401 Stratford Road, Shirley B90 4AA — the only DVSA car test centre inside Solihull borough."),
            ("Which test centre near Solihull has the highest pass rate?", "Shirley, with 58.1% in 2024-25 — the highest of the Birmingham-area centres."),
            ("Where do north Solihull learners take their test?", "Usually Garretts Green (B33 0SD), the nearest centre to Chelmsley Wood, Kingshurst and Marston Green."),
            ("Is there a theory test centre in Solihull?", "No. It closed in 2011; learners use Birmingham or Coventry.")]
    return S(path, "Solihull Driving Test Centres Compared: Pass Rates 2026 | SQ Driving School", "Test centres", ("Test centres compared", path),
             "Solihull driving test centres compared", "Every driving test centre Solihull learners use — Shirley, Garretts Green, South Yardley, Kings Heath, Coventry, Warwick, Redditch — with pass rates and which suits your postcode.",
             [("58.1%", "Shirley — highest"), ("7", "centres compared"), ("16+ pts", "pass-rate spread"), ("B90", "Shirley postcode")],
             ["Shirley is Solihull's only test centre and had the highest pass rate nearby (58.1%).", "North Solihull learners usually book Garretts Green.", "Pick the centre whose roads you can practise.", "Solihull's theory test centre closed in 2011."],
             body, faqs, ["pr_bham", "pr_shirley", "pr_gg", "pr_sy", "pr_kh", "pr_cov", "pr_war", "pr_red", "pr_nat", "theory_close"],
             [("solihull/shirley-driving-test-centre-routes.html", "Test routes", "Shirley test routes", "Roads, roundabouts and mistakes."), ("solihull/garretts-green-driving-test-centre-routes.html", "Test routes", "Garretts Green test routes", "For north Solihull learners.")])


# ============================================================ AREAS
AREAS = [
    dict(slug="shirley", name="Shirley", pcs=["B90"], centre="shirley",
         intro="Shirley is where the borough's driving test centre is — on the A34 Stratford Road — so learning here means practising on test-route roads from your very first lessons.",
         local="The A34 Stratford Road runs through the heart of Shirley with its shops, bus stops and side roads. Off it you'll find quiet residential streets for early lessons, and the roundabouts of Monkspath and Cranmore Boulevard for later ones.",
         roads=["Stratford Road (A34)", "Haslucks Green Road", "Tanworth Lane", "Bills Lane", "Blackford Road"],
         near=["Shirley station", "Stratford Road shops", "Blythe Valley Park (M42 J4)"],
         angle="Because the test centre is in Shirley, most of our Shirley learners book Shirley test centre — the area's highest pass rate in 2024-25."),
    dict(slug="solihull-town-centre", name="Solihull town centre", pcs=["B91"], centre="shirley",
         intro="Learning to drive in Solihull town centre means Touchwood, the High Street, Warwick Road and some of the busiest junctions in the borough — great practice once the basics are solid.",
         local="Early lessons start on the quieter residential roads around the town centre; later we tackle the Warwick Road (A41), Lode Lane and the junctions around Touchwood and Solihull station.",
         roads=["Warwick Road (A41)", "Lode Lane", "Blossomfield Road", "Widney Manor Road", "Homer Road"],
         near=["Touchwood shopping centre (opened 2001)", "Solihull station", "Solihull College Blossomfield campus", "Solihull Sixth Form College", "Solihull Hospital, Lode Lane"],
         angle="Town-centre learners usually test at Shirley, about ten minutes away."),
    dict(slug="olton", name="Olton", pcs=["B92"], centre="shirley",
         intro="Olton sits between Solihull town centre and Acocks Green, with the Warwick Road (A41) running through it and the JLR Solihull plant on Lode Lane nearby.",
         local="Olton's tree-lined residential roads suit first lessons; the A41 Warwick Road and Lode Lane give busy main-road practice, and shift-change traffic around the JLR plant is real-world anticipation training.",
         roads=["Warwick Road (A41)", "Lode Lane", "Kineton Green Road"],
         near=["Olton station", "JLR Solihull plant (Lode Lane)", "Olton Mere"],
         angle="Olton learners usually test at Shirley; South Yardley is an alternative for an earlier date."),
    dict(slug="knowle", name="Knowle", pcs=["B93"], centre="shirley",
         intro="Knowle is a historic village in south Solihull. Its High Street is busy and narrow, and the roads around it mix village streets with faster rural lanes.",
         local="We use Knowle's quieter residential roads for early lessons, then the village centre for parked-car clearance and pedestrian awareness, and the surrounding lanes for bends and national speed limits.",
         roads=["Warwick Road (A4141) / High Street — 20mph", "Station Road", "Kenilworth Road", "Lodge Road"],
         near=["Knowle village High Street", "Dorridge station (nearby)", "M42 junctions 4 and 5"],
         angle="Knowle learners usually test at Shirley; Warwick is an alternative."),
    dict(slug="dorridge", name="Dorridge", pcs=["B93"], centre="shirley",
         intro="Dorridge, next to Knowle and Bentley Heath, is a quiet commuter village with a station on the Chiltern line — perfect for calm first lessons.",
         local="Wide residential roads and gentle traffic make Dorridge one of the best places in Solihull for a nervous beginner. We progress to Knowle's village centre and the lanes towards Hockley Heath.",
         roads=["Four Ashes Road", "Mill Lane", "Widney Road", "Station Road"],
         near=["Dorridge station (opened 1852)", "Drum & Monkey, Four Ashes Road", "Bentley Heath"],
         angle="Dorridge learners usually test at Shirley."),
    dict(slug="chelmsley-wood", name="Chelmsley Wood", pcs=["B37", "B36"], centre="garretts-green",
         intro="Chelmsley Wood in north Solihull has its own town centre, and is minutes from Birmingham Airport, the NEC and the M6 and M42. Garretts Green is usually the nearest test centre.",
         local="Estates with mini-roundabouts and parked cars make great early practice. Later lessons use the faster roads towards the A45, the M6 and the M42 — the same kind of roads you'll meet on a Garretts Green test.",
         roads=["Chester Road (A452)", "Moorend Avenue", "Chelmsley Road", "Coleshill Heath Road"],
         near=["Chelmsley Wood shopping centre and bus interchange", "Solihull College Woodlands campus (Smith's Wood)", "Marston Green station"],
         angle="Chelmsley Wood learners usually test at Garretts Green — we focus lessons on its roads."),
    dict(slug="castle-bromwich", name="Castle Bromwich", pcs=["B36"], centre="garretts-green",
         intro="Castle Bromwich, on the north-west edge of the borough, is close to the M6 and the A452 Chester Road — busy roads that make confident drivers.",
         local="Quiet residential streets for the basics, then the A452 Chester Road dual carriageway and the junctions near the M6 for faster, multi-lane driving.",
         roads=["Chester Road (A452)", "Bradford Road (B4114)", "Hall Road"],
         near=["Castle Bromwich Hall Gardens", "St Mary & St Margaret church (Grade I)", "Bradford Arms"],
         angle="Castle Bromwich learners usually book Garretts Green."),
    dict(slug="kingshurst-smiths-wood", name="Kingshurst and Smith's Wood", pcs=["B36", "B37"], centre="garretts-green",
         intro="Kingshurst, Smith's Wood and Fordbridge sit between Castle Bromwich and Chelmsley Wood. Solihull College's Woodlands campus is in Smith's Wood, so many of our learners here are students.",
         local="Estate roads with mini-roundabouts and parked cars are ideal for clutch control and junction observation; we move on to Chester Road and Cooks Lane — which also appears on Garretts Green routes.",
         roads=["Cooks Lane", "Chester Road (A452)", "Windward Way", "Auckland Drive"],
         near=["Solihull College Woodlands campus (Auckland Drive)", "Kingshurst village centre", "Chelmsley Wood Shopping Centre"],
         angle="Learners here usually test at Garretts Green — Cooks Lane is on its reported routes."),
    dict(slug="marston-green", name="Marston Green", pcs=["B37"], centre="garretts-green",
         intro="Marston Green is a village beside Birmingham Airport and the NEC, with its own station. Airport and NEC traffic makes for great hazard-awareness practice.",
         local="Quiet village roads first, then the routes towards the A45, the airport and the NEC — taxis, coaches and drivers who don't know where they're going.",
         roads=["Station Road", "Elmdon Road", "Holly Lane", "Chester Road (A452)"],
         near=["Marston Green station", "Birmingham Airport", "NEC and Resorts World"],
         angle="Marston Green learners usually test at Garretts Green."),
    dict(slug="dickens-heath", name="Dickens Heath", pcs=["B90"], centre="shirley",
         intro="Dickens Heath is a modern village south of Shirley. Dickens Heath Road itself appears on reported Shirley test routes.",
         local="New-build streets, a village centre with parking and crossings, and the lanes towards Shirley and Tidbury Green — bends, changing limits and cyclists.",
         roads=["Dickens Heath Road", "Tythe Barn Lane", "Tanworth Lane"],
         near=["Dickens Heath village centre", "Whitlock's End station", "Shirley (nearby)"],
         angle="Dickens Heath learners test at Shirley — you'll already know some of its roads."),
    dict(slug="monkspath", name="Monkspath", pcs=["B90"], centre="shirley",
         intro="Monkspath, east of Shirley's A34, is a large modern estate with wide boulevards and roundabouts — Monkspath Hall Road and Cranmore Boulevard both appear on Shirley test routes.",
         local="Monkspath is almost a training ground for the Shirley test: roundabouts, boulevards, estate junctions and Blythe Valley Park at M42 junction 4.",
         roads=["Monkspath Hall Road", "Cranmore Boulevard", "Stratford Road (A34)"],
         near=["Blythe Valley Park", "Cranmore Boulevard", "M42 junction 4"],
         angle="Monkspath learners test at Shirley, a few minutes away."),
    dict(slug="balsall-common", name="Balsall Common", pcs=["CV7"], centre=None,
         intro="Balsall Common is Solihull's rural south-east, near Berkswell, Kenilworth and Coventry. Country lanes, the A452 and village traffic make it a different kind of learning.",
         local="Rural lanes teach bends, national speed limits, cyclists and horse riders; the A452 Kenilworth Road gives faster main-road driving. For towns, we head to Solihull or Coventry.",
         roads=["Kenilworth Road (A452) — HS2 contraflow to Aug 2027", "Station Road", "Kelsey Lane"],
         near=["Berkswell station", "Balsall Common village centre", "Coventry (nearby)"],
         angle="Balsall Common learners choose between Shirley, Coventry and Warwick — see our comparison."),
    dict(slug="hockley-heath", name="Hockley Heath", pcs=["B94"], centre="shirley",
         intro="Hockley Heath is a village on the Stratford Road south of the M42, surrounded by country lanes.",
         local="The Stratford Road through the village, the approach to M42 junction 4 and country lanes towards Earlswood and Lapworth cover almost every type of road on the test.",
         roads=["Stratford Road through the village", "B4439 towards Lapworth", "Box Trees Road (40mph)"],
         near=["Stratford-upon-Avon Canal (Bridge 25)", "M42 junction 4", "Blythe Valley Park"],
         angle="Hockley Heath learners usually test at Shirley; Redditch is an alternative."),
    dict(slug="meriden", name="Meriden", pcs=["CV7"], centre=None,
         intro="Meriden, between Solihull and Coventry, is a village known for its 'centre of England' marker on the green. It's surrounded by fast roads and lanes.",
         local="Village roads for the basics, then country lanes and the faster roads towards the A45 — ideal for building speed judgement.",
         roads=["London Road", "Fillongley Road", "A45 (Meriden bypass, 1958)"],
         near=["Centre-of-England cross on the village green", "A45 dual carriageway", "Coventry (nearby)"],
         angle="Meriden learners often test at Coventry or Shirley."),
]


def area_page(a):
    path = f"solihull/driving-lessons-{a['slug']}.html"
    n = a["name"]
    c = next((x for x in CENTRES if x["slug"] == a["centre"]), None)
    roads = "".join(f"<li>{r}</li>" for r in a["roads"])
    near = landmarks([(x, f"Near {n}") for x in a["near"]])
    centre_html = (f'<p>{a["angle"]} Read our <a href="{c["slug"]}-driving-test-centre-routes.html">{c["name"]} test route guide</a> — {c["rate"]}% pass rate in 2024-25.</p>' if c
                   else f'<p>{a["angle"]} <a href="solihull-driving-test-centres-compared.html">Compare Solihull test centres</a>.</p>')
    body = f"""
<p class="lead">{a['intro']}</p>
<div class="rx-figs" data-stagger=".06"><div class="rx-fig" data-reveal="up"><b>£35</b><span>per hour, manual or automatic</span></div><div class="rx-fig" data-reveal="up"><b>£350</b><span>10-hour block (£320 NHS &amp; students)</span></div><div class="rx-fig" data-reveal="up"><b>{a.get('pop') or ' / '.join(a['pcs'])}</b><span>{a.get('pop_label') or 'postcodes covered'}</span></div><div class="rx-fig" data-reveal="up"><b>{c['rate'] if c else '—'}{'%' if c else ''}</b><span>{(c['name'] + ' test centre pass rate') if c else 'see comparison'}</span></div></div>
<h2>Driving lessons in {n}: where you'll learn</h2>
<p>{a['local']}</p>
{a.get('extra', '')}
<p>Roads we use around {n}:</p><ul>{roads}</ul>
<h2>Landmarks and pick-up points in {n}</h2>
<p>We pick you up from home, school, college or work — door to door. Popular spots:</p>
{near}
<h2>Your nearest driving test centre</h2>
{centre_html}
<h2>Manual and automatic lessons in {n}</h2>
<p>Both cost the same: £35 an hour, £70 for 2 hours, £350 for 10 hours. Automatic is popular with nervous learners and anyone who wants to pass faster — see <a href="automatic-driving-lessons-solihull.html">automatic driving lessons in Solihull</a>. In a hurry? Try an <a href="intensive-driving-courses-solihull.html">intensive course</a>.</p>
<h2>What makes SQ different in {n}</h2>
<ul class="check"><li>Free <a href="../student-portal.html">DriveSQ Student Portal</a>: 23 skills tracked after every lesson, theory practice and a test-readiness checklist — see exactly when you're ready for {(c or CENTRES[0])['name']}.</li><li>Instructors run their diaries in the DriveSQ Instructor Portal, so lesson times, progress notes and messages are always up to date.</li><li>Lessons planned around your test centre's real roads.</li><li>Mock test before your real one.</li><li>Same transparent prices as our Manchester learners — no hidden fees.</li></ul>"""
    faqs = [(f"How much are driving lessons in {n}?", "£35 an hour for manual or automatic, £70 for 2 hours, and £350 for 10 hours (£320 for NHS staff and students)."),
            (f"Do you offer automatic driving lessons in {n}?", "Yes — automatic and manual lessons are the same price."),
            (f"Which test centre is nearest to {n}?", (f"Usually {c['full']} ({c['address']})." if c else "Coventry, Warwick or Shirley, depending on where you live.")),
            (f"Do you pick up from home in {n}?", "Yes, door-to-door from home, school, college or work.")]
    rel = [("solihull/automatic-driving-lessons-solihull.html", "Lessons", "Automatic lessons in Solihull", "Same price as manual."),
           (f"solihull/{a['centre'] or 'shirley'}-driving-test-centre-routes.html", "Test routes", f"{(c or CENTRES[0])['name']} test routes", "Roads and mistakes to avoid.")]
    return S(path, f"Driving Lessons {n} | £35/hr Manual & Automatic | SQ Driving School", f"Solihull · {' / '.join(a['pcs'])}", (n, path),
             f"Driving lessons in {n}", f"Driving lessons in {n}, Solihull ({', '.join(a['pcs'])}) — manual and automatic from £35/hr, door-to-door pick-up, local test-route practice and the free DriveSQ Student Portal.",
             [("£35", "per hour"), (" / ".join(a["pcs"]), "postcodes"), ("Manual & auto", "same price"), ("Free", "Student Portal")],
             [f"Lessons across {n} from £35/hr, manual or automatic.", f"Roads like {a['roads'][0]} and {a['roads'][1]}.", (f"Nearest test centre: {c['name']} ({c['rate']}% pass rate)." if c else "Several test centres nearby — see the comparison."), "Door-to-door pick-up and free DriveSQ Student Portal."],
             body, faqs, ["census", "find", "book", "cost"], rel, extra_schema=_biz(path, n, a["pcs"]))


# ============================================================ LESSON TYPES
def lesson_pages():
    out = {}
    common_src = ["lessons", "cost", "book", "pr_shirley"]
    defs = [
        ("automatic-driving-lessons-solihull", "Automatic driving lessons in Solihull", "Automatic Driving Lessons Solihull | £35/hr | SQ Driving School",
         "Automatic driving lessons across Solihull — Shirley, Solihull, Knowle, Chelmsley Wood and more — at £35/hr, the same as manual.",
         """<p class="lead">Automatic driving lessons in Solihull cost exactly the same as manual with SQ: £35 an hour. No clutch, no stalling — just steering, observation and decision-making, which is what the test is really about.</p>
<h2>Why learners in Solihull choose automatic</h2>
<ul><li><b>Roundabouts.</b> Shirley's routes are full of them. Without a clutch, you can give every roundabout your full attention.</li><li><b>Stop-start traffic.</b> The A34, A41 and A45 at rush hour are much less tiring in an automatic.</li><li><b>Nerves.</b> Removing stalling removes one of the biggest worries.</li><li><b>Electric future.</b> Electric cars are automatic. More and more new drivers never need a manual.</li></ul>
<h2>The catch</h2><p>Pass in an automatic and your licence only covers automatics. If you'll need to drive a manual (some work vans, cheaper older cars), learn manual. Not sure? Read <a href="../guides/manual-vs-automatic.html">manual vs automatic</a>.</p>
<h2>How many hours?</h2><p>Many learners need fewer hours in an automatic than in a manual, but the DVSA's average of about 45 hours is a sensible planning figure. Use our <a href="../driving/learning-to-drive-timeline-planner.html">timeline planner</a>.</p>""",
         [("Is automatic more expensive in Solihull?", "Not with SQ — automatic and manual are both £35 an hour."), ("Can I take my test in an automatic at Shirley?", "Yes. Your licence will then cover automatic cars only.")]),
        ("intensive-driving-courses-solihull", "Intensive driving courses in Solihull", "Intensive Driving Courses Solihull | Pass Faster | SQ Driving School",
         "Intensive and semi-intensive driving courses in Solihull — several hours a week, planned around a test at Shirley, Garretts Green or nearby.",
         """<p class="lead">An intensive driving course in Solihull packs your lessons into a few weeks instead of months. The hours are the same; the gaps between them shrink — so you spend less time relearning.</p>
<h2>How our Solihull intensive courses work</h2>
<ol class="rx-steps"><li data-n="1"><h4>Assessment</h4><p>A first lesson to see where you are.</p></li><li data-n="2"><h4>A plan around a test date</h4><p>Ideally at Shirley (58.1% pass rate in 2024-25). We'll help you find a date.</p></li><li data-n="3"><h4>Several lessons a week</h4><p>Usually 2-hour lessons, several days a week.</p></li><li data-n="4"><h4>Mock test and test day</h4><p>Including a warm-up lesson ending at the test centre.</p></li></ol>
<h2>Is intensive right for you?</h2><p>It suits people with some experience, a theory pass and a test date. Complete beginners usually do better with a semi-intensive plan (6–10 hours a week). Prices are the same as normal lessons: £35/hr, £350 for 10 hours.</p>""",
         [("How fast can I pass with an intensive course in Solihull?", "It depends on experience and test availability. With a theory pass and a test date, a few weeks is realistic for many learners."), ("Do intensive courses cost more?", "No — the same £35/hr.")]),
        ("motorway-driving-lessons-m42-solihull", "Motorway lessons on the M42 near Solihull", "Motorway Driving Lessons M42 Solihull | Learners & New Drivers | SQ",
         "Motorway lessons on the M42 around Solihull — smart motorway signs, joining at junctions 4–6, and lane discipline — for learners and new drivers.",
         """<p class="lead">Solihull is wrapped by the M42, with junctions 4, 5 and 6 serving Shirley, Solihull and the NEC and airport. Since June 2018 learners can drive on motorways with an approved instructor in a dual-control car — and Solihull is one of the best places in the country to learn.</p>
<h2>Why the M42 is special</h2>
<p>The M42 between junctions 3a and 7 was the UK's first Active Traffic Management pilot, from September 2006 — the forerunner of today's smart motorways, with variable speed limits and hard-shoulder running. Learning here means learning to read overhead signs: a speed in a red circle is a legal limit, and a red X means the lane is closed.</p>
<h2>Junction 6 works</h2><p>National Highways' M42 junction 6 improvement serves the airport and NEC, and the HS2 Interchange station is being built between the M42, A45 and A452 (TfWM now expects HS2 services between 2029 and 2033). Roadworks, temporary limits and changed layouts are part of driving here — and great practice.</p>
<h2>What a motorway lesson covers</h2><ul><li>Joining from the slip road and matching speed</li><li>Lane discipline and overtaking</li><li>Smart motorway signs and emergency areas</li><li>Leaving at the right junction</li></ul>""",
         [("Can learners drive on the M42?", "Yes, with an approved driving instructor in a car with dual controls."), ("What does a red X on the M42 mean?", "The lane is closed. Move out of it safely and never drive under a red X.")]),
        ("student-driving-lessons-solihull", "Student driving lessons in Solihull", "Student Driving Lessons Solihull | £320 for 10 Hours | SQ Driving School",
         "Driving lessons for Solihull College, Solihull Sixth Form College and school students — 10 hours for £320, pick-up from campus.",
         """<p class="lead">Students in Solihull get our student price: 10 hours for £320 instead of £350. We pick up from campus and fit lessons around timetables.</p>
<h2>Colleges we pick up from</h2>
<div class="rt-marks"><div class="rt-mark"><b>Solihull College — Blossomfield campus</b><small>Blossomfield Road, a few minutes from Solihull station</small></div><div class="rt-mark"><b>Solihull College — Woodlands campus</b><small>Auckland Drive, Smith's Wood</small></div><div class="rt-mark"><b>Solihull Sixth Form College</b><small>Widney Manor Road, B91</small></div></div>
<h2>Why learn while you study</h2><p>About 18% of Solihull households had no car or van in 2021 — and young people are the most likely to depend on lifts and buses. A licence opens up jobs at places like the airport, the NEC and JLR's Lode Lane plant, which public transport doesn't always serve at shift times.</p>
<h2>How to claim</h2><p>Tell us you're a student when you book. We'll check your uni or college student ID to confirm — then your 10 hours are £320.</p>""",
         [("Is there a student discount in Solihull?", "Yes: 10 hours for £320 instead of £350."), ("Can you pick me up from Solihull College?", "Yes, from either campus or the Sixth Form College.")]),
        ("nhs-driving-lessons-solihull", "Driving lessons for NHS staff in Solihull", "NHS Staff Driving Lessons Solihull | £320 for 10 Hours | SQ",
         "NHS staff discount on driving lessons in Solihull — 10 hours for £320 — with lessons around shifts at Solihull Hospital and nearby.",
         """<p class="lead">NHS staff in Solihull get 10 hours of driving lessons for £320. We plan lessons around early, late and night shifts, and pick up from home or from work.</p>
<h2>Around Solihull Hospital</h2><p>Solihull Hospital is on Lode Lane, B91 2JL. Lessons can start or finish there — handy after a shift.</p>
<h2>Shift-friendly lessons</h2><ul><li>Early-morning and evening slots</li><li>2-hour lessons to make the most of days off</li><li>Never straight after a night shift — tiredness slows your reactions (see our <a href="../driving/stopping-distances-calculator.html">stopping distance calculator</a>).</li></ul>
<h2>How to claim</h2><p>Mention you work for the NHS when you book and show your ID at your first lesson.</p>""",
         [("Is there an NHS discount for driving lessons in Solihull?", "Yes: 10 hours for £320 instead of £350."), ("Can lessons fit around shifts?", "Yes — early, late and weekend slots.")]),
    ]
    for slug, title, seo, desc, body, faqs in defs:
        path = f"solihull/{slug}.html"
        faqs = faqs + [("How much are driving lessons in Solihull?", "£35 an hour, £70 for 2 hours, £350 for 10 hours.")]
        rel = [("solihull/shirley-driving-test-centre-routes.html", "Test routes", "Shirley test routes", "Solihull's own test centre."), ("solihull/solihull-driving-test-centres-compared.html", "Compare", "Solihull test centres compared", "Pass rates and postcodes.")]
        src = common_src + (["m42", "tfwm", "motorway"] if "motorway" in slug else []) + (["college", "story"] if "student" in slug else [])
        out[path] = S(path, seo, "Lessons in Solihull", (title.replace(" in Solihull", "").replace(" near Solihull", ""), path), title, desc,
                      [("£35", "per hour"), ("£350", "10 hours"), ("58.1%", "Shirley pass rate"), ("Free", "Student Portal")],
                      [desc.split(" — ")[0] + ".", "Manual and automatic both £35/hr.", "Lessons planned around your test centre's roads.", "Free DriveSQ Student Portal with every lesson."],
                      body, faqs, src, rel, extra_schema=_biz(path, "Solihull", ["B90", "B91", "B92", "B93", "B94", "B36", "B37"]))
    return out


# ============================================================ GUIDE
def guide():
    path = "solihull/learning-to-drive-in-solihull.html"
    body = f"""
<p class="lead">Solihull is not Manchester, and it's not Birmingham either. It has more cars per household than most of England, the country's first smart motorway on its doorstep, an airport and the NEC inside its borders, and a test centre with one of the best pass rates in the region. Here is what that means for learning to drive here — with every figure sourced.</p>
{RS._figs([("216,245", "Solihull residents (Census 2021)", "Up 4.6% since 2011"), ("~18%", "households with no car or van (2021)", "England: about 23.5%"), ("58.1%", "Shirley test pass rate, 2024-25", "UK: 48.7%"), ("2006", "M42 became the UK's first smart-motorway pilot", "J3a–J7")])}
<h2>A borough of drivers</h2>
<p>At the 2021 Census, Solihull Council reports that just 18% of households — about 15,750 — had no car or van, compared with roughly 23.5% across England. North Solihull has more households without a car than the south. With a median age of 43, Solihull is older than England as a whole, and 16–24 year olds make up about 9% of residents. Most young people grow up in car-owning households — which means more chances for <a href="{ROOT}knowledge/practising-with-family-supervisor-rules.html">private practice</a> between lessons.</p>
<h2>The roads that shape Solihull drivers</h2>
<ul><li><b>The A34 Stratford Road</b> — Shirley's high street and the backbone of Shirley test routes.</li><li><b>The A41 Warwick Road</b> — through Olton and Solihull town centre.</li><li><b>The A45 Coventry Road</b> — fast dual carriageway to the airport and NEC, and on Garretts Green and South Yardley routes.</li><li><b>The M42</b> — junctions 4 (Shirley/Blythe Valley), 5 (Solihull) and 6 (NEC/airport). The stretch from 3a to 7 was the UK's first Active Traffic Management pilot in 2006.</li></ul>
<h2>20mph in Solihull</h2>
<p>Solihull adopted a new speed-limit policy in July 2022, prioritising 20mph limits around schools, retail centres and village centres, and continues a rolling programme of school 20mph limits. Expect them near schools in places like Chelmsley Wood and Dorridge — and expect examiners to notice if you miss one.</p>
<h2>Birmingham's Clean Air Zone doesn't apply in Solihull</h2>
<p>Birmingham's Clean Air Zone covers roads inside the A4540 Middleway ring road only. Non-compliant cars pay £8 a day there; Solihull roads aren't affected. Our lesson cars are compliant anyway.</p>
<h2>Roadworks: M42 junction 6 and HS2</h2>
<p>National Highways' M42 junction 6 improvement and the HS2 Interchange station (between the M42, A45 and A452) mean changing layouts and temporary limits around the NEC and airport. TfWM now expects HS2 services to start between 2029 and 2033.</p>
<h2>Theory and practical tests</h2>
<p>Solihull's theory test centre closed in August 2011 — take your theory test in Birmingham or Coventry. For the practical, <a href="shirley-driving-test-centre-routes.html">Shirley</a> is the borough's only centre and had the area's highest pass rate in 2024-25. See all options in our <a href="solihull-driving-test-centres-compared.html">comparison</a>.</p>
<h2>Jobs that need a licence</h2>
<p>JLR's Solihull plant on Lode Lane — its largest, covering about 300 acres and building Range Rover and Discovery models — plus the airport, the NEC, Resorts World and Blythe Valley Park are major employers. Many shifts start before buses run.</p>"""
    faqs = [("How many people live in Solihull?", "216,245 at the 2021 Census, up 4.6% since 2011."),
            ("What share of Solihull households have no car?", "About 18% in 2021, according to Solihull Council — below the England figure of about 23.5%."),
            ("Does the Birmingham Clean Air Zone cover Solihull?", "No. It only covers roads inside Birmingham's A4540 Middleway."),
            ("Where can I take my theory test near Solihull?", "Birmingham or Coventry. Solihull's theory centre closed in 2011.")]
    return S(path, "Learning to Drive in Solihull: Local Guide & Data 2026 | SQ Driving School", "Solihull guide", ("Learning to drive in Solihull", path),
             "Learning to drive in Solihull: the local guide", "Everything about learning to drive in Solihull: car ownership, the M42 smart motorway, 20mph limits, the Clean Air Zone, test and theory centres and local roads — all sourced.",
             [("216k", "residents"), ("18%", "no-car households"), ("58.1%", "Shirley pass rate"), ("3", "M42 junctions")],
             ["About 18% of Solihull households had no car in 2021 — fewer than England overall.", "The M42 here was the UK's first smart-motorway pilot (2006).", "Birmingham's Clean Air Zone doesn't apply in Solihull.", "Shirley is the only test centre in the borough."],
             body, faqs, ["census", "story", "ons_cars", "speed", "safety", "caz", "brum", "m42", "tfwm", "theory_close", "jlr", "pr_shirley"],
             [("solihull/solihull-driving-test-centres-compared.html", "Compare", "Test centres compared", "Pass rates and postcodes."), ("solihull/motorway-driving-lessons-m42-solihull.html", "Lessons", "M42 motorway lessons", "Smart-motorway skills.")])


# ============================================================ PILLAR
def pillar():
    path = "driving-lessons-solihull.html"
    areas = "".join(f'<a class="rx-study" href="solihull/driving-lessons-{a["slug"]}.html" data-reveal="up"><span class="k-cat">{" / ".join(a["pcs"])}</span><h3>{a["name"]}</h3><p>{a["intro"][:110].rsplit(" ", 1)[0]}…</p></a>' for a in AREAS)
    cen = "".join(f'<a class="rx-study" href="solihull/{c["slug"]}-driving-test-centre-routes.html" data-reveal="up"><span class="k-cat">{c["pc"]} · {c["rate"]}%</span><h3>{c["name"]} test centre</h3><p>{len(c["roads"])} roads, mistakes and landmarks.</p></a>' for c in CENTRES)
    body = f"""
<p class="lead">SQ Driving School — part of DriveSQ — now teaches across Solihull, from Shirley, Solihull town centre, Olton, Knowle and Dorridge to Chelmsley Wood, Castle Bromwich, Kingshurst, Marston Green, Balsall Common, Meriden and every village in between. Manual or automatic, £35 an hour, door-to-door pick-up and the free DriveSQ Student Portal.</p>
{RS._figs([("£35", "per hour, manual or automatic", "Same price either way"), ("£350", "10-hour block", "£320 NHS staff & students"), ("58.1%", "Shirley test pass rate 2024-25", "UK 48.7%"), (str(len(AREAS)), "Solihull areas covered", "B90–B94, B36, B37, B40, CV7")])}
<h2>Driving lessons in every part of Solihull</h2>
<div class="grid grid--3" data-stagger=".04">{areas}</div>
<h2>Driving test centres for Solihull learners</h2>
<p>Shirley is the borough's own centre; north Solihull learners usually book Garretts Green. Every guide lists the roads on reported routes, landmarks and the mistakes learners make. <a href="solihull/solihull-driving-test-centres-compared.html">Compare them all</a>.</p>
<div class="grid grid--2" data-stagger=".05">{cen}</div>
<h2>Every Solihull guide</h2>
<p>Postcode districts, schools and colleges, workplaces, ten road guides and more: <a href="solihull/all-solihull-guides.html">see every Solihull guide</a> · <a href="solihull/solihull-road-guides.html">Solihull road guides</a> · <a href="solihull/driving-lesson-prices-solihull.html">Solihull prices</a> · <a href="solihull/drivesq-student-portal-solihull.html">DriveSQ Student Portal</a> · <a href="solihull/drivesq-instructor-portal-solihull.html">DriveSQ Instructor Portal</a>.</p>
<h2>Lessons for every learner</h2>
<ul><li><a href="solihull/automatic-driving-lessons-solihull.html">Automatic driving lessons in Solihull</a> — same price as manual.</li><li><a href="solihull/nervous-driver-lessons-solihull.html">Nervous drivers</a>, <a href="solihull/refresher-driving-lessons-solihull.html">refresher lessons</a>, <a href="solihull/adult-driving-lessons-solihull.html">adults and over-50s</a>, <a href="solihull/evening-weekend-driving-lessons-solihull.html">evenings and weekends</a>, <a href="solihull/semi-intensive-driving-course-solihull.html">semi-intensive courses</a>, <a href="solihull/mock-driving-test-solihull.html">mock tests</a>, <a href="solihull/pass-plus-solihull.html">Pass Plus</a> and <a href="solihull/driving-test-cancellations-shirley.html">finding an earlier test</a>.</li><li><a href="solihull/intensive-driving-courses-solihull.html">Intensive driving courses in Solihull</a>.</li><li><a href="solihull/manual-driving-lessons-solihull.html">Manual lessons</a>, <a href="solihull/beginner-driving-lessons-solihull.html">beginners</a>, <a href="solihull/cheap-driving-lessons-solihull.html">affordable lessons</a>, <a href="solihull/female-driving-instructor-solihull.html">female instructor</a>, <a href="solihull/failed-driving-test-lessons-solihull.html">failed your test</a>, <a href="solihull/driving-lessons-overseas-licence-solihull.html">overseas licence holders</a> and <a href="solihull/pass-driving-test-fast-solihull.html">pass fast</a>.</li><li><a href="solihull/motorway-driving-lessons-m42-solihull.html">Motorway lessons on the M42</a>.</li><li><a href="solihull/student-driving-lessons-solihull.html">Student lessons</a> and <a href="solihull/nhs-driving-lessons-solihull.html">NHS staff lessons</a> — 10 hours for £320.</li><li><a href="solihull/learning-to-drive-in-solihull.html">Learning to drive in Solihull: the local guide</a>.</li></ul>
<h2>How lessons work</h2>
<ol class="rx-steps"><li data-n="1"><h4>Book in 60 seconds</h4><p>Choose manual or automatic and enter your postcode below — a real person replies fast.</p></li><li data-n="2"><h4>First lesson from your door</h4><p>We pick you up anywhere in Solihull.</p></li><li data-n="3"><h4>Track every skill</h4><p>Your instructor logs 23 skills in your DriveSQ Student Portal after every lesson.</p></li><li data-n="4"><h4>Test-route practice and mock test</h4><p>On the real roads around your test centre.</p></li></ol>"""
    faqs = [("Do you offer driving lessons in Solihull?", "Yes. SQ Driving School, part of DriveSQ, teaches across Solihull — manual and automatic."),
            ("How much are driving lessons in Solihull?", "£35 an hour, £70 for 2 hours and £350 for 10 hours (£320 for NHS staff and students)."),
            ("Which driving test centre is in Solihull?", "Birmingham (Shirley), 401 Stratford Road, B90 4AA — 58.1% pass rate in 2024-25."),
            ("Which Solihull areas do you cover?", ", ".join(a["name"] for a in AREAS) + ".")]
    return S(path, "Driving Lessons Solihull | £35/hr Manual & Automatic | SQ Driving School", "Driving lessons Solihull", None,
             "Driving lessons in Solihull", "Driving lessons across Solihull from £35/hr — manual and automatic, door-to-door pick-up, Shirley test-route practice and the free DriveSQ Student Portal. Part of DriveSQ.",
             [("£35", "per hour"), (str(len(AREAS)), "areas"), ("58.1%", "Shirley pass rate"), ("Free", "Student Portal")],
             ["Lessons across Solihull from £35/hr, manual or automatic.", "10 hours £350 — £320 for NHS staff and students.", "Shirley test centre had the area's best pass rate in 2024-25 (58.1%).", "Part of DriveSQ — free Student Portal with every lesson."],
             body, faqs, ["census", "story", "pr_shirley", "pr_bham", "cost", "book"],
             [("solihull/learning-to-drive-in-solihull.html", "Guide", "Learning to drive in Solihull", "Local data and roads."), ("solihull/solihull-driving-test-centres-compared.html", "Compare", "Solihull test centres compared", "Pass rates by centre.")],
             root="", extra_schema=_biz(path, "Solihull", ["B90", "B91", "B92", "B93", "B94", "B36", "B37", "CV7"]))


def all_pages():
    out = {"driving-lessons-solihull.html": pillar(), "solihull/solihull-driving-test-centres-compared.html": compare_page(), "solihull/learning-to-drive-in-solihull.html": guide()}
    for c in CENTRES:
        out[f"solihull/{c['slug']}-driving-test-centre-routes.html"] = centre_page(c)
    for a in AREAS:
        out[f"solihull/driving-lessons-{a['slug']}.html"] = area_page(a)
    out.update(lesson_pages())
    return out
