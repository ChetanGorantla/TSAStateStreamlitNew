import streamlit as st
import pandas as pd
import datetime

# Define a function to load the medication data
def load_data():
    data = pd.read_csv("medications.csv")
    data["start_date"] = pd.to_datetime(data["start_date"])
    data["end_date"] = pd.to_datetime(data["end_date"])
    return data

# Define a function to get the medications due for refill
def get_refill_medication(data):
    today = datetime.datetime.today().date()
    return data.loc[data["end_date"].dt.date <= today]

# Define the main function
def main():
    st.title("Medication Management")

    # Load the medication data
    data = load_data()

    # Display the medication data
    st.subheader("Medication List")
    st.write(data)

    # Display the medications due for refill
    st.subheader("Medications Due for Refill")
    refill_medication = get_refill_medication(data)
    st.write(refill_medication)

if name == "main":
    main()
