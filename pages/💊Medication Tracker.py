import streamlit as st
import pandas as pd
med_data = pd.read_csv("medications.csv")

def filter_data(search_term):
    filtered_data = med_data[med_data['name'].str.contains(search_term, case=False)]
    return filtered_data
# Define a function to add a new medication to the medication data CSV file
def add_medication(name, dose, frequency):
    new_med = {'name': name, 'dose': dose, 'frequency': frequency}
    med_data = med_data.append(new_med, ignore_index=True)
    med_data.to_csv("medications.csv", index=False)
    return med_data
def app():
    # Set the app title and icon
    st.set_page_config(page_title="Medication Tracker", page_icon=":pill:")
    # Set the app header
    st.title("Medication Tracker")
    # Add a search bar to filter the medication data by name
    search_term = st.text_input("Search for a medication:")
    filtered_data = filter_data(search_term)
    # Display the filtered medication data
    if not filtered_data.empty:
        st.write(filtered_data[['name', 'dose', 'frequency']])
    else:
        st.write("No matching medications found.")
    #add a new medication to the CSV file
    st.header("Add a new medication")
    name = st.text_input("Medication name:")
    dose = st.text_input("Medication dose:")
    frequency = st.text_input("Medication frequency:")
    if st.button("Add medication"):
        add_medication(name, dose, frequency)
        st.success("Medication added!")
