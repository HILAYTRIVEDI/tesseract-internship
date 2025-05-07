import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample DataFrame
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [30000, 50000, 70000, 90000, 110000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

### StandardScaler
standard_scaler = StandardScaler()

# Fit and transform the data
df_standard_scaled = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=['Age_Standard', 'Salary_Standard']
)

print("\nStandard Scaled DataFrame:")
print(df_standard_scaled)

### MinMaxScaler
minmax_scaler = MinMaxScaler(feature_range=(0, 1))  # Scale to range [0, 1]

# Fit and transform the data
df_minmax_scaled = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=['Age_MinMax', 'Salary_MinMax']
)

print("\nMin-Max Scaled DataFrame:")
print(df_minmax_scaled)

# Combine all DataFrames
df_final = pd.concat([df, df_standard_scaled, df_minmax_scaled], axis=1)

print("\nFinal Combined DataFrame:")
print(df_final)
