import urllib.parse
from openai import OpenAI

# ── Page config (must be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="LawBuddy Portugal",
    page_icon="🇵🇹",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── OpenAI client ─────────────────────────────────────────────────────────
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))

# ── Constants ─────────────────────────────────────────────────────────────
FREE_MAX_TABS = 2
FREE_MAX_MESSAGES = 5
COOLDOWN_SECONDS = 30
WHOP_URL = "https://whop.com/lawbuddy-portugal"  # Update with your real Whop link

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
        st.session_state.tabs = [{"id": 0, "name": "Consultation #1", "messages": [], "profile": None}]
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = 0
    if "total_messages" not in st.session_state:
        st.session_state.total_messages = 0
    if "is_premium" not in st.session_state:
        st.session_state.is_premium = False
    if "share_code" not in st.session_state:
        st.session_state.share_code = "#LB" + "".join(random.choices(string.digits, k=2)) + random.choice(string.ascii_uppercase) + random.choice(string.digits)
    if "bonus_messages" not in st.session_state:
        st.session_state.bonus_messages = 0
    if "last_message_time" not in st.session_state:
        st.session_state.last_message_time = 0
    if "verified_shares" not in st.session_state:
        st.session_state.verified_shares = set()
    if "tab_counter" not in st.session_state:
        st.session_state.tab_counter = 1

init_session()

# ── Helper functions ──────────────────────────────────────────────────────
def get_current_tab():
    for tab in st.session_state.tabs:
        if tab["id"] == st.session_state.active_tab:
            return tab
    if st.session_state.tabs:
        st.session_state.active_tab = st.session_state.tabs[0]["id"]
        return st.session_state.tabs[0]
    return None

def message_limit():
    return FREE_MAX_MESSAGES + st.session_state.bonus_messages

def is_locked():
    if st.session_state.is_premium:
        return False
    return st.session_state.total_messages >= message_limit()

def cooldown_remaining():
    if st.session_state.is_premium:
        return 0
    elapsed = time.time() - st.session_state.last_message_time
    remaining = COOLDOWN_SECONDS - elapsed
    return max(0, int(remaining))

def add_new_tab():
    if not st.session_state.is_premium and len(st.session_state.tabs) >= FREE_MAX_TABS:
        return False
    st.session_state.tab_counter += 1
    new_id = st.session_state.tab_counter
    st.session_state.tabs.append({
        "id": new_id,
        "name": f"Consultation #{new_id}",
        "messages": [],
        "profile": None,
    })
    st.session_state.active_tab = new_id
    return True

def clear_all_data():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    init_session()
    st.rerun()

def get_ai_response(messages, profile):
    """Call OpenAI API with the conversation history."""
    try:
        system = SYSTEM_PROMPT
        if profile:
            system += f"\n\nUser profile: {profile}. Tailor your answer accordingly (e.g., 90-day Schengen rule for tourists, NHR/D8 visa details for digital nomads, etc.)."

        openai_messages = [{"role": "system", "content": system}]
        for m in messages:
            openai_messages.append({"role": m["role"], "content": m["content"]})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=openai_messages,
            max_tokens=1024,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ An error occurred while contacting the AI: {str(e)}\n\n*Note from LawBuddy Portugal: This consultation is for informational purposes only regarding Portuguese law and compliance. It does not substitute official legal counsel from a Portuguese lawyer.*"

# ── SIDEBAR ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🇵🇹 LawBuddy Portugal")
    st.caption("Your AI Legal Guide in Portugal")
    st.divider()

    # New consultation button
    if st.button("➕ New Consultation", use_container_width=True, type="primary"):
        if add_new_tab():
            st.rerun()
        else:
            st.error("🔒 Free plan allows up to 2 consultations. Upgrade to Whop for unlimited!")

    # Usage indicator (free users)
    if not st.session_state.is_premium:
        msgs_used = st.session_state.total_messages
        msgs_max = message_limit()
        tabs_used = len(st.session_state.tabs)
        st.progress(min(msgs_used / max(msgs_max, 1), 1.0))
        st.caption(f"Messages: {msgs_used}/{msgs_max} | Tabs: {tabs_used}/{FREE_MAX_TABS}")

    st.divider()

    # Conversation history (tabs list)
    st.subheader("💬 My Consultations")
    for tab in st.session_state.tabs:
        is_active = tab["id"] == st.session_state.active_tab
        label = f"{'▶ ' if is_active else ''}{tab['name']}"
        if st.button(label, key=f"tab_btn_{tab['id']}", use_container_width=True):
            st.session_state.active_tab = tab["id"]
            st.rerun()

    st.divider()

    # Portugal compliance tips
    st.subheader("📌 Top Portugal Tips")
    tips_today = random.sample(PORTUGAL_TIPS, 3)
    for tip in tips_today:
        st.info(tip)

    st.divider()

    # Emergency contacts
    st.subheader("🚨 Portugal Emergency Contacts")
    st.error("**112** — General Emergency (Police, Fire, Ambulance)")
    st.warning("**808 24 24 24** — SNS 24 National Health Line")
    st.info("**+351 211 940 278** — AIMA Immigration Support")
    st.info("**217 814 100** — PSP (Public Security Police)")
    st.info("**800 204 204** — DGS Health Line (free)")

    st.divider()

    # GDPR clear button
    if st.button("🗑️ Clear All My Data & History", use_container_width=True, type="secondary"):
        clear_all_data()


# ── MAIN CONTENT ──────────────────────────────────────────────────────────
current_tab = get_current_tab()

# Header
col1, col2 = st.columns([4, 1])
with col1:
    st.title("🇵🇹 LawBuddy Portugal")
    st.caption("**Your Legal Guide in Portugal** — AI-powered advice on Portuguese law & compliance")
with col2:
    if st.session_state.is_premium:
        st.success("✅ Premium")
    else:
        st.info(f"🆓 Free Plan")

st.divider()

if current_tab is None:
    st.warning("No consultation selected. Click '➕ New Consultation' in the sidebar.")
    st.stop()

# Profile selector (shown once per tab)
# Use a flat session_state key as the source of truth (more reliable than nested dict mutation)
_profile_state_key = f"tab_profile_{current_tab['id']}"
if _profile_state_key in st.session_state and st.session_state[_profile_state_key]:
    current_tab["profile"] = st.session_state[_profile_state_key]

if current_tab["profile"] is None:
    st.subheader("👤 To give you accurate advice, what is your current status in Portugal?")
    profile_choice = st.selectbox(
        "Select your profile:",
        ["— Please select —", "Short-term Tourist", "Digital Nomad / Remote Worker", "Golden Visa / Investor", "Long-term Expat"],
        key=f"profile_select_{current_tab['id']}",
    )
    if profile_choice == "— Please select —":
        st.info("Please select your profile to begin your consultation.")
        st.stop()
    else:
        current_tab["profile"] = profile_choice
        st.session_state[_profile_state_key] = profile_choice
        # No rerun needed — continue rendering the chat below

# Show profile badge
st.caption(f"Profile: **{current_tab['profile']}** | Consultation: *{current_tab['name']}*")

# ── LOCKOUT SCREEN ────────────────────────────────────────────────────────
if is_locked():
    st.divider()
    st.markdown(
        """
        <div style='text-align:center; padding:2rem 1rem;'>
            <h2>🔒 Your Free LawBuddy Portugal Memory Has Expired</h2>
            <p style='font-size:1.1rem; max-width:600px; margin:auto;'>
                Upgrade now to unlock <strong>unlimited AI consultations</strong> about Portuguese law,
                permanent chat history, and automated real-time local law alerts.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
    code = st.session_state.share_code
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown(f"### 📢 Share & Earn Free Questions")
        st.markdown(f"Your invite code: **`{code}`**")
        whatsapp_text = f"Check out LawBuddy Portugal! Your personal AI legal guide in Portugal. Use my invite code {code} to get started! 🇵🇹"
        whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(whatsapp_text)}"
        st.link_button("📢 Share on WhatsApp for +3 Free Questions", whatsapp_url, use_container_width=True)

        st.markdown("**Verify your share to unlock +3 questions:**")
        verification = st.text_input("Enter your code to verify:", placeholder=f"e.g. {code}", key="verify_input")
        if st.button("✅ Verify Share", use_container_width=True):
            if verification.strip().upper() == code.upper():
                if code not in st.session_state.verified_shares:
                    st.session_state.bonus_messages += 3
                    st.session_state.verified_shares.add(code)
                    st.success("🎉 Verified! You've unlocked +3 free questions.")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.warning("This code has already been used.")
            else:
                st.error("❌ Incorrect code. Make sure you copied it exactly.")

    with col_b:
        st.markdown("### 🔓 Full Lifetime Access")
        st.markdown(
            """
            **Whop Premium** — $19/month
            - ✅ Unlimited AI consultations
            - ✅ Permanent chat history
            - ✅ Real-time Portuguese law alerts
            - ✅ Priority AI responses
            - ✅ Apple Pay, Google Pay & Credit Cards
            """
        )
        st.link_button("🔓 Unlock Full Access via Whop ($19/mo)", WHOP_URL, use_container_width=True, type="primary")

    st.divider()
    st.chat_input("Upgrade to continue your consultation...", disabled=True)
    st.stop()

# ── CHAT HISTORY ──────────────────────────────────────────────────────────
for msg in current_tab["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── CHAT INPUT ────────────────────────────────────────────────────────────
cooldown = cooldown_remaining()
if cooldown > 0 and not st.session_state.is_premium:
    st.warning(f"⏳ Please wait **{cooldown} seconds** before sending your next message. (Free plan rate limit)")
    st.chat_input("Please wait for the cooldown...", disabled=True)
else:
    user_input = st.chat_input("Ask anything about Portuguese law, immigration, taxes, or compliance...")

    if user_input:
        # Append user message and record time
        current_tab["messages"].append({"role": "user", "content": user_input})
        st.session_state.last_message_time = time.time()

        with st.chat_message("user"):
            st.markdown(user_input)

        # Get AI response — only count the message if the call succeeds
        with st.chat_message("assistant"):
            with st.spinner("LawBuddy Portugal is researching Portuguese law..."):
                answer = get_ai_response(current_tab["messages"], current_tab["profile"])
            st.markdown(answer)

        current_tab["messages"].append({"role": "assistant", "content": answer})
        # Increment quota only after a successful response
        if not answer.startswith("⚠️ An error occurred"):
            st.session_state.total_messages += 1
        st.rerun()
