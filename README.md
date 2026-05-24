# Insurance Risk Analytics

## Project Overview

This project analyzes insurance claim data for AlphaCare Insurance Solutions (ACIS) to identify low-risk segments and optimize marketing strategy. The analysis covers 18 months of historical data (Feb 2014 – Aug 2015).

## Project Structure

insurance-risk-analytics/
├── .github/workflows/
│   └── ci.yml
├── data/
│   ├── insurance_data.csv
│   └── insurance_data_cleaned.csv
├── notebooks/
│   └── 01_eda.ipynb
├── src/
│   └── eda_utils.py
├── scripts/
│   └── clean_data.py
├── tests/
├── .dvc/
├── .gitignore
├── requirements.txt
└── README.md

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/bethabreham/insurance-risk-analytics.git
   cd insurance-risk-analytics

2. Create and activate virtual environment:
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Pull data from DVC remote:
   dvc pull

## Task 1: Exploratory Data Analysis

### Data Loading and Quality Assessment

- Dataset shape: XX rows, XX columns
- No missing values found in key columns
- Data types correctly identified (numerical, categorical, date)

### Key Metrics Calculated

- Loss Ratio = TotalClaims / TotalPremium

### Loss Ratio Findings

- Overall portfolio loss ratio: XX.XX%
- Highest loss ratio province: [Province Name]
- Gender difference: [Gender] has higher loss ratio than [other gender]

### Visualizations Created

The EDA notebook includes the following plots:
- Histograms for TotalPremium, TotalClaims, and Loss Ratio
- Bar charts for Gender and Province distribution
- Box plots for outlier detection
- Scatter plot of TotalPremium vs TotalClaims
- Correlation heatmap
- Geographic trends by province

### Outlier Summary

- TotalPremium: X outliers (X% of data)
- TotalClaims: X outliers (X% of data)

## Task 2: Data Version Control (DVC)

### DVC Setup

1. Install DVC:
   pip install dvc

2. Initialize DVC:
   dvc init

3. Set up local remote storage:
   mkdir C:\Users\betha\dvc-storage
   dvc remote add -d localstorage C:\Users\betha\dvc-storage

### Data Versions

| Version | File | Description |
|---------|------|-------------|
| v1 | data/insurance_data.csv | Raw data from source |
| v2 | data/insurance_data_cleaned.csv | Cleaned data (duplicates removed, missing values handled) |

### How to Reproduce the Data Pipeline

1. Clone the repository:
   git clone https://github.com/bethabreham/insurance-risk-analytics.git
   cd insurance-risk-analytics

2. Create virtual environment and install dependencies:
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt

3. Pull data from DVC remote:
   dvc pull

4. Run the EDA notebook:
   jupyter notebook notebooks/01_eda.ipynb

### Adding New Data Versions

To add a new version of the data:

1. Add or update the data file:
   dvc add data/insurance_data.csv

2. Push to remote storage:
   dvc push

3. Commit the .dvc file to Git:
   git add data/insurance_data.csv.dvc
   git commit -m "chore: update data version"
   git push

## CI/CD Pipeline

GitHub Actions runs on every push to the main branch:
- Python 3.13 setup
- Dependency installation from requirements.txt
- Unit tests via pytest

## Dependencies

pandas
numpy
matplotlib
seaborn
jupyter
ipykernel
scipy
statsmodels
scikit-learn
pytest
dvc