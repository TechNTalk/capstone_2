from pathlib import Path
import streamlit as st
import pandas as pd
import os
import sys
import base64

#Grab the filepath:
filepath=os.path.join(Path(__file__).parents[1])

#Insert the filepath into the system:
sys.path.insert(0, filepath)

#Import the ToMongo class:
from tomongo import ToMongo
import myfuncs as mf

# Instaniate the class:
c=ToMongo()

# Initiate cursor
cursor = c.news_info.find()
df = pd.read_csv('/Users/investmentguy/Documents/python_stuff/coding_temple/capstone_2_updated/src/data/national_news_broadcast.csv')

st.set_page_config(
    page_title="Articles ", #<------- Change this to the page you're currently on when copying/pasting after your imports
    page_icon="⛰️",
    menu_items={
        'About': """This is an app developed by Joshua Lewis at Coding Temple. Here are our
        Github accounts : https://github.com/TechNTalk,"""}
)
# def autoplay_audio(file_path: str):
#         with open(file_path, "rb") as f:
#             data = f.read()
#             b64 = base64.b64encode(data).decode()
#             md = f"""
#                 <audio controls autoplay="true">
#                 <source src="data:audio/ogg;base64,{b64}" type="audio/mp3">
#                 </audio>
#                 """
#             st.markdown(
#                 md,
#                 unsafe_allow_html=True,
#             )
# autoplay_audio('/Users/investmentguy/Downloads/idokay - Ive Seen It All.mp3')
c.autoplay_audio('/Users/investmentguy/Downloads/idokay - Ive Seen It All.mp3')
st.title("Find An Article")
art_list = df.title.tolist()

select = st.selectbox('Search For An Article', options=sorted(art_list))

if select:
    new_dframe = df[df['title'] == select].reset_index()
    st.subheader(f"The source of this article: {new_dframe['source'][0]}")
    for i in range(len(df['title'])):
            print(df['title'][i])
            if select == df['title'][i]:
                if df['url_to_image'][i] == 'No image found':
                   st.image('https://cdn.pixabay.com/photo/2014/04/02/17/04/newspaper-307829_1280.png')  
                else:     
                    st.image((df['url_to_image'][i]))
            

                index = i
    st.subheader('About The Article')
    st.write(df['description'][index])

st.subheader('Press the link for more info')
st.write(df['url'][index])
# #grab my collection
# cursor=c.news_info.find({ "longitude" : {"$ne" :None},"latitude" : {"$ne" :None}})
# answer = st.text_input('Enter an article name: ', value = 'The AI Engine that Fits in 100K')
# st.write(pd.DataFrame((list(c.news_info.find({'title': answer})))))


