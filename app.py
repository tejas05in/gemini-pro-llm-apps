import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()  # load environment variables


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro")


def get_gemini_response(question):
    respose = model.generate_content(question)
    return respose.text


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

# When submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)
