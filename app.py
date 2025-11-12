import streamlit as st
import pandas as pd
import gdown
import joblib

url = "https://drive.google.com/uc?id=1atuUQWrpQ3Arh_TWZNk-q_0KS-kI2Xtu"

gdown.download(url, "bank_account_model.pkl", quiet=False)
model = joblib.load("bank_account_model.pkl")

st.title("💰 Financial Inclusion Predictor")

st.write("Predict if an individual is likely to have a bank account based on their demographics.")

# Input fields
country = st.selectbox("Country", ["Kenya", "Rwanda", "Tanzania", "Uganda"])
year = st.selectbox("Year", [2016, 2017, 2018])
location_type = st.selectbox("Location Type", ["Urban", "Rural"])
cellphone_access = st.selectbox("Cellphone Access", ["Yes", "No"])
household_size = st.number_input("Household Size", min_value=1, max_value=20, value=3)
age = st.number_input("Age of Respondent", min_value=15, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female"])
relationship = st.selectbox("Relationship with Head", ["Head of Household", "Spouse", "Child", "Other relative"])
marital_status = st.selectbox("Marital Status", ["Married/Living together", "Single/Never Married", "Divorced/Separated", "Widowed"])
education = st.selectbox("Education Level", ["No formal education", "Primary education", "Secondary education", "Vocational/Specialised training", "Tertiary education"])
job_type = st.selectbox("Job Type", ["Self employed", "Formally employed Government", "Formally employed Private", "Informally employed", "Farming and Fishing", "Remittance Dependent", "Other Income", "Government Dependent"])

if st.button("Predict"):
    input_df = pd.DataFrame({
        'country': [country],
        'year': [year],
        'location_type': [location_type],
        'cellphone_access': [cellphone_access],
        'household_size': [household_size],
        'age_of_respondent': [age],
        'gender_of_respondent': [gender],
        'relationship_with_head': [relationship],
        'marital_status': [marital_status],
        'education_level': [education],
        'job_type': [job_type]
    })

    # Apply simple encoding for object dtype columns
    for col in input_df.select_dtypes(include='object').columns:
        input_df[col] = input_df[col].astype('category').cat.codes

    prediction = model.predict(input_df)[0]
    result = "✅ Likely to have a bank account" if prediction == 1 else "❌ Not likely to have a bank account"
    st.success(result)
