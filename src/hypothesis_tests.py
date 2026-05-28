"""
Reusable hypothesis testing functions for insurance risk analytics
"""

import pandas as pd
import numpy as np
from scipy.stats import f_oneway, ttest_ind, chi2_contingency

def anova_test(data, group_col, value_col):
    """Perform ANOVA test for differences across multiple groups"""
    groups = [group[value_col].dropna().values for name, group in data.groupby(group_col)]
    if len(groups) >= 2:
        f_stat, p_value = f_oneway(*groups)
        return f_stat, p_value
    return None, None

def ttest_gender(data, value_col, male_label='Male', female_label='Female'):
    """Perform t-test between male and female groups"""
    male = data[data['Gender'] == male_label][value_col].dropna()
    female = data[data['Gender'] == female_label][value_col].dropna()
    t_stat, p_value = ttest_ind(male, female, equal_var=False)
    return t_stat, p_value

def chi_square_test(data, col1, col2):
    """Perform chi-square test for independence between two categorical variables"""
    contingency = pd.crosstab(data[col1], data[col2])
    chi2, p_value, dof, expected = chi2_contingency(contingency)
    return chi2, p_value, dof, expected