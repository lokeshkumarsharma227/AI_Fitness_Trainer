# 🏋️‍♂️ AI Fitness Trainer Agent

An **AI-powered fitness coaching chatbot** that helps beginners create personalized **workout plans** and **nutrition guidance**.
Built with **Google Gemini**, **LangChain**, **RAG**, **FAISS**, and **Streamlit**, the agent provides context-aware recommendations from custom fitness datasets.

---

## 🚀 Features

* **Personalized Coaching** – Tailored workout and meal plans generated in real-time.
* **LLM + RAG** – Combines Google Gemini with Retrieval-Augmented Generation for accurate, context-driven responses.
* **Efficient Search** – FAISS-based vector retrieval for fast and relevant fitness information.
* **Interactive UI** – Streamlit-powered interface for a simple and intuitive user experience.
* **Modular Design** – Scalable architecture for easy updates and deployment.

---

## 🛠️ Tech Stack

* **LLM:** Google Gemini
* **Frameworks:** LangChain, Streamlit
* **Vector Search:** FAISS
* **Language:** Python

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/ai-fitness-trainer-agent.git
cd ai-fitness-trainer-agent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
# Run the Streamlit app
streamlit run app.py
```

Then open the local URL in your browser to interact with the agent.

---

## 📂 Project Structure

```
ai-fitness-trainer-agent/
│── app.py              # Streamlit interface  
│── agent/              # Core AI agent logic  
│── data/               # Fitness datasets (workout + nutrition)  
│── utils/              # Helper functions  
│── requirements.txt    # Dependencies  
│── README.md           # Project documentation  
```

---

## 🎯 Roadmap

* [ ] Add user progress tracking (weights, goals, history).
* [ ] Integrate multimodal support (image-based form checks).
* [ ] Deploy as a web app with authentication.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a PR or issue.

---
