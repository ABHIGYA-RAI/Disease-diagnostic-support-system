import os, json
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from google import genai

st.set_page_config(page_title="😷Submit your symptoms", page_icon="🩺")

st.markdown("""
<style>
.stApp { background-color: #eaf3fc; }
h1, p, label, span, div { color: black; }
textarea { background-color: white !important; color: black !important; }

/* Blue button with white text */
.stButton button { background-color: #1e73e8 !important; border: none; }
.stButton button p { color: white !important; }

/* Black loading icon */
[data-testid="stSpinnerIcon"],
[data-testid="stSpinner"] i {
    border-color: black !important;
    border-top-color: transparent !important;
}
[data-testid="stSpinner"] svg { stroke: black !important; }
</style>
""", unsafe_allow_html=True)

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
symptoms = joblib.load(os.path.join(folder, "Symptoms.pkl"))
model = joblib.load(os.path.join(folder, "Final Model.pkl"))
disease_encoder = joblib.load(os.path.join(folder, "Disease Encoder.pkl"))

load_dotenv(os.path.join(folder, "API Key.env"))
client = genai.Client(api_key=os.environ["API_saacho"])


def map_symptoms(user_text, symptom_list):
    prompt = f"""From the patient's text, pick every matching symptom from the LIST.
    Use only names exactly as written in the LIST. If none match, return [].
    Return only a JSON list.

    TEXT: {user_text}
    LIST: {symptom_list}"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config={"response_mime_type": "application/json"}
    )

    matched = json.loads(response.text)
    return [s for s in matched if s in symptom_list]


st.markdown(
    "<h1 style='text-align: center; font-weight: bold;'>✍️Describe your symptoms</h1>",
    unsafe_allow_html=True
)

text = st.text_area(
    "What are you suffering from?",
    placeholder="My head has been hurting a lot since this morning.",
    height=150
)

# The button lives inside this slot so we can remove it after a click
button_slot = st.empty()

if button_slot.button("Report symptoms"):
    if not text.strip():
        st.warning("Please describe your symptoms.")
    else:
        button_slot.empty()  # hide the button
        try:
            with st.spinner("Analysing your symptoms"):
                chosen = map_symptoms(text, symptoms)

                if not chosen:
                    st.warning("We couldn't recognize any symptoms. Please try rephrasing.")
                else:
                    row = pd.DataFrame(0, index=[0], columns=symptoms)
                    row.loc[0, chosen] = 1

                    probs = model.predict_proba(row)[0]
                    top = np.argsort(probs)[::-1][:3]
                    names = disease_encoder.inverse_transform(model.classes_[top])

                    st.session_state["top3"] = list(zip(names, probs[top]))
                    st.switch_page("pages/Possible_diseases.py")

        except Exception as e:
            st.error(f"Something went wrong: {e}")