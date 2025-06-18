# 🧠 AI-Powered ToDo App with FastAPI & Gemini

This project is a smart ToDo application developed as part of the **Google AI Academy** program. It uses **FastAPI** as the backend framework and integrates **Gemini**, a large language model (LLM), to enhance task creation and user interaction via natural language.

---

## 🚀 Features

- ✅ Create ToDo tasks using natural language input
- 🤖 Get smart task suggestions from Gemini LLM
- 🔁 API-based architecture using FastAPI
- 📂 JSON-based data storage (or insert your method)
- 🌐 Language understanding via Gemini API

---

## 🛠️ Technologies Used

- **Python**
- **FastAPI**
- **Google Gemini (LLM)**
- Uvicorn
- Pydantic
- HTTP requests / RESTful API
- Prompt Engineering

---

## 📷 Example Usage

### Natural Language Task Input
```json
POST /create-task

{
  "prompt": "Remind me to send the report before Monday"
}
```

➡️ Gemini converts it to:

```json
{
  "task": "Send report",
  "due_date": "Next Monday"
}
```

---

🧠 How Gemini is Used

Gemini LLM is used to:

- Understand user inputs in free-form language

- Extract tasks and deadlines

- Generate helpful suggestions or auto-prioritize tasks

---

📚 Project Context
This project was built during the Google Yapay Zeka Akademisi (Google AI Academy), as a practical exercise in combining LLMs with real-world applications using FastAPI.
