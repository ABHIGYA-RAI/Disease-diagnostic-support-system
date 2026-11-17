from pathlib import Path
import streamlit as slt


slt.set_page_config(page_title = "Home",page_icon="🩺")


slt.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;600;800&family=Playfair+Display:wght@800&display=swap');
html,body, .stApp, p, h1, a, span, div, button{ font-family:
'Garamond','EB Garamond', Georgia, serif;}
[data-testid="collapsedControl"]{display: none !important;}


.stApp{
background: radial-gradient(circle at 15% 25%, rgba(47,111,237, .22), transparent 40%),
radial-gradient(circle at 85% 75%, rgba(0,190,180, .20), transparent 40%),
linear-gradient(135deg, #eef3ff, #f8f5ff) ;}


.block-container{ max-width: 96vw; padding: 1.5vh 1.5rem 1vh !important;}
[data-testid="stVerticalBlock"]{gap:0 !important;}
[data-testid="stHorizontalBlock"]{margin-top: 5vh;}


.nav{display: flex; justify-content: space-between;align-items:center;
padding-bottom: 1vh; border-bottom:2px solid rgba(21,43,94, .12);}
.brand{font-size: min(2.4vw, 4.4vh); font-weight:800; color: #152b5e;}
.nav a{font-size: min(1.6vw,3vh);font-weight:700;
letter-spacing:2px;text-transform:uppercase;color: #2f6fed; text-decoration:none;transition:letter-spacing .2s;}
.nav a: hover{letter-spacing: 4px;}
.hero {padding: 0 0 12vh 2vw; animation: rise 1s ease both;}


h1.title{ font-family : 'Playfair Display',Georgia,serif !important;
font-weight:800;font-size:min(5vw,8vh) !important; margin: 0 0 4vh; line-height: 1.15;
color: black !important}


h1.title::after{content:"";display:block;width:140px;height:6px;margin:2.5vh 0 0;
border-radius:3px;background:linear-gradient(90deg,#2f6fed,#00bfb3);}
p.desc{font-size:min(2.3vw,4.6vh) !important;color:#152b5e !important;line-height:1.4;margin:0;}
[data-testid="stImage"]{display:flex;justify-content:center;}
[data-testid="stImage"] img{border: 8px solid white;border-radius:30px;transform:rotate(3deg);
box-shadow: 0 20px 50px rgba(47,111,237,.4); animation:float 4s ease-in-out infinite;}


[data-testid="stElementContainer"]:has(button){padding left:2vw;}
.stButton button{background: linear-gradient(135deg,#152b5e,#2f6fed) !important;border:none !important;
border-radius:40px !important;width:300px;height:80px;animation:glow 2s infinite; transition: transform .2s;}
.stButton button p{color:white !important;font-size:2.3rem !important;font-weight:800 !important;letter-spacing:3px;}
.stButton button:hover{transform:scale(1.08);}
@keyframes rise{from{opacity:0;transform:translateY(30px);} to{opacity:1;transform:none;}}
@keyframes float{0%,100% {transform:rotate(3deg) translateY(0);}
50% {transform:rotate(3deg) translateY(-18px);}}
@keyframes glow{0%,100% {box-shadow:0 6px 20px rgba(47,111,237,.35);}
50% {box-shadow:0 6px 40px rgba(47,111,237,.75);}}
</style>
<div class="nav">
<span class="brand">ML&amp;Med</span>
<a href="/"target="_self">Home</a>
</div>
""",unsafe_allow_html=True)


text_side,image_side = slt.columns([3,2],vertical_alignment="center")
with text_side:
   slt.markdown("""
   <div class="hero">
   <h1 class = "title"> Disease Diagnosis System </h1>
   <p class = "desc"> A machine-learning based symptom checker designed to help you explore potential health conditions.</p>
    </div>
   """,unsafe_allow_html=True)
   if slt.button("START"):
       slt.switch_page("/pages/What_symptoms_should_be.py")
with image_side:
   slt.image(next(Path(__file__).parent.glob("doraemon*.jpg")),width=300)



