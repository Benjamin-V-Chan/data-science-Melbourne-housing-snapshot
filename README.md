# data-science-Melbourne-housing-snapshot

## Project Overview

This project analyzes and models the Melbourne housing market to uncover insights and predict property prices. The pipeline ingests raw data, cleans and preprocesses it, explores key patterns, engineers predictive features, trains a regression model, and evaluates its performance.

## Folder Structure

```
project-root/
├── data/
│   ├── raw/
│   │   └── melb_data.csv
│   └── processed/
│       ├── melb_raw.parquet
│       ├── melb_clean.parquet
│       └── melb_features.parquet
├── scripts/
│   ├── 01_data_ingestion.py
│   ├── 02_data_preprocessing.py
│   ├── 03_exploratory_analysis.py
│   ├── 04_feature_engineering.py
│   ├── 05_model_training.py
│   └── 06_model_evaluation.py
└── outputs/
    ├── figures/
    ├── models/
    └── metrics/
```  

## Usage

1. Setup the Project:

   Clone the repository.  
   Ensure you have Python installed.  
   Install required dependencies using the requirements.txt file.
   ```bash
   pip install -r requirements.txt
   ```

2. Ingest the raw data:
   ```bash
   python scripts/01_data_ingestion.py
   ```

3. Preprocess the data:
   ```bash
   python scripts/02_data_preprocessing.py
   ```

4. Run exploratory data analysis:
   ```bash
   python scripts/03_exploratory_analysis.py
   ```

5. Generate features:
   ```bash
   python scripts/04_feature_engineering.py
   ```

6. Train the model:
   ```bash
   python scripts/05_model_training.py
   ```

7. Evaluate the model:
   ```bash
   python scripts/06_model_evaluation.py
   ```

## Requirements

- Python 3.7+  
- pandas  
- numpy  
- scikit-learn  
- matplotlib  
- seaborn  
- pyarrow (for Parquet support)  
- joblib

## Acknowledgments

- **dataset name**: Melbourne Housing Snapshot  
- **dataset author**: DanB  
- **dataset source**: https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot

