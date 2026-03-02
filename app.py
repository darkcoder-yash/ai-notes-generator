import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# MUST be the first Streamlit command
st.set_page_config(
    page_title="AI Notes & Quiz Generator",
    page_icon="📝",
    layout="centered"
)

# Load environment variables (for local use)
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key not found. Please set GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

# Initialize Gemini client (new SDK)
client = genai.Client(api_key=api_key)


def generate_content(topic):
    try:
        prompt = f"""
        Act as an expert educator.

        Topic: {topic}

        1. Provide a clear and beginner-friendly explanation.
        2. Provide a 3-point summary.
        3. Create 5 multiple-choice questions with answers clearly marked.
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        # Safe response handling
        if hasattr(response, "text") and response.text:
            return response.text
        else:
            return "Error: No text returned from Gemini."

    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- UI ---------------- #

st.title("📝 AI Notes & Quiz Generator")
st.write("Enter a topic to generate explanation, summary, and quiz.")

topic = st.text_input("Topic")

if st.button("Generate Learning Material"):
    if not topic.strip():
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