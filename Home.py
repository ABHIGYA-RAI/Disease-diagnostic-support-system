import streamlit as st

st.set_page_config(
    page_title="MediSense",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------- Minimal, theme-safe styling ----------
# Uses Streamlit's own CSS variables (--text-color, --background-color, etc.)
# instead of hardcoded colors, so it looks correct in both light and dark mode.
st.markdown("""
    <style>
    .hero-title {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 3.2rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        color: var(--text-color);
        margin-bottom: 0.2rem;
    }
    .hero-accent {
        width: 60px;
        height: 4px;
        background-color: #0f766e;
        border-radius: 2px;
        margin: 0.6rem 0 1.2rem 0;
    }
    .hero-subtitle {
        font-size: 1.15rem;
        color: var(--text-color);
        opacity: 0.75;
        max-width: 34rem;
        line-height: 1.5;
    }
    .section-label {
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #0f766e;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown('<div class="hero-title">MediSense</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-accent"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">A decision-support tool that estimates likely conditions '
    'from the symptoms you describe — built to inform, not replace, medical judgment.</div>',
    unsafe_allow_html=True
)

st.write("")

# ---------- Disclaimer (native component, theme-adaptive) ----------
st.error(
    "**This is not a medical professional.** MediSense does not diagnose disease. "
    "It is a decision-support framework that suggests a likely condition based on "
    "patterns in symptom data. Always consult a qualified healthcare provider before "
    "making medical decisions.",
    icon="⚠️"
)

# ---------- How it works ----------
st.markdown('<div class="section-label">How it works</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    with st.container(border=True):
        st.markdown("**1. Describe**")
        st.caption("Enter the symptoms you're experiencing on the next page.")
with c2:
    with st.container(border=True):
        st.markdown("**2. Analyze**")
        st.caption("The model compares your input against learned symptom patterns.")
with c3:
    with st.container(border=True):
        st.markdown("**3. Review**")
        st.caption("See the most likely condition, along with a confidence level.")

# ---------- Why it's useful ----------
st.markdown('<div class="section-label">Good to know</div>', unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("🔬 &nbsp; **Evidence-based** — trained on real symptom-disease datasets, not guesswork.")
with st.container(border=True):
    st.markdown("🔒 &nbsp; **Private by default** — your inputs stay within this session; nothing is stored.")
with st.container(border=True):
    st.markdown("⚡ &nbsp; **Instant** — a preliminary read in seconds, before you decide on next steps.")

st.divider()
st.sidebar.success("👈 Select a page above to get started.")
st.caption("MediSense is an educational decision-support tool, not a substitute for professional medical advice.")