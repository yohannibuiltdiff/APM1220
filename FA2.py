# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16hTKKfTPaxAgjobz7SLyC9VHbUxu0bDY
"""

import pandas as pd

file_path = '/content/sample_data/Political Interest.csv'
data = pd.read_csv(file_path)

data_info = data.info()
data_head = data.head()

data_info, data_head

import statsmodels.api as sm
from statsmodels.formula.api import ols

data['gender'] = data['gender'].map({1: 'Male', 2: 'Female'})
data['education_level'] = data['education_level'].astype('category')

model = ols('political_interest ~ gender * education_level', data=data).fit()

anova_table = sm.stats.anova_lm(model, typ=2)

anova_table