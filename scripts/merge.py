from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "2" / "data"
OUTPUT = DATA / "AirQualityKarachi.csv"

FILES = {
    "co": DATA / "Pollutant_CO_Karachi.csv",
    "no2": DATA / "Pollutant_NO2_Karachi.csv",
    "o3": DATA / "Pollutant_O3_Karachi.csv",
    "so2": DATA / "Pollutant_SO2_Karachi.csv",
}

frames = []
for pollutant, path in FILES.items():
    if not path.exists():
        raise FileNotFoundError(f"Missing required source file: {path}")

    df = pd.read_csv(path)
    df.columns = [str(c).strip().lower() for c in df.columns]
    if "feature_index" in df.columns:
        df = df.drop(columns=["feature_index"])
    if "date" not in df.columns:
        raise ValueError(f"{path.name} must contain a 'date' column")

    value_cols = [c for c in df.columns if c != "date"]
    if len(value_cols) != 1:
        raise ValueError(
            f"{path.name} must contain exactly one pollutant value column besides date; found {value_cols}"
        )

    value_col = value_cols[0]
    df = df.rename(columns={value_col: pollutant})
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if df["date"].isna().any():
        bad = int(df["date"].isna().sum())
        raise ValueError(f"{path.name} contains {bad} invalid date value(s)")
    if df["date"].duplicated().any():
        dupes = int(df["date"].duplicated().sum())
        raise ValueError(f"{path.name} contains {dupes} duplicate date row(s)")

    df[pollutant] = pd.to_numeric(df[pollutant], errors="coerce")
    frames.append(df[["date", pollutant]])

merged = frames[0]
for frame in frames[1:]:
    merged = merged.merge(frame, on="date", how="outer", validate="one_to_one")

merged = merged[["date", "co", "no2", "o3", "so2"]].sort_values("date").reset_index(drop=True)
merged["date"] = merged["date"].dt.strftime("%Y-%m-%d")
merged.to_csv(OUTPUT, index=False)

print(f"Merged file saved: {OUTPUT}")
print(f"Rows: {len(merged)}")
print(f"Columns: {list(merged.columns)}")
