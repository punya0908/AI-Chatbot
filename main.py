from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInfo(BaseModel):
    age: int
    weight: float
    height: float
    gender: str

class CustomPrompt(BaseModel):
    prompt: str

@app.post("/get_plan")
async def get_nutrition_plan(data: UserInfo):
    prompt = (
        f"Create a detailed, healthy nutrition plan for a {data.gender}, "
        f"{data.age} years old, weighing {data.weight} kg, and {data.height} cm tall. "
        "Include meals for breakfast, lunch, dinner, and snacks with calories and nutrition tips."
    )
    response = model.generate_content(prompt)
    return {"plan": response.text}

@app.post("/custom_prompt")
async def custom_prompt(prompt: CustomPrompt):
    response = model.generate_content(prompt.prompt)
    return {"plan": response.text}
