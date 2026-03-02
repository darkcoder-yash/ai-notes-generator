import streamlit as st
st.write("NEW CLEAN BUILD V4")
import google.generativeai as genai
import os

# MUST be first Streamlit command
st.set_page_config(
    page_title="AI Notes & Quiz Generator",
    page_icon="📝"
)

# Get API key from Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API key not found. Please add GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Use stable production model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_notes(topic):
    try:
        prompt = f"""
You are an expert teacher.

Topic: {topic}

1. Give a beginner-friendly explanation.
2. Give a 3-point summary.
3. Create 5 multiple-choice questions with answers marked.
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- UI ---------------- #

st.title("📝 AI Notes & Quiz Generator")
st.write("Enter a topic to generate explanation, summary, and quiz.")

topic = st.text_input("Topic")

if st.button("Generate"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating..."):
            result = generate_notes(topic)

            if result.startswith("Error"):
                st.error(result)
            else:
                st.markdown(result)

st.divider()
st.caption("Built with ❤️ using Streamlit & Gemini")