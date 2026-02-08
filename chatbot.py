import pickle
import numpy as np
from textblob import TextBlob

model = pickle.load(open("model/chatbot_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

responses = {
    "greeting": "Hello! How can I help you today?",
    "goodbye": "Goodbye! Take care 😊",
    "emotion_sad": "I'm sorry you're feeling this way. Want to talk about it?",
    "emotion_happy": "That’s wonderful to hear! 😄",
    "career_advice": "Tell me your interests and I can suggest career paths.",
    "help": "I am here to help you. Please explain your problem.",
    "info_ai": "AI is the science of making machines intelligent.",
    "thanks": "You're welcome! Happy to help!"
}

def get_personality(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment < -0.3:
        return "supportive"
    elif sentiment > 0.3:
        return "friendly"
    else:
        return "neutral"

def chatbot_response(user_input):
    X = vectorizer.transform([user_input])
    probs = model.predict_proba(X)[0]

    confidence = max(probs)
    intent = model.classes_[np.argmax(probs)]

    tone = get_personality(user_input)
    explanation = f"I predicted this because your message matches the '{intent}' category."

    if confidence < 0.6:
        return "🤔 I'm not confident about this. Please teach me the correct intent.", confidence, explanation, True

    reply = responses.get(intent, "I am not sure how to answer that.")

    if tone == "supportive":
        reply = "💙 " + reply
    elif tone == "friendly":
        reply = "😄 " + reply

    return reply, confidence, explanation, False


def learn_new_data(question, intent):
    with open("data/dataset.csv", "a") as f:
        f.write(f"\n{question},{intent}")
