import streamlit as st
from config import apply_styles
from quiz import QUESTIONS
from ai_engine import generate_ai_analysis, generate_roadmap
from ui_components import render_radar_chart

# ================= CONFIG =================
st.set_page_config(page_title="AI Edu Navigator", layout="wide", page_icon="🚀")
apply_styles()

# ================= STATE =================
if "step" not in st.session_state:
    st.session_state.step = "register"
if "scores" not in st.session_state:
    st.session_state.scores = {k: 3 for k in QUESTIONS.keys()}
if "xp" not in st.session_state:
    st.session_state.xp = 0

# ================= REGISTER =================
if st.session_state.step == "register":

    st.markdown("<div class='hero-title'>🚀 AI Edu Navigator</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        name = st.text_input("Как тебя зовут?")
        grade = st.selectbox("Класс", ["9", "10", "11"])
        interest = st.selectbox("Интерес", ["IT", "Дизайн", "Бизнес", "Наука"])

        if st.button("Начать тест", use_container_width=True):
            if name:
                st.session_state.name = name
                st.session_state.grade = grade
                st.session_state.interest = interest
                st.session_state.step = "quiz"
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# ================= QUIZ =================
elif st.session_state.step == "quiz":

    st.header("🧠 Мини-тест")

    for skill, question in QUESTIONS.items():
        st.session_state.scores[skill] = st.slider(question, 1, 5, 3)

    if st.button("AI Анализ 🚀", use_container_width=True):
        st.session_state.xp += 50
        st.session_state.step = "analysis"
        st.rerun()

# ================= ANALYSIS =================
elif st.session_state.step == "analysis":

    st.header("🤖 AI Анализ")

    render_radar_chart(st.session_state.scores)

    with st.spinner("AI анализирует профиль..."):
        analysis = generate_ai_analysis(
            st.session_state.name,
            st.session_state.scores
        )

    st.markdown(f"<div class='card'>{analysis}</div>", unsafe_allow_html=True)

    goal = st.selectbox("Выбери цель:",
                        ["Backend разработчик",
                         "Frontend разработчик",
                         "Data Scientist",
                         "Cybersecurity эксперт"])

    if st.button("Построить Roadmap", use_container_width=True):
        st.session_state.goal = goal
        st.session_state.step = "roadmap"
        st.session_state.xp += 50
        st.rerun()

# ================= ROADMAP =================
elif st.session_state.step == "roadmap":

    st.header(f"🛤 Roadmap: {st.session_state.goal}")

    with st.spinner("AI строит твой план..."):
        roadmap = generate_roadmap(st.session_state.goal)

    st.markdown(f"<div class='card'>{roadmap}</div>", unsafe_allow_html=True)

    st.success(f"🎉 XP: {st.session_state.xp}")

    if st.button("Начать заново"):
        st.session_state.step = "register"
        st.session_state.xp = 0
        st.rerun()