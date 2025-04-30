import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def eda(input_parquet, figures_dir):
    df = pd.read_parquet(input_parquet)
    os.makedirs(figures_dir, exist_ok=True)

    plt.hist(df["Price"], bins=50)
    plt.title("Price Distribution")
    plt.savefig(f"{figures_dir}/price_distribution.png")
    plt.clf()

    sns.scatterplot(x="Distance", y="Price", data=df)
    plt.title("Price vs Distance from CBD")
    plt.savefig(f"{figures_dir}/price_vs_distance.png")
    plt.clf()

    corr = df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True, fmt=".2f")
    plt.title("Correlation Matrix")
    plt.savefig(f"{figures_dir}/correlation_matrix.png")
    plt.clf()

if __name__ == "__main__":
    eda(
        "data/processed/melb_clean.parquet",
        "outputs/figures"
    )
