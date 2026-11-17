import streamlit as slt
slt.set_page_config(page_icon="📝",page_title="Rules for writing symptoms")


slt.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@500;600&display=swap');
.stApp { background: linear-gradient(135deg,#cfdcfb,#f5f5ff 55%,#d3eef5); }
h1, .cap, .rule { font-family:'EB Garamond',Garamond !important;}
h1 { color:#1e3a8a !important; font-size:2.8rem; margin:0; }
.bar { width:110px; height:6px; border-radius:6px; margin:12px 0 18px;
       background:linear-gradient(90deg,#2563eb,#14b8a6); }
.cap { color:#1e3a8a; font-size:1.2rem; margin-bottom:28px; }
.rule { background:rgba(255,255,255,.8); border-left:6px solid #2563eb;
        border-radius:18px; padding:18px 24px; margin-bottom:16px;
        color:#1e3a8a; font-size:1.1rem;
        box-shadow:0 8px 24px rgba(37,99,235,.15); }
.rule b { color:#0b0f19; }
.stButton { margin-top:45px; }
.stButton button { background:linear-gradient(90deg,#1e3a8a,#2f66e0);
        border:none; border-radius:50px; padding:.7rem 3rem;
        box-shadow:0 8px 20px rgba(37,99,235,.35); }
.stButton button p { color:white; font-size:1.5rem; font-weight:600;
        letter-spacing:2px; font-family:'EB Garamond', Garamond, serif; }
</style>

<h1> How should you write your symptoms?</h1>
<div class="bar"></div>
<div class="cap">Before you write down your symptoms, you will have to follow few rules that will act as guidance.</div>
<div class="rule"><b>1.</b> List all the symptoms you <b>DO</b> have as this increases the chances of the model catching the most likely disease.</div>
<div class="rule"><b>2.</b> Write in full English sentences using correct grammar and spelling.</div>
<div class="rule"><b>3.</b> Be hyper-specific about your symptoms.<br>
 <i>Don't just say:</i> "I have a headache."<br>
<i>Write something like:</i> "My head has been hurting a lot and I feel like I'm about to have a fever soon."</div>
""", unsafe_allow_html=True)
if slt.button("CONTINUE"):
    slt.switch_page("pages/Diagnosis.py")
