from pydantic import BaseModel
class InterviewQuestion(BaseModel):
    role:str
    question:str
    topic:str
    difficulty:str
class InterviewRequest(BaseModel):
    role: str
    experience: int
    difficulty: str
    number_of_questions: int