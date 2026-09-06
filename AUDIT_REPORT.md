# Strict Project Audit — Karachi Air Quality PSD

**Student:** Joni Kumar Meghwar  
**NIM:** 240411100234  
**Reference:** https://github.com/mfarhancode/PSD  
**Requested adaptation:** Sialkot → Karachi, Sindh, Pakistan

## Executive verdict

**Overall quality: 55/100 for the supplied project before this cleanup.**

The project shows a technically plausible Sentinel-5P/openEO direction and a successful-looking NO₂ test, but the supplied archive does not contain the required completed four-pollutant Karachi daily dataset. The main blocker is therefore not cosmetic; it is the absence of verifiable underlying data needed for the requested annual statistics and KNIME/PostgreSQL result reproduction.

I did **not** copy or relabel Sialkot data and did **not** fabricate CO/O₃/SO₂ values.

## What was found

### Structure

The supplied project did not preserve the original top-level course structure. Instead it used a custom MyST project with a single analysis notebook, a GeoJSON box, and scripts. The original reference repository has `.github/`, `1/`, `2/`, `intro.md`, and `myst.yml`; under `2/data` it contains the four pollutant CSVs plus `merge.py`. The reference `merge.py` merges the four pollutant CSVs on `date` and writes `AirQualitySialkot.csv`.

### Data provenance

The supplied project documents **Copernicus Data Space Ecosystem / Sentinel-5P Level-2 / openEO**, which is a legitimate authoritative source pathway. Official Copernicus documentation lists: CO total column in mol/m², NO₂ tropospheric column in mol/m², O₃ total column in mol/m², and SO₂ total column in mol/m². ESA describes TROPOMI as an atmospheric sensor capable of imaging these trace gases and detecting pollution patterns at city scale.

### What can and cannot be verified

The project contains a summary file and notebook outputs for one NO₂ test on **25 August 2026**. The reported raster had 468 cells, 419 finite pixels and 49 non-finite cells. However, the archive does not contain the source GeoTIFF or the 419-row CSV generated inside the notebook. Therefore the exact 419-pixel statistics cannot be independently recalculated from the archive; they are only cross-checked against the included summary/output.

The archive also does not contain the requested year-long daily CO/NO₂/O₃/SO₂ CSV. Consequently, the following cannot be independently validated from raw project data: annual row count, annual missing values for each pollutant, and annual descriptive statistics.

### Fabrication check

No evidence was found that the archive secretly contains a complete Karachi four-pollutant dataset. The stronger integrity conclusion is that the project is **incomplete**, not that the missing data are fabricated. The project was deliberately repaired to preserve this limitation instead of disguising it.

### Security check

A prior notebook output contained a Copernicus OIDC device authentication URL with a one-time user code. This is not a reusable password/API key, but it is unnecessary authentication-session material. The cleaned notebook in the final ZIP has outputs removed so that authentication artifacts are not redistributed. No real Aiven password, API key, or database secret is included.

## Exact data/source facts

**Source:** Copernicus Data Space Ecosystem / Sentinel-5P Level-2 / TROPOMI via openEO.  
**Collection named in the project:** `SENTINEL_5P_L2`.  
**Intended period:** 24 August 2025 – 24 August 2026.  
**Verified test date present in the supplied notebook outputs:** 25 August 2026.

**Units:**

- CO — mol/m² total column
- NO₂ — mol/m² tropospheric column
- O₃ — mol/m² total column
- SO₂ — mol/m² total column

**Measurement type:** satellite atmospheric observations / column quantities, not direct ground-level concentration measurements.

## Independent statistics status

The requested annual statistics are **not independently calculable from the archive** because the annual raw/merged dataset is missing. The included `scripts/quality_audit.py` is designed to prevent an accidental false pass: it exits instead of calculating an annual result when `AirQualityKarachi.csv` has zero rows.

For a populated dataset, it uses sample standard deviation and sample variance (`ddof=1`), Pandas skewness, and Fisher excess kurtosis, and reports missing/NaN/±infinity counts separately.

## Fixes made

1. Reorganized the project into the original reference-style `1/` and `2/` structure.
2. Replaced student/profile information with Joni Kumar Meghwar / 240411100234 / Teknik Informatika / Semester 5 / Proyek Sains Data.
3. Created a reference-shaped Karachi `2/index.md` covering Aiven, pgAdmin, CSV import, KNIME, and statistical definitions.
4. Added a robust `scripts/merge.py` that validates dates, duplicate dates, one-value-per-pollutant input files, sorting, and output schema.
5. Added `scripts/quality_audit.py` for reproducible annual statistics.
6. Removed notebook execution outputs, including the previous Copernicus authentication device-code output.
7. Corrected scientific wording so Sentinel-5P variables are treated as atmospheric column quantities, not ground-level AQI values.
8. Added explicit data-gap documentation rather than adding fabricated records.
9. Added authoritative Copernicus/ESA references.

## Remaining manual work before genuine submission

The single blocking task is to obtain and retain the real Karachi four-pollutant daily dataset for the intended period, or to revise the assignment scope explicitly to a one-date NO₂ satellite analysis. After obtaining the data, populate the four pollutant CSVs, run `python scripts/merge.py`, run `python scripts/quality_audit.py`, import the merged CSV into PostgreSQL/KNIME, and reconcile the KNIME output with the Python audit and Markdown report.

Do not submit the current zero-row `AirQualityKarachi.csv` as though it were the finished annual dataset.
