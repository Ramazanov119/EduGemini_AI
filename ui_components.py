import plotly.graph_objects as go
import streamlit as st

def render_radar_chart(scores):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=list(scores.values()),
        theta=list(scores.keys()),
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0,5])),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)