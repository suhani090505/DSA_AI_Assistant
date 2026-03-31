import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse # <-- ADDED THIS
from pydantic import BaseModel
from google import genai
from google.genai import types
from dotenv import load_dotenv
import json

FILE_PATH = "chat_history.json"

def load_sessions():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except:
        return {}

def save_sessions(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

# Load existing sessions
sessions = load_sessions()

load_dotenv()

app = FastAPI()


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
for m in client.models.list():
    print(m.name)

class ChatRequest(BaseModel):
    prompt: str
    session_id:str


# --- ADD THIS NEW ROUTE ---
@app.get("/")
async def serve_frontend():
    # This tells FastAPI to return your HTML file when you visit http://127.0.0.1:8000
    return FileResponse("index.html") 
# --------------------------

@app.post("/chat")
async def chat_with_ai(request: ChatRequest):
    if request.session_id not in sessions:
        sessions[request.session_id] = []
    chat_history = sessions[request.session_id]  
    chat_history.append({
        "role": "user",
        "parts": [{"text": request.prompt}]
    }) 
    chat_history=chat_history[-6:]
    sessions[request.session_id]=chat_history
    config = types.GenerateContentConfig(
        system_instruction="""
            You are an expert Data Structures and Algorithms instructor.

            When answering:
            1. First explain the intuition
            2. Then give step-by-step approach
            3. Then provide code (Python preferred)
            4. Mention time and space complexity
            5. Suggest optimization if possible

           Rules:
           - Be clear and structured
           - Use simple language
           - Format code properly
           - If not DSA-related, respond in sarcastic or mocking way and refuse
           """
    )
    
    
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            config=config,
            contents=chat_history
        )
        chat_history.append({
            "role": "model",
            "parts": [{"text": response.text}]
        })
        save_sessions(sessions)
        if len(chat_history) > 20:
            chat_history.pop(0)
        

        return {"reply": response.text}

    except Exception as e:
        return {"reply": "Too many request, wait"}