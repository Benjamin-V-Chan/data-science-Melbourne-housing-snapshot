# Load pandas, sklearn.model_selection, sklearn.pipeline, preprocessing, ensemble, joblib, os
# Define train(input_parquet, model_output_path)
#   read Parquet
#   separate X (drop non‐numeric/meta), y = Price
#   train_test_split (80/20, random_state=42)
#   build Pipeline([("scaler",StandardScaler()),("rf",RandomForestRegressor(...))])
#   fit on train
#   ensure model directory exists
#   joblib.dump({"model":pipeline,"X_test":X_test,"y_test":y_test}, model_output_path)
# if __name__ == "__main__": call train with paths
