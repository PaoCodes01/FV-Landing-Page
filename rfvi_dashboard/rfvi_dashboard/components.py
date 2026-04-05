"""
components.py — HTML fragment builders for the RFVI dashboard page.
Each function returns a self-contained HTML string injected via st.markdown.
"""

from __future__ import annotations
from config import AUTHOR, COVERAGE, DATA_SOURCE, INDEX_NAME, TABLEAU_BASE_URL


def hero_html(active_label: str, active_description: str, active_tags: list[str]) -> str:
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in active_tags)
    return f"""
<div class="hero">
    <div class="hero-eyebrow">A Data Story on Regional Financial Vulnerability</div>
    <h1 class="hero-title">Financial Vulnerability<br><em>in the Philippines</em></h1>
    <p class="hero-subtitle">
        Explore how financial vulnerability varies across regions, sociodemographic
        groups, and work-related characteristics — built on the Labour Force Survey
        and the Regional Financial Vulnerability Index.
    </p>
    <div class="hero-meta-row">
        <div class="hero-stat">
            <span class="hero-stat-val">17</span>
            <span class="hero-stat-lbl">Regions</span>
        </div>
        <div class="hero-divider"></div>
        <div class="hero-stat">
            <span class="hero-stat-val">2018</span>
            <span class="hero-stat-lbl">Series Start</span>
        </div>
        <div class="hero-divider"></div>
        <div class="hero-stat">
            <span class="hero-stat-val">37.7%</span>
            <span class="hero-stat-lbl">Avg. RFVI</span>
        </div>
        <div class="hero-divider"></div>
        <div class="hero-stat">
            <span class="hero-stat-val">LFS</span>
            <span class="hero-stat-lbl">Data Source</span>
        </div>
    </div>
</div>

<div class="desc-card">
    <span class="desc-card-label">Viewing</span>
    <div class="desc-card-body">
        <strong style="color: var(--text); font-family: var(--font-body);">
            {active_label}
        </strong><br>
        {active_description}
        <div class="tag-row">{tags_html}</div>
    </div>
</div>
"""


def embed_toolbar_html(dashboard_id: str) -> str:
    url = f"{TABLEAU_BASE_URL}/{dashboard_id}"
    return f"""
<div class="embed-toolbar">
    <div class="embed-dot active"></div>
    <div class="embed-dot"></div>
    <div class="embed-dot"></div>
    <span class="embed-url">public.tableau.com › FinancialVulnerabilityinthePhilippines › {dashboard_id}</span>
</div>
"""


def tableau_embed_html(dashboard_id: str, height_px: int = 900) -> str:
    """
    Renders the Tableau JS embed snippet inside a styled wrapper.
    Uses the Tableau JavaScript API (viz_v1.js) for proper interactivity.
    """
    embed_url = (
        f"{TABLEAU_BASE_URL}/{dashboard_id}"
        "?:showVizHome=no&:embed=true&:toolbar=yes&:animate_transition=yes"
    )
    unique_id = f"tableau-viz-{dashboard_id}"

    return f"""
<div class="embed-wrapper">
    {embed_toolbar_html(dashboard_id)}
    <div style="position:relative; width:100%; height:{height_px}px; overflow:hidden;">
        <iframe
            id="{unique_id}"
            src="{embed_url}"
            width="100%"
            height="{height_px}"
            frameborder="0"
            scrolling="no"
            marginwidth="0"
            marginheight="0"
            allowfullscreen
            style="border:none; display:block;"
            loading="lazy"
        ></iframe>
    </div>
</div>
"""


def footer_html() -> str:
    return f"""
<div class="footer">
    <div class="footer-left">
        <strong>{INDEX_NAME}</strong> &nbsp;·&nbsp;
        Source: {DATA_SOURCE} &nbsp;·&nbsp;
        {COVERAGE}
    </div>
    <div class="footer-right">
        By {AUTHOR} &nbsp;·&nbsp; Hosted on Tableau Public
    </div>
</div>
"""
