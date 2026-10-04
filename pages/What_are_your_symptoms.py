import streamlit as st

st.set_page_config(page_title="tame impala", page_icon="🩺")

st.title("🩺 Describe Your Symptoms")
st.caption("Write freely — the more detail you give, the more accurate the prediction.")

user_input = st.text_area(
    "What are you experiencing?",
    placeholder="e.g. I've had a high fever for 3 days, with chills and a bad headache...",
    height=150
)

st.write("")
submit = st.button("Submit", type="primary", use_container_width=True)

if submit:
    if user_input.strip():
        st.success("Got it — here's what you entered:")
        st.subheader(user_input)
    else:
        st.warning("Please describe your symptoms before submitting.")
