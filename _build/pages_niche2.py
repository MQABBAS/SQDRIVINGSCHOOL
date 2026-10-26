"""Batch 5: famous questions and niche searches the site didn't answer yet — Ramadan lessons, driving at 16 on PIP,
theory test languages and BSL, L and P plates, wrong turns on the test, serious and dangerous faults, blind spots,
country roads and horses, fog and headlights, cancelled tests, the cockpit drill, manual vs automatic after 2030,
and dash cams. Each guide pairs with a free DriveSQ tool or page, and those link back. Facts are from GOV.UK and the
Highway Code; where public sources disagree, the page says so rather than picking a number."""
from hub_shell import shell
import pages_solihull as SOL

DSQ = "https://www.drivesq.co.uk/"
G = {
    "prov": ("GOV.UK — Apply for your first provisional driving licence", "https://www.gov.uk/apply-first-provisional-driving-licence"),
    "lessons": ("GOV.UK — Driving lessons and learning to drive", "https://www.gov.uk/driving-lessons-learning-to-drive"),
    "supervise": ("GOV.UK — Supervising a learner driver", "https://www.gov.uk/supervise-learner-driver"),
    "lplate": ("GOV.UK — L plate sizes (statutory guidance)", "https://gov.uk/government/publications/l-plate-size-rules/l-plate-sizes"),
    "during": ("GOV.UK — Driving test: what happens during the test", "https://www.gov.uk/driving-test/what-happens-during-test"),
    "result": ("GOV.UK — Driving test: test result", "https://www.gov.uk/driving-test/test-result"),
    "ready": ("Ready to Pass (DVSA) — driving test video transcript", "https://readytopass.campaign.gov.uk/driving-test-video-transcript/"),
    "sdfl_ind": ("Safe Driving for Life — understanding the independent drive", "https://www.safedrivingforlife.info/blog/understanding-independent-drive"),
    "nid_ind": ("nidirect — Independent driving", "https://www.nidirect.gov.uk/articles/independent-driving"),
    "lang2014": ("GOV.UK — Foreign language driving tests end (2014)", "https://www.gov.uk/government/news/foreign-language-driving-tests-end"),
    "theory": ("GOV.UK — Theory test: cars", "https://www.gov.uk/theory-test"),
    "nid_lang": ("nidirect — Taking your theory test if you have special requirements (Northern Ireland)", "https://www.nidirect.gov.uk/articles/taking-your-theory-test-if-you-have-special-requirements"),
    "bsl": ("Limping Chicken — DVSA BSL service for theory test bookings (2025)", "https://limpingchicken.com/2025/08/27/the-dvsa-introduces-first-of-its-kind-government-service-for-bsl-users-taking-theory-tests/"),
    "mobility": ("Driving Mobility — provisional drivers", "https://drivingmobility.org.uk/assessments/provisional-drivers"),
    "hc_road": ("GOV.UK — The Highway Code: using the road (159 to 203)", "https://www.gov.uk/guidance/the-highway-code/using-the-road-159-to-203"),
    "hc_vuln": ("GOV.UK — The Highway Code: road users requiring extra care (204 to 225)", "https://www.gov.uk/guidance/the-highway-code/road-users-requiring-extra-care-204-to-225"),
    "hc_weather": ("GOV.UK — The Highway Code: driving in adverse weather (226 to 237)", "https://www.gov.uk/guidance/the-highway-code/driving-in-adverse-weather-conditions-226-to-237"),
    "hc_lights": ("GOV.UK — The Highway Code: general rules, lights (113 to 116)", "https://www.gov.uk/guidance/the-highway-code/general-rules-techniques-and-advice-for-all-drivers-and-riders-103-to-158"),
    "hc_ped": ("GOV.UK — The Highway Code: introduction and hierarchy of road users", "https://www.gov.uk/guidance/the-highway-code/introduction"),
    "cancel_form": ("GOV.UK — Apply for out-of-pocket expenses for a cancelled test (DVSA form)", "https://assets.publishing.service.gov.uk/media/65f8066a50397e0011c755f7/apply-cancelled-driving-test-expenses.pdf"),
    "cancel_foi": ("GOV.UK — Out-of-pocket expenses awarded for short-notice cancellations (FOI)", "https://gov.uk/government/publications/out-of-pocket-expenses-awarded-for-short-notice-driving-test-cancellations"),
    "cancel_pmf": ("PassMeFast — how to claim for a cancelled test", "https://passmefast.co.uk/resources/get-test-ready/practical-test/how-to-make-claim-test-cancellation"),
    "change": ("GOV.UK — Change your driving test appointment", "https://www.gov.uk/change-driving-test"),
    "zev": ("Fleet News — changes to the ZEV mandate (April 2025)", "https://www.fleetnews.co.uk/news/changes-to-zev-mandate-sale-of-hybrid-cars-and-vans-to-be-allowed"),
    "zev2": ("Electrifying.com — 2030 petrol and diesel ban explained", "https://www.electrifying.com/blog/article/government-confirms-tweaks-to-petrol-and-diesel-cars-ban-here-s-everything-you-need-to-know"),
    "licence_auto": ("GOV.UK — Driving licence categories", "https://www.gov.uk/driving-licence-categories"),
    "film": ("GOV.UK — Filming or recording driving tests (DVSA policy)", "https://www.gov.uk/government/publications/filming-or-recording-driving-tests"),
    "tired": ("GOV.UK — The Highway Code: rules for drivers, fitness to drive (90 to 102)", "https://www.gov.uk/guidance/the-highway-code/rules-for-drivers-and-motorcyclists-89-to-102"),
    "faults": ("Theory Test Pro — DVSA's top reasons learners fail", "https://www.theorytestpro.co.uk/posts/top-10-reasons-why-learners-failed-their-driving-test-in-2023/"),
}
SIDE = SOL.SIDE if hasattr(SOL, "SIDE") else None


def tool(href, label):
    return f'<div class="callout"><b>Free DriveSQ tool:</b> <a href="{DSQ}{href}" target="_blank" rel="noopener">{label} →</a></div>'


def local(man, sol):
    return f'<h2>In Manchester and Solihull</h2><p><b>Manchester:</b> {man}</p><p><b>Solihull:</b> {sol}</p>'


GUIDES = [
    ("ramadan-driving-lessons-fasting", "Driving lessons during Ramadan", "Learning to drive while fasting in Ramadan: when to book lessons, staying alert, test timing and Eid — practical advice for Muslim learners in Manchester and Solihull.",
     [("Earlier", "lessons usually feel best"), ("Tired?", "say so and stop"), ("Rule 91", "Highway Code on tiredness"), ("Flexible", "times on request")],
     f"""<p class="lead">Lots of our learners fast during Ramadan and keep learning right through it. With a bit of planning it works well — the key is booking lessons for when you're sharpest, and being honest when you're not.</p>
<h2>When to book lessons</h2><ul><li><b>Mornings</b>, soon after suhoor, are when most fasting learners feel most alert.</li><li><b>Avoid the hour before iftar</b> — energy and concentration are lowest and roads are busy with people rushing home.</li><li><b>After iftar</b> works for some learners, especially in summer when the days are long; it's also good night-driving practice.</li><li><b>Shorter lessons</b> are fine for the month if two hours feels too long.</li></ul>
<h2>Staying safe</h2><p>The Highway Code (rule 91) says to make sure you're fit to drive and to stop and rest if you feel sleepy. Fasting can bring headaches, low energy and slower reactions — especially later in the day and in the first few days. Tell your instructor how you feel; we'll keep it to quiet roads or stop the lesson early.</p>
<h2>Booking your test during Ramadan</h2><ul><li>Choose a morning slot if you can.</li><li>Don't book a test for the day after Eid celebrations if you expect a late night.</li></ul>
<h2>Eid</h2><p>Let us know your Eid dates early so we can plan lessons around family time. We don't mind moving lessons with notice.</p>
{local("Lessons across Cheetham Hill, Longsight, Levenshulme, Rusholme and the rest of the city can be timed around suhoor and iftar.", "Lessons in Shirley, Olton, Chelmsley Wood and across the borough can be timed the same way.")}
{tool("solihull-learner-driver-lesson-plan.html", "Plan your lessons week by week")}""",
     [("Can I have driving lessons while fasting?", "Yes. Book morning lessons if you can, tell your instructor if you feel tired, and stop if you're not fit to drive."),
      ("Is it safe to take my driving test while fasting?", "Many people do. Choose a morning test, sleep well the night before and don't drive if you feel unwell or faint."),
      ("Can I move lessons around Eid?", "Yes — tell us your dates early.")], ["tired", "lessons"],
     [("guides/nervous-drivers.html", "Guide", "Nervous drivers", "Building confidence."), (DSQ + "urdu-driving-lessons-manchester.html", "DriveSQ", "Urdu-speaking lessons", "Manchester.")]),

    ("driving-at-16-pip-mobility", "Driving at 16 with PIP", "You can start driving a car at 16 if you get the enhanced rate of the mobility component of PIP. When to apply, what to declare, adapted cars and how lessons work.",
     [("15y 9m", "apply for provisional"), ("16", "start driving with enhanced PIP mobility"), ("17", "everyone else"), ("Free", "age checker tool")],
     f"""<p class="lead">Most people can't drive a car until they're 17. But if you get — or have applied for — the enhanced rate of the mobility component of Personal Independence Payment (PIP), you can start at 16.</p>
<h2>The rules</h2><ul><li>Anyone can apply for a provisional licence from 15 years and 9 months.</li><li>With the enhanced rate of PIP mobility, you can drive a car from your 16th birthday.</li><li>You can take your theory test once you're allowed to drive, so at 16 in this case.</li><li>Your supervisor has the same rules as for anyone: at least 21 and held a full licence for 3 years.</li></ul>
<h2>Declaring medical conditions</h2><p>When you apply, you must declare any medical condition that could affect your driving. DVLA may ask for more information or a medical report — it doesn't mean you can't drive. Check GOV.UK's list of conditions before you apply.</p>
<h2>Adapted cars and assessments</h2><p>Driving Mobility's centres assess what adaptations you might need (hand controls, steering aids, left-foot accelerators and more). An assessment before lessons can save time and money. Our cars are standard manual and automatic cars — tell us what you need and we'll be honest about whether we can teach you or point you to an instructor with an adapted car.</p>
<h2>Learning at 16</h2><p>Lessons work exactly like any other learner's. An automatic often makes sense, and starting a year early means no rush.</p>
{tool("solihull-driving-test-readiness-check.html", "Test readiness check")}<p>Work out your own dates with DriveSQ's <a href="{DSQ}learner-driver-age-checker.html" target="_blank" rel="noopener">learner age checker</a>.</p>""",
     [("Can you drive at 16 in the UK?", "Only if you get, or have applied for, the enhanced rate of the mobility component of PIP. Otherwise it's 17."),
      ("When can I apply for my provisional licence?", "From 15 years and 9 months."),
      ("Do I need an adapted car?", "It depends on your needs. A Driving Mobility assessment can tell you.")], ["prov", "mobility", "supervise"],
     [("driving-lessons-for-older-learners-manchester.html", "Lessons", "Older learners", "Never too late."), (DSQ + "disabled-driving-lessons-manchester.html", "DriveSQ", "Disabled driving lessons", "Manchester.")]),

    ("theory-test-languages-bsl-and-support", "Theory test languages, BSL and extra support", "The driving theory test in Great Britain is in English or Welsh — foreign-language voiceovers ended in 2014. What support you can get: BSL, voiceover, extra time and how to ask.",
     [("English", "or Welsh in Great Britain"), ("2014", "foreign voiceovers ended"), ("BSL", "available"), ("Extra time", "for reading difficulties")],
     """<p class="lead">"Can I take my theory test in Urdu / Polish / Arabic?" is one of the most common questions we get. In Great Britain the answer is no — but there is support, and lessons in your own language still help a lot.</p>
<h2>The rule in Great Britain</h2><p>Since 7 April 2014, DVSA theory tests in England, Scotland and Wales are in English or Welsh only. Before that, there were voiceovers in 19 other languages and interpreters were allowed; DVSA ended them to reduce fraud and because drivers need to read English road signs.</p>
<h2>Support you can ask for</h2><ul><li><b>English or Welsh voiceover</b> — if you have dyslexia or another reading difficulty.</li><li><b>Extra time</b> on the multiple-choice part — ask when you book; you may need evidence of your reading difficulty.</li><li><b>British Sign Language</b> — you can take the theory test with BSL video, and bring a BSL interpreter to the practical test.</li><li>Other needs (a separate room, breaks) — ask when you book.</li></ul>
<h2>Northern Ireland is different</h2><p>Northern Ireland's tests are run by DVA, which lists voiceover languages (including Arabic, Cantonese, Farsi, Polish, Portuguese and Turkish). That doesn't apply to tests in Great Britain.</p>
<h2>How we help if English isn't your first language</h2><ul><li>We explain the Highway Code in plain English, slowly, with real examples on the road.</li><li>Road signs are mostly symbols — we teach the shapes and colours first.</li><li>Practise with free mock tests in the DriveSQ Student Portal.</li></ul>""" + tool("solihull-theory-test-guide.html", "DriveSQ theory test guide") + """<p>DriveSQ also has pages for learners who want an <a href="https://www.drivesq.co.uk/urdu-driving-lessons-manchester.html" target="_blank" rel="noopener">Urdu-speaking</a>, <a href="https://www.drivesq.co.uk/punjabi-driving-lessons-manchester.html" target="_blank" rel="noopener">Punjabi-speaking</a> or <a href="https://www.drivesq.co.uk/polish-driving-instructor-manchester.html" target="_blank" rel="noopener">Polish-speaking</a> instructor in Manchester.</p>""",
     [("Can I take the theory test in another language?", "Not in Great Britain — only English or Welsh since April 2014. You can ask for BSL, an English or Welsh voiceover if you have a reading difficulty, and extra time."),
      ("Can I bring an interpreter to my driving test?", "Only a BSL interpreter. Other interpreters stopped being allowed in 2014."),
      ("Can I get extra time on the theory test?", "Yes, if you have a reading difficulty such as dyslexia — ask when you book.")], ["lang2014", "theory", "nid_lang", "bsl"],
     [("knowledge/theory-test-greater-manchester.html", "Knowledge", "Theory test in Greater Manchester", "Centres and tips."), ("knowledge/learning-to-drive-with-dyslexia-adhd-or-anxiety.html", "Knowledge", "Dyslexia, ADHD or anxiety", "Support that works.")]),

    ("l-plates-and-p-plates-rules", "L plates and P plates: the rules", "L plates must be shown front and back whenever a learner drives, and taken off or covered when they don't. P plates are optional. Sizes, magnetic plates, Wales's D plates and penalties.",
     [("Front & back", "L plates required"), ("Optional", "P plates"), ("Remove", "when no learner drives"), ("D plates", "allowed in Wales")],
     """<p class="lead">L plates are simple — until you're in the family car, a plate has blown off on the M60, or you've just passed and wonder about P plates.</p>
<h2>L plates</h2><ul><li>Any car driven by a learner must show red L plates, visible from the front and the back.</li><li>They must be the official size: a red L on a white background (GOV.UK publishes the exact measurements).</li><li>Take them off or cover them when the car isn't being driven by a learner — driving-school cars are the exception.</li><li>In Wales you can use red D plates, red L plates or both.</li><li>Not displaying L plates can lead to a fine and penalty points on your provisional licence. Sources quote different amounts, so we won't guess — just keep them on.</li></ul>
<h2>Magnetic plates and motorways</h2><p>Magnetic plates can fly off at speed and don't stick to every car. Motorway lessons must be with an approved driving instructor in a dual-control car — check plates are secure before every drive.</p>
<h2>P plates</h2><p>Green P plates are optional in Great Britain. Many new drivers use them for the first few months so other drivers give a little more space. Northern Ireland is different — R plates are required there for the first year.</p>
<h2>Don't forget the new driver rules</h2><p>For two years after passing, 6 penalty points cancels your licence — see our <a href="../knowledge/after-you-pass-new-driver-guide.html">new driver guide</a>.</p>""" + tool("penalty-points-new-drivers.html", "DriveSQ: penalty points for new drivers"),
     [("Do L plates have to be on the front and back?", "Yes — they must be visible from both."),
      ("Do I have to use P plates after passing?", "No, they're optional in Great Britain."),
      ("Can I leave L plates on when my parent drives?", "No — remove or cover them when no learner is driving.")], ["lplate", "lessons", "supervise"],
     [("knowledge/practising-with-family-supervisor-rules.html", "Knowledge", "Practising with family", "Supervisor rules."), ("knowledge/learner-driver-insurance.html", "Knowledge", "Learner driver insurance", "What you need.")]),

    ("wrong-turn-on-driving-test", "Went the wrong way on your driving test?", "Going the wrong way on the independent drive isn't a fault. What happens if you miss a turn, how to ask the examiner, and the faults that can come from panicking.",
     [("~20 min", "independent driving"), ("Sat nav", "or road signs"), ("Not a fault", "going the wrong way"), ("Ask", "the examiner any time")],
     f"""<p class="lead">It's the fear that comes up in nearly every mock test: "What if I go the wrong way?" Good news — the independent drive isn't a navigation test.</p>
<h2>What DVSA says</h2><p>DVSA's own Ready to Pass campaign says it doesn't matter if you go the wrong way or need to check where you're going — driving safely is what counts. If you go off route, the examiner helps you get back on it.</p>
<h2>How faults happen anyway</h2><p>The wrong turn itself isn't marked. What gets marked is what you do because of it:</p><ul><li>Swerving across lanes at the last second.</li><li>Braking hard to make a turn you nearly missed.</li><li>Stopping somewhere unsafe to "think".</li><li>Forgetting mirrors and signals while you're worrying.</li></ul>
<h2>What to do instead</h2><ol><li>If you're not sure, ask the examiner to repeat the direction — that's allowed.</li><li>If you've missed it, carry on safely. Take the next safe option.</li><li>Breathe — you can still pass.</li></ol>
<h2>Sat nav or signs</h2><p>Most independent drives follow a sat nav the examiner sets up; on some you follow road signs instead. Ask if you're unsure which.</p>
{local("Expect signs to places like the M60 or the city centre if you're asked to follow road signs.", "Around Shirley, signs to the M42, Solihull or Birmingham are the obvious ones to practise.")}
{tool("driving-test-sat-nav-guide-manchester.html", "DriveSQ: sat nav on the driving test")}""",
     [("Do you fail your driving test if you go the wrong way?", "No. Going the wrong way isn't a fault — only unsafe driving because of it."),
      ("Can I ask the examiner to repeat directions?", "Yes, at any time."),
      ("How long is independent driving?", "About 20 minutes of the test.")], ["ready", "sdfl_ind", "nid_ind", "during"],
     [("guides/test-day-checklist.html", "Guide", "Test day checklist", "Be ready."), ("test-faults/junction-observations.html", "Test faults", "Junction observations", "The #1 fault.")]),

    ("serious-and-dangerous-faults-explained", "Minor, serious and dangerous faults explained", "How the driving test is marked: up to 15 driving faults to pass, no serious or dangerous faults. What turns a minor into a serious, with real examples.",
     [("15", "driving faults allowed"), ("0", "serious faults allowed"), ("0", "dangerous faults allowed"), ("#1", "junction observation")],
     f"""<p class="lead">There are three kinds of fault on a UK driving test. Understanding the difference takes a lot of the mystery — and fear — out of the marking.</p>
<h2>The three fault types</h2><div class="table-wrap"><table><thead><tr><th>Fault</th><th>What it means</th><th>Allowed</th></tr></thead><tbody>
<tr><td>Driving fault (minor)</td><td>Not potentially dangerous, but could become serious if repeated</td><td>Up to 15</td></tr>
<tr><td>Serious fault</td><td>Something potentially dangerous</td><td>None</td></tr>
<tr><td>Dangerous fault</td><td>Actual danger to you, the examiner, the public or property</td><td>None</td></tr></tbody></table></div>
<h2>How a minor becomes a serious</h2><ul><li><b>Repetition:</b> one missed mirror check before changing direction might be a minor; doing it at every junction can become a serious fault for a habit.</li><li><b>Circumstances:</b> a slow emergence onto an empty road is a minor; the same hesitation that forces another driver to brake is serious.</li><li><b>Intervention:</b> if the examiner has to use the dual controls or speak to prevent danger, it's at least serious.</li></ul>
<h2>The most common fault areas</h2><p>Observation at junctions has been DVSA's top reason for failing for years, followed by mirrors when changing direction, steering control, turning right, moving off and response to traffic lights. Our <a href="../test-faults.html">test faults section</a> covers each one.</p>
{tool("driving-test-fault-counter.html", "Fault counter: would I have passed?")}""",
     [("How many minors can you get on a driving test?", "Up to 15 driving faults, as long as there are no serious or dangerous faults."),
      ("Can one serious fault fail you?", "Yes — one serious or dangerous fault is a fail."),
      ("Can minors add up to a fail?", "Yes: more than 15, or repeating the same minor fault so often that it shows a serious weakness.")], ["result", "faults"],
     [("test-faults.html", "Test faults", "Every test fault explained", "And how to fix it."), (DSQ + "how-many-minors-driving-test.html", "DriveSQ", "How many minors can you get?", "Explained.")]),

    ("blind-spot-checks", "Blind spot checks: when and how", "When to check your blind spot — moving off, changing lanes, merging and before opening doors — and why missing one is among the commonest driving test faults.",
     [("Moving off", "always"), ("Lane change", "always"), ("Merging", "slip roads"), ("Dutch reach", "before opening door")],
     """<p class="lead">Mirrors don't show everything. The areas just behind your shoulders — your blind spots — are where cyclists, motorbikes and cars hide.</p>
<h2>When to look</h2><ul><li><b>Moving off</b> from the side of the road: look over your right shoulder every time. "Moving off safely" is one of DVSA's regular reasons for failing.</li><li><b>Changing lanes</b> on dual carriageways and multi-lane roads.</li><li><b>Joining a motorway or dual carriageway</b> from a slip road.</li><li><b>Before opening your door</b>: the Highway Code recommends the "Dutch reach" — open with the hand furthest from the door so you turn to look behind.</li><li><b>Pulling out after parallel parking or pulling up on the right.</b></li></ul>
<h2>When not to</h2><p>Don't look over your shoulder when it isn't needed — like going round a roundabout or in moving traffic — because you take your eyes off what's ahead. Mirrors, then a quick glance only where a vehicle could genuinely be hidden.</p>
<h2>Where we practise</h2><p>Manchester: the M60 slip roads and dual carriageways like Princess Parkway. Solihull: the A45 and the M42 junctions.</p>""" + tool("solihull-driving-test-readiness-check.html", "Readiness check"),
     [("When should I check my blind spot?", "Moving off, changing lanes, merging and before opening your door — and whenever someone could be hidden beside you."),
      ("Is a missed blind spot check a fail?", "It can be. If it puts someone at risk it's a serious fault.")], ["hc_road", "faults"],
     [("test-faults/moving-off-safely.html", "Test faults", "Moving off safely", "The fault and the fix."), ("test-faults/mirrors-changing-direction.html", "Test faults", "Mirrors changing direction", "The fault and the fix.")]),

    ("country-roads-horses-and-cyclists", "Country roads, horses and cyclists", "Driving on country roads as a learner: national speed limit, bends, passing horses (under 10 mph, at least 2 metres) and cyclists (at least 1.5 metres) under the Highway Code.",
     [("60 mph", "limit, not a target"), ("2 m", "and under 10 mph past horses"), ("1.5 m", "past cyclists up to 30 mph"), ("2 m", "past people walking in the road")],
     f"""<p class="lead">Country roads catch out town learners: bends you can't see round, mud, horses, cyclists and drivers who know the road far too well.</p>
<h2>Speed</h2><p>The national speed limit (60 mph on single carriageways for cars) is a maximum. Drive so you can stop in the distance you can see is clear — on a blind bend that may be very slow.</p>
<h2>Passing people</h2><div class="table-wrap"><table><thead><tr><th>Road user</th><th>Highway Code advice</th></tr></thead><tbody>
<tr><td>Horse riders and horse-drawn vehicles</td><td>Pass at under 10 mph, leaving at least 2 metres</td></tr>
<tr><td>Cyclists</td><td>At least 1.5 metres at speeds up to 30 mph, more at higher speeds</td></tr>
<tr><td>People walking in the road</td><td>At least 2 metres, at low speed</td></tr></tbody></table></div>
<p>If you can't pass with that space, wait behind until you can.</p>
<h2>Bends, lanes and passing places</h2><ul><li>Slow down before the bend, not in it.</li><li>Keep left on blind bends.</li><li>On single-track lanes, pull into passing places on your left — or wait opposite one on your right.</li><li>Watch for mud and gravel near farm entrances.</li></ul>
{local("Lessons out towards Saddleworth, the Peak District edge and around Bolton's moors.", "Lanes around Berkswell, Hampton-in-Arden, Hockley Heath and Earlswood — see our <a href=\"../solihull/knowle-dorridge-and-village-speed-limits.html\">village limits guide</a>.")}
{tool("passing-distance-guide.html", "Passing distance guide")}""",
     [("How fast should I pass a horse?", "Under 10 mph, leaving at least 2 metres."),
      ("How much room should I give a cyclist?", "At least 1.5 metres at up to 30 mph, and more at higher speeds."),
      ("Do I have to drive at 60 on country roads?", "No — 60 is the limit, not a target.")], ["hc_vuln", "hc_road", "hc_ped"],
     [("guides/winter-driving-pennine-roads.html", "Guide", "Winter on Pennine roads", "Ice, snow and fog."), ("solihull/knowle-dorridge-and-village-speed-limits.html", "Solihull", "Village speed limits", "Solihull's lanes.")]),

    ("fog-and-headlights", "Driving in fog: which lights to use", "Fog, mist and heavy rain: when to use dipped headlights, when fog lights are allowed (visibility under about 100 m) and why you must switch them off afterwards.",
     [("100 m", "visibility rule of thumb"), ("Dipped", "headlights when visibility is seriously reduced"), ("Off", "fog lights when it clears"), ("Gap", "leave more room")],
     f"""<p class="lead">Fog turns familiar roads into strange ones. The rules on lights are short — and getting them wrong dazzles others or makes you invisible.</p>
<h2>Which lights</h2><ul><li><b>Dipped headlights</b> whenever visibility is seriously reduced — generally when you can't see more than about 100 metres.</li><li><b>Fog lights</b> (front and rear) may be used when visibility is seriously reduced, but you must switch them off when it improves — rear fog lights dazzle drivers behind and can hide your brake lights.</li><li><b>Don't use main beam</b> in fog — it reflects back and makes it worse.</li></ul>
<h2>Driving in fog</h2><ul><li>Slow down: be able to stop within the distance you can see.</li><li>Leave a much bigger gap — don't follow tail lights closely.</li><li>Wind the window down at junctions to listen for traffic.</li><li>Use your wipers and demister.</li></ul>
<h2>Fog on test day</h2><p>Tests can be cancelled for poor visibility. If DVSA cancels, you get a new date free — see <a href="driving-test-cancelled-what-now.html">test cancelled: what now?</a></p>
{local("Fog is common over the M62 and the Pennines.", "Low-lying fields around the M42, the NEC and the airport collect early-morning mist.")}
{tool("which-lights-should-i-use.html", "Which lights should I use?")}""",
     [("When should I use fog lights?", "When visibility is seriously reduced — generally under about 100 metres — and switch them off when it improves."),
      ("Should I use full beam in fog?", "No — it reflects back off the fog.")], ["hc_weather", "hc_lights"],
     [("guides/wet-weather-driving.html", "Guide", "Wet weather driving", "Rain and spray."), ("guides/winter-driving-pennine-roads.html", "Guide", "Winter driving", "Pennine roads.")]),

    ("driving-test-cancelled-what-now", "Driving test cancelled: what now?", "Your driving test was cancelled — by DVSA, for bad weather, or because of a car problem. Your rights to a new date, and when you can claim out-of-pocket expenses.",
     [("Free", "new date if DVSA cancels"), ("Short notice", "expenses may be claimable"), ("Weather", "no expenses"), ("Your car", "check it's test-ready")],
     """<p class="lead">A cancelled test is frustrating — especially after months of waiting. What happens next depends on who cancelled and why.</p>
<h2>If DVSA cancels</h2><p>You get a new test date without paying again. If they cancel at short notice, you can apply for out-of-pocket expenses with DVSA's claim form (for example, the lesson you paid for, or lost earnings). Guides commonly describe "short notice" as less than 3 working days — check the current form for the exact rules.</p>
<h2>Bad weather</h2><p>Tests can be cancelled for ice, snow or fog. You'll get a new date, but weather cancellations aren't covered for expenses. Unless you've been told otherwise, go to your test as normal.</p>
<h2>If your car isn't suitable</h2><p>If you use your own car and it doesn't meet the rules (dual mirrors, L plates, roadworthy, insured for the test), the test can't go ahead — and you may lose your fee. Using an SQ car avoids this.</p>
<h2>If you cancel</h2><p>Give enough notice to keep your fee — see GOV.UK's change or cancel page for the current notice period.</p>
<h2>What we do</h2><ul><li>We keep you driving while you wait so you don't go rusty.</li><li>We can help you check for earlier dates within DVSA's booking rules.</li></ul>""" + tool("driving-test-cancellations-manchester.html", "DriveSQ: driving test cancellations in Manchester"),
     [("What happens if DVSA cancels my driving test?", "You get a new date without paying again, and you may be able to claim expenses if it was at short notice."),
      ("Can I claim if my test is cancelled for snow?", "No — bad-weather cancellations aren't covered for expenses, but you get a free new date.")], ["change", "cancel_form", "cancel_foi", "cancel_pmf"],
     [("knowledge/driving-test-booking-rules-2026.html", "Knowledge", "Booking rules 2026", "What changed."), ("solihull/driving-test-cancellations-shirley.html", "Solihull", "Cancellations at Shirley", "Earlier dates.")]),

    ("cockpit-drill-dsssm", "The cockpit drill (DSSSM) explained", "The cockpit drill every learner starts with: Doors, Seat, Steering, Seatbelt, Mirrors — then the POM routine for moving off. With a free printable checklist.",
     [("D", "doors"), ("S S S", "seat, steering, seatbelt"), ("M", "mirrors"), ("POM", "prepare, observe, move")],
     f"""<p class="lead">Every first lesson starts the same way: the cockpit drill. Five checks, about thirty seconds, every time you get in.</p>
<h2>DSSSM</h2><ol class="rx-steps"><li data-n="D"><h4>Doors</h4><p>All shut properly — look at the dashboard warning light.</p></li><li data-n="S"><h4>Seat</h4><p>Push the clutch (or brake in an automatic) fully down with a slight bend in your knee; back supported; head restraint roughly level with the top of your head.</p></li><li data-n="S"><h4>Steering</h4><p>Wrists rest on the top of the wheel with your back against the seat.</p></li><li data-n="S"><h4>Seatbelt</h4><p>On, flat and not twisted. Passengers too.</p></li><li data-n="M"><h4>Mirrors</h4><p>Interior mirror to frame the rear window; door mirrors with a sliver of your own car showing.</p></li></ol>
<h2>Then: POM to move off</h2><p><b>Prepare</b> (gear, gas, find the bite or release the brake), <b>Observe</b> (mirrors and blind spot), <b>Move</b> (only when safe, signal if it helps anyone).</p>
<h2>Why it matters on test</h2><p>The examiner won't mark the drill itself, but a badly set seat or mirrors leads straight to steering and observation faults.</p>
{tool("cockpit-drill-checklist.html", "Interactive cockpit drill checklist")}""",
     [("What does DSSSM stand for?", "Doors, Seat, Steering, Seatbelt, Mirrors."),
      ("What is POM?", "Prepare, Observe, Move — the routine for moving off.")], ["lessons", "hc_road"],
     [("first-lesson.html", "Lessons", "Your first lesson", "What to expect."), ("guides/show-me-tell-me.html", "Guide", "Show me, tell me", "Vehicle questions.")]),

    ("manual-or-automatic-2030-petrol-ban", "Manual or automatic after the 2030 petrol ban?", "From 2030 new pure petrol and diesel cars can't be sold in the UK, with some hybrids until 2035. What that means for learning manual or automatic in 2026.",
     [("2030", "end of new petrol/diesel-only car sales"), ("2035", "hybrids with significant electric range"), ("Auto", "licence = automatic only"), ("Manual", "licence = both")],
     f"""<p class="lead">Electric cars don't have a clutch, and the government's 2030 deadline is getting closer. So is it still worth learning manual?</p>
<h2>What the 2030 rule actually says</h2><p>In April 2025 the government confirmed that new cars powered only by petrol or diesel can't be sold from 2030. Hybrids with "significant electric range" can be sold until 2035, after which new cars must be zero emission. Sources differ on exactly which hybrids qualify. Used petrol and diesel cars can still be bought, sold and driven.</p>
<h2>What your licence covers</h2><ul><li><b>Pass in a manual:</b> you can drive manual and automatic cars.</li><li><b>Pass in an automatic:</b> automatic only (electric cars count as automatic).</li></ul>
<h2>So which should you learn?</h2><div class="table-wrap"><table><thead><tr><th>Learn automatic if…</th><th>Learn manual if…</th></tr></thead><tbody>
<tr><td>You'll drive an electric or hybrid car</td><td>Your first car will be a cheap used manual</td></tr>
<tr><td>You want to pass sooner</td><td>Your job may involve manual vans or pool cars</td></tr>
<tr><td>Clutch control is holding you back</td><td>You might drive abroad, where hire cars are often manual</td></tr></tbody></table></div>
<p>Both cost the same with us: £35 an hour for 2 hours or more.</p>
{tool("manual-or-automatic-decider.html", "Manual or automatic? 60-second decider")}""",
     [("Will manual cars be banned in 2030?", "No — the 2030 rule stops sales of new petrol- and diesel-only cars. Used manual cars can still be driven."),
      ("Does an automatic licence let me drive an electric car?", "Yes. Electric cars are automatic."),
      ("Is it worth learning manual in 2026?", "If you'll drive older or cheaper cars, or vans for work — yes. For electric or hybrid cars, automatic is enough.")], ["zev", "zev2", "licence_auto"],
     [("guides/manual-vs-automatic.html", "Guide", "Manual vs automatic", "The full comparison."), (DSQ + "electric-car-driving-lessons-manchester.html", "DriveSQ", "Electric car lessons", "Manchester.")]),

    ("dash-cams-for-learner-drivers", "Dash cams for learners and new drivers", "Can you use a dash cam on driving lessons or your test? DVSA's policy on filming tests, insurance discounts, and where to mount it legally.",
     [("Check", "DVSA's filming policy"), ("Inside", "not allowed on test"), ("Windscreen", "keep your view clear"), ("Insurance", "some discounts")],
     """<p class="lead">Dash cams are cheap and can protect new drivers after a crash. But a driving test has its own rules.</p>
<h2>On your driving test</h2><p>DVSA publishes a policy on filming and recording driving tests, including dash cams. Its general position is not to allow tests to be filmed, and recording inside the car isn't allowed. Read the policy and tell the examiner about any camera before you start — if in doubt, switch it off.</p>
<h2>On lessons</h2><p>If you'd like footage of your own drives to review, talk to your instructor first — everyone in the car should agree to being recorded.</p>
<h2>After you pass</h2><ul><li>Some insurers offer a small discount — check before assuming.</li><li>Mount it so it doesn't block your view of the road (behind the rear-view mirror is usual).</li><li>Footage can help after a crash; you can also submit dangerous-driving footage to the police online.</li></ul>""" + tool("solihull-new-drivers-first-year.html", "DriveSQ: your first year after passing"),
     [("Can I use a dash cam on my driving test?", "DVSA's policy generally doesn't allow filming tests, and inside recording isn't allowed. Read the policy and tell the examiner — if in doubt, switch it off."),
      ("Do dash cams lower insurance?", "Some insurers offer a discount; many don't. Ask yours.")], ["film"],
     [("knowledge/after-you-pass-new-driver-guide.html", "Knowledge", "After you pass", "Your first year."), (DSQ + "best-first-cars-new-drivers-uk.html", "DriveSQ", "Best first cars", "For new drivers.")]),
]


def guide_page(g):
    slug, title, desc, stats, body, faqs, src, related = g
    path = f"guides/{slug}.html"
    rel = [(h if h.startswith("http") else h, c, t, d) for h, c, t, d in related] + [("guides.html", "Guides", "All learner guides", "Everything in one place.")]
    html = shell(path, f"{title} | SQ Driving School", "Guide", [("Guides", "guides.html"), (title, path)], title + ".", desc, stats, [desc], body, faqs, [G[k] for k in src], rel,
                 side_title="Learn with SQ", booking_heading="Book a lesson in 60 seconds", active="knowledge.html")
    return html.replace(f'href="../{DSQ}', f'href="{DSQ}')


def all_pages():
    return {f"guides/{g[0]}.html": guide_page(g) for g in GUIDES}
