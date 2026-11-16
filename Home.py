
"""Machine Learning-Powered Disease Diagnosis - Home Page."""

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Disease Diagnosis System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

NAVY = "#152b5e"
GARAMOND = "'Garamond', 'EB Garamond', 'Cormorant Garamond', Georgia, serif"

# Doraemon image location
DORAEMON_IMAGE = Path(__file__).parent / "doraemon_doctor.jpg"


# ---------- CSS ----------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap');

    /* ORIGINAL FONT STYLING - PRESERVED */
    html, body, [class*="css"], .stApp, .stMarkdown,
    button, p, h1, h2, h3, a, span, div {{
        font-family: {GARAMOND};
    }}

    #MainMenu, header, footer, [data-testid="stToolbar"],
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {{
        display: none !important;
    }}

    .stApp {{
        background: #f4f7fc;
    }}

    .block-container {{
        max-width: 96vw;
        margin: 0 auto;
        padding: 1.5vh 1.5rem 1vh 1.5rem !important;
    }}

    [data-testid="stVerticalBlock"] {{
        gap: 0 !important;
    }}

    /* Navigation */
    .nav {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 1vh;
        border-bottom: 1px solid #d9e2f1;
    }}

    .nav .brand {{
        font-size: min(2.2vw, 4.2vh);
        font-weight: 800;
        color: {NAVY};
        letter-spacing: .5px;
    }}

    .nav a {{
        font-size: min(1.6vw, 3vh);
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #4b5b78;
        text-decoration: none;
    }}

    .nav a:hover {{
        color: {NAVY};
    }}

    /* Main section */
    .hero {{
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding-top: 1vh;
        gap: 1.5vh;
    }}

    /* Original font style preserved */
    .hero .title {{
        font-family: 'Playfair Display', Georgia, serif !important;
        font-weight: 800;
        color: {NAVY};
        font-size: min(3.5vw, 7.2vh);
        line-height: 1.15;
        margin: 1vh 0;
    }}

    .hero .desc {{
        font-family: 'Times New Roman', Times, 'Liberation Serif', serif !important;
        font-size: min(2.2vw, 4vh);
        color: #5d6b82;
        margin: 0;
        line-height: 1.5;
    }}

    /* Feature captions - no white boxes */
    .features {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 5vw;
        margin: 5vh 2vw 5vh;
        text-align: left;
    }}

    .feature h3 {{
        color: {NAVY};
        font-weight: 700;
        font-size: min(2.5vw, 4.8vh);
        margin: 0 0 2vh 0;
    }}

    .feature p {{
        color: #5d6b82;
        font-size: min(2vw, 3.8vh);
        line-height: 1.6;
        margin: 0;
    }}

    /* START button - original design preserved */
    div.stButton, [data-testid="stButton"],
    [data-testid="stElementContainer"]:has(button) {{
        width: 100% !important;
        display: flex;
        justify-content: center;
    }}

    div.stButton > button, [data-testid^="stBaseButton"] {{
        background: {NAVY} !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 18px !important;
        width: 250px !important;
        height: 70px;
        min-height: 0;
        box-shadow: 0 6px 16px rgba(21,43,94,.30);
        transition: transform .12s ease, background .12s ease;
    }}

    div.stButton > button p, [data-testid^="stBaseButton"] p {{
        color: #ffffff !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        letter-spacing: .5px;
    }}

    div.stButton > button:hover {{
        background: #1f3d82 !important;
        transform: translateY(-2px);
    }}

    /* Responsive layout */
    @media (max-width: 768px) {{
        .features {{
            grid-template-columns: 1fr;
            gap: 3vh;
            margin: 4vh 1vw;
        }}

        .hero .title {{
            font-size: 2.5rem;
        }}

        .hero .desc {{
            font-size: 1.4rem;
        }}

        .feature h3 {{
            font-size: 1.8rem;
        }}

        .feature p {{
            font-size: 1.3rem;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Navigation ----------
st.markdown(
    """
    <div class="nav">
        <span class="brand">ML&amp;Med</span>
        <a href="/" target="_self">Home</a>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------- Doraemon Logo ----------
left, center, right = st.columns([1, 1, 1])

with center:
    st.image(DORAEMON_IMAGE, width=240)


# ---------- Main Heading ----------
st.markdown(
    """
    <div class="hero">
        <h1 class="title">Disease Diagnosis System</h1>

        <p class="desc">
            An intelligent machine learning-based symptom checker
            designed to help you explore potential health conditions.
        </p>
    </div>

    <div class="features">

        <div class="feature">
            <h3>🧠 Intelligent predictions</h3>
            <p>
                Machine learning-powered disease prediction
                based on reported symptoms.
            </p>
        </div>

        <div class="feature">
            <h3>📋 Symptom-based analysis</h3>
            <p>
                Explore possible conditions based on your
                selected symptoms.
            </p>
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ---------- START Button ----------
if st.button("START", key="start_btn"):
    st.switch_page("pages/Diagnosis.py")
