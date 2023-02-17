import streamlit as st
import pandas as pd

st.set_page_config(page_title="Medication Tracker", page_icon=":pill:")
med_data = pd.read_csv("medications.csv")
my_meds = []
search_term = st.sidebar.text_input("Search for a medication:")
filtered_data = med_data[med_data['medication_name'].str.contains(search_term, case=False)]
st.write(filtered_data[['medication_name', 'dose', 'frequency']])

st.write("Add a new medication:")
name = st.text_input("Medication name:")
dose = st.text_input("Dose:")
frequency = st.text_input("Frequency:")
if st.button("Add"):
    med_data = med_data.append({'medication_name': name, 'dose': dose, 'frequency': frequency}, ignore_index=True)
    med_data.to_csv("medications.csv", index=False)
    my_meds.append(name)

st.write("Your Medications:")
if len(my_meds) == 0:
    st.write("No medications added.")
else:
    for med in my_meds:
        st.write(med)

        
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Raleway:ital@1&display=swap');
			html, body, [class*="css"]  {
			font-family: 'Raleway', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)
