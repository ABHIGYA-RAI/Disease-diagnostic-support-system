"""Machine Learning-Powered Disease Diagnosis - front / home page (Streamlit)."""
import streamlit as st

st.set_page_config(
    page_title="Machine Learning-Powered Disease Diagnosis",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "page" not in st.session_state:
    st.session_state.page = "home"


def go_next():
    st.session_state.page = "diagnosis"


def go_home():
    st.session_state.page = "home"


GARAMOND = "'Garamond', 'EB Garamond', 'Cormorant Garamond', Georgia, serif"
NAVY = "#152b5e"

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap');

/* every text is Garamond, except where overridden below */
html, body, [class*="css"], .stApp, .stMarkdown, button, p, h1, h2, h3, a, span, div {{
    font-family: {GARAMOND};
}}
#MainMenu, header, footer, [data-testid="stToolbar"],
[data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display: none !important; }}

.stApp {{ background: #f4f7fc; }}
.block-container {{
    max-width: 96vw;
    margin: 0 auto;
    padding: 1.5vh 1.5rem 1vh 1.5rem !important;
}}
[data-testid="stVerticalBlock"] {{ gap: 0 !important; }}

/* ---------- top bar: only "Home" at the upper right ---------- */
.nav {{
    display: flex; justify-content: space-between; align-items: center;
    padding-bottom: 1vh; border-bottom: 1px solid #d9e2f1;
}}
.nav .brand {{
    font-size: min(2.2vw, 4.2vh); font-weight: 800; color: {NAVY}; letter-spacing: .5px;
}}
.nav a {{
    font-size: min(1.6vw, 3vh); font-weight: 600; letter-spacing: 1.5px;
    text-transform: uppercase; color: #4b5b78; text-decoration: none;
}}
.nav a:hover {{ color: {NAVY}; }}

/* ---------- hero ---------- */
.hero {{
    display: flex; flex-direction: column; align-items: center;
    text-align: center; padding-top: 2vh; gap: 2vh;
}}
.hero .logo {{
    width: min(6vw, 10vh); height: min(6vw, 10vh);
    background: #e1ebfa; border-radius: 24px;
    display: flex; align-items: center; justify-content: center;
    font-size: min(3.3vw, 5.5vh);
}}
.hero .title {{
    font-family: 'Playfair Display', Georgia, serif !important;
    font-weight: 800; color: {NAVY};
    font-size: min(3.5vw, 7.2vh);          /* biggest text on the page */
    line-height: 1.15; margin: 0; white-space: nowrap;
}}
.hero .desc {{
    font-family: 'Times New Roman', Times, 'Liberation Serif', serif !important;
    font-size: min(1.9vw, 3.6vh); color: #5d6b82; margin: 0;
}}

/* ---------- two white boxes side by side ---------- */
.cards {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 1.6vw;
    margin: 3vh 0 8vh 0;
}}
.card {{
    background: #ffffff; border-radius: 18px;
    padding: 2.6vh 2vw; box-shadow: 0 4px 18px rgba(21,43,94,.08);
}}
.card h3 {{
    margin: 0 0 1vh 0; color: {NAVY}; font-weight: 700;
    font-size: min(2.2vw, 4.2vh);
}}
.card p {{ margin: 0; color: #5d6b82; font-size: min(1.6vw, 3.1vh); }}

/* ---------- Get Started button ---------- */
div.stButton, [data-testid="stButton"],
[data-testid="stElementContainer"]:has(button) {{
    width: 100% !important; display: flex; justify-content: center;
}}
div.stButton > button, [data-testid^="stBaseButton"] {{
    background: {NAVY} !important; color: #ffffff !important;
    border: none !important; border-radius: 18px !important;
    width: 250px !important; height: 150px; min-height: 0;
    box-shadow: 0 6px 16px rgba(21,43,94,.30);
    transition: transform .12s ease, background .12s ease;
}}
div.stButton > button p, [data-testid^="stBaseButton"] p {{
    color: #ffffff !important; font-size: 2.00rem !important;
    font-weight: 700 !important; letter-spacing: .5px;
}}
div.stButton > button:hover {{ background: #1f3d82 !important; transform: translateY(-2px); }}

/* ---------- notice (no box) ---------- */
.warning {{
    display: flex; align-items: center; justify-content: center; gap: .6vw;
    position: fixed; left: 0; right: 0; bottom: 1.2vh; padding: 0;
}}
.warning .sign {{ font-size: min(1.6vw, 3.1vh); line-height: 1; }}
.warning .msg {{
    color: #8a5a14; font-weight: 400; margin: 0;
    font-size: min(1.6vw, 3.1vh); white-space: nowrap;
}}
</style>
""",
    unsafe_allow_html=True,
)


def home_page():
    st.markdown(
        """
<div class="nav"><span class="brand">ML&amp;Med</span><a href="/" target="_self">Home</a></div>
<div class="hero">
<div class="logo">🩺</div>
<h1 class="title">Machine Learning-Powered Disease Diagnosis</h1>
<p class="desc">An intelligent machine learning-based symptom checker designed to help you explore potential health conditions.</p>
</div>
<div class="cards">
<div class="card"><h3>🧠 Intelligent predictions</h3><p>Machine learning-powered disease prediction based on reported symptoms.</p></div>
<div class="card"><h3>📋 Symptom-based analysis</h3><p>Explore possible conditions based on your selected symptoms.</p></div>
</div>
""",
        unsafe_allow_html=True,
    )
    st.button("START", on_click=go_next, key="start_btn")
    st.markdown(
        """
<div class="warning"><span class="sign">⚠️</span><p class="msg">For informational purposes only. Not a substitute for professional medical advice.</p></div>
""",
        unsafe_allow_html=True,
    )


def diagnosis_page():
    """Placeholder for the next page - replace with your symptom-input page."""
    st.title("Symptom Checker")
    st.write("This is where the next page of your app goes.")
    st.button("BACK", on_click=go_home)


if st.session_state.page == "home":
    home_page()
else:
    diagnosis_page()