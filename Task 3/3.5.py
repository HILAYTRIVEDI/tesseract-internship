# Program to demonstrate all assignment operators in Python

# Initialize variables
x = 10
y = 5
z = 20

print("Initial values:")
print(f"x = {x}, y = {y}, z = {z}")

# Simple assignment operator
x = 15
print(f"\nAfter simple assignment: x = {x}")

# Add and assign (x += y)
x += y
print(f"After x += y: x = {x}")

# Subtract and assign (x -= y)
x -= y
print(f"After x -= y: x = {x}")

# Multiply and assign (x *= y)
x *= y
print(f"After x *= y: x = {x}")

# Divide and assign (x /= y)
x /= y
print(f"After x /= y: x = {x}")

# Floor divide and assign (x //= y)
x //= y
print(f"After x //= y: x = {x}")

# Modulus and assign (x %= y)
x %= y
print(f"After x %= y: x = {x}")

# Exponentiation and assign (x **= y)
x **= y
print(f"After x **= y: x = {x}")

# Bitwise AND and assign (x &= y)
x &= y
print(f"After x &= y: x = {x}")

# Bitwise OR and assign (x |= y)
x |= y
print(f"After x |= y: x = {x}")

# Bitwise XOR and assign (x ^= y)
x ^= y
print(f"After x ^= y: x = {x}")

# Bitwise left shift and assign (x <<= y)
x <<= y
print(f"After x <<= y: x = {x}")

# Bitwise right shift and assign (x >>= y)
x >>= y
print(f"After x >>= y: x = {x}")
