"""Greater Manchester Driving Knowledge Hub — article content.

Every fact here should be checkable against the linked official sources.
Where sources disagree (pass rates, exact addresses, waiting times) we link
to the official figures instead of repeating numbers that go out of date.
"""

GOV_BOOK = ("GOV.UK — Book your driving test", "https://www.gov.uk/book-driving-test")
GOV_CHANGE = ("GOV.UK — Change your driving test", "https://www.gov.uk/change-driving-test")
GOV_THEORY = ("GOV.UK — Book your theory test", "https://www.gov.uk/book-theory-test")
GOV_FIND_CENTRE = ("GOV.UK — Find a driving test centre", "https://www.gov.uk/find-driving-test-centre")
HC = ("The Highway Code (GOV.UK)", "https://www.gov.uk/guidance/the-highway-code")
DVSA_STATS = ("DVSA — Driving test statistics", "https://www.gov.uk/government/collections/driving-tests-and-instructors-statistics")

ARTICLES = [
    # ---------------------------------------------------------------- TESTS & BOOKING
    {
        "slug": "driving-test-booking-rules-2026", "cat": "Tests & booking", "icon": "calendar",
        "title": "The 2026 driving test booking rules, explained",
        "desc": "Two changes per booking, learners must book their own test, and the three-centre rule. What changed in 2026 and what it means for Greater Manchester learners.",
        "takeaways": [
            "Since 31 March 2026 a car test booking can normally be changed only twice.",
            "Since May 2026 only the learner can book, change, cancel or swap their test — not an instructor or a third-party service.",
            "Since 9 June 2026 a booked test can only be moved to one of the three centres nearest the original booking (or back to the original centre).",
            "Cancellation-finder bots and apps are not allowed. Search for slots yourself on GOV.UK.",
        ],
        "body": """
<h2>Why the rules changed</h2>
<p>Demand for practical tests has been high across Great Britain, and the DVSA found that some booking services were buying up and reselling test slots. The 2026 changes are designed to stop slots being hoarded and resold, so more learners can book directly at the normal price.</p>
<h2>Change 1: a maximum of two changes</h2>
<p>From <b>31 March 2026</b>, a car driving test booking can normally be changed <b>twice</b> (it used to be six times). Changing the date and the centre at the same time counts as one change. Swapping a test with another learner also counts as a change.</p>
<div class="callout">Used both changes? The booking becomes fixed. If you need a different slot you'll have to cancel and book again. You still get a full refund if you cancel with at least 10 full working days' notice, and the new booking comes with a fresh allowance of two changes.</div>
<h2>Change 2: only you can manage your test</h2>
<p>From <b>May 2026</b>, only the learner can book and manage their practical test. Your instructor can't book or change it for you, and neither can a paid booking service. You'll need your provisional licence number and theory test pass number.</p>
<p>We'll still help you choose <i>when</i> to book: your DriveSQ Student Portal readiness checklist shows when you're ready, and we'll agree the date with you before you book.</p>
<h2>Change 3: the three-centre rule</h2>
<p>From <b>9 June 2026</b>, if you move a booked test to a different centre, you can only choose one of the <b>three centres nearest</b> to the one you booked, or move back to your original centre. New bookings can still be made at any centre. Sources describe the reference point slightly differently, so check the wording on GOV.UK when you change.</p>
<p>In Greater Manchester that usually still gives you sensible options — for example, a test booked at West Didsbury could typically move to a nearby centre such as Sale or Cheetham Hill. See our <a href="greater-manchester-driving-test-centres.html">guide to every Greater Manchester test centre</a>.</p>
<h2>No more cancellation bots</h2>
<p>The DVSA doesn't allow services that automatically scan the booking system for cancellations, including many apps and websites. You're still free to check GOV.UK yourself as often as you like — cancellations do appear.</p>
<h2>What this means for SQ learners</h2>
<ul><li><b>Book when you're ready, not before.</b> With only two changes, booking too early is risky.</li><li><b>Tell us your date straight away</b> so we can plan lessons, a mock test and test-route practice.</li><li><b>Pick your centre carefully</b> — moving it later is now limited.</li></ul>
""",
        "faqs": [("Can my driving instructor book my test for me?", "No. Since May 2026 only the learner can book, change, cancel or swap their practical test."),
                 ("How many times can I change my driving test?", "Normally twice per booking since 31 March 2026. After that you must cancel and rebook."),
                 ("Can I still use a cancellation app?", "The DVSA doesn't allow services that automatically scan for cancellations. You can check GOV.UK yourself.")],
        "sources": [GOV_BOOK, GOV_CHANGE, ("DVSA blog — changes to the booking system", "https://despatch.blog.gov.uk/2025/12/09/changes-to-booking-system-understanding-views-and-how-these-inform-the-planned-changes/"), ("ADINJC — DVSA booking changes 2026", "https://www.adinjc.org.uk/dvsa-driving-test-booking-changes-2026/")],
        "related": ["greater-manchester-driving-test-centres", "driving-test-waiting-times-greater-manchester", "why-learners-fail-the-driving-test"],
    },
    {
        "slug": "driving-test-waiting-times-greater-manchester", "cat": "Tests & booking", "icon": "clock",
        "title": "Driving test waiting times in Greater Manchester",
        "desc": "How to check real waiting times at Greater Manchester test centres, how to find an earlier test legally, and how to plan lessons around your date.",
        "takeaways": [
            "Waiting times change week to week. The only reliable figure is the one you see on GOV.UK when you book.",
            "Greater Manchester has around ten practical test centres — checking several can find an earlier date.",
            "Cancellations appear regularly. Checking GOV.UK yourself is allowed; automated bots are not.",
            "Book when you're nearly ready — with only two changes allowed, an early date can backfire.",
        ],
        "body": """
<h2>Why you'll see different numbers online</h2>
<p>Websites quote waiting times for Manchester centres ranging from around 10 weeks to over 20 weeks. They're usually drawn from different weeks or months, so they rarely agree. Treat any figure you read (including on driving school websites) as a rough guide only.</p>
<div class="callout callout--info">The real answer is on GOV.UK: start a booking and you'll see the earliest available dates at each centre you search.</div>
<h2>How to find an earlier test — legally</h2>
<ol><li><b>Search more than one centre.</b> There's no catchment area for the practical test. Learners in south Manchester, for example, can compare West Didsbury, Sale and Bredbury.</li>
<li><b>Check at different times of day.</b> Cancellations are released when other learners change or cancel.</li>
<li><b>Be flexible.</b> Weekday daytime slots tend to be easier to find than evenings and weekends (which also cost more).</li>
<li><b>Don't use bots or paid slot-finders.</b> They're not allowed under the 2026 rules.</li></ol>
<h2>Plan your lessons around the wait</h2>
<p>A long wait isn't wasted time. Use it to:</p>
<ul><li>Finish your manoeuvres and independent driving.</li><li>Take a <a href="../services/mock-driving-tests.html">mock test</a> 2–3 weeks before.</li><li>Keep your skills warm — a big gap with no lessons often means more lessons later.</li></ul>
<p>Use our <a href="../tools.html#countdown">test countdown planner</a> to see how many hours a week you need to be ready in time.</p>
<h2>Theory test first</h2>
<p>You need a theory test pass before you can book your practical test, and the pass lasts two years. See our <a href="theory-test-greater-manchester.html">theory test guide</a>.</p>
""",
        "faqs": [("How long is the wait for a driving test in Manchester?", "It changes constantly. Start a booking on GOV.UK to see the current earliest dates at each centre."),
                 ("Can I take my test anywhere in Greater Manchester?", "Yes — there's no catchment area for new bookings. Moving an existing booking is limited to nearby centres since June 2026.")],
        "sources": [GOV_BOOK, GOV_FIND_CENTRE, ("GOV.UK — Driving test cost", "https://www.gov.uk/driving-test-cost")],
        "related": ["driving-test-booking-rules-2026", "greater-manchester-driving-test-centres", "theory-test-greater-manchester"],
    },
    {
        "slug": "why-learners-fail-the-driving-test", "cat": "Tests & booking", "icon": "target",
        "title": "Why learners fail the driving test (and how to avoid it)",
        "desc": "The most common driving test faults reported by the DVSA — junction observations, mirrors, moving off, positioning and more — with practical fixes.",
        "takeaways": [
            "The DVSA's most common fault is not making effective observations at junctions.",
            "Mirror checks before changing direction, moving off safely and positioning for right turns are also top faults.",
            "You can have up to 15 driving faults, but one serious or dangerous fault is a fail.",
            "If you regularly make these mistakes in lessons, you're not test-ready yet.",
        ],
        "body": """
<h2>How the test is marked</h2>
<p>Examiners record three kinds of fault: <b>driving faults</b> (minors), <b>serious faults</b> (potentially dangerous) and <b>dangerous faults</b> (actual danger). You pass with up to <b>15 driving faults</b> and <b>no</b> serious or dangerous faults.</p>
<h2>The most common faults</h2>
<p>The DVSA publishes the most common reasons for failing. These have topped the list consistently:</p>
<table><tr><th>Fault</th><th>What it looks like</th><th>How to fix it</th></tr>
<tr><td>Observations at junctions</td><td>Pulling out without looking properly, or looking but not seeing an approaching vehicle</td><td>Slow down earlier on approach so you have time to look both ways — twice if the view is restricted</td></tr>
<tr><td>Mirrors when changing direction</td><td>Turning or changing lanes without checking mirrors, or checking too late</td><td>Use MSPSL every time: Mirrors, Signal, Position, Speed, Look</td></tr>
<tr><td>Moving off safely</td><td>Pulling away from the kerb without a blind-spot check</td><td>Check all mirrors and over your shoulder every single time</td></tr>
<tr><td>Positioning for right turns</td><td>Staying too far left when turning right</td><td>Position just left of the centre line, as far as is safe</td></tr>
<tr><td>Steering control</td><td>Steering too little or too late around corners and parked cars</td><td>Look where you want to go and start steering earlier</td></tr>
<tr><td>Responding to road markings</td><td>Ignoring lane arrows or stopping in a yellow box</td><td>Read the road ahead — markings tell you which lane you need</td></tr>
<tr><td>Control during reverse parking</td><td>Mounting the kerb or finishing outside the bay</td><td>Go slower than feels necessary and keep looking all around</td></tr></table>
<h2>Manchester-specific traps</h2>
<ul><li><b>Bus lanes and bus gates</b> — driving in one during its hours can be marked as a fault. <a href="bus-lanes-and-bus-gates-manchester.html">Our bus lane guide</a>.</li>
<li><b>Multi-lane roundabouts</b> — lane markings override the general left/right rule. <a href="../guides/roundabouts.html">Roundabouts guide</a>.</li>
<li><b>Trams</b> — never stop on tram tracks. <a href="driving-with-trams-metrolink.html">Driving with Metrolink</a>.</li></ul>
<h2>Use your portal</h2>
<p>Your DriveSQ Student Portal tracks 23 skills. If junctions or mirrors aren't at "Independent" yet, that's what your next lessons should focus on.</p>
""",
        "faqs": [("How many minors can you get on a driving test?", "Up to 15 driving faults. Any serious or dangerous fault means a fail."),
                 ("What is the number one reason for failing?", "Not making effective observations at junctions, according to DVSA data.")],
        "sources": [("GOV.UK — Driving test: what happens", "https://www.gov.uk/driving-test"), ("GOV.UK — DVSA top driving test faults", "https://www.gov.uk/government/news/dvsa-reveals-top-driving-test-faults-made-in-the-first-year-of-the-new-test"), HC],
        "related": ["greater-manchester-driving-test-centres", "bus-lanes-and-bus-gates-manchester", "driving-test-booking-rules-2026"],
    },
    {
        "slug": "theory-test-greater-manchester", "cat": "Tests & booking", "icon": "quiz",
        "title": "Taking your theory test in Greater Manchester",
        "desc": "Theory test centres in Manchester and Stockport, what's in the test, pass marks, adjustments for dyslexia and anxiety, and how to prepare for free.",
        "takeaways": [
            "Two parts on the same day: 50 multiple-choice questions (pass 43) and hazard perception (pass 44 out of 75).",
            "Greater Manchester theory test centres include Manchester (Ardwick) and Stockport (town centre).",
            "Bring your photocard provisional licence. The pass lasts two years.",
            "You can ask for extra time or other support if you have dyslexia or another condition.",
        ],
        "body": """
<h2>What's in the test</h2>
<h3>Multiple-choice</h3>
<p>50 questions in 57 minutes, including a short video case study. The pass mark is <b>43 out of 50</b>.</p>
<h3>Hazard perception</h3>
<p>14 video clips of everyday road scenes. Click when you see a developing hazard — the earlier you respond, the more you score. Maximum 75, pass mark <b>44</b>.</p>
<h2>Theory test centres near you</h2>
<p>Greater Manchester learners most often use the theory test centres in <b>Manchester</b> (Ardwick, near Piccadilly) and <b>Stockport</b> (town centre). Centres occasionally move, so always check the address on your booking confirmation before you travel, and plan for limited parking — public transport is often easier.</p>
<h2>Support if you need it</h2>
<p>If you have dyslexia, a learning difficulty or another condition, you can ask for support when you book, such as extra time. The test also includes an English or Welsh voiceover you can listen to. Tell the DVSA what you need when booking and have any supporting evidence ready.</p>
<p>See also: <a href="learning-to-drive-with-dyslexia-adhd-or-anxiety.html">Learning to drive with dyslexia, ADHD or anxiety</a>.</p>
<h2>Free ways to prepare</h2>
<ul><li>Read the Highway Code — every question is based on it.</li><li>SQ learners get the DriveSQ Student Portal free, with a theory library and full 50-question mock tests.</li><li>Try our <a href="../theory-quiz.html">Highway Code quiz</a>, <a href="../road-signs.html">road sign flashcards</a> and <a href="../hazard-game.html">hazard game</a>.</li></ul>
<h2>On the day</h2>
<ul><li>Bring your photocard provisional licence — you can't sit the test without it.</li><li>Arrive early; personal items go in a locker.</li><li>You can take a short break of up to 3 minutes between the two parts.</li></ul>
""",
        "faqs": [("Where can I take my theory test in Greater Manchester?", "Commonly at the Manchester (Ardwick) or Stockport centres. Check the address on your booking confirmation."),
                 ("How long does my theory pass last?", "Two years. You must pass your practical test within that time."),
                 ("Can I get extra time for dyslexia?", "Yes — you can request support such as extra time when you book.")],
        "sources": [GOV_THEORY, ("GOV.UK — Theory test: cars", "https://www.gov.uk/theory-test"), ("GOV.UK — Theory test reasonable adjustments", "https://www.gov.uk/theory-test/reading-difficulty-disability-or-health-condition"), HC],
        "related": ["learning-to-drive-with-dyslexia-adhd-or-anxiety", "driving-test-waiting-times-greater-manchester", "highway-code-2022-changes"],
    },

    # ---------------------------------------------------------------- MANCHESTER ROADS
    {
        "slug": "driving-with-trams-metrolink", "cat": "Manchester roads", "icon": "road",
        "title": "Driving with Metrolink trams: a learner's guide",
        "desc": "How to drive safely alongside Manchester Metrolink trams: shared streets, tram-only lanes, tram signals, tram stops and cycling over rails.",
        "takeaways": [
            "Trams can't steer around you and take longer to stop than cars.",
            "Never stop or wait on tram tracks, and never enter a reserved tram lane.",
            "Tram signals (white bars and shapes) are for trams only — follow your normal traffic lights.",
            "Watch for passengers crossing the road at on-street tram stops.",
        ],
        "body": """
<h2>Why trams are different</h2>
<p>Metrolink trams run on fixed rails. They can't swerve to avoid you, they're long and heavy, and they need more distance to stop than a car. In the city centre and on some routes trams share the road with traffic, so you'll meet them on lessons — and possibly on your test.</p>
<h2>The golden rules</h2>
<ul><li><b>Never stop on the tracks</b> — including in queues and at junctions. Wait behind the line until there's space to clear the tracks completely.</li>
<li><b>Don't drive in reserved tram lanes.</b> These are marked with white lines, different surfaces or signs.</li>
<li><b>Give way to trams</b> where signs or markings tell you to, and never try to race one through a junction.</li>
<li><b>Look out for pedestrians at tram stops.</b> At on-street stops people may step into the road to board or leave.</li>
<li><b>Take care when turning across tracks</b> — check for trams from both directions.</li></ul>
<h2>Tram signals</h2>
<p>Trams have their own signals using white bars and shapes rather than red, amber and green lights. These are only for tram drivers — always follow the normal traffic lights for your lane.</p>
<h2>Cyclists and motorcyclists</h2>
<p>Rails can catch narrow tyres. Cyclists often cross rails at an angle or move out to do so — give them plenty of space.</p>
<h2>Practising with SQ</h2>
<p>We introduce tram roads only once junctions and observations feel natural. Your instructor will pick quieter times for your first tram encounters.</p>
""",
        "faqs": [("Can learners drive on roads with trams?", "Yes. Trams share some roads with traffic in Greater Manchester, and learners practise there with their instructor."),
                 ("What do tram signals mean for car drivers?", "Nothing — they're for trams only. Follow your normal traffic lights.")],
        "sources": [HC, ("Highway Code — rules for trams (rules 300–307)", "https://www.gov.uk/guidance/the-highway-code/other-road-users-204-to-225"), ("Transport for Greater Manchester — Metrolink", "https://tfgm.com/public-transport/tram")],
        "related": ["manchester-city-centre-driving-guide", "bus-lanes-and-bus-gates-manchester", "why-learners-fail-the-driving-test"],
    },
    {
        "slug": "bus-lanes-and-bus-gates-manchester", "cat": "Manchester roads", "icon": "flag",
        "title": "Bus lanes and bus gates in Manchester",
        "desc": "How to read bus lane signs, the Oxford Road bus gate, Manchester bus lane fines and how bus lanes are treated on the driving test.",
        "takeaways": [
            "A bus lane's operating times are on the blue sign. Outside those times you can usually use it.",
            "A bus gate is a short section only certain vehicles may pass through — it applies to everyone else, even for a moment.",
            "Oxford Road's bus gates are open only to buses, taxis and cycles from 6am to 9pm every day.",
            "Manchester City Council lists bus lane and bus gate penalties at £70 (reduced if paid early).",
        ],
        "body": """
<h2>Bus lanes</h2>
<p>A bus lane is marked by a thick solid white line and the words BUS LANE. A blue sign at the start shows which vehicles can use it and when. If the sign shows times, you may usually drive in it outside those times. If there are no times, it operates 24 hours.</p>
<div class="callout">Look at the markings: some bus lanes have a broken white line where other traffic may cross to turn, while a solid line means stay out during the hours shown. If in doubt, don't enter it.</div>
<h2>Bus gates</h2>
<p>A bus gate is a short stretch of road that only permitted vehicles (often buses, taxis and cycles) can drive through. Cameras enforce them. Unlike a bus lane, you can't just drive through one outside "busy" times unless the sign says so.</p>
<h3>Oxford Road</h3>
<p>Manchester's best-known bus gates are on <b>Oxford Road</b>, the route past the universities and hospitals. Manchester City Council says the gates are open only to buses, black cabs and pedal cycles from <b>6am to 9pm every day</b>. Satnavs don't always know this — use the diversion signs.</p>
<h2>Fines</h2>
<p>Manchester City Council lists bus lane and bus gate penalty charge notices at <b>£70</b>, reduced if you pay early and increased if you don't pay. Council pages give slightly different early-payment windows, so check the notice itself. Other Greater Manchester councils set their own charges.</p>
<h2>On your driving test</h2>
<p>Driving in a bus lane or through a bus gate when it's in operation can be marked as a fault. Your instructor will practise reading the signs with you, especially if you're testing at <a href="test-centre-west-didsbury.html">West Didsbury</a> or <a href="test-centre-cheetham-hill.html">Cheetham Hill</a>, where busy main roads are common.</p>
""",
        "faqs": [("Can I drive in a bus lane outside its hours?", "Usually yes — the blue sign shows its operating times. No times means it operates all day."),
                 ("How much is a bus lane fine in Manchester?", "Manchester City Council lists £70, reduced for early payment. Check the notice for exact deadlines."),
                 ("When is the Oxford Road bus gate in operation?", "Manchester City Council says 6am to 9pm every day, for buses, black cabs and cycles only.")],
        "sources": [("Manchester City Council — Bus lanes", "https://www.manchester.gov.uk/info/471/tickets_and_fines/698/bus_lanes/2"), ("Manchester City Council — Bus gates", "https://www.manchester.gov.uk/info/471/parking_in_public_areas/7420/bus_gates/2"), HC],
        "related": ["manchester-city-centre-driving-guide", "driving-with-trams-metrolink", "why-learners-fail-the-driving-test"],
    },
    {
        "slug": "smart-motorways-m60-m62", "cat": "Manchester roads", "icon": "road",
        "title": "Smart motorways around Manchester: M60, M62 and M6",
        "desc": "What a red X means, variable speed limits, emergency areas and how to break down safely on Greater Manchester's smart motorways.",
        "takeaways": [
            "A red X over a lane means it's closed — never drive in it.",
            "Speed limits shown in a red circle on overhead signs are legal limits.",
            "Emergency areas are marked with orange surfaces and blue signs with an orange SOS symbol.",
            "Learners can have motorway lessons with an approved instructor in a dual-controlled car.",
        ],
        "body": """
<h2>What makes a motorway "smart"</h2>
<p>Smart motorways use technology to manage traffic. Some use the hard shoulder as a live lane permanently or at busy times. Several stretches of motorway around Greater Manchester — including sections of the M60, M62 and M6 — work this way.</p>
<h2>Signs you must obey</h2>
<ul><li><b>Red X:</b> the lane is closed, often because of a breakdown or workers ahead. Move out of it safely. Driving in a red X lane is an offence.</li>
<li><b>Speed in a red circle:</b> a legal limit, often lowered for congestion or incidents. Cameras may enforce it.</li>
<li><b>Solid white line:</b> marks the hard shoulder where it isn't a live lane. Don't use it unless signs say so.</li></ul>
<h2>If you break down</h2>
<ol><li>Try to leave at the next junction or reach an emergency area (orange surface, blue sign with an orange SOS).</li>
<li>If you can't, move as far left as possible, switch on hazard lights and, if safe, get out on the left and go behind a barrier.</li>
<li>Call 999 if you're stopped in a live lane.</li></ol>
<h2>Motorway lessons with SQ</h2>
<p>Since 2018, learners in England, Scotland and Wales can drive on motorways with an approved driving instructor in a car with dual controls. We'll cover joining, lane discipline, overtaking and leaving — and smart motorway signs. See <a href="../services/motorway-driving-lessons.html">motorway lessons</a>.</p>
""",
        "faqs": [("What does a red X on the motorway mean?", "The lane is closed. Move out of it safely and never drive in a red X lane."),
                 ("Can learner drivers go on the motorway?", "Yes, with an approved driving instructor in a dual-controlled car.")],
        "sources": [("National Highways — Driving on motorways", "https://nationalhighways.co.uk/road-safety/driving-on-motorways/"), ("Highway Code — Motorways (rules 253–274)", "https://www.gov.uk/guidance/the-highway-code/motorways-253-to-274"), ("GOV.UK — Learner drivers on motorways", "https://www.gov.uk/government/news/learner-drivers-on-motorways-how-it-will-work")],
        "related": ["m60-ring-road-guide", "after-you-pass-new-driver-guide", "manchester-city-centre-driving-guide"],
    },
    {
        "slug": "m60-ring-road-guide", "cat": "Manchester roads", "icon": "globe",
        "title": "The M60 ring road: a guide for new drivers",
        "desc": "How the M60 orbital works, joining and leaving safely, lane discipline and why the M60 matters to every Greater Manchester driver.",
        "takeaways": [
            "The M60 is a full orbital motorway around Manchester, linking most Greater Manchester boroughs.",
            "Plan your exit by junction number and destination, not just the road name.",
            "Join at the speed of traffic using the slip road, and give way to traffic already on the motorway.",
            "Leave lane 1 only to overtake, then move back when it's safe.",
        ],
        "body": """
<h2>Why the M60 matters</h2>
<p>The M60 circles Manchester and passes through or close to Stockport, Tameside, Oldham, Rochdale, Bury, Salford and Trafford. It connects with the M56, M61, M62, M66 and M67, so most Greater Manchester drivers use it sooner or later.</p>
<h2>Joining</h2>
<ol><li>Use the slip road to build up to the speed of traffic on the main carriageway.</li><li>Check your right-hand mirror and blind spot early.</li><li>Find a safe gap and merge — traffic already on the motorway has priority.</li><li>Don't stop at the end of a slip road unless the traffic is stationary.</li></ol>
<h2>On the M60</h2>
<ul><li>Drive in the left-hand lane unless overtaking.</li><li>Keep at least a two-second gap — four in the wet.</li><li>Watch overhead signs for lane closures and speed limits (see <a href="smart-motorways-m60-m62.html">smart motorways</a>).</li></ul>
<h2>Leaving</h2>
<p>Countdown markers (three, two, one bars) start 300 yards before the exit. Move into lane 1 in good time, signal, and slow down on the slip road, not the main carriageway.</p>
<h2>Learning with SQ</h2>
<p>Motorway lessons are available to learners with us. Many Greater Manchester learners find a lesson on the M60 transforms their confidence after passing.</p>
""",
        "faqs": [("Is the M60 a smart motorway?", "Some sections of the M60 use smart motorway technology. Always follow the overhead signs."),
                 ("Can I practise on the M60 as a learner?", "Yes, with an approved instructor in a dual-controlled car.")],
        "sources": [("Highway Code — Motorways (rules 253–274)", "https://www.gov.uk/guidance/the-highway-code/motorways-253-to-274"), ("National Highways — Driving on motorways", "https://nationalhighways.co.uk/road-safety/driving-on-motorways/")],
        "related": ["smart-motorways-m60-m62", "after-you-pass-new-driver-guide", "manchester-city-centre-driving-guide"],
    },
    {
        "slug": "manchester-city-centre-driving-guide", "cat": "Manchester roads", "icon": "pin",
        "title": "Driving in Manchester city centre as a learner",
        "desc": "One-way streets, bus gates, trams, cycle lanes and pedestrians: how to handle Manchester city centre with confidence.",
        "takeaways": [
            "Expect one-way systems, bus-only sections, tram streets and lots of pedestrians.",
            "Read lane markings and signs early — the city centre gives you little time to change lanes.",
            "Give way to pedestrians crossing a road you're turning into (Highway Code rule H2).",
            "We only take learners into the city centre when junctions and observations are solid.",
        ],
        "body": """
<h2>What makes the city centre tricky</h2>
<ul><li><b>One-way streets</b> and turn restrictions.</li><li><b>Bus lanes and bus gates</b> — see <a href="bus-lanes-and-bus-gates-manchester.html">our guide</a>.</li><li><b>Trams</b> on shared streets — see <a href="driving-with-trams-metrolink.html">driving with Metrolink</a>.</li><li><b>Cycle lanes</b>, some segregated, some painted.</li><li><b>Pedestrians</b> crossing between parked vehicles and at junctions.</li></ul>
<h2>Skills that help</h2>
<ul><li><b>Plan ahead.</b> Read signs and lane arrows early so you're in the right lane in good time.</li><li><b>Keep your speed down.</b> Low speed gives you time to see and react.</li><li><b>Observe at junctions.</b> Look for cyclists on your left and pedestrians crossing.</li><li><b>Stay calm in queues.</b> Never block junctions, yellow boxes or tram tracks.</li></ul>
<h2>Pedestrian priority</h2>
<p>Since the 2022 Highway Code update, you should give way to pedestrians crossing or waiting to cross a road you're turning into. In the city centre this happens constantly. See <a href="highway-code-2022-changes.html">Highway Code changes</a>.</p>
<h2>When we'll take you there</h2>
<p>City-centre driving comes later in your lessons, once junctions and roundabouts are at "Developing" or "Independent" in your DriveSQ Student Portal. Nervous? We can choose quieter times like Sunday mornings for your first visit.</p>
""",
        "faqs": [("Will I drive in Manchester city centre during lessons?", "Yes, once you're ready. We build up to it gradually."),
                 ("Is the city centre on the driving test?", "It depends on your test centre and route. Busy urban roads are common around Manchester centres.")],
        "sources": [HC, ("Manchester City Council — Bus gates", "https://www.manchester.gov.uk/info/471/parking_in_public_areas/7420/bus_gates/2")],
        "related": ["bus-lanes-and-bus-gates-manchester", "driving-with-trams-metrolink", "highway-code-2022-changes"],
    },
    {
        "slug": "greater-manchester-clean-air-zone", "cat": "Manchester roads", "icon": "globe",
        "title": "Greater Manchester Clean Air Zone: do learners pay?",
        "desc": "The current position on Greater Manchester's Clean Air Zone, why private cars aren't charged, and what it means for learner drivers.",
        "takeaways": [
            "There is no Clean Air Zone charge for private cars in Greater Manchester.",
            "Charging was paused in 2022, and an investment-led, non-charging plan was approved by government in 2025.",
            "Learner drivers and driving school cars don't pay a daily clean air charge.",
            "Check Clean Air Greater Manchester for the latest position — policies can change.",
        ],
        "body": """
<h2>The short answer</h2>
<p>No — learner drivers don't pay a Clean Air Zone charge in Greater Manchester, and neither do private cars.</p>
<h2>What happened</h2>
<p>Greater Manchester originally planned a charging Clean Air Zone for some older commercial vehicles, but the first phase did not go ahead in May 2022. In 2025 the government approved Greater Manchester's <b>investment-led, non-charging</b> Clean Air Plan, which funds cleaner buses, taxi upgrades and traffic measures instead of daily charges.</p>
<h2>Private cars were never in scope</h2>
<p>Even the original charging plans didn't charge private cars. Your lessons, your test and your own car after passing aren't affected.</p>
<h2>Other cities</h2>
<p>Other UK cities run their own clean air schemes with different rules. If you drive elsewhere after passing, check that city's rules first.</p>
""",
        "faqs": [("Is there a congestion charge or ULEZ in Manchester?", "No. Greater Manchester does not charge private cars to drive in a clean air or congestion zone."),
                 ("Do driving school cars pay a clean air charge?", "No — there is no clean air charge for cars in Greater Manchester.")],
        "sources": [("Clean Air Greater Manchester — Clean Air Plan", "https://cleanairgm.com/clean-air-plan/"), ("Parkers — Manchester clean air zone", "https://www.parkers.co.uk/car-advice/manchester-ulez/")],
        "related": ["manchester-city-centre-driving-guide", "after-you-pass-new-driver-guide", "m60-ring-road-guide"],
    },

    # ---------------------------------------------------------------- LEARNER LIFE
    {
        "slug": "practising-with-family-supervisor-rules", "cat": "Learner life", "icon": "users",
        "title": "Private practice: rules for supervising a learner",
        "desc": "Who can supervise a learner driver, L plates, insurance and how to combine family practice with professional lessons in Greater Manchester.",
        "takeaways": [
            "Your supervisor must be at least 21 and have held a full licence for that type of car for 3 years.",
            "You must display L plates (or D plates in Wales) and be insured for the car.",
            "Supervisors can't be paid unless they're an approved driving instructor.",
            "Private practice works best alongside lessons — practise what your instructor has already taught.",
        ],
        "body": """
<h2>Who can supervise you</h2>
<p>To supervise a learner, someone must:</p>
<ul><li>be at least <b>21 years old</b>,</li><li>be qualified to drive that type of vehicle (for example, a manual licence to supervise in a manual car), and</li><li>have held a full driving licence for <b>3 years</b>.</li></ul>
<p>They must be fit to supervise — for example, not over the drink-drive limit and not using a hand-held phone.</p>
<h2>What you need</h2>
<ul><li><b>L plates</b> on the front and back.</li><li><b>Insurance</b> that covers you as a learner in that car — see <a href="learner-driver-insurance.html">learner insurance</a>.</li><li>A car that's taxed and has a valid MOT if required.</li></ul>
<h2>Making practice count</h2>
<ul><li>Practise skills your instructor has already introduced — your DriveSQ Student Portal shows which ones.</li><li>Start on quiet roads and short trips.</li><li>Avoid new or advanced skills (like manoeuvres) until your instructor has taught them, so you don't learn bad habits.</li><li>Keep it calm — a stressed supervisor makes a stressed learner.</li></ul>
<p>The DVSA suggests learners typically need around 45 hours of lessons plus around 22 hours of private practice.</p>
""",
        "faqs": [("Can my parent teach me to drive?", "Yes, if they're 21 or over, have held a full licence for 3 years and you're insured. They can't charge you unless they're an approved instructor."),
                 ("Do I need L plates for private practice?", "Yes — L plates on the front and back of the car.")],
        "sources": [("GOV.UK — Supervising a learner driver", "https://www.gov.uk/driving-lessons-learning-to-drive/practising-with-family-or-friends"), ("GOV.UK — Learner drivers", "https://www.gov.uk/driving-lessons-learning-to-drive")],
        "related": ["learner-driver-insurance", "parents-guide-to-learner-drivers", "choosing-a-driving-instructor"],
    },
    {
        "slug": "learner-driver-insurance", "cat": "Learner life", "icon": "shield",
        "title": "Learner driver insurance explained",
        "desc": "Do you need insurance for driving lessons? When you need learner insurance, the options for practising in a family car, and what happens when you pass.",
        "takeaways": [
            "You don't need your own insurance for lessons in a driving school car — the school's insurance covers you.",
            "To practise in a family or friend's car you must be insured, often with a learner driver policy.",
            "Most learner policies end when you pass — you'll need a new policy to drive alone.",
            "Driving uninsured can mean penalty points, a fine and your licence at risk.",
        ],
        "body": """
<h2>Lessons with SQ</h2>
<p>When you're learning in an SQ Driving School car, you're covered by the car's driving school insurance — you don't need to buy anything.</p>
<h2>Practising in someone else's car</h2>
<p>To practise privately you must be insured for that car. Common options are:</p>
<ul><li><b>A short-term or standalone learner driver policy</b> — covers you without affecting the owner's no-claims bonus in many cases.</li><li><b>Being added to the owner's policy</b> as a learner — check how a claim would affect their premium.</li></ul>
<p>Compare policies carefully: check excess, who can supervise and whether the cover ends automatically when you pass.</p>
<h2>When you pass</h2>
<p>Learner cover usually ends the moment you pass. Arrange a new policy before you drive alone — even the drive home from the test centre.</p>
<h2>Why it matters</h2>
<p>Driving without insurance is a serious offence that can lead to penalty points and a fine. For new drivers, six points within two years of passing means losing your licence.</p>
""",
        "faqs": [("Do I need insurance for driving lessons?", "Not for lessons in a driving school car — the school's insurance covers you."),
                 ("Can I drive home after passing on my learner insurance?", "Usually not — most learner policies end when you pass. Check your policy.")],
        "sources": [("GOV.UK — Vehicle insurance", "https://www.gov.uk/vehicle-insurance"), ("GOV.UK — Practising with family or friends", "https://www.gov.uk/driving-lessons-learning-to-drive/practising-with-family-or-friends")],
        "related": ["practising-with-family-supervisor-rules", "after-you-pass-new-driver-guide", "parents-guide-to-learner-drivers"],
    },
    {
        "slug": "choosing-a-driving-instructor", "cat": "Learner life", "icon": "star",
        "title": "How to choose a driving instructor in Greater Manchester",
        "desc": "Green and pink badges, questions to ask, red flags and what to expect from a good driving instructor or school.",
        "takeaways": [
            "A green badge on the windscreen means a fully qualified Approved Driving Instructor (ADI).",
            "A pink badge means a trainee instructor licensed by the DVSA to give lessons while training.",
            "Ask about prices, lesson length, cancellation terms and how progress is tracked.",
            "Be wary of pass-rate claims that can't be explained or evidenced.",
        ],
        "body": """
<h2>Check the badge</h2>
<p>Anyone paid to teach you to drive must be registered with the DVSA. They must display their badge on the windscreen during lessons:</p>
<table><tr><th>Badge</th><th>Meaning</th></tr><tr><td>Green (octagonal)</td><td>Approved Driving Instructor (ADI) — fully qualified</td></tr><tr><td>Pink (triangular)</td><td>Trainee instructor with a DVSA trainee licence</td></tr></table>
<p>Both have passed criminal record checks as part of DVSA registration.</p>
<h2>Questions to ask</h2>
<ul><li>How much are lessons, and are there any extra fees?</li><li>How long is each lesson?</li><li>What's your cancellation policy?</li><li>How will I know my progress?</li><li>Manual, automatic, or both?</li><li>Do you cover my area and test centre?</li></ul>
<h2>Red flags</h2>
<ul><li>No visible badge.</li><li>Prices that change once you've started.</li><li>Pressure to book a test before you're ready.</li><li>Pass-rate figures with no explanation of how they're calculated.</li></ul>
<h2>How SQ answers those questions</h2>
<p>All our prices are on our website (2-hour lessons £70, 10 hours £350 or £320 with a discount). Your progress is tracked in the free DriveSQ Student Portal, and we only publish genuine reviews — see our <a href="../review-policy.html">review policy</a>.</p>
""",
        "faqs": [("What's the difference between a green and pink badge?", "Green is a fully qualified ADI. Pink is a trainee licensed by the DVSA to teach while completing training."),
                 ("How do I know my instructor is approved?", "They must display a DVSA badge on the windscreen during paid lessons.")],
        "sources": [("GOV.UK — Find a driving instructor / ADI registration", "https://www.gov.uk/find-driving-schools-and-lessons"), ("GOV.UK — Become a driving instructor", "https://www.gov.uk/become-driving-instructor")],
        "related": ["practising-with-family-supervisor-rules", "parents-guide-to-learner-drivers", "why-learners-fail-the-driving-test"],
    },
    {
        "slug": "foreign-licence-exchange-uk", "cat": "Learner life", "icon": "globe",
        "title": "New to Manchester? Driving on a foreign licence",
        "desc": "Driving in Great Britain on a licence from another country: the 12-month rule, exchanging your licence and when you need to pass a UK test.",
        "takeaways": [
            "Many visitors and new residents can drive on their foreign licence for up to 12 months.",
            "Licences from some 'designated' countries can be exchanged for a GB licence.",
            "Otherwise you'll need a provisional licence and to pass the UK theory and practical tests.",
            "Rules depend on where your licence is from — always check GOV.UK.",
        ],
        "body": """
<h2>The 12-month rule</h2>
<p>If you become resident in Great Britain with a full licence from many non-EU countries, you can usually drive small vehicles for up to <b>12 months</b> from when you became resident.</p>
<h2>Exchanging your licence</h2>
<p>If your licence is from a <b>designated country</b> (the list includes places such as Australia, Canada, Japan, New Zealand and South Africa), you may be able to exchange it for a GB licence without taking a test. Rules on automatic and manual entitlement can differ.</p>
<h2>If you can't exchange</h2>
<p>You'll need to apply for a <b>provisional licence</b> and pass the <b>theory and practical tests</b> before your 12 months run out.</p>
<h2>EU and EEA licences</h2>
<p>Different rules apply to licences from EU and EEA countries. Check GOV.UK for your situation.</p>
<h2>How SQ helps</h2>
<p>Experienced drivers often need far fewer lessons — the focus is UK road rules, roundabouts and test technique. Try our <a href="../tools.html#lessons">lesson calculator</a> and choose "Drove abroad".</p>
""",
        "faqs": [("Can I drive in the UK on my foreign licence?", "Often for up to 12 months after becoming resident, depending on where your licence is from."),
                 ("Do I need lessons if I've driven abroad?", "Not necessarily many, but UK road rules and test technique are different — a few lessons usually help.")],
        "sources": [("GOV.UK — Driving in GB on a non-GB licence", "https://www.gov.uk/driving-nongb-licence"), ("GOV.UK — Exchange a foreign driving licence", "https://www.gov.uk/exchange-foreign-driving-licence")],
        "related": ["theory-test-greater-manchester", "choosing-a-driving-instructor", "driving-test-booking-rules-2026"],
    },
    {
        "slug": "learning-to-drive-with-dyslexia-adhd-or-anxiety", "cat": "Learner life", "icon": "heart",
        "title": "Learning to drive with dyslexia, ADHD or anxiety",
        "desc": "Support available in the theory and practical tests, how lessons can be adapted, and practical tips for neurodivergent and anxious learners.",
        "takeaways": [
            "You can ask for support in the theory test, such as extra time.",
            "In the practical test you can tell the examiner about dyslexia or similar — they can adapt how directions are given.",
            "Lessons can be structured with shorter tasks, more repetition and written recaps.",
            "Tell your instructor what helps you learn — there's no wrong way to learn.",
        ],
        "body": """
<h2>The theory test</h2>
<p>When booking, you can ask for support if you have a reading difficulty, disability or health condition. This can include <b>extra time</b>. The test also has an English or Welsh voiceover.</p>
<h2>The practical test</h2>
<p>Tell the examiner at the start if you have dyslexia or another condition that affects how you follow directions. During independent driving they can make reasonable adjustments, such as how directions are given.</p>
<h2>How we adapt lessons</h2>
<ul><li><b>One focus at a time</b> — fewer instructions at once.</li><li><b>Repetition</b> until it feels automatic.</li><li><b>Written recaps</b> in your DriveSQ Student Portal after every lesson.</li><li><b>Breaks</b> whenever you need them — our 2-hour lessons leave room for that.</li></ul>
<h2>For anxiety</h2>
<p>Visit our <a href="../comfort.html">Comfort Zone</a> for a personal comfort plan and a calm-breathing coach, and read <a href="../first-lesson.html">what happens in your first lesson</a> so there are no surprises.</p>
<div class="callout callout--info">Medical conditions: some conditions must be reported to the DVLA. Check GOV.UK if you're unsure — many conditions don't stop you driving.</div>
""",
        "faqs": [("Can I get extra time in the theory test?", "Yes, you can ask for support such as extra time when booking."),
                 ("Should I tell the examiner I have dyslexia?", "Yes — they can adapt how directions are given during independent driving.")],
        "sources": [("GOV.UK — Theory test support", "https://www.gov.uk/theory-test/reading-difficulty-disability-or-health-condition"), ("GOV.UK — Driving test: disability or health condition", "https://www.gov.uk/driving-test/disability-health-condition-or-learning-difficulty"), ("GOV.UK — Medical conditions and driving", "https://www.gov.uk/health-conditions-and-driving")],
        "related": ["theory-test-greater-manchester", "choosing-a-driving-instructor", "parents-guide-to-learner-drivers"],
    },
    {
        "slug": "learning-to-drive-as-a-student-in-manchester", "cat": "Learner life", "icon": "grad",
        "title": "Learning to drive as a student in Manchester",
        "desc": "Fitting lessons around lectures, student discounts, theory tests near campus and making the most of a tight budget.",
        "takeaways": [
            "SQ students get 10 hours for £320 with valid student ID.",
            "Book 2-hour lessons around your timetable — evenings and weekends are popular.",
            "Theory test centres in Manchester and Stockport are easy to reach by public transport.",
            "Avoid long gaps between lessons, like the whole summer — skills fade.",
        ],
        "body": """
<h2>Fitting lessons around uni</h2>
<p>Most students find two 2-hour lessons a week fits well around lectures. Pick-ups from halls, campus or home are all possible within Greater Manchester.</p>
<h2>Keeping costs down</h2>
<ul><li><b>Student discount:</b> 10 hours for £320 instead of £350 with a valid student ID.</li><li><b>Free theory prep</b> in the DriveSQ Student Portal — no paid apps needed.</li><li><b>Consistent lessons</b> mean fewer hours overall.</li></ul>
<h2>Term breaks</h2>
<p>If you're going home for the holidays, try to finish your lessons or book a test before you go. Long breaks usually mean extra recap lessons.</p>
<h2>Students near Oxford Road</h2>
<p>If you live near the universities, learn about the <a href="bus-lanes-and-bus-gates-manchester.html">Oxford Road bus gates</a> early — they catch out many new drivers.</p>
""",
        "faqs": [("Do you offer student discounts?", "Yes — 10 hours for £320 with a valid student ID or enrolment letter."),
                 ("Can you pick me up from university?", "Yes, anywhere within Greater Manchester.")],
        "sources": [GOV_THEORY, ("Manchester City Council — Bus gates", "https://www.manchester.gov.uk/info/471/parking_in_public_areas/7420/bus_gates/2")],
        "related": ["theory-test-greater-manchester", "bus-lanes-and-bus-gates-manchester", "driving-test-waiting-times-greater-manchester"],
    },
    {
        "slug": "parents-guide-to-learner-drivers", "cat": "Learner life", "icon": "users",
        "title": "A parent's guide to your teenager learning to drive",
        "desc": "When teenagers can start, costs, private practice, insurance and how to support (not stress) a learner driver in Greater Manchester.",
        "takeaways": [
            "Teens can apply for a provisional licence at 15 years 9 months and drive a car from 17.",
            "The DVSA suggests around 45 hours of lessons plus around 22 hours of practice.",
            "To supervise you must be 21+ and have held a full licence for 3 years.",
            "Calm, regular practice helps far more than long, stressful sessions.",
        ],
        "body": """
<h2>Getting started</h2>
<p>Teenagers can apply for a provisional licence from <b>15 years and 9 months</b> and start driving a car at <b>17</b>. Many families book lessons as a birthday present — see our <a href="../gift-vouchers.html">gift vouchers</a>.</p>
<h2>Budgeting</h2>
<p>With SQ, lessons are £35 an hour in 2-hour lessons, or 10 hours for £350. Add DVSA fees for the theory and practical tests. Our <a href="../prices.html">cost calculator</a> works out a realistic total.</p>
<h2>Supervising practice</h2>
<p>See <a href="practising-with-family-supervisor-rules.html">supervisor rules</a> and <a href="learner-driver-insurance.html">learner insurance</a>. Keep sessions short, calm and focused on skills already taught.</p>
<h2>Staying in the loop</h2>
<p>The DriveSQ Student Portal shows hours, skills and instructor feedback. Many parents look at it together with their learner — it makes progress (and the money spent) visible.</p>
<h2>Supporting, not stressing</h2>
<ul><li>Praise what went well before mentioning mistakes.</li><li>Don't compare with siblings or friends.</li><li>Let the instructor set the pace for the test.</li></ul>
""",
        "faqs": [("At what age can my child start driving lessons?", "From 17 for a car, with a provisional licence (they can apply from 15 years 9 months)."),
                 ("How can I see my teenager's progress?", "SQ learners' progress is tracked in the DriveSQ Student Portal.")],
        "sources": [("GOV.UK — Apply for a provisional licence", "https://www.gov.uk/apply-first-provisional-driving-licence"), ("GOV.UK — Practising with family or friends", "https://www.gov.uk/driving-lessons-learning-to-drive/practising-with-family-or-friends")],
        "related": ["practising-with-family-supervisor-rules", "learner-driver-insurance", "choosing-a-driving-instructor"],
    },
    {
        "slug": "after-you-pass-new-driver-guide", "cat": "Learner life", "icon": "flag",
        "title": "Just passed: a new driver's guide for Greater Manchester",
        "desc": "The New Drivers Act six-point rule, insurance, P plates, motorways and building confidence after passing your test in Greater Manchester.",
        "takeaways": [
            "Get six or more penalty points within two years of passing and your licence is revoked.",
            "Learner insurance usually ends when you pass — arrange new cover first.",
            "P plates are optional but can help other drivers give you space.",
            "Motorway lessons or Pass Plus build confidence on roads you didn't meet on your test.",
        ],
        "body": """
<h2>The two-year rule</h2>
<p>Under the New Drivers Act, if you get <b>six or more penalty points</b> within <b>two years</b> of passing, your licence is revoked and you'll have to reapply for a provisional licence and pass both tests again. A single hand-held phone offence carries six points.</p>
<h2>Insurance</h2>
<p>Sort your new policy before driving alone. See <a href="learner-driver-insurance.html">learner insurance</a> for why your learner cover won't carry over.</p>
<h2>P plates</h2>
<p>Green P plates are optional in Great Britain. Many new drivers find they help other road users be patient.</p>
<h2>Build confidence</h2>
<ul><li><a href="../services/motorway-driving-lessons.html">Motorway lessons</a> — the M60 and M62 are part of everyday life here.</li><li><a href="../services/pass-plus-courses.html">Pass Plus</a> — post-test training in different conditions.</li><li>Night and wet-weather driving — see our <a href="../guides/wet-weather-driving.html">wet weather guide</a>.</li></ul>
""",
        "faqs": [("How many points can a new driver get?", "Six or more points within two years of passing means your licence is revoked."),
                 ("Do I have to use P plates?", "No, they're optional in Great Britain.")],
        "sources": [("GOV.UK — Penalty points (endorsements)", "https://www.gov.uk/penalty-points-endorsements"), ("GOV.UK — Pass Plus", "https://www.gov.uk/pass-plus")],
        "related": ["smart-motorways-m60-m62", "m60-ring-road-guide", "learner-driver-insurance"],
    },
    {
        "slug": "highway-code-2022-changes", "cat": "Learner life", "icon": "book",
        "title": "The Highway Code changes every learner must know",
        "desc": "The hierarchy of road users, giving way to pedestrians at junctions, passing distances for cyclists and horses, and the Dutch Reach.",
        "takeaways": [
            "Hierarchy of road users: those who can cause the greatest harm have the greatest responsibility.",
            "Give way to pedestrians crossing or waiting to cross a road you're turning into.",
            "Leave at least 1.5 metres when overtaking cyclists at up to 30mph.",
            "Pass horse riders at under 10mph, leaving at least 2 metres.",
        ],
        "body": """
<h2>Hierarchy of road users (rule H1)</h2>
<p>People driving larger or faster vehicles carry the greatest responsibility to reduce the danger they pose to others. For car drivers, that means extra care around pedestrians, cyclists and horse riders.</p>
<h2>Pedestrians at junctions (rule H2)</h2>
<p>At a junction, give way to pedestrians crossing or <b>waiting to cross</b> a road you're turning into or out of. You should also give way to pedestrians on a zebra crossing and to people walking or cycling on a parallel crossing.</p>
<h2>Cyclists (rule H3 and rule 163)</h2>
<ul><li>Don't cut across cyclists when turning into or out of a junction or changing lanes.</li><li>Leave at least <b>1.5 metres</b> when overtaking at speeds up to 30mph, and more at higher speeds.</li><li>Cyclists may ride in the centre of a lane on quieter roads, in slower traffic and at junctions.</li></ul>
<h2>Horse riders and pedestrians in the road</h2>
<p>Pass horses at <b>under 10mph</b>, allowing at least <b>2 metres</b>. Allow at least 2 metres when passing pedestrians walking in the road at low speed.</p>
<h2>The Dutch Reach</h2>
<p>Open your car door with the hand furthest from it. It makes you turn your head and look for cyclists before opening.</p>
<p>Test yourself with our <a href="../theory-quiz.html">Highway Code quiz</a>.</p>
""",
        "faqs": [("What is the hierarchy of road users?", "A Highway Code principle that those who can cause the greatest harm have the greatest responsibility to reduce danger."),
                 ("How much space should I give a cyclist?", "At least 1.5 metres at speeds up to 30mph, and more at higher speeds.")],
        "sources": [HC, ("GOV.UK — Highway Code changes 2022", "https://www.gov.uk/government/news/the-highway-code-8-changes-you-need-to-know-from-29-january-2022")],
        "related": ["manchester-city-centre-driving-guide", "why-learners-fail-the-driving-test", "theory-test-greater-manchester"],
    },
]

# ---------------------------------------------------------------- TEST CENTRES
# Areas each centre commonly serves come from the boroughs nearest to it.
# Addresses and pass rates are deliberately not repeated: they change and
# third-party sources disagree. Learners are pointed to GOV.UK instead.
CENTRES = [
    ("cheetham-hill", "Cheetham Hill", "North Manchester", ["Manchester", "Salford", "Bury"],
     "Cheetham Hill is one of the city's two practical test centres, serving north Manchester and nearby parts of Salford and Bury.",
     "Expect busy, multi-lane main roads such as Bury New Road (A56) and Cheetham Hill Road, multi-lane roundabouts, bus stops, parked cars on narrow side streets and traffic lights that change quickly.",
     ["Lane discipline on multi-lane roundabouts", "Bus lanes and bus stops on main roads", "Meeting traffic on narrow, parked-up streets", "Observations at busy junctions"]),
    ("west-didsbury", "West Didsbury", "South Manchester", ["Manchester", "Trafford", "Stockport"],
     "West Didsbury serves south Manchester — Didsbury, Chorlton, Withington, Fallowfield and beyond — and is popular with learners from Trafford and Stockport too.",
     "Routes often include busy stretches like Wilmslow Road with bus lanes and lots of pedestrians, residential streets with parked cars, and a mix of roundabouts and traffic-light junctions.",
     ["Reading bus lane signs and times", "Pedestrians and cyclists in busy areas", "Clutch or brake control in stop-start traffic", "Parking and narrow residential roads"]),
    ("sale", "Sale", "Trafford", ["Trafford", "Manchester"],
     "Sale serves Trafford — Sale, Altrincham, Stretford, Urmston and surrounding areas — and parts of south Manchester.",
     "Expect suburban roads, dual carriageways, roundabouts and roads near the M60, plus busy town-centre streets.",
     ["Dual carriageway joining and lane discipline", "Roundabouts of different sizes", "Suburban junctions with parked cars", "Independent driving with sat-nav"]),
    ("bredbury", "Bredbury", "Stockport", ["Stockport", "Tameside"],
     "Bredbury serves Stockport and nearby Tameside — Bredbury, Romiley, Marple, Hazel Grove, Reddish and more.",
     "Routes can include faster roads near the M60, busy roundabouts, hills and residential estates.",
     ["Higher-speed roads and joining traffic", "Busy roundabouts", "Hill starts and control", "Junction observations on fast roads"]),
    ("chadderton", "Chadderton", "Oldham", ["Oldham", "Rochdale", "Tameside"],
     "Chadderton serves Oldham and nearby parts of Rochdale and Tameside — Chadderton, Royton, Failsworth, Middleton and beyond.",
     "Expect hills, busy main roads, roundabouts and roads near the A627(M) and M60.",
     ["Hill starts and gear/brake control", "Main-road junctions", "Roundabouts", "Following road signs"]),
    ("rochdale", "Rochdale", "Rochdale", ["Rochdale", "Oldham"],
     "Rochdale's test centre serves Rochdale, Heywood, Middleton, Milnrow, Littleborough and surrounding areas.",
     "Routes can mix town-centre traffic, the ring road, faster roads towards the A627(M) and M62, and quieter country roads.",
     ["Town-centre lanes and junctions", "Faster roads and country roads", "Roundabouts", "Independent driving"]),
    ("bolton", "Bolton", "Bolton", ["Bolton", "Bury", "Wigan"],
     "Bolton serves Bolton and nearby Bury and Wigan — Farnworth, Kearsley, Westhoughton, Horwich, Bromley Cross and more.",
     "Expect ring roads such as St Peter's Way (A666), busy town-centre roundabouts and roads near the M61.",
     ["Multi-lane town-centre roundabouts", "Ring road lane choice", "Busy junctions", "Following signs to a destination"]),
    ("bury", "Bury", "Bury", ["Bury", "Bolton", "Rochdale"],
     "Bury's test centre serves Bury, Radcliffe, Prestwich, Whitefield, Tottington, Ramsbottom and nearby areas.",
     "Routes can include the town-centre ring road, main roads such as the A56, and roads near the M66 and M60.",
     ["Ring road lane discipline", "Main-road junctions", "Roundabouts", "Residential roads with parked cars"]),
    ("hyde", "Hyde", "Tameside", ["Tameside", "Stockport"],
     "Hyde serves Tameside — Hyde, Denton, Dukinfield, Stalybridge, Ashton-under-Lyne — and nearby parts of Stockport.",
     "Expect hilly roads, busy town centres, roundabouts and roads near the M60 and M67.",
     ["Hill starts", "Town-centre traffic", "Roundabouts", "Faster roads near the motorway"]),
    ("atherton", "Atherton", "Wigan", ["Wigan", "Salford", "Bolton"],
     "Atherton serves the Wigan borough — Atherton, Leigh, Tyldesley, Hindley and beyond — and parts of Salford and Bolton.",
     "Expect suburban and semi-rural roads, roundabouts and main roads such as the A577 and A580 East Lancs Road.",
     ["Higher-speed main roads", "Roundabouts", "Semi-rural bends and junctions", "Independent driving"]),
]
