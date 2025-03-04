import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 22, 28, 38, 42, 47, 53, 58, 63],
    'Salary': [40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000,
               35000, 48000, 65000, 72000, 85000, 95000, 105000, 115000],
    'Experience': [1, 3, 5, 7, 9, 11, 13, 15, 0, 2, 4, 6, 8, 10, 12, 14]
}

df = pd.DataFrame(data)

# Compute correlation matrix
correlation_matrix = df.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()
