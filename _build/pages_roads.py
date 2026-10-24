"""Greater Manchester road & junction guides — roads/<slug>.html plus the roads.html hub.

One hand-written guide per road: what it is, what catches learners out, how we teach it, and (worked out from
pages_routes) which driving-test centres use it. Road numbers are only given where we're sure of them.
Facts kept conservative: no invented speed limits, layouts or casualty figures."""
from hub_shell import *
import pages_routes as RT
import pages_seo as SEO

HOODS = {h["slug"]: h for h in SEO.neighbourhoods()}
SIDE = (f'<p>£35/hr manual or automatic · single hour £40 · 10 hours £350 (£320 for NHS staff, students and M16, M18 &amp; M19) · door-to-door pick-up.</p>'
        f'<a class="btn btn--red btn--block" href="#book">{icon("calendar")} Book in 60 seconds</a>')
SRC = [("GOV.UK — The Highway Code", "https://www.gov.uk/guidance/the-highway-code"),
       ("GOV.UK — Learner drivers on motorways (from 4 June 2018)", "https://www.gov.uk/government/news/learner-drivers-will-be-allowed-on-motorways-from-2018"),
       ("Transport for Greater Manchester — roads and travel", "https://tfgm.com/")]

# slug, name, number (or ""), where, what, [(hard title, how to handle)], teach, hoods, motorway?
R = [
 ("mancunian-way", "The Mancunian Way", "A57(M)", "Manchester city centre (Ardwick to Chester Road)",
  "Manchester's elevated urban motorway runs along the southern edge of the city centre, linking the A6 and Ardwick with Chester Road and the A56. Because it's a motorway, motorway rules apply — no stopping, no cyclists, and slip roads that join and leave on short merges above the streets.",
  [("Short slip roads", "Build speed early on the slip road and pick your gap from the mirrors, not at the last second."), ("Exits close together", "Read the overhead signs and get into lane early — there isn't room to change late."), ("Motorway rules in the city", "No stopping, hard shoulders aren't there to use, and learners may only drive it with an approved instructor in a dual-control car.")],
  "We only take learners onto the Mancunian Way once slip-road merging is solid on quieter dual carriageways, and we drive it first as a demonstration so you know where every exit comes.", ["ardwick", "hulme", "chorlton-on-medlock", "city-centre"], True),
 ("princess-parkway", "Princess Road & Princess Parkway", "A5103", "Hulme and Moss Side to Northenden and the M60/M56",
  "One of south Manchester's main arteries: Princess Road runs out of the city through Moss Side and Whalley Range, then becomes the faster dual-carriageway Princess Parkway past Chorlton and Withington towards Northenden. It features on West Didsbury test routes.",
  [("Changing speed limits", "The limit rises and falls along the route — check every sign and repeater, and don't assume a wide road is a fast one."), ("Big signal-controlled junctions", "Junctions with Barlow Moor Road and Mauldeth Road West have several lanes — read the arrows on the road early."), ("Joining from side roads", "Traffic is quick; wait for a real gap rather than forcing out.")],
  "We build up from the slower Princess Road end to the Parkway, practising lane choice at the big junctions until you can do it without being told.", ["moss-side", "whalley-range", "chorlton-cum-hardy", "withington", "northenden"], False),
 ("kingsway", "Kingsway", "A34", "Fallowfield and Levenshulme to Burnage, East Didsbury and Parrs Wood",
  "A long, straight dual carriageway through south Manchester, with retail parks at its southern end around Parrs Wood. Traffic lights, right turns across the central reservation and busy shopping traffic make it a great place to practise lane discipline.",
  [("Right turns across the reservation", "Position in the right-turn lane, wait in the gap if it's marked, and only go when both carriageways are clear."), ("Retail-park traffic", "Cars slow suddenly to turn into car parks — look well ahead and keep a two-second gap."), ("Lane changes on a long straight", "Mirror, signal and blind-spot check every time — the straight road makes people careless.")],
  "Kingsway is our go-to for learning dual-carriageway lane discipline at moderate speeds before anything faster.", ["burnage", "levenshulme", "fallowfield", "east-didsbury", "didsbury"], False),
 ("wilmslow-road", "Wilmslow Road (Rusholme, Fallowfield & Withington)", "", "Oxford Road corridor south through Rusholme's Curry Mile to Didsbury",
  "One of the busiest bus corridors in Europe, Wilmslow Road runs through the Curry Mile in Rusholme, past the student areas of Fallowfield and Withington and on to Didsbury village. Buses, cycle lanes, pedestrians and parked cars all compete for space.",
  [("Bus-stop bypasses and cycle lanes", "Watch for cyclists coming alongside and pedestrians crossing to bus-stop islands."), ("Pedestrians stepping out", "Especially around the Curry Mile at night and near the universities — keep your speed down and cover the brake."), ("Bus priority sections", "Read the times on bus-lane signs; some stretches are bus-only at set hours.")],
  "We bring you here once your car control is automatic, because it trains the most important test skill of all — looking far enough ahead.", ["rusholme", "fallowfield", "withington", "didsbury"], False),
 ("oxford-road", "Oxford Road", "", "St Peter's Square and the universities to Rusholme",
  "The road through the University of Manchester, Manchester Metropolitan University and the Manchester Royal Infirmary. Large parts are restricted to buses, cycles and taxis at set times, with segregated cycle lanes and bus-stop islands.",
  [("Bus gates and restrictions", "Read the signs before you turn in — getting it wrong can mean a fine once you've passed."), ("Huge numbers of pedestrians", "Students cross everywhere; expect people stepping out between buses."), ("Hospital traffic", "Ambulances use this corridor — move over safely and never stop on a crossing to let one through.")],
  "We show you the legal routes around the restricted sections and practise the junctions that ordinary cars can use.", ["chorlton-on-medlock", "rusholme", "hulme"], False),
 ("stockport-road", "Stockport Road", "A6", "Ardwick through Longsight and Levenshulme towards Stockport",
  "The A6 heads south-east out of the city through Longsight and Levenshulme — a classic shopping street with bus lanes, side roads every few metres and constant parking and unloading.",
  [("Side roads every few metres", "Watch for cars nosing out and give a clear signal if you're turning."), ("Bus lanes", "Check the hours; outside them you can use the lane, inside them you can't."), ("Parked cars and double-parking", "Check mirrors early and give room when passing.")],
  "Levenshulme learners practise here a lot — it's busy but slow, which makes it ideal for building observation habits.", ["longsight", "levenshulme", "ardwick"], False),
 ("hyde-road", "Hyde Road", "A57", "Ardwick through Belle Vue and Gorton towards Denton",
  "A wide main road heading east, with big junctions near Belle Vue, a mix of retail and housing, and a steady stream of buses and goods vehicles.",
  [("Multi-lane signal junctions", "Choose your lane from the road markings well before the lights."), ("Large vehicles", "Leave extra room; lorries need space to turn."), ("Speed management", "Wide sections tempt people to speed — keep checking the limit.")],
  "Gorton and Belle Vue learners use Hyde Road to step up from estate roads to proper main-road driving.", ["gorton", "belle-vue", "ardwick", "west-gorton"], False),
 ("ashton-old-road", "Ashton Old Road", "A635", "Ardwick through Openshaw towards Ashton-under-Lyne",
  "Runs east past the Etihad Campus area through Openshaw, with long straights, pedestrian crossings and junctions with busy side roads.",
  [("Pedestrian crossings", "Approach at a speed where you could stop, and check for people waiting."), ("Matchday traffic", "Around the Etihad on event days roads fill quickly and some close — plan lessons around fixtures."), ("Right turns", "Wait for a safe gap in oncoming traffic; don't feel pressured by cars behind.")],
  "Good for practising steady main-road driving with plenty of crossings to anticipate.", ["openshaw", "ardwick", "beswick", "clayton"], False),
 ("ashton-new-road", "Ashton New Road", "A662", "Ancoats and the Etihad Campus to Clayton and Droylsden",
  "Shares space with Metrolink trams on parts of its route east, past the Etihad Stadium and through Clayton.",
  [("Trams alongside", "Know where the tram stops and crossings are; never stop on the tracks."), ("Event days", "Huge crowds near the stadium — slow right down."), ("Junction lanes with tram priority", "Follow traffic signals for cars, not the tram signals.")],
  "We use Ashton New Road to teach tram awareness safely, alongside our guide to driving with Metrolink.", ["clayton", "beswick", "ancoats"], False),
 ("oldham-road", "Oldham Road", "A62", "Ancoats through Miles Platting and Newton Heath to Failsworth and Oldham",
  "A long north-east radial with shops, bus stops and a mix of 30 and faster sections as it leaves the city.",
  [("Bus stops and buses pulling out", "Anticipate buses indicating and let them out where it's safe."), ("Speed changes", "Limits change as the road leaves built-up stretches — keep checking."), ("Junction observation", "Busy side roads join from both sides.")],
  "Newton Heath and Miles Platting learners build up to Oldham Road once they're comfortable on estates.", ["newton-heath", "miles-platting", "ancoats"], False),
 ("rochdale-road", "Rochdale Road", "A664", "Collyhurst through Harpurhey and Blackley towards Middleton",
  "North Manchester's main road to Middleton and Rochdale: hills, shopping parades in Harpurhey and busy junctions.",
  [("Hill starts at lights", "Handbrake and clutch control (or brake hold in an automatic) on the climbs."), ("Shopping parades", "Pedestrians and parked cars around Harpurhey."), ("Bus lanes", "Check the hours on each sign.")],
  "We use the gradients here for hill starts once you can move off smoothly on the flat.", ["harpurhey", "blackley", "collyhurst"], False),
 ("cheetham-hill-road", "Cheetham Hill Road", "A665", "Manchester city centre to Cheetham Hill and Prestwich",
  "A busy shopping and business street heading north out of the centre, and one of the main roads on Cheetham Hill driving-test routes.",
  [("Constant stopping vehicles", "Deliveries and taxis stop suddenly — look well ahead."), ("Pedestrians crossing between cars", "Keep your speed down near the shops."), ("Lane choice near the city", "Multi-lane approaches towards the centre and the inner ring road.")],
  "Essential practice if you're testing at Cheetham Hill.", ["cheetham-hill", "strangeways", "crumpsall"], False),
 ("bury-new-road", "Bury New Road", "A56", "Strangeways and Cheetham Hill through Broughton to Prestwich and Whitefield",
  "Another Cheetham Hill test-route road: a long radial with shops, synagogues and schools, then faster sections towards Prestwich.",
  [("School-run times", "Children crossing and parked cars at drop-off and pick-up."), ("Changing character", "City-style junctions near Strangeways, then faster suburban stretches."), ("Right turns into side roads", "Positioning and a safe gap in oncoming traffic.")],
  "We practise it at different times of day so it holds no surprises on test day.", ["cheetham-hill", "broughton", "prestwich"], False),
 ("great-ancoats-street", "Great Ancoats Street", "A665", "The inner ring road between Ancoats and the Northern Quarter",
  "Part of the city's inner ring road, with multiple lanes, signal junctions and heavy pedestrian traffic between Ancoats and the Northern Quarter.",
  [("Multi-lane junctions", "Pick your lane from the signs and stay in it through the junction."), ("Pedestrians and cyclists", "Lots of crossing points between Ancoats and the city."), ("Keeping up a sensible pace", "Too slow is a fault as well as too fast — match the traffic safely.")],
  "A step up from M1's one-way streets towards test-standard city driving.", ["ancoats", "city-centre", "new-islington"], False),
 ("alan-turing-way", "Alan Turing Way", "A6010", "The Etihad Campus between Ashton New Road and Ashton Old Road",
  "A modern dual carriageway past the Etihad Stadium and the Manchester Regional Arena, with wide junctions and cycle lanes.",
  [("Event closures", "Roads near the stadium close or fill before and after events."), ("Wide junctions", "Take care to end up in the correct lane."), ("Cyclists", "Segregated cycle lanes with crossings at junctions.")],
  "Quiet outside event days — a good place for early dual-carriageway practice.", ["beswick", "clayton", "openshaw"], False),
 ("barlow-moor-road", "Barlow Moor Road", "A5145", "Chorlton through Withington to Didsbury",
  "A West Didsbury test-route road linking Chorlton, Withington and Didsbury, with shops, schools and the Princess Parkway junction.",
  [("The Princess Parkway junction", "Multi-lane signals — read the lane arrows well before."), ("Village centres", "Pedestrians and parked cars in Chorlton and Didsbury."), ("Buses", "Frequent stops; anticipate them pulling out.")],
  "We practise it in both directions because examiners use it both ways.", ["chorlton-cum-hardy", "withington", "didsbury", "west-didsbury"], False),
 ("wilbraham-road", "Wilbraham Road", "A6010", "Chorlton to Fallowfield",
  "Links Chorlton with Whalley Range and Fallowfield, featuring on West Didsbury test routes, with Metrolink stops, shops and student housing.",
  [("Trams at Chorlton", "Know where the tram stop and crossings are."), ("Student areas", "Pedestrians and cyclists around Fallowfield."), ("Roundabouts and mini-roundabouts", "Signal and position correctly for each one.")],
  "A favourite for practising a mix of everything in a short distance.", ["chorlton-cum-hardy", "whalley-range", "fallowfield"], False),
 ("palatine-road", "Palatine Road", "", "West Didsbury and Northenden",
  "A tree-lined residential road through West Didsbury down to Northenden, close to the West Didsbury test centre.",
  [("Parked cars both sides", "Judge gaps and who should give way."), ("Speed", "It feels quiet, but limits still apply — watch for 20 mph areas."), ("Junction observation", "Many side roads with restricted views.")],
  "Calm enough for early lessons, close enough to the test centre to matter later.", ["west-didsbury", "didsbury", "northenden"], False),
 ("mauldeth-road", "Mauldeth Road & Mauldeth Road West", "", "Chorlton across to Burnage",
  "An east–west road across south Manchester, crossing Princess Parkway and Kingsway, and used on West Didsbury routes.",
  [("Crossing major roads", "Big signal junctions with the Parkway and Kingsway."), ("Schools", "Children and parked cars at peak times."), ("Bus stops", "Anticipate buses.")],
  "Great for linking quiet residential driving with major-junction practice.", ["chorlton-cum-hardy", "withington", "burnage", "fallowfield"], False),
 ("chester-road", "Chester Road", "A56", "Manchester city centre through Old Trafford and Stretford to Sale",
  "The A56 south-west of the city, past Old Trafford football and cricket grounds towards Stretford and Sale — multi-lane, busy and on Sale test routes.",
  [("Multi-lane roads", "Lane discipline and mirrors before every change."), ("Matchdays", "Old Trafford events change everything — plan around them."), ("Big junctions near the M60", "Read the signs early.")],
  "Essential for anyone testing at Sale.", ["old-trafford", "stretford", "hulme"], False),
 ("washway-road", "Washway Road", "A56", "Sale to Altrincham",
  "The A56 through Sale towards Brooklands and Altrincham, a Sale test-route road with shops, schools and frequent junctions.",
  [("Busy junctions", "Lots of traffic turning in and out."), ("Bus stops", "Anticipate buses."), ("Changing speed limits", "Check the limit as the road changes character.")],
  "We practise Washway Road heavily with learners testing at Sale.", ["sale", "brooklands", "altrincham"], False),
 ("east-lancashire-road", "East Lancashire Road", "A580", "Salford (Swinton, Walkden) towards Liverpool",
  "A fast dual carriageway heading west from Salford through Swinton and Worsley, with big junctions and the M60 and M61 nearby.",
  [("Higher speeds", "Keep a safe gap and look further ahead."), ("Joining and leaving", "Use slip roads properly and check blind spots."), ("Large junctions", "Plan your lane well before.")],
  "One of the best roads for dual-carriageway confidence before motorway lessons.", ["swinton", "walkden", "worsley", "pendlebury"], False),
 ("regent-road", "Regent Road", "A57", "Salford, between the M602 and Manchester city centre",
  "A busy multi-lane road carrying M602 traffic into the city, with retail parks and big signal junctions.",
  [("Multi-lane traffic", "Plan lane changes early."), ("Retail park entrances", "Cars turning suddenly."), ("Traffic from the M602", "Fast traffic arriving from the motorway.")],
  "Good practice for heavy, multi-lane city traffic.", ["ordsall", "salford-quays", "pendleton"], False),
 ("trafford-road", "Trafford Road", "A5063", "Salford Quays and MediaCityUK to Trafford Park",
  "Links Salford Quays and MediaCityUK with Trafford Park — wide, busy and full of commuters, buses and Metrolink crossings nearby.",
  [("Commuter peaks", "Very heavy at rush hour."), ("Wide junctions", "Lane choice."), ("Pedestrians around the Quays", "Lots of people crossing.")],
  "We use it for learners who work at MediaCityUK or Trafford Park.", ["salford-quays", "ordsall", "old-trafford"], False),
 ("m602", "The M602", "M602", "Salford — from the M60/M62 into Salford and the city",
  "A short motorway into Salford ending on Regent Road. Learners may drive it with an approved instructor in a dual-control car.",
  [("Joining from the M60/M62", "Plan your lane on the main motorway early."), ("Motorway ending", "Speed reduces into city roads — watch for the change."), ("Lane changes", "Mirror, signal, blind spot.")],
  "A common first motorway for Salford learners because it's short and straightforward.", ["eccles", "pendleton", "ordsall"], True),
 ("m56", "The M56", "M56", "South Manchester to Manchester Airport and Cheshire",
  "Runs from the end of Princess Parkway past Manchester Airport towards Cheshire. Learners can drive it with an approved instructor in a dual-control car.",
  [("Airport traffic", "Drivers looking for terminal exits change lanes late."), ("Joining from Princess Parkway", "Read lane markings early."), ("Higher speeds", "Keep a two-second gap — more in the wet.")],
  "Often our first motorway lesson with south Manchester learners.", ["wythenshawe", "northenden", "baguley"], True),
 ("a555", "A555 Manchester Airport Relief Road", "A555", "Hazel Grove and Bramhall area to Manchester Airport",
  "A modern dual carriageway linking south Stockport with Manchester Airport, with large roundabouts and fast traffic.",
  [("Large roundabouts at speed", "Slow down early and choose your lane."), ("Fast traffic", "Keep a safe following distance."), ("Cyclist and pedestrian crossings", "Some junctions have crossings — watch for them.")],
  "Ideal for higher-speed practice and big roundabouts before a motorway lesson.", ["bramhall", "hazel-grove", "cheadle-hulme"], False),
 ("wellington-road-stockport", "Wellington Road North & South (Stockport)", "A6", "Through Stockport town centre",
  "The A6 through Stockport, crossing the town centre near the station and the Mersey, with busy junctions and buses.",
  [("Town-centre junctions", "Several lanes and signals close together."), ("Buses and taxis", "Frequent stops near the station."), ("Hills", "Gradients in and around the centre.")],
  "Stockport learners practise here before tests at Bredbury.", ["stockport", "heaton-chapel", "edgeley"], False),
 ("stockport-road-west-bredbury", "Stockport Road West (Bredbury)", "A560", "Bredbury, near the M60",
  "A Bredbury test-route road near M60 junction 25, with industrial traffic, roundabouts and retail.",
  [("Lorries", "Industrial estates bring large vehicles."), ("Roundabouts", "Lane choice and signals."), ("Motorway junction traffic", "Cars joining and leaving the M60.")],
  "Key practice for anyone testing at Bredbury.", ["bredbury", "romiley"], False),
 ("ashton-road-bredbury", "Ashton Road (Bredbury)", "A6017", "Bredbury towards Denton",
  "A Bredbury test-route road heading north from Bredbury, mixing residential stretches with junctions near the test centre.",
  [("Junction observations", "Side roads with limited views."), ("Speed changes", "Check the limit often."), ("Buses", "Stops along the route.")],
  "We run through it with every Bredbury learner.", ["bredbury"], False),
 ("broadway-chadderton", "Broadway (Chadderton)", "A663", "Chadderton, near the test centre and Broadway Business Park",
  "The main road near Chadderton test centre, with business-park roundabouts and fast-moving traffic.",
  [("Business-park roundabouts", "Count exits and pick your lane early."), ("Fast traffic", "Judge gaps carefully when joining."), ("Lorries and vans", "Leave space.")],
  "Must-practise for Chadderton tests.", ["chadderton"], False),
 ("a627m", "The A627(M)", "A627(M)", "Chadderton/Oldham to Rochdale",
  "A short motorway linking Oldham and Rochdale with the M62. Learners can drive it with an approved instructor in a dual-control car.",
  [("Merging", "Match speed on the slip road."), ("Lane discipline", "Keep left unless overtaking."), ("Motorway junction with the M62", "Read the signs early.")],
  "A handy first motorway for learners in Oldham and Rochdale.", ["chadderton", "middleton"], True),
 ("kingsway-rochdale", "Kingsway (Rochdale)", "", "Rochdale, near the test centre",
  "A main road near Rochdale test centre, with the Kingsway Business Park and busy roundabouts nearby.",
  [("Roundabouts", "Signal and position for each exit."), ("Business traffic", "Vans and lorries."), ("Speed", "Watch the limit as the road changes.")],
  "We practise it with every Rochdale learner.", ["rochdale"], False),
 ("queensway-rochdale", "Queensway roundabout (Rochdale)", "", "Rochdale, on Rochdale test routes",
  "A large roundabout that appears on Rochdale test routes, with several entries and lanes.",
  [("Lane choice", "Use the road markings and signs."), ("Signalling", "Signal left after passing the exit before yours."), ("Traffic from the right", "Look right early and keep checking.")],
  "We drive it until you can choose your lane without prompting.", ["rochdale"], False),
 ("st-peters-way-bolton", "St Peter's Way (Bolton)", "A666", "Bolton town centre",
  "Bolton's main through-route on the A666, with multi-lane sections and junctions near the town centre, used on Bolton test routes.",
  [("Lane changes", "Plan early; lanes split for different destinations."), ("Junctions close together", "Read signs well ahead."), ("Traffic speed", "Keep up safely with the flow.")],
  "Key practice for Bolton tests.", ["bolton"], False),
 ("peel-way-bury", "Peel Way (Bury)", "A56", "Bury's inner ring road",
  "Bury's inner ring road, with roundabouts and junctions that feature on Bury test routes.",
  [("Roundabouts in quick succession", "Deal with each one separately."), ("Lane choice", "Know your exit before you arrive."), ("Pedestrians near the town centre", "Watch crossings.")],
  "We practise the ring road in both directions for Bury learners.", ["bury"], False),
 ("atherleigh-way", "Atherleigh Way", "A579", "Atherton and Leigh",
  "A faster road linking Atherton and Leigh, used on Atherton test routes.",
  [("Higher speeds", "Look further ahead and keep a safe gap."), ("Roundabouts", "Plan your lane."), ("Joining traffic", "Watch for cars joining from side roads.")],
  "Good practice for Atherton tests.", ["atherton", "leigh"], False),
 ("hyde-road-denton", "Manchester Road & Hyde Road (Denton)", "", "Denton in Tameside",
  "Main roads through Denton, close to M60 and M67 junctions, with busy shopping areas.",
  [("Motorway junction traffic", "Cars joining and leaving."), ("Shopping streets", "Pedestrians and parked cars."), ("Lane choice", "Read signs early.")],
  "We use Denton's main roads for Tameside learners building up to tests.", ["denton"], False),
 ("piccadilly-gardens", "Piccadilly Gardens & tram crossings", "", "Manchester city centre",
  "The heart of Manchester's tram network, where several Metrolink lines meet and roads cross the tracks.",
  [("Tram crossings", "Never stop on the tracks while queuing."), ("Tram signals", "White tram signals are for trams — follow normal traffic lights."), ("Pedestrians", "Very busy all day.")],
  "We only bring you here when you're ready, and we practise it slowly.", ["city-centre", "piccadilly"], False),
 ("st-peters-square", "St Peter's Square", "", "Manchester city centre",
  "A city-centre square where Metrolink lines meet, with restricted roads and one-way streets around it.",
  [("Restricted access", "Some roads are trams or buses only."), ("One-way streets", "Read no-entry signs."), ("Pedestrians", "Lots of crossing points.")],
  "We practise the approach slowly so you know where cars can and can't go.", ["city-centre"], False),
 ("trafford-centre-roads", "Roads around the Trafford Centre", "", "Trafford, near the M60",
  "Busy roads around the Trafford Centre with large roundabouts, retail traffic and motorway junctions.",
  [("Large roundabouts", "Plan lanes early."), ("Shoppers driving slowly or stopping", "Look far ahead."), ("Motorway traffic", "Cars joining and leaving the M60.")],
  "Great for practising busy, unpredictable traffic before a test.", ["urmston", "davyhulme", "stretford"], False),
 ("manchester-fort", "Roads around Manchester Fort", "", "Cheetham Hill",
  "Roads around the Manchester Fort shopping park, signed on Cheetham Hill test routes, with retail traffic and junctions.",
  [("Retail traffic", "Cars turning in and out."), ("Pedestrians", "Crossing to the shops."), ("Junctions", "Observation and positioning.")],
  "Practise it before any Cheetham Hill test.", ["cheetham-hill"], False),
 ("sale-water-park", "Roads to Sale Water Park", "", "Sale, near the M60",
  "Roads signed for Sale Water Park, used on Sale test routes, with roundabouts and changing speed limits.",
  [("Roundabouts", "Lane choice."), ("Changing limits", "Watch for signs."), ("Cyclists", "Leisure cyclists near the park.")],
  "We practise them for Sale tests.", ["sale", "ashton-upon-mersey"], False),
]


# which test centres' reported routes use each road — checked by hand against pages_routes
TESTS = {"princess-parkway": ["west-didsbury"], "barlow-moor-road": ["west-didsbury"], "wilbraham-road": ["west-didsbury"], "mauldeth-road": ["west-didsbury"],
         "palatine-road": ["west-didsbury"], "cheetham-hill-road": ["cheetham-hill"], "bury-new-road": ["cheetham-hill"], "manchester-fort": ["cheetham-hill"],
         "chester-road": ["sale"], "washway-road": ["sale"], "sale-water-park": ["sale"], "stockport-road-west-bredbury": ["bredbury"], "ashton-road-bredbury": ["bredbury"],
         "broadway-chadderton": ["chadderton"], "kingsway-rochdale": ["rochdale"], "queensway-rochdale": ["rochdale"], "st-peters-way-bolton": ["bolton"],
         "peel-way-bury": ["bury"], "atherleigh-way": ["atherton"]}
CBY = {c["slug"]: c for c in RT.C}


def test_links(slug):
    return [CBY[x] for x in TESTS.get(slug, [])]


def road_page(r):
    slug, name, no, where, what, hard, teach, hoods, mway = r
    path = f"roads/{slug}.html"
    tests = test_links(slug)
    hard_html = "".join(f"<li><b>{t}.</b> {d}</li>" for t, d in hard)
    hood_chips = "".join(f'<a class="chip" href="../driving-lessons/{h}.html">{HOODS[h]["name"]}</a>' for h in hoods if h in HOODS)
    test_html = ("<p>This road appears on reported driving-test routes for: " + ", ".join(f'<a href="../test-routes/{c["slug"]}-driving-test-routes.html">{c["name"]}</a>' for c in tests) + ".</p>") if tests else ""
    body = f"""<p class="lead">{what}</p>
<h2>Where it is</h2><p>{name}{f" ({no})" if no else ""} — {where}.</p>
<h2>What catches learners out</h2><ul>{hard_html}</ul>
<h2>How we teach it</h2><p>{teach}</p>
{"<h2>Motorway rules for learners</h2><p>Learner drivers have been allowed on motorways in England since June 2018 — but only with an approved driving instructor in a car with dual controls. You can't practise it with a friend or family member.</p>" if mway else ""}
{"<h2>On the driving test</h2>" + test_html if test_html else ""}
<h2>Areas nearby</h2><div class="hero__badges">{hood_chips or '<a class="chip" href="../areas.html">All areas</a>'}</div>
<p class="mt-2"><a href="../roads.html">All Greater Manchester road guides →</a></p>"""
    faqs = [(f"Will I drive on {name} in my lessons?", "If it's near where you live or on your test centre's routes, yes — once you're ready. We always build up from quieter roads first."),
            (f"Is {name} on the driving test?", ("It appears on reported routes for " + ", ".join(c["name"] for c in tests) + ". Routes vary, so we practise the whole area.") if tests else "It isn't one of the roads we've seen on reported test routes, but it's useful everyday practice."),
            ("How much are lessons?", "£35/hr for lessons of 2 hours or more, £40 for a single hour, £350 for 10 hours (£320 for NHS staff, students and M16/M18/M19).")]
    stats = [(no or "Local road", "road"), (str(len(hard)), "things to master"), (str(len(tests)) if tests else "—", "test centres using it"), ("£35", "per hour")]
    keys = [h[0] for h in hard] + ["Practised with dual controls"]
    return shell(path, f"{name} — Learner Driver Guide | SQ Driving", "Road guide", [("Road guides", "roads.html"), (name, path)], f"{name}: a learner's guide.",
                 f"What learners find hard on {name}{f' ({no})' if no else ''}, how we teach it" + (", and the test centres that use it." if tests else "."),
                 stats, keys, body, faqs, SRC, [("driving-lessons-manchester.html", "Manchester", "Driving lessons in Manchester", "Prices, every area and the learner planner."),
                                                ("guides/roundabouts.html", "Guide", "Roundabouts made simple", "Lanes, signals and timing."),
                                                ("knowledge/m60-ring-road-guide.html", "Guide", "The M60 ring road", "Junctions and lanes explained.")],
                 side_title="Lessons on these roads", booking_heading="Book a lesson in 60 seconds", active="areas.html", side_html=SIDE)


def hub():
    cards = [(f"roads/{r[0]}.html", "Motorway" if r[8] else "Road guide", r[1], (r[2] + " · " if r[2] else "") + r[3], "road") for r in R]
    return hub_page("roads.html", "Greater Manchester Road Guides for Learners | SQ Driving", "Road guides", "Greater Manchester road guides.",
                    f"{len(R)} hand-written guides to the roads, motorways and junctions learners in Greater Manchester worry about most — and how we teach them.", cards)


def all_pages():
    out = {f"roads/{r[0]}.html": road_page(r) for r in R}
    out["roads.html"] = hub()
    return out
