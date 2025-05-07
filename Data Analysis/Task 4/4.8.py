import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample dataset: customer behavioral features
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'avg_purchase_value': [500, 50, 800, 70, 600, 40],
    'purchase_frequency': [12, 2, 15, 3, 13, 1],
    'days_since_last_purchase': [5, 40, 2, 30, 4, 45]
}

df = pd.DataFrame(data)

# Step 1: Prepare features (exclude IDs)
features = df[['avg_purchase_value', 'purchase_frequency', 'days_since_last_purchase']]

# Step 2: Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Step 3: Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled_features)

# Optional: Map cluster numbers to readable categories
cluster_map = {
    0: 'Casual Buyer',
    1: 'High-Value Frequent',
    2: 'Infrequent Low-Spender'
}
df['customer_segment'] = df['cluster'].map(cluster_map)

# Step 4: Final DataFrame with new categorical feature
print(df)
