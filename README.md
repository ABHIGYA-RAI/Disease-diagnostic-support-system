# Disease diagnostic support system
This machine learning–based system diagnoses diseases from patient-reported symptoms, operating on a straightforward diagnostic paradigm: the patient provides a set of observed symptoms, and the system infers the most probable disease based on this input.

## Overview

This project takes a list of symptoms as input and predicts the most likely disease(s) using classical machine learning models. It was developed as an end-to-end pipeline — from raw symptom data to a deployed, interactive website application.

## Dataset

- **Kaggle Disease-Symptom Dataset** (`DiseaseAndSymptoms.csv`) — 41 diseases, 131 symptoms

## Pipeline

1. **Data Preprocessing** — Multi one-hot encoding of symptoms into a binary feature matrix (implemented from scratch using pandas rather than sklearn encoders)
2. **Data Splitting** — Train/test split of the encoded dataset
3. **Model Training** — Multiple classifiers trained and compared:
   - Random Forest
   - Logistic Regression
   - K-Nearest Neighbors (KNN)
   - Support Vector Machine (SVM)
   - XGBoost
   - CatBoost
   - LightGBM
   - Multinomial Naive Bayes
   - Gaussian Naive Bayes
   - AdaBoost
4. **Evaluation** — Models compared using accuracy, precision, recall and F1 score.
5. **Deployment** — Best-performing classifier deployed via a Streamlit web application for interactive symptom-based diagnosis

## Tech Stack

- **Model Training:** Google Colab, pandas, scikit-learn, XGBoost, CatBoost, LightGBM
- **Deployment:** PyCharm, Streamlit


The pipeline of this system is highlighted as:

Data Collection → Data Preprocessing → Feature Engineering → 
Model Training -> Model evaluation → Model Deployment → Monitoring


The integration of Large Language Model for matching the symptoms is given as : 

<img width="2720" height="800" alt="prompt_to_symptom_flow" src="https://github.com/user-attachments/assets/b686cf4d-da72-4267-b680-16c378b95f38" />


