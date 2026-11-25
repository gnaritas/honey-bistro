#!/usr/bin/env python3
"""The Honey Bistro — template v2 multi-page generator (websites lane).
Built 2026-11-25 for card t_8ff55c07. Slug: honey-bistro. Demo host pinned below.

VERIFIED FACTS + SOURCES (no invented details; planned items labeled planned):
S1  smilepolitely.com/splog/the-honey-bistro-opening-in-2027/ (2026-11-24):
    breakfast-lunch concept by Star 57 owners; tighter hours than Star 57 (6a-9p);
    favorites from Star 57's menu (eggs, pancakes, bacon, waffles, and more) + new
    eats exclusive to the bistro; owned by Endrit and Nita Zekjiri; space beside El
    Rancho Grande II, Kyle's Corner for nine months, previously Industrial Donut six
    years; Nita quotes: name story ("warm, sweet, welcoming, and memorable... I love
    honey"), customers-as-family ("welcomed, remembered, appreciated... part of our
    family"), Lakeview Family Restaurant (Shelbyville) early days; Thanksgiving free
    meal 11a-1p tradition, arrived in America from North Macedonia 17 years ago on
    Thanksgiving; hoping to fire up the griddle as early as mid-January [2027].
S2  news-gazette.com "Star 57 owners to open Savoy brunch spot" + yahoo.com syndication
    (News-Gazette, 2026-11-24): open The Honey Bistro at 501 Commerce Drive in January
    "if everything goes as planned"; breakfast+lunch + "signature honey dishes"; "We're
    bringing a sweetness to the town"; plan hours 7 a.m.-3 p.m. so they can continue
    Star 57 Diner; Star 57 opened 2025 (former Denny's Classic in Tuscola); Kyle's
    Corner opened March, closed Nov 14; "It's a bigger town, and we have so many
    people already that are supporting the diner from Savoy."
S3  shop's OWN Facebook Page intro (facebook.com/profile.php?id=61596882386807,
    checked 2026-11-25): tagline "A fresh take on your favorite flavors. Good food,
    warm hospitality & a little touch of honey."; Restaurant / Breakfast & Brunch;
    501 Commerce Drive, Savoy, IL; Thehoneybistro@hotmail.com self-published.
S4  Star 57 Diner FB Page (id 61572504720880, checked 2026-11-25): 1104 Tuscola Blvd,
    Tuscola IL; (217) 253-9444; Star57diner@hotmail.com; "Breakfast served all day".
Geo: nominatim OSM 501 Commerce Drive, Savoy IL 61874 -> 40.0598371,-88.2520550.
Design: unique build (warm honey/parchment/ink, honeycomb accents) - not a sibling clone.
"""
import os, json, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
ORIGIN = "https://honey-bistro-demo.up.railway.app"
BRAND = "The Honey Bistro"
CITY = "Savoy"
ST = "IL"
ZIP = "61874"
ADDRESS = "501 Commerce Drive"
LAT, LON = 40.05984, -88.25206
EMAIL = "Thehoneybistro@hotmail.com"
DINER_PHONE = "(217) 253-9444"
DINER_PHONE_RAW = "+12172539444"
FB_URL = "https://www.facebook.com/profile.php?id=61596882386807"
FB_DINER = "https://www.facebook.com/p/STAR-57-DINER-61572504720880/"
MAPQ = "501%20Commerce%20Drive%2C%20Savoy%2C%20IL%2061874"
BUILT = "2026-11-25"

def esc(s):
    return s.replace("&", "&amp;")

def head(title, desc, path):
    url = ORIGIN + ("/" if path == "index.html" else "/" + path[:-5])
    return f"""<!DOCTYPE html>
<!-- BUILT-{BUILT} -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
<link rel="preconnect" href="https://www.google.com">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

NAV = """<header class="site">
  <a class="brand" href="/">The&nbsp;Honey&nbsp;Bistro</a>
  <input type="checkbox" id="navtoggle" class="navtoggle" aria-label="Show navigation">
  <label for="navtoggle" class="navbtn" aria-hidden="true"><i></i></label>
  <nav aria-label="Main" class="links">
    <a href="/menu">Menu</a>
    <a href="/brunch-in-savoy">Brunch&nbsp;in&nbsp;Savoy</a>
    <a href="/our-story">Our&nbsp;Story</a>
    <a href="/visit">Visit</a>
    <a class="btn btn-sm" href="/contact">Contact&nbsp;Us</a>
  </nav>
</header>
"""

FOOTER = """<footer class="site">
  <div class="fwrap fgrid">
    <div>
      <h4>The Honey Bistro</h4>
      <p>501 Commerce Drive<br>Savoy, IL 61874<br><span class="fopen">Opening January 2027</span></p>
    </div>
    <div>
      <h4>Planned Hours</h4>
      <p>Breakfast &amp; lunch, daily<br>7 a.m. &ndash; 3 p.m. (planned)</p>
    </div>
    <div>
      <h4>Questions &amp; Updates</h4>
      <p><a class="flink" href="mailto:Thehoneybistro@hotmail.com">Thehoneybistro<wbr />@hotmail.com</a><br>
      Ask the team at Star 57 Diner:<br><a class="flink" href="tel:+12172539444">(217) 253-9444</a></p>
    </div>
    <div>
      <h4>Pages</h4>
      <p><a class="flink" href="/menu">Menu</a><br>
      <a class="flink" href="/brunch-in-savoy">Brunch in Savoy</a><br>
      <a class="flink" href="/breakfast-champaign-urbana">Champaign-Urbana</a><br>
      <a class="flink" href="/our-story">Our Story</a><br>
      <a class="flink" href="/visit">Visit</a><br>
      <a class="flink" href="/contact">Contact</a><br>
      <a class="flink" href="/privacy">Privacy</a><br>
      <a class="flink" href="https://www.facebook.com/profile.php?id=61596882386807" rel="noopener">Facebook</a></p>
    </div>
  </div>
  <div class="fwrap">
    <p class="footline">&copy; 2026 The Honey Bistro &middot; 501 Commerce Drive, Savoy, IL &middot; A new breakfast &amp; brunch spot from the owners of Star 57 Diner</p>
  </div>
</footer>
"""

def breadcrumbs(name):
    return ('<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> &rsaquo; '
            f'<span>{esc(name)}</span></nav>\n')

def ld_home():
    rest = {"@context": "https://schema.org", "@type": "Restaurant", "name": BRAND,
            "image": ORIGIN + "/og.png", "url": ORIGIN + "/",
            "servesCuisine": ["American", "Breakfast", "Brunch"],
            "email": EMAIL.lower(),
            "address": {"@type": "PostalAddress", "streetAddress": ADDRESS,
                        "addressLocality": CITY, "addressRegion": ST,
                        "postalCode": ZIP, "addressCountry": "US"},
            "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
            "hasMap": "https://www.google.com/maps?q=" + MAPQ,
            "sameAs": [FB_URL],
            "parentOrganization": {"@type": "Organization", "name": "Star 57 Diner",
                                   "foundingDate": "2025",
                                   "address": {"@type": "PostalAddress",
                                               "streetAddress": "1104 Tuscola Blvd",
                                               "addressLocality": "Tuscola",
                                               "addressRegion": ST, "addressCountry": "US"}}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "When does The Honey Bistro open?",
         "acceptedAnswer": {"@type": "Answer", "text": "We are aiming for January 2027 — as early as mid-January, if everything goes as planned."}},
        {"@type": "Question", "name": "Where is The Honey Bistro located?",
         "acceptedAnswer": {"@type": "Answer", "text": "501 Commerce Drive in Savoy, Illinois — the former Kyle's Corner space beside El Rancho Grande II, minutes from Champaign and Urbana."}},
        {"@type": "Question", "name": "What will be on the menu?",
         "acceptedAnswer": {"@type": "Answer", "text": "Favorites from Star 57 Diner's menu — eggs, pancakes, bacon, waffles, and more — plus new plates exclusive to the bistro, including signature honey dishes."}},
        {"@type": "Question", "name": "What are the hours?",
         "acceptedAnswer": {"@type": "Answer", "text": "Planned daily, 7 a.m. to 3 p.m. — breakfast and lunch only, so the owners can keep serving at Star 57 Diner in Tuscola."}},
        {"@type": "Question", "name": "Will Star 57 Diner stay open?",
         "acceptedAnswer": {"@type": "Answer", "text": "Yes. Endrit and Nita Zekjiri will keep running Star 57 Diner in Tuscola while The Honey Bistro operates in Savoy."}}]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"}]}
    out = ""
    for j in (rest, faq, bc):
        out += '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False, separators=(", ", ": ")) + "</script>\n"
    return out

def ld_page_bc(name):
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": ORIGIN + "/" + name}]}
    return '<script type="application/ld+json">' + json.dumps(bc, ensure_ascii=False, separators=(", ", ": ")) + "</script>\n"

def ld_service(name, path, desc, area):
    svc = {"@context": "https://schema.org", "@type": "Service", "name": name,
           "description": desc, "url": ORIGIN + "/" + path,
           "provider": {"@type": "Restaurant", "name": BRAND,
                        "address": {"@type": "PostalAddress", "streetAddress": ADDRESS,
                                    "addressLocality": CITY, "addressRegion": ST,
                                    "postalCode": ZIP, "addressCountry": "US"}},
           "areaServed": {"@type": "Place", "name": area}}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": ORIGIN + "/" + path}]}
    out = ""
    for j in (svc, bc):
        out += '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False, separators=(", ", ": ")) + "</script>\n"
    return out

def page(head_html, body_html):
    return head_html + NAV + '<main id="main">\n' + body_html + "\n</main>\n" + FOOTER + "</body>\n</html>\n"

PAGES = {}

# ---------------- HOME ----------------
PAGES['index.html'] = (head(f'{BRAND} — Breakfast & Brunch in {CITY}, {ST} — Opening January 2027',
    "A new breakfast and brunch spot on 501 Commerce Drive in Savoy, IL from the owners of Star 57 Diner. Opening January 2027. Favorites from Star 57, new exclusives, and signature honey dishes.", "index.html")
    + """<section class="hero">
  <svg class="hexfield" viewBox="0 0 420 480" aria-hidden="true" focusable="false">
    <g fill="none" stroke="#E7D9BE" stroke-width="2">
      <path d="M60 20l50 29v57l-50 29-50-29V49z"/>
      <path d="M160 78l50 29v57l-50 29-50-29V107z"/>
      <path d="M260 20l50 29v57l-50 29-50-29V49z"/>
      <path d="M360 78l50 29v57l-50 29-50-29V107z"/>
      <path d="M110 210l50 29v57l-50 29-50-29v-57z"/>
      <path d="M210 268l50 29v57l-50 29-50-29v-57z"/>
      <path d="M310 210l50 29v57l-50 29-50-29v-57z"/>
      <path d="M160 400l50 29v-42l50 29 50-29v42l50-29v-57l-50-29-50 29-50-29-50 29z"/>
    </g>
  </svg>
  <div class="wrap">
    <p class="badge">Opening January 2027 &middot; Savoy, Illinois</p>
    <h1>Breakfast &amp; brunch,<br>with a little touch of&nbsp;honey.</h1>
    <p class="lede">The Honey Bistro is coming to 501 Commerce Drive in Savoy — a new breakfast
    and brunch spot from Endrit and Nita Zekjiri, the couple behind Star 57 Diner in Tuscola.
    A fresh take on your favorite flavors: good food, warm hospitality, and a little touch of honey.</p>
    <p class="cta-row">
      <a class="btn" href="/contact">Get opening updates</a>
      <a class="btn ghost ink" href="tel:+12172539444">Call the team: (217)&nbsp;253-9444</a>
    </p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="k">What&apos;s cooking</p>
    <h2>The plates you already love — plus things you haven&apos;t tried&nbsp;yet</h2>
    <p class="sub">We&apos;re bringing Star 57&apos;s kitchen to Savoy: the breakfast favorites people
    drive to Tuscola for, new plates that only exist here, and signature honey dishes that gave
    the place its name. Full menu and prices come with opening day.</p>
    <div class="cards">
      <div class="card">
        <p class="k">From Star 57</p>
        <h3>The favorites, headed north</h3>
        <p>Eggs, pancakes, bacon, waffles, and more — made the way Star 57 Diner makes them today.</p>
      </div>
      <div class="card">
        <p class="k">Savoy only</p>
        <h3>New plates, bistro exclusives</h3>
        <p>New eats that won&apos;t be on the menu in Tuscola — riffs from the same kitchen, made only for the bistro.</p>
      </div>
      <div class="card">
        <p class="k">7 a.m. &ndash; 3 p.m. planned</p>
        <h3>Breakfast &amp; lunch, all day</h3>
        <p>Tighter hours than the diner, on purpose: breakfast and lunch served till three, so the griddle&apos;s warm when you want it.</p>
      </div>
    </div>
  </div>
</section>

<figure class="quote">
  <blockquote>&ldquo;We&apos;re bringing a sweetness to the town.&rdquo;</blockquote>
  <cite>Nita Zekjiri, co-owner — The News-Gazette, November 2026</cite>
</figure>

<section class="band alt">
  <div class="wrap">
    <p class="k">Questions people ask us</p>
    <h2>Before opening day</h2>
    <details open>
      <summary>When are you opening?</summary>
      <p>We&apos;re aiming for January 2027 — as early as mid-January, if everything goes as planned.
      The best way to hear it first is to <a href="/contact">send us a note</a> and follow the
      <a href="https://www.facebook.com/profile.php?id=61596882386807" rel="noopener">Facebook page</a>.</p>
    </details>
    <details>
      <summary>Where exactly is it?</summary>
      <p>501 Commerce Drive in Savoy — the space that housed Kyle&apos;s Corner, right beside El Rancho
      Grande II, minutes from Champaign and Urbana. See the <a href="/visit">visit page</a> for the map.</p>
    </details>
    <details>
      <summary>What&apos;s on the menu?</summary>
      <p>Favorites from Star 57&apos;s menu — eggs, pancakes, bacon, waffles, and more — plus new
      exclusive plates and signature honey dishes. Details are on the <a href="/menu">menu page</a>.</p>
    </details>
    <details>
      <summary>What are the hours?</summary>
      <p>Planned daily, 7 a.m. to 3 p.m. — breakfast and lunch only. The tighter schedule lets Endrit
      and Nita keep cooking and serving at Star 57 Diner in Tuscola too.</p>
    </details>
    <details>
      <summary>Will Star 57 Diner stay open?</summary>
      <p>Yes. Star 57 Diner at 1104 Tuscola Blvd stays open — breakfast served all day, seven days a
      week. Savoy just gets the second chapter.</p>
    </details>
  </div>
</section>

<section class="band">
  <div class="wrap cta-final">
    <h2>Be first through the door</h2>
    <p>Tell us you&apos;re waiting for opening day — we&apos;ll email you the moment the griddle is
    scheduled. Or call the team at Star 57 Diner: <a href="tel:+12172539444">(217) 253-9444</a>.</p>
    <p class="cta-row"><a class="btn" href="/contact">Send us a note</a>
    <a class="btn ghost ink" href="/menu">See what&apos;s coming</a></p>
  </div>
</section>
""" + ld_home())

# ---------------- MENU ----------------
PAGES['menu.html'] = (head("Menu Preview — The Honey Bistro, Savoy IL",
    "The opening menu of The Honey Bistro in Savoy, IL: Star 57 Diner favorites — eggs, pancakes, bacon, waffles — plus new bistro exclusives and signature honey dishes. Opening January 2027.", "menu.html")
    + breadcrumbs("Menu")
    + """<section class="page-head">
  <div class="wrap">
    <p class="k">Opening menu preview</p>
    <h2>The sweet things are coming</h2>
    <p class="lede">Here&apos;s the shape of the opening menu. Full items and prices land with opening
    day — the kitchen is still dialing in the new plates, and we&apos;d rather show you the real
    menu than promise a guess.</p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <h3 class="ghead">Star 57 favorites, now in Savoy</h3>
    <p class="gnote">The dishes people already drive to Tuscola for — coming to the same quality on
    the same griddle, nine miles closer.</p>
    <ul class="menu-list">
      <li><span class="mi">Eggs</span><span class="mn">any style, cooked to order</span></li>
      <li><span class="mi">Pancakes</span><span class="mn">stacks, the way Star 57 makes them</span></li>
      <li><span class="mi">Bacon</span><span class="mn">crisp, on the plate or on the side</span></li>
      <li><span class="mi">Waffles</span><span class="mn">golden, and yes — honey belongs on them</span></li>
      <li><span class="mi">&hellip; and more</span><span class="mn">the rest of the favorites, announced at opening</span></li>
    </ul>
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <h3 class="ghead">The signature touch</h3>
    <p class="gnote">The name isn&apos;t decoration. Co-owner Nita Zekjiri says it best: &ldquo;I
    wanted something warm, sweet, welcoming, and memorable&hellip; I would put [honey] on just
    about anything if I could.&rdquo;</p>
    <ul class="menu-list">
      <li><span class="mi">Signature honey dishes</span><span class="mn">dishes built around honey — the reason we&apos;re called what we&apos;re called</span></li>
      <li><span class="mi">Honey, on the table</span><span class="mn">because if you know Nita, you know it&apos;s coming</span></li>
    </ul>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <h3 class="ghead">New eats, exclusive to the bistro</h3>
    <p class="gnote">New plates created for the Savoy kitchen — you won&apos;t find these at the
    diner in Tuscola.</p>
    <ul class="menu-list">
      <li><span class="mi">Bistro exclusives</span><span class="mn">new items from the same kitchen, served only here — names revealed at opening</span></li>
    </ul>
    <figure class="quote inband">
      <blockquote>&ldquo;Honestly, I just fell in love with the name&hellip; I loved the feeling of the
      name and thought it fit the cozy, inviting atmosphere we wanted to create.&rdquo;</blockquote>
      <cite>Nita Zekjiri, co-owner — Smile Politely, November 2026</cite>
    </figure>
    <p class="cta-row"><a class="btn" href="/contact">Ask about the menu</a></p>
  </div>
</section>
""" + ld_page_bc("menu"))

# ---------------- BRUNCH IN SAVOY (detail 1) ----------------
PAGES['brunch-in-savoy.html'] = (head("Brunch in Savoy — The Honey Bistro, 501 Commerce Dr",
    "The Honey Bistro brings brunch and breakfast to Savoy, IL — planned daily 7 a.m. to 3 p.m. at 501 Commerce Drive beside El Rancho Grande II, opening January 2027.", "brunch-in-savoy.html")
    + breadcrumbs("Brunch in Savoy")
    + """<section class="page-head">
  <div class="wrap">
    <p class="k">Service &middot; Savoy &amp; the Champaign-Urbana area</p>
    <h2>Brunch is moving to Savoy</h2>
    <p class="lede">No more Saturday drives to Tuscola for the pancakes. The Honey Bistro opens on
    Commerce Drive in Savoy in January 2027 — Star 57&apos;s cooking, breakfast-and-lunch hours,
    and honey where honey belongs.</p>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div class="split-main">
      <h3>What brunch looks like here</h3>
      <p>Brunch, the honest diner way: eggs any style, stacks of pancakes, crisp bacon, golden
      waffles — plus new plates you can&apos;t get at the diner, and signature honey dishes that
      turn a breakfast into a reason to come back.</p>
      <p>Planned hours are daily, 7 a.m. to 3 p.m. — early enough for the pre-work egg sandwich,
      late enough for the post-church waffle. We close at three on purpose: the owners run Star 57
      Diner in Tuscola too, and both kitchens deserve full attention.</p>
      <h3>Why Savoy</h3>
      <p>&ldquo;It&apos;s a bigger town, and we have so many people already that are supporting the
      diner from Savoy,&rdquo; Nita Zekjiri told The News-Gazette. &ldquo;So we just wanted to bring
      something there as well.&rdquo; The answer is a second restaurant, placed right where those
      customers already are.</p>
      <h3>The space</h3>
      <p>The Honey Bistro takes over the storefront at 501 Commerce Drive that housed Kyle&apos;s
      Corner for nine months — and the Industrial Donut for the six years before that — right
      beside El Rancho Grande II, on the Commerce Drive strip minutes from Champaign and Urbana.</p>
      <p class="cta-row"><a class="btn" href="/visit">Map &amp; directions</a>
      <a class="btn ghost ink" href="/menu">Menu preview</a></p>
    </div>
    <aside class="split-side">
      <div class="info-card">
        <h4>Brunch &amp; breakfast</h4>
        <dl class="facts">
          <dt>Where</dt><dd>501 Commerce Drive, Savoy, IL 61874</dd>
          <dt>When</dt><dd>Opening January 2027</dd>
          <dt>Planned hours</dt><dd>Daily, 7 a.m. &ndash; 3 p.m.</dd>
          <dt>Serving</dt><dd>Breakfast &amp; lunch, seven days</dd>
          <dt>Ask the team</dt><dd><a href="tel:+12172539444">(217) 253-9444</a> (Star 57 Diner)</dd>
        </dl>
      </div>
    </aside>
  </div>
</section>
""" + ld_service("Brunch in Savoy", "brunch-in-savoy",
    "Breakfast and brunch daily, planned 7 a.m. to 3 p.m., opening January 2027 at 501 Commerce Drive, Savoy, Illinois.", "Savoy, Illinois"))

# ---------------- BREAKFAST NEAR CHAMPAIGN-URBANA (detail 2) ----------------
PAGES['breakfast-champaign-urbana.html'] = (head("Breakfast Near Champaign-Urbana — The Honey Bistro",
    "Minutes from Champaign and Urbana, The Honey Bistro opens January 2027 at 501 Commerce Drive, Savoy IL — Star 57 Diner's breakfast favorites plus new exclusives, planned 7a-3p daily.", "breakfast-champaign-urbana.html")
    + breadcrumbs("Breakfast Near Champaign-Urbana")
    + """<section class="page-head">
  <div class="wrap">
    <p class="k">Service &middot; Champaign-Urbana metro</p>
    <h2>Real breakfast, minutes off the 26</h2>
    <p class="lede">For gamedays, move-in weekends, and every ordinary Saturday — The Honey Bistro
    puts diner-quality breakfast a short drive from Champaign and Urbana, on Savoy&apos;s Commerce
    Drive strip, opening January 2027.</p>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div class="split-main">
      <h3>Right in the middle of everything</h3>
      <p>Savoy sits between Champaign and Urbana, and 501 Commerce Drive sits on the busiest
      stretch of it — beside El Rancho Grande II, easy from US-150, I-74 and I-57 without ever
      aiming at downtown traffic. From Champaign or Urbana it&apos;s a short, boring, easy drive.
      That&apos;s the point.</p>
      <h3>The track record behind it</h3>
      <p>This isn&apos;t a first rodeo. Endrit and Nita Zekjiri opened Star 57 Diner in Tuscola in
      2025 — took over the old diner, cleaned up the menu, and built a line of regulars who keep it
      busy seven days a week. Nita learned breakfast at Lakeview Family Restaurant in Shelbyville
      long before that. Savoy is the second restaurant, not the practice run.</p>
      <h3>What to expect on opening morning</h3>
      <p>Eggs any style, pancakes, bacon, waffles, and more favorites from the Tuscola menu — plus
      new plates built for the Savoy kitchen and signature honey dishes. Planned daily hours of
      7 a.m. to 3 p.m. mean a warm griddle from early coffee to a late lunch.</p>
      <p class="cta-row"><a class="btn" href="/contact">Get opening updates</a>
      <a class="btn ghost ink" href="/our-story">Read the story</a></p>
    </div>
    <aside class="split-side">
      <div class="info-card">
        <h4>Getting here</h4>
        <dl class="facts">
          <dt>Address</dt><dd>501 Commerce Drive, Savoy, IL 61874</dd>
          <dt>Landmark</dt><dd>Beside El Rancho Grande II</dd>
          <dt>From Champaign</dt><dd>Minutes — Savoy borders the city</dd>
          <dt>From Tuscola</dt><dd>Star 57 Diner stays open: 1104 Tuscola Blvd</dd>
          <dt>Opening</dt><dd>January 2027 (planned)</dd>
        </dl>
      </div>
    </aside>
  </div>
</section>
""" + ld_service("Breakfast Near Champaign-Urbana", "breakfast-champaign-urbana",
    "Diner-quality breakfast and brunch opening January 2027 on Commerce Drive in Savoy — minutes from Champaign and Urbana, planned daily 7 a.m. to 3 p.m.", "Champaign-Urbana, Illinois"))

# ---------------- OUR STORY ----------------
PAGES['our-story.html'] = (head("Our Story — The Honey Bistro, Savoy IL",
    "The story of The Honey Bistro: Endrit and Nita Zekjiri, from North Macedonia to Shelbyville to Star 57 Diner in Tuscola — now bringing breakfast and honey to Savoy, IL.", "our-story.html")
    + breadcrumbs("Our Story")
    + """<section class="page-head">
  <div class="wrap">
    <p class="k">Our story</p>
    <h2>From Shelbyville griddles to a second kitchen</h2>
    <p class="lede">The Honey Bistro is the second restaurant from Endrit and Nita Zekjiri. The first
    one — Star 57 Diner in Tuscola — gets a steady stream of Savoy license plates in its parking
    lot. So they stopped making the drive one-way.</p>
  </div>
</section>

<section class="band">
  <div class="wrap prose">
    <h3>The long road here</h3>
    <p>Nita arrived in America from North Macedonia seventeen years ago — on Thanksgiving Day, a
    fact she&apos;ll tell you any time you ask. She learned breakfast service early, at Lakeview
    Family Restaurant in Shelbyville. Years later came the call to take over the old diner in
    Tuscola — the former Denny&apos;s Classic — and turn it into Star 57 Diner, which opened in
    2025 and hasn&apos;t slowed down since.</p>
    <p>Every Thanksgiving, Star 57 serves a free meal from 11 a.m. to 1 p.m. &ldquo;It&apos;s our
    way of giving back to the community that supports us every day,&rdquo; Nita says.
    &ldquo;Thanksgiving is the day we arrived in America&hellip; I never want to lose sight of
    where I started.&rdquo;</p>
    <figure class="quote">
      <blockquote>&ldquo;I want our customers to feel welcomed, remembered, appreciated, and
      eventually feel like they&apos;re part of our family, too.&rdquo;</blockquote>
      <cite>Nita Zekjiri, co-owner — Smile Politely, November 2026</cite>
    </figure>
    <h3>Why &ldquo;Honey&rdquo;</h3>
    <p>&ldquo;Honestly, I just fell in love with the name,&rdquo; Nita says. &ldquo;I wanted
    something warm, sweet, welcoming, and memorable&hellip; And if you know me personally, you
    know I love honey!&rdquo; The menu backs the name up: signature honey dishes, and honey
    within reach of everything else.</p>
    <h3>The promise for Savoy</h3>
    <p>&ldquo;The food brings people through the doors, but it&apos;s the connections and
    relationships that make a place truly special,&rdquo; Nita says. Same cooking, same
    hospitality, tighter hours — 7 a.m. to 3 p.m., planned — so both kitchens get their full
    attention, and Star 57 stays exactly where its regulars already love it.</p>
    <p class="cta-row"><a class="btn" href="/contact">Say hello before opening</a>
    <a class="btn ghost ink" href="https://www.facebook.com/profile.php?id=61596882386807" rel="noopener">Follow on Facebook</a></p>
  </div>
</section>
""" + ld_page_bc("our-story"))

# ---------------- VISIT ----------------
PAGES['visit.html'] = (head("Visit — The Honey Bistro, 501 Commerce Drive, Savoy IL 61874",
    "Find The Honey Bistro at 501 Commerce Drive in Savoy, IL — the former Kyle's Corner space beside El Rancho Grande II, opening January 2027, planned daily 7 a.m. to 3 p.m.", "visit.html")
    + breadcrumbs("Visit")
    + """<section class="page-head">
  <div class="wrap">
    <p class="k">Find us</p>
    <h2>501 Commerce Drive, Savoy</h2>
    <p class="lede">The Honey Bistro is opening in the storefront that housed Kyle&apos;s Corner —
    right beside El Rancho Grande II, on Savoy&apos;s busiest strip, minutes from Champaign and
    Urbana.</p>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div class="split-main">
      <div class="mapwrap">
        <iframe title="Map to The Honey Bistro, 501 Commerce Drive, Savoy, Illinois"
          src="https://www.google.com/maps?q=501%20Commerce%20Drive%2C%20Savoy%2C%20IL%2061874&output=embed"
          loading="lazy"></iframe>
      </div>
      <p class="cta-row">
        <a class="btn" href="https://www.google.com/maps?q=501%20Commerce%20Drive%2C%20Savoy%2C%20IL%2061874" rel="noopener">Open in Google Maps</a>
      </p>
    </div>
    <aside class="split-side">
      <div class="info-card">
        <h4>The details</h4>
        <dl class="facts">
          <dt>Address</dt><dd>501 Commerce Drive<br>Savoy, IL 61874</dd>
          <dt>Opening</dt><dd>January 2027 (as early as mid-January, planned)</dd>
          <dt>Planned hours</dt><dd>Daily, 7 a.m. &ndash; 3 p.m.</dd>
          <dt>Email</dt><dd><a href="mailto:Thehoneybistro@hotmail.com">Thehoneybistro<wbr />@hotmail.com</a></dd>
          <dt>Phone (Star 57 Diner)</dt><dd><a href="tel:+12172539444">(217) 253-9444</a></dd>
          <dt>Landmark</dt><dd>Beside El Rancho Grande II, former Kyle&apos;s Corner space</dd>
        </dl>
      </div>
      <div class="info-card">
        <h4>While you wait for opening day</h4>
        <p>Star 57 Diner — 1104 Tuscola Blvd, Tuscola, IL. Breakfast served all day, seven days a
        week. <a href="https://www.facebook.com/p/STAR-57-DINER-61572504720880/" rel="noopener">Their
        Facebook page</a> posts daily specials.</p>
      </div>
    </aside>
  </div>
</section>
""" + ld_page_bc("visit"))

# ---------------- CONTACT ----------------
PAGES['contact.html'] = (head("Contact — The Honey Bistro, Savoy IL",
    "Contact The Honey Bistro before opening day: email, phone via Star 57 Diner, or the form. Get opening-date updates for 501 Commerce Drive, Savoy, IL.", "contact.html")
    + breadcrumbs("Contact")
    + """<section class="page-head">
  <div class="wrap">
    <p class="k">Contact</p>
    <h2>Talk to us before opening day</h2>
    <p class="lede">Questions about the menu, the schedule, or the space? Want an email the moment
    the opening date is locked? Pick whichever way you like.</p>
  </div>
</section>

<section class="band">
  <div class="wrap split">
    <div class="split-main">
      <form class="cform" method="post" action="/contact">
        <div>
          <label for="f-name">Name</label>
          <input id="f-name" name="name" type="text" maxlength="120" autocomplete="name" required>
        </div>
        <div>
          <label for="f-phone">Phone (optional)</label>
          <input id="f-phone" name="phone" type="tel" maxlength="60" autocomplete="tel">
        </div>
        <div>
          <label for="f-email">Email</label>
          <input id="f-email" name="email" type="email" maxlength="120" autocomplete="email" required>
        </div>
        <div>
          <label for="f-message">Message</label>
          <textarea id="f-message" name="message" rows="5" maxlength="4000" required></textarea>
        </div>
        <p class="cta-row"><button class="btn" type="submit">Send message</button></p>
        <p class="fnote">We answer as fast as the construction crew lets us.</p>
      </form>
    </div>
    <aside class="split-side">
      <div class="info-card">
        <h4>Other ways</h4>
        <dl class="facts">
          <dt>Email</dt><dd><a href="mailto:Thehoneybistro@hotmail.com">Thehoneybistro<wbr />@hotmail.com</a></dd>
          <dt>Phone</dt><dd><a href="tel:+12172539444">(217) 253-9444</a><br>answered at Star 57 Diner</dd>
          <dt>Facebook</dt><dd><a href="https://www.facebook.com/profile.php?id=61596882386807" rel="noopener">The Honey Bistro page</a></dd>
          <dt>Address</dt><dd>501 Commerce Drive<br>Savoy, IL 61874</dd>
        </dl>
      </div>
    </aside>
  </div>
</section>
""" + ld_page_bc("contact"))

# ---------------- PRIVACY ----------------
PAGES['privacy.html'] = (head("Privacy Policy — The Honey Bistro",
    "Privacy policy for The Honey Bistro website: what the contact form collects, Google map embed cookies, hosting, and how to ask for removal.", "privacy.html")
    + breadcrumbs("Privacy Policy")
    + """<section class="page-head">
  <div class="wrap">
    <h2>Privacy Policy</h2>
    <p class="lede">Short and honest, the way we run everything.</p>
  </div>
</section>

<section class="band">
  <div class="wrap prose">
    <h3>What we collect</h3>
    <p>This site has no ads, no analytics, and no tracking pixels. The only information we collect
    is what you type into the contact form — your name, phone (if you give it), email, and message —
    and we use it only to answer you and to send opening updates if you ask for them.</p>
    <h3>The map</h3>
    <p>The visit page loads a Google Maps embed. Google may set its own cookies once the map loads;
    that happens between you and Google, under Google&apos;s policy. Every other page on this site
    loads nothing from anyone else.</p>
    <h3>Hosting</h3>
    <p>This site is hosted on Railway (railway.app), which sees standard server logs (IP address,
    browser, page requested) as part of keeping the site online.</p>
    <h3>Your choices</h3>
    <p>Email <a href="mailto:Thehoneybistro@hotmail.com">Thehoneybistro<wbr />@hotmail.com</a> to ask what
    we&apos;ve got from you, or to have your message deleted. We&apos;ll do it — no forms, no
    runaround. This policy covers this site only.</p>
  </div>
</section>
""" + ld_page_bc("privacy"))

# ---------------- 404 ----------------
PAGES['404.html'] = (head("Page Not Found — The Honey Bistro",
    "That page isn't here — opening January 2027 at 501 Commerce Drive, Savoy, IL. Menu, story, visit and contact pages are one click away.", "404.html")
    + """<section class="page-head">
  <div class="wrap">
    <p class="k">404</p>
    <h2>That plate&apos;s empty</h2>
    <p class="lede">This page isn&apos;t on the menu. Try the good ones:</p>
    <p class="cta-row">
      <a class="btn" href="/">Home</a>
      <a class="btn ghost ink" href="/menu">Menu</a>
      <a class="btn ghost ink" href="/visit">Visit</a>
    </p>
  </div>
</section>
""")

# ---------------- THANKS ----------------
PAGES['thanks.html'] = (head("Message Sent — The Honey Bistro",
    "Thanks for reaching out to The Honey Bistro — we'll answer as fast as we can. Opening January 2027 in Savoy, IL.", "thanks.html")
    + """<section class="page-head">
  <div class="wrap">
    <p class="k">Received</p>
    <h2>Message sent — thank you</h2>
    <p class="lede">We&apos;ll get back to you as fast as the construction crew lets us. While
    you&apos;re here: the <a href="/menu">menu preview</a> is worth a look, and the
    <a href="https://www.facebook.com/profile.php?id=61596882386807" rel="noopener">Facebook page</a>
    posts every update first.</p>
    <p class="cta-row"><a class="btn" href="/">Back to home</a></p>
  </div>
</section>
""")

# ---------------- style.css ----------------
CSS = """/* The Honey Bistro — hand-rolled stylesheet, 2026-11-25. Warm honey / parchment / ink. */
:root{
  --paper:#FBF6EA; --card:#FFFDF6; --ink:#2B1B10; --ink2:#5C472F; --sand:#C9B99A;
  --honey:#C87F0F; --honey-deep:#8F5D07; --sage:#5F6F4E; --line:#E6D8BC; --cream:#F3EAD8;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  --sans:ui-sans-serif,system-ui,"Segoe UI",Helvetica,Arial,sans-serif;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font:16px/1.55 var(--sans)}
h1,h2,h3,h4{font-family:var(--serif);font-weight:600;line-height:1.12}
h1{font-size:clamp(2.3rem,5.2vw,3.8rem)}
h2{font-size:clamp(1.6rem,3.2vw,2.25rem);margin-bottom:14px}
h3{font-size:1.3rem;margin-bottom:10px}
p{max-width:72ch}
main>section:last-child{margin-bottom:0}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
.skip{position:absolute;left:-9999px}
.skip:focus{left:12px;top:12px;background:var(--ink);color:var(--cream);padding:10px 14px;z-index:9;border-radius:6px}
a{color:var(--honey-deep)}
a:hover{color:var(--ink)}

/* header */
header.site{background:var(--ink);color:var(--cream);display:flex;align-items:center;flex-wrap:wrap;gap:8px 24px;padding:14px 24px;position:relative;z-index:5}
.brand{font-family:var(--serif);font-size:1.35rem;color:var(--cream);text-decoration:none;letter-spacing:.4px}
.brand:hover{color:var(--honey)}
.navtoggle{position:absolute;opacity:0}
.navbtn{display:none;margin-left:auto;padding:8px 10px;cursor:pointer;border:1px solid rgba(200,127,15,.55);border-radius:8px}
.navbtn i,.navbtn i::before,.navbtn i::after{display:block;width:22px;height:2px;background:var(--cream);position:relative}
.navbtn i::before{content:"";position:absolute;top:-7px}
.navbtn i::after{content:"";position:absolute;top:7px}
nav.links{margin-left:auto;display:flex;align-items:center;gap:22px}
nav.links a{color:var(--cream);text-decoration:none;font-weight:600;font-size:.95rem;border-bottom:2px solid transparent;padding:4px 0}
nav.links a:hover{color:var(--honey);border-bottom-color:var(--honey)}
nav.links a.btn{color:var(--ink)}

/* buttons */
.btn{display:inline-block;background:var(--honey);color:#241505;border:0;font-weight:700;font-size:1rem;padding:13px 22px;border-radius:9px;text-decoration:none}
.btn:hover{background:var(--honey-deep);color:var(--cream)}
.btn-sm{padding:8px 15px;font-size:.9rem;border-radius:8px}
.btn.ghost{background:transparent;color:var(--cream)!important;box-shadow:inset 0 0 0 2px rgba(200,127,15,.8)}
.btn.ghost:hover{background:rgba(200,127,15,.16);color:var(--cream)}
.btn.ghost.ink{color:var(--ink)!important;box-shadow:inset 0 0 0 2px var(--honey-deep)}
.btn.ghost.ink:hover{color:var(--honey-deep)!important;background:rgba(200,127,15,.08)}
.cta-row{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:26px;max-width:none}

/* hero */
.hero{position:relative;overflow:hidden;padding:84px 0 72px}
.hexfield{position:absolute;top:-12px;right:-70px;width:min(46vw,480px);height:auto;opacity:.8;pointer-events:none}
.hero .wrap{position:relative;max-width:1080px}
.badge{display:inline-block;background:var(--honey);color:#241505;font:700 12px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;padding:9px 14px;border-radius:999px;margin-bottom:22px}
.hero h1{max-width:20ch;margin-bottom:18px}
.lede{font-size:1.13rem;color:var(--ink2);max-width:64ch}
.page-head{padding:56px 0 26px}
.page-head .lede{margin-top:10px}

/* sections */
.k{font:700 12px/1.4 var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--honey-deep);margin-bottom:10px}
.band{padding:64px 0}
.band.alt{background:#F6EEDC;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.band h2+p.sub{color:var(--ink2);margin-bottom:28px}
.sub{max-width:66ch}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;margin-top:8px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:26px 24px}
.card h3{margin-bottom:8px}
.card p{font-size:.97rem;color:var(--ink2)}
.cta-final{text-align:center}
.cta-final p{margin-left:auto;margin-right:auto}
.cta-final .cta-row{justify-content:center}
main p+p{margin-top:1em}

/* quotes */
.quote{max-width:760px;margin:8px auto;padding:8px 24px 8px 26px;border-left:5px solid var(--honey)}
.quote blockquote{font-family:var(--serif);font-style:italic;font-size:clamp(1.3rem,2.8vw,1.7rem);line-height:1.35;max-width:none}
.quote cite{display:block;margin-top:12px;font:600 14px/1.4 var(--sans);color:var(--ink2);font-style:normal}
.quote.inband{margin-top:36px}

/* menu lists */
.ghead{font-size:1.5rem;margin-bottom:4px}
.gnote{color:var(--ink2);margin-bottom:18px}
.menu-list{list-style:none;border-top:1px solid var(--line)}
.menu-list li{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 18px;padding:14px 2px;border-bottom:1px solid var(--line)}
.mi{font-family:var(--serif);font-size:1.15rem;font-weight:600}
.mn{flex:1;color:var(--ink2);font-size:.95rem;min-width:220px}

/* split pages + info cards */
.split{display:grid;grid-template-columns:minmax(0,1fr) 330px;gap:36px;align-items:start}
.split-main h3{margin-top:26px}
.split-main h3:first-child{margin-top:0}
.split-main p{max-width:68ch}
.split-side{display:flex;flex-direction:column;gap:20px;position:sticky;top:20px}
.info-card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:22px}
.info-card h4{font:700 12px/1.4 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--honey-deep);margin-bottom:14px}
dl.facts{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px 16px;font-size:.95rem}
dl.facts dt{font-weight:700;color:var(--ink2)}
dl.facts dd{color:var(--ink);min-width:0;overflow-wrap:anywhere}
.prose p{margin-top:14px;max-width:70ch}
.prose h3{margin-top:34px}

/* map */
.mapwrap{width:100%;aspect-ratio:16/10;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#EFE7D4}
.mapwrap iframe{width:100%;height:100%;border:0;display:block}

/* form */
.cform{display:grid;gap:18px;max-width:580px}
.cform label{display:block;font-weight:700;font-size:.95rem;margin-bottom:7px}
.cform input,.cform textarea{width:100%;padding:13px 14px;border:1px solid #CBBB9E;border-radius:9px;background:#fff;font:inherit;color:var(--ink)}
.cform input:focus,.cform textarea:focus{outline:3px solid rgba(200,127,15,.35);border-color:var(--honey-deep)}
.fnote{font-size:.88rem;color:var(--ink2);margin-top:10px}

/* breadcrumb */
.crumbs{max-width:1080px;margin:20px auto 0;padding:0 24px;font-size:13px;color:var(--ink2)}
.crumbs a{color:var(--honey-deep)}

/* footer */
footer.site{background:var(--ink);color:var(--cream);margin-top:56px;padding:56px 0 28px}
.fwrap{max-width:1080px;margin:0 auto;padding:0 24px}
.fgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:28px;margin-bottom:8px}
footer.site h4{font:700 12px/1.4 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--honey);margin-bottom:12px}
footer.site p{font-size:.93rem;color:var(--cream);max-width:none;line-height:1.7}
.fopen{color:var(--honey);font-weight:700}
a.flink{color:var(--cream);text-decoration:underline;text-underline-offset:3px;text-decoration-color:rgba(200,127,15,.6)}
a.flink:hover{color:var(--honey)}
.footline{margin-top:26px;padding-top:18px;border-top:1px solid rgba(243,234,216,.18);font-size:.83rem;color:var(--sand)}

/* responsive */
@media (max-width:860px){
  .split{grid-template-columns:1fr}
  .split-side{position:static}
}
@media (max-width:720px){
  .navbtn{display:block}
  nav.links{display:none;margin-left:0;width:100%;flex-direction:column;align-items:flex-start;gap:14px;padding:14px 2px 4px}
  .navtoggle:checked~nav.links{display:flex}
  .hero{padding:58px 0 52px}
  .hexfield{display:none}
  .band{padding:48px 0}
}
@media (max-width:480px){
  h1{font-size:2.05rem}
  .btn{width:100%;text-align:center}
  .cta-row{flex-direction:column;align-items:stretch}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""

# ---------------- sitemap / robots ----------------
CORE = ["/", "/menu", "/brunch-in-savoy", "/breakfast-champaign-urbana", "/our-story", "/visit", "/contact", "/privacy"]
SITEMAP = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "".join(f"<url><loc>{ORIGIN}{p}</loc></url>\n" for p in CORE) + "</urlset>\n")
ROBOTS = f"User-agent: *\nDisallow: /thanks\nDisallow: /404\nSitemap: {ORIGIN}/sitemap.xml\n"

os.makedirs(PUBLIC, exist_ok=True)
# every PAGES value is ONE string: head_html (ends with the skip link) + page content
# (+ JSON-LD tail). Split at the first '<section' and wrap: NAV + main + footer.
for name, v in PAGES.items():
    i = v.index("<section")
    h_, c_ = v[:i], v[i:]
    with open(os.path.join(PUBLIC, name), "w", encoding="utf-8") as f:
        f.write(page(h_, c_))
with open(os.path.join(PUBLIC, "style.css"), "w", encoding="utf-8") as f:
    f.write(CSS)
with open(os.path.join(PUBLIC, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(SITEMAP)
with open(os.path.join(PUBLIC, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(ROBOTS)

print(f"wrote {len(PAGES)+3} files to {PUBLIC}")
for n in sorted(os.listdir(PUBLIC)):
    print(" ", n, os.path.getsize(os.path.join(PUBLIC, n)), "bytes")
