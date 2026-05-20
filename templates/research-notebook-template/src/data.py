"""Shared data loading and utility functions.

Keep reusable logic here, not in notebooks.
Notebooks are for exploration; this module is for production code.
"""

import pandas as pd
import numpy as np


def load_data(filepath=None):
    """Load the research dataset.

    If no filepath is provided, generates sample data for demonstration.

    Parameters
    ----------
    filepath : str, optional
        Path to CSV file. If None, generates synthetic data.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: date, station, temperature
    """
    if filepath:
        return pd.read_csv(filepath, parse_dates=["date"])

    # Generate sample data for demonstration
    np.random.seed(42)
    dates = pd.date_range("2000-01-01", "2023-12-31", freq="D")
    stations = ["Sydney", "Melbourne", "Brisbane"]

    records = []
    for station in stations:
        base_temp = {"Sydney": 22, "Melbourne": 20, "Brisbane": 25}[station]
        temps = (
            base_temp
            + 5 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)
            + np.random.normal(0, 2, len(dates))
        )
        # Add a slight warming trend
        temps += np.linspace(0, 1.5, len(dates))
        for d, t in zip(dates, temps):
            records.append({"date": d, "station": station, "temperature": round(t, 1)})

    return pd.DataFrame(records)


def describe_dataset(df):
    """Print a summary of the dataset."""
    print(f"Records:  {len(df):,}")
    print(f"Stations: {df['station'].nunique()}")
    print(f"Period:   {df['date'].min().date()} to {df['date'].max().date()}")
    print(f"Missing:  {df.isnull().sum().sum()}")


def remove_outliers(df, column, method="iqr"):
    """Remove outliers from a numeric column.

    Parameters
    ----------
    df : pd.DataFrame
    column : str
    method : str
        'iqr' (default) or 'zscore'

    Returns
    -------
    pd.DataFrame
        Filtered DataFrame with outliers removed.
    """
    if method == "iqr":
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        mask = (df[column] >= Q1 - 1.5 * IQR) & (df[column] <= Q3 + 1.5 * IQR)
    elif method == "zscore":
        mean = df[column].mean()
        std = df[column].std()
        mask = abs(df[column] - mean) <= 3 * std
    else:
        raise ValueError(f"Unknown method: {method}. Use 'iqr' or 'zscore'.")

    removed = len(df) - mask.sum()
    print(f"Removed {removed} outliers ({removed/len(df)*100:.1f}%) using {method}")
    return df[mask].copy()
