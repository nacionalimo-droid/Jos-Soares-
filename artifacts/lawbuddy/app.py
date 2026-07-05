import streamlit as st
import os
import time
import random
import string
import urllib.parse
import google.generativeai as genai

# ── Page config (must be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="LawBuddy Portugal",
    page_icon="🇵🇹",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Gemini client ─────────────────────────────────────────────────────────
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ── Constants ─────────────────────────────────────────────────────────────
FREE_MAX_TABS = 2
FREE_MAX_MESSAGES = 5
COOLDOWN_SECONDS = 30
WHOP_URL = "https://whop.com/lawbuddy-portugal"

SYSTEM_PROMPT = """You are LawBuddy Portugal — an expert EXCLUSIVELY in Portuguese jurisdiction, laws, bureaucracy, and compliance. Your audience is international tourists, digital nomads, and expats traveling to or living in PORTUGAL.

Rules:
1. ONLY answer questions about Portuguese law, regulations, bureaucracy, immigration, taxes, visas, and compliance within Portugal.
2. If a user asks about laws or regulations of ANY other country (China, USA, UK, Brazil, etc.), politely decline and say: "LawBuddy Portugal only provides legal assistance for Portugal. I'm not able to help with laws outside of Portugal."
3. Always adapt your advice to the user's stated profile (Tourist, Digital Nomad, Golden Visa holder, Long-term Expat).
4. Speak like a wise, protective, and welcoming local Portuguese counselor. Avoid complex legal jargon — translate laws into clear, simple English.
5. Mention official sources when relevant (e.g., AIMA, SEF, AT - Autoridade Tributária, Portal das Finanças).
6. End EVERY response with this exact italic note on a new line: "*Note from LawBuddy Portugal: This consultation is for informational purposes only regarding Portuguese law and compliance. It does not substitute official legal counsel from a Portuguese lawyer.*"
"""

PORTUGAL_TIPS = [
    "🛂 **90-Day Rule**: Tourists from non-EU countries may stay up to 90 days in any 180-day period in the Schengen Area.",
    "💼 **Digital Nomad Visa**: Portugal's D8 Visa requires proof of remote income ≥ €3,480/month (2026 update).",
    "🏠 **NHR Tax Regime**: New residents may qualify for a 20% flat tax on Portuguese-source income for 10 years.",
    "🚗 **Driving in Portugal**: EU driving licences are valid. Non-EU licences valid for 185 days; then exchange required.",
    "🏖️ **Tourist Tax (2026)**: Lisbon €2/night, Porto €3/night, Algarve municipalities €1–2/night.",
    "📋 **AIMA Appointments**: Immigration appointments (formerly SEF) via aima.gov.pt — book well in advance.",
    "💰 **Golden Visa**: Investment fund route from €500,000. Real estate route mostly closed since 2023.",
    "🏥 **SNS Health**: EU citizens with EHIC card can use National Health Service. Non-EU need private insurance.",
]

# ── Session state initialisation ──────────────────────────────────────────
def init_session():
    if "tabs" not in st.session_state:
        st.session_state.tabs = [{"id": 0, "name
