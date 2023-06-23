import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Page details
st.set_page_config(page_title="Stroke Predictor", page_icon="🧠")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.markdown("# Stroke Predictor")
st.write("Input your symptoms below")

st.set_option('deprecation.showfileUploaderEncoding', False)

# Load the ML model
try:
    model = pickle.load(open('stroke2.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading the model: {e}")

# Inputs
age = st.number_input("How old are you?", value=25, min_value=25, max_value=100)
sex = st.selectbox('What is your sex?', ('Male', 'Female'))

# Initializing columns
col1, col2 = st.columns(2)

# Inputs Column 1
avg_glucose_level = col1.number_input("What is your average glucose level?", value=0.0, min_value=0.0, max_value=300.0)
bmi = col1.number_input("What is your BMI (Body Mass Index)?", value=20.0, min_value=20.0, max_value=40.0)
smoking_status = col1.selectbox("What is your smoking status?", ("Never smokes", "Formerly smoked", "Smokes", "Unknown"))

# Inputs Column 2
work_type = col2.selectbox("What is your form of work?", ("Private", "Self-employed", "Govt. job"))
residence_type = col2.selectbox("What is your area of residency?", ("Urban", "Rural"))
hypertension = col2.checkbox("Do you have hypertension?")
heart_disease = col2.checkbox("Do you have heart disease?")
married = col2.checkbox("Are you married?")

predict = col1.button("Predict")

# Prepare input data
sex_male = 1 if sex == 'Male' else 0
sex_female = 1 if sex == 'Female' else 0

# One-hot encode smoking status
smoking_never = 1 if smoking_status == 'Never smokes' else 0
smoking_former = 1 if smoking_status == 'Formerly smoked' else 0
smoking_smokes = 1 if smoking_status == 'Smokes' else 0
smoking_unknown = 1 if smoking_status == 'Unknown' else 0

# One-hot encode work type
work_private = 1 if work_type == 'Private' else 0
work_self_employed = 1 if work_type == 'Self-employed' else 0
work_govt_job = 1 if work_type == 'Govt. job' else 0

# One-hot encode residence type
residence_urban = 1 if residence_type == 'Urban' else 0
residence_rural = 1 if residence_type == 'Rural' else 0

# Select relevant features for prediction
input_data = np.array([[age, sex_male, sex_female, avg_glucose_level, bmi, smoking_never, smoking_former, smoking_smokes, smoking_unknown, married]], dtype=object)

if predict:
    try:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.write("The model predicts that you are likely to have a stroke.")
        else:
            st.write("The model predicts that you are unlikely to have a stroke.")
    except Exception as e:
        st.error(f"Error predicting stroke: {e}")
