"""Manchester — one strong page for "driving lessons Manchester", plus the searches the site didn't answer yet.

Until now 30+ pages had "driving lessons … Manchester" in their title and none of them owned the main search. This module adds:
  driving-lessons-manchester.html            the pillar: prices, every lesson type, every Manchester postcode and
                                             neighbourhood, the test centres with pass rates, a learner planner tool, FAQ
  driving-instructors-manchester.html        "driving instructor Manchester" (how matching works, ADI/PDI badges)
  female-driving-instructor-manchester.html  "female driving instructor Manchester"
  evening-weekend-driving-lessons-manchester.html
  pass-driving-test-fast-manchester.html     "how to pass your driving test fast in Manchester"
  driving-lessons-for-overseas-drivers-manchester.html
  driving-lessons-for-older-learners-manchester.html
Prices come from the site's price list; pass rates from pages_routes (passrates.uk / DVSA). No invented reviews, numbers of
instructors or promises we can't keep (e.g. a female instructor is matched where one covers the postcode)."""
import json
from hub_shell import *
import pages_routes as RT
import pages_seo as SEO
import pages_postcodes as PCD

PILLAR = "driving-lessons-manchester.html"
NAT = 48.5  # GB average used across the site's test-route guides
SRC = {
    "lessons": ("GOV.UK — Driving lessons and learning to drive", "https://www.gov.uk/driving-lessons-learning-to-drive"),
    "cost": ("GOV.UK — Driving test cost", "https://www.gov.uk/driving-test-cost"),
    "book": ("GOV.UK — Book your driving test", "https://www.gov.uk/book-driving-test"),
    "change": ("GOV.UK — Change your driving test appointment", "https://www.gov.uk/change-driving-test"),
    "adi": ("GOV.UK — Find your nearest driving instructor / approved driving instructors", "https://www.gov.uk/find-driving-schools-and-lessons"),
    "badge": ("GOV.UK — Approved driving instructor (ADI) badge and trainee licence", "https://www.gov.uk/become-driving-instructor"),
    "nongb": ("GOV.UK — Driving in Great Britain on a non-GB licence", "https://www.gov.uk/driving-nongb-licence"),
    "exchange": ("GOV.UK — Exchange a foreign driving licence", "https://www.gov.uk/exchange-foreign-driving-licence"),
    "provisional": ("GOV.UK — Apply for your first provisional driving licence", "https://www.gov.uk/apply-first-provisional-driving-licence"),
    "eyesight": ("GOV.UK — Driving eyesight rules", "https://www.gov.uk/driving-eyesight-rules"),
    "theory": ("GOV.UK — Theory test: cars", "https://www.gov.uk/theory-test"),
    "pr_gm": ("passrates.uk — Greater Manchester test centres, 2024-25 (from DVSA data)", "https://passrates.uk/counties/greater-manchester"),
}
SIDE = (f'<p>£35/hr manual or automatic · single hour £40 · 10 hours £350 (£320 for NHS staff, students and M16, M18 &amp; M19) · free DriveSQ Student Portal · door-to-door pick-up.</p>'
        f'<a class="btn btn--red btn--block" href="#book">{icon("calendar")} Book in 60 seconds</a>')
HOODS = SEO.neighbourhoods()
MAN_HOODS = sorted([h for h in HOODS if h["borough"] == "Manchester" and h["slug"] != "chorlton"], key=lambda h: h["name"])  # chorlton redirects to chorlton-cum-hardy
CODES = [c for c in PCD.postcode_list(SEO.load_postcodes) if c[1] == "Manchester"]
CENTRES = {c["slug"]: c for c in RT.C}
NEAR = ["west-didsbury", "cheetham-hill", "sale", "bredbury", "chadderton"]  # the centres Manchester learners actually book


def _biz(path, name):
    return [{"@context": "https://schema.org", "@type": "DrivingSchool", "@id": f"{SITE}/{path}#school", "name": name, "url": f"{SITE}/{path}",
             "telephone": "+44 7352 932003", "priceRange": "£35–£350", "parentOrganization": {"@type": "Organization", "name": "DriveSQ", "url": "https://www.drivesq.co.uk"},
             "areaServed": [{"@type": "City", "name": "Manchester"}] + [{"@type": "Place", "name": h["name"] + ", Manchester"} for h in MAN_HOODS[:40]],
             "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Driving lessons in Manchester", "itemListElement": [
                 {"@type": "Offer", "name": "Single 1-hour driving lesson", "price": "40", "priceCurrency": "GBP"},
                 {"@type": "Offer", "name": "Driving lesson (2 hours or more), per hour", "price": "35", "priceCurrency": "GBP"},
                 {"@type": "Offer", "name": "10-hour block", "price": "350", "priceCurrency": "GBP"},
                 {"@type": "Offer", "name": "10-hour block for NHS staff, students and M16/M18/M19", "price": "320", "priceCurrency": "GBP"}]}}]


def M(path, seo, cat, crumb, title, desc, stats, keys, body, faqs, src, related, after="", extra_schema=None):
    crumbs = [("Driving lessons Manchester", PILLAR)] + ([crumb] if crumb else [])
    return shell(path, seo, cat, crumbs, title, desc, stats, keys, body, faqs, [SRC[k] if isinstance(k, str) else k for k in src], related,
                 side_title="Lessons in Manchester", booking_heading="Book driving lessons in Manchester in 60 seconds", active="lessons.html",
                 side_html=SIDE, root="", extra_schema=extra_schema, after_body=after)


def _centre_table():
    rows = ""
    for s in NEAR:
        c = CENTRES[s]
        d = c["rate"] - NAT
        rows += (f'<tr><td><a href="test-routes/{s}-driving-test-routes.html"><b>{c["name"]}</b></a></td><td>{c["pc"]}</td>'
                 f'<td class="mono">{c["rate"]}%</td><td style="color:{"#22e07a" if d >= 0 else "#ff6b6b"}">{"+" if d >= 0 else "−"}{abs(d):.1f} pts</td>'
                 f'<td><a href="knowledge/test-centre-{s}.html">Centre guide</a> · <a href="test-routes/{s}-driving-test-routes.html">Routes</a></td></tr>')
    return (f'<div class="rx-table-wrap" data-reveal="up"><table class="rx-table"><thead><tr><th>Test centre</th><th>Postcode</th><th>Pass rate 2024-25</th>'
            f'<th>vs GB ({NAT}%)</th><th>Guides</th></tr></thead><tbody>{rows}</tbody></table></div>')


SERV = [("automatic-driving-lessons-manchester.html", "Automatic lessons", "No clutch — easier in city traffic."),
        ("manual-driving-lessons-manchester.html", "Manual lessons", "Licence covers manual and automatic."),
        ("services/intensive-driving-courses-manchester.html", "Intensive courses", "Licence in weeks, planned around your test."),
        ("services/nervous-driver-lessons-manchester.html", "Nervous drivers", "Quiet roads first, at your pace."),
        ("services/beginner-driving-lessons-manchester.html", "Complete beginners", "Never driven? Perfect."),
        ("services/refresher-driving-lessons-manchester.html", "Refresher lessons", "Passed years ago? Get confident again."),
        ("services/motorway-driving-lessons-manchester.html", "Motorway lessons", "M60, M56 and M602 with dual controls."),
        ("services/pass-plus-courses-manchester.html", "Pass Plus", "After your test — night, rural, dual carriageways."),
        ("services/mock-driving-tests-manchester.html", "Mock tests", "A full test drive, marked like the real one."),
        ("services/failed-driving-test-lessons-manchester.html", "Failed your test?", "Fix the faults, rebook with confidence."),
        ("services/affordable-driving-lessons-manchester.html", "Affordable lessons", "£35/hr, blocks from £320."),
        ("student-driving-lessons-manchester.html", "Students", "10 hours £320 with student ID."),
        ("nhs-driving-lessons.html", "NHS staff", "10 hours £320, lessons around shifts."),
        ("female-driving-instructor-manchester.html", "Female instructor", "Ask and we'll match you where one covers you."),
        ("evening-weekend-driving-lessons-manchester.html", "Evenings &amp; weekends", "Lessons around work, college and family."),
        ("driving-lessons-for-overseas-drivers-manchester.html", "Drove abroad?", "Get test-ready for UK roads."),
        ("driving-lessons-for-older-learners-manchester.html", "Learning later", "30, 50 or 70 — it's never too late."),
        ("pass-driving-test-fast-manchester.html", "Pass fast", "The quickest honest route to a full licence.")]


def _service_grid():
    return '<div class="grid grid--3" data-stagger=".04">' + "".join(
        f'<a class="rx-study" href="{h}" data-reveal="up"><span class="k-cat">Manchester</span><h3>{t}</h3><p>{d}</p></a>' for h, t, d in SERV) + "</div>"


PLANNER = """
<div class="rx-tool" id="planner" data-reveal="up">
  <div class="rx-tool__head"><div class="card__icon">{pin}</div><div><h3>Manchester learner planner</h3><p>Your postcode → your nearest test centres, your price and a realistic plan</p></div></div>
  <form class="mp-form" autocomplete="off">
    <div><label for="mp-pc">Your postcode</label><input id="mp-pc" class="mp-in" placeholder="e.g. M19 2AB" required maxlength="8" style="text-transform:uppercase"></div>
    <div><label for="mp-exp">Driving so far</label><select id="mp-exp" class="mp-in"><option value="0">Never driven</option><option value="10">A few lessons</option><option value="25">Quite a few lessons</option><option value="35">Nearly test-ready</option></select></div>
    <div><label for="mp-hpw">Hours a week</label><select id="mp-hpw" class="mp-in"><option value="2">2 hours</option><option value="4" selected>4 hours</option><option value="6">6 hours</option><option value="10">10 hours (intensive)</option></select></div>
    <div><label for="mp-disc">Discount</label><select id="mp-disc" class="mp-in"><option value="">None</option><option value="nhs">NHS staff</option><option value="stu">Student</option></select></div>
    <button class="btn btn--red" type="submit">Plan my lessons</button>
  </form>
  <div class="mp-res" aria-live="polite"></div>
</div>
<script>
(function(){
  var C=__CENTRES__, OFFER=["M16","M18","M19"];
  var f=document.querySelector('.mp-form'), out=document.querySelector('.mp-res');
  function km(a,b){var R=6371,r=Math.PI/180,dl=(b[0]-a[0])*r,dn=(b[1]-a[1])*r,x=Math.sin(dl/2)*Math.sin(dl/2)+Math.cos(a[0]*r)*Math.cos(b[0]*r)*Math.sin(dn/2)*Math.sin(dn/2);return 2*R*Math.asin(Math.sqrt(x));}
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var pc=document.getElementById('mp-pc').value.toUpperCase().replace(/[^A-Z0-9]/g,'');
    if(pc.length<2){return;}
    out.innerHTML='<p class="note">Looking up '+esc(pc)+'…</p>';
    var full=/^[A-Z]{1,2}\\d[A-Z\\d]?\\d[A-Z]{2}$/.test(pc), oc=full?pc.slice(0,-3):pc;
    var url='https://api.postcodes.io/'+(full?'postcodes/':'outcodes/')+encodeURIComponent(pc);
    // look the centres up live from their postcodes (falls back to the rounded coordinates baked in)
    var bulk=fetch('https://api.postcodes.io/postcodes',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({postcodes:C.map(function(c){return c.pc;})})}).then(function(r){return r.json();}).then(function(b){(b.result||[]).forEach(function(x,i){if(x&&x.result&&C[i]){C[i].lat=x.result.latitude;C[i].lon=x.result.longitude;}});}).catch(function(){});
    Promise.all([fetch(url).then(function(r){return r.json();}),bulk]).then(function(arr){var j=arr[0];
      if(!j||!j.result){out.innerHTML='<p class="note">We couldn\\'t find that postcode — check it and try again, or message us on WhatsApp.</p>';return;}
      var me=[j.result.latitude,j.result.longitude];
      var exp=+document.getElementById('mp-exp').value, hpw=+document.getElementById('mp-hpw').value, disc=document.getElementById('mp-disc').value;
      var hours=Math.max(6,45-exp), weeks=Math.ceil(hours/hpw);
      var offer=OFFER.indexOf(oc)>=0, cheap=offer||disc;
      var blocks=Math.floor(hours/10), rest=hours-blocks*10, cost=blocks*(cheap?320:350)+rest*35;
      var list=C.map(function(c){return Object.assign({d:km(me,[c.lat,c.lon])*0.621},c);}).sort(function(a,b){return a.d-b.d;}).slice(0,3);
      var best=list.slice().sort(function(a,b){return b.rate-a.rate;})[0];
      var rows=list.map(function(c,i){return '<tr><td><a href="test-routes/'+c.slug+'-driving-test-routes.html"><b>'+c.name+'</b></a>'+(c===best?' <span class="rx-badge" style="margin-left:4px"><i></i>highest pass rate nearby</span>':'')+'</td><td class="mono">'+c.d.toFixed(1)+' mi</td><td class="mono">'+c.rate+'%</td></tr>';}).join('');
      out.innerHTML='<div class="rx-out"><div><b>'+hours+' hrs</b><span>lessons, roughly</span></div><div><b>'+weeks+' weeks</b><span>at '+hpw+' hrs a week</span></div><div class="rx-big"><b>£'+cost.toLocaleString('en-GB')+'</b><span>'+(cheap?'with your £320 blocks':'at £350 per 10 hours')+'</span></div><div><b>'+(offer?'Yes':'—')+'</b><span>'+(offer?oc+' offer: 10 hrs £320':'postcode offer')+'</span></div></div>'+
        '<div class="rx-table-wrap mt-2"><table class="rx-table"><thead><tr><th>Nearest test centres</th><th>Distance</th><th>Pass rate</th></tr></thead><tbody>'+rows+'</tbody></table></div>'+
        '<p class="note">Hours are a starting estimate based on DVSA\\'s average of about 45 hours of lessons plus private practice — everyone is different, and your instructor will tell you honestly after your first lesson. Distances are straight-line.</p>'+
        '<div class="btn-row"><a class="btn btn--red" href="#book">Book my first lesson</a><a class="btn btn--wa" href="https://wa.me/447352932003?text='+encodeURIComponent("Hi SQ! I'm in "+pc+" and I'd like about "+hours+" hours of lessons ("+hpw+" hrs a week).")+'">WhatsApp this plan</a></div>';
    }).catch(function(){out.innerHTML='<p class="note">The postcode lookup isn\\'t responding — message us on WhatsApp and we\\'ll plan it with you.</p>';});
  });
})();
</script>
<style>.mp-form{display:grid;grid-template-columns:repeat(4,minmax(0,1fr)) auto;gap:10px;align-items:end}.mp-form label{display:block;font-size:.8rem;font-weight:600;margin-bottom:4px;color:var(--muted)}.mp-in{width:100%;padding:11px 12px;border-radius:12px;border:1px solid var(--line-2);background:var(--panel-2);color:var(--white);font:500 .95rem var(--font-body)}.mp-res{margin-top:14px}@media(max-width:760px){.mp-form{grid-template-columns:1fr 1fr}.mp-form .btn{grid-column:1/-1}}</style>
"""
# approximate centre coordinates — only used if the live postcode lookup for the centres fails
COORDS = {"west-didsbury": (53.418, -2.253), "cheetham-hill": (53.512, -2.236), "sale": (53.431, -2.315), "bredbury": (53.425, -2.112),
          "chadderton": (53.538, -2.142), "atherton": (53.522, -2.497), "bolton": (53.565, -2.44), "bury": (53.595, -2.29), "rochdale": (53.611, -2.152)}


def planner():
    data = [{"slug": s, "name": CENTRES[s]["name"], "pc": CENTRES[s]["pc"], "rate": CENTRES[s]["rate"], "lat": COORDS[s][0], "lon": COORDS[s][1]} for s in COORDS if s in CENTRES]
    return PLANNER.replace("{pin}", icon("pin")).replace("__CENTRES__", json.dumps(data))


def pillar():
    path = PILLAR
    chips_pc = "".join(f'<a class="chip" href="postcodes/{c[0].lower()}.html">{c[0]} · {c[2]}</a>' for c in CODES)
    chips_hood = "".join(f'<a class="chip" href="driving-lessons/{h["slug"]}.html">{h["name"]}</a>' for h in MAN_HOODS)
    other = "".join(f'<a class="chip" href="areas/{b}.html">{n}</a>' for b, n in [("salford", "Salford"), ("trafford", "Trafford"), ("stockport", "Stockport"), ("tameside", "Tameside"), ("oldham", "Oldham"), ("rochdale", "Rochdale"), ("bury", "Bury"), ("bolton", "Bolton"), ("wigan", "Wigan")])
    wd, ch = CENTRES["west-didsbury"], CENTRES["cheetham-hill"]
    body = f"""
<p class="lead">SQ Driving School teaches manual and automatic driving lessons across the whole of Manchester — from the city centre and Ancoats to Didsbury, Chorlton, Levenshulme, Gorton, Wythenshawe, Cheetham Hill and Blackley. Lessons are <b>£35 an hour</b> (a single hour is £40), with door-to-door pick-up, and every learner gets the free <b>DriveSQ Student Portal</b> to see their progress, lessons and theory practice in one place.</p>
<h2>Driving lesson prices in Manchester</h2>
<div class="rx-table-wrap" data-reveal="up"><table class="rx-table"><thead><tr><th>Option</th><th>Price</th><th>Best for</th></tr></thead><tbody>
<tr><td>Single 1-hour lesson</td><td class="mono">£40</td><td>A refresher, a mock test or trying us out</td></tr>
<tr><td>Standard lesson (2 hours or more)</td><td class="mono">£35/hr · £70 for 2 hours</td><td>Most learners — two hours means real progress each time</td></tr>
<tr><td>10-hour block</td><td class="mono">£350</td><td>Steady weekly lessons</td></tr>
<tr><td>10-hour block — NHS staff, students, M16/M18/M19</td><td class="mono">£320</td><td><a href="nhs-driving-lessons.html">NHS</a> · <a href="student-driving-lessons-manchester.html">students</a> · <a href="offer-m16-m18-m19.html">postcode offer</a></td></tr>
<tr><td>DVSA test fees (paid to DVSA)</td><td class="mono">Theory £23 · practical £62 (£75 evenings/weekends)</td><td>Booked on GOV.UK</td></tr>
</tbody></table></div>
<p>Manual and automatic are the same price. No booking fee, no fuel surcharge. <a href="prices.html">Build your own package →</a></p>
<h2>Plan your lessons in 30 seconds</h2>
<p>Enter your postcode to see the three test centres nearest to you with their pass rates, roughly how many hours and weeks you'll need, what it will cost, and whether your postcode gets the £320 offer.</p>
{planner()}
<h2>Every kind of lesson, Manchester-wide</h2>
{_service_grid()}
<h2>Manchester driving test centres — pass rates and routes</h2>
<p>Most Manchester learners test at <b>West Didsbury</b> (M21, {wd['rate']}% in 2024-25) or <b>Cheetham Hill</b> (M8, {ch['rate']}%). Sale, Bredbury and Chadderton are close enough that many people book them for an earlier date. Each centre has its own roads and its own common mistakes — we practise on them before your test.</p>
{_centre_table()}
<p class="note">Pass rates: passrates.uk's analysis of DVSA data for 2024-25. GB average ≈ {NAT}%. A lower pass rate doesn't make a centre "harder for you" — preparation matters far more. <a href="research/driving-test-pass-rates-explained-manchester.html">How to read pass rates →</a></p>
<h2>What learning to drive in Manchester is really like</h2>
<ul>
<li><b>Trams and bus lanes.</b> Metrolink runs on shared streets in the city centre, and bus lanes and bus gates are enforced — <a href="knowledge/driving-with-trams-metrolink.html">driving with trams</a> · <a href="knowledge/bus-lanes-and-bus-gates-manchester.html">bus lanes and gates</a>.</li>
<li><b>Big multi-lane roundabouts</b> — Kingsway, Princess Parkway and the Mancunian Way junctions reward early lane choice. <a href="guides/roundabouts.html">Roundabout guide →</a></li>
<li><b>Quiet roads first.</b> Every learner starts somewhere calm (Levenshulme, Burnage and Chorlton have plenty) before busy roads.</li>
<li><b>Motorways once you're ready.</b> The M60 and M56 are minutes away for <a href="services/motorway-driving-lessons-manchester.html">motorway lessons</a> with dual controls.</li>
<li><b>Clean Air Zone:</b> Greater Manchester's plans changed — <a href="knowledge/greater-manchester-clean-air-zone.html">what it means for learners</a>.</li>
</ul>
<h2>Every Manchester postcode we cover</h2>
<div class="hero__badges">{chips_pc}</div>
<h2>Every Manchester neighbourhood</h2>
<div class="hero__badges">{chips_hood}</div>
<h3 class="mt-2">Elsewhere in Greater Manchester</h3>
<div class="hero__badges">{other}<a class="chip" href="driving-lessons-solihull.html">Solihull (new)</a></div>
<h2>How it works</h2>
<ol>
<li><b>Book in 60 seconds</b> below or on WhatsApp — a real person replies, usually within the hour.</li>
<li><b>We match you</b> with an instructor who covers your postcode, teaches your gearbox and fits your times.</li>
<li><b>Your first lesson</b> starts somewhere quiet. <a href="first-lesson.html">What happens in lesson one →</a></li>
<li><b>Track everything</b> in the DriveSQ Student Portal — skills, hours, upcoming lessons and theory practice.</li>
<li><b>Mock test, then the real thing</b> — on your test centre's roads.</li>
</ol>
<p>Want a guide you can come back to? <a href="guides/cost-of-learning-to-drive-manchester.html">The real cost of learning to drive in Manchester</a> · <a href="knowledge/driving-test-waiting-times-greater-manchester.html">test waiting times</a> · <a href="learner-toolkit.html">free learner toolkit</a>.</p>
"""
    faqs = [
        ("How much are driving lessons in Manchester?", "With SQ Driving School it's £35 an hour for lessons of two hours or more, £40 for a single hour, £350 for 10 hours, or £320 for 10 hours for NHS staff, students and learners in M16, M18 and M19. Manual and automatic cost the same."),
        ("How many driving lessons will I need?", "DVSA says learners need about 45 hours of professional lessons on average, plus private practice. Some people need fewer, some more — use the planner on this page for an estimate, and your instructor will give you an honest view after your first lesson."),
        ("Which driving test centre is best in Manchester?", f"Most Manchester learners use West Didsbury ({wd['rate']}% in 2024-25) or Cheetham Hill ({ch['rate']}%). Pick the one you can practise around and get a date at — preparation on that centre's roads matters more than its pass rate."),
        ("Do you pick up from home, work or college?", "Yes — door-to-door pick-up anywhere we cover in Manchester, including the city centre, universities and hospitals."),
        ("Do you do automatic driving lessons in Manchester?", "Yes, at the same price as manual. Automatic is popular in Manchester's stop-start traffic. See automatic driving lessons Manchester."),
        ("Can I have lessons in the evening or at weekends?", "Many of our instructors teach evenings and weekends. Tell us your times when you book and we'll match you with someone who fits them."),
        ("Can I ask for a female driving instructor?", "Yes. Say so when you book and we'll match you with a female instructor where one covers your postcode — and tell you straight away if one isn't free."),
        ("Is SQ Driving School part of DriveSQ?", "Yes — SQ Driving School is a brand owned and managed by DriveSQ, which is why every learner gets the free DriveSQ Student Portal."),
    ]
    related = [("automatic-driving-lessons-manchester.html", "Pillar", "Automatic driving lessons Manchester", "Every area, same £35/hr price."),
               ("manual-driving-lessons-manchester.html", "Pillar", "Manual driving lessons Manchester", "Clutch control taught properly."),
               ("driving-lessons-near-me.html", "Postcodes", "Driving lessons near me", "Find your postcode and neighbourhood."),
               ("test-routes/west-didsbury-driving-test-routes.html", "Test routes", "West Didsbury test routes", "Roads, roundabouts and common mistakes."),
               ("test-routes/cheetham-hill-driving-test-routes.html", "Test routes", "Cheetham Hill test routes", "Roads, roundabouts and common mistakes."),
               ("driving-instructors-manchester.html", "Instructors", "Driving instructors in Manchester", "How we match you, and what to check.")]
    return M(path, "Driving Lessons Manchester | £35/hr Manual & Automatic | SQ Driving", "Manchester · Driving lessons", None,
             "Driving lessons in Manchester.",
             "Manual and automatic lessons across every Manchester postcode — £35/hr, door-to-door pick-up, the free DriveSQ Student Portal, and test-centre-route practice.",
             [("£35", "per hour, manual or automatic"), (str(len(CODES)), "Manchester postcodes covered"), (str(len(MAN_HOODS)), "neighbourhoods"), (f"{wd['rate']}%", "West Didsbury pass rate")],
             ["£35/hr, single hour £40, 10 hours £350 — or £320 for NHS, students and M16/M18/M19.", "Same price for manual and automatic.",
              "Plan your lessons, cost and nearest test centre with your postcode.", "Practise on West Didsbury and Cheetham Hill test roads before your test."],
             body, faqs, ["lessons", "cost", "book", wd["rate_src"], ch["rate_src"], "pr_gm"], related, extra_schema=_biz(path, "SQ Driving School — Manchester"))


# ───────────────────────── focused pages for searches the site didn't answer ─────────────────────────
REL = [(PILLAR, "Manchester", "Driving lessons in Manchester", "Prices, every area, test centres and the planner."),
       ("prices.html", "Prices", "Prices and package builder", "£35/hr · blocks from £320."),
       ("book.html", "Book", "Book in 60 seconds", "A real person replies, usually within the hour.")]


def instructors():
    path = "driving-instructors-manchester.html"
    body = """
<p class="lead">Looking for a driving instructor in Manchester? Instead of phoning round, tell us your postcode, gearbox and the times that suit you — SQ Driving School (part of DriveSQ) matches you with an instructor who covers your area, and you can see every lesson and skill in the free DriveSQ Student Portal.</p>
<h2>How we match you with an instructor</h2>
<ol><li><b>Your postcode</b> — we look for instructors who already teach around you, so pick-ups are easy and you learn your local roads.</li>
<li><b>Manual or automatic</b> — and whether you'd like a <a href="female-driving-instructor-manchester.html">female instructor</a>.</li>
<li><b>Your times</b> — weekdays, <a href="evening-weekend-driving-lessons-manchester.html">evenings or weekends</a>.</li>
<li><b>Your test centre</b> — so your lessons build towards West Didsbury, Cheetham Hill or wherever you'll test.</li></ol>
<p>Not clicking with your instructor? Tell us and we'll find you another — no awkward conversations.</p>
<h2>What to check about any driving instructor</h2>
<ul><li><b>The badge on the windscreen.</b> A fully qualified Approved Driving Instructor (ADI) displays a <b>green</b> badge. A trainee instructor working under a trainee licence displays a <b>pink</b> one. Both are legal — but you should know which you're paying for.</li>
<li><b>Dual controls</b> on the car.</li>
<li><b>A clear price</b> with nothing hidden — ours is £35/hr, £40 for a single hour.</li>
<li><b>A plan</b> — after your first lesson you should know roughly how many hours you need and what comes next.</li>
<li><b>Progress you can see</b> — every SQ learner gets the DriveSQ Student Portal.</li></ul>
<h2>Questions worth asking before you book</h2>
<ul><li>Which test centre do you know best?</li><li>Do you teach in my area at the times I'm free?</li><li>Do you do 2-hour lessons? (Two hours means real progress each time.)</li><li>How will I know when I'm ready for my test?</li></ul>
<h2>Want to become an instructor?</h2>
<p>DriveSQ works with instructors across Greater Manchester and matches them with pupils by postcode. <a href="research/become-a-driving-instructor-manchester.html">How to become a driving instructor in Manchester →</a></p>
"""
    faqs = [("How do I find a good driving instructor in Manchester?", "Check the windscreen badge (green for a fully qualified ADI, pink for a trainee), make sure the car has dual controls, get a clear price and ask how they'll track your progress. Or let us match you by postcode, gearbox and times."),
            ("Can I change instructor?", "Yes. If it isn't working, tell us and we'll match you with someone else."),
            ("Are your instructors DVSA approved?", "Instructors display their DVSA badge in the car — green for a qualified ADI, pink for a trainee under a trainee licence. Ask us which you'll have when we match you."),
            ("How much does a driving instructor cost in Manchester?", "With SQ it's £35 an hour for lessons of two hours or more, £40 for a single hour, and £350 for 10 hours (£320 for NHS staff, students and M16/M18/M19).")]
    return M(path, "Driving Instructors Manchester | Matched by Postcode | SQ Driving", "Instructors", ("Driving instructors", path),
             "Driving instructors in Manchester.", "We match you with an instructor who covers your postcode, teaches your gearbox and fits your times — and you can see every lesson in the DriveSQ Student Portal.",
             [("£35", "per hour"), ("ADI", "green badge = qualified"), ("1", "message to get matched"), ("Free", "Student Portal")],
             ["Tell us postcode, gearbox and times — we match you.", "Green badge = qualified ADI; pink = trainee.", "Change instructor any time, no awkwardness.", "Every lesson tracked in the Student Portal."],
             body, faqs, ["adi", "badge", "lessons"], REL + [("research/become-a-driving-instructor-manchester.html", "Careers", "Become a driving instructor", "Training, costs and earnings.")])


def female():
    path = "female-driving-instructor-manchester.html"
    body = """
<p class="lead">Would you feel more comfortable learning with a female driving instructor? Lots of learners do — and it's a completely normal thing to ask for. Tell us when you book and we'll match you with a female instructor wherever one covers your postcode. If one isn't free at your times, we'll tell you straight away rather than leave you guessing.</p>
<h2>How to ask</h2>
<ol><li>Message us on <a href="https://wa.me/447352932003?text=Hi%20SQ!%20I%27d%20like%20driving%20lessons%20with%20a%20female%20instructor.">WhatsApp</a> saying you'd like a female instructor — or book below and tell us when we reply.</li>
<li>Tell us your postcode, manual or automatic, and your times.</li>
<li>We confirm who your instructor is before your first lesson.</li></ol>
<h2>Feeling safe and comfortable on every lesson</h2>
<ul><li><b>You know who's coming.</b> We confirm your instructor's name before the first lesson.</li>
<li><b>Pick-up where you choose</b> — home, work, college or somewhere public.</li>
<li><b>You set the pace.</b> Quiet roads first; busy roads only when you're ready. See <a href="comfort.html">our Comfort Zone for nervous drivers</a>.</li>
<li><b>Everything is written down</b> in your DriveSQ Student Portal — lessons, progress and notes.</li>
<li><b>Change instructor any time.</b> If anything doesn't feel right, message us and we'll sort it.</li></ul>
<h2>Same prices, every option</h2>
<p>£35/hr manual or automatic, £40 for a single hour, £350 for 10 hours — or £320 for NHS staff, students and learners in M16, M18 and M19.</p>
"""
    faqs = [("Can I request a female driving instructor in Manchester?", "Yes. Ask when you book. We match you with a female instructor where one covers your postcode and fits your times, and tell you straight away if not."),
            ("Does it cost more?", "No — the same £35/hr as every lesson."),
            ("Can I change instructor later?", "Yes, at any time — just message us."),
            ("Do you offer automatic lessons with a female instructor?", "Where a female instructor who teaches automatic covers your area, yes. Tell us your gearbox when you book.")]
    return M(path, "Female Driving Instructor Manchester | Ask When You Book | SQ Driving", "Comfort", ("Female instructor", path),
             "Female driving instructor in Manchester.", "Prefer a female instructor? Ask when you book and we'll match you where one covers your postcode — and tell you honestly if one isn't free.",
             [("£35", "per hour"), ("You", "choose the pick-up"), ("Any time", "change instructor"), ("Free", "Student Portal")],
             ["Ask for a female instructor when you book.", "We confirm your instructor before lesson one.", "Same price — £35/hr.", "Change instructor any time."],
             body, faqs, ["lessons", "adi"], REL + [("comfort.html", "Comfort", "Nervous about driving?", "Our Comfort Zone and breathing coach.")])


def evenings():
    path = "evening-weekend-driving-lessons-manchester.html"
    body = """
<p class="lead">Working 9 to 5, at college all day or juggling family? Many SQ Driving School instructors teach in the evenings and at weekends across Manchester. Tell us the times you're free when you book and we'll match you with an instructor who fits them.</p>
<h2>Why evening lessons are worth it</h2>
<ul><li><b>Driving in the dark</b> is a real skill — headlights, glare and pedestrians in dark clothes. Evening lessons in autumn and winter let you practise it with dual controls.</li>
<li><b>Quieter roads after rush hour</b> are great for confidence and manoeuvres.</li>
<li><b>Fits around work</b> — no time off needed.</li></ul>
<h2>Why weekend lessons are worth it</h2>
<ul><li><b>Two-hour lessons</b> fit naturally into a Saturday or Sunday.</li>
<li><b>Busy retail-park traffic</b> (Fort, Trafford Centre, Kingsway) is good practice for test-day pressure.</li>
<li><b>Intensive weekends</b> can move you on quickly — see <a href="intensive.html">intensive courses</a>.</li></ul>
<h2>Prices</h2>
<p>Lessons are £35/hr (£40 for a single hour) and £350 for 10 hours, or £320 for NHS staff, students and M16/M18/M19. Note that the <b>DVSA practical test</b> itself costs £75 on evenings, weekends and bank holidays instead of £62 on weekdays.</p>
<h2>Popular times go first</h2>
<p>Weekday evenings and Saturday mornings book up fastest. If you can be flexible by even an hour or two, tell us — it makes matching much quicker. See <a href="knowledge/learning-to-drive-as-a-student-in-manchester.html">learning to drive around a timetable</a>.</p>
"""
    faqs = [("Do you do evening driving lessons in Manchester?", "Yes — many of our instructors teach evenings. Tell us your times when you book and we'll match you."),
            ("Do you do weekend driving lessons?", "Yes, Saturdays and Sundays where your instructor teaches them. Weekend slots are popular, so book early."),
            ("Do evening or weekend lessons cost more?", "Our lessons are £35/hr. The DVSA charges more for an evening or weekend practical test (£75 instead of £62)."),
            ("Is it safe to learn in the dark?", "Yes — the car has dual controls, and practising night driving with an instructor is one of the best things you can do before driving alone.")]
    return M(path, "Evening & Weekend Driving Lessons Manchester | SQ Driving", "Timing", ("Evenings & weekends", path),
             "Evening and weekend driving lessons in Manchester.", "Lessons around work, college and family — many of our Manchester instructors teach evenings and weekends.",
             [("£35", "per hour"), ("2 hrs", "ideal weekend lesson"), ("£75", "DVSA evening/weekend test fee"), ("Free", "Student Portal")],
             ["Tell us your times — we match an instructor who fits them.", "Evening lessons = real night-driving practice.", "Weekends suit 2-hour and intensive lessons.", "Popular slots go first — flexibility helps."],
             body, faqs, ["lessons", "cost"], REL)


def fast():
    path = "pass-driving-test-fast-manchester.html"
    rates = ", ".join(f'{CENTRES[s]["name"]} {CENTRES[s]["rate"]}%' for s in NEAR)
    body = f"""
<p class="lead">Want your licence quickly in Manchester? There's no shortcut around the theory test, the practical test or the hours it takes to drive safely — but there is a fastest <i>honest</i> route. Here it is, step by step.</p>
<h2>The fastest honest route</h2>
<ol><li><b>Get your provisional licence</b> (online on GOV.UK) and start lessons straight away — you don't need your theory first to have lessons.</li>
<li><b>Book your theory test now</b> and revise with our <a href="theory-quiz.html">free theory quiz</a> and the <a href="guides/theory-test-guide.html">theory guide</a>. Your pass certificate lasts two years.</li>
<li><b>Book your practical test as soon as you pass the theory</b> — waiting times are the biggest delay. Read the <a href="knowledge/driving-test-booking-rules-2026.html">2026 booking rules</a> and <a href="knowledge/driving-test-waiting-times-greater-manchester.html">Greater Manchester waiting times</a>.</li>
<li><b>Look wider than one centre.</b> Manchester learners can choose from {rates} — the one you can get a date at soonest is often the one to pick, as long as you practise its roads.</li>
<li><b>Check for earlier dates yourself</b> through the official GOV.UK “change your driving test” service. Be wary of paid apps or sellers offering “guaranteed” early tests.</li>
<li><b>Go intensive when your date is set.</b> Concentrate your hours in the weeks before the test with an <a href="intensive.html">intensive course</a>.</li>
<li><b>Do a mock test</b> on your centre's roads a week before. <a href="services/mock-driving-tests-manchester.html">Mock tests →</a></li></ol>
<h2>Automatic can be quicker</h2>
<p>With no clutch or gears, many learners reach test standard sooner in an automatic. The catch: an automatic licence only covers automatic cars. <a href="guides/manual-vs-automatic.html">Manual vs automatic →</a></p>
<h2>What actually slows people down</h2>
<ul><li>Waiting to book the theory test.</li><li>Gaps of weeks between lessons (you lose skills).</li><li>Booking a test before you're ready, failing and waiting again. <a href="test-faults.html">The faults people fail on →</a></li></ul>
"""
    faqs = [("How fast can I pass my driving test in Manchester?", "It depends mostly on how soon you can get a practical test date and how much driving you've done. Book your theory straight away, book the practical as soon as you pass it, and concentrate your lessons before the date."),
            ("Can I have lessons before passing my theory?", "Yes — you only need a provisional licence to start lessons. You need a theory pass to book the practical test."),
            ("Is it worth buying an early test from an app or seller?", "Be careful. Use the official GOV.UK service to change your test and check the latest DVSA booking rules — some third-party sellers break them."),
            ("Do intensive courses work?", "They work best once you have a test date and some experience — the lessons build straight towards the test.")]
    return M(path, "How to Pass Your Driving Test Fast in Manchester | SQ Driving", "Pass fast", ("Pass fast", path),
             "How to pass your driving test fast in Manchester.", "The quickest honest route to a full licence: theory first, practical booked early, the right test centre, and lessons concentrated before your date.",
             [("2 yrs", "theory certificate lasts"), ("5", "test centres to choose from"), (f"{max(CENTRES[s]['rate'] for s in NEAR)}%", "highest nearby pass rate"), ("£35", "per hour")],
             ["Start lessons with just a provisional licence.", "Book the practical the day you pass your theory.", "Use the official GOV.UK service to find earlier dates.", "Go intensive once your date is set."],
             body, faqs, ["provisional", "theory", "book", "change", "pr_gm"], REL + [("intensive.html", "Intensive", "Intensive driving courses", "Licence in weeks.")])


def overseas():
    path = "driving-lessons-for-overseas-drivers-manchester.html"
    body = """
<p class="lead">Drove for years in Pakistan, India, Nigeria, Iraq, Poland or anywhere else, and now live in Manchester? Whether you can swap your licence or need to pass the UK test depends on where your licence is from — and either way, a few lessons on UK roads make a big difference.</p>
<h2>Can you exchange your licence, or do you need the UK test?</h2>
<ul><li><b>Licences from “designated countries”</b> and the EU/EEA can usually be exchanged for a UK licence — check the list on GOV.UK.</li>
<li><b>Other countries:</b> you can generally drive on your licence for up to 12 months after becoming resident. After that you need a provisional licence and must pass the theory and practical tests.</li>
<li>Full details in our guide: <a href="knowledge/foreign-licence-exchange-uk.html">exchanging a foreign licence in the UK</a>.</li></ul>
<p class="note">Rules change — always check GOV.UK for your country before you rely on your licence.</p>
<h2>What experienced drivers usually need to change</h2>
<ul><li><b>Mirror–signal–manoeuvre</b>, done visibly every time.</li>
<li><b>Roundabouts</b> — UK lane discipline and signalling on multi-lane roundabouts like Kingsway and Princess Parkway.</li>
<li><b>Speed limits and signs</b> in miles per hour, and 20 mph zones across Manchester.</li>
<li><b>Pedestrian crossings, bus lanes and trams.</b></li>
<li><b>Test-style driving</b> — the examiner marks habits that were fine where you learned.</li></ul>
<p>Most experienced drivers need far fewer lessons than a beginner — often a handful of 2-hour lessons and a <a href="services/mock-driving-tests-manchester.html">mock test</a>. We'll tell you honestly after the first lesson.</p>
<h2>Prices</h2><p>£35/hr (2 hours or more), £40 for a single assessment hour. Manual or automatic.</p>
"""
    faqs = [("I have a foreign licence — do I need lessons?", "If you need to pass the UK test, a few lessons focused on UK test standards are strongly recommended — experienced drivers often fail on habits, not skill."),
            ("How many lessons will an experienced driver need?", "Usually far fewer than a beginner. Book a 1-hour assessment (£40) and your instructor will tell you honestly."),
            ("Can I drive in the UK on my foreign licence?", "It depends on the country and how long you've lived here. Check GOV.UK's guidance on driving in Great Britain on a non-GB licence."),
            ("Can you help with the theory test?", "Yes — practise with our free theory quiz and see our theory test guide.")]
    return M(path, "Driving Lessons for Overseas Drivers Manchester | UK Test Ready", "Overseas drivers", ("Overseas drivers", path),
             "Driving lessons for overseas drivers in Manchester.", "Drove abroad? Find out whether you can exchange your licence, then get UK-test-ready with a few focused lessons on Manchester roads.",
             [("12", "months on many foreign licences"), ("£40", "1-hour assessment"), ("£35", "per hour after"), ("Free", "Student Portal")],
             ["Some licences can be exchanged — check GOV.UK for your country.", "Others: up to 12 months, then pass the UK tests.", "Experienced drivers fail on habits, not skill.", "Start with a 1-hour assessment."],
             body, faqs, ["nongb", "exchange", "theory"], REL + [("knowledge/foreign-licence-exchange-uk.html", "Licences", "Exchange a foreign licence", "What's allowed and how.")])


def older():
    path = "driving-lessons-for-older-learners-manchester.html"
    body = """
<p class="lead">There's no upper age limit for learning to drive in the UK. Whether you're 30, 50 or 70 — maybe you never needed a car in Manchester, a partner always drove, or you've just decided it's time — we'll teach you calmly, at your pace, with no judgement.</p>
<h2>What's different when you learn later</h2>
<ul><li><b>You read the road well already</b> — years as a pedestrian and passenger count for a lot.</li>
<li><b>Nerves can be stronger.</b> We start somewhere quiet and only move to busier roads when you're ready. See our <a href="comfort.html">Comfort Zone</a>.</li>
<li><b>Automatic is popular</b> — no clutch to learn, so you can focus on the road. <a href="automatic-driving-lessons-manchester.html">Automatic lessons →</a></li>
<li><b>Two-hour lessons</b> help you settle in rather than rushing.</li></ul>
<h2>Before your first lesson</h2>
<ul><li>A <b>provisional licence</b> (apply on GOV.UK).</li>
<li>Your <b>eyesight</b>: you must be able to read a number plate from 20 metres, with glasses or contact lenses if you need them. <a href="driving/eyesight-test-20-metres.html">Check how far 20 metres is →</a></li>
<li>Tell us about anything that affects your driving — we'll plan around it.</li></ul>
<h2>Prices</h2><p>£35/hr (2 hours or more), £40 for a single hour, £350 for 10 hours — or £320 for NHS staff and learners in M16, M18 and M19.</p>
"""
    faqs = [("Am I too old to learn to drive?", "No. There's no upper age limit in the UK — you need a provisional licence and to meet the eyesight standard."),
            ("Is automatic easier for older learners?", "Many find it easier because there's no clutch or gears, but an automatic licence only covers automatic cars."),
            ("Can I go slowly?", "Yes. We start on quiet roads and you set the pace."),
            ("Do I need to tell DVLA about a medical condition?", "Some conditions must be reported to DVLA — check GOV.UK, and tell your instructor so lessons can be planned around it.")]
    return M(path, "Driving Lessons for Older Learners Manchester | Never Too Late", "Learning later", ("Older learners", path),
             "Driving lessons for older learners in Manchester.", "30, 50 or 70 — there's no upper age limit. Calm, patient lessons at your pace, manual or automatic, with door-to-door pick-up.",
             [("No", "upper age limit"), ("20 m", "eyesight standard"), ("£35", "per hour"), ("Free", "Student Portal")],
             ["No upper age limit to learn.", "Quiet roads first, at your pace.", "Automatic is popular — no clutch.", "Eyesight: read a number plate at 20 metres."],
             body, faqs, ["provisional", "eyesight", "lessons"], REL + [("comfort.html", "Comfort", "Nervous about driving?", "Our Comfort Zone.")])


def all_pages():
    return {PILLAR: pillar(), "driving-instructors-manchester.html": instructors(), "female-driving-instructor-manchester.html": female(),
            "evening-weekend-driving-lessons-manchester.html": evenings(), "pass-driving-test-fast-manchester.html": fast(),
            "driving-lessons-for-overseas-drivers-manchester.html": overseas(), "driving-lessons-for-older-learners-manchester.html": older()}
