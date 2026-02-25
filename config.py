import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    .hero-title {
        font-size: 52px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 20px;
    }
    .card {
        background: rgba(255,255,255,0.06);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(15px);
        margin-bottom: 20px;
    }
    .glow-btn button {
        background: linear-gradient(90deg,#ff00cc,#3333ff);
        color: white;
        border-radius: 14px;
        font-weight: 600;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)