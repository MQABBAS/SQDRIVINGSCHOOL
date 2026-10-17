# Learner facts for each district that other driving school sites don't publish.
#  - coords: postcode-district centre (postcodes.io), used to work out distance to the city centre
#  - ratings: SQ instructors' own 1–5 rating of what learners face here (5 = most demanding)
#  - best: when our instructors find it easiest to practise
#  - trams / events / hills: quick yes/no facts for the area
import math

PICCADILLY = (53.4810, -2.2366)  # Piccadilly Gardens

FACTS = {
    "M1":  {"coords": (53.4775, -2.2361), "ratings": {"Traffic": 5, "Junctions": 5, "Trams": 5, "Cyclists & pedestrians": 5, "Hills": 1}, "best": "Before 8am or after 7pm on weekdays; early Sunday mornings", "trams": True, "events": "Concerts and city-centre events", "hills": False},
    "M2":  {"coords": (53.4804, -2.2445), "ratings": {"Traffic": 5, "Junctions": 5, "Trams": 5, "Cyclists & pedestrians": 5, "Hills": 1}, "best": "Early mornings before office traffic, or weekends", "trams": True, "events": "Christmas markets and civic events in Albert Square", "hills": False},
    "M3":  {"coords": (53.4838, -2.2529), "ratings": {"Traffic": 5, "Junctions": 5, "Trams": 4, "Cyclists & pedestrians": 5, "Hills": 1}, "best": "Weekday mornings after 9:30am; Sunday mornings", "trams": True, "events": "Weekend nightlife around Deansgate", "hills": False},
    "M4":  {"coords": (53.4851, -2.2301), "ratings": {"Traffic": 4, "Junctions": 4, "Trams": 3, "Cyclists & pedestrians": 5, "Hills": 1}, "best": "Weekday mornings; streets get busy from late afternoon", "trams": True, "events": "Northern Quarter nightlife", "hills": False},
    "M8":  {"coords": (53.5087, -2.2401), "ratings": {"Traffic": 4, "Junctions": 4, "Trams": 2, "Cyclists & pedestrians": 4, "Hills": 2}, "best": "Mid-morning and early afternoon, avoiding school runs", "trams": True, "events": "Busy shopping on Cheetham Hill Road at weekends", "hills": False},
    "M9":  {"coords": (53.5220, -2.2139), "ratings": {"Traffic": 3, "Junctions": 3, "Trams": 1, "Cyclists & pedestrians": 3, "Hills": 4}, "best": "Mid-morning on weekdays; quiet on Sunday mornings", "trams": False, "events": "Heaton Park events", "hills": True},
    "M11": {"coords": (53.4788, -2.1810), "ratings": {"Traffic": 3, "Junctions": 4, "Trams": 4, "Cyclists & pedestrians": 3, "Hills": 1}, "best": "Any non-event day; avoid match and concert days", "trams": True, "events": "Etihad Stadium match and concert days", "hills": False},
    "M12": {"coords": (53.4644, -2.2019), "ratings": {"Traffic": 4, "Junctions": 4, "Trams": 1, "Cyclists & pedestrians": 4, "Hills": 1}, "best": "Mid-morning; Longsight is busiest late afternoon and Saturdays", "trams": False, "events": "Longsight Market days", "hills": False},
    "M13": {"coords": (53.4605, -2.2155), "ratings": {"Traffic": 4, "Junctions": 4, "Trams": 1, "Cyclists & pedestrians": 5, "Hills": 1}, "best": "University holidays and weekday mornings", "trams": False, "events": "Start of term and graduation weeks", "hills": False},
    "M14": {"coords": (53.4486, -2.2259), "ratings": {"Traffic": 4, "Junctions": 3, "Trams": 1, "Cyclists & pedestrians": 5, "Hills": 1}, "best": "Weekday mornings; Wilmslow Road is busiest in the evening", "trams": False, "events": "Freshers' week and Platt Fields events", "hills": False},
    "M15": {"coords": (53.4677, -2.2517), "ratings": {"Traffic": 4, "Junctions": 5, "Trams": 2, "Cyclists & pedestrians": 4, "Hills": 1}, "best": "Mid-morning and early afternoon", "trams": True, "events": "City-centre event traffic on the Mancunian Way", "hills": False},
    "M16": {"coords": (53.4552, -2.2647), "ratings": {"Traffic": 3, "Junctions": 4, "Trams": 3, "Cyclists & pedestrians": 3, "Hills": 1}, "best": "Non-match days; Whalley Range is quiet most mornings", "trams": True, "events": "Old Trafford football and cricket days", "hills": False},
    "M17": {"coords": (53.4680, -2.3197), "ratings": {"Traffic": 4, "Junctions": 4, "Trams": 2, "Cyclists & pedestrians": 1, "Hills": 1}, "best": "Weekends for the industrial estate; weekdays for the Trafford Centre", "trams": True, "events": "Trafford Centre at weekends and in December", "hills": False},
    "M18": {"coords": (53.4612, -2.1708), "ratings": {"Traffic": 3, "Junctions": 3, "Trams": 1, "Cyclists & pedestrians": 3, "Hills": 2}, "best": "Mid-morning, avoiding 8:30am and 3pm school runs", "trams": False, "events": "Evening events at Belle Vue sports venues", "hills": False},
    "M19": {"coords": (53.4364, -2.1962), "ratings": {"Traffic": 3, "Junctions": 3, "Trams": 1, "Cyclists & pedestrians": 3, "Hills": 1}, "best": "Weekday mornings after 9:30am; Stockport Road is busiest at rush hour", "trams": False, "events": "Levenshulme Market days", "hills": False},
    "M20": {"coords": (53.4242, -2.2327), "ratings": {"Traffic": 3, "Junctions": 3, "Trams": 2, "Cyclists & pedestrians": 4, "Hills": 1}, "best": "Weekday mornings; Didsbury village is busiest on Saturdays", "trams": True, "events": "Weekend village traffic in Didsbury", "hills": False},
    "M21": {"coords": (53.4380, -2.2729), "ratings": {"Traffic": 3, "Junctions": 3, "Trams": 2, "Cyclists & pedestrians": 5, "Hills": 1}, "best": "Weekday mornings; Beech Road is busy at weekends", "trams": True, "events": "Weekend markets and festivals", "hills": False},
    "M22": {"coords": (53.3858, -2.2601), "ratings": {"Traffic": 2, "Junctions": 3, "Trams": 2, "Cyclists & pedestrians": 2, "Hills": 1}, "best": "Most of the day — wide roads and lighter traffic", "trams": True, "events": "Airport traffic at peak holiday times", "hills": False},
    "M23": {"coords": (53.3996, -2.2888), "ratings": {"Traffic": 2, "Junctions": 2, "Trams": 3, "Cyclists & pedestrians": 2, "Hills": 1}, "best": "Most of the day; the hospital area is busiest at visiting times", "trams": True, "events": "Wythenshawe Hospital visiting times", "hills": False},
    "M25": {"coords": (53.5283, -2.2758), "ratings": {"Traffic": 3, "Junctions": 3, "Trams": 1, "Cyclists & pedestrians": 3, "Hills": 2}, "best": "Weekday mornings; the village is busy on Saturdays", "trams": True, "events": "Heaton Park concerts", "hills": True},
    "M40": {"coords": (53.5040, -2.1912), "ratings": {"Traffic": 3, "Junctions": 3, "Trams": 3, "Cyclists & pedestrians": 3, "Hills": 1}, "best": "Mid-morning and early afternoon", "trams": True, "events": "Etihad match-day traffic along nearby routes", "hills": False},
    "WA14": {"coords": (53.3879, -2.3610), "ratings": {"Traffic": 3, "Junctions": 3, "Trams": 1, "Cyclists & pedestrians": 3, "Hills": 3}, "best": "Weekday mornings; the town centre is busiest on Saturdays", "trams": True, "events": "Busy town centre and market at weekends", "hills": True},
    "WA15": {"coords": (53.3844, -2.3255), "ratings": {"Traffic": 2, "Junctions": 2, "Trams": 1, "Cyclists & pedestrians": 2, "Hills": 1}, "best": "Most of the day — quiet residential roads", "trams": True, "events": "Airport holiday traffic", "hills": False},
}


def miles_to_centre(code):
    (a, b), (c, d) = FACTS[code]["coords"], PICCADILLY
    r = 3958.8
    p1, p2 = math.radians(a), math.radians(c)
    dl, dp = math.radians(d - b), math.radians(c - a)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def score(code):
    """SQ Learner Challenge score out of 10 — average of the ratings, weighted to traffic and junctions."""
    r = FACTS[code]["ratings"]
    w = {"Traffic": 1.3, "Junctions": 1.3, "Trams": 0.8, "Cyclists & pedestrians": 1.0, "Hills": 0.6}
    s = sum(r[k] * w[k] for k in r) / sum(w[k] for k in r)
    return round(s * 2, 1)
