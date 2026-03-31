# 🚀 DSA AI Assistant

An intelligent chatbot that helps solve **Data Structures and Algorithms (DSA)** problems with structured explanations, code, and complexity analysis.

---

## 🔥 Features

* 💬 Chat-based UI (like ChatGPT)
* 🧠 Context-aware conversations (session-based memory)
* 📊 Structured solutions:

  * Intuition
  * Approach
  * Code
  * Complexity
* 💻 Clean Python code generation
* 🔄 Multi-user session support
* 💾 Persistent chat history (saved in JSON)
* ⚡ FastAPI backend + Gemini API

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **LLM:** Google Gemini API (`google-genai`)
* **Storage:** JSON (for chat history)

---

## 📂 Project Structure

```bash
dsa-ai-assistant/
│
├── app.py
├── index.html
├── chat_history.json
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/dsa-ai-assistant.git
cd dsa-ai-assistant
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Add API key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the server

```bash
uvicorn app:app --reload
```

---

### 5️⃣ Open in browser

```text
http://127.0.0.1:8000
```

---

## 💡 Example Questions

* What is an array?
* Solve Two Sum problem
* Explain BFS vs DFS
* Optimize this dynamic programming solution
* Reverse a linked list

---

## 🧠 How It Works

1. User sends a message from frontend
2. FastAPI backend receives request
3. Session-based memory maintains chat history
4. Gemini API generates structured response
5. Response is sent back and displayed

---

## ⚠️ Limitations

* Free API has rate limits (429 errors possible)
* Chat history stored locally (JSON, not database)
* Requires internet connection for API calls

---
