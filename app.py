import streamlit as st
from chatbot import chatbot_response, learn_new_data

st.set_page_config(page_title="META-BOT", page_icon="🧠")
st.title("🧠 META-BOT (Meta-Cognitive Chatbot)")

user_input = st.text_input("You:")

if "history" not in st.session_state:
    st.session_state.history = []

if user_input:
    reply, confidence, explanation, need_learning = chatbot_response(user_input)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", reply))

    for speaker, msg in st.session_state.history:
        st.write(f"**{speaker}:** {msg}")

    st.write("🔍 Confidence:", round(confidence,2))
    st.write("🧠 Explanation:", explanation)

    if need_learning:
        correct_intent = st.text_input("Teach me correct intent (example: greeting, help, emotion_sad):")
        if st.button("Save"):
            learn_new_data(user_input, correct_intent)
            st.success("✅ Thank you! I learned. Retrain me using train.py")
