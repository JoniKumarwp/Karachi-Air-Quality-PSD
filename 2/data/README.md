# Karachi data status

`AirQualityKarachi.csv` currently contains **schema only**. It is not a completed dataset.

The original reference project contains daily Sialkot data, but this Karachi adaptation intentionally does not copy or relabel those values. Real Karachi observations must be populated before statistical results can be claimed.

Required final schema:

```text
date,co,no2,o3,so2
```

Expected annual row count for the documented period: 366 daily rows, subject to the final collection method and date coverage. Missing pollutant values should remain explicit as empty/NaN values rather than being invented.
