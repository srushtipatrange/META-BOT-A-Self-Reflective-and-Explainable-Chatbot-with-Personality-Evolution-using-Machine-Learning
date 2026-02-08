# 🧠 META-BOT  
### A Self-Reflective and Explainable Chatbot with Personality Evolution using Machine Learning

META-BOT is an intelligent chatbot designed using machine learning that can:
- Predict user intent
- Explain its reasoning
- Adapt personality based on emotion
- Detect low confidence
- Learn from user feedback

This project demonstrates the concept of **meta-cognition in AI**, where the chatbot understands its own uncertainty and improves over time.

---

## 🚀 Features

- Intent classification using Machine Learning
- Confidence-based self-reflection
- Explainable AI responses
- Personality adaptation using sentiment analysis
- Human-in-the-loop learning
- Streamlit web interface

---

## 🛠 Technologies Used

- Python
- Scikit-learn
- Pandas
- TextBlob (sentiment analysis)
- Streamlit (web interface)

---

## 📁 Project Structure

meta_bot/
│
├── data/
│ └── dataset.csv
│
├── model/
│ ├── chatbot_model.pkl
│ └── vectorizer.pkl
│
├── train.py
├── chatbot.py
├── app.py
└── README.md


---

## ⚙️ Installation and Setup

### Step 1: Install Python
Download and install Python from:
https://www.python.org/downloads/

During installation, check:


Add Python to PATH


---

### Step 2: Install required libraries

Open terminal inside the project folder and run:



pip install streamlit scikit-learn pandas textblob
python -m textblob.download_corpora


---

## 🧠 Train the Chatbot

Run:



python train.py


This will create:



model/chatbot_model.pkl
model/vectorizer.pkl


These files represent the chatbot’s trained brain.

---

## ▶️ Run the Chatbot

In the same folder, run:



streamlit run app.py


The chatbot will open in your browser at:



http://localhost:8501


---

## 💬 How It Works

1. User enters a message.
2. Text is converted into numerical features using TF-IDF.
3. Machine learning model predicts the intent.
4. Confidence score is calculated.
5. If confidence is low:
   - Bot asks the user to teach the correct intent.
6. Bot generates:
   - Response
   - Confidence score
   - Explanation
7. Personality adapts based on sentiment.

---

## 🧪 Example Interaction

User:


I feel sad


Bot:


💙 I'm sorry you're feeling this way.
Confidence: 0.82
Explanation: I predicted this because your message matches the 'emotion_sad' category.


---

## 🌟 Unique Features (Innovation)

- Self-reflective chatbot
- Explainable responses
- Personality evolution
- Learning from user corrections
- Adaptive dataset

---

## 🔮 Future Scope

- Voice-based interaction
- Multilingual chatbot
- Emotion trend tracking
- Image understanding
- Mobile app integration

---

## 📚 Project Concept

> Instead of building a chatbot that knows everything,  
> we built a chatbot that knows when it doesn’t know — and learns.

---

## 👨‍💻 Author

Your Name  
Course/College Name  
Year

---

## 📄 License

This project is for educational purposes.

