# Function to convert two lists into a dictionary
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Example lists
keys = ["name", "age", "location"]
values = ["Alice", 25, "New York"]

# Convert lists to dictionary
result_dict = lists_to_dict(keys, values)

# Print the result
print(result_dict)
