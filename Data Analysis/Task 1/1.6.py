import pandas as pd

df = pd.read_csv("data.csv")

df.fillna(0, inplace=True) # fill all NaN values with 0

df.dropna(subset=["important_column"], inplace=True) # drop all rows with NaN in important_column

df["column_name"].fillna(df["column_name"].mean(), inplace=True) # fill NaN values in column_name with the mean of the column

print(df.isnull().sum())
