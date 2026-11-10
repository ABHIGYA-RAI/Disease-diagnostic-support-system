import streamlit as st

st.set_page_config(page_title="Results", page_icon="🩺")
st.title("Your results")

if "top3" not in st.session_state:
    st.warning("No results yet. Please describe your symptoms first.")
    st.stop()

top3 = st.session_state["top3"]

if top3[0][1] < 0.40:
    st.info("Result inconclusive. Try adding more symptoms.")
else:
    for disease, prob in top3:
        st.write(f"**{disease}**: {prob * 100:.0f}%")

if st.button("Try again"):
    st.switch_page("pages/Diagnosis.py")