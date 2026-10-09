from layout import *

MASCOT = '<div data-mascot style="--rope:60px" data-say="{say}"></div>'


def comfort_page():
    root = ""
    worries = [("traffic", "Busy traffic"), ("roundabouts", "Roundabouts"), ("judged", "Being judged"), ("stalling", "Stalling"),
               ("parking", "Parking & manoeuvres"), ("forget", "Forgetting what to do"), ("test", "The driving test"), ("instructor", "Meeting someone new")]
    w = "".join(f'<input type="checkbox" name="worry" id="w-{k}" value="{k}" data-label="{l}"><label for="w-{k}">{l}</label>' for k, l in worries)
    tips = [("🫁", "Breathe before you start", "Two minutes of slow breathing calms your body before you turn the key. Try the coach above."),
            ("🗣️", "Say how you feel", "Tell your instructor when something feels too much. We'll slow down — no questions asked."),
            ("🎯", "One thing at a time", "Each lesson focuses on one or two skills. Nobody expects you to know everything at once."),
            ("📱", "See your progress", "Your DriveSQ Student Portal shows every skill improving, so you can see how far you've come."),
            ("☕", "Take breaks", "Need a pause? Pull over somewhere safe and take five. It's your lesson."),
            ("🌱", "Mistakes are learning", "Stalling, wrong lane, forgotten mirror — it happens to every learner. It's how you improve.")]
    t = "".join(f'<article class="card" data-reveal="up"><div style="font-size:2rem">{e}</div><h3 class="mt-1">{h}</h3><p class="mb-0">{d}</p></article>' for e, h, d in tips)
    faqs = [("What if I panic while driving?", "Your instructor has dual controls and can brake at any time. If you feel overwhelmed, they'll help you pull over safely so you can take a breather."),
            ("Will I have to drive on busy roads in my first lesson?", "No. Your first lesson is on quiet roads. You'll move to busier roads only when you and your instructor agree you're ready."),
            ("Can I learn in an automatic to make it easier?", "Yes. Automatic cars have no clutch or gears, which many nervous learners find much less stressful. The price is the same."),
            ("Can I tell you about my anxiety before my first lesson?", "Please do. Message us on WhatsApp and we'll plan your first lessons around how you feel."),
            ("What if I make lots of mistakes?", "That's how everyone learns. There's no judgement — your instructor will calmly help you understand what happened and try again.")]
    f = "".join(f'<details data-reveal="up"><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    body = page_hero("Comfort Zone", "Nervous? You're in the right place.", "Feeling anxious about driving is completely normal. Here's everything we do to help you feel calm, safe and in control.", ["Comfort Zone"], root,
                     MASCOT.format(say="You've got this! 💙 <b>Let's take it slow.</b>"))
    body += reassure()
    body += f"""<section class="section"><div class="container" style="max-width:960px"><div class="tool neon-border" id="plan" data-reveal="up">
  <div class="tool__head"><div class="card__icon">{icon('heart')}</div><div><h3>Your personal comfort plan</h3><p class="mb-0 note">Tell us what worries you. We'll show you exactly how we'll help.</p></div></div>
  <form data-tool="comfort">
    <div class="field"><span class="label">What worries you most? (pick any)</span><div class="seg">{w}</div></div>
    <div class="field"><span class="label">Have you driven before?</span><div class="seg"><input type="radio" name="cexp" id="ce1" value="none" checked><label for="ce1">Never</label><input type="radio" name="cexp" id="ce2" value="some"><label for="ce2">A little</label><input type="radio" name="cexp" id="ce3" value="lots"><label for="ce3">Quite a lot</label></div></div>
    <div class="field"><span class="label">What pace feels right?</span><div class="seg"><input type="radio" name="cpace" id="cp1" value="gentle" checked><label for="cp1">Gentle &amp; slow</label><input type="radio" name="cpace" id="cp2" value="steady"><label for="cp2">Steady</label></div></div>
    <button class="btn btn--red btn--block" type="submit">{icon('heart')} Show my comfort plan</button>
    <div class="result" role="status" aria-live="polite"></div>
  </form>
</div></div></section>
<section class="section section--alt" id="breathe"><div class="container split">
  <div data-reveal="left"><div class="eyebrow">Calm breathing coach</div><h2 data-split>Two minutes to feel calmer.</h2>
    <p class="lead">Box breathing is a simple technique: breathe in for 4, hold for 4, breathe out for 4, hold for 4. Do four rounds before a lesson or your test.</p>
    <p class="note">This is a general relaxation exercise, not medical advice. If anxiety is affecting your daily life, speak to your GP.</p></div>
  <div class="tool" data-tool="breathe" data-reveal="right"><div class="breathe">
    <div class="breathe__ring"><div class="breathe__circle"></div><span class="breathe__label">Ready?</span></div>
    <div class="breathe__count" aria-live="polite">Press start and follow the circle</div>
    <button class="btn btn--red js-breathe" type="button">Start breathing</button>
  </div></div>
</div></section>
<section class="section"><div class="container"><div class="section__head center"><div class="eyebrow">Tips that help</div><h2 data-split>Small things that make a big difference.</h2></div><div class="grid grid--3" data-stagger=".06">{t}</div></div></section>
<section class="section section--alt"><div class="container" style="max-width:900px"><div class="section__head"><div class="eyebrow">Nervous learner questions</div><h2 data-split>You're not the only one asking.</h2></div><div class="faq">{f}</div>
<div class="btn-row mt-3"><a class="btn btn--ghost" href="first-lesson.html">What happens in your first lesson</a><a class="btn btn--ghost" href="guides/nervous-drivers.html">Guide: learning as a nervous driver</a></div></div></section>
{cta(root, "Ready when you are.", "Message us and tell us how you feel. We'll plan your lessons around you.")}"""
    return page("comfort.html", "Nervous Driver Lessons Manchester | Comfort Zone | SQ Driving School",
                "Nervous about learning to drive? SQ Driving School's Comfort Zone: a personal comfort plan, calm-breathing coach and patient lessons across Greater Manchester.", body, root)


def first_lesson_page():
    root = ""
    steps = [("Before", "💬", "We say hello", "We confirm your lesson time and pick-up address on WhatsApp. Ask us anything — nothing is a silly question."),
             ("0:00", "🪪", "Quick checks", "We check your provisional licence and do a quick eyesight check: reading a car number plate from 20 metres."),
             ("0:10", "🛣️", "Off somewhere quiet", "Your instructor drives you to a calm, empty road, chatting on the way so you can settle in."),
             ("0:25", "🎛️", "Meet the car", "Seat, steering, mirrors and the controls — explained slowly with plenty of time for questions."),
             ("0:50", "🚗", "Your first drive", "Moving off and stopping on quiet roads, with your instructor guiding every step. Dual controls mean you're always safe."),
             ("1:30", "🔁", "Practise & relax", "A few more goes at moving off, stopping and gentle turns. Breaks whenever you like."),
             ("1:45", "🎉", "How did it go?", "A friendly chat about what went well, and your DriveSQ Student Portal gets set up so you can see your progress.")]
    st = "".join(f'<div class="step" data-reveal="left"><div class="step__dot" style="font-size:1.3rem">{e}</div><div class="step__body"><span class="lesson-step__time">{tm}</span><h3>{h}</h3><p class="mb-0">{d}</p></div></div>' for tm, e, h, d in steps)
    bring = [("🪪", "Your provisional licence", "The photocard — we'll check it before you drive."),
             ("👓", "Glasses or contacts", "If you need them to see distances."),
             ("👟", "Comfortable shoes", "Flat, thin soles help you feel the pedals. Avoid heels, flip-flops and heavy boots."),
             ("💧", "A bottle of water", "Two hours goes quickly — stay comfortable.")]
    b = "".join(f'<article class="card" data-reveal="up"><div style="font-size:2rem">{e}</div><h3 class="mt-1">{h}</h3><p class="mb-0">{d}</p></article>' for e, h, d in bring)
    wont = ["Busy main roads or the city centre", "Motorways or dual carriageways", "Manoeuvres like parallel parking", "Anything you don't feel ready for"]
    wt = "".join(f"<li><span><b>{x}</b></span></li>" for x in wont)
    body = page_hero("Your first lesson", "No surprises. Just a calm first drive.", "Here's exactly what happens in your first 2-hour lesson with SQ Driving School — so you can relax and enjoy it.", ["First lesson"], root,
                     MASCOT.format(say="First lesson? <b>I'll show you how it goes!</b> 🚗"))
    body += reassure()
    body += f"""<section class="section"><div class="container split" style="align-items:start">
  <div data-reveal="left" style="position:sticky;top:110px"><div class="eyebrow">Step by step</div><h2 data-split>Your first two hours.</h2><p class="lead">Two hours gives you time to settle in properly — no rushing.</p>
  <div class="btn-row mt-2"><a class="btn btn--red" data-wa="Hi SQ! I'd like to book my first lesson." href="https://wa.me/{WA}">{icon('wa')} Book my first lesson</a></div></div>
  <div class="timeline"><div class="timeline__fill"></div>{st}</div>
</div></section>
<section class="section section--alt"><div class="container"><div class="section__head center"><div class="eyebrow">What to bring</div><h2 data-split>Four simple things.</h2></div><div class="grid grid--4" data-stagger=".06">{b}</div></div></section>
<section class="section"><div class="container split">
  <div data-reveal="left"><div class="eyebrow">Relax</div><h2 data-split>Things you won't do in your first lesson.</h2><p class="lead">Your first lesson is about getting comfortable. These come later, when you're ready.</p></div>
  <ul class="ticks" data-reveal="right">{wt}</ul>
</div></section>
<section class="section section--alt"><div class="container" style="max-width:900px"><div class="faq">
<details data-reveal="up"><summary>Do I need to have passed my theory test first?</summary><div>No. You can start lessons as soon as you have your provisional licence. You'll need your theory test before you book your practical test.</div></details>
<details data-reveal="up"><summary>Manual or automatic for my first lesson?</summary><div>Either — and the price is the same. Read our <a class="red" href="guides/manual-vs-automatic.html">manual vs automatic guide</a> if you're not sure.</div></details>
<details data-reveal="up"><summary>Can I have just one hour for my first lesson?</summary><div>Yes — a single 1-hour session is £40. Most learners prefer 2 hours (£70) because it gives time to settle in.</div></details>
<details data-reveal="up"><summary>I'm really nervous. What should I do?</summary><div>Tell us when you book, and visit our <a class="red" href="comfort.html">Comfort Zone</a> for a personal comfort plan and a calm-breathing coach.</div></details>
</div></div></section>
{cta(root, "Your first drive is closer than you think.", "Message us on WhatsApp to book your first lesson.")}"""
    return page("first-lesson.html", "Your First Driving Lesson | What to Expect | SQ Driving School",
                "What happens in your first driving lesson with SQ Driving School: step-by-step guide, what to bring, and what you won't have to do. Greater Manchester.", body, root)
