import plotly.express as px
from pathlib import Path
import streamlit as st
import pandas as pd
import os
from tomongo import ToMongo
c=ToMongo()

c.autoplay_audio("src/I've Seen It All.mp3")
#Establish a filepath to the national_news_broadcast.csv file
filepath = os.path.join(Path(__file__).parents[1], 'data', 'national_news_broadcast_graph.csv')
df = pd.read_csv(filepath, low_memory=False)

# Take in a user input
answer = st.selectbox("Select a Column to Visualize:", options=list(df.columns))
if answer:
    try:
        st.plotly_chart(px.histogram(df, answer))
    except BaseException:
        print("Error visualizing this column")
