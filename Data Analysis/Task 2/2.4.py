# Normalize and standardize numerical data (MinMaxScaler, StandardScaler).

import pandas as pd

data = pd.read_csv('sample_data.csv')

# Normalize data
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
data[['Age', 'Salary']] = scaler.fit_transform(data[['Age', 'Salary']])
print(data)

# Standardize data
from sklearn.preprocessing import StandardScaler

scalerStandard = StandardScaler()
data[['Age', 'Salary']] = scalerStandard.fit_transform(data[['Age', 'Salary']])
