import pandas as pd

# Sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60],
    'Salary': [40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000],
    'Experience': [1, 3, 5, 7, 9, 11, 13, 15]
}

df = pd.DataFrame(data)

# Generate summary statistics
summary = df.describe()
print(summary)
