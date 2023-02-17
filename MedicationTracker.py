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
    search_term = st.text_input("Search Medications")
    if search_term:
        filtered_data = data[data["medication_name"].str.contains(search_term, case=False)]
        if filtered_data.empty:
            st.write("No medications found.")
        else:
            st.write(filtered_data)
    else:
        st.write(data)

    # Display the medications due for refill
    st.subheader("Medications Due for Refill")
    refill_medication = get_refill_medication(data)
    st.write(refill_medication)

    # Allow the user to add a new medication
    st.subheader("Add New Medication")
    medication_name = st.text_input("Medication Name")
    start_date = st.date_input("Start Date", datetime.date.today())
    end_date = st.date_input("End Date", datetime.date.today())
    if st.button("Add Medication"):
        new_data = pd.DataFrame({
            "medication_name": [medication_name],
            "start_date": [start_date],
            "end_date": [end_date]
        })
        data = pd.concat([data, new_data], ignore_index=True)
        data.to_csv("medications.csv", index=False)
        st.success("Medication added to the list.")


if name == "main":
    main()
