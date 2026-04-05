"""
config.py — Dashboard configuration constants.
Centralises all runtime-tunable values to keep app.py clean.
"""

# ── Tableau ─────────────────────────────────────────────────────────────────
TABLEAU_BASE_URL = (
    "https://public.tableau.com/views"
    "/FinancialVulnerabilityinthePhilippines"
)

DASHBOARDS: list[dict] = [
    {
        "id": "Dashboard1",
        "label": "01 — Main Overview",
        "description": (
            "National RFVI trends, average S-R-E scores, "
            "regional breakdown, urban-rural comparison, and cluster distribution."
        ),
        "tags": ["RFVI Trend", "S-R-E Scores", "Urban vs Rural", "Cluster Types"],
    },
    {
        "id": "Dashboard2",
        "label": "02 — Sociodemographic",
        "description": (
            "Financial vulnerability by sex, age group, household size, "
            "marital status, and relationship to household head."
        ),
        "tags": ["Sex", "Age Group", "Household Size", "Marital Status"],
    },
    {
        "id": "Dashboard3",
        "label": "03 — Work-related",
        "description": (
            "Vulnerability across employment status, work availability, "
            "working hours, and other labour-related indicators."
        ),
        "tags": ["Employment", "Work Availability", "Working Hours", "Job Indicators"],
    },
    {
        "id": "Dashboard4",
        "label": "04 — S-R-E Clusters",
        "description": (
            "Scatter plots of sensitivity, resilience, and exposure across "
            "three cluster groups — Balanced, Exposure-Weighted, and Sensitivity-Weighted."
        ),
        "tags": ["Sensitivity vs Resilience", "Resilience vs Exposure", "3 Clusters"],
    },
]

# ── Meta ─────────────────────────────────────────────────────────────────────
PAGE_TITLE = "Financial Vulnerability in the Philippines"
PAGE_ICON = "📊"
AUTHOR = "Juan Paolo Aguilar"
DATA_SOURCE = "PSA Data Repository (PSADA)"
COVERAGE = "17 Regions · All Provinces · 2018–2024"
INDEX_NAME = "Regional Financial Vulnerability Index (RFVI)"
