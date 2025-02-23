import pandas as pd
from sklearn.impute import SimpleImputer

# Load sample data
df = pd.read_csv("sample_data.csv")

df_dropna = df.dropna()

df_fillna = df.fillna({"Age": df["Age"].median(), "Salary": df["Salary"].mean(), "Department": "Unknown"})

imputer = SimpleImputer(strategy="mean")
df["Age"] = imputer.fit_transform(df[["Age"]])
df["Salary"] = imputer.fit_transform(df[["Salary"]])

# Display results
print("Original Data:\n", df)
print("\nData After Dropping Rows (dropna):\n", df_dropna)
print("\nData After Filling Specific Values (fillna):\n", df_fillna)
