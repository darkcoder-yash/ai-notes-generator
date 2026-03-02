import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key not found. Set GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

client = genai.Client(api_key=api_key)

def generate_content(topic):
    try:
        prompt = f"""
        Act as an expert educator. For the topic: "{topic}"

        1. Provide a clear beginner-friendly explanation.
        2. Provide a 3-bullet point summary.
        3. Generate 5 MCQs with answers clearly marked.

        Format:
        ---EXPLANATION---
        ---SUMMARY---
        ---QUIZ---
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


st.set_page_config(page_title="AI Notes & Quiz Generator", page_icon="📝")

st.title("📝 AI Notes & Quiz Generator")
st.write("Enter a topic to get explanation, summary, and quiz.")

topic = st.text_input("Topic")

if st.button("Generate Learning Material"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating..."):
            result = generate_content(topic)

            if result.startswith("Error"):
                st.error(result)
            else:
                st.write(result)

st.divider()
st.caption("Built with ❤️ using Streamlit and Gemini")