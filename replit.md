# LawBuddy Portugal

AI-powered assistant that explains Portuguese laws, bureaucracy, and compliance exclusively to international tourists, digital nomads, and expats — with a freemium business model monetised via Whop.

## Run & Operate

- `LawBuddy Portugal` workflow — runs the Streamlit app on port 5000
- Command: `.venv/bin/python3 -m streamlit run app.py --server.port 5000`
- Python deps live in `.venv/` (created with `python3 -m venv .venv`)
- To reinstall deps: `.venv/bin/pip install streamlit openai`

## Stack

- Python 3.13, Streamlit 1.58+, OpenAI Python SDK
- Session state for freemium quota tracking (no database needed)

## Where things live

- `app.py` — entire application (single-file Streamlit app)
- `.streamlit/config.toml` — server config (port 5000, headless)
- `.venv/` — Python virtual environment (gitignored)
- `requirements.txt` — pinned Python dependencies

## Product

LawBuddy Portugal is a legal information assistant for Portugal, strictly scoped to Portuguese jurisdiction. Features:

- **AI chat** — GPT-4o, system-prompted to only answer Portuguese law questions
- **User profiles** — Tourist / Digital Nomad / Golden Visa / Long-term Expat
- **Freemium model** — 2 chat tabs + 5 messages free; lockout with upgrade CTA
- **Whop paywall** — $19/mo unlock via Whop checkout link
- **Share-to-unlock** — WhatsApp share earns +3 bonus questions (with 4-digit code verification)
- **Cooldown** — 30-second rate limit between messages for free users (anti-bot)
- **Emergency sidebar** — 112, SNS 24, AIMA, PSP contacts
- **GDPR** — "Clear All My Data" button wipes all session state

## User preferences

- UI language: English
- Payment: Whop ($19/mo) — update `WHOP_URL` in `app.py` with your real checkout link

## Architecture decisions

- Single `app.py` file as requested; all state in `st.session_state` (no DB)
- Message quota increments only after a successful AI response (failed calls don't burn free quota)
- WhatsApp URLs use `urllib.parse.quote()` so `#` in invite codes is properly encoded
- XSRF protection left enabled (Streamlit default) for security

## Gotchas

- The `.venv` Python must be used explicitly (`.venv/bin/python3 -m streamlit`) — the venv shebang resolves to system Python which can't find the packages
- Update `WHOP_URL` constant in `app.py` before going live
- `OPENAI_API_KEY` must be set as a Replit Secret
