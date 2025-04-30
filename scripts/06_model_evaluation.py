import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

def evaluate(model_path, metrics_path, plot_path):
    data = joblib.load(model_path)
    model = data["model"]
    X_test = data["X_test"]
    y_test = data["y_test"]
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds, squared=False)
    r2 = r2_score(y_test, preds)

    os.makedirs(os.path.dirname(metrics_path), exist_ok=True)
    with open(metrics_path, "w") as f:
        f.write(f"MAE: {mae:.2f}\nRMSE: {rmse:.2f}\nR2: {r2:.4f}")

    os.makedirs(os.path.dirname(plot_path), exist_ok=True)
    plt.scatter(y_test, preds, alpha=0.5)
    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        "r--"
    )
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted Price")
    plt.savefig(plot_path)
    plt.clf()

if __name__ == "__main__":
    evaluate(
        "outputs/models/rf_model.joblib",
        "outputs/metrics/metrics.txt",
        "outputs/figures/actual_vs_predicted.png"
    )
