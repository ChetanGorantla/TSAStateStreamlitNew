import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('stroke2.pkl','rb'))

st.set_page_config(page_title="Diabetes Predictor", page_icon="🧠")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
st.markdown("# Diabetes  Predictor")
st.write("Input your symptoms below")
age = st.slider("Input Your age", 0, 120)
hypertension = st.checkbox("Do you suffer from hypertension?")
heartdisease = st.checkbox("Do you suffer from heartdisease?")
sugar = st.slider("Please input your most recent measured glucose level",150.0, 300.000)
bmi = st.slider("Please input your BMI",0.0,70.0)

  inputs = [[age,hypertension,heartdisease,sugar,bmi]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)
    if updated_res == 0:
       st.write("You are unlikely to suffer from a stroke")
    else:
       st.write("You are at risk of suffering from a stroke")
   


if __name__ =='__main__':
  main()
