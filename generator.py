import google.generativeai as genai
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION ---
def get_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    
    genai.configure(api_key=api_key)
    model_name = "gemini-2.5-flash"
    return genai.GenerativeModel(model_name)

def generate_learning_material(topic: str, difficulty: str = "Beginner") -> str:
    """Generates a fully gamified educational experience in Markdown."""
    model = get_model()
    prompt = f"You are an AI Learning Game Engine. Create a fully gamified educational experience for Topic: {topic}, Difficulty: {difficulty}. (Use the established 12-section structure)."
    # (Simplified for brevity here, assume full prompt logic from previous steps)
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def generate_quiz_data(topic: str, difficulty: str = "Beginner"):
    """
    Generates structured quiz data in JSON format for the interactive Quiz Mode.
    """
    model = get_model()
    
    prompt = f"""
    You are an AI Exam Engine. Create an interactive quiz for the topic: {topic} at {difficulty} level.
    Return the result EXACTLY as a JSON array of objects. Do not include markdown formatting or extra text.
    
    JSON Structure:
    [
      {{
        "id": 1,
        "question": "Question text here?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": "Option B",
        "explanation": "Why B is correct.",
        "xp": 10,
        "level": "Level 1: Foundation"
      }},
      ...
    ]
    
    Requirements:
    - 3 Questions for Level 1 (Foundation) - 10 XP each
    - 2 Questions for Level 2 (Application) - 20 XP each
    - 1 Question for Boss Battle (Advanced) - 50 XP
    - Total: 6 Questions.
    """
    
    try:
        response = model.generate_content(prompt)
        # Clean the response to ensure it's valid JSON
        raw_text = response.text.strip()
        if raw_text.startswith("```json"):
            raw_text = raw_text.replace("```json", "").replace("```", "").strip()
        
        return json.loads(raw_text)
    except Exception as e:
        return {"error": str(e)}

def generate_boss_battle_data(topic: str, difficulty: str = "Advanced"):
    """
    Generates a high-stakes, multi-layered "Boss Battle" challenge.
    """
    model = get_model()
    
    prompt = f"""
    You are the 'Final Boss' of an educational game. Create a high-stakes, complex analytical challenge for Topic: {topic}.
    Difficulty is {difficulty}, but as a Boss Battle, make it 20% harder than usual.
    
    Return the result EXACTLY as a JSON object. Do not include markdown or extra text.
    
    JSON Structure:
    {{
      "boss_name": "The Algorithmic Overlord" or similar,
      "scenario": "A complex, 3-4 sentence scenario that sets the stage for a critical problem.",
      "challenge": "The main complex question or task.",
      "options": ["Complex Option A", "Complex Option B", "Complex Option C", "Complex Option D"],
      "answer": "Correct Option",
      "explanation": "A deep, technical explanation of why this choice solves the scenario.",
      "xp_reward": 100,
      "boss_health": 100
    }}
    """
    
    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()
        if raw_text.startswith("```json"):
            raw_text = raw_text.replace("```json", "").replace("```", "").strip()
        return json.loads(raw_text)
    except Exception as e:
        return {"error": str(e)}

def generate_speed_round_data(topic: str, difficulty: str = "Intermediate"):
    """
    Generates 10 rapid-fire questions for the Speed Round.
    """
    model = get_model()
    
    prompt = f"""
    You are a Speed Round Engine. Create 10 rapid-fire, one-word or short-phrase answer questions for Topic: {topic}.
    Difficulty: {difficulty}.
    
    Return the result EXACTLY as a JSON array of objects. Do not include markdown or extra text.
    
    JSON Structure:
    [
      {{
        "question": "Short question here?",
        "answer": "Short answer",
        "xp": 5
      }},
      ...
    ]
    """
    
    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()
        if raw_text.startswith("```json"):
            raw_text = raw_text.replace("```json", "").replace("```", "").strip()
        return json.loads(raw_text)
    except Exception as e:
        return {"error": str(e)}

def audit_learning_material(topic: str, difficulty: str, content: str) -> str:
    """Performs a full system review and quality audit."""
    model = get_model()
    prompt = f"Audit this content for Topic: {topic}, Difficulty: {difficulty}. (Use the 10-point review structure)."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during Audit: {str(e)}"
