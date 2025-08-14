from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    # Simple logic: echo or basic response
    if not user_message.strip():
        return {"response": "Please enter a message."}
    if "hello" in user_message.lower():
        return {"response": "Hello! How can I assist you today?"}
    if "name" in user_message.lower():
        return {"response": "I am Krishna, your AI assistant."}
    # Default echo
    return {"response": f"You said: {user_message}"}