import streamlit as st
import base64



st.set_page_config(
    page_title="News App", #<------- Change this to the page you're currently on when copying/pasting after your imports
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

st.title("World News Publication")

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGvE9EopHY-v6XRwTtN1_OvTeZokvi904_Zg&usqp=CAU',width=200)

st.text("""In today's rapidly evolving technological landscape, we recognize the pressing need 
to keep pace with change while preserving the essence of our origins. Is it possible 
to seamlessly blend the comforts of tradition with the ever-advancing world of 
technology? Welcome to the World News Publication App, featuring access to a 
staggering 30,000 publications. This app places up-to-the-minute news articles right 
at your fingertips, allowing you to enjoy them on the go, at your favorite coffee 
shop, or from the comfort of your own home. It's simplicity at its finest.""")

st.text("The application uses the following to create a National Parks App:")
        
st.text(""">Streamlit 
>Python
>MongoDB
>Pandas
>Base64
>News API """)

st.header("Here are the different pages of the application:")

st.subheader('Articles')

st.text("""As you navigate to the 'Articles' page, reminisce about the days when you'd eagerly 
open your morning newspaper, and the first captivating image would beckon you. With 
the app, you can effortlessly scroll through a myriad of articles without ever 
needing to turn a page. Discover an intriguing article you'd like to delve deeper 
into? Simply click the link below, and you'll be instantly directed to the full 
article.""")

# st.markdown("""The information fields displayed are:
#         name of the article, title, the url image, and url link to read more.""")

st.subheader("Search By Author")
st.text("""Found an author whose work resonates with you and want to explore their other 
publications? Head over to the 'Search By Author' Page and indulge your curiosity.""")

st.subheader("Search By Description")
st.text("""Struggling to recall the name of an article or the author who wrote it? The 
'Search By Description' Page is designed with user-friendliness in mind, making it a 
breeze to locate your desired content.""")
        
st.subheader("Visuals Page")        

st.text("""For the data and statistics enthusiasts among us, the 'Visuals' Page offers 
graphical insights, allowing you to compare your favorite authors and assess the 
contributions of various companies or sources behind these authors' works.""")

st.subheader("Summary")
st.markdown("""This page provides a comprehensive explanation of further implementations to better improve
the scalibility of this app""")
