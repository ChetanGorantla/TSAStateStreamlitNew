import streamlit as st

st.set_page_config(page_title="KGK Diagnosis", page_icon="🏠")
st.markdown("KGK Diagnosis")
SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True

st.image("newLogo.png")
st.write(
    "Welcome! The Doctor is a univeral medical diagnostic tool with a range of functionality."
)
st.write(
    "Choose a page to the left most consistent with the particular problem you are having, and you can find more information on the individual screens."
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
