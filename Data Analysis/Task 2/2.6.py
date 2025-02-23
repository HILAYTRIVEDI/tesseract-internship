import pandas as pd

# Example dataset with inconsistent categorical values
data = pd.DataFrame({
    'Category': ['cat', 'Cat', 'CAT', 'dog', 'Dog', 'DOG', 'cow', 'COW', 'cAt', 'dOg']
})

print("Original Data:")
print(data)

# Step 1: Replace inconsistent values using a mapping dictionary
mapping = {
    'Cat': 'cat',
    'CAT': 'cat',
    'cAt': 'cat',
    'Dog': 'dog',
    'DOG': 'dog',
    'dOg': 'dog',
    'Cow': 'cow',
    'COW': 'cow'
}

data['Category'] = data['Category'].replace(mapping)

print("\nAfter Replacing Inconsistent Values:")
print(data)

# Step 2: Standardize values using `apply` (convert all to lowercase)
data['Category'] = data['Category'].apply(lambda x: x.lower())

print("\nAfter Standardizing Values (Lowercase):")
print(data)

# Step 3: Encode categorical values using `factorize`
data['Category_Code'], unique_categories = pd.factorize(data['Category'])

print("\nAfter Encoding Categorical Values:")
print(data)
print("\nUnique Categories and Their Codes:")
print(dict(zip(unique_categories, range(len(unique_categories)))))