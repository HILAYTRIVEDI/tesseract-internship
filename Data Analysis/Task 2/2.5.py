import numpy as np
from scipy.stats import zscore

# Example dataset
data = np.array([10, 12, 12, 13, 12, 14, 13, 15, 1000])

# Calculate Z-scores
z_scores = zscore(data)

# Define threshold (commonly 3)
threshold = 3

# Filter out outliers
filtered_data = data[np.abs(z_scores) < threshold]

print("Original Data:", data)
print("Filtered Data:", filtered_data)