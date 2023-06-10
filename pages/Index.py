import streamlit as st

col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")
   st.header("Doggies are very nice to play with because they aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

with col4:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")
