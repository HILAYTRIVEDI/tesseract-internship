def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Example usage
result = is_prime(11)
print(f"Is the number prime? {result}")
