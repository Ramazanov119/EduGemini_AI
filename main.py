import streamlit as st
import time

from pages.home import show_home
from pages.quiz import show_quiz
from pages.professions import show_professions
from pages.library import show_library
from pages.game import show_game
from pages.subscription import show_subscription

# ----------------- НАСТРОЙКА СТРАНИЦЫ -----------------
st.set_page_config(page_title="EduPlatform 2026", layout="wide", page_icon="🎓")

# ----------------- SOFT TECH СТИЛИЗАЦИЯ (LIGHT MODE) -----------------
st.markdown("""
<style>
    /* 1. Общий фон: Чистый, светлый, с легким градиентом */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');

    .stApp {
        background: radial-gradient(at 0% 0%, #f8fafc 0, transparent 50%),
                    radial-gradient(at 100% 100%, #eff6ff 0, transparent 50%);
        background-color: #ffffff;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #0f172a;
    }

    /* 2. Навигация: Сетчатый «стеклянный» эффект */
    div[data-testid="stHorizontalBlock"] {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        padding: 8px 15px;
        border-radius: 18px;
        border: 1px solid rgba(226, 232, 240, 0.8);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
        margin-bottom: 30px;
    }

    div[data-testid="stHorizontalBlock"] button {
        color: #64748b !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        border: none !important;
        background: transparent !important;
        transition: all 0.3s ease;
    }

    div[data-testid="stHorizontalBlock"] button:hover {
        color: #2563eb !important;
        transform: translateY(-1px);
    }

    /* 3. Заголовки и акценты: Насыщенный синий */
    h1, h2, h3, b, strong {
        color: #1e293b !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
    }

    /* Синие «умные» акценты */
    .blue-highlight { color: #2563eb; }

    /* 4. Карточки: Объемные и мягкие */
    .news-card, .job-card, .lib-card-container, .pricing-card {
        background: #ffffff !important;
        border: 1px solid #f1f5f9 !important;
        border-radius: 24px !important;
        padding: 24px !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.02), 0 4px 6px -4px rgba(0, 0, 0, 0.02);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .job-card:hover, .pricing-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 25px -5px rgba(37, 99, 235, 0.1), 0 8px 10px -6px rgba(37, 99, 235, 0.05) !important;
        border-color: #dbeafe !important;
    }

    /* 5. Детализация: Декоративные элементы */
    .news-card::before {
        content: "";
        display: block;
        width: 40px;
        height: 4px;
        background: #2563eb;
        border-radius: 10px;
        margin-bottom: 12px;
    }

    /* 6. Кнопки: Современный плоский стиль */
    .stButton>button {
        background: #1e293b !important;
        color: #ffffff !important;
        border-radius: 14px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        border: 1px solid #1e293b !important;
        box-shadow: 0 4px 12px rgba(30, 41, 59, 0.15) !important;
        transition: background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease, color 0.2s ease !important;
    }

    .stButton>button:hover {
        background: #2563eb !important;
        border-color: #2563eb !important;
        color: #e0f2fe !important;
        transform: translateY(-3px) scale(1.01);
        box-shadow: 0 10px 18px rgba(37, 99, 235, 0.35) !important;
    }

    /* 7. Метрики: Чистые и крупные */
    [data-testid="stMetric"] {
        background: white;
        padding: 15px;
        border-radius: 20px;
        border: 1px solid #f1f5f9;
    }

    /* Цвет текста метрик (подписи и значения) */
    [data-testid="stMetricLabel"], 
    [data-testid="stMetricValue"], 
    [data-testid="stMetricDelta"] {
        color: #0f172a !important;
    }

    /* 8. ИИ-Ассистент: Плавающий виджет */
    .ai-box {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        color: #1e293b !important;
        border-radius: 28px !important;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15) !important;
    }

    /* 9. Сообщения чата ассистента */
    [data-testid="stChatMessage"] {
        background: #f8fafc;
        border-radius: 16px;
        padding: 8px 12px;
        margin-bottom: 8px;
    }
    [data-testid="stChatMessage"] p {
        color: #0f172a !important;
    }

    /* 10. Подпись выбора класса на регистрации */
    .registration-label {
        font-size: 14px;
        font-weight: 600;
        color: #0f172a;
        opacity: 0.85;
        margin-bottom: 4px;
    }
</style>
""", unsafe_allow_html=True)
# ----------------- СОСТОЯНИЕ -----------------
if "auth" not in st.session_state:
    st.session_state.auth = False
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Главная"
if "test_step" not in st.session_state:
    st.session_state.test_step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# ----------------- РЕГИСТРАЦИЯ -----------------
if not st.session_state.auth:
    _, col_main, _ = st.columns([1, 2, 1])

    with col_main:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 30px; animation: fadeInUp 0.8s ease-out;">
                <h1 style="font-size: 40px;">🚀 EduPlatform 2026</h1>
                <p style="font-size: 16px; opacity: 0.8;">Твой путь в IT начинается здесь</p>
            </div>
        """, unsafe_allow_html=True)

        with st.container():
            st.markdown('<div class="pricing-card" style="text-align: left; padding: 40px;">', unsafe_allow_html=True)

            st.subheader("📝 Создай свой профиль")

            # Аватар
            st.write("Выбери свой аватар:")
            avatar_list = ["🚀", "💻", "🧠", "🕶️", "⚡", "🤖", "🎨", "🛡️"]
            selected_avatar = st.select_slider("Аватар", options=avatar_list, value="🚀", label_visibility="collapsed")

            # Поля
            u_name = st.text_input("Как тебя зовут?", placeholder="Например, Иван")
            u_email = st.text_input("Твой Email", placeholder="example@mail.com")

            # Возвращаем выбор классов
            st.markdown('<p class="registration-label">В каком ты классе?</p>', unsafe_allow_html=True)
            u_status = st.radio(
                "Класс",
                ["9 класс", "10 класс", "11 класс", "Взрослый"],
                horizontal=True,
                label_visibility="collapsed"
            )

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button("Начать обучение ✨", use_container_width=True):
                if not u_name or not u_email:
                    st.error("Пожалуйста, введи имя и email!")
                elif "@" not in u_email:
                    st.warning("Проверь корректность email (нужна @)!")
                else:
                    with st.spinner("Создаем твою цифровую личность..."):
                        time.sleep(1)
                        st.session_state.auth = True
                        st.session_state.user_name = u_name
                        st.session_state.user_avatar = selected_avatar
                        st.session_state.user_level = u_status  # Теперь здесь будет "9 класс", "10 класс" и т.д.
                        st.balloons()
                        st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

# ----------------- НАВИГАЦИЯ И РОУТЕР -----------------
tabs = ["Главная", "Опросник", "Профессии", "Библиотека", "Мини-игра", "Подписка"]

with st.sidebar:
    st.markdown(
        f"""
        <div style="
            padding: 18px 12px;
            border-radius: 18px;
            text-align: center;
            background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
            box-shadow: 0 10px 25px rgba(15,23,42,0.45);
            color: #f9fafb;
        ">
            <div style="font-size: 40px; margin-bottom: 6px;">{st.session_state.user_avatar}</div>
            <div style="font-weight: 700; font-size: 17px; letter-spacing: -0.02em;">{st.session_state.user_name}</div>
            <div style="
                font-size: 12px;
                opacity: 0.95;
                margin-top: 6px;
                padding: 4px 10px;
                border-radius: 999px;
                background: rgba(15,23,42,0.7);
                display: inline-block;
            ">
                {st.session_state.user_level}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    selected_tab = st.radio("Разделы", tabs, index=tabs.index(st.session_state.active_tab))
    st.session_state.active_tab = selected_tab

st.markdown("<hr style='margin: 0px 0 25px 0; opacity: 0.1;'>", unsafe_allow_html=True)

if st.session_state.active_tab == "Главная":
    show_home()
elif st.session_state.active_tab == "Опросник":
    show_quiz()
elif st.session_state.active_tab == "Профессии":
    show_professions()
elif st.session_state.active_tab == "Библиотека":
    show_library()
elif st.session_state.active_tab == "Мини-игра":
    show_game()
elif st.session_state.active_tab == "Подписка":
    show_subscription()
