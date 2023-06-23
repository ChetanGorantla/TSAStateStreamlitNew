import streamlit as st
import joblib
import pandas as pd
import pickle

#Page details
st.set_page_config(page_title="Stroke Predictor", page_icon="🧠")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.markdown("# Stroke Predictor")
st.write("Input your symptoms below")

st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('stroke.pkl','rb'))
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

inputs = [[age,option,avg_glucose_level,bmi,smoking_status,work_type,residence_type,hypertension,heart_disease,married]]

for i in range(1, len(input_arr)):
    if input_arr[i]:
        input_arr[i] = "Yes"
    else:
        input_arr[i] = "No"
@st.cache_data
    def load_pickle(file):
        return pickle.load(file)
    lbl = load_pickle(pkl_file)
	
    pkl_file.close()
    # if symptoms[i] == "Age":
    # st.write(lbl.get_params())
    input_arr[i] = lbl.transform([input_arr[i]])[0]

if st.button("Predict"):
    pred = rf.predict(pd.DataFrame([input_arr], columns=symptoms))[0]
    if pred == 1:
        st.write(
            """<div style="text-align: center;">
                <div><span style="font-size: x-large; background-color: #ff6600;">You have a HIGH chance of having diabetes or being prediabetic. Please see a doctor immediately.</span></div>
                <p>&nbsp;</p>
                <p>&nbsp;</p>
                <p><strong>Diabetes is leading cause of death across the world. An estimated 6.7 million people die from diabetes yearly, representing 11.3% of all global deaths.</strong></p>
                <p>&nbsp;</p>
                <p><em>Identifying those at the highest risk of diabetes, diagnosing as early as possible, and ensuring patients receive appropriate treatment at the correct time can prevent premature and consequential deaths. Access to noncommunicable disease medicines and basic health technologies is essential to ensure that those in need receive appropriate care.</em></p>
                </div>""",
            unsafe_allow_html=True,
        )
    else:
        st.write(
            """<div style="text-align: center;"><span style="font-size: x-large; background-color: #00ff00;">You most likely DO NOT have diabetes.</span></div>
                <p><strong>If concerned, there are several ways you can reduce your risk of developing diabetes, such as:</strong></p>
                <p><span>1. Lowering your blood and cholesterol levels.</span></p>
                <p><span> 2. Eating a healthy, balanced diet which includes plant based foods.</span></p>
                <p><span> 3. Maintaining a healthy weight.</span></p>
                <p><span> 4. Giving up and/or avoiding smoking and tobacco.</span></p>
                <p><span> 5. Reducing alcohol consumption.</span></p>
                <p><span> 6. Keeping blood pressure under control.</span></p>
                <p><span> 7. Being consistently active and involved in physical activity.</span></p>
                <p>&nbsp;</p>
                <p><strong>Diabetes is a leading cause of death globally. An estimated 6.7 million people died from cardiovascular diseases per year, representing 11.2% of all global deaths.</strong></p>
                <p>&nbsp;</p>
                <p><em>Identifying those at the highest risk of Diabetes early on,diagnosing as early as possible, and ensuring patients receive appropriate treatment at the correct time can prevent premature and consequential deaths. Access to noncommunicable disease medicines and basic health technologies is essential to ensure that those in need receive appropriate care.</em></p>
                """,
            unsafe_allow_html=True,
        )
footer = """
<style>
footer{
    visibility:visible;
}
footer:before{
    content:"Please keep in mind that this app uses predictors based on machine learning algorithms. Although the results are highly accurate, false positive or negative results can occur. If you still have concerns after consulting our app, please contact your doctor or find a hospital using our locator tool.";
    display:block;
    position:relative;
}
</style>
"""
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
