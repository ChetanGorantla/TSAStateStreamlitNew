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
