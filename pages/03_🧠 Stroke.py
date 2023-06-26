import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open("stroke.pickle", "rb") as f:
    model = pickle.load(f)

# Function to preprocess the data
def preprocess_data(df):
    # Encode categorical features
    label_encoder = LabelEncoder()
    df['gender'] = label_encoder.fit_transform(df['gender'])
    df["Residence_type"] = label_encoder.fit_transform(df["Residence_type"])
    df["ever_married"] = label_encoder.fit_transform(df["ever_married"])
    df['smoking_status'] = label_encoder.fit_transform(df['smoking_status'])

    # Perform one-hot encoding
    to_encode = pd.get_dummies(df[['work_type']])
    df = df.merge(to_encode, left_index=True, right_index=True, how='left')
    df.drop(['work_type'], inplace=True, axis=1)

    return df

# Function to make predictions
def predict_stroke(data):
    prediction = model.predict(data)
    return prediction

# Streamlit app
def main():
    st.title("Stroke Prediction")
    st.write("Enter the patient's information to predict the likelihood of a stroke.")

    # Create input fields for user input
    age = st.slider("Age", min_value=1, max_value=100, value=30)
    hypertension = st.radio("Hypertension", ['Yes', 'No'])
    heart_disease = st.radio("Heart Disease", ['Yes', 'No'])
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=1.0, step=1.0, value=100.0)
    bmi = st.number_input("BMI", min_value=1.0, step=1.0, value=25.0)
    gender = st.selectbox("Gender", ['Male', 'Female'])
    residence_type = st.selectbox("Residence Type", ['Urban', 'Rural'])
    ever_married = st.selectbox("Ever Married", ['Yes', 'No'])
    smoking_status = st.selectbox("Smoking Status", ['formerly smoked', 'never smoked', 'smokes'])
    work_type = st.selectbox("Work Type", ['Private', 'Self-employed', 'Govt_job', 'Children'])

    # Prepare user input data
    input_data = {
        'age': [age],
        'hypertension': [1 if hypertension == 'Yes' else 0],
        'heart_disease': [1 if heart_disease == 'Yes' else 0],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'gender': [gender],
        'Residence_type': [residence_type],
        'ever_married': [ever_married],
        'smoking_status': [smoking_status],
        'work_type_Private': [1 if work_type == 'Private' else 0],
        'work_type_Self-employed': [1 if work_type == 'Self-employed' else 0],
        'work_type_Govt_job': [1 if work_type == 'Govt_job' else 0],
        'work_type_Children': [1 if work_type == 'Children' else 0]
    }
    input_df = pd.DataFrame(input_data)

    # Preprocess user input data
    processed_data = preprocess_data(input_df)

    if st.button("Predict"):
        # Make prediction
        prediction = predict_stroke(processed_data)

        # Display the prediction result
        if prediction[0] == 1:
            st.error("The patient is at high risk of a stroke.")
        else:
            st.success("The patient is at low risk of a stroke.")

if __name__ == '__main__':
    main()
