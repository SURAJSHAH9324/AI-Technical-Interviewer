from fastapi import APIRouter
from ollama import chat
from app.schemas.chat import ChatRequest

router = APIRouter()

conversation = [
    {
        "role": "system",
        "content": "You are an AI technical interviewer. Ask clear technical questions and evaluate the candidate's answers."
    }
]


@router.post("/chat")
def chat_with_ai(request: ChatRequest):
    conversation.append(
        {
            "role": "user",
            "content": request.question,
        }
    )

    response = chat(
        model="qwen3:8b",
        messages=conversation,
    )
    conversation.append(
        {
            "role": "assistant",
            "content": response.message.content,
        }
    )

    return {"response": response.message.content}
