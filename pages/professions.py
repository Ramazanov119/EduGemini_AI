import streamlit as st


def show_professions():
    st.header("💼 Навигатор профессий 2026")
    st.subheader("Исследуй востребованные направления и начни свой путь")

    professions_data = [
        {
            "name": "Frontend Developer",
            "icon": "🎨",
            "salary": "450k+",
            "level": "Средний",
            "skills": ["React/Vue", "TypeScript", "Tailwind CSS"],
            "desc": "Создание интерфейсов, с которыми взаимодействует пользователь.",
        },
        {
            "name": "Data Scientist",
            "icon": "📊",
            "salary": "600k+",
            "level": "Высокий",
            "skills": ["Python", "Machine Learning", "Statistics"],
            "desc": "Анализ больших данных и построение прогнозных моделей.",
        },
        {
            "name": "Cybersecurity Expert",
            "icon": "🛡️",
            "salary": "550k+",
            "level": "Высокий",
            "skills": ["Pentesting", "Network Security", "Linux"],
            "desc": "Защита информационных систем от взломов и атак.",
        },
        {
            "name": "AI Prompt Engineer",
            "icon": "🤖",
            "salary": "400k+",
            "level": "Низкий",
            "skills": ["NLP", "Logic", "Creative Writing"],
            "desc": "Оптимизация запросов для нейросетей типа GPT и Claude.",
        },
        {
            "name": "DevOps Engineer",
            "icon": "♾️",
            "salary": "650k+",
            "level": "Высокий",
            "skills": ["Docker/K8s", "CI/CD", "AWS/Azure"],
            "desc": "Автоматизация процессов разработки и эксплуатации ПО.",
        },
        {
            "name": "UI/UX Designer",
            "icon": "✨",
            "salary": "350k+",
            "level": "Средний",
            "skills": ["Figma", "User Flow", "Prototyping"],
            "desc": "Проектирование удобного и красивого пользовательского опыта.",
        },
        {
            "name": "Backend Developer",
            "icon": "⚙️",
            "salary": "500k+",
            "level": "Средний",
            "skills": ["Python/Go/Node", "PostgreSQL", "API"],
            "desc": "Разработка серверной логики и баз данных.",
        },
        {
            "name": "Mobile Dev (Swift/Kotlin)",
            "icon": "📱",
            "salary": "480k+",
            "level": "Средний",
            "skills": ["SwiftUI", "Android SDK", "Architecture"],
            "desc": "Создание приложений для iOS и Android.",
        },
        {
            "name": "Blockchain Developer",
            "icon": "⛓️",
            "salary": "800k+",
            "level": "Очень высокий",
            "skills": ["Solidity", "Cryptography", "Smart Contracts"],
            "desc": "Разработка децентрализованных систем и сервисов.",
        },
        {
            "name": "Game Developer",
            "icon": "🎮",
            "salary": "420k+",
            "level": "Средний",
            "skills": ["C#", "Unity/Unreal Engine", "Math"],
            "desc": "Создание игровых миров и механик.",
        },
        {
            "name": "QA Automation",
            "icon": "🔍",
            "salary": "380k+",
            "level": "Низкий",
            "skills": ["Selenium", "Pytest", "Bug Tracking"],
            "desc": "Автоматизированное тестирование качества программ.",
        },
        {
            "name": "Digital Marketer",
            "icon": "📈",
            "salary": "300k+",
            "level": "Низкий",
            "skills": ["SEO", "Targeting", "Analytics"],
            "desc": "Продвижение продуктов в цифровой среде.",
        },
        {
            "name": "VR/AR Architect",
            "icon": "👓",
            "salary": "550k+",
            "level": "Высокий",
            "skills": ["3D Modeling", "C++", "Spatial UX"],
            "desc": "Проектирование миров дополненной и виртуальной реальности.",
        },
        {
            "name": "Project Manager",
            "icon": "📅",
            "salary": "400k+",
            "level": "Средний",
            "skills": ["Agile/Scrum", "Soft Skills", "Risk Mgmt"],
            "desc": "Управление командой и сроками реализации проектов.",
        },
        {
            "name": "Fullstack Engineer",
            "icon": "🌐",
            "salary": "600k+",
            "level": "Высокий",
            "skills": ["React", "Node.js", "System Design"],
            "desc": "Универсальный боец, создающий продукт целиком.",
        },
    ]

    cols = st.columns(3)
    for i, prof in enumerate(professions_data):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div style="background: white; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; margin-bottom: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
                    <div style="font-size: 40px; margin-bottom: 10px;">{prof['icon']}</div>
                    <h3 style="color: #1e3a8a; margin-bottom: 5px;">{prof['name']}</h3>
                    <p style="color: #28a745; font-weight: bold; margin-bottom: 5px;">ЗП: {prof['salary']}</p>
                    <hr style="margin: 10px 0; opacity: 0.2;">
                </div>
            """,
                unsafe_allow_html=True,
            )

            with st.expander("ℹ️ Подробнее"):
                st.write(f"**Описание:** {prof['desc']}")
                st.write(f"**Сложность входа:** {prof['level']}")
                st.write("**Ключевые стеки:**")
                st.code(", ".join(prof["skills"]))
                if st.button(f"Выбрать {prof['name']}", key=f"prof_btn_{i}"):
                    st.session_state.user_goal = prof["name"]
                    st.toast(f"Цель установлена: {prof['name']}!")

