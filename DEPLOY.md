# honey-bistro — deploy record (websites lane)

Shop: The Honey Bistro — 501 Commerce Drive, Savoy IL 61874 (Zekjiri family / Star 57 Diner; opening Jan 2027). Card: t_8ff55c07 (board: websites).

## Live topology (as of 2026-11-25)
- Origin (preview): https://honey-bistro-demo.up.railway.app  (noindex — demo host, keep tag forever, strip only at owner-domain delivery)
- Railway: workspace "Ramon Leon's Projects", **project the-plain-bar** (`604a72a9-09eb-4169-920d-e64619651640`) — CO-HOSTED shell (account-wide project cap; do NOT create projects, do NOT `railway project delete` here — capitol-locksmith-demo + ~11 other services share it)
- Service: `honey-bistro-demo` id `77271220-ca32-4e0a-ac29-8cfea85dd016`
- GitHub (public, no secrets): https://github.com/gnaritas/honey-bistro (main; render evidence committed in renders/)
- Durable mirror: ~/.hermes/projects/websites/sites/honey-bistro (generator `build_pages.py` = single source for all 10 pages; server.js static+/contact+ /open pixel; public/ is generated output)

## Deploy commands
- Build pages: `python3 build_pages.py` (from this dir; pins the -demo host)
- Gate: `python3 /Users/rleon/sites/_verify.py public https://honey-bistro-demo.up.railway.app` (must print PASS; 10 pages)
- Deploy: `railway up -d -y -s honey-bistro-demo` (service name carries -demo suffix; multi-service project → -s required)
- Bookkeeping after deploy: `sites_agency_state.py set deploy honey-bistro ...` + `export` then `verify` (all IDENTICAL)

## Form relay
- Contact form POST /contact → server.js → Brevo HTTP API (api.brevo.com/v3/smtp/email, htmlContent/textContent keys, header `api-key:`, env BREVO_API_KEY — extract from secrets/brevo_smtp_key.txt from "xkeysib" onward, label prefix trap) → lane mailbox jarvis+websites@onsmalltalk.com; 303 → /thanks.
- Verified live 2026-11-25 02:1x PST: test submit 303 + Railway logs MAILSENT (attempt-1 checkpoint). Mail goes to the LANE until delivery flips recipient handling.

## Teardown (GARBAGE RULE) — serviceDelete ONLY
- `railway service delete -s 77271220-ca32-4e0a-ac29-8cfea85dd016 -y --json` (from linked dir; NEVER project delete — shared shell)
- `gh repo delete gnaritas/honey-bistro --yes`
- `sites_agency_state.py delete deploy honey-bistro` + `delete service 77271220-ca32-4e0a-ac29-8cfea85dd016` + `export` + `verify`
- rm -rf this mirror dir + scratch ~/sites clone if present

## Pitch posture
- Recipient: Thehoneybistro@hotmail.com — self-published on the shop's OWN FB Page intro (id 61596882386807; address 501 Commerce Dr + phone 217-819-8222 = press-named business). Greeting: Nita (quoted co-owner in News-Gazette + Smile Politely).
- Arm coin sha256('honey-bistro')%2 = 1 → v7 subject "Website demo for The Honey Bistro". Founder bundle $249 + $39/mo (31-day trial), link 14A14ockBahRdfIcb93ks09.
- Shop tz America/Chicago (seeded shop_tz). t2 ladder due 2026-12-03; mature_on 2026-12-10.
- Homonym guard: "Blue Honey Bistro" Memphis TN = different business; honeybistro.com + star57.com = namebright-parked 3P domains, NOT shop property (registry homonym_guard row 2026-11-25).
- Send kit: _pitch_honey-bistro.md / .envelope.json / .send.py in projects/websites (grampys-hardened clone; --check-only PASS 2026-11-25 02:5x PST: 109 words, 2 links, guards clean, parked-claim holds, MX ok).
