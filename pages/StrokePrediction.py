
import streamlit as st
import pickle
import numpy as np

# Load the pickled model
with open('stroke.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a function to predict the diagnosis
def predict_diagnosis(features):
    features_array = np.array(features).reshape(1, -1)
    diagnosis = model.predict(features_array)[0]
    return diagnosis

# Define the Streamlit app
def app():
    st.title('Diagnosis App')
    st.write('Please enter the following 11 factors to receive a diagnosis:')
    feature_names = ['Factor 1', 'Factor 2', 'Factor 3', 'Factor 4', 'Factor 5', 'Factor 6', 'Factor 7', 'Factor 8', 'Factor 9', 'Factor 10', 'Factor 11']
    features = []
    for feature_name in feature_names:
        feature_value = st.number_input(feature_name, min_value=0, max_value=100, value=50)
        features.append(feature_value)
    if st.button('Diagnose'):
        diagnosis = predict_diagnosis(features)
        st.write('Diagnosis:', diagnosis)
