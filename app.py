import streamlit as st
from generator import generate_learning_material, audit_learning_material
import pandas as pd

# --------- STATE INITIALIZATION --------- #
if "xp" not in st.session_state: st.session_state.xp = 450
if "streak" not in st.session_state: st.session_state.streak = 5
if "current_content" not in st.session_state: st.session_state.current_content = ""
if "current_topic" not in st.session_state: st.session_state.current_topic = ""
if "current_difficulty" not in st.session_state: st.session_state.current_difficulty = ""

def get_rank_info(xp):
    if xp <= 100: return "Rookie Explorer", "🥉"
    elif xp <= 300: return "Knowledge Warrior", "🥈"
    elif xp <= 600: return "Concept Master", "🥇"
    elif xp <= 1000: return "Master Strategist", "💎"
    else: return "Grand Scholar", "👑"

# --------- UI SETUP --------- #
st.set_page_config(page_title="AI Learning Engine", page_icon="💎", layout="wide")

# Production-Grade SaaS Styling
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&family=Inter:wght@400;500;600&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        background-color: #F9FAFB;
    }}
    
    /* Navbar Styles */
    .stAppHeader {{
        background: #FFFFFF !important;
        border-bottom: 1px solid #E5E7EB !important;
    }}
    
    .navbar-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5rem 2rem;
        background: #FFFFFF;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 2rem;
    }}
    .logo {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.5rem;
        font-weight: 800;
        color: #1E3A8A;
        letter-spacing: -0.5px;
    }}
    
    /* Card Styles */
    .saas-card {{
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .stat-label {{
        color: #64748B;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .stat-value {{
        color: #1E3A8A;
        font-size: 1.75rem;
        font-weight: 800;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    
    /* Button Styles */
    .stButton>button {{
        background: #1E3A8A !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.2s ease !important;
    }}
    .stButton>button:hover {{
        background: #1e40af !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }}
    
    /* Sidebar Overrides */
    [data-testid="stSidebar"] {{
        background-color: #0F172A !important;
    }}
    [data-testid="stSidebar"] * {{
        color: #F8FAFC !important;
    }}
    .sidebar-active {{
        background: rgba(30, 58, 138, 0.2);
        border-left: 4px solid #06B6D4;
    }}
</style>
""", unsafe_allow_html=True)

# --------- TOP BAR --------- #
rank_name, rank_icon = get_rank_info(st.session_state.xp)
st.markdown(f'''
<div class="navbar-container">
    <div class="logo">💎 AI Learning Engine</div>
    <div style="display: flex; gap: 1rem; align-items: center;">
        <div style="text-align: right">
            <span style="font-weight: 700; color: #1E3A8A;">⚡ {st.session_state.xp} XP</span>
            <span style="margin: 0 10px; color: #E2E8F0;">|</span>
            <span style="font-weight: 600; color: #4B5563;">{rank_icon} {rank_name}</span>
            <span style="margin: 0 10px; color: #E2E8F0;">|</span>
            <span style="font-weight: 700; color: #EF4444;">🔥 {st.session_state.streak}</span>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# --------- SIDEBAR --------- #
with st.sidebar:
    st.markdown("### 🗺️ Workspace")
    menu = st.radio("Navigation", [
        "📊 Dashboard", 
        "📝 Generate Notes", 
        "🎮 Quiz Mode", 
        "⚔️ Boss Battle", 
        "⏳ Speed Round",
        "🔍 AI Audit",
        "📈 Analytics",
        "🏆 Leaderboard"
    ], label_visibility="collapsed")
    st.divider()
    st.caption("v4.0 Production Redesign")

# --------- CONTENT AREA --------- #

if menu == "📊 Dashboard":
    st.markdown("### Welcome Back, Scholar!")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="saas-card"><div class="stat-label">Total Progress</div><div class="stat-value">{st.session_state.xp} XP</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="saas-card"><div class="stat-label">Current Rank</div><div class="stat-value">{rank_icon} {rank_name.split(" ")[0]}</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="saas-card"><div class="stat-label">Daily Streak</div><div class="stat-value">{st.session_state.streak} Days</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="saas-card"><div class="stat-label">Accuracy</div><div class="stat-value">84%</div></div>', unsafe_allow_html=True)
    
    st.markdown("#### Recommended for You")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**Mission:** Unlock 'Binary Search Trees' at Advanced level.")
    with c2:
        st.success("**Daily Challenge:** Complete a Speed Round for +20 XP.")

elif menu == "📝 Generate Notes":
    st.markdown("### 📝 Smart Notes Generator")
    with st.container(border=True):
        t = st.text_input("What would you like to master today?", placeholder="e.g. Deep Learning Transformers")
        d = st.select_slider("Select Cognitive Depth", options=["Beginner", "Intermediate", "Advanced"])
        if st.button("🚀 Launch AI Mission", use_container_width=True):
            if t:
                with st.spinner("Assembling production-grade learning module..."):
                    content = generate_learning_material(t, d)
                    st.session_state.current_content = content
                    st.session_state.current_topic = t
                    st.session_state.current_difficulty = d
                    st.divider()
                    st.markdown(content)
            else:
                st.warning("Please enter a target topic.")

elif menu == "🔍 AI Audit":
    st.markdown("### 🔍 Enterprise Quality Audit")
    if not st.session_state.current_content:
        st.warning("Generate a learning module first to run a system audit.")
    else:
        st.write(f"**Target:** {st.session_state.current_topic} | **Level:** {st.session_state.current_difficulty}")
        if st.button("🔎 Run Full Integrity Audit", use_container_width=True):
            with st.spinner("Performing 10-point system review..."):
                report = audit_learning_material(st.session_state.current_topic, st.session_state.current_difficulty, st.session_state.current_content)
                st.markdown(report)

elif menu == "📈 Analytics":
    st.markdown("### 📈 Learning Analytics")
    # Mock data for production feel
    chart_data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "XP Earned": [20, 45, 30, 80, 100, 150, 450]
    })
    st.line_chart(chart_data, x="Day", y="XP Earned")
    st.markdown("""
    **Insights:**
    - You are most active on weekends.
    - Your accuracy in 'Applied Logic' has increased by 15% this week.
    """)

elif menu == "🏆 Leaderboard":
    st.markdown("### 🏆 Global Leaderboard")
    leader_data = pd.DataFrame([
        {"Pos": "🥇", "User": "Alex_AI", "XP": 2450, "Rank": "Grand Scholar"},
        {"Pos": "🥈", "User": "Sara_Tech", "XP": 1820, "Rank": "Master Strategist"},
        {"Pos": "🥉", "User": "David_Dev", "XP": 1400, "Rank": "Master Strategist"},
        {"Pos": "4", "User": "You", "XP": st.session_state.xp, "Rank": rank_name}
    ])
    st.table(leader_data)

else:
    st.info(f"{menu} is currently in development for v4.1.")
