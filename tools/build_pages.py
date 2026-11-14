"""Build the generated pages of lr2b.com: one page per product (work/<slug>/), privacy/, terms/ and 404.html.

The home page (index.html) is hand-written. Everything here shares one header and footer, so edit this
file and run it instead of editing the generated HTML:

    python tools/build_pages.py
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS_VERSION = "20261115c"  # bump together with index.html when assets/home.css changes

FIRE_PLAY = "https://play.google.com/store/apps/details?id=com.firevpn.vpnx"
FIRE_IOS = "https://apps.apple.com/us/app/vpn-by-firevpn/id6464175174"
ZF_PLAY = "https://play.google.com/store/apps/details?id=net.atallah.zforex.zforexsignals"

PRODUCTS = [
    dict(slug="firevpn", name="FireVPN", kind="VPN app", status="Live",
         lead="A free VPN for Android and iPhone. The apps, the API and the servers are all ours.",
         built=["Android app and iPhone app", "VPN API: accounts, sessions and the server list",
                "OpenVPN server fleet, set up and managed over SSH", "Product site with clear data and privacy pages"],
         facts=[("Platforms", "Android 7.0+ · iOS 14+"), ("Price", "Free, paid by ads")],
         stack="Android · iOS · Python · Flask · MySQL · Celery · OpenVPN",
         links=[("Google Play", FIRE_PLAY, "dark"), ("App Store", FIRE_IOS, "line"), ("firevpn.net", "https://firevpn.net/", "text")]),
    dict(slug="zproxies", name="ZProxies", kind="Proxy platform", status="Live",
         lead="IPv6 datacenter proxies by country, sold by the month and set up on our own nodes.",
         built=["Orders, invoices and account balance", "Card and crypto payments",
                "Proxies set up automatically on our proxy nodes", "Customer dashboard and API"],
         facts=[("Price", "From $4.99/mo for 50 IPs"), ("Plans", "50 to 2,000 IPv6 addresses")],
         stack="Python · Flask · MySQL · Celery · Squid · IPv6",
         links=[("zproxies.com", "https://zproxies.com/", "primary")]),
    dict(slug="zasend", name="ZaSend", kind="Email API", status="Beta",
         lead="Transactional email by API or SMTP, sent from your own domain.",
         built=["REST API and SMTP submission", "DKIM signing and domain setup checks",
                "Delivery, bounce handling and webhooks", "Dashboard and admin panel"],
         facts=[("Status", "Beta"), ("Free tier", "100 emails a day")],
         stack="Python · Flask · Celery · Postfix",
         links=[("zasend.com", "https://zasend.com/", "primary")]),
    dict(slug="proxy11", name="Proxy11", kind="Proxy API", status="Live",
         lead="Free proxy lists and a simple proxy API.",
         built=["Proxy lists as TXT, JSON, CSV or XML", "Python and Node.js SDKs",
                "Free proxy checker", "Our own scanner keeps the lists fresh"],
         facts=[("Plans", "Free and paid"), ("Formats", "TXT · JSON · CSV · XML")],
         stack="Python · Flask · proxy scanner on our own server",
         links=[("proxy11.com", "https://proxy11.com/", "primary")]),
    dict(slug="heldercheck", name="HelderCheck", kind="Calculators", status="Live",
         lead="Dutch calculators for everyday money questions.",
         built=["Calculators for income, housing, transport, energy and work", "Source and validity date on every result",
                "Search and categories", "No account needed"],
         facts=[("Language", "Dutch"), ("Price", "Free")],
         stack="Python · Flask",
         links=[("heldercheck.nl", "https://heldercheck.nl/", "primary")]),
    dict(slug="freetoolo", name="FreeToolo", kind="Web tools", status="Live",
         lead="Browser tools and website checks for everyday web work.",
         built=["SEO checker", "Full website audit", "Sitemap generator", "Developer and image tools"],
         facts=[("Price", "Free tools, Pro checks")],
         stack="Python · Flask",
         links=[("freetoolo.com", "https://freetoolo.com/", "primary")]),
    dict(slug="vpnnu", name="VPNNu", kind="VPN service", status="Live",
         lead="Free OpenVPN profiles with Dutch setup guides.",
         built=["Personal OpenVPN profiles", "Setup guides per device, in Dutch",
                "Node manager that installs and runs the VPN servers", "Free tools: VPN check, leak test, config checker"],
         facts=[("Protocol", "OpenVPN"), ("Price", "Free")],
         stack="Python · Flask · SQLite · OpenVPN",
         links=[("vpnnu.nl", "https://vpnnu.nl/", "primary")]),
    dict(slug="zforex", name="ZForex", kind="Forex signals", status="Public test",
         lead="Forex signals with an entry, a target and a stop, and an Android app for alerts.",
         built=["Rule-based signal engine, tested on years of price data", "Live scanner on our own market-data server",
                "Public track record of every signal", "Android app with alerts"],
         facts=[("Status", "Public test since 14 Nov 2026"), ("Pairs", "4")],
         stack="Python · Flask · MySQL · Android · Firebase",
         links=[("zforex.net", "https://zforex.net/", "primary"), ("Android app", ZF_PLAY, "line")]),
]

PRIVACY = ("Privacy Policy", "15 November 2026", [
    ("What we receive", "When you email LR2B, directly or through the form on the home page (which only opens your own email app), "
     "we receive what you choose to send: your name, email address, project details, links and files. Our host, Cloudflare, "
     "processes basic technical data such as your IP address and browser type to deliver and protect the website."),
    ("How we use it", "We use it to reply to you, discuss and deliver projects, prevent abuse and keep basic business records. "
     "We do not sell personal information."),
    ("Cookies and tracking", "This website sets no cookies and runs no analytics or advertising trackers. Fonts and images are "
     "served from lr2b.com itself."),
    ("Our products and other sites", "Links lead to our products and to third-party sites such as Google Play and the App Store. "
     "Each of our products has its own privacy policy on its own website, and third-party sites follow their own policies."),
    ("How long we keep it", "We keep project and contact information only as long as needed for communication, delivery, "
     "records, security or legal requirements."),
    ("Contact", 'For privacy questions or requests, email <a href="mailto:contact@lr2b.com">contact@lr2b.com</a>.'),
])

TERMS = ("Terms of Service", "21 May 2026", [
    ("Use of this website", "By using lr2b.com, you agree to use the website lawfully and not attempt to disrupt, copy, abuse, "
     "or misuse the site, its content, or its infrastructure."),
    ("Project work", "Project scope, pricing, timelines, deliverables, revisions, ownership, and payment terms are agreed "
     "separately before work begins. Messages through this website do not create a service agreement until both sides "
     "confirm the project terms."),
    ("Client responsibilities", "Clients are responsible for providing accurate requirements, legal content, required access, "
     "approvals, and any rights or permissions needed for materials supplied to LR2B."),
    ("Third-party services", "Some projects may use hosting providers, APIs, payment processors, analytics tools, marketplaces, "
     "or other third-party services. LR2B is not responsible for outages, policy changes, pricing changes, or actions by "
     "third-party providers."),
    ("No guarantees", "We aim to build reliable, practical software, but the website and services are provided without "
     "guarantees of uninterrupted operation, specific rankings, revenue, trading results, or business outcomes."),
    ("Limitation of liability", "To the fullest extent permitted by law, LR2B is not liable for indirect, incidental, special, "
     "consequential, or punitive damages arising from use of this website or related services."),
    ("Contact", 'For questions about these terms, email <a href="mailto:contact@lr2b.com">contact@lr2b.com</a>.'),
])


def e(s):
    return html.escape(s, quote=True)


def head(title, desc, path, image="/assets/og-image.png", ld=None, robots="index, follow"):
    url = f"https://lr2b.com{path}"
    ld_tag = f'\n    <script type="application/ld+json">{json.dumps(ld)}</script>' if ld else ""
    canonical = f'\n    <link rel="canonical" href="{url}">' if robots.startswith("index") else ""
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{e(title)}</title>
    <meta name="description" content="{e(desc)}">
    <meta name="robots" content="{robots}">{canonical}
    <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
    <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{e(title)}">
    <meta property="og:description" content="{e(desc)}">
    <meta property="og:image" content="https://lr2b.com{image}">
    <meta property="og:site_name" content="LR2B">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preload" href="/assets/fonts/ibm-plex-sans.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="/assets/home.css?v={CSS_VERSION}">{ld_tag}
  </head>
  <body>
    <a class="skip" href="#main">Skip to content</a>
    <header class="site-header">
      <div class="wrap header-row">
        <a class="logo" href="/" aria-label="LR2B home"><span>LR2B</span></a>
        <nav class="nav" aria-label="Main">
          <a href="/#products">Products</a>
          <a href="/#how">How we work</a>
          <a href="/#build">Custom builds</a>
          <a class="nav-mail" href="mailto:contact@lr2b.com">contact@lr2b.com</a>
        </nav>
      </div>
    </header>
"""


FOOT = """    <footer class="site-footer">
      <div class="wrap footer-row">
        <span>© 2026 LR2B</span>
        <nav aria-label="Footer">
          <a href="/#products">Products</a>
          <a href="/#build">Custom builds</a>
          <a href="/privacy/">Privacy</a>
          <a href="/terms/">Terms</a>
          <a href="mailto:contact@lr2b.com">contact@lr2b.com</a>
        </nav>
      </div>
    </footer>
  </body>
</html>
"""


def button(label, href, style):
    if style == "text":
        return f'<a class="text-link" href="{e(href)}">{e(label)} <span aria-hidden="true">↗</span></a>'
    cls = {"primary": "btn btn-primary", "dark": "btn btn-dark", "line": "btn btn-line"}[style]
    return f'<a class="{cls}" href="{e(href)}">{e(label)}</a>'


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def product_page(i, p):
    nxt = PRODUCTS[(i + 1) % len(PRODUCTS)]
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "LR2B", "item": "https://lr2b.com/"},
        {"@type": "ListItem", "position": 2, "name": "Products", "item": "https://lr2b.com/#products"},
        {"@type": "ListItem", "position": 3, "name": p["name"], "item": f"https://lr2b.com/work/{p['slug']}/"}]}
    tag = "tag" if p["status"] == "Live" else "tag tag-soft"
    built = "\n".join(f"            <li>{e(b)}</li>" for b in p["built"])
    facts = "\n".join(f"            <div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in p["facts"])
    links = "\n            ".join(button(*l) for l in p["links"])
    body = f"""
    <main id="main" class="wrap product-page">
      <nav class="crumbs mono" aria-label="Breadcrumb"><a href="/">LR2B</a> / <a href="/#products">Products</a> / <span aria-current="page">{e(p['name'])}</span></nav>
      <section class="product-head">
        <div>
          <p class="mono muted">{e(p['kind'])} <span class="{tag}">{e(p['status'])}</span></p>
          <h1>{e(p['name'])}</h1>
          <p class="lead">{e(p['lead'])}</p>
          <div class="actions">
            {links}
          </div>
        </div>
        <div class="product-side">
          <h2>What we built</h2>
          <ul class="kinds">
{built}
          </ul>
          <dl class="product-facts">
{facts}
          </dl>
        </div>
      </section>
      <figure class="product-shot">
        <img src="/assets/work/full/{p['slug']}.webp" alt="{e(p['name'])} website" width="1200" height="758" decoding="async">
      </figure>
      <p class="mono stack">{e(p['stack'])}</p>
      <div class="product-next">
        <a class="text-link" href="/#products">All products</a>
        <a class="text-link" href="/work/{nxt['slug']}/">Next: {e(nxt['name'])} <span aria-hidden="true">→</span></a>
      </div>
    </main>
"""
    title = f"{p['name']}: {p['kind']} | LR2B"
    desc = f"{p['name']} by LR2B. {p['lead']}"
    write(f"work/{p['slug']}/index.html",
          head(title, desc, f"/work/{p['slug']}/", image=f"/assets/og/{p['slug']}.jpg", ld=ld) + body + FOOT)


def legal_page(slug, doc):
    title, updated, sections = doc
    secs = "\n".join(f"        <section>\n          <h2>{e(h)}</h2>\n          <p>{t}</p>\n        </section>" for h, t in sections)
    body = f"""
    <main id="main" class="wrap legal">
      <h1>{e(title)}</h1>
      <p class="mono muted">Last updated {e(updated)}</p>
      <article>
{secs}
      </article>
    </main>
"""
    write(f"{slug}/index.html", head(f"{title} | LR2B", f"{title} for lr2b.com.", f"/{slug}/") + body + FOOT)


def not_found():
    body = """
    <main id="main" class="wrap legal">
      <h1>Page not found</h1>
      <p class="lead">This page does not exist, or it moved.</p>
      <div class="actions">
        <a class="btn btn-primary" href="/">Home</a>
        <a class="btn btn-line" href="/#products">All products</a>
      </div>
    </main>
"""
    write("404.html", head("Page not found | LR2B", "This page does not exist.", "/404", robots="noindex") + body + FOOT)


if __name__ == "__main__":
    for i, p in enumerate(PRODUCTS):
        product_page(i, p)
    legal_page("privacy", PRIVACY)
    legal_page("terms", TERMS)
    not_found()
    print(f"built {len(PRODUCTS)} product pages, privacy, terms, 404")
