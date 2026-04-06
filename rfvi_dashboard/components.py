"""
components.py — Header, footer, and Tableau embed HTML.
No author credit. No redundant stats. Matches landing page tone.
"""

from config import COVERAGE, DATA_SOURCE


def header_html() -> str:
    return """
<div class="rfvi-hdr">
  <div class="rfvi-hdr-inner">
    <div class="rfvi-hdr-left">
      <span class="rfvi-eyebrow">A data story on</span>
      <h1 class="rfvi-title">
        Financial Vulnerability &nbsp;<em>in the Philippines</em>
      </h1>
    </div>
    <div class="rfvi-hdr-right">
      <span class="rfvi-pill"><strong>17</strong> regions</span>
      <div class="rfvi-sep"></div>
      <span class="rfvi-pill"><strong>2018 – 2024</strong></span>
      <div class="rfvi-sep"></div>
      <span class="rfvi-pill">PSA · Labour Force Survey</span>
    </div>
  </div>
</div>
"""


def footer_html() -> str:
    return f"""
<div class="rfvi-ftr">
  <div class="rfvi-ftr-inner">
    <span><strong>Source</strong> &nbsp; {DATA_SOURCE} &nbsp;·&nbsp; {COVERAGE}</span>
    <span>Tableau Public &nbsp;·&nbsp; Philippine Statistics Authority</span>
  </div>
</div>
"""


def tableau_embed_html(viz_name: str, height_px: int) -> str:
    """
    Tableau JS API embed (viz_v1.js + object tag).
    Background matches landing page dark end of gradient.
    """
    return f"""<!DOCTYPE html>
<html>
<head>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{
    width:100%; height:{height_px}px;
    background: linear-gradient(180deg, #1A0A04 0%, #110601 100%);
    overflow:hidden;
  }}

  #loader {{
    position:absolute; inset:0; z-index:5;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center; gap:1rem;
    background: linear-gradient(180deg, #1A0A04 0%, #110601 100%);
    transition:opacity 0.5s ease;
  }}
  .ld-label {{
    font-family:Georgia,serif; font-style:italic;
    font-size:1rem; color:rgba(255,255,255,0.25);
    letter-spacing:0.04em;
  }}
  .ld-bar {{
    width:80px; height:2px;
    background:rgba(255,255,255,0.08);
    border-radius:2px; overflow:hidden;
  }}
  .ld-bar::after {{
    content:''; display:block; height:100%; width:30%;
    background:#CA4010; border-radius:2px;
    animation:sweep 1.3s ease-in-out infinite;
  }}
  @keyframes sweep {{
    0%   {{ transform:translateX(-100%); }}
    100% {{ transform:translateX(400%); }}
  }}

  #viz {{ position:absolute; inset:0; width:100%; height:100%; }}
  #viz object {{ width:100% !important; height:100% !important; display:block; }}
</style>
</head>
<body>
  <div id="loader">
    <p class="ld-label">Loading dashboard…</p>
    <div class="ld-bar"></div>
  </div>

  <div id="viz">
    <object class="tableauViz" style="display:none;">
      <param name="host_url"             value="https%3A%2F%2Fpublic.tableau.com%2F"/>
      <param name="embed_code_version"   value="3"/>
      <param name="site_root"            value=""/>
      <param name="name"                 value="{viz_name}"/>
      <param name="tabs"                 value="yes"/>
      <param name="toolbar"              value="yes"/>
      <param name="animate_transition"   value="yes"/>
      <param name="display_static_image" value="yes"/>
      <param name="display_spinner"      value="yes"/>
      <param name="display_overlay"      value="yes"/>
      <param name="display_count"        value="yes"/>
      <param name="language"             value="en-US"/>
      <param name="filter"               value="publish=yes"/>
    </object>
  </div>

  <script>
    (function() {{
      var obj = document.querySelector("#viz object");
      obj.style.width  = "100%";
      obj.style.height = "{height_px}px";

      var s  = document.createElement("script");
      s.src  = "https://public.tableau.com/javascripts/api/viz_v1.js";
      s.onload = function() {{
        var loader = document.getElementById("loader");
        setTimeout(function() {{
          loader.style.opacity = "0";
          setTimeout(function() {{ loader.style.display = "none"; }}, 500);
        }}, 1200);
      }};
      obj.parentNode.insertBefore(s, obj);
    }})();
  </script>
</body>
</html>"""
