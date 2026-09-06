from ollama import chat

response = chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "What is Python? Answer in 2 short sentences."
        }
    ]
)

print(response.message.content)