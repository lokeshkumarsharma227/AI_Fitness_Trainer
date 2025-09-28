# 🏋️‍♂️ AI Fitness Trainer Agent

An **AI-powered fitness coaching agent** that helps beginners create **personalized workout and nutrition plans**.
Built with **Google Gemini**, **LangChain**, **RAG**, **FAISS**, and **Streamlit**, the agent delivers **context-aware recommendations** from custom fitness datasets.

---

## 🚀 Features

* **Personalized Coaching** – Workout and nutrition plans generated in real-time.
* **LLM + RAG** – Combines Google Gemini with Retrieval-Augmented Generation for accurate, context-driven responses.
* **Vector Search** – FAISS-based vector store for efficient retrieval.
* **Interactive UI** – Streamlit interface for easy interaction.
* **Scalable Design** – Modular Python architecture for extensibility.

---

## 🛠️ Tech Stack

* **LLM:** Google Gemini
* **Frameworks:** LangChain, Streamlit
* **Vector Store:** FAISS
* **Language:** Python

---

## 📂 Project Structure

```
ai-fitness-trainer-agent/
│── archive_env/        # Archived environment or configs  
│── data/               # Fitness datasets (workout + nutrition)  
│── vectorstore/        # FAISS vector database files  
│── ingest.py           # Script to build/update vector store  
│── embeddings.py       # Embedding generation functions  
│── gemini_llm.py       # Google Gemini LLM integration  
│── rag_chain.py        # RAG pipeline logic (retrieval + generation)  
│── app.py              # Streamlit UI for chatbot interaction  
│── requirements.txt    # Dependencies  
│── .gitignore          # Git ignore rules  
│── README.md           # Project documentation  
│── .DS_Store           # System file (can be ignored)  
```

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/ai-fitness-trainer-agent.git
cd ai-fitness-trainer-agent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
# Run the Streamlit app
streamlit run app.py
```

Open the URL from the terminal (usually `http://localhost:8501`) to start chatting with the fitness agent.

---

## 🎯 Roadmap

* [ ] Add progress tracking (weight, goals, workout history).
* [ ] Support multimodal input (e.g., check exercise form from images/videos).
* [ ] Deploy on cloud with authentication and persistent storage.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Open a PR or create an issue to get started.

---
