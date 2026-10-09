from layout import *

GOV = '<a href="{u}" target="_blank" rel="noopener">{t}</a>'

GUIDES = [
    ("provisional-licence", "How to get your provisional licence", "shield", "Step 1 of every learner's journey — who can apply, what you need and when you can start lessons.", """
<h2>Who can apply?</h2>
<p>You can apply for your provisional driving licence from the age of <b>15 years and 9 months</b>. You can start driving a car on public roads when you turn <b>17</b> (or 16 if you receive the higher or enhanced rate mobility component of Personal Independence Payment).</p>
<h2>How to apply</h2>
<ol><li>Apply online at """ + GOV.format(u="https://www.gov.uk/apply-first-provisional-driving-licence", t="GOV.UK") + """ — it's the quickest way.</li>
<li>Have your identity document ready (for example, a UK passport), your addresses for the last 3 years and your National Insurance number if you know it.</li>
<li>Pay the fee by card. Check GOV.UK for the current fee.</li>
<li>Your photocard licence usually arrives within about a week if you apply online.</li></ol>
<h2>Watch out for copycat websites</h2>
<p>Only apply through GOV.UK. Some websites charge extra to "help" you apply — you don't need them.</p>
<h2>What next?</h2>
<p>Once your licence arrives you can book your first SQ lesson and start revising for your theory test in the DriveSQ Student Portal.</p>"""),
    ("theory-test-guide", "The complete theory test guide", "quiz", "How the theory test works, the pass marks, and how to prepare using free tools.", """
<h2>Two parts, one test</h2>
<p>The car theory test has two parts, taken on the same day. You must pass both.</p>
<h3>1. Multiple-choice questions</h3>
<ul><li>50 questions in 57 minutes</li><li>Pass mark: <b>43 out of 50</b></li><li>Includes a video case study with questions about it</li></ul>
<h3>2. Hazard perception</h3>
<ul><li>14 video clips showing everyday road scenes</li><li>Click when you see a developing hazard — the earlier you spot it, the more points you score</li><li>Maximum 75 points, pass mark <b>44</b></li></ul>
<h2>Your pass certificate</h2>
<p>Your theory test pass lasts <b>2 years</b>. You must pass your practical test within that time or take the theory test again.</p>
<h2>How to prepare</h2>
<ul><li>Read the Highway Code — every question is based on it.</li><li>Use the theory library and full 50-question mock tests in the DriveSQ Student Portal (free for SQ learners).</li><li>Warm up with our <a href="../theory-quiz.html">theory quiz</a>, <a href="../road-signs.html">road sign flashcards</a> and <a href="../hazard-game.html">spot-the-hazard game</a>.</li></ul>
<p>Book your theory test on """ + GOV.format(u="https://www.gov.uk/book-theory-test", t="GOV.UK") + """ and bring your photocard provisional licence on the day.</p>"""),
    ("show-me-tell-me", "Show me, tell me questions explained", "eye", "The vehicle safety questions you'll be asked on your practical test — with answers.", """
<p>During your practical test you'll be asked two vehicle safety questions: one <b>"tell me"</b> question at the start, before you drive, and one <b>"show me"</b> question while you're driving. Getting one or both wrong is a driving fault (a minor).</p>
<h2>Tell me questions (examples)</h2>
<ul>
<li><b>How would you check the brakes are working before starting a journey?</b> Brakes shouldn't feel spongy or slack. Test them as you set off — the car shouldn't pull to one side.</li>
<li><b>Where would you find the recommended tyre pressures and how would you check them?</b> In the manufacturer's guide. Use a reliable pressure gauge, check when tyres are cold, don't forget the spare and refit the valve caps.</li>
<li><b>How would you check the head restraint is correctly adjusted?</b> The rigid part should be at least as high as your eyes or the top of your ears, and as close to the back of your head as is comfortable.</li>
<li><b>How would you check the tyres have enough tread and are in good condition?</b> No cuts or bulges, and at least 1.6mm of tread across the central three-quarters of the tyre, all the way around.</li>
<li><b>How would you switch on the rear fog lights and when would you use them?</b> Operate the switch (a warning light shows). Use them when visibility is seriously reduced — generally below 100 metres.</li>
<li><b>How would you switch to main beam and how would you know it's on?</b> Operate the switch; a blue warning light shows on the dashboard.</li>
<li><b>How would you know if there was a problem with the anti-lock braking system?</b> The ABS warning light would stay on.</li>
</ul>
<h2>Show me questions (examples)</h2>
<ul>
<li>When it's safe to do so, show me how you wash and clean the front windscreen.</li>
<li>Show me how you'd switch on your dipped headlights.</li>
<li>Show me how you'd set the rear demister.</li>
<li>Show me how you'd operate the horn.</li>
<li>Show me how you'd demist the front windscreen.</li>
<li>Show me how you'd open and close the side window.</li>
</ul>
<p>Your SQ instructor will practise every one of these with you in the car you'll take your test in.</p>"""),
    ("manoeuvres", "Driving test manoeuvres guide", "car", "Parallel parking, bay parking, pulling up on the right and the emergency stop.", """
<p>On your practical test you'll be asked to do <b>one</b> of these reversing manoeuvres:</p>
<h2>Parallel park</h2>
<p>Pull up alongside a parked car and reverse in behind it, finishing reasonably close and parallel to the kerb within about two car lengths.</p>
<h2>Park in a bay</h2>
<p>Either drive in and reverse out, or reverse in and drive out — the examiner will tell you which.</p>
<h2>Pull up on the right</h2>
<p>Pull up on the right-hand side of the road, reverse for about two car lengths, then rejoin the traffic safely.</p>
<h2>The emergency stop</h2>
<p>You may also be asked to do an emergency stop — it happens in around one in three tests. Brake firmly and promptly while keeping control.</p>
<h2>Key skills for every manoeuvre</h2>
<ul><li><b>Control:</b> slow, steady speed — clutch control in a manual, gentle brake control in an automatic.</li><li><b>Observation:</b> all-round checks before and during the manoeuvre. Stop for anyone approaching.</li><li><b>Accuracy:</b> finish in the right place without mounting the kerb.</li></ul>
<p>Every manoeuvre is tracked as its own skill in the DriveSQ Student Portal, so you'll know when each one reaches "Independent".</p>"""),
    ("roundabouts", "How to drive on roundabouts", "road", "Lanes, signals and priority — roundabouts made simple, the Highway Code way.", """
<h2>The basics</h2>
<ul><li>Use MSPSL on approach: <b>Mirror, Signal, Position, Speed, Look</b>.</li><li>Give way to traffic coming from your <b>right</b>, unless signs or markings say otherwise.</li><li>Keep moving if the way is clear — but be ready to stop.</li></ul>
<h2>Which lane and which signal?</h2>
<h3>Taking the first exit (turning left)</h3>
<p>Signal left on approach, approach in the left-hand lane and keep left on the roundabout.</p>
<h3>Going straight ahead</h3>
<p>Usually no signal on approach. Approach in the correct lane (normally the left, unless markings say otherwise), then signal left after you pass the exit before the one you want.</p>
<h3>Turning right (exits past 12 o'clock)</h3>
<p>Signal right on approach, approach in the right-hand lane and keep to the right on the roundabout. Signal left after you pass the exit before the one you want.</p>
<h2>Watch out for</h2>
<ul><li>Cyclists and horse riders, who may stay in the left lane while signalling right.</li><li>Long vehicles, which may take up more than one lane.</li><li>Lane markings on big Manchester roundabouts — they override the general rule.</li></ul>"""),
    ("test-day-checklist", "Driving test day checklist", "flag", "Everything to bring, check and remember on the day of your practical test.", """
<h2>Bring</h2>
<ul><li>Your UK photocard provisional driving licence.</li><li>Glasses or contact lenses if you need them to drive.</li><li>A suitable car — we can provide an SQ car for your test.</li></ul>
<h2>The test itself</h2>
<ul><li><b>Eyesight check:</b> read a number plate from 20 metres.</li><li><b>Tell me question</b> before you drive, and a <b>show me question</b> while driving.</li><li><b>About 40 minutes</b> of driving, including about 20 minutes of independent driving following a sat-nav or road signs.</li><li><b>One reversing manoeuvre</b>, and possibly an emergency stop.</li><li>Up to <b>15 driving faults</b> and no serious or dangerous faults to pass.</li></ul>
<h2>On the day</h2>
<ul><li>Book a warm-up lesson with us beforehand.</li><li>Arrive at the test centre early.</li><li>If you make a mistake, keep calm and keep going — one error doesn't mean you've failed.</li></ul>
<p>Use our <a href="../tools.html#readiness">readiness checker</a> and your portal checklist to know you're ready before you book.</p>"""),
    ("manual-vs-automatic", "Manual or automatic: which should you learn?", "auto", "The pros and cons of each — and why more Manchester learners are choosing automatic.", """
<h2>The licence difference</h2>
<p>If you pass in an <b>automatic</b>, your licence only lets you drive automatic cars. If you pass in a <b>manual</b>, you can drive both.</p>
<h2>Why choose automatic?</h2>
<ul><li>No clutch or gears — more brainpower for the road.</li><li>Easier in stop-start city traffic.</li><li>Electric cars are automatic, and sales of new petrol and diesel cars are being phased out in the UK.</li></ul>
<h2>Why choose manual?</h2>
<ul><li>Your licence covers both manual and automatic cars.</li><li>Useful if you might drive older or family-owned manual cars.</li></ul>
<h2>Does it cost more?</h2>
<p>Not with SQ — manual and automatic lessons are the same price: £70 for a 2-hour lesson.</p>
<p>Not sure? Our <a href="../tools.html#lessons">lesson calculator</a> shows how the choice might affect your hours.</p>"""),
    ("nervous-drivers", "Learning to drive as a nervous driver", "heart", "Practical ways to beat driving anxiety — and how we teach nervous learners.", """
<h2>You're not alone</h2>
<p>Feeling nervous about driving is extremely common. The good news: confidence is a skill you build, just like steering.</p>
<h2>What helps</h2>
<ul><li><b>Start somewhere quiet.</b> We begin on calm residential roads and only move on when you're ready.</li><li><b>See your progress.</b> The DriveSQ Student Portal shows every skill improving lesson by lesson — proof you're getting better.</li><li><b>Longer lessons.</b> Our 2-hour lessons give you time to settle in before trying anything new.</li><li><b>Know what's coming.</b> Your instructor's notes tell you what you'll work on next time, so there are no surprises.</li><li><b>Breathe.</b> Slow breathing before you move off really does calm your nervous system.</li></ul>
<h2>Tell us</h2>
<p>Let us know you're nervous when you book. We'll plan your first lessons around it.</p>"""),
    ("failed-driving-test", "Failed your driving test? What to do next", "target", "How to bounce back, when you can rebook and how to fix the faults that cost you.", """
<h2>First: it happens</h2>
<p>Lots of people don't pass first time. A fail is information — it tells you exactly what to work on.</p>
<h2>When can you retake?</h2>
<p>You have to wait at least <b>10 working days</b> before you can take another practical test. Book on """ + GOV.format(u="https://www.gov.uk/book-driving-test", t="GOV.UK") + """.</p>
<h2>Use your test report</h2>
<p>Your examiner marks every fault on your driving test report. Bring it to your next SQ lesson — your instructor will log those faults as focus skills in your DriveSQ Student Portal.</p>
<h2>A plan that works</h2>
<ul><li>A 10-hour block focused on your faults (£350, or £320 with a discount).</li><li>A full mock test before your retest.</li><li>Test route practice around your test centre.</li></ul>"""),
    ("cost-of-learning-to-drive-manchester", "How much does it cost to learn to drive in Manchester?", "pound", "A clear breakdown of lessons, test fees and ways to save in Greater Manchester.", """
<h2>Lessons</h2>
<p>The DVSA says learners typically need around <b>45 hours</b> of lessons plus about 22 hours of private practice. Everyone is different — try our <a href="../tools.html#lessons">lesson calculator</a>.</p>
<table class="table"><tr><th>Hours</th><th>Standard (£35/hr)</th><th>With NHS / student / M16·M18·M19 blocks</th></tr>
<tr><td>20 hours</td><td>£700</td><td>£640</td></tr><tr><td>30 hours</td><td>£1,050</td><td>£960</td></tr><tr><td>40 hours</td><td>£1,400</td><td>£1,280</td></tr><tr><td>45 hours</td><td>£1,575</td><td>£1,455</td></tr></table>
<h2>Test fees (paid to the DVSA)</h2>
<ul><li>Theory test: £23</li><li>Practical test: £62 on weekdays, £75 on evenings, weekends and bank holidays</li></ul>
<p>Fees can change — check """ + GOV.format(u="https://www.gov.uk/driving-test-cost", t="GOV.UK") + """.</p>
<h2>Ways to save</h2>
<ul><li>Book 10-hour blocks with a discount: NHS, students and M16/M18/M19 pay £320.</li><li>Use the free DriveSQ Student Portal to revise theory instead of paying for apps.</li><li>Choose 2-hour lessons — more learning per journey.</li></ul>
<p>Work out your own total with our <a href="../prices.html">package builder and cost calculator</a>.</p>"""),
    ("wet-weather-driving", "Driving in Manchester rain, fog and ice", "moon", "Stay safe in the weather Manchester is famous for.", """
<h2>Rain</h2>
<ul><li>Stopping distances are <b>at least double</b> on wet roads — leave a gap of at least four seconds.</li><li>Use dipped headlights when visibility is reduced.</li><li>If the steering feels light in standing water (aquaplaning), ease off the accelerator and don't brake sharply.</li></ul>
<h2>Fog</h2>
<ul><li>Use fog lights when visibility drops below about <b>100 metres</b>, and switch them off when it improves.</li><li>Slow down — you need to be able to stop in the distance you can see is clear.</li></ul>
<h2>Ice and snow</h2>
<ul><li>Stopping distances can be up to <b>ten times</b> longer.</li><li>Clear all windows and lights completely before setting off.</li><li>Use gentle steering, braking and acceleration. Pull away in a higher gear in a manual car to reduce wheelspin.</li></ul>
<p>Ask us to add a night or all-weather lesson to your package.</p>"""),
]


def guides_hub():
    root = ""
    cards = "".join(f'<a class="card" href="guides/{s}.html" data-reveal="up" data-tilt="6"><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p>{d}</p><span class="red mono" style="font-size:.8rem">READ GUIDE →</span></a>' for s, t, i, d, _ in GUIDES)
    body = page_hero("Learner guides", "Everything you need to know.", "Free guides for learner drivers in Greater Manchester, from your provisional licence to passing your test.", ["Guides"], root)
    body += f'<section class="section--tight"><div class="container"><div class="grid grid--3" data-stagger=".05">{cards}</div></div></section>{cta(root)}'
    return page("guides.html", "Learner Driver Guides | Theory, Test & Tips | SQ Driving School",
                "Free learner driver guides: provisional licence, theory test, show me tell me, manoeuvres, roundabouts, test day, costs and more.", body, root)


def guide_page(g):
    slug, title, ic, desc, html = g
    root = "../"
    others = "".join(f'<a class="chip" href="{s}.html">{t}</a>' for s, t, *_ in GUIDES if s != slug)[:4000]
    schema = [{"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
               "author": {"@type": "Organization", "name": "SQ Driving School"}, "publisher": {"@type": "Organization", "name": "SQ Driving School"}}]
    body = page_hero("Learner guide", title, desc, [f'<a href="{root}guides.html">Guides</a>', title], root)
    body += f"""<section class="section--tight"><div class="container"><article class="prose" data-reveal="up">{html}</article>
<div class="mt-4"><h3>More guides</h3><div class="hero__badges">{others}</div></div></div></section>
{cta(root)}"""
    return page(f"guides/{slug}.html", f"{title} | SQ Driving School", desc, body, root, active="guides.html", schema=schema)


def sign(kind):
    T = '<polygon points="50,8 94,86 6,86" fill="#fff" stroke="#d4161d" stroke-width="9" stroke-linejoin="round"/>'
    RING = '<circle cx="50" cy="50" r="42" fill="#fff" stroke="#d4161d" stroke-width="10"/>'
    BLUE = '<circle cx="50" cy="50" r="44" fill="#1e5bbf" stroke="#fff" stroke-width="3"/>'
    s = {
        "stop": '<polygon points="30,4 70,4 96,30 96,70 70,96 30,96 4,70 4,30" fill="#d4161d" stroke="#fff" stroke-width="4"/><text x="50" y="60" font-family="Arial Black,Arial" font-weight="900" font-size="26" fill="#fff" text-anchor="middle">STOP</text>',
        "giveway": '<polygon points="6,14 94,14 50,90" fill="#fff" stroke="#d4161d" stroke-width="9" stroke-linejoin="round"/>',
        "noentry": '<circle cx="50" cy="50" r="46" fill="#d4161d"/><rect x="16" y="42" width="68" height="16" fill="#fff"/>',
        "30": RING + '<text x="50" y="63" font-family="Arial Black,Arial" font-weight="900" font-size="36" fill="#111" text-anchor="middle">30</text>',
        "nsl": '<circle cx="50" cy="50" r="44" fill="#fff" stroke="#111" stroke-width="2"/><line x1="78" y1="20" x2="22" y2="80" stroke="#111" stroke-width="16"/>',
        "noright": RING + '<path d="M38 74V48h22" fill="none" stroke="#111" stroke-width="8"/><path d="M56 36l14 12-14 12z" fill="#111"/><line x1="22" y1="22" x2="78" y2="78" stroke="#d4161d" stroke-width="9"/>',
        "ahead": BLUE + '<path d="M50 78V34" stroke="#fff" stroke-width="10"/><path d="M32 42l18-20 18 20z" fill="#fff"/>',
        "left": BLUE + '<path d="M74 50H38" stroke="#fff" stroke-width="10"/><path d="M42 32L22 50l20 18z" fill="#fff"/>',
        "mini": BLUE + '<circle cx="50" cy="50" r="22" fill="none" stroke="#fff" stroke-width="7" stroke-dasharray="30 16"/><path d="M68 34l6 14-14-2z M30 70l-6-14 14 2z M36 26l14-4-4 14z" fill="#fff"/>',
        "roundabout": T + '<circle cx="50" cy="60" r="13" fill="none" stroke="#111" stroke-width="5" stroke-dasharray="18 10"/><path d="M62 50l3 9-9-1z M38 70l-3-9 9 1z" fill="#111"/>',
        "crossroads": T + '<path d="M50 38v40M32 60h36" stroke="#111" stroke-width="8"/>',
        "signals": T + '<rect x="42" y="36" width="16" height="40" rx="4" fill="#111"/><circle cx="50" cy="45" r="4.5" fill="#ff3b3b"/><circle cx="50" cy="56" r="4.5" fill="#ffb020"/><circle cx="50" cy="67" r="4.5" fill="#22e07a"/>',
        "nostopping": '<circle cx="50" cy="50" r="42" fill="#1e5bbf" stroke="#d4161d" stroke-width="10"/><path d="M22 22l56 56M78 22L22 78" stroke="#d4161d" stroke-width="9"/>',
        "nowaiting": '<circle cx="50" cy="50" r="42" fill="#1e5bbf" stroke="#d4161d" stroke-width="10"/><path d="M22 22l56 56" stroke="#d4161d" stroke-width="9"/>',
        "twoway": T + '<path d="M40 76V48M60 40v28" stroke="#111" stroke-width="6"/><path d="M33 52l7-12 7 12zM53 64l7 12 7-12z" fill="#111"/>',
    }[kind]
    return f'<svg viewBox="0 0 100 100" aria-hidden="true">{s}</svg>'


SIGNS = [("stop", "Stop and give way", "Order", "You must stop completely at the line, then give way to traffic on the major road."),
         ("giveway", "Give way to traffic on the major road", "Order", "Slow down and be ready to stop. Give way to traffic on the major road."),
         ("noentry", "No entry for vehicular traffic", "Order", "You must not enter the road. Often seen at the end of one-way streets."),
         ("30", "Maximum speed 30mph", "Order", "A red ring with a number shows the maximum speed limit."),
         ("nsl", "National speed limit applies", "Order", "For cars: 60mph on single carriageways, 70mph on dual carriageways and motorways."),
         ("noright", "No right turn", "Order", "Red circles prohibit. The red diagonal bar means 'don't do this'."),
         ("ahead", "Ahead only", "Order", "Blue circles give positive (mandatory) instructions."),
         ("left", "Turn left (ahead)", "Order", "A mandatory instruction to turn left."),
         ("mini", "Mini-roundabout", "Order", "Give way to traffic from the right. Go around the central marking."),
         ("roundabout", "Roundabout ahead", "Warning", "Triangles warn. Prepare to give way to traffic from the right."),
         ("crossroads", "Crossroads ahead", "Warning", "A junction where roads cross — look out for traffic from both sides."),
         ("signals", "Traffic signals ahead", "Warning", "Traffic lights ahead. Be ready to stop."),
         ("twoway", "Two-way traffic straight ahead", "Warning", "You're leaving a one-way section — expect oncoming traffic."),
         ("nostopping", "No stopping (clearway)", "Order", "You must not stop on the main carriageway, even to set down or pick up passengers."),
         ("nowaiting", "No waiting", "Order", "Waiting restrictions apply — check the times on the nearby plate.")]


def signs_page():
    root = ""
    cards = ""
    for k, name, typ, what in SIGNS:
        cards += f"""<div class="flash" tabindex="0" role="button" aria-label="Flashcard: tap to reveal what this sign means" data-reveal="zoom"><div class="flash__inner">
<div class="flash__face">{sign(k)}<div class="flash__hint">Tap to flip</div></div>
<div class="flash__face flash__back"><span class="tag">{typ}</span><h3 class="mt-1">{name}</h3><p class="note">{what}</p><div class="flash__actions"><button class="btn btn--sm btn--ghost" type="button" data-know="no">Still learning</button><button class="btn btn--sm btn--red" type="button" data-know="yes">I knew it</button></div></div>
</div></div>"""
    body = page_hero("Road sign flashcards", "Learn the signs. Flip the cards.", "Tap a sign to flip it. Mark the ones you know and watch your score build. Circles give orders, triangles warn, rectangles inform.", ["Road signs"], root)
    body += f"""<section class="section--tight"><div class="container" data-tool="flash">
<div class="hud"><span class="chip">Known <b class="js-known">0</b> / {len(SIGNS)}</span><button class="btn btn--ghost btn--sm js-shuffle" type="button">Shuffle</button><a class="btn btn--ghost btn--sm" href="theory-quiz.html">Theory quiz</a></div>
<div class="grid grid--4 js-flash-grid" data-stagger=".04">{cards}</div>
<p class="note mt-2">Simplified illustrations for learning. See the official <a class="red" href="https://www.gov.uk/guidance/the-highway-code/traffic-signs" target="_blank" rel="noopener">Highway Code traffic signs</a>.</p></div></section>
{cta(root)}"""
    return page("road-signs.html", "Road Sign Flashcards | Learn UK Road Signs | SQ Driving School",
                "Interactive UK road sign flashcards for learner drivers. Flip, learn and test yourself — free from SQ Driving School.", body, root)


LIGHTS = [("red", "Oil pressure", "Stop", '<path d="M6 30h22l10-8h6l-4 10H12z" fill="none" stroke="currentColor" stroke-width="3"/><path d="M40 16c2 3 3 5 0 7" fill="none" stroke="currentColor" stroke-width="3"/>', "Low oil pressure. Stop as soon as it's safe, switch off the engine and check the oil level. Don't drive until it's fixed."),
          ("red", "Battery / charging", "Stop", '<rect x="6" y="14" width="36" height="22" rx="3" fill="none" stroke="currentColor" stroke-width="3"/><path d="M12 10v4M36 10v4M14 25h6M30 22v6M27 25h6" stroke="currentColor" stroke-width="3"/>', "The charging system isn't working properly. Get it checked straight away — the car may stop when the battery runs flat."),
          ("red", "Brake system", "Stop", '<circle cx="24" cy="24" r="12" fill="none" stroke="currentColor" stroke-width="3"/><path d="M8 12a20 20 0 0 0 0 24M40 12a20 20 0 0 1 0 24M24 17v9M24 30v1" stroke="currentColor" stroke-width="3" fill="none"/>', "Usually the handbrake is on. If it stays on with the handbrake off, brake fluid may be low or there's a brake fault — stop safely and get help."),
          ("red", "Engine temperature", "Stop", '<path d="M24 8v20M18 14h6M18 20h6" stroke="currentColor" stroke-width="3"/><circle cx="24" cy="32" r="5" fill="currentColor"/><path d="M8 40c4-3 8 3 12 0s8 3 12 0 8 3 8 0" fill="none" stroke="currentColor" stroke-width="3"/>', "The engine is overheating. Stop safely, switch off and let it cool. Never open a hot coolant cap."),
          ("red", "Airbag fault", "Check now", '<circle cx="18" cy="12" r="4" fill="currentColor"/><path d="M14 20l-4 16h12l6-10M26 22a9 9 0 1 1 14 8" fill="none" stroke="currentColor" stroke-width="3"/>', "A fault with the airbag system. The airbags may not work in a crash — get it checked as soon as possible."),
          ("red", "Seat belt reminder", "Check now", '<circle cx="24" cy="10" r="4" fill="currentColor"/><path d="M16 40V20h16v20M18 18l14 18" fill="none" stroke="currentColor" stroke-width="3"/>', "Someone isn't wearing a seat belt. The driver is responsible for passengers under 14."),
          ("amber", "Engine management", "Check soon", '<path d="M8 18h6v-4h12v4h6l4 4h4v12h-4l-4 4H14l-6-6z" fill="none" stroke="currentColor" stroke-width="3"/>', "The engine has detected a fault. Get it checked soon. If it's flashing, reduce speed and get it checked immediately."),
          ("amber", "ABS fault", "Check soon", '<circle cx="24" cy="24" r="14" fill="none" stroke="currentColor" stroke-width="3"/><text x="24" y="29" font-size="11" font-family="Arial" font-weight="700" fill="currentColor" text-anchor="middle">ABS</text>', "Anti-lock brakes aren't working. Normal braking still works, but the wheels may lock under hard braking. Get it checked."),
          ("amber", "Tyre pressure", "Check soon", '<path d="M10 14c-3 6-3 14 0 20h28c3-6 3-14 0-20" fill="none" stroke="currentColor" stroke-width="3"/><path d="M24 18v10M24 31v2" stroke="currentColor" stroke-width="3"/>', "One or more tyres may be under-inflated. Check and adjust pressures when the tyres are cold."),
          ("amber", "Power steering", "Check soon", '<circle cx="24" cy="24" r="13" fill="none" stroke="currentColor" stroke-width="3"/><path d="M24 24v13M11 24h26" stroke="currentColor" stroke-width="3"/>', "Steering assistance fault — the steering may feel heavy. Drive carefully and get it checked."),
          ("amber", "Rear fog light", "Info", '<path d="M26 12c-8 0-8 24 0 24s8-24 0-24z" fill="none" stroke="currentColor" stroke-width="3"/><path d="M20 16H8M20 24H8M20 32H8M30 6v36" stroke="currentColor" stroke-width="3"/>', "Your rear fog light is on. Use it only when visibility is below about 100 metres."),
          ("green", "Dipped headlights", "Info", '<path d="M22 12c-8 0-8 24 0 24 8 0 12-6 12-12s-4-12-12-12z" fill="none" stroke="currentColor" stroke-width="3"/><path d="M38 16l6 2M38 24l6 2M38 32l6 2" stroke="currentColor" stroke-width="3"/>', "Your dipped headlights are on."),
          ("blue", "Main beam", "Info", '<path d="M22 12c-8 0-8 24 0 24 8 0 12-6 12-12s-4-12-12-12z" fill="none" stroke="currentColor" stroke-width="3"/><path d="M38 16h8M38 24h8M38 32h8" stroke="currentColor" stroke-width="3"/>', "Full beam is on. Dip your lights for oncoming traffic and when following another vehicle.")]


def dash_page():
    root = ""
    level = {"red": "Red — stop or act now", "amber": "Amber — check soon", "green": "Green — information", "blue": "Blue — information"}
    lights = "".join(f'<button type="button" class="dlight dlight--{c}" data-name="{n}" data-level="{level[c]}" data-what="{w}" aria-pressed="false"><svg viewBox="0 0 48 48" aria-hidden="true">{svg}</svg>{n}</button>' for c, n, _, svg, w in LIGHTS)
    body = page_hero("Dashboard lights", "Know your warning lights.", "Tap a light to find out what it means and what to do. Red means act now. Amber means check soon. Green and blue are information.", ["Dashboard lights"], root)
    body += f"""<section class="section--tight"><div class="container"><div class="dash" data-tool="dash" data-reveal="zoom">
<div class="hud"><button class="btn btn--red btn--sm js-ignite" type="button">{icon('bolt')} Ignition on</button><span class="chip">Red <b>act now</b></span><span class="chip">Amber <b>check soon</b></span></div>
<div class="dash__grid">{lights}</div>
<div class="dinfo" role="status" aria-live="polite"><p class="note">Tap a light above.</p></div>
</div><p class="note mt-2">Symbols vary between car makes — always check your car's handbook.</p></div></section>
{cta(root)}"""
    return page("dashboard-lights.html", "Car Dashboard Warning Lights Explained | SQ Driving School",
                "Interactive guide to car dashboard warning lights for learner drivers. Tap a light to see what it means and what to do.", body, root)
