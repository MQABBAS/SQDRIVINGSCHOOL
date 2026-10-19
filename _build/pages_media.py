# Real pass photos and video reviews from DriveSQ learners (SQ Driving School is powered by DriveSQ).
from layout import *

PHOTOS = [
    ("pass-pic1", "Learner holding their pass certificate beside a DriveSQ car with L-plate roof sign", "portrait"),
    ("pass-pic2", "Learner celebrating their driving test pass next to a DriveSQ tuition car", "portrait"),
    ("pass-pic5", "Smiling learner with their pass certificate by a DriveSQ car", "portrait"),
    ("pass-pic3", "Learner who just passed, standing with a DriveSQ car", "portrait"),
    ("pass-pic4", "New driver with their pass certificate outside the test centre", "landscape"),
    ("pass-adi", "Learner and DriveSQ instructor celebrating a test pass", "landscape"),
]
VIDEOS = [  # (n, short label)
    (3, "Pass certificate in hand"), (1, "Straight after the test"), (8, "Passed and showing the certificate"),
    (5, "In the car after passing"), (4, "A learner's review"), (6, "Talking about lessons"),
    (7, "Fresh from the test"), (2, "Handshake moment"), (9, "Just passed with DriveSQ"),
]
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>'


def video_cards(root, items=None):
    items = items or VIDEOS
    return "".join(
        f'<button type="button" class="mw-vid" data-video="{root}assets/media/review-{n}.mp4" data-poster="{root}assets/media/review-{n}.webp" aria-label="Play video: {lab}">'
        f'<img src="{root}assets/media/review-{n}.webp" alt="Video still: {lab}" loading="lazy" width="300" height="530">'
        f'<span class="mw-vid__play">{PLAY}</span><span class="mw-vid__tag">✅ Passed</span><span class="mw-vid__cap">{lab}</span></button>'
        for n, lab in items)


def photo_cards(root, items=None):
    items = items or PHOTOS
    return "".join(
        f'<button type="button" class="mw-pic mw-pic--{shape}" data-photo="{root}assets/media/{f}.webp" aria-label="View photo: {alt}">'
        f'<img src="{root}assets/media/{f}-sm.webp" alt="{alt}" loading="lazy"></button>'
        for f, alt, shape in items)


def media_section(root="", heading="Real learners. Real passes.", lead="Photos and videos from learners who passed with our DriveSQ instructors across Greater Manchester. Tap any one to watch.", videos=6, link=True):
    more = f'<div class="center mt-3"><a class="btn btn--ghost" href="{root}passes.html">See every pass &amp; video review {icon("arrow")}</a></div>' if link else ""
    return f'''<section class="section mediawall" data-media-wall>
  <div class="container">
    <div class="section__head center"><div class="eyebrow">Pass wall</div><h2 data-split>{heading}</h2><p class="lead">{lead}</p></div>
    <div class="mw-row" data-reveal="up" role="list" aria-label="Video reviews">{video_cards(root, VIDEOS[:videos])}</div>
    <div class="mw-grid mt-3" data-reveal="up" aria-label="Pass photos">{photo_cards(root)}</div>
    {more}
  </div>
</section>'''


def passes_strip(root=""):
    """Small social-proof strip for the booking page."""
    pics = "".join(f'<button type="button" class="mw-pic mw-pic--sq" data-photo="{root}assets/media/{f}.webp" aria-label="View photo: {alt}"><img src="{root}assets/media/{f}-sm.webp" alt="{alt}" loading="lazy"></button>' for f, alt, _ in PHOTOS[:4])
    return f'<div class="mw-strip" data-media-wall data-reveal="up"><div class="mw-strip__pics">{pics}</div><div class="mw-strip__txt"><b>Real passes from our learners.</b> <a href="{root}passes.html">See photos &amp; video reviews</a></div></div>'


def passes_page():
    root = ""
    body = page_hero("Real passes", "Pass photos & video reviews.", "Real learners, real certificates. These learners passed with DriveSQ instructors — the same team behind SQ Driving School.", ["Real passes"], root,
                     f'<div class="btn-row mt-2" data-reveal="up"><a class="btn btn--red" href="{root}book.html">{icon("calendar")} Book in 60 seconds</a><a class="btn btn--ghost" href="https://www.instagram.com/drive_sq_academy/" target="_blank" rel="noopener">More on Instagram</a></div>')
    body += f'''<section class="section mediawall" data-media-wall><div class="container">
<div class="section__head"><div class="eyebrow">Video reviews</div><h2 data-split>Hear it from them.</h2><p class="lead">Short videos filmed straight after passing. Tap to play with sound.</p></div>
<div class="mw-gridv" data-reveal="up">{video_cards(root)}</div>
<div class="section__head mt-4"><div class="eyebrow">Pass photos</div><h2 data-split>Certificates in hand.</h2></div>
<div class="mw-grid" data-reveal="up">{photo_cards(root)}</div>
<p class="note mt-3">Photos and videos are shared with each learner's permission. Want yours here? Send it to us on <a href="https://www.instagram.com/drive_sq_academy/" target="_blank" rel="noopener">Instagram</a> or WhatsApp.</p>
</div></section>
{cta(root, "Your pass photo could be next.", "Book in 60 seconds or message us on WhatsApp.")}'''
    schema = [{"@context": "https://schema.org", "@type": "VideoObject", "name": f"SQ Driving School learner video review — {lab}",
               "description": f"A learner who passed their driving test with a DriveSQ instructor in Greater Manchester: {lab.lower()}.",
               "thumbnailUrl": f"{SITE}/assets/media/review-{n}.webp", "contentUrl": f"{SITE}/assets/media/review-{n}.mp4", "uploadDate": "2026-10-19"} for n, lab in VIDEOS]
    return page("passes.html", "Real Driving Test Passes & Video Reviews | SQ Driving School Manchester",
                "Real pass photos and video reviews from learners who passed with DriveSQ instructors across Greater Manchester. See why learners choose SQ Driving School.", body, root, schema=schema)
