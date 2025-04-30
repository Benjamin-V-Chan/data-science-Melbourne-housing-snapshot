import pandas as pd
import os

def ingest(input_csv_path, output_parquet_path):
    df = pd.read_csv(input_csv_path, parse_dates=["Date"])
    os.makedirs(os.path.dirname(output_parquet_path), exist_ok=True)
    df.to_parquet(output_parquet_path, index=False)

if __name__ == "__main__":
    ingest(
        "data/raw/melb_data.csv",
        "data/processed/melb_raw.parquet"
    )
