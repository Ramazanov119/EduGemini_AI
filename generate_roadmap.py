def generate_roadmap(goal):
    prompt = f"""
    Создай 3-месячный roadmap для школьника,
    который хочет стать {goal}.
    Разбей по неделям.
    Добавь темы и практику.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception:
        return """
        ⚠ Roadmap временно недоступен.
        
        Примерный план:
        Месяц 1 — Основы
        Месяц 2 — Практика
        Месяц 3 — Проект
        
        Продолжай учиться 🚀
        """