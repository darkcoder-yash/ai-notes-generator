import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION ---
def get_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    
    genai.configure(api_key=api_key)
    # Using the 2026 stable flagship model
    model_name = "gemini-2.5-flash"
    return genai.GenerativeModel(model_name)

def generate_learning_material(topic: str, difficulty: str = "Beginner") -> str:
    """
    Generates a fully gamified educational experience using the Gemini 2.5 Flash model.
    """
    model = get_model()
    
    prompt = f"""
You are an AI Learning Game Engine.

Create a fully gamified educational experience.

Topic: {topic}
Difficulty: {difficulty}

Follow this structure EXACTLY:

==================================================
🎯 MISSION INTRO
==================================================
Present the topic as a game mission.
Make it exciting and story-driven.

==================================================
🧠 KNOWLEDGE CORE
==================================================
Provide a concise explanation required to complete the mission.

==================================================
⚔️ LEVEL 1 QUIZ (Easy)
==================================================
Create 3 MCQs.
Each question must have 4 options (A–D).

==================================================
🔥 LEVEL 2 QUIZ (Applied)
==================================================
Create 2 scenario-based MCQs.

==================================================
🏆 BOSS BATTLE (Hard)
==================================================
Create 1 advanced analytical or conceptual question.

==================================================
⏳ SPEED ROUND (Timed Challenge)
==================================================
Create 3 rapid-fire short-answer questions.
Keep them short and fact-based.

==================================================
🎁 XP SYSTEM
==================================================
Assign XP values:

Level 1 MCQ = 10 XP each
Level 2 MCQ = 15 XP each
Boss Battle = 30 XP
Speed Round = 5 XP each
Perfect Streak Bonus (all correct in a section) = +10 XP

==================================================
🏅 RANK SYSTEM
==================================================
Define rank titles based on total XP:

0–30 XP → Rookie Explorer
31–60 XP → Knowledge Adventurer
61–100 XP → Concept Warrior
101–150 XP → Master Strategist
151+ XP → Grand Scholar

==================================================
📈 ADAPTIVE DIFFICULTY LOGIC
==================================================
Explain how difficulty should adjust:

If user scores below 40% → suggest easier follow-up topic.
If user scores 40–70% → keep same level.
If user scores above 70% → increase difficulty next round.

==================================================
🏆 LEADERBOARD LOGIC
==================================================
Explain how to track:
- Username
- Total XP
- Highest Rank
- Fastest Speed Round time
- Current streak

Provide leaderboard display format.

==================================================
🔓 UNLOCK SYSTEM
==================================================
Suggest 3 next topics:
- Easier
- Same Level
- Harder

==================================================
📋 ANSWER KEY
==================================================
Provide correct answers clearly at the end.
Do NOT reveal answers inside questions.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def audit_learning_material(topic: str, difficulty: str, content: str) -> str:
    """
    Performs a full system review and quality audit of the generated learning material.
    """
    model = get_model()
    
    prompt = f"""
You are an AI System Auditor, Debugging Engineer, and Educational Quality Analyst.

Your task is to rigorously test, evaluate, debug, and rate the AI Learning Engine.

Topic Used: {topic}
Difficulty Selected: {difficulty}

Analyze the AI response output and perform a FULL SYSTEM REVIEW.

AI RESPONSE OUTPUT TO AUDIT:
---
{content}
---

Follow this structure EXACTLY and perform a FULL SYSTEM REVIEW:

==================================================
1️⃣ STRUCTURE VALIDATION
==================================================
- Check if all required sections are present.
- Detect formatting inconsistencies.
- Verify answer key alignment.
- Ensure no answers are revealed inside questions.
- Confirm XP rules are correctly applied.

Report:
- Missing Sections
- Structural Errors
- Formatting Issues

==================================================
2️⃣ CONTENT ACCURACY CHECK
==================================================
- Evaluate conceptual correctness.
- Detect hallucinated facts.
- Identify vague or ambiguous explanations.
- Check logical consistency in answers.

Rate accuracy from 1–10.
Explain reasoning.

==================================================
3️⃣ DIFFICULTY VALIDATION
==================================================
- Does content match selected difficulty?
- Are Level 1 questions basic?
- Are Level 2 questions applied?
- Is Boss Battle truly advanced?

Rate difficulty alignment from 1–10.

==================================================
4️⃣ PEDAGOGICAL QUALITY ANALYSIS
==================================================
Evaluate:
- Clarity of explanation
- Learning progression
- Cognitive depth
- Bloom’s taxonomy alignment
- Engagement factor

Score each from 1–10.

==================================================
5️⃣ GAMIFICATION LOGIC TEST
==================================================
- Are XP values logical?
- Is reward progression balanced?
- Is rank scaling reasonable?
- Is adaptive difficulty logic sound?

Identify balancing flaws.

==================================================
6️⃣ STRESS TEST SIMULATION
==================================================
Simulate:
- 0% score scenario
- 50% score scenario
- 100% score scenario

For each scenario:
- Calculate XP
- Assign rank
- Determine next difficulty
- Identify improvement suggestion

==================================================
7️⃣ EDGE CASE TESTING
==================================================
Test:
- Very simple topic (e.g., “Water”)
- Very advanced topic (e.g., “Quantum Entanglement”)
- Very vague topic (e.g., “Technology”)

Explain how system would behave.

==================================================
8️⃣ RESPONSE CLARITY CLEANUP
==================================================
Rewrite any:
- Redundant sections
- Overly verbose content
- Unclear questions
- Ambiguous phrasing

Make improved version cleaner and more professional.

==================================================
9️⃣ PERFORMANCE RATING DASHBOARD
==================================================
Generate an analytics summary:

Overall Quality Score (1–100)
Accuracy Score
Difficulty Match Score
Engagement Score
Structure Integrity Score
Gamification Balance Score

Provide final grade:
A+ / A / B / C / Needs Improvement

==================================================
🔟 FINAL VERDICT
==================================================
- Is this AI production-ready?
- What are the top 5 improvements needed?
- What risks remain?
- What next evolution stage is recommended?

Be strict.
Be analytical.
Be detailed.
Do not be overly generous in scoring.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during Audit: {str(e)}"
