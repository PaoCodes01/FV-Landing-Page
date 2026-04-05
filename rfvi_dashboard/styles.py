"""
styles.py — CSS injected via st.markdown.
Uses @import inside <style> to avoid <link> tag parsing issues in Streamlit.
No f-strings on the CSS block — avoids brace-escaping bugs.
"""

_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400&family=DM+Mono:wght@300;400&family=DM+Sans:wght@300;400;500&display=swap');

:root {
  --bg:     #0E0C0B;
  --border: #2C2420;
  --terra:  #C94C1F;
  --text:   #EDE9E3;
  --muted:  #7A706A;
  --dim:    #3D3430;
  --fd: 'Cormorant Garamond', Georgia, serif;
  --fm: 'DM Mono', monospace;
  --fb: 'DM Sans', system-ui, sans-serif;
}

#MainMenu, footer, header, .stDeployButton { display: none !important; }
[data-testid="stSidebar"]                  { display: none !important; }
html, body { background: var(--bg) !important; }

.main .block-container {
  padding: 0 !important;
  max-width: 100% !important;
}
[data-testid="stAppViewContainer"] > section { padding: 0 !important; }

/* Header */
.rfvi-hdr {
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.75rem;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  position: relative;
}
.rfvi-hdr::after {
  content: '';
  position: absolute;
  bottom: -1px; left: 0;
  width: 64px; height: 2px;
  background: var(--terra);
}
.rfvi-title {
  font-family: var(--fd);
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--text);
  line-height: 1;
  white-space: nowrap;
}
.rfvi-title em {
  font-style: italic;
  color: var(--terra);
  font-weight: 400;
}
.rfvi-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}
.rfvi-pill {
  font-family: var(--fm);
  font-size: 0.58rem;
  color: var(--muted);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.rfvi-pill strong {
  color: var(--text);
  font-weight: 400;
}

/* Footer */
.rfvi-ftr {
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.75rem;
  background: var(--bg);
  border-top: 1px solid var(--border);
  font-family: var(--fm);
  font-size: 0.55rem;
  color: var(--dim);
  letter-spacing: 0.05em;
}
.rfvi-ftr strong { color: var(--muted); font-weight: 400; }
</style>
"""

def get_styles() -> str:
    return _CSS
