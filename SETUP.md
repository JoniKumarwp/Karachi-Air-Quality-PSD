# Setup

## Build the MyST site

```bash
pip install -r requirements.txt
myst start
```

## Validate the project

The current `AirQualityKarachi.csv` is intentionally zero-row. To complete the annual data workflow, add the four real pollutant CSVs to `2/data/` and run:

```bash
python scripts/merge.py
python scripts/quality_audit.py
```

The audit script is designed to fail loudly when the annual dataset is absent rather than produce misleading zero-row statistics.

## Copernicus authentication

The notebook uses interactive OIDC authentication. Never store account passwords, tokens or authentication-session links in the repository.
