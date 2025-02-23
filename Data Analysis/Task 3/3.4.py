import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Sample dataset with missing values
data = {
    'Age': [25, 30, None, 40, 45, None, 55, 60, 22, 28, 38, None, 47, 53, 58, 63],
    'Salary': [40000, 50000, 60000, None, 80000, 90000, 100000, 110000,
               35000, None, 65000, 72000, 85000, None, 105000, 115000],
    'Experience': [1, 3, 5, 7, None, 11, 13, 15, 0, 2, None, 6, 8, 10, 12, 14]
}

df = pd.DataFrame(data)

# Plot missing values bar chart
plt.figure(figsize=(8, 5))
msno.bar(df, color='dodgerblue')
plt.title("Missing Values Bar Chart")
plt.tight_layout()
plt.show()