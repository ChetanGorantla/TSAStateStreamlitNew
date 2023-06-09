import streamlit as st
import requests
st.set_page_config(page_title="Find Nearby Hospitals", page_icon="🏥")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
@st.cache_resource
def get_user_location():
    ip_url = "https://api.ipify.org"
    location_url = "http://ip-api.com/json"
    ip = requests.get(ip_url).text
    print(f"IP address: {ip}")
    location = requests.get(f"{location_url}/{ip}").json()
    print(f"Location info: {location}")
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
        "key": "AIzaSyBH7EzdJtxiYWVgJ_p-MgYU7k9kt1_R9CA"
    }
    response = requests.get(url, params=params)
    hospitals = response.json()["results"]
    for hospital in hospitals:
        name = hospital["name"]
        address = hospital["vicinity"]
        rating = hospital.get("rating", "N/A")
        st.write(f"{name} ({rating}) - {address}")
def main():
    st.title("Find Nearby Hospitals")
    max_radius = st.slider("Select max distance from you (in miles):", min_value=1, max_value=50, value=5)
    st.write(f"Searching for hospitals within {max_radius} miles...")
    find_hospitals(max_radius)
if __name__ == "__main__":
    main()
    
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Raleway:ital@1&display=swap');
			html, body, [class*="css"]  {
			font-family: 'Raleway', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)
