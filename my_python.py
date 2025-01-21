import streamlit as st
from streamlit_card import card


st.title("PYTHON PROJECT")

st.write('''
This is a Python-based Data Analysis Project designed to provide powerful insights and visualizations, leveraging the 
flexibility and interactivity of Streamlit. The application is aimed at simplifying the data exploration and analysis process 
for users, offering real-time results and actionable insights.
''')

card(
    title="Hotel Management Project",
    text="click this card for project",
    url = "https://hotelpy.streamlit.app/"
)
