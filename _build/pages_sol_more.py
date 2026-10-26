"""Solihull batch 2: more neighbourhoods, postcode districts, schools & colleges, employers, lesson types, prices,
and the DriveSQ Student / Instructor Portal pages. Facts from Census 2021, Solihull Council, LGBCE (2026 wards),
GIAS/Ofsted, school and employer sites, National Rail, HS2 and parish councils — each page cites its sources."""
from hub_shell import *
import pages_solihull as SOL
from pages_solihull import S, CENTRES, SRC

CEN = {c["slug"]: c for c in CENTRES}
STUDENT = "https://www.drivesq.co.uk/student.html"
INSTR = "https://www.drivesq.co.uk/dashboard.html"
LGBCE = ("LGBCE — Solihull electoral review (2026 wards)", "https://www.lgbce.org.uk/all-reviews/solihull")
GIAS = ("GOV.UK — Get information about schools", "https://get-information-schools.service.gov.uk/")
SIXTH = ("Solihull Council — sixth forms and colleges", "https://www.solihull.gov.uk/schools-and-learning/infant-and-primary-schools/sixth-forms-and-colleges")
PROV = ("GOV.UK — Apply for your first provisional driving licence", "https://www.gov.uk/apply-first-provisional-driving-licence")


def portal_strip():
    return f"""<div class="rx-portals" data-stagger=".08"><div class="rx-portal" data-reveal="up"><div class="eyebrow">Learners</div><h3>DriveSQ Student Portal</h3><p>Your progress after every lesson: 23 skills, theory library, 50-question mock tests and a test-readiness checklist. Free with every SQ lesson in Solihull.</p><div class="btn-row"><a class="btn btn--red btn--sm" href="{ROOT}solihull/drivesq-student-portal-solihull.html">See the Student Portal</a><a class="btn btn--ghost btn--sm" href="{STUDENT}" target="_blank" rel="noopener">Login ↗</a></div></div>
<div class="rx-portal" data-reveal="up" data-delay=".1"><div class="eyebrow">Instructors</div><h3>DriveSQ Instructor Portal</h3><p>Diary, pupils, skill records and messages in one place — and new Solihull learners matched to you by postcode.</p><div class="btn-row"><a class="btn btn--red btn--sm" href="{ROOT}solihull/drivesq-instructor-portal-solihull.html">See the Instructor Portal</a><a class="btn btn--ghost btn--sm" href="{INSTR}" target="_blank" rel="noopener">Login ↗</a></div></div></div>"""


# ============================================================ MORE NEIGHBOURHOODS (appended to the pillar list)
def A(slug, name, pcs, centre, intro, local, roads, near, angle, extra="", pop=None, pop_label=None):
    return dict(slug=slug, name=name, pcs=pcs, centre=centre, intro=intro, local=local, roads=roads, near=near, angle=angle, extra=extra, pop=pop, pop_label=pop_label)


NEW_AREAS = [
    A("hillfield", "Hillfield", ["B91"], "shirley", "Hillfield sits between Solihull town centre and Monkspath, around Hillfield Park and the Grade II* Hillfield Hall of 1576.",
      "Quiet estate roads off Monkspath Hall Road and Widney Lane suit first lessons; within minutes you're on the A34 roads that Shirley test routes use.",
      ["Monkspath Hall Road", "Widney Lane", "Stratford Road (A34) nearby"], ["Hillfield Park (Green Flag, with a lake)", "Hillfield Hall (1576)", "Widney Manor and Solihull stations"],
      "Hillfield learners test at Shirley, a few minutes away.",
      "<p>Hillfield Park's car-park gates close at 8pm from April to October and 4pm from November to March — handy to know if we use it for manoeuvre practice.</p>"),
    A("cheswick-green", "Cheswick Green", ["B90"], "shirley", "Cheswick Green is a 1970s planned village built around a central green, south of the A34 and next to Blythe Valley Park.",
      "Its lanes — Creynolds Lane, Watery Lane, Tanworth Lane — were once single-track, and the parish council says they're narrow for today's traffic. Perfect for learning to meet oncoming cars and judge clearance.",
      ["Tanworth Lane", "Creynolds Lane", "Watery Lane", "Stratford Road (A34)"], ["The village green and shop parade", "Blythe Valley Park (same parish)", "M42 junction 4"],
      "Cheswick Green learners test at Shirley."),
    A("bentley-heath", "Bentley Heath", ["B93"], "shirley", "Bentley Heath lies between Knowle and Dorridge, around the Widney Road / Tilehouse Green Lane junction.",
      "A good mix: village shops and a primary school for hazard awareness, residential roads for manoeuvres, and lanes towards Knowle and Dorridge.",
      ["Widney Road", "Mill Lane", "Four Ashes Road", "Tilehouse Green Lane"], ["Drum & Monkey (since about 1860)", "Village Co-op and post office", "Dorridge station (about half a mile)"],
      "Bentley Heath learners test at Shirley."),
    A("elmdon", "Elmdon", ["B92", "B26"], "south-yardley", "Elmdon sits south of the A45, beside Birmingham Airport (once Elmdon Aerodrome) and JLR's entrances on Damson Parkway.",
      "Airport traffic, JLR shift changes and the A45 make Elmdon great for anticipation practice; residential roads off Tanhouse Farm Road suit the basics.",
      ["A45 Coventry Road", "Damson Parkway", "Tanhouse Farm Road", "Lode Lane / Hobs Moat Road"], ["Elmdon Park (Green Flag)", "St Nicholas Church (1780)", "Birmingham Airport"],
      "Elmdon learners often book South Yardley or Garretts Green.",
      "<p>A temporary 30mph order covers the A45, Damson Parkway and Terminal Road near the airport from about August 2026 — see our <a href=\"a45-coventry-road-airport-nec.html\">A45 guide</a>.</p>"),
    A("lyndon", "Lyndon", ["B92"], "south-yardley", "Lyndon is the area around Hobs Moat Road, between Olton and Elmdon, partly bounded by the Grand Union Canal.",
      "Hobs Moat Road is where we teach bus lanes and busy junctions — its junction with Ulleries Road topped the council's collision rankings for 2016–18, so observation is everything.",
      ["Hobs Moat Road", "Lode Lane", "Barn Lane", "Daylesford Road"], ["Lyndon School (Daylesford Road)", "Grand Union Canal", "Lode Lane bus lanes"],
      "Lyndon learners often book South Yardley; Shirley is the alternative.",
      "<p>Read our <a href=\"lode-lane-hobs-moat-road-bus-lanes.html\">Lode Lane and Hobs Moat Road guide</a> before your lessons here.</p>"),
    A("fordbridge", "Fordbridge", ["B37"], "garretts-green", "Fordbridge is in north Solihull between Kingshurst and Chelmsley Wood — and a ward in its own right since 2026.",
      "Cooks Lane straddles the Birmingham/Solihull boundary and appears on Garretts Green test routes, so Fordbridge learners can practise test roads from home.",
      ["Cooks Lane", "Bosworth Drive", "Nine Acres Drive"], ["The Fordbridge Centre (buses 71, 91, 94)", "Kingshurst village centre", "Chelmsley Wood shopping centre"],
      "Fordbridge learners usually book Garretts Green."),
    A("smiths-wood", "Smith's Wood", ["B36"], "garretts-green", "Smith's Wood is home to Solihull College's Woodlands campus and Smith's Wood Academy, bounded by the A452 Collector Road and the M6.",
      "Student-heavy roads around Windward Way and Auckland Drive, then the A452 and Chester Road for faster driving.",
      ["Windward Way", "Auckland Drive", "A452 Collector Road", "Chester Road (A452)"], ["Solihull College Woodlands campus", "Smith's Wood Academy", "M6 nearby"],
      "Smith's Wood learners usually book Garretts Green.", pop="10,905", pop_label="residents (2021 parish)"),
    A("kingshurst", "Kingshurst", ["B37"], "garretts-green", "Kingshurst is a north Solihull village with a busy shopping parade — and a village centre being rebuilt, with net-zero homes delivered in phase 1.",
      "Cooks Lane (on Garretts Green routes), Gilson Way and the shopping parade give a mix of junctions, parked cars and pedestrians.",
      ["Cooks Lane", "Gilson Way", "Meriden Drive", "Fordbridge Road"], ["Kingshurst shopping parade", "St Barnabas Church", "Kingshurst Park", "Tudor Grange Academy Kingshurst"],
      "Kingshurst learners usually book Garretts Green.", pop="8,348", pop_label="residents (2021)"),
    A("hampton-in-arden", "Hampton-in-Arden", ["B92"], "south-yardley", "Hampton-in-Arden is a village between Solihull and Meriden on the West Coast Main Line — right beside HS2's construction.",
      "Village lanes, the B4102 Meriden Road and HS2 works mean traffic lights, closures and plant crossings. Average speed cameras cover the village.",
      ["B4102 Meriden Road", "High Street", "Marsh Lane", "Fentham Road", "Diddington Lane"], ["Hampton-in-Arden station", "White Lion pub", "The Beeches, Marsh Lane"],
      "Hampton-in-Arden learners book South Yardley, Shirley or Coventry.",
      "<p>In 2026 the B4102 Meriden Road had HS2 closures for the River Blythe viaduct, and Diddington Lane was fully closed from 16 March to 19 September 2026. Check before you drive.</p>"),
    A("berkswell", "Berkswell", ["CV7"], "shirley", "Berkswell is a historic village by Balsall Common, famous for its 16-foot stone well and Norman church — and for an unusual single-file tunnel.",
      "At Berkswell station the level crossing closed in 2004 and was replaced by a narrow, single-file road tunnel controlled by traffic lights. It's a brilliant lesson in obeying signals and patience. Average speed cameras cover the village.",
      ["Station Road (single-file tunnel)", "Truggist Lane", "Kenilworth Road (A452)"], ["Berkswell station", "St John the Baptist church (12th century)", "The Bear Inn"],
      "Berkswell learners usually book Coventry, Warwick or Shirley."),
    A("catherine-de-barnes", "Catherine-de-Barnes", ["B91", "B92"], "shirley", "Catherine-de-Barnes is a canal-side village east of Solihull on the B4102, where the road narrows at the canal bridge.",
      "A narrow canal bridge, changing speed limits on Catherine de Barnes Lane (40, 50 and 20mph since October 2025) and the M42 nearby — excellent for speed judgement.",
      ["B4102 Hampton Lane / Solihull Road", "B4438 Catherine de Barnes Lane", "Clock Lane"], ["Grand Union Canal", "The Boat Inn", "M42 junction 5A (new 2024)"],
      "Catherine-de-Barnes learners book Shirley or South Yardley."),
    A("tidbury-green", "Tidbury Green", ["B90"], "shirley", "Tidbury Green is a small village in the triangle of Fulford Hall Road, Norton Lane and Lowbrook Lane, close to three railway stations.",
      "Rural lanes with bends and no pavements teach hazard awareness and speed for the conditions; Shirley's test roads are a short drive away.",
      ["Fulford Hall Road", "Norton Lane", "Lowbrook Lane"], ["Wythall station (about 800m)", "Whitlocks End and Earlswood stations", "Dickens Heath nearby"],
      "Tidbury Green learners test at Shirley.", pop="2,039", pop_label="residents (2021 parish)"),
    A("blythe-valley", "Blythe Valley", ["B90"], "shirley", "Blythe Valley Park, at M42 junction 4, combines a business park with new homes around a 122-acre country park.",
      "New-build estates, business-park roundabouts and the A34/M42 junction — about as close to Shirley's test conditions as it gets.",
      ["Stratford Road (A34)", "M42 junction 4", "Blythe Valley Park roads"], ["The 122-acre country park", "Virgin Active and Co-op", "M42 junction 4"],
      "Blythe Valley learners test at Shirley."),
    A("sharmans-cross", "Sharmans Cross", ["B91"], "shirley", "Sharmans Cross is a residential area between Shirley and Solihull, giving its name to the new Shirley East & Sharmans Cross ward from 2026.",
      "Leafy residential roads with junctions onto the B4025 Streetsbrook Road — great for junction observation practice before tackling the A34.",
      ["Sharmans Cross Road", "Streetsbrook Road (B4025)", "Prospect Lane", "Solihull Road"], ["Former Birmingham & Solihull RFC ground", "Solihull town centre", "Shirley"],
      "Sharmans Cross learners test at Shirley."),
    A("widney-manor", "Widney Manor", ["B91"], "shirley", "Widney Manor is south of Solihull town centre, around Widney Manor Road and its station, home to the Sixth Form College Solihull.",
      "Student traffic at the Sixth Form College and the station car park, residential roads for manoeuvres and quick access to the A34 and M42.",
      ["Widney Manor Road", "Widney Lane", "Monkspath Hall Road"], ["Widney Manor station (step-free, ~274 spaces)", "The Sixth Form College Solihull", "Malvern & Brueton Park"],
      "Widney Manor learners test at Shirley."),
    A("solihull-lodge", "Solihull Lodge", ["B90"], "shirley", "Solihull Lodge is Solihull's south-western corner on the Birmingham border, by the Stratford-upon-Avon Canal and Major's Green Aqueduct.",
      "Border roads like Yardley Wood Road, plus quieter streets for early lessons. Kings Heath test centre is also within reach.",
      ["Yardley Wood Road", "Aqueduct Road", "Haslucks Green Road"], ["Stratford-upon-Avon Canal and Major's Green Aqueduct", "The Lodge pub", "Peterbrook Primary School"],
      "Solihull Lodge learners book Shirley or Kings Heath.", pop="~2,500", pop_label="residents"),
    A("copt-heath", "Copt Heath", ["B93"], "shirley", "Copt Heath is on the A4141 between Knowle and M42 junction 5, home to Copt Heath Golf Club (laid out by Harry Vardon in 1907).",
      "Fast approaches to M42 junction 5, then Knowle's 20mph High Street a minute later — a lesson in adjusting speed.",
      ["Warwick Road (A4141)", "M42 junction 5", "Knowle High Street (20mph)"], ["Copt Heath Golf Club", "M42 junction 5 (Copt Hill Interchange)", "Knowle village"],
      "Copt Heath learners test at Shirley."),
    A("bickenhill", "Bickenhill", ["B92"], "garretts-green", "Bickenhill is the historic village at the heart of Solihull's transport hub: the airport, the NEC, the M42, the A45 — and the HS2 Interchange station.",
      "New limits from October 2025 (20mph on Church Lane and St Peters Lane, 40 and 50mph on Catherine de Barnes Lane), the A452 40mph clearway and constant HS2 layout changes.",
      ["Church Lane (20mph)", "Catherine de Barnes Lane", "A452 Chester Road (40mph clearway)", "A45"], ["St Peter's Church (Grade I)", "NEC and Birmingham Airport", "HS2 Interchange site"],
      "Bickenhill learners usually book Garretts Green."),
    A("elmdon-heath", "Elmdon Heath", ["B91"], "shirley", "Elmdon Heath is about a mile north of Solihull town centre, centred on Damson Lane.",
      "Residential roads for early lessons and quick access to Lode Lane, Solihull Hospital and the town centre for busier driving.",
      ["Damson Lane", "Cornyx Lane", "Lode Lane (B425)"], ["The Greville Arms", "Solihull Hospital (Lode Lane)", "Solihull town centre"],
      "Elmdon Heath learners book Shirley or South Yardley."),
]
SOL.AREAS.extend(NEW_AREAS)


# ============================================================ POSTCODE DISTRICTS
PCS = [
    ("B90", "Shirley, Monkspath, Dickens Heath, Cheswick Green, Tidbury Green, Blythe Valley and Solihull Lodge", "shirley",
     ["Stratford Road (A34)", "Tanworth Lane", "Haslucks Green Road", "Dog Kennel Lane"], ["Light Hall School", "Shirley station", "Parkgate shopping centre", "Blythe Valley Park"],
     ["shirley", "monkspath", "dickens-heath", "cheswick-green", "tidbury-green", "blythe-valley", "solihull-lodge"],
     "B90 is home to Solihull's only driving test centre, at 401 Stratford Road. Learners here can practise real test roads on almost every lesson."),
    ("B91", "Solihull town centre, Hillfield, Sharmans Cross, Widney Manor, Elmdon Heath and Catherine-de-Barnes", "shirley",
     ["Warwick Road", "Lode Lane", "Blossomfield Road", "Widney Manor Road"], ["Touchwood", "Solihull School", "Tudor Grange Academy", "Alderbrook School", "Solihull College (Blossomfield)", "Solihull Hospital"],
     ["solihull-town-centre", "hillfield", "sharmans-cross", "widney-manor", "elmdon-heath", "catherine-de-barnes"],
     "B91 is the heart of Solihull — the town centre's bus-only streets, the new Blossomfield signals and the busy Lode Lane corridor."),
    ("B92", "Olton, Lyndon, Elmdon, Bickenhill and Hampton-in-Arden", "south-yardley",
     ["A41 Warwick Road", "Hobs Moat Road", "A45 Coventry Road", "Damson Parkway"], ["JLR Solihull (Lode Lane, B92 8NW)", "Langley School", "Lyndon School", "Olton station"],
     ["olton", "lyndon", "elmdon", "bickenhill", "hampton-in-arden"],
     "B92 covers the A41 safety corridor (new 20/30mph limits from July 2025) and the JLR plant."),
    ("B93", "Knowle, Dorridge, Bentley Heath and Copt Heath", "shirley",
     ["Warwick Road (A4141)", "Station Road", "Four Ashes Road", "Widney Road"], ["Arden Academy", "Dorridge station", "Copt Heath Golf Club"],
     ["knowle", "dorridge", "bentley-heath", "copt-heath"],
     "B93's villages had a wave of new limits in 2023 — 20mph on Knowle High Street and 40mph on surrounding lanes."),
    ("B94", "Hockley Heath and Earlswood (part)", "shirley",
     ["Stratford Road", "B4439", "Box Trees Road"], ["Stratford-upon-Avon Canal", "Earlswood Lakes"],
     ["hockley-heath"], "B94 is rural Solihull: canal bridges, country lanes and the approach to M42 junction 4."),
    ("B36", "Castle Bromwich and Smith's Wood", "garretts-green",
     ["Chester Road (A452)", "Bradford Road (B4114)", "Windward Way", "A452 Collector Road"], ["Park Hall Academy", "Smith's Wood Academy", "Solihull College (Woodlands)", "Castle Bromwich Hall Gardens"],
     ["castle-bromwich", "smiths-wood", "kingshurst-smiths-wood"], "B36 sits between the M6 and the A452 — fast roads close to home."),
    ("B37", "Chelmsley Wood, Kingshurst, Fordbridge and Marston Green", "garretts-green",
     ["Chester Road (A452)", "Cooks Lane", "Chelmsley Road", "Station Road (Marston Green)"], ["John Henry Newman Catholic College", "Grace Academy", "Tudor Grange Academy Kingshurst", "WMG Academy", "Chelmsley Wood shopping centre"],
     ["chelmsley-wood", "kingshurst", "fordbridge", "marston-green"], "B37 learners usually test at Garretts Green — and Cooks Lane is on its routes."),
    ("B40", "The NEC, Birmingham Airport area and Bickenhill", "garretts-green",
     ["A45", "M42 junction 6", "Pendigo Way", "A452"], ["NEC", "Resorts World Birmingham", "Birmingham International station"],
     ["bickenhill", "marston-green"], "B40 is Solihull's events and travel hub — new junctions, HS2 works and drivers who don't know the area."),
    ("CV7", "Balsall Common, Berkswell and Meriden", "shirley",
     ["Kenilworth Road (A452)", "Station Road", "London Road", "A45"], ["Heart of England School", "Berkswell station", "Meriden village green"],
     ["balsall-common", "berkswell", "meriden"], "CV7 learners choose between Coventry, Warwick and Shirley — and drive HS2 contraflows until 2027."),
]


def pc_page(code, areas, centre, roads, near, slugs, lead):
    path = f"solihull/{code.lower()}-driving-lessons.html"
    c = CEN[centre]
    names = {a["slug"]: a["name"] for a in SOL.AREAS}
    links = "".join(f'<a class="chip" href="driving-lessons-{s}.html">{names[s]}</a>' for s in slugs if s in names)
    body = f"""<p class="lead">Driving lessons in {code}: {areas}. {lead}</p>
{RS._figs([("£35", "per hour, manual or automatic", ""), (c['name'], "usual nearest test centre", f"{c['rate']}% pass rate 2024-25"), (str(len(slugs)), "areas in this guide", ""), ("Free", "DriveSQ Student Portal", "")])}
<h2>Areas we cover in {code}</h2><div class="hero__badges">{links}</div>
<h2>Main roads in {code}</h2><ul>{''.join(f'<li>{r}</li>' for r in roads)}</ul>
<p>Our <a href="solihull-road-guides.html">Solihull road guides</a> cover limits, cameras and roadworks for each.</p>
<h2>Schools, colleges and landmarks</h2>{landmarks([(x, code) for x in near])}
<h2>Your nearest test centre</h2><p>Most {code} learners book <a href="{c['slug']}-driving-test-centre-routes.html">{c['full']}</a> ({c['address']}). Compare all options in our <a href="solihull-driving-test-centres-compared.html">test centre comparison</a>.</p>
{portal_strip()}"""
    faqs = [(f"Do you offer driving lessons in {code}?", f"Yes — across {areas}."), (f"Which test centre is nearest to {code}?", f"Usually {c['full']}."),
            (f"How much are driving lessons in {code}?", "£35 an hour, £70 for 2 hours, £350 for 10 hours (£320 NHS staff and students).")]
    return S(path, f"Driving Lessons {code} Solihull | £35/hr | SQ Driving School", "Postcode district", (code, path), f"Driving lessons in {code}",
             f"Driving lessons in {code} ({areas.split(',')[0]} and more): £35/hr manual or automatic, nearest test centre {c['name']}, local roads and schools.",
             [("£35", "per hour"), (code, "postcode"), (f"{c['rate']}%", c["name"] + " pass rate"), ("Free", "Student Portal")],
             [f"{code} covers {areas}.", f"Usual test centre: {c['name']}.", f"Main roads: {', '.join(roads[:2])}.", "Free DriveSQ Student Portal with every lesson."],
             body, faqs, [SRC[c["src"]], SRC["census"], SRC["find"]], [(f"solihull/driving-lessons-{slugs[0]}.html", "Area", f"Driving lessons in {names.get(slugs[0], slugs[0])}", "Local guide.")])


# ============================================================ SCHOOLS & COLLEGES
SCHOOLS = [
    ("tudor-grange-academy", "Tudor Grange Academy", "Dingle Lane, Solihull B91 3PD", True, "shirley", "About 1,700 pupils aged 11–18. Dingle Lane meets Blossomfield Road at a junction being changed from a roundabout to traffic signals.", ["Dingle Lane", "Blossomfield Road (B4102)"]),
    ("alderbrook-school", "Alderbrook School", "Blossomfield Road, Solihull B91 1SN", True, "shirley", "About 1,700 pupils; its sixth form opened in 2015. Next door to Solihull College's Blossomfield campus — some of the busiest student traffic in the borough.", ["Blossomfield Road (B4102)", "Dingle Lane"]),
    ("arden-academy", "Arden Academy", "Station Road, Knowle B93 0PT", True, "shirley", "About 1,800 pupils aged 11–18. The Knowle Society notes Station Road drop-offs cause congestion; parts of Station Road are 20mph.", ["Station Road", "Warwick Road (A4141, 20mph)"]),
    ("light-hall-school", "Light Hall School", "Hathaway Road, Shirley B90 2PZ", None, "shirley", "About 1,050 pupils, a short drive from Shirley test centre.", ["Hathaway Road", "Haslucks Green Road", "Stratford Road (A34)"]),
    ("lode-heath-school", "Lode Heath School", "Lode Lane, Solihull B91 2HW", False, "shirley", "An 11–16 school on Lode Lane, the same road as Solihull Hospital and the JLR plant — bus lanes and shift traffic outside the gates.", ["Lode Lane (B425)", "Bus lanes"]),
    ("langley-school", "Langley School", "Kineton Green Road, Olton B92 7ER", None, "south-yardley", "An Olton school now advertising its first sixth form open evening, close to the A41 safety corridor.", ["Kineton Green Road", "A41 Warwick Road"]),
    ("lyndon-school", "Lyndon School", "Daylesford Road, Solihull B92 8EJ", False, "south-yardley", "An 11–16 school near Hobs Moat Road, whose junction with Ulleries Road topped the council's 2016–18 collision rankings.", ["Daylesford Road", "Hobs Moat Road"]),
    ("st-peters-catholic-school", "St Peter's Catholic School", "Whitefields Road, Solihull B91 3NZ", True, "shirley", "A Catholic secondary with a sixth form, near Widney and Monkspath.", ["Whitefields Road", "Monkspath Hall Road"]),
    ("heart-of-england-school", "Heart of England School", "Gipsy Lane, Balsall Common CV7 7FW", True, "shirley", "About 1,185 pupils aged 11–18. Balsall Common's streets went 20mph in 2024, and the A452 has an HS2 contraflow until August 2027.", ["Gipsy Lane", "Kenilworth Road (A452)"]),
    ("john-henry-newman-catholic-college", "John Henry Newman Catholic College", "Chelmsley Road, Chelmsley Wood B37 5GA", True, "garretts-green", "An 11–18 Catholic college in Chelmsley Wood; Garretts Green is the nearest test centre.", ["Chelmsley Road", "Chester Road (A452)"]),
    ("grace-academy-solihull", "Grace Academy Solihull", "Chapelhouse Road, Chelmsley Wood B37 5JS", True, "garretts-green", "An 11–18 academy in Chelmsley Wood.", ["Chapelhouse Road", "Chester Road (A452)"]),
    ("park-hall-academy", "Park Hall Academy", "Water Orton Road, Castle Bromwich B36 9HF", True, "garretts-green", "An 11–18 academy in Castle Bromwich, near the A452 and M6.", ["Water Orton Road", "Chester Road (A452)"]),
    ("tudor-grange-academy-kingshurst", "Tudor Grange Academy Kingshurst", "Cooks Lane, Kingshurst B37 6NU", True, "garretts-green", "About 1,150–1,200 pupils aged 11–18 — on Cooks Lane, a road that appears on Garretts Green test routes.", ["Cooks Lane", "Gilson Way"]),
    ("smiths-wood-academy", "Smith's Wood Academy", "Windward Way, Smith's Wood B36 0UE", None, "garretts-green", "A Smith's Wood academy beside Solihull College's Woodlands campus.", ["Windward Way", "A452 Collector Road"]),
    ("wmg-academy-solihull", "WMG Academy for Young Engineers", "Chelmsley Road, Chelmsley Wood B37 5FD", True, "garretts-green", "A specialist engineering academy — plenty of students heading for engineering jobs where a licence matters.", ["Chelmsley Road", "Chester Road (A452)"]),
    ("solihull-school", "Solihull School", "Warwick Road, Solihull B91 3DJ", True, "shirley", "An independent 11–18 school of about 1,100 pupils on the Warwick Road, near the town centre.", ["Warwick Road", "Solihull town centre"]),
    ("sixth-form-college-solihull", "The Sixth Form College Solihull", "Widney Manor Road, Solihull", True, "shirley", "About 2,400–2,500 students aged 16–19 taking A levels, BTECs and T levels; rated Good by Ofsted in March 2024. Widney Manor station is nearby.", ["Widney Manor Road", "Widney Lane"]),
    ("solihull-college-blossomfield", "Solihull College — Blossomfield campus", "Blossomfield Road, Solihull B91 1SB", True, "shirley", "A few minutes' walk from Solihull station, next to Alderbrook School. The college has over 5,000 learners aged 16–18 across its campuses.", ["Blossomfield Road (B4102)", "Station Road"]),
    ("solihull-college-woodlands", "Solihull College — Woodlands campus", "Auckland Drive, Smith's Wood B36 0NF", True, "garretts-green", "Off the A452 with free parking, three motor-vehicle workshops (including hybrid and electric) and aviation facilities with flight simulators.", ["Auckland Drive", "A452"]),
]


def school_page(s):
    slug, name, addr, sixth, centre, note, roads = s
    path = f"solihull/{slug}-driving-lessons.html"
    c = CEN[centre]
    sixth_txt = {True: "It has a sixth form, so many students turn 17 while still at school.", False: "It's an 11–16 school, so most learners start lessons after moving on to college or sixth form.", None: "Check with the school about sixth-form provision."}[sixth]
    body = f"""<p class="lead">Driving lessons for students at {name}, {addr}. We pick up from the school gates after lessons (once you're 17), plan around your timetable and exams, and give students 10 hours for £320.</p>
<h2>About {name}</h2><p>{note} {sixth_txt}</p>
<h2>Roads around {name}</h2><ul>{''.join(f'<li>{r}</li>' for r in roads)}</ul><p>Solihull is rolling out 20mph limits at every school location (the first order took effect on 28 August 2025). Driving past schools at home time is excellent hazard-perception training.</p>
<h2>When to start</h2><ol class="rx-steps"><li data-n="1"><h4>Apply for your provisional licence at 15 years 9 months</h4><p>So it arrives in time for your 17th birthday.</p></li><li data-n="2"><h4>Start theory early</h4><p>The DriveSQ Student Portal includes a theory library and 50-question mock tests.</p></li><li data-n="3"><h4>First lesson on your 17th birthday</h4><p>We pick up from school, home or college.</p></li><li data-n="4"><h4>Test around exams</h4><p>Most students test at <a href="{c['slug']}-driving-test-centre-routes.html">{c['name']}</a> ({c['rate']}% pass rate in 2024-25). Avoid booking during exam season.</p></li></ol>
{portal_strip()}
<p class="note">SQ Driving School is independent of {name}; this page is a guide for its students and parents.</p>"""
    faqs = [(f"Can you pick me up from {name}?", "Yes — from the school gates once you're 17, as well as from home."), ("Is there a student discount?", "Yes: 10 hours for £320 instead of £350."),
            ("When can I start driving lessons?", "From your 17th birthday, with a provisional licence (apply from 15 years 9 months).")]
    return S(path, f"Driving Lessons for {name} Students | Solihull | SQ", "Students", (name, path), f"Driving lessons for {name} students",
             f"Driving lessons for {name} students ({addr.split(',')[-1].strip()}): pick-up from school, 10 hours for £320, nearest test centre {c['name']} and the free DriveSQ Student Portal.",
             [("£320", "10 hours, students"), (c["name"], "nearest test centre"), ("17", "minimum age"), ("Free", "Student Portal")],
             [f"Pick-up from {name} after school.", "Student price: 10 hours for £320.", f"Nearest test centre: {c['name']}.", "Theory practice in the free DriveSQ Student Portal."],
             body, faqs, [SIXTH, GIAS, PROV, SRC[c["src"]]], [("solihull/student-driving-lessons-solihull.html", "Students", "Student driving lessons in Solihull", "All colleges and schools.")])


# ============================================================ EMPLOYERS
JOBS = [
    ("jlr-solihull", "JLR Solihull", "Lode Lane, Solihull B92 8NW", "The 300-acre plant — JLR's largest — builds Range Rover models. Older reports put the workforce at 9,000–10,000, and JLR has described a three-shift, 24-hour pattern five days a week.",
     "Shifts that start or end outside bus hours. Lode Lane has camera-enforced bus lanes and new Sprint signals; JLR also has entrances on Damson Parkway.", "south-yardley", [("JLR — where we are", "https://careers.jaguarlandrover.com/where-we-are/united-kingdom")]),
    ("birmingham-airport", "Birmingham Airport", "B26 3QJ (Elmdon)", "More than 150 companies on site employ around 9,000 people. Shift work is common — for example 12-hour 6am–6pm and 6pm–6am patterns at some employers.",
     "A rail campaign noted the first trains (around 05:40 and 06:05) arrive too late for early flights and staff. The airport wants 33% of staff not driving alone by 2028 — but for 4am starts, a licence is often the only practical option.", "garretts-green", [("Birmingham Airport — staff travel", "https://www.birminghamairport.co.uk/transport-links/staff-travel/")]),
    ("nec-birmingham", "The NEC", "Bickenhill Lane, B40 1NT", "Europe-scale exhibition venue reached from M42 junction 6 via the A45. Event days mean heavy traffic and changing layouts.",
     "Event build-ups and breakdowns run late into the night; Birmingham International station is a 5-minute covered walk, but late finishes can miss the last convenient trains.", "garretts-green", [("National Highways — M42 J6", "https://nationalhighways.co.uk/projects/m42-junction-6-improvement")]),
    ("resorts-world-birmingham", "Resorts World Birmingham", "Pendigo Way, B40 1PU", "On the NEC campus. Recruitment around launch was for about 1,100 jobs, and current roles include night, weekend and bank-holiday shifts with free on-site staff parking.",
     "Night shifts plus free staff parking make driving the obvious way to get to work.", "garretts-green", [("DWP Find a Job — Resorts World role", "https://findajob.dwp.gov.uk/details/17814028")]),
    ("blythe-valley-park", "Blythe Valley Park", "M42 junction 4, Shirley (B90 8)", "More than 25 businesses and around 3,500 staff beside M42 junction 4 and the A34.",
     "It's 2 minutes from Shirley test centre's roads — learners working here can practise the A34 on their commute.", "shirley", [("UK Central — Blythe Valley", "https://www.investinukcentral.com/blythe-valley")]),
    ("birmingham-business-park", "Birmingham Business Park", "Solihull Parkway, B37 7", "Around 116–120 companies and more than 7,000 staff off M42 junction 6 and M6 junction 4. The new A4545 link (December 2024) gives direct access.",
     "Office hours, but a site built around car and motorway access.", "garretts-green", [("Birmingham Business Park (Wikipedia)", "https://en.wikipedia.org/wiki/Birmingham_Business_Park")]),
    ("solihull-hospital", "Solihull Hospital", "Lode Lane, Solihull B91 2JL", "Near M42 junction 5, the A41 and the A34, with one main visitor car park that gets congested at peak times.",
     "NHS staff get 10 hours for £320. We plan lessons around early, late and night shifts.", "shirley", [("UHB — Solihull Hospital by car", "https://www.uhb.nhs.uk/getting-here/solihull-hospital/by-car/")]),
    ("heartlands-hospital", "Heartlands Hospital", "Bordesley Green East, Birmingham B9 5SS", "Run by UHB, with 981 on-site and 784 off-site staff parking spaces, permit waiting lists and a winter shuttle from November to February.",
     "Many north Solihull NHS staff work here. NHS staff get 10 hours for £320.", "garretts-green", [("UHB — staff parking passes and permits", "https://www.uhb.nhs.uk/getting-here/getting-to-work/driving-to-work/parking-passes-and-permits/")]),
]


def job_page(j):
    slug, name, addr, about, why, centre, src = j
    path = f"solihull/{slug}-driving-lessons.html"
    c = CEN[centre]
    nhs = "hospital" in slug
    body = f"""<p class="lead">Driving lessons for people who work at {name} ({addr}). We fit lessons around shifts — early mornings, evenings and days off — and pick up from home or work.</p>
<h2>Getting to work at {name}</h2><p>{about}</p><p>{why}</p>
<h2>Shift-friendly lessons</h2><ul class="check"><li>2-hour lessons on days off to make faster progress.</li><li>Never straight after a night shift — tiredness slows reactions (see our <a href="../driving/stopping-distances-calculator.html">stopping distance calculator</a>).</li><li>Lessons can start or finish at {name}.</li>{'<li><b>NHS staff: 10 hours for £320.</b></li>' if nhs else ''}</ul>
<h2>Test centre</h2><p>The nearest test centre is usually <a href="{c['slug']}-driving-test-centre-routes.html">{c['full']}</a>.</p>
{portal_strip()}
<p class="note">SQ Driving School is independent of {name}.</p>"""
    faqs = [(f"Can I have driving lessons around my shifts at {name}?", "Yes — early, late, evening and weekend slots."), ("How much are lessons?", "£35 an hour, £350 for 10 hours" + (" (£320 for NHS staff)." if nhs else "."))]
    return S(path, f"Driving Lessons for {name} Staff | Shift-Friendly | SQ Solihull", "Work", (name, path), f"Driving lessons for {name} staff",
             f"Shift-friendly driving lessons for people working at {name}: early, late and weekend slots, pick-up from work, and the free DriveSQ Student Portal.",
             [("£35", "per hour"), ("Shifts", "early & late slots"), (c["name"], "test centre"), ("Free", "Student Portal")],
             [f"Lessons planned around {name} shifts.", "Pick-up from home or work.", f"Usual test centre: {c['name']}.", "Track progress in the DriveSQ Student Portal."],
             body, faqs, [tuple(x) for x in src] + [SRC[c["src"]]], [("solihull/nhs-driving-lessons-solihull.html" if nhs else "solihull/intensive-driving-courses-solihull.html", "Lessons", "NHS staff lessons" if nhs else "Intensive courses", "Pass faster.")])


# ============================================================ LESSON TYPES, PRICES, PORTALS
def L(slug, title, seo, desc, stats, keys, body, faqs, src=("lessons", "cost", "book")):
    path = f"solihull/{slug}.html"
    return path, S(path, seo, "Lessons in Solihull", (title.replace(" in Solihull", ""), path), title, desc, stats, keys, body + portal_strip(), faqs,
                   [SRC[k] if isinstance(k, str) else k for k in src], [("driving-lessons-solihull.html", "Solihull", "Driving lessons in Solihull", "All areas and prices.")])


def lesson_pages():
    out = {}
    pages = [
        L("driving-lesson-prices-solihull", "Driving lesson prices in Solihull", "Driving Lesson Prices Solihull 2026 | £35/hr, No Booking Fees | SQ",
          "Driving lesson prices in Solihull for 2026: £35/hr manual or automatic, £70 for 2 hours, £350 for 10 hours (£320 NHS & students), no booking fees — plus what Solihull schools typically charge.",
          [("£35", "per hour"), ("£0", "booking fees"), ("£350", "10 hours"), ("£320", "NHS & students")],
          ["£35 an hour, manual or automatic — same price.", "No booking fees, no fuel surcharges.", "10 hours £350, or £320 for NHS staff and students.", "Typical advertised Solihull rates: roughly £32–£42 an hour."],
          """<p class="lead">One clear price list — no booking fees, no "from" prices, no surcharge for automatic.</p>
<div class="rx-table-wrap"><table class="rx-table"><thead><tr><th>What</th><th>Price</th><th>Per hour</th></tr></thead><tbody>
<tr><td>Single 1-hour lesson (manual or automatic)</td><td><b>£40</b></td><td>£40</td></tr><tr><td>2-hour lesson</td><td><b>£70</b></td><td>£35</td></tr>
<tr><td>10-hour block</td><td><b>£350</b></td><td>£35</td></tr><tr><td>10-hour block — NHS staff and students</td><td><b>£320</b></td><td>£32</td></tr>
<tr><td>DriveSQ Student Portal</td><td><b>Free</b></td><td>—</td></tr><tr><td>Booking fee</td><td><b>£0</b></td><td>—</td></tr></tbody></table></div>
<h2>What does learning to drive cost in Solihull?</h2><p>Using the DVSA's average of about 45 hours of lessons, that's around £1,575 at £35/hr — less with blocks — plus the £23 theory test and £62 weekday practical test (£75 evenings, weekends and bank holidays). Use our <a href="../driving/learning-to-drive-timeline-planner.html">timeline planner</a> for your own numbers.</p>
<h2>How Solihull prices compare</h2><p>We looked at advertised prices from driving schools and national providers covering Solihull in October 2026. Advertised single-hour rates mostly clustered around £32–£36, with a range of roughly £27–£42; 10-hour blocks ranged from about £300 to £410. Some providers don't publish a price at all, and some add a booking fee. Check exactly what's included before you compare.</p>
<h2>What's included at SQ</h2><ul class="check"><li>Door-to-door pick-up across Solihull.</li><li>Dual-controlled car.</li><li>Free DriveSQ Student Portal: 23 skills, theory library, mock tests.</li><li>Test-route practice for Shirley, Garretts Green and others.</li></ul>""",
          [("How much are driving lessons in Solihull?", "£35 an hour with SQ, manual or automatic; £350 for 10 hours (£320 for NHS staff and students)."), ("Do you charge a booking fee?", "No."), ("Is automatic more expensive?", "No — the same £35 an hour.")], ("lessons", "cost", "book")),
        L("nervous-driver-lessons-solihull", "Nervous driver lessons in Solihull", "Nervous Driver Lessons Solihull | Calm, Patient Instructors | SQ",
          "Driving lessons for nervous and anxious learners in Solihull: quiet first lessons in Dorridge or Hillfield, automatic option, no pressure, and progress you can see in the DriveSQ Student Portal.",
          [("Quiet", "first-lesson roads"), ("Auto", "option, same price"), ("23", "skills tracked"), ("£35", "per hour")],
          ["We start on quiet residential roads.", "Automatic removes clutch worries.", "You see your own progress in the Student Portal.", "Nothing new until you're ready."],
          """<p class="lead">Nerves are normal — and very manageable. We'll start where you're comfortable and only move on when you are.</p>
<h2>Quiet places to start in Solihull</h2><p>Dorridge's wide residential roads, Hillfield's estates near the park, Cheswick Green's village lanes — all calm places for your first lessons. Busy roads like the A34 come much later.</p>
<h2>Seeing your progress helps</h2><p>Anxious learners often feel they're not improving. The DriveSQ Student Portal shows every skill moving from "introduced" to "independent" — proof that you're getting there.</p>
<h2>Automatic can help</h2><p>No clutch, no stalling. Same £35 an hour. See <a href="automatic-driving-lessons-solihull.html">automatic lessons</a>.</p>
<p>Read more in our guide to <a href="../knowledge/learning-to-drive-with-dyslexia-adhd-or-anxiety.html">learning to drive with anxiety, dyslexia or ADHD</a>.</p>""",
          [("Do you teach nervous drivers in Solihull?", "Yes — we start on quiet roads and go at your pace."), ("Is automatic better for nervous learners?", "Often, because there's no clutch or stalling.")]),
        L("refresher-driving-lessons-solihull", "Refresher driving lessons in Solihull", "Refresher Driving Lessons Solihull | Get Confident Again | SQ",
          "Refresher lessons in Solihull for qualified drivers who haven't driven for a while: the new 20mph limits, A34 cameras, the M42 junctions and Solihull town centre's bus-only streets.",
          [("2025", "new A41 limits"), ("J5A", "new M42 junction"), ("£35", "per hour"), ("Your car", "or ours")],
          ["Ideal if you passed years ago or moved to Solihull.", "Catch up on new limits, cameras and junctions.", "Motorway confidence on the M42.", "Lessons in our dual-controlled car."],
          """<p class="lead">Passed years ago? New to Solihull? Solihull's roads have changed a lot recently — refresher lessons get you confident again.</p>
<h2>What's changed in Solihull</h2><ul><li>A34 average speed cameras (2023) and a U-turn camera (2026). <a href="a34-stratford-road-shirley.html">A34 guide</a></li><li>New 20mph and 30mph limits on the A41 corridor (2025). <a href="a41-warwick-road-olton-solihull.html">A41 guide</a></li><li>New M42 junction 5A and the A4545 (2024). <a href="m42-junctions-3a-4-5-6-solihull.html">M42 guide</a></li><li>Bus-only streets in the town centre. <a href="solihull-town-centre-driving-guide.html">Town centre guide</a></li><li>Village 20mph limits. <a href="knowle-dorridge-and-village-speed-limits.html">Village guide</a></li></ul>
<h2>Highway Code changes</h2><p>The 2022 Highway Code changes introduced the hierarchy of road users and new priorities for pedestrians at junctions. <a href="../knowledge/highway-code-2022-changes.html">What changed</a>.</p>""",
          [("How many refresher lessons do I need?", "Most people need a few hours; we'll assess you on the first lesson."), ("Can I have refresher lessons on the motorway?", "Yes — the M42 is minutes away.")]),
        L("pass-plus-solihull", "Pass Plus in Solihull", "Pass Plus Solihull | Motorway, Night & Rural Driving | SQ",
          "Pass Plus in Solihull after you pass: motorway driving on the M42, night driving, rural lanes around Knowle and Balsall Common, and town driving.",
          [("6", "modules"), ("M42", "motorway module"), ("Rural", "Knowle & Balsall Common"), ("New", "drivers")],
          ["Pass Plus covers town, all-weather, rural, night, dual carriageways and motorways.", "Solihull has all of them within minutes.", "Some insurers offer discounts — check yours.", "Perfect after passing at Shirley."],
          """<p class="lead">Pass Plus is a short practical course for new drivers. Solihull is ideal: the M42, fast dual carriageways like the A45, rural lanes and a busy town centre all within a few miles.</p>
<h2>The six modules</h2><ol class="rx-steps"><li data-n="1"><h4>Town</h4><p>Solihull town centre and Shirley.</p></li><li data-n="2"><h4>All weathers</h4><p>Whatever the day brings.</p></li><li data-n="3"><h4>Rural roads</h4><p>Lanes around Knowle, Hockley Heath and Balsall Common.</p></li><li data-n="4"><h4>At night</h4><p>Unlit lanes and town at night.</p></li><li data-n="5"><h4>Dual carriageways</h4><p>A45 and A452.</p></li><li data-n="6"><h4>Motorways</h4><p>M42 junctions 4–6 — smart-motorway signs and the new J5A.</p></li></ol>""",
          [("Is Pass Plus worth it in Solihull?", "It builds confidence on the M42, at night and on rural lanes; some insurers offer discounts."), ("How long is Pass Plus?", "It's normally at least 6 hours.")], ("lessons", "motorway", "book")),
        L("mock-driving-test-solihull", "Mock driving tests in Solihull", "Mock Driving Test Solihull | Shirley & Garretts Green Routes | SQ",
          "A full mock driving test in Solihull, marked like the real DVSA sheet, on the roads around Shirley or Garretts Green — with results saved in your DriveSQ Student Portal.",
          [("40 min", "like the real test"), ("DVSA", "style marking"), ("Shirley", "or Garretts Green roads"), ("Portal", "results saved")],
          ["Same format as the real test: eyesight, show me/tell me, 40 minutes of driving.", "Marked on DVSA categories.", "On your test centre's roads.", "Results saved in your Student Portal."],
          """<p class="lead">The best predictor of passing is passing a realistic mock test. Ours follows the real test exactly — on the roads around your test centre.</p>
<h2>What happens</h2><ol class="rx-steps"><li data-n="1"><h4>Eyesight check</h4><p>Number plate at 20 metres.</p></li><li data-n="2"><h4>Show me, tell me</h4><p>Vehicle safety questions.</p></li><li data-n="3"><h4>About 40 minutes driving</h4><p>Including about 20 minutes of independent driving and a manoeuvre.</p></li><li data-n="4"><h4>Marked debrief</h4><p>Driving, serious and dangerous faults — saved in your Student Portal.</p></li></ol>
<p>Practise for Shirley with our <a href="shirley-driving-test-centre-routes.html">Shirley route guide</a>, or <a href="garretts-green-driving-test-centre-routes.html">Garretts Green</a>.</p>""",
          [("How much is a mock test?", "It's charged at our normal lesson rate."), ("Where is the mock test?", "On the roads around your chosen test centre.")]),
        L("driving-test-cancellations-shirley", "Driving test cancellations at Shirley: how to find an earlier test", "Shirley Driving Test Cancellations: Find an Earlier Date Safely | SQ",
          "How to find an earlier driving test at Shirley or nearby centres safely: checking GOV.UK yourself, the 2026 booking rules, avoiding paid 'cancellation finder' traps, and being test-ready first.",
          [("2", "changes per booking (2026)"), ("3", "nearest-centre rule"), ("GOV.UK", "only official site"), ("£62", "weekday test")],
          ["Only book and change tests on GOV.UK.", "Since 2026 you can usually change a booking twice.", "A booked test can only move to one of the three nearest centres.", "Make sure you're ready before chasing an early date."],
          """<p class="lead">Shirley had the area's best pass rate in 2024-25, so it's popular. Here's how to find an earlier date — honestly and safely.</p>
<h2>Check GOV.UK yourself</h2><p>Cancellations appear on the official booking service. Checking regularly — especially early mornings — is free.</p>
<h2>Know the 2026 rules</h2><p>Since 31 March 2026 a booking can normally be changed twice, and since 9 June 2026 a booked test can only move to one of the three centres nearest it. See <a href="../knowledge/driving-test-booking-rules-2026.html">the 2026 rules</a>.</p>
<h2>Be careful with paid services</h2><p>Some third-party services charge to find or resell tests. The DVSA has acted against test resellers. Never share your licence details with a site you don't trust.</p>
<h2>Be ready first</h2><p>An earlier date only helps if you'll pass. Your DriveSQ Student Portal shows when all 23 skills are at test standard — and a <a href="mock-driving-test-solihull.html">mock test</a> confirms it.</p>""",
          [("How do I get a cancellation at Shirley test centre?", "Check the official GOV.UK service regularly — cancellations appear there."), ("How many times can I change my driving test?", "Normally twice since 31 March 2026.")], ("book", "cost")),
        L("adult-driving-lessons-solihull", "Adult and over-50s driving lessons in Solihull", "Adult & Over 50s Driving Lessons Solihull | Learn at Any Age | SQ",
          "Driving lessons for adults and over-50s in Solihull — first-time learners, people who moved to the UK, and those returning after years away — with patient instructors and lessons at your pace.",
          [("Any age", "never too late"), ("£35", "per hour"), ("Auto", "option"), ("Portal", "see your progress")],
          ["It's never too late to learn.", "Lessons around work and family.", "Automatic is popular with adult learners.", "Moved to the UK? See licence exchange rules."],
          """<p class="lead">More adults are learning to drive than ever — after a move, a new job, a family change or simply deciding it's time. We teach at your pace, without judgement.</p>
<h2>Who we teach</h2><ul><li>First-time learners in their 20s, 30s, 40s, 50s and beyond.</li><li>People who drove abroad — see <a href="../knowledge/foreign-licence-exchange-uk.html">exchanging a foreign licence</a>.</li><li>Drivers returning after many years — see <a href="refresher-driving-lessons-solihull.html">refresher lessons</a>.</li></ul>
<h2>Why many adults choose automatic</h2><p>Fewer things to coordinate, no stalling, and often fewer hours. Same £35 an hour.</p>""",
          [("Am I too old to learn to drive?", "No — there's no upper age limit."), ("Can I learn in an automatic?", "Yes, at the same price.")]),
        L("evening-weekend-driving-lessons-solihull", "Evening and weekend driving lessons in Solihull", "Evening & Weekend Driving Lessons Solihull | SQ Driving School",
          "Evening and weekend driving lessons across Solihull for people who work or study — including dark-evening practice and quieter weekend roads for beginners.",
          [("Evenings", "after work/college"), ("Weekends", "quieter roads"), ("£35", "per hour"), ("£75", "weekend test fee")],
          ["Lessons after work, college or school.", "Weekend mornings are quieter for beginners.", "Evening lessons in winter give night-driving practice.", "Weekend and evening tests cost £75 (weekday £62)."],
          """<p class="lead">Work 9 to 5? At college all day? Evening and weekend lessons fit around you.</p>
<h2>Why evenings are useful</h2><p>From late October, evening lessons in Solihull are in the dark — valuable practice with dipped headlights, judging speed at night and spotting pedestrians. Our <a href="../driving/driving-test-day-planner.html">test day planner</a> shows sunrise and sunset for your date.</p>
<h2>Why weekends are useful</h2><p>Quieter roads for beginners — and the A34 and town centre are calmer on Sunday mornings.</p>""",
          [("Do you offer weekend driving lessons in Solihull?", "Yes."), ("Do evening and weekend tests cost more?", "Yes — £75 instead of £62 for a weekday test.")], ("lessons", "cost", "book")),
        L("semi-intensive-driving-course-solihull", "Semi-intensive driving courses in Solihull", "Semi-Intensive Driving Course Solihull | 6–10 Hours a Week | SQ",
          "Semi-intensive driving courses in Solihull — 6 to 10 hours a week, ideal for beginners who want to pass in weeks rather than months, at £35/hr.",
          [("6–10", "hours a week"), ("£35", "per hour"), ("Weeks", "not months"), ("Shirley", "58.1%")],
          ["Faster than weekly lessons, gentler than a one-week intensive.", "Ideal for beginners.", "Same £35 an hour.", "Planned around a test date."],
          """<p class="lead">A semi-intensive course is the sweet spot for many beginners: 6–10 hours a week, so you don't forget between lessons, without the pressure of a one-week crash course.</p>
<h2>How it compares</h2><div class="rx-table-wrap"><table class="rx-table"><thead><tr><th>Plan</th><th>Hours a week</th><th>45 hours takes</th></tr></thead><tbody><tr><td>Weekly lessons</td><td>2</td><td>About 23 weeks</td></tr><tr><td><b>Semi-intensive</b></td><td><b>6–10</b></td><td><b>About 5–8 weeks</b></td></tr><tr><td>Intensive</td><td>15–30</td><td>About 2–3 weeks</td></tr></tbody></table></div>
<p>See also <a href="intensive-driving-courses-solihull.html">intensive courses</a>.</p>""",
          [("What is a semi-intensive driving course?", "Around 6–10 hours of lessons a week, so you progress quickly without a one-week crash course."), ("How much does it cost?", "£35 an hour — no premium.")]),
    ]
    for p, h in pages:
        out[p] = h
    # portals
    sp = "solihull/drivesq-student-portal-solihull.html"
    out[sp] = S(sp, "DriveSQ Student Portal for Solihull Learners | Track Every Skill | SQ", "DriveSQ Student Portal", ("Student Portal", sp),
                "The DriveSQ Student Portal for Solihull learners", "Free with every SQ lesson in Solihull: 23 driving skills tracked after every lesson, theory library, 50-question mock tests, a test-readiness checklist and messages with your instructor.",
                [("23", "skills tracked"), ("50", "question mock tests"), ("Free", "with lessons"), ("24/7", "on your phone")],
                ["Free for every SQ Driving School learner in Solihull.", "See all 23 skills move from introduced to independent.", "Theory library and mock tests built in.", "Know when you're ready for Shirley or Garretts Green."],
                f"""<p class="lead">Most driving schools give you a lesson and a "see you next week". With SQ — part of DriveSQ — you get the DriveSQ Student Portal: a clear record of where you are, what's left and when you're test-ready.</p>
<h2>What's inside</h2><div class="rt-marks"><div class="rt-mark"><b>23 driving skills</b><small>Recorded by your instructor after every lesson — from moving off to roundabouts and manoeuvres.</small></div><div class="rt-mark"><b>Theory library</b><small>Revise the Highway Code and road signs.</small></div><div class="rt-mark"><b>50-question mock tests</b><small>Like the real multiple-choice test (pass mark 43).</small></div><div class="rt-mark"><b>Test-readiness checklist</b><small>Know when to book Shirley — not guess.</small></div><div class="rt-mark"><b>Instructor messaging</b><small>Lesson times and questions in one place.</small></div></div>
<h2>Why it matters in Solihull</h2><p>Shirley test centre had the area's best pass rate in 2024-25 (58.1%) — but only for learners who turn up ready. The portal makes "ready" visible.</p>
<p><a class="btn btn--red" href="{STUDENT}" target="_blank" rel="noopener">Student login ↗</a> <a class="btn btn--ghost" href="../student-portal.html">How it works</a></p>{portal_strip()}""",
                [("Is the DriveSQ Student Portal free?", "Yes, for every SQ Driving School learner."), ("Can my parents see my progress?", "You can share your progress with them from the portal.")],
                [SRC["lessons"], SRC["pr_shirley"]], [("solihull/drivesq-instructor-portal-solihull.html", "Instructors", "DriveSQ Instructor Portal", "For Solihull instructors.")])
    ip = "solihull/drivesq-instructor-portal-solihull.html"
    out[ip] = S(ip, "DriveSQ Instructor Portal | Driving Instructors in Solihull | SQ", "DriveSQ Instructor Portal", ("Instructor Portal", ip),
                "The DriveSQ Instructor Portal for Solihull instructors", "How the DriveSQ Instructor Portal works for driving instructors in Solihull: learners matched by postcode, diary and bookings, skill records, messaging — and how to join.",
                [("Postcode", "learner matching"), ("1", "dashboard"), ("23", "skills to record"), ("B90–B94", "B36, B37")],
                ["Learners from DriveSQ and SQ bookings are matched to instructors by postcode.", "Diary, pupils, progress and messages in one dashboard.", "Your pupils see what you record in their Student Portal.", "DriveSQ is growing in Solihull and taking on ADIs."],
                f"""<p class="lead">Every SQ Driving School and DriveSQ instructor runs their teaching from the DriveSQ Instructor Portal — and in Solihull, that's how new learners reach you.</p>
<h2>What instructors get</h2><div class="rt-marks"><div class="rt-mark"><b>Learners by postcode</b><small>Bookings from both websites are matched to the nearest suitable instructor.</small></div><div class="rt-mark"><b>Diary and bookings</b><small>All your lessons in one place.</small></div><div class="rt-mark"><b>Skill records</b><small>Record 23 skills after each lesson — your pupils see them instantly.</small></div><div class="rt-mark"><b>Messaging</b><small>Talk to pupils without sharing personal numbers.</small></div></div>
<h2>Teach in Solihull</h2><p>We're taking on ADIs across Shirley, Solihull, Knowle, Dorridge, Olton, Chelmsley Wood and the villages. See <a href="https://www.drivesq.co.uk/driving-instructor-jobs-solihull.html">driving instructor jobs in Solihull</a>.</p>
<p><a class="btn btn--red" href="{INSTR}" target="_blank" rel="noopener">Instructor login ↗</a></p>{portal_strip()}""",
                [("How do instructors get pupils in Solihull?", "Bookings are matched by postcode through the DriveSQ system."), ("Is DriveSQ recruiting in Solihull?", "Yes — ADIs, manual and automatic.")],
                [("GOV.UK — Become a driving instructor", "https://www.gov.uk/become-driving-instructor")], [("solihull/drivesq-student-portal-solihull.html", "Learners", "DriveSQ Student Portal", "For Solihull learners.")])
    return out


def hub_extra():
    """Directory page linking every batch-2 page (also linked from the pillar)."""
    path = "solihull/all-solihull-guides.html"
    sec = lambda t, items: f'<h2>{t}</h2><div class="hero__badges">' + "".join(f'<a class="chip" href="{h}">{n}</a>' for h, n in items) + "</div>"
    body = "<p class=\"lead\">Every SQ Driving School guide for Solihull in one place — areas, postcodes, test centres, roads, schools, workplaces and lesson types.</p>"
    body += sec("Areas", [(f"driving-lessons-{a['slug']}.html", a["name"]) for a in SOL.AREAS])
    body += sec("Postcode districts", [(f"{p[0].lower()}-driving-lessons.html", p[0]) for p in PCS])
    body += sec("Test centres", [(f"{c['slug']}-driving-test-centre-routes.html", c["name"]) for c in CENTRES] + [("solihull-driving-test-centres-compared.html", "Compare all")])
    import pages_sol_roads as RD
    body += sec("Road guides", [(f"{r['slug']}.html", r["short"]) for r in RD.ROADS])
    body += sec("Schools & colleges", [(f"{s[0]}-driving-lessons.html", s[1]) for s in SCHOOLS])
    body += sec("Workplaces", [(f"{j[0]}-driving-lessons.html", j[1]) for j in JOBS])
    # every lesson-type page (both batches + the gap pages)
    import re as _re, pages_sol_gaps as GAPS
    _lt = {}
    for _src in (SOL.lesson_pages(), lesson_pages(), GAPS.gap_pages()):
        for _p, _h in _src.items():
            _m = _re.search(r"<h1[^>]*>(.*?)</h1>", _h, _re.S)
            _lt[_p.split("/")[-1]] = _re.sub(r"<[^>]+>", "", _m.group(1)).strip().rstrip(".") if _m else _p
    body += sec("Lesson types", sorted(_lt.items(), key=lambda x: x[1]))
    body += sec("DriveSQ Solihull tools &amp; guides", [(u, t) for u, c, t, d in SOL.DSQ_ALL])
    body += portal_strip()
    return {path: S(path, "All Solihull Driving Guides | Areas, Tests, Roads & Schools | SQ", "Solihull guides", ("All guides", path), "Every Solihull driving guide",
                    "Directory of every SQ Driving School guide to Solihull: 33 areas, 9 postcode districts, 4 test centres, 10 road guides, 19 schools and colleges and 8 workplaces.",
                    [(str(len(SOL.AREAS)), "areas"), ("9", "postcodes"), ("10", "road guides"), (str(len(SCHOOLS)), "schools & colleges")],
                    ["Every Solihull guide in one place.", "All researched and sourced.", "Booking on every page.", "Free DriveSQ Student Portal."], body,
                    [("How many areas of Solihull do you cover?", f"{len(SOL.AREAS)} areas across B90–B94, B36, B37, B40 and CV7.")], [SRC["census"], LGBCE], [])}


def all_pages():
    out = {}
    for p in PCS:
        out[f"solihull/{p[0].lower()}-driving-lessons.html"] = pc_page(*p)
    for s in SCHOOLS:
        out[f"solihull/{s[0]}-driving-lessons.html"] = school_page(s)
    for j in JOBS:
        out[f"solihull/{j[0]}-driving-lessons.html"] = job_page(j)
    out.update(lesson_pages())
    out.update(hub_extra())
    return out
