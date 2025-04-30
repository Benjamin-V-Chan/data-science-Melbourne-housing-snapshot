# Load joblib, sklearn.metrics, matplotlib.pyplot, os
# Define evaluate(model_path, metrics_path, plot_path)
#   load dict = joblib.load(model_path)
#   extract model, X_test, y_test
#   predict on X_test
#   compute MAE, RMSE, R2
#   ensure metrics directory exists; write metrics.txt
#   ensure plot directory exists; scatter y_test vs preds with 45° line → save plot
# if __name__ == "__main__": call evaluate with paths
