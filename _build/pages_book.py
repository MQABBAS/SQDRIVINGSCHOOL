from layout import *


def _choices(name, opts, kind="radio"):
    out = ""
    for i, (val, em, title, sub) in enumerate(opts):
        out += f'<div class="choice"><input type="{kind}" name="{name}" id="{name}{i}" value="{val}"><label for="{name}{i}"><span class="em">{em}</span><b>{title}</b><small>{sub}</small></label></div>'
    return f'<div class="choice-grid">{out}</div>'


def wizard_html():
    steps = [
        ("Manual or automatic?", "Same price either way.", _choices("wtrans", [("Manual", "⚙️", "Manual", "Drive any car once you pass"), ("Automatic", "🅰️", "Automatic", "No clutch, easier to learn"), ("Not sure", "🤔", "Not sure yet", "We'll help you decide")])),
        ("Where should we pick you up?", "Enter your postcode — we'll check it instantly.", '<div class="field mt-2"><label for="wpc">Postcode</label><input class="input input--big" id="wpc" name="wpostcode" type="text" autocomplete="postal-code" placeholder="e.g. M19 2AB"></div><p class="js-wpc" aria-live="polite" style="min-height:1.6em"></p>'),
        ("How much have you driven?", "No wrong answers.", _choices("wexp", [("Never driven", "🌱", "Never", "Complete beginner"), ("A few lessons", "🚗", "A few lessons", "Some experience"), ("Lots of lessons", "🛣️", "Lots", "Nearly test ready"), ("Failed a test before", "🔁", "Failed a test", "Let's fix those faults")])),
        ("What would you like?", "You can always change later.", _choices("wpkg", [("2-hour lessons", "⏱️", "2-hour lessons", f"£70 each"), ("10-hour block", "📦", "10-hour block", "£350 · £320 discounted"), ("Intensive course", "⚡", "Intensive", "Pass in weeks"), ("Single 1-hour session", "1️⃣", "Single hour", "£40"), ("Not sure yet", "💬", "Not sure", "Let's chat")])),
        ("Do you qualify for a discount?", "M16, M18 &amp; M19 postcodes get the offer automatically.", _choices("wdisc", [("NHS", "🏥", "NHS staff", "10 hrs £320"), ("Student", "🎓", "Student", "10 hrs £320"), ("None", "➖", "No discount", "That's fine!")])),
        ("When would you like to start?", "Pick up to 3 days that suit you — we'll confirm the exact time with you.", '<div class="wdates js-wdates" role="group" aria-label="Preferred start days"></div>' +
         _choices("wtime", [("Mornings", "🌅", "Mornings", "8am – 12pm"), ("Afternoons", "☀️", "Afternoons", "12pm – 5pm"), ("Evenings", "🌙", "Evenings", "5pm – 8pm")], "checkbox") +
         '<div class="choice mt-2"><input type="checkbox" name="wnervous" id="wnervous" value="yes"><label for="wnervous"><span class="em">💙</span><b>I\'m a bit nervous</b><small>We\'ll take it slow and start somewhere quiet</small></label></div>'),
        ("Nearly there — your details", "So your instructor can contact you and plan your first lesson.", '<div class="grid grid--2 mt-2" style="gap:12px"><div class="field mb-0"><label for="wname">Full name *</label><input class="input" id="wname" name="wname" type="text" autocomplete="name" placeholder="First and last name"></div><div class="field mb-0"><label for="wphone">Mobile number *</label><input class="input" id="wphone" name="wphone" type="tel" inputmode="tel" autocomplete="tel" placeholder="07…"></div><div class="field mb-0"><label for="wemail">Email <span class="note">(optional)</span></label><input class="input" id="wemail" name="wemail" type="email" inputmode="email" autocomplete="email" placeholder="you@example.com"></div><div class="field mb-0"><label for="wstreet">Pick-up street <span class="note">(optional)</span></label><input class="input" id="wstreet" name="wstreet" type="text" autocomplete="street-address" placeholder="e.g. 12 Stockport Road"></div></div><div class="field mt-2 mb-0"><label for="wmsg">Anything we should know? <span class="note">(optional)</span></label><div class="wnotechips" role="group" aria-label="Quick add to your note"><button type="button" data-note="I already have a test date: ">📅 I have a test date</button><button type="button" data-note="Please pick me up from college / work: ">🏫 Pick-up from college / work</button><button type="button" data-note="I&#39;d prefer a female instructor if possible.">👩 Female instructor preferred</button><button type="button" data-note="Best time to call me: ">📞 Best time to call</button><button type="button" data-note="I&#39;m switching from another instructor.">🔄 Switching instructor</button></div><textarea class="input wnotes" id="wmsg" name="wmsg" rows="3" maxlength="500" placeholder="e.g. My test is on 12 March · I can only do weekends · I have dyslexia, please explain things slowly"></textarea><div class="wnotecount" aria-live="polite"><span class="js-wnotecount">0</span>/500</div></div><p class="js-werr form-status is-err" aria-live="polite"></p><div class="choice wdraw js-wdraw mt-2"><input type="checkbox" name="wdraw" id="wdraw" value="yes"><label for="wdraw"><span class="em">🎟️</span><b>Yes, enter me into this month\'s free draw to win a £35 lesson voucher</b><small>Free to enter, no purchase needed. One entry per mobile number each month. <a href="/free-prize-draw.html" target="_blank" rel="noopener">Draw terms</a></small></label></div><p class="note mb-0">By sending, you agree SQ Driving School (part of DriveSQ) can contact you about lessons. We never share your details. <a href="privacy.html">Privacy</a></p>'),
        ("Booking received! 🎉", "SQ Driving School has your request and will be in touch shortly.", f'<p class="js-wstatus form-status" aria-live="polite"></p><div class="wizard__summary"></div><button class="btn btn--red btn--block js-wsubmit hide" type="button">{icon("send") if "send" in ICONS else "📩"} Try sending again</button><a class="btn btn--wa btn--block mt-1 js-wsend" target="_blank" rel="noopener" href="https://wa.me/{WA}">{icon("wa")} Also send on WhatsApp — fastest reply</a>'),
    ]
    st = "".join(f'<div class="wizard__step"><div class="wizard__q">{q}</div><p class="mb-0">{sub}</p>{body}</div>' for q, sub, body in steps)
    return f"""<div class="tool neon-border wizard" data-tool="wizard" data-reveal="up">
  <div class="quiz__meta"><span class="js-stepnum">Step 1</span><span>⏱ about 60 seconds</span></div>
  <div class="wizard__bar"><span></span></div>
  {st}
  <div class="wizard__nav"><button class="btn btn--ghost js-back" type="button">← Back</button><button class="btn btn--red js-next" type="button">Next →</button></div>
</div>"""


def draw_banner(root=""):
    return f'''<div class="drawbar" data-reveal="up"><span class="drawbar__em" aria-hidden="true">🎟️</span><div class="drawbar__txt"><b>Win a £35 lesson voucher this month.</b> Tick the box when you book in 60 seconds and you\'re in the draw. Free to enter.</div><a class="drawbar__link" href="{root}free-prize-draw.html">How it works {icon('arrow')}</a></div>'''


def draw_page():
    root = ""
    steps = [("1", "Book in 60 seconds", "Fill in the quick booking form — it takes about a minute."),
             ("2", "Tick the draw box", "On the last step, tick “Enter me into this month's free draw”."),
             ("3", "Get your ticket", "You'll see your ticket number straight away. One winner every month.")]
    st = "".join(f'<div class="step" data-reveal="left"><div class="step__dot">{n}</div><div class="step__body"><h3>{a}</h3><p class="mb-0">{b}</p></div></div>' for n, a, b in steps)
    faqs = [("Is it really free?", "Yes. Entering costs nothing and you don't have to buy lessons. Sending a booking request with the box ticked is enough."),
            ("Do I have to tick the box?", "Only if you want to enter. If you leave it unticked we'll still help you book — you just won't be in the draw."),
            ("When is the draw?", "Entries close at 6pm (UK time) on the last day of each month. The winner is usually chosen the same evening or within a few days."),
            ("What can I spend the voucher on?", "£35 off driving lessons with SQ Driving School (part of DriveSQ). It's valid for 6 months."),
            ("Can I enter more than once?", "One entry per mobile number each month. You can enter again next month."),
            ("Will my name be shown?", "Only if you say yes. If you agree, we show your first name and postcode area — for example “Aisha from M19”.")]
    fq = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    body = page_hero("Free prize draw", "Win a £35 lesson voucher.", "Every month one learner wins £35 off their driving lessons. Entering is free — just tick the box when you book in 60 seconds.", ["Free prize draw"], root)
    body += f"""<section class="section--tight"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">How to enter</div><h2 data-split>Three steps. One minute.</h2></div>
<div class="timeline"><div class="timeline__fill"></div>{st}</div>
<div class="btn-row mt-3"><a class="btn btn--red" href="book.html">{icon('send') if 'send' in ICONS else ''} Book in 60 seconds &amp; enter</a><a class="btn btn--ghost" href="discounts.html">See all offers</a></div></div></section>
<section class="section section--alt"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">Questions</div><h2 data-split>Good to know.</h2></div><div class="faq">{fq}</div></div></section>
<section class="section"><div class="container prose" style="max-width:900px" id="terms"><h2>Prize draw terms</h2>
<p><b>Promoter.</b> SQ Driving School, part of DriveSQ Driving School, Manchester. Contact us on WhatsApp or phone: <a href="tel:{TEL}">{PHONE}</a>.</p>
<p><b>Prize.</b> Each month's prize is a £35 driving lesson voucher, to use towards lessons with SQ Driving School / DriveSQ. This draw is run together with DriveSQ's monthly Free Hour Draw, so all eligible entries from both go into the same draw.</p>
<p><b>Who can enter.</b> UK residents aged 17 or over who live in an area we cover. DriveSQ and SQ Driving School staff, instructors and their households can't enter.</p>
<p><b>How to enter.</b> Send a booking request using the “Book in 60 seconds” form on this website and tick the box to enter the draw. Entry is free — no purchase is necessary and you don't have to book or pay for lessons to win. One entry per person (per mobile number) per month; extra entries are ignored.</p>
<p><b>Closing time.</b> Entries for each month close at 6pm UK time on the last day of that month. If you enter after that month's draw has taken place, you're entered into the next month's draw.</p>
<p><b>Choosing the winner.</b> One winner is chosen at random from all eligible entries for the month, shortly after entries close. We keep a record of every draw. Entering is a chance to win, not a guaranteed prize.</p>
<p><b>Telling the winner.</b> We'll contact the winner by WhatsApp, text or phone within 7 days of the draw. If we can't reach the winner within 14 days, or they aren't eligible, we may choose another winner.</p>
<p><b>Using the voucher.</b> The voucher can only be used for SQ Driving School / DriveSQ driving lessons and is valid for 6 months. There's no cash alternative, and it can't be transferred, sold or exchanged. It can be used alongside our other offers.</p>
<p><b>Publicity.</b> We'll only show a winner's name on our website or social media if they agree, and then only their first name and postcode area.</p>
<p><b>Your data.</b> We use your details to run the draw, contact the winner and reply to your booking request. Entering doesn't sign you up for marketing. See our <a href="privacy.html">privacy policy</a>.</p>
<p><b>Changes.</b> We may change or end the draw for future months by updating this page. This won't affect entries already made or vouchers already given.</p>
<p><b>Law.</b> These terms are governed by the law of England and Wales.</p>
<p class="note">Last updated: 17 October 2026</p></div></section>
{cta(root, "Ready to enter?", "Book in 60 seconds and tick the box — it's free.")}"""
    return page("free-prize-draw.html", "Win a £35 Driving Lesson Voucher | Free Prize Draw | SQ Driving School",
                "Enter SQ Driving School's free monthly prize draw to win a £35 driving lesson voucher. Tick the box when you book in 60 seconds — no purchase needed.", body, root)


def book_page():
    root = ""
    body = page_hero("Book now", "Book in 60 seconds.", "Answer a few quick questions and we'll have everything we need to get you started. No forms to email, no waiting.", ["Book now"], root,
                     '<div data-mascot style="--rope:60px" data-say="Quick and easy — <b>let\'s get you booked!</b> 🚗"></div>')
    body += reassure()
    body += f'<section class="section--tight"><div class="container" style="max-width:900px">{draw_banner(root)}{wizard_html()}</div></section>'
    body += f"""<section class="section section--alt"><div class="container"><div class="grid grid--3" data-stagger=".08">
<a class="card" href="tel:{TEL}" data-reveal="up"><div class="card__icon">{icon('phone')}</div><h3>Prefer to call?</h3><p class="mb-0 mono">{PHONE}</p></a>
<a class="card" data-wa="Hi SQ Driving School! I'd like to book lessons." href="https://wa.me/{WA}" data-reveal="up"><div class="card__icon">{icon('wa')}</div><h3>Just WhatsApp us</h3><p class="mb-0">Message us in your own words.</p></a>
<a class="card" href="first-lesson.html" data-reveal="up"><div class="card__icon">{icon('car')}</div><h3>What happens next?</h3><p class="mb-0">See exactly how your first lesson goes.</p></a>
</div></div></section>"""
    return page("book.html", "Book Driving Lessons Online | 60-Second Booking | SQ Driving School",
                "Book driving lessons in Greater Manchester in 60 seconds. Choose manual or automatic, check your postcode and discounts, and send your booking — a real person replies fast.", body, root)


def voucher_page():
    root = ""
    vals = [("40", "Single 1-hour session"), ("70", "One 2-hour lesson"), ("140", "Two 2-hour lessons"), ("350", "10-hour block")]
    v = "".join(f'<input type="radio" name="vval" id="vv{i}" value="{a}" data-label="{l}" {"checked" if i == 1 else ""}><label for="vv{i}">£{a} · {l}</label>' for i, (a, l) in enumerate(vals))
    body = page_hero("Gift vouchers", "Give the gift of driving.", "Birthdays, 17th birthdays, Christmas, passing exams — a driving lesson voucher is a gift they'll actually use.", ["Gift vouchers"], root)
    body += f"""<section class="section--tight"><div class="container"><div class="tool neon-border" data-tool="voucher" data-reveal="up">
  <div class="tool__head"><div class="card__icon">{icon('tag')}</div><div><h3>Design your voucher</h3><p class="mb-0 note">See it update live, then send your request on WhatsApp.</p></div></div>
  <div class="grid grid--2" style="align-items:center">
    <div>
      <div class="field"><span class="label">Voucher value</span><div class="seg">{v}</div></div>
      <div class="field"><label for="vto">To</label><input class="input" id="vto" name="vto" maxlength="30" placeholder="Their name"></div>
      <div class="field"><label for="vfrom">From</label><input class="input" id="vfrom" name="vfrom" maxlength="30" placeholder="Your name"></div>
      <div class="field"><label for="vmsg">Message</label><input class="input" id="vmsg" name="vmsg" maxlength="80" placeholder="Happy 17th birthday!"></div>
    </div>
    <div>
      <div class="voucher" data-tilt="10">
        <div class="voucher__top"><div><span class="sq-logo" style="font-size:2.6rem">SQ</span><div class="voucher__small">Driving School · Gift voucher</div></div><div class="voucher__small" style="text-align:right">Powered by<br>DriveSQ</div></div>
        <div><div class="voucher__amount js-vamt">£70</div><div class="voucher__small js-vlabel">One 2-hour lesson</div></div>
        <div><div class="voucher__to">For <b class="js-vto">Someone special</b> · from <b class="js-vfrom">Me</b></div><div class="voucher__msg js-vmsg">Happy driving! 🚗</div></div>
      </div>
      <a class="btn btn--red btn--block mt-2 js-vsend" target="_blank" rel="noopener" href="https://wa.me/{WA}">{icon('wa')} Request this voucher on WhatsApp</a>
      <p class="note mt-1">We'll confirm payment and send the voucher. Lessons are booked with SQ Driving School across Greater Manchester.</p>
    </div>
  </div>
</div></div></section>
{cta(root, "Know someone turning 17?", "A driving lesson voucher is the perfect start.")}"""
    return page("gift-vouchers.html", "Driving Lesson Gift Vouchers Manchester | SQ Driving School",
                "Driving lesson gift vouchers for Greater Manchester. Design your voucher online and request it on WhatsApp. From £40.", body, root)
