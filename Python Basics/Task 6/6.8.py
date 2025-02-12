def is_palindrome(s):
    return s == s[::-1] # Check if the string is equal to its reverse

# Example usage
result = is_palindrome("racecar")
print(f"Is the string a palindrome? {result}")
