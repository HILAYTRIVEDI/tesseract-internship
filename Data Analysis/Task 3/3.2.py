import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 22, 28, 38, 42, 47, 53, 58, 63],
    'Salary': [40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000,
               35000, 48000, 65000, 72000, 85000, 95000, 105000, 115000],
    'Experience': [1, 3, 5, 7, 9, 11, 13, 15, 0, 2, 4, 6, 8, 10, 12, 14]
}

df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df['Age'], bins=10, kde=True, color='blue')
plt.title("Age Distribution")

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Salary'], color='red')
plt.title("Salary Boxplot")

# Show the plots
plt.tight_layout()
plt.show()
