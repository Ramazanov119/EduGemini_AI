import streamlit as st
from openai import OpenAI


client = None
USE_REAL_AI = False

try:
    api_key = st.secrets.get("OPENAI_API_KEY")

    if api_key:
        client = OpenAI(api_key=api_key)
        USE_REAL_AI = True
    else:
        USE_REAL_AI = False

except Exception:
    USE_REAL_AI = False


def generate_ai_analysis(name, scores):

    prompt = f"""
    Ты карьерный AI-наставник для школьников Казахстана.

    Пользователь: {name}
    Результаты теста: {scores}

    Сделай:
    1. Анализ сильных сторон
    2. Зоны роста
    3. Подходящие IT-направления
    4. Предметы для подготовки к ЕНТ
    5. Университеты Казахстана

    Пиши мотивирующе и понятно для школьника.
    """

    # ---------- REAL AI ----------
    if USE_REAL_AI:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )

            return response.choices[0].message.content

        except Exception as e:
            # fallback если API временно недоступен
            return fallback_analysis(name, scores)

    # ---------- MOCK MODE ----------
    else:
        return fallback_analysis(name, scores)



def generate_roadmap(goal):

    prompt = f"""
    Создай 3-месячный roadmap для школьника,
    который хочет стать {goal}.

    Разбей по неделям.
    Добавь:
    - темы
    - практику
    - мини-проекты
    """

    if USE_REAL_AI:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )

            return response.choices[0].message.content

        except Exception:
            return fallback_roadmap(goal)

    else:
        return fallback_roadmap(goal)



def fallback_analysis(name, scores):

    strongest = max(scores, key=scores.get)

    text = f"""
    ⚠ AI временно работает в демо-режиме.

    {name}, по твоим результатам видно:

    """

    if strongest in ["logic", "backend"]:
        text += """
        🔥 У тебя сильная аналитика и логика.

        Подойдут:
        • Backend разработка
        • Data Science
        • Инженерия

        Прокачай:
        • Математику
        • Python
        • Алгоритмы
        """

    elif strongest in ["design", "frontend"]:
        text += """
        🎨 У тебя развито визуальное мышление.

        Подойдут:
        • UI/UX дизайн
        • Frontend разработка
        • Digital направление
        """

    elif strongest in ["security"]:
        text += """
        🛡 Ты склонен к защите и анализу рисков.

        Подойдут:
        • Кибербезопасность
        • Pentesting
        """

    else:
        text += """
        🚀 У тебя сбалансированный профиль.
        Можно развиваться в любом IT-направлении.
        """

    text += """

    🎓 Университеты Казахстана:
    • Назарбаев Университет
    • КБТУ
    • СДУ
    • IT University

    Продолжай развиваться!
    """

    return text

def fallback_roadmap(goal):

    return f"""
    ⚠ Roadmap создан в демо-режиме.

    🎯 Цель: {goal}

    📅 Месяц 1 — Основы
    - Изучить базовую теорию
    - Пройти 1 курс
    - Сделать мини-задания

    📅 Месяц 2 — Практика
    - 2 небольших проекта
    - Решать задачи ежедневно

    📅 Месяц 3 — Проект
    - Сделать полноценный проект
    - Выложить на GitHub
    - Подготовить портфолио

    Ты на правильном пути 🚀
    """