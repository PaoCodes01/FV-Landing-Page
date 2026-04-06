"""
styles.py — Only strips Streamlit chrome. No layout CSS here.
All layout lives inside components.html() where it has full HTML support.
"""

_CSS = """
<style>
#MainMenu, footer, header, .stDeployButton,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }
[data-testid="stSidebar"]      { display: none !important; }

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
  background: #0E0A08 !important;
}
</style>
"""

def get_styles() -> str:
    return _CSS
