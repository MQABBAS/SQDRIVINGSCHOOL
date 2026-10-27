"""Solihull batch 4: every postcode sector in and around Solihull, plus the everyday places learners drive to —
petrol stations (incl. the three Shell sites), car parks, shops and retail parks — and the signs, markings,
crossings and roundabouts on local test routes, with the good and the hard parts of each.

Sector centroids come from the free UK postcode list (dwyl/uk-postcodes-latitude-longitude-complete-csv, built from
ONS/OS Code-Point Open data); distances to test centres are straight-line from those centroids. Fuel stations, car
parks and shops are only listed where a public source names them; prices and car-park rules change, so pages say so.
No invented reviews: the "good and hard" notes are road features and DVSA fault categories, not quotes."""
from math import radians, sin, cos, asin, sqrt
import pages_solihull as SOL
import pages_research as RS
from pages_sol_more import SRC, portal_strip, CEN

S, DSQ, CENTRES = SOL.S, SOL.DSQ, SOL.CENTRES

SRC.setdefault("pcdata", ("UK postcode centroids — Code-Point Open derived list (dwyl, GitHub)", "https://github.com/dwyl/uk-postcodes-latitude-longitude-complete-csv"))
SRC.setdefault("hc_signs", ("GOV.UK — The Highway Code: traffic signs", "https://www.gov.uk/guidance/the-highway-code/traffic-signs"))
SRC.setdefault("kyts", ("GOV.UK — Know your traffic signs", "https://www.gov.uk/government/publications/know-your-traffic-signs"))
SRC.setdefault("hc_marks", ("GOV.UK — The Highway Code: road markings", "https://www.gov.uk/guidance/the-highway-code/road-markings"))
SRC.setdefault("hc_road", ("GOV.UK — The Highway Code: using the road (rules 159 to 203)", "https://www.gov.uk/guidance/the-highway-code/using-the-road-159-to-203"))
SRC.setdefault("hc_mway", ("GOV.UK — The Highway Code: motorways (rules 253 to 274)", "https://www.gov.uk/guidance/the-highway-code/motorways-253-to-273"))
SRC.setdefault("e10", ("GOV.UK — E10 petrol explained", "https://www.gov.uk/guidance/e10-petrol-explained"))
SRC.setdefault("shell_loc", ("petrolfinder.uk — Shell stations in Solihull", "https://www.petrolfinder.uk/brands/shell/solihull"))
SRC.setdefault("fuel_list", ("petrolprices.co.uk — petrol and diesel stations in Solihull", "https://petrolprices.co.uk/towns/solihull.php"))
SRC.setdefault("fuel_sup", ("fuel-finder.uk — Solihull fuel stations", "https://www.fuel-finder.uk/fuel-prices/united-kingdom/england/west-midlands/solihull/"))
SRC.setdefault("bp_loc", ("bp — station locator, Solihull", "https://map.bp.com/en-GB/GB/petrol-station/solihull"))
SRC.setdefault("cp_town", ("Solihull Council — Solihull town centre car parks", "https://www.solihull.gov.uk/Parking/Solihull-town-centre-car-parks"))
SRC.setdefault("cp_all", ("Solihull Council — car parks across Solihull", "https://www.solihull.gov.uk/parking/car-parks-across-solihull"))
SRC.setdefault("cp_knowle", ("Solihull Council — Knowle car parks", "https://solihull.gov.uk/parking/Knowlecarparks"))
SRC.setdefault("cp_fees", ("Solihull Council — fees and charges 2026, on and off-street tariff notice", "https://www.solihull.gov.uk/sites/default/files/2026-03/Fees-and-Charges-2026-On-and-Off-Street-Tariff-Variation-Apr-2026-NOTICE.pdf"))
SRC.setdefault("holbeche", ("Solihull Council — Holbeche Place (Mell Square) phase 1", "https://www.solihull.gov.uk/news/2026/major-step-forward-holbeche-place-phase-1-starts-june"))
SRC.setdefault("touchwood", ("Wikipedia — Touchwood, Solihull", "https://en.wikipedia.org/wiki/Touchwood,_Solihull"))
SRC.setdefault("parkgate", ("TheBusinessDesk — £85m Parkgate scheme, Shirley", "https://www.thebusinessdesk.com/westmidlands/?p=195840"))
SRC.setdefault("sears", ("Parkopedia — Sears Retail Park, Shirley", "https://en.parkopedia.co.uk/parking/carpark/sears_retail_park/b90/solihull/"))
SRC.setdefault("ms_sears", ("Coventry Telegraph — M&S moves from Solihull town centre to Shirley", "https://www.coventrytelegraph.net/news/local-news/ms-reveals-move-out-solihull-20639984"))
SRC.setdefault("faults", ("Theory Test Pro — DVSA's top reasons learners fail (2022-23 data)", "https://www.theorytestpro.co.uk/posts/top-10-reasons-why-learners-failed-their-driving-test-in-2023/"))
SRC.setdefault("faults2", ("PassMeFast — driving test fail reasons explained", "https://www.passmefast.co.uk/resources/learning-to-drive/driving-test-fail-reasons"))
SRC.setdefault("during", ("GOV.UK — Driving test: what happens during the test", "https://www.gov.uk/driving-test/what-happens-during-test"))

# exact test-centre points from their postcodes (Warwick: approximate, the centre has no single published postcode)
TC = {"shirley": (52.40429, -1.82203), "garretts-green": (52.47267, -1.77128), "south-yardley": (52.45396, -1.81010),
      "kings-heath": (52.40657, -1.88712), "coventry": (52.46378, -1.47516), "warwick": (52.291, -1.597), "redditch": (52.30854, -1.94704)}


def miles(a, b):
    la1, lo1, la2, lo2 = map(radians, (a[0], a[1], b[0], b[1]))
    h = sin((la2 - la1) / 2) ** 2 + cos(la1) * cos(la2) * sin((lo2 - lo1) / 2) ** 2
    return 3958.8 * 2 * asin(sqrt(h))


# fuel stations named by public listings, with their postcode's coordinates
FUEL = [
    ("Shell", "Shell Shirley Triangle", "Stratford Road, Shirley B90 4AU", (52.40089, -1.82202), "Listed as open 24 hours.", "shell_loc"),
    ("Shell", "Shell Solihull", "Warwick Road, Solihull B91 1BB", (52.42480, -1.79608), "", "shell_loc"),
    ("Shell", "Shell Box Trees (with Little Waitrose)", "Stratford Road (A3400), Hockley Heath B94 6NS", (52.36213, -1.78002), "Listed 05:30–22:30.", "shell_loc"),
    ("Tesco", "Tesco Solihull Extra", "1505 Stratford Road, Shirley B90 4EN", (52.38436, -1.78927), "Listed as open 24 hours.", "fuel_sup"),
    ("Sainsbury's", "Sainsbury's Marshall Lake", "545 Stratford Road, Shirley B90 4AJ", (52.40199, -1.82070), "Listed 06:30–22:30.", "fuel_sup"),
    ("Asda", "Asda Shirley Superstore", "Parkgate, Stratford Road, Shirley B90 3GG", (52.41308, -1.82901), "Listed 07:00–23:00.", "fuel_sup"),
    ("BP", "BP Mereside", "197 Warwick Road, Olton B92 7AW", (52.43700, -1.80445), "", "bp_loc"),
    ("Texaco", "Texaco Olton", "10–24 Warwick Road, Olton B92 7HS", (52.44210, -1.81108), "", "fuel_list"),
    ("Esso", "Esso Hobs Moat Road", "Hobs Moat Road, Solihull B92 8JN", (52.44497, -1.78493), "", "fuel_list"),
    ("Esso", "Esso Coventry Road", "Coventry Road (A45), B92 0EH", (52.44525, -1.72126), "", "fuel_list"),
    ("Esso", "Esso Knowle", "Kenilworth Road, Knowle B93 0JD", (52.38700, -1.72965), "", "fuel_list"),
    ("Esso", "Esso Widney Road", "Widney Road, Bentley Heath B93 9DZ", (52.38154, -1.75123), "", "fuel_list"),
    ("Esso", "Esso Solihull Lodge area", "B90 1JS", (52.40578, -1.86188), "", "fuel_list"),
    ("Texaco", "Texaco Marston Green", "53 Station Road, Marston Green B37 7AU", (52.46774, -1.75150), "", "fuel_sup"),
    ("Independent", "Kay Group, Chelmsley Wood", "Chester Road, Chelmsley Wood B37 6RD", (52.49035, -1.73823), "", "fuel_sup"),
    ("Independent", "Tile Cross Service Station", "Cooks Lane, B37 6PB", (52.48281, -1.75963), "", "fuel_sup"),
]

# car parks and shopping places (council or public listings) — tied to sectors by hand, not by coordinates
PARK = {
    "town": [("Church Hill car park", "Council, 127 spaces, pay and display.", "cp_town"), ("Brueton car park", "Council, 69 spaces, open 24 hours.", "cp_town"),
             ("Poplar Road, Lode Lane and Dominion Court (Herbert Road)", "The council's suggested replacements while Mell Square is redeveloped.", "holbeche"),
             ("Touchwood", "Shopping centre parking, about 1,650 spaces.", "touchwood")],
    "shirley": [("Shirley council car parks", "Free for up to 3 hours Monday–Saturday under the April 2026 tariff notice; check signs.", "cp_fees"),
                ("Parkgate (Asda)", "500-space basement car park under the Parkgate scheme.", "parkgate"),
                ("Sears Retail Park", "M&S, Boots, TK Maxx and more; around 920 spaces with a 2-hour stay limit reported.", "sears")],
    "knowle": [("Knowle car parks (rear of Tesco, rear of the Greswolde Arms)", "Council pay and display, PayByPhone accepted.", "cp_knowle")],
    "chelmsley": [("Hedingham Grove car park", "Council, free, 55 spaces, open 24 hours.", "cp_all")],
}

# sector: (areas, kind, roads, area slugs, road-guide slugs, parking key, local note)
R = dict(a34="a34-stratford-road-shirley", m42="m42-junctions-3a-4-5-6-solihull", a45="a45-coventry-road-airport-nec", a41="a41-warwick-road-olton-solihull",
         lode="lode-lane-hobs-moat-road-bus-lanes", town="solihull-town-centre-driving-guide", a452="a452-chester-road-kenilworth-road-hs2",
         vil="knowle-dorridge-and-village-speed-limits", blos="blossomfield-road-junction-signals", cam="solihull-speed-cameras-20mph-and-enforcement",
         stone="stonebridge-island-a446-hs2-roundabout", air="birmingham-airport-roads-and-drop-off", a3400="a3400-hockley-heath-m40-junction-16")
SECTORS = {
    "B90 1": ("Dickens Heath, Majors Green, Tidbury Green and Solihull Lodge", "village", ["Dickens Heath Road", "Haslucks Green Road", "Tilehouse Lane"], ["dickens-heath", "tidbury-green", "solihull-lodge", "majors-green"], ["vil", "a34"], "shirley",
              "Canal bridges, narrow lanes on the edge of the countryside and the busy village centre at Dickens Heath."),
    "B90 2": ("west Shirley — Bills Lane, Shakespeare Drive and Haslucks Green", "suburb", ["Bills Lane", "Shakespeare Drive", "Haslucks Green Road"], ["shirley", "haslucks-green"], ["a34", "cam"], "shirley",
              "Long residential roads with parked cars on both sides — meeting oncoming traffic is the daily lesson here."),
    "B90 3": ("central Shirley and Stratford Road's shops, including Parkgate", "town", ["Stratford Road (A34)", "Solihull Road", "Church Road"], ["shirley"], ["a34", "cam"], "shirley",
              "Stratford Road's shops, bus stops, side roads and pedestrian crossings come one after another."),
    "B90 4": ("Monkspath, Cheswick Green and south Shirley around the test centre", "suburb", ["Stratford Road (A34)", "Monkspath Hall Road", "Cranmore Boulevard", "Tanworth Lane"], ["monkspath", "cheswick-green", "blythe-valley"], ["a34", "m42"], "shirley",
              "The Shirley test centre (B90 4AA) is here, so these are the roads examiners start and finish on."),
    "B91 1": ("Blossomfield, Sharmans Cross and west Solihull", "suburb", ["Blossomfield Road", "Streetsbrook Road", "Sharmans Cross Road", "Warwick Road (A41)"], ["sharmans-cross"], ["blos", "a41"], "town",
              "Leafy roads with schools and colleges — school-run traffic and the signals at Blossomfield Road."),
    "B91 2": ("Lode Heath, Elmdon Heath and north Solihull", "suburb", ["Lode Lane", "Hampton Lane", "Warwick Road (A41)"], ["elmdon-heath"], ["lode", "a41"], "town",
              "Lode Lane's bus lanes and the traffic around JLR's plant at shift changes."),
    "B91 3": ("Hillfield, Widney and south-east Solihull", "suburb", ["Widney Lane", "Widney Road", "Monkspath Hall Road"], ["hillfield", "widney-manor"], ["town", "cam"], "town",
              "Estate roads with mini-roundabouts, linking out to Monkspath and the town centre."),
    "B91 9": ("Solihull town centre, Malvern Park and Widney Manor", "town", ["Warwick Road (A41)", "Homer Road", "Station Road", "Widney Manor Road"], ["solihull-town-centre", "widney-manor"], ["town", "a41"], "town",
              "Town-centre lanes, car-park entrances, buses and pedestrians in every direction."),
    "B92 0": ("Hampton-in-Arden, Catherine-de-Barnes and Bickenhill", "village", ["Hampton Lane / Solihull Road (B4102)", "Catherine-de-Barnes Lane", "Coventry Road (A45)"], ["hampton-in-arden", "catherine-de-barnes", "bickenhill", "barston", "eastcote"], ["vil", "a45"], None,
              "Country lanes at national speed limit, then the fast A45 near the NEC."),
    "B92 7": ("west Olton and the Warwick Road shops", "suburb", ["Warwick Road (A41)", "Kineton Green Road", "Ulverley Green Road"], ["olton", "ulverley-green"], ["a41", "cam"], None,
              "The A41 through Olton: shops, bus stops and right turns across busy traffic."),
    "B92 8": ("east Olton, Hobs Moat and Lode Lane north", "suburb", ["Hobs Moat Road", "Lode Lane", "Ulleries Road", "Old Lode Lane"], ["olton"], ["lode", "a45"], None,
              "Bus lanes and busy junctions where Lode Lane and Hobs Moat Road meet the A45."),
    "B92 9": ("Lyndon, Elmdon and Damsonwood", "estate", ["Damson Parkway", "Lyndon Road", "Coventry Road (A45)"], ["lyndon", "elmdon"], ["a45", "air"], None,
              "Damson Parkway's dual carriageway and roundabouts, with airport traffic close by."),
    "B93 0": ("south Knowle and Chadwick End", "village", ["Warwick Road (Knowle)", "Kenilworth Road", "Hampton Road"], ["knowle", "chadwick-end", "temple-balsall"], ["vil", "a452"], "knowle",
              "Knowle's high street, then fast country roads heading south towards Warwick."),
    "B93 8": ("Dorridge", "village", ["Station Road", "Four Ashes Road", "Grange Road"], ["dorridge"], ["vil"], None,
              "Quiet roads ideal for first lessons, with a busy station area at peak times."),
    "B93 9": ("north Knowle, Bentley Heath and Copt Heath", "village", ["High Street", "Station Road", "Widney Road"], ["knowle", "bentley-heath", "copt-heath"], ["vil", "m42"], "knowle",
              "Knowle's centre and the link out towards M42 junction 5."),
    "B94 5": ("Earlswood and the lanes towards Tanworth-in-Arden (mostly outside Solihull borough)", "village", ["Malthouse Lane", "country lanes at national speed limit"], ["tidbury-green", "earlswood", "tanworth-in-arden"], ["vil"], None,
              "Narrow, twisty lanes where you need to read bends and meet tractors and horses."),
    "B94 6": ("Hockley Heath and the A3400 corridor", "village", ["Stratford Road (A3400)", "Nuthurst Grange Road"], ["hockley-heath", "lapworth", "packwood"], ["a3400", "vil"], None,
              "The A3400 out to M40 junction 16, with village limits and fast stretches in between."),
    "B36 0": ("Smith's Wood and north Kingshurst", "estate", ["Chester Road (A452)", "estate roads off Chester Road"], ["smiths-wood", "kingshurst"], ["a452"], "chelmsley",
              "Estate roads with traffic calming, opening onto the busy A452."),
    "B36 9": ("Castle Bromwich", "suburb", ["Chester Road (A452)", "Bradford Road", "Hurst Lane"], ["castle-bromwich"], ["a452"], None,
              "Junctions on the A452 and links towards the M6 — Garretts Green's patch."),
    "B37 5": ("Fordbridge and south Chelmsley Wood", "estate", ["Chelmsley Road", "Fordbridge Road"], ["fordbridge", "chelmsley-wood"], ["a452"], "chelmsley",
              "Estate roads and the routes to Chelmsley Wood's shops."),
    "B37 6": ("north Chelmsley Wood and the Cooks Lane area", "estate", ["Cooks Lane", "Chester Road (A452)"], ["chelmsley-wood", "kingshurst-smiths-wood"], ["a452"], "chelmsley",
              "Cooks Lane and the A452 — useful for busier junction practice close to Garretts Green."),
    "B37 7": ("Marston Green", "suburb", ["Station Road", "Elmdon Road", "Coleshill Road"], ["marston-green"], ["air", "a45"], None,
              "A village-feel centre next to the airport and NEC, with station traffic at peak times."),
    "CV7 7": ("Balsall Common, Berkswell and Meriden", "village", ["Kenilworth Road (A452)", "Station Road", "Main Road (Meriden)"], ["balsall-common", "berkswell", "meriden"], ["a452", "stone"], None,
              "HS2 works traffic on the A452, plus country lanes and village centres."),
    "B26 3": ("east Sheldon and Elmdon, around Birmingham Airport", "suburb", ["Coventry Road (A45)", "Sheldon side roads"], ["elmdon"], ["a45", "air"], None,
              "The A45 by the airport: several lanes, speed changes and drivers looking for terminal signs."),
    # next to the borough — Birmingham and Bromsgrove sectors whose learners often use Solihull-area test centres
    "B26 1": ("Sheldon and the South Yardley test centre area (Birmingham)", "city", ["Coventry Road (A45)", "Clay Lane", "Sheldon Heath Road"], [], ["a45"], None,
              "South Yardley's test centre is on Clay Lane (B26 1EA) — these are its home roads."),
    "B26 2": ("north Sheldon (Birmingham)", "city", ["Coventry Road (A45)", "Church Road"], [], ["a45"], None,
              "Busy suburban roads either side of the A45."),
    "B27 6": ("Acocks Green (Birmingham)", "city", ["Warwick Road (A41)", "Westley Road", "Yardley Road"], [], ["a41"], None,
              "Acocks Green's busy centre on the A41, a short drive from Olton."),
    "B27 7": ("south Acocks Green and the Shirley Road area (Birmingham)", "city", ["Shirley Road", "Fox Hollies Road", "Warwick Road (A41)"], [], ["a41"], None,
              "Residential roads that feed the A41 and A34."),
    "B28 0": ("south Hall Green and the Robin Hood area (Birmingham)", "city", ["Stratford Road (A34)", "Robin Hood Lane", "Baldwins Lane"], [], ["a34"], None,
              "The A34 heading south into Shirley — the same road the Shirley test uses."),
    "B28 8": ("Hall Green north (Birmingham)", "city", ["Fox Hollies Road", "Shaftmoor Lane", "Stratford Road (A34)"], [], ["a34"], None,
              "Busy city junctions and bus routes."),
    "B28 9": ("Hall Green east (Birmingham)", "city", ["Stratford Road (A34)", "Highfield Road"], [], ["a34"], None,
              "Residential roads between the A34 and Olton."),
    "B47 5": ("Hollywood (Bromsgrove district)", "village", ["Alcester Road (A435)", "May Lane"], ["solihull-lodge", "hollywood"], ["a34"], None,
              "On the borough edge — Kings Heath, Shirley and Redditch are all within reach."),
    "B47 6": ("Wythall (Bromsgrove district)", "village", ["Alcester Road (A435)", "Station Road"], ["wythall"], ["vil"], None,
              "Semi-rural roads; Redditch and Kings Heath are the nearest centres."),
    "B33 0": ("Garretts Green and Kitts Green (Birmingham)", "city", ["Granby Avenue", "Garretts Green Lane", "Kitts Green Road"], [], ["a45"], None,
              "Garretts Green's test centre is on Granby Avenue (B33 0SD) — these are its home roads."),
    "B33 8": ("Stechford (Birmingham)", "city", ["Station Road", "Flaxley Road", "Bordesley Green East"], [], [], None,
              "Busy city junctions close to Garretts Green."),
    "B33 9": ("Lea Hall and north Stechford (Birmingham)", "city", ["Bordesley Green East", "Meadway"], [], [], None,
              "Dual-carriageway stretches and estate roads near Garretts Green."),
    "B34 6": ("Shard End (Birmingham)", "city", ["Shard End Crescent", "Cole Hall Lane"], ["castle-bromwich"], ["a452"], None,
              "Estate roads between Castle Bromwich and Garretts Green."),
    "B34 7": ("east Shard End (Birmingham)", "city", ["Cole Hall Lane", "Packington Avenue"], ["kingshurst"], ["a452"], None,
              "Quiet estate roads next to Kingshurst."),
    "B25 8": ("Yardley (Birmingham)", "city", ["Coventry Road (A45)", "Church Road", "Stoney Lane"], [], ["a45"], None,
              "Inner-city traffic between South Yardley and Garretts Green."),
    "B36 8": ("Hodge Hill (Birmingham)", "city", ["Coleshill Road", "Hodge Hill Common"], ["castle-bromwich"], [], None,
              "Busy routes towards Castle Bromwich and the M6."),
    "B35 6": ("Castle Vale (Birmingham)", "city", ["Farnborough Road", "Chester Road"], ["castle-bromwich"], ["a452"], None,
              "Wide estate roads and roundabouts beside the A452."),
    "B35 7": ("south Castle Vale (Birmingham)", "city", ["Tangmere Drive", "Chester Road"], ["castle-bromwich"], ["a452"], None,
              "Estate roads and the A452 junctions towards Castle Bromwich."),
}
# centroids of every sector (lat, lon) from the postcode list
CENT = {"B90 1": (52.39547, -1.84847), "B90 2": (52.40599, -1.83506), "B90 3": (52.41219, -1.82116), "B90 4": (52.39137, -1.80551),
        "B91 1": (52.41642, -1.79946), "B91 2": (52.42197, -1.7716), "B91 3": (52.40558, -1.782), "B91 9": (52.41324, -1.77575),
        "B92 0": (52.42482, -1.71596), "B92 7": (52.4402, -1.8045), "B92 8": (52.44088, -1.78864), "B92 9": (52.438, -1.76866),
        "B93 0": (52.3767, -1.72226), "B93 8": (52.37457, -1.75548), "B93 9": (52.38972, -1.74782), "B94 5": (52.34456, -1.81981),
        "B94 6": (52.35426, -1.77107), "B36 0": (52.50202, -1.75375), "B36 9": (52.5079, -1.77133), "B37 5": (52.47829, -1.74915),
        "B37 6": (52.48861, -1.74397), "B37 7": (52.47142, -1.73618), "CV7 7": (52.40794, -1.64467), "B26 3": (52.45591, -1.77887),
        "B26 1": (52.46096, -1.80426), "B26 2": (52.46787, -1.78986), "B27 6": (52.45024, -1.81915), "B27 7": (52.44023, -1.82586),
        "B28 0": (52.42063, -1.84741), "B28 8": (52.43721, -1.84322), "B28 9": (52.42807, -1.83586), "B47 5": (52.39053, -1.87959),
        "B47 6": (52.37869, -1.88105), "B33 0": (52.47514, -1.77133), "B33 8": (52.47966, -1.80402), "B33 9": (52.48616, -1.79176),
        "B34 6": (52.49656, -1.79235), "B34 7": (52.49597, -1.76954), "B25 8": (52.46573, -1.82113), "B36 8": (52.50346, -1.81078),
        "B35 6": (52.52242, -1.78788), "B35 7": (52.5162, -1.78991)}

# good and hard, by kind of area (road features — not quotes)
KIND = {
    "village": (["Quiet roads to build confidence before anything busy.", "Real country driving that town learners rarely get.", "Light traffic, so you can think about each skill.", "Village centres teach slow, careful driving around people."],
                ["Bends you can't see round — slow down before the bend, not in it.", "National speed limit doesn't mean drive at 60.", "Meeting tractors, cyclists and horses on narrow lanes.",
                 "Roads with no pavement — expect walkers in the road.", "Single-track stretches where someone has to reverse to a passing place.", "Sudden drops from 60 to 30 at village gateways.",
                 "Mud and leaves on country roads in autumn.", "Parked cars narrowing the high street."]),
    "suburb": (["Calm residential roads for junction practice.", "Busier main roads only a few minutes away when you're ready.", "Plenty of side roads for turning and emerging.", "Easy places for parallel parking practice."],
               ["Parked cars on both sides — who gives way?", "Mini-roundabouts and side roads close together.", "School-run traffic at 8–9am and 3–4pm.", "Emerging from side roads with parked cars blocking your view.",
                "Cyclists and delivery vans stopping suddenly.", "Speed humps and 20 mph limits near schools.", "Bus stops where buses pull out without much warning.", "Right turns onto a busy main road."]),
    "town": (["Everything in one place: lanes, signals, crossings and parking.", "Lots of variety in a short lesson.", "Good for building observation habits.", "Real car parks for manoeuvre practice."],
             ["Lane choice at signals and roundabouts.", "Pedestrians stepping out between buses.", "Bus lanes and their hours.", "Car-park entrances and exits across the pavement.",
              "Delivery vehicles stopped in the lane.", "Crossings every few hundred metres.", "Taxis and buses pulling in and out.", "Queues that block junctions — keep them clear."]),
    "estate": (["Long estate roads for clutch control, turning and manoeuvres.", "Quiet loops for repeating a skill until it sticks.", "Wide roads for turning in the road.", "Low speeds while you build confidence."],
               ["Speed humps and chicanes — slow and smooth.", "Children and ball games near the road.", "Joining a fast main road from a quiet estate.", "Cars parked half on the pavement.",
                "Blind bends between blocks of houses.", "Mini-roundabouts on estate spine roads.", "Pedestrians crossing anywhere, not just at crossings.", "Narrow gaps between parked cars."]),
    "city": (["Busy roads build the skills every Birmingham test centre checks.", "Plenty of traffic lights and filter lanes to practise.", "Good bus and cycle awareness training.", "Close to two or three test centres."],
             ["Multi-lane junctions and filter lights.", "Bus lanes and box junctions.", "Heavy traffic at peak times.", "Cyclists filtering through queues.",
              "Pedestrians crossing between queuing cars.", "Lane changes with little space.", "Parked cars on main roads.", "Junctions with several sets of lights."]),
}


def pick(pool, n, seed):
    return [pool[(seed * 3 + i) % len(pool)] for i in range(n)]


ROADG = {r: f"{R[r]}.html" for r in R}
NAMES = {a["slug"]: a["name"] for a in SOL.AREAS}
SHORT = {}
try:
    import pages_sol_roads as _RD
    SHORT = {r["slug"]: r["short"] for r in _RD.ROADS}
except Exception:  # pragma: no cover
    pass


def slug(code):
    return f"postcode-{code.lower().replace(' ', '-')}-driving-lessons"


def P(sl, crumb, title, seo, desc, stats, keys, body, faqs, src, related=None, cat="Solihull local guide"):
    path = f"solihull/{sl}.html"
    rel = related or [("solihull/solihull-postcode-sectors.html", "Postcodes", "Every Solihull postcode sector", "Nearest test centres for each.")]
    return path, S(path, seo, cat, (crumb, path), title, desc, stats, keys, body + portal_strip(), faqs, [SRC[k] if isinstance(k, str) else k for k in src], rel)


def chips(items):
    return '<div class="hero__badges">' + "".join(f'<a class="chip" href="{h}">{n}</a>' for h, n in items) + "</div>"


def ranked(code):
    c = CENT[code]
    return sorted(((miles(c, TC[x["slug"]]), x) for x in CENTRES), key=lambda t: t[0])


def sector_page(code):
    areas, kind, roads, aslugs, rg, park, note = SECTORS[code]
    rk = ranked(code)
    (d1, c1), (d2, c2) = rk[0], rk[1]
    best = max(rk[:3], key=lambda t: t[1]["rate"])
    district = code.split()[0]
    seed = sorted(SECTORS).index(code)
    good, hard = pick(KIND[kind][0], 2, seed), pick(KIND[kind][1], 3, seed)
    mk = c1["mistakes"][seed % len(c1["mistakes"])]
    areas_obj = [a for a in SOL.AREAS if a["slug"] in aslugs]
    fuel = sorted(((miles(CENT[code], f[3]), f) for f in FUEL), key=lambda t: t[0])
    fuel = [t for t in fuel if t[0] <= 2.0][:4]
    rows = "".join(f'<tr><td><a href="{x["slug"]}-driving-test-centre-routes.html">{x["full"]}</a></td><td>{d:.1f} miles</td><td>{x["rate"]}%</td></tr>' for d, x in rk)
    body = f"""<p class="lead">Driving lessons in {code}: {areas}. {note}</p>
{RS._figs([(f"{d1:.1f} mi", f"to {c1['name']} test centre", "straight line from the middle of " + code), (f"{c1['rate']}%", f"{c1['name']} pass rate", "2024-25"), (f"{d2:.1f} mi", f"to {c2['name']}", "next nearest"), ("£35", "per hour", "manual or automatic")])}
<h2>Which test centre for {code}?</h2>
<p>From the middle of {code}, {c1['full']} is closest at about {d1:.1f} miles in a straight line, then {c2['full']} at {d2:.1f} miles. {"Within your three nearest, " + best[1]['name'] + " has the highest recent pass rate (" + str(best[1]['rate']) + "%)." if best[1] is not c1 else c1['name'] + " is also the best pass rate of your three nearest."} Most learners do best at the centre whose roads they've practised most, so pick early and train there.</p>
<div class="table-wrap"><table><thead><tr><th>Test centre</th><th>Distance</th><th>Pass rate 2024-25</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="note">Distances are straight-line from the centre of the postcode sector; driving distances are longer. Pass rates from passrates.uk (DVSA data).</p>
<h2>Roads you'll learn on in {code}</h2><ul>{''.join(f'<li>{r}</li>' for r in roads)}</ul>
{('<p>Road guides for this area: ' + ', '.join(f'<a href="{ROADG[r]}">{SHORT.get(R[r], R[r])}</a>' for r in rg) + '.</p>') if rg else ''}
<h2>The good and the hard here</h2>
<p><b>Good:</b> {' '.join(good)}</p><p><b>Harder parts learners meet:</b></p><ul>{''.join(f'<li>{h}</li>' for h in hard)}</ul>
<p>A test fault at {c1['name']} we prepare {code} learners for: <b>{mk[0]}</b> — {mk[1]} {mk[2]}</p>"""
    if areas_obj:
        body += f"<h2>What lessons look like in {code}</h2>" + "".join(f"<p><b>{a['name']}:</b> {a['local']}</p>" for a in areas_obj[:2])
        lm = [x for a in areas_obj for x in a["near"]][:5]
        if lm:
            body += "<p>Landmarks you'll drive past: " + ", ".join(lm) + ".</p>"
    near = sorted((miles(CENT[code], CENT[o]), o) for o in SECTORS if o != code)[:4]
    body += f"<p>Closest sectors: " + ", ".join(f'<a href="{slug(o)}.html">{o}</a> ({d:.1f} mi)' for d, o in near) + ".</p>"
    if fuel:
        body += f"<h2>Filling up near {code}</h2><ul>" + "".join(f'<li><b>{f[1]}</b> — {f[2]} ({d:.1f} mi). {f[4]}</li>' for d, f in fuel) + '</ul><p>First time at a pump? Our <a href="petrol-stations-solihull-learner-guide.html">petrol station guide</a> walks you through it.</p>'
    if park:
        body += f"<h2>Parking and shops nearby</h2><ul>" + "".join(f"<li><b>{n}</b> — {d}</li>" for n, d, _ in PARK[park]) + '</ul><p>See <a href="car-parks-solihull-learner-guide.html">car parks for learners</a> before practising bay parking anywhere.</p>'
    links = [(f"driving-lessons-{s}.html", NAMES[s]) for s in aslugs if s in NAMES]
    if district in ("B90", "B91", "B92", "B93", "B94", "B36", "B37", "B40") or district == "CV7":
        links.append((f"{district.lower()}-driving-lessons.html", f"All of {district}"))
    body += f"<h2>Nearby</h2>{chips(links)}"
    faqs = [(f"Do you give driving lessons in {code}?", f"Yes — across {areas.split(' (')[0]}, manual or automatic, from £35 an hour."),
            (f"What is the nearest driving test centre to {code}?", f"{c1['full']}, about {d1:.1f} miles in a straight line. {c2['full']} is next at about {d2:.1f} miles."),
            (f"Which roads will I practise on in {code}?", ", ".join(roads[:3]) + ", then the test routes for your chosen centre.")]
    src = [c1["src"], c2["src"], "pcdata"] + sorted({f[5] for _, f in fuel}) + sorted({s for _, _, s in PARK.get(park, [])})
    return P(slug(code), code, f"Driving lessons in {code}", f"Driving Lessons {code} | Nearest Test Centre {c1['name']} | SQ Driving School",
             f"Driving lessons in {code} ({areas.split(',')[0].split(' (')[0]}): nearest test centre {c1['name']} ({d1:.1f} mi), local roads, fuel and parking, and the good and hard parts for learners. £35/hr.",
             [(code, "postcode sector"), (c1["name"], f"nearest centre, {d1:.1f} mi"), (f"{c1['rate']}%", "its pass rate"), ("£35", "per hour")],
             [f"Nearest test centre: {c1['name']} ({d1:.1f} mi).", f"Next: {c2['name']} ({d2:.1f} mi).", f"Main roads: {', '.join(roads[:2])}.", "Free DriveSQ Student Portal."],
             body, faqs, src, cat="Postcode sector")


def sectors_hub():
    rows = ""
    for code in sorted(SECTORS):
        (d1, c1) = ranked(code)[0]
        rows += f'<tr><td><a href="{slug(code)}.html">{code}</a></td><td>{SECTORS[code][0]}</td><td>{c1["name"]} ({d1:.1f} mi)</td></tr>'
    body = f"""<p class="lead">Every postcode sector in Solihull — and the Birmingham and Bromsgrove sectors right next to it — with the nearest driving test centre, the roads you'll learn on, and where to fill up and park.</p>
{RS._figs([(str(len(SECTORS)), "postcode sectors", ""), ("7", "test centres compared", ""), (str(len(FUEL)), "fuel stations listed", ""), ("£35", "per hour", "")])}
<div class="table-wrap"><table><thead><tr><th>Sector</th><th>Covers</th><th>Nearest test centre</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="note">Distances are straight-line from each sector's centre, worked out from published postcode coordinates. Not sure of your sector? It's the first half of your postcode plus the first number of the second half — B91 3QJ is sector B91 3.</p>
<h2>Postcode districts</h2>{chips([(f"{d.lower()}-driving-lessons.html", d) for d in ("B90", "B91", "B92", "B93", "B94", "B36", "B37", "B40", "CV7")])}
<p>Rather type your postcode? The free <a href="{DSQ}solihull-driving-test-centre-finder.html" target="_blank" rel="noopener">DriveSQ test centre finder</a> does it for you.</p>"""
    return P("solihull-postcode-sectors", "Postcode sectors", "Every Solihull postcode sector", "Solihull Postcode Sectors | Nearest Driving Test Centre for Each | SQ",
             f"All {len(SECTORS)} postcode sectors in and around Solihull — B90 to B94, B36, B37, CV7 and neighbouring Birmingham sectors — with nearest test centre and local driving guide.",
             [(str(len(SECTORS)), "sectors"), ("7", "test centres"), ("Free", "postcode finder"), ("£35", "per hour")],
             ["Find your sector's nearest test centre.", "Each sector has its own local guide.", "Fuel and parking near you.", "Book from any page."],
             body, [("How do I find my postcode sector?", "Take the first half of your postcode and the first number of the second half: B91 3QJ is B91 3."),
                    ("Do you cover the Birmingham side of Solihull too?", "Yes — Sheldon, Acocks Green, Hall Green, Garretts Green, Shard End, Castle Vale and nearby sectors.")],
             ["pcdata", "pr_shirley", "pr_gg", "pr_sy", "find"], cat="Postcode sector")


# ============================================================ GUIDES
def fuel_rows(items):
    return "".join(f"<tr><td>{f[0]}</td><td>{f[1]}</td><td>{f[2]}</td><td>{min(miles(f[3], TC[c]) for c in ('shirley', 'garretts-green', 'south-yardley')):.1f} mi</td></tr>" for f in items)


def guides():
    out = []
    near_tc = lambda f: min(((miles(f[3], TC[c]), CEN[c]["name"]) for c in ("shirley", "garretts-green", "south-yardley")))
    shell = [f for f in FUEL if f[0] == "Shell"]
    out.append(P("petrol-stations-solihull-learner-guide", "Petrol stations", "Petrol stations in Solihull: a learner's guide",
                 "Petrol Stations in Solihull for Learner Drivers | Shell, Tesco, Esso & More | SQ",
                 f"{len(FUEL)} petrol stations across Solihull — Shell, Tesco, Sainsbury's, Asda, BP, Esso and Texaco — and how to fill up for the first time without getting it wrong.",
                 [(str(len(FUEL)), "stations listed"), ("Green", "petrol nozzle"), ("Black", "diesel nozzle"), ("E10", "standard petrol since 2021")],
                 ["Check which side your filler cap is on before you pull in.", "Green nozzle = petrol, black = diesel.", "Engine off, no smoking.", "Wrong fuel? Don't start the engine."],
                 f"""<p class="lead">Your first fill-up is a rite of passage — and a forecourt is a surprisingly good driving lesson: slow-speed control, tight spaces, other drivers pulling out, and a busy road to rejoin. Here are the stations across Solihull, and how to do it right.</p>
<h2>Filling up, step by step</h2><ol class="rx-steps"><li data-n="1"><h4>Know your side</h4><p>On most modern cars a small arrow next to the fuel gauge points to the filler cap side. Pull in so the pump is on that side.</p></li><li data-n="2"><h4>Engine off</h4><p>Handbrake on, engine off, no smoking, phone away.</p></li><li data-n="3"><h4>Right fuel</h4><p>In the UK, petrol nozzles are usually green and diesel nozzles black. Read the label too. E10 is the standard petrol; E5 (super) is for older cars that need it.</p></li><li data-n="4"><h4>Pay</h4><p>Some pumps are pay-at-pump; otherwise note your pump number and pay in the shop.</p></li><li data-n="5"><h4>Leave carefully</h4><p>Check around the car, then rejoin the road like any junction — mirrors, signal, and wait for a proper gap.</p></li></ol>
<div class="callout"><b>Put the wrong fuel in?</b> Don't start the engine or switch on the ignition. Tell the staff, push the car clear if it's safe, and call your breakdown cover.</div>
<h2>Stations across Solihull</h2>
<div class="table-wrap"><table><thead><tr><th>Brand</th><th>Station</th><th>Address</th><th>To nearest Solihull-area test centre</th></tr></thead><tbody>{fuel_rows(FUEL)}</tbody></table></div>
<p class="note">Listed from public fuel-price sites and station locators in 2026. Prices change daily and sites open or close — check before you travel.</p>
<h2>Forecourts as practice</h2><ul><li><b>Slow-speed control:</b> creeping into a pump space is clutch and steering practice.</li><li><b>Observation:</b> people walk between pumps, and cars reverse out of air and car-wash bays.</li><li><b>Rejoining:</b> stations on the A34, A41 and A45 mean pulling out onto busy main roads — treat it as an emergency-proof junction.</li></ul>
<p>Shell drivers: see our <a href="shell-garages-solihull-learner-drivers.html">Shell garages guide</a>. Stations by your postcode: <a href="solihull-postcode-sectors.html">find your sector</a>.</p>""",
                 [("Can learner drivers go into petrol stations?", "Yes. With L plates and a qualified supervising driver, filling up is normal driving — and good practice."),
                  ("How do I know which side the petrol cap is on?", "On most modern cars there's a small arrow next to the fuel gauge pointing to that side."),
                  ("What if I put diesel in a petrol car?", "Don't start the engine. Tell the staff and call your breakdown cover.")],
                 ["e10", "shell_loc", "fuel_list", "fuel_sup", "bp_loc"]))
    srows = "".join(f"<li><b>{f[1]}</b> — {f[2]}. {f[4]} About {near_tc(f)[0]:.1f} miles from {near_tc(f)[1]} test centre.</li>" for f in shell)
    out.append(P("shell-garages-solihull-learner-drivers", "Shell garages", "Shell garages in Solihull for learner drivers",
                 "Shell Garages Solihull | Shirley Triangle, Warwick Road, Box Trees | SQ Driving School",
                 "The three Shell garages in Solihull — Shirley Triangle on the A34, Warwick Road in Solihull and Box Trees on the A3400 — and what each teaches a learner driver.",
                 [("3", "Shell sites"), (f"{miles(FUEL[0][3], TC['shirley']):.1f} mi", "Shirley Triangle to Shirley test centre"), ("24h", "Shirley Triangle"), ("A34", "A41 and A3400")],
                 ["Shirley Triangle is on the same stretch of the A34 as the test centre.", "Warwick Road is on the A41 into Solihull.", "Box Trees is on the fast A3400.", "Each one means rejoining a main road."],
                 f"""<p class="lead">Solihull has three Shell garages, each on a main road learners use — so they're as much a driving lesson as a fuel stop.</p><ul>{srows}</ul>
<h2>What each one teaches</h2>
<h3>Shirley Triangle, Stratford Road (A34)</h3><p>A few hundred metres from the Shirley test centre on the same road. Getting in and out means reading the A34's lanes, buses and traffic from the side roads — exactly what <a href="shirley-driving-test-centre-routes.html">Shirley test routes</a> ask of you.</p>
<h3>Warwick Road, Solihull (A41)</h3><p>On the A41 into Solihull — a busy single road with junctions and right turns. See the <a href="a41-warwick-road-olton-solihull.html">A41 guide</a>.</p>
<h3>Box Trees, Hockley Heath (A3400)</h3><p>A faster road between villages and M40 junction 16. Leaving means judging the speed of traffic that may be doing much more than you — see the <a href="a3400-hockley-heath-m40-junction-16.html">A3400 guide</a>.</p>
<p>All stations, all brands: <a href="petrol-stations-solihull-learner-guide.html">petrol stations in Solihull</a>.</p>""",
                 [("How many Shell garages are in Solihull?", "Public listings show three: Shirley Triangle (B90 4AU), Warwick Road (B91 1BB) and Box Trees, Hockley Heath (B94 6NS)."),
                  ("Is there a petrol station near Shirley test centre?", "Yes — Shell Shirley Triangle and Sainsbury's Marshall Lake are both a few hundred metres away on Stratford Road.")],
                 ["shell_loc", "fuel_sup", "e10"]))
    pk = "".join(f"<h3>{t}</h3><ul>" + "".join(f"<li><b>{n}</b> — {d}</li>" for n, d, _ in PARK[k]) + "</ul>" for k, t in (("town", "Solihull town centre"), ("shirley", "Shirley"), ("knowle", "Knowle"), ("chelmsley", "Chelmsley Wood")))
    out.append(P("car-parks-solihull-learner-guide", "Car parks", "Car parks in Solihull: a learner driver's guide",
                 "Car Parks Solihull for Learner Drivers | Bay Parking Practice | SQ Driving School",
                 "Solihull car parks for learners — town centre, Shirley, Knowle and Chelmsley Wood — plus how the driving test's bay park works and how to practise it properly.",
                 [("3", "parking manoeuvres on the test"), ("1", "asked on your test"), ("Free", "Shirley council car parks up to 3 hrs Mon–Sat"), ("Closed", "Mell Square (redevelopment)")],
                 ["Mell Square car park has closed for the Holbeche Place redevelopment.", "Shirley council car parks: free up to 3 hours Mon–Sat (April 2026 notice).", "Retail parks are private land — follow their rules.", "Practise at quiet times."],
                 f"""<p class="lead">Parking is the part of driving most learners worry about — and the part that improves fastest with the right practice in the right place.</p>
<h2>Parking on the driving test</h2><p>You'll be asked to do one of three: <b>parallel park</b> at the side of the road, <b>park in a bay</b> (either drive in and reverse out, or reverse in and drive out), or <b>pull up on the right</b>, reverse about two car lengths and rejoin the traffic.</p>
<h2>Where to park in Solihull</h2>{pk}
<p class="note">Charges and rules change — check signs and the council website. Retail-park and supermarket car parks are private land; many limit stays and use cameras.</p>
<h2>How we practise bay parking</h2><ol><li>Start in a quiet corner of a car park at an off-peak time.</li><li>Use reference points (where the bay line meets your mirror) rather than guessing.</li><li>Creep — clutch control or gentle brake in an automatic.</li><li>Look all round: people walk behind reversing cars.</li><li>Then move to busier car parks and multi-storeys: ramps, pillars, height bars and ticket barriers.</li></ol>
<h2>Multi-storey tips</h2><ul><li>Ramps: keep to your side and hold your speed low.</li><li>Pillars and tight bays: check your mirrors as you turn in.</li><li>Ticket barriers: stop close enough to reach.</li></ul>""",
                 [("Which car parks in Solihull are good for learners?", "Quiet corners of large car parks at off-peak times. Follow each car park's rules — retail parks are private land."),
                  ("What parking will I do on my driving test?", "One of: parallel park, bay park (in forwards or backwards) or pull up on the right and reverse two car lengths."),
                  ("Is Mell Square car park open?", "No — the council closed it for the Holbeche Place redevelopment. It names Poplar Road, Lode Lane and Dominion Court as alternatives.")],
                 ["during", "cp_town", "holbeche", "cp_fees", "cp_knowle", "cp_all", "touchwood", "sears", "parkgate"]))
    out.append(P("shops-and-retail-parks-solihull-driving", "Shops & retail parks", "Driving to Solihull's shops and retail parks",
                 "Driving to Touchwood, Parkgate & Sears Retail Park | Solihull Learner Guide | SQ",
                 "Touchwood, Holbeche Place, Parkgate, Sears Retail Park, Knowle and Chelmsley Wood: what each is like to drive to as a learner, and what each teaches.",
                 [("1,650", "Touchwood spaces"), ("500", "Parkgate basement spaces"), ("~920", "Sears Retail Park spaces"), ("2 hrs", "reported Sears stay limit")],
                 ["Busy car parks are advanced practice, not first-lesson places.", "Watch for people between parked cars.", "Basement parking means ramps and tight turns.", "Check stay limits and cameras."],
                 """<p class="lead">Shopping trips are where new drivers meet the hardest parking: busy aisles, people pushing trolleys, ramps and tight bays. Here's what Solihull's main shopping places are like to drive to.</p>
<h2>Solihull town centre — Touchwood and Holbeche Place</h2><p>Touchwood's car park is large (about 1,650 spaces). Mell Square is being redeveloped as Holbeche Place, so its car park has closed — the council points drivers to Poplar Road, Lode Lane and Dominion Court instead. Getting there means the town centre's lanes and signals — see the <a href="solihull-town-centre-driving-guide.html">town centre guide</a>.</p>
<h2>Shirley — Parkgate and Stratford Road</h2><p>Parkgate's Asda has a 500-space basement car park: ramps, pillars and artificial light. The approach is the A34 — busy, with buses and many side roads. See <a href="a34-stratford-road-shirley.html">A34 Stratford Road</a>.</p>
<h2>Sears Retail Park, Shirley</h2><p>M&amp;S, Boots, TK Maxx and more, with around 920 spaces and a reported 2-hour stay limit. Wide but busy — a step up from quiet bay practice.</p>
<h2>Knowle and Dorridge</h2><p>Village centres with pay-and-display car parks behind the high street. Narrow access roads and pedestrians — slow is the skill. See <a href="knowle-dorridge-and-village-speed-limits.html">village speed limits</a>.</p>
<h2>Chelmsley Wood</h2><p>The council's Hedingham Grove car park is free with 55 spaces. Estate roads and the A452 around it — see <a href="a452-chester-road-kenilworth-road-hs2.html">A452 guide</a>.</p>
<p>Before you practise: <a href="car-parks-solihull-learner-guide.html">car parks for learners</a>.</p>""",
                 [("Can I practise parking at Touchwood?", "Busy shopping car parks are best once you can already bay park in quiet places. Follow the car park's rules."),
                  ("Is there free parking in Shirley?", "Under the council's April 2026 notice, Shirley council car parks are free for up to 3 hours Monday–Saturday. Check signs on the day.")],
                 ["touchwood", "holbeche", "parkgate", "sears", "ms_sears", "cp_fees", "cp_knowle", "cp_all"]))
    out.append(P("road-signs-solihull-test-routes", "Road signs", "Road signs you'll meet on Solihull test routes",
                 "Road Signs on Solihull Driving Test Routes | What They Mean | SQ Driving School",
                 "The road signs Solihull learners meet most — 20 mph zones, bus lanes, mini-roundabouts, no entry, school and camera signs, and the gantry signs on the M42 — and what each tells you to do.",
                 [("Circles", "give orders"), ("Triangles", "warn"), ("Rectangles", "inform"), ("Red X", "lane closed — don't use it")],
                 ["Circles give orders, triangles warn, rectangles inform.", "Bus lane signs show the hours it applies.", "A red X over a motorway lane means you must not drive in it.", "Not responding to signs is a regular test fault."],
                 """<p class="lead">Every sign on a Solihull test route is there to tell you something — and not responding to signs and road markings is one of DVSA's regular reasons for failing. Learn the shapes first, then the local ones.</p>
<h2>The shapes</h2><ul><li><b>Circles</b> give orders. Red rings say what you mustn't do (speed limits, no entry, no right turn); blue circles say what you must do (turn left, mini-roundabout, keep left).</li><li><b>Triangles</b> warn: junctions, bends, roundabouts, school crossings, humps.</li><li><b>Rectangles</b> inform: directions, lanes, bus lane times. Blue on motorways, green on primary roads like the A34 and A45, white on local roads, brown for attractions such as the NEC and Resorts World.</li></ul>
<h2>The ones you'll meet most in Solihull</h2>
<h3>20 mph zones and limits</h3><p>More residential streets and areas near schools are 20 mph. Repeater signs and road markings remind you — see <a href="solihull-speed-cameras-20mph-and-enforcement.html">cameras and 20 mph</a>.</p>
<h3>Bus lanes</h3><p>A blue sign shows the hours the lane is in force. Outside those hours you can use it; inside them you can't. Lode Lane is a good place to learn this — <a href="lode-lane-hobs-moat-road-bus-lanes.html">bus lane guide</a>.</p>
<h3>Mini-roundabouts</h3><p>A blue circle with three white arrows. Give way to traffic from the right and go round the painted circle where you can.</p>
<h3>No entry and one-way</h3><p>Town-centre and car-park entrances use them a lot — see the <a href="solihull-town-centre-driving-guide.html">town centre guide</a>.</p>
<h3>School and pedestrian warning triangles</h3><p>Expect them on roads like Blossomfield Road and near every school we list on our Solihull pages.</p>
<h3>Motorway gantries on the M42</h3><p>Overhead signs set speed limits and close lanes. A red X means that lane is closed — you must not drive in it. A speed in a red ring is mandatory. See <a href="m42-junctions-3a-4-5-6-solihull.html">M42 junctions</a> and <a href="motorway-driving-lessons-m42-solihull.html">motorway lessons</a>.</p>
<h3>Countdown markers</h3><p>On the approach to a motorway exit, markers with three, two and one bar count down roughly 300, 200 and 100 yards to the slip road.</p>""",
                 [("What does a red X on the M42 mean?", "That lane is closed. You must not drive in it — move out of it safely and stay out until signs say otherwise."),
                  ("Can I drive in a bus lane in Solihull?", "Only outside the hours shown on its blue sign. During those hours, only the vehicles shown on the sign can use it."),
                  ("What's the easiest way to learn road signs?", "Shapes first: circles order, triangles warn, rectangles inform.")],
                 ["hc_signs", "kyts", "hc_mway", "faults", "speed"]))
    out.append(P("road-markings-solihull-learner-guide", "Road markings", "Road markings in Solihull: what learners need to know",
                 "Road Markings Solihull | Box Junctions, Hatching, Bus Lanes | SQ Driving School",
                 "Box junctions, hatched areas, double white lines, zig-zags, bus lanes and give-way lines: what each road marking means and where Solihull learners meet them.",
                 [("Yellow box", "don't enter unless your exit is clear"), ("Zig-zags", "no parking or overtaking"), ("Solid white", "don't cross"), ("Dashed", "give way")],
                 ["Don't enter a yellow box unless your exit is clear (unless turning right and only blocked by oncoming traffic).", "Hatching with a solid edge: don't enter except in an emergency.", "Zig-zags at crossings: no parking, no overtaking.", "Lane arrows tell you where each lane goes."],
                 """<p class="lead">Road markings are signs painted on the road — and "not responding correctly to road markings" is one of the faults DVSA lists most often. On busy roads like the A34 and A45 they tell you which lane to be in long before you reach the junction.</p>
<h2>The markings that matter most</h2>
<h3>Lane arrows</h3><p>On multi-lane approaches (the A34 through Shirley, the A45 near the airport, the M42 junction roundabouts) the arrows tell you where each lane goes. Read them early and get in lane before the solid lines start.</p>
<h3>Yellow box junctions</h3><p>Don't enter the box unless your exit is clear. The exception: you may wait in it to turn right if only oncoming traffic or other right-turners are stopping you.</p>
<h3>Hatched areas</h3><p>Diagonal stripes or chevrons separate traffic. With a broken border, don't enter unless it's necessary and safe; with a solid border, don't enter except in an emergency.</p>
<h3>Double white lines</h3><p>If the line nearest you is solid, don't cross or straddle it except in the situations the Highway Code allows, such as passing a stationary vehicle.</p>
<h3>Zig-zags at crossings</h3><p>No parking, and don't overtake the moving vehicle nearest the crossing. School "keep clear" markings work the same way at school entrances.</p>
<h3>Give way and stop lines</h3><p>A double broken line means give way; a solid line with a STOP sign means stop, every time.</p>
<h3>Bus lanes</h3><p>A thick solid white line marks the lane; "BUS LANE" is painted at the start. Check the sign for its hours.</p>
<p>Next: <a href="road-signs-solihull-test-routes.html">road signs</a> · <a href="pedestrian-crossings-solihull-learner-guide.html">pedestrian crossings</a> · <a href="roundabouts-solihull-learner-guide.html">roundabouts</a>.</p>""",
                 [("Can I stop in a yellow box junction?", "Only when you're turning right and the only thing stopping you is oncoming traffic or other vehicles waiting to turn right."),
                  ("Can I drive over hatched lines?", "With a broken border, only if it's necessary and safe. With a solid border, only in an emergency.")],
                 ["hc_marks", "hc_road", "faults"]))
    out.append(P("pedestrian-crossings-solihull-learner-guide", "Pedestrian crossings", "Pedestrian crossings in Solihull: zebra, pelican, puffin and toucan",
                 "Pedestrian Crossings Solihull | Zebra, Pelican, Puffin, Toucan | SQ Driving School",
                 "Zebra, pelican, puffin and toucan crossings explained for Solihull learners — what the lights mean, when to wait, and where crossings come thick and fast on the A34, A41 and in the town centre.",
                 [("Zebra", "give way to people on it"), ("Flashing amber", "pelican only"), ("Puffin", "sensors, no flashing amber"), ("Toucan", "pedestrians and cyclists")],
                 ["At a zebra, give way to anyone already on it.", "Flashing amber at a pelican: give way to anyone still crossing.", "Puffin and toucan crossings use sensors — wait for green.", "Never wave pedestrians across."],
                 """<p class="lead">Shirley's Stratford Road, Olton's Warwick Road and Solihull town centre have crossings every few hundred metres. Each type works differently — and a crossing mistake can be a serious fault.</p>
<h2>The four you'll meet</h2>
<h3>Zebra</h3><p>Black and white stripes with flashing yellow beacons. Be ready to stop for anyone waiting, and you must give way once someone has stepped onto the crossing.</p>
<h3>Pelican</h3><p>Lights with a flashing amber phase. On flashing amber you can go only if the crossing is clear — give way to anyone still on it.</p>
<h3>Puffin</h3><p>Sensors watch the people crossing, so there's no flashing amber — the lights go red, red-and-amber, then green.</p>
<h3>Toucan</h3><p>Like a puffin, but cyclists can ride across too. Look for bikes approaching fast.</p>
<h2>Good habits examiners look for</h2><ul><li>Scan the pavements as you approach — not just the crossing.</li><li>Slow down early; don't brake hard at the line.</li><li>Don't wave people across — you can't see what's coming the other way.</li><li>Don't stop on the zig-zags or overtake near the crossing.</li><li>Keep the crossing clear in queues.</li></ul>
<p>More: <a href="road-markings-solihull-learner-guide.html">road markings</a> · <a href="a34-stratford-road-shirley.html">A34 Stratford Road</a> · <a href="solihull-town-centre-driving-guide.html">town centre</a>.</p>""",
                 [("What's the difference between a pelican and a puffin crossing?", "A pelican has a flashing amber phase; a puffin uses sensors and has no flashing amber."),
                  ("Should I wave pedestrians across?", "No — you can't be sure the other lane will stop.")],
                 ["hc_road", "hc_marks"]))
    out.append(P("roundabouts-solihull-learner-guide", "Roundabouts", "Roundabouts in Solihull: from mini to motorway junctions",
                 "Roundabouts Solihull | Mini, Multi-Lane & Signalled | SQ Driving School",
                 "Solihull's roundabouts for learners: estate mini-roundabouts, multi-lane roundabouts on the A34, signalled M42 junction roundabouts and Stonebridge Island — lanes, signals and observation.",
                 [("Right", "give way to traffic from your right"), ("Left lane", "usually first exit"), ("Signals", "on big junctions"), ("#1", "fault: observation at junctions")],
                 ["Give way to traffic from the right unless signs or lights say otherwise.", "Choose your lane from the signs and arrows early.", "Signal left after the exit before yours.", "Check mirrors before you leave."],
                 """<p class="lead">Observation at junctions — roundabouts included — is the top reason learners fail, and Solihull has every kind of roundabout. Here's the progression we follow.</p>
<h2>1. Mini-roundabouts</h2><p>Estate roads in Monkspath, Hillfield, Chelmsley Wood and Lyndon have them. Give way to the right, go round the painted circle where you can, and signal clearly. Two mini-roundabouts close together count as separate junctions.</p>
<h2>2. Single-lane roundabouts</h2><p>Village edges and estate distributors. Plan your exit, signal, check your left mirror before leaving.</p>
<h2>3. Multi-lane roundabouts</h2><p>On the A34 and A45. Read the lane signs early: usually left lane for left and often straight on, right lane for right — but always follow the arrows.</p>
<h2>4. Signalled roundabouts</h2><p>The big M42 junction roundabouts have traffic lights on the circle. Treat each set as a junction, stay in your lane, and watch for traffic lights on the roundabout itself. See <a href="m42-junctions-3a-4-5-6-solihull.html">M42 junctions</a>.</p>
<h2>5. Stonebridge Island and the new HS2 roundabout</h2><p>Busy, fast and recently changed — our <a href="stonebridge-island-a446-hs2-roundabout.html">Stonebridge guide</a> covers it.</p>
<h2>The usual mistakes</h2><ul><li>Not looking right early enough, then stopping when it was clear (or going when it wasn't).</li><li>Wrong lane on approach.</li><li>No mirror check before leaving.</li><li>Signalling left too early on a roundabout with exits close together.</li></ul>""",
                 [("Which lane do I use on a Solihull roundabout?", "Follow the signs and lane arrows. Usually left lane for the first exit, right lane for exits past 12 o'clock — but road markings always win."),
                  ("Do I always give way to the right?", "Yes, unless road markings, signs or lights tell you otherwise.")],
                 ["hc_road", "faults", "faults2", "m42"]))
    out.append(P("hardest-and-easiest-roads-solihull-learners", "Hard & easy roads", "The good and the hard: Solihull roads for learners",
                 "Hardest & Easiest Roads in Solihull for Learner Drivers | SQ Driving School",
                 "The good and bad of Solihull's roads for learners: the calm places to start, and the junctions, lanes and roundabouts that catch people out on test — matched to DVSA's most common faults.",
                 [("#1", "fault: junction observation"), ("7", "test centres"), ("13", "road guides"), (str(len(SECTORS)), "postcode guides")],
                 ["Start on quiet estate and village roads.", "Build up to the A34, A41 and A45.", "Junctions and roundabouts cause the most fails.", "Practise the hard bits until they're boring."],
                 """<p class="lead">Every learner has good days and bad days on the road. These are the places in and around Solihull that make learning easier — and the ones that catch people out — matched to the faults DVSA records most.</p>
<h2>The good: where learning feels easy</h2><ul>
<li><b>Dorridge, Monkspath and Cheswick Green</b> — quiet residential roads for first lessons. <a href="driving-lessons-dorridge.html">Dorridge</a> · <a href="driving-lessons-monkspath.html">Monkspath</a></li>
<li><b>Village lanes around Berkswell, Hampton-in-Arden and Hockley Heath</b> — real country driving. <a href="knowle-dorridge-and-village-speed-limits.html">Village limits</a></li>
<li><b>Estate roads in Chelmsley Wood and Lyndon</b> — clutch control and manoeuvres.</li>
<li><b>Flat ground</b> — Solihull is mostly flat, which is kind to beginners (we have to look harder for hill starts).</li></ul>
<h2>The hard: what catches people out</h2>
<div class="table-wrap"><table><thead><tr><th>DVSA fault</th><th>Where Solihull learners meet it</th><th>Guide</th></tr></thead><tbody>
<tr><td>Observation at junctions</td><td>Side roads off the A34 in Shirley; emerging onto the A41 in Olton</td><td><a href="a34-stratford-road-shirley.html">A34</a></td></tr>
<tr><td>Mirrors when changing direction</td><td>Leaving multi-lane roundabouts; lane changes on the A45</td><td><a href="a45-coventry-road-airport-nec.html">A45</a></td></tr>
<tr><td>Turning right at junctions</td><td>Right turns across two lanes on Warwick Road and Stratford Road</td><td><a href="a41-warwick-road-olton-solihull.html">A41</a></td></tr>
<tr><td>Response to traffic lights</td><td>Signalled roundabouts at the M42 junctions; Blossomfield Road signals</td><td><a href="blossomfield-road-junction-signals.html">Blossomfield</a></td></tr>
<tr><td>Response to road markings and signs</td><td>Bus lanes on Lode Lane; lane arrows in the town centre</td><td><a href="lode-lane-hobs-moat-road-bus-lanes.html">Lode Lane</a></td></tr>
<tr><td>Positioning in normal driving</td><td>Dual carriageways like Damson Parkway and the A45 — don't sit in lane two</td><td><a href="roundabouts-solihull-learner-guide.html">Roundabouts</a></td></tr>
<tr><td>Moving off safely</td><td>Pulling away from parked cars on busy residential streets</td><td><a href="what-happens-on-a-driving-lesson-solihull.html">Lessons</a></td></tr>
<tr><td>Control while reverse parking</td><td>Test centre car parks and busy retail parks</td><td><a href="car-parks-solihull-learner-guide.html">Car parks</a></td></tr>
</tbody></table></div>
<p class="note">Fault categories are from DVSA's published reasons for failing; their order changes slightly from year to year. Places are where these situations come up, not quotes from learners.</p>
<h2>Fast-changing roads</h2><p>HS2 works on the A452 and around Stonebridge, and new layouts near the airport, mean what you practised last month may have changed. See <a href="stonebridge-island-a446-hs2-roundabout.html">Stonebridge</a> and <a href="birmingham-airport-roads-and-drop-off.html">airport roads</a>.</p>""",
                 [("What's the hardest part of driving in Solihull for learners?", "Busy junctions and multi-lane roundabouts on the A34, A41 and A45 — and the signalled M42 junctions."),
                  ("Where's best for a first driving lesson in Solihull?", "Quiet residential roads such as Dorridge, Monkspath or Cheswick Green.")],
                 ["faults", "faults2", "during", "pr_shirley"]))
    return out


def road_az():
    idx = {}
    for code, v in SECTORS.items():
        for r in v[2]:
            if "lanes" in r or "roads" in r:
                continue
            idx.setdefault(r, []).append(code)
    rows = "".join(f'<tr><td>{r}</td><td>{" ".join(f"<a href=\"{slug(c)}.html\">{c}</a>" for c in sorted(cs))}</td></tr>' for r, cs in sorted(idx.items(), key=lambda t: t[0].lower()))
    guides = chips([(f"{r['slug']}.html", r["short"]) for r in _RD.ROADS]) if SHORT else ""
    return P("solihull-road-names-a-z", "Road names A–Z", "Solihull road names A–Z for learner drivers", "Solihull Road Names A–Z | Learner Driver Guides by Road | SQ",
             f"An A–Z of {len(idx)} roads Solihull learners drive on — from Bills Lane to Widney Road — each linked to the postcode guides that cover it, plus our in-depth road guides.",
             [(str(len(idx)), "roads"), (str(len(SECTORS)), "postcode guides"), (str(len(SHORT)), "in-depth road guides"), ("A–Z", "find yours")],
             ["Find your road, then your postcode guide.", "Each guide shows the nearest test centre.", "In-depth guides for the major roads.", "Book from any page."],
             f"""<p class="lead">Looking for the roads near you? Find them here, then open the postcode guide for nearest test centres, fuel, parking and the good and hard parts.</p>
<h2>In-depth road guides</h2>{guides}
<h2>All roads</h2><div class="table-wrap"><table><thead><tr><th>Road</th><th>Postcode guides</th></tr></thead><tbody>{rows}</tbody></table></div>""",
             [("Which roads are on the Shirley driving test?", "DVSA doesn't publish routes, but the A34, Cranmore Boulevard, Monkspath and nearby estates come up often. See our Shirley test centre guide.")],
             ["pcdata", "hc_road"])


def all_pages():
    out = dict(sector_page(c) for c in SECTORS)
    out.update(dict([sectors_hub()]))
    out.update(dict(guides()))
    out.update(dict([road_az()]))
    return out


DIRECTORY = [("solihull-postcode-sectors.html", "All postcode sectors"), ("solihull-road-names-a-z.html", "Road names A–Z"),
             ("petrol-stations-solihull-learner-guide.html", "Petrol stations"), ("shell-garages-solihull-learner-drivers.html", "Shell garages"),
             ("car-parks-solihull-learner-guide.html", "Car parks"), ("shops-and-retail-parks-solihull-driving.html", "Shops & retail parks"),
             ("road-signs-solihull-test-routes.html", "Road signs"), ("road-markings-solihull-learner-guide.html", "Road markings"),
             ("pedestrian-crossings-solihull-learner-guide.html", "Pedestrian crossings"), ("roundabouts-solihull-learner-guide.html", "Roundabouts"),
             ("hardest-and-easiest-roads-solihull-learners.html", "Hardest & easiest roads")]
