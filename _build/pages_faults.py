"""Driving test faults — one practical, hand-written page per fault on the DVSA's list of the most common reasons
for failing the car test (test-faults/). Each page: what the examiner marks, what it looks like, why it happens,
drills to fix it, where it bites on Greater Manchester test routes, a self-check, booking and portal promo."""
from hub_shell import *
import pages_routes as RT

T10 = ("GOV.UK — Top 10 reasons for failing the driving test", "https://www.gov.uk/government/publications/top-10-reasons-for-failing-the-driving-test")
NEWS = ("GOV.UK — DVSA reveals top driving test faults", "https://www.gov.uk/government/news/dvsa-reveals-top-driving-test-faults-made-in-the-first-year-of-the-new-test")
HC = ("The Highway Code (GOV.UK)", "https://www.gov.uk/guidance/the-highway-code")
HCJ = ("Highway Code — Rules 170–183, road junctions", "https://www.gov.uk/guidance/the-highway-code/using-the-road-159-to-203")
TEST = ("GOV.UK — What happens during the driving test", "https://www.gov.uk/driving-test/what-happens-during-test")


def R(slug):
    c = next(x for x in RT.C if x["slug"] == slug)
    return f'<a href="{ROOT}test-routes/{slug}-driving-test-routes.html">{c["name"]}</a>'


F = [
    dict(slug="junction-observations", short="Junctions: observation", title="Observation at junctions",
         lead="Not looking properly at junctions has been the single most common reason for failing the driving test for years. It's rarely that learners don't look — it's that they look too late, too quickly, or without actually seeing what's coming.",
         marks="The examiner watches whether you take effective observation before emerging or turning: looking in all directions, at the right time, for long enough to judge speed and distance — and whether you then act on what you saw.",
         looks=["Emerging into the path of a vehicle you didn't see, or misjudged.", "Looking right but not left (or not re-checking right) at a crossroads.", "Arriving so fast that there's no time to look before you have to decide.", "Looking at a junction with parked cars blocking the view but not edging forward to see more.", "Missing a cyclist or motorcyclist — smaller and easier to lose behind a pillar or parked van."],
         why="Most junction faults start fifty metres earlier: approach speed. If you arrive at 20mph, your head has to do everything in a second. If you arrive at walking pace, there's time to look twice.",
         drills=[("Slow-down-early drill", "On lessons, call out 'junction ahead' and be at the speed you'd take the turn by the time you're three car lengths away."), ("Look-twice rule", "Right, left, right again — and at a restricted junction, a fourth look after you've crept forward."), ("Name what you see", "Say aloud 'blue van, 30mph, too close' — it forces your brain to process, not just glance."), ("Creep and peep", "At blind junctions, inch forward with clutch control until you can see, then decide.")],
         where=f"Narrow streets lined with parked cars around {R('cheetham-hill')} and {R('west-didsbury')}; busy town-centre junctions in {R('bury')} and {R('rochdale')}; lorries pulling out near {R('bredbury')} and {R('bolton')}.",
         check=["I'm at turning speed three car lengths before the line.", "I look right, left and right again before emerging.", "At a blind junction I creep forward before deciding.", "I check for cyclists and motorcyclists specifically.", "I don't pull out if I'd make anyone slow down."]),
    dict(slug="mirrors-changing-direction", short="Mirrors: changing direction", title="Using mirrors when changing direction",
         lead="Turning, changing lanes or moving out round a parked car without checking your mirrors — or checking them too late to act on — is consistently near the top of the DVSA's fail list.",
         marks="Before any change of direction you should check the relevant mirrors in good time, and act on what you see. Checking the mirror at the same moment as you turn the wheel doesn't count: it's too late to change your mind.",
         looks=["Signalling before checking the mirror.", "Moving out round a parked car without a door-mirror check.", "Changing lanes on a dual carriageway without a blind-spot check.", "Checking the interior mirror but not the door mirror on the side you're moving to."],
         why="Under pressure, learners compress the routine. MSM becomes SM or just M-as-you-steer. The routine has to be automatic before test day, or nerves will strip it out.",
         drills=[("Say MSM aloud", "Mirror, signal, manoeuvre — out loud, for every turn, for a whole lesson."), ("Mirror first, signal second", "Your instructor will cover the indicator stalk for a few turns if you keep signalling first."), ("Lane-change narration", "On a dual carriageway: 'interior, right door mirror, blind spot, signal, move'.")],
         where=f"Lane changes on Princess Road around {R('west-didsbury')}, Broadway near {R('chadderton')} and St Peter's Way at {R('bolton')}; the Peel Way roundabouts at {R('bury')}.",
         check=["I check mirrors before signalling — every time.", "I use the door mirror on the side I'm moving to.", "I check my blind spot before changing lanes.", "I check mirrors before slowing down, too."]),
    dict(slug="steering-control", short="Control: steering", title="Steering control",
         lead="Steering faults sound basic, but they're one of the most common reasons for failing — usually because the car ends up in the wrong place: cutting a corner, swinging wide, or clipping the kerb.",
         marks="The examiner looks for steering that's smooth and accurate: the car follows a safe path, you don't mount or hit the kerb, and you don't swing out or cut across lanes.",
         looks=["Turning too early and cutting a right-hand corner.", "Swinging wide before turning left.", "Mounting or hitting the kerb when pulling up or manoeuvring.", "Wandering in the lane on a straight road.", "Over-steering on roundabouts and drifting into the next lane."],
         why="Most steering errors are vision errors: the eyes look at the bonnet or the kerb instead of where the car needs to go. Speed is the other culprit — too fast into a turn leaves no time to steer smoothly.",
         drills=[("Look where you want to go", "Pick the exit point of the turn and look at it as you steer."), ("Pull-push practice", "Smooth pull-push steering on a quiet estate until it's automatic."), ("Slow into corners", "Brake before the bend, steer through it, gently accelerate out.")],
         where=f"Tight terraced streets in {R('rochdale')} and around Hag Fold near {R('atherton')}; mini-roundabouts on Tottington Road near {R('bury')}.",
         check=["My speed is set before I start turning.", "I look at the exit of the turn.", "I don't cut right-hand corners.", "I can pull up close to the kerb without touching it."]),
    dict(slug="turning-right-at-junctions", short="Junctions: turning right", title="Turning right at junctions",
         lead="Right turns are where you cross the path of oncoming traffic, so the examiner watches position, timing and judgement closely. It's a regular entry on the DVSA's list.",
         marks="Correct position (just left of the centre line, or in the right-turn lane), the correct point of turn, and judging gaps in oncoming traffic safely — without cutting the corner or waiting when it's clearly safe.",
         looks=["Staying too far left so traffic behind can't pass.", "Turning across an oncoming car that's closer than you thought.", "Cutting the corner and ending up on the wrong side of the new road.", "Not noticing pedestrians crossing the road you're turning into.", "Hesitating with a large, safe gap."],
         why="Judging the speed of oncoming traffic is hard for new drivers, and right turns combine positioning, observation and judgement all at once.",
         drills=[("Position check", "At every right turn, ask: could a car pass on my left?"), ("Gap judgement", "Count 'one thousand, two thousand' as an oncoming car passes a fixed point; learn what a safe gap feels like."), ("Pedestrian check", "Since 2022, give way to people crossing or waiting to cross the road you're turning into.")],
         where=f"Right turns at lights on Bury New Road near {R('cheetham-hill')}, Wilbraham Road near {R('west-didsbury')}, Walmersley Road at {R('bury')} and Manchester Road at {R('bolton')}.",
         check=["I position just left of the centre line.", "I turn at the correct point, not early.", "I give way to pedestrians in the road I'm entering.", "I go when a gap is clearly safe."]),
    dict(slug="moving-off-safely", short="Move off: safely", title="Moving off safely",
         lead="Moving off happens dozens of times on every test — after pulling up, at the start, after the manoeuvre. A single missed blind-spot check can be a serious fault.",
         marks="Before moving off you should check all around, including the blind spot over your shoulder, and only move when it's safe — signalling if it would help someone.",
         looks=["Pulling away without a right blind-spot check.", "Checking, then waiting, then moving off without re-checking.", "Moving off when a car or cyclist is approaching.", "Forgetting the left blind spot when moving off from the right side of the road."],
         why="Learners do POM perfectly at the start of the test and then skip it after the tenth pull-up because it feels routine.",
         drills=[("POM every time", "Prepare, Observe, Move — every single time the car is stationary at the kerb."), ("Re-check rule", "If you've waited more than a couple of seconds, look again before you go."), ("Pull-up practice", "A lesson of repeated pull-ups and move-offs on different roads.")],
         where=f"Busy roads right outside the centres — Weston Street at {R('bolton')}, Lingard Lane at {R('bredbury')}, Cross Street at {R('sale')}.",
         check=["I check my right blind spot before moving off.", "I re-check if I've waited.", "I signal only if it helps someone.", "I never move off if it would make anyone slow down."]),
    dict(slug="traffic-lights", short="Response to signals: traffic lights", title="Responding to traffic lights",
         lead="Traffic lights are simple — until there are three sets in 200 metres, a filter arrow, a box junction and a bus lane. Responding wrongly to lights is a regular DVSA top-10 fault.",
         marks="Stopping at red, not going on amber when you could stop safely, moving when green only if it's safe, obeying filter arrows, and stopping at the first white line where there's an advanced stop line for cyclists.",
         looks=["Going through an amber when you could have stopped.", "Stopping across the cyclists' box at an advanced stop line.", "Moving on green without checking the junction is clear.", "Missing a filter arrow, or following one meant for another lane.", "Waiting at a green light for no reason."],
         why="Learners either brake too hard for every amber or speed up to 'make it'. The fix is approaching at a speed where the decision is easy.",
         drills=[("Stale green thinking", "If a green has been showing for a while, expect it to change — be ready to stop."), ("Point of no return", "Pick the point where you'd go if it turned amber now. Before it: stop. After it: go."), ("Lane-arrow reading", "Read the lane arrows and filter lights well before the stop line.")],
         where=f"Light-heavy corridors like Princess Road and Barlow Moor Road near {R('west-didsbury')}, Edinburgh Way at {R('rochdale')} and Manchester Road at {R('bolton')}.",
         check=["I stop at amber unless stopping would be unsafe.", "I stop at the first line at advanced stop lines.", "I check the junction is clear before moving on green.", "I read filter arrows for my lane only."]),
    dict(slug="positioning-normal-driving", short="Positioning: normal driving", title="Positioning during normal driving",
         lead="Driving too close to the kerb, too near the middle of the road, or straddling lanes — positioning faults are less dramatic than junction faults but just as likely to appear on a DVSA marking sheet.",
         marks="Keeping a safe, sensible position: normally about a metre from the kerb, in the centre of your lane on multi-lane roads, and following lane markings.",
         looks=["Hugging the kerb so you'll hit drains and gutters and can't see ahead.", "Drifting towards the centre line on bends.", "Straddling two lanes on a wide road.", "Staying in the right-hand lane of a dual carriageway after overtaking."],
         why="Learners often don't know where the car is on the road. Reference points — where the kerb appears in the windscreen — fix it fast.",
         drills=[("Reference points", "Learn where the kerb and centre line appear from the driver's seat at 1 metre."), ("Lane-centre focus", "Look far ahead down the middle of your lane, not at the line next to you."), ("Keep left", "After overtaking, return to the left lane when it's safe.")],
         where=f"Dual carriageways like Broadway near {R('chadderton')} and St Peter's Way near {R('bolton')}; long residential roads around {R('sale')}.",
         check=["I'm about a metre from the kerb in normal driving.", "I stay centred in my lane on multi-lane roads.", "I return to the left lane after overtaking.", "I follow lane markings at junctions."]),
    dict(slug="traffic-signs", short="Response to signals: traffic signs", title="Responding to traffic signs",
         lead="No entry, no right turn, speed limits, bus lanes, give way — missing or misreading a sign is a common reason for failing, especially during independent driving.",
         marks="Noticing signs in good time and responding correctly: obeying orders (circles), reacting to warnings (triangles), and using direction signs to choose a lane early.",
         looks=["Missing a speed-limit change.", "Entering a bus lane during its hours of operation.", "Turning where a 'no right turn' sign applies.", "Choosing the wrong lane because you read the direction sign too late."],
         why="Signs are easy to miss when you're concentrating on traffic. Scanning far ahead and talking signs through on lessons builds the habit.",
         drills=[("Sign spotting", "Name every sign aloud on one lesson — you'll be surprised how many you were missing."), ("Bus-lane rule", "Read the times on the blue sign every time."), ("Speed-limit clues", "Street lights usually mean 30 unless signs say otherwise.")],
         where=f"Bus lanes and speed changes on Washway Road near {R('sale')}; one-way systems in {R('rochdale')} and {R('chadderton')}.",
         check=["I notice speed-limit changes before the sign.", "I check bus-lane times.", "I read direction signs early enough to change lanes calmly.", "I know what circles, triangles and rectangles mean."]),
    dict(slug="moving-off-control", short="Move off: control", title="Control when moving off",
         lead="Stalling, rolling back on a hill, or kangarooing away from the kerb. A single stall isn't usually serious — but rolling back towards a car behind is.",
         marks="Moving off smoothly and under control, on the flat, uphill, downhill and at an angle from behind a parked car, using the correct gear and without rolling back.",
         looks=["Rolling back on a hill start.", "Stalling repeatedly.", "Moving off in the wrong gear.", "Too much gas and a lurch forward, or releasing the parking brake before you're ready."],
         why="Biting-point control isn't consistent yet — especially under test nerves, on a slope you haven't practised, or in a car with a different clutch feel.",
         drills=[("Hill-start ladder", "Start on gentle slopes and work up to the steepest street you can find."), ("Stall recovery", "Parking brake, neutral, restart, POM, go — practise it so a stall doesn't rattle you."), ("Consider automatic", "No clutch, no stalls. See our manual vs automatic guide.")],
         where=f"Hilly streets in {R('rochdale')} and Romiley on routes from {R('bredbury')}.",
         check=["I can hold the car on the biting point on a hill.", "I don't roll back when moving off uphill.", "I recover calmly from a stall.", "I move off in first (or second on a downhill if appropriate)."]),
    dict(slug="road-markings", short="Response to signals: road markings", title="Responding to road markings",
         lead="Lane arrows, box junctions, hatched areas, give-way lines and bus lanes are all painted on the road — and missing them is a regular entry on the DVSA's list.",
         marks="Following lane markings and arrows, not stopping in yellow boxes unless allowed, not crossing solid white lines, and stopping at stop and give-way lines.",
         looks=["Following the wrong lane arrow on a roundabout approach.", "Stopping in a yellow box junction when your exit isn't clear.", "Driving over hatched markings with a solid border.", "Ignoring 'KEEP CLEAR' markings."],
         why="Markings are often half-worn, covered by traffic or appear late. Reading the road far ahead is the fix.",
         drills=[("Read the road", "Look 10–15 seconds ahead and say which lane the arrows want you in."), ("Box junction rule", "Don't enter unless your exit is clear — except when turning right and only blocked by oncoming traffic."), ("Roundabout lanes", "Learn the lanes for each exit at the big roundabouts near your test centre.")],
         where=f"Multi-lane roundabouts at Queensway near {R('rochdale')}, Peel Way near {R('bury')} and Featherstall Road near {R('chadderton')}.",
         check=["I follow lane arrows on approach.", "I don't stop in yellow boxes.", "I stop at stop lines and give-way lines.", "I don't cross solid white lines except where allowed."]),
    dict(slug="safe-reasonable-speed", short="Speed: safe and reasonable", title="Driving at a safe and reasonable speed",
         lead="Not driving at a safe and reasonable speed for the road and conditions was added to the DVSA's list in 2024. It isn't only about speeding — driving well under the limit when it's safe to go faster can also be a fault.",
         marks="Keeping to speed limits, adjusting for conditions (parked cars, pedestrians, weather, schools), and making progress when it's safe — not holding up traffic without reason.",
         looks=["Doing 30 past a row of parked cars and a school entrance.", "Missing a drop to 20mph.", "Doing 40 on a clear 70mph dual carriageway.", "Approaching hazards too fast to stop in the distance you can see."],
         why="New drivers judge speed by the sign rather than by what they can see. A safe speed is one where you can stop in the distance you can see to be clear.",
         drills=[("Stopping distance check", "Use our stopping distance calculator, then ask on every road: could I stop in the space I can see?"), ("Progress practice", "On a clear dual carriageway, build up to the limit smoothly."), ("20mph zones", "Learn where the 20mph zones are on your lessons.")],
         where=f"20mph residential zones across Manchester near {R('west-didsbury')} and {R('cheetham-hill')}; dual carriageways near {R('chadderton')} and {R('bolton')}.",
         check=["I can stop in the distance I can see to be clear.", "I slow down for parked cars, schools and pedestrians.", "I keep up with traffic on clear, fast roads.", "I notice every speed-limit change."]),
]


def fault_page(f, idx):
    path = f"test-faults/{f['slug']}.html"
    looks = "".join(f"<li>{x}</li>" for x in f["looks"])
    drills = "".join(f'<li data-n="{i + 1}"><h4>{h}</h4><p>{p}</p></li>' for i, (h, p) in enumerate(f["drills"]))
    checks = "".join(f'<li><label><input type="checkbox"> {x}</label></li>' for x in f["check"])
    others = [x for x in F if x["slug"] != f["slug"]]
    body = f"""
<p class="lead">{f['lead']}</p>
<h2>What the examiner is looking for</h2>
<p>{f['marks']}</p>
<div class="callout callout--info">On the DVSA marking sheet, a <b>driving fault</b> is minor (up to 15 allowed). A <b>serious fault</b> is potentially dangerous, and a <b>dangerous fault</b> involves actual danger — one of either means you fail. The same mistake can be any of the three depending on what else was happening.</div>
<h2>What it looks like on test</h2>
<ul>{looks}</ul>
<h2>Why it happens</h2>
<p>{f['why']}</p>
<h2>How to fix it: drills we use</h2>
<ol class="rx-steps">{drills}</ol>
<h2>Where it catches learners in Greater Manchester</h2>
<p>{f['where']} Our <a href="{ROOT}test-routes.html">test-route guides</a> list the exact roads.</p>
<h2>Self-check before your test</h2>
<div class="rx-tool" data-reveal="up"><div class="rx-tool__head"><div class="card__icon">{icon('check')}</div><div><h3>Can you tick all of these?</h3><p>Be honest — if not, tell your instructor and practise it on your next lesson.</p></div></div><ul class="check" style="list-style:none;padding:0">{checks}</ul></div>
<p>In the DriveSQ Student Portal your instructor marks "{f['short']}" as its own skill after each lesson, so you can watch it move from "introduced" to "independent" before you book.</p>"""
    faqs = [(f"Is {f['title'].lower()} a common reason for failing the driving test?", "Yes. It appears on the DVSA's published list of the most common reasons for failing the car driving test."),
            (f"Is a {f['short'].lower()} fault always a fail?", "No. It depends on seriousness: a minor driving fault isn't a fail on its own, but a serious or dangerous fault is."),
            (f"How do I stop making {f['title'].lower()} mistakes?", f"{f['drills'][0][0]}: {f['drills'][0][1]}"),
            ("How many minor faults can you have and still pass?", "Up to 15 driving faults, with no serious or dangerous faults.")]
    related = [(f"test-faults/{x['slug']}.html", "Test fault", x["title"], x["lead"][:110].rsplit(" ", 1)[0] + "…") for x in (others[idx % len(others)], others[(idx + 3) % len(others)])]
    related.append(("knowledge/why-learners-fail-the-driving-test.html", "Guide", "Why learners fail the driving test", "An overview of the most common faults."))
    return shell(path, f"{f['title']}: Driving Test Fault Explained & Fixed | SQ Driving School", "Test faults", [("Test faults", "test-faults.html"), (f["short"], path)],
                 f"Driving test fault: {f['title'].lower()}", f"Why '{f['short']}' is one of the most common reasons for failing the UK driving test, what the examiner looks for, how to fix it, and where it catches learners in Greater Manchester.",
                 [("Top 10", "DVSA fail reason"), ("15", "driving faults allowed"), ("1", "serious fault = fail"), (str(len(f["drills"])), "drills to fix it")],
                 [f"'{f['short']}' is on the DVSA's list of the most common reasons for failing.", f["why"].split(". ")[0] + ".", f"Drill: {f['drills'][0][0]}.", "Your DriveSQ Student Portal tracks this skill lesson by lesson."],
                 body, faqs, [T10, NEWS, TEST, HC] + ([HCJ] if "junction" in f["slug"] else []), related, side_title="Fix it with SQ")


def hub():
    cards = [(f"test-faults/{f['slug']}.html", "DVSA top-10 fault", f["title"], f["lead"][:120].rsplit(" ", 1)[0] + "…", "target") for f in F]
    intro = f"""<p class="lead" data-reveal="up">The DVSA publishes the most common reasons people fail the car driving test. Observation at junctions has topped the list for years. Here's every fault on the list, explained properly: what the examiner marks, what it looks like, why it happens, drills to fix it, and where it catches learners on Greater Manchester's test routes.</p>
<div class="callout callout--info" data-reveal="up">The DVSA updates the list each year — its latest update covers tests from April 2024 to March 2025 and added "not driving at a safe and reasonable speed". See the <a href="{T10[1]}" target="_blank" rel="noopener">official list on GOV.UK</a> for the current order.</div>"""
    return hub_page("test-faults.html", "Top Reasons for Failing the Driving Test — Every Fault Fixed | SQ", "Test faults",
                    "Why people fail the driving test.", "Every fault on the DVSA's list of top reasons for failing the car driving test — explained, with drills to fix each one and where it happens in Greater Manchester.",
                    cards, intro, [(str(len(F)), "faults explained"), ("15", "minor faults allowed"), ("1", "serious fault fails"), ("9", "test centres linked")])


def all_pages():
    out = {"test-faults.html": hub()}
    for i, f in enumerate(F):
        out[f"test-faults/{f['slug']}.html"] = fault_page(f, i)
    return out
