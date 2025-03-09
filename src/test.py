import streamlit as st
import requests

# API URL from SheetDB
API_URL = "https://sheetdb.io/api/v1/mj8tv5n9mce76"

# Configuring Streamlit page
st.set_page_config(page_title="AYUSH Plant Chatbot", page_icon="🤖", layout="centered")

# Title of the app
st.title("AYUSHI 🌿")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to fetch plant data from SheetDB API
def get_plant_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        # Print the data to see its structure
        #st.write("Data fetched from API:", response.json())
        return response.json()  # Returns the list of plant data
    else:
        return None

# Function to search for plant info by name or related query
def find_plant_info(query, plant_data):
    query = query.lower()  # Make the query lowercase for case-insensitive matching
    #print(query)
    for plant in plant_data:
        # Check for plant name or scientific name match
        if plant["Plant Name"].lower() in query or plant["Scientific Name"].lower() in query:
            return f"**Plant Name**: {plant['Plant Name']}\n\n**Scientific Name**: {plant['Scientific Name']}\n\n**Uses**: {plant['Medicinal Use']}"
    return "Sorry, I couldn't find any relevant information about that plant."

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user's question
user_input = st.chat_input("Ask me about a plant (e.g., 'Tell me about Aloe Vera')")

if user_input:
    # Add user's input to the chat history
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Fetch plant data from API
    plant_data = get_plant_data()

    if plant_data:
        # Search the plant data for the user's query
        plant_info = find_plant_info(user_input, plant_data)
    else:
        plant_info = "Sorry, I'm having trouble accessing the plant database at the moment."

    # Add the bot's response to the chat history and display it
    st.session_state.chat_history.append({"role": "assistant", "content": plant_info})
    with st.chat_message("assistant"):
        st.markdown(plant_info)
