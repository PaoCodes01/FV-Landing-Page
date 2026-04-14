"""
config.py — Dashboard configuration constants.
"""

PAGE_TITLE = "Financial Vulnerability in the Philippines"
PAGE_ICON  = "📊"

DATA_SOURCE = "PSA Data Repository (PSADA)"
COVERAGE    = "17 Regions · All Provinces · 2018–2024"

# Skip the Tableau landing page (redundant with index.html).
# Start directly on the FV Overview dashboard.
# Tab name must match exactly what's in Tableau — check yours and update if needed.
TABLEAU_VIZ_NAME = "FinancialVulnerabilityinthePhilippines/FVOverview"
