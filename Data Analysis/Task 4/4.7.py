import pandas as pd
import numpy as np

# Simulated E-commerce order data
data = {
    'user_id': [101, 102, 101, 103, 102, 101],
    'order_value': [200, 150, 100, 300, 80, 250],
    'order_date': [
        '2024-01-01', '2024-01-01', '2024-01-10',
        '2024-01-03', '2024-01-15', '2024-01-20'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)
df['order_date'] = pd.to_datetime(df['order_date'])

# Sort by user and date
df.sort_values(by=['user_id', 'order_date'], inplace=True)

# 🎯 Feature Engineering Based on Domain Knowledge

# 1. Time-Based Features
df['day_of_week'] = df['order_date'].dt.dayofweek  # 0 = Monday
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

# 2. Value Flag
df['high_value_order'] = (df['order_value'] > 150).astype(int)

# 3. Log Transformation to normalize skewed order values
df['log_order_value'] = np.log1p(df['order_value'])

# 4. Previous order difference (lag-based feature)
df['prev_order_value'] = df.groupby('user_id')['order_value'].shift(1)
df['order_value_diff'] = df['order_value'] - df['prev_order_value']

# 5. Days since previous order
df['prev_order_date'] = df.groupby('user_id')['order_date'].shift(1)
df['days_since_last_order'] = (df['order_date'] - df['prev_order_date']).dt.days

# 6. Aggregated customer behavior
agg_features = df.groupby('user_id').agg({
    'order_value': ['count', 'sum', 'mean', 'max'],
    'high_value_order': 'sum'
})
agg_features.columns = ['_'.join(col) for col in agg_features.columns]
agg_features.reset_index(inplace=True)

# Final Output
print("📦 Order-Level Features:")
print(df)
print("\n👤 Customer-Level Aggregated Features:")
print(agg_features)
