import streamlit as st
import requests

def get_user_location():
    ip_url = "https://api.ipify.org"
    location_url = "http://ip-api.com/json"
    ip = requests.get(ip_url).text
    location = requests.get(f"{location_url}/{ip}").json()
    return location["lat"], location["lon"]

def find_hospitals(max_radius):
    lat, lng = get_user_location()
    location = f"{lat},{lng}"
    radius = max_radius * 1609.34  # Convert miles to meters
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "type": "hospital",
        "key": "AIzaSyBVcFCp2zsoinAa85PBwUhYfJ2mEc7bwYU"
    }
    response = requests.get(url, params=params)
    hospitals = response.json()["results"]
    results = []
    for hospital in hospitals:
        name = hospital["name"]
        address = hospital["vicinity"]
        rating = hospital.get("rating", "N/A")
        result = {"name": name, "rating": rating, "address": address}
        results.append(result)
    return results

st.title("Hospitals Near You")
max_radius = st.slider("Maximum Distance (miles)", 1, 50, 10)
if st.button("Search"):
    hospitals = find_hospitals(max_radius)
    for hospital in hospitals:
        st.write(hospital["name"])
        st.write(f"Rating: {hospital['rating']}")
        st.write(hospital["address"])
        st.write("---")
