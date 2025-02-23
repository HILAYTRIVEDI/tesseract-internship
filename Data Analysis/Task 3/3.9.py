import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


np.random.seed(42)
df = pd.DataFrame(np.random.rand(100, 10) * 100, columns=[f'Feature_{i}' for i in range(1, 11)])


scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)


pca = PCA()
df_pca = pca.fit_transform(df_scaled)


explained_variance = pca.explained_variance_ratio_


plt.figure(figsize=(10, 5))
plt.plot(range(1, len(explained_variance) + 1), np.cumsum(explained_variance), marker='o', linestyle='--', color='b')
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("Explained Variance by Principal Components")
plt.grid(True)
plt.show()


pca_optimal = PCA(n_components=2)
df_pca_optimal = pca_optimal.fit_transform(df_scaled)


df_pca_final = pd.DataFrame(df_pca_optimal, columns=['PC1', 'PC2'])


plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_pca_final['PC1'], y=df_pca_final['PC2'], color='red', alpha=0.7)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA: Data in 2D Space")
plt.grid(True)
plt.show()
