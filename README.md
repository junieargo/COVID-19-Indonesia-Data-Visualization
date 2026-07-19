# COVID-19 Indonesia Data Visualization

Exploratory data visualization of early COVID-19 data in Indonesia, using
pandas, matplotlib, and seaborn.

## What it does

- Reads province-level death counts (Jumlah_Kematian.csv) and
  patient-level records (patient.csv)
- Plots the 10 provinces with the fewest recorded COVID-19 deaths
- Plots patient current state (e.g. released, deceased, isolated) by
  province, colored by nationality, to visualize how outcomes were
  distributed across regions

## Setup

```bash
pip install -r requirements.txt
python analysis/covid_indonesia_visualization.py
```

## Data

Jumlah_Kematian.csv and patient.csv are included in the repo root.
COVID-19 di Indonesia.xlsx contains the same data in spreadsheet form.
