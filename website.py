import streamlit as st
import google.generativeai as genai
api_key= st.secrets["GOOGLE_API_KEY"]
# api_key="AIzaSyA5OlFXSvu9N8J_feL3X_R4xpgAIFSLxmk"
genai.configure(api_key= api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2=st.columns(2)


with col1:

    st.subheader("hi:wave:")
    st.title("i am jakir")
with col2:

    st.image("images/20231209.jpg")
st.title(" ")
persona = """
          You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
          """

st.title("jakirs AI Bot")
user_question = st.text_input("ask anything about me")

if st.button("ASK",use_container_width=400):
    prompt= persona+ "here is question that  the user asked" +  user_question
    response = model.generate_content(prompt)
    st.write(response.text)

col1,col2 = st.columns(2)
with col1:
    st.subheader("youtube channel")
    st.write("Lagrest computer vision channel")
    st.write("- 400k subscribers")
    st.write("- 1.5 million+ views")
    st.write("- 1.5 million hours watch time")
with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3...")

st.title(" ")

st.title("My Setup ")
st.image("images/20230910.jpg")

st.title(" ")
st.title(" My Skill")
st.slider("Programming",0,100,70)
st.slider("Teaching",0,100,70)
st.slider("Robotics",0,100,70)

st.title(" ")
st.title("Gallery")

col1,col2,col3 = st.columns(3)

with col1:
    st.image("images/20230915.jpg")
    st.image("images/20230924.jpg")
    st.image("images/20231001.jpg")


with col2:
    st.image("images/20231110.jpg")
    st.image("images/20231124.jpg")
    st.image("images/20231209.jpg")

with col3:
    st.image("images/20231110.jpg")
    st.image("images/20231209.jpg")
    st.image("images/20231209.jpg")

st.subheader(" ")

st.write("Contact")
st.title("For any inquries, please contact me")
st.subheader("mohammodjakir.789@gamil.com")
