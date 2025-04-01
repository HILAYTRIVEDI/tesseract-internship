import pandas as pd
import numpy as np

# Sample DataFrame with timestamps
data = {
    'timestamp': [
        '2024-03-28 14:45:30',
        '2024-06-15 08:20:10',
        '2024-12-01 21:10:05',
        '2025-01-10 04:55:00'
    ]
}


# Create DataFrame
df = pd.DataFrame(data)

# Convert 'timestamp' column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract time stamp features
df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day
df['quarter'] = df['timestamp'].dt.quarter
df['weekofyear'] = df['timestamp'].dt.isocalendar().week
df['dayofweek'] = df['timestamp'].dt.dayofweek
df['hour'] = df['timestamp'].dt.hour
df['minute'] = df['timestamp'].dt.minute
df['second'] = df['timestamp'].dt.second


# Is Weekend (Saturday/Sunday)
df['is_weekend'] = np.where(df['dayofweek'] >= 5, 1, 0)

# Define function for time of day categorization
def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

# Apply time of day categorization
df['time_of_day'] = df['hour'].apply(categorize_time_of_day)

# Compute Elapsed Time from a Reference Date
reference_date = pd.to_datetime("2024-01-01")
df['days_since_reference'] = (df['timestamp'] - reference_date).dt.days

# Print the final DataFrame
print("\nFinal DataFrame with Extracted Time Features:")
print(df)