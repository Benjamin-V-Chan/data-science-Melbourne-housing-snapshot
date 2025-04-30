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

