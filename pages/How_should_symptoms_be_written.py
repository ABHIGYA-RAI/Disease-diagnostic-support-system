import streamlit as slt
slt.set_page_config(page_title="How should symptoms be written?",page_icon="📝")
slt.title("⚠️Be cautious while reporting your symptoms⚠️")
slt.subheader("You get what you give")
slt.warning("The input symptoms that you give directly effects the diagnosis made by the machine learning algorithm. To prevent false predictions and misinformation as much as possible, follow the instructions listed below.")

with slt.container(border=True):
    slt.markdown("### 1️⃣ Report everything")
    slt.write("Write down each and every symptoms that you have but make sure you actually have them.")

with slt.container(border=True):
    slt.markdown("### 2️⃣ Write in proper sentences")
    slt.write("For example : ")
    slt.write("*My knees hurt a lot. I can't run and workout properly because of the pain. It hurts even more during winter.*")

with slt.container(border=True):
    slt.markdown("### 3️⃣ Be specific about your symptoms")
    slt.write("For example: ")
    slt.write("*My body temperature is 102 degree celsius and I have had high fever since the last three days. I feel dizzy when I stand up and have lost my appetite.*")

