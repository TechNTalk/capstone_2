import streamlit as st
from tomongo import ToMongo
c=ToMongo()

# c.autoplay_audio("/Users/investmentguy/Documents/python_stuff/coding_temple/capstone_2_updated/src/I've Seen It All.mp3")
st.header("News Publication Application Summary")
st.text("""
        I believe that this platform has the potential to become a sustainable resource for 
staying informed about global topics. With partnerships established with validated 
freelance authors and renowned publishing companies, I can aim to make this platform a 
staple in your daily life. To build a robust foundation, I am considering further 
developments with additional time and resources, including:

1. Implementing a rating scale for articles, authors, and sources, inviting user feedback 
to enhance my content and graphical assessments. 
        
2. Creating a suggestion box to engage users in the platform's growth, allowing 
them to influence the development of new features and functionalities. This sense of 
involvement fosters a strong connection with our user community, ensuring their 
loyalty during any challenges we may encounter.
        
3. Establishing an internal system to accept requests from publishing companies and 
authors interested in featuring their work on my platform.
        
4. Leveraging machine learning models to suggest articles that align with users' interests.
        
5. Teasing 'Coming Soon' initiatives to keep my users excited about upcoming articles.
        
6. Utilizing push notifications to maintain user engagement.
        
7. Expanding the depth of my author and source data, including factors such as 
their tenure in the publishing industry and the age demographics of their user base."
        """)

st.text("""
        I would like to thank the News Publication for giving me
        permission to use their api.
        """)

