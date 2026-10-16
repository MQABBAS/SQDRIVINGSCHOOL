"""SQ Driving Data Lab — original, data-led research pages for SQ Driving School (a DriveSQ brand).

Hand-written studies, each built around a dataset: our own sun-position calculations for Manchester, DVSA test and
instructor figures, Department for Transport casualty data and Census 2021. Every figure is cited on the page."""
import json, re
from layout import *
import research_sun as SUN

UPDATED = "16 October 2026"
UPDATED_ISO = "2026-10-16"
ROOT = "../"
STUDENT_PORTAL = "https://www.drivesq.co.uk/student.html"
INSTRUCTOR_PORTAL = "https://www.drivesq.co.uk/dashboard.html"

SRC = {
    "noaa": ("NOAA Global Monitoring Laboratory — solar position calculator (the algorithm we used)", "https://gml.noaa.gov/grad/solcalc/"),
    "metoffice": ("Met Office — location-specific long-term climate averages", "https://www.metoffice.gov.uk/research/climate/maps-and-data/location-specific-long-term-averages"),
    "dvsa_centre": ("DVSA — car driving test data by test centre (GOV.UK statistical data set)", "https://www.gov.uk/government/statistical-data-sets/car-driving-test-data-by-test-centre"),
    "mm2025": ("Mancunian Matters — Where in Greater Manchester are you most likely to fail your driving test? (DVSA figures, April 2024–March 2025)", "https://www.mancunianmatters.co.uk/news/08072025-where-in-greater-manchester-are-you-most-likely-to-fail-your-driving-test/"),
    "passrates_gm": ("passrates.uk — Driving test centres in Greater Manchester, 2024-25", "https://passrates.uk/counties/greater-manchester"),
    "test_cost": ("GOV.UK — Driving test cost (theory and practical)", "https://www.gov.uk/driving-test-cost"),
    "book": ("GOV.UK — Book your driving test", "https://www.gov.uk/book-driving-test"),
    "adi": ("GOV.UK — Become a driving instructor", "https://www.gov.uk/become-driving-instructor"),
    "adi_data": ("DVSA — Approved driving instructor (ADI) qualifying test data", "https://www.gov.uk/government/statistical-data-sets/approved-driving-instructor-adi-qualifying-test-data"),
    "passrates_guide": ("passrates.uk — UK driving test statistics 2026 (ADI Part 3 pass rate)", "https://passrates.uk/guide/driving-test-statistics-uk-2026"),
    "dft_young": ("Department for Transport — Reported road casualties Great Britain: younger and older car drivers factsheet, 2025", "https://www.gov.uk/government/statistics/reported-road-casualties-great-britain-older-and-younger-driver-factsheets/reported-road-casualties-in-great-britain-younger-and-older-car-drivers-factsheet-2025"),
    "commons": ("House of Commons Library — Road safety for young drivers (CDP-2025-0021)", "https://commonslibrary.parliament.uk/research-briefings/cdp-2025-0021/"),
    "new_drivers": ("GOV.UK — Penalty points (endorsements), including the rules for new drivers", "https://www.gov.uk/penalty-points-endorsements"),
    "gmca_cars": ("Greater Manchester Combined Authority — Census 2021 car availability briefing", "https://greatermanchester-ca.gov.uk/media/9704/car-availability-gmca-census-2021-briefing-final.pdf"),
    "mcc_census": ("Manchester City Council — Census 2021 overview", "https://www.manchester.gov.uk/info/500388/census_2021/8622/census_2021_-_overview/5"),
    "rac": ("RAC Foundation — Car and van availability (Census 2021)", "https://www.racfoundation.org/media-centre/car-van-availability"),
    "ons_ts045": ("Office for National Statistics — Census 2021 TS045: Car or van availability", "https://www.ons.gov.uk/datasets/TS045/editions/2021/versions/1"),
}

STUDIES = [
    ("best-time-to-take-driving-test-manchester", "Daylight & glare", "The best time of year to take your driving test in Manchester", "sun", "7h 29m", "of daylight on the shortest day"),
    ("driving-test-pass-rates-explained-manchester", "Pass rates", "Manchester driving test pass rates, explained with real odds", "flag", "20.9 pts", "between Bolton and Bury"),
    ("become-a-driving-instructor-manchester", "Careers", "Becoming a driving instructor in Greater Manchester: the real route, costs and maths", "car", "£603", "minimum DVSA fees to qualify"),
    ("young-driver-road-safety-data", "Road safety", "Young drivers and road safety: what 20 years of DfT data shows", "shield", "−75%", "young driver deaths since 2004"),
    ("greater-manchester-driving-statistics", "By the numbers", "Driving in Greater Manchester by the numbers (2026)", "chart", "27%", "of GM households have no car"),
]


def _cites(keys):
    return [SRC[k] for k in keys]


def _ids(body):
    toc = []

    def rep(m):
        text = re.sub("<[^>]+>", "", m.group(1))
        hid = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
        toc.append((hid, text))
        return f'<h2 id="{hid}">{m.group(1)}</h2>'
    return re.sub(r"<h2>(.*?)</h2>", rep, body), toc


def _minutes(html):
    return max(3, round(len(re.sub("<[^>]+>", " ", html).split()) / 200))


def _bars(rows, unit="%", maxv=100):
    out = ""
    for label, sub, val, kind in rows:
        w = max(1.5, val / maxv * 100)
        out += (f'<div class="rx-bar"><div class="rx-bar__lbl"><b>{label}</b>{f"<small>{sub}</small>" if sub else ""}</div>'
                f'<div class="rx-bar__track"><span class="rx-bar__fill {kind}" style="--w:{w:.1f}%"></span></div><div class="rx-bar__val">{(f"{val:,}" if float(val).is_integer() else f"{val:g}")}{unit}</div></div>')
    return f'<div class="rx-bars" data-reveal="up">{out}</div>'


def _figs(items):
    return '<div class="rx-figs" data-stagger=".06">' + "".join(
        f'<div class="rx-fig" data-reveal="up"><b>{v}</b><span>{t}</span>{f"<small>{s}</small>" if s else ""}</div>' for v, t, s in items) + "</div>"


def _portals(mode="both"):
    student = f"""<div class="rx-portal" data-reveal="up"><div class="eyebrow">Free with every SQ lesson</div><h3>DriveSQ Student Portal</h3>
<p>Every SQ Driving School learner gets the DriveSQ Student Portal free — so you always know where you stand, not just how many hours you've had.</p>
<ul><li>23 driving skills tracked after every lesson</li><li>Theory library and 50-question mock tests</li><li>Test-readiness checklist and instructor messaging</li></ul>
<div class="btn-row"><a class="btn btn--red btn--sm" href="{ROOT}student-portal.html">How it works</a><a class="btn btn--ghost btn--sm" href="{STUDENT_PORTAL}" target="_blank" rel="noopener">Student login ↗</a></div></div>"""
    instructor = f"""<div class="rx-portal" data-reveal="up" data-delay=".1"><div class="eyebrow">For instructors</div><h3>DriveSQ Instructor Portal</h3>
<p>Instructors who teach with DriveSQ and SQ Driving School run their whole diary from one place — and get new learners matched to them by postcode.</p>
<ul><li>Pupils, lesson bookings and progress in one dashboard</li><li>Message pupils and record skills after each lesson</li><li>New learners assigned from DriveSQ's own booking system</li></ul>
<div class="btn-row"><a class="btn btn--red btn--sm" href="become-a-driving-instructor-manchester.html">Teach with DriveSQ</a><a class="btn btn--ghost btn--sm" href="{INSTRUCTOR_PORTAL}" target="_blank" rel="noopener">Instructor login ↗</a></div></div>"""
    if mode == "student":
        return f'<div class="rx-portals" data-stagger=".08">{student}<div class="rx-portal" data-reveal="up" data-delay=".1"><div class="eyebrow">Part of DriveSQ</div><h3>Why SQ Driving School?</h3><p>SQ Driving School is owned and managed by DriveSQ — the Greater Manchester driving school behind the Student and Instructor Portals.</p><ul><li>Manual &amp; automatic, same price: £35/hr</li><li>10 hours £350 — £320 for NHS staff, students and M16/M18/M19</li><li>Door-to-door pick-up across Greater Manchester</li></ul><div class="btn-row"><a class="btn btn--red btn--sm" href="{ROOT}book.html">Book in 60 seconds</a><a class="btn btn--ghost btn--sm" href="https://www.drivesq.co.uk" target="_blank" rel="noopener">DriveSQ ↗</a></div></div></div>'
    return f'<div class="rx-portals" data-stagger=".08">{student}{instructor}</div>'


def _cite_box(title, path):
    ref = f"SQ Driving School (DriveSQ). \"{title}\". SQ Driving Data Lab, {UPDATED}. {SITE}/{path}"
    return f'<div class="rx-cite" data-rx="cite"><b>Using this data?</b> You&#39;re welcome to quote or chart these figures — please credit SQ Driving School with a link to this page.<code>{ref}</code><button class="btn btn--ghost btn--sm" type="button">Copy citation</button></div>'


def _schema(title, desc, path, faqs, dataset=None):
    out = [
        {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "datePublished": UPDATED_ISO, "dateModified": UPDATED_ISO,
         "author": {"@type": "Organization", "name": "SQ Driving School", "url": SITE, "parentOrganization": {"@type": "Organization", "name": "DriveSQ", "url": "https://www.drivesq.co.uk"}},
         "publisher": {"@type": "Organization", "name": "SQ Driving School", "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/icon-512.png"}},
         "mainEntityOfPage": SITE + "/" + path, "about": "Learning to drive in Greater Manchester"},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Driving Data Lab", "item": SITE + "/research.html"},
            {"@type": "ListItem", "position": 3, "name": title, "item": SITE + "/" + path}]},
    ]
    if dataset:
        out.append({"@context": "https://schema.org", "@type": "Dataset", "name": dataset[0], "description": dataset[1], "url": SITE + "/" + path,
                    "creator": {"@type": "Organization", "name": "SQ Driving School", "url": SITE}, "license": "https://creativecommons.org/licenses/by/4.0/",
                    "spatialCoverage": {"@type": "Place", "name": "Greater Manchester, England"}, "dateModified": UPDATED_ISO, "isAccessibleForFree": True})
    return out


SEO_TITLES = {
    "best-time-to-take-driving-test-manchester": "Best Time to Take Your Driving Test in Manchester (Data)",
    "driving-test-pass-rates-explained-manchester": "Manchester Driving Test Pass Rates and Your Real Odds",
    "become-a-driving-instructor-manchester": "How to Become a Driving Instructor in Manchester (2026)",
    "young-driver-road-safety-data": "Young Driver Road Safety Statistics: 20 Years of DfT Data",
    "greater-manchester-driving-statistics": "Greater Manchester Driving Statistics 2026 | SQ Data Lab",
}


def _shell(slug, cat, title, desc, hero_stats, takeaways, body, faqs, src_keys, method, dataset=None, portal_mode="both"):
    path = f"research/{slug}.html"
    body, toc = _ids(body)
    mins = _minutes(body)
    stats = "".join(f'<div class="rx-stat" data-reveal="up" data-delay="{.08 * i:.2f}"><b>{v}</b><span>{t}</span></div>' for i, (v, t) in enumerate(hero_stats))
    meta = (f'<div class="article-meta" data-reveal="up"><span class="rx-badge"><i></i>SQ Driving Data Lab</span><span>Published {UPDATED}</span><span>{mins} min read</span>'
            f'<span>By SQ Driving School · part of DriveSQ</span></div><div class="rx-stats">{stats}</div>')
    tk = "".join(f"<li>{t}</li>" for t in takeaways)
    toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    faq_html = "".join(f"<details><summary>{q}</summary><div>{a}</div></details>" for q, a in faqs)
    src = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in _cites(src_keys))
    others = "".join(f'<a class="rx-study" href="{s[0]}.html" data-reveal="up"><span class="rx-study__num">0{i + 1}</span><span class="k-cat">{s[1]}</span><h3>{s[2]}</h3><div class="rx-kpi">{s[4]}<small>{s[5]}</small></div></a>'
                     for i, s in enumerate(STUDIES) if s[0] != slug)
    html = page_hero(cat, title, desc, [f'<a href="{ROOT}research.html">Driving Data Lab</a>', cat], ROOT, meta)
    html += f"""<section class="section--tight"><div class="container article-grid">
  <article>
    <div class="takeaways" data-reveal="up"><h3>Key findings</h3><ul>{tk}</ul></div>
    <div class="prose">{body}
      {_portals(portal_mode)}
      <div class="rx-method" data-reveal="up"><h3>How we worked this out</h3>{method}</div>
      {_cite_box(title, path)}
      <h2 id="faq">Frequently asked questions</h2><div class="faq">{faq_html}</div>
      <h2 id="sources">Sources</h2><ul class="sources">{src}</ul>
      <p class="note">Published by SQ Driving School, a brand owned and managed by DriveSQ. Figures were checked on {UPDATED}; official statistics are revised over time, so always check GOV.UK before booking.</p>
    </div>
  </article>
  <aside>
    <nav class="toc" aria-label="On this page"><h4>On this page</h4><ol>{toc_html}<li><a href="#faq">FAQ</a></li><li><a href="#sources">Sources</a></li></ol></nav>
    <div class="card mt-2"><span class="rx-badge" style="color:var(--red);background:var(--red-soft)"><i></i>Data Lab</span><h3 style="font-size:1.1rem;margin-top:10px">Learn with SQ</h3><p>£35/hr manual or automatic · 10 hours £350 (£320 NHS, students, M16/M18/M19) · free DriveSQ Student Portal.</p><a class="btn btn--red btn--block" href="{ROOT}book.html">{icon('calendar')} Book in 60 seconds</a></div>
  </aside>
</div></section>
<section class="section section--alt"><div class="container"><div class="section__head"><div class="eyebrow">More from the Data Lab</div><h2 data-split>Other studies.</h2></div><div class="grid grid--2" data-stagger=".06">{others}</div>
<div class="center mt-3"><a class="btn btn--ghost" href="{ROOT}research.html">All Data Lab studies {icon('arrow')}</a></div></div></section>
{cta(ROOT)}
<link rel="stylesheet" href="{ROOT}assets/css/research.css"><script src="{ROOT}assets/js/research.js" defer></script>"""
    return page(path, SEO_TITLES.get(slug, title), desc, html, ROOT, active="knowledge.html", schema=_schema(title, desc, path, faqs, dataset))


# ---------------------------------------------------------------- study 1: daylight & glare
def _verdict(m):
    sr, ss = m["sunrise"], m["sunset"]
    if m["noon_elev"] < 20:
        return (f"<b>Short, low-sun days.</b> The sun rises at {sr}, sets at {ss} and never climbs above {m['noon_elev']:.0f}° — glare is possible all day, "
                f"and the last tests of the day finish close to dusk ({m['dusk']}). Wet, dark roads are normal: practise them before test day.")
    if m["glare_am_min"] + m["glare_pm_min"] > 150:
        return (f"<b>Glare season.</b> Low sun on the morning run ({m['glare_am'] or '—'}) and the afternoon ({m['glare_pm'] or '—'}). Daylight is fine ({sr}–{ss}), "
                f"but book a time that avoids driving straight into a low sun if glare bothers you.")
    if m["glare_am_min"] + m["glare_pm_min"] > 40:
        return (f"<b>A balanced month.</b> Long enough days ({sr}–{ss}) and only short glare windows ({m['glare_am'] or 'none in the morning'}"
                f"{', ' + m['glare_pm'] if m['glare_pm'] else ''}). Most test slots are in clear daylight.")
    return (f"<b>Maximum daylight.</b> Sunrise {sr}, sunset {ss}; the sun is high for every test slot and glare is limited to very early mornings. "
            f"Demand is often highest around school and university holidays, so book early.")


def study_daylight():
    ms = SUN.months()
    ex = SUN.extra()
    names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for m in ms:
        m["verdict"] = _verdict(m)
    js = json.dumps([{k: m[k] for k in ("sunrise", "sunset", "dawn", "dusk", "daylight_min", "glare_am", "glare_pm", "glare_am_min", "glare_pm_min", "verdict")} for m in ms])
    sh, lo = ex["shortest"], ex["longest"]
    hm = lambda x: f"{x // 60}h {x % 60:02d}m"
    rows = "".join(
        f'<tr><td><b>{names[i]}</b> <small class="note">{m["clock"]}</small></td><td class="mono">{m["sunrise"]}</td><td class="mono">{m["sunset"]}</td><td class="mono">{m["dusk"]}</td>'
        f'<td class="mono">{hm(m["daylight_min"])}</td><td class="mono">{m["noon_elev"]:.0f}°</td><td class="mono">{m["glare_am"] or "—"}</td><td class="mono">{m["glare_pm"] or "—"}</td>'
        f'<td>{"<span class=rx-hot>Dark</span>" if m["dark_1730"] else "<span class=rx-ok>Light</span>"}</td></tr>' for i, m in enumerate(ms))
    jump = (int(ex["before_change"]["dusk"][:2]) * 60 + int(ex["before_change"]["dusk"][3:])) - (int(ex["after_change"]["dusk"][:2]) * 60 + int(ex["after_change"]["dusk"][3:]))
    glare_rows = [(names[i][:3], f'{m["glare_am"] or "no morning glare"}', m["glare_am_min"] + m["glare_pm_min"], "") for i, m in enumerate(ms)]
    worst = max(ms, key=lambda m: m["glare_am_min"] + m["glare_pm_min"])
    worst_name = names[ms.index(worst)]
    dec = ms[11]
    body = f"""
<p class="lead">Most advice about <em>when</em> to take your driving test is guesswork. So we did the maths. Using the same solar-position formulas the US National Oceanic and Atmospheric Administration (NOAA) publishes, we calculated sunrise, sunset, dusk, the sun's height and — the part nobody talks about — the exact windows when a <b>low sun</b> sits in a driver's eyeline across Manchester, for every month of the year.</p>
<p>The result is a month-by-month picture of the conditions you'll actually drive in on test day. It doesn't change the test (the examiner marks the same skills in July and December), but it changes how hard those skills feel — and it should change how you practise.</p>

<h2>Explore any month</h2>
<div class="rx-tool" data-rx="sun" data-reveal="up" data-months='{js.replace("'", "&#39;")}'>
  <div class="rx-tool__head"><div class="card__icon">{icon('clock')}</div><div><h3>Manchester daylight &amp; low-sun explorer</h3><p>Pick a month — the bar shows a full 24 hours on the 15th of that month (UK clock time).</p></div></div>
  <div class="rx-chips" role="group" aria-label="Choose a month"></div>
  <div class="rx-day" role="img" aria-label="24-hour daylight bar"></div>
  <div class="rx-hours"><span>00:00</span><span>06:00</span><span>12:00</span><span>18:00</span><span>24:00</span></div>
  <div class="rx-legend"><span><i style="background:#ffc457"></i>Daylight</span><span><i style="background:#6b5aa6"></i>Civil twilight</span><span><i style="background:repeating-linear-gradient(135deg,#ff4d00 0 4px,#ffa000 4px 8px)"></i>Low-sun glare (sun 0.5°–15°, 07:00–10:00 &amp; 15:00–19:00)</span><span><i style="border:2px dashed var(--grey);background:none"></i>Typical test hours</span></div>
  <div class="rx-out"><div><b class="js-sunrise">—</b><span>Sunrise</span></div><div><b class="js-sunset">—</b><span>Sunset</span></div><div><b class="js-dusk">—</b><span>Dark (civil dusk)</span></div><div class="rx-big"><b class="js-glare">—</b><span>Low-sun glare in commute hours</span></div></div>
  <p class="mt-2 mb-0 js-verdict" aria-live="polite"></p>
  <p class="rx-note">Daylight: <span class="js-daylight"></span>. Calculated for Manchester city centre (53.48°N, 2.24°W). Times move by a minute or two across Greater Manchester.</p>
</div>

<h2>The full year in one table</h2>
<p>Here's every month side by side. "Dark at 17:30" tells you whether the last lessons of a winter school day, or a late-afternoon practice drive, will be in the dark.</p>
<div class="rx-table-wrap" data-reveal="up"><table class="rx-table"><thead><tr><th>Month (15th)</th><th>Sunrise</th><th>Sunset</th><th>Dark from</th><th>Daylight</th><th>Sun at noon</th><th>Morning glare</th><th>Afternoon glare</th><th>17:30</th></tr></thead><tbody>{rows}</tbody></table></div>

<h2>Finding 1: December's sun never gets above {dec['noon_elev']:.0f}°</h2>
<p>On 15 December the sun peaks at just <b>{dec['noon_elev']:.1f}° above the horizon</b> over Manchester. That's below our 15° "low sun" threshold all day long — so in December and much of January, dazzle isn't confined to rush hour. A sun that low sits directly behind traffic lights and on the far side of wet, reflective roads.</p>
<p>The shortest day, <b>21 December</b>, gives you only <b>{hm(sh['daylight_min'])}</b> of daylight (sunrise {sh['sunrise']}, sunset {sh['sunset']}). The longest, <b>21 June</b>, gives <b>{hm(lo['daylight_min'])}</b> (sunrise {lo['sunrise']}, sunset {lo['sunset']}). Same city, same test — more than double the daylight.</p>
{_figs([(hm(sh['daylight_min']), "Daylight on the shortest day (21 Dec)", "Our calculation"), (hm(lo['daylight_min']), "Daylight on the longest day (21 Jun)", "Our calculation"), (f"{dec['noon_elev']:.0f}°", "Highest the sun climbs on 15 December", "Below the 15° glare line all day"), (f"{jump} min", "Earlier darkness overnight when the clocks go back (25 Oct 2026)", f"Dusk {ex['before_change']['dusk']} → {ex['after_change']['dusk']}")])}

<h2>Finding 2: glare peaks in {worst_name}, not midwinter</h2>
<p>You might expect December to be the worst month for glare. It isn't — at least not in the hours most people drive. In <b>{worst_name}</b> the low sun overlaps both the morning (<b>{worst['glare_am'] or '—'}</b>) and the afternoon (<b>{worst['glare_pm'] or '—'}</b>) windows for a combined <b>{worst['glare_am_min'] + worst['glare_pm_min']} minutes</b>. In midwinter the sun rises later and sets before many people head home, so it spends less of the commute in your eyes.</p>
<p>Minutes of low-sun glare inside the 07:00–10:00 and 15:00–19:00 windows, on the 15th of each month:</p>
{_bars(glare_rows, " min", max(r[2] for r in glare_rows))}
<p>Direction matters too. In December the sun rises in the <b>south-east (about {dec['rise_az']}°)</b> and sets in the <b>south-west (about {dec['set_az']}°)</b>; in June it rises far to the north-east ({ms[5]['rise_az']}°) and sets in the north-west ({ms[5]['set_az']}°). So a winter-morning drive heading south-east — think the A6 towards Stockport, or the A34 towards Cheadle — puts the sun straight through the windscreen.</p>

<h2>Finding 3: the clocks going back costs you {jump} minutes overnight</h2>
<p>On Saturday 24 October 2026 it's dark in Manchester from <b>{ex['before_change']['dusk']}</b>. On Monday 26 October it's dark from <b>{ex['after_change']['dusk']}</b>. If you've only ever practised in light evenings, the first week after the clocks change is a good time to book an extra lesson that finishes in the dark — headlight use, judging speed at junctions and spotting pedestrians in dark clothing all feel different.</p>
<p>British Summer Time starts again on <b>28 March 2027</b> and ends on <b>31 October 2027</b>.</p>

<h2>So when should you book?</h2>
<p>There's no "easy" month — the examiner applies the same standard all year. But if you have a choice:</p>
<ul class="ticks">
<li><span><b>April to August</b> gives the most daylight and the least glare during typical test hours. It's also when holiday demand is high, so book well ahead (see our <a href="{ROOT}knowledge/driving-test-waiting-times-greater-manchester.html">waiting-times guide</a>).</span></li>
<li><span><b>March and September</b> are a sweet spot: 12–13 hours of daylight, short glare windows, and roads busy enough to be realistic.</span></li>
<li><span><b>October to February</b> is perfectly passable — thousands of people pass every winter — but practise low sun, wet roads and dark evenings first, and pick a mid-morning slot if glare bothers you.</span></li>
</ul>
<div class="callout"><b>The honest answer:</b> the best time to take your test is when you're consistently driving at test standard — not a particular month. That's exactly what the test-readiness checklist in the DriveSQ Student Portal is for.</div>

<h2>How SQ lessons prepare you for any season</h2>
<p>With SQ Driving School your instructor plans lessons around the conditions you'll face: a dusk lesson after the clocks change, a low-sun drive in October and November, and wet-road practice whenever Manchester obliges. Every skill is logged in your <b>DriveSQ Student Portal</b>, so you and your instructor can see when you're ready — whatever month your test is in.</p>
"""
    faqs = [
        ("What is the best month to take a driving test in Manchester?", "Based on our daylight and sun-position calculations, April to August offer the most daylight and the least low-sun glare in typical test hours, with March and September a good balance. The test standard is the same all year, so the best month is when you're consistently test-ready."),
        ("Is it harder to pass a driving test in winter?", "The marking is identical, but conditions are tougher: in Manchester the shortest day has under 7½ hours of daylight and the December sun never rises above about 13°, so glare and dark, wet roads are common. Practise those conditions before your test."),
        ("When is sun glare worst for drivers in Manchester?", f"In our calculations, {worst_name} has the most low-sun glare in the 07:00–10:00 and 15:00–19:00 windows, because the low sun overlaps both commutes. In midwinter the sun is low all day but spends less time in commute hours."),
        ("How much earlier does it get dark when the clocks go back?", f"In Manchester, dusk moves from {ex['before_change']['dusk']} on 24 October 2026 to {ex['after_change']['dusk']} on 26 October 2026 — about {jump} minutes earlier overnight."),
        ("Do driving tests go ahead in the dark?", "Yes. Tests run through the winter, and late-afternoon tests in December and January can finish around dusk. Driving tests are only cancelled for genuinely dangerous conditions such as snow or ice."),
    ]
    method = f"""<p>We implemented the NOAA solar-position algorithm (the same maths behind NOAA's online solar calculator) for Manchester city centre (53.4808°N, 2.2426°W) and ran it minute by minute for the 15th of every month, plus the solstices and the October 2026 clock change, applying UK daylight saving rules. Sunrise and sunset use the standard −0.833° sun-centre altitude (allowing for refraction and the sun's size); "dark" is the end of civil twilight (sun 6° below the horizon). We define <b>low-sun glare</b> as the sun being between 0.5° and 15° above the horizon during 07:00–10:00 or 15:00–19:00 — roughly when it's low enough to sit inside a driver's field of view. "Typical test hours" (08:00–16:00) are approximate. Times are accurate to about a minute.</p>"""
    return _shell("best-time-to-take-driving-test-manchester", "Daylight & glare", "The best time of year to take your driving test in Manchester",
                  "We calculated sunrise, sunset, dusk and low-sun glare for every month in Manchester. Here's what it means for your driving test — and when to book.",
                  [(hm(sh['daylight_min']), "daylight on 21 December"), (hm(lo['daylight_min']), "daylight on 21 June"), (f"{dec['noon_elev']:.0f}°", "highest December sun"), (f"{jump} min", "earlier dark after the clocks change")],
                  [f"The December sun never climbs above about {dec['noon_elev']:.0f}° over Manchester — low enough to cause glare all day.",
                   f"Commute-hour glare peaks in {worst_name} ({worst['glare_am_min'] + worst['glare_pm_min']} minutes a day), not in midwinter.",
                   f"When the clocks go back on 25 October 2026, it gets dark about {jump} minutes earlier overnight.",
                   "April–August gives the most daylight and least glare in test hours; March and September are a good balance.",
                   "The test standard never changes — practise the conditions of the month you'll test in."],
                  body, faqs, ["noaa", "metoffice", "book", "dvsa_centre"], method,
                  dataset=("Manchester daylight and low-sun glare by month", "Sunrise, sunset, civil dusk, solar noon elevation and low-sun glare windows for Manchester city centre on the 15th of each month, calculated by SQ Driving School with the NOAA solar-position algorithm."),
                  portal_mode="student")


# ---------------------------------------------------------------- study 2: pass rates & odds
def _wilson(x, n, z=1.96):
    import math
    p = x / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (c - h) * 100, (c + h) * 100


def study_pass_rates():
    import math
    BOL = (3250, 5548)
    BUR = (1643, 4355)
    NAT = 48.5
    pb, pu = BOL[0] / BOL[1] * 100, BUR[0] / BUR[1] * 100
    lb, hb = _wilson(*BOL)
    lu, hu = _wilson(*BUR)
    pp = (BOL[0] + BUR[0]) / (BOL[1] + BUR[1])
    z = (pb - pu) / 100 / math.sqrt(pp * (1 - pp) * (1 / BOL[1] + 1 / BUR[1]))
    within = lambda p, n: (1 - (1 - p / 100) ** n) * 100
    fee = 62
    body = f"""
<p class="lead">Pass-rate league tables are everywhere. What they don't tell you is what a pass rate actually <em>means</em> for you — how many attempts to expect, how much it could cost, and whether the gap between two test centres is real or just noise. We took the official DVSA counts for two Greater Manchester centres at opposite ends of the table and ran the numbers properly.</p>

<h2>Bolton vs Bury: the same county, a 21-point gap</h2>
<p>Between April 2024 and March 2025, DVSA figures reported by Mancunian Matters show:</p>
{_figs([(f"{pb:.1f}%", f"Bolton: {BOL[0]:,} passes from {BOL[1]:,} tests", "Highest in Greater Manchester"), (f"{pu:.1f}%", f"Bury: {BUR[0]:,} passes from {BUR[1]:,} tests", "Among the lowest"), (f"{NAT}%", "Great Britain average over the same period", "As reported"), (f"{pb - pu:.1f} pts", "Gap between the two centres", f"z = {z:.1f} — not chance")])}
{_bars([("Bolton", f"95% range {lb:.1f}–{hb:.1f}%", round(pb, 1), "rx-bar__fill--green"), ("Great Britain", "2024-25 average", NAT, "rx-bar__fill--grey"), ("Bury", f"95% range {lu:.1f}–{hu:.1f}%", round(pu, 1), "")])}
<p>Is the gap real? With more than 5,500 tests at Bolton and 4,300 at Bury, the 95% confidence ranges ({lb:.1f}–{hb:.1f}% and {lu:.1f}–{hu:.1f}%) don't come close to overlapping. A two-proportion test gives z ≈ {z:.1f} — a difference that size essentially never happens by chance. The centres really do produce different results.</p>
<p>Across Greater Manchester as a whole, independent site passrates.uk puts the 2024-25 average at around 50.1%, slightly above its 48.7% UK figure — but individual centres range from the high 30s to the high 50s and beyond.</p>

<h2>What a pass rate means in attempts</h2>
<p>A pass rate is <em>passes per test</em>, not per person. If you treat each attempt as having the same chance (a simplification — people usually improve after a fail), the maths is simple: expected attempts = 1 ÷ pass rate.</p>
<div class="rx-table-wrap" data-reveal="up"><table class="rx-table"><thead><tr><th>Centre</th><th>Pass rate</th><th>Expected attempts</th><th>Chance within 2 tests</th><th>Chance within 3 tests</th><th>Expected test fees*</th></tr></thead><tbody>
<tr><td><b>Bolton</b></td><td class="mono rx-ok">{pb:.1f}%</td><td class="mono">{100 / pb:.2f}</td><td class="mono">{within(pb, 2):.1f}%</td><td class="mono">{within(pb, 3):.1f}%</td><td class="mono">£{fee * 100 / pb:.0f}</td></tr>
<tr><td><b>GB average</b></td><td class="mono">{NAT}%</td><td class="mono">{100 / NAT:.2f}</td><td class="mono">{within(NAT, 2):.1f}%</td><td class="mono">{within(NAT, 3):.1f}%</td><td class="mono">£{fee * 100 / NAT:.0f}</td></tr>
<tr><td><b>Bury</b></td><td class="mono rx-hot">{pu:.1f}%</td><td class="mono">{100 / pu:.2f}</td><td class="mono">{within(pu, 2):.1f}%</td><td class="mono">{within(pu, 3):.1f}%</td><td class="mono">£{fee * 100 / pu:.0f}</td></tr>
</tbody></table></div>
<p class="note">*Weekday practical test fee of £{fee} multiplied by expected attempts. It excludes lessons, car hire and travel — which usually cost far more than the fee itself.</p>

<h2>Try it: your own pass odds</h2>
<div class="rx-tool" data-rx="odds" data-fee="{fee}" data-reveal="up">
  <div class="rx-tool__head"><div class="card__icon">{icon('target')}</div><div><h3>Pass-odds calculator</h3><p>Drag the pass rate — or pick a centre — to see your cumulative chance of passing.</p></div></div>
  <div class="rx-chips" role="group" aria-label="Presets"><button type="button" data-rate="{pb:.1f}">Bolton {pb:.1f}%</button><button type="button" data-rate="{NAT}">GB average {NAT}%</button><button type="button" data-rate="{pu:.1f}">Bury {pu:.1f}%</button></div>
  <label class="label" for="rxRate">Pass rate: <b class="js-rate">—</b></label>
  <input class="rx-range" id="rxRate" type="range" min="20" max="80" step="0.1" value="{NAT}">
  <div class="rx-odds" aria-live="polite">{''.join(f'<div><b>—</b><i></i><span>Within {k} test{"s" if k > 1 else ""}</span></div>' for k in range(1, 6))}</div>
  <div class="rx-out"><div class="rx-big"><b class="js-exp">—</b><span>Expected attempts</span></div><div><b class="js-w2">—</b><span>Pass within 2 tests</span></div><div><b class="js-w3">—</b><span>Pass within 3 tests</span></div><div><b class="js-cost">—</b><span>Expected test fees</span></div></div>
  <p class="rx-note">Assumes each attempt has the same chance. In reality your odds rise after each test as you fix the faults on your report.</p>
</div>

<h2>Why do centres differ so much?</h2>
<p>A low pass rate doesn't mean examiners are harsher. The DVSA trains every examiner to the same standard. The differences come from the roads and the people:</p>
<ul class="ticks">
<li><span><b>Road layout.</b> Centres with complex multi-lane roundabouts, bus lanes, tram crossings or fast dual carriageways nearby simply give candidates more chances to make a serious fault. Our <a href="{ROOT}knowledge/greater-manchester-driving-test-centres.html">test centre guides</a> describe each one.</span></li>
<li><span><b>Who tests there.</b> Centres serving lots of first-time candidates, people who booked before they were ready, or people re-testing quickly after a fail will have lower rates.</span></li>
<li><span><b>Traffic at test times.</b> Congested routes create more hazards per mile — more decisions, more chances to hesitate or misjudge.</span></li>
<li><span><b>Readiness, above all.</b> The biggest single factor is whether the candidate was genuinely test-ready. That's the one you control.</span></li>
</ul>

<h2>Should you travel to an "easier" centre?</h2>
<p>Booking a higher-pass-rate centre across Greater Manchester is allowed — there are no catchment areas. But it often backfires: you'll be tested on roads you don't know, and your instructor may not have taught there. A learner who knows the Bury roads well is usually a safer bet at Bury than at a centre they've never driven around. Read <a href="{ROOT}knowledge/test-centre-bolton.html">our Bolton guide</a> and <a href="{ROOT}knowledge/test-centre-bury.html">our Bury guide</a> for what each route is like.</p>
<div class="callout"><b>What actually moves your odds:</b> mock tests in test conditions, fixing every fault on your last report, and only booking when you can drive the full route without your instructor stepping in. The DriveSQ Student Portal's readiness checklist tracks exactly that.</div>

<h2>How SQ Driving School gets you test-ready</h2>
<p>SQ Driving School (part of DriveSQ) teaches on the roads around every Greater Manchester test centre. Your instructor logs all 23 core skills in the <b>DriveSQ Student Portal</b> after each lesson, so you can see which ones are test-standard and which still need work — and you'll do at least one full mock test before your real one.</p>
"""
    faqs = [
        ("What is the driving test pass rate in Greater Manchester?", f"It varies by centre. DVSA figures for April 2024–March 2025 put Bolton at {pb:.1f}% and Bury at {pu:.1f}%, against a Great Britain average of {NAT}%. Independent site passrates.uk estimates the Greater Manchester average at about 50.1% for 2024-25."),
        ("Which Greater Manchester test centre has the highest pass rate?", f"In the April 2024–March 2025 DVSA figures reported by Mancunian Matters, Bolton had the highest pass rate in Greater Manchester at {pb:.1f}% ({BOL[0]:,} passes from {BOL[1]:,} tests)."),
        ("How many attempts does it take to pass a driving test?", f"At the {NAT}% Great Britain average, the expected number of attempts is about {100 / NAT:.1f}, and roughly {within(NAT, 2):.0f}% of people would pass within two tests if every attempt had the same chance. In practice most people improve after a fail."),
        ("Is the difference between test centres statistically significant?", f"Yes. Bolton's and Bury's 95% confidence ranges ({lb:.1f}–{hb:.1f}% and {lu:.1f}–{hu:.1f}%) don't overlap, and a two-proportion z-test gives z ≈ {z:.1f}, far beyond chance."),
        ("Should I book a test centre with a higher pass rate?", "You can book any centre, but being tested on unfamiliar roads often cancels out any advantage. It's usually better to test where you've learned and practised."),
    ]
    method = f"""<p>We used the test and pass counts for Bolton ({BOL[0]:,}/{BOL[1]:,}) and Bury ({BUR[0]:,}/{BUR[1]:,}) for April 2024–March 2025, as published from DVSA data by Mancunian Matters, and the {NAT}% Great Britain average quoted alongside them. 95% confidence ranges use the Wilson score interval; the significance test is a pooled two-proportion z-test. "Expected attempts" and "chance within <i>n</i> tests" assume every attempt has the same pass probability (a geometric model) — real candidates usually improve between attempts, so treat these as a conservative baseline. Expected fees use the £{fee} weekday practical test fee. We only used centres where we could verify both counts.</p>"""
    return _shell("driving-test-pass-rates-explained-manchester", "Pass rates", "Manchester driving test pass rates, explained with real odds",
                  "DVSA figures show a 21-point gap between Bolton and Bury. We turned pass rates into the numbers that matter: expected attempts, odds and cost — with a calculator.",
                  [(f"{pb:.1f}%", "Bolton pass rate 2024-25"), (f"{pu:.1f}%", "Bury pass rate 2024-25"), (f"{100 / NAT:.2f}", "expected attempts at the GB average"), (f"z = {z:.0f}", "the gap is not chance")],
                  [f"Bolton passed {pb:.1f}% of tests and Bury {pu:.1f}% in April 2024–March 2025 — a {pb - pu:.1f}-point gap.",
                   "The gap is statistically decisive: the 95% confidence ranges don't overlap.",
                   f"At the {NAT}% GB average you'd expect about {100 / NAT:.1f} attempts; at Bury about {100 / pu:.1f}.",
                   "Pass rates reflect roads and candidates, not harsher examiners — every examiner works to the same standard.",
                   "Being genuinely test-ready moves your odds far more than which centre you pick."],
                  body, faqs, ["mm2025", "dvsa_centre", "passrates_gm", "test_cost", "book"], method,
                  dataset=("Bolton and Bury driving test pass rates with confidence intervals", "Pass rates, 95% Wilson confidence intervals, expected attempts and expected test fees for Bolton and Bury driving test centres, April 2024–March 2025."),
                  portal_mode="student")


# ---------------------------------------------------------------- study 3: becoming an instructor
def study_instructor():
    fees = [("Part 1 — theory &amp; hazard perception", 81, "Required"), ("Part 2 — test of driving ability", 111, "Required"), ("Part 3 — test of instructional ability", 111, "Required"),
            ("ADI registration (green badge, 4 years)", 300, "Required"), ("Trainee licence (pink badge, 6 months)", 140, "Optional"), ("Enhanced DBS criminal record check", None, "Required — price varies")]
    req = sum(f[1] for f in fees if f[1] and f[2] == "Required")
    rows = "".join(f'<tr><td>{n}</td><td class="mono">{"£" + str(v) if v else "varies"}</td><td>{t}</td></tr>' for n, v, t in fees)
    body = f"""
<p class="lead">Thinking about teaching people to drive in Greater Manchester? Most "become an instructor" pages are adverts for training courses. This one is the honest version: the official route, every DVSA fee, the bits that catch people out, and a calculator so you can model what you'd actually take home — with your real numbers, not ours.</p>

<h2>The route to the green badge</h2>
<p>To teach driving for money in Great Britain you must be a DVSA <b>Approved Driving Instructor (ADI)</b>. You'll need to have held a full licence for at least three years, pass a background check, and then pass three tests:</p>
<ol class="rx-steps" data-reveal="up">
<li data-n="1"><h4>Part 1: theory and hazard perception <span class="tag">£81</span></h4><p>100 multiple-choice questions in four bands — you need at least 85 overall and at least 20 in each band — plus a hazard perception test with a pass mark of 57 out of 75. Passing Part 1 starts a <b>two-year clock</b> to finish Parts 2 and 3.</p></li>
<li data-n="2"><h4>Part 2: your own driving <span class="tag">£111</span></h4><p>An eyesight check and about an hour of driving to a much higher standard than the learner test: no more than six driving faults, and no serious or dangerous ones. You get <b>three attempts</b>.</p></li>
<li data-n="3"><h4>Optional: trainee licence <span class="tag">£140</span></h4><p>After Part 2 and at least 40 hours of training, you can apply for a six-month "pink badge" to teach paying pupils while you prepare for Part 3 — a popular way to earn and build experience at the same time.</p></li>
<li data-n="4"><h4>Part 3: your teaching <span class="tag">£111</span></h4><p>An examiner watches you give a real lesson for about an hour and marks you out of 51 across lesson planning, risk management and teaching and learning strategies. You need at least 31 overall and at least 8 for risk management; 43 or more is grade A. Again, <b>three attempts</b>.</p></li>
<li data-n="5"><h4>Register and qualify <span class="tag">£300</span></h4><p>Pay the registration fee for your green ADI badge, valid for four years. From then on you'll take a periodic standards check to stay on the register.</p></li>
</ol>
<div class="callout"><b>The rule that catches people out:</b> you must pass Parts 2 and 3 within two years of passing Part 1, with three attempts at each. Run out of attempts or time and you start again from Part 1.</div>

<h2>What it costs: every DVSA fee</h2>
<div class="rx-table-wrap" data-reveal="up"><table class="rx-table"><thead><tr><th>Item</th><th>Fee</th><th></th></tr></thead><tbody>{rows}
<tr><td><b>Minimum official fees to qualify (one attempt at each part)</b></td><td class="mono rx-hot">£{req}</td><td>Excludes DBS, training and car</td></tr></tbody></table></div>
<p>The official fees are the cheap part. Most of the real cost is <b>training</b> (from independent trainers or training providers) and, for Parts 2 and 3, access to a suitable car. Retakes mean paying the test fee again. Budget for the training you'll actually need — many people underestimate Part 3.</p>
{_figs([("£" + str(req), "Minimum DVSA fees to qualify", "Parts 1–3 + registration"), ("2 years", "To pass Parts 2 and 3 after Part 1", "DVSA rule"), ("3", "Attempts each at Parts 2 and 3", "DVSA rule"), ("~28%", "Recent ADI Part 3 pass rate", "passrates.uk, 2025-26")])}

<h2>Part 3 is where most people stall</h2>
<p>Part 3 is the hardest step by a distance. Independent analysis of DVSA data puts the recent Part 3 pass rate at around <b>28%</b> — far below the roughly 50% learner pass rate. The reason is simple: being a good driver and being a good <em>teacher</em> are different skills. The examiner wants to see you set goals with a real pupil, manage risk, adapt when things change and let the pupil do the learning.</p>
<p>The DVSA publishes quarterly pass rates for all three parts in its ADI qualifying test data — worth checking before you start, so you know what you're signing up for.</p>

<h2>Model your earnings</h2>
<p>Instructor income depends almost entirely on three things: your hourly rate, how many hours you actually fill, and your costs. Change the numbers below to match your situation — the defaults use SQ Driving School's standard £35 an hour.</p>
<div class="rx-tool" data-rx="earn" data-reveal="up">
  <div class="rx-tool__head"><div class="card__icon">{icon('calc')}</div><div><h3>Driving instructor earnings calculator</h3><p>An illustration only — put in your own figures.</p></div></div>
  <div class="rx-row">
    <div><label for="ea">Hourly lesson rate (£)</label><input class="input" id="ea" name="rate" type="number" min="0" step="1" value="35"></div>
    <div><label for="eb">Paid hours per week</label><input class="input" id="eb" name="hours" type="number" min="0" step="1" value="30"></div>
    <div><label for="ec">Working weeks per year</label><input class="input" id="ec" name="weeks" type="number" min="0" max="52" step="1" value="46"></div>
    <div><label for="ed">Car lease + insurance (£/week)</label><input class="input" id="ed" name="car" type="number" min="0" step="1" value="90"></div>
    <div><label for="ee">Fuel per lesson hour (£)</label><input class="input" id="ee" name="fuel" type="number" min="0" step="0.5" value="3"></div>
    <div><label for="ef">Franchise / school fee (£/week)</label><input class="input" id="ef" name="fee" type="number" min="0" step="1" value="0"></div>
  </div>
  <div class="rx-out"><div><b class="js-gross">—</b><span>Lesson income a year</span></div><div><b class="js-costs">—</b><span>Running costs a year</span></div><div class="rx-big"><b class="js-net">—</b><span>Before tax</span></div><div><b class="js-hourly">—</b><span>Per paid hour</span></div></div>
  <p class="rx-note">Before income tax and National Insurance. Doesn't include training, equipment, phone, marketing, or unpaid time between lessons. These are your assumptions, not DriveSQ figures.</p>
</div>
<p>The number that matters most is <b>paid hours</b>. An empty diary costs the same as a full one — which is why where your pupils come from is the most important decision you'll make after qualifying.</p>

<h2>Teaching with DriveSQ and SQ Driving School</h2>
<p>SQ Driving School is a brand owned and managed by <b>DriveSQ</b>, a Greater Manchester driving school built around its own technology. Instructors who work with DriveSQ get:</p>
<ul class="ticks">
<li><span><b>Pupils matched to you by postcode.</b> Learners book through the DriveSQ and SQ Driving School websites; DriveSQ's own matching system ranks instructors by distance, gearbox and coverage area and assigns them.</span></li>
<li><span><b>The DriveSQ Instructor Portal.</b> Your pupils, bookings and lesson history in one dashboard, with messaging and skill tracking after every lesson.</span></li>
<li><span><b>Pupils who arrive organised.</b> Every learner gets the DriveSQ Student Portal, so they can see their 23 skills, revise theory and know what's next.</span></li>
<li><span><b>Flexible ways to work.</b> Talk to us about referral or franchise arrangements, your hours and the areas you want to cover.</span></li>
</ul>
<div class="btn-row mt-2"><a class="btn btn--red" href="https://www.drivesq.co.uk/#join" target="_blank" rel="noopener">Apply to teach with DriveSQ ↗</a><a class="btn btn--ghost" data-wa="Hi! I'm a driving instructor (or training to be one) and I'd like to teach with DriveSQ / SQ Driving School." href="https://wa.me/{WA}">{icon('wa')} Ask on WhatsApp</a></div>
"""
    faqs = [
        ("How much does it cost to become a driving instructor in the UK?", f"The DVSA fees are £81 for Part 1, £111 for Part 2, £111 for Part 3 and £300 to register — at least £{req} for one attempt at each, plus a DBS check. The optional trainee licence is £140. Training and car costs are usually much larger than the fees."),
        ("How long do you have to pass the ADI tests?", "You must pass Parts 2 and 3 within two years of passing Part 1, and you get three attempts at each of Parts 2 and 3. Otherwise you must start again from Part 1."),
        ("What is the ADI Part 3 pass rate?", "Recent independent analysis of DVSA data puts the Part 3 pass rate at around 28% for 2025-26. The DVSA publishes official quarterly pass rates for all three parts."),
        ("Can I teach while I'm training to be an instructor?", "Yes — after passing Part 2 and completing at least 40 hours of training you can apply for a six-month trainee licence (£140) and teach paying pupils while you prepare for Part 3."),
        ("How do I get pupils as a new driving instructor in Manchester?", "Many new instructors join a school that supplies pupils. DriveSQ and SQ Driving School match learners to instructors by postcode and give instructors the DriveSQ Instructor Portal to manage them."),
    ]
    method = """<p>The route, attempt limits and fees come from GOV.UK's "Become a driving instructor" guidance. The Part 3 pass rate is from passrates.uk's 2026 analysis of DVSA's ADI qualifying test data; the DVSA publishes the official quarterly figures (tables DRT511, DRT521) on GOV.UK. The DBS fee varies by provider, so we haven't quoted one. The earnings calculator is a simple model — lesson income (rate × paid hours × weeks) minus weekly car and franchise costs over 52 weeks and fuel per lesson hour. Every input is yours to change, and none of the defaults are DriveSQ earnings figures.</p>"""
    return _shell("become-a-driving-instructor-manchester", "Careers", "Becoming a driving instructor in Greater Manchester: the real route, costs and maths",
                  "The honest guide to becoming an ADI in Greater Manchester: every DVSA fee, the two-year rule, Part 3 pass rates and an earnings calculator — plus teaching with DriveSQ.",
                  [(f"£{req}", "minimum DVSA fees"), ("2 years", "to pass Parts 2 & 3"), ("3", "attempts at Parts 2 & 3"), ("~28%", "recent Part 3 pass rate")],
                  [f"Minimum DVSA fees to qualify are £{req} (Parts 1–3 plus registration), before DBS, training and car costs.",
                   "You must pass Parts 2 and 3 within two years of Part 1, with three attempts at each.",
                   "Part 3 — the teaching test — is the hardest step, with a recent pass rate of around 28%.",
                   "A trainee licence (£140) lets you teach paying pupils for six months while preparing for Part 3.",
                   "Filled hours drive income — DriveSQ matches learners to instructors by postcode via the Instructor Portal."],
                  body, faqs, ["adi", "adi_data", "passrates_guide"], method, portal_mode="both")


# ---------------------------------------------------------------- study 4: young driver safety
def study_safety():
    k04, s04, k24, s24 = 330, 3481, 84, 1297
    dk = round((1 - k24 / k04) * 100)
    ds = round((1 - s24 / s04) * 100)
    body = f"""
<p class="lead">Passing your test is the start, not the finish. The Department for Transport's own figures show that newly qualified young drivers carry a much higher risk than everyone else on the road — but also that the picture has improved dramatically in 20 years. Here's what the data says, and what it means for how you should learn.</p>

<h2>Twenty years of progress</h2>
<p>The DfT's latest factsheet on younger car drivers (aged 17–24) compares casualties among young drivers themselves in 2004 and today:</p>
{_figs([(str(k24), "Young car drivers killed (latest year)", f"Down from {k04} in 2004"), (f"{s24:,}", "Young car drivers seriously injured", f"Down from {s04:,} in 2004"), (f"−{dk}%", "Fall in young driver deaths since 2004", "Our calculation from DfT figures"), (f"−{ds}%", "Fall in serious injuries since 2004", "Our calculation from DfT figures")])}
{_bars([("Killed, 2004", "young car drivers", k04, "rx-bar__fill--grey"), ("Killed, latest year", "young car drivers", k24, "")], "", k04)}
{_bars([("Seriously injured, 2004", "young car drivers", s04, "rx-bar__fill--grey"), ("Seriously injured, latest", "young car drivers", s24, "")], "", s04)}
<p>Better cars, better roads and better training have all played a part. But {k24} deaths and {s24:,} serious injuries a year are still {k24} families and {s24:,} lives changed — and young drivers remain over-represented.</p>

<h2>Why young drivers are still at higher risk</h2>
<ul class="ticks">
<li><span><b>About a fifth of serious casualties.</b> In 2023 a young driver was involved in around one in five of all killed or seriously injured casualties from collisions involving cars — far more than their share of drivers or miles driven.</span></li>
<li><span><b>Young men especially.</b> Male drivers aged 17–24 were around <b>four times</b> as likely to be killed or seriously injured while driving as car drivers aged 25 and over.</span></li>
<li><span><b>Per mile, not just per head.</b> Young (and the oldest) drivers have higher killed-or-seriously-injured rates per mile driven than drivers in the middle age groups — so it isn't just that they drive more.</span></li>
</ul>
<p>Research into young driver collisions consistently points to the same pressure points: <b>inexperience</b> spotting hazards early, <b>night-time driving</b>, <b>carrying friends as passengers</b>, <b>speed</b> and fast <b>rural roads</b>. None of these is fully tested in a 40-minute driving test — which is exactly why how you learn matters.</p>

<h2>The New Drivers Act: six points and you're out</h2>
<p>For your first two years after passing, the rules are stricter. If you build up <b>six or more penalty points</b> within two years of passing your test, your licence is revoked and you go back to being a learner — provisional licence, theory test and practical test all over again. One mobile-phone offence (six points) is enough on its own.</p>
<div class="callout"><b>Quick maths:</b> a speeding fine is usually 3 points. Two of them in your first two years and you're re-sitting your theory test.</div>

<h2>What the data means for how you learn</h2>
<p>The test measures a minimum standard on one day. The DfT figures are a reminder that real safety comes from experience in the conditions where young drivers get hurt. With SQ Driving School, that means:</p>
<ul class="ticks">
<li><span><b>Dark and low-light driving</b> before you pass — especially after the clocks change (see our <a href="best-time-to-take-driving-test-manchester.html">daylight study</a>).</span></li>
<li><span><b>Fast roads and dual carriageways</b> such as the M60 and A-roads around Greater Manchester, so speed and merging aren't new after your test.</span></li>
<li><span><b>Hazard perception that goes beyond the theory test</b> — try our <a href="{ROOT}hazard-game.html">spot-the-hazard game</a>.</span></li>
<li><span><b>Honest progress tracking</b> in the DriveSQ Student Portal, so you book your test when you're ready, not just when a slot appears.</span></li>
</ul>
<p>After your test, our <a href="{ROOT}knowledge/after-you-pass-new-driver-guide.html">new driver's guide</a> covers your first months on the road, and <a href="{ROOT}knowledge/learner-driver-insurance.html">our insurance guide</a> explains how telematics policies reward safe driving.</p>
"""
    faqs = [
        ("How many young drivers are killed on UK roads each year?", f"The Department for Transport's latest younger driver factsheet records {k24} car drivers aged 17–24 killed and {s24:,} seriously injured, down from {k04} and {s04:,} in 2004."),
        ("Are young drivers more likely to crash?", "Yes. In 2023 a young driver (17–24) was involved in around a fifth of all killed or seriously injured casualties from collisions involving cars, and young male drivers were about four times as likely to be killed or seriously injured as drivers aged 25 and over."),
        ("What happens if you get 6 points in your first 2 years of driving?", "Under the New Drivers Act your licence is revoked. You have to apply for a new provisional licence and pass both the theory and practical tests again."),
        ("How can new drivers reduce their risk?", "Get experience in the conditions linked to young driver collisions — dark roads, fast roads, bad weather and driving with passengers — before and after passing, keep speed down and never use a phone while driving."),
    ]
    method = f"""<p>Casualty counts for car drivers aged 17–24 (killed {k04} → {k24}; seriously injured {s04:,} → {s24:,}) are from the Department for Transport's "Reported road casualties Great Britain: younger and older car drivers factsheet, 2025". The "around a fifth" and "four times as likely" figures are 2023 findings reported in the DfT factsheet series and summarised by the House of Commons Library. The percentage falls are our own calculation. These are Great Britain-wide figures; the DfT doesn't publish this young-driver breakdown for Greater Manchester alone.</p>"""
    return _shell("young-driver-road-safety-data", "Road safety", "Young drivers and road safety: what 20 years of DfT data shows",
                  f"Young driver deaths are down {dk}% since 2004, but 17–24-year-olds still face far higher risk. What the Department for Transport data shows — and how to learn safer.",
                  [(f"−{dk}%", "young driver deaths since 2004"), (f"−{ds}%", "serious injuries since 2004"), ("1 in 5", "serious car casualties involve a young driver"), ("4×", "risk for young male drivers")],
                  [f"Young car drivers killed fell from {k04} in 2004 to {k24} — a {dk}% drop; serious injuries fell {ds}%.",
                   "A young driver was involved in around a fifth of killed-or-seriously-injured casualties from car collisions in 2023.",
                   "Male drivers aged 17–24 are about four times as likely to be killed or seriously injured as drivers aged 25+.",
                   "Six penalty points in your first two years means losing your licence and re-sitting both tests.",
                   "Experience of dark roads, fast roads and passengers before you pass is the best protection."],
                  body, faqs, ["dft_young", "commons", "new_drivers"], method,
                  dataset=("Young car driver casualties in Great Britain, 2004 vs latest", "Killed and seriously injured car drivers aged 17–24 in Great Britain, 2004 and the latest year, with percentage change calculated by SQ Driving School."),
                  portal_mode="student")


# ---------------------------------------------------------------- study 5: GM by the numbers
def study_numbers():
    ex = SUN.extra()
    hm = lambda x: f"{x // 60}h {x % 60:02d}m"
    body = f"""
<p class="lead">How many households in Greater Manchester can't drive anywhere because they don't have a car? How do local test centres compare? What does it actually cost to learn? We've pulled the most useful official numbers about driving in Greater Manchester into one place — each one sourced, and each linked to a deeper study where we have one.</p>

<h2>Car ownership: a city that still needs drivers</h2>
<p>The 2021 Census shows Greater Manchester households are less likely to have a car than the national average — and the gap between boroughs is huge.</p>
{_figs([("27%", "of Greater Manchester households have no car or van", "319,000 households · Census 2021"), ("575,000", "residents live in those car-free households", "GMCA analysis"), ("24%", "England average for households without a car", "Census 2021"), ("73%", "of GM households have a car — up 4 points since 2011", "GMCA analysis")])}
{_bars([("Manchester", "households with no car", 39, ""), ("Greater Manchester", "households with no car", 27, "rx-bar__fill--grey"), ("England", "households with no car", 24, "rx-bar__fill--grey"), ("Trafford", "households with no car", 19, "rx-bar__fill--green")], "%", 45)}
<p>Inside the city of Manchester the contrast is sharper still: in <b>Piccadilly 68%</b> of households have no car, and in some central neighbourhoods more than three-quarters don't. Across Great Britain as a whole, 76.4% of households have at least one car or van.</p>
<p>Why it matters: a quarter of Greater Manchester households depend entirely on public transport, lifts or taxis. For jobs outside the city centre — warehouses, hospitals, shifts that start before the first tram — a licence can be the difference between applying and not. It's one reason we offer an <a href="{ROOT}nhs-driving-lessons.html">NHS staff discount</a> and a <a href="{ROOT}student-driving-lessons-manchester.html">student discount</a>.</p>

<h2>Driving tests: big differences between centres</h2>
{_figs([("58.6%", "Bolton pass rate, Apr 2024–Mar 2025", "3,250 passes / 5,548 tests"), ("37.7%", "Bury pass rate, same period", "1,643 passes / 4,355 tests"), ("48.5%", "Great Britain average, same period", "As reported"), ("~22 wks", "Peak national average wait for a practical test (March 2025)", "As reported")])}
<p>That's a 21-point gap between two centres a few miles apart. We tested whether it's real (it is) and turned the rates into expected attempts and costs in <a href="driving-test-pass-rates-explained-manchester.html">our pass-rate study</a>. For booking strategy, see our <a href="{ROOT}knowledge/driving-test-waiting-times-greater-manchester.html">waiting-times guide</a>.</p>

<h2>Daylight: the conditions you'll test in</h2>
{_figs([(hm(ex['shortest']['daylight_min']), "Daylight on the shortest day in Manchester", f"Sunrise {ex['shortest']['sunrise']} · sunset {ex['shortest']['sunset']}"), (hm(ex['longest']['daylight_min']), "Daylight on the longest day", f"Sunrise {ex['longest']['sunrise']} · sunset {ex['longest']['sunset']}"), (ex['after_change']['dusk'], "Dark from, the Monday after the clocks go back (26 Oct 2026)", f"It was {ex['before_change']['dusk']} two days earlier")])}
<p>All three figures are our own calculations for Manchester city centre. Month-by-month sunrise, sunset and low-sun glare windows are in <a href="best-time-to-take-driving-test-manchester.html">our daylight study</a>.</p>

<h2>What learning costs</h2>
<div class="rx-table-wrap" data-reveal="up"><table class="rx-table"><thead><tr><th>Item</th><th>Cost</th><th>Notes</th></tr></thead><tbody>
<tr><td>Theory test</td><td class="mono">£23</td><td>DVSA fee</td></tr>
<tr><td>Practical test — weekday</td><td class="mono">£62</td><td>DVSA fee</td></tr>
<tr><td>Practical test — evening, weekend or bank holiday</td><td class="mono">£75</td><td>DVSA fee</td></tr>
<tr><td>SQ lessons — manual or automatic</td><td class="mono">£35/hr</td><td>2-hour lessons £70; single 1-hour session £40</td></tr>
<tr><td>SQ 10-hour block</td><td class="mono">£350</td><td><b>£320</b> for NHS staff, students and M16/M18/M19 postcodes</td></tr>
<tr><td>DriveSQ Student Portal</td><td class="mono rx-ok">£0</td><td>Free with every SQ lesson</td></tr>
</tbody></table></div>
<p>For a full budget — including how many hours most learners need — see our <a href="{ROOT}guides/cost-of-learning-to-drive-manchester.html">cost of learning to drive guide</a> and the <a href="{ROOT}tools.html">lesson calculator</a>.</p>

<h2>Young drivers: safer than ever, still the highest risk</h2>
{_figs([("−75%", "Fall in young car drivers killed since 2004", "DfT, 330 → 84"), ("1 in 5", "Killed or seriously injured car casualties involving a young driver (2023)", "DfT / Commons Library"), ("6 points", "Lose your licence within 2 years of passing", "New Drivers Act")])}
<p>The full picture — and what it means for how you learn — is in <a href="young-driver-road-safety-data.html">our young driver safety study</a>.</p>

<h2>Becoming an instructor</h2>
{_figs([("£603", "Minimum DVSA fees to qualify as an ADI", "Parts 1–3 + registration"), ("~28%", "Recent ADI Part 3 pass rate", "passrates.uk"), ("2 years", "To pass Parts 2 & 3 after Part 1", "DVSA rule")])}
<p>See the full route, the maths and how to teach with DriveSQ in <a href="become-a-driving-instructor-manchester.html">our instructor study</a>.</p>
"""
    faqs = [
        ("How many households in Greater Manchester don't have a car?", "Census 2021 shows 27% of Greater Manchester households — about 319,000 households with 575,000 residents — have no car or van, compared with 24% across England."),
        ("Which Greater Manchester borough has the most car-free households?", "Manchester, where 39% of households have no car. Trafford has the fewest at 19%. Within Manchester, 68% of households in Piccadilly have no car."),
        ("How much is the driving test in 2026?", "The DVSA charges £23 for the theory test and £62 for a weekday practical test, or £75 for evenings, weekends and bank holidays."),
        ("How much are driving lessons with SQ Driving School?", "£35 an hour for manual or automatic (2-hour lessons £70), a single 1-hour session £40, or 10 hours for £350 — £320 for NHS staff, students and M16, M18 and M19 postcodes. The DriveSQ Student Portal is free."),
    ]
    method = """<p>Car-ownership figures are from Census 2021 (ONS table TS045) as analysed by the Greater Manchester Combined Authority and Manchester City Council, with the Great Britain total from the RAC Foundation; Census 2021 took place during the pandemic, which may have affected some household patterns. Test-centre counts are DVSA figures for April 2024–March 2025 reported by Mancunian Matters. Daylight figures are our own NOAA-algorithm calculations. Young driver figures are from the DfT's younger driver factsheet; ADI figures are from GOV.UK and passrates.uk. Prices are SQ Driving School's published prices and the DVSA fees on GOV.UK.</p>"""
    return _shell("greater-manchester-driving-statistics", "By the numbers", "Driving in Greater Manchester by the numbers (2026)",
                  "Car ownership by borough, test-centre pass rates, daylight, costs and young driver safety — the key official numbers about driving in Greater Manchester, sourced.",
                  [("27%", "of GM households have no car"), ("39%", "in Manchester"), ("58.6%", "Bolton pass rate"), ("£35/hr", "SQ manual or automatic")],
                  ["27% of Greater Manchester households (319,000) have no car — above the 24% England average.",
                   "Car-free households range from 19% in Trafford to 39% in Manchester, and 68% in Piccadilly.",
                   "Test-centre pass rates range from 37.7% (Bury) to 58.6% (Bolton) for April 2024–March 2025.",
                   "Manchester gets 7h 29m of daylight on the shortest day and 17h 02m on the longest.",
                   "DVSA fees are £23 (theory) and £62/£75 (practical); SQ lessons are £35/hr, Student Portal free."],
                  body, faqs, ["gmca_cars", "mcc_census", "rac", "ons_ts045", "mm2025", "test_cost", "dft_young", "adi", "noaa"], method,
                  dataset=("Driving in Greater Manchester: key statistics 2026", "Car availability by area (Census 2021), driving test pass rates, daylight extremes, driving test fees and young driver casualty figures for Greater Manchester, compiled by SQ Driving School."),
                  portal_mode="both")


# ---------------------------------------------------------------- hub
def hub():
    cards = "".join(f'<a class="rx-study" href="research/{s[0]}.html" data-reveal="up"><span class="rx-study__num">0{i + 1}</span><div class="card__icon">{icon(s[3])}</div><span class="k-cat">{s[1]}</span><h3>{s[2]}</h3><div class="rx-kpi">{s[4]}<small>{s[5]}</small></div></a>'
                    for i, s in enumerate(STUDIES))
    stats = "".join(f'<div class="rx-stat" data-reveal="up" data-delay="{.08 * i:.2f}"><b>{v}</b><span>{t}</span></div>' for i, (v, t) in enumerate([("5", "original studies"), ("23,000+", "minutes of sun positions calculated"), ("100%", "sources cited"), ("CC BY", "free to reuse with credit")]))
    meta = f'<div class="article-meta" data-reveal="up"><span class="rx-badge"><i></i>SQ Driving Data Lab</span><span>Updated {UPDATED}</span><span>By SQ Driving School · part of DriveSQ</span></div><div class="rx-stats">{stats}</div>'
    body = page_hero("Driving Data Lab", "Driving data you won't find anywhere else.",
                     "Original research about learning to drive in Greater Manchester — our own calculations and official statistics, turned into answers you can actually use.", ["Driving Data Lab"], "", meta)
    body += f"""<section class="section--tight"><div class="container">
<div class="grid grid--2" data-stagger=".06">{cards}</div>
<div class="rx-method mt-3" data-reveal="up"><h3>Our approach</h3><p>Every Data Lab study is written by SQ Driving School, part of DriveSQ, and built around a real dataset — either our own calculations (like minute-by-minute sun positions for Manchester) or official statistics from the DVSA, the Department for Transport and the Census. We cite every figure, explain our method, and only publish numbers we can verify. When sources disagree, we tell you. You're welcome to reuse our charts and figures with a link back.</p></div>
{_portals("both")}
</div></section>
{cta("")}
<link rel="stylesheet" href="assets/css/research.css"><script src="assets/js/research.js" defer></script>"""
    desc = "Original research on learning to drive in Greater Manchester: daylight and glare by month, test-centre pass odds, instructor costs, young driver safety and local statistics."
    sch = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "SQ Driving Data Lab", "description": desc, "url": SITE + "/research.html",
            "hasPart": [{"@type": "Article", "headline": s[2], "url": f"{SITE}/research/{s[0]}.html"} for s in STUDIES]}]
    return page("research.html", "SQ Driving Data Lab | Original Driving Research for Greater Manchester", desc, body, "", active="knowledge.html", schema=sch)


def all_pages():
    pages = {"research.html": hub()}
    for fn in (study_daylight, study_pass_rates, study_instructor, study_safety, study_numbers):
        html = fn()
        slug = re.search(r'<link rel="canonical" href="[^"]*/research/([^"]+)\.html"', html).group(1)
        pages[f"research/{slug}.html"] = html
    return pages
