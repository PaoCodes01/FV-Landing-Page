"""
app.py — RFVI Dashboard.
Run:  py -m streamlit run app.py
"""

import streamlit as st
import streamlit.components.v1 as components

from config import PAGE_ICON, PAGE_TITLE, TABLEAU_VIZ_NAME
from components import footer_html, header_html, tableau_embed_html
from styles import get_styles

EMBED_H = 840   # adjust up/down ~20px if embed cuts off or leaves gap

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(get_styles(), unsafe_allow_html=True)
st.markdown(header_html(), unsafe_allow_html=True)
components.html(
    tableau_embed_html(viz_name=TABLEAU_VIZ_NAME, height_px=EMBED_H),
    height=EMBED_H,
    scrolling=False,
)
st.markdown(footer_html(), unsafe_allow_html=True)
