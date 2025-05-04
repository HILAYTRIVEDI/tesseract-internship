import pandas as pd

# Sample continuous data
data = {'age': [18, 22, 25, 30, 34, 40, 44, 52, 60, 65]}
df = pd.DataFrame(data)

# 🟢 1. Equal-width binning (cut)
df['age_bin_cut'] = pd.cut(df['age'], bins=4, labels=['Young', 'Mid-Young', 'Mid-Old', 'Old'])

# 🔵 2. Quantile-based binning (qcut)
df['age_bin_qcut'] = pd.qcut(df['age'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

# 🔍 Display results
print(df)
