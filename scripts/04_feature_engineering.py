import pandas as pd
import os

def engineer(input_parquet, output_parquet):
    df = pd.read_parquet(input_parquet)
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["PricePerRoom"] = df["Price"] / df["Rooms"]
    df["PricePerSqm"] = df["Price"] / df["BuildingArea"]
    cat_cols = ["Type", "Method", "Regionname", "CouncilArea"]
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    os.makedirs(os.path.dirname(output_parquet), exist_ok=True)
    df.to_parquet(output_parquet, index=False)

if __name__ == "__main__":
    engineer(
        "data/processed/melb_clean.parquet",
        "data/processed/melb_features.parquet"
    )
