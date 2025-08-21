import pathlib, typing as t
import pandas as pd

def detect_format(path: t.Union[str, pathlib.Path]):
    s = str(path).lower()
    if s.endswith('.csv'): return 'csv'
    if s.endswith(('.parquet', '.pq', '.parq')): return 'parquet'
    raise ValueError(f'Unsupported format: {s}')

def write_df(df: pd.DataFrame, path: t.Union[str, pathlib.Path]):
    p = pathlib.Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    fmt = detect_format(p)
    if fmt == 'csv':
        df.to_csv(p, index=False)
    else:
        try:
            df.to_parquet(p)
        except Exception as e:
            raise RuntimeError('Parquet engine not available. Install pyarrow or fastparquet.') from e
    return p

def read_df(path: t.Union[str, pathlib.Path]):
    p = pathlib.Path(path)
    fmt = detect_format(p)
    if fmt == 'csv':
        cols = pd.read_csv(p, nrows=0).columns
        return pd.read_csv(p, parse_dates=['date']) if 'date' in cols else pd.read_csv(p)
    else:
        try:
            return pd.read_parquet(p)
        except Exception as e:
            raise RuntimeError('Parquet engine not available. Install pyarrow or fastparquet.') from e
