"""SQ Learner Toolkit — interactive, hand-written tools for learner drivers (driving/ section).

Each page has a working tool (research.js), a written guide built on official GOV.UK / Highway Code figures,
the 60-second booking wizard (sends to the DriveSQ admin) and the DriveSQ Student Portal promo."""
from hub_shell import *

GOV = {
    "hc126": ("Highway Code — Rule 126, stopping distances", "https://www.gov.uk/guidance/the-highway-code/general-rules-techniques-and-advice-for-all-drivers-and-riders-103-to-158"),
    "hc_eyes": ("Highway Code — Rules 90–94, fitness to drive and vision", "https://www.gov.uk/guidance/the-highway-code/rules-for-drivers-and-motorcyclists-89-to-102"),
    "eyes": ("GOV.UK — Driving eyesight rules", "https://www.gov.uk/driving-eyesight-rules"),
    "plates": ("GOV.UK — Displaying number plates (character size)", "https://www.gov.uk/displaying-number-plates"),
    "test": ("GOV.UK — What happens during the driving test", "https://www.gov.uk/driving-test/what-happens-during-test"),
    "cost": ("GOV.UK — Driving test cost", "https://www.gov.uk/driving-test-cost"),
    "hpt": ("GOV.UK — Theory test: hazard perception", "https://www.gov.uk/theory-test/hazard-perception-test"),
    "pass": ("GOV.UK — Theory test pass mark and result", "https://www.gov.uk/theory-test/pass-mark-and-result"),
    "mcq": ("GOV.UK — Theory test: multiple-choice questions", "https://www.gov.uk/theory-test/multiple-choice-questions"),
    "lessons": ("GOV.UK — Driving lessons and learning to drive", "https://www.gov.uk/driving-lessons-learning-to-drive"),
    "book": ("GOV.UK — Book your driving test", "https://www.gov.uk/book-driving-test"),
    "showme": ("GOV.UK — Car show me, tell me questions", "https://www.gov.uk/government/publications/car-show-me-tell-me-vehicle-safety-questions"),
    "hc": ("The Highway Code (GOV.UK)", "https://www.gov.uk/guidance/the-highway-code"),
    "nightdark": ("Highway Code — Rules 113–116, lighting requirements", "https://www.gov.uk/guidance/the-highway-code/general-rules-techniques-and-advice-for-all-drivers-and-riders-103-to-158"),
}
SECTION = ("Learner Toolkit", "learner-toolkit.html")
TOOLS = [
    ("stopping-distances-calculator", "Calculator", "Stopping distance calculator", "See your thinking and braking distance at any speed, in the dry, wet or ice — in metres and car lengths.", "calc"),
    ("driving-test-day-planner", "Planner", "Driving test day planner", "Enter your test date and time: sunrise, sunset, glare, rush hour, school run and a minute-by-minute plan.", "calendar"),
    ("learning-to-drive-timeline-planner", "Planner", "How long to learn to drive? Timeline planner", "Hours left, weeks to go, when to book your test and what it will cost — built on the DVSA average.", "clock"),
    ("eyesight-test-20-metres", "Guide", "The 20-metre eyesight test explained", "What 20 metres looks like, the number plate rules, and what happens if you can't read it on test day.", "eye"),
    ("hazard-perception-test-scoring-explained", "Interactive", "Hazard perception scoring explained", "How the 5-4-3-2-1 scoring window works — try the timing demo and learn why clicking too much scores zero.", "bolt"),
    ("driving-lesson-glossary", "Glossary", "Driving lesson glossary A–Z", "80+ terms instructors and examiners use — MSM, POM, bite point, serious fault, bay park, bus gate — explained simply.", "book"),
]


def _path(slug):
    return f"driving/{slug}.html"


def _related(slug, extra=()):
    out = [(_path(s), c, t, d) for s, c, t, d, i in TOOLS if s != slug][:3]
    return list(extra) + out


# ---------------------------------------------------------------- stopping distances
def stopping():
    slug = "stopping-distances-calculator"
    rows = [(20, 6, 6), (30, 9, 14), (40, 12, 24), (50, 15, 38), (60, 18, 55), (70, 21, 75)]
    tr = "".join(f'<tr data-mph="{m}"><td class="mono">{m} mph</td><td class="mono">{t} m</td><td class="mono">{b} m</td><td class="mono"><b>{t + b} m</b></td><td>{(t + b) / 4:.1f} car lengths</td></tr>' for m, t, b in rows)
    body = f"""
<p class="lead">Every theory test asks about stopping distances, and every driving test examiner watches how much space you leave. Most learners memorise the Highway Code table without ever <em>seeing</em> it. Move the slider below and watch your stopping distance grow — it's the fastest way to understand why 30mph and 40mph feel so different.</p>
<div class="rx-tool" data-rx="stop" data-reveal="up">
  <div class="rx-tool__head"><div class="card__icon">{icon('calc')}</div><div><h3>Stopping distance calculator</h3><p>Highway Code model · reaction time 0.67s by default</p></div></div>
  <div class="rx-chips" role="group" aria-label="Road surface"><button type="button" class="is-on" data-cond="1">☀️ Dry</button><button type="button" data-cond="2">🌧️ Wet (×2 braking)</button><button type="button" data-cond="10">🧊 Ice (up to ×10)</button></div>
  <div class="rx-row" style="grid-template-columns:1fr 1fr">
    <div><label for="st-speed">Speed: <b class="js-mph">30 mph</b></label><input class="rx-range" id="st-speed" name="speed" type="range" min="10" max="70" step="10" value="30"></div>
    <div><label for="st-react">Reaction time: <b class="js-rt">0.67 s</b></label><input class="rx-range" id="st-react" name="react" type="range" min="0.5" max="2" step="0.01" value="0.67"></div>
  </div>
  <div class="rx-stop"><div class="rx-stop__track"><span class="rx-stop__think"></span><span class="rx-stop__brake"></span><span class="rx-stop__over">150 m+</span></div>
  <div class="rx-stop__legend"><span><i style="background:var(--amber)"></i>Thinking distance</span><span><i style="background:var(--red)"></i>Braking distance</span><span>Grid lines every 15 m</span></div></div>
  <div class="rx-out"><div><b class="js-think">9 m</b><span>Thinking distance</span></div><div><b class="js-brake">14 m</b><span>Braking distance</span></div><div class="rx-big"><b class="js-total">23 m</b><span>Total stopping distance</span></div><div><b class="js-cars">5.8</b><span>Car lengths (4 m each)</span></div></div>
  <div class="rx-stop__cars" aria-hidden="true"></div>
  <div class="rx-table-wrap"><table class="rx-table rx-hc"><thead><tr><th>Speed</th><th>Thinking</th><th>Braking</th><th>Total (dry)</th><th>Roughly</th></tr></thead><tbody>{tr}</tbody></table></div>
  <p class="note">The highlighted row matches the Highway Code when the surface is dry and reaction time is 0.67s.</p>
</div>
<h2>The Highway Code stopping distances, explained</h2>
<p>Rule 126 of the Highway Code gives "typical stopping distances" for a car on a dry road. Each one is made of two parts:</p>
<ul><li><b>Thinking distance</b> — how far you travel between seeing a hazard and pressing the brake. The Highway Code figures assume a reaction time of about two-thirds of a second, so thinking distance grows in a straight line: 6m at 20mph, 9m at 30mph, 21m at 70mph.</li>
<li><b>Braking distance</b> — how far the car travels once the brakes are on. This grows with the <em>square</em> of your speed. Double your speed and braking distance roughly quadruples: 14m at 30mph becomes 55m at 60mph.</li></ul>
<div class="callout callout--info"><b>Theory test shortcut:</b> thinking distance in feet is the same as your speed in mph (30mph → 30ft ≈ 9m). For braking, multiply by speed ÷ 20 (30mph → 30 × 1.5 = 45ft ≈ 14m). It's a memory trick, not a law of physics, but it reproduces the table.</div>
<h2>Why 20mph vs 30mph matters so much in Manchester</h2>
<p>Many residential streets across Manchester, Salford, Trafford and Stockport now have 20mph limits. At 20mph you stop in about 12 metres — three car lengths. At 30mph it's 23 metres. That 11-metre difference is the gap between stopping before a child who steps out from between parked cars and hitting them at around 20mph. It's why examiners mark "speed too fast for the conditions" even when you're under the limit on a narrow street lined with parked cars.</p>
<h2>Wet roads, ice and the two-second rule</h2>
<p>The Highway Code says stopping distances will be at least <b>double</b> on wet roads and can be up to <b>ten times</b> greater on icy roads. Greater Manchester is one of the wetter parts of England, so "wet" is the normal test condition, not the exception. Press the 🌧️ button above at 30mph: you'll need around 37 metres.</p>
<p>In practice you don't measure metres — you count seconds. Leave at least a <b>two-second gap</b> to the vehicle in front on a dry road, and at least four seconds in the wet. Pick a lamp post, wait until the car ahead passes it, and say "only a fool breaks the two-second rule". If you reach the post before you finish, drop back.</p>
<h2>What makes your thinking distance longer</h2>
<p>Drag the reaction-time slider to 1.5 seconds — a realistic figure for a distracted or tired driver — and watch the yellow bar. At 30mph your thinking distance more than doubles. Things that slow reactions:</p>
<ul><li>Using a phone, even hands-free, or fiddling with the sat-nav or music.</li><li>Tiredness — early-morning and late-evening drives, long shifts (we teach plenty of NHS staff after night shifts and plan lessons around it).</li><li>Alcohol and drugs, including some prescription and over-the-counter medicines.</li><li>Inexperience: new drivers take longer to recognise a hazard. That's exactly what the hazard perception test measures.</li></ul>
<h2>How stopping distances show up on your driving test</h2>
<p>You won't be asked to quote the table on your practical test, but you'll be assessed on using it. Faults we commonly correct before test day include following too closely in queuing traffic on main roads, not leaving enough room to stop when traffic lights change, and approaching zebra crossings too fast to stop for someone stepping out. The examiner may also ask you to do an <b>emergency stop</b> — you'll need to stop quickly, under control, without locking the wheels. See our <a href="{ROOT}knowledge/why-learners-fail-the-driving-test.html">guide to why learners fail</a>.</p>
<h2>How we teach it at SQ</h2>
<p>On lessons we use the same "count the seconds" method on real roads, then practise controlled braking in a quiet road before you ever need it. Your DriveSQ Student Portal logs "use of speed", "following distance" and "emergency stop" as separate skills after each lesson, so you can see when each one reaches test standard.</p>"""
    faqs = [("What is the stopping distance at 30mph?", "23 metres on a dry road in the Highway Code: 9m thinking distance plus 14m braking distance — about six car lengths."),
            ("What is the stopping distance at 70mph?", "96 metres: 21m thinking plus 75m braking. That's about 24 car lengths."),
            ("How much longer are stopping distances in the wet?", "The Highway Code says at least double on wet roads and up to ten times greater on icy roads."),
            ("What reaction time does the Highway Code use?", "The typical stopping distances work out at a reaction time of about 0.67 seconds — two-thirds of a second."),
            ("How many car lengths is 23 metres?", "About six, using an average car length of four metres.")]
    return shell(_path(slug), "Stopping Distance Calculator (Highway Code 2026) | SQ Driving School", "Calculator", [SECTION, ("Stopping distances", _path(slug))],
                 "Stopping distance calculator", "Work out thinking, braking and total stopping distance at any speed in the dry, wet or ice — with the Highway Code table and a visual car-length guide.",
                 [("23 m", "at 30mph, dry"), ("96 m", "at 70mph, dry"), ("×2", "in the wet"), ("×10", "on ice")],
                 ["Stopping distance = thinking distance + braking distance.", "Thinking distance grows with speed; braking distance grows with speed squared.", "Wet roads at least double the distance; ice can make it ten times longer.", "Use the two-second rule on dry roads and four seconds in the wet."],
                 body, faqs, [GOV["hc126"], GOV["test"], GOV["hc"]], _related(slug, [("theory-quiz.html", "Practice", "Free theory test quiz", "Test yourself on stopping distances and road rules.")]))


# ---------------------------------------------------------------- test day planner
def testday():
    slug = "driving-test-day-planner"
    body = f"""
<p class="lead">Your driving test is about 40 minutes long, but test day starts hours before. This planner calculates the actual sunrise and sunset for your date in Manchester, works out whether you'll be driving into a low sun or the dark, warns you about rush hour and the school run, and builds a simple timetable backwards from your test time.</p>
<div class="rx-tool" data-rx="testday" data-reveal="up">
  <div class="rx-tool__head"><div class="card__icon">{icon('calendar')}</div><div><h3>Driving test day planner</h3><p>Sun positions calculated in your browser for Manchester (53.48°N)</p></div></div>
  <div class="rx-row" style="grid-template-columns:1fr 1fr"><div><label for="td-date">Test date</label><input id="td-date" name="tdate" type="date"></div>
  <div><label for="td-time">Test time</label><input id="td-time" name="ttime" type="time" value="08:57" step="60"></div></div>
  <div class="js-plan" aria-live="polite"></div>
</div>
<h2>What happens on the day</h2>
<ol class="rx-steps"><li data-n="1"><h4>Eyesight check</h4><p>You read a number plate from 20 metres before you get in the car. Fail it and the test doesn't go ahead. See our <a href="eyesight-test-20-metres.html">eyesight test guide</a>.</p></li>
<li data-n="2"><h4>"Tell me" question</h4><p>Before you set off you'll be asked one "tell me" vehicle safety question, such as how you'd check the tyres.</p></li>
<li data-n="3"><h4>General driving</h4><p>About 20 minutes on a mix of roads — the examiner gives directions.</p></li>
<li data-n="4"><h4>Independent driving</h4><p>About 20 minutes following a sat-nav or road signs. You can ask for directions to be repeated.</p></li>
<li data-n="5"><h4>"Show me" question and a manoeuvre</h4><p>One "show me" question while driving (e.g. demisting the windscreen), and one reversing manoeuvre: parallel park, bay park, or pull up on the right and reverse. Around one test in three includes an emergency stop.</p></li>
<li data-n="6"><h4>Result</h4><p>The examiner tells you your result and gives feedback straight away. Up to 15 driving faults is a pass; any serious or dangerous fault is a fail.</p></li></ol>
<h2>Picking a test time: what the planner is checking</h2>
<p><b>Low sun.</b> When the sun is less than about 15° above the horizon it sits right in your field of view. In Manchester in autumn and winter that happens in normal test hours — mornings around 8–10am and mid-afternoons. The planner tells you which direction the sun will be in, so you know which roads will be hardest. Our <a href="{ROOT}research/best-time-to-take-driving-test-manchester.html">daylight study</a> shows the pattern month by month.</p>
<p><b>Darkness.</b> In December the sun sets before 4pm in Manchester. A 3pm test can end in twilight. If yours could, make sure you've had at least one lesson in the dark.</p>
<p><b>Rush hour and the school run.</b> Weekday slots roughly 7:30–9:15am and 3–6:30pm meet heavier traffic, buses and parked cars outside schools. Some learners prefer this (it's what they've practised); others find it stressful. It's a personal choice — the point is to practise at the same time of day as your test.</p>
<p><b>Clock changes.</b> The week after the clocks go back in late October, afternoon tests suddenly finish in poorer light. The planner flags this.</p>
<p><b>Cost.</b> A weekday test costs £62; evenings, weekends and bank holidays cost £75. Prices are set by the DVSA.</p>
<h2>Your test-day checklist</h2>
<ul class="check"><li>Provisional licence photocard — no licence, no test.</li><li>Glasses or contact lenses if you need them to drive.</li><li>A warm-up lesson ending at the test centre (most SQ learners do 1 hour).</li><li>Arrive about 10 minutes early. Toilet, phone off.</li><li>Eat something. A 40-minute test on an empty stomach doesn't help nerves.</li><li>Know the tell-me answers — practise with our <a href="{ROOT}guides/show-me-tell-me.html">show me, tell me guide</a>.</li></ul>
<p>Read the full <a href="{ROOT}guides/test-day-checklist.html">test-day checklist</a> and our guides to every <a href="{ROOT}test-routes.html">Greater Manchester test centre's roads</a>.</p>"""
    faqs = [("How long is the UK driving test?", "About 40 minutes of driving, including around 20 minutes of independent driving."),
            ("What should I take to my driving test?", "Your provisional licence photocard, and glasses or contact lenses if you need them. If you take your own car it must meet the DVSA's rules — SQ learners use our dual-controlled car."),
            ("Is it harder to take a driving test in the dark?", "Tests aren't harder in the dark, but they're different: you need to use dipped headlights properly and judge speed and distance at night. Make sure you've practised it."),
            ("What is the best time of day for a driving test?", "The time you've practised most. Use the planner above to avoid surprises such as low sun, darkness or the school run."),
            ("How much does a driving test cost?", "£62 on weekdays and £75 for evenings, weekends and bank holidays.")]
    return shell(_path(slug), "Driving Test Day Planner: Light, Traffic & Timings | SQ Driving School", "Planner", [SECTION, ("Test day planner", _path(slug))],
                 "Driving test day planner", "Enter your test date and time to see sunrise, sunset, low-sun glare, rush hour and the school run in Manchester — plus a step-by-step test-day timetable.",
                 [("40 min", "test length"), ("20 min", "independent driving"), ("1 in 3", "tests have an emergency stop"), ("£62", "weekday test fee")],
                 ["The planner calculates real sun positions for your test date in Manchester.", "Low sun, darkness, rush hour and the school run are flagged automatically.", "Plan a warm-up lesson ending at the test centre and arrive 10 minutes early.", "Practise at the same time of day as your test."],
                 body, faqs, [GOV["test"], GOV["cost"], GOV["showme"], GOV["nightdark"]], _related(slug, [("research/best-time-to-take-driving-test-manchester.html", "Data Lab", "Best time to take your test", "Daylight and glare month by month in Manchester.")]))


# ---------------------------------------------------------------- timeline
def timeline():
    slug = "learning-to-drive-timeline-planner"
    body = f"""
<p class="lead">"How long will it take me to pass?" is the question we hear most. The honest answer depends on how many hours you need, how often you drive and how long the test waiting list is. This planner puts all three together and tells you <em>when to book your test</em> — the bit most learners get wrong.</p>
<div class="rx-tool" data-rx="timeline" data-reveal="up">
  <div class="rx-tool__head"><div class="card__icon">{icon('clock')}</div><div><h3>Learning-to-drive timeline</h3><p>Starts from the DVSA average of 45 hours with an instructor</p></div></div>
  <div class="rx-row"><div><label for="tl-need">Hours you'll need in total</label><input id="tl-need" name="need" type="number" min="5" max="120" value="45"></div>
  <div><label for="tl-done">Hours done so far</label><input id="tl-done" name="done" type="number" min="0" max="120" value="0"></div>
  <div><label for="tl-per">Lesson hours per week</label><input id="tl-per" name="perweek" type="number" min="1" max="30" value="2"></div>
  <div><label for="tl-wait">Test waiting time (weeks)</label><input id="tl-wait" name="wait" type="number" min="0" max="40" value="16"></div></div>
  <div class="rx-tl" aria-hidden="true"><span class="rx-tl__fill"></span></div><p class="note">Progress towards your total hours</p>
  <div class="rx-out"><div><b class="js-hrs">45 hrs</b><span>Hours to go</span></div><div><b class="js-weeks">23 weeks</b><span>At your pace</span></div><div class="rx-big"><b class="js-ready">—</b><span>Likely test-ready</span></div><div><b class="js-bookby">—</b><span>Book your test by</span></div></div>
  <div class="rx-out" style="grid-template-columns:1fr 2fr"><div><b class="js-cost">£1,575</b><span>Lessons left at £35/hr</span></div><div><span class="js-tip"></span></div></div>
</div>
<h2>Where the 45 hours comes from</h2>
<p>The DVSA says the average learner needs about <b>45 hours of professional lessons plus 22 hours of private practice</b> to pass. It's an average across everyone — some people need 25 hours, some need 80. Things that usually shorten it: driving several times a week rather than once, private practice with family between lessons, and starting in an automatic. Things that lengthen it: long gaps between lessons, nerves (very manageable with the right instructor) and booking the test before you're ready.</p>
<h2>Pace matters more than total hours</h2>
<p>Try the planner with 2 hours a week and then 6 hours a week. The total cost barely changes, but you go from about half a year to two months. Frequent lessons mean less time re-learning what you'd forgotten. That's the idea behind <a href="{ROOT}intensive.html">intensive courses</a> — and why we recommend 2-hour lessons (£70) over single hours for most learners.</p>
<h2>When to book your practical test</h2>
<p>You can only book your practical test after passing your theory test, and since 2026 you can normally only change a booking twice. Book too early and you risk turning up before you're ready; book too late and you finish lessons and then wait months. The planner subtracts your waiting time from your test-ready date to give a "book by" date. Check real dates on GOV.UK — waiting times differ a lot between centres. See our <a href="{ROOT}knowledge/driving-test-waiting-times-greater-manchester.html">waiting times guide</a> and <a href="{ROOT}knowledge/driving-test-booking-rules-2026.html">2026 booking rules</a>.</p>
<h2>The full journey, step by step</h2>
<ol class="rx-steps"><li data-n="1"><h4>Provisional licence</h4><p>Apply on GOV.UK from age 15 years 9 months; you can drive a car from 17. <a href="{ROOT}guides/provisional-licence.html">How to apply</a>.</p></li>
<li data-n="2"><h4>First lessons</h4><p>Controls, moving off, junctions. Your DriveSQ Student Portal starts logging your 23 skills from lesson one.</p></li>
<li data-n="3"><h4>Theory test</h4><p>50 multiple-choice questions (pass mark 43) and hazard perception (pass mark 44 out of 75). £23. Your certificate lasts 2 years. <a href="hazard-perception-test-scoring-explained.html">How hazard perception is scored</a>.</p></li>
<li data-n="4"><h4>Book the practical</h4><p>Use the "book by" date above. Tell us your date straight away.</p></li>
<li data-n="5"><h4>Test-route practice and mock test</h4><p>Lessons on the roads around your centre — see our <a href="{ROOT}test-routes.html">test-route guides</a> — then a full mock test.</p></li>
<li data-n="6"><h4>Pass</h4><p>Then consider <a href="{ROOT}services/pass-plus-courses.html">Pass Plus</a> or motorway lessons.</p></li></ol>"""
    faqs = [("How many driving lessons do I need?", "The DVSA average is about 45 hours of lessons plus 22 hours of private practice, but it varies a lot from person to person."),
            ("How long does it take to learn to drive?", "At 2 hours a week, 45 hours takes around 23 weeks. At 6 hours a week, about 8 weeks. Test waiting times can add to this, so book at the right moment."),
            ("When should I book my driving test?", "After passing your theory test, at a date that lands when you expect to be ready. Subtract the current waiting time from your expected test-ready date."),
            ("How much does it cost to learn to drive in Manchester?", "At SQ's £35 an hour, 45 hours is £1,575 (less with block discounts), plus £23 for the theory test and £62 for a weekday practical test."),
            ("How long is a theory test certificate valid?", "Two years. If you don't pass your practical test in that time, you have to take the theory test again.")]
    return shell(_path(slug), "How Long to Learn to Drive? Timeline & Test Booking Planner | SQ", "Planner", [SECTION, ("Timeline planner", _path(slug))],
                 "How long will it take to learn to drive?", "Plan your hours, weekly lessons and test waiting time — and find out exactly when to book your practical test and what it will cost.",
                 [("45 hrs", "DVSA average lessons"), ("+22 hrs", "private practice"), ("2 yrs", "theory certificate lasts"), ("£35", "per hour at SQ")],
                 ["The DVSA average is 45 hours of lessons plus 22 hours of practice.", "Driving more often shortens the calendar time without costing much more.", "Book your test so your date lands when you'll be ready — the planner works it out.", "Pass your theory test first; the certificate lasts two years."],
                 body, faqs, [GOV["lessons"], GOV["pass"], GOV["book"], GOV["cost"]], _related(slug, [("guides/cost-of-learning-to-drive-manchester.html", "Guide", "Cost of learning to drive in Manchester", "Every cost, from licence to test.")]))


# ---------------------------------------------------------------- eyesight
def eyesight():
    slug = "eyesight-test-20-metres"
    body = f"""
<p class="lead">The very first thing that happens on your practical driving test is the eyesight check — before you even sit in the car. If you can't read the number plate, the test ends there and you lose your fee. Here's exactly what the rule says, what 20 metres actually looks like, and how to check yourself on your street tonight.</p>
<div class="rx-figs" data-stagger=".06"><div class="rx-fig" data-reveal="up"><b>20 m</b><span>Distance to read a post-2001 number plate</span></div><div class="rx-fig" data-reveal="up"><b>20.5 m</b><span>For an older-style plate</span></div><div class="rx-fig" data-reveal="up"><b>79 mm</b><span>Height of each number-plate character</span></div><div class="rx-fig" data-reveal="up"><b>6/12</b><span>Minimum visual acuity (decimal 0.5)</span></div></div>
<h2>The rule in plain English</h2>
<p>GOV.UK says you must be able to read, with glasses or contact lenses if you need them, a car number plate made after 1 September 2001 from <b>20 metres</b>. You also need a visual acuity of at least <b>decimal 0.5 (6/12)</b> on the Snellen scale, using both eyes together or one eye if you only have sight in one, and an adequate field of vision. The Highway Code repeats the rule and allows 20.5 metres for older-style plates.</p>
<p>Characters on a modern UK number plate are 79mm tall. At 20 metres that's a small target — roughly what you'd see across five parked cars.</p>
<h2>What 20 metres looks like</h2>
<ul><li>About <b>five car lengths</b> along a residential street.</li><li>Roughly the length of a typical double-decker bus and a half.</li><li>Around <b>26 normal walking steps</b> for most adults (one step ≈ 0.75m).</li><li>A little shorter than a cricket pitch (20.12m between the stumps).</li></ul>
<h2>How to check yourself before test day</h2>
<ol class="rx-steps"><li data-n="1"><h4>Find a parked car in daylight</h4><p>The test is done in good light outdoors. Choose a car with a modern plate (two letters, two numbers, three letters).</p></li>
<li data-n="2"><h4>Pace out 26 steps</h4><p>Or count five car lengths along the kerb.</p></li>
<li data-n="3"><h4>Read it aloud, then walk back and check</h4><p>Do it with three different plates. Wear the glasses or lenses you'll drive in.</p></li>
<li data-n="4"><h4>Struggling? Book an optician now</h4><p>Not the week of your test. Many opticians offer eye tests at no cost to under-16s, students under 19 in full-time education and some benefit claimants; for others it's usually a modest fee.</p></li></ol>
<h2>What happens on the test</h2>
<p>The examiner points out a vehicle and asks you to read its plate. If you can't, they measure out the exact distance and try a second plate; if needed, a third at exactly 20 metres. If you still can't read it, you fail the test — it won't continue — and the DVLA is told, which means your licence can be revoked until you can show your eyesight meets the standard.</p>
<div class="callout callout--warn"><b>If you need glasses to read the plate, you must wear them every time you drive.</b> That includes every lesson. Your instructor will check.</div>
<h2>Other eyesight conditions</h2>
<p>You must tell the DVLA about certain eye conditions that affect both eyes or your remaining eye, such as glaucoma, cataracts in both eyes or diabetic retinopathy treated with laser. Colour blindness does not usually need to be reported and doesn't stop you driving — we teach learners with colour vision deficiency to read traffic lights by position as well as colour. Check the full list on GOV.UK.</p>
<h2>Night driving and glare</h2>
<p>Eyesight that's fine at noon can struggle at dusk. If headlights or a low sun dazzle you, get your eyes checked and ask the optician about lenses for driving. Our <a href="driving-test-day-planner.html">test day planner</a> tells you whether your test will be in low sun or twilight.</p>"""
    faqs = [("How far away do you have to read a number plate for the driving test?", "20 metres for a plate made after 1 September 2001, or 20.5 metres for an older-style plate."),
            ("What happens if I fail the eyesight test on my driving test?", "Your test ends and you fail. The DVLA is told and your licence can be revoked until you meet the standard."),
            ("Can I wear glasses for the driving test eyesight check?", "Yes. If you need them to meet the standard, you must wear them every time you drive."),
            ("Is 20 metres the same as five car lengths?", "Roughly — an average car is about four metres long."),
            ("Can you drive if you are colour blind?", "Yes, usually. Colour blindness doesn't normally need to be reported to the DVLA.")]
    return shell(_path(slug), "Driving Test Eyesight Check: Reading a Plate at 20 Metres | SQ", "Guide", [SECTION, ("Eyesight test", _path(slug))],
                 "The 20-metre number plate eyesight test", "What the driving eyesight rule says, what 20 metres looks like, how to check yourself, and what happens if you can't read the plate on test day.",
                 [("20 m", "post-2001 plates"), ("20.5 m", "older plates"), ("6/12", "minimum acuity"), ("3", "plates before a fail")],
                 ["Read a post-2001 plate from 20 metres (20.5m for older plates).", "You also need visual acuity of at least decimal 0.5 (6/12).", "Fail the check and the test ends — and the DVLA is told.", "Test yourself on your street: 26 steps or five car lengths."],
                 body, faqs, [GOV["eyes"], GOV["hc_eyes"], GOV["plates"], GOV["test"]], _related(slug))


# ---------------------------------------------------------------- hazard perception
def hazard():
    slug = "hazard-perception-test-scoring-explained"
    body = f"""
<p class="lead">Hazard perception is the part of the theory test that learners understand least. You can see every hazard and still fail — because the test isn't about <em>whether</em> you spot it, it's about <em>when</em>. Try the demo below to feel how the scoring window works.</p>
<div class="rx-tool" data-rx="hazard" data-reveal="up">
  <div class="rx-tool__head"><div class="card__icon">{icon('bolt')}</div><div><h3>Scoring window demo</h3><p>A 9-second "clip". A hazard starts to develop at about 3 seconds — click as early as you can once it does.</p></div></div>
  <div class="rx-hp"><div class="rx-hp__bar"><div class="rx-hp__win" aria-hidden="true"><span>5</span><span>4</span><span>3</span><span>2</span><span>1</span></div><span class="rx-hp__head"></span></div>
  <div class="rx-hp__ctl"><button class="btn btn--red js-hpgo" type="button">▶ Start clip</button><button class="btn btn--ghost js-hpclick" type="button" disabled>👆 Hazard! (click)</button></div>
  <p class="rx-hp__res js-hpres" aria-live="polite"></p></div>
  <p class="note">The coloured window shows the five scoring bands. In the real test you can't see the window — you have to judge the moment a hazard begins to develop.</p>
</div>
<h2>How the hazard perception test is scored</h2>
<div class="rx-figs" data-stagger=".06"><div class="rx-fig" data-reveal="up"><b>14</b><span>video clips</span></div><div class="rx-fig" data-reveal="up"><b>15</b><span>scored hazards (one clip has two)</span></div><div class="rx-fig" data-reveal="up"><b>75</b><span>maximum score</span></div><div class="rx-fig" data-reveal="up"><b>44</b><span>pass mark</span></div></div>
<p>Each clip contains at least one <b>developing hazard</b> — something that would make you take action, such as slowing down, stopping or changing direction. One clip contains two. Each developing hazard has a scoring window: click early in the window and you score 5; the later you click, the lower the score, down to 1. Click before the window opens or after it closes and you score 0 for that hazard.</p>
<h2>Why clicking a lot can score zero</h2>
<p>If you click continuously or in a pattern, the test detects it and you score zero for that clip. Clicking two or three times when you see a potential hazard and again as it develops is normal and fine. Clicking every second "just in case" isn't.</p>
<h2>Potential hazard vs developing hazard</h2>
<p>A <b>potential hazard</b> is something that <em>might</em> become a problem: a pedestrian on the pavement, a parked van, a car waiting at a side road. A <b>developing hazard</b> is one that's actually becoming a problem: the pedestrian steps towards the kerb, the van's indicator comes on, the car starts to edge out. Points come from spotting the moment the potential hazard starts to develop.</p>
<div class="callout callout--info"><b>A good habit:</b> click once when you see a potential hazard, and again the moment it starts to change. That usually lands at least one click early in the scoring window without looking like a pattern.</div>
<h2>The other half: the multiple-choice questions</h2>
<p>The theory test starts with 50 multiple-choice questions in 57 minutes; the pass mark is 43. Three questions are based on a short video case study. You need to pass both parts at the same sitting. The test costs £23 and your pass certificate lasts two years.</p>
<h2>Real hazards on Greater Manchester roads</h2>
<p>The clips are filmed all over Britain, but the hazards are the same ones you'll meet here: a bus pulling out from a stop on Wilmslow Road, a cyclist moving out to pass parked cars, a tram approaching a crossing, a delivery driver's door opening in a narrow terraced street, a child running for an ice-cream van. On lessons we commentate hazards aloud — "car edging out on the left, ready to slow" — which trains exactly the skill this test measures.</p>
<p>Practise with our free <a href="{ROOT}hazard-game.html">hazard game</a> and <a href="{ROOT}theory-quiz.html">theory quiz</a>, and read about <a href="{ROOT}knowledge/theory-test-greater-manchester.html">theory test centres in Greater Manchester</a>.</p>"""
    faqs = [("What is the pass mark for hazard perception?", "44 out of 75."),
            ("How many clips are in the hazard perception test?", "14 video clips containing 15 developing hazards — one clip has two."),
            ("How is hazard perception scored?", "Each developing hazard has a scoring window. Clicking early in the window scores 5, then 4, 3, 2 and 1. Clicking outside the window scores 0."),
            ("Can you click too much in hazard perception?", "Yes. Clicking continuously or in a pattern scores zero for that clip."),
            ("What is the theory test pass mark?", "43 out of 50 for the multiple-choice part and 44 out of 75 for hazard perception. You must pass both.")]
    return shell(_path(slug), "Hazard Perception Test Scoring Explained (5-4-3-2-1) | SQ Driving School", "Interactive", [SECTION, ("Hazard perception", _path(slug))],
                 "How the hazard perception test is scored", "The 5-4-3-2-1 scoring window, why clicking too much scores zero, potential vs developing hazards — with an interactive timing demo.",
                 [("44/75", "pass mark"), ("14", "clips"), ("5", "points per hazard max"), ("£23", "theory test fee")],
                 ["Each hazard has a scoring window — earlier clicks score up to 5.", "Clicking constantly or in a pattern scores zero for that clip.", "Points come from spotting the moment a hazard starts to develop.", "You must pass both the multiple-choice (43/50) and hazard perception (44/75)."],
                 body, faqs, [GOV["hpt"], GOV["pass"], GOV["mcq"]], _related(slug, [("hazard-game.html", "Practice", "Free hazard game", "Train your reactions in the browser.")]))


# ---------------------------------------------------------------- glossary
GLOSSARY = [
    ("ADI", "Approved Driving Instructor — a fully qualified instructor registered with the DVSA. Look for the green badge on the windscreen."),
    ("Advanced stop line", "A second white stop line at traffic lights with a box for cyclists in front of traffic. Stop at the first line when the lights are red."),
    ("Anticipation", "Reading the road ahead and predicting what others will do so you can act early and smoothly."),
    ("Biting point", "The point where the clutch plates meet and the car wants to move. Finding it smoothly is the key to clutch control in a manual car."),
    ("Blind spot", "Areas around the car you can't see in your mirrors. Check them with a look over your shoulder before moving off or changing lanes."),
    ("Box junction", "A yellow criss-cross area. Don't enter unless your exit is clear — except when turning right and only blocked by oncoming traffic or others turning right."),
    ("Bus gate", "A short stretch of road only buses (and sometimes taxis and cycles) may use. Manchester has several, including on Oxford Road."),
    ("Bus lane", "A lane for buses and other permitted vehicles during the times on the blue sign. No times shown means it operates all day."),
    ("Cockpit drill", "The checks you do before driving: doors, seat, steering, seatbelt, mirrors (often called DSSSM)."),
    ("Clutch control", "Using the clutch around the biting point to move very slowly — for manoeuvres, queues and hill starts."),
    ("Coasting", "Rolling with the clutch down or in neutral. It reduces control and is marked as a fault."),
    ("Commentary driving", "Saying aloud what you see and plan to do. A great way to improve hazard awareness."),
    ("Creep and peep", "Edging forward slowly at a junction with limited view until you can see properly."),
    ("Crossroads", "Where two roads cross. Watch for vehicles turning right in front of you and make sure of priority."),
    ("Dangerous fault", "A fault involving actual danger to you, the examiner, the public or property. One dangerous fault is a fail."),
    ("Defensive driving", "Driving so you're ready for the mistakes of others — space, speed and observation."),
    ("DL25", "The marking sheet examiners use on the practical test to record faults."),
    ("Dry steering", "Turning the steering wheel while the car is stationary. It wears tyres and is best avoided."),
    ("Dual carriageway", "A road with a central reservation separating the two directions. The national limit for cars is 70mph."),
    ("Dual controls", "A second brake (and often clutch) pedal on the instructor's side. All SQ lesson cars have them."),
    ("Driving fault", "A minor fault. You can have up to 15 and still pass, as long as none is serious or dangerous."),
    ("DVLA", "Driver and Vehicle Licensing Agency — issues licences and handles medical conditions and eyesight issues."),
    ("DVSA", "Driver and Vehicle Standards Agency — runs theory and practical tests and regulates instructors."),
    ("Emergency stop", "Stopping quickly and under control when the examiner signals. Around one test in three includes it."),
    ("Eyesight check", "Reading a number plate from 20 metres at the start of the practical test."),
    ("Filter arrow", "A green arrow at traffic lights that lets you go in the arrow's direction even while the main light is red."),
    ("Forward bay park", "Driving forwards into a parking bay and reversing out. One of the test manoeuvres."),
    ("Give way", "Let traffic on the major road go first. Shown by a triangle sign and a broken double white line."),
    ("Hazard perception", "The video part of the theory test: 14 clips, 75 points, pass mark 44."),
    ("Hierarchy of road users", "The 2022 Highway Code principle that those who can do most harm have the most responsibility to look out for others."),
    ("Hill start", "Moving off uphill without rolling back, using clutch control and the parking brake."),
    ("Independent driving", "About 20 minutes of the test where you follow a sat-nav or road signs without turn-by-turn directions."),
    ("Junction observations", "Looking properly before emerging at a junction. Consistently one of the most common reasons for failing."),
    ("Kickdown", "In an automatic, pressing the accelerator hard to make the gearbox change down for quick acceleration."),
    ("L plates", "Red L on a white background, front and back. Required whenever a learner drives."),
    ("LADA", "Look, Assess, Decide, Act — a routine for approaching junctions and hazards."),
    ("Lane discipline", "Staying in the correct lane and following lane markings, especially on roundabouts and multi-lane roads."),
    ("Meeting traffic", "Dealing with oncoming vehicles where the road is narrowed, e.g. by parked cars. Decide early who has room."),
    ("Mini-roundabout", "A painted or slightly raised roundabout. Give way to traffic from the right; you may need to go over the markings carefully."),
    ("Mirror–Signal–Manoeuvre (MSM)", "The core routine for any change of speed or direction."),
    ("Mock test", "A full practice test under exam conditions with your instructor. SQ learners do at least one."),
    ("MSPSL", "Mirrors, Signal, Position, Speed, Look — an expanded MSM routine for junctions."),
    ("National speed limit", "Shown by a white circle with a black diagonal stripe: 60mph on single carriageways and 70mph on dual carriageways for cars."),
    ("Neutral", "No gear engaged. In an automatic, N. Don't sit in neutral to coast."),
    ("Normal driving position", "About a metre from the kerb in normal conditions — not hugging it, not in the middle."),
    ("Observations", "All the looking you do: mirrors, blind spots, junctions, ahead. Examiners watch your head movements."),
    ("Parallel park", "Reversing into a space behind a parked car, finishing close and parallel to the kerb within about two car lengths."),
    ("Pass Plus", "An optional post-test course covering motorways, night driving, rural roads and more."),
    ("PDI", "Potential Driving Instructor — someone training to become an ADI. May hold a pink trainee licence."),
    ("Pegasus crossing", "A crossing with extra-high push buttons for horse riders, sometimes alongside a toucan crossing."),
    ("Pelican crossing", "A light-controlled crossing with a flashing amber phase — give way to pedestrians still crossing."),
    ("POM", "Prepare, Observe, Move — the routine for moving off."),
    ("Positioning", "Where you place the car on the road. Poor positioning on right turns and roundabouts is a common fault."),
    ("Progress", "Driving at an appropriate speed and not hesitating unnecessarily. Being too slow can be a fault."),
    ("Provisional licence", "The licence you need before your first lesson. Apply from 15 years 9 months."),
    ("Puffin crossing", "A light-controlled crossing where sensors detect pedestrians. No flashing amber."),
    ("Pull up on the right", "A test manoeuvre: pull up on the right side of the road, reverse about two car lengths, then rejoin traffic."),
    ("Response to signals", "Reacting correctly to traffic lights, signs, road markings and other road users' signals."),
    ("Reverse bay park", "Reversing into a parking bay — usually at the test centre car park or a supermarket."),
    ("Roundabout", "A circular junction. Give way to traffic from the right unless signs or markings say otherwise."),
    ("Serious fault", "A potentially dangerous fault, or a driving fault repeated so much it shows a habit. One serious fault is a fail."),
    ("Show me, tell me", "Two vehicle-safety questions on the test — one before you drive, one while you drive."),
    ("Signal", "Indicators, brake lights, arm signals or the horn. Signal clearly and in good time, and cancel afterwards."),
    ("Slip road", "The road used to join or leave a motorway or dual carriageway. Build up speed on the slip road to merge."),
    ("Smart motorway", "A motorway using technology to manage traffic, sometimes with the hard shoulder as a live lane. Never drive under a red X."),
    ("Spiral roundabout", "A roundabout with markings that guide you into the correct lane for your exit as you go round."),
    ("Stall", "When the engine cuts out, usually from lifting the clutch too fast. Stay calm: handbrake, neutral, restart."),
    ("Standards check", "The DVSA's periodic check on instructors' teaching. Instructors are graded A or B."),
    ("Stopping distance", "Thinking distance plus braking distance — 23m at 30mph in the dry. Try our calculator."),
    ("Tailgating", "Driving too close to the vehicle in front. Use the two-second rule."),
    ("Theory test", "50 multiple-choice questions (pass 43) and hazard perception (pass 44/75). £23."),
    ("Toucan crossing", "A light-controlled crossing shared by pedestrians and cyclists — 'two can' cross."),
    ("Tram stop", "Metrolink stops in the road: don't block the tracks, and watch for passengers crossing."),
    ("Two-second rule", "The minimum gap behind the vehicle in front on a dry road; double it in the wet."),
    ("Undue hesitation", "Waiting when it was safe to go. Repeated, it can be a serious fault."),
    ("Wheelspin", "Wheels spinning without grip, usually from too much power on a wet or icy surface."),
    ("Zebra crossing", "Black and white stripes with flashing Belisha beacons. Give way to people on the crossing — and be ready for those waiting."),
]


def glossary():
    slug = "driving-lesson-glossary"
    groups = {}
    for t, d in sorted(GLOSSARY, key=lambda x: x[0].lower()):
        groups.setdefault(t[0].upper(), []).append((t, d))
    az = "".join(f'<a href="#g-{k}">{k}</a>' for k in groups)
    secs = "".join(f'<section data-letter="{k}" id="g-{k}"><h3>{k}</h3><dl>' + "".join(f'<div data-term="{(t + " " + d).lower().replace(chr(34), "")}"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in items) + "</dl></section>" for k, items in groups.items())
    body = f"""
<p class="lead">Driving instructors and examiners have their own language. "Check your blind spot, find the bite point, POM, then MSM on approach to the mini" makes perfect sense after ten hours and none at all on lesson one. Here are {len(GLOSSARY)} terms you'll hear on lessons and on test day, explained simply.</p>
<div class="rx-tool rx-gl" data-rx="glossary" data-reveal="up">
  <div class="rx-gl__bar"><input type="search" placeholder="Search terms — e.g. clutch, roundabout, fault" aria-label="Search the glossary"><span class="note js-gcount">{len(GLOSSARY)} terms</span></div>
  <nav class="rx-gl__az" aria-label="Jump to letter">{az}</nav>
  {secs}
</div>
<h2>The terms that matter most on test day</h2>
<p>Three words decide your result: <b>driving fault</b>, <b>serious fault</b> and <b>dangerous fault</b>. Up to 15 driving faults is a pass. One serious or dangerous fault is a fail. A driving fault repeated over and over can become serious because it shows a habit — for example, missing mirror checks before every lane change.</p>
<h2>Why we teach the vocabulary</h2>
<p>Learners progress faster when they understand the instructions. Your DriveSQ Student Portal uses the same terms as the DVSA marking sheet, so "junction observations" or "response to signals: traffic lights" on your progress chart means exactly what the examiner will be looking for.</p>"""
    faqs = [("What does MSM mean in driving?", "Mirror, Signal, Manoeuvre — the routine you use before any change of speed or direction."),
            ("What does POM stand for?", "Prepare, Observe, Move — the routine for moving off safely."),
            ("What is the difference between a serious and a dangerous fault?", "A serious fault could have been dangerous; a dangerous fault involved actual danger. Either one means you fail."),
            ("How many minor faults can you get on a driving test?", "Up to 15 driving (minor) faults, with no serious or dangerous faults."),
            ("What is the biting point?", "The point where the clutch starts to connect the engine to the wheels and the car wants to move.")]
    extra = [{"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Driving lesson glossary", "url": f"{SITE}/{_path(slug)}",
              "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in GLOSSARY]}]
    return shell(_path(slug), "Driving Lesson Glossary: 80+ Terms Explained (MSM, POM…) | SQ", "Glossary", [SECTION, ("Glossary", _path(slug))],
                 "Driving lesson glossary A–Z", f"{len(GLOSSARY)} driving lesson and driving test terms explained simply — MSM, POM, biting point, serious fault, bay park, bus gate and more. Searchable.",
                 [(str(len(GLOSSARY)), "terms explained"), ("15", "driving faults allowed"), ("1", "serious fault = fail"), ("A–Z", "searchable")],
                 ["Search or jump by letter to any term.", "Up to 15 driving faults is a pass; one serious or dangerous fault is a fail.", "Routines like MSM, POM and LADA are the backbone of safe driving.", "Your DriveSQ Student Portal uses the same terms as the DVSA marking sheet."],
                 body, faqs, [GOV["test"], GOV["hc"], GOV["hpt"]], _related(slug, [("road-signs.html", "Reference", "UK road signs explained", "Every common sign and what it means.")]), extra_schema=extra)


def hub():
    cards = [(f"driving/{s}.html", c, t, d, i) for s, c, t, d, i in TOOLS] + [
        ("theory-quiz.html", "Practice", "Theory test quiz", "Free practice questions with explanations.", "quiz"),
        ("hazard-game.html", "Practice", "Hazard perception game", "Sharpen your hazard-spotting reactions.", "bolt"),
        ("postcode-checker.html", "Tool", "Postcode checker", "Check SQ covers your area and see your discount.", "pin"),
        ("road-signs.html", "Reference", "Road signs", "Common UK road signs explained.", "flag"),
        ("dashboard-lights.html", "Reference", "Dashboard warning lights", "What each warning light means.", "gear"),
        ("test-routes.html", "Local guides", "Test-route guides", "Roads, junctions and mistakes at every Greater Manchester test centre.", "road"),
        ("test-faults.html", "Test faults", "Why people fail — fault by fault", "The most common driving test faults and how to fix each one.", "target"),
        ("research.html", "Data Lab", "Driving Data Lab", "Original research on learning to drive in Greater Manchester.", "chart"),
    ]
    intro = '<p class="lead" data-reveal="up">Free, interactive tools built by SQ Driving School (part of DriveSQ) for learners in Greater Manchester. Every figure is taken from GOV.UK, the Highway Code or the DVSA — and every tool works on your phone.</p>'
    return hub_page("learner-toolkit.html", "Free Learner Driver Toolkit: Calculators & Planners | SQ Driving School", "Learner Toolkit",
                    "The learner driver toolkit.", "Free calculators, planners and guides for learner drivers in Greater Manchester — stopping distances, test-day planning, hazard perception, eyesight and more.",
                    cards, intro, [(str(len(cards)), "free tools & guides"), ("0", "sign-ups needed"), ("100%", "official sources"), ("£35", "per hour lessons")])


def all_pages():
    out = {"learner-toolkit.html": hub()}
    for fn, (s, *_r) in zip((stopping, testday, timeline, eyesight, hazard, glossary), TOOLS):
        out[_path(s)] = fn()
    return out
