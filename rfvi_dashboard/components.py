"""
components.py — Full page: app bar + Tableau embed in one components.html() call.
Anchor tags inside st.markdown get stripped by Streamlit — moving everything
into the sandboxed component iframe gives us full HTML support.
"""

TABLEAU_PUBLIC_URL = (
    "https://public.tableau.com/views/"
    "FinancialVulnerabilityinthePhilippines/Dashboard1"
)


def full_embed_html(viz_name: str, embed_height: int) -> str:
    """
    Single HTML document: app bar (48px) + Tableau embed (embed_height px).
    Total height passed to components.html() = 48 + embed_height.
    """
    bar_h = 48
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,500&family=DM+Sans:wght@300;400;500&display=swap');

* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{
  width:100%;
  height:{bar_h + embed_height}px;
  background:#0E0A08;
  overflow:hidden;
  font-family:'DM Sans', system-ui, sans-serif;
}}

/* ── App bar ── */
.app-bar {{
  height:{bar_h}px;
  display:flex; align-items:center; justify-content:space-between;
  padding:0 40px;
  background:linear-gradient(150deg,#CA4010 0%,#A83208 55%,#8C2405 100%);
  position:relative; overflow:hidden;
  animation:bar-in 0.5s cubic-bezier(0.16,1,0.3,1) both;
}}
@keyframes bar-in {{
  from {{ opacity:0; transform:translateY(-100%); }}
  to   {{ opacity:1; transform:translateY(0); }}
}}
.app-bar::before {{
  content:''; position:absolute; inset:0;
  background:
    radial-gradient(ellipse 40% 200% at 5% 50%, rgba(232,168,100,0.15) 0%, transparent 60%),
    radial-gradient(ellipse 25% 150% at 100% 100%, rgba(0,0,0,0.22) 0%, transparent 70%);
  pointer-events:none;
}}
.app-bar::after {{
  content:''; position:absolute; inset:0;
  background-image:
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size:56px 56px;
  animation:grid-drift 18s linear infinite;
  pointer-events:none;
}}
@keyframes grid-drift {{
  from {{ background-position:0 0; }}
  to   {{ background-position:56px 56px; }}
}}
.bar-inner {{
  position:relative; z-index:2; width:100%;
  display:flex; align-items:center; justify-content:space-between;
}}
.wordmark {{
  display:flex; align-items:baseline; gap:0.5rem;
}}
.wordmark-eyebrow {{
  font-size:0.52rem; font-weight:300;
  color:rgba(255,255,255,0.38);
  letter-spacing:0.18em; text-transform:uppercase;
}}
.wordmark-title {{
  font-family:'Cormorant Garamond', Georgia, serif;
  font-size:1.1rem; font-weight:600;
  color:#fff; line-height:1; white-space:nowrap;
}}
.wordmark-title em {{
  font-style:italic; font-weight:500;
  color:rgba(255,255,255,0.65);
}}
.cta-link {{
  display:inline-flex; align-items:center; gap:0.4rem;
  font-size:0.65rem; font-weight:400;
  color:rgba(255,255,255,0.50);
  text-decoration:none;
  letter-spacing:0.04em;
  padding:0.28rem 0.7rem;
  border:1px solid rgba(255,255,255,0.18);
  border-radius:4px;
  background:rgba(0,0,0,0.15);
  transition:color 0.2s, background 0.2s, border-color 0.2s;
}}
.cta-link:hover {{
  color:rgba(255,255,255,0.90);
  background:rgba(0,0,0,0.28);
  border-color:rgba(255,255,255,0.35);
}}
.cta-arrow {{
  font-size:0.68rem; opacity:0.6;
  display:inline-block;
  transition:transform 0.2s, opacity 0.2s;
}}
.cta-link:hover .cta-arrow {{
  transform:translate(2px,-2px);
  opacity:1;
}}

/* ── Embed area ── */
.embed-area {{
  position:relative;
  width:100%;
  height:{embed_height}px;
  background:linear-gradient(180deg,#1C0804 0%,#0E0A08 100%);
}}

/* Loading shimmer */
#loader {{
  position:absolute; inset:0; z-index:5;
  display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:1rem;
  background:linear-gradient(180deg,#1C0804 0%,#0E0A08 100%);
  transition:opacity 0.5s ease;
}}
.ld-label {{
  font-family:Georgia,serif; font-style:italic;
  font-size:0.95rem; color:rgba(255,255,255,0.18);
  letter-spacing:0.04em;
}}
.ld-bar {{
  width:72px; height:2px;
  background:rgba(255,255,255,0.07);
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

  <!-- App bar -->
  <div class="app-bar">
    <div class="bar-inner">
      <div class="wordmark">
        <span class="wordmark-eyebrow">Data Story</span>
        <span class="wordmark-title">
          Financial Vulnerability <em>in the Philippines</em>
        </span>
      </div>
      <a class="cta-link"
         href="{TABLEAU_PUBLIC_URL}"
         target="_blank"
         rel="noopener noreferrer">
        Open in Tableau Public
        <span class="cta-arrow">↗</span>
      </a>
    </div>
  </div>

  <!-- Tableau embed -->
  <div class="embed-area">
    <div id="loader">
      <p class="ld-label">Loading…</p>
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
  </div>

  <script>
    (function() {{
      var obj = document.querySelector("#viz object");
      obj.style.width  = "100%";
      obj.style.height = "{embed_height}px";

      var s = document.createElement("script");
      s.src = "https://public.tableau.com/javascripts/api/viz_v1.js";
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
