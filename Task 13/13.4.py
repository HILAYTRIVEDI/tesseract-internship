# Create a package containing multiple modules and demonstrate its usage
from custom_package import add, subtract, to_upper, to_lower

# Using math_operations module
result_add = add(10, 5)
result_subtract = subtract(10, 5)

# Using string_operations module
uppercase_text = to_upper("hello")
lowercase_text = to_lower("WORLD")

# Displaying results
print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_subtract}")
print(f"Uppercase: {uppercase_text}")
print(f"Lowercase: {lowercase_text}")
