import pandas as pd

# Create the datasets
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

orders = pd.DataFrame({
    'OrderID': [101, 102, 103],
    'CustomerID': [1, 2, 1],
    'Product': ['Laptop', 'Phone', 'Tablet']
})

payments = pd.DataFrame({
    'PaymentID': [201, 202, 203],
    'CustomerID': [1, 2, 3],
    'Amount': [1000, 500, 750]
})

# Display the datasets
print("Customers Dataset:")
print(customers)

print("\nOrders Dataset:")
print(orders)

print("\nPayments Dataset:")
print(payments)

# Step 1: Merge Customers and Orders on CustomerID
merged_data = pd.merge(customers, orders, on='CustomerID', how='inner')

print("\nMerged Customers and Orders:")
print(merged_data)

# Step 2: Merge the result with Payments on CustomerID
final_data = pd.merge(merged_data, payments, on='CustomerID', how='left')

print("\nFinal Merged Dataset:")
print(final_data)