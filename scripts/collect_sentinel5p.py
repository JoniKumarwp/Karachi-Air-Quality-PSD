import json
from pathlib import Path
import openeo

ROOT = Path(__file__).resolve().parents[1]
GEOJSON_PATH = ROOT / "geojson" / "Karachi_Study_Area.geojson"
RAW_DIR = ROOT / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

START = "2025-08-24"
END = "2026-08-25"  # exclusive end; includes 24 Aug 2026
BANDS = ["CO", "NO2", "SO2", "O3"]

with open(GEOJSON_PATH, "r", encoding="utf-8") as f:
    geojson = json.load(f)
aoi = geojson["features"][0]["geometry"]

bbox = {
    "west": 66.652885437,
    "south": 24.759555817,
    "east": 67.5849169905,
    "north": 25.6510581344,
    "crs": "EPSG:4326",
}

connection = openeo.connect("openeo.dataspace.copernicus.eu").authenticate_oidc()

cubes = []
for band in BANDS:
    cube = connection.load_collection(
        "SENTINEL_5P_L2",
        temporal_extent=[START, END],
        spatial_extent=bbox,
        bands=[band],
    )
    cube = cube.aggregate_temporal_period(reducer="mean", period="day")
    cube = cube.aggregate_spatial(reducer="mean", geometries=aoi)
    cubes.append(cube)

merged = cubes[0]
for cube in cubes[1:]:
    merged = merged.merge_cubes(cube)

job = merged.execute_batch(
    title="Karachi Sentinel-5P Air Pollution 2025-2026",
    outputfile=str(RAW_DIR / "Karachi_Sentinel5P_2025_2026.nc"),
)
print(job)
