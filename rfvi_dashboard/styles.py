"""
styles.py — CSS for RFVI Streamlit wrapper.
Palette and typography match index.html landing page.
"""

_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400;1,500&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@300;400&display=swap');

:root {
  --terra-1: #CA4010;
  --terra-2: #A83208;
  --terra-3: #8C2405;
  --bg-dark:  #110601;
  --text:     #ffffff;
  --text-dim: rgba(255,255,255,0.45);
  --border:   rgba(255,255,255,0.10);
  --fd: 'Cormorant Garamond', Georgia, serif;
  --fb: 'DM Sans', system-ui, sans-serif;
  --fm: 'DM Mono', monospace;
}

/* ── Nuke every bit of Streamlit spacing ── */
#MainMenu, footer, header, .stDeployButton,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"]              { display: none !important; }
[data-testid="stSidebar"]                  { display: none !important; }

html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
.main, .block-container,
[data-testid="stAppViewContainer"] > section,
[data-testid="stVerticalBlock"],
[data-testid="stVerticalBlockBorderWrapper"] {
  margin: 0 !important;
  padding: 0 !important;
  max-width: 100% !important;
  background: var(--bg-dark) !important;
}

/* Pull the whole page flush to the very top */
[data-testid="stAppViewContainer"] {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  overflow: hidden !important;
}

/* ── Header ── */
.rfvi-hdr {
  height: 54px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  background: linear-gradient(150deg, #CA4010 0%, #A83208 55%, #8C2405 100%);
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
}
.rfvi-hdr::before {
  content: '';
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 50% 150% at 8% 50%, rgba(232,168,100,0.13) 0%, transparent 60%),
    radial-gradient(ellipse 30% 100% at 100% 100%, rgba(0,0,0,0.20) 0%, transparent 70%);
  pointer-events: none;
}
.rfvi-hdr::after {
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 56px 56px;
  pointer-events: none;
}
.rfvi-hdr-inner {
  position: relative; z-index: 2;
  width: 100%;
  display: flex; align-items: center; justify-content: space-between;
}
.rfvi-hdr-left {
  display: flex; align-items: baseline; gap: 0.6rem;
}
.rfvi-eyebrow {
  font-family: var(--fb);
  font-size: 0.55rem; font-weight: 300;
  color: rgba(255,255,255,0.40);
  letter-spacing: 0.16em; text-transform: uppercase;
}
.rfvi-title {
  font-family: var(--fd);
  font-size: 1.35rem; font-weight: 700;
  color: #fff; line-height: 1; white-space: nowrap;
}
.rfvi-title em {
  font-style: italic; font-weight: 500;
  color: rgba(255,255,255,0.72);
}
.rfvi-hdr-right {
  display: flex; align-items: center; gap: 1.5rem;
}
.rfvi-pill {
  font-family: var(--fm);
  font-size: 0.56rem;
  color: rgba(255,255,255,0.38);
  letter-spacing: 0.09em; text-transform: uppercase;
}
.rfvi-pill strong { color: rgba(255,255,255,0.78); font-weight: 400; }
.rfvi-sep { width: 1px; height: 14px; background: rgba(255,255,255,0.15); }

/* ── Footer ── */
.rfvi-ftr {
  height: 36px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 40px;
  background: linear-gradient(90deg, #6B1A02 0%, #8C2405 100%);
  position: relative; overflow: hidden; flex-shrink: 0;
}
.rfvi-ftr::after {
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 56px 56px;
  pointer-events: none;
}
.rfvi-ftr-inner {
  position: relative; z-index: 2; width: 100%;
  display: flex; align-items: center; justify-content: space-between;
  font-family: var(--fm);
  font-size: 0.54rem;
  color: rgba(255,255,255,0.28);
  letter-spacing: 0.07em;
}
.rfvi-ftr-inner strong { color: rgba(255,255,255,0.48); font-weight: 400; }
</style>
"""

def get_styles() -> str:
    return _CSS
