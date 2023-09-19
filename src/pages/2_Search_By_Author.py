from pathlib import Path
import streamlit as st
import pandas as pd
import os
import sys
import numpy as np
import base64


#establish a filepath to the orcale_cards.csv file
filepath=os.path.join(Path(__file__).parents[1],'/data/national_news_broadcast.csv')
csv = filepath + '/data/national_news_broadcast.csv'
sys.path.insert(0, csv)

from tomongo import ToMongo
import myfuncs as mf
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
# audio_file = open('/Users/investmentguy/Downloads/idokay - Ive Seen It All.mp3', 'rb')
# audio_bytes = audio_file.read()

# st.audio(audio_bytes, format='audio/ogg', start_time=0)

# c.autoplay_audio('/Users/investmentguy/Downloads/idokay - Ive Seen It All.mp3')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

# #grab my collection
a_list = mf.pos_values(df,'author')

selection = st.selectbox('Search for your author here:', options=sorted(a_list), index=1)

#custom df for outputs and my avail states
dff = df.iloc[mf.locator(df,'author',selection)] 
#index corrector 
dff.reset_index(drop=True,inplace=True)
#create dummy string that plays nice in  streamlit
dff['pl']= mf.stringConvert(dff,'source')

#create possible title for the seleced activities
title_list = mf.pos_values(dff,'title')

titles = st.selectbox('Articles from this author:', placeholder="Click Here", options=(["Click Here"] + sorted(title_list)))

#conditional to make create different outputs
if titles == "Click Here":
    st.dataframe(pd.DataFrame({"Results": dff.title.tolist(),"Source":dff.pl.tolist()}), width=800, hide_index=True)
else:
    new_dframe = df[df['title'] == titles].reset_index()
    # for auth in df[df['title'] == titles].reset_index():
         
    st.subheader(f"The source of this article: {new_dframe['source'][0]}")
    for i in range(len(df['title'])):
            if titles == df['title'][i]:
                if df['url_to_image'][i] == 'No image found':
                    st.image('https://cdn.pixabay.com/photo/2014/04/02/17/04/newspaper-307829_1280.png')  
                else:     
                    st.image((df['url_to_image'][i]))
            

                index = i
    st.subheader('About The Article')
    st.write(df['description'][index])

    st.subheader('Press the link for more info')
    st.write((df['url'].tolist())[index])

