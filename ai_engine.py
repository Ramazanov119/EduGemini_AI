from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_ai_analysis(name, scores):
    prompt = f"""
    Ты карьерный AI-наставник.
    Пользователь: {name}
    Результаты теста: {scores}

    Сделай:
    1. Анализ сильных сторон
    2. Зоны роста
    3. Рекомендуемые IT-направления
    4. Предметы для подготовки
    5. Университеты Казахстана
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def generate_roadmap(goal):
    prompt = f"""
    Создай 3-месячный roadmap для школьника,
    который хочет стать {goal}.
    Разбей по неделям.
    Добавь темы и практику.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content