"""
styles.py — Strips Streamlit chrome only. All visual design is in components.py.
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
  background: #0A1628 !important;
}
</style>
"""

def get_styles() -> str:
    return _CSS
