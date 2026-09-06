#from ollama import chat
# response = chat(
#     model="qwen3:8b",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is Python? Answer in 2 short sentences."
#         }
#     ]
# )

# print(response.message.content)

from fastapi import FastAPI
from app.routes.home import router as home_router
from app.routes.health import router as health_router
app = FastAPI(title="AI Technical Interviewer")

app.include_router(home_router)
app.include_router(health_router)