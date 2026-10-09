"""Shared layout for SQ Driving School pages."""
import json

SITE = "https://sqdrivingschool.com"
PHONE = "07352 932003"
TEL = "+447352932003"
WA = "447352932003"
STUDENT = "https://www.drivesq.co.uk/student.html"
INSTRUCTOR = "https://www.drivesq.co.uk/portal.html"

ICONS = {
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "pound": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 20H7c2-2 2-4 2-7V9a4 4 0 0 1 7.5-2M6 13h8"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/><path d="M9 11h6M12 8v6"/></svg>',
    "grad": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 1 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "phone-app": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="5" y="2" width="14" height="20" rx="3"/><path d="M11 18h2"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 6-7"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5v14z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
    "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 17h14v-5l-2-5H7l-2 5z"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/><path d="M5 12h14"/></svg>',
    "auto": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="7" y="3" width="10" height="18" rx="3"/><path d="M12 7v4M10 15h4"/></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="6" cy="6" r="2"/><circle cx="12" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="12" cy="18" r="2"/><path d="M6 8v8M12 8v8M18 8v4H6"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
    "calc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h4"/></svg>',
    "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8S1 12 1 12z"/><circle cx="12" cy="12" r="3"/></svg>',
    "quiz": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3M12 17h.01"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2l10 5-10 5L2 7z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg>',
    "road": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 22L9 2M20 22L15 2M12 4v3M12 11v3M12 18v3"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>',
    "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
    "flag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1zM4 22v-7"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>',
    "tag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}

CAR_TOP = '<svg class="road-rail__car" viewBox="0 0 20 36" aria-hidden="true"><rect x="2" y="2" width="16" height="32" rx="6" fill="#ff1f1f"/><rect x="4.5" y="8" width="11" height="7" rx="2" fill="#111"/><rect x="4.5" y="22" width="11" height="6" rx="2" fill="#111"/><circle cx="5" cy="3.5" r="1.4" fill="#fff"/><circle cx="15" cy="3.5" r="1.4" fill="#fff"/></svg>'

CAR_SIDE = '<svg class="road-strip__car" viewBox="0 0 160 60" aria-hidden="true"><path d="M8 40c0-8 6-12 14-13l18-12c4-3 9-4 14-4h34c6 0 11 2 15 6l12 10 25 4c8 1 12 6 12 12v5H8z" fill="#ff1f1f"/><path d="M46 17l-14 10h34V15H54c-3 0-6 1-8 2zM72 15v12h40L100 18c-3-2-6-3-10-3z" fill="#141418"/><circle cx="40" cy="46" r="11" fill="#0b0b0d" stroke="#555" stroke-width="3"/><circle cx="122" cy="46" r="11" fill="#0b0b0d" stroke="#555" stroke-width="3"/><rect x="146" y="34" width="8" height="5" rx="2" fill="#fff"/><text x="80" y="38" font-family="Russo One, sans-serif" font-style="italic" font-size="12" fill="#fff" text-anchor="middle">SQ</text></svg>'

NAV = [
    ("index.html", "Home", "nav.home"),
    ("lessons.html", "Lessons", "nav.lessons"),
    ("prices.html", "Prices", "nav.prices"),
    ("discounts.html", "Discounts", "nav.discounts"),
    ("comfort.html", "Nervous?", None),
    ("tools.html", "Tools", "nav.tools"),
    ("student-portal.html", "Student Portal", "nav.portal"),
    ("areas.html", "Areas", "nav.areas"),
    ("knowledge.html", "Learn", None),
]

MOBILE_EXTRA = [
    ("book.html", "Book in 60 Seconds"),
    ("automatic-driving-lessons-manchester.html", "Automatic Lessons"),
    ("manual-driving-lessons-manchester.html", "Manual Lessons"),
    ("gift-vouchers.html", "Gift Vouchers"),
    ("nhs-driving-lessons.html", "NHS Staff Discount"),
    ("student-driving-lessons-manchester.html", "Student Discount"),
    ("comfort.html", "Comfort Zone"),
    ("intensive.html", "Intensive Courses"),
    ("first-lesson.html", "Your First Lesson"),
    ("offer-m16-m18-m19.html", "M16 · M18 · M19 Offer"),
    ("postcode-checker.html", "Postcode Checker"),
    ("theory-quiz.html", "Theory Quiz"),
    ("hazard-game.html", "Hazard Game"),
    ("road-signs.html", "Road Sign Flashcards"),
    ("dashboard-lights.html", "Dashboard Lights"),
    ("guides.html", "Learner Guides"),
    ("test-centres.html", "Test Centres"),
    ("contact.html", "Contact"),
    ("driving-lessons-near-me.html", "Lessons Near Me"),
    ("postcodes.html", "All Postcodes"),
    ("services.html", "All Lesson Types"),
    ("faq.html", "FAQ"),
    ("about.html", "About"),
]


WAVE_PATH = "M0,30 C240,70 480,10 720,40 C960,70 1200,10 1440,50 L1440,104 L0,104 Z"


def wave_down():
    """Dark section above -> light page below."""
    return f'<svg class="wave wave--anim" viewBox="0 0 1440 100" preserveAspectRatio="none" aria-hidden="true" style="background:#050506"><path d="{WAVE_PATH}"/></svg>'


def wave_up():
    """Light page above -> dark footer below."""
    return f'<svg class="wave wave--anim" viewBox="0 0 1440 100" preserveAspectRatio="none" aria-hidden="true" style="--wave:#0b0b0d;background:var(--bg)"><path d="{WAVE_PATH}"/></svg>'


def icon(name):
    return ICONS[name]


def wa_url(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"


ORG_SCHEMA = json.dumps([
    {"@context": "https://schema.org", "@type": "Organization", "@id": SITE + "/#org", "name": "SQ Driving School", "url": SITE + "/", "logo": SITE + "/favicon.svg",
     "telephone": "+44 7352 932003", "parentOrganization": {"@type": "Organization", "name": "DriveSQ", "url": "https://www.drivesq.co.uk"},
     "areaServed": "Greater Manchester", "contactPoint": {"@type": "ContactPoint", "telephone": "+44 7352 932003", "contactType": "customer service", "areaServed": "GB", "availableLanguage": "English"}},
    {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "name": "SQ Driving School", "url": SITE + "/", "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en-GB"},
], ensure_ascii=False)


def head(title, desc, path, root, schema=None, noindex=False):
    canon = SITE + "/" + ("" if path == "index.html" else path)
    sch = ""
    if schema:
        for s in schema:
            sch += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + "</script>\n"
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<!-- Google tag (gtag.js) with Consent Mode v2: analytics stays off until the visitor accepts -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('consent', 'default', {{ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied', wait_for_update: 500}});
  try {{ if (localStorage.getItem('sq-consent') === 'granted') gtag('consent', 'update', {{ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted', analytics_storage: 'granted'}}); }} catch (e) {{}}
  gtag('js', new Date());
  gtag('config', 'G-CQP798G5TW');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CQP798G5TW"></script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#050506">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SQ Driving School">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Russo+One&family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/sq.css">
<noscript><style>[data-reveal],.split-chars .char{{opacity:1!important;transform:none!important;filter:none!important;clip-path:none!important}}.hero h1 .line>span{{transform:none!important}}</style></noscript>
<script type="application/ld+json">{ORG_SCHEMA}</script>
<script>try{{var t=localStorage.getItem("sq-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{sch}</head>
"""


PRELOADER = '<div class="preloader" aria-hidden="true"><div class="preloader__inner"><div class="sq-logo">SQ</div><div class="preloader__bar"><span></span></div><div class="preloader__label">Starting engine…</div></div></div>'


def header(active, root):
    links = ""
    for href, label, key in NAV:
        cur = ' aria-current="page"' if href == active else ""
        k = f' data-i18n="{key}"' if key else ""
        links += f'<li><a href="{root}{href}"{cur}{k}>{label}</a></li>'
    mob = "".join(f'<a href="{root}{h}">{l}</a>' for h, l, _ in NAV)
    mob += "".join(f'<a href="{root}{h}">{l}</a>' for h, l in MOBILE_EXTRA)
    return f"""<body>
<a class="skip-link" href="#main">Skip to content</a>
{PRELOADER if active == "index.html" else ""}
<canvas class="fx-canvas" aria-hidden="true"></canvas>
<div class="noise" aria-hidden="true"></div>
<div class="scroll-progress" aria-hidden="true"><span></span></div>
<div class="road-rail" aria-hidden="true"><div class="road-rail__track"></div>{CAR_TOP}</div>
<div class="topbar"><span data-i18n="offer.title">🔥 Special offer: 10 hours for £320 in M16, M18 &amp; M19</span> · <a href="{root}postcode-checker.html">Check your postcode</a></div>
<header class="nav zone-dark">
  <div class="container nav__inner">
    <a class="brand" href="{root}index.html" aria-label="SQ Driving School home">
      <span class="sq-logo sq-logo--nav">SQ</span>
      <span class="brand__text"><span class="brand__name">Driving School</span><span class="brand__sub">Powered by DriveSQ</span></span>
    </a>
    <nav aria-label="Main"><ul class="nav__links">{links}</ul></nav>
    <div class="nav__actions">
      <select class="lang-select" aria-label="Language"><option value="en">EN</option><option value="ur">اردو</option><option value="ar">عربي</option><option value="pl">PL</option></select>
      <button class="icon-btn theme-toggle" type="button" aria-label="Switch light or dark mode">{ICONS['sun']}</button>
      <a class="btn btn--red btn--sm" href="{root}book.html">{ICONS['calendar']}<span>Book now</span></a>
      <button class="icon-btn burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" aria-hidden="true">{mob}</div>
<main id="main">
"""


def footer(root):
    FOOTER_AREAS = " · ".join(f'<a href="{root}areas/{sl}.html">{nm}</a>' for sl, nm in [("manchester", "Manchester"), ("salford", "Salford"), ("trafford", "Trafford"), ("stockport", "Stockport"), ("tameside", "Tameside"), ("oldham", "Oldham"), ("rochdale", "Rochdale"), ("bury", "Bury"), ("bolton", "Bolton"), ("wigan", "Wigan")]) + f' · <a href="{root}postcodes.html">All postcodes</a> · <a href="{root}driving-lessons-near-me.html">Lessons near me</a> · <a href="{root}areas.html">All neighbourhoods</a>'
    return f"""</main>
{wave_up()}
<footer class="footer zone-dark" style="margin-top:0">
  <div class="container">
    <div class="footer__grid">
      <div>
        <a class="brand" href="{root}index.html"><span class="sq-logo sq-logo--nav">SQ</span><span class="brand__text"><span class="brand__name">Driving School</span><span class="brand__sub">Powered by DriveSQ</span></span></a>
        <p class="mt-2">Fast, modern driving lessons across all of Greater Manchester. Manual &amp; automatic. Free DriveSQ Student Portal for every learner.</p>
        <div class="btn-row mt-2">
          <a class="btn btn--wa btn--sm" data-wa="Hi SQ Driving School!" href="https://wa.me/{WA}">{ICONS['wa']} WhatsApp</a>
          <a class="btn btn--ghost btn--sm" href="tel:{TEL}">{ICONS['phone']} {PHONE}</a>
        </div>
      </div>
      <div>
        <h4>Learn</h4>
        <ul>
          <li><a href="{root}book.html">Book in 60 seconds</a></li>
          <li><a href="{root}gift-vouchers.html">Gift vouchers</a></li>
          <li><a href="{root}first-lesson.html">Your first lesson</a></li>
          <li><a href="{root}comfort.html">Comfort Zone (nervous drivers)</a></li>
          <li><a href="{root}automatic-driving-lessons-manchester.html">Automatic lessons Manchester</a></li>
          <li><a href="{root}manual-driving-lessons-manchester.html">Manual lessons Manchester</a></li>
          <li><a href="{root}lessons.html">Driving lessons</a></li>
          <li><a href="{root}intensive.html">Intensive courses</a></li>
          <li><a href="{root}prices.html">Prices &amp; package builder</a></li>
          <li><a href="{root}nhs-driving-lessons.html">NHS staff discount</a></li>
          <li><a href="{root}student-driving-lessons-manchester.html">Student discount</a></li>
          <li><a href="{root}offer-m16-m18-m19.html">M16 · M18 · M19 offer</a></li>
          <li><a href="{root}services.html">All lesson types</a></li>
          <li><a href="{root}areas.html">Areas we cover</a></li>
        </ul>
      </div>
      <div>
        <h4>Free tools</h4>
        <ul>
          <li><a href="{root}postcode-checker.html">Postcode checker</a></li>
          <li><a href="{root}tools.html">Lesson calculator</a></li>
          <li><a href="{root}theory-quiz.html">Theory quiz</a></li>
          <li><a href="{root}hazard-game.html">Spot the hazard</a></li>
          <li><a href="{root}road-signs.html">Road sign flashcards</a></li>
          <li><a href="{root}dashboard-lights.html">Dashboard lights</a></li>
          <li><a href="{root}guides.html">Learner guides</a></li>
          <li><a href="{root}knowledge.html">Greater Manchester knowledge hub</a></li>
          <li><a href="{root}knowledge/greater-manchester-driving-test-centres.html">Test centre guides</a></li>
          <li><a href="{root}student-portal.html">DriveSQ Student Portal</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="{root}about.html">About SQ</a></li>
          <li><a href="{root}faq.html">FAQ</a></li>
          <li><a href="{root}contact.html">Contact</a></li>
          <li><a href="{STUDENT}" target="_blank" rel="noopener">Student login ↗</a></li>
          <li><a href="{INSTRUCTOR}" target="_blank" rel="noopener">Instructor login ↗</a></li>
          <li><a href="{root}privacy.html">Privacy</a></li>
          <li><a href="{root}review-policy.html">Review policy</a></li>
          <li><a href="#" data-cookie-settings>Cookie settings</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__areas" style="margin-top:44px;padding-top:26px;border-top:1px solid var(--line)">
      <h4>Driving lessons across Greater Manchester</h4>
      <p style="font-size:.9rem;line-height:2">{FOOTER_AREAS}</p>
    </div>
    <div class="footer__own">
      <span data-i18n="footer.owned"><b>SQ Driving School</b> is a brand owned and managed by <a href="https://www.drivesq.co.uk" target="_blank" rel="noopener"><b>DriveSQ</b></a>.</span>
      <span>Crafted by <b>Mohammed Qaim Abbas</b></span>
      <span>© <span class="js-year">2026</span> SQ Driving School · Greater Manchester</span>
    </div>
  </div>
  <div class="footer__credit">Website designed &amp; built by <a href="https://www.sqwebsites.co.uk" target="_blank" rel="noopener">SQ Websites</a></div>
</footer>
<a class="wa-float" data-wa="Hi SQ Driving School! I'd like to book driving lessons." href="https://wa.me/{WA}" aria-label="Chat on WhatsApp">{ICONS['wa']}</a>
<div class="mobile-bar"><a class="btn btn--ghost" href="tel:{TEL}">{ICONS['phone']} Call</a><a class="btn btn--red" href="{root}book.html">{ICONS['calendar']} Book now</a></div>
<script src="{root}assets/js/sq.js" defer></script>
</body>
</html>
"""


def page_hero(eyebrow, title, lead, crumbs, root, extra=""):
    cr = f'<a href="{root}index.html">Home</a>'
    for c in crumbs:
        cr += f' <span aria-hidden="true">/</span> {c}'
    return f"""<section class="page-hero zone-dark">
  <div class="grid-bg" aria-hidden="true"></div>
  <div class="speed-lines" aria-hidden="true"></div>
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb" data-reveal="down">{cr}</nav>
    <div class="eyebrow" data-reveal="up">{eyebrow}</div>
    <h1 data-split>{title}</h1>
    <p class="lead" data-reveal="up" data-delay=".2">{lead}</p>
    {extra}
  </div>
</section>
{wave_down()}
"""


def cta(root, title="Ready to start your engine?", text="Message us on WhatsApp and we'll get you booked in — usually within the hour."):
    return f"""<section class="section--tight">
  <div class="container">
    <div class="cta zone-dark" data-reveal="zoom">
      <div class="speed-lines" aria-hidden="true"></div>
      <div class="sq-logo" style="font-size:4rem">SQ</div>
      <h2 class="mt-2" data-split>{title}</h2>
      <p class="lead">{text}</p>
      <div class="btn-row">
        <a class="btn btn--red" data-wa="Hi SQ Driving School! I'd like to book driving lessons." href="https://wa.me/{WA}">{ICONS['wa']} Book on WhatsApp</a>
        <a class="btn btn--ghost" href="tel:{TEL}">{ICONS['phone']} Call {PHONE}</a>
      </div>
    </div>
  </div>
</section>
"""


def phone_mock():
    return """<div class="phone" data-tilt="10" aria-hidden="true">
  <div class="phone__notch"></div>
  <div class="phone__screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px"><b style="font-family:var(--font-display);font-size:1rem">Drive<span style="color:#ff1f1f">SQ</span></b><span class="app-badge">Nearly test ready</span></div>
    <div class="app-card"><small>Next lesson</small><b>Thu · 4:00pm</b><div style="color:#8a8a92;font-size:.68rem">2 hrs · Pick-up M19</div></div>
    <div class="app-row"><div class="app-card"><small>Hours</small><b>18</b></div><div class="app-card"><small>Topics</small><b>11</b></div><div class="app-card"><small>Theory</small><b>12d</b></div></div>
    <div class="app-card"><small>Overall competency</small><div style="display:flex;justify-content:space-between"><span>78%</span><span style="color:#8a8a92">23 skills</span></div><div class="app-bar"><span style="--w:78%"></span></div>
      <div style="margin-top:8px;display:flex;justify-content:space-between;font-size:.66rem"><span>Bay parking</span><span style="color:#22e07a">Independent</span></div><div class="app-bar"><span style="--w:100%"></span></div>
      <div style="margin-top:8px;display:flex;justify-content:space-between;font-size:.66rem"><span>Roundabouts</span><span style="color:#ffb020">Developing</span></div><div class="app-bar"><span style="--w:60%"></span></div></div>
    <div class="bubble bubble--in">Great lesson today — your roundabout positioning is really coming together 👏</div>
    <div class="bubble bubble--out">Thank you! See you Thursday 🚗</div>
  </div>
</div>"""


def page(path, title, desc, body, root="", active=None, schema=None, noindex=False):
    for cut in (" | Manual & Automatic", " | Manual &amp; Automatic"):
        if len(title) > 62:
            title = title.replace(cut, "")
    if len(title) > 62:
        title = title.replace(" | SQ Driving School", " | SQ Driving")
    if len(title) > 62:
        title = title.replace(" | SQ Driving", "")
    return head(title, desc, path, root, schema, noindex) + header(active or path, root) + body + footer(root)


def reassure():
    items = [("check", "No hidden fees"), ("pin", "Door-to-door pick-up"), ("clock", "Learn at your own pace"),
             ("phone-app", "Free Student Portal"), ("chat", "A real person on WhatsApp"), ("gear", "Manual &amp; automatic")]
    li = "".join(f"<li>{ICONS[i]}{t}</li>" for i, t in items)
    return f'<div class="reassure" aria-label="Why learners feel at ease with SQ"><div class="container"><ul class="reassure__list">{li}</ul></div></div>'
