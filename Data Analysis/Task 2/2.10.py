import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, MinMaxScaler, PolynomialFeatures

data = {
    'Age': [25, 30, 35, np.nan, 40, 50, np.nan],
    'Salary': [50000, 60000, 75000, 80000, np.nan, 110000, 120000],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco', np.nan, 'Los Angeles'],
    'Purchase': [1, 0, 1, 0, 1, 0, 1],
    'Date': pd.date_range(start='1/1/2023', periods=7, freq='D')
}

# Convert to DataFrame
df = pd.DataFrame(data)

df['Age'].fillna(df['Age'].median(), inplace=True) 
df['Salary'].fillna(df['Salary'].mean(), inplace=True) 
df['City'].fillna(df['City'].mode()[0], inplace=True) 

# Label Encoding
label_encoder = LabelEncoder()
df['City_Label'] = label_encoder.fit_transform(df['City'])

# One-Hot Encoding
df = pd.get_dummies(df, columns=['City'], drop_first=True)

df['Log_Salary'] = np.log1p(df['Salary'])

poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df[['Age', 'Salary']])
df_poly = pd.DataFrame(poly_features, columns=poly.get_feature_names_out(['Age', 'Salary']))
df = pd.concat([df, df_poly], axis=1)

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.weekday

scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

minmax_scaler = MinMaxScaler()
df[['Age', 'Salary']] = minmax_scaler.fit_transform(df[['Age', 'Salary']])

# Drop the original Date column
df.drop(columns=['Date'], inplace=True)

print(df.head())
