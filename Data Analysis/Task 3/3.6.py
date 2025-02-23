import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 22, 28, 38, 42, 47, 53, 58, 63],
    'Salary': [40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000,
               35000, 48000, 65000, 72000, 85000, 95000, 105000, 115000]
}

df = pd.DataFrame(data)

# Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Age'], y=df['Salary'], color='blue', alpha=0.7)
plt.title("Scatter Plot: Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
