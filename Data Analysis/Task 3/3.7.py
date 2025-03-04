import pandas as pd

# Sample dataset with duplicates
data = {
    'ID': [101, 102, 103, 104, 105, 101, 103, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice', 'Charlie', 'Frank'],
    'Age': [25, 30, 35, 40, 45, 25, 35, 50],
    'Salary': [50000, 60000, 70000, 80000, 90000, 50000, 70000, 100000]
}

df = pd.DataFrame(data)

# Find duplicate rows
duplicates = df[df.duplicated()]
print("Duplicate Rows:\n", duplicates)

# Remove duplicates
df_cleaned = df.drop_duplicates()
print("\nDataset after removing duplicates:\n", df_cleaned)
