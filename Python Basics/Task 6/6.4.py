def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
result = factorial(5)
print(f"The factorial is: {result}")
