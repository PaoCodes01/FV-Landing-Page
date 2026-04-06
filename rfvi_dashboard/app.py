"""
app.py — RFVI Dashboard.
Single components.html() call: app bar (48px) + embed (EMBED_H px).
No st.markdown for layout — avoids Streamlit HTML sanitization entirely.

Run:  py -m streamlit run app.py
"""

import streamlit as st
import streamlit.components.v1 as components

from config import PAGE_ICON, PAGE_TITLE, TABLEAU_VIZ_NAME
from components import full_embed_html
from styles import get_styles

BAR_H   = 48
EMBED_H = 900
TOTAL_H = BAR_H + EMBED_H

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Only use st.markdown for the Streamlit chrome-stripping CSS — no layout HTML
st.markdown(get_styles(), unsafe_allow_html=True)

# Everything visual lives inside this one sandboxed component
components.html(
    full_embed_html(viz_name=TABLEAU_VIZ_NAME, embed_height=EMBED_H),
    height=TOTAL_H,
    scrolling=False,
)
