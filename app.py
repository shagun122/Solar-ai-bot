import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("OPENROUTER_API_KEY")


if not API_KEY:
    st.error("API Key is missing! Set OPENROUTER_API_KEY in a .env file.")
    st.stop()

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "your_site_url",
    "X-Title": "your_site_name",
}

def get_solar_advice(query):
    """Fetch AI response using OpenRouter with Gemini Flash Lite 2.0 Preview (free)."""
    data = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",  
        "messages": [{"role": "system", "content": "You are a solar energy expert AI."},
                     {"role": "user", "content": query}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             headers=HEADERS, data=json.dumps(data))

    try:
        json_response = response.json()
        return json_response["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        return f"Error: Unexpected response format: {response.text}"


st.title("☀️ Solar Industry AI Assistant")
st.write("Ask anything about solar energy!")

user_input = st.text_input("Enter your question:")
if user_input:
    answer = get_solar_advice(user_input)
    st.write("### Answer:")
    st.write(answer)
