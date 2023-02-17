import streamlit as st
import pandas as pd

# Define the file name for the medication data
MEDICATION_FILE = "medications.csv"

# Load the medication data from the CSV file
@st.cache
def load_data():
    data = pd.read_csv(MEDICATION_FILE)
    return data

# Add a new medication to the CSV file
def add_medication(name, dose, frequency):
    new_row = {'name': name, 'dose': dose, 'frequency': frequency}
    with open(MEDICATION_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=new_row.keys())
        writer.writerow(new_row)

# Define the search function
def search_data(search_term, data):
    if search_term:
        filtered_data = data[data['name'].str.contains(search_term, case=False)]
    else:
        filtered_data = data
    return filtered_data
st.set_page_config(page_title="Medication Management", page_icon=":pill:")

medication_data = load_data()

st.title("Medication Management")
st.subheader("Add a New Medication")
name = st.text_input("Name")
dose = st.text_input("Dose")
frequency = st.text_input("Frequency")
if st.button("Add Medication"):
    add_medication(name, dose, frequency)
    st.success("Medication added!")
    # Update the medication data
    medication_data = load_data()
st.subheader("Search Medications")
search_term = st.text_input("Enter a medication name to search")
filtered_data = search_data(search_term, medication_data)
st.write("Here are your search results:")
if not filtered_data.empty:
    st.write(filtered_data[['name', 'dose', 'frequency']])
else:
    st.write("No medications found.")
