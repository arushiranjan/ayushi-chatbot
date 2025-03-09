import json
import os
import google.generativeai as genai
import streamlit as st
import requests
from dotenv import load_dotenv

HISTORY_FILE = "chat_history.json"
API_URL = "https://sheetdb.io/api/v1/mj8tv5n9mce76"

# Load environment variables
load_dotenv()

# Configure the API key for the Gemini AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini AI model setup
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to load existing chat history from a file
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Function to save chat history to a file
def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file)

# Initialize session state for chat history, and load from the file if available
if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_history()

# Initialize a toggle to switch between chat and history view
if "show_history" not in st.session_state:
    st.session_state.show_history = False

# Function to fetch plant data from SheetDB API
def get_plant_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()  # Returns the list of plant data
    else:
        return None

# Function to search for plant info by name or related query
def find_plant_info(query, plant_data):
    query = query.lower()  # Make the query lowercase for case-insensitive matching
    for plant in plant_data:
        # Check for plant name or scientific name match
        if plant["Plant Name"].lower() in query or plant["Scientific Name"].lower() in query:
            return f"**Plant Name**: {plant['Plant Name']}\n\n**Scientific Name**: {plant['Scientific Name']}\n\n**Uses**: {plant['Medicinal Use']}"
    return "Sorry, I couldn't find any relevant information about that plant."

# Function to get response from Gemini AI model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)  # Streaming response
    return response

# Streamlit page configuration
st.set_page_config(page_title="AYUSHI Chatbot", page_icon="🤖", layout="centered")
st.title("AYUSHI 🌿")

# Toggle between chat view and history view
if st.session_state.show_history:
    # Display chat history
    st.subheader("Chat History")
    if st.session_state.chat_history:
        for message in st.session_state.chat_history:
            role = message["role"]
            content = message["content"]
            st.write(f"**{role.capitalize()}:** {content}")
    else:
        st.write("No chat history available.")

    # Button to go back to the chat page
    if st.button("Back to Chat"):
        st.session_state.show_history = False
else:
    # Input field for user's question
    user_input = st.chat_input("Ask me a question (e.g., 'Tell me about Aloe Vera' or general queries)")

    if user_input:
        # Add user's input to the chat history
        st.chat_message("user").markdown(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Check if user is asking about a plant (e.g., mentioning a plant name)
        plant_data = get_plant_data()
        if plant_data and any(plant["Plant Name"].lower() in user_input.lower() for plant in plant_data):
            # Search the plant data for the user's query
            plant_info = find_plant_info(user_input, plant_data)
            bot_response = plant_info
        else:
            # If it's not a plant-specific query, use the Gemini AI model
            response = get_gemini_response(user_input)
            bot_response = ''.join([chunk.text for chunk in response])

        # Add the bot's response to the chat history and display it
        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant"):
            st.markdown(bot_response)

        # Save the updated chat history to the JSON file
        save_history(st.session_state.chat_history)

    # Button to view chat history
    if st.button("View Chat History"):
        st.session_state.show_history = True
