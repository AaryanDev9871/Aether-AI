import streamlit as st
from chatbot import get_response

st.markdown("""
<div style="text-align:center;padding:15px">

<h1 style="color:#6b4f3a;">
☕ Aether AI
</h1>

<p style="color:#8a6b54;">
Your Elegant AI Companion
</p>

</div>
""", unsafe_allow_html=True)

# Page Config

st.set_page_config(
    page_title="Aether AI",
    page_icon="🤖",
    layout="wide"
)

# Load CSS

with open("styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Sidebar

with st.sidebar:

    st.markdown("# 🤖 Aether AI")

    st.caption("Nothing OS Inspired")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.caption("Powered by Gemini AI")

# Header

st.markdown("""
<div style="text-align:center">

<h1>🤖 Aether AI</h1>

<p style="color:gray">
Beautiful AI Assistant built with Python
</p>

</div>
""", unsafe_allow_html=True)

# Session State

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Messages

for message in st.session_state.messages:

    avatar = "🧑" if message["role"] == "user" else "🤖"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):
        st.markdown(message["content"])

# Chat Input

prompt = st.chat_input(
    "Ask me anything..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message(
        "user",
        avatar="🧑"
    ):
        st.markdown(prompt)

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        placeholder = st.empty()

        placeholder.markdown(
            "⚪ Thinking..."
        )

        response = get_response(prompt)

        placeholder.markdown(
            response
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )