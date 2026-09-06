# Karachi Air Quality — Proyek Sains Data

**Student:** Joni Kumar Meghwar  
**NIM:** 240411100234  
**Program:** Teknik Informatika  
**Semester:** 5  
**Course:** Proyek Sains Data  
**Study area:** Karachi, Sindh, Pakistan

This repository is a Karachi adaptation of the original course project at:
https://github.com/mfarhancode/PSD

## Audit status

**Strict review status: NOT YET SUBMISSION-READY.**

The supplied Claude-generated project contains a reproducible Sentinel-5P/openEO **single-date NO₂ test** for 25 August 2026 and supporting documentation, but it does **not** contain the required completed 24 August 2025–24 August 2026 four-pollutant daily CSV dataset (CO, NO₂, O₃, SO₂). Because the raw observations are absent, this repository intentionally does not invent or copy Sialkot values and does not claim year-long statistics.

The project has been cleaned so that the missing data is explicit, the statistical calculation code is reproducible, the merge workflow is robust, and the documentation keeps Sentinel-5P atmospheric column measurements distinct from ground-level AQI.

## Verified scientific data source

The intended source is **Copernicus Sentinel-5P Level-2 data accessed through the Copernicus Data Space Ecosystem/openEO**. The official Sentinel-5P documentation identifies the following physical quantities and units:

- CO: total column, mol/m²
- NO₂: tropospheric column, mol/m²
- O₃: total column, mol/m²
- SO₂: total column, mol/m²

These are satellite atmospheric observations; they are not direct ground-station concentrations or an official AQI value.

## Required data before submission

Populate `2/data/` with real Karachi observations for the documented study period, then run:

```bash
python scripts/merge.py
python scripts/quality_audit.py
```

The expected merged schema is `date,co,no2,o3,so2`. The audit script computes min, max, mean, sample standard deviation, sample variance, skewness, kurtosis, sum, missing values, NaN count, ±infinity counts, median, and row count directly from the CSV.

## Source references

- Reference course repository: https://github.com/mfarhancode/PSD
- Copernicus Sentinel-5P: https://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-5p
- Sentinel-5P Level-2 band documentation: https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data/S5PL2.html
- ESA TROPOMI overview: https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-5P/Tropomi

See `AUDIT_REPORT.md` for the complete strict review and the evidence behind the submission block.
