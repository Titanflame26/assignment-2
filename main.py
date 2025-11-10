from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

app=FastAPI(title="LangChain OpenAI Chat API")

llm=ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-4o-mini")

class ChatRequest(BaseModel):
    message: str

class SummarizeRequest(BaseModel):
    text: str


chat_prompt = ChatPromptTemplate.from_template(
    "You are a friendly assistant. Answer the following user query clearly:\nUser: {message}\nAssistant:"
)

summary_prompt = ChatPromptTemplate.from_template(
    "Summarize the following text in 3 concise sentences:\n\n{text}"
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "LangChain Chatbot API is healthy!"}



@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    """Chat with the AI assistant."""
    try:
        formatted_prompt = chat_prompt.format_messages(message=req.message)
        response = llm.invoke(formatted_prompt)
        return {"response": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/summarize")
async def summarize_endpoint(req: SummarizeRequest):
    """Summarize input text."""
    try:
        if len(req.text.strip()) < 10:
            raise HTTPException(status_code=400, detail="Input text too short to summarize.")
        formatted_prompt = summary_prompt.format_messages(text=req.text)
        response = llm.invoke(formatted_prompt)
        return {"summary": response.content}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
