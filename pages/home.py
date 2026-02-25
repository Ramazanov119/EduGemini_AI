import streamlit as st

from components.ai_assistant import render_ai_card


def show_home():
    st.markdown(
        f"<div style='text-align: center; padding-bottom: 20px;'><h1>EduPlatform 2026 🚀</h1><p>Привет, {st.session_state.user_name}!</p></div>",
        unsafe_allow_html=True,
    )
    c_nav, c_news = st.columns([2, 1])
    with c_nav:
        st.subheader("📍 Навигация")
        n1, n2 = st.columns(2)
        if n1.button("🧠 Тесты", use_container_width=True):
            st.session_state.active_tab = "Опросник"
            st.rerun()
        if n1.button("💼 Профессии", use_container_width=True):
            st.session_state.active_tab = "Профессии"
            st.rerun()
        if n2.button("📚 Библиотека", use_container_width=True):
            st.session_state.active_tab = "Библиотека"
            st.rerun()
        if n2.button("🎮 Мини-игра", use_container_width=True):
            st.session_state.active_tab = "Мини-игра"
            st.rerun()
    with c_news:
        st.subheader("📢 Новости")
        st.markdown(
            '<div class="news-card"><small>Сегодня</small><br>Gemini 2.0 интегрирован!</div>',
            unsafe_allow_html=True,
        )
    st.divider()
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Онлайн", "1,240")
    s2.metric("Курсов", "45")
    s3.metric("Баллы", "2,850")
    s4.metric("Ударка", "14 дн")
    st.write("---")
    render_ai_card()

