import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="D:\Work\GenAI Practice\GenAI_learning\.env")


# Configure API
genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))


# Use latest working model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_flashcards(text, num_cards):
    prompt = f"""
    Convert the following text into {num_cards} flashcards.

    Format strictly like this:
    Q1: question
    A1: answer

    Q2: question
    A2: answer

    Keep answers short and clear.

    Text:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text


# UI
st.title("📚 AI Flashcards Generator")

# Main input
input_text = st.text_area("Paste your notes here")

# Sidebar settings
st.sidebar.header("Settings")

num_cards = st.sidebar.slider("Number of flashcards", 3, 15, 5)

generate_btn = st.sidebar.button("Generate")

# Generate
if generate_btn:
    if input_text.strip() == "":
        st.warning("Please enter some text")
    else:
        output = generate_flashcards(input_text, num_cards)

        st.subheader("Flashcards")
        st.write(output)