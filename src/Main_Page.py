import streamlit as st
import base64



st.set_page_config(
    page_title="News App", #<------- Change this to the page you're currently on when copying/pasting after your imports
    page_icon="⛰️",
    menu_items={
        'About': """This is an app developed by Joshua Lewis at Coding Temple. Here are our
        Github accounts : https://github.com/TechNTalk,"""}
)
def autoplay_audio(file_path: str):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio controls autoplay="true">
                <source src="data:audio/ogg;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(
                md,
                unsafe_allow_html=True,
            )
autoplay_audio('/Users/investmentguy/Downloads/idokay - Ive Seen It All.mp3')

st.title("National News Publication")

st.image('https://storage.googleapis.com/stateless-mountainmedianews-co/sites/29/2020/09/US-Text.jpg',width=200)

st.text("My application uses the following to create a National Parks App:")
        
st.text(""">Streamlit 
>Python
>MongoDB
>Pandas
>News API """)

st.header("Here are the different pages of my application:")

st.subheader('Articles')

st.text('Queries to pull up information for each article provided.')

st.markdown("""The information fields displayed are:
        name of the article, title, the url image, and url link to read more.""")

st.subheader("Search By Author")
st.text("Queries and returns all articles by author name.")

st.subheader("Summary")
st.markdown("""This page provides a comprehensive explanation 
        of the app's internal mechanisms and delves into the underlying 
        reasons for each design choice.""")
