"""
app.py — Regional Financial Vulnerability Index (RFVI) Dashboard
Streamlit wrapper for the Tableau Public visualisation.

Run:
    streamlit run app.py
"""

import streamlit as st

from config import DASHBOARDS, PAGE_ICON, PAGE_TITLE
from components import embed_toolbar_html, footer_html, hero_html, tableau_embed_html
from styles import get_styles

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Inject styles ─────────────────────────────────────────────────────────────
st.markdown(get_styles(), unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">Financial Vulnerability<br>in the Philippines</div>
        <div class="sidebar-sub">RFVI · PSA · PSADA · 2018–2024</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-label">Select Dashboard</div>', unsafe_allow_html=True)

    dashboard_labels = [d["label"] for d in DASHBOARDS]
    selected_label = st.radio(
        label="dashboard_selector",
        options=dashboard_labels,
        index=0,
        label_visibility="collapsed",
    )

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label">About</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="sidebar-meta">
            <span>Index</span><br>Regional Financial Vulnerability Index (RFVI)<br><br>
            <span>Source</span><br>Philippine Statistics Authority · PSADA<br><br>
            <span>Method</span><br>FAMD · MICE Imputation · K-Means Clustering<br><br>
            <span>Coverage</span><br>17 Regions · All Provinces<br><br>
            <span>Dimensions</span><br>Sensitivity · Resilience · Exposure
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Resolve active dashboard ──────────────────────────────────────────────────
active = next(d for d in DASHBOARDS if d["label"] == selected_label)

# ── Main content ──────────────────────────────────────────────────────────────
st.markdown(
    hero_html(
        active_label=active["label"],
        active_description=active["description"],
        active_tags=active["tags"],
    ),
    unsafe_allow_html=True,
)

st.markdown(
    tableau_embed_html(dashboard_id=active["id"], height_px=900),
    unsafe_allow_html=True,
)

st.markdown(footer_html(), unsafe_allow_html=True)
