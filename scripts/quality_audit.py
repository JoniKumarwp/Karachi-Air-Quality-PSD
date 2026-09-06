from pathlib import Path
import math
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "2" / "data" / "AirQualityKarachi.csv"
OUTPUT = ROOT / "2" / "data" / "statistics_audit.csv"

if not INPUT.exists():
    raise FileNotFoundError(INPUT)

df = pd.read_csv(INPUT)
required = ["date", "co", "no2", "o3", "so2"]
if list(df.columns) != required:
    raise ValueError(f"Expected columns {required}; found {list(df.columns)}")
if len(df) == 0:
    raise ValueError("AirQualityKarachi.csv contains no data rows; annual statistics cannot be calculated.")

df["date"] = pd.to_datetime(df["date"], errors="coerce")
rows = []
for col in required[1:]:
    raw = df[col]
    numeric = pd.to_numeric(raw, errors="coerce")
    finite = numeric[pd.notna(numeric) & numeric.map(math.isfinite)]
    rows.append({
        "column": col,
        "min": finite.min(),
        "max": finite.max(),
        "mean": finite.mean(),
        "std_sample": finite.std(ddof=1),
        "variance_sample": finite.var(ddof=1),
        "skewness": finite.skew(),
        "kurtosis_fisher": finite.kurt(),
        "sum": finite.sum(),
        "no_missing": int(raw.isna().sum()),
        "no_nans": int(numeric.isna().sum()),
        "no_pos_inf": int((numeric == float("inf")).sum()),
        "no_neg_inf": int((numeric == float("-inf")).sum()),
        "median": finite.median(),
        "row_count": len(df),
    })

out = pd.DataFrame(rows)
out.to_csv(OUTPUT, index=False)
print(out.to_string(index=False))
print(f"\nSaved: {OUTPUT}")
