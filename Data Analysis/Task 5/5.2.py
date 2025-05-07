# Generate heatmaps using seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10),
    'D': np.random.rand(10),
    'E': np.random.rand(10),
    'F': np.random.rand(10),
    'G': np.random.rand(10),
    'H': np.random.rand(10)
}

df = pd.DataFrame(data)

# Create a correlation matrix
correlation_matrix = df.corr()

# Set the size of the plot
plt.figure(figsize=(10, 8))

# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Heatmap')

# Show the plot
plt.show()
