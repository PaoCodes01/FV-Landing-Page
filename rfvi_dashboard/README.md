# Financial Vulnerability in the Philippines — Dashboard

Streamlit wrapper embedding the RFVI Tableau Public dashboards.

## Structure

```
rfvi_dashboard/
├── app.py           # Entry point — layout, sidebar, page assembly
├── config.py        # All constants (URLs, dashboard metadata, copy)
├── components.py    # HTML fragment builders (hero, embed, footer)
├── styles.py        # CSS injection (palette, typography, overrides)
├── requirements.txt
└── .streamlit/
    └── config.toml  # Streamlit theme (dark, terracotta accent)
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (Streamlit Community Cloud)
