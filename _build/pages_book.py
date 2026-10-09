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
        ("When suits you best?", "Pick any that work.", _choices("wtime", [("Weekday daytime", "☀️", "Weekday daytime", ""), ("Weekday evenings", "🌙", "Weekday evenings", ""), ("Weekends", "🗓️", "Weekends", "")], "checkbox") +
         '<div class="choice mt-2"><input type="checkbox" name="wnervous" id="wnervous" value="yes"><label for="wnervous"><span class="em">💙</span><b>I\'m a bit nervous</b><small>We\'ll take it slow and plan around you</small></label></div>'),
        ("Last thing — what's your name?", "So we know who we're chatting to.", '<div class="field mt-2"><label for="wname">First name</label><input class="input" id="wname" name="wname" type="text" autocomplete="given-name" placeholder="Your first name"></div>'),
        ("All set! 🎉", "Check your details, then send them to us on WhatsApp. A real person will reply.", f'<div class="wizard__summary"></div><a class="btn btn--wa btn--block js-wsend" target="_blank" rel="noopener" href="https://wa.me/{WA}">{icon("wa")} Send to SQ on WhatsApp</a><p class="note mt-1 mb-0">Nothing is stored on this website — your details go straight into a WhatsApp message for you to send.</p>'),
    ]
    st = "".join(f'<div class="wizard__step"><div class="wizard__q">{q}</div><p class="mb-0">{sub}</p>{body}</div>' for q, sub, body in steps)
    return f"""<div class="tool neon-border wizard" data-tool="wizard" data-reveal="up">
  <div class="quiz__meta"><span class="js-stepnum">Step 1</span><span>⏱ about 60 seconds</span></div>
  <div class="wizard__bar"><span></span></div>
  {st}
  <div class="wizard__nav"><button class="btn btn--ghost js-back" type="button">← Back</button><button class="btn btn--red js-next" type="button">Next →</button></div>
</div>"""


def book_page():
    root = ""
    body = page_hero("Book now", "Book in 60 seconds.", "Answer a few quick questions and we'll have everything we need to get you started. No forms to email, no waiting.", ["Book now"], root,
                     '<div data-mascot style="--rope:60px" data-say="Quick and easy — <b>let\'s get you booked!</b> 🚗"></div>')
    body += reassure()
    body += f'<section class="section--tight"><div class="container" style="max-width:900px">{wizard_html()}</div></section>'
    body += f"""<section class="section section--alt"><div class="container"><div class="grid grid--3" data-stagger=".08">
<a class="card" href="tel:{TEL}" data-reveal="up"><div class="card__icon">{icon('phone')}</div><h3>Prefer to call?</h3><p class="mb-0 mono">{PHONE}</p></a>
<a class="card" data-wa="Hi SQ Driving School! I'd like to book lessons." href="https://wa.me/{WA}" data-reveal="up"><div class="card__icon">{icon('wa')}</div><h3>Just WhatsApp us</h3><p class="mb-0">Message us in your own words.</p></a>
<a class="card" href="first-lesson.html" data-reveal="up"><div class="card__icon">{icon('car')}</div><h3>What happens next?</h3><p class="mb-0">See exactly how your first lesson goes.</p></a>
</div></div></section>"""
    return page("book.html", "Book Driving Lessons Online | 60-Second Booking | SQ Driving School",
                "Book driving lessons in Greater Manchester in 60 seconds. Choose manual or automatic, check your postcode and discounts, and send your booking on WhatsApp.", body, root)


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
