import pandas as pd

def extract():
    df = pd.read_csv("data/raw_logs.csv")
    print(f"[EXTRACT] Loaded {len(df)} rows from raw_logs.csv")
    return df
