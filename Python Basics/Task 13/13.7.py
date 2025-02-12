import string_utils

text = "Hello World"

# Using the utility functions
print("Original Text:", text)
print("Uppercase:", string_utils.to_uppercase(text))
print("Lowercase:", string_utils.to_lowercase(text))
print("Reversed:", string_utils.reverse_string(text))
print("Is Palindrome:", string_utils.is_palindrome(text))
print("Word Count:", string_utils.count_words(text))
print("Without Whitespace:", string_utils.remove_whitespace(text))
print("Capitalized Words:", string_utils.capitalize_words(text))
