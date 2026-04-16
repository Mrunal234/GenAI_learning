import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="D:\Work\GenAI Practice\GenAI_learning\.env")

# configure API KEY
genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# prompt = f"""Write a {content_type} about "{topic}".
# Requirements:
# - Tone: {tone}
# - Use headings
# -Limit to {word_limit} words
# - Keep paragraphs short
# - Make it engaging
# - Add a strong introduction and conclusion"""

def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text


st.title("AI Story / Blog Generator (Gemini)")

topic = st.sidebar.text_input("Enter Topic")
content_type = st.sidebar.selectbox("Select Type", ["Story", "Blog"])
tone = st.sidebar.selectbox("Select Tone", ["Formal", "Casual", "Funny", "Inspirational"])

if st.sidebar.button("Generate"):
    prompt = f"""
    Write a {content_type} about {topic}.
    Tone: {tone}
    Make it engaging, well-structured,Limit to 200 words,Keep paragraphs short and easy to read.
    """

    output = generate_text(prompt)

    st.subheader("Generated Content")
    st.write(output)