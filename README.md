
# 💰 Financial Inclusion Predictor

This project is a **Streamlit web application** that predicts the likelihood of an individual having a bank account based on demographic features. The app uses a trained **Random Forest classifier** on the [Financial Inclusion in Africa dataset](https://i.imgur.com/UNUZ4zR.jpg).

The purpose of this project is to promote **financial inclusion insights** and demonstrate a full **data science workflow**, from data exploration to machine learning deployment.

---

## **Features**

* Predicts if an individual has a bank account.
* Interactive input fields for demographic features:

  * Country, year, location type, cellphone access, household size, age, gender, relationship with head, marital status, education level, job type.
* Real-time predictions in the browser.
* Fully deployable on **Streamlit Cloud**.

---

## **Dataset**

* Source: [Zindi – Financial Inclusion in Africa](https://i.imgur.com/UNUZ4zR.jpg)
* Contains **33,600 individuals** across East Africa.
* Features include:

  * `country`, `year`, `uniqueid`, `bank_account`, `location_type`, `cellphone_access`, `household_size`, `age_of_respondent`, `gender_of_respondent`, `relationship_with_head`, `marital_status`, `education_level`, `job_type`.

---

## **Installation**

1. Clone this repository:

```bash
git clone https://github.com/yourusername/financial_inclusion_predictor.git
cd financial_inclusion_predictor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app locally:

```bash
streamlit run app.py
```

---

## **Usage**

1. Open the app in your browser (automatically opened when running Streamlit).
2. Fill in the demographic information for an individual.
3. Click the **Predict** button to see if the individual is likely to have a bank account.

---

## **Deployment**

* The app can be deployed on **Streamlit Cloud**.
* Ensure the trained model (`bank_account_model.pkl`) is accessible:

  * Either include it in the repo (if small enough)
  * Or download dynamically from a shared link (Google Drive, Hugging Face, S3, etc.)

---

## **Dependencies**

* pandas
* numpy
* scikit-learn
* streamlit
* ydata-profiling
* matplotlib
* seaborn
* joblib
* gdown (if loading model from Google Drive)

---

## **Project Structure**

```
financial_inclusion_predictor/
│
├─ app.py                  # Main Streamlit app
├─ bank_account_model.pkl   # Trained Random Forest model
├─ requirements.txt        # Project dependencies
└─ README.md               # Project documentation
```

---

## **Acknowledgements**

* Dataset: Zindi – Financial Inclusion in Africa
* Python libraries: Streamlit, scikit-learn, pandas, ydata-profiling

---

## **License**

This project is open-source and available under the MIT License.

