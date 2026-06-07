"""
components.py — Full page: app bar + Tableau embed + light/dark toggle.
Palette matches the updated index.html exactly:
  Dark:  #0F2240 → #0A1628 → #071020, gold #C8A84B / #E2C46A
  Light: #F5F2EB → #FFFDF8, navy text #0D1B2E, gold accents
Fonts: EB Garamond (display) + Inter (UI) — matches index.html.
"""

TABLEAU_PUBLIC_URL = (
    "https://public.tableau.com/views/"
    "FinancialVulnerabilityinthePhilippines/Dashboard1"
)


def full_embed_html(viz_name: str, embed_height: int) -> str:
    bar_h   = 52
    total_h = bar_h + embed_height

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Inter:wght@300;400;500&display=swap');

:root {{
  --bar-h:      {bar_h}px;
  --bg:         linear-gradient(160deg, #0F2240 0%, #0A1628 55%, #071020 100%);
  --bg-solid:   #0A1628;
  --embed-bg:   #071020;
  --bar-bg:     #0D1B2E;
  --bar-border: rgba(200,168,75,0.18);
  --text:       #E8E4D9;
  --text-dim:   rgba(232,228,217,0.40);
  --gold:       #E2C46A;
  --gold-dim:   rgba(200,168,75,0.55);
  --btn-bg:     rgba(200,168,75,0.08);
  --btn-border: rgba(200,168,75,0.30);
  --btn-text:   rgba(226,196,106,0.75);
  --btn-hover-bg:     rgba(200,168,75,0.16);
  --btn-hover-border: rgba(200,168,75,0.55);
  --btn-hover-text:   #E2C46A;
  --accent-bar: linear-gradient(180deg,#C8A84B 0%,#E2C46A 40%,#C8A84B 100%);
  --circle-stroke: rgba(200,170,90,0.07);
  --loader-bg:  #071020;
  --loader-text: rgba(232,228,217,0.18);
  --loader-bar-bg: rgba(255,255,255,0.06);
}}

/* ── Reset ── */
*, *::before, *::after {{ box-sizing:border-box; margin:0; padding:0; }}
html {{
  width:100%; height:{total_h}px;
  overflow:hidden;
  background: var(--bg-solid);
  transition: background 0.35s ease;
}}
body {{
  width:100%; height:{total_h}px;
  overflow:hidden;
  font-family:'Inter', system-ui, sans-serif;
  background: var(--bg);
  transition: background 0.35s ease;
}}

/* ── App bar ── */
.app-bar {{
  height: var(--bar-h);
  display:flex; align-items:center; justify-content:space-between;
  padding:0 40px;
  background: var(--bar-bg);
  border-bottom: 1px solid var(--bar-border);
  position:relative; overflow:hidden;
  animation: bar-in 0.45s cubic-bezier(0.16,1,0.3,1) both;
  transition: background 0.35s ease, border-color 0.35s ease;
  flex-shrink:0;
}}

/* Subtle geometric circles — matches index.html */
.app-bar::before {{
  content:'';
  position:absolute; right:-60px; top:-40px;
  width:180px; height:180px; border-radius:50%;
  border:1px solid var(--circle-stroke);
  pointer-events:none;
  transition: border-color 0.35s;
}}
.app-bar::after {{
  content:'';
  position:absolute; right:30px; top:10px;
  width:110px; height:110px; border-radius:50%;
  border:1px solid var(--circle-stroke);
  pointer-events:none;
  transition: border-color 0.35s;
}}

/* Gold left accent bar — signature element from index.html */
.accent-bar {{
  position:absolute; left:0; top:0; bottom:0;
  width:4px;
  background: var(--accent-bar);
}}

@keyframes bar-in {{
  from {{ opacity:0; transform:translateY(-100%); }}
  to   {{ opacity:1; transform:translateY(0); }}
}}

.bar-inner {{
  position:relative; z-index:2; width:100%;
  display:flex; align-items:center; justify-content:space-between;
  padding-left:12px;
}}

/* Wordmark */
.wordmark {{
  display:flex; align-items:baseline; gap:0.55rem;
}}
.wordmark-eyebrow {{
  font-size:0.52rem; font-weight:400;
  color: var(--text-dim);
  letter-spacing:0.18em; text-transform:uppercase;
  transition: color 0.35s;
}}
.wordmark-title {{
  font-family:'EB Garamond', Georgia, serif;
  font-size:1.15rem; font-weight:600;
  color: var(--text);
  line-height:1; white-space:nowrap;
  letter-spacing:-0.01em;
  transition: color 0.35s;
}}
.wordmark-title em {{
  font-style:italic; font-weight:400;
  color: var(--gold);
  opacity:0.80;
  transition: color 0.35s;
}}

/* Right side controls */
.bar-right {{
  display:flex; align-items:center; gap:0.75rem;
}}

/* CTA button */
.cta-link {{
  display:inline-flex; align-items:center; gap:0.4rem;
  font-size:0.63rem; font-weight:400;
  color: var(--btn-text);
  text-decoration:none;
  letter-spacing:0.05em;
  padding:0.3rem 0.75rem;
  border:1px solid var(--btn-border);
  border-radius:4px;
  background: var(--btn-bg);
  transition: color 0.2s, background 0.2s, border-color 0.2s;
}}
.cta-link:hover {{
  color: var(--btn-hover-text);
  background: var(--btn-hover-bg);
  border-color: var(--btn-hover-border);
}}
.cta-arrow {{
  font-size:0.68rem; opacity:0.6;
  display:inline-block;
  transition: transform 0.2s, opacity 0.2s;
}}
.cta-link:hover .cta-arrow {{
  transform:translate(2px,-2px); opacity:1;
}}

/* ── Embed area ── */
.embed-area {{
  position:relative;
  width:100%; height:{embed_height}px;
  background: var(--embed-bg);
  transition: background 0.35s ease;
}}

/* Loader shimmer */
#loader {{
  position:absolute; inset:0; z-index:5;
  display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:1rem;
  background: var(--loader-bg);
  transition: opacity 0.5s ease, background 0.35s ease;
}}
.ld-label {{
  font-family:'EB Garamond', Georgia, serif;
  font-style:italic; font-size:1rem;
  color: var(--loader-text);
  letter-spacing:0.04em;
}}
.ld-bar {{
  width:64px; height:2px;
  background: var(--loader-bar-bg);
  border-radius:2px; overflow:hidden;
}}
.ld-bar::after {{
  content:''; display:block; height:100%; width:30%;
  background: #C8A84B; border-radius:2px;
  animation: sweep 1.3s ease-in-out infinite;
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
    <div class="accent-bar"></div>
    <div class="bar-inner">

      <div class="wordmark">
        <span class="wordmark-eyebrow">Data Story</span>
        <span class="wordmark-title">
          Financial Vulnerability <em>in the Philippines</em>
        </span>
      </div>

      <div class="bar-right">
        <!-- GitHub repo -->
        <a class="cta-link"
           href="https://github.com/clemweb3/Undergraduate-Thesis-Repository"
           target="_blank"
           rel="noopener noreferrer">
          GitHub Repo
          <span class="cta-arrow">↗</span>
        </a>
        <!-- Tableau Public -->
        <a class="cta-link"
           href="{TABLEAU_PUBLIC_URL}"
           target="_blank"
           rel="noopener noreferrer">
          Open in Tableau Public
          <span class="cta-arrow">↗</span>
        </a>
      </div>

    </div>
  </div>

  <!-- Tableau embed -->
  <div class="embed-area">
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
  </div>

  <script>
    (function() {{
      /* ── Tableau embed ── */
      var obj = document.querySelector('#viz object');
      obj.style.width  = '100%';
      obj.style.height = '{embed_height}px';

      var s = document.createElement('script');
      s.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
      s.onload = function() {{
        var loader = document.getElementById('loader');
        setTimeout(function() {{
          loader.style.opacity = '0';
          setTimeout(function() {{ loader.style.display = 'none'; }}, 500);
        }}, 1200);
      }};
      obj.parentNode.insertBefore(s, obj);
    }})();
  </script>

</body>
</html>"""
