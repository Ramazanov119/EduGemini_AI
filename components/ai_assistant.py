import streamlit as st
import time


def render_ai_card():
    st.markdown(
        """
        <div style="background: white; padding: 2px; border-radius: 25px; border: 1px solid #e0e0e0; box-shadow: 0 10px 30px rgba(0,0,0,0.08); margin-top: 20px;">
            <div style="background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%); padding: 15px 25px; border-radius: 23px 23px 5px 5px; display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <span style="font-size: 30px;">🤖</span>
                    <div>
                        <h3 style="
                            margin: 0;
                            font-size: 18px;
                            background: linear-gradient(90deg,#bfdbfe 0%,#facc15 50%,#f97316 100%);
                            -webkit-background-clip: text;
                            color: transparent;
                        ">
                            EduAI Assistant
                        </h3>
                        <div style="display: flex; align-items: center; gap: 6px;">
                            <div style="width: 8px; height: 8px; background: #00ff00; border-radius: 50%; box-shadow: 0 0 10px #00ff00;"></div>
                            <small style="color: rgba(255,255,255,0.8);">Система активна (Gemini 2.0)</small>
                        </div>
                    </div>
                </div>
                <div style="background: rgba(255,255,255,0.2); padding: 5px 12px; border-radius: 10px; color: white; font-size: 12px;">v2.4</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Привет! Я твой наставник. Могу составить план обучения или объяснить сложную тему. С чего начнем?",
            }
        ]

    with st.container(height=350, border=False):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

    st.write("⚡ **Быстрые вопросы:**")
    c1, c2, c3 = st.columns(3)
    if c1.button("📚 План на неделю", use_container_width=True):
        st.session_state.messages.append(
            {"role": "user", "content": "Составь мне план обучения на неделю"}
        )
        st.rerun()
    if c2.button("🚀 Взлом карьеры", use_container_width=True):
        st.session_state.messages.append(
            {"role": "user", "content": "Как быстрее всего стать Senior?"}
        )
        st.rerun()
    if c3.button("🧠 Мини-тест", use_container_width=True):
        st.session_state.messages.append(
            {"role": "user", "content": "Проведи короткий квиз по IT"}
        )
        st.rerun()

    if prompt := st.chat_input("Напиши сообщение..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner("ИИ думает..."):
            time.sleep(1)
            response = (
                f"Анализирую твой запрос: '{prompt}'. В 2026 году это решается через "
                "интеграцию нейросетей и системного подхода. "
                "Рекомендую изучить документацию в нашей библиотеке!"
            )
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )
        st.rerun()

