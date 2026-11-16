import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from google import genai
import joblib
import streamlit as slt
import json

slt.set_page_config(page_icon="😷",page_title = "Symptoms reporting")
slt.markdown(""" 
<style>
.stApp{ background-color : #eaf3fc;}
h1,p,label,span,div{color : black;}
textarea{background-color: white !important; color: black !important; }

.stButton button {background-color: #1e73e8 !important; border: none;}
.stButton button p{color: white !important;}

[data-testid="stSpinnerIcon"],
[data-testid="stSpinner"] i {
border-color : black !important;
border-top-color: transparent !important;
}
[data-testid="stSpinner"] svg {stroke : black !important;}
</style>
""",unsafe_allow_html=True)

folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
symptoms = joblib.load(os.path.join(folder,"Symptoms.pkl"))
model = joblib.load(os.path.join(folder,"Final Model.pkl"))
disease_encoder = joblib.load(os.path.join(folder,"Disease Encoder.pkl"))


load_dotenv(os.path.join(folder,"API Key.env"))
client = genai.Client(api_key = os.environ["API_saacho"])


def map_symptoms(user_symptoms,symptom_list):
    prompt = f""" From the user's input text, pick every matching symptom
    from the LIST. Use only names exactly as written in the LIST. 
    If nothing matched even a little, just return [ ], but don't try to forcefully match.
    Return only a JSON list.
    
    TEXT : {user_symptoms}
    LIST : {symptom_list} """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config={"response_mime_type": "application/json"}
    )

    matched = json.loads(response.text)
    gemini_replied = [ ]
    for s in matched:
        if s in symptom_list:
            gemini_replied.append(s)
    return gemini_replied


slt.markdown(
    "<h1 style='text-align: center; font-weight: bold;'>✍️Describe your symptoms</h1>",
    unsafe_allow_html=True)

textarea = slt.text_area("What are you suffering from?",
                         placeholder = "Example : My head has been hurting a lot since this morning.", height = 150)
button_slot = slt.empty()
if button_slot.button("Report symptoms"):
    if not textarea.strip():
        slt.warning("Please describe your symptoms first.")
    else:
        button_slot.empty()
        try:
            with slt.spinner("Analysing your symptoms"):
                chosen = map_symptoms(textarea,symptoms)
                if not chosen:
                    slt.warning("Your symptoms couldn't be recognized. Please try rephrasing it.")
                else:
                    single_row = pd.DataFrame(0,index=[0],columns=symptoms)
                    single_row.loc[0,chosen] = 1
                    probability = model.predict_proba(single_row)[0]
                    top = np.argsort(probability)[::-1][:3]
                    decoded_diseases = disease_encoder.inverse_transform(model.classes_[top])
                    slt.session_state["top3"] = list(zip(decoded_diseases,probability[top]))

                    slt.switch_page("pages/Possible_diseases.py")
        except Exception as e:
            slt.error(f"An error occured 😬😬: {e}")









