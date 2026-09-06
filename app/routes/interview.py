from fastapi import APIRouter
from ollama import chat
from app.schemas.interview import InterviewRequest, InterviewQuestion

router = APIRouter()

@router.post("/interview/question")
def generate_questions(request:InterviewRequest):
     prompt = f"""
You are a technical interviewer.

Generate ONE interview question for:

Role: {request.role}
Experience: {request.experience} years
Difficulty: {request.difficulty}
Total interview questions: {request.number_of_questions}

Return ONLY valid JSON in this format:

{{
    "role": "...",
    "question": "...",
    "topic": "...",
    "difficulty": "..."
}}
"""
     response = chat(
          model ="qwen3:8b",
          messages = [
               {
                    "role":"user",
                    "content": prompt
               }
          ],
          format="json",
           options = {
               "num_predict":100
           }
     )
     return response.message.content
