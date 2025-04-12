import pandas as pd
import numpy as np

# Simulated time series data
np.random.seed(42)
data = {
    'Date': pd.date_range(start='2024-01-01', periods=30),
    'Sales': np.random.randint(100, 200, size=30)
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Calculate 7-day Rolling Mean and Rolling Std
df['Rolling_Mean_7'] = df['Sales'].rolling(window=7).mean()
df['Rolling_Std_7'] = df['Sales'].rolling(window=7).std()

# Calculate Exponential Moving Average (EMA)
df['EMA_7'] = df['Sales'].ewm(span=7, adjust=False).mean()

# Display final DataFrame
print(df.head(15))  # Show first 15 rows
