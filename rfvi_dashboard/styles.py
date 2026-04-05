"""
styles.py — All custom CSS injected into Streamlit via st.markdown.
Kept in its own module so app.py stays readable.
"""

# Colours mirror the Tableau dashboard palette exactly.
PALETTE = {
    "bg":          "#0E0C0B",
    "surface":     "#1A1512",
    "surface_alt": "#231E1A",
    "border":      "#2E2722",
    "terracotta":  "#C94C1F",
    "terracotta_dim": "#9A3A17",
    "gold":        "#D4A84B",
    "text":        "#EDE9E3",
    "muted":       "#8A7F76",
    "subtle":      "#3D342E",
}

GOOGLE_FONTS = (
    "https://fonts.googleapis.com/css2?"
    "family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&"
    "family=DM+Mono:wght@300;400;500&"
    "family=DM+Sans:wght@300;400;500&"
    "display=swap"
)


def get_styles() -> str:
    p = PALETTE
    return f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{GOOGLE_FONTS}" rel="stylesheet">

<style>
/* ── Reset & Base ─────────────────────────────────────────────────────────── */
:root {{
    --bg:           {p['bg']};
    --surface:      {p['surface']};
    --surface-alt:  {p['surface_alt']};
    --border:       {p['border']};
    --terra:        {p['terracotta']};
    --terra-dim:    {p['terracotta_dim']};
    --gold:         {p['gold']};
    --text:         {p['text']};
    --muted:        {p['muted']};
    --subtle:       {p['subtle']};

    --font-display: 'Cormorant Garamond', Georgia, serif;
    --font-mono:    'DM Mono', 'Courier New', monospace;
    --font-body:    'DM Sans', system-ui, sans-serif;
}}

/* Hide Streamlit chrome */
#MainMenu, footer, header {{ visibility: hidden; }}
.stDeployButton {{ display: none; }}
.block-container {{
    padding: 0 !important;
    max-width: 100% !important;
}}
section[data-testid="stSidebar"] > div:first-child {{
    background: var(--surface);
    border-right: 1px solid var(--border);
}}

/* ── Sidebar ──────────────────────────────────────────────────────────────── */
.sidebar-brand {{
    font-family: var(--font-display);
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text);
    letter-spacing: 0.02em;
    line-height: 1.3;
    margin-bottom: 0.25rem;
}}
.sidebar-sub {{
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: var(--muted);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}}
.sidebar-divider {{
    height: 1px;
    background: var(--border);
    margin: 1.5rem 0;
}}
.sidebar-label {{
    font-family: var(--font-mono);
    font-size: 0.6rem;
    color: var(--muted);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}}
.sidebar-meta {{
    font-family: var(--font-body);
    font-size: 0.72rem;
    color: var(--muted);
    line-height: 1.7;
}}
.sidebar-meta span {{
    color: var(--text);
    font-weight: 500;
}}

/* Streamlit radio override */
div[data-testid="stRadio"] label {{
    font-family: var(--font-body) !important;
    font-size: 0.82rem !important;
    color: var(--muted) !important;
    transition: color 0.2s;
}}
div[data-testid="stRadio"] label:hover {{
    color: var(--text) !important;
}}
div[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p {{
    font-family: var(--font-body) !important;
    font-size: 0.82rem !important;
}}

/* ── Main canvas ──────────────────────────────────────────────────────────── */
.main-canvas {{
    background: var(--bg);
    min-height: 100vh;
    padding: 0;
}}

/* ── Hero Header ──────────────────────────────────────────────────────────── */
.hero {{
    background: linear-gradient(
        160deg,
        #1C1009 0%,
        #2A1505 40%,
        #1A0D03 70%,
        var(--bg) 100%
    );
    border-bottom: 1px solid var(--border);
    padding: 3.5rem 3rem 2.5rem;
    position: relative;
    overflow: hidden;
}}
.hero::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(
        ellipse 60% 80% at 70% 50%,
        rgba(201, 76, 31, 0.08) 0%,
        transparent 70%
    );
    pointer-events: none;
}}
.hero-eyebrow {{
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--terra);
    margin-bottom: 0.75rem;
}}
.hero-title {{
    font-family: var(--font-display);
    font-size: clamp(2rem, 4vw, 3.5rem);
    font-weight: 600;
    color: var(--text);
    line-height: 1.1;
    margin: 0 0 0.25rem;
}}
.hero-title em {{
    font-style: italic;
    color: var(--terra);
}}
.hero-subtitle {{
    font-family: var(--font-body);
    font-size: 0.9rem;
    color: var(--muted);
    font-weight: 300;
    max-width: 52ch;
    line-height: 1.6;
    margin-top: 0.75rem;
}}
.hero-meta-row {{
    display: flex;
    gap: 2rem;
    margin-top: 2rem;
    flex-wrap: wrap;
}}
.hero-stat {{
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
}}
.hero-stat-val {{
    font-family: var(--font-display);
    font-size: 1.6rem;
    font-weight: 600;
    color: var(--text);
    line-height: 1;
}}
.hero-stat-lbl {{
    font-family: var(--font-mono);
    font-size: 0.58rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
}}
.hero-divider {{
    width: 1px;
    background: var(--border);
    align-self: stretch;
}}

/* ── Dashboard description card ───────────────────────────────────────────── */
.desc-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--terra);
    border-radius: 4px;
    padding: 1.25rem 1.5rem;
    margin: 1.75rem 2rem 0;
    display: flex;
    align-items: flex-start;
    gap: 1.25rem;
}}
.desc-card-label {{
    font-family: var(--font-mono);
    font-size: 0.58rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--terra);
    white-space: nowrap;
    padding-top: 0.05rem;
    min-width: 4rem;
}}
.desc-card-body {{
    font-family: var(--font-body);
    font-size: 0.82rem;
    color: var(--muted);
    line-height: 1.65;
}}
.tag-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 0.6rem;
}}
.tag {{
    font-family: var(--font-mono);
    font-size: 0.58rem;
    letter-spacing: 0.06em;
    color: var(--muted);
    background: var(--surface-alt);
    border: 1px solid var(--border);
    border-radius: 2px;
    padding: 0.2rem 0.5rem;
}}

/* ── Tableau embed wrapper ────────────────────────────────────────────────── */
.embed-wrapper {{
    margin: 1.5rem 2rem 2rem;
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
    background: var(--surface);
    box-shadow: 0 24px 64px rgba(0,0,0,0.5);
}}
.embed-toolbar {{
    background: var(--surface-alt);
    border-bottom: 1px solid var(--border);
    padding: 0.6rem 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}}
.embed-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--border);
}}
.embed-dot.active {{ background: var(--terra); }}
.embed-url {{
    font-family: var(--font-mono);
    font-size: 0.62rem;
    color: var(--muted);
    margin-left: 0.5rem;
    letter-spacing: 0.02em;
}}

/* ── Footer ───────────────────────────────────────────────────────────────── */
.footer {{
    border-top: 1px solid var(--border);
    padding: 1.5rem 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1rem;
}}
.footer-left {{
    font-family: var(--font-mono);
    font-size: 0.62rem;
    color: var(--muted);
    letter-spacing: 0.06em;
}}
.footer-left strong {{
    color: var(--text);
    font-weight: 500;
}}
.footer-right {{
    font-family: var(--font-mono);
    font-size: 0.6rem;
    color: var(--subtle);
    letter-spacing: 0.06em;
}}

/* ── Streamlit element overrides ─────────────────────────────────────────── */
.stRadio > div {{
    gap: 0.4rem !important;
}}
div[data-testid="stSidebarContent"] {{
    padding: 1.5rem 1rem !important;
}}
</style>
"""
