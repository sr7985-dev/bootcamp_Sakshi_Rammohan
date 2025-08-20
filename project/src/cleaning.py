import pandas as pd
import numpy as np

def fill_missing_median(df, columns):
    for col in columns:
        df[col].fillna(df[col].median(), inplace=True)
    return df

def drop_missing(df, columns=None):
    if columns:
        return df.dropna(subset=columns)
    return df.dropna()

def normalize_data(df, columns):
    for col in columns:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)
    return df
