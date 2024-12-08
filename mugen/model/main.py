from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from agent import agent_executor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI()

# Request and response models
class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to Michibiku: Your Japan Guide!"}

@app.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon available."}

@app.post("/ask-japan", response_model=AnswerResponse)
async def ask_japan(question_request: QuestionRequest):
    try:
        response = agent_executor.invoke({"input": question_request.question})
        return AnswerResponse(answer=response["output"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
