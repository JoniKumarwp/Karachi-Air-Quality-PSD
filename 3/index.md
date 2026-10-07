---
title: Mapping and Classification of Paddy Fields and Settlements Using Sentinel-2A Imagery
---

# Mapping and Classification of Paddy Fields and Settlements Using Sentinel-2A Imagery

This project maps paddy fields (`Sawah`) and settlements (`Pemukiman`) in Hyderabad, Sindh, Pakistan, using Sentinel-2A imagery and a Random Forest classifier. Training and test samples are split by polygon to avoid placing pixels from the same polygon in both sets.

## Project files

- [Python script](code-klasifikasiLahan.py)
- [Jupyter notebook](code-klasifikasiLahan.ipynb)
- [Input sample polygons](data/geojson/hyd_rice_building_data.geojson)
- [Python dependencies](requirements.txt)

## Run

From this directory, install the project dependencies and run the script:

```bash
python -m pip install -r requirements.txt
python code-klasifikasiLahan.py
```

The notebook can also be opened and run from this directory, cell by cell. The first run downloads Sentinel-2A imagery and a Copernicus DEM through openEO and may open a browser for Copernicus Data Space authentication. A free account is required. Existing rasters in `data/tif/` are reused.

## Data and results

The supplied GeoJSON contains labelled paddy-field and building polygons. The workflow normalizes known label spelling variants, removes invalid geometries, creates a study-area extent when needed, extracts Sentinel-2 spectral bands and indices, evaluates a Random Forest model, and generates a land-cover raster and maps.

The script creates intermediate CSV/GeoJSON files under `data/`, the classified GeoTIFF at `data/tif/klasifikasi_sawah_pemukiman.tif`, and map outputs under `assets/`. Classification metrics depend on the exact data and imagery returned by the run; no unverified accuracy values are reported here.

Satellite reflectance and DEM downloads are generated data and are not included in the repository.
