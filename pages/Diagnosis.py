import os, json
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from google import genai

st.set_page_config(page_title="Diagnosis", page_icon="🩺")

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


st.title("Describe your symptoms")
text = st.text_area("Tell us how you feel, in your own words", height=150)

if st.button("Continue"):
    if not text.strip():
        st.warning("Please describe your symptoms.")
    else:
        try:
            with st.spinner("Reading your symptoms..."):# noqa
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
                st.switch_page("pages/Results.py")
        except Exception as e:
            st.error(f"Something went wrong: {e}")