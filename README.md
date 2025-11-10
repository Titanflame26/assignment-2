A lightweight REST API built with FastAPI and LangChain, powered by OpenAI’s GPT models.
It provides AI-driven chat and summarization endpoints, complete with health checks and modular prompt templates.
---
```## 📁 Project Structure
fastapi-langchain-chatbot/
│
├── main.py
├── requirements.txt
├── .env
└── README.md
---
---

## ⚙️ Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

##Create and Activate a Virtual Environment

python -m venv venv
venv\Scripts\activate   
# or
source venv/bin/activate

pip install -r requirements.txt

4️)Configure Environment Variables

Create a .env file in the root directory and add your OpenAI API key:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Run the Server

uvicorn main:app --reload

```
🧠 API Endpoints

Endpoint: GET /health

curl -X GET http://127.0.0.1:8000/health

{
  "status": "ok",
  "message": "LangChain Chatbot API is healthy!"
}

Endpoint: POST /chat

curl -X POST http://127.0.0.1:8000/chat ^
-H "Content-Type: application/json" ^
-d "{\"message\": \"What is LangChain used for?\"}"

{
  "response": "LangChain is a framework for building applications powered by large language models."
}


Endpoint: POST /summarize

curl -X POST http://127.0.0.1:8000/summarize ^
-H "Content-Type: application/json" ^
-d "{\"text\": \"LangChain helps developers build applications that combine large language models with data sources and tools.\"}"

{
  "summary": "LangChain enables developers to integrate LLMs with external data and tools for smarter applications."
}







