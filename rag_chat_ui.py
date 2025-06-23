import streamlit as st
import requests

st.set_page_config(page_title="NurseAI Chat", layout="wide")

st.markdown(
    """
    # 🩺 NurseAI Chat
    
    **Welcome to the AI Nurse Assistant!**
    
    This chat simulates a nurse assistant for non-real patients, powered by AI. All patient charts and data are fictional and generated for educational or demonstration purposes. The responses are powered by OpenAI's gpt-3.5-turbo.
    """
)

patient_id = st.sidebar.selectbox("Select Patient", [f"patient{i}" for i in range(1, 9)])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask a question about the patient...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = requests.post(
            # "http://localhost:8000/ask",
            "https://nursegame-chat-backend.onrender.com/ask",
            json={"question": user_input, "patient_id": patient_id},
            timeout=10
        )
        answer = response.json().get("answer", "⚠️ No answer found.")
    except Exception as e:
        answer = f"⚠️ Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
