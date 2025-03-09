

AYUSHI Chatbot 🌿

Overview

AYUSHI Chatbot is an AI-powered chatbot designed to provide knowledge about medicinal plants. It fetches data from a SheetDB API and uses Google's Gemini AI model to answer general queries. The chatbot is built using Streamlit for the interface and supports a chat history feature.

Features

🌱 Provides information on medicinal plants from a SheetDB database.

💡 Uses Google Gemini AI for answering general queries.

💾 Saves chat history locally in a JSON file.

🔄 Allows users to toggle between chat and history views.

🚀 Built with Streamlit for a smooth UI experience.

Tech Stack

Python

Streamlit

Google Gemini AI (Generative AI)

SheetDB API

Requests (for API calls)

Dotenv (for environment variable management)

Installation

Prerequisites

Ensure you have the following installed:

Python 3.x

pip

Steps

Clone the repository:

git clone <repository-url>
cd ayushi-chatbot

Install dependencies:

pip install -r requirements.txt

Set up environment variables:

Create a .env file in the project root.

Add your Google API key:

GOOGLE_API_KEY=your_google_api_key

Run the chatbot:

streamlit run app.py

Usage

Enter a query related to medicinal plants (e.g., "Tell me about Aloe Vera").

If the plant is found in the database, the bot will return its scientific name and medicinal uses.

If it's a general question, the Gemini AI model will generate a response.

Click "View Chat History" to see previous conversations.

File Structure

📂 ayushi-chatbot
 ┣ 📜 app.py               # Main Streamlit app
 ┣ 📜 requirements.txt     # Dependencies
 ┣ 📜 chat_history.json    # Stores chat history
 ┣ 📜 .env                 # API keys (ignored in git)
 ┗ 📜 README.md            # Project documentation

API Details

SheetDB API: Fetches medicinal plant data.

Google Gemini AI: Provides intelligent responses for general queries.

Contributing

If you want to contribute:

Fork the repository.

Create a new branch: git checkout -b feature-branch

Make your changes and commit them.

Push to your fork and submit a Pull Request.

License

This project is open-source and available under the MIT License.

Contact

For any questions or issues, feel free to reach out!

