from pathlib import Path
import streamlit as st
import pandas as pd
import os
import sys
import numpy as np
import base64

#establish a filepath to the orcale_cards.csv file
filepath=os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from tomongo import ToMongo
import myfuncs as mf
c=ToMongo()

# Initiate cursor
cursor = c.news_info.find()
df = pd.read_csv("src/I've Seen It All.mp3")

st.set_page_config(
    page_title="Articles ", #<------- Change this to the page you're currently on when copying/pasting after your imports
    page_icon="⛰️",
    menu_items={
        'About': """This is an app developed by Joshua Lewis at Coding Temple. Here are our
        Github accounts : https://github.com/TechNTalk,"""}
)
# audio_file = open('/Users/investmentguy/Downloads/idokay - Ive Seen It All.mp3', 'rb')
# audio_bytes = audio_file.read()

# st.audio(audio_bytes, format='audio/ogg', start_time=0)

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

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

# #grab my collection
a_list = mf.pos_values(df,'description')

selection = st.selectbox('Type here and click enter to search', placeholder = "Type Here", options =(["Type Here"] + a_list))

#custom df for outputs and my avail articles
dff = df.iloc[mf.locator(df,'description',selection)] 
#index corrector 
dff.reset_index(drop=True,inplace=True)
#create dummy string that plays nice in  streamlit
dff['pl']= mf.stringConvert(dff,'description')

#create possible title for the seleced activities
title_list = mf.pos_values(dff,'description')

# titles = st.selectbox('Articles from this author:', placeholder="Click Here", options=(["Click Here"] + sorted(title_list)))

if st.button("enter"):
    try:
        new_dframe = df[df['description'] == selection].reset_index()
        # for auth in df[df['title'] == titles].reset_index():
        # st.write(new_dframe)   
        st.subheader(f"The source of this article: {new_dframe['source'][0]}")
        for i in range(len(new_dframe['description'])):
            if selection == new_dframe['description'][0]:
                if new_dframe['url_to_image'][i] == 'No image found':
                    st.image('https://cdn.pixabay.com/photo/2014/04/02/17/04/newspaper-307829_1280.png')
                else:     
                    st.image((new_dframe['url_to_image'][0]))
                index = i
        st.subheader('About The Article')
        st.write(selection)

        st.subheader('Press the link for more info')
        st.write((new_dframe['url'][i]))
    except:
        ("Error in your selection. Please write a description, then press enter to continue")
  # st.dataframe(pd.DataFrame({"Results": dff.title.tolist(),"Source":dff.pl.tolist()}), width=800, hide_index=True)
# else: