from layout import *
from pages_main import postcode_form, builder

BOROUGHS = [
    ("manchester", "Manchester", ["M1", "M2", "M3", "M4", "M8", "M9", "M11", "M12", "M13", "M14", "M15", "M16", "M18", "M19", "M20", "M21", "M22", "M23", "M40", "M90"],
     "Levenshulme, Gorton, Old Trafford, Whalley Range, Didsbury, Chorlton, Fallowfield, Withington, Wythenshawe, Moss Side, Hulme, Ancoats, Cheetham Hill, Blackley and the city centre",
     "City-centre one-way systems, bus lanes, trams on shared streets, the Mancunian Way and busy multi-lane roundabouts — plus quieter residential roads to build confidence first.",
     ["Cheetham Hill", "West Didsbury"]),
    ("salford", "Salford", ["M3", "M5", "M6", "M7", "M27", "M28", "M30", "M38", "M44", "M50"],
     "Salford Quays, Pendleton, Eccles, Swinton, Worsley, Walkden, Irlam, Broughton and Little Hulton",
     "MediaCityUK's junctions, the A6 corridor, busy retail parks and the East Lancs Road.", ["Cheetham Hill", "Atherton"]),
    ("trafford", "Trafford", ["M16", "M17", "M31", "M32", "M33", "M41", "WA14", "WA15"],
     "Old Trafford, Stretford, Sale, Urmston, Flixton, Altrincham, Hale, Timperley and Partington",
     "Chester Road, Trafford Park's industrial traffic, the M60 junctions and the leafy roads of Sale and Altrincham.", ["Sale", "West Didsbury"]),
    ("stockport", "Stockport", ["SK1", "SK2", "SK3", "SK4", "SK5", "SK6", "SK7", "SK8"],
     "Stockport town centre, Heaton Moor, Reddish, Cheadle, Gatley, Bramhall, Hazel Grove, Marple, Bredbury and Romiley",
     "The A6, the town-centre gyratory, hilly residential streets and fast dual carriageways around the M60.", ["Bredbury", "West Didsbury"]),
    ("tameside", "Tameside", ["M34", "M43", "OL5", "OL6", "OL7", "SK14", "SK15", "SK16"],
     "Ashton-under-Lyne, Denton, Droylsden, Audenshaw, Hyde, Stalybridge, Dukinfield and Mossley",
     "Hill starts in Stalybridge and Mossley, Ashton's busy centre and the M60/M67 junctions.", ["Hyde", "Bredbury"]),
    ("oldham", "Oldham", ["OL1", "OL2", "OL3", "OL4", "OL8", "OL9", "M35"],
     "Oldham centre, Chadderton, Royton, Shaw, Failsworth, Lees, Hollinwood and Saddleworth",
     "Steep hills, the A62 and A627(M), and rural roads out towards Saddleworth.", ["Chadderton", "Rochdale"]),
    ("rochdale", "Rochdale", ["OL10", "OL11", "OL12", "OL15", "OL16", "M24"],
     "Rochdale centre, Heywood, Middleton, Milnrow, Littleborough and Whitworth",
     "The A627(M), M62 links, town-centre traffic and Pennine country roads.", ["Rochdale", "Chadderton"]),
    ("bury", "Bury", ["BL0", "BL8", "BL9", "M25", "M26", "M45"],
     "Bury centre, Prestwich, Whitefield, Radcliffe, Tottington and Ramsbottom",
     "The M66 and M60 junctions, Bury's ring road and the A56.", ["Bury", "Cheetham Hill"]),
    ("bolton", "Bolton", ["BL1", "BL2", "BL3", "BL4", "BL5", "BL6", "BL7"],
     "Bolton centre, Farnworth, Kearsley, Westhoughton, Horwich, Blackrod and Bromley Cross",
     "The A666 St Peter's Way, the M61 junctions and busy town-centre roundabouts.", ["Bolton", "Atherton"]),
    ("wigan", "Wigan", ["WN1", "WN2", "WN3", "WN4", "WN5", "WN6", "WN7", "M29", "M46"],
     "Wigan centre, Leigh, Atherton, Tyldesley, Hindley, Ashton-in-Makerfield, Orrell and Standish",
     "The A49, A577 and A580 East Lancs Road, plus links to the M6 and M58.", ["Atherton", "Bolton"]),
]

CENTRES = [("Cheetham Hill", "North Manchester", "City-centre style traffic, multi-lane roads and busy junctions."),
           ("West Didsbury", "South Manchester", "Mix of residential streets, main roads and roundabouts."),
           ("Sale", "Trafford", "Suburban roads, dual carriageways and roundabouts."),
           ("Bredbury", "Stockport", "Fast roads, roundabouts and M60 junctions nearby."),
           ("Chadderton", "Oldham", "Hills, main roads and town traffic."),
           ("Rochdale", "Rochdale", "Town-centre traffic and country roads."),
           ("Bolton", "Bolton", "Ring roads, roundabouts and busy town-centre junctions."),
           ("Atherton", "Wigan", "Suburban and semi-rural roads with roundabouts."),
           ("Bury", "Bury", "Ring road, main roads and roads near the M66 and M60."),
           ("Hyde", "Tameside", "Hilly roads, town centres and roads near the M60 and M67.")]


def tools():
    root = ""
    skills = ["Cockpit drill & controls", "Moving off & stopping", "Mirrors & signals (MSPSL)", "Junctions — turning left & right", "Roundabouts", "Crossroads",
              "Pedestrian crossings", "Dual carriageways", "Meeting traffic & clearance", "Parallel parking", "Bay parking", "Pulling up on the right",
              "Emergency stop", "Independent driving with sat-nav", "Following road signs", "Show me / tell me questions", "Theory test passed"]
    sk = "".join(f'<li><label><input type="checkbox"> {s}</label></li>' for s in skills)
    body = page_hero("Free tools", "Your learner toolkit.", "Calculators, checkers and planners to help you learn faster and spend less. Free, with no sign-up.", ["Tools"], root,
                     '<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--ghost btn--sm" href="#postcode">Postcode</a><a class="btn btn--ghost btn--sm" href="#area">Area finder</a><a class="btn btn--ghost btn--sm" href="#lessons">Lesson calculator</a><a class="btn btn--ghost btn--sm" href="#readiness">Readiness</a><a class="btn btn--ghost btn--sm" href="#countdown">Countdown</a><a class="btn btn--ghost btn--sm" href="#builder">Package builder</a><a class="btn btn--ghost btn--sm" href="theory-quiz.html">Theory quiz</a><a class="btn btn--ghost btn--sm" href="hazard-game.html">Hazard game</a><a class="btn btn--ghost btn--sm" href="comfort.html#plan">Comfort plan</a><a class="btn btn--ghost btn--sm" href="comfort.html#breathe">Breathing coach</a><a class="btn btn--ghost btn--sm" href="road-signs.html">Road signs</a><a class="btn btn--ghost btn--sm" href="dashboard-lights.html">Dashboard lights</a></div>')
    body += f"""<section class="section--tight"><div class="container grid grid--2" style="align-items:start">
  <div class="tool" id="postcode" data-reveal="left"><div class="tool__head"><div class="card__icon">{icon('pin')}</div><h3>Postcode checker</h3></div>{postcode_form(False, "Your postcode")}</div>
  <div class="tool" id="area" data-reveal="right"><div class="tool__head"><div class="card__icon">{icon('globe')}</div><h3>Area finder</h3></div>
    <form data-tool="area"><div class="field"><label for="area-in">Town or neighbourhood</label><div style="display:flex;gap:10px;flex-wrap:wrap"><input class="input" id="area-in" list="area-list" placeholder="e.g. Levenshulme" style="flex:1;min-width:180px"><datalist id="area-list"></datalist><button class="btn btn--red" type="submit">Find</button></div></div><div class="result" role="status" aria-live="polite"></div></form></div>
</div></section>
<section class="section" id="lessons"><div class="container" style="max-width:900px"><div class="tool neon-border" data-reveal="up">
  <div class="tool__head"><div class="card__icon">{icon('calc')}</div><div><h3>How many lessons do I need?</h3><p class="mb-0 note">Five quick questions for a personal estimate.</p></div></div>
  <form data-tool="lessons">
    <div class="field"><span class="label">1. Driving experience</span><div class="seg">
      <input type="radio" name="exp" id="e1" value="none" checked><label for="e1">None at all</label><input type="radio" name="exp" id="e2" value="some"><label for="e2">A few lessons</label>
      <input type="radio" name="exp" id="e3" value="lots"><label for="e3">Lots of lessons</label><input type="radio" name="exp" id="e4" value="failed"><label for="e4">Failed a test before</label><input type="radio" name="exp" id="e5" value="abroad"><label for="e5">Drove abroad</label></div></div>
    <div class="field"><span class="label">2. How confident are you?</span><div class="seg"><input type="radio" name="conf" id="c1" value="nervous"><label for="c1">Nervous</label><input type="radio" name="conf" id="c2" value="ok" checked><label for="c2">Okay</label><input type="radio" name="conf" id="c3" value="confident"><label for="c3">Confident</label></div></div>
    <div class="field"><span class="label">3. Gearbox</span><div class="seg"><input type="radio" name="trans" id="g1" value="Manual" checked><label for="g1">Manual</label><input type="radio" name="trans" id="g2" value="Automatic"><label for="g2">Automatic</label></div></div>
    <div class="field"><span class="label">4. Private practice with family or friends?</span><div class="seg"><input type="radio" name="practice" id="p1" value="yes"><label for="p1">Yes</label><input type="radio" name="practice" id="p2" value="no" checked><label for="p2">No</label></div></div>
    <div class="field"><span class="label">5. Hours per week</span><div class="seg"><input type="radio" name="pace" id="w2" value="2"><label for="w2">2</label><input type="radio" name="pace" id="w4" value="4" checked><label for="w4">4</label><input type="radio" name="pace" id="w6" value="6"><label for="w6">6</label><input type="radio" name="pace" id="w10" value="10"><label for="w10">10+</label></div></div>
    <button class="btn btn--red btn--block" type="submit">{icon('bolt')} Calculate my hours</button>
    <div class="result" role="status" aria-live="polite"></div>
  </form>
</div></div></section>
<section class="section section--alt" id="readiness"><div class="container"><div class="tool" data-tool="readiness" data-reveal="up">
  <div class="tool__head"><div class="card__icon">{icon('target')}</div><div><h3>Test readiness checker</h3><p class="mb-0 note">Tick each skill you can do confidently on your own.</p></div></div>
  <div class="grid grid--2" style="align-items:center">
    <ul class="checklist">{sk}</ul>
    <div class="center">
      <div class="gauge" style="margin:0 auto" data-gauge="0"><svg viewBox="0 0 320 320" aria-hidden="true"><path d="M50 250 A140 140 0 1 1 270 250" fill="none" stroke="var(--line-2)" stroke-width="14" stroke-linecap="round"/><path class="gauge__arc" d="M50 250 A140 140 0 1 1 270 250" fill="none" stroke="#ff1f1f" stroke-width="14" stroke-linecap="round" style="filter:drop-shadow(0 0 8px #ff1f1f)"/><line class="gauge__needle" x1="160" y1="160" x2="160" y2="50" stroke="#fff" stroke-width="4" stroke-linecap="round" transform="rotate(-120 160 160)"/><circle cx="160" cy="160" r="12" fill="#ff1f1f"/></svg><div class="gauge__val"><b class="js-pct">0%</b><span>test ready</span></div></div>
      <div class="progress mt-2"><span></span></div>
      <p class="js-msg mt-2" style="color:var(--white)">Tick your skills to see how close you are.</p>
      <p class="note">In the DriveSQ Student Portal your instructor rates all 23 skills for you after every lesson.</p>
    </div>
  </div>
</div></div></section>
<section class="section" id="countdown"><div class="container" style="max-width:900px"><div class="tool" data-reveal="up">
  <div class="tool__head"><div class="card__icon">{icon('calendar')}</div><div><h3>Test countdown planner</h3><p class="mb-0 note">How many hours a week do you need to be ready?</p></div></div>
  <form data-tool="countdown"><div class="grid grid--3">
    <div class="field"><label for="td">Test date</label><input class="input" type="date" id="td" required></div>
    <div class="field"><label for="hd">Hours done</label><input class="input" type="number" id="hd" name="done" min="0" value="10"></div>
    <div class="field"><label for="hn">Hours you think you need</label><input class="input" type="number" id="hn" name="need" min="2" value="40"></div>
  </div><button class="btn btn--red" type="submit">Plan it</button><div class="result" role="status" aria-live="polite"></div></form>
</div></div></section>
<section class="section section--alt" id="builder"><div class="container">{builder(root)}</div></section>
{cta(root)}"""
    return page("tools.html", "Free Learner Driver Tools | Lesson Calculator & Readiness Checker | SQ Driving School",
                "Free tools for learner drivers in Greater Manchester: postcode checker, lesson calculator, test readiness checker, test countdown and package builder.", body, root)


def postcode_page():
    root = ""
    import collections
    groups = collections.OrderedDict()
    for slug, name, codes, *_ in BOROUGHS:
        groups[name] = (slug, codes)
    cloud = ""
    for name, (slug, codes) in groups.items():
        pcs = "".join(f'<span class="pc{" pc--hot" if c in ("M16", "M18", "M19") else ""}">{c}</span>' for c in codes)
        cloud += f'<div class="card" data-reveal="up"><h3><a href="areas/{slug}.html">{name}</a></h3><div class="pc-cloud">{pcs}</div></div>'
    body = page_hero("Postcode checker", "Do we cover you?", "Type your postcode to see instantly if we cover your area — and whether you unlock our M16, M18 &amp; M19 special offer.", ["Postcode checker"], root)
    body += f"""<section class="section--tight"><div class="container" style="max-width:820px"><div class="tool neon-border" data-reveal="zoom">{postcode_form(True, "Your postcode")}</div></div></section>
<section class="section"><div class="container"><div class="section__head"><div class="eyebrow">Coverage</div><h2 data-split>Every Greater Manchester postcode.</h2><p class="lead">Red postcodes unlock 10 hours for £320.</p></div><div class="grid grid--2" data-stagger=".05">{cloud}</div></div></section>
{cta(root)}"""
    return page("postcode-checker.html", "Driving Lessons Postcode Checker | Greater Manchester | SQ Driving School",
                "Check if SQ Driving School covers your postcode. All Greater Manchester postcodes covered. M16, M18 and M19 get 10 hours for £320.", body, root)


def quiz_page():
    root = ""
    body = page_hero("Theory quiz", "Think you know the Highway Code?", "Ten random questions from our bank of 40. Get instant answers and explanations. Score 8 or more for a celebration.", ["Theory quiz"], root)
    body += f"""<section class="section--tight"><div class="container" style="max-width:860px"><div class="tool neon-border" data-tool="quiz" data-reveal="up">
  <div class="js-stage">
    <div class="quiz__meta"><span class="js-meta">Question 1 / 10</span><span class="js-score">Score 0</span></div>
    <div class="progress mb-2"><span></span></div>
    <div class="quiz__q" aria-live="polite"></div>
    <div class="quiz__opts"></div>
    <div class="quiz__explain" role="status"></div>
    <div class="mt-2"><button class="btn btn--red js-next hide" type="button">Next question →</button></div>
  </div>
  <div class="js-end hide center">
    <div class="eyebrow">Your score</div>
    <div class="offer__price js-final" style="color:var(--white)">0 / 10</div>
    <p class="lead js-verdict" style="margin:14px auto"></p>
    <div class="btn-row" style="justify-content:center"><button class="btn btn--red js-restart" type="button">Play again</button><a class="btn btn--ghost" href="{STUDENT}" target="_blank" rel="noopener">Full mock test in the Student Portal ↗</a></div>
  </div>
</div>
<p class="note mt-2">Practice questions written by SQ Driving School based on the Highway Code. These are not official DVSA questions. Book your real theory test on <a class="red" href="https://www.gov.uk/book-theory-test" target="_blank" rel="noopener">GOV.UK</a>.</p>
</div></section>
{cta(root)}"""
    return page("theory-quiz.html", "Free Theory Test Quiz | Highway Code Practice | SQ Driving School",
                "Free Highway Code theory quiz: 40 questions, 10 per round, with instant explanations. Practise for your UK driving theory test.", body, root)


def hazard_page():
    root = ""
    body = page_hero("Spot the hazard", "See it before it happens.", "Three road scenes. 20 seconds each. Click every hazard you can see — the faster you spot it, the more points you score. Wrong clicks cost a point.", ["Hazard game"], root)
    body += f"""<section class="section--tight"><div class="container"><div class="tool neon-border" data-tool="hazard" data-reveal="up">
  <div class="hud"><span class="chip">Scene <b class="js-scene">1/3</b></span><span class="chip">Found <b class="js-found">0/3</b></span><span class="chip">Time <b class="js-time">20s</b></span><span class="chip">Score <b class="js-hscore">0</b></span><button class="btn btn--red btn--sm js-hstart" type="button">{icon('bolt')} Start</button></div>
  <div class="hazard-stage"><svg viewBox="0 0 800 500" role="img" aria-label="Road scene — click the hazards"></svg></div>
  <div class="grid grid--2 mt-2"><div><h3>Your hazard log</h3><ol class="js-log" style="color:var(--grey)"></ol></div>
  <div class="js-hend hide"><div class="eyebrow">Final score</div><div class="offer__price js-hfinal" style="color:var(--white)">0</div><p class="js-hsum"></p><a class="btn btn--ghost" href="{STUDENT}" target="_blank" rel="noopener">Practise more in the Student Portal ↗</a></div></div>
</div><p class="note mt-2">A fun training game, not the official DVSA hazard perception test, which uses video clips.</p></div></section>
{cta(root)}"""
    return page("hazard-game.html", "Spot the Hazard Game | Hazard Perception Practice | SQ Driving School",
                "Free spot-the-hazard game for learner drivers. Click the hazards in three road scenes before time runs out.", body, root)


def centres_page():
    root = ""
    cards = "".join(f'<a class="card" href="knowledge/test-centre-{a.lower().replace(" ", "-")}.html" data-reveal="up" data-tilt="6"><div class="card__icon">{icon("flag")}</div><span class="discount__who">{b}</span><h3>{a}</h3><p>{c}</p><span class="red mono" style="font-size:.8rem">FULL GUIDE →</span></a>' for a, b, c in CENTRES)
    steps = [("Pass your theory test", "You need your theory test pass before you can book your practical."),
             ("Get ready with your instructor", "Use your portal readiness checklist and a mock test to know you're ready."),
             ("Book on GOV.UK", "Book your own practical test on the official GOV.UK service — never pay a third party for a slot."),
             ("Choose your centre", "Waiting times vary between centres. Check a few nearby centres on GOV.UK."),
             ("Tell us your date", "Message us your test date and centre so we can plan lessons and test-route practice.")]
    st = "".join(f'<div class="step" data-reveal="left"><div class="step__dot">{i+1}</div><div class="step__body"><h3>{a}</h3><p class="mb-0">{b}</p></div></div>' for i, (a, b) in enumerate(steps))
    body = page_hero("Test centre guide", "Greater Manchester test centres.", "Which centre is near you, what the roads are like, and how to book your own test.", ["Test centres"], root)
    body += f"""<section class="section--tight"><div class="container"><div class="grid grid--4" data-stagger=".05">{cards}</div><p class="note mt-2">Centres and waiting times change. Always check the official <a class="red" href="https://www.gov.uk/book-driving-test" target="_blank" rel="noopener">GOV.UK booking service</a>.</p></div></section>
<section class="section section--alt"><div class="container split"><div data-reveal="left"><div class="eyebrow">Booking your test</div><h2 data-split>How to book your own test.</h2><p class="lead">Learners book their own practical tests on GOV.UK. Here's how we help.</p><a class="btn btn--red mt-2" href="https://www.gov.uk/book-driving-test" target="_blank" rel="noopener">Book on GOV.UK ↗</a></div><div class="timeline"><div class="timeline__fill"></div>{st}</div></div></section>
<section class="section"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">Test day</div><h2 data-split>What to bring.</h2></div>
<ul class="ticks" data-reveal="up"><li><span><b>Your UK provisional driving licence</b> (photocard)</span></li><li><span><b>Glasses or contact lenses</b> if you need them — you'll read a number plate from 20 metres</span></li><li><span><b>An SQ car</b> — we can arrange the car and a warm-up lesson before your test</span></li><li><span><b>Arrive early</b> — late arrivals may lose their test</span></li></ul>
<p>Read our <a class="red" href="guides/test-day-checklist.html">full test day checklist</a>.</p></div></section>
{cta(root)}"""
    return page("test-centres.html", "Driving Test Centres Greater Manchester | How to Book | SQ Driving School",
                "Guide to Greater Manchester driving test centres: Cheetham Hill, West Didsbury, Sale, Bredbury, Chadderton, Rochdale, Bolton and Atherton — and how to book your own test.", body, root)


def portal_page():
    root = ""
    feats = [("chart", "Live progress tracking", "A competency ring and 23 practical skills, each rated Not Started, Introduced, Developing or Independent after every lesson."),
             ("book", "Theory study library", "Eight theory sections — road signs, rules of the road, hazards, alcohol & drugs, vehicle safety, eco-driving and first aid."),
             ("quiz", "Mock theory tests", "A full 50-question mock, timed at 57 minutes with a 43/50 pass mark — or Practice Mode with instant feedback."),
             ("chat", "Instructor messaging", "A direct chat with your instructor, plus one-tap WhatsApp and call buttons."),
             ("calendar", "Confirm & reschedule", "Confirm attendance in one tap, or request a new time with a reason — no phone tag."),
             ("target", "Test readiness checklist", "Hours, manoeuvres, junctions, independent driving, theory and instructor sign-off — it ticks itself off."),
             ("clock", "Test countdowns", "Set your theory and practical dates and two live countdowns appear on your home screen."),
             ("star", "Achievements", "Eight badges — First Lesson, 10 Hours, All Manoeuvres, Test Ready and more — to keep you motivated."),
             ("phone-app", "Works on any device", "No app store needed. Add it to your home screen and it opens like a native app.")]
    f = "".join(f'<article class="card" data-reveal="up" data-tilt="6"><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p class="mb-0">{d}</p></article>' for i, t, d in feats)
    instr = [("users", "Pupil list in one place", "Every learner's details, hours and progress in one dashboard."),
             ("calendar", "Bookings & availability", "Lessons and availability tracked without paper diaries."),
             ("chart", "Progress notes", "Rate skills and leave written notes after every lesson — the learner sees them instantly."),
             ("chat", "Direct communication", "Message learners and DriveSQ management from the portal.")]
    ins = "".join(f'<article class="card" data-reveal="up"><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p class="mb-0">{d}</p></article>' for i, t, d in instr)
    cmp_rows = [("Lesson record", "Paper diary, if remembered", "Every lesson logged automatically"),
                ("Knowing your progress", "“You're getting there”", "23 skills rated after every lesson"),
                ("Theory revision", "Buy a book or app", "Free theory library and mock tests"),
                ("Contacting your instructor", "Missed calls and texts", "In-app chat, confirm and reschedule"),
                ("Am I ready for my test?", "A guess", "A self-updating readiness checklist"),
                ("Cost", "—", "£0 — free for every SQ learner")]
    cm = "".join(f"<tr><td>{a}</td><td>{b}</td><td class='red'>{c}</td></tr>" for a, b, c in cmp_rows)
    how = [("Clarity removes fear", "Learners who can see their progress in black and white go into lessons calmer. Calm drivers make better decisions — and better decisions pass tests."),
           ("Revision between lessons", "Each practical topic links to a written guide once your instructor has taught it, so lessons build on each other instead of starting from scratch."),
           ("No wasted lesson time", "Your instructor opens your record before every lesson and picks up exactly where you left off."),
           ("Honest test timing", "The readiness checklist means you book your test when the data says you're ready, not when you hope you are."),
           ("Theory sorted early", "Unlimited mock theory tests with a section-by-section breakdown show exactly what to revise.")]
    hw = "".join(f'<div class="step" data-reveal="left"><div class="step__dot">{i+1}</div><div class="step__body"><h3>{a}</h3><p class="mb-0">{b}</p></div></div>' for i, (a, b) in enumerate(how))
    body = page_hero("DriveSQ Student Portal", "The app that teaches between lessons.", "SQ Driving School uses the DriveSQ Student Portal. It's free for every SQ learner, works on any phone, and connects you to your instructor after every lesson.", ["Student Portal"], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="{STUDENT}" target="_blank" rel="noopener">{icon("lock")} Student login ↗</a><a class="btn btn--ghost" href="{INSTRUCTOR}" target="_blank" rel="noopener">{icon("users")} Instructor login ↗</a></div>')
    body += f"""<section class="section--tight"><div class="container split">
  <div data-reveal="left">{phone_mock()}</div>
  <div data-reveal="right"><div class="stats" style="grid-template-columns:repeat(2,1fr)">
    <div class="stat"><div class="stat__num"><span class="red">£</span><span data-count="0">0</span></div><div class="stat__label">cost to SQ learners</div></div>
    <div class="stat"><div class="stat__num" data-count="23">0</div><div class="stat__label">practical skills tracked</div></div>
    <div class="stat"><div class="stat__num" data-count="50">0</div><div class="stat__label">question mock theory test</div></div>
    <div class="stat"><div class="stat__num" data-count="24" data-suffix="/7">0</div><div class="stat__label">access from any device</div></div>
  </div><p class="mt-2">Powered by <b>DriveSQ</b>, the same platform DriveSQ's own learners use. Your instructor links your account at your first lesson.</p></div>
</div></section>
<section class="section"><div class="container"><div class="section__head center"><div class="eyebrow">For students</div><h2 data-split>Everything you need to pass.</h2></div><div class="grid grid--3" data-stagger=".05">{f}</div></div></section>
<section class="section section--alt"><div class="container split"><div data-reveal="left"><div class="eyebrow">How it helps you pass</div><h2 data-split>Why portal learners progress faster.</h2><p class="lead">Learning to drive used to rely on memory and guesswork. The portal replaces both with information.</p></div><div class="timeline"><div class="timeline__fill"></div>{hw}</div></div></section>
<section class="section"><div class="container"><div class="section__head center"><div class="eyebrow">For instructors</div><h2 data-split>The DriveSQ Instructor Portal.</h2><p class="lead">Less admin, more teaching. Instructors manage pupils, bookings and progress in one dashboard — so every lesson is better planned.</p></div><div class="grid grid--4" data-stagger=".06">{ins}</div>
<div class="center mt-3"><a class="btn btn--ghost" href="{INSTRUCTOR}" target="_blank" rel="noopener">Instructor login ↗</a></div></div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">Old way vs SQ way</div><h2 data-split>Learning with and without the portal.</h2></div>
<div class="table-wrap" data-reveal="up"><table class="table"><thead><tr><th></th><th>Typical driving school</th><th>SQ + DriveSQ Portal</th></tr></thead><tbody>{cm}</tbody></table></div></div></section>
<section class="section"><div class="container"><div class="section__head center"><div class="eyebrow">Pass stories</div><h2 data-split>Passed with the portal?</h2><p class="lead">We only share real stories from real learners, with their permission. As SQ learners pass, their stories will appear here.</p></div>
<div class="center" data-reveal="up"><a class="btn btn--red" data-wa="Hi SQ! I passed my test and the DriveSQ portal helped — I'd like to share my story." href="https://wa.me/{WA}">{icon('star')} Share your pass story</a></div></div></section>
{cta(root, "Get your free portal access.", "Book your first lesson and your instructor will set up your DriveSQ Student Portal account.")}"""
    return page("student-portal.html", "DriveSQ Student Portal | Free Learner App | SQ Driving School",
                "Every SQ Driving School learner gets the DriveSQ Student Portal free: progress tracking, theory library, mock tests, instructor messaging and test readiness.", body, root)


def areas_page():
    root = ""
    cards = "".join(f'<a class="card" href="areas/{s}.html" data-reveal="up" data-tilt="8"><div class="card__icon">{icon("pin")}</div><h3>{n}</h3><p>{d.split(",")[0]}, {d.split(",")[1].strip()} and more</p><div class="pc-cloud">{"".join(f"<span class={chr(39)}pc{(chr(32)+"pc--hot") if c in ("M16","M18","M19") else ""}{chr(39)}>{c}</span>" for c in codes[:6])}</div></a>' for s, n, codes, d, *_ in BOROUGHS)
    body = page_hero("Areas we cover", "All of Greater Manchester.", "Ten boroughs, every neighbourhood. Door-to-door pick-up from home, college, university or work.", ["Areas"], root)
    body += f"""<section class="section--tight"><div class="container"><div class="grid grid--3" data-stagger=".05">{cards}</div></div></section>
<section class="section"><div class="container" style="max-width:820px"><div class="tool neon-border" data-reveal="up">{postcode_form(True, "Check your postcode")}</div></div></section>
{cta(root)}"""
    return page("areas.html", "Driving Lessons Across Greater Manchester | Areas Covered | SQ Driving School",
                "SQ Driving School covers all 10 Greater Manchester boroughs: Manchester, Salford, Trafford, Stockport, Tameside, Oldham, Rochdale, Bury, Bolton and Wigan.", body, root)


def borough_page(b):
    slug, name, codes, districts, roads, centres = b
    root = "../"
    has_offer = any(c in ("M16", "M18", "M19") for c in codes)
    offer_html = ""
    if has_offer:
        hot = ", ".join(c for c in codes if c in ("M16", "M18", "M19"))
        offer_html = f'<section class="section--tight"><div class="container"><div class="offer" data-reveal="zoom"><div class="eyebrow">Special offer in {name}</div><h2>10 hours for <span class="glow-text">£320</span></h2><div class="offer__codes">{"".join(f"<span class={chr(39)}offer__code{chr(39)}>{c}</span>" for c in hot.split(", "))}</div><p>Learners picked up in {hot} save £30 on a 10-hour block.</p><a class="btn btn--red" href="{root}offer-m16-m18-m19.html">See offer</a></div></div></section>'
    pcs = "".join(f'<span class="pc{" pc--hot" if c in ("M16", "M18", "M19") else ""}">{c}</span>' for c in codes)
    others = "".join(f'<a class="chip" href="{x[0]}.html">{x[1]}</a>' for x in BOROUGHS if x[0] != slug)
    body = page_hero(f"{name} · Greater Manchester", f"Driving lessons in {name}.", f"Manual and automatic driving lessons across {name} — 2-hour lessons £70, 10 hours £350 (£320 for NHS staff &amp; students). Free DriveSQ Student Portal.", [f'<a href="{root}areas.html">Areas</a>', name], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" data-wa="Hi! I\'d like driving lessons in {name}." href="https://wa.me/{WA}">{icon("wa")} Book in {name}</a><a class="btn btn--ghost" href="{root}prices.html">Prices</a></div>')
    body += f"""{offer_html}
<section class="section"><div class="container split">
  <div data-reveal="left"><div class="eyebrow">Where we teach</div><h2 data-split>Every corner of {name}.</h2><p class="lead">We pick up from {districts}.</p><div class="pc-cloud mt-2">{pcs}</div></div>
  <div data-reveal="right"><div class="card"><div class="card__icon">{icon('road')}</div><h3>Local roads we'll master</h3><p>{roads}</p><h3 class="mt-2">Nearby test centres</h3><p class="mb-0">{' and '.join(centres)} — see our <a class="red" href="{root}test-centres.html">test centre guide</a>.</p></div></div>
</div></section>
<section class="section section--alt"><div class="container"><div class="grid grid--3" data-stagger=".08">
  <article class="card" data-reveal="up"><div class="card__icon">{icon('pound')}</div><h3>£70 per 2 hours</h3><p class="mb-0">£35/hr standard. Single 1-hour session £40.</p></article>
  <article class="card" data-reveal="up"><div class="card__icon">{icon('heart')}</div><h3>£320 for 10 hours</h3><p class="mb-0">For NHS staff and students in {name}{" — and everyone in " + ", ".join(c for c in codes if c in ("M16","M18","M19")) if has_offer else ""}.</p></article>
  <article class="card" data-reveal="up"><div class="card__icon">{icon('phone-app')}</div><h3>Free Student Portal</h3><p class="mb-0">Track progress, revise theory and message your instructor.</p></article>
</div></div></section>
<section class="section"><div class="container" style="max-width:820px"><div class="tool neon-border" data-reveal="up">{postcode_form(True, f"Check your {name} postcode")}</div>
<div class="mt-3"><h3>Other areas</h3><div class="hero__badges">{others}</div></div></div></section>
{cta(root, f"Start driving in {name}.")}"""
    schema = [{"@context": "https://schema.org", "@type": "Service", "serviceType": "Driving lessons", "provider": {"@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE},
               "areaServed": {"@type": "AdministrativeArea", "name": name}, "offers": {"@type": "Offer", "price": "70", "priceCurrency": "GBP", "description": "2-hour driving lesson"}}]
    return page(f"areas/{slug}.html", f"Driving Lessons {name} | Manual & Automatic | SQ Driving School",
                f"Driving lessons in {name}, Greater Manchester. 2-hour lessons £70, 10 hours £350 or £320 for NHS & students. Free DriveSQ Student Portal.", body, root, active="areas.html", schema=schema)


FAQS = [
    ("Prices", [
        ("How much are your driving lessons?", "Our standard lesson is 2 hours for £70 (£35/hr). A single 1-hour session is £40. A 10-hour block is £350."),
        ("Why is the minimum lesson 2 hours?", "Two hours gives time to warm up, learn a new skill and practise it properly. If you only want one hour, a single session is £40."),
        ("Do automatic lessons cost more?", "No — our prices are the same for manual and automatic."),
        ("How do I pay?", "Message us on WhatsApp and we'll explain payment options. Block bookings are paid in advance."),
    ]),
    ("Discounts", [
        ("Who gets 10 hours for £320?", "NHS staff, students, and learners picked up in M16, M18 or M19."),
        ("What proof do I need?", "NHS: ID badge, NHS email or payslip. Students: valid student ID or enrolment letter. Postcode offer: your pick-up address."),
        ("Can I combine discounts?", "No — one discount per 10-hour block."),
    ]),
    ("Lessons", [
        ("Which areas do you cover?", "All 10 Greater Manchester boroughs. Use our postcode checker to confirm."),
        ("Do you pick up from home?", "Yes — from home, college, university or work within our area."),
        ("Can I learn on the motorway?", "Yes. Learners can drive on motorways with an approved instructor in a dual-controlled car."),
        ("I'm really nervous. Can you help?", "Absolutely. We go at your pace, start on quiet roads, and the Student Portal shows how far you've come."),
        ("Do you offer intensive courses?", "Yes — 10 to 40 hours over 1 to 4 weeks. See our intensive page and course planner."),
    ]),
    ("Student Portal", [
        ("What is the DriveSQ Student Portal?", "A free online app for every SQ learner, powered by DriveSQ. It tracks 23 skills, has a theory library, mock tests and instructor messaging."),
        ("Do I need to download it?", "No. It works in your browser on any device, and you can add it to your home screen."),
        ("How do I get access?", "Your instructor sets up your account at your first lesson."),
    ]),
    ("Tests", [
        ("Do you book my driving test?", "You book your own practical test on GOV.UK. We help you plan when and where — see our test centre guide."),
        ("Can I use your car for my test?", "Yes — message us to arrange the car and a warm-up lesson for test day."),
        ("What if I fail?", "It happens. You can book another test, and we'll focus lessons on the faults from your test report."),
    ]),
    ("About SQ", [
        ("Who owns SQ Driving School?", "SQ Driving School is a brand owned and managed by DriveSQ."),
        ("Who built this website?", "This website was crafted by Mohammed Qaim Abbas and built by SQ Websites."),
    ]),
]


def faq_page():
    root = ""
    html = ""
    allq = []
    for cat, qs in FAQS:
        html += f'<h2 class="mt-3" data-reveal="up" style="font-size:1.6rem">{cat}</h2><div class="faq">'
        for q, a in qs:
            html += f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>'
            allq.append((q, a))
        html += "</div>"
    schema = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in allq]}]
    body = page_hero("FAQ", "Questions, answered.", "Can't find yours? Ask our chat assistant (bottom right) or message us on WhatsApp.", ["FAQ"], root)
    body += f'<section class="section--tight"><div class="container" style="max-width:900px">{html}</div></section>{cta(root)}'
    return page("faq.html", "Driving Lessons FAQ | Prices, Discounts & Tests | SQ Driving School",
                "Answers about SQ Driving School prices, NHS and student discounts, lessons, the DriveSQ Student Portal and driving tests in Greater Manchester.", body, root, schema=schema)


def contact_page():
    root = ""
    body = page_hero("Contact", "Let's get you driving.", "WhatsApp is the fastest way to reach us. Or fill in the form — it opens WhatsApp with your message ready to send.", ["Contact"], root)
    body += f"""<section class="section--tight"><div class="container grid grid--2" style="align-items:start">
  <div data-reveal="left">
    <a class="card" style="display:block;margin-bottom:18px" data-wa="Hi SQ Driving School!" href="https://wa.me/{WA}"><div class="card__icon">{icon('wa')}</div><h3>WhatsApp</h3><p class="mb-0 mono">{PHONE}</p></a>
    <a class="card" style="display:block;margin-bottom:18px" href="tel:{TEL}"><div class="card__icon">{icon('phone')}</div><h3>Call</h3><p class="mb-0 mono">{PHONE}</p></a>
    <div class="card"><div class="card__icon">{icon('pin')}</div><h3>Area</h3><p class="mb-0">All of Greater Manchester — door-to-door pick-up.</p></div>
  </div>
  <div class="tool neon-border" data-reveal="right">
    <div class="tool__head"><div class="card__icon">{icon('chat')}</div><h3>Send an enquiry</h3></div>
    <form data-tool="contact">
      <div class="field"><label for="cn">Name</label><input class="input" id="cn" name="Name" autocomplete="name" required></div>
      <div class="field"><label for="cp">Postcode</label><input class="input" id="cp" name="Postcode" autocomplete="postal-code"></div>
      <div class="field"><label for="cg">Gearbox</label><select class="select" id="cg" name="Gearbox"><option>Manual</option><option>Automatic</option><option>Not sure</option></select></div>
      <div class="field"><label for="ci">I'm interested in</label><select class="select" id="ci" name="Interested in"><option>2-hour lessons (£70)</option><option>10-hour block (£350)</option><option>NHS discount (£320)</option><option>Student discount (£320)</option><option>M16/M18/M19 offer (£320)</option><option>Intensive course</option><option>Single 1-hour session (£40)</option><option>Something else</option></select></div>
      <div class="field"><label for="cm">Message</label><textarea class="textarea" id="cm" name="Message" placeholder="Experience, availability, test date…"></textarea></div>
      <button class="btn btn--red btn--block" type="submit">{icon('wa')} Send via WhatsApp</button>
      <p class="note mt-1 mb-0">Nothing is stored on this website. Your message opens in WhatsApp for you to send.</p>
    </form>
  </div>
</div></section>"""
    return page("contact.html", "Contact SQ Driving School | WhatsApp 07352 932003", "Contact SQ Driving School on WhatsApp or call 07352 932003. Driving lessons across Greater Manchester.", body, root)


def about_page():
    root = ""
    vals = [("bolt", "Fast & modern", "Two-hour lessons, digital progress tracking and tools no other school offers."),
            ("pound", "Honest", "Every price on the website. Real reviews only. No made-up pass rates."),
            ("heart", "Fair", "Discounts for NHS staff, students and local communities."),
            ("shield", "Safe", "We teach drivers for life, not just for test day.")]
    v = "".join(f'<article class="card" data-reveal="up"><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p class="mb-0">{d}</p></article>' for i, t, d in vals)
    body = page_hero("About", "The SQ story.", "SQ Driving School is a new brand from DriveSQ, built to give Greater Manchester a faster, clearer and more modern way to learn to drive.", ["About"], root)
    body += f"""<section class="section--tight"><div class="container split">
  <div data-reveal="left" class="center"><div class="sq-logo sq-logo--xl sq-logo--flicker">SQ</div><div class="hero__powered">Powered by <b>DriveSQ</b></div></div>
  <div data-reveal="right" class="prose"><h2 class="mt-0">Owned and managed by DriveSQ.</h2>
    <p>SQ Driving School is a brand owned and managed by <a href="https://www.drivesq.co.uk" target="_blank" rel="noopener">DriveSQ</a>. Our learners use the same DriveSQ Student Portal that DriveSQ's own learners use.</p>
    <p>We built SQ for learners who want a straight-talking, modern school: clear prices, two-hour lessons that make real progress, discounts for the people who keep Manchester running, and free tools that help you learn between lessons.</p>
    <p>Crafted by <b>Mohammed Qaim Abbas</b>.</p></div>
</div></section>
<section class="section"><div class="container"><div class="section__head center"><div class="eyebrow">What we stand for</div><h2 data-split>Four promises.</h2></div><div class="grid grid--4" data-stagger=".08">{v}</div></div></section>
{cta(root)}"""
    return page("about.html", "About SQ Driving School | A DriveSQ Brand", "SQ Driving School is a brand owned and managed by DriveSQ. Crafted by Mohammed Qaim Abbas.", body, root)


def privacy_page():
    root = ""
    body = page_hero("Privacy", "Privacy policy.", "Short and clear: this website doesn't collect your personal data.", ["Privacy"], root)
    body += f"""<section class="section--tight"><div class="container prose">
<h2>Who we are</h2><p>SQ Driving School is a brand owned and managed by DriveSQ. Contact: WhatsApp or phone {PHONE}.</p>
<h2>What this website collects</h2><p>The tools on this website (postcode checker, calculators, quiz and games) run entirely in your browser — nothing you type into them is sent to us.</p>
<p>Your browser may remember your chosen theme, language and accessibility settings using local storage on your own device. You can clear this at any time in your browser settings.</p>
<h2>Cookies and Google Analytics</h2><p>With your permission, we use <b>Google Analytics</b> and Google Ads measurement to understand how visitors use the site and which adverts work — for example, how many people open the booking form or tap our WhatsApp or call buttons. Google may set cookies and process your IP address and device information to do this.</p>
<p>These cookies are <b>off by default</b>. They're only switched on if you choose "Accept" on our cookie banner. If you choose "Reject", or ignore the banner, Google Analytics runs without cookies in a restricted mode. You can change your choice at any time with the "Cookie settings" link in the footer.</p>
<p>Google's own privacy policy explains how it uses data: <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">policies.google.com/privacy</a>.</p>
<h2>Contact forms and WhatsApp</h2><p>When you use our contact form or chat assistant, your message opens in WhatsApp for you to send. Once you send it, we receive it via WhatsApp and use it only to reply to your enquiry and arrange lessons. WhatsApp's own privacy policy applies to messages sent through WhatsApp.</p>
<h2>The DriveSQ Student Portal</h2><p>The Student Portal is operated by DriveSQ at drivesq.co.uk. Its own privacy policy applies when you use it.</p>
<h2>Third-party services</h2><p>This website loads fonts from Google Fonts and the Google tag from Google, which may receive your IP address when they load.</p>
<h2>Your rights</h2><p>Under UK GDPR you can ask what information we hold about you and ask us to correct or delete it. Message us on {PHONE}.</p>
</div></section>"""
    return page("privacy.html", "Privacy Policy | SQ Driving School", "SQ Driving School privacy policy.", body, root)


def review_page():
    root = ""
    body = page_hero("Reviews", "Our review policy.", "We only publish genuine reviews from real learners.", ["Review policy"], root)
    body += """<section class="section--tight"><div class="container prose">
<h2>How we collect reviews</h2><p>We ask learners for feedback after they finish their lessons or pass their test. Reviews are written by the learners themselves.</p>
<h2>What we publish</h2><ul><li>We never write, buy or invent reviews.</li><li>We don't offer discounts or rewards in exchange for positive reviews. If we ever offer an incentive for leaving a review of any kind, we will say so clearly next to the review.</li><li>We don't hide negative reviews to make our rating look better.</li><li>We only publish a learner's name or story with their permission.</li></ul>
<h2>Pass rates and claims</h2><p>We won't publish pass rates or statistics we can't back up with real records.</p>
<h2>Questions</h2><p>If you think a review on our website is not genuine, message us and we'll look into it.</p>
</div></section>"""
    return page("review-policy.html", "Review Policy | SQ Driving School", "How SQ Driving School collects and publishes genuine reviews.", body, root)


def notfound_page():
    root = "/"
    body = f"""<section class="hero"><div class="grid-bg" aria-hidden="true"></div><div class="speed-lines" aria-hidden="true"></div><div class="container center">
<div class="traffic" aria-hidden="true" style="margin-bottom:24px"><i></i><i></i><i></i></div>
<div class="sq-logo sq-logo--xl sq-logo--flicker">404</div><h1 style="font-size:2.4rem">Wrong turn.</h1><p class="lead">This road doesn't exist. Let's get you back on route.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn--red" href="/index.html">Back home</a><a class="btn btn--ghost" href="/postcode-checker.html">Postcode checker</a></div></div></section>"""
    return page("404.html", "Page not found | SQ Driving School", "Page not found.", body, root, noindex=True)
