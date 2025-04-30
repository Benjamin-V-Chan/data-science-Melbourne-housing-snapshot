import pandas as pd
import os

def preprocess(input_parquet, output_parquet):
    df = pd.read_parquet(input_parquet)
    df = df.dropna(subset=["Price"])
    df = df[df["Price"] > 0]
    thresh = df["Price"].quantile(0.99)
    df = df[df["Price"] <= thresh]
    df["BuildingArea"] = df["BuildingArea"].fillna(df["BuildingArea"].median())
    os.makedirs(os.path.dirname(output_parquet), exist_ok=True)
    df.to_parquet(output_parquet, index=False)

if __name__ == "__main__":
    preprocess(
        "data/processed/melb_raw.parquet",
        "data/processed/melb_clean.parquet"
    )
