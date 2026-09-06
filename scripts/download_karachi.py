from pathlib import Path
import openeo


# =========================================================
# Paths
# =========================================================
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "2" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


# =========================================================
# Karachi study area
# =========================================================
KARACHI = {
    "type": "Polygon",
    "coordinates": [[
        [66.70, 24.70],
        [67.40, 24.70],
        [67.40, 25.40],
        [66.70, 25.40],
        [66.70, 24.70]
    ]]
}


# =========================================================
# Date range
# =========================================================
TEMPORAL_EXTENT = [
    "2025-08-24",
    "2026-08-24"
]


# =========================================================
# Pollutants
# =========================================================
POLLUTANTS = {
    "CO": "Pollutant_CO_Karachi.csv",
    "NO2": "Pollutant_NO2_Karachi.csv",
    "O3": "Pollutant_O3_Karachi.csv",
    "SO2": "Pollutant_SO2_Karachi.csv",
}


# =========================================================
# Connect to Copernicus
# =========================================================
print("Connecting to Copernicus Data Space...")

connection = openeo.connect(
    "https://openeo.dataspace.copernicus.eu"
)

connection.authenticate_oidc()

print("Authenticated successfully.")


# =========================================================
# Download each pollutant
# =========================================================
for band, filename in POLLUTANTS.items():

    print("\n" + "=" * 60)
    print(f"Processing {band}")
    print("=" * 60)

    cube = connection.load_collection(
        "SENTINEL_5P_L2",
        bands=[band],
        temporal_extent=TEMPORAL_EXTENT,
        spatial_extent={
            "west": 66.70,
            "south": 24.70,
            "east": 67.40,
            "north": 25.40,
            "crs": "EPSG:4326",
        },
    )

    # Daily average over the Karachi polygon.
    daily = cube.aggregate_temporal_period(
        period="day",
        reducer="mean"
    )

    spatial_mean = daily.aggregate_spatial(
        geometries=KARACHI,
        reducer="mean",
    )

    output_file = DATA_DIR / filename

    print(f"Submitting {band} batch job...")

    job = spatial_mean.create_job(
        out_format="CSV",
        title=f"Karachi Sentinel-5P {band} Daily Mean",
    )

    job.start_and_wait()

    print(f"Downloading {band} result...")

    job.download_result(output_file)

    print(f"Saved: {output_file}")


print("\nAll pollutant downloads completed.")