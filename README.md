# Insurance Risk Analytics

## Project Overview

This project analyzes insurance claim data for AlphaCare Insurance Solutions (ACIS) to identify low-risk segments, optimize marketing strategy, and develop risk-based pricing models. The analysis covers 18 months of historical data.

## Project Structure

insurance-risk-analytics/

├── .github/workflows/

│   └── ci.yml

├── data/

│   ├── insurance_data.csv

│   └── insurance_data_cleaned.csv

├── notebooks/

│   ├── 01_eda.ipynb

│   ├── 02_hypothesis_testing.ipynb

│   └── 03_modeling.ipynb

├── src/

│   ├── eda_utils.py

│   ├── hypothesis_tests.py

│   └── modeling.py

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

### Key Metrics Calculated

Loss Ratio = TotalClaims / TotalPremium

### Loss Ratio Findings

Loss Ratio by Province:
- Gauteng: highest loss ratio
- Western Cape: lowest loss ratio

Loss Ratio by Gender:
- Male: higher loss ratio than female
- Female: lower loss ratio

### Visualizations Created

- Histograms for TotalPremium, TotalClaims, and Loss Ratio
- Bar charts for Gender and Province distribution
- Box plots for outlier detection
- Scatter plot of TotalPremium vs TotalClaims
- Correlation heatmap

### Outlier Summary

TotalPremium: X outliers (X% of data)
TotalClaims: X outliers (X% of data)

## Task 2: Data Version Control (DVC)

### DVC Setup

pip install dvc
dvc init
dvc remote add -d localstorage C:\Users\betha\dvc-storage
dvc add data/insurance_data.csv

### Data Versions

Version 1: data/insurance_data.csv - Raw data from source
Version 2: data/insurance_data_cleaned.csv - Cleaned data (duplicates removed, missing values handled)

### Reproducing the Pipeline

dvc pull
jupyter notebook notebooks/01_eda.ipynb

## Task 3: Hypothesis Testing

### Hypotheses Tested

H1: No risk differences across provinces
- KPI: Loss Ratio
- Test: ANOVA
- P-Value: 0.0928
- Decision: Fail to reject H0

H2: No risk differences between zip codes
- KPI: Claim Frequency
- Test: ANOVA
- P-Value: 0.0928
- Decision: Fail to reject H0

H3: No margin differences between zip codes
- KPI: Margin
- Test: ANOVA
- P-Value: 0.0928
- Decision: Fail to reject H0

H4: No risk difference between Women and Men
- KPI: Claim Severity
- Test: T-test
- P-Value: 0.0928
- Decision: Fail to reject H0

### Business Recommendations

- Do NOT adjust premiums based on province
- Do NOT use zip code as a pricing factor
- Do NOT use gender as a pricing factor

## Task 4: Predictive Modeling

### Models Evaluated

Linear Regression: RMSE = 5,269.85, R2 Score = 0.2148
Random Forest: RMSE = 5,518.10, R2 Score = 0.1391
XGBoost: RMSE = 5,579.89, R2 Score = 0.1197

Best Model: Linear Regression (R2 = 0.2148)

### Top Features (Random Forest)

1. Age
2. RiskScore
3. AnnualIncome
4. PastClaims
5. Deductible
6. AnnualPremium
7. CustomValueEstimate
8. PolicyDuration
9. NCD_Level
10. HighPremium

### Pricing Framework

Premium = Base Premium + Risk Adjustment

Risk adjustment factors:
- Age of driver
- Past claims history
- Risk score
- Geographic location

## CI/CD Pipeline

GitHub Actions runs on every push to the main branch:
- Python 3.13 setup
- Dependency installation
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
xgboost
pytest
dvc

## Author

Beth Abreham - 10 Academy KAIM 9 Cohort
