import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables (for local development)
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key not found. Please set GEMINI_API_KEY in Streamlit Secrets or .env file.")
    st.stop()

genai.configure(api_key=api_key)

def generate_content(topic):
    """Generates explanation, summary, and quiz using Gemini AI."""
    
    try:
        # Use supported model for google.generativeai SDK
        model = genai.GenerativeModel("gemini-pro")

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

        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text
        else:
            return "Error: No response generated from the model."

    except Exception as e:
        return f"Error: {str(e)}"


# --- UI Setup ---
st.set_page_config(
    page_title="AI Notes & Quiz Generator",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI Notes & Quiz Generator")
st.markdown("Enter a topic below to get a simplified explanation, a summary, and a practice quiz!")

topic = st.text_input(
    "What topic do you want to learn about?",
    placeholder="e.g., Quantum Physics, Photosynthesis, Python Loops"
)

if st.button("Generate Learning Material"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner(f"Generating notes and quiz for '{topic}'..."):
            result = generate_content(topic)

            if result.startswith("Error:"):
                st.error(result)
            else:
                parts = result.split("---")

                explanation = ""
                summary = ""
                quiz = ""

                for part in parts:
                    part = part.strip()
                    if part.startswith("EXPLANATION"):
                        explanation = part.replace("EXPLANATION", "").strip()
                    elif part.startswith("SUMMARY"):
                        summary = part.replace("SUMMARY", "").strip()
                    elif part.startswith("QUIZ"):
                        quiz = part.replace("QUIZ", "").strip()

                tab1, tab2, tab3 = st.tabs(["📖 Explanation", "📋 Summary", "🧠 Quiz"])

                with tab1:
                    st.subheader("Explanation")
                    st.write(explanation)

                with tab2:
                    st.subheader("Key Summary")
                    st.write(summary)

                with tab3:
                    st.subheader("Test Your Knowledge")
                    st.write(quiz)

st.divider()
st.caption("Built with ❤️ using Streamlit and Google Gemini AI")