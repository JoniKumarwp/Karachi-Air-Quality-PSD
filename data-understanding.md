---
title: "Data Understanding"
---

# Data Understanding

## 1. Data source

The intended data source is the **Copernicus Sentinel-5P mission**, accessed through the **Copernicus Data Space Ecosystem** and its openEO interface. Sentinel-5P carries the TROPOMI instrument and provides daily global observations of atmospheric constituents. Official Level-2 documentation lists CO, NO₂, O₃ and SO₂ products.

## 2. Physical quantities and units

| Variable | Physical quantity | Unit | Satellite/ground |
| --- | --- | --- | --- |
| CO | Carbon monoxide total column | mol/m² | Satellite atmospheric observation |
| NO₂ | Nitrogen dioxide tropospheric column | mol/m² | Satellite atmospheric observation |
| O₃ | Ozone total column | mol/m² | Satellite atmospheric observation |
| SO₂ | Sulfur dioxide total column | mol/m² | Satellite atmospheric observation |

The values must **not** be described as ground-level concentrations or converted into an official AQI unless a separate, valid conversion and the relevant AQI standard are available.

## 3. Study area

The project uses a Karachi study-area bounding box stored in `geojson/Karachi_Study_Area.geojson`. The geometry is intentionally documented as a **study-area box**, not an official administrative boundary. The bounding box is:

- West: 66.652885437
- South: 24.759555817
- East: 67.5849169905
- North: 25.6510581344
- CRS: EPSG:4326

If the lecturer requires an official Karachi administrative boundary, replace this box with an authoritative boundary and document the source.

## 4. Intended observation period

**24 August 2025 – 24 August 2026**. The openEO collection code uses `2026-08-25` as an exclusive end date so that 24 August 2026 is included.

## 5. What is actually present in the supplied project

The supplied project contains a successful-looking **25 August 2026 NO₂ test workflow** with 419 finite pixels and a separate summary CSV. It does **not** contain the underlying raster/point data for independent re-calculation, and it does not contain the completed year-long four-pollutant CSV. Therefore the current repository does not claim completed annual statistics.

## 6. Provenance references

- Copernicus Sentinel-5P overview: https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-5p
- Official Level-2 bands/units: https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data/S5PL2.html
- ESA TROPOMI overview: https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-5P/Tropomi
