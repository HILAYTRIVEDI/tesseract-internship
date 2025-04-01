import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Sample dataset with two features
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [10, 20, 30, 40, 50]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Create Polynomial Features with degree 2
poly = PolynomialFeatures(degree=2, include_bias=False)

# Transform the data
df_poly = pd.DataFrame(poly.fit_transform(df), columns=poly.get_feature_names_out())

print("\nPolynomial Features (Degree=2):")
print(df_poly)
