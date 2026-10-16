"""Shared page shell for the learner toolkit, test-route guides and driving-test fault guides.

Every page gets: hero with stats, key points, a table of contents, the hand-written body, a 60-second booking
wizard that sends straight to the DriveSQ admin, the DriveSQ Student/Instructor Portal promo, FAQ (with schema),
sources, and related links. The footer (with the SQ Websites credit) comes from layout.page()."""
import re
from layout import *
import pages_research as RS
import pages_book as K

UPDATED = RS.UPDATED
UPDATED_ISO = RS.UPDATED_ISO
ROOT = "../"


def booking_block(heading="Book a lesson in 60 seconds", sub="Tell us what you need — it goes straight to the SQ Driving School team at DriveSQ and a real person replies, usually within the hour."):
    return f"""<section class="section section--alt" id="book"><div class="container" style="max-width:900px">
<div class="section__head center"><div class="eyebrow">Book with SQ · part of DriveSQ</div><h2 data-split>{heading}</h2><p class="lead">{sub}</p></div>
{K.wizard_html().replace('href="privacy.html"', 'href="../privacy.html"')}
<p class="note center mt-2">£35/hr manual or automatic · 10 hours £350 (£320 for NHS staff, students and M16/M18/M19) · free DriveSQ Student Portal with every lesson.</p>
</div></section>"""


def wm_portals():
    return f"""<div class="rx-portals" data-stagger=".08"><div class="rx-portal" data-reveal="up"><div class="eyebrow">Free with every SQ lesson</div><h3>DriveSQ Student Portal</h3>
<p>Every SQ Driving School learner — in Solihull as well as Greater Manchester — gets the DriveSQ Student Portal free, so you always know exactly how close you are to test standard.</p>
<ul><li>23 driving skills tracked after every lesson</li><li>Theory library and 50-question mock tests</li><li>Test-readiness checklist and instructor messaging</li></ul>
<div class="btn-row"><a class="btn btn--red btn--sm" href="{ROOT}student-portal.html">How it works</a><a class="btn btn--ghost btn--sm" href="{RS.STUDENT_PORTAL}" target="_blank" rel="noopener">Student login ↗</a></div></div>
<div class="rx-portal" data-reveal="up" data-delay=".1"><div class="eyebrow">Instructors wanted · Solihull</div><h3>DriveSQ Instructor Portal</h3>
<p>DriveSQ is growing in Solihull and taking on more ADIs. New learners are matched to you by postcode, and your whole diary runs in the DriveSQ Instructor Portal.</p>
<ul><li>New Solihull learners matched by postcode</li><li>Bookings, progress and messaging in one place</li><li>Part of DriveSQ — an established Manchester driving school</li></ul>
<div class="btn-row"><a class="btn btn--red btn--sm" href="https://www.drivesq.co.uk/driving-instructor-jobs-solihull.html">Teach in Solihull</a><a class="btn btn--ghost btn--sm" href="{RS.INSTRUCTOR_PORTAL}" target="_blank" rel="noopener">Instructor login ↗</a></div></div></div>"""


def schema(path, title, desc, faqs, crumbs, kind="Article", extra=None):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (n, href) in enumerate(crumbs):
        items.append({"@type": "ListItem", "position": i + 2, "name": n, "item": SITE + "/" + href})
    out = [
        {"@context": "https://schema.org", "@type": kind, "headline": title, "name": title, "description": desc, "datePublished": UPDATED_ISO, "dateModified": UPDATED_ISO,
         "author": {"@type": "Organization", "name": "SQ Driving School", "url": SITE, "parentOrganization": {"@type": "Organization", "name": "DriveSQ", "url": "https://www.drivesq.co.uk"}},
         "publisher": {"@type": "Organization", "name": "SQ Driving School", "logo": {"@type": "ImageObject", "url": SITE + "/favicon.svg"}},
         "mainEntityOfPage": SITE + "/" + path},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items},
    ]
    if faqs:
        out.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]})
    if extra:
        out += extra
    return out


def shell(path, seo_title, cat, crumbs, title, desc, hero_stats, takeaways, body, faqs, sources, related, side_title="Learn with SQ",
          portal_mode="student", booking_heading=None, kind="Article", extra_schema=None, after_body="", booking_html=None, active="knowledge.html", side_html=None, root=ROOT):
    """crumbs: [(label, href-from-site-root)], last one is this page."""
    body, toc = RS._ids(body)
    mins = RS._minutes(body)
    stats = "".join(f'<div class="rx-stat" data-reveal="up" data-delay="{.08 * i:.2f}"><b>{v}</b><span>{t}</span></div>' for i, (v, t) in enumerate(hero_stats))
    meta = (f'<div class="article-meta" data-reveal="up"><span class="rx-badge"><i></i>{cat}</span><span>Updated {UPDATED}</span><span>{mins} min read</span>'
            f'<span>By SQ Driving School · part of DriveSQ</span></div><div class="rx-stats">{stats}</div>')
    tk = "".join(f"<li>{t}</li>" for t in takeaways)
    toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    faq_html = "".join(f"<details><summary>{q}</summary><div>{a}</div></details>" for q, a in faqs)
    src = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n, u in sources)
    rel = "".join(f'<a class="rx-study" href="{ROOT}{h}" data-reveal="up"><span class="k-cat">{c}</span><h3>{t}</h3><p>{d}</p></a>' for h, c, t, d in related)
    cr = [f'<a href="{ROOT}{h}">{n}</a>' for n, h in crumbs[:-1]] + [crumbs[-1][0]]
    html = page_hero(cat, title, desc, cr, ROOT, meta)
    html += f"""<section class="section--tight"><div class="container article-grid">
  <article>
    <div class="takeaways" data-reveal="up"><h3>Key points</h3><ul>{tk}</ul></div>
    <div class="prose">{body}
      {wm_portals() if portal_mode == "wm" else RS._portals(portal_mode).replace('href="become-a-driving', 'href="../research/become-a-driving')}
      {after_body}
      <h2 id="faq">Frequently asked questions</h2><div class="faq">{faq_html}</div>
      <h2 id="sources">Sources</h2><ul class="sources">{src}</ul>
      <p class="note">Published by SQ Driving School, a brand owned and managed by DriveSQ. Checked on {UPDATED}. Rules, fees and test centres change — always confirm on GOV.UK before you book.</p>
    </div>
  </article>
  <aside>
    <nav class="toc" aria-label="On this page"><h4>On this page</h4><ol>{toc_html}<li><a href="#faq">FAQ</a></li><li><a href="#book">Book a lesson</a></li></ol></nav>
    <div class="card mt-2"><span class="rx-badge" style="color:var(--red);background:var(--red-soft)"><i></i>SQ · DriveSQ</span><h3 style="font-size:1.1rem;margin-top:10px">{side_title}</h3>{side_html or f'<p>£35/hr manual or automatic · 10 hours £350 (£320 NHS, students, M16/M18/M19) · free DriveSQ Student Portal.</p><a class="btn btn--red btn--block" href="#book">{icon("calendar")} Book in 60 seconds</a>'}<a class="btn btn--ghost btn--block mt-1" href="https://wa.me/{WA}" data-wa="Hi SQ Driving School! I found you on {title}." target="_blank" rel="noopener">{icon('wa')} WhatsApp us</a></div>
  </aside>
</div></section>
{booking_html or (booking_block(booking_heading) if booking_heading else booking_block())}
<section class="section"><div class="container"><div class="section__head"><div class="eyebrow">Keep reading</div><h2 data-split>Related guides.</h2></div><div class="grid grid--3" data-stagger=".06">{rel}</div></div></section>
{cta(ROOT)}
<link rel="stylesheet" href="{ROOT}assets/css/research.css"><script src="{ROOT}assets/js/research.js" defer></script>"""
    if root == "":
        html = html.replace('href="../', 'href="').replace('src="../', 'src="')
    return page(path, seo_title, desc, html, root, active=active, schema=schema(path, title, desc, faqs, crumbs, kind, extra_schema))


def hub_page(path, seo_title, eyebrow, title, desc, cards, intro_html="", stats=None):
    """cards: [(href-from-root, cat, title, blurb, icon)] — hubs live at the site root."""
    st = ""
    if stats:
        st = '<div class="rx-stats">' + "".join(f'<div class="rx-stat" data-reveal="up" data-delay="{.08 * i:.2f}"><b>{v}</b><span>{t}</span></div>' for i, (v, t) in enumerate(stats)) + "</div>"
    meta = f'<div class="article-meta" data-reveal="up"><span class="rx-badge"><i></i>{eyebrow}</span><span>Updated {UPDATED}</span><span>By SQ Driving School · part of DriveSQ</span></div>{st}'
    body = page_hero(eyebrow, title, desc, [eyebrow], "", meta)
    cs = "".join(f'<a class="rx-study" href="{h}" data-reveal="up"><div class="card__icon">{icon(ic)}</div><span class="k-cat">{c}</span><h3>{t}</h3><p>{b}</p></a>' for h, c, t, b, ic in cards)
    body += f"""<section class="section--tight"><div class="container">{intro_html}<div class="grid grid--3" data-stagger=".05">{cs}</div>
<div class="mt-3">{RS._portals("both").replace('href="../', 'href="').replace('href="become-a-driving', 'href="research/become-a-driving')}</div></div></section>
{booking_block().replace('href="../', 'href="')}
{cta("")}
<link rel="stylesheet" href="assets/css/research.css"><script src="assets/js/research.js" defer></script>"""
    sch = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": title, "description": desc, "url": f"{SITE}/{path}",
            "hasPart": [{"@type": "WebPage", "name": t, "url": f"{SITE}/{h}"} for h, c, t, b, ic in cards]}]
    return page(path, seo_title, desc, body, "", active="knowledge.html", schema=sch)


def road(no, name, note, tags=()):
    cls = " is-m" if no.startswith("M") else (" is-b" if no.startswith("B") else "")
    badge = f'<span class="rt-road__no{cls}">{no}</span>' if no else '<span class="rt-road__no is-b">Local</span>'
    t = "".join(f"<span>{x}</span>" for x in tags)
    return f'<div class="rt-road" data-reveal="up">{badge}<h4>{name}</h4><p>{note}</p>{f"<div class=rt-tags>{t}</div>" if t else ""}</div>'


def mistakes(items):
    return '<div class="rt-mistakes">' + "".join(f'<div class="rt-mistake" data-reveal="up"><h4>{h}</h4><p>{p}</p><p class="rt-fix">{f}</p></div>' for h, p, f in items) + "</div>"


def landmarks(items):
    return '<div class="rt-marks" data-stagger=".04">' + "".join(f'<div class="rt-mark" data-reveal="up"><b>{n}</b><small>{d}</small></div>' for n, d in items) + "</div>"


def feedback_form(centre):
    return f"""<form class="rx-tool rt-fb" data-rx="feedback" data-centre="{centre}" novalidate data-reveal="up">
  <div class="rx-tool__head"><div class="card__icon">{icon('chat')}</div><div><h3>Taken your test at {centre}? Tell us how it went.</h3><p>Pass or fail, your feedback helps the next learner. It goes privately to the SQ Driving School team — we never publish names, and we only add feedback to this guide after checking it.</p></div></div>
  <div class="rx-row"><div><label for="fbname">First name</label><input class="input" id="fbname" name="fbname" autocomplete="given-name" maxlength="40" required></div>
  <div><label for="fbresult">Result</label><select class="input" id="fbresult" name="fbresult" required><option value="">Choose…</option><option>Passed</option><option>Passed with 0 faults</option><option>Failed — serious fault</option><option>Failed — dangerous fault</option><option>Test cancelled / didn't go ahead</option><option>Haven't taken it yet</option></select></div>
  <div><label for="fbwhen">Month of test</label><input class="input" id="fbwhen" name="fbwhen" type="month"></div>
  <div><label for="fbgear">Car</label><select class="input" id="fbgear" name="fbgear"><option>Manual</option><option>Automatic</option></select></div>
  <div><label for="fbfault">Hardest part / main fault</label><input class="input" id="fbfault" name="fbfault" maxlength="80" placeholder="e.g. right turn at a roundabout"></div>
  <div><label for="fbphone">Phone (optional — for a free debrief call)</label><input class="input" id="fbphone" name="fbphone" type="tel" autocomplete="tel" maxlength="20"></div></div>
  <div class="mt-2"><label for="fbtext">What happened? Roads, junctions, manoeuvres, the examiner's advice…</label><textarea id="fbtext" name="fbtext" maxlength="800" required></textarea></div>
  <button class="btn btn--red mt-2" type="submit">{icon('chat')} Send my feedback</button>
  <p class="js-fbmsg" aria-live="polite"></p>
</form>"""


def radial_map(centre, spokes):
    """Animated, schematic (not-to-scale) diagram of roads radiating from the test centre."""
    import math
    n = len(spokes)
    parts = ['<circle class="rt-ring" cx="300" cy="170" r="80"/><circle class="rt-ring" cx="300" cy="170" r="140"/>']
    for i, (label, direction) in enumerate(spokes):
        a = -math.pi / 2 + i * 2 * math.pi / n
        x, y = 300 + 150 * math.cos(a), 170 + 130 * math.sin(a)
        tx, ty = 300 + 205 * math.cos(a), 170 + 150 * math.sin(a)
        anchor = "middle" if abs(math.cos(a)) < .3 else ("start" if math.cos(a) > 0 else "end")
        parts.append(f'<line class="rt-spoke" x1="300" y1="170" x2="{x:.0f}" y2="{y:.0f}" style="animation-delay:{i * .2:.1f}s"/><circle class="rt-dot" cx="{x:.0f}" cy="{y:.0f}" r="5"/>'
                     f'<text x="{tx:.0f}" y="{ty + 4:.0f}" text-anchor="{anchor}">{label}</text>')
        if direction:
            parts.append(f'<text x="{tx:.0f}" y="{ty + 22:.0f}" text-anchor="{anchor}" style="fill:var(--grey);font-weight:500;font-size:14px">{direction}</text>')
    parts.append(f'<circle class="rt-centre" cx="300" cy="170" r="16"/><circle cx="300" cy="170" r="9" fill="#fff"/><text x="300" y="206" text-anchor="middle" style="font-size:16px">{centre} test centre</text>')
    return f'<figure class="rt-map" data-reveal="up"><svg viewBox="-60 -10 720 370" role="img" aria-label="Schematic of main roads around {centre} driving test centre">{"".join(parts)}</svg><figcaption class="note center">Schematic only — not to scale. Roads shown are the main routes out of the area around the test centre.</figcaption></figure>'
