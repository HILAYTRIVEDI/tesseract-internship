import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Generate Sample Time-Series Data
np.random.seed(42)
date_rng = pd.date_range(start='2023-01-01', periods=100, freq='D')  # 100 days
sales = np.random.randint(100, 500, size=(100,))  # Random sales data

df = pd.DataFrame({'Date': date_rng, 'Sales': sales})
df.set_index('Date', inplace=True)

# 🔹 Plot Daily Sales Trend (Matplotlib)
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['Sales'], color='blue', linestyle='-', marker='o', markersize=4, alpha=0.7, label="Daily Sales")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.show()

# 🔹 Seaborn Line Plot for Sales Trend
plt.figure(figsize=(12, 5))
sns.lineplot(x=df.index, y=df['Sales'], color='blue', label="Daily Sales")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.legend()
plt.show()

# 🔹 Add a 7-Day Rolling Average (Moving Average)
df['Rolling_Avg'] = df['Sales'].rolling(window=7).mean()

# 🔹 Plot Sales with Rolling Average
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['Sales'], color='lightgray', linestyle='-', alpha=0.5, label='Daily Sales')
plt.plot(df.index, df['Rolling_Avg'], color='red', linestyle='-', label='7-Day Rolling Average')
plt.title("Sales Trend with 7-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
