import streamlit as st
from transformers import pipeline

st.title("OCR Chatbot Application")

# Load Chatbot Model
chatbot = pipeline("text-generation", model="gpt2")

# Input Text
input_text = st.text_area("Enter text for the chatbot:")

if st.button("Generate Response"):
    if input_text:
        response = chatbot(input_text, max_length=150, do_sample=True)
        st.write("Response:", response[0]['generated_text'])
    else:
        st.warning("Please enter some text.")
