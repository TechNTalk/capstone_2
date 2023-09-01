import streamlit as st
from tomongo import ToMongo
c=ToMongo()

c.autoplay_audio("/Users/investmentguy/Documents/python_stuff/coding_temple/capstone_2_updated/src/I've Seen It All.mp3")
st.header("News Publication Application Summary")
st.text("""
        The purpose of this application is to create an application using the
        News Pubilcation Api. The first steps to do this was pulling the data,
        cleaning the data and pushing the data to MongoDB. Afterwards, I created a
        virtual environment that housed all of my python installs and
        the application. Following that, I queried the data and ran it through
        Streamlit. I then created an easily accessible application that allows
        the user to look up any author or the article and its corresponding info.
        """)

st.text("""
        I would like to thank the News Publication for giving me
        permission to use their api.
        """)

st.image('https://logos-download.com/wp-content/uploads/2016/09/MongoDB_logo_Mongo_DB.png')