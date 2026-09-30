import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

load_dotenv()

app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant",
    description="Lightweight AI-powered educational assistant.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextRequest(BaseModel):
    text: str


class QuestionRequest(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/qa")
async def qa(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    return {"result": answer_question(request.question)}


@app.post("/explain")
async def explain(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty.")
    return {"result": explain_topic(request.text)}


@app.post("/quiz")
async def quiz(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Passage cannot be empty.")
    return JSONResponse(content=generate_quiz(request.text))


@app.post("/summarize")
async def summarize(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    return {"result": summarize_text(request.text)}


@app.post("/learn/recommendations")
async def learning_recommendations(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty.")
    return {"result": get_learning_recommendations(request.text)}


@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
