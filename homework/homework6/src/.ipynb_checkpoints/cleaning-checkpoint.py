import pandas as pd
import numpy as np

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include="number").columns
    for col in columns:
        median_val = df_copy[col].median()
        df_copy[col] = df_copy[col].fillna(median_val)
    return df_copy

def drop_missing(df: pd.DataFrame, thresh: float = 0.5) -> pd.DataFrame:
    df_copy = df.copy()
    keep_cols = df_copy.columns[df_copy.isnull().mean() < (1 - thresh)]
    return df_copy[keep_cols].dropna()

def normalize_data(df: pd.DataFrame, columns=None) -> pd.DataFrame:
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include="number").columns
    scaler = MinMaxScaler()
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy


