"""
COVID-19 Indonesia Data Visualization

Visualizes early COVID-19 data in Indonesia from two datasets:
- Jumlah_Kematian.csv: death counts by province
- patient.csv: individual patient records (nationality, state, province)

Run from the repo root:
    python analysis/covid_indonesia_visualization.py
"""

import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA_DIR = os.path.join(os.path.dirname(__file__), "..")


def load_data():
    death = pd.read_csv(os.path.join(DATA_DIR, "Jumlah_Kematian.csv"))
    patient = pd.read_csv(os.path.join(DATA_DIR, "patient.csv"))
    return death, patient


def plot_deaths_by_province(death: pd.DataFrame):
    """Bar chart of death counts for the 10 provinces with the fewest deaths."""
    counts = death["provinsi"].value_counts().sort_values().head(10)

    plt.figure(figsize=(15, 5))
    plt.title("10 Provinsi di Indonesia Dengan Jumlah Kematian COVID-19 Tersedikit")
    counts.plot.bar()
    plt.xlabel("Provinsi")
    plt.ylabel("Jumlah Kematian")
    plt.tight_layout()


def plot_state_by_province_and_nationality(patient: pd.DataFrame):
    """Scatter plot of patient current_state across provinces, colored by nationality."""
    sns.set_style("darkgrid")
    grid = sns.FacetGrid(patient, hue="nationality", height=10)
    grid.map(plt.scatter, "current_state", "province").add_legend()
    plt.title("State by Province and Nationality")


def main():
    death, patient = load_data()
    plot_deaths_by_province(death)
    plot_state_by_province_and_nationality(patient)
    plt.show()


if __name__ == "__main__":
    main()
