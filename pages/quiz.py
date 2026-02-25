import streamlit as st


def show_quiz():
    st.header("🧠 Профориентационный Квест")

    if "quest_pool" not in st.session_state:
        st.session_state.quest_pool = [
            {
                "q": "Что тебе ближе в творчестве?",
                "opts": {
                    "Логика и алгоритмы": "backend",
                    "Визуал и эстетика": "design",
                    "Поиск скрытых ошибок": "qa",
                },
            },
            {
                "q": "Если бы ты строил дом, ты бы...",
                "opts": {
                    "Рисовал фасад": "design",
                    "Прокладывал сложные коммуникации": "backend",
                    "Проверял стены на прочность": "qa",
                },
            },
            {
                "q": "Какая суперсила тебе нужнее?",
                "opts": {
                    "Предсказывать будущее по данным": "data",
                    "Создавать миры из кода": "frontend",
                    "Защищать от темных сил (хакеров)": "security",
                },
            },
        ]
        st.session_state.test_step = 0
        st.session_state.score = {
            "backend": 0,
            "design": 0,
            "qa": 0,
            "data": 0,
            "frontend": 0,
            "security": 0,
        }

    progress = st.session_state.test_step / len(st.session_state.quest_pool)
    st.progress(progress)
    st.write(
        f"Вопрос {st.session_state.test_step + 1} из {len(st.session_state.quest_pool)}"
    )

    if st.session_state.test_step < len(st.session_state.quest_pool):
        current_q = st.session_state.quest_pool[st.session_state.test_step]

        st.markdown(
            f"""
            <div class="job-card" style="margin-bottom: 20px; border-left: 5px solid #3b82f6;">
                <h2 style="margin: 0;">{current_q['q']}</h2>
            </div>
        """,
            unsafe_allow_html=True,
        )

        for text, category in current_q["opts"].items():
            if st.button(text, use_container_width=True, key=f"btn_{text}"):
                st.session_state.score[category] += 1
                st.session_state.test_step += 1
                st.rerun()
    else:
        st.balloons()
        top_category = max(
            st.session_state.score, key=st.session_state.score.get
        )

        results = {
            "backend": "Твой путь — Backend Разработчик ⚙️",
            "design": "Ты рожден быть UI/UX Дизайнером ✨",
            "qa": "Твое призвание — QA Инженер (Тестировщик) 🔍",
            "data": "Ты будущий Data Scientist 📊",
            "frontend": "Твой выбор — Frontend Разработчик 🎨",
            "security": "Ты — будущий Кибер-ниндзя (Security Expert) 🛡️",
        }

        st.markdown(
            f"""
            <div class="pricing-card" style="background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%); color: white; border: none;">
                <h1 style="color: white !important;">Результат теста:</h1>
                <h2 style="color: white !important;">{results[top_category]}</h2>
                <p style="color: rgba(255,255,255,0.8);">На основе твоих ответов мы подобрали идеальное направление в ИТ.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button("К списку профессий", use_container_width=True):
            st.session_state.active_tab = "Профессии"
            st.rerun()

        if st.button("Пройти заново", type="secondary"):
            del st.session_state.quest_pool
            st.session_state.test_step = 0
            st.rerun()

