from layout import *
from pages_book import wizard_html

AREAS = ["Manchester", "Salford", "Trafford", "Stockport", "Tameside", "Oldham", "Rochdale", "Bury", "Bolton", "Wigan",
         "Levenshulme", "Gorton", "Old Trafford", "Whalley Range", "Didsbury", "Chorlton", "Fallowfield", "Sale", "Altrincham", "Eccles", "Ashton-under-Lyne", "Middleton"]


def marquee():
    items = "".join(f'<span class="marquee__item">{a}</span>' for a in AREAS)
    return f'<div class="marquee" aria-label="Areas we cover"><div class="marquee__track">{items}{items}</div></div>'


def postcode_form(big=False, label="Enter your postcode"):
    return f"""<form class="pc-form" data-tool="postcode" novalidate>
  <div class="field"><label for="pc-{id(label)}{big}">{label}</label>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <input class="input {'input--big' if big else ''}" id="pc-{id(label)}{big}" name="postcode" autocomplete="postal-code" placeholder="e.g. M19 2AB" style="flex:1;min-width:180px" required>
      <button class="btn btn--red" type="submit">{icon('pin')} Check</button>
    </div>
  </div>
  <div class="result" role="status" aria-live="polite"></div>
</form>"""


def price_cards(root):
    return f"""<div class="grid grid--3" data-stagger=".12">
  <article class="card price-card" data-reveal="up" data-tilt="6">
    <div class="eyebrow">Taster</div>
    <h3>Single 1-hour session</h3>
    <div class="price">£40<small> / 1 hr</small></div>
    <p>A one-off hour — perfect for an assessment or a quick refresher.</p>
    <ul><li>Manual or automatic</li><li>Door-to-door pick-up</li><li>Free DriveSQ Student Portal</li></ul>
    <a class="btn btn--ghost btn--block" data-wa="Hi! I'd like to book a single 1-hour session (£40)." href="https://wa.me/{WA}">Book 1 hour</a>
  </article>
  <article class="card price-card price-card--featured neon-border" data-reveal="up" data-tilt="6">
    <span class="price-card__tag">Most popular</span>
    <div class="eyebrow">Standard lesson</div>
    <h3>2-hour lesson</h3>
    <div class="price">£70<small> / 2 hrs</small></div>
    <p>Just £35 an hour. Our standard lesson — two hours means real progress every time.</p>
    <ul><li>£35 per hour</li><li>2-hour minimum for real progress</li><li>Manual or automatic</li><li>Progress logged in your portal</li></ul>
    <a class="btn btn--red btn--block" data-wa="Hi! I'd like to book a 2-hour lesson (£70)." href="https://wa.me/{WA}">Book 2 hours</a>
  </article>
  <article class="card price-card" data-reveal="up" data-tilt="6">
    <div class="eyebrow">Block booking</div>
    <h3>10-hour block</h3>
    <div class="price">£350<small> / 10 hrs</small></div>
    <p><b class="red">£320</b> for NHS staff, students and learners in M16, M18 &amp; M19.</p>
    <ul><li>Lock in your rate</li><li>Priority lesson slots</li><li>Discounts available</li><li>Full portal access</li></ul>
    <a class="btn btn--ghost btn--block" data-wa="Hi! I'd like to book a 10-hour block." href="https://wa.me/{WA}">Book a block</a>
  </article>
</div>"""


def builder(root):
    addons = [("Mock test", 2), ("Motorway lesson", 2), ("Night driving", 2), ("Test route practice", 2)]
    ad = "".join(f'<input type="checkbox" name="addon" id="ad{i}" data-hours="{h}" data-label="{n}"><label for="ad{i}">+ {n} ({h} hrs)</label>' for i, (n, h) in enumerate(addons))
    return f"""<div class="tool neon-border" data-tool="builder" data-reveal="up">
  <div class="tool__head"><div class="card__icon">{icon('layers')}</div><div><h3>Package builder</h3><p class="mb-0 note">Build your own package and see the price live.</p></div></div>
  <div class="grid grid--2" style="align-items:start">
    <div>
      <div class="field"><span class="label">Gearbox</span><div class="seg">
        <input type="radio" name="trans" id="bt1" value="Manual" checked><label for="bt1">Manual</label>
        <input type="radio" name="trans" id="bt2" value="Automatic"><label for="bt2">Automatic</label></div></div>
      <div class="field"><span class="label">Booking type</span><div class="seg">
        <input type="radio" name="type" id="ty1" value="hours" checked><label for="ty1">Lessons / blocks</label>
        <input type="radio" name="type" id="ty2" value="single"><label for="ty2">Single 1-hour (£40)</label></div></div>
      <div class="field"><label for="hrs">How many hours? <b class="js-hours red">10 hours</b></label>
        <input class="range" type="range" id="hrs" name="hours" min="2" max="60" step="2" value="10"></div>
      <div class="field"><span class="label">Discount</span><div class="seg">
        <input type="radio" name="discount" id="dc0" value="none" data-label="None" checked><label for="dc0">None</label>
        <input type="radio" name="discount" id="dc1" value="nhs" data-label="NHS discount"><label for="dc1">NHS</label>
        <input type="radio" name="discount" id="dc2" value="student" data-label="Student discount"><label for="dc2">Student</label>
        <input type="radio" name="discount" id="dc3" value="postcode" data-label="M16/M18/M19 offer"><label for="dc3">M16 · M18 · M19</label></div></div>
      <div class="field"><span class="label">Add to your hours</span><div class="seg">{ad}</div></div>
    </div>
    <div class="result is-visible" style="margin-top:0">
      <div class="eyebrow">Your package</div>
      <div class="result__big js-total">£350</div>
      <table class="summary js-summary"></table>
      <a class="btn btn--red btn--block js-wa" target="_blank" rel="noopener" href="https://wa.me/{WA}">{icon('wa')} Send this package on WhatsApp</a>
      <p class="note mt-1 mb-0">Discounted 10-hour blocks are £320. Extra hours outside a full block are £35/hr. One discount per block; proof of eligibility needed.</p>
    </div>
  </div>
</div>"""


def index():
    root = ""
    schema = [{
        "@context": "https://schema.org", "@type": "DrivingSchool", "name": "SQ Driving School", "url": SITE,
        "telephone": "+44 7352 932003", "priceRange": "£35–£350", "logo": SITE + "/favicon.svg",
        "description": "Fast, modern driving lessons across Greater Manchester. Manual & automatic. NHS & student discounts. Powered by DriveSQ.",
        "areaServed": [{"@type": "AdministrativeArea", "name": "Greater Manchester"}] + [{"@type": "AdministrativeArea", "name": n} for n in ["Manchester", "Salford", "Trafford", "Stockport", "Tameside", "Oldham", "Rochdale", "Bury", "Bolton", "Wigan"]]
            + [{"@type": "Place", "name": h["name"]} for h in __import__("pages_seo").neighbourhoods()]
            + [{"@type": "PostalAddress", "postalCode": c[0], "addressCountry": "GB"} for c in __import__("pages_postcodes").postcode_list(__import__("pages_seo").load_postcodes)],
        "parentOrganization": {"@type": "Organization", "name": "DriveSQ", "url": "https://www.drivesq.co.uk"},
        "makesOffer": [
            {"@type": "Offer", "name": "2-hour driving lesson", "price": "70", "priceCurrency": "GBP"},
            {"@type": "Offer", "name": "Single 1-hour session", "price": "40", "priceCurrency": "GBP"},
            {"@type": "Offer", "name": "10-hour block", "price": "350", "priceCurrency": "GBP"},
            {"@type": "Offer", "name": "10-hour block — NHS, student or M16/M18/M19", "price": "320", "priceCurrency": "GBP"}]
    }]
    tools = [("postcode-checker.html", "pin", "Postcode checker", "Instantly see if we cover you — and if you unlock the £320 offer."),
             ("prices.html#builder", "layers", "Package builder", "Build your own package and watch the price update live."),
             ("tools.html#lessons", "calc", "Lesson calculator", "Five questions. A personal estimate of the hours you'll need."),
             ("tools.html#readiness", "target", "Test readiness", "Tick off your skills and watch your readiness gauge climb."),
             ("theory-quiz.html", "quiz", "Theory quiz", "40 Highway Code questions. Ten per round. Can you score 10/10?"),
             ("hazard-game.html", "eye", "Spot the hazard", "A fun take on hazard perception. Click the dangers before time runs out."),
             ("tools.html#countdown", "calendar", "Test countdown", "Enter your test date and get a lesson plan to be ready in time."),
             ("test-centres.html", "flag", "Test centre guide", "Every Greater Manchester test centre and how to book your own test."),
             ("book.html", "calendar", "Book in 60 seconds", "A quick step-by-step booking with live postcode, discount and price checks."),
             ("gift-vouchers.html", "tag", "Gift voucher designer", "Design a driving lesson voucher and see it update live."),
             ("comfort.html#plan", "heart", "Comfort plan", "Tell us what worries you and get a personal plan for calm, confident lessons."),
             ("comfort.html#breathe", "moon", "Calm breathing coach", "A guided 2-minute breathing exercise for before your lesson or test."),
             ("road-signs.html", "tag", "Road sign flashcards", "Flip the cards, learn the signs and track how many you know."),
             ("dashboard-lights.html", "bolt", "Dashboard lights", "Tap a warning light to learn what it means and what to do.")]
    tool_cards = "".join(f'<a class="card" href="{h}" data-reveal="up" data-tilt="8"><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p>{d}</p><span class="red mono" style="font-size:.8rem">OPEN TOOL →</span></a>' for h, i, t, d in tools)
    why = [("clock", "2-hour lessons", "Two hours means time to warm up, learn something new and actually nail it — not just get going and stop."),
           ("phone-app", "Free DriveSQ Student Portal", "Track every skill, message your instructor, revise theory and sit mock tests — free for every SQ learner."),
           ("pound", "Prices you can see", "No hidden fees, no 'rates vary'. Every price is on this website, including every discount."),
           ("heart", "NHS & student discounts", "10 hours for £320 for NHS staff and students. Because you deserve it."),
           ("gear", "Manual & automatic", "Learn in whichever gearbox suits you. Automatic is growing fast with the move to electric."),
           ("flag", "Test help nobody else gives", "From booking your own test to choosing a centre — we guide you through it, step by step.")]
    why_cards = "".join(f'<article class="card" data-reveal="up" data-tilt="6"><span class="card__num">0{n+1}</span><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p>{d}</p></article>' for n, (i, t, d) in enumerate(why))
    steps = [("Get your provisional licence", "Apply on GOV.UK. You can start lessons as soon as it arrives."),
             ("Pass your theory test", "Revise in the DriveSQ Student Portal — theory library and 50-question mock tests included."),
             ("Learn with SQ", "2-hour lessons, every skill logged in your portal so you always know where you stand."),
             ("Mock test", "A full test-style drive with your instructor so test day feels familiar."),
             ("Book your practical test", "We'll show you how to book your own test and pick the right centre."),
             ("Pass. Drive. Celebrate.", "Then keep going with motorway lessons or Pass Plus if you want extra confidence.")]
    step_html = "".join(f'<div class="step" data-reveal="left"><div class="step__dot">{i+1}</div><div class="step__body"><h3>{t}</h3><p class="mb-0">{d}</p></div></div>' for i, (t, d) in enumerate(steps))
    faqs = [("I'm really nervous about driving. Can you help?", "Yes — lots of our learners start nervous. We go at your pace, start on quiet roads, explain everything first and never judge. Try our Comfort Zone for a personal comfort plan."),
            ("How much are driving lessons?", "A 2-hour lesson is £70 (£35/hr). A single 1-hour session is £40. A 10-hour block is £350, or £320 for NHS staff, students and learners in M16, M18 and M19."),
            ("Why are lessons 2 hours?", "Two hours gives you time to settle in, learn a new skill and practise it properly. Learners progress faster with longer lessons. If you only need one hour, it's £40."),
            ("Do you teach manual and automatic?", "Yes — both, across all of Greater Manchester."),
            ("What is the DriveSQ Student Portal?", "A free online app every SQ learner gets. It tracks your progress, has a theory library and mock tests, and lets you message your instructor."),
            ("Who owns SQ Driving School?", "SQ Driving School is a brand owned and managed by DriveSQ.")]
    faq_html = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    body = f"""
<section class="hero zone-dark">
  <div class="grid-bg" aria-hidden="true"></div>
  <div data-mascot style="--rope:150px" data-say="Hi! 👋 Nervous? <b>You're in the right place.</b> Tap me if you have a question."></div>
  <div class="speed-lines" aria-hidden="true"></div>
  <div class="container hero__grid">
    <div>
      <div class="eyebrow" data-reveal="up" data-i18n="hero.eyebrow">Greater Manchester · Manual &amp; Automatic</div>
      <h1><span class="line"><span>Learn.</span></span><span class="line"><span>Drive.</span></span><span class="line"><span class="glow-text scribble">Pass.<svg viewBox="0 0 200 24" preserveAspectRatio="none" aria-hidden="true"><path d="M4 16 C50 4 120 2 196 12"/></svg></span></span></h1>
      <p class="lead" data-reveal="up" data-delay=".35">Friendly, patient driving lessons across Greater Manchester. Go at your own pace — powered by DriveSQ, with a free Student Portal for every learner.</p>
      <p data-reveal="up" data-delay=".45" style="font-size:1.15rem;color:var(--white)">Lessons for <span class="red" data-type="nervous drivers|first-timers|NHS heroes|students|automatic learners|fast-trackers">nervous drivers</span></p>
      <div class="btn-row mt-2" data-reveal="up" data-delay=".55">
        <a class="btn btn--red" href="book.html">{icon('calendar')} Book in 60 seconds</a>
        <a class="btn btn--ghost" data-wa="Hi SQ Driving School! I'd like to book driving lessons." href="https://wa.me/{WA}">{icon('wa')} <span data-i18n="cta.book">WhatsApp us</span></a>
      </div>
      <div class="hero__badges" data-reveal="up" data-delay=".7">
        <span class="chip chip--red">{icon('pound')} 2-hr lesson £70</span>
        <span class="chip">{icon('heart')} NHS &amp; student £320 / 10 hrs</span>
        <span class="chip">{icon('phone-app')} Free Student Portal</span>
      </div>
    </div>
    <div class="hero__visual" data-reveal="zoom" data-delay=".2">
      <div class="hero__glow"></div><div class="hero__ring"></div><div class="hero__ring hero__ring--2"></div>
      <div style="position:relative;text-align:center">
        <div class="sq-logo sq-logo--xl" role="img" aria-label="SQ">SQ</div>
        <div class="hero__powered">Driving School · Powered by <b>DriveSQ</b></div>
      </div>
      <div data-hero-car></div>
    </div>
  </div>
</section>
{wave_down()}
{reassure()}
{marquee()}
<section class="section--tight">
  <div class="container">
    <div class="stats" data-reveal="up">
      <div class="stat"><div class="stat__num"><span class="red">£</span><span data-count="35">0</span></div><div class="stat__label">per hour, 2-hour lessons</div></div>
      <div class="stat"><div class="stat__num" data-count="10">0</div><div class="stat__label">Greater Manchester boroughs</div></div>
      <div class="stat"><div class="stat__num"><span class="red">£</span><span data-count="0">0</span></div><div class="stat__label">for the DriveSQ Student Portal</div></div>
      <div class="stat"><div class="stat__num" data-count="23">0</div><div class="stat__label">driving skills tracked in your portal</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="comfort" data-reveal="up">
      <div class="comfort__blob" aria-hidden="true"></div>
      <div class="split">
        <div>
          <div class="eyebrow">Feeling nervous?</div>
          <h2>Nervous? You're in the <span class="scribble">right place.<svg viewBox="0 0 200 24" preserveAspectRatio="none" aria-hidden="true"><path d="M4 16 C50 4 120 2 196 12"/></svg></span></h2>
          <p class="lead">Most of our learners feel nervous at the start. That's completely normal — and it's exactly what we're good at.</p>
          <ul class="soft-ticks">
            <li><span class="ico">{icon('clock')}</span><div><b>Your pace, always</b><span>We only move on when you say you're ready.</span></div></li>
            <li><span class="ico">{icon('road')}</span><div><b>Quiet roads first</b><span>Your first drives are on calm, empty streets.</span></div></li>
            <li><span class="ico">{icon('chat')}</span><div><b>Everything explained first</b><span>No surprises — you'll know what's coming before you do it.</span></div></li>
            <li><span class="ico">{icon('heart')}</span><div><b>No judgement, ever</b><span>Stalls and mistakes are part of learning. Breaks whenever you need.</span></div></li>
          </ul>
          <div class="btn-row"><a class="btn btn--red" href="comfort.html">{icon('heart')} Get your comfort plan</a><a class="btn btn--ghost" data-wa="Hi SQ! I'm a bit nervous about learning to drive. Can we take it slowly?" href="https://wa.me/{WA}">{icon('wa')} Tell us you're nervous</a></div>
        </div>
        <div>
          <div class="bubble-quote" data-reveal="right">"I'd like to learn, but I'm really nervous…"</div>
          <div class="bubble-quote mt-3" data-reveal="right" data-delay=".3" style="margin-left:12%;background:#e3141c;color:#fff;border-color:#e3141c">That's okay. We'll start somewhere quiet, go through everything together, and you'll set the pace. 💙</div>
          <p class="note mt-3">Try our <a class="red" href="comfort.html#breathe">calm-breathing coach</a> before your lesson.</p>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section__head center"><div class="eyebrow">No surprises</div><h2 data-split>What happens in your first lesson.</h2><p class="lead">Two relaxed hours. Here's exactly how they go.</p></div>
    <div class="lesson-steps" data-stagger=".08">
      <div class="lesson-step" data-reveal="up"><span class="lesson-step__time">Before</span><span class="lesson-step__emoji">💬</span><h3>We say hello</h3><p class="mb-0">We confirm your time and pick-up on WhatsApp, and answer any questions.</p></div>
      <div class="lesson-step" data-reveal="up"><span class="lesson-step__time">0:00</span><span class="lesson-step__emoji">🪪</span><h3>Quick checks</h3><p class="mb-0">We check your provisional licence and that you can read a number plate from 20 metres.</p></div>
      <div class="lesson-step" data-reveal="up"><span class="lesson-step__time">0:10</span><span class="lesson-step__emoji">🛣️</span><h3>Somewhere quiet</h3><p class="mb-0">Your instructor drives you to a calm, empty road. No pressure.</p></div>
      <div class="lesson-step" data-reveal="up"><span class="lesson-step__time">0:25</span><span class="lesson-step__emoji">🎛️</span><h3>Meet the car</h3><p class="mb-0">Seat, mirrors and controls, explained slowly. Ask as many questions as you like.</p></div>
      <div class="lesson-step" data-reveal="up"><span class="lesson-step__time">0:50</span><span class="lesson-step__emoji">🚗</span><h3>Your first drive</h3><p class="mb-0">Moving off and stopping on quiet roads. Most people surprise themselves!</p></div>
      <div class="lesson-step" data-reveal="up"><span class="lesson-step__time">1:45</span><span class="lesson-step__emoji">🎉</span><h3>How did it go?</h3><p class="mb-0">A friendly chat about what went well, and your Student Portal gets set up.</p></div>
    </div>
    <div class="center mt-3"><a class="btn btn--ghost" href="first-lesson.html">Full first-lesson guide {icon('arrow')}</a></div>
  </div>
</section>
<section class="section--tight">
  <div class="container">
    <div class="offer zone-dark" data-reveal="zoom">
      <div class="split">
        <div>
          <div class="eyebrow">Special offer · Local learners</div>
          <h2>10 hours for</h2>
          <div class="offer__price">£320</div>
          <div class="offer__codes"><span class="offer__code">M16</span><span class="offer__code">M18</span><span class="offer__code">M19</span></div>
          <p>Live in Old Trafford, Whalley Range, Firswood, Gorton, Abbey Hey, Levenshulme or Burnage? Save £30 on a 10-hour block.</p>
          <a class="btn btn--ghost" href="offer-m16-m18-m19.html" style="color:#fff">See offer details {icon('arrow')}</a>
        </div>
        <div class="tool" style="background:rgba(0,0,0,.35)">{postcode_form(True, "Check if your postcode qualifies")}</div>
      </div>
    </div>
  </div>
</section>
<section class="section" id="book">
  <div class="container" style="max-width:960px">
    <div class="section__head center"><div class="eyebrow">Book in 60 seconds</div><h2 data-split>Ready? Let's get you booked.</h2><p class="lead">A few taps. We'll check your postcode, your discount and your price as you go.</p></div>
    {wizard_html()}
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section__head center"><div class="eyebrow">Why SQ</div><h2 data-split>Not your average driving school.</h2><p class="lead">We looked at every driving school in Greater Manchester, then built the one we'd want to learn with.</p></div>
    <div class="grid grid--3" data-stagger=".08">{why_cards}</div>
  </div>
</section>
<div class="road-strip" aria-hidden="true">{CAR_SIDE}</div>
<section class="section section--alt" id="prices">
  <div class="container">
    <div class="section__head center"><div class="eyebrow">Simple pricing</div><h2 data-split>Every price. Right here.</h2><p class="lead">No "rates vary". No small print. Manual and automatic.</p></div>
    {price_cards(root)}
    <div class="center mt-3"><a class="btn btn--ghost" href="prices.html">Full price list &amp; package builder {icon('arrow')}</a></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section__head center"><div class="eyebrow">Discounts</div><h2 data-split>Save £30 on every 10-hour block.</h2></div>
    <div class="grid grid--3" data-stagger=".1">
      <article class="card discount" data-reveal="flip"><div class="card__icon">{icon('heart')}</div><span class="discount__who">NHS staff</span><span class="discount__badge">£320</span><p>10 hours instead of £350. Thank you for everything you do.</p><span class="discount__proof">Show your NHS ID badge or NHS email.</span></article>
      <article class="card discount" data-reveal="flip"><div class="card__icon">{icon('grad')}</div><span class="discount__who">Students</span><span class="discount__badge">£320</span><p>College and university students across Greater Manchester.</p><span class="discount__proof">Show a valid student ID card.</span></article>
      <article class="card discount" data-reveal="flip"><div class="card__icon">{icon('pin')}</div><span class="discount__who">M16 · M18 · M19</span><span class="discount__badge">£320</span><p>Special local offer for learners picked up in these postcodes.</p><span class="discount__proof">Pick-up address must be in M16, M18 or M19.</span></article>
    </div>
    <div class="center mt-3"><a class="btn btn--ghost" href="discounts.html">All discounts {icon('arrow')}</a></div>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section__head"><div class="eyebrow">Free tools</div><h2 data-split>Tools no other driving school has.</h2><p class="lead">Work out your hours, build your package, test your theory and spot hazards — all free, no sign-up.</p></div>
    <div class="grid grid--4" data-stagger=".06">{tool_cards}</div>
  </div>
</section>
<section class="section section--alt">
  <div class="container">
    <div class="section__head"><div class="eyebrow">Greater Manchester Knowledge Hub</div><h2 data-split>Know the local rules before your test.</h2><p class="lead">Fact-checked guides you won't find elsewhere — written for Greater Manchester learners.</p></div>
    <div class="grid grid--3" data-stagger=".06">
      <a class="card" href="knowledge/driving-test-booking-rules-2026.html" data-reveal="up"><div class="card__icon">{icon('calendar')}</div><span class="k-cat">Tests &amp; booking</span><h3 class="mt-1">The 2026 test booking rules</h3><p class="mb-0">Two changes per booking, learner-only booking and the three-centre rule.</p></a>
      <a class="card" href="knowledge/bus-lanes-and-bus-gates-manchester.html" data-reveal="up"><div class="card__icon">{icon('flag')}</div><span class="k-cat">Manchester roads</span><h3 class="mt-1">Bus lanes &amp; the Oxford Road bus gate</h3><p class="mb-0">Read the signs, avoid a £70 fine and a test fault.</p></a>
      <a class="card" href="knowledge/greater-manchester-driving-test-centres.html" data-reveal="up"><div class="card__icon">{icon('pin')}</div><span class="k-cat">Test centres</span><h3 class="mt-1">Every Greater Manchester test centre</h3><p class="mb-0">Which centre serves your area and how to choose.</p></a>
    </div>
    <div class="center mt-3"><a class="btn btn--ghost" href="knowledge.html">Explore the knowledge hub {icon('arrow')}</a></div>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div data-reveal="left">
      <div class="eyebrow">DriveSQ Student Portal</div>
      <h2 data-split>Your whole driving journey, in your pocket.</h2>
      <p class="lead">Every SQ Driving School learner gets the DriveSQ Student Portal free. It's the same platform DriveSQ learners use every day.</p>
      <ul class="ticks">
        <li><span><b>Live progress</b> — 23 skills rated after every lesson.</span></li>
        <li><span><b>Mock theory tests</b> — 50 questions, timed, just like the real thing.</span></li>
        <li><span><b>Message your instructor</b> — confirm or reschedule lessons in one tap.</span></li>
        <li><span><b>Test readiness</b> — a checklist that updates itself as you improve.</span></li>
      </ul>
      <div class="btn-row"><a class="btn btn--red" href="student-portal.html">How the portal works {icon('arrow')}</a><a class="btn btn--ghost" href="{STUDENT}" target="_blank" rel="noopener">Student login ↗</a></div>
    </div>
    <div data-reveal="right">{phone_mock()}</div>
  </div>
</section>
<section class="section section--alt">
  <div class="container split">
    <div data-reveal="left">
      <div class="eyebrow">Your journey</div>
      <h2 data-split>From provisional to passed.</h2>
      <p class="lead">Six stages. We're with you for every one.</p>
      <div class="traffic mt-2" aria-hidden="true"><i></i><i></i><i></i></div>
    </div>
    <div class="timeline"><div class="timeline__fill"></div>{step_html}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section__head center"><div class="eyebrow">Reviews</div><h2 data-split>Real learners. Real reviews.</h2><p class="lead">We only publish genuine reviews from real SQ learners — never made-up ones. As our learners pass, their stories will appear here.</p></div>
    <div class="center" data-reveal="up"><a class="btn btn--ghost" href="review-policy.html">Read our review policy</a> <a class="btn btn--red" data-wa="Hi SQ! I passed and I'd like to leave a review." href="https://wa.me/{WA}">Passed with SQ? Share your story</a></div>
  </div>
</section>
<section class="section section--alt">
  <div class="container" style="max-width:900px">
    <div class="section__head center"><div class="eyebrow">FAQ</div><h2 data-split>Quick answers.</h2></div>
    <div class="faq" data-stagger=".06">{faq_html}</div>
    <div class="center mt-3"><a class="btn btn--ghost" href="faq.html">All questions {icon('arrow')}</a></div>
  </div>
</section>
{cta(root)}
"""
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    return page("index.html", "SQ Driving School | Driving Lessons Greater Manchester | Powered by DriveSQ",
                "Driving lessons across Greater Manchester from £35/hr. 2-hour lessons £70, 10 hours £350 — or £320 for NHS, students and M16/M18/M19. Free DriveSQ Student Portal.",
                body, root, schema=schema + [faq_schema])


def lessons():
    root = ""
    types = [("car", "Manual lessons", "Master clutch control, gears and hill starts with a patient instructor."),
             ("auto", "Automatic lessons", "Simpler to learn and the future of driving. Same great teaching."),
             ("star", "Complete beginners", "Never sat behind a wheel? Perfect. We start in quiet roads and build up."),
             ("heart", "Nervous drivers", "Calm, judgement-free lessons at your pace. Your portal shows your progress so you can see how far you've come."),
             ("bolt", "Intensive courses", "Need your licence fast? Concentrated lessons over 1–4 weeks."),
             ("road", "Motorway lessons", "Learners can drive on motorways with an approved instructor in a dual-controlled car."),
             ("moon", "Night & all-weather", "Manchester rain and dark evenings — learn to handle both safely."),
             ("target", "Mock tests", "A full test-style drive marked like the real thing, so test day holds no surprises."),
             ("flag", "Test route practice", "Practise around the test centre you're booked at."),
             ("users", "Refresher lessons", "Passed years ago but lost confidence? We'll get you back on the road."),
             ("globe", "Foreign licence holders", "Converting to a UK licence? We'll get you test-ready for UK roads."),
             ("shield", "Pass Plus", "Extra training after you pass. Ask us about the course.")]
    cards = "".join(f'<article class="card" data-reveal="up" data-tilt="6"><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p>{d}</p></article>' for i, t, d in types)
    flow = [("0:00", "Warm-up & recap", "Quick check-in. Your instructor reviews your portal notes from last time."),
            ("0:15", "Today's skill", "A new topic, explained and demonstrated."),
            ("0:45", "Practise", "Repetition until it clicks — the part 1-hour lessons never have time for."),
            ("1:30", "Put it together", "Real roads, real traffic, combining today's skill with everything you know."),
            ("1:50", "Debrief & portal update", "Your skills get rated in the DriveSQ Student Portal so you can see your progress.")]
    flow_html = "".join(f'<div class="step" data-reveal="left"><div class="step__dot" style="font-size:.8rem">{t}</div><div class="step__body"><h3>{h}</h3><p class="mb-0">{d}</p></div></div>' for t, h, d in flow)
    body = page_hero("Lessons", "Every kind of lesson. One standard.", "Manual and automatic driving lessons across Greater Manchester — for beginners, nervous drivers, fast-trackers and everyone in between.", ["Lessons"], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" data-wa="Hi! I would like to book lessons." href="https://wa.me/{WA}">{icon("wa")} Book on WhatsApp</a><a class="btn btn--ghost" href="prices.html">See prices</a></div>')
    body += f"""<section class="section"><div class="container"><div class="grid grid--3" data-stagger=".05">{cards}</div></div></section>
<section class="section section--alt"><div class="container split">
  <div data-reveal="left"><div class="eyebrow">Why 2 hours?</div><h2 data-split>Inside a 2-hour SQ lesson.</h2>
  <p class="lead">One hour goes fast — by the time you've warmed up, it's nearly over. Two hours gives you time to actually learn. That's why 2 hours is our standard lesson (£70), with single 1-hour sessions available for £40.</p>
  <div class="gauge mt-3" data-gauge="100"><svg viewBox="0 0 320 320" aria-hidden="true"><path d="M50 250 A140 140 0 1 1 270 250" fill="none" stroke="var(--line-2)" stroke-width="14" stroke-linecap="round"/><path class="gauge__arc" d="M50 250 A140 140 0 1 1 270 250" fill="none" stroke="#ff1f1f" stroke-width="14" stroke-linecap="round" style="filter:drop-shadow(0 0 8px #ff1f1f)"/><line class="gauge__needle" x1="160" y1="160" x2="160" y2="50" stroke="#fff" stroke-width="4" stroke-linecap="round" transform="rotate(-120 160 160)"/><circle cx="160" cy="160" r="12" fill="#ff1f1f"/></svg><div class="gauge__val"><b><span class="gauge__num">0</span>%</b><span>more practice time</span></div></div>
  </div>
  <div class="timeline"><div class="timeline__fill"></div>{flow_html}</div>
</div></section>
{cta(root)}"""
    return page("lessons.html", "Driving Lessons Greater Manchester | Manual & Automatic | SQ Driving School",
                "Manual and automatic driving lessons across Greater Manchester. Beginners, nervous drivers, intensive courses, motorway lessons and mock tests. 2-hour lessons £70.", body, root)


def prices():
    root = ""
    rows = [("Single 1-hour session", "£40", "One-off hour"), ("2-hour lesson", "£70", "£35/hr · our standard lesson"),
            ("Extra hours", "£35/hr", "Booked in 2-hour lessons"), ("10-hour block", "£350", "£35/hr"),
            ("10-hour block — NHS", "£320", "£32/hr · save £30"), ("10-hour block — Students", "£320", "£32/hr · save £30"),
            ("10-hour block — M16, M18, M19", "£320", "£32/hr · save £30"), ("Intensive courses", "From £35/hr", "Discounted blocks apply")]
    tr = "".join(f"<tr><td>{a}</td><td class='mono red'>{b}</td><td>{c}</td></tr>" for a, b, c in rows)
    body = page_hero("Prices", "Clear prices. Zero surprises.", "£35 an hour. 2-hour lessons. Discounted blocks for NHS staff, students and M16, M18 &amp; M19 learners. Manual and automatic.", ["Prices"], root)
    body += f"""<section class="section--tight"><div class="container">{price_cards(root)}</div></section>
<section class="section" id="builder"><div class="container"><div class="section__head center"><div class="eyebrow">Package builder</div><h2 data-split>Build your perfect package.</h2></div>{builder(root)}</div></section>
<section class="section section--alt"><div class="container">
  <div class="section__head"><div class="eyebrow">Full price list</div><h2 data-split>Everything, in one table.</h2></div>
  <div class="table-wrap" data-reveal="up"><table class="table"><thead><tr><th>Option</th><th>Price</th><th>Details</th></tr></thead><tbody>{tr}</tbody></table></div>
  <p class="note mt-2">Prices apply to manual and automatic lessons. One discount per block booking. Discounts need proof of eligibility. DVSA test fees are paid separately to the DVSA.</p>
</div></section>
<section class="section"><div class="container"><div class="tool" data-tool="budget" data-reveal="up">
  <div class="tool__head"><div class="card__icon">{icon('calc')}</div><div><h3>Total cost calculator</h3><p class="mb-0 note">Lessons plus DVSA test fees — your full budget to get your licence.</p></div></div>
  <div class="grid grid--2">
    <div>
      <div class="field"><label for="bh">Hours of lessons</label><input class="input" type="number" id="bh" name="bhours" min="2" max="80" step="2" value="40"></div>
      <ul class="checklist">
        <li><label><input type="checkbox" name="bdisc"> I qualify for NHS / student / M16·M18·M19 discount</label></li>
        <li><label><input type="checkbox" name="bslot"> Evening or weekend practical test</label></li>
        <li><label><input type="checkbox" name="btheory"> I've already passed my theory test</label></li>
      </ul>
    </div>
    <div><table class="summary js-budget"></table><p class="note">DVSA fees shown are standard rates; always check <a class="red" href="https://www.gov.uk/driving-test-cost" target="_blank" rel="noopener">GOV.UK</a> for the latest.</p></div>
  </div>
</div></div></section>
{cta(root)}"""
    return page("prices.html", "Driving Lesson Prices Manchester | £35/hr | SQ Driving School",
                "SQ Driving School prices: 2-hour lesson £70, single hour £40, 10 hours £350 or £320 for NHS, students and M16/M18/M19. Build your package online.", body, root)


def discounts():
    root = ""
    more = [("shield", "Key workers"), ("flag", "Armed forces & veterans"), ("users", "Refer a friend"), ("heart", "Carers"),
            ("book", "Teachers & school staff"), ("target", "Second-time test takers"), ("users", "Family & siblings"), ("bolt", "Emergency services")]
    more_html = "".join(f'<article class="card" data-reveal="zoom"><div class="card__icon">{icon(i)}</div><h3>{t}</h3><p class="mb-0"><span class="tag">Coming soon</span></p></article>' for i, t in more)
    body = page_hero("Discounts", "More ways to save.", "Our 10-hour block is £350. If you're NHS staff, a student or live in M16, M18 or M19, it's just £320.", ["Discounts"], root)
    body += f"""<section class="section--tight"><div class="container"><div class="grid grid--3" data-stagger=".1">
  <article class="card discount neon-border" data-reveal="flip"><div class="card__icon">{icon('heart')}</div><span class="discount__who">NHS discount</span><span class="discount__badge">£320</span><p><s>£350</s> · 10 hours · save £30</p><p>For doctors, nurses, healthcare assistants, porters, admin — anyone who works for the NHS.</p><span class="discount__proof">Proof: NHS ID badge, NHS email address or recent payslip.</span><a class="btn btn--red mt-2" data-wa="Hi! I work for the NHS and I'd like the NHS discount (10 hours for £320)." href="https://wa.me/{WA}">Claim NHS discount</a></article>
  <article class="card discount neon-border" data-reveal="flip"><div class="card__icon">{icon('grad')}</div><span class="discount__who">Student discount</span><span class="discount__badge">£320</span><p><s>£350</s> · 10 hours · save £30</p><p>Sixth form, college and university students — Manchester, Salford, MMU and beyond.</p><span class="discount__proof">Proof: valid student ID card or enrolment letter.</span><a class="btn btn--red mt-2" data-wa="Hi! I'm a student and I'd like the student discount (10 hours for £320)." href="https://wa.me/{WA}">Claim student discount</a></article>
  <article class="card discount neon-border" data-reveal="flip"><div class="card__icon">{icon('pin')}</div><span class="discount__who">M16 · M18 · M19 offer</span><span class="discount__badge">£320</span><p><s>£350</s> · 10 hours · save £30</p><p>Old Trafford, Whalley Range, Firswood, Gorton, Abbey Hey, Levenshulme and Burnage.</p><span class="discount__proof">Pick-up address must be in M16, M18 or M19.</span><a class="btn btn--red mt-2" href="offer-m16-m18-m19.html">See the offer</a></article>
</div></div></section>
<section class="section"><div class="container"><div class="section__head center"><div class="eyebrow">More discounts</div><h2 data-split>More discounts on the way.</h2><p class="lead">We're adding more ways to save. Message us to ask about them.</p></div><div class="grid grid--4" data-stagger=".05">{more_html}</div></div></section>
<section class="section section--alt"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">How to claim</div><h2 data-split>Three steps.</h2></div>
<div class="timeline"><div class="timeline__fill"></div>
<div class="step" data-reveal="left"><div class="step__dot">1</div><div class="step__body"><h3>Message us on WhatsApp</h3><p class="mb-0">Tell us which discount you qualify for.</p></div></div>
<div class="step" data-reveal="left"><div class="step__dot">2</div><div class="step__body"><h3>Show your proof</h3><p class="mb-0">A quick photo of your ID, or show it at your first lesson.</p></div></div>
<div class="step" data-reveal="left"><div class="step__dot">3</div><div class="step__body"><h3>Start driving for less</h3><p class="mb-0">Your discounted block is booked, and your DriveSQ Student Portal is set up.</p></div></div>
</div>
<p class="note mt-3">Terms: one discount per 10-hour block. Discounts can't be combined. Proof of eligibility is required. Discounted blocks are paid in advance. Offers may change; the price you're quoted when you book is the price you pay.</p>
</div></section>
{cta(root)}"""
    return page("discounts.html", "NHS & Student Driving Lesson Discounts Manchester | SQ Driving School",
                "10 hours of driving lessons for £320 for NHS staff, students and learners in M16, M18 and M19. Save £30 with SQ Driving School, Greater Manchester.", body, root)


def offer():
    root = ""
    zones = [("M16", "Old Trafford · Whalley Range · Firswood"), ("M18", "Gorton · Abbey Hey"), ("M19", "Levenshulme · Burnage")]
    z = "".join(f'<article class="card" data-reveal="flip" data-tilt="8"><div class="offer__code" style="display:inline-block">{c}</div><h3 class="mt-2">{c}</h3><p class="mb-0">{a}</p></article>' for c, a in zones)
    body = page_hero("Special offer", "10 hours. £320. M16, M18 &amp; M19.", "A special local offer for learners picked up in Old Trafford, Whalley Range, Firswood, Gorton, Abbey Hey, Levenshulme and Burnage. Save £30 on a 10-hour block.", ["Special offer"], root)
    body += f"""<section class="section--tight"><div class="container"><div class="grid grid--3" data-stagger=".12">{z}</div></div></section>
<section class="section"><div class="container" style="max-width:820px"><div class="tool neon-border" data-reveal="zoom"><div class="tool__head"><div class="card__icon">{icon('pin')}</div><h3>Do you qualify?</h3></div>{postcode_form(True, "Your pick-up postcode")}</div></div></section>
<section class="section section--alt"><div class="container split">
  <div data-reveal="left"><div class="offer__price">£320</div><p class="lead">instead of £350 for 10 hours of manual or automatic lessons.</p></div>
  <ul class="ticks" data-reveal="right"><li><span><b>Five 2-hour lessons</b> — or split however suits you</span></li><li><span><b>Free DriveSQ Student Portal</b> from day one</span></li><li><span><b>Manual or automatic</b> — same price</span></li><li><span><b>Pick-up</b> from your home, college or work in M16, M18 or M19</span></li></ul>
</div><div class="container"><p class="note mt-3">Pick-up address must be in M16, M18 or M19. Can't be combined with other discounts. Paid in advance.</p></div></section>
{cta(root, "Claim your £320 block.", "Message us your postcode on WhatsApp and we'll book you in.")}"""
    return page("offer-m16-m18-m19.html", "10 Hours £320 Driving Lessons M16, M18, M19 | Levenshulme, Gorton, Old Trafford",
                "Special offer: 10 hours of driving lessons for £320 in M16 (Old Trafford, Whalley Range), M18 (Gorton) and M19 (Levenshulme, Burnage).", body, root)


def intensive():
    root = ""
    hrs = "".join(f'<input type="radio" name="ihours" id="ih{h}" value="{h}" {"checked" if h == 20 else ""}><label for="ih{h}">{h} hrs</label>' for h in (10, 20, 30, 40))
    wks = "".join(f'<input type="radio" name="iweeks" id="iw{w}" value="{w}" {"checked" if w == 2 else ""}><label for="iw{w}">{w} week{"s" if w > 1 else ""}</label>' for w in (1, 2, 3, 4))
    who = [("10 hrs", "Test-ready refresh", "Failed before or nearly ready? Polish the faults and get test-sharp."),
           ("20 hrs", "Some experience", "You've had lessons before. Pull it together quickly."),
           ("30 hrs", "A little experience", "You know the basics but need a solid programme."),
           ("40 hrs", "Complete beginner", "From zero to test-ready in a concentrated burst.")]
    w = "".join(f'<article class="card" data-reveal="up"><div class="discount__badge">{a}</div><h3 class="mt-1">{b}</h3><p class="mb-0">{c}</p></article>' for a, b, c in who)
    body = page_hero("Intensive courses", "Licence in weeks, not months.", "Concentrated lessons over 1 to 4 weeks for learners who need to pass fast. Manual or automatic, anywhere in Greater Manchester.", ["Intensive"], root)
    body += f"""<section class="section--tight"><div class="container"><div class="grid grid--4" data-stagger=".08">{w}</div></div></section>
<section class="section"><div class="container"><div class="tool neon-border" data-tool="intensive" data-reveal="up">
  <div class="tool__head"><div class="card__icon">{icon('bolt')}</div><div><h3>Intensive course planner</h3><p class="mb-0 note">Choose hours and weeks to see your schedule and cost.</p></div></div>
  <div class="grid grid--2"><div>
    <div class="field"><span class="label">Course hours</span><div class="seg">{hrs}</div></div>
    <div class="field"><span class="label">Over how long?</span><div class="seg">{wks}</div></div>
    <div class="field"><span class="label">NHS / student / M16·M18·M19?</span><div class="seg"><input type="radio" name="idisc" id="id0" value="no" checked><label for="id0">No</label><input type="radio" name="idisc" id="id1" value="yes"><label for="id1">Yes</label></div></div>
  </div><div class="result is-visible js-plan" style="margin-top:0"></div></div>
  <p class="note">The lesson cost uses our standard prices (£35/hr; discounted blocks £320). Your practical test is booked separately with the DVSA — ask us how to plan your course around your test date.</p>
</div></div></section>
<section class="section section--alt"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">Good to know</div><h2 data-split>Before you go intensive.</h2></div>
<div class="faq">
<details data-reveal="up"><summary>Do I need my theory test first?</summary><div>Yes — you must pass your theory test before you can book your practical test. Use the DriveSQ Student Portal mock tests to prepare.</div></details>
<details data-reveal="up"><summary>Will the test be booked for me?</summary><div>You book your practical test with the DVSA on GOV.UK. We'll help you plan your course so you're ready for your test date. See our <a class="red" href="test-centres.html">test centre guide</a>.</div></details>
<details data-reveal="up"><summary>How many hours a day?</summary><div>Usually 2–4 hours a day, with breaks. Our planner above shows the average for your choices.</div></details>
</div></div></section>
{cta(root, "Need your licence fast?")}"""
    return page("intensive.html", "Intensive Driving Courses Manchester | Fast Track | SQ Driving School",
                "Intensive and fast-track driving courses across Greater Manchester. 10–40 hours over 1–4 weeks, manual or automatic. Plan your course online.", body, root)
