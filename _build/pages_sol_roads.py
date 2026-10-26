"""Solihull road & junction guides for learner drivers (solihull/).

Every fact is from Solihull Council traffic orders and notices, National Highways, TfWM, HS2, West Midlands PCC
or parish councils (cited per page). Layout detail we couldn't verify is described in general terms only."""
from hub_shell import *
import pages_solihull as SOL

C = {
    "pcc_cam": ("West Midlands PCC — average speed cameras on the A34 in Solihull", "https://www.westmidlands-pcc.gov.uk/pcc-welcomes-new-average-speed-cameras-in-solihull"),
    "villages_cam": ("Solihull Council — new average speed cameras in villages", "https://www.solihull.gov.uk/news/villages-solihull-borough-get-new-average-speed-cameras"),
    "mte": ("Solihull Council — moving traffic enforcement", "https://www.solihull.gov.uk/parking/parking-bus-lane-and-moving-traffic-fines/moving-traffic-enforcement"),
    "mte_news": ("Solihull Council — moving traffic enforcement gears up (2026)", "https://www.solihull.gov.uk/news/2026/solihull-council-gears-moving-traffic-enforcement"),
    "ranked": ("Solihull Council — ranked collision sites (2016–18 data)", "https://www.solihull.gov.uk/sites/default/files/migrated/Portals_0_ParkingTravelRoads%252FRanked_Single_Sites.pdf"),
    "dkl": ("Solihull Council — Dog Kennel Lane red route proposal (2021)", "https://www.solihull.gov.uk/sites/default/files/2021-03/Dog-Kennel-Lane-Shirley-RR-March-2021-PROPOSAL-NOTICE.pdf"),
    "a34_tr229": ("Solihull Council — A34 Stratford Road closure notice, Feb 2026", "https://www.solihull.gov.uk/sites/default/files/2026-02/TR229-2025-Stratford-Road-TTRN-Notice.pdf"),
    "j4": ("roads.org.uk — M42 junction 4 (Monkspath Interchange)", "https://www.roads.org.uk/motorway/m42/150"),
    "j5": ("roads.org.uk — M42 junction 5", "https://www.roads.org.uk/motorway/m42/140"),
    "m42atm": ("Express & Star — M42 hard shoulder running", "https://www.expressandstar.com/news/m42-drivers-given-hard-shoulder-6525935"),
    "j6": ("National Highways — M42 junction 6 improvement", "https://nationalhighways.co.uk/projects/m42-junction-6-improvement"),
    "j6news": ("Highways Magazine — new M42 link opens", "https://www.highwaysmagazine.co.uk/National-Highways-beats-the-clock-with-new-M42-link/14275"),
    "j3a": ("Henley-in-Arden PC — M40/M42 interchange update (2023)", "https://www.henley-in-arden-pc.gov.uk/wp-content/uploads/2023/10/2023.10.05-M40-M42-Interchange-Stakeholder-Update-Letter-FINAL.pdf"),
    "m42worst": ("Express & Star — M42 ranked England's worst motorway (Transport Focus)", "https://www.expressandstar.com/uk-news/m42-is-ranked-englands-worst-motorway-thanks-to-potholes-and-delays-5757048"),
    "cdb": ("Solihull Council — Catherine de Barnes Lane / Bickenhill speed limits (2025)", "https://www.solihull.gov.uk/sites/default/files/2025-09/Catherine-de-Barnes-Lane-Bickenhill-Village-Speed-Limits-July-2025-IMP-NOTICE.pdf"),
    "sprint": ("TfWM — Sprint", "https://www.tfwm.org.uk/sprint/"),
    "a45works": ("TfWM — A45 Sprint works", "https://tfwm.org.uk/plan-your-journey/major-roadworks-and-events/sprint/a45-works"),
    "a45_30": ("Solihull Council — A45 / Damson Parkway 30mph order (2026)", "https://www.solihull.gov.uk/sites/default/files/2026-07/TR160-A45-Damson-Parkway-TTRO-Aug-2026-Onwards-NOTICE.pdf"),
    "hs2_a45": ("HS2 — A45 overnight closures near Bickenhill", "https://www.hs2.org.uk/work-items/temporary-midweek-overnight-full-carriageway-closures-of-a45-coventry-road-eastbound-westbound-near-bickenhill/"),
    "a41sr": ("Solihull Council — A41 road safety improvements", "https://solihull.gov.uk/news/solihull-council-seeks-views-a41-road-safety-improvements"),
    "a41sl": ("Solihull Council — A41 corridor 20mph/30mph order (2025)", "https://www.solihull.gov.uk/sites/default/files/2025-06/A41-Corridor-Improvements-20MPH-30MPH-March-2025-IMP-NOTICE.pdf"),
    "a41zebra": ("Solihull Council — A41 Warwick Road / Reservoir Road consultation", "https://www.solihull.gov.uk/sites/default/files/2025-11/A41%20Warwick%20Road%20Reservoir%20Road%20-%20Consultation%20Outcomes%20Report.pdf"),
    "lode": ("TfWM — Sprint works, Lode Lane", "https://tfwm.org.uk/plan-your-journey/major-roadworks-and-events/sprint/lode-lane"),
    "hobs": ("TfWM — Sprint works, Lode Lane / Hobs Moat Road", "https://tfwm.org.uk/plan-your-journey/major-roadworks-and-events/sprint/lode-lane-hobs-moat-road"),
    "sprint_order": ("Solihull Council — Sprint Phase 2 traffic provisions (2026)", "https://www.solihull.gov.uk/sites/default/files/2026-02/SPRINT-Various-Provisions-July-2024-IMP-NOTICE-Ph2.pdf"),
    "gateway": ("Solihull Council — Solihull Gateway FAQs", "https://www.solihull.gov.uk/sites/default/files/migrated/Portals_0_ParkingTravelRoads%252FSolihull_Gateway_FAQs.pdf"),
    "mte_consult": ("Solihull Council — new traffic enforcement powers consultation", "https://www.solihull.gov.uk/news/solihull-council-consults-new-traffic-enforcement-powers"),
    "touchwood": ("Solihull Council — Touchwood traffic arrangements", "https://www.solihull.gov.uk/sites/default/files/migrated/Portals_0_StrategiesPlansPolicies%252FTE%252Ftouchwood20.pdf"),
    "masterplan": ("Solihull Council — Town Centre Masterplan", "https://www.solihull.gov.uk/about-council/solihull-town-centre-masterplan"),
    "a452": ("Solihull Council — A452 Chester Road 40mph & clearway order (2025)", "https://www.solihull.gov.uk/sites/default/files/2025-05/A452-Chester-Road-40MPH-Clearway-PoRHT-PoLHT-April-2025-IMP-NOTICE.pdf"),
    "hs2_a452": ("HS2 — A452 Chester Road closures near Bickenhill", "https://www.hs2.org.uk/work-items/temporary-mid-weeknight-full-closures-on-the-a452-chester-road-in-both-directions-near-bickenhill/"),
    "bc40": ("Solihull Council — Kenilworth Road, Balsall Common 40mph proposal (2026)", "https://www.solihull.gov.uk/sites/default/files/2026-05/Kenilworth-Road-Balsall-Common-40MPH-May-2026-PROPOSAL-NOTICE.pdf"),
    "bc_hs2": ("Solihull Council — Kenilworth Road, Balsall Common HS2 order (2026–27)", "https://www.solihull.gov.uk/sites/default/files/2026-04/TR019-Kenilworth-Road-BC-TTRO-May-2026-Aug-2027-NOTICE.pdf"),
    "bc20": ("Solihull Council — Balsall Common village 20mph (2024)", "https://www.solihull.gov.uk/sites/default/files/2024-10/Balsall-Common-Village-20-MPH-Feb-2024-IMP-NOTICE-Web.pdf"),
    "knowle": ("Knowle Society — speed limit changes", "https://www.knowlesociety.org.uk/speed-limit-changes-road-closure/"),
    "blossom": ("Solihull Council — Blossomfield Road works order (2026)", "https://www.solihull.gov.uk/sites/default/files/2026-07/TR180-Blossomfield-Road-Sol-TTRO-July-Sept-2026-NOTICE.pdf"),
    "blossom2": ("Hockley Heath PC — work to start at Blossomfield roundabout", "https://www.hockleyheathparishcouncil.gov.uk/work-to-start-at-blossomfield-roundabout"),
    "dh20": ("Solihull Council — Dickens Heath Road 20mph (2025)", "https://www.solihull.gov.uk/sites/default/files/2025-09/Dickens-Heath-Road-20MPH-March-2025-IMP-NOTICE.pdf"),
    "school20": ("Solihull Council — school 20mph limits (2025)", "https://www.solihull.gov.uk/sites/default/files/2025-08/Various-Roads-Schools-20MPH-April-2025-IMP-NOTICE.pdf"),
    "hh20": ("Hockley Heath PC — 20mph consultation", "https://www.hockleyheathparishcouncil.gov.uk/consultation-on-change-from-30mph-to-20mph-in-hockley-heath-for-school-road-blackberry-avenue-lindhurst-drive-muntz-crescent-and-tysoe-close/"),
    "hia": ("Hampton-in-Arden PC — Meriden Road closures (2026)", "https://hamptoninardenparish.gov.uk/update-on-meriden-road-daytime-closures-now-expected"),
    "didd": ("HS2 — Diddington Lane closure", "https://www.hs2.org.uk/work-items/temporary-prolonged-full-closure-of-diddington-lane-hampton-in-arden/"),
    "crash": ("Crashview — Solihull collisions (STATS19)", "https://crashview.co.uk/towns/solihull"),
    "strategy": ("Solihull Council — Road Safety Strategy 2017–2030", "https://www.solihull.gov.uk/sites/default/files/migrated/ParkingTravelRoads_SMBC_Road_Safety_Strategy.pdf"),
    "hc": ("The Highway Code (GOV.UK)", "https://www.gov.uk/guidance/the-highway-code"),
    "hs2_rbt": ("HS2 — overnight lane closures on the new A452/A446 roundabout over the trace near Bickenhill (Sept 2025)", "https://www.hs2.org.uk/work-items/notice-of-temporary-overnight-lane-closures-on-the-a452-roundabout-over-the-trace-connecting-the-a446-stonebridge-road-a446-link-road-and-a452-chester-road-near-bickenhill"),
    "hs2_a452": ("HS2 — A452 Kenilworth Road overnight closures, Stonebridge Island to Meriden Road roundabout (2025)", "https://www.hs2.org.uk/work-items/hs2-notice-a452-kenilworth-road-temporary-overnight-closures-stonebridge-island-to-meriden-road-roundabout"),
    "hs2_a446": ("HS2 — overnight closures of the A452 Chester Road and A446 Stonebridge Road near Bickenhill", "https://www.hs2.org.uk/work-items/temporary-overnight-closures-of-a452-chester-road-a446-stonebridge-road-near-bickenhill"),
    "nh_open": ("National Highways — brand new road fully opened as M42 improvements scheme reaches final stages (June 2025)", "https://nationalhighways.co.uk/press/brand-new-road-fully-opened-as-m42-improvements-scheme-reaches-final-stages"),
    "dropoff": ("Express & Star — Birmingham Airport drop-off fees (2026)", "https://www.expressandstar.com/news/birmingham-airport-drop-off-fees-hiked-as-charges-rise-at-uk-airports-8767733"),
    "aph": ("APH — UK airport drop-off and pick-up charges (2026 guide)", "https://www.aph.com/holidays/drop-off-and-pick-up-charges-of-up-to-50-revealed-at-uk-airports-find-yours-here/"),
    "a3400": ("Lapworth Parish Council — A3400 Stratford Road, Hockley Heath night closure (April 2025)", "https://lapworth-pc.gov.uk/road-closures/temporary-closure-of-a3400-stratford-road-hockley-heath-10th-to-15th-april-2025-night-time-closure"),
    "trainee_mway": ("DVSA blog — learner drivers on motorways: what you need to know (2018)", "https://movingon.blog.gov.uk/2018/06/04/learner-drivers-on-motorways-what-lorry-and-coach-drivers-need-to-know"),
    "motorway": SOL.SRC["motorway"],
}
CHECKED = "Checked October 2026 — roadworks and temporary limits change often; always obey the signs on the day."

ROADS = [
    dict(slug="stonebridge-island-a446-hs2-roundabout", title="Stonebridge Island, the A446 and the new HS2 roundabout: a learner's guide", short="Stonebridge & HS2 roundabout",
         seo="Stonebridge Island, A446 & New HS2 Roundabout Solihull: Learner Guide | SQ",
         desc="Stonebridge Island (A45/A452/A446) and the new roundabout built over the HS2 line near Bickenhill: what changed, what's still changing and how to handle it as a learner or new driver.",
         stats=[("3", "A-roads meet"), ("2025", "new roundabout in use"), ("HS2", "Interchange works"), ("Near", "M42 J6 & the NEC")],
         keys=["Stonebridge Island joins the A45, A452 and A446 east of the NEC.", "HS2 has built a new roundabout over the railway line linking the A452, the A446 Stonebridge Road and a new A446 link road.", "Overnight closures and lane closures have been common — check before you drive.", "Big, fast junctions: pick your lane early."],
         body="""<p class="lead">East of the NEC and Birmingham Airport, three busy A-roads — the A45, the A452 and the A446 — meet at Stonebridge Island. HS2's Interchange station is being built next door, and the roads around it have been rebuilt to match.</p>
<h2>What's changed</h2><p>HS2 has built a <b>new roundabout over the line (the "trace")</b> near Bickenhill, connecting the <b>A452 Chester Road</b>, the <b>A446 Stonebridge Road</b> and a new <b>A446 link road</b>. It was in use by 2025, when HS2 carried out overnight surveys on it, and the former A452 overbridge nearby was due to be demolished in summer 2025. The wider plan widens and realigns the A452 to serve the new station's access.</p>
<h2>Closures you might meet</h2><p>HS2 has repeatedly closed lanes or whole carriageways overnight here — for example the A452 Kenilworth Road between Stonebridge Island and the Meriden Road roundabout in February 2025, and the A452 northbound and A446 southbound in June 2025. Signed diversions are put in place. Before an evening drive, check HS2's work notices.</p>
<h2>How to handle it</h2><ul><li><b>Lane choice early:</b> these are big, fast roundabouts. Read the signs on the approach and get into lane in good time.</li><li><b>Changed layouts:</b> sat-nav maps can lag behind new roads. Follow the road signs if they disagree.</li><li><b>Roadworks speed limits:</b> temporary limits are enforced — watch every sign.</li><li><b>Large vehicles:</b> construction lorries use these roads; give them room.</li></ul>
<h2>Do we teach here?</h2><p>Yes — once you're comfortable on dual carriageways and big roundabouts. It's ideal practice for learners in Meriden, Hampton-in-Arden, Marston Green and Chelmsley Wood, and for anyone heading to <a href="../solihull/coventry-driving-test-centre-routes.html">Coventry</a> for their test.</p>""",
         faqs=[("What is Stonebridge Island?", "The junction east of the NEC where the A45, A452 and A446 meet."), ("Why have the roads changed near Bickenhill?", "HS2 has rebuilt them around its Interchange station, including a new roundabout over the line linking the A452, A446 Stonebridge Road and a new A446 link road.")],
         src=["hs2_rbt", "hs2_a452", "hs2_a446", "hc"]),
    dict(slug="birmingham-airport-roads-and-drop-off", title="Driving to Birmingham Airport: roads, drop-off and tips for new drivers", short="Birmingham Airport roads",
         seo="Driving to Birmingham Airport: Roads, Drop-Off & New Driver Tips | SQ Solihull",
         desc="The roads into Birmingham Airport — the A45, the Clock Interchange and the new A4545 link with its own airport slip road — plus how drop-off works and tips for new drivers.",
         stats=[("A45", "main approach"), ("2025", "A4545 airport slip road open"), ("Free", "drop-off option (further out)"), ("~15 min", "paid premium set-down")],
         keys=["Most traffic arrives via the A45 Coventry Road and the Clock Interchange.", "The A4545 link from M42 junction 5A fully opened in June 2025, including a slip road into the airport.", "There's a free drop-off area a short walk away and a paid premium set-down by the terminal.", "Check the airport's own website for current prices before you go."],
         body="""<p class="lead">Lots of Solihull drivers make their first "big" solo drive to Birmingham Airport — dropping someone off before a flight. It's close, but the roads are busy, fast and full of people looking for signs.</p>
<h2>The approach roads</h2><ul><li><b>A45 Coventry Road</b> — the main route from Solihull and Birmingham. See our <a href="a45-coventry-road-airport-nec.html">A45 guide</a>.</li><li><b>The Clock Interchange</b> — rebuilt as part of the M42 junction 6 scheme.</li><li><b>The A4545</b> — a new 2.4km dual carriageway from <a href="m42-junctions-3a-4-5-6-solihull.html">M42 junction 5A</a> to the Clock Interchange, fully open since June 2025 including a slip road into the airport.</li></ul>
<h2>Dropping off</h2><p>In 2026 the airport offered a <b>free drop-off area</b> a short walk from the terminal and a <b>paid premium set-down</b> right by it (reported at around £6–£7 for up to 15 minutes, with prices rising). Many airports now use number-plate cameras and online payment with a deadline — miss it and you can get a charge notice. <b>Check the airport's website for current prices and rules before you set off.</b></p>
<h2>Tips for new drivers</h2><ul><li>Do the route once at a quiet time before the real trip.</li><li>Expect drivers changing lanes late as they spot signs — keep a big gap.</li><li>Don't stop on the approach roads or roundabouts to drop people off.</li><li>Learners can drive the airport roads with a supervisor — but not the M42, which needs an approved instructor in a dual-control car.</li></ul>
<p>Work at the airport? See <a href="birmingham-airport-driving-lessons.html">lessons for airport staff</a>.</p>""",
         faqs=[("Is it free to drop off at Birmingham Airport?", "There's a free drop-off area a short walk from the terminal and a paid premium set-down next to it. Prices change — check the airport's website."), ("Can a learner drive to the airport?", "Yes on ordinary roads with a qualified supervisor — but learners can only use motorways like the M42 with an approved instructor in a dual-control car.")],
         src=["nh_open", "dropoff", "aph", "motorway", "hc"]),
    dict(slug="a3400-hockley-heath-m40-junction-16", title="A3400 Stratford Road to Hockley Heath and M40 junction 16: a learner's guide", short="A3400 & M40 J16",
         seo="A3400 Hockley Heath & M40 Junction 16: Learner Driver Guide | SQ Solihull",
         desc="The A3400 Stratford Road from M42 junction 4 through Hockley Heath to the M40 junction 16 roundabout: changing limits, a village centre, rural sections and the motorway junction.",
         stats=[("J4", "M42 Monkspath start"), ("J16", "M40 roundabout"), ("Rural", "and village sections"), ("Instructor", "only on motorways")],
         keys=["South of M42 junction 4 the A34 becomes the A3400 towards Hockley Heath and Henley-in-Arden.", "It passes through Hockley Heath village and meets the M40 at junction 16.", "Limits change between village and rural stretches — check every sign.", "Learners can only join the M40 with an approved instructor in a dual-control car."],
         body="""<p class="lead">Leave the A34 at M42 junction 4 heading south and you're on the A3400 Stratford Road — through Hockley Heath village and on to the M40 junction 16 roundabout. It's one of the best roads near Solihull for learning how a road changes character.</p>
<h2>What the road is like</h2><ul><li><b>From M42 junction 4</b> — busy junction traffic near Blythe Valley Park.</li><li><b>Hockley Heath village</b> — shops, side roads, pedestrians and parked cars: slow right down.</li><li><b>Rural stretches</b> — faster sections with bends, field entrances and slow farm vehicles.</li><li><b>M40 junction 16</b> — a roundabout where traffic joins and leaves the motorway.</li></ul>
<h2>Roadworks</h2><p>The stretch between the M40 junction 16 roundabout and Nuthurst Grange Road was closed overnight for resurfacing in April 2025, with a signed diversion. Check parish and council notices before late drives.</p>
<h2>Motorway lessons from here</h2><p>The M40 is right there, but learners can only drive on a motorway with an <b>approved driving instructor in a dual-control car</b> — not with family, and not with a trainee instructor. We use it for <a href="motorway-driving-lessons-m42-solihull.html">motorway lessons</a> once you're ready.</p>
<h2>Who practises here</h2><p>Learners from <a href="driving-lessons-hockley-heath.html">Hockley Heath</a>, <a href="driving-lessons-dickens-heath.html">Dickens Heath</a>, <a href="driving-lessons-cheswick-green.html">Cheswick Green</a> and <a href="driving-lessons-monkspath.html">Monkspath</a> — and anyone testing at <a href="shirley-driving-test-centre-routes.html">Shirley</a> or <a href="redditch-driving-test-centre-routes.html">Redditch</a>.</p>""",
         faqs=[("Where does the A3400 start near Solihull?", "At M42 junction 4 (Monkspath), where the A34 continues south as the A3400 towards Hockley Heath."), ("Can learners drive on the M40?", "Only with an approved driving instructor in a car with dual controls. Trainee instructors can't give motorway lessons.")],
         src=["a3400", "trainee_mway", "motorway", "hc"]),
    dict(slug="a34-stratford-road-shirley", title="A34 Stratford Road, Shirley: a learner's guide", short="A34 Stratford Road",
         seo="A34 Stratford Road Shirley: Driving Test Guide, Cameras & Limits | SQ",
         desc="The A34 Stratford Road through Shirley and Monkspath for learner drivers: 30/40mph changes, average speed cameras, red routes, the U-turn camera, Blackford Road roundabout and M42 junction 4.",
         stats=[("40mph", "average-speed section"), ("2023", "cameras went live"), ("13/15", "Shirley routes use it"), ("J4", "M42 Monkspath")],
         keys=["The A34 appears on almost every reported Shirley test route.", "Average speed cameras enforce the 40mph section from Marshall Lake Road to M42 J4 (since January 2023).", "A camera enforces the U-turn ban at Richard Lewis Way from 1 June 2026.", "Red-route no-stopping rules apply along much of it."],
         body="""<p class="lead">If you're taking your test at Shirley, the A34 Stratford Road is the road you need to master. In one public collection of 15 Shirley test routes, 13 used it. It changes character every few hundred metres — shopping street, 40mph dual carriageway, roundabouts, red route — and it's watched by cameras.</p>
<h2>Speed limits and average speed cameras</h2>
<p>Average speed cameras went live on <b>16 January 2023</b> on the 40mph section of the A34 between the <b>B4102 Marshall Lake Road</b> junction and <b>M42 junction 4</b>, replacing older fixed cameras. West Midlands Police and Crime Commissioner said the stretch "continues to have a high road traffic collision rate". Closer to the shops, parts of the A34 are 30mph. The change between 30 and 40 is the single most common speed mistake we correct on this road: you must be at the new limit by the sign, not accelerating towards it.</p>
<h2>Red route: no stopping</h2>
<p>Red-route restrictions apply along the A34, and a red-route clearway was proposed in 2021 for the whole of Dog Kennel Lane (40mph, "busy but relatively narrow, traffic sensitive"). On test, if the examiner asks you to pull up on the left, never choose a red-route section — find a side road or a legal bay.</p>
<h2>The U-turn camera at Richard Lewis Way</h2>
<p>From <b>1 June 2026</b>, a moving-traffic enforcement camera at the A34 / Richard Lewis Way junction catches drivers making the banned U-turn, with warning letters for first offences during the first six months. Following a sat-nav during independent driving? If you miss a turn, carry on and let it re-route — never U-turn where it's banned.</p>
<h2>Blackford Road roundabout</h2>
<p>In Solihull Council's ranking of collision sites (2016–18 data), the <b>A34 Stratford Road / Blackford Road roundabout</b> was second worst in the borough, with excessive speed on the A34 a contributory factor. Approach it slowly enough to judge traffic coming from your right, and be in the right lane early.</p>
<h2>M42 junction 4 — Monkspath Interchange</h2>
<p>Junction 4 links the A34 with the A3400 towards Hockley Heath and Henley-in-Arden. It opened in 1976 and was later remodelled to give direct access to Blythe Valley Park. Learners won't go onto the M42 on a test, but you'll meet traffic joining and leaving the motorway at speed.</p>
<h2>Roadworks in 2026</h2>
<p>The A34 had several overnight closures in 2026 for resurfacing — for example, northbound between Cranmore Boulevard and Blackford Road in February, diverted via Dog Kennel Lane and Blackford Road. Expect temporary lights and diversions from time to time.</p>
<h2>How we teach the A34</h2>
<ol class="rx-steps"><li data-n="1"><h4>Quiet hours first</h4><p>Sunday mornings or mid-morning, to learn lane positions and limit changes.</p></li><li data-n="2"><h4>Bus stops and side roads</h4><p>Anticipating buses pulling out and cars emerging from retail parks.</p></li><li data-n="3"><h4>Rush hour</h4><p>Once you're confident, at the time of day of your test.</p></li></ol>""",
         faqs=[("Are there speed cameras on the A34 in Shirley?", "Yes. Average speed cameras enforce the 40mph section between Marshall Lake Road and M42 junction 4, live since 16 January 2023."),
               ("Can you U-turn on the A34 at Richard Lewis Way?", "No. It's banned and camera-enforced from 1 June 2026."),
               ("Is the A34 on the Shirley driving test?", "Very often — it appears on most reported Shirley routes.")],
         src=["pcc_cam", "mte", "mte_news", "dkl", "ranked", "j4", "a34_tr229"]),
    dict(slug="m42-junctions-3a-4-5-6-solihull", title="M42 junctions 3A to 6 around Solihull", short="M42 junctions 3A–6",
         seo="M42 Junctions 3A, 4, 5 & 6 Solihull: Smart Motorway Guide for New Drivers | SQ",
         desc="The M42 around Solihull explained for learners and new drivers: the 2006 hard-shoulder-running pilot, red X signs, J3A's tricky priority, J4 Monkspath, J5, the new J5A and A4545 link, and J6 for the airport and NEC.",
         stats=[("2006", "first UK hard-shoulder pilot"), ("£282m", "J6 improvement"), ("J5A", "new junction (2024)"), ("2.4km", "new A4545 link")],
         keys=["J3A–J7 was the UK's first Active Traffic Management pilot.", "At J3A, drivers staying on the M42 must leave the main carriageway.", "A new J5A and the A4545 dual carriageway opened in December 2024.", "Learners can have motorway lessons with an ADI in a dual-control car."],
         body="""<p class="lead">Solihull is wrapped by the M42, and its four junctions shape how everyone in the borough drives. Since 2018, learners can drive on motorways with an approved instructor in a dual-control car — and here's what makes this stretch different.</p>
<h2>Hard-shoulder running: the UK's first pilot</h2>
<p>From 2005–06 the M42 between junctions 3A and 7 was the UK's first Active Traffic Management pilot: at busy times the hard shoulder opens as a running lane under gantry signals, a red X closes a lane, and emergency refuge areas sit roughly every 500 metres. The rule that matters most: <b>never drive in a lane under a red X</b>, and treat a speed shown in a red circle as the legal limit.</p>
<h2>Junction 3A — the M40 interchange</h2>
<p>J3A isn't fully free-flowing. Priority goes to the M40↔M42 westbound movement, so drivers <b>staying on the M42 have to leave the main carriageway</b>. It catches out new drivers who assume "straight on" means staying in lane. Read the overhead signs early.</p>
<h2>Junction 4 — Monkspath</h2>
<p>Links the A34 (Shirley, Solihull, Birmingham) and the A3400 (Hockley Heath). It's next to Blythe Valley Park and the A34's average-speed section. See our <a href="a34-stratford-road-shirley.html">A34 guide</a>.</p>
<h2>Junction 5 — Solihull and Knowle</h2>
<p>Connects the A41 north towards the Solihull bypass and the A4141 south to Knowle (the A4141 is the old A41). Variable speed limits apply here.</p>
<h2>New junction 5A and the A4545</h2>
<p>National Highways' £282m M42 junction 6 improvement built a new <b>junction 5A</b> about 1.8km south of J6 — two roundabouts joined by a bridge, with south-facing slips only — and a new 2.4km <b>A4545 dual carriageway</b> to the A45 Clock Interchange, giving direct access to the airport and Birmingham Business Park. The link opened on 18 December 2024. If your sat-nav is old, it may not know it exists.</p>
<h2>Junction 6 — airport, NEC and Resorts World</h2>
<p>J6 has new free-flow links and changing layouts, and temporary limits around Clock Interchange and the A45 have come and gone with the works. Catherine de Barnes Lane and Bickenhill got new permanent limits in October 2025 — 40mph north of the St Peters Lane roundabout, 50mph south to the B4102, and 20mph on Church Lane and St Peters Lane.</p>
<h2>England's worst motorway?</h2><p>A Transport Focus survey for the year to March 2026 ranked the M42 England's worst-rated motorway, citing roadworks, potholes and reduced limits. All the more reason to have a few lessons on it before driving it alone.</p>
<p>Book <a href="motorway-driving-lessons-m42-solihull.html">M42 motorway lessons</a>.</p>""",
         faqs=[("What does a red X on the M42 mean?", "The lane is closed. Move out of it safely and never drive under a red X."),
               ("Where is M42 junction 5A?", "About 1.8km south of J6, with south-facing slips, connected to the A45 Clock Interchange by the new A4545. It opened in December 2024."),
               ("Can learners drive on the M42?", "Yes, with an approved driving instructor in a dual-control car.")],
         src=["m42atm", "j3a", "j4", "j5", "j6", "j6news", "cdb", "m42worst", "motorway"]),
    dict(slug="a45-coventry-road-airport-nec", title="A45 Coventry Road, the airport and the NEC", short="A45 Coventry Road",
         seo="A45 Coventry Road Solihull: Airport, NEC, Sprint Bus Lanes & HS2 | SQ",
         desc="Driving the A45 Coventry Road around Birmingham Airport and the NEC: Sprint bus lanes, temporary limits, Clock Interchange, the new A4545 link, HS2 at Stonebridge and Garretts Green/South Yardley test routes.",
         stats=[("Sprint", "bus lanes"), ("30mph", "temporary limit by the airport (2026)"), ("50mph", "east of the works"), ("HS2", "Stonebridge")],
         keys=["The A45 appears on Garretts Green and South Yardley test routes.", "Sprint bus lanes run along the A45 — check the times on the signs.", "A temporary 30mph applies near the airport from August 2026.", "HS2 passes under the A45 near Stonebridge; overnight closures happen."],
         body="""<p class="lead">The A45 Coventry Road is north Solihull's main artery: Birmingham to the airport, the NEC, Resorts World and on towards Coventry. It's on reported test routes from <a href="garretts-green-driving-test-centre-routes.html">Garretts Green</a> and <a href="south-yardley-driving-test-centre-routes.html">South Yardley</a>, and it's where many north Solihull learners first drive a fast dual carriageway.</p>
<h2>Sprint bus lanes</h2>
<p>The A45 is part of the Sprint bus corridor linking Walsall, Birmingham, Solihull and the airport. Phase 1 added extended bus lanes and bus-priority signals. Phase 2 on the Birmingham side, between Wagon Lane and Gilberstone Avenue in Sheldon, turns one general traffic lane into a bus lane, with works due to finish by autumn 2026. Bus lanes have times on the blue signs — read them every time.</p>
<h2>Speed limits around the airport</h2>
<p>Limits here change with the roadworks. Solihull Council made a temporary 30mph order on the A45, Damson Parkway and Terminal Road from about August 2026, running to the start of the 50mph section east of the works. Earlier temporary orders set 30mph around Clock Interchange (2024) and 40mph near the airport (2025). The lesson for test day: the sign beats your memory.</p>
<h2>Clock Interchange and the new A4545</h2>
<p>The new A4545 dual carriageway from M42 junction 5A meets the A45 at Clock Interchange. See our <a href="m42-junctions-3a-4-5-6-solihull.html">M42 junctions guide</a>.</p>
<h2>HS2 at Stonebridge</h2>
<p>HS2 passes under the A45 near Stonebridge and has carried out overnight A45 closures near Bickenhill. Plans also change accesses at Stonebridge Island (A45/A452/A446). See our <a href="a452-chester-road-kenilworth-road-hs2.html">A452 and HS2 guide</a>.</p>
<h2>Learner tips for the A45</h2><ul><li>Use the whole slip road to match speed before merging.</li><li>Expect drivers who don't know the area — airport and NEC traffic.</li><li>Watch for buses using bus-priority signals.</li><li>Keep left unless overtaking.</li></ul>""",
         faqs=[("What is the speed limit on the A45 by Birmingham Airport?", "It varies with roadworks. From about August 2026 a temporary 30mph order applies on the A45 near Damson Parkway and Terminal Road, with 50mph further east. Always follow the signs."),
               ("Are there bus lanes on the A45?", "Yes — Sprint bus lanes. Check the operating times on the signs."),
               ("Is the A45 on the Garretts Green driving test?", "It's on reported Garretts Green and South Yardley routes.")],
         src=["sprint", "a45works", "a45_30", "hs2_a45", "j6"]),
    dict(slug="a41-warwick-road-olton-solihull", title="A41 Warwick Road through Olton and Solihull", short="A41 Warwick Road",
         seo="A41 Warwick Road Olton & Solihull: New Limits, Crossings & Safety Scheme | SQ",
         desc="The A41 Warwick Road from Olton Hollow to the Solihull bypass: the £1.265m Safer Roads Fund scheme, the 2025 20mph/30mph changes on Seven Star Road and Lode Lane, new crossings and collision history.",
         stats=[("£1.265m", "Safer Roads Fund scheme"), ("5.7km", "corridor"), ("30mph", "Seven Star Road (was 40)"), ("2025", "new limits")],
         keys=["The A41 corridor from Olton Hollow to the bypass was chosen for safety funding because of its collision history.", "From 14 July 2025, Seven Star Road dropped from 40 to 30mph and residential roads became 20mph.", "A raised zebra crossing is proposed at Reservoir Road near Olton station.", "South of M42 J5 the road becomes the A4141 to Knowle."],
         body="""<p class="lead">The A41 Warwick Road runs from Birmingham through Olton and past Solihull to M42 junction 5. Solihull Council won £1.265m from the Department for Transport's Safer Roads Fund for the 5.7km stretch from Olton Hollow to the Solihull bypass via Warwick Road and Seven Star Road — because of its collision history.</p>
<h2>What the council found</h2><p>High speeds, a lack of crossing points, poor driver behaviour at junctions and roadside hazards. In other words, exactly the things examiners mark: speed, observation and junction judgement.</p>
<h2>New limits from July 2025</h2>
<p>A speed limit order took effect on <b>14 July 2025</b>: <b>20mph</b> on residential and service roads along the corridor, and <b>30mph</b> on Seven Star Road (cut from 40mph) and Lode Lane. If you learned the area before then, re-learn it — and so should your parents if they're supervising practice.</p>
<h2>Crossings</h2><p>A zebra crossing on a raised table is proposed on Warwick Road at Reservoir Road, near Olton station. Zebra crossings mean giving way to anyone on the crossing — and, since the 2022 Highway Code changes, being ready for people waiting to cross.</p>
<h2>Solihull bypass and Hampton Lane</h2><p>The Solihull Bypass / Hampton Lane / Yew Tree Lane junction is flagged in the council's collision rankings, including drivers disobeying signals. Approach lights at a speed where an amber is an easy decision.</p>
<h2>South of junction 5: the A4141</h2><p>Past M42 J5 the road continues to Knowle as the A4141 — see our <a href="knowle-dorridge-and-village-speed-limits.html">village speed limits guide</a>.</p>""",
         faqs=[("What is the speed limit on Seven Star Road, Solihull?", "30mph since 14 July 2025 (previously 40mph)."),
               ("Why is the A41 in Solihull getting safety changes?", "Its collision history — the council identified high speeds, few crossings, poor junction behaviour and roadside hazards.")],
         src=["a41sr", "a41sl", "a41zebra", "ranked", "j5"]),
    dict(slug="lode-lane-hobs-moat-road-bus-lanes", title="Lode Lane and Hobs Moat Road: bus lanes and Sprint", short="Lode Lane & Hobs Moat Road",
         seo="Lode Lane & Hobs Moat Road Solihull: Bus Lanes, Cameras & Sprint | SQ",
         desc="Lode Lane (B425) and Hobs Moat Road for learner drivers: CCTV-enforced bus lanes, Sprint Phase 2 signals and turning bans, JLR and Solihull Hospital traffic, and the borough's top-ranked collision junction.",
         stats=[("2017", "bus lane cameras"), ("2,944", "penalties in six months"), ("#1", "ranked collision site (2016–18)"), ("Sprint", "Phase 2")],
         keys=["Lode Lane bus lanes have been CCTV-enforced since 2017.", "Sprint Phase 2 added new signals, a bus lane, a controlled crossing and turning bans.", "Hobs Moat Road / Ulleries Road was the borough's No.1 ranked collision site (2016–18).", "JLR's plant and Solihull Hospital both sit on Lode Lane."],
         body="""<p class="lead">Lode Lane links Solihull town centre with Elmdon and the A45, past Solihull Hospital, Lode Heath School and the JLR plant. Hobs Moat Road carries on north. Together they're a crash course in bus lanes, shift traffic and busy junctions.</p>
<h2>Bus lanes with cameras</h2><p>Lode Lane's bus lanes have been CCTV-enforced since September 2017 — one report counted 2,944 penalties in the first six months. Read the blue sign: if it shows times, the lane is only restricted then; if it shows none, it's 24 hours.</p>
<h2>Sprint Phase 2</h2><p>From September 2024, Sprint works on Lode Lane added drainage, new signals, a new bus lane and a controlled crossing. The traffic order introduced turning bans (including opposite Radcliffe House and at Dovehouse Lane) and red-route revisions. On Hobs Moat Road, widening is done, shelters are open and the A45 junction signals have been upgraded.</p>
<h2>The borough's top-ranked collision junction</h2><p>In the council's ranking of collision sites (2016–18 data), <b>Hobs Moat Road / Ulleries Road</b> was number one — linked to turning manoeuvres and drivers failing to look properly. That's "junctions — observation", the most common reason people fail the driving test. See our <a href="../test-faults/junction-observations.html">junction observations guide</a>.</p>
<h2>Shift-change traffic</h2><p>JLR's Solihull plant runs shifts around the clock, and Solihull Hospital's car park is busy at peak times. Expect sudden queues, cars turning right across you and pedestrians crossing near the hospital.</p>""",
         faqs=[("Are the Lode Lane bus lanes enforced by camera?", "Yes, since September 2017."),
               ("Which junction in Solihull had the most collisions?", "In the council's 2016–18 ranking, Hobs Moat Road / Ulleries Road was the No.1 site.")],
         src=["lode", "hobs", "sprint_order", "ranked", "sprint"]),
    dict(slug="solihull-town-centre-driving-guide", title="Driving in Solihull town centre", short="Solihull town centre",
         seo="Driving in Solihull Town Centre: Bus-Only Streets, Touchwood & Cameras | SQ",
         desc="How to drive through Solihull town centre as a learner: bus-only Station Road and Poplar Road, the Touchwood loop (Church Hill Road, Homer Road, Herbert Road), the planned cameras and yellow box, and parking.",
         stats=[("2015", "Solihull Gateway scheme"), ("£70", "proposed fine (£35 early)"), ("~1,700", "Touchwood parking spaces"), ("2036", "masterplan horizon")],
         keys=["Station Road and Poplar Road are restricted to buses and permitted vehicles since the 2015 Gateway scheme.", "A camera at Station Road into Poplar Road is planned.", "Touchwood is ringed by Church Hill Road, Homer Road and Herbert Road with restricted movements.", "A yellow-box camera is planned at the B4102 Warwick Road / New Road junction."],
         body="""<p class="lead">Solihull town centre is compact but full of rules: bus-only streets, restricted turns around Touchwood, pedestrian zones and new cameras on the way. Sat-navs don't always know them. Here's what learners need to know.</p>
<h2>Bus-only: Station Road and Poplar Road</h2><p>Since the 2015 Solihull Gateway scheme, Station Road and Poplar Road are two-way but <b>restricted to buses and permitted vehicles</b>. A moving-traffic camera is planned at Station Road into Poplar Road (a pedestrian zone), and the council proposed fines of £70 (£35 if paid early). Bus stands on Station Road changed in November 2025 after Sprint works.</p>
<h2>The Touchwood loop</h2><p>Touchwood is bounded by <b>Church Hill Road</b> (east), <b>Homer Road</b> (south) and <b>Herbert Road</b> (west). Traffic inside the loop is restricted by vehicle type and/or direction. Homer Road had closures in late 2024 and early 2025, with right turns banned at the Touchwood car park access during the works.</p>
<h2>Yellow box at Warwick Road / New Road</h2><p>A camera is planned at the B4102 Warwick Road / New Road yellow box junction. Rule: don't enter the box unless your exit is clear (unless turning right and only blocked by oncoming traffic).</p>
<h2>Parking</h2><p>Touchwood has roughly 1,700 of the town centre's 6,000 or so spaces. Car parks are good places to practise bay parking — at quiet times.</p>
<h2>What's coming</h2><p>The council's Town Centre Masterplan, with a horizon to 2036, includes a new station transport hub and offices on the Homer Road gateway. Expect layouts to keep changing.</p>""",
         faqs=[("Can you drive on Station Road in Solihull?", "Only buses and permitted vehicles — it has been restricted since the 2015 Gateway scheme, and a camera is planned."),
               ("Where can I park in Solihull town centre?", "Touchwood has about 1,700 spaces; there are around 6,000 across the town centre.")],
         src=["gateway", "mte_consult", "mte", "touchwood", "masterplan"]),
    dict(slug="a452-chester-road-kenilworth-road-hs2", title="A452 Chester Road and Kenilworth Road (and HS2)", short="A452 & HS2 works",
         seo="A452 Chester Road & Kenilworth Road Solihull: HS2 Works, 40mph & Clearway | SQ",
         desc="The A452 through Solihull — Chester Road at Chelmsley Wood, Marston Green and Bickenhill, and Kenilworth Road at Balsall Common — with the 2025 40mph clearway, HS2 closures and contraflows running to 2027.",
         stats=[("40mph", "A452 Bickenhill clearway (2025)"), ("24hr", "clearway"), ("2027", "Balsall Common contraflow ends"), ("HS2", "Interchange")],
         keys=["A452 Chester Road at Bickenhill is a 40mph 24-hour clearway from June 2025, with a right-turn ban at Bickenhill Parkway.", "HS2 works bring night closures and lane closures near Bickenhill.", "Kenilworth Road at Balsall Common has an HS2 30mph contraflow from May 2026 to August 2027.", "Balsall Common village has 20mph streets (2024)."],
         body="""<p class="lead">The A452 runs the length of Solihull's eastern side — Chester Road past Castle Bromwich, Chelmsley Wood and Marston Green, and Kenilworth Road through Balsall Common. HS2 is reshaping both ends.</p>
<h2>Chester Road at Bickenhill</h2><p>A permanent order from <b>6 June 2025</b> sets <b>40mph</b>, a <b>24-hour clearway</b> (no stopping) and a ban on right turns into the roundabout at the A452 / B4438 Bickenhill Parkway junction — made for the HS2 layout. In 2026 HS2 has carried out mid-weeknight full closures, overnight slip closures and daytime lane closures at a newly built roundabout connecting the A446 and A452.</p>
<h2>Chelmsley Wood</h2><p>Coleshill Heath Road had a temporary 40mph from Chester Road to the boundary between May 2024 and November 2025. Chester Road itself is the fast road most Chelmsley Wood, Kingshurst and Castle Bromwich learners first meet.</p>
<h2>Kenilworth Road at Balsall Common</h2><ul><li><b>HS2 realignment:</b> 30mph and a contraflow between the Bradnocks Marsh and Meriden Road roundabouts, 19 May 2026 to 24 August 2027.</li><li><b>Temporary 40mph</b> between Hallmeadow Road and Wootton Lane, May 2026 to May 2027.</li><li><b>Proposed permanent 40mph</b> (from 50) for about 600m from Hallmeadow Road, including the Park Lane roundabout.</li><li><b>Village 20mph</b> on Balsall Common's streets from October 2024.</li></ul>
<h2>Contraflows: how to drive them</h2><p>Narrow lanes, cones close to your wheels and oncoming traffic with no central reservation. Keep to the limit, hold the centre of your lane, don't follow closely and look well ahead rather than at the cones.</p>""",
         faqs=[("What is the speed limit on the A452 Chester Road at Bickenhill?", "40mph, with a 24-hour clearway, since 6 June 2025."),
               ("How long are the HS2 works on Kenilworth Road, Balsall Common?", "The 30mph contraflow between Bradnocks Marsh and Meriden Road roundabouts runs from 19 May 2026 to 24 August 2027.")],
         src=["a452", "hs2_a452", "bc_hs2", "bc40", "bc20"]),
    dict(slug="knowle-dorridge-and-village-speed-limits", title="Speed limits in Knowle, Dorridge, Dickens Heath and Solihull's villages", short="Village speed limits",
         seo="Knowle, Dorridge & Solihull Village Speed Limits (20/30/40/50mph) | SQ",
         desc="Every recent speed-limit change in Solihull's villages for learners: Knowle High Street 20mph, Dickens Heath clock tower 20mph, Balsall Common 20mph, Hockley Heath, Bickenhill 40/50mph and village average speed cameras.",
         stats=[("20mph", "Knowle High Street"), ("2025", "Dickens Heath 20mph"), ("4", "villages with average-speed cameras"), ("40mph", "Fen End & Box Trees Road")],
         keys=["Knowle's A4141 High Street became 20mph in June 2023.", "Dickens Heath Road near the clock tower roundabout is 20mph from October 2025.", "Average speed cameras cover Berkswell, Hampton-in-Arden, Meriden and Balsall Common.", "Country lanes around Knowle went to 40mph in April 2023."],
         body="""<p class="lead">Solihull's villages have had a wave of speed-limit changes. For learners, that's a trap: the limit you remember from last year may be wrong. Here's the current picture, from council orders and parish councils.</p>
<h2>Knowle</h2><ul><li><b>20mph</b> on the A4141 Warwick Road / High Street (roughly Lodge Road to Milverton Avenue) and parts of Wilsons Road, Kenilworth Road and Station Road, from 5 June 2023.</li><li><b>30mph</b> on Warwick Road from Lady Byron Lane to Wychwood Avenue, and on Norton Green Lane.</li><li><b>40mph</b> on Fen End Road, Box Trees Road and Earlswood Road from 20 April 2023.</li></ul>
<h2>Dickens Heath</h2><p>20mph on Dickens Heath Road near the clock tower roundabout from 1 October 2025. The Tanworth Lane / Dickens Heath Road roundabout was resurfaced in February 2026.</p>
<h2>Balsall Common, Berkswell, Hampton-in-Arden and Meriden</h2><p>Average speed cameras, funded from HS2's road-safety allocation, cover these four villages. Balsall Common's village streets became 20mph in October 2024. Hampton-in-Arden has had HS2 closures on Meriden Road (B4102) and Diddington Lane in 2026.</p>
<h2>Hockley Heath</h2><p>30mph where the A3400 enters the village at the canal bridge. A 2022 consultation proposed 20mph on side roads such as School Road and Blackberry Avenue.</p>
<h2>Bickenhill and Catherine-de-Barnes</h2><p>From 10 October 2025: 40mph on Catherine de Barnes Lane north of the St Peters Lane roundabout and on Clock Lane, 50mph south to the B4102, and 20mph on Church Lane and St Peters Lane.</p>
<h2>Schools across the borough</h2><p>Solihull is rolling out 20mph limits at every school location; the first order took effect on 28 August 2025. See our <a href="solihull-speed-cameras-20mph-and-enforcement.html">cameras and 20mph guide</a>.</p>""",
         faqs=[("Is Knowle High Street 20mph?", "Yes, since 5 June 2023."),
               ("Are there average speed cameras in Solihull villages?", "Yes — Berkswell, Hampton-in-Arden, Meriden and Balsall Common.")],
         src=["knowle", "dh20", "villages_cam", "bc20", "hh20", "cdb", "hia", "didd", "school20"]),
    dict(slug="blossomfield-road-junction-signals", title="Blossomfield Road junction: roundabout to traffic lights", short="Blossomfield junction",
         seo="Blossomfield Roundabout Solihull Now Traffic Lights: What Learners Need to Know | SQ",
         desc="The B4102 Blossomfield Road / Dingle Lane / Danford Lane junction near Solihull College and Tudor Grange has changed from a roundabout to traffic signals with a controlled crossing and cycle lanes.",
         stats=[("23,000", "vehicles a day"), ("2026", "works"), ("Signals", "replace roundabout"), ("Cycle", "priority lanes")],
         keys=["The Blossomfield roundabout is being replaced with traffic signals.", "About 23,000 vehicles use it each day.", "A controlled crossing on Dingle Lane and cycle-priority lanes are included.", "It's beside Solihull College, Alderbrook and Tudor Grange — heavy student traffic."],
         body="""<p class="lead">The junction of the B4102 Blossomfield Road, Dingle Lane and Danford Lane carries around 23,000 vehicles a day, close to Solihull College's Blossomfield campus, Alderbrook School and Tudor Grange Academy. Solihull Council is replacing the roundabout with traffic signals, a controlled crossing on Dingle Lane and cycle-priority lanes. A temporary order for the works ran from 20 July to 18 September 2026.</p>
<h2>What changes for learners</h2><ul><li><b>Lights, not give-way.</b> Your decision is now about the signals and the junction ahead being clear — not gaps from the right.</li><li><b>Cycle lanes.</b> Check for cyclists on your left before turning left, and don't stop in advanced stop boxes.</li><li><b>Pedestrians.</b> Students cross here in large numbers at the start and end of the day. Give way to people crossing the road you're turning into.</li></ul>
<h2>Why it matters for your test</h2><p>Shirley test routes reach this side of Solihull. A junction that changed recently is exactly where people revert to old habits.</p>""",
         faqs=[("Is Blossomfield roundabout being replaced?", "Yes — with traffic signals, a controlled crossing on Dingle Lane and cycle-priority lanes."),
               ("How busy is the Blossomfield junction?", "About 23,000 vehicles a day.")],
         src=["blossom", "blossom2"]),
    dict(slug="solihull-speed-cameras-20mph-and-enforcement", title="Solihull speed cameras, 20mph zones and traffic enforcement", short="Cameras, 20mph & enforcement",
         seo="Solihull Speed Cameras, 20mph Zones & Traffic Cameras (2026 Guide) | SQ",
         desc="Every enforcement learner drivers meet in Solihull: A34 and village average speed cameras, the four moving-traffic cameras, bus lanes, red routes, school 20mph limits and collision figures.",
         stats=[("4", "moving-traffic camera sites"), ("2023", "A34 average speed cameras"), ("111", "collisions in Solihull town, 2024"), ("2030", "road safety strategy horizon")],
         keys=["Average speed cameras: A34 Shirley and four villages.", "Moving-traffic cameras: A34 U-turn (live 2026), Warwick Road/New Road yellow box, Elm Farm Avenue school street, Station Road/Poplar Road.", "Red routes on the A34, Dog Kennel Lane, Lode Lane and Hobs Moat Road.", "School 20mph limits are being rolled out borough-wide."],
         body="""<p class="lead">Solihull has more traffic enforcement than many learners expect. Most of it you'll never notice if you drive the way the examiner wants. Here's the full list.</p>
<h2>Average speed cameras</h2><ul><li><b>A34 Stratford Road, Shirley</b> — 40mph, Marshall Lake Road to M42 J4, since January 2023. <a href="a34-stratford-road-shirley.html">A34 guide</a>.</li><li><b>Villages</b> — Berkswell, Hampton-in-Arden, Meriden and Balsall Common, funded from HS2's road-safety allocation.</li></ul>
<h2>Moving-traffic cameras</h2><div class="rx-table-wrap"><table class="rx-table"><thead><tr><th>Site</th><th>Catches</th><th>Status (Oct 2026)</th></tr></thead><tbody>
<tr><td>A34 Stratford Road / Richard Lewis Way</td><td>Banned U-turns</td><td>Live from 1 June 2026 (warning letters for first offences for six months)</td></tr>
<tr><td>B4102 Warwick Road / New Road</td><td>Stopping in the yellow box</td><td>Planned</td></tr>
<tr><td>Elm Farm Avenue, Marston Green</td><td>School Street (8:20–9:00am, 2:45–3:45pm)</td><td>Planned</td></tr>
<tr><td>Station Road into Poplar Road</td><td>Entering the pedestrian/bus zone</td><td>Planned</td></tr></tbody></table></div>
<h2>Bus lanes and red routes</h2><p>Lode Lane bus lanes are CCTV-enforced. Red routes (no stopping) cover the A34, Dog Kennel Lane, Lode Lane and Hobs Moat Road. <a href="lode-lane-hobs-moat-road-bus-lanes.html">Lode Lane guide</a>.</p>
<h2>School 20mph limits and School Streets</h2><p>The council has assessed every school location and is rolling out 20mph limits year by year — the first order took effect on 28 August 2025. Some primary schools have "School Streets" that close to traffic at opening and closing times.</p>
<h2>Collisions</h2><p>Crashview's analysis of STATS19 data counts 118 collisions in the Solihull town area in 2023 and 111 in 2024; the most common limit at crash sites is 30mph. The council's Road Safety Strategy runs to 2030.</p>""",
         faqs=[("Where are the speed cameras in Solihull?", "Average speed cameras on the A34 in Shirley and in Berkswell, Hampton-in-Arden, Meriden and Balsall Common."),
               ("Does Solihull have bus lane cameras?", "Yes — Lode Lane's bus lanes are CCTV-enforced."),
               ("Is Solihull going 20mph?", "Around schools, village centres and retail centres — not borough-wide.")],
         src=["pcc_cam", "villages_cam", "mte", "mte_news", "mte_consult", "school20", "crash", "strategy", "lode"]),
]


def road_page(r):
    path = f"solihull/{r['slug']}.html"
    others = [x for x in ROADS if x["slug"] != r["slug"]][:2]
    rel = [(f"solihull/{x['slug']}.html", "Road guide", x["title"], x["desc"][:100] + "…") for x in others]
    body = r["body"] + f'<p class="note">{CHECKED}</p>'
    return SOL.S(path, r["seo"], "Solihull road guide", (r["short"], path), r["title"], r["desc"], r["stats"], r["keys"], body,
                 r["faqs"] + [("Do you teach on this road?", "Yes — SQ Driving School teaches across Solihull and builds up to roads like this once the basics are solid.")],
                 [C[k] for k in r["src"]], rel)


def hub():
    path = "solihull/solihull-road-guides.html"
    cards = "".join(f'<a class="rx-study" href="{x["slug"]}.html" data-reveal="up"><span class="k-cat">{x["short"]}</span><h3>{x["title"]}</h3><p>{x["desc"][:120]}…</p></a>' for x in ROADS)
    body = f"""<p class="lead">{len(ROADS)} road guides written for learner drivers in Solihull — every speed limit, camera, bus lane, new junction and roadwork we could verify from council orders, National Highways, TfWM and HS2. Nobody else publishes this.</p>
<div class="grid grid--2" data-stagger=".05">{cards}</div>"""
    return SOL.S(path, "Solihull Roads Guide for Learner Drivers: A34, M42, A45, A41 & More | SQ", "Solihull roads", ("Road guides", path),
                 "Solihull roads: the learner driver's guide", "Every major Solihull road explained for learners — the A34, M42 junctions 3A–6, A45, A41, Lode Lane, the town centre, A452 and HS2, village speed limits and cameras.",
                 [(str(len(ROADS)), "road guides"), ("2026", "limits & works"), ("4", "camera sites"), ("100%", "sourced")],
                 ["Every guide is sourced from council orders and official bodies.", "Covers cameras, limits, bus lanes and roadworks.", "Written for learners and new drivers.", "Updated October 2026."],
                 body, [("Which Solihull roads are on the driving test?", "Shirley routes use the A34 heavily; Garretts Green and South Yardley use the A45.")], [C["mte"], C["j6"], C["sprint"]],
                 [("solihull/shirley-driving-test-centre-routes.html", "Test routes", "Shirley test routes", "Solihull's own test centre.")])


def all_pages():
    out = {"solihull/solihull-road-guides.html": hub()}
    for r in ROADS:
        out[f"solihull/{r['slug']}.html"] = road_page(r)
    return out
