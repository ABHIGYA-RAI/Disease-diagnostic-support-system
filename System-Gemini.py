Large language model integration


#Integrating Gemini-3.5-Flash into Python Script
from google import genai
from google.colab import userdata
api = userdata.get('GEMINI_API_KEY')
client = genai.Client(api_key=api)
print("Congratualtions!!! 🥳🥳🥳\n You're now connected to Gemini-3.5-Flash.\n You can enter your prompt.\n If you want to exit, write 'exit'")



user_report = str(input("Report your symptoms:"))


reference_list = [ ]
indra_columns = indra_chowk.columns
for symptoms in indra_columns:
  reference_list.append(symptoms)
print(reference_list)

prompt = (
    f"This is a list of symptoms : {reference_list}"
    f"This is the patient's report : {user_report}"
    "Gemini, you will have to match the symptoms reported by the patient with only the symptoms inside of the list I gave you." 
    "Then, send me a comma seperated list of matching symptoms which should only be the ones from the list and nowhere else."
    "If none of the symptoms matched, just send me an empty list and also comment,'Sorry, your symptoms are out of the scope.😢' "

)
