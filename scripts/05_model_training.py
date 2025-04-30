import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train(input_parquet, model_output_path):
    df = pd.read_parquet(input_parquet)
    X = df.drop(
        ["Price", "Date", "Address", "SellerG", "Suburb"],
        axis=1,
        errors="ignore"
    )
    y = df["Price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("rf", RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    pipeline.fit(X_train, y_train)
    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
    joblib.dump(
        {"model": pipeline, "X_test": X_test, "y_test": y_test},
        model_output_path
    )

if __name__ == "__main__":
    train(
        "data/processed/melb_features.parquet",
        "outputs/models/rf_model.joblib"
    )
