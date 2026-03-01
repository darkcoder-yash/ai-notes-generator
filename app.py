import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API Key not found. Please set GOOGLE_API_KEY in your .env file or Streamlit Secrets.")

def generate_content(topic):
    """Generates explanation, summary, and quiz using Gemini AI."""
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Act as an expert educator. For the topic: "{topic}"
    
    1. Provide a clear and simple explanation suitable for a beginner.
    2. Provide a 3-bullet point summary of the key takeaways.
    3. Generate 5 multiple-choice quiz questions with 4 options each. 
       Clearly mark the correct answer for each.
    
    Format the output strictly as follows:
    ---EXPLANATION---
    (Explanation text)
    ---SUMMARY---
    (Summary bullet points)
    ---QUIZ---
    (Quiz questions and answers)
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# --- UI Setup ---
st.set_page_config(page_title="AI Notes & Quiz Generator", page_icon="📝", layout="centered")

st.title("📝 AI Notes & Quiz Generator")
st.markdown("Enter a topic below to get a simplified explanation, a summary, and a practice quiz!")

topic = st.text_input("What topic do you want to learn about?", placeholder="e.g., Quantum Physics, Photosynthesis, Python Loops")

if st.button("Generate Learning Material"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    elif not api_key:
        st.error("API Key is missing. Check your configuration.")
    else:
        with st.spinner(f"Generating notes and quiz for '{topic}'..."):
            result = generate_content(topic)
            
            if "Error:" in result:
                st.error(result)
            else:
                # Splitting the content based on markers
                parts = result.split("---")
                
                explanation = ""
                summary = ""
                quiz = ""
                
                for part in parts:
                    if "EXPLANATION" in part:
                        explanation = part.replace("EXPLANATION", "").strip()
                    elif "SUMMARY" in part:
                        summary = part.replace("SUMMARY", "").strip()
                    elif "QUIZ" in part:
                        quiz = part.replace("QUIZ", "").strip()
                
                # Displaying results in tabs
                tab1, tab2, tab3 = st.tabs(["📖 Explanation", "📋 Summary", "🧠 Quiz"])
                
                with tab1:
                    st.header("Explanation")
                    st.write(explanation)
                
                with tab2:
                    st.header("Key Summary")
                    st.write(summary)
                
                with tab3:
                    st.header("Test Your Knowledge")
                    st.write(quiz)

st.divider()
st.caption("Built with ❤️ using Streamlit and Google Gemini AI")
