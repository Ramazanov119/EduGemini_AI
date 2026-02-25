import streamlit as st


def show_subscription():
    st.header("💎 Выбери свой уровень доступа")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="pricing-card"><h3>🐣 Free</h3><div class="price-val">0 ₸</div><p>Базовые курсы<br>Лента новостей</p></div>',
            unsafe_allow_html=True,
        )
        if st.button("Активировать Free", use_container_width=True):
            st.success("Бесплатный доступ открыт!")
    with c2:
        st.markdown(
            '<div class="pricing-card" style="border: 2px solid #007bff;"><h3>🚀 PRO</h3><div class="price-val">15 000 ₸</div><p>Все курсы<br>ИИ-наставник 24/7</p></div>',
            unsafe_allow_html=True,
        )
        if st.button("Купить PRO", use_container_width=True):
            with st.expander("Оплата PRO"):
                st.text_input("Номер карты", placeholder="0000 0000 0000 0000")
                col1, col2 = st.columns(2)
                col1.text_input("ММ/ГГ", placeholder="12/28")
                col2.text_input("CVC", type="password", placeholder="***")
                if st.button("Оплатить PRO"):
                    st.success("Оплата PRO успешна! 🎉")
                    st.balloons()
    with c3:
        st.markdown(
            '<div class="pricing-card"><h3>👑 VIP</h3><div class="price-val">30 000 ₸</div><p>Личные консультации<br>Трудоустройство</p></div>',
            unsafe_allow_html=True,
        )
        if st.button("Купить VIP", use_container_width=True):
            with st.expander("Оплата VIP"):
                st.text_input("Номер карты", placeholder="0000 0000 0000 0000")
                col1, col2 = st.columns(2)
                col1.text_input("ММ/ГГ", placeholder="12/28")
                col2.text_input("CVC", type="password", placeholder="***")
                if st.button("Оплатить VIP"):
                    st.success("Оплата VIP успешна! 🎉")
                    st.balloons()
    st.markdown("<hr>", unsafe_allow_html=True)
    st.info("По вопросам корпоративного обучения: nagibator@gmail.com")

