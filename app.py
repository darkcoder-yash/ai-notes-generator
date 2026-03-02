import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables (local)
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key not found. Set GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

# Initialize Gemini client (new SDK)
client = genai.Client(api_key=api_key)

def generate_content(topic):
    try:
        prompt = f"""
        Act as an expert educator.

        Topic: {topic}

        1. Give a simple beginner explanation.
        2. Give a 3-point summary.
        3. Create 5 MCQ questions with answers marked.

        Format clearly using headings.
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
st.write("Enter a topic to generate explanation, summary, and quiz.")

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
                st.markdown(result)

st.divider()
st.caption("Built with ❤️ using Streamlit & Gemini")