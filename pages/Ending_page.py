import streamlit as slt
slt.set_page_config(page_icon="😊",page_title="That's it!")
slt.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@500;800&display=swap');
.stApp { background: linear-gradient(135deg,#cfdcfb,#f5f5ff 55%,#d3eef5); }
.end { text-align:center; padding-top:70px;
       font-family:'EB Garamond', Garamond, serif; }
.emoji { font-size:12rem; line-height:1; }
.thanks { color:#1e3a8a; font-size:5rem; font-weight:800; margin-top:10px; }
.bar { width:110px; height:6px; border-radius:6px; margin:14px auto 20px;
       background:linear-gradient(90deg,#2563eb,#14b8a6); }
.cap { color:#1e3a8a; font-size:1.6rem; }
.stButton { margin-top:30px; text-align:center; }
.stButton button { background:linear-gradient(90deg,#1e3a8a,#2f66e0);
        border:none; border-radius:50px; padding:.7rem 3rem;
        box-shadow:0 8px 20px rgba(37,99,235,.35); }
.stButton button p { color:white; font-size:1.5rem; font-weight:600;
        letter-spacing:2px; font-family:'EB Garamond', Garamond, serif; }
</style>
<div class="end">
<div class="emoji">🤗</div>
<div class="thanks">Thank you!</div>
<div class="bar"></div>
<div class="cap">Hopefully, this system has offered you some helpful insights into your symptoms.</div>
<div class="cap">Take care!🌸🦋🧸 </div>
</div>
""",unsafe_allow_html=True)
_,mid,_ = slt.columns([1,2,1])
if mid.button("BACK TO HOME",use_container_width=True):
    slt.switch_page("Home.py")