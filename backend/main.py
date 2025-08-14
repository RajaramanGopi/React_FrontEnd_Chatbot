from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Set this in your Codespace env

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    if not user_message.strip():
        return {"response": "Please enter a message."}

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://github.com/<your-github-username>/<your-repo>",  # Optional, for OpenRouter analytics
        "X-Title": "Krishna Chatbot"
    }
    payload = {
        "model": "mistralai/mistral-7b-instruct",  # Free and fast, or try "meta-llama/llama-3-8b-instruct"
        "messages": [
            {"role": "system", "content": "You are Krishna, a helpful AI assistant."},
            {"role": "user", "content": user_message}
        ]
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
            ai_response = result["choices"][0]["message"]["content"]
            return {"response": ai_response}
        except Exception as e:
            return {"response": f"Error: {str(e)}"}