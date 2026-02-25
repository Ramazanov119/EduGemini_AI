import streamlit as st


def show_library():
    st.header("📚 Образовательный центр")
    st.subheader("Топ-10 книг 2026 года и связанные с ними курсы")

    library_data = [
        {
            "title": "Чистый код",
            "author": "Роберт Мартин",
            "tag": "Разработка",
            "img": "https://m.media-amazon.com/images/I/41xShlnTZTL._SX376_BO1,204,203,200_.jpg",
            "desc": "Библия для тех, кто хочет писать поддерживаемый и красивый код.",
            "courses": [
                "Основы Java",
                "Архитектура ПО",
                "Рефакторинг",
                "Unit-тесты",
                "Clean Code Pro",
            ],
        },
        {
            "title": "Грокаем алгоритмы",
            "author": "Адитья Бхаргава",
            "tag": "Computer Science",
            "img": "https://m.media-amazon.com/images/I/91cw36IKp6L.jpg",
            "desc": "Самое простое и наглядное введение в мир алгоритмов и структур данных.",
            "courses": [
                "Алгоритмы",
                "Python для профи",
                "Data Structures",
                "LeetCode",
                "Olymp Prog",
            ],
        },
        {
            "title": "Дизайн привычных вещей",
            "author": "Дон Норман",
            "tag": "Дизайн / UX",
            "img": "https://m.media-amazon.com/images/I/410vJpYvA6L._SX322_BO1,204,203,200_.jpg",
            "desc": "Как создавать вещи, которыми людям будет удобно пользоваться.",
            "courses": [
                "UX UI Design",
                "User Research",
                "Figma Expert",
                "Psychology",
                "Product Design",
            ],
        },
        {
            "title": "Атомные привычки",
            "author": "Джеймс Клир",
            "tag": "Продуктивность",
            "img": "https://m.media-amazon.com/images/I/51-nXsSRfZL._SX328_BO1,204,203,200_.jpg",
            "desc": "Как маленькие изменения приводят к огромным результатам.",
            "courses": [
                "Time Management",
                "Efficiency",
                "Neurobiology",
                "Success Psych",
                "Biohacking",
            ],
        },
        {
            "title": "Думай медленно... решай быстро",
            "author": "Даниэль Канеман",
            "tag": "Психология",
            "img": "https://m.media-amazon.com/images/I/41shS294S5L._SX330_BO1,204,203,200_.jpg",
            "desc": "Шедевр о том, как работает наше мышление и почему мы ошибаемся.",
            "courses": [
                "Critical Thinking",
                "Cognitive Psych",
                "Behavioral Econ",
                "Decision Making",
                "Logic",
            ],
        },
        {
            "title": "Не заставляйте меня думать",
            "author": "Стив Круг",
            "tag": "Веб-дизайн",
            "img": "https://m.media-amazon.com/images/I/41ovv6p3S9L._SX385_BO1,204,203,200_.jpg",
            "desc": "Ключевые принципы юзабилити веб-интерфейсов.",
            "courses": [
                "Web Analytics",
                "HTML & CSS",
                "Usability Test",
                "Frontend Dev",
                "Mobile UX",
            ],
        },
        {
            "title": "Scrum",
            "author": "Джефф Сазерленд",
            "tag": "Менеджмент",
            "img": "https://m.media-amazon.com/images/I/51H-pYk663L._SX326_BO1,204,203,200_.jpg",
            "desc": "Метод управления проектами, который изменил мир современной разработки.",
            "courses": [
                "Agile Project",
                "Scrum Master",
                "IT Management",
                "Kanban",
                "JIRA Mastery",
            ],
        },
        {
            "title": "Антихрупкость",
            "author": "Нассим Талеб",
            "tag": "Бизнес",
            "img": "https://m.media-amazon.com/images/I/416T0S-mGTL._SX323_BO1,204,203,200_.jpg",
            "desc": "Как извлекать выгоду из хаоса и неопределенности в бизнесе и жизни.",
            "courses": [
                "Risk Management",
                "Strategy",
                "Crisis Mgmt",
                "Investments",
                "Finance",
            ],
        },
        {
            "title": "Код",
            "author": "Чарльз Петцольд",
            "tag": "Computer Science",
            "img": "https://m.media-amazon.com/images/I/41-A8N8M0FL._SX382_BO1,204,203,200_.jpg",
            "desc": "Увлекательное объяснение того, как работают компьютеры на низком уровне.",
            "courses": [
                "CS Basics",
                "Hardware",
                "Low-level Prog",
                "OS Systems",
                "Assembler",
            ],
        },
        {
            "title": "Пиши, сокращай",
            "author": "Максим Ильяхов",
            "tag": "Копирайтинг",
            "img": "https://m.media-amazon.com/images/I/61S08H5vGvL.jpg",
            "desc": "Как создавать сильные тексты без мусора, фальши и лишних слов.",
            "courses": [
                "Copywriting",
                "Storytelling",
                "Editing",
                "Content Mark",
                "SMM Strategy",
            ],
        },
    ]

    for item in library_data:
        with st.container():
            st.markdown(
                f"""
                <div style="background: white; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                    <div style="display: flex; gap: 25px; flex-wrap: wrap; align-items: flex-start;">
                        <img src="{item['img']}" style="width: 130px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.15); object-fit: contain;">
                        <div style="flex: 1; min-width: 300px;">
                            <span style="background: #e1f5fe; color: #007bff; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold;">{item['tag']}</span>
                            <h2 style="margin: 15px 0 5px 0; color: #1e3a8a; font-size: 24px;">{item['title']}</h2>
                            <p style="margin: 0; color: #64748b; font-size: 16px;"><b>Автор:</b> {item['author']}</p>
                            <p style="margin: 15px 0; font-size: 15px; color: #333; line-height: 1.5;">{item['desc']}</p>
                        </div>
                    </div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            st.write(f"**🎓 Курсы к книге «{item['title']}»:**")
            c_cols = st.columns(5)
            for idx, course in enumerate(item["courses"]):
                with c_cols[idx]:
                    if st.button(
                        course,
                        key=f"lib_btn_{item['title']}_{idx}",
                        use_container_width=True,
                    ):
                        st.toast(f"Вы записаны на: {course}")
                        st.success("Успешно!")
            st.markdown("<br>", unsafe_allow_html=True)

