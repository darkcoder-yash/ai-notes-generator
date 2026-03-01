# AI Notes & Quiz Generator 🚀

A Streamlit-based web application that uses Google's Gemini AI to generate simple explanations, summaries, and quizzes for any topic.

## 🛠️ Setup Instructions

1. **Clone the repository** (or create a new folder and copy the files).
2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Get a Gemini API Key**:
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Create a new API key.
5. **Configure Environment Variables**:
   - Open the `.env` file.
   - Replace `your_gemini_api_key_here` with your actual API key.
6. **Run the App**:
   ```bash
   streamlit run app.py
   ```

## 📤 How to Push to GitHub

1. Create a new repository on GitHub.
2. Initialize git locally:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Link to GitHub and push:
   ```bash
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

## 🌐 How to Deploy on Streamlit Cloud

1. Push your code to a public GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Connect your GitHub account.
4. Select your repository and `app.py` as the main file.
5. **Crucial**: Go to **Advanced Settings** -> **Secrets** and add your API key:
   ```toml
   GOOGLE_API_KEY = "your_actual_api_key"
   ```

## 🚀 How to Upgrade Later

- **Chat History**: Use `st.session_state` to store and display previous messages.
- **PDF Upload**: Add `st.file_uploader` and use a library like `PyPDF2` to extract text for the AI to analyze.
- **Login System**: Use `streamlit-authenticator` for simple user authentication.
- **Database**: Integrate `Supabase` or `Firebase` to save user-generated notes and quiz scores.
