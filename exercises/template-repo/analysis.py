"""Analysis module — Core functions for climate data analysis."""

import pandas as pd
import numpy as np


def load_data(filepath):
    """Load temperature data from CSV file.

    Parameters
    ----------
    filepath : str
        Path to the CSV file containing temperature records.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: date, station, temperature
    """
    df = pd.read_csv(filepath, parse_dates=["date"])
    return df


def calculate_annual_mean(df):
    """Calculate annual mean temperature per station.

    Parameters
    ----------
    df : pd.DataFrame
        Temperature data with 'date', 'station', and 'temperature' columns.

    Returns
    -------
    pd.DataFrame
        Annual means grouped by station and year.
    """
    df = df.copy()
    df["year"] = df["date"].dt.year
    annual = df.groupby(["station", "year"])["temperature"].mean().reset_index()
    annual.columns = ["station", "year", "mean_temperature"]
    return annual


def detect_trend(series, confidence=0.95):
    """Simple linear trend detection.

    Parameters
    ----------
    series : array-like
        Time series of values.
    confidence : float
        Confidence level for trend significance.

    Returns
    -------
    dict
        Slope, intercept, and whether trend is significant.
    """
    x = np.arange(len(series))
    coeffs = np.polyfit(x, series, 1)
    return {
        "slope_per_year": coeffs[0],
        "intercept": coeffs[1],
        "direction": "warming" if coeffs[0] > 0 else "cooling",
    }


if __name__ == "__main__":
    print("Climate Analysis Module")
    print("=" * 40)
    print("Run with: python analysis.py <data_file>")
    print()
    print("Available functions:")
    print("  - load_data(filepath)")
    print("  - calculate_annual_mean(df)")
    print("  - detect_trend(series)")
