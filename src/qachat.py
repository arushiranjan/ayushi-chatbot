import os
from dotenv import load_dotenv
import time

load_dotenv()

import google.generativeai as genai
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

# this func should give the response we are getting from gen ai model
def get_gemini_response(question):
    response=chat.send_message(question, stream=True) # as llm model giving o/p we are going to stream and display it
    simulate_typing()
    return response

def simulate_typing():
    st.markdown("🤖 **Bot is typing...**")
    time.sleep(2)  # Simulate delay for typing effect

# initialize stremlit app
st.set_page_config(page_title="AYUSH Plant Chatbot", page_icon="🤖", layout="centered")
st.header("Gemini LLM Application")

# record the history
# initialize chat session state for chat history if it doesn't exists
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)

    # add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")