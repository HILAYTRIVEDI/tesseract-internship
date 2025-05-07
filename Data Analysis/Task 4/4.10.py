import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Sample DataFrame
df = pd.DataFrame({
    'price': [100, 200, 150, 300],
    'discount_rate': [0.1, 0.2, 0.05, 0.15],
    'quantity': [2, 1, 3, 2]
})


poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
interaction_data = poly.fit_transform(df[['price', 'discount_rate', 'quantity']])

# Get new column names
feature_names = poly.get_feature_names_out(['price', 'discount_rate', 'quantity'])

# Create new DataFrame with interactions
interaction_df = pd.DataFrame(interaction_data, columns=feature_names)
print(interaction_df)
