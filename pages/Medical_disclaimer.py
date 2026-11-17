import streamlit as slt
slt.set_page_config(page_icon="⚠️",page_title="Medical Disclaimer")
slt.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@500;600&display=swap');
.stApp { background: linear-gradient(135deg,#cfdcfb,#f5f5ff 55%,#d3eef5); }
h1, .cap, .box, [data-testid="stCheckbox"] p
   { font-family:'EB Garamond', Garamond, serif !important; }
h1 { color:#1e3a8a !important; font-size:3.2rem; margin:0; }
.bar { width:110px; height:6px; border-radius:6px; margin:12px 0 18px;
      background:linear-gradient(90deg,#2563eb,#14b8a6); }
.cap { color:#1e3a8a; font-size:1.4rem; margin-bottom:28px; }
.box { background:rgba(255,255,255,.85); border-left:6px solid #2563eb;
      border-radius:18px; padding:20px 26px; margin-bottom:16px;
      color:#1e3a8a; font-size:1.3rem; line-height:1.6;
      box-shadow:0 8px 24px rgba(37,99,235,.15); }
.box b { color:#0b0f19; }
[data-testid="stCheckbox"] p { color:#1e3a8a; font-size:1.3rem;margin:0;}
[data-testid="stCheckbox"] label {align-items:center;}
[data-testid="stCheckbox"] label > *:not(input):not(:has(p)),
[data-baseweb="checkbox"] > *:not(input):not(:has(p))
{background:white !important; border:2px solid #2563eb !important;}
[data-testid="stCheckbox"] label:has(input:checked) > *:not(input):not(:has(p))
{background:#2563eb !important;}


.stButton { margin-top:30px;}
.stButton button { background:linear-gradient(90deg,#1e3a8a,#2f66e0);
       border:none; border-radius:50px; padding:.7rem 3rem;
       box-shadow:0 8px 20px rgba(37,99,235,.35); }
.stButton button:disabled { opacity:.4; }
.stButton button p { color:white; font-size:1.5rem; font-weight:600;
       letter-spacing:2px; font-family:'EB Garamond', Garamond, serif; }
</style>

<h1> User discretion advised </h1>
<div class="bar"></div>
<div class="cap">Please read this before you continue.</div>
<div class="box"><b>Not a medical diagnosis:</b> The system is a machine-learning model that matches your described symptoms to patterns in data. Its results are possibilities, not conclusions.</div>
<div class="box"><b>Not a substitute for a professional:</b> Consult a licensed doctor for any health concerns as this tool will not be making the final evaluations.</div>
<div class="box"><b>In an emergency, don't use this tool:</b> If you have severe symptoms such as difficulty in breathing,heavy bleeding and fever that lasted more than a week, contact local emergency services or go to the nearest hospital immediately.</div>
""",unsafe_allow_html=True)

agree = slt.checkbox("I understand the risks involved and choose to proceed.")
if slt.button("CONTINUE",disabled=not agree):
    slt.switch_page("pages/How_should_symptoms_be_written.py")
