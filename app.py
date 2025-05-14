import streamlit as st
from chatbot import get_sentiment, generate_chatbot_reply

# Set the title for the web app
st.title("AI Mental Health Chatbot")
st.subheader("Talk to me, I'm here to help.")

# Create a session state for tracking conversation
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Function to handle the user input and AI responses
def process_input(user_input):
    # Add user's input to chat history
    st.session_state.chat_history.append(f"You: {user_input}")

    # Get sentiment of the user's input (positive/negative)
    sentiment = get_sentiment(user_input)

    # Generate AI reply based on the input
    ai_reply = generate_chatbot_reply(user_input)

    # Add AI's response to the chat history
    st.session_state.chat_history.append(f"AI: {ai_reply}")

    return sentiment, ai_reply

# Display chat history
for message in st.session_state.chat_history:
    st.write(message)

# Text input from the user
user_input = st.text_input("How are you feeling today?")

if user_input:
    sentiment, ai_reply = process_input(user_input)
    if sentiment == "POSITIVE":
        st.write("AI: I'm glad you're feeling positive today! 😊")
    else:
        st.write("AI: I'm here for you. Let's talk through it. 💬")
