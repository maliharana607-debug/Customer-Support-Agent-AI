import streamlit as st
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Customer Support Agent",
    page_icon="🎧",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:1rem;
}

section[data-testid="stSidebar"]{
    background:#1A1C24;
}

section[data-testid="stSidebar"] h1{
    font-size:28px;
}

div[data-testid="stChatMessage"]{
    border-radius:15px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🎧 Support Center")

    st.success("🟢 Online")

    st.markdown("---")

    st.subheader("Services")

    st.markdown("""
📦 Orders

🚚 Shipping

💳 Payments

🔄 Returns
""")

# -----------------------------
# Header
# -----------------------------
st.title("🤖 AI Customer Support Agent")

st.write(
    "Fast AI-powered customer support for orders, shipping, payments, and returns."
)

st.divider()

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
if user_input := st.chat_input("Ask a question..."):

    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system="You are a helpful customer support assistant. Answer customer questions briefly, professionally, and clearly. Do not use large markdown headings. Respond naturally like a customer support representative using short paragraphs and bullet points when appropriate.",
        messages=st.session_state.messages
    )

    assistant_message = response.content[0].text

    with st.chat_message("assistant"):
        st.write(assistant_message)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )