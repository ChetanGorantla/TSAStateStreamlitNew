import streamlit as st
import joblib
import pandas as pd
import pickle

#Page details
st.set_page_config(page_title="Diabetes Predictor", page_icon="🧠")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.markdown("# Stroke Predictor")
st.write("Input your symptoms below")

#Inputs
age = st.number_input("How old are you?", value=25, min_value=25, max_value=100) 
option = st.selectbox(
    'What is your sex?',
    ('Male', 'Female'))

#Initializing columns
col1, col2 = st.columns(2)

#Inputs Column 1
avg_glucose_level = col1.number_input("What is your average glucose level?", value = 0, min_value = 0, max_value = 300)
bmi = col1.number_input("What is your BMI (Body Mass Index)?", value = 20, min_value = 20, max_value = 40)
smoking_status = col1.selectbox("What is your smoking status?", ("Never smokes", "Formerly smoked", "Smokes", "Unknown"))

#Inputs Column 2
work_type = col2.selectbox("What is your form of work?", ("Private", "Self-employed", "Govt. job"))
residence_type = col2.selectbox("What is your area of residency?", ("Urban","Rural"))
hypertension = col2.checkbox("Do you have hypertension?")
heart_disease = col2.checkbox("Do you have heart disease?")
married = col2.checkbox("Are you married?")

predict = col1.button("Predict")
                                                          
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Raleway:ital@1&display=swap');
			html, body, [class*="css"]  {
			font-family: 'Raleway', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.markdown(footer, unsafe_allow_html=True)
