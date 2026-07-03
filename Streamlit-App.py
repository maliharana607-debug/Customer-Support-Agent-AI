import streamlit as st
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

st.set_page_config(page_title="Support Agent", page_icon="🤖")

st.title("🤖 AI Customer Support Agent")
st.write("Ask me anything about orders, shipping, or products!")

# Initialize session state for conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if user_input := st.chat_input("Type your question..."):
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Add to messages
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get Claude response
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system="You are a helpful customer support agent. Answer questions briefly and clearly.",
        messages=st.session_state.messages
    )
    
    assistant_message = response.content[0].text
    
    # Show agent response
    with st.chat_message("assistant"):
        st.write(assistant_message)
    
    # Add to messages
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})