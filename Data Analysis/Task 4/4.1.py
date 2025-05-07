import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Sample DataFrame
data = {
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue'],
    'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Label Encoding
label_encoder = LabelEncoder()

# Apply label encoding on the 'Color' column
df['Color_Label'] = label_encoder.fit_transform(df['Color'])
print("\nLabel Encoded DataFrame:")
print(df)

# One-Hot Encoding
one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first')
one_hot_encoded = one_hot_encoder.fit_transform(df[['Size']])

# Convert one-hot encoded array to DataFrame
one_hot_df = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(['Size']))

# Merge with the original DataFrame
df = pd.concat([df, one_hot_df], axis=1)

print("\nOne-Hot Encoded DataFrame:")
print(df)
