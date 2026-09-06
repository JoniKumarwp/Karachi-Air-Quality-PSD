---
title: "Business Understanding"
---

# Business Understanding

## 1. Problem

Urban air quality varies across space and time. The project uses satellite atmospheric observations to demonstrate a reproducible data-science workflow for Karachi, Pakistan.

## 2. AQI distinction

The Air Quality Index is a communication index based on pollutant concentrations, averaging periods and a chosen standard. A Sentinel-5P column measurement is not automatically an AQI value. This project therefore reports the source measurement in its official physical quantity and unit.

## 3. Pollutants

| Pollutant | Current project status |
| --- | --- |
| NO₂ | One-date test analyzed (25 Aug 2026) |
| CO | Four-pollutant annual dataset not present |
| O₃ | Four-pollutant annual dataset not present |
| SO₂ | Four-pollutant annual dataset not present |

## 4. Objective

The target final workflow is:

1. obtain real Karachi Sentinel-5P observations;
2. aggregate them consistently by day and study area;
3. merge CO, NO₂, O₃ and SO₂ on date;
4. load the merged data into PostgreSQL;
5. reproduce the statistical features in KNIME/Python; and
6. document the results without fabricating missing values.
