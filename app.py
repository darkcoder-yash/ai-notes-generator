import streamlit as st
from generator import generate_learning_material, audit_learning_material, generate_quiz_data, generate_boss_battle_data, generate_speed_round_data
import pandas as pd
import time

# --------- STATE INITIALIZATION --------- #
if "xp" not in st.session_state: st.session_state.xp = 450
if "streak" not in st.session_state: st.session_state.streak = 5
if "current_content" not in st.session_state: st.session_state.current_content = ""
if "current_topic" not in st.session_state: st.session_state.current_topic = ""
if "current_difficulty" not in st.session_state: st.session_state.current_difficulty = "Beginner"

# Game Modes State
if "quiz_active" not in st.session_state: st.session_state.quiz_active = False
if "boss_active" not in st.session_state: st.session_state.boss_active = False
if "speed_active" not in st.session_state: st.session_state.speed_active = False
if "speed_data" not in st.session_state: st.session_state.speed_data = []
if "speed_idx" not in st.session_state: st.session_state.speed_idx = 0
if "speed_score" not in st.session_state: st.session_state.speed_score = 0

def get_rank_info(xp):
    if xp <= 100: return "Rookie Explorer", "🥉"
    elif xp <= 300: return "Knowledge Warrior", "🥈"
    elif xp <= 600: return "Concept Master", "🥇"
    elif xp <= 1000: return "Master Strategist", "💎"
    else: return "Grand Scholar", "👑"

# --------- UI SETUP --------- #
st.set_page_config(page_title="AI Learning Engine", page_icon="⏳", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800&family=Inter:wght@400;500;600&display=swap');
    html, body { font-family: 'Inter', sans-serif; background-color: #F9FAFB; }
    .navbar-container {
        display: flex; justify-content: space-between; align-items: center;
        padding: 0.5rem 2rem; background: #FFFFFF; border-bottom: 1px solid #E2E8F0;
        margin-bottom: 2rem;
    }
    .logo { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.5rem; font-weight: 800; color: #1E3A8A; }
    .saas-card { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem; }
    .stat-label { color: #64748B; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; }
    .stat-value { color: #1E3A8A; font-size: 1.75rem; font-weight: 800; }
    
    /* Speed Round Styling */
    .timer-box {
        font-size: 3rem; font-weight: 800; color: #EF4444; text-align: center;
        padding: 1rem; background: #FEE2E2; border-radius: 12px; margin-bottom: 1rem;
    }
    .speed-q { font-size: 1.5rem; font-weight: 700; color: #1E3A8A; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

# --------- TOP BAR --------- #
rank_name, rank_icon = get_rank_info(st.session_state.xp)
st.markdown(f'''
<div class="navbar-container">
    <div class="logo">💎 AI Learning Engine</div>
    <div style="text-align: right">
        <span style="font-weight: 700; color: #1E3A8A;">⚡ {st.session_state.xp} XP</span>
        <span style="margin: 0 10px; color: #E2E8F0;">|</span>
        <span style="font-weight: 600; color: #4B5563;">{rank_icon} {rank_name}</span>
        <span style="margin: 0 10px; color: #E2E8F0;">|</span>
        <span style="font-weight: 700; color: #EF4444;">🔥 {st.session_state.streak}</span>
    </div>
</div>
''', unsafe_allow_html=True)

# --------- SIDEBAR --------- #
with st.sidebar:
    st.markdown("### 🗺️ Workspace")
    menu = st.radio("Navigation", ["📊 Dashboard", "📝 Generate Notes", "🎮 Quiz Mode", "⚔️ Boss Battle", "⏳ Speed Round", "🔍 AI Audit"], label_visibility="collapsed")
    st.divider()
    st.caption("v6.0 Speed Round Enabled")

# --------- CONTENT AREA --------- #

if menu == "📊 Dashboard":
    st.markdown("### Welcome Back, Scholar!")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown(f'<div class="saas-card"><div class="stat-label">Total XP</div><div class="stat-value">{st.session_state.xp}</div></div>', unsafe_allow_html=True)
    with col2: st.markdown(f'<div class="saas-card"><div class="stat-label">Current Rank</div><div class="stat-value">{rank_name.split(" ")[0]}</div></div>', unsafe_allow_html=True)
    with col3: st.markdown(f'<div class="saas-card"><div class="stat-label">Daily Streak</div><div class="stat-value">{st.session_state.streak}</div></div>', unsafe_allow_html=True)
    with col4: st.markdown(f'<div class="saas-card"><div class="stat-label">Accuracy</div><div class="stat-value">84%</div></div>', unsafe_allow_html=True)

elif menu == "📝 Generate Notes":
    t = st.text_input("Topic", placeholder="e.g. History of Rome")
    if st.button("🚀 Launch Mission"):
        if t:
            with st.spinner("Generating..."):
                st.session_state.current_content = generate_learning_material(t, "Intermediate")
                st.session_state.current_topic = t
                st.markdown(st.session_state.current_content)

elif menu == "⏳ Speed Round":
    st.markdown("### ⏳ Rapid-Fire Speed Round")
    
    if not st.session_state.speed_active:
        st.info("⏱️ You have 60 seconds to answer 10 questions. Speed is key!")
        target = st.session_state.current_topic or st.text_input("Speed Round Topic", "General Knowledge")
        if st.button("🏁 START SPEED ROUND", use_container_width=True):
            with st.spinner("Loading rapid-fire deck..."):
                data = generate_speed_round_data(target, "Intermediate")
                if isinstance(data, list):
                    st.session_state.speed_data = data
                    st.session_state.speed_active = True
                    st.session_state.speed_idx = 0
                    st.session_state.speed_score = 0
                    st.rerun()
    else:
        # SPEED ROUND UI
        idx = st.session_state.speed_idx
        data = st.session_state.speed_data
        
        if idx < len(data):
            st.markdown(f'<div class="timer-box">QUESTION {idx + 1}/10</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="speed-q">{data[idx]["question"]}</div>', unsafe_allow_html=True)
            
            user_ans = st.text_input("Type your answer...", key=f"speed_ans_{idx}")
            
            if st.button("NEXT ➡️", use_container_width=True):
                if user_ans.strip().lower() == data[idx]["answer"].lower():
                    st.session_state.speed_score += 1
                    st.session_state.xp += data[idx]["xp"]
                    st.toast("✅ Correct! +5 XP")
                else:
                    st.toast(f"❌ Wrong! Correct: {data[idx]['answer']}")
                
                st.session_state.speed_idx += 1
                st.rerun()
        else:
            st.balloons()
            st.success(f"Speed Round Complete! Score: {st.session_state.speed_score}/10")
            st.session_state.speed_active = False
            if st.button("Return to Dashboard"): st.rerun()

elif menu == "⚔️ Boss Battle":
    st.write("Boss Battle mode is ready.")

elif menu == "🎮 Quiz Mode":
    st.write("Quiz Mode is ready.")

elif menu == "🔍 AI Audit":
    st.write("Audit mode is ready.")
