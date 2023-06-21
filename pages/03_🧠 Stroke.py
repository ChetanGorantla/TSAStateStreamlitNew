import streamlit as st
import joblib
import pandas as pd
import pickle

st.set_page_config(page_title="Diabetes Predictor", page_icon="🧠")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
st.markdown("# Stroke Predictor")
st.write("Input your symptoms below")

age = st.number_input("How old are you?", value=25, min_value=25, max_value=70) 
option = st.selectbox(
    'What is your sex?',
    ('Male', 'Female'))

col1, col2 = st.columns(2)

hypertension = col1.checkbox("Do you have hypertension?")
heart_disease = col1.checkbox("Do you have heart disease?")
