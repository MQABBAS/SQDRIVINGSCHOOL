"""Test-route guides — one in-depth, hand-researched page per Greater Manchester driving test centre (test-routes/).

DVSA stopped publishing official test routes, so road names come from routes reported by learners and instructors
on public route sheets, cross-checked between sources; low-confidence claims were left out. Pass rates are quoted
with their period and source. No reviews or learner quotes are invented: each page has a real feedback form that
sends to the SQ Driving School team (DriveSQ admin)."""
from hub_shell import *

SRC = {
    "find": ("GOV.UK — Find a driving test centre", "https://www.gov.uk/find-driving-test-centre"),
    "book": ("GOV.UK — Book your driving test", "https://www.gov.uk/book-driving-test"),
    "dvsa": ("DVSA — Car driving test data by test centre (DVSA1203)", "https://www.gov.uk/government/statistical-data-sets/car-driving-test-data-by-test-centre"),
    "top10": ("GOV.UK — Top 10 reasons for failing the driving test", "https://www.gov.uk/government/publications/top-10-reasons-for-failing-the-driving-test"),
    "test": ("GOV.UK — What happens during the driving test", "https://www.gov.uk/driving-test/what-happens-during-test"),
    "pr_gm": ("passrates.uk — Greater Manchester test centres, 2024-25 (from DVSA data)", "https://passrates.uk/counties/greater-manchester"),
    "mm": ("Mancunian Matters — DVSA pass rates, April 2024–March 2025", "https://www.mancunianmatters.co.uk/news/08072025-where-in-greater-manchester-are-you-most-likely-to-fail-your-driving-test/"),
}

# slug, name, borough, address, pass (rate, label, source-key-or-tuple), roads [(no, name, note, tags)], spokes [(label, dir)], landmarks [(name, note)],
# mistakes [(title, why, fix)], intro, area_html, serves, nearby slugs, extra_faq
C = [
    dict(slug="west-didsbury", name="West Didsbury", borough="Manchester", pc="M21 7QY",
         address="Unit 11, Christie Park, Christie Way, West Didsbury, Manchester M21 7QY",
         rate=50.9, rate_note="2024-25, about 17,200 tests", rate_src=("passrates.uk — West Didsbury driving test centre", "https://passrates.uk/guide/west-didsbury-manchester-driving-test-centre"),
         serves="Chorlton, Didsbury, Withington, Fallowfield, Burnage, Levenshulme, Rusholme, Moss Side, Whalley Range, Wythenshawe and Sale Moor",
         intro="West Didsbury is the busiest practical test centre in south Manchester. It sits on Christie Park, an office park facing Princess Road (A5103) beside its junction with Barlow Moor Road — between Chorlton and West Didsbury, a few minutes from junction 5 of the M60. In the 2024-25 test year it carried out around 17,000 car tests, more than almost any other centre in Greater Manchester.",
         area="Routes here mix a fast, multi-lane primary road with dense inner-suburb streets: Victorian terraces lined with parked cars, high streets with crossings and bus stops, traffic-light junctions that come thick and fast, and quieter residential loops used for manoeuvres.",
         roads=[("A5103", "Princess Road / Princess Parkway", "The dual-carriageway spine of south Manchester. Joining it from side roads, choosing a lane early and holding steady speed between sets of lights is where most faults happen.", ("Dual carriageway", "Lane choice", "Traffic lights")),
                ("A5145", "Barlow Moor Road", "Runs right past the centre. Busy traffic-light junctions — including the one with Princess Road — and buses stopping and pulling out.", ("Traffic lights", "Buses")),
                ("A6010", "Wilbraham Road", "Reported on route sheets with turns on and off at traffic lights. Several lanes at junctions and lots of pedestrians near Chorlton.", ("Right turns at lights", "Pedestrians")),
                ("", "Mauldeth Road West", "Appears again and again on reported routes, often as a turn off Princess Road. Residential, with parked cars on both sides — meeting traffic and holding back are key.", ("Parked cars", "Meeting traffic")),
                ("", "Hardy Lane", "Reported as straight ahead at the lights when leaving the centre — an early test of moving off and traffic-light response.", ("Moving off", "Traffic lights")),
                ("", "Alexandra Road South", "Long residential road with side turnings and parked cars; good for junction observations and maintaining a safe speed.", ("Junctions", "Speed")),
                ("", "Burton Road", "West Didsbury's high street: shops, cafés, parked cars and pedestrians stepping out. Speed and hazard awareness matter more than anywhere.", ("High street", "Pedestrians")),
                ("", "Palatine Road", "A typical test road between Didsbury and Northenden, with traffic calming and side roads.", ("Traffic calming",)),
                ("", "Withington side streets", "Narrow terraced streets with parked cars both sides — clearance, meeting traffic and bay or parallel parking.", ("Clearance", "Manoeuvres"))],
         spokes=[("Princess Rd (A5103)", "city / M60 J5"), ("Barlow Moor Rd", "Chorlton"), ("Wilbraham Rd", "Chorlton"), ("Burton Rd", "West Didsbury"), ("Palatine Rd", "Didsbury"), ("Mauldeth Rd W", "Withington")],
         marks=[("Withington Metrolink stop", "Walking distance — handy if you meet your instructor there."), ("Christie Office Park", "Where the test centre is."), ("M60 junction 5", "The nearest motorway junction, south along Princess Parkway."), ("Chorlton", "Shops and junctions along Barlow Moor Road and Wilbraham Road."), ("Burton Road shops", "West Didsbury's café strip — expect pedestrians.")],
         mistakes=[("Late lane choice on Princess Road", "Multi-lane approaches to traffic lights catch learners in the wrong lane and they swerve late.", "Read the lane arrows from the previous set of lights and move across early with a full MSM routine."),
                   ("Joining the dual carriageway too slowly", "Pulling out of a side road onto a 40-feeling road at 15mph forces others to brake.", "Look early, pick a safe gap, and build speed briskly in second then third gear."),
                   ("Meeting traffic on Mauldeth Road West", "Committing into a gap between parked cars when an oncoming car has priority.", "Plan which gap you'll wait in, hold back early, and don't wave others through."),
                   ("Pedestrians on Burton Road", "Driving at the speed limit past crowded pavements and crossings.", "Slow down for the conditions, cover the brake near crossings, and watch for people between parked cars."),
                   ("Right turns at the Wilbraham Road lights", "Waiting in the wrong position or not turning when there's a safe gap.", "Position just left of centre, check the oncoming lane and the pedestrian crossing in the road you're entering.")]),
    dict(slug="sale", name="Sale", borough="Trafford", pc="M33 7ER",
         address="36–38 Poplar Grove, Sale M33 7ER",
         rate=49.1, rate_note="2024-25, about 10,000 tests", rate_src=("passrates.uk — Sale driving test centre", "https://passrates.uk/centres/sale-manchester"),
         serves="Sale, Ashton upon Mersey, Brooklands, Timperley, Altrincham, Stretford, Urmston, Flixton, Partington and parts of Chorlton and Wythenshawe",
         intro="Sale test centre is on Poplar Grove, a short walk from Sale town centre and close to Brooklands. It serves almost all of Trafford and parts of south Manchester. Routes typically leave along Cross Street, the A56 through the middle of Sale, so the first few minutes of every test are on one of the busiest roads in the borough.",
         area="Expect the A56 corridor (Cross Street, Washway Road, Chester Road) with bus lanes and changing speed limits, and then classic suburban Trafford: long residential roads with parked cars, school zones, mini-roundabouts and crossings. Independent driving often follows signs, for example towards Sale Water Park.",
         roads=[("A56", "Cross Street", "Many reported routes leave the centre and join Cross Street. Busy through-traffic, bus stops and traffic lights from the first minute.", ("Moving off", "Buses", "Traffic lights")),
                ("A56", "Washway Road", "The A56 south of Sale town centre. Bus lanes with set hours, speed-limit changes and cameras — read every sign.", ("Bus lanes", "Speed changes")),
                ("A56", "Chester Road", "Continues north towards Stretford, with faster sections and multi-lane junctions.", ("Lane discipline",)),
                ("", "Dane Road", "On many reported routes, often straight after Cross Street. Residential with parked cars and crossings, close to Dane Road Metrolink stop.", ("Parked cars", "Crossings")),
                ("A6144", "Marsland Road", "Residential stretch with parked cars and pedestrian crossings near Brooklands.", ("Crossings", "Parked cars")),
                ("", "Brooklands Road", "A frequent turn on reported routes. Parked cars hide vehicles emerging from side roads, and estate roads nearby have speed humps.", ("Junctions", "Speed humps")),
                ("", "Roads signed for Sale Water Park", "Common for independent driving by following signs. Take your time at the roundabouts and read signs early.", ("Independent driving", "Roundabouts"))],
         spokes=[("Cross St (A56)", "Stretford"), ("Washway Rd (A56)", "Altrincham"), ("Dane Rd", "Sale Water Park"), ("Marsland Rd", "Brooklands"), ("Brooklands Rd", "Timperley")],
         marks=[("Sale town centre", "About half a mile away."), ("The Square shopping centre", "In the town centre — busy junctions around it."), ("Brooklands Metrolink stop", "On the Altrincham line south of the centre."), ("Sale Water Park", "Often used as a destination for independent driving."), ("Sale Moor", "Residential area with mini-roundabouts.")],
         mistakes=[("Driving in a bus lane during its hours", "Washway Road's bus lanes have set times. Entering one when it's in operation is a fault — and a fine after you pass.", "Read the blue sign for times every time; if in doubt, stay out."),
                   ("Moving off too early at junctions", "Emerging onto the A56 or Dane Road before a safe gap, forcing others to slow.", "Wait until you're sure. Undue hesitation is a smaller risk than pulling out in front of someone."),
                   ("Speed control on residential roads", "Driving at 30 where parked cars and school entrances call for much less.", "Match your speed to what you can see, not the sign."),
                   ("Missed speed-limit changes", "Not noticing a change in limit along the A56.", "Scan for repeater signs and street lights; adjust smoothly before the change, not after."),
                   ("Hesitation at roundabouts on the way to Sale Water Park", "Stopping at clear roundabouts during independent driving.", "Look right early on approach so you know whether you can keep moving.")]),
    dict(slug="bredbury", name="Bredbury", borough="Stockport", pc="SK6 2QT",
         address="Lingard Lane, Bredbury, Stockport SK6 2QT",
         rate=54.2, rate_note="2024-25, about 9,900 tests", rate_src=("passrates.uk — Bredbury driving test centre", "https://passrates.uk/centres/bredbury-manchester"),
         serves="Bredbury, Romiley, Marple, Woodley, Brinnington, Reddish, Stockport, Hazel Grove, Bramhall and — since Hyde closed in 2022 — much of Tameside",
         intro="Bredbury test centre is on Lingard Lane beside Bredbury Park Industrial Estate, between Brinnington and Bredbury, a short distance from junction 25 of the M60. When the DVSA closed Hyde test centre in 2022, Bredbury became the nearest centre for many Tameside learners. In 2024-25 it had one of the highest pass rates in Greater Manchester.",
         area="Every reported route starts and ends on Lingard Lane with lorries and vans from the industrial estate. From there routes head out on main roads such as Ashton Road and Stockport Road West towards Romiley and Woodley, with hills, roundabouts, terraced streets and village centres.",
         roads=[("", "Lingard Lane", "The start and finish of every test. Industrial-estate traffic, HGVs turning, and traffic lights where it meets Ashton Road.", ("HGVs", "Traffic lights")),
                ("A6017", "Ashton Road", "Reported early on routes, often with a roundabout. Busy link to M60 junction 25 — expect traffic joining and leaving the motorway.", ("Roundabouts", "Motorway traffic")),
                ("M60", "M60 junction 25 area", "A large multi-lane junction near the centre. You won't drive on the M60 on a test, but you'll meet its traffic.", ("Multi-lane",)),
                ("A560", "Stockport Road West", "Main road towards Romiley used on several reported routes. Changing speed limits and junctions with side roads.", ("Speed", "Junctions")),
                ("", "George's Lane", "Reported with a left turn at traffic lights heading towards Romiley.", ("Traffic lights",)),
                ("", "Romiley: Stockport Road / Compstall Road / School Brow", "Village-centre junctions with shops, pedestrians and a hill — a good test of observation and control.", ("Hill", "Pedestrians")),
                ("", "Town Lane, Oldham Street and Manchester Road North", "Side roads on a reported loop — residential junctions and parked cars.", ("Junctions", "Parked cars")),
                ("", "Grosvenor Street and Marple Hall Drive", "Named on reported routes for the parallel park.", ("Parallel park",)),
                ("", "Vernon Drive", "Named on a reported route for the emergency stop.", ("Emergency stop",))],
         spokes=[("Lingard Ln", "test centre"), ("Ashton Rd (A6017)", "M60 J25"), ("Stockport Rd W (A560)", "Romiley"), ("George's Ln", "Romiley"), ("Stockport Rd", "Woodley")],
         marks=[("Bredbury Park Industrial Estate", "Right next to the centre — lots of lorries."), ("M60 junction 25", "The nearest motorway junction."), ("Bredbury station", "On the Hope Valley line."), ("Woodley", "The A560 passes Woodley station."), ("Romiley village", "Shops, a hill and busy junctions on reported routes.")],
         mistakes=[("Pulling out in front of lorries on Lingard Lane", "Misjudging the speed and length of an HGV and emerging too close.", "Give large vehicles more time and space than cars — wait for a bigger gap."),
                   ("Roundabout lane choice on Ashton Road", "Taking the wrong lane near the M60 junction and drifting across lanes.", "Read the lane markings on approach; keep your lane all the way round."),
                   ("Hill starts in Romiley", "Rolling back or stalling on School Brow and similar hills.", "Find the biting point, more gas, then release the parking brake — practise until it's automatic."),
                   ("Observation at village junctions", "Missing pedestrians crossing the road you're turning into.", "Since 2022 the Highway Code says give way to people crossing or waiting to cross a road you're turning into."),
                   ("Parallel parking too far from the kerb", "Finishing wide or touching the kerb on narrower streets.", "Go slowly, use clutch control and reference points in your mirrors.")]),
    dict(slug="cheetham-hill", name="Cheetham Hill", borough="Manchester", pc="M8 0AL",
         address="Alderglen Road, Cheetham Hill, Manchester M8 0AL",
         rate=43.7, rate_note="2024-25", rate_src=("passrates.uk — Cheetham Hill driving test centre", "https://passrates.uk/centres/cheetham-hill-manchester"),
         serves="Cheetham Hill, Crumpsall, Harpurhey, Blackley, Moston, Collyhurst, Broughton, Higher Broughton, Prestwich, Salford and north Manchester",
         intro="Cheetham Hill test centre is on Alderglen Road, a residential street in north Manchester close to Waterloo Road. It's one of the busiest and most urban centres in Greater Manchester, and its 2024-25 pass rate was below the national average. That's not because examiners are harsher — it's because the roads give you more to deal with in every minute.",
         area="Routes combine the big radial roads into Manchester — Bury New Road (A56) and Cheetham Hill Road / Bury Old Road (A665) — with dense, narrow residential streets full of parked cars. Shopping strips, bus stops, traffic lights close together and pedestrians crossing between cars all add up.",
         roads=[("", "Alderglen Road", "The start and finish of every test. Residential, so moving off and pulling up safely start straight away.", ("Moving off",)),
                ("", "Waterloo Road", "On most reported routes and near the centre. Narrow residential area; parallel parking is reported nearby.", ("Parked cars", "Parallel park")),
                ("A56", "Bury New Road", "One of Manchester's main radial roads: very busy, with right turns at traffic lights and bus stops.", ("Right turns at lights", "Buses")),
                ("A665", "Cheetham Hill Road", "A busy shopping street with pedestrians, loading vans and buses. Becomes Bury Old Road in Crumpsall.", ("Shops", "Pedestrians", "Buses")),
                ("A665", "Bury Old Road", "Reported on routes heading north through Crumpsall towards Prestwich and Heaton Park.", ("Speed changes",)),
                ("", "Singleton Road, Heywood Street and Elizabeth Street", "Residential streets reported on route sheets — junctions with restricted views.", ("Junction observations",)),
                ("", "Cheetwood Road, Broughton Lane and Great Cheetham Street", "Side roads linking Cheetham Hill with Broughton and Salford — tight junctions and parked cars.", ("Clearance",)),
                ("", "Roads signed for Manchester Fort", "Manchester Fort Shopping Park is reported as a sat-nav or sign-following destination for independent driving.", ("Independent driving",))],
         spokes=[("Bury New Rd (A56)", "city / Prestwich"), ("Cheetham Hill Rd (A665)", "city"), ("Bury Old Rd (A665)", "Crumpsall"), ("Waterloo Rd", "Cheetham Hill"), ("Broughton Ln", "Salford")],
         marks=[("Manchester Fort Shopping Park", "A reported independent-driving destination."), ("Cheetham Hill shops", "Along Cheetham Hill Road — expect pedestrians and loading."), ("Heaton Park", "To the north via Bury Old Road."), ("Crumpsall", "Where Cheetham Hill Road becomes Bury Old Road.")],
         mistakes=[("Junction observations on parked-up streets", "Emerging from narrow streets where parked cars block the view.", "Creep and peep: edge forward slowly until you can genuinely see, then decide."),
                   ("Right turns at lights on Bury New Road", "Turning across oncoming traffic without a safe gap, or not moving when it's safe.", "Position correctly, judge the gap early, and remember pedestrians in the road you're turning into."),
                   ("Pedestrians on Cheetham Hill Road", "People cross between parked cars and buses on the shopping strip.", "Lower speed, wider berth and constant scanning of the pavements."),
                   ("Meeting traffic around Waterloo Road", "Getting stuck nose-to-nose because you committed too late or too early.", "Look far ahead, spot gaps, and decide early who has room to pass."),
                   ("Following signs during independent driving", "Late lane changes when following signs on multi-lane roads.", "Read the sign, check mirrors, then move — and if you go the wrong way, it's not a fault as long as you do it safely.")]),
    dict(slug="chadderton", name="Chadderton", borough="Oldham", pc="OL9 9XA",
         address="9 Broadgate, Broadway Business Park, Chadderton, Oldham OL9 9XA",
         rate=44.9, rate_note="2024-25, about 12,500 tests", rate_src=("passrates.uk — Chadderton driving test centre", "https://passrates.uk/centres/chadderton"),
         serves="Chadderton, Oldham, Royton, Shaw, Failsworth, Hollinwood, Middleton, Moston and parts of Rochdale and Tameside",
         intro="Chadderton test centre is at Broadway Business Park, just off Broadway (A663) and right next to the M60. It's the main centre for Oldham and a busy one — about 12,500 car tests in 2024-25. Routes start on business-park roads with large roundabouts and quickly reach Broadway, a fast dual carriageway.",
         area="Expect large business-park roundabouts, the A663 Broadway dual carriageway with several lane changes, the Featherstall Road roundabout, residential loops off Middleton Road, and town-centre traffic towards Oldham and Middleton.",
         roads=[("", "Broadgate", "The centre's own road — on nearly every reported route. Busy business-park traffic and large vehicles.", ("Moving off", "Large vehicles")),
                ("A663", "Broadway", "Dual carriageway with several lane changes. Choose your lane early, keep up with traffic and check mirrors before every move.", ("Dual carriageway", "Lane changes")),
                ("", "Broadway Business Park roundabouts", "Large roundabouts on the business park, often in the first few minutes of a test.", ("Roundabouts",)),
                ("", "Featherstall Road roundabout", "Busy and needs precise timing and lane discipline. Hesitating here is a common reason for faults.", ("Roundabout", "Timing")),
                ("", "Middleton Road", "Residential loops come off it. Parked traffic can hide side turnings, so position carefully.", ("Positioning", "Junctions")),
                ("", "Oldham Road", "Tight turns and town traffic on reported routes.", ("Junctions",)),
                ("", "Oldham and Middleton town-centre roads", "One-way systems, buses and pedestrian crossings.", ("One-way systems", "Buses"))],
         spokes=[("Broadway (A663)", "M60 / Royton"), ("Broadgate", "business park"), ("Featherstall Rd", "Oldham"), ("Middleton Rd", "Middleton"), ("Oldham Rd", "Failsworth")],
         marks=[("M60 motorway", "Right next to the business park."), ("Costco", "On Broadway Business Park."), ("Elk Mill Retail Park, Royton", "Asda and other shops by A627(M) junction 1."), ("Broadway Green business park", "Off Foxdenton Lane.")],
         mistakes=[("Late lane changes on Broadway", "Moving across lanes without enough mirror and blind-spot checks.", "Plan from the signs, check mirrors and blind spot, signal, then move — once, smoothly."),
                   ("Hesitation at the Featherstall Road roundabout", "Waiting for a perfect gap that never comes, then rushing a poor one.", "Look right early on approach and judge speed as well as distance."),
                   ("Speed on dual carriageways", "Driving well below the limit on Broadway when it's clear — a lack of progress.", "Use the speed the road and traffic allow, up to the limit."),
                   ("Positioning on Middleton Road", "Drifting too close to parked cars or hiding behind them at junctions.", "Hold a door's width from parked cars when you can, and be ready to stop."),
                   ("Roundabout signalling on the business park", "Forgetting to signal left before your exit.", "Signal left after passing the exit before yours.")]),
    dict(slug="rochdale", name="Rochdale", borough="Rochdale", pc="OL16 5EB",
         address="Globe House Business Centre, Moss Bridge Road, Rochdale OL16 5EB",
         rate=41.2, rate_note="2024-25, about 9,800 tests", rate_src=("passrates.uk — Rochdale driving test centre", "https://passrates.uk/centres/rochdale-manchester"),
         serves="Rochdale, Milnrow, Littleborough, Wardle, Heywood, Castleton, Norden, Bamford and parts of Middleton",
         intro="Rochdale test centre is in Globe House Business Centre on Moss Bridge Road, a few minutes from Rochdale town centre. It has long had one of the lowest pass rates in Greater Manchester — around 41% in 2024-25. Some directories still show an older town-centre address, so always check your booking confirmation.",
         area="Routes are compact but demanding: the exit from the centre itself, the busy Queensway roundabout, traffic lights on Kingsway and Edinburgh Way, the town-centre one-way system, steep hills and tight terraced streets.",
         roads=[("", "Moss Bridge Road", "The centre's road. Some routes start at a roundabout here, and pulling out of the centre is often described as tricky.", ("Moving off", "Roundabout")),
                ("", "Wallhead Road", "The centre is just off it; it appears on reported routes.", ("Junctions",)),
                ("", "Kingsway", "Often reached by turning right off Moss Bridge Road at the lights. A busy main road on many reported routes.", ("Right turn at lights",)),
                ("", "Queensway roundabout", "Large and often busy, with traffic entering from several roads. Lane choice and timing are critical.", ("Multi-lane roundabout",)),
                ("", "Edinburgh Way", "Traffic lights followed by a roundabout — be in the right lane before the lights.", ("Lights then roundabout",)),
                ("", "Manchester Road and Oldham Road", "Main roads into and out of town, with turns at traffic lights.", ("Traffic lights",)),
                ("", "Town-centre one-way system", "Lanes split quickly and buses cut across; read the overhead and road signs early.", ("One-way", "Buses")),
                ("", "Hilly terraced streets", "Steep hills with parked cars both sides — hill starts and meeting traffic.", ("Hill starts", "Meeting traffic"))],
         spokes=[("Moss Bridge Rd", "test centre"), ("Kingsway", "Milnrow"), ("Queensway", "ring road"), ("Edinburgh Way", "town centre"), ("Oldham Rd", "Oldham")],
         marks=[("Globe House / Globe Park", "The test centre building."), ("Rochdale town centre", "About 5–10 minutes away."), ("Queensway", "The large roundabout on many routes.")],
         mistakes=[("Leaving the test centre", "Nerves plus a busy exit lead to rushed observations in the first minute.", "Take your time pulling out — an extra look costs nothing."),
                   ("Queensway roundabout lane choice", "Entering in the wrong lane or changing lanes on the roundabout.", "Learn the lane markings for each exit on lessons; follow them all the way round."),
                   ("Lights then roundabout on Edinburgh Way", "Concentrating on the lights and missing the lane you need for the roundabout.", "Read the lane arrows before the lights."),
                   ("Hill starts", "Rolling back on steep terraced streets.", "Biting point, gas, release the parking brake — practise on the steepest roads you can find."),
                   ("Meeting traffic on narrow streets", "Getting stuck because you didn't spot the oncoming car early.", "Look as far ahead as possible and decide early where you'll wait.")]),
    dict(slug="bolton", name="Bolton", borough="Bolton", pc="BL3 2AW",
         address="143 Weston Street, Great Lever, Bolton BL3 2AW",
         rate=58.6, rate_note="April 2024–March 2025, 3,250 passes from 5,548 tests", rate_src=SRC["mm"],
         serves="Bolton, Great Lever, Farnworth, Kearsley, Little Lever, Harwood, Astley Bridge, Halliwell, Heaton, Deane, Westhoughton and Horwich",
         intro="Bolton test centre is on Weston Street in Great Lever, about five minutes from Bolton town centre, next to a bus depot. In the DVSA figures for April 2024 to March 2025 it had the highest pass rate in Greater Manchester — 58.6%. That doesn't make it easy: many routes use St Peter's Way, a fast dual carriageway with short slip roads.",
         area="Expect industrial-street traffic with buses and lorries on Weston Street, traffic-light junctions on Manchester Road, the A666 St Peter's Way dual carriageway, town-centre roads and residential areas near schools and Bolton College.",
         roads=[("", "Weston Street", "The centre's road: an industrial street with frequent HGVs and buses — observe carefully when you pull out.", ("HGVs", "Buses")),
                ("", "Nelson Street and Orlando Street", "Reported as the opening steps of a route out of the centre.", ("Junctions",)),
                ("", "Manchester Road", "Reached at traffic lights; reported routes turn right at the second set.", ("Right turn at lights",)),
                ("A666", "St Peter's Way", "Fast dual carriageway with short slip roads. You need to match the speed of traffic quickly when joining — a common place to lose marks.", ("Slip roads", "Dual carriageway")),
                ("A676", "A676 corridor", "A main road named in the test area.", ("Speed changes",)),
                ("", "Derby Street, St Helens Road and Wigan Road", "On a reported route west of the town centre — traffic lights, buses and side roads.", ("Traffic lights", "Buses")),
                ("", "Bolton town-centre roads", "Busy junctions, especially near schools and Bolton College at peak times.", ("Peak traffic", "Pedestrians"))],
         spokes=[("Weston St", "Great Lever"), ("Manchester Rd", "town centre"), ("St Peter's Way (A666)", "M61 / Kearsley"), ("Derby St", "Daubhill"), ("St Helens Rd", "Westhoughton")],
         marks=[("Bus depot", "Next to the test centre — expect buses pulling out."), ("Makkah Mosque & Community Centre", "Next to the centre on Weston Street."), ("Bolton town centre", "About five minutes away."), ("Bolton College", "Busy roads at the start and end of the college day."), ("Royal Bolton Hospital", "South-west of Great Lever in Farnworth.")],
         mistakes=[("Joining St Peter's Way too slowly", "Short slip roads leave little time; arriving at the end at 30mph is dangerous.", "Use the whole slip road to build speed, check mirrors and blind spot, and merge into a gap."),
                   ("Pulling out on Weston Street", "Underestimating a lorry or bus.", "Wait for a clear, generous gap, and watch for buses leaving the depot."),
                   ("Observation at blind junctions", "Emerging where buildings or parked vans block the view.", "Slow right down, creep and peep, and look both ways more than once."),
                   ("Lane discipline on the dual carriageway", "Staying in lane two after overtaking, or changing lanes without a blind-spot check.", "Return to the left lane when it's safe, and check your blind spot every time."),
                   ("School-time traffic", "Not anticipating children and parked cars near schools and the college.", "Lower your speed and be ready to stop near school entrances.")]),
    dict(slug="bury", name="Bury", borough="Bury", pc="BL9 6HH",
         address="Smith Street, Bury BL9 6HH (corner of Brook Street, near Bury College)",
         rate=37.7, rate_note="April 2024–March 2025, 1,643 passes from 4,355 tests", rate_src=SRC["mm"],
         serves="Bury, Radcliffe, Whitefield, Prestwich, Tottington, Ramsbottom, Walmersley, Unsworth and parts of Heywood and Bolton",
         intro="Bury test centre is on Smith Street, near Bury College, just off the A56 and Peel Way. In the DVSA figures for April 2024 to March 2025 it had one of the lowest pass rates in Greater Manchester — 37.7%. Our pass-rate study shows that gap with Bolton is real and not chance. The roads explain a lot: a ring road with multi-lane roundabouts sits minutes from the centre.",
         area="Expect Peel Way (the A56 inner ring road) and its roundabouts, the Peel Way / Angouleme Way junctions, mini-roundabouts on Tottington Road, traffic lights on Walmersley Road, and narrow residential streets.",
         roads=[("", "Smith Street and Brook Street", "The start of reported routes — residential with parked cars.", ("Moving off", "Parked cars")),
                ("A56", "Peel Way (inner ring road)", "Busy roundabouts needing strong lane discipline and clear signals. Reported at traffic lights too.", ("Multi-lane roundabouts", "Signals")),
                ("", "Peel Way / Angouleme Way", "A roundabout complex with several lanes and exits; heavy at peak times.", ("Lane choice",)),
                ("", "Peel Way, A56, The Rock and B6222 junction", "Named by local instructors as one of the trickiest areas in Bury.", ("Complex junction",)),
                ("", "Tottington Road / Bury Road", "Mini-roundabouts close together — including going ahead at a second mini-roundabout.", ("Mini-roundabouts",)),
                ("", "Walmersley Road", "Reported with a right turn at traffic lights.", ("Right turn at lights",)),
                ("", "Market Street, Kirkless Street, Royds Street and Holcombe Road", "Reported on routes around the town centre — side roads and a right turn onto Holcombe Road.", ("Junctions",)),
                ("", "Bolton Street / Bolton Road", "A main road used to join Peel Way.", ("Joining traffic",))],
         spokes=[("Peel Way (A56)", "ring road"), ("Walmersley Rd", "Walmersley"), ("Tottington Rd", "Tottington"), ("Bolton St", "Bolton"), ("The Rock", "town centre")],
         marks=[("The Rock shopping centre", "A common route reference point in the town centre."), ("Bury Market", "Busy streets on market days."), ("Bury College", "Close to the test centre."), ("Bury town centre", "Minutes away.")],
         mistakes=[("Wrong lane on Peel Way roundabouts", "Choosing lanes late or changing lanes on the roundabout.", "Learn each Peel Way roundabout on lessons; follow the arrows and keep your lane."),
                   ("Signals on the ring road", "Not signalling left to exit, or leaving a signal on.", "Signal after passing the exit before yours, then cancel."),
                   ("Mini-roundabouts on Tottington Road", "Treating two close mini-roundabouts as one, or not giving way to the right.", "Deal with each one separately: look right, give way, signal if needed."),
                   ("Right turn at Walmersley Road lights", "Hesitating or turning without a safe gap.", "Position, look, judge the gap, and watch for pedestrians."),
                   ("Complex junctions near The Rock", "Information overload: signs, lanes and pedestrians all at once.", "Slow down earlier — giving yourself time is the cure for most junction faults.")]),
    dict(slug="atherton", name="Atherton", borough="Wigan", pc="M46 0SU",
         address="Gibfield Park Avenue, Atherton, Manchester M46 0SU",
         rate=44.4, rate_note="2024-25, about 7,700 tests", rate_src=SRC["pr_gm"],
         serves="Atherton, Leigh, Tyldesley, Astley, Hindley, Westhoughton, Daisy Hill, Hag Fold, Boothstown and parts of Walkden and Little Hulton",
         intro="Atherton test centre is on Gibfield Park Avenue by the Gibfield business area. It serves Wigan borough's eastern towns — Atherton, Leigh, Tyldesley — and parts of Bolton and Salford. Routes leave over a pair of roundabouts and onto Atherleigh Way, then mix faster A-roads with some of the narrowest parked-up streets in the area.",
         area="Expect roundabouts straight out of the centre, Atherleigh Way with lights and roundabouts, Leigh Road's filter lanes into Atherton, Bolton Road, faster A-roads like the A58 and A577, a level crossing, and narrow streets in Hag Fold and Hindsford.",
         roads=[("", "Gibfield Park Avenue / Gibfield Park Way", "Two roundabouts straight out of the centre on reported routes — your first test of observation and lane choice.", ("Roundabouts",)),
                ("A579", "Atherleigh Way", "A busy through-route with long straights, traffic lights and roundabouts. Needs good anticipation.", ("Roundabouts", "Traffic lights")),
                ("", "Leigh Road", "The approach into Atherton has several filter lanes that catch learners out on lane choice.", ("Filter lanes",)),
                ("", "Bolton Road", "Common on reported routes; town traffic and side roads.", ("Junctions",)),
                ("A58 / A577", "Faster A-roads", "Higher-speed roads with multi-lane roundabouts.", ("Speed", "Multi-lane roundabouts")),
                ("", "Hag Fold and Hindsford streets", "Narrow, with cars parked on both sides — clearance and meeting oncoming traffic.", ("Meeting traffic", "Clearance")),
                ("", "Level crossing near Hag Fold", "Reported on routes. Never stop on the crossing; wait behind the line when lights flash.", ("Level crossing",))],
         spokes=[("Gibfield Park Ave", "test centre"), ("Atherleigh Way (A579)", "Leigh"), ("Leigh Rd", "Atherton"), ("Bolton Rd", "Hag Fold"), ("A58", "Westhoughton")],
         marks=[("Gibfield Park business area", "Where the centre is."), ("Atherleigh Business Park", "Along Atherleigh Way."), ("Hag Fold and Atherton stations", "Near the level crossing on some routes."), ("Leigh", "About two miles away; reached on some routes."), ("Westhoughton", "Reached on some longer routes.")],
         mistakes=[("Filter lanes on Leigh Road", "Ending up in a filter lane for the wrong direction.", "Read the road markings early and move across with a full MSM routine."),
                   ("Clearance on Hag Fold and Hindsford streets", "Squeezing past parked cars too close or too fast.", "Slow down; if there's less than a door's width, slow down more."),
                   ("Level crossings", "Stopping too late, or not knowing what to do when lights flash.", "Approach at a speed where you can stop; when amber then red lights show, stop behind the white line."),
                   ("Roundabouts straight out of the centre", "Nerves in the first minute lead to missed observations.", "Treat the first roundabout as a warm-up: look right early and take your time."),
                   ("Progress on Atherleigh Way", "Driving too slowly on a clear road.", "Drive at the speed the road and conditions allow.")]),
]


def _gauge(rate):
    return f'<div class="rx-gauge-num" data-count="{rate}" data-suffix="%">{rate}%</div>'


def centre_page(c, nearby):
    path = f"test-routes/{c['slug']}-driving-test-routes.html"
    name = c["name"]
    roads = "".join(road(*r) for r in c["roads"])
    near = "".join(f'<a class="chip" href="{x["slug"]}-driving-test-routes.html">{x["name"]} ({x["rate"]}%)</a>' for x in nearby)
    diff = c["rate"] - 48.5
    cmp = f"{abs(diff):.1f} points {'above' if diff > 0 else 'below'}"
    body = f"""
<p class="lead">{c['intro']}</p>
<div class="callout callout--info"><b>Where it is:</b> {c['address']}. Check the address on your booking confirmation and on GOV.UK before you travel — centres occasionally move.</div>
<h2>Pass rate at {name}</h2>
<div class="rt-pass" data-reveal="up">{_gauge(c['rate'])}<div><p class="mb-0"><b>{name} car test pass rate</b> — {c['rate_note']}.</p><p class="note mb-0">That's {cmp} the Great Britain average of about 48.5% for the same period. Source: <a href="{c['rate_src'][1]}" target="_blank" rel="noopener">{c['rate_src'][0]}</a>. Different websites publish slightly different figures for different periods; the official numbers are in the DVSA's DVSA1203 statistics.</p></div></div>
<p>A pass rate tells you about the roads and the candidates, not about your chances. What moves your odds most is being genuinely test-ready. Our <a href="{ROOT}research/driving-test-pass-rates-explained-manchester.html">pass-rate study</a> turns pass rates into expected attempts and costs.</p>
<h2>The roads around {name} test centre</h2>
<p>{c['area']}</p>
{radial_map(name, c['spokes'])}
<p class="note">The DVSA no longer publishes official test routes, and examiners vary them. The roads below are the ones reported most often on recent routes from this centre, cross-checked between several public route sheets and local instructors. Your test could use any of them, or none.</p>
{roads}
<h2>Local landmarks you'll drive past</h2>
<p>Useful for finding your way during independent driving, and for knowing where you are when your instructor says "we'll practise round by…".</p>
{landmarks(c['marks'])}
<h2>Mistakes learners make at {name}</h2>
<p>These are the faults that the roads around {name} make most likely. They line up with the DVSA's national list of the most common reasons for failing — <a href="{ROOT}test-faults.html">see each one explained</a>.</p>
{mistakes(c['mistakes'])}
<h2>How SQ prepares you for a test at {name}</h2>
<ol class="rx-steps"><li data-n="1"><h4>Learn the road types first</h4><p>Dual carriageways, multi-lane roundabouts, narrow parked-up streets — on quieter roads before we bring you near the centre.</p></li>
<li data-n="2"><h4>Drive the area around {name}</h4><p>In the last few weeks before your test we practise on the roads above, at the same time of day as your test.</p></li>
<li data-n="3"><h4>A full mock test</h4><p>Marked on the same categories as the DVSA sheet and recorded in your DriveSQ Student Portal.</p></li>
<li data-n="4"><h4>Warm-up lesson on the day</h4><p>A one-hour lesson ending at the test centre so you arrive calm and warmed up.</p></li></ol>
<h2>Who tests at {name}?</h2>
<p>Learners from {c['serves']} commonly book {name}. There's no catchment area for new bookings, so you can book any centre — but since June 2026 a booked test can only move to one of the three centres nearest it. Nearby centres: <span class="hero__badges">{near}</span></p>"""
    faqs = [(f"Where is {name} driving test centre?", f"{c['address']}."),
            (f"What is the pass rate at {name} test centre?", f"{c['rate']}% ({c['rate_note']}), against a Great Britain average of about 48.5%."),
            (f"What roads are on the {name} driving test routes?", "Commonly reported roads include " + ", ".join(r[1] for r in c["roads"][:5]) + ". The DVSA doesn't publish official routes and examiners vary them."),
            (f"Can I practise the {name} test routes with SQ?", f"Yes. We teach on the roads around {name} test centre and finish with a mock test and a warm-up lesson that ends at the centre."),
            ("Are driving test routes published?", "No. The DVSA stopped publishing test routes, so any route you see online has been reported by learners or instructors.")]
    sch = [{"@context": "https://schema.org", "@type": "Place", "name": f"{name} driving test centre (DVSA)", "address": {"@type": "PostalAddress", "streetAddress": c["address"].rsplit(",", 1)[0], "postalCode": c["pc"], "addressRegion": "Greater Manchester", "addressCountry": "GB"}}]
    sources = [c["rate_src"], SRC["dvsa"], SRC["find"], SRC["top10"], SRC["book"]]
    related = [(f"knowledge/test-centre-{c['slug']}.html", "Test centre", f"{name} test centre: quick guide", "Booking, who tests there and skills to practise."),
               ("driving/driving-test-day-planner.html", "Planner", "Test day planner", "Sunrise, glare, rush hour and a test-day timetable."),
               ("test-faults.html", "Test faults", "Why people fail — fault by fault", "The DVSA's most common faults and how to fix them.")]
    return shell(path, f"{name} Driving Test Routes, Roads & Tips ({c['rate']}% Pass) | SQ", "Test-route guide", [("Test routes", "test-routes.html"), (name, path)],
                 f"{name} driving test routes: roads, junctions and mistakes", f"In-depth guide to {name} driving test centre ({c['pc']}): the roads on reported test routes, tricky junctions, local landmarks, the pass rate and the mistakes learners make.",
                 [(f"{c['rate']}%", "pass rate"), (str(len(c["roads"])), "roads profiled"), (str(len(c["mistakes"])), "common mistakes"), (c["pc"], "postcode")],
                 [f"{name} test centre: {c['address']}.", f"Pass rate {c['rate']}% ({c['rate_note']}).", f"Reported routes use roads like {c['roads'][0][1]} and {c['roads'][1][1]}.", "DVSA doesn't publish routes — prepare for the road types, not one route."],
                 body, faqs, sources, related, side_title=f"Test at {name}?", booking_heading=f"Learning for a test at {name}? Book in 60 seconds",
                 extra_schema=sch, after_body=feedback_form(name))


def hyde_page():
    path = "test-routes/hyde-driving-test-centre-closed.html"
    body = f"""
<p class="lead">If you're searching for Hyde driving test centre, you'll still find it listed on some websites. It isn't open for car tests. The DVSA closed the Hyde car test centre on Perrin Street after Sunday 10 April 2022, despite a petition with more than 5,500 signatures, a Tameside Council motion and objections from local MPs.</p>
<div class="callout callout--warn"><b>Hyde (23 Perrin Street, SK14 1JE) is closed for car tests.</b> Some directories and older driving-school pages still list it. Always use GOV.UK's "find a driving test centre" tool.</div>
<h2>Where Tameside learners test now</h2>
<p>When the centre closed, the DVSA said examiners would move to nearby centres and no tests would be lost. Learners in Hyde, Denton, Dukinfield, Stalybridge, Ashton-under-Lyne and Mossley now usually book one of these:</p>
<div class="grid grid--2" data-stagger=".06">
<a class="rx-study" href="bredbury-driving-test-routes.html" data-reveal="up"><span class="k-cat">Stockport · SK6 2QT</span><h3>Bredbury</h3><p>The nearest for Hyde, Denton and Woodley. 54.2% pass rate (2024-25).</p></a>
<a class="rx-study" href="chadderton-driving-test-routes.html" data-reveal="up"><span class="k-cat">Oldham · OL9 9XA</span><h3>Chadderton</h3><p>Often closer for Ashton, Mossley and Droylsden. 44.9% pass rate (2024-25).</p></a>
<a class="rx-study" href="cheetham-hill-driving-test-routes.html" data-reveal="up"><span class="k-cat">Manchester · M8 0AL</span><h3>Cheetham Hill</h3><p>An option for Droylsden and Audenshaw learners. 43.7% pass rate (2024-25).</p></a>
<div class="rx-study" data-reveal="up"><span class="k-cat">Derbyshire</span><h3>Buxton</h3><p>The DVSA also pointed Glossop-side learners towards Buxton when Hyde closed.</p></div></div>
<h2>Choosing between Bredbury and Chadderton</h2>
<p>Don't just pick the higher pass rate. Pick the centre whose roads you can practise on most. For Hyde and Denton learners, Bredbury's roads (Ashton Road, Stockport Road West, Romiley) are close and similar to home. For Ashton and Mossley, Chadderton's Broadway dual carriageway and large roundabouts may be easier to reach for practice. Since June 2026 a booked test can only move to one of the three centres nearest it, so choose carefully.</p>
<h2>Learning to drive in Tameside with SQ</h2>
<p>SQ Driving School covers all of Tameside with door-to-door pick-up. We'll teach you on Tameside's hills and town centres, then on the roads around whichever test centre you choose. See <a href="{ROOT}areas/tameside.html">driving lessons in Tameside</a>.</p>"""
    faqs = [("Is Hyde driving test centre still open?", "No. The DVSA closed the Hyde car test centre after 10 April 2022."),
            ("Where do Hyde learners take their driving test now?", "Usually Bredbury (Stockport), the nearest centre, or Chadderton. Some Glossop-side learners use Buxton."),
            ("Which test centre is closest to Hyde?", "Bredbury, on Lingard Lane SK6 2QT, a short drive from Hyde."),
            ("Why did Hyde test centre close?", "The DVSA decided to close it and move examiners to nearby centres. Local campaigners, the council and MPs opposed the decision.")]
    return shell(path, "Hyde Driving Test Centre: Closed — Where to Test Instead | SQ", "Test-route guide", [("Test routes", "test-routes.html"), ("Hyde (closed)", path)],
                 "Hyde driving test centre is closed — where to test instead", "Hyde's car test centre closed in April 2022. Where Tameside learners test now — Bredbury, Chadderton and more — with pass rates and how to choose.",
                 [("2022", "Hyde closed"), ("5,500+", "petition signatures"), ("54.2%", "Bredbury pass rate"), ("SK6 2QT", "Bredbury postcode")],
                 ["Hyde car test centre (Perrin Street) closed after 10 April 2022.", "Most Tameside learners now test at Bredbury or Chadderton.", "Some websites still list Hyde — check GOV.UK.", "Pick the centre whose roads you can practise on, not just the pass rate."],
                 body, faqs, [("Quest Media Network — Hyde driving test centre set to close", "https://www.questmedianetwork.co.uk/news/tameside-reporter/hyde-driving-test-centre-set-to-close/"),
                              ("Tameside Council — motion on Hyde test centre closure", "https://tameside.moderngov.co.uk/documents/s121795/ITEM%2016%20-%20Motion%20-%20Hyde%20test%20centre%20closure.pdf"), SRC["find"], SRC["dvsa"]],
                 [("test-routes/bredbury-driving-test-routes.html", "Test routes", "Bredbury test routes", "Roads, junctions and mistakes."), ("test-routes/chadderton-driving-test-routes.html", "Test routes", "Chadderton test routes", "Roads, junctions and mistakes."), ("areas/tameside.html", "Area", "Driving lessons in Tameside", "Door-to-door lessons across Tameside.")],
                 side_title="Learning in Tameside?")


def hub():
    rows = "".join(f'<tr><td><a href="test-routes/{c["slug"]}-driving-test-routes.html">{c["name"]}</a></td><td>{c["borough"]}</td><td class="mono">{c["pc"]}</td><td class="mono"><b>{c["rate"]}%</b></td><td>{c["rate_note"].split(",")[0]}</td></tr>' for c in sorted(C, key=lambda x: -x["rate"]))
    bars = RS._bars([(c["name"], c["borough"], c["rate"], "rx-bar__fill--green" if c["rate"] >= 48.5 else "") for c in sorted(C, key=lambda x: -x["rate"])], "%", 70)
    intro = f"""<p class="lead" data-reveal="up">Every Greater Manchester driving test centre, profiled road by road: the junctions on reported routes, local landmarks, pass rates and the specific mistakes learners make there. Written by SQ Driving School, part of DriveSQ, which teaches around all of them.</p>
<div class="rx-table-wrap" data-reveal="up"><table class="rx-table"><thead><tr><th>Centre</th><th>Borough</th><th>Postcode</th><th>Pass rate</th><th>Period</th></tr></thead><tbody>{rows}<tr><td><a href="test-routes/hyde-driving-test-centre-closed.html">Hyde</a></td><td>Tameside</td><td class="mono">SK14 1JE</td><td>Closed 2022</td><td>—</td></tr></tbody></table></div>
<p class="note">Bolton and Bury: DVSA figures for April 2024–March 2025 as reported by Mancunian Matters. Others: passrates.uk's 2024-25 analysis of DVSA data. Great Britain average ≈ 48.5%.</p>
{bars}
<h2 class="mt-3">Test-route guides</h2>"""
    cards = [(f"test-routes/{c['slug']}-driving-test-routes.html", f"{c['borough']} · {c['rate']}%", f"{c['name']} test routes", f"{len(c['roads'])} roads, {len(c['mistakes'])} common mistakes, landmarks and tips.", "road") for c in C]
    cards.append(("test-routes/hyde-driving-test-centre-closed.html", "Tameside · closed", "Hyde test centre (closed)", "Where Tameside learners test now.", "flag"))
    return hub_page("test-routes.html", "Greater Manchester Driving Test Routes: Every Centre | SQ Driving School", "Test routes",
                    "Greater Manchester driving test routes.", "Road-by-road guides to every Greater Manchester driving test centre — reported routes, tricky junctions, landmarks, pass rates and common mistakes.",
                    cards, intro, [(str(len(C)), "test centres profiled"), (str(sum(len(c["roads"]) for c in C)), "roads described"), (str(sum(len(c["mistakes"]) for c in C)), "mistakes to avoid"), ("58.6%", "highest pass rate")])


def all_pages():
    out = {"test-routes.html": hub(), "test-routes/hyde-driving-test-centre-closed.html": hyde_page()}
    order = [c["slug"] for c in C]
    for c in C:
        i = order.index(c["slug"])
        nearby = [x for x in C if x["slug"] != c["slug"] and (x["borough"] == c["borough"] or abs(order.index(x["slug"]) - i) <= 2)][:4]
        out[f"test-routes/{c['slug']}-driving-test-routes.html"] = centre_page(c, nearby)
    return out
