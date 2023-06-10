import streamlit as st

col1, col2, col3 = st.columns(3, gap = "medium")

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")
   
   st.header("Fungal Infection")
   st.text("Symptoms include itching, soreness, redness or rash in the affected area. Discolored, thick or cracked nails. Pain while eating, loss of taste or white patches in mouth or throat. A painless lump under your skin.")
   st.text("A Fungal Infection is a fungus that invades the tissue which can cause a disease that's confined to the skin, spreads into tissue, bones, and organs, or affects the whole body.")
   st.text("To avoid attracting a Fungal Infection, keep your skin clean and dry, particularly the folds of your skin. Maintain good hygeine.")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")
   st.header("Doggies are very nice to play with because they aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
   st.header("Doggies are very nice to play with because they aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
   st.image("https://static.streamlit.io/examples/dog.jpg")


