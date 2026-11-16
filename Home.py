import streamlit as st

st.set_page_config(
    page_title="Disease Diagnosis System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;600;800&family=Playfair+Display:wght@800&display=swap');
html, body, .stApp, p, h1, a, span, div, button { font-family: 'Garamond', 'EB Garamond', Georgia, serif; }
#MainMenu, header, footer, [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }

/* Gradient background with two blurred colour glows */
.stApp {
    background:
        radial-gradient(circle at 15% 25%, rgba(47, 111, 237, .22), transparent 40%),
        radial-gradient(circle at 85% 75%, rgba(0, 190, 180, .20), transparent 40%),
        linear-gradient(135deg, #eef3ff, #f8f5ff);
}
.block-container { max-width: 96vw; padding: 1.5vh 1.5rem 1vh !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }

/* Navigation bar */
.nav { display: flex; justify-content: space-between; align-items: center;
       padding-bottom: 1vh; border-bottom: 2px solid rgba(21, 43, 94, .12); }
.brand { font-size: min(2.4vw, 4.4vh); font-weight: 800; color: #152b5e; }
.nav a { font-size: min(1.6vw, 3vh); font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
         color: #2f6fed; text-decoration: none; transition: letter-spacing .2s; }
.nav a:hover { letter-spacing: 4px; }

/* Gradient title with an accent bar, and a big caption */
.hero { text-align: center; padding: 10vh 2vw 12vh; animation: rise 1s ease both; }
h1.title {
    font-family: 'Playfair Display', Georgia, serif !important;
    font-weight: 800; font-size: min(7vw, 14vh) !important; margin: 0 0 5vh;
    background: linear-gradient(90deg, #152b5e, #2f6fed, #152b5e);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
h1.title::after {
    content: ""; display: block; width: 140px; height: 6px; margin: 2vh auto 0;
    border-radius: 3px; background: linear-gradient(90deg, #2f6fed, #00bfb3);
}
p.desc { font-size: min(3vw, 6vh) !important; color: #152b5e !important; line-height: 1.35; margin: 0; }

/* Centred START button with a pulsing glow */
.stButton, [data-testid="stElementContainer"]:has(button) { width: 100% !important; display: flex; justify-content: center; }
.stButton button {
    background: linear-gradient(135deg, #152b5e, #2f6fed) !important; border: none !important;
    border-radius: 40px !important; width: 300px; height: 80px;
    animation: glow 2s infinite; transition: transform .2s;
}
.stButton button p { color: white !important; font-size: 2.3rem !important; font-weight: 800 !important; letter-spacing: 3px; }
.stButton button:hover { transform: scale(1.08); }

@keyframes rise { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: none; } }
@keyframes glow {
    0%, 100% { box-shadow: 0 6px 20px rgba(47, 111, 237, .35); }
    50% { box-shadow: 0 6px 40px rgba(47, 111, 237, .75); }
}
</style>

<div class="nav">
    <span class="brand">ML&amp;Med</span>
    <a href="/" target="_self">Home</a>
</div>

<div class="hero">
    <h1 class="title">Disease Diagnosis System</h1>
    <p class="desc">
        An intelligent machine learning-based symptom checker
        designed to help you explore potential health conditions.
    </p>
</div>
""", unsafe_allow_html=True)

if st.button("START"):
    st.switch_page("pages/Diagnosis.py")