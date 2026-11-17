import streamlit as slt
slt.set_page_config(page_icon="🤗",page_title="What to do now?")
slt.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@500;600;800&display=swap');
.stApp { background: linear-gradient(135deg,#cfdcfb,#f5f5ff 55%,#d3eef5); }
h1, h2, .box { font-family:'EB Garamond', Garamond, serif !important; }
h2 { color:#1e3a8a !important; font-size:3.4rem; font-weight:800;
     margin:36px 0 6px; padding:0; }
.bar { width:110px; height:6px; border-radius:6px; margin:0 0 22px;
       background:linear-gradient(90deg,#2563eb,#14b8a6); }
.box { background:rgba(255,255,255,.85); border-left:6px solid #2563eb;
       border-radius:18px; padding:20px 26px; margin-bottom:16px;
       color:#1e3a8a; font-size:1.3rem; line-height:1.6;
       box-shadow:0 8px 24px rgba(37,99,235,.15); }
.box b { color:#0b0f19; }
.box h3 { font-family:'EB Garamond', Garamond, serif !important;
          color:#0b0f19 !important; font-size:1.8rem; margin:0 0 6px;
          padding:0; }
.stButton { margin-top:30px; }
.stButton button { background:linear-gradient(90deg,#1e3a8a,#2f66e0);
        border:none; border-radius:50px; padding:.7rem 3rem;
        box-shadow:0 8px 20px rgba(37,99,235,.35); }
.stButton button p { color:white; font-size:1.5rem; font-weight:600;
        letter-spacing:2px; font-family:'EB Garamond', Garamond, serif; }
</style>
<div class="box" style="margin-top:20px">
<h3>A note about your results</h3>
These results are just predictions and should not be considered as a final evaluation. For more accurate and safe diagnosis, please consult a licensed medical professional as soon as possible.</div>
<h2>What can you do now?</h2>
<div class="bar"></div>
<div class="box"><b>Rest and sleep🥱🛌:</b> The body recovers faster when it is rested enough.</div>
<div class="box"><b>Eat nutritious meals🥟🥗:</b> Eat fruits, vegetables, fish and easily digestible food like porridge.😋🤤🤤</div>
<div class="box"><b>Avoid self-treatment💀:</b> Without getting a prescription from a doctor, do not try to engage in self-medication and try to perform treatment on your own.</div>
""",unsafe_allow_html=True)

if slt.button("NEXT"):
    slt.switch_page("pages/Ending_page.py")
